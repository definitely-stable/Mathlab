"""AA4-BH independent fixed two-typed original 7GF5 P,L coefficient falsifiers."""
import unittest
from collections import Counter,defaultdict
from itertools import combinations,permutations,product

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import (
    localized_original_seven_fiber,dyadic_all_h_seven_coefficient_scope
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,independent_joint_classify,
)
from hyp105_issue230_d6aa4bg_fixed_squarefree_D6_trace import (
    squarefree_trace_six_dp,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS,
)


def independent_original_point_C6_local_D6_fiber(model,P):
    """Direct real GQ incidence point cycle -> line six-edge dual oracle.

    No seven-sector point multigraph candidate enumeration, and
    no matrix trace or colored flag D graph. Exhaust 720 six-coord
    point cyclic orders with all real original point physical f-edges.
    """
    P=tuple(sorted(P))
    inc=tuple(tuple(q) for q in model["incidences"])
    f={tuple(sorted(e)):i for i,e in enumerate(model["left_labels"])}
    g=tuple(tuple(sorted(e)) for e in model["right_labels"])
    V=len(model["left_labels"])
    neigh=[[] for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        neigh[p].append((j,l))
    by_L=Counter()
    for vertices in permutations(P,6):
        if vertices[0]!=min(vertices) or vertices[1]>vertices[5]:
            continue
        edges=tuple(tuple(sorted((vertices[i],vertices[(i+1)%6])))
                    for i in range(6))
        if any(e not in f for e in edges):
            continue
        ps=[f[e] for e in edges]
        for picked in product(*(neigh[p] for p in ps)):
            flags=tuple(j for j,l in picked)
            ls=tuple(l for j,l in picked)
            if len(set(ls))!=6:
                continue
            ge=tuple(g[l] for l in ls)
            shared=[]
            for i in range(6):
                x=set(ge[i])&set(ge[(i+1)%6])
                if len(x)!=1:
                    break
                shared.append(next(iter(x)))
            if len(shared)==6 and len(set(shared))==6:
                by_L[tuple(sorted(shared))]+=1
    return dict(by_L)


class AA4BHOriginalSevenLocalized(unittest.TestCase):
    def test_01_all_five_true_original_W32_full_seven_census_and_trace(self):
        models=[("dual_zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        P=(0,1,2,3,4,5)
        for name,model in models:
            local=localized_original_seven_fiber(model,P)
            J=local["local_right_physical_fibers"]
            self.assertEqual(set(J),{P})
            cell=J[P]
            old=exact_two_sided_original_seven_join(
                model,independent_history=False,collect=False)
            historical=seven_census(model,independent_checks=False)
            trace=squarefree_trace_six_dp(model)
            self.assertEqual(local["point_side_true_original_sixflag_candidates_by_type"],
                             {"A":51030,"B":10935,"C":405})
            self.assertEqual(local["point_side_true_original_sixflag_candidates"],62370)
            self.assertEqual(cell["two_sided_join_coefficient"],
                             old["exact_source_original_Q_double_projection_intersection"])
            self.assertEqual(cell["AA_squarefree_source_factor_coefficient"],
                             old["physical_A_A_joint_candidates"])
            self.assertEqual(cell["original_D6_squarefree_sixtrace_coefficient"],
                             trace["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"])
            self.assertEqual(cell["original_D6_from_trace"],trace["accepted_original_six_ID_D6"])
            self.assertEqual(cell["seven_GF5_positive_coefficient"],historical["S_seven"])
            self.assertEqual(cell["all_seven_GF5_tags"],
                             {k:v for k,v in historical["seven_class_motif_counts"].items()
                              if v})
            self.assertEqual(cell["GF5_51palette_certified_weighted_numerator"],
                             historical["GF5_seven_lower_numerator"])
            self.assertEqual(cell["seven_GF5_positive_coefficient"],
                             cell["compensator_non_AA"]+cell["original_D6_from_trace"])
            self.assertTrue(local["branch_C_full_equivalence_NOT_CLAIMED"])

    def test_02_actual_W32_D6_zero_but_seven_GF5_compensation_strict_positive(self):
        for name in ("S68","S72"):
            model=fixture(1,name)
            p=(0,1,2,3,4,5)
            z=localized_original_seven_fiber(model,p)["local_right_physical_fibers"][p]
            self.assertEqual(z["original_D6_from_trace"],0)
            self.assertEqual(z["original_D6_squarefree_sixtrace_coefficient"],0)
            self.assertGreater(z["compensator_non_AA"],0)
            self.assertEqual(z["compensator_non_AA"],z["seven_GF5_positive_coefficient"])
            self.assertTrue(any(v>0 for v in z["all_seven_GF5_tags"].values()))

    def test_03_independent_W34_lex_and_random_true_original_seven_per_masks(self):
        P=(0,1,2,3,4,5)
        for name in ("lex","random"):
            model=fixture(2,name)
            local=localized_original_seven_fiber(model,P)
            self.assertEqual(local["s"],4)
            self.assertEqual(local["a"],14)
            self.assertEqual(local["V"],85)
            self.assertGreater(local["point_side_true_original_sixflag_candidates"],0)
            samples=0
            for L,z in local["local_right_physical_fibers"].items():
                self.assertEqual(len(L),6)
                self.assertEqual(z["seven_GF5_positive_coefficient"],
                                 z["two_sided_join_coefficient"]-
                                 z["AA_squarefree_source_factor_coefficient"]+
                                 z["original_D6_squarefree_sixtrace_coefficient"]//12)
                self.assertEqual(z["compensator_non_AA"],
                                 sum(v for key,v in z["all_seven_GF5_tags"].items()
                                     if key!="D6"))
                self.assertEqual(z["GF5_51palette_certified_weighted_numerator"],
                                 sum(R3_CERTIFIED_FLOORS[k]*v
                                     for k,v in z["all_seven_GF5_tags"].items()))
                for six,tag in z["sample_true_original_sixflag_sets"]:
                    # Independent join classifier needs A/B/C source
                    # partitions explicitly, not None.
                    from collections import Counter
                    profiles=(
                        tuple(sorted(Counter(model["incidences"][i][side]
                                             for i in six).values()))
                        for side in (0,1))
                    lookup={(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",(2,2,2):"C"}
                    lk,rk=(lookup[p] for p in profiles)
                    independently=independent_joint_classify(
                        six,lk,rk,tuple(model["incidences"]),
                        tuple(model["left_labels"]),tuple(model["right_labels"]))
                    self.assertEqual(independently,tag)
                    samples+=1
            self.assertGreater(samples,0)
            self.assertEqual(local["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_04_independent_original_W34_pointC6_vs_local_squarefree_trace(self):
        model=fixture(2,"lex")
        P=(0,1,2,3,4,5)
        direct=independent_original_point_C6_local_D6_fiber(model,P)
        local=localized_original_seven_fiber(model,P)["local_right_physical_fibers"]
        self.assertEqual(
            {L:z["original_D6_from_trace"] for L,z in local.items()
             if z["original_D6_from_trace"]},
            {L:n for L,n in direct.items() if n})
        self.assertEqual(sum(direct.values()),
                         sum(z["original_D6_from_trace"] for z in local.values()))

    def test_05_all_h_abstract_physical_pair_coefficient_identity_scope(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            z=dyadic_all_h_seven_coefficient_scope(1<<h)
            self.assertEqual(z["h"],h)
            self.assertEqual(z["seven_fiber_exact_identity"],
                             "S[P,L]=J[P,L]-AA[P,L]+D6[P,L]")
            self.assertTrue(z["full_original_W3_incidence_required"])
            self.assertTrue(z["not_root_Branch_A_or_B_or_accepted_C"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_06_genuine_original_global_injection_and_coordinate_domain_fail_closed(self):
        model=fixture(1,"lex")
        for invalid in ((0,1,2,3,4,4),(0,1,2,3,4,6),(0,1,2,3,4,True)):
            with self.assertRaises(ValueError):
                localized_original_seven_fiber(model,invalid)
        for broken in (dict(model,left_labels=((0,1),)*15),
                       dict(model,right_labels=((0,1),)*15),
                       dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                localized_original_seven_fiber(broken,(0,1,2,3,4,5))
        for bad in (0,3,7,-1,33,True):
            with self.assertRaises(ValueError):
                dyadic_all_h_seven_coefficient_scope(bad)

if __name__=="__main__":
    unittest.main()
