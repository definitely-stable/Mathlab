"""INDEX-001 G2-B4-C1: bounded peak/query impossibility, *one-level immutable WAL only*.

The oracle includes a full page-aligned base, a control page, and an append-only
CRC WAL. It does not establish NAND, crash-atomicity or universal cell-probe bounds.
"""
from dataclasses import dataclass
from itertools import product
import argparse
import json

from index001_page_recourse import lookup_page_probe, packed_image
from index001_priced_wal import (
    WalState, assign, initial_wal, pages, wal_disk_bytes, wal_lookup, wal_step,
)
from index001_variable_checkpoint import encode_wal, decode_wal, uvarint


@dataclass(frozen=True)
class Budget:
    """Rational alpha*S(f) + beta*B + gamma*ceil(M_bits/8), *integer bytes*."""
    alpha_num: int
    alpha_den: int
    beta: int
    gamma: int = 0
    persistent_m_bits: int = 0

    def __post_init__(self):
        if (not all(type(z) is int for z in (
                self.alpha_num, self.alpha_den, self.beta, self.gamma,
                self.persistent_m_bits)) or self.alpha_num < 0 or
                self.alpha_den < 1 or self.beta < 0 or self.gamma < 0 or
                self.persistent_m_bits < 0):
            raise ValueError("nonnegative integers and positive alpha denominator required")

    def cap(self, state, block):
        if type(block) is not int or block < 4:
            raise ValueError("invalid page size")
        payload = len(packed_image(state))
        # Only the fractional alpha term rounds down; beta and gamma are integers.
        return ((self.alpha_num*payload)//self.alpha_den +
                self.beta*block + self.gamma*((self.persistent_m_bits+7)//8))


def alternating(n):
    if type(n) is not int or n < 3 or n % 2 == 0:
        raise ValueError("odd N>=3 required")
    if len(uvarint(n)) != len(uvarint(n-1)):
        raise ValueError("run-count varint width crossing excluded")
    return tuple(i & 1 for i in range(n))


def hot_op(t):
    if type(t) is not int or t < 1:
        raise ValueError("step must be positive")
    return (0, 1, t % 2)


def reachable_policies(initial, operations, block, budget, query_cap):
    """Exact finite Bellman oracle on C0 one-level WAL action states.

    Direct CHECKPOINT materializes the new base without also logging the
    current update, exactly as in C0. APPEND acknowledges every update.
    Report minimum modeled page-write bytes over budget-admissible paths.
    """
    if type(query_cap) is not int or query_cap < 1:
        raise ValueError("query limit must be >=1")
    start=initial_wal(initial)
    dp={start: (0, ())}
    history=[]
    for op in operations:
        nxt={}
        for state,(spent,actions) in dp.items():
            for name in ("append","checkpoint"):
                threshold=(len(state.frames)+2 if name=="append" else 1)
                successor,row=wal_step(state,op,block,threshold)
                if (row["peak_bytes"] > budget.cap(successor.latest,block) or
                    row["disk_bytes_after"] > budget.cap(successor.latest,block) or
                    row["max_point_query_pages"] > query_cap):
                    continue
                key=successor
                cost=spent+row["written_model_bytes"]
                sequence=actions+(name,)
                if key not in nxt or (cost,sequence)<nxt[key]:
                    nxt[key]=(cost,sequence)
        dp=nxt
        history.append(len(dp))
    answer=min(dp.values(),default=None)
    return {"feasible":answer is not None,"minimum_written_model_bytes":
            None if answer is None else answer[0],
            "optimal_schedule":None if answer is None else list(answer[1]),
            "reachable_states_by_step":history}


def restricted_witness(n=129, block=32, budget=Budget(7,4,2),
                       query_cap=12, maximum_updates=5000):
    """Certify a hard, *effective* alternating hot-bit workload.

    Feasible initial state, both alternating targets have equal page count,
    and at each checkpoint old base and newly allocated base overlap.
    The statement applies ONLY to immutable-base, append-all, no-history-
    summarization, one-control-page + one-log layout.
    """
    base=alternating(n)
    flipped=assign(base,hot_op(1))
    if type(query_cap) is not int or query_cap<1:
        raise ValueError("invalid Q")
    if type(maximum_updates) is not int or maximum_updates<1:
        raise ValueError("invalid maximum_updates")
    s0,s1=len(packed_image(base)),len(packed_image(flipped))
    p0,p1=pages(s0,block),pages(s1,block)
    if p0!=p1:
        raise ValueError("this simple witness requires equal page-count snapshots")
    if tuple(flipped)==tuple(base) or assign(flipped,hot_op(2))!=base:
        raise AssertionError("effective two-state trace required")
    frame0,frame1=encode_wal(n,*hot_op(1)),encode_wal(n,*hot_op(2))
    if len(frame0)!=len(frame1):
        raise ValueError("constant-width frames required")
    e=len(frame0)
    if decode_wal(n,frame0)!=hot_op(1) or decode_wal(n,frame1)!=hot_op(2):
        raise AssertionError("canonical WAL encoding diverged")
    q_base=len(lookup_page_probe("packed",base,n-1, min(n,8),block)["page_indices"])
    old_base_pages=p0
    baseline_peak=(p0+p1+1)*block   # old + new + persistent control, ZERO log
    caps=(budget.cap(base,block),budget.cap(flipped,block))
    if wal_disk_bytes(initial_wal(base),block)>caps[0]:
        raise ValueError("initial state already over budget")
    if baseline_peak<=max(caps):
        raise ValueError("cannot certify universal checkpoint obstruction")
    # Forward-scan WAL must always read the log and a late base position not
    # overwritten by hot-op(0,1,v), so it costs at least q_base+1+logpages.
    # This is an exact worst-case for THIS implementation: hot bit at 0.
    prefix_q=q_base+1
    state=initial_wal(base)
    steps=[]
    for t in range(1,maximum_updates+1):
        op=hot_op(t)
        # Explicit append path; never checkpoint. threshold above next count.
        candidate,row=wal_step(state,op,block,len(state.frames)+2)
        expected_state=flipped if t%2 else base
        if candidate.latest!=expected_state:
            raise AssertionError("dense state diverged")
        log_pages=pages(e*t,block)
        steady=(p0+1+log_pages)*block
        predicted_q=prefix_q+log_pages
        if (row["disk_bytes_after"]!=steady or
            row["max_point_query_pages"]!=predicted_q or
            len(candidate.frames)!=t):
            raise AssertionError("independent arithmetic and executable ledger disagree")
        if wal_lookup(candidate,n-1,block)[1]!=predicted_q:
            raise AssertionError("exact untouched-position query disproves bound")
        cap=budget.cap(candidate.latest,block)
        read_ok=predicted_q<=query_cap
        space_ok=steady<=cap
        steps.append({"t":t,"state":"flipped" if t%2 else "initial",
                      "log_pages":log_pages,"steady_bytes":steady,
                      "query_pages":predicted_q,"budget_cap_bytes":cap,
                      "read_ok":read_ok,"space_ok":space_ok})
        if not (read_ok and space_ok):
            # Could instead checkpoint at t? Not even the NO-LOG old/new
            # two-generation overlap is affordable for EITHER target.
            return {"schema":"mathlab.index001.g2b4c1.double-generation.v1",
                    "classification":"RESTRICTED_TWO_GENERATION_LIVENESS_IMPOSSIBILITY",
                    "universe":n,"block_bytes":block,
                    "alpha_num":budget.alpha_num,"alpha_den":budget.alpha_den,
                    "beta_pages":budget.beta,"persistent_m_bits":budget.persistent_m_bits,
                    "query_cap_pages":query_cap,
                    "snapshot_before_bytes":s0,"snapshot_after_bytes":s1,
                    "snapshot_pages_each":p0,
                    "wal_frame_bytes_each":e,
                    "read_untouched_base_pages":q_base,
                    "checkpoint_peak_floor_bytes":baseline_peak,
                    "state_budget_caps_bytes":list(caps),
                    "last_feasible_append":t-1,
                    "first_blocked_update":t,
                    "blocking_resources":[k for k,ok in
                         (("read",read_ok),("steady_space",space_ok)) if not ok],
                    "no_checkpoint_even_with_empty_log":True,
                    "rows":steps}
        state=candidate
    raise ValueError("finite horizon did not force an impossible step")


def report():
    b=Budget(7,4,2)
    read=restricted_witness(129,32,b,12)
    space=restricted_witness(129,32,b,100)
    if read["first_blocked_update"]!=8 or space["first_blocked_update"]!=22:
        raise AssertionError("pinned stop steps changed")
    return {
        "schema":"mathlab.index001.g2b4c1.gate.v1",
        "scientific_classification":"MODEL_SPECIFIC_TWO_GENERATION_CAPACITY_NOT_UNIVERSAL_THEOREM",
        "hardware_nand_and_syscall_measurement":"NONE",
        "unbounded_ram_workspace":"NOT_ACCOUNTED",
        "query_limited":{k:v for k,v in read.items() if k!="rows"},
        "space_limited":{k:v for k,v in space.items() if k!="rows"},
        "short_policy_frontier":reachable_policies(
            (0,1,0,1,0),[(0,1,1),(0,1,0),(0,1,1)],
            32,Budget(4,1,2),8),
    }


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--json",action="store_true")
    opt=args.parse_args()
    row=report()
    if opt.json:
        print(json.dumps(row,sort_keys=True,indent=2))
    else:
        for label in ("query_limited","space_limited"):
            obj=row[label]
            print(f"{label}: N={obj['universe']} B={obj['block_bytes']} "
                  f"checkpoint_min_peak={obj['checkpoint_peak_floor_bytes']} "
                  f"caps={obj['state_budget_caps_bytes']} "
                  f"last_append={obj['last_feasible_append']} "
                  f"first_impossible={obj['first_blocked_update']} "
                  f"blockers={','.join(obj['blocking_resources'])}")
        print("INDEX001_G2B4C1_DOUBLE_GENERATION_GATE_PASS")
