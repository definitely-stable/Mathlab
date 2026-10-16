"""Strict genuine ORIGINAL D6 source-path all-h and independent tests."""
import unittest
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports,exact_original_D_pair_six_Q_funnel)
from hyp105_issue230_d6aa4ap_unique_original_D6_path_kernel import (
    occupied_oriented_original_P5_paths,
    true_original_D6_direct_path_kernel,
    independent_D6_physical_pairs,
    true_original_W32_all_D6_source_path_census,
    all_h_original_D6_unique_source_path_upper)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independently_get_original_D_pair(model):
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    for i,(p,l) in enumerate(inc):
        for j in range(i+1,len(inc)):
            q,m=inc[j]
            if p!=q and l!=m and set(f[p])&set(f[q]) and set(g[l])&set(g[m]):
                return (i,j)
    raise AssertionError("genuine original source has no D pair")


def independent_direct_original_P5xP5_for_subset(model,pair,count):
    """Physical-template-MAJOR independent true-original flags with
    specified FIRST count of actual point physical paths.
    Do NOT call source d4 path-neighbor algorithm."""
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    ports=true_original_D_physical_ports(inc,f,g,pair)
    P=list(occupied_oriented_original_P5_paths(ports[0],f,a))[:count]
    L=occupied_oriented_original_P5_paths(ports[1],g,a)
    index={tuple(flag):i for i,flag in enumerate(inc)}
    sets=set()
    for point in P:
        for line in L:
            ids=tuple(index.get((p,l)) for p,l in zip(point,line))
            if None in ids:continue
            if len(set(ids))!=4 or set(ids)&set(pair):
                raise AssertionError("original source flags must be six distinct")
            six=tuple(sorted(tuple(pair)+ids))
            if six in sets:raise AssertionError("duplicate true source physical P5")
            sets.add(six)
    return sets


class GenuineOriginalAlignedD6UniqueSourceFourPath(unittest.TestCase):
    def test_01_every_dyadic_all_h_unique_path_capacity_not_GF5_positive(self):
        for h in range(1,81):
            s=1<<h
            z=all_h_original_D6_unique_source_path_upper(s)
            a=z["a"]; d=s+1
            n=6*comb(a-3,3)
            self.assertEqual(z["full_Ka_P5_per_typed_side"],n)
            self.assertEqual(z["full_Ka_physical_P5xP5_template_capacity"],n*n)
            self.assertEqual(z["true_original_source_neighbor_cap_per_D_anchor"],
                             min(n*n,n*d**4))
            self.assertTrue(z["aligned_original_D6_at_most_ONE_per_occupied_physical_P5xP5"])
            self.assertTrue(z["non_P5_template_cannot_be_D6"])
            self.assertTrue(z["no_root_issue230_A_B_C_proof"])

    def test_02_true_W32_all_five_global_maps_full_D_FIRST_and_historical_Q_FIRST(self):
        schemes=[("zero",zero_split_original_W32(),277,6,1),
                 ("lex",fixture(1,"lex"),307,90,15),
                 ("reverse",fixture(1,"reverse"),300,18,3),
                 ("S68",fixture(1,"S68"),257,0,0),
                 ("S72",fixture(1,"S72"),261,0,0)]
        for name,m,expected_D,expected_charge,expected_Q in schemes:
            z=true_original_W32_all_D6_source_path_census(
                m,independent_physical=True,historical_Q_first=True)
            self.assertEqual(
                (z["actual_original_D_pairs"],
                 z["exact_D6_true_original_D_anchor_charge"],
                 z["exact_D6_unique_true_original_six_Q"]),
                (expected_D,expected_charge,expected_Q))
            self.assertEqual(
                sum(z["D_anchor_D6_charge_histogram"].values()),
                expected_D)
            print("AA4AP TRUE ORIGINAL W32",name,"D",expected_D,
                  "D6 charge",expected_charge,"unique",expected_Q,
                  "D6 positive anchors",z["D_anchor_with_positive_D6_extensions"])

    def test_03_original_W32_same_real_D_anchor_point_first_line_first_physical_and_parent_seven(self):
        for name,m in [("zero",zero_split_original_W32()),
                       ("lex",fixture(1,"lex")),("reverse",fixture(1,"reverse")),
                       ("S68",fixture(1,"S68")),("S72",fixture(1,"S72"))]:
            D=original_D_pair_index(m)
            for i,anchor in enumerate(sorted(D)):
                if i%11:continue
                point=true_original_D6_direct_path_kernel(
                    m,anchor,direction="point",include_Q=True)
                line=true_original_D6_direct_path_kernel(
                    m,anchor,direction="line",include_Q=True)
                physical=independent_D6_physical_pairs(m,anchor)
                q=point["accepted_true_original_D6_six_incidence_Q"]
                self.assertEqual(q,line["accepted_true_original_D6_six_incidence_Q"])
                self.assertEqual(q,physical["original_D6_six_Q"])
                self.assertEqual(point["point_occupied_original_P5_paths"],6)
                self.assertEqual(point["line_occupied_original_P5_paths"],6)
                self.assertEqual(point["physically_occupied_P5xP5_template_pairs"],36)
                parent=exact_original_D_pair_six_Q_funnel(
                    m,anchor,retain_selected=True)
                accepted={Q for Q,tag in parent[
                    "selected_ORIGINAL_six_incidence_ID_Q_tags"].items()
                          if tag=="D6"}
                self.assertEqual(set(q),accepted)
                self.assertLessEqual(len(q),36)

    def test_04_true_W34_global_partial_K14_two_independent_FULL_algorithms(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
            self.assertEqual((a,comb(a,2)-V),(14,6))
            D=sorted(original_D_pair_index(m))
            self.assertTrue(D)
            for anchor in (D[0],D[min(7,len(D)-1)]):
                point=true_original_D6_direct_path_kernel(
                    m,anchor,direction="point",include_Q=True)
                line=true_original_D6_direct_path_kernel(
                    m,anchor,direction="line",include_Q=True)
                brute=independent_D6_physical_pairs(m,anchor)
                self.assertEqual(
                    point["accepted_true_original_D6_six_incidence_Q"],
                    line["accepted_true_original_D6_six_incidence_Q"])
                self.assertEqual(
                    point["accepted_true_original_D6_six_incidence_Q"],
                    brute["original_D6_six_Q"])
                self.assertLessEqual(
                    point["accepted_original_D6_D_anchor_charge"],
                    point["all_h_complete_D6_4neighbor_source_upper"])

    def test_05_true_W38_nononto_K35_partial_EXPLICIT_sampled_path_oracle(self):
        for scheme in ("lex","random"):
            m=fixture(3,scheme)
            s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(m)
            self.assertEqual((a,comb(a,2)-V),(35,10))
            anchor=independently_get_original_D_pair(m)
            sample=true_original_D6_direct_path_kernel(
                m,anchor,direction="point",include_Q=True,
                max_first_paths=12)
            direct=independent_direct_original_P5xP5_for_subset(
                m,anchor,12)
            self.assertTrue(sample["partial_source_first_paths_only"])
            self.assertEqual(
                set(sample["accepted_true_original_D6_six_incidence_Q"]),
                direct)
            self.assertEqual(sample["first_typed_original_P5_paths_examined"],12)
            self.assertGreater(sample["point_occupied_original_P5_paths"],12)
            self.assertLessEqual(len(direct),12*(s+1)**4)

    def test_06_true_W32_original_symplectic_source_automorphism_and_independent_physical_perms(self):
        m=fixture(1,"lex")
        before=true_original_W32_all_D6_source_path_census(
            m,independent_physical=True,historical_Q_first=False)
        pt,ln=symplectic_transvection_source(m,2)
        a=m["a"]
        changed=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((v+2)%a for v in range(a)))
        after=true_original_W32_all_D6_source_path_census(
            changed,independent_physical=True,historical_Q_first=False)
        for field in (
            "actual_original_D_pairs","exact_D6_true_original_D_anchor_charge",
            "exact_D6_unique_true_original_six_Q",
            "D_anchor_with_positive_D6_extensions",
            "D_anchor_D6_charge_histogram"):
            self.assertEqual(before[field],after[field])

    def test_07_fail_closed_invalid_source_and_injected_physical_anchor(self):
        m=fixture(1,"lex")
        anchor=independently_get_original_D_pair(m)
        with self.assertRaises(ValueError):
            true_original_D6_direct_path_kernel(m,anchor,direction="both")
        with self.assertRaises(ValueError):
            true_original_D6_direct_path_kernel(m,anchor,
                                                  max_first_paths=0)
        with self.assertRaises(ValueError):
            occupied_oriented_original_P5_paths((0,1,1),m["left_labels"],6)
        for bad in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=tuple(m["incidences"])[:-1])):
            with self.assertRaises(ValueError):
                true_original_D6_direct_path_kernel(bad,anchor)
        with self.assertRaises(ValueError):
            true_original_W32_all_D6_source_path_census(fixture(2,"lex"))
        with self.assertRaises(ValueError):
            all_h_original_D6_unique_source_path_upper(12)


if __name__=="__main__":unittest.main()
