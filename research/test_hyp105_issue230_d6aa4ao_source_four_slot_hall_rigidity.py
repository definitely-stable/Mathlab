"""AA4-AO strict true ORIGINAL source four-slot GQ rigidity tests."""
import unittest
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import original_D_pair_index
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    physical_D_pair_half_patterns,
    exact_original_D_pair_six_Q_funnel,
)
from hyp105_issue230_d6aa4ao_source_four_slot_hall_rigidity import (
    _four_slot_certificate,
    exact_true_original_four_slot_Hall_certificate,
    exact_true_original_D_anchor_slot_upper,
    all_h_complete_palette_port_four_slot_Hall_upper,
)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)

PROFILES={
    "A/A":((0,1,2,3),(0,1,2,3),{0:11321,1:4824,2:72}),
    "B/A":((0,0,1,2),(0,1,2,3),{0:1496,1:360}),
    "A/B":((0,1,2,3),(0,0,1,2),{0:1496,1:360}),
    "B/B":((0,0,1,2),(0,0,1,2),{0:302,1:26}),
}


def independent_original_local_girth8(edge_set):
    """Independently inspect source edge paths, not slot-matchings."""
    pp={p for p,l in edge_set}
    ll={l for p,l in edge_set}
    N={p:{l for l in ll if (p,l) in edge_set} for p in pp}
    for p,q in combinations(pp,2):
        if len(N[p]&N[q])>1:return False
    for p,q,t in combinations(pp,3):
        c0=N[p]&N[q];c1=N[q]&N[t];c2=N[t]&N[p]
        if c0 and c1 and c2 and len({next(iter(c0)),next(iter(c1)),next(iter(c2))})==3:
            return False
    return True


def independent_four_source_edge_subset_census(point_slots,line_slots,index):
    """Original EDGE-first four-subset source Hall, no 4-slot permutations."""
    chosen_point=Counter(point_slots)
    chosen_line=Counter(line_slots)
    candidates=((p,l,identifier) for (p,l),identifier in index.items()
                if p in chosen_point and l in chosen_line)
    edges=tuple(candidates)
    accepted=set()
    for pick in combinations(edges,4):
        if (Counter(p for p,l,_ in pick)==chosen_point and
                Counter(l for p,l,_ in pick)==chosen_line):
            accepted.add(tuple(sorted(i for p,l,i in pick)))
    return accepted


def first_true_D_anchor(model):
    s,V,d,a,P,L,inc,np,nl=_actual_strict_original_transport(model)
    for i,(p,l) in enumerate(inc):
        for j in range(i+1,len(inc)):
            q,m=inc[j]
            if p!=q and l!=m and (set(P[p])&set(P[q])) and (set(L[l])&set(L[m])):
                return (i,j)
    raise AssertionError("true original source must have D anchor")


class GenuineOriginalFourSlotHallRigidity(unittest.TestCase):
    def test_01_all_h_149_over_2400_complete_global_source_port_bound(self):
        for h in range(1,81):
            s=1<<h
            z=all_h_complete_palette_port_four_slot_Hall_upper(s)
            a=z["a"];t=comb(a-3,3)
            self.assertEqual(z["full_Ka_per_side_A_port_template_count"],7*t)
            self.assertEqual(z["full_Ka_per_side_B_port_template_count"],3*t)
            self.assertEqual(z["new_ALL_typed_full_Ka_source_Hall_template_charge_upper"],
                             149*t*t)
            self.assertEqual(z["old_naive_parent_twentyfour_source_per_template_upper"],
                             2400*t*t)
            self.assertGreater(2400*t*t,16*149*t*t)
            self.assertTrue(z["old_genuine_original_AA_four_rook_at_most_two_from_pr512"])
            self.assertTrue(z["new_repeated_factor_source_Hall_unique_or_zero"])
            self.assertTrue(z["universally_positive_all_D_anchor_selected_seven_NOT_PROVED"])

    def test_02_all_short_cycle_FREE_local_original_source_matrices_and_edgefirst_four_Q(self):
        for tag,(ps,ls,expected_hist) in PROFILES.items():
            pp=len(set(ps));ll=len(set(ls))
            hist=Counter()
            for bitmask in range(1<<(pp*ll)):
                index={(i,j):i*ll+j for i in range(pp) for j in range(ll)
                       if (bitmask>>(i*ll+j))&1}
                if not independent_original_local_girth8(index):
                    continue
                expected=independent_four_source_edge_subset_census(ps,ls,index)
                actual=_four_slot_certificate(ps,ls,index,
                            independent_direct=False)
                self.assertEqual(set(actual["actual_source_four_incidence_ID_sets"]),
                                 expected)
                n=len(expected)
                cap=2 if tag=="A/A" else 1
                self.assertLessEqual(n,cap)
                den=(2 if "B"==tag.split("/")[0] else 1)*(
                    2 if "B"==tag.split("/")[1] else 1)
                self.assertEqual(actual["slot_permutation_orbit_denominator"],den)
                self.assertEqual(
                    actual["valid_source_permutations_with_DISTINCT_actual_incidence_IDs"],
                    den*n)
                hist[n]+=1
            self.assertEqual(dict(sorted(hist.items())),expected_hist)
            print("AA4AO exhaustive TRUE-GQ-local",tag,"hist",dict(hist))

    def test_03_full_true_W32_five_global_maps_PER_D_anchor_source_Hall_bounds(self):
        data=(("dual-zero",zero_split_original_W32(),277,736,(578,75,73,10),572,6),
              ("lex",fixture(1,"lex"),307,1504,(1077,213,193,21),987,90),
              ("reverse",fixture(1,"reverse"),300,986,(758,118,102,8),740,18),
              ("S68",fixture(1,"S68"),257,492,(413,27,50,2),413,0),
              ("S72",fixture(1,"S72"),261,599,(524,38,36,1),524,0))
        for name,model,D,total_H,expected_profiles,rejected_aa,aligned_D6_charge in data:
            anchors=original_D_pair_index(model)
            self.assertEqual(len(anchors),D)
            got=sum_exact=0
            kind=Counter()
            for e in sorted(anchors):
                cert=exact_true_original_D_anchor_slot_upper(
                    model,e,independent_all_templates=False)
                got+=cert["exact_true_original_Hall_source_six_ID_Q_extensions"]
                sum_exact+=cert["NEW_universal_true_original_port_template_Hall_charge_upper"]
                kind.update(cert["source_four_slot_class_Hall_charge"])
                self.assertLessEqual(
                    cert["exact_true_original_Hall_source_six_ID_Q_extensions"],
                    cert["NEW_universal_true_original_port_template_Hall_charge_upper"])
                self.assertEqual(
                    (cert["point_A_occupied_port_templates"],
                     cert["point_B_occupied_port_templates"],
                     cert["line_A_occupied_port_templates"],
                     cert["line_B_occupied_port_templates"]),
                    (7,3,7,3))
                self.assertEqual(
                    cert["NEW_universal_true_original_port_template_Hall_charge_upper"],149)
            self.assertEqual(got,total_H)
            self.assertEqual(sum_exact,149*D)
            self.assertEqual(
                tuple(kind[key] for key in ("A/A","A/B","B/A","B/B")),
                expected_profiles)
            self.assertEqual(kind["A/A"]-rejected_aa,aligned_D6_charge)
            self.assertEqual(aligned_D6_charge%6,0)
            # This ties per-port TRUE SOURCE Hall factor multiplicities
            # to historical AA4-AM true D6 anchor multiplicity k(Q)=6;
            # the non-AA Hall part is ALL seven-GF5 accepted.
            self.assertEqual(
                sum(kind[k] for k in ("A/B","B/A","B/B"))+
                aligned_D6_charge,total_H-rejected_aa)
            print("AA4AO real W32",name,"D",D,"source_H",got,
                  "new_uniform_Hall_upper",sum_exact,"Hall_profile",dict(kind))

    def test_04_strict_actual_W32_induced_C8_double_matching_witness(self):
        m=fixture(1,"lex")
        # AA4-AE #512's genuine actual induced C8 source-factor
        # witness uses these EIGHT true source factors, not fake
        # abstract binary source regularity.
        cases=(((1,2,5,12),(0,3,6,12)),
               ((0,3,6,12),(1,2,5,12)))
        valid=[]
        for ps,ls in cases:
            z=exact_true_original_four_slot_Hall_certificate(
                m,ps,ls,independent_direct=True)
            valid.append(z["exact_DISTINCT_true_original_four_incidence_Q_completions"])
        self.assertIn(2,valid)

    def test_05_actual_W34_W38_nononto_complete_global_port_source_oracles(self):
        for power in (2,3):
            for scheme in ("lex","random"):
                m=fixture(power,scheme)
                anchor=first_true_D_anchor(m)
                left=physical_D_pair_half_patterns(m,anchor,side=0)
                right=physical_D_pair_half_patterns(m,anchor,side=1)
                # Cover each A and B physical source multiplicity mode,
                # without materializing millions of two-side templates.
                P=left["globally_occupied_true_original_source_factor_patterns"]
                L=right["globally_occupied_true_original_source_factor_patterns"]
                def samples(items):
                    out=[]
                    for x in items:
                        if x[0] in ("P5","K2+C3") and not any(y[0] in (
                                "P5","K2+C3") for y in out):
                            out.append(x)
                        if x[0]=="P3+2K2" and not any(y[0]=="P3+2K2" for y in out):
                            out.append(x)
                        if len(out)==2:break
                    return out
                for lp in samples(P):
                    for rp in samples(L):
                        z=exact_true_original_four_slot_Hall_certificate(
                            m,lp[1],rp[1],pinned=anchor,independent_direct=True)
                        self.assertLessEqual(
                            z["exact_DISTINCT_true_original_four_incidence_Q_completions"],
                            z["new_GQ_repeated_source_factor_matching_rigidity_upper"])
                        self.assertIn(z["slot_permutation_orbit_denominator"],(1,2,4))

    def test_06_same_original_source_symplectic_and_independent_physical_relabels(self):
        m=zero_split_original_W32()
        D=first_true_D_anchor(m)
        old=exact_true_original_D_anchor_slot_upper(
            m,D,independent_all_templates=True)
        pt,ln=symplectic_transvection_source(m,2)
        a=m["a"]
        changed=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((v+3)%a for v in range(a)))
        inc=tuple(m["incidences"]);new_inc=tuple(changed["incidences"])
        new_index={t:i for i,t in enumerate(new_inc)}
        target=tuple(sorted(new_index[(pt[inc[j][0]],ln[inc[j][1]])] for j in D))
        new=exact_true_original_D_anchor_slot_upper(
            changed,target,independent_all_templates=True)
        for key in (
            "point_A_occupied_port_templates",
            "point_B_occupied_port_templates",
            "line_A_occupied_port_templates",
            "line_B_occupied_port_templates",
            "NEW_universal_true_original_port_template_Hall_charge_upper",
            "exact_true_original_Hall_source_six_ID_Q_extensions",
            "original_source_C8_double_match_template_count",
            "source_four_slot_class_Hall_charge"):
            self.assertEqual(old[key],new[key])

    def test_07_fake_source_C4_C6_repetition_and_duplicate_incidence_fail_closed(self):
        badC4={(0,0):0,(0,1):1,(1,0):2,(1,1):3}
        badC6={(0,0):0,(0,1):1,(1,1):2,(1,2):3,
               (2,2):4,(2,0):5,(3,3):6}
        with self.assertRaises(ValueError):
            _four_slot_certificate((0,1,2,3),(0,1,2,3),badC4)
        with self.assertRaises(ValueError):
            _four_slot_certificate((0,1,2,3),(0,1,2,3),badC6)
        with self.assertRaises(ValueError):
            _four_slot_certificate((0,0,0,1),(0,1,2,3),{})
        with self.assertRaises(ValueError):
            exact_true_original_four_slot_Hall_certificate(
                dict(fixture(1,"lex"),right_labels=((0,1),)*15),
                (0,1,2,3),(0,1,2,3))
        with self.assertRaises(ValueError):
            exact_true_original_four_slot_Hall_certificate(
                dict(fixture(1,"lex"),incidences=tuple(
                    fixture(1,"lex")["incidences"])[:-1]),
                (0,1,2,3),(0,1,2,3))


if __name__=="__main__":unittest.main()
