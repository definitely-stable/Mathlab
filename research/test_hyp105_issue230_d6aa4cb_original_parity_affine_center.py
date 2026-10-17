"""Independent finite ORIGINAL GF2 parity center and full seven-GF5 falsifiers."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,true_original_W32_all_seven_center_envelope,
)
from hyp105_issue230_d6aa4cb_original_parity_affine_center import (
    _gf2_rank,_screen_error,
    genuine_original_Q_parity_sixcube,
    true_original_W32_g_conditioned_all_seven_center,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def independent_original_physical_right_even(Q,inc,images):
    """Literal physical degree parity, not the affine-source evaluator."""
    parity=Counter(vertex for j in Q for vertex in images[inc[j][1]])
    return all(n%2==0 for n in parity.values())


def independent_original_right_six_2regular(Q,inc,images):
    degree=Counter(vertex for j in Q for vertex in images[inc[j][1]])
    return len(degree)==6 and set(degree.values())=={2}


def independent_signed_local_bound(S,k,reference=0):
    """Independent positive/negative source support kernel sum oracle."""
    K=high_degree_boolean_kernel(k)
    vals=[K[reference^u] for u in S]
    return Fraction(max(sum(t for t in vals if t>0),
                        -sum(t for t in vals if t<0)),1<<k)


class CBTrueOriginalGF2PhysicalCenter(unittest.TestCase):
    def test_01_exact_F2_rank_and_parity_affine_cosets_real_original_W32(self):
        self.assertEqual(_gf2_rank((0,0,0)),0)
        self.assertEqual(_gf2_rank((3,5,6)),2)
        self.assertEqual(_gf2_rank((1,2,4,8,16,32)),6)
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(m)
            picked=Counter();seen_rank=set()
            for Q,_ in selected_left_six(m):
                tag=immutable_original_sixflag_class(Q,inc)
                if tag not in R3_CERTIFIED_FLOORS:continue
                touched=sum(any(inc[j][1] in p for j in Q) for p in PACKETS)
                if touched<4 or picked[touched]>=6:continue
                picked[touched]+=1
                z=genuine_original_Q_parity_sixcube(m,Q,PACKETS)
                used=z["touched_original_LINE_packet_indices"]
                k=len(used)
                seen_rank.add((k,z["exact_GF2_column_rank"]))
                correct_parity=[];correct_2factor=[];correct_historical=[]
                for local in range(1<<k):
                    images=apply_disjoint_factor_swaps(g,PACKETS,
                        tuple(used[j] for j in range(k) if local>>j&1))
                    if independent_original_physical_right_even(Q,inc,images):
                        correct_parity.append(local)
                    if independent_original_right_six_2regular(Q,inc,images):
                        correct_2factor.append(local)
                    if classify_seven_prechecked(Q,f,images,inc) is not None:
                        correct_historical.append(local)
                self.assertEqual(tuple(correct_parity),
                                 z["parity_zero_affine_coset"])
                self.assertEqual(tuple(correct_2factor),
                                 z["physical_right_2regular_states"])
                self.assertEqual(tuple(correct_historical),
                                 z["historically_accepted_original_GF5_states"])
                self.assertTrue(set(correct_historical)<=set(correct_2factor)
                                <=set(correct_parity))
                if correct_parity:
                    self.assertEqual(len(correct_parity),
                        1<<(k-z["exact_GF2_column_rank"]))
                else:self.assertEqual(z["zero_parity_state_count"],0)
            self.assertGreater(sum(picked.values()),0)
            self.assertGreater(len(seen_rank),1)

    def test_02_exact_signed_local_parity_and_two_factor_bounds_all_vertices(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(m)
            sampled=0
            for Q,_ in selected_left_six(m):
                if immutable_original_sixflag_class(Q,inc) not in R3_CERTIFIED_FLOORS:
                    continue
                if sum(any(inc[j][1] in pair for j in Q) for pair in PACKETS)<4:
                    continue
                z=genuine_original_Q_parity_sixcube(m,Q,PACKETS)
                k=len(z["touched_original_LINE_packet_indices"])
                for key,S in (("parity",z["parity_zero_affine_coset"]),
                              ("2regular",z["physical_right_2regular_states"])):
                    self.assertEqual(z[
                        "local_"+("parity" if key=="parity" else "2regular")+
                        "_center_absolute_highpass_upper"],
                                     independent_signed_local_bound(S,k))
                    max_ind=max(independent_signed_local_bound(S,k,c)
                                for c in range(1<<k))
                    self.assertEqual(z[
                        "local_"+("parity" if key=="parity" else "2regular")+
                        "_ALL_VERTEX_absolute_highpass_upper"],max_ind)
                    self.assertLessEqual(z[
                        "local_"+("parity" if key=="parity" else "2regular")+
                        "_center_absolute_highpass_upper"],max_ind)
                sampled+=1
                if sampled>=25:break
            self.assertEqual(sampled,25)

    def test_03_true_original_W32_ALL_SEVEN_g_conditioned_new_error_envelopes(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            z=true_original_W32_g_conditioned_all_seven_center(model,PACKETS)
            E=z["true_original_g_quenched_all_seven_envelopes"]
            self.assertEqual(z["s"],2)
            self.assertGreater(z["source_Q_high_order_candidates"],0)
            self.assertGreater(z["parent_original_f_only_all_seven_E"],0)
            self.assertLessEqual(E["parity_uniform"],
                                 z["parent_original_f_only_all_seven_E"])
            self.assertLessEqual(E["right_2factor_uniform"],E["parity_uniform"])
            self.assertLessEqual(E["right_2factor_original_center"],
                                 E["parity_original_center"])
            self.assertLessEqual(E["parity_original_center"],E["parity_uniform"])
            self.assertTrue(z["exact_g_conditional_parity_linear_system_each_Q"])
            print("AA4CB_W32_G_CONDITIONED",scheme,
                "Q",z["source_Q_high_order_candidates"],
                "f-only",z["parent_original_f_only_all_seven_E"],
                "parity-center",E["parity_original_center"],
                "parity-uniform",E["parity_uniform"],
                "2reg-center",E["right_2factor_original_center"],
                "2reg-uniform",E["right_2factor_uniform"],flush=True)

    def test_04_REAL_W32_full_SEVEN_GF5_all_64_original_center_verified(self):
        # FULL historical seven_GF5 oracle is intentionally separate
        # from the novel physical right-degree parity/right-2factor
        # source-Q supports. Every x changes the WHOLE g globally.
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            z=true_original_W32_g_conditioned_all_seven_center(m,PACKETS)
            whole=true_original_W32_all_seven_center_envelope(m,PACKETS)
            signed=whole["signed_higher_order_weighted_values"]
            E=z["true_original_g_quenched_all_seven_envelopes"]
            self.assertEqual(len(signed),64)
            self.assertLessEqual(abs(signed[0]),
                                 E["parity_original_center"])
            self.assertLessEqual(abs(signed[0]),
                                 E["right_2factor_original_center"])
            self.assertLessEqual(max(abs(v) for v in signed),
                                 E["parity_uniform"])
            self.assertLessEqual(max(abs(v) for v in signed),
                                 E["right_2factor_uniform"])
            low=whole["degree_at_most_three_weighted_values"]
            exact=whole["full_64_original_GF5_seven_weighted_necessary_numerators"]
            self.assertEqual(
                Fraction(exact[0]),low[0]+signed[0])
            self.assertGreaterEqual(exact[0],max(
                Fraction(0),low[0]-E["right_2factor_original_center"]))
            print("AA4CB_ACTUAL_CENTER",scheme,
                  "historical_weighted_seven",exact[0],
                  "low-degree",low[0],
                  "signed_high",signed[0],
                  "new_certified_lower",max(Fraction(0),low[0]-
                      E["right_2factor_original_center"]),flush=True)

    def test_05_actual_original_f_g_same_occupied_right_support_but_g_sensitive(self):
        model=fixture(1,"S72")
        parent=true_original_W32_g_conditioned_all_seven_center(model,PACKETS)
        changed=dict(model,right_labels=tuple(reversed(model["right_labels"])))
        other=true_original_W32_g_conditioned_all_seven_center(changed,PACKETS)
        self.assertEqual(parent["parent_original_f_only_all_seven_E"],
                         other["parent_original_f_only_all_seven_E"])
        for z in (parent,other):
            self.assertLessEqual(z["true_original_g_quenched_all_seven_envelopes"][
                "right_2factor_original_center"],
                z["parent_original_f_only_all_seven_E"])
        # No assert that the two map-conditioned errors differ:
        # in some physical palette symmetries or degenerate packet
        # choices they can coincide despite different complete g.
        self.assertEqual(set(model["right_labels"]),set(changed["right_labels"]))

    def test_07_real_original_W34_GF4_NONONTO_K14_affine_source_parity(self):
        # Actual genuine symplectic W(3,4), V=85, a=14 NONONTO E(K14).
        # This tests direct source-incidence affine GF2 algebra on a
        # larger-than-W32 physical palette, without enumerating all
        # high-h candidate six-Q or pretending a synthetic GQ.
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for shift in (0,1,2):
                source_lines=(0,2,4,6,8,10)
                Q=tuple(tuple(j for j,(p,l) in enumerate(inc)
                              if l==line)[shift]
                        for line in source_lines)
                z=genuine_original_Q_parity_sixcube(
                    model,Q,PACKETS,verify_historical=False)
                used=z["touched_original_LINE_packet_indices"]
                self.assertEqual(len(used),6)
                actual=tuple(y for y in range(64)
                    if independent_original_physical_right_even(
                        Q,inc,apply_disjoint_factor_swaps(
                            g,PACKETS,tuple(used[j] for j in range(6)
                                            if y>>j&1))))
                self.assertEqual(actual,z["parity_zero_affine_coset"])
                self.assertLessEqual(len(z["physical_right_2regular_states"]),
                                     len(actual))

    def test_06_adversarial_invalid_true_original_flag_or_global_g_fails_closed(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        Q=next(Q for Q,_ in selected_left_six(model))
        for bad in ((Q[0],)*6,(Q[0],Q[1],Q[2],Q[3],Q[4],999)):
            with self.assertRaises(ValueError):
                genuine_original_Q_parity_sixcube(model,bad,PACKETS)
        with self.assertRaises(ValueError):
            genuine_original_Q_parity_sixcube(model,Q,PACKETS[:5])
        with self.assertRaises(ValueError):
            genuine_original_Q_parity_sixcube(model,Q,
                ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10)))
        with self.assertRaises(ValueError):
            genuine_original_Q_parity_sixcube(
                dict(model,right_labels=((0,1),)*15),Q,PACKETS)
        with self.assertRaises(ValueError):
            true_original_W32_g_conditioned_all_seven_center(
                fixture(2,"lex"),PACKETS)
        with self.assertRaises(ValueError):
            _screen_error((100,),4,all_centers=True)

if __name__=="__main__":
    unittest.main()
