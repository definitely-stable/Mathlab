"""HYP-105 E1-B0: independent seven-family/typed incidence tensor falsifiers."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import finite_census
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, GF5_DENOM, classify_seven_prechecked,
    physical_column_dual, is_connected_column_cycle, seven_census,
    exact_seven_weighted_GF5, report,
)


def independent_brute_tag(model, ids):
    """No use of the optimized classifier or original E1A type function."""
    if len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("distinct selected original incidences")
    physical=[]
    factor=[]
    for half in (0,1):
        labels=model["left_labels"] if half==0 else model["right_labels"]
        endpoints=[model["incidences"][i][half] for i in sorted(ids)]
        coord_freq=Counter(coord for endpoint in endpoints
                           for coord in labels[endpoint])
        if len(coord_freq)!=6 or set(coord_freq.values())!={2}:
            return None
        freq=tuple(sorted(Counter(endpoints).values(),reverse=True))
        pattern={
            (1,1,1,1,1,1):"A",
            (2,1,1,1,1):"B",
            (2,2,2):"C",
        }.get(freq)
        if pattern is None:
            return None
        physical.append(pattern)
        factor.append(endpoints)
    L,R=physical
    if (L,R)==("B","A"):
        return "B-left/A-right"
    if (L,R)==("A","B"):
        return "A-left/B-right"
    if L==R=="A":
        dual=[]
        for h in (0,1):
            p=tuple((model["left_labels"] if h==0 else
                     model["right_labels"])[factor[h][j]] for j in range(6))
            all_coords=set(coord for e in p for coord in e)
            adj=tuple(sorted(tuple(i for i,e in enumerate(p) if coord in e)
                             for coord in all_coords))
            dual.append(adj)
        if dual[0]!=dual[1]:
            return None
        edges=dual[0]
        neighbors=[set() for _ in range(6)]
        for u,v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
        if all(len(n)==2 for n in neighbors):
            todo={0}
            seen=set()
            while todo:
                u=todo.pop()
                if u in seen:
                    continue
                seen.add(u)
                todo.update(neighbors[u]-seen)
            if len(seen)==6:
                return "D6"
        return None
    if {L,R}=={"A","C"}:
        return "C/A"
    if {L,R}=={"B","C"}:
        return "C/B"
    if L==R=="B":
        rows=[]
        for f in factor:
            repeated=next(v for v,n in Counter(f).items() if n==2)
            rows.append({j for j,x in enumerate(f) if x==repeated})
        return "B/B-overlap" if rows[0]&rows[1] else "B/B-disjoint"
    return None


class SevenMotifJointFixedTests(unittest.TestCase):
    def test_exact_full_W32_new_class_regression_and_joint_r2_r3(self):
        for scheme,expected_new,total in (
            ("lex",{"C/A":13,"C/B":1,"B/B-overlap":8,
                    "B/B-disjoint":14},36),
            ("reverse-line",{"C/A":1,"C/B":1,"B/B-overlap":7,
                             "B/B-disjoint":6},15),
        ):
            model=pair_labeled_symplectic(1,scheme)
            z=seven_census(model)
            self.assertEqual(z["left_6coordinate_candidates"],62370)
            self.assertEqual(z["new_classes"],expected_new)
            pinned = {
                "lex":({
                    "D6":15, "B-left/A-right":98, "A-left/B-right":110,
                    "C/A":13, "C/B":1, "B/B-overlap":8,
                    "B/B-disjoint":14,
                }, 259, 50, 11225795),
                "reverse-line":({
                    "D6":3, "B-left/A-right":77, "A-left/B-right":74,
                    "C/A":1, "C/B":1, "B/B-overlap":7,
                    "B/B-disjoint":6,
                }, 169, 32, 7627209),
            }
            expected_seven,expected_S,expected_Q4,expected_lower = pinned[scheme]
            self.assertEqual(z["seven_class_motif_counts"],expected_seven)
            self.assertEqual(z["S_seven"],expected_S)
            self.assertEqual(z["Q4"],expected_Q4)
            self.assertEqual(z["GF5_seven_lower_numerator"],expected_lower)
            self.assertEqual(sum(z["new_classes"].values()),total)
            self.assertGreaterEqual(z["S_seven"],total)
            baseline=finite_census(model)
            self.assertEqual(z["new_classes"],baseline["new_motif_counts"])
            self.assertGreaterEqual(z["GF5_seven_lower"],
                                    baseline["GF5_exact_restricted_R3_lower"])
            self.assertIsInstance(z["GF5_Q4_R2_lower"],Fraction)
            self.assertGreaterEqual(z["Q4"],0)
            self.assertEqual(z["GF5_Q4_R2_lower"],
                             Fraction(531*z["Q4"],51**4))
            self.assertEqual(z["GF5_seven_lower"],
                             Fraction(z["GF5_seven_lower_numerator"],GF5_DENOM))
            self.assertEqual(z["S_seven"],
                             sum(z["seven_class_motif_counts"].values()))
            self.assertFalse(z["all_h_universal_S_lower_proved"])
            self.assertFalse(z["full_GF5_R2_or_R3_computed"])

    def test_independent_ten_column_full_seven_family_brute(self):
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            all_result=seven_census(model,witness_sets=True,
                                    independent_checks=False)
            actual=all_result["sets"]
            witnesses=list(all_result["witnesses"].values())
            if not witnesses:
                raise AssertionError("nonempty genuine W32 E1B0 witnesses needed")
            for witness in witnesses:
                selected=list(witness)+[
                    i for i in range(model["N"]) if i not in witness
                ][:4]
                self.assertEqual(len(selected),10)
                for ids in combinations(sorted(selected),6):
                    independent=independent_brute_tag(model,ids)
                    optimized=classify_seven_prechecked(
                        ids,model["left_labels"],model["right_labels"],
                        model["incidences"])
                    self.assertEqual(independent,optimized)
                    self.assertEqual(independent,actual.get(ids))

    def test_independent_left_and_right_physical_gauge(self):
        model=pair_labeled_symplectic(1,"lex")
        left_perm=(2,0,5,1,4,3)
        right_perm=(4,1,0,5,3,2)
        rename=lambda edge,per:tuple(sorted(per[v] for v in edge))
        new=dict(model)
        new["left_labels"]=tuple(rename(e,left_perm)
                                 for e in model["left_labels"])
        new["right_labels"]=tuple(rename(e,right_perm)
                                  for e in model["right_labels"])
        # Deliberately does not alter model["supports"], since this
        # is a structural motif and risk-floor census, NOT actual
        # full GF5 support oracle on the rewritten map.
        a=seven_census(model)
        b=seven_census(new)
        self.assertEqual(a["seven_class_motif_counts"],
                         b["seven_class_motif_counts"])
        self.assertEqual(a["Q4"],b["Q4"])
        self.assertEqual(a["GF5_seven_lower"],b["GF5_seven_lower"])

    def test_formal_all_h_polynomial_coefficient_identity_toy(self):
        """Independent subset enumeration equals formal generating polynomial.

        Ten selected original columns, then the entire 2^10 squarefree
        product P=prod_e(1+t*x_f(e)^2*y_g(e)^2) is expanded (truncated
        combinatorially, no mod 5 reduction). Exact degree filters count
        leafless 6x6 physical coordinates. This identity is valid for
        ANY incidence system, despite no all-h constructive lower.
        """
        m=pair_labeled_symplectic(1,"lex")
        indices=tuple(range(10))
        polynomial=Counter()
        by_support=Counter()
        for k in range(11):
            for local in combinations(indices,k):
                LX=Counter(v for eid in local
                           for v in m["left_labels"][m["incidences"][eid][0]])
                RY=Counter(v for eid in local
                           for v in m["right_labels"][m["incidences"][eid][1]])
                signature=(k,tuple(sorted(LX.items())),tuple(sorted(RY.items())))
                polynomial[signature]+=1
                if k==6 and len(LX)==len(RY)==6 and (
                        set(LX.values())=={2} and set(RY.values())=={2}):
                    by_support[(tuple(sorted(LX)),tuple(sorted(RY)))]+=1
        exact=Counter()
        for (k,l,r),coeff in polynomial.items():
            if k!=6 or len(l)!=6 or len(r)!=6:
                continue
            if {deg for _,deg in l}!={2} or {deg for _,deg in r}!={2}:
                continue
            exact[(tuple(u for u,_ in l),tuple(u for u,_ in r))]+=coeff
        self.assertEqual(exact,by_support)
        self.assertEqual(sum(polynomial.values()),2**10)

    def test_exact_full_pallette_GF5_signed_subset_seven_class_risk(self):
        """All TEN signed configurations of EVERY accepted actual sixset."""
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            structural=seven_census(model)
            weighted=exact_seven_weighted_GF5(model,max_signed_events=5000)
            self.assertEqual(weighted["seven_class_original_sixsets"],
                             structural["S_seven"])
            self.assertEqual(weighted["selected_exact_GF5_signed_events"],
                             10*structural["S_seven"])
            self.assertGreaterEqual(weighted["exact_selected_GF5_R3"],
                                    structural["GF5_seven_lower"])
            self.assertEqual(weighted["exact_selected_GF5_R3"],
                             Fraction(weighted["exact_selected_GF5_R3_numerator"],
                                      GF5_DENOM))
            self.assertEqual(sum(weighted["selected_GF5_sum_by_class"].values()),
                             weighted["exact_selected_GF5_R3_numerator"])
            self.assertFalse(weighted["total_GF5_R3_all_motifs"])
            self.assertFalse(weighted["all_h_general_GF5_bound"])
        with self.assertRaises(ValueError):
            exact_seven_weighted_GF5(pair_labeled_symplectic(1,"lex"),
                                     max_signed_events=1)

    def test_classifier_invalid_and_no_asymptotic_promotion(self):
        m=pair_labeled_symplectic(1,"lex")
        with self.assertRaises(ValueError):
            classify_seven_prechecked([0,0,1,2,3,4],
                                      m["left_labels"],m["right_labels"],
                                      m["incidences"])
        with self.assertRaises(ValueError):
            classify_seven_prechecked([0,1,2,3,4,45],
                                      m["left_labels"],m["right_labels"],
                                      m["incidences"])
        r=report()
        self.assertTrue(r["all_h_formal_coefficient_identity"])
        self.assertFalse(r["all_h_universal_motif_lower"])
        self.assertFalse(r["all_h_strict_R3_upper"])
        self.assertFalse(r["actual_full_R3_computed"])


if __name__=="__main__":
    unittest.main()
