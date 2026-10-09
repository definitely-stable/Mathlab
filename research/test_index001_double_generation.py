"""INDEX-001 G2-B4-C1: independent finite schedule enumeration and phase gates."""
from itertools import product
from math import ceil
import unittest

from index001_double_generation import (
    Budget, alternating, compulsory_checkpoint_bound, hot_op,
    reachable_policies, report, restricted_witness,
)
from index001_page_recourse import packed_image, lookup_page_probe
from index001_priced_wal import (
    initial_wal, assign, pages, wal_step, wal_lookup, wal_disk_bytes
)
from index001_variable_checkpoint import encode_wal


def independent_budget(state,b,budget):
    # Independent arithmetical formula with fractions.Fraction; no call to .cap.
    from fractions import Fraction
    cost=Fraction(budget.alpha_num,budget.alpha_den)*len(packed_image(state))
    return (cost.numerator//cost.denominator + budget.beta*b +
            budget.gamma*ceil(budget.persistent_m_bits/8))


def enumerate_schedules(initial, operations, b, budget, q):
    """Policy oracle uses all 2^U action words, not DP/Bellman recursion."""
    feasible=[]
    history = [set() for _ in operations]
    for word in product(("append","checkpoint"), repeat=len(operations)):
        state=initial_wal(initial)
        sum_w=0
        valid=True
        for t,(action,op) in enumerate(zip(word,operations)):
            next_threshold=len(state.frames)+2 if action=="append" else 1
            state,ledger=wal_step(state,op,b,next_threshold)
            truth=list(initial)
            for old in operations[:t+1]:
                truth[old[0]:old[1]]=[old[2]]*(old[1]-old[0])
            if tuple(truth)!=state.latest:
                raise AssertionError("independent dense state differs")
            if (ledger["disk_bytes_after"]>independent_budget(state.latest,b,budget) or
                ledger["peak_bytes"]>independent_budget(state.latest,b,budget) or
                ledger["max_point_query_pages"]>q):
                valid=False
                break
            sum_w+=ledger["written_model_bytes"]
            history[t].add(state)
        if valid:
            feasible.append((sum_w,word))
    return {
        "feasible":bool(feasible),
        "minimum_written_model_bytes":min((w for w,_ in feasible),default=None),
        "optimal_schedule":list(min(feasible)[1]) if feasible else None,
        "prefix_state_counts":[len(h) for h in history],
    }


class DoubleGenerationTest(unittest.TestCase):
    def test_pinned_effective_hot_toggle_both_blockers(self):
        b=Budget(7,4,2)
        q=restricted_witness(129,32,b,12)
        s=restricted_witness(129,32,b,100)
        self.assertEqual(q["snapshot_before_bytes"],270)
        self.assertEqual(q["snapshot_after_bytes"],268)
        self.assertEqual(q["wal_frame_bytes_each"],9)
        self.assertEqual(q["checkpoint_peak_floor_bytes"],608)
        self.assertEqual(q["state_budget_caps_bytes"],[536,533])
        self.assertEqual(q["read_untouched_base_pages"],9)
        self.assertEqual(q["first_blocked_update"],8)
        self.assertEqual(q["last_feasible_append"],7)
        self.assertEqual(q["blocking_resources"],["read"])
        self.assertEqual(q["rows"][-2]["query_pages"],12)
        self.assertEqual(q["rows"][-1]["query_pages"],13)
        self.assertTrue(q["rows"][-1]["space_ok"])
        self.assertEqual(s["first_blocked_update"],22)
        self.assertEqual(s["blocking_resources"],["steady_space"])
        self.assertEqual(s["rows"][-2]["steady_bytes"],512)
        self.assertEqual(s["rows"][-1]["steady_bytes"],544)
        self.assertTrue(s["rows"][-1]["read_ok"])

    def test_analytic_model_against_exact_wal_and_independent_rational_budget(self):
        for n in (3,5,31,127,129,511):
            base=alternating(n)
            target=assign(base,(0,1,1))
            snapshots=[len(packed_image(x)) for x in (base,target)]
            width=len(__import__("index001_variable_checkpoint").uvarint(n))
            self.assertEqual(snapshots,[8+2*width+2*n,6+2*width+2*n])
            for block in (16,32,64):
                if pages(snapshots[0],block)!=pages(snapshots[1],block):
                    continue
                params=Budget(7,4,2,1,10)
                state=initial_wal(base)
                self.assertEqual(params.cap(base,block),
                                 independent_budget(base,block,params))
                for t in range(1,11):
                    state,row=wal_step(state,hot_op(t),block,len(state.frames)+2)
                    self.assertEqual(params.cap(state.latest,block),
                                     independent_budget(state.latest,block,params))
                    self.assertEqual(len(state.frames),t)
                    self.assertEqual(row["disk_bytes_after"],
                                     (pages(snapshots[0],block)+1+
                                      ceil(9*t/block))*block)
                    target=assign(base,(0,1,t%2))
                    self.assertEqual(state.latest,target)
                    self.assertEqual(wal_lookup(state,n-1,block)[0],base[-1])
                    control=1
                    prefix=len(lookup_page_probe(
                        "packed",base,n-1,min(n,8),block)["page_indices"])
                    self.assertEqual(wal_lookup(state,n-1,block)[1],
                                     control+ceil(9*t/block)+prefix)

    def test_short_horizon_bellman_matches_complete_policy_words(self):
        for n in range(1,4):
            alphabet=[(lo,hi,bit) for lo in range(n)
                      for hi in range(lo+1,n+1) for bit in (0,1)]
            for state in product((0,1),repeat=n):
                for first in alphabet:
                    for second in alphabet:
                        operations=[first,second]
                        for budget,q in ((Budget(1,1,2),3),(Budget(4,1,2),8)):
                            exact=enumerate_schedules(state,operations,32,budget,q)
                            dp=reachable_policies(state,operations,32,budget,q)
                            self.assertEqual(dp["feasible"],exact["feasible"])
                            self.assertEqual(dp["minimum_written_model_bytes"],
                                             exact["minimum_written_model_bytes"])
                            self.assertEqual(dp["optimal_schedule"],
                                             exact["optimal_schedule"])
                            self.assertEqual(dp["reachable_states_by_step"],
                                             exact["prefix_state_counts"])

    def test_universal_checkpoint_minimum_for_restricted_wal(self):
        n=129
        a=compulsory_checkpoint_bound(n,32,12,24)
        self.assertEqual(a["max_consecutive_appends"],7)
        self.assertEqual(a["min_checkpoints"],3)
        self.assertEqual(a["min_checkpoint_model_bytes"],960)
        self.assertFalse(compulsory_checkpoint_bound(n,32,9,24)["admissible"])
        self.assertEqual(compulsory_checkpoint_bound(n,32,12,0)["min_checkpoints"],0)
        # For no intervening WAL reads allowed, every effective update must
        # directly checkpoint or the appended log necessarily costs one page.
        tight=compulsory_checkpoint_bound(n,32,10,4)
        self.assertEqual(tight["max_consecutive_appends"],0)
        self.assertEqual(tight["min_checkpoints"],4)
        self.assertEqual(tight["min_checkpoint_model_bytes"],4*320)

    def test_boundaries_and_invalid_proof_preconditions(self):
        for args in ((0,),(2,),(-1,),(128,)):
            with self.assertRaises(ValueError):
                alternating(*args)
        for args in ((-1,4,2),(1,0,2),(1,1,-1),(1,1,2,-1),(1,1,2,0,-1)):
            with self.assertRaises(ValueError):
                Budget(*args)
        with self.assertRaises(ValueError):
            restricted_witness(129,32,Budget(3,1,2),12)
        with self.assertRaises(ValueError):
            restricted_witness(129,32,Budget(0,1,0),12)
        with self.assertRaises(ValueError):
            restricted_witness(129,32,Budget(7,4,2),0)
        with self.assertRaises(ValueError):
            restricted_witness(129,32,Budget(7,4,2),12,0)
        with self.assertRaises(ValueError):
            reachable_policies((0,1),[(0,1,1)],32,Budget(3,1,2),0)
        with self.assertRaises(ValueError):
            compulsory_checkpoint_bound(129,32,12,-1)
        with self.assertRaises(ValueError):
            hot_op(0)

    def test_report_reproducible(self):
        obj=report()
        self.assertEqual(obj,report())
        self.assertEqual(obj["query_limited"]["first_blocked_update"],8)
        self.assertEqual(obj["space_limited"]["first_blocked_update"],22)
        self.assertIsNone(obj.get("nand_bytes"))
        self.assertEqual(obj["hardware_nand_and_syscall_measurement"],"NONE")


if __name__=="__main__":
    unittest.main()
