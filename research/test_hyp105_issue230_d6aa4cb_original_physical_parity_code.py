"""Independent finite and genuine original W32 AA4-CB parity-code checks."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from hyp105_issue230_d6aa4cb_original_physical_parity_code import (
    K6, GLOBAL_PARITY_CODE_ETA, GLOBAL_CA_TO_CB_SAVING,
    parity_columns_from_12_images, gf2_rank, syndrome, profile_scores,
    affine_kernel_bound, exact_rank2_profile_certificate,
    independent_rank2_dual_mask_oracle, original_packet_parity_columns,
    original_Q_parity_sieve, original_W32_f_only_all_seven_parity_envelope,
    original_W32_all64_true_center_parity_envelope)
from hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel import assert_n3_independent_cube
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import original_six_packet_source_line_A, physical_right_is_six_vertex_two_regular
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))
EXACT_PROFILES={
 (0,2,2,2):54,(0,3,2,1):44,(0,3,3,0):36,
 (0,4,1,1):52,(0,4,2,0):48,(0,5,1,0):52,
 (1,2,2,1):38,(1,3,1,1):50,(1,3,2,0):40,
 (1,4,1,0):48,(2,2,1,1):34,(2,2,2,0):46,
 (2,3,1,0):42,(3,1,1,1):42,(3,2,1,0):38,
 (4,1,1,0):42}

class AA4CBParity(unittest.TestCase):
 def test_01_exact_16_profile_certificate(self):
    self.assertEqual(exact_rank2_profile_certificate(),EXACT_PROFILES)
    self.assertEqual(profile_scores(0,2,2,2)[0],(54,6))
    self.assertEqual(GLOBAL_PARITY_CODE_ETA,Fraction(27,32))
    self.assertEqual(GLOBAL_CA_TO_CB_SAVING,Fraction(3,32))

 def test_02_independent_651_dual_space_certificate(self):
    z=independent_rank2_dual_mask_oracle()
    self.assertEqual(z["dual_spaces"],651)
    self.assertEqual(z["max_abs_numerator"],54)
    self.assertEqual(sum(z["score_histogram"].values()),651)
    u,v=15,51
    coset={x for x in range(64) if (u&x).bit_count()%2==0 and (v&x).bit_count()%2==0}
    positive=tuple(int(x in coset and K6[x.bit_count()]>0) for x in range(64))
    assert_n3_independent_cube(positive)
    self.assertEqual(sum(positive[x]*K6[x.bit_count()] for x in range(64)),54)

 def test_03_rank_one_no_original_physical_2factor_and_validation(self):
    packets=tuple(((0,i+2),(1,i+2)) for i in range(6))
    cols=parity_columns_from_12_images(packets)
    self.assertEqual(gf2_rank(cols),1)
    self.assertEqual(affine_kernel_bound(cols)["eta"],0)
    for x in range(64):
        edges=tuple(p[x>>i&1] for i,p in enumerate(packets))
        degree=Counter(z for e in edges for z in e)
        self.assertFalse(len(degree)==6 and all(z==2 for z in degree.values()))
    for bad in (packets[:5], tuple(((0,2),(1,2)) for _ in range(6)),
                packets[:5]+(((0,7),(7,7)),)):
        with self.assertRaises(ValueError):parity_columns_from_12_images(bad)
    with self.assertRaises(ValueError):profile_scores(0,0,0,5)

 def test_04_affine_syndrome_nonzero_at_original_center(self):
    base=tuple((i,(i+1)%6) for i in range(6))
    occupied={tuple(sorted(e)) for e in base}
    free=tuple(e for e in combinations(range(6),2) if e not in occupied)
    packets=tuple((free[i],base[i]) for i in range(6))
    columns=parity_columns_from_12_images(packets)
    self.assertGreaterEqual(gf2_rank(columns),2)
    original_parity=0
    for edge,_ in packets:
        original_parity^=(1<<edge[0])^(1<<edge[1])
    self.assertNotEqual(original_parity,0)
    self.assertEqual(syndrome(columns,63),original_parity)
    self.assertEqual(Counter(z for e in base for z in e),
                     Counter({j:2 for j in range(6)}))

 def test_05_TRUE_original_W32_351_301_Q_complete_global_maps(self):
    for scheme in ("lex","S72"):
        model=fixture(1,scheme)
        s,V,a,inc,f,g,_,_=_original_source(model)
        rank=gf2_rank(original_packet_parity_columns(model,PACKETS))
        Qs=tuple(Q for Q,_ in selected_left_six(model)
                 if original_six_packet_source_line_A(Q,inc,PACKETS,V))
        self.assertEqual(len(Qs),351 if scheme=="lex" else 301)
        full_maps=tuple(apply_disjoint_factor_swaps(
            g,PACKETS,tuple(j for j in range(6) if x>>j&1))
            for x in range(64))
        positive=0
        for Q in Qs:
            val=original_Q_parity_sieve(model,Q,PACKETS)
            self.assertEqual(val["parity_rank"],rank)
            positive+=bool(val["physical_active_states"])
            self.assertLessEqual(val["physical_code_eta"],Fraction(27,32))
            for x in range(64):
                right=physical_right_is_six_vertex_two_regular(Q,inc,full_maps[x])
                self.assertEqual(val["physical_indicator"][x],int(right))
                tag=classify_seven_prechecked(Q,f,full_maps[x],inc)
                self.assertLessEqual(int(tag is not None),int(right))
        print("AA4CB_ORIGINAL",scheme,"Q",len(Qs),
              "rank",rank,"physical_positive_Q",positive,flush=True)

 def test_06_original_W32_weighted_all_seven_center_and_f_only(self):
    expected={
      "lex":(4690929,Fraction(14072787,32),Fraction(16212794755,32),11225795),
      "S72":(3731790,Fraction(5597685,16),Fraction(7761243177,16),3283610)}
    for scheme,(mass,saving,e,center) in expected.items():
        model=fixture(1,scheme)
        d=original_W32_f_only_all_seven_parity_envelope(model,PACKETS)
        self.assertEqual(d["original_f_only_six_source_Q_weight"],mass)
        self.assertEqual(d["strict_universal_saving"],saving)
        self.assertEqual(d["new_CB_universal_f_only_E"],e)
        self.assertLessEqual(d["new_CB_actual_f_g_rank_adaptive_E"],e)
        changed=dict(model,right_labels=tuple(reversed(model["right_labels"])))
        d2=original_W32_f_only_all_seven_parity_envelope(changed,PACKETS)
        self.assertEqual(d2["new_CB_universal_f_only_E"],e)
        original=original_W32_all64_true_center_parity_envelope(model,PACKETS)
        self.assertEqual(original["actual_weighted_original_GF5_center"],center)
        self.assertEqual(original["new_rank_adaptive_E"],d["new_CB_actual_f_g_rank_adaptive_E"])
        self.assertLessEqual(original["certified_center_lower"],center)
        print("AA4CB_ENVELOPE",scheme,"f_only",e,
              "adaptive",original["new_rank_adaptive_E"],
              "lower",original["certified_center_lower"],flush=True)

if __name__=="__main__":
 unittest.main()
