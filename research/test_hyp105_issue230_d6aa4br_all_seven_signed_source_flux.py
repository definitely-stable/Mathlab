"""AA4-BR independent historical real original W32 seven-GF5 evidence."""
import unittest
from itertools import permutations
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import (
  seven_census,R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
  immutable_original_sixflag_class,exact_original_W32_signed_index,
  exact_original_W32_signed_swap,exact_permutation_involution_balance,
)

class TestBR(unittest.TestCase):
  def test_01_genuine_original_W32_stable_source_GF5_tag(self):
    for scheme in ("lex","reverse","S68","S72"):
      model=fixture(1,scheme)
      i=exact_original_W32_signed_index(model)
      census=seven_census(model,independent_checks=False,witness_sets=True)
      self.assertEqual(len(i["rows"]),62370)
      for Q,tag in census["sets"].items():
        self.assertEqual(immutable_original_sixflag_class(Q,i["incidences"]),tag)
      for Q in i["rows"][::329]:
        observed=classify_seven_prechecked(Q,i["left"],i["right"],i["incidences"])
        self.assertIn(observed,(None,immutable_original_sixflag_class(Q,i["incidences"])))

  def test_02_true_W32_signed_flux_vs_independent_entire_historical_census(self):
    for scheme,pair in (("lex",(0,1)),("reverse",(3,11)),
                        ("S68",(2,7)),("S72",(4,9))):
      model=fixture(1,scheme)
      i=exact_original_W32_signed_index(model)
      x=exact_original_W32_signed_swap(model,*pair,index=i)
      print("SIGNED_GF5_FLUX_SCHEME",scheme,"swap",pair,"births",x["births"],"deaths",x["deaths"],"seven_delta",x["signed_seven_total_delta"],"floor_delta",x["signed_seven_GF5_R3_floor_numerator_delta"],flush=True)
      pinned_flux={"lex":(-42,-1502050),"reverse":(18,901714),
                   "S68":(51,2306970),"S72":(19,841023)}
      self.assertEqual((x["signed_seven_total_delta"],
                        x["signed_seven_GF5_R3_floor_numerator_delta"]),
                       pinned_flux[scheme])
      before=seven_census(model,independent_checks=False)
      changed=dict(model,right_labels=x["new_complete_global_original_LINE_map"])
      after=seven_census(changed,independent_checks=False)
      for c in R3_CERTIFIED_FLOORS:
        self.assertEqual(x["signed_class_deltas"][c],
             after["seven_class_motif_counts"][c]-before["seven_class_motif_counts"][c])
      self.assertEqual(x["signed_seven_total_delta"],after["S_seven"]-before["S_seven"])
      self.assertEqual(x["signed_seven_GF5_R3_floor_numerator_delta"],
          after["GF5_seven_lower_numerator"]-before["GF5_seven_lower_numerator"])
      self.assertLess(x["touched_true_original_Q"],62370)
      for operation,tag,Q in x["original_sixflag_transition_witnesses"]:
        self.assertEqual(immutable_original_sixflag_class(Q,model["incidences"]),tag)

  def test_03_no_crossing_under_different_real_original_global_maps(self):
    model=fixture(1,"lex")
    i=exact_original_W32_signed_index(model)
    rows=i["rows"][::43]
    right=list(i["right"])
    for a,b in ((0,1),(2,7),(5,11),(10,14)):
      right[a],right[b]=right[b],right[a]
      for Q in rows:
        tag=classify_seven_prechecked(Q,i["left"],tuple(right),i["incidences"])
        self.assertIn(tag,(None,immutable_original_sixflag_class(Q,i["incidences"])))

  def test_04_true_original_source_line_swap_inverse_birth_death(self):
    model=fixture(1,"S72")
    first=exact_original_W32_signed_swap(model,0,1)
    updated=dict(model,right_labels=first["new_complete_global_original_LINE_map"])
    back=exact_original_W32_signed_swap(updated,0,1)
    for c in R3_CERTIFIED_FLOORS:
      self.assertEqual(first["signed_class_deltas"][c],-back["signed_class_deltas"][c])
      self.assertEqual(first["births"][c],back["deaths"][c])
      self.assertEqual(first["deaths"][c],back["births"][c])
    self.assertEqual(first["signed_seven_GF5_R3_floor_numerator_delta"],
                    -back["signed_seven_GF5_R3_floor_numerator_delta"])

  def test_05_original_id_and_scope_guards(self):
    model=fixture(1,"lex")
    index=exact_original_W32_signed_index(model)
    for u,v in ((0,0),(-1,2),(0,15),(0,True)):
      with self.assertRaises(ValueError):
        exact_original_W32_signed_swap(model,u,v,index=index)
    with self.assertRaises(ValueError):
      immutable_original_sixflag_class((0,0,1,2,3,4),model["incidences"])
    with self.assertRaises(ValueError):
      immutable_original_sixflag_class((0,1,2,3,4,999),model["incidences"])
    tampered=dict(model,right_labels=tuple(reversed(model["right_labels"])))
    with self.assertRaises(ValueError):
      exact_original_W32_signed_swap(tampered,0,1,index)
    with self.assertRaises(ValueError):
      exact_original_W32_signed_index(fixture(2,"lex"))

  def test_06_complete_uniform_S4_involution_no_center_sign(self):
    maps=tuple(permutations(range(4)))
    def cost(row):return 7*(row[0]==0)+3*(row[1] in (1,2))
    x=exact_permutation_involution_balance(maps,0,1,cost)
    self.assertGreater(x["positive"],0)
    self.assertEqual(x["positive"],x["negative"])
    self.assertFalse(x["original_center_sign_known"])
    with self.assertRaises(ValueError):
      exact_permutation_involution_balance(maps[:-1],0,1,cost)
    with self.assertRaises(ValueError):
      exact_permutation_involution_balance(maps+(maps[0],),0,1,cost)
if __name__=="__main__":unittest.main()
