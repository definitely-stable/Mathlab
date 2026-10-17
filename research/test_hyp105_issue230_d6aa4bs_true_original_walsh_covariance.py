"""AA4-BS: independent original full seven GF5 8-map Walsh/variance falsifiers."""
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import exact_original_W32_signed_swap
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_issue230_d6aa4bs_true_original_walsh_covariance import (
    true_original_line_swap_support,
    all_h_true_original_source_walsh_bound,
    unnormalized_walsh,
    exact_individual_original_six_Q_cube,
    exact_true_W32_seven_walsh_gram,
)

SWAPS=((0,1),(2,3),(4,5))
SEVEN=tuple(R3_CERTIFIED_FLOORS)

def independent_real_W32_seven_census_whole_cube(model,swaps):
    old=tuple(model["right_labels"])
    result=[]
    for mask in range(1<<len(swaps)):
        state=apply_disjoint_factor_swaps(old,swaps,
                     tuple(j for j in range(len(swaps)) if mask&(1<<j)))
        record=seven_census(dict(model,right_labels=state),independent_checks=False)
        result.append(record)
    return result


class AA4BSWalshTrueOriginal(unittest.TestCase):
    def test_01_all_h_genuine_source_incidence_bound_no_fake_large_W3(self):
        for h in tuple(range(1,38))+(40,48,64,80):
            s=1<<h
            prev=None
            for t in range(1,9):
                x=all_h_true_original_source_walsh_bound(s,t)
                self.assertEqual(x["d_original_incident_flags_per_source_LINE"],s+1)
                self.assertEqual(x["M_true_original_incidence_flags"],
                                 (s+1)**2*(s*s+1))
                if t>6:
                    self.assertEqual(x["max_original_sixflag_Q_touching_ALL_t"],0)
                    self.assertEqual(x["maximum_abs_unweighted_nonconstant_Walsh_coefficient"],0)
                else:
                    self.assertGreater(x["max_original_sixflag_Q_touching_ALL_t"],0)
                    self.assertEqual(
                        x["maximum_abs_selected_GF5_weighted_nonconstant_Walsh_coefficient"],
                        x["maximum_abs_unweighted_nonconstant_Walsh_coefficient"]*
                        max(R3_CERTIFIED_FLOORS.values()))
                prev=x
        for s,t in ((1,1),(3,2),(4,0),(True,1),(2,True)):
            with self.assertRaises(ValueError):
                all_h_true_original_source_walsh_bound(s,t)

    def test_02_historical_genuine_W32_ALL_seven_classes_independent_cube(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            data=exact_true_W32_seven_walsh_gram(model,SWAPS)
            independently=independent_real_W32_seven_census_whole_cube(model,SWAPS)
            self.assertEqual(data["genuine_original_left_sixflag_Q_count"],62370)
            self.assertEqual(data["n_actual_COMPLETE_original_global_maps"],8)
            for i,rec in enumerate(independently):
                self.assertEqual(data["per_vertex_all_seven_GF5_counts"][i],
                                 rec["seven_class_motif_counts"])
                self.assertEqual(data["historical_selected_GF5_floor_weighted_values"][i],
                                 rec["GF5_seven_lower_numerator"])
            self.assertGreater(data["TRUE_original_Q_with_nonconstant_acceptance_under_cube"],0)
            self.assertTrue(data["full_original_right_image_support_unchanged"])

    def test_03_weighted_all_SEVEN_Gram_independent_counts_and_signed_correlations(self):
        data=exact_true_W32_seven_walsh_gram(fixture(1,"S72"),SWAPS)
        counts=data["per_vertex_all_seven_GF5_counts"]
        n=len(counts)
        for c in SEVEN:
            for d in SEVEN:
                direct=Fraction(sum(x[c]*x[d] for x in counts),n)\
                  -Fraction(sum(x[c] for x in counts),n)*Fraction(sum(x[d] for x in counts),n)
                self.assertEqual(data["seven_class_covariance_matrix"][(c,d)],direct)
        weighted=data["historical_selected_GF5_floor_weighted_values"]
        directvar=Fraction(sum(x*x for x in weighted),n)-Fraction(sum(weighted),n)**2
        self.assertEqual(data["weighted_original_GF5_floor_variance"],directvar)
        self.assertEqual(directvar,Fraction(3508898523703,4))
        self.assertEqual(data["weighted_gradient_Poincare_energy"],1011049069881)
        self.assertGreater(data["strict_higher_order_gradient_energy"],0)
        self.assertGreaterEqual(data["weighted_gradient_Poincare_energy"],directvar)
        offdiag=[(data["seven_class_covariance_matrix"][(c,d)],c,d)
                 for i,c in enumerate(SEVEN) for d in SEVEN[i+1:]]
        print("AA4BS_TRUE_W32_SEVEN_CROSS_COV_MIN_MAX",
              min(offdiag),max(offdiag),flush=True)
        for T in range(1,8):
            cap=all_h_true_original_source_walsh_bound(2,T.bit_count())
            self.assertLessEqual(
                Fraction(abs(data["historical_selected_GF5_floor_weighted_Walsh_numerators"][T]),8),
                cap["maximum_abs_selected_GF5_weighted_nonconstant_Walsh_coefficient"])
            for c in SEVEN:
                self.assertLessEqual(
                    Fraction(abs(data["seven_class_Walsh_numerators"][c][T]),8),
                    cap["maximum_abs_unweighted_nonconstant_Walsh_coefficient"])
        print("AA4BS_TRUE_W32_WEIGHTED_VARIANCE",directvar,
              "GRADIENT_ENERGY",data["weighted_gradient_Poincare_energy"],
              "HIGHER_ORDER",data["strict_higher_order_gradient_energy"],flush=True)

    def test_04_real_original_Q_disjoint_SOURCE_swap_support_zero_covariance(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        rows=tuple(Q for Q,_ in selected_left_six(model))
        chosen={}
        for Q in rows:
            D=true_original_line_swap_support(Q,inc,SWAPS,V)
            if D in (1,2) and D not in chosen:chosen[D]=Q
            if len(chosen)==2:break
        self.assertEqual(set(chosen),{1,2})
        a=exact_individual_original_six_Q_cube(model,chosen[1],SWAPS)
        b=exact_individual_original_six_Q_cube(model,chosen[2],SWAPS)
        self.assertEqual(a["touched_source_LINE_pair_mask"]&
                         b["touched_source_LINE_pair_mask"],0)
        x=a["historical_G5_accepted_indicator_at_each_FULL_global_map"]
        y=b["historical_G5_accepted_indicator_at_each_FULL_global_map"]
        actual=Fraction(sum(u*v for u,v in zip(x,y)),8)\
              -Fraction(sum(x),8)*Fraction(sum(y),8)
        self.assertEqual(actual,0)
        for witness in (a,b):
            for T,c in enumerate(witness["unnormalized_Walsh_numerators"]):
                if T&~witness["touched_source_LINE_pair_mask"]:
                    self.assertEqual(c,0)
        self.assertEqual(len(chosen[1]),6)
        self.assertEqual(len(chosen[2]),6)

    def test_05_first_order_TRUE_original_SIGNED_BR_flux_equals_Walsh(self):
        model=fixture(1,"S72")
        x=exact_true_W32_seven_walsh_gram(model,((4,9),))
        flux=exact_original_W32_signed_swap(model,4,9)
        for c in SEVEN:
            self.assertEqual(x["seven_class_Walsh_numerators"][c][1],
                             -flux["signed_class_deltas"][c])
        self.assertEqual(x["historical_selected_GF5_floor_weighted_Walsh_numerators"][1],
                         -flux["signed_seven_GF5_R3_floor_numerator_delta"])
        self.assertEqual(x["weighted_gradient_Poincare_energy"],
                         x["weighted_original_GF5_floor_variance"])

    def test_06_invalid_real_original_six_flags_overlap_swaps_and_wrong_scope(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        Q=tuple(next(iter(selected_left_six(model)))[0])
        with self.assertRaises(ValueError):
            true_original_line_swap_support((Q[0],)*6,inc,SWAPS,V)
        with self.assertRaises(ValueError):
            exact_individual_original_six_Q_cube(model,Q,((0,1),(1,2)))
        with self.assertRaises(ValueError):
            exact_true_W32_seven_walsh_gram(model,())
        with self.assertRaises(ValueError):
            exact_true_W32_seven_walsh_gram(fixture(2,"lex"),SWAPS)
        with self.assertRaises(ValueError):
            exact_true_W32_seven_walsh_gram(model,((0,1),)*2)
        with self.assertRaises(ValueError):
            unnormalized_walsh((1,2,3))
        with self.assertRaises(ValueError):
            unnormalized_walsh((1,False))
        with self.assertRaises(ValueError):
            all_h_true_original_source_walsh_bound(2,-1)


if __name__=="__main__":
    unittest.main()
