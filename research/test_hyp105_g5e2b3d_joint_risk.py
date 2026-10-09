"""Independent full-four vs bounded weighted-six GF5 cross-checks."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3c_plucker_shift import plucker_shift_model
from hyp105_g5e0_boundary_flows import exact_nonzero_trade_flow
from hyp105_g5e2b1_energy import single_signed_trade_mitm
from hyp105_g5e2b3b2_coincident_cycles import _physical_dual_column_edges
from hyp105_g5e2b3d_joint_risk import (
    C4_FOUR_SUPPORTS,C4_SIGNS,exact_c4_GF5_flow_weight,
    physical_four_cycles,exact_coincident_c4,exact_unit_T4,
    selected_c6_witness_sample,exact_weighted_sample,
    all_h_expected_Q4_lower,
)


def direct_Q4_by_four_column_subsets(model):
    """Independent O(binomial(N,4)) exact GQ matching-4 join (small cap)."""
    incidence=model["incidences"]
    if len(incidence)>14:
        raise ValueError("only capped independent oracle")
    total=0
    for selected in combinations(range(len(incidence)),4):
        chosen=tuple(incidence[i] for i in selected)
        if len({p for p,_ in chosen})!=4 or len({l for _,l in chosen})!=4:
            continue
        left=[model["left_labels"][p] for p,_ in chosen]
        right=[model["right_labels"][l] for _,l in chosen]

        def adjacency(pairs):
            counts={}
            for j,pair in enumerate(pairs):
                for coord in pair:
                    counts.setdefault(coord,[]).append(j)
            if len(counts)!=4 or any(len(x)!=2 for x in counts.values()):
                return None
            edge_set=tuple(sorted(tuple(x) for x in counts.values()))
            graph=[set() for _ in range(4)]
            for u,v in edge_set:
                graph[u].add(v)
                graph[v].add(u)
            if any(len(x)!=2 for x in graph):
                return None
            return edge_set

        le=adjacency(left)
        if le and adjacency(right)==le:
            total+=1
    return total


def direct_unit_T4_brute(supports,m):
    """Independent flat GF5 4-column/3-partition comparison."""
    total=0
    subsets=set()
    for subset in combinations(range(len(supports)),4):
        for first in combinations(subset,2):
            second=tuple(i for i in subset if i not in first)
            if first>=second:
                continue
            equal=all(
                sum(c in supports[i] for i in first) ==
                sum(c in supports[j] for j in second)
                for c in range(m))
            if equal:
                total+=1
                subsets.add(subset)
    return total,len(subsets)


def small_model(model,ids):
    s=dict(model)
    s["incidences"]=tuple(model["incidences"][i] for i in ids)
    s["N"]=len(ids)
    return s


class JointGF5RiskTests(unittest.TestCase):
    def test_C4_exact_GF5_independent_nonzero_flow_oracle(self):
        exact=exact_c4_GF5_flow_weight()
        self.assertGreater(exact,0)
        independent=exact_nonzero_trade_flow(
            C4_FOUR_SUPPORTS,C4_SIGNS,max_edges=16)
        self.assertEqual(exact,independent[
            "number_of_nonzero_GF5_weight_assignments"])
        self.assertEqual(independent["total_checksum4_nonzero_weight_assignments"],
                         51**4)

    def test_K6_C4_count_and_synthetic_positive_Q4(self):
        palette=tuple(combinations(range(6),2))
        self.assertEqual(len(tuple(physical_four_cycles(palette,6))),
                         3*len(tuple(combinations(range(6),4))))
        cyc=((0,1),(1,2),(2,3),(0,3))
        fixture={"a":6,"m":12,"N":4,"left_labels":cyc,
                 "right_labels":cyc,
                 "incidences":((0,0),(1,1),(2,2),(3,3))}
        report=exact_coincident_c4(fixture)
        self.assertEqual(report["Q4"],1)
        self.assertEqual(report["physical_left_C4"],1)
        self.assertEqual(direct_Q4_by_four_column_subsets(fixture),1)

    def test_full_GF2_exact_four_unit_event_oracle_and_subgraph_Q4(self):
        for scheme in ("plucker-lex-mincollision","old-reverse-line"):
            model=(plucker_shift_model(1,"plucker-lex-mincollision")
                   if scheme!="old-reverse-line"
                   else pair_labeled_symplectic(1,"reverse-line"))
            got=exact_unit_T4(model["supports"],model["m"])
            subset=model["supports"][:10]
            independent=direct_unit_T4_brute(subset,model["m"])
            unit_sub=exact_unit_T4(subset,model["m"])
            self.assertEqual(
                (unit_sub["unit_signed_four_events"],
                 unit_sub["unit_four_subsets"]),independent)
            self.assertGreaterEqual(got["unit_signed_four_events"],
                                    unit_sub["unit_signed_four_events"])
            selected,ds=selected_c6_witness_sample(model)
            self.assertEqual(len(selected),7)
            self.assertGreater(ds,0)
            sample=exact_weighted_sample(model,selected)
            self.assertGreater(sample["sample_exact_GF5_R3_numerator"],0)
            self.assertFalse(sample["whole_family_exact_GF5_R3"])
            small=small_model(model,list(selected)+[i for i in range(model["N"])
                                                     if i not in selected][:4])
            q=exact_coincident_c4(small)
            self.assertEqual(q["Q4"],direct_Q4_by_four_column_subsets(small))
            # Direct signed 2v2 GF5 for FIRST 4 selected columns, if
            # any topology flow exists; independent of 2-sum energy.
            four=tuple(model["supports"][i] for i in selected[:4])
            risk=Fraction(0)
            for plus in combinations(range(4),2):
                minus=tuple(j for j in range(4) if j not in plus)
                if plus>=minus:
                    continue
                chosen=tuple(four[i] for i in plus+minus)
                risk+=single_signed_trade_mitm(
                    chosen,(1,1,-1,-1),model["m"])["exact_probability"]
            from hyp105_g5e2b1_energy import risk_from_pair_energy
            self.assertEqual(risk,risk_from_pair_energy(four,model["m"])["R2"])

    def test_GF4_physical_full_Q4_T4_and_positive_GF5_witness(self):
        model=plucker_shift_model(2,"plucker-lex-mincollision")
        q=exact_coincident_c4(model)
        self.assertEqual(q["physical_left_C4"],len(tuple(
            physical_four_cycles(model["left_labels"],model["a"]))))
        unit=exact_unit_T4(model["supports"],model["m"])
        self.assertEqual(unit["pairs"],90100)
        for witness in q["witnesses"]:
            self.assertEqual(len(set(witness)),4)
        sample=exact_weighted_sample(model)
        self.assertGreaterEqual(
            sample["sample_exact_GF5_R3_numerator"],5643)
        self.assertFalse(sample["whole_family_exact_GF5_R2"])
        self.assertFalse(q["complete_full_51_palette_R2"])

    def test_all_h_symbolic_matching_Q4_random_expectation_and_guards(self):
        for s in (2,4,8,16):
            x=all_h_expected_Q4_lower(s)
            self.assertGreater(x["factor_matching_count_lower"],0)
            self.assertGreater(x["E_Q4_lower"],0)
            self.assertGreater(x["E_R2_lower"],0)
            self.assertFalse(x["individual_R2_lower"])
        with self.assertRaises(ValueError):
            all_h_expected_Q4_lower(3)
        with self.assertRaises(ValueError):
            exact_unit_T4(C4_FOUR_SUPPORTS,8,max_pairs=3)
        with self.assertRaises(ValueError):
            exact_weighted_sample(plucker_shift_model(1),selected=[0]*7)
        with self.assertRaises(RuntimeError):
            exact_coincident_c4(
                {"a":6,"m":12,"N":15,"left_labels":tuple(combinations(range(6),2)),
                 "right_labels":tuple(combinations(range(6),2)),
                 "incidences":tuple((i,i) for i in range(15))},
                 cycle_limit=1)


if __name__=="__main__":
    unittest.main()
