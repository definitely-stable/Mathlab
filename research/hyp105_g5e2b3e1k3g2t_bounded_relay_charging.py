"""HYP-105 E1-K3-G2-T: congestion-limited original GQ two-hop charging.

This is a strictly sufficient candidate for physical P2, NOT a theorem that
the candidate holds on every labeling. True original point p may use:
* its own B/A target-credit A_p;
* TRUE original-dual A/B target-credit B_l, only if p is incident to l;
* B/A target-credit A_q via p--l--q, for true original GQ incidences.
Every relay line l has ONE shared throughput gate kappa_l, and every
original or dual target-credit is spent AT MOST ONCE.

All capacities are exact nonnegative integers after multiplication by
the physical Johnson target density denominator. We cross-check a
Dinic flow/cut certificate with an independent Edmonds-Karp residual
implementation and a closed-form generalized Hall cut witness.

The model-specific finite W32 outcome cannot prove/disprove P2/P7 all-h.
"""
from collections import deque
from fractions import Fraction
from math import ceil
import json

from hyp105_g5e2b3e1k3g2s_incidence_hall_charging import (
    report as parent_report, exact_integer_maxflow,
    exhaustive_hall_deficit,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    gq_pair_model, rat,
)
from hyp105_g5e2b3e1k3g2q_gq_anchor_permanents import original_GQ_tables


def _validate(demand, own, dual, incidence, relay_capacity):
    n = len(demand)
    if (n == 0 or len(own)!=n or len(dual)!=n or len(incidence)!=n or
            len(relay_capacity)!=n):
        raise ValueError("nonempty balanced point/line ledgers required")
    if any(type(v) is not int or v<0
           for row in (demand,own,dual,relay_capacity) for v in row):
        raise ValueError("all demand, original/dual and relay budgets must be nonnegative integers")
    cleaned=[]
    for row in incidence:
        if not isinstance(row,(tuple,list,set,frozenset)):
            raise ValueError("explicit ORIGINAL GQ incidence IDs required")
        row=tuple(row)
        if len(row)!=len(set(row)) or any(
                type(x) is not int or not 0<=x<n for x in row):
            raise ValueError("duplicate or invalid original GQ incidence ID")
        cleaned.append(tuple(sorted(row)))
    return n,tuple(cleaned)


def _network(demand, own, dual, incidence, relay_capacity):
    n,incidence=_validate(demand,own,dual,incidence,relay_capacity)
    # s=0; point demands 1..n; BA credit n+1..2n;
    # dual AB credit 2n+1..3n; relay input 3n+1..4n;
    # relay output 4n+1..5n; t=5n+1.
    source=0
    target=5*n+1
    huge=sum(demand)+sum(own)+sum(dual)+sum(relay_capacity)+1
    arcs=[]
    def arc(u,v,c,kind="",identity=-1):
        arcs.append((u,v,c,kind,identity))
    for p in range(n):
        arc(source,1+p,demand[p],"demand",p)
        arc(1+p,1+n+p,huge,"same-BA",p)
        arc(1+n+p,target,own[p],"BA-credit",p)
        for l in incidence[p]:
            arc(1+p,1+2*n+l,huge,"incident-dual",l)
            arc(1+p,1+3*n+l,huge,"incident-relay",l)
    for l in range(n):
        arc(1+2*n+l,target,dual[l],"AB-credit",l)
        arc(1+3*n+l,1+4*n+l,relay_capacity[l],"relay-gate",l)
        for q in range(n):
            if l in incidence[q]:
                arc(1+4*n+l,1+n+q,huge,"relay-to-BA",q)
    return target+1,arcs,huge,incidence


def _dinic(size,arcs):
    """Capacity-preserving integer Dinic implementation and exact residual cut."""
    g=[[] for _ in range(size)]
    refs=[]
    for u,v,c,kind,identity in arcs:
        k=len(g[u])
        g[u].append([v,len(g[v]),c])
        g[v].append([u,k,0])
        refs.append((u,k,c,kind,identity))
    sink=size-1
    flow=0
    while True:
        level=[-1]*size
        level[0]=0
        q=deque([0])
        while q:
            u=q.popleft()
            for v,_,cap in g[u]:
                if cap>0 and level[v]<0:
                    level[v]=level[u]+1
                    q.append(v)
        if level[sink]<0:
            break
        pos=[0]*size
        def dfs(u,amount):
            if u==sink:
                return amount
            while pos[u]<len(g[u]):
                edge=g[u][pos[u]]
                v,back,cap=edge
                if cap and level[v]==level[u]+1:
                    got=dfs(v,min(amount,cap))
                    if got:
                        edge[2]-=got
                        g[v][back][2]+=got
                        return got
                pos[u]+=1
            return 0
        while True:
            augment=dfs(0,10**100)
            if not augment:
                break
            flow+=augment
    reachable={0}
    q=deque([0])
    while q:
        u=q.popleft()
        for v,_,cap in g[u]:
            if cap>0 and v not in reachable:
                reachable.add(v)
                q.append(v)
    usage=[(u,g[u][index][0],cap-g[u][index][2],cap,kind,identity)
           for u,index,cap,kind,identity in refs]
    return flow,reachable,usage


def _edmonds_karp(size,arcs):
    """Independent matrix-based integer max-flow; no Dinic code reused."""
    residual=[[0]*size for _ in range(size)]
    nbr=[set() for _ in range(size)]
    for u,v,c,_,_ in arcs:
        residual[u][v]+=c
        nbr[u].add(v)
        nbr[v].add(u)
    target=size-1
    total=0
    while True:
        parent=[-1]*size
        parent[0]=0
        q=deque([0])
        while q and parent[target]<0:
            u=q.popleft()
            for v in sorted(nbr[u]):
                if parent[v]<0 and residual[u][v]>0:
                    parent[v]=u
                    q.append(v)
                    if v==target:
                        break
        if parent[target]<0:
            break
        add=10**100
        v=target
        while v:
            u=parent[v]
            add=min(add,residual[u][v])
            v=u
        v=target
        while v:
            u=parent[v]
            residual[u][v]-=add
            residual[v][u]+=add
            v=u
        total+=add
    return total


def _certificate(demand,own,dual,incidence,relay_capacity):
    n=len(demand)
    size,arcs,huge,incidence=_network(
        demand,own,dual,incidence,relay_capacity)
    value,side,usage=_dinic(size,arcs)
    independent=_edmonds_karp(size,arcs)
    if value!=independent:
        raise AssertionError("independent exact Dinic/Edmonds-Karp disagreement")
    cut_capacity=sum(c for u,v,c,_,_ in arcs
                     if u in side and v not in side)
    if cut_capacity!=value:
        raise AssertionError("explicit residual min-cut capacity != exact max-flow")
    internal=[0]*size
    for u,v,used,cap,_,_ in usage:
        if not 0<=used<=cap:
            raise AssertionError("original credit or relay gate overdrawn")
        internal[u]-=used
        internal[v]+=used
    if (internal[0]!=-value or internal[-1]!=value or
            any(v!=0 for v in internal[1:-1])):
        raise AssertionError("integer flow conservation at EVERY network node failed")
    U={p for p in range(n) if 1+p in side}
    forced_lines=set(l for p in U for l in incidence[p])
    J={l for l in forced_lines if 1+4*n+l in side}
    actual_BA={p for p in range(n) if 1+n+p in side}
    actual_AB={l for l in range(n) if 1+2*n+l in side}
    actual_input={l for l in range(n) if 1+3*n+l in side}
    forced_BA=U | {q for q in range(n)
                     if any(l in incidence[q] for l in J)}
    if (not forced_BA<=actual_BA or not forced_lines<=actual_AB or
            not forced_lines<=actual_input):
        raise AssertionError("residual min cut violates mandatory infinite-capacity arcs")
    # Residual reverse arcs can make additional zero-cost credit nodes or
    # relay outputs reachable. The canonical source cut fixes precisely
    # U, N(U), and J subset N(U), pruning all optional extra nodes.
    # It is a valid ORIGINAL directed cut and cannot cost LESS than
    # max-flow. Its measured equality is an independent certificate.
    demand_U=sum(demand[p] for p in U)
    BA_forced=sum(own[p] for p in forced_BA)
    AB_forced=sum(dual[l] for l in forced_lines)
    relay_cut=sum(relay_capacity[l] for l in forced_lines-J)
    generalized_hall_deficit=demand_U-BA_forced-AB_forced-relay_cut
    if generalized_hall_deficit!=sum(demand)-value:
        raise AssertionError("generalized Hall all-h cut identity failed")
    relay_used=[0]*n
    for _,_,used,_,kind,identity in usage:
        if kind=="relay-gate":
            relay_used[identity]=used
    if any(relay_used[l]>relay_capacity[l] for l in range(n)):
        raise AssertionError("relay line bottleneck was bypassed")
    return {
        "flow":value,"total_demand":sum(demand),
        "deficit":sum(demand)-value,
        "feasible":value==sum(demand),
        "independent_flow":independent,
        "mincut_demand_points":sorted(U),
        "mincut_incident_original_lines":sorted(forced_lines),
        "mincut_activated_relay_lines":sorted(J),
        "mincut_BA_credit_points":sorted(forced_BA),
        "mincut_demand":demand_U,
        "mincut_BA_credit":BA_forced,
        "mincut_AB_credit":AB_forced,
        "mincut_relay_cut_capacity":relay_cut,
        "relay_line_used":relay_used,
        "edge_and_node_capacity_conservation":True,
        "generalized_Hall_min_cut_equality":True,
    }


def exact_bounded_relay_gate(demand,own,dual,incidence,
                             *, unit_denominator=143):
    """Uniform ORIGINAL GQ relay-line gate, calibrated EXACTLY in scaled units.

    Result includes 0 relay (S), <= one target-credit unit per line,
    and minimal *integer-scaled* uniform relay capacity for feasibility.
    This parameter is a candidate protocol budget, NOT proved geometric.
    """
    if type(unit_denominator) is not int or unit_denominator<1:
        raise ValueError("positive exact physical scaling denominator required")
    n,incidence=_validate(demand,own,dual,incidence,[0]*len(demand))
    cache={}
    def run(k):
        if k not in cache:
            cache[k]=_certificate(demand,own,dual,incidence,[k]*n)
        return cache[k]
    base=run(0)
    one=run(unit_denominator)
    whole_margin=sum(own)+sum(dual)-sum(demand)
    if base["deficit"]<0 or one["deficit"]>base["deficit"]:
        raise AssertionError("new relay cannot worsen exact transport optimum")
    if n==15:
        old_flow,_,old_deficit=exact_integer_maxflow(
            demand,own,dual,incidence)
        exhaustive,_=exhaustive_hall_deficit(
            demand,own,dual,incidence)
    else:
        # S's production finite checker deliberately accepts ONLY W32=15;
        # synthetic adversarial graphs are evaluated independently instead.
        old_flow=base["independent_flow"]
        old_deficit=sum(demand)-old_flow
        exhaustive=0
        if n<=15:
            for mask in range(1<<n):
                U=[p for p in range(n) if mask & (1<<p)]
                N=set(l for p in U for l in incidence[p])
                deficit=(sum(demand[p]-own[p] for p in U)-
                         sum(dual[l] for l in N))
                exhaustive=max(exhaustive,deficit)
    if (base["flow"],base["deficit"])!=(old_flow,old_deficit) or (
            n<=15 and exhaustive!=base["deficit"]):
        raise AssertionError("kappa=0 does not reproduce independent baseline Hall")
    lo=0
    upper=sum(demand)
    upper_cert=run(upper)
    minimum=None
    if upper_cert["feasible"]:
        hi=upper
        while lo<hi:
            mid=(lo+hi)//2
            if run(mid)["feasible"]:
                hi=mid
            else:
                lo=mid+1
        minimum=lo
        if not run(minimum)["feasible"]:
            raise AssertionError("minimal relay threshold is not sufficient")
        if minimum and run(minimum-1)["feasible"]:
            raise AssertionError("minimal relay threshold is not minimal")
    return {
        "zero_relay":base,
        "one_physical_credit_per_line":one,
        "minimal_uniform_relay_scaled":minimum,
        "minimal_uniform_relay_physical_units":(
            rat(Fraction(minimum,unit_denominator))
            if minimum is not None else None),
        "smallest_integer_physical_credit_cap":(
            ceil(Fraction(minimum,unit_denominator))
            if minimum is not None else None),
        "minimal_relay_certificate":(
            run(minimum) if minimum is not None else None),
        "minimal_minus_one_certificate":(
            run(minimum-1) if minimum else None),
        "all_32768_old_Hall_cuts_independently_matched_at_kappa_zero":n==15,
        "scalar_P2_margin":rat(Fraction(whole_margin,unit_denominator)),
        "all_h_P2_proved":False,
        "relay_budget_derived_from_GQ_theorem":False,
        "finite_all_label_W32_proved":False,
    }


def report():
    old=parent_report()
    old_cases=old["original_and_true_dual_complete_W32_cases"]
    actual_model=gq_pair_model(1,"lex")
    incidence,_,_=original_GQ_tables(
        2,tuple(actual_model["incidences"]))
    results=[]
    for x in old_cases:
        demand=x["actual_original_BA_anchor_demand"]
        own=x["actual_original_BA_own_target_capacity"]
        dual=x["actual_original_dual_AB_target_capacity"]
        z=exact_bounded_relay_gate(
            demand,own,dual,incidence,unit_denominator=x["scaled_denominator"])
        if (z["zero_relay"]["deficit"],z["scalar_P2_margin"])!=(
                x["hall_shortfall"],x["scalar_P2_margin"]):
            raise AssertionError("parent exact original/dual Hall result changed")
        results.append({
            "name":x["name"],
            "parent_S_Hall_shortfall":x["hall_shortfall"],
            "parent_S_original_point_cut":x["min_cut_original_point_ids"],
            "true_BA":x["original_BA_target_hits"],
            "true_dual_AB":x["true_original_dual_AB_target_hits"],
            "original_BA_source_mass":x["original_BA_source_mass"],
            "joint_C5":x["joint_signed_rank5"],
            "joint_C6":x["joint_signed_rank6"],
            **z,
        })
    return {
        "slice":"HYP-105-E1-K3-G2-T",
        "genuine_original_and_dual_complete_W32_cases":results,
        "true_original_GQ_typed_point_line_relay":True,
        "independent_exact_integer_Dinic_Edmonds_Karp":True,
        "all_h_theorem_only_conditional_sufficient_Hall":True,
        "universal_hypothesis_P2":"OPEN",
        "universal_hypothesis_P7":"OPEN",
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
