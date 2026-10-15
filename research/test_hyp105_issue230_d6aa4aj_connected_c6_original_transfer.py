"""AA4-AJ: true-original exact connected-C6 completion, two separate oracles."""
import unittest
from collections import Counter
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
    exact_original_connected_C6_transfer,sector_shapes_by_literal_edges,
    sparse_true_original_C6_upper_bound)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,single_original_A_sector_permanent,
    full_original_W32_sector_certificate,classify_physical_A_twofactor)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    pinned_twofactor_completions)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import _source_cohort
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    transform_model,symplectic_transvection_source)


def independent_literal_single_C6(model,side,root,pair_offset,four):
    """Separate complete source-permanent/H enumeration, no AJ shortcuts."""
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    true=Counter()
    physical=Counter()
    if set(pins[0])&set(pins[1]):
        # AJ is the exact DISJOINT-pinned physical C6 transfer.
        # Adjacent pinned physical C6 are genuine and counted by AI,
        # but outside the mathematical domain of this AJ channel.
        return dict(true),dict(physical)
    for H in pinned_twofactor_completions(*pins,a):
        if classify_physical_A_twofactor(H,pins)!="connected_C6":
            continue
        rest=tuple(e for e in H if e not in pins)
        if any(e not in inv for e in rest):continue
        tag=sector_shapes_by_literal_edges(H,pins)
        physical[tag]+=1
        opposite=tuple(inv[e] for e in rest)
        for perm in permutations(opposite):
            if all(perm[i] in neighbors[four[i]] for i in range(4)):
                true[tag]+=1
    return dict(true),dict(physical)


class ConnectedC6OriginalTrueGQ(unittest.TestCase):
    def test_01_physical_complete_K6_K7_K8_disjoint_pair_2plus4(self):
        for a in (6,7,8):
            E=tuple(combinations(range(a),2))
            for e0,e1 in combinations(E,2):
                if set(e0)&set(e1):continue
                count=Counter()
                Hs=set()
                for H in pinned_twofactor_completions(e0,e1,a):
                    if classify_physical_A_twofactor(H,(e0,e1))=="connected_C6":
                        tag=sector_shapes_by_literal_edges(H,(e0,e1))
                        count[tag]+=1
                        self.assertNotIn(frozenset(H),Hs)
                        Hs.add(frozenset(H))
                self.assertEqual(count["two_cross_spoke"],2*(a-4)*(a-5))
                self.assertEqual(count["internal_aux_link"],4*(a-4)*(a-5))
                self.assertEqual(sum(count.values()),6*(a-4)*(a-5))

    def test_02_all_original_W32_labels_both_types_every_actual_rootpair_and_C4(self):
        maps=[zero_split_original_W32()]+[
            fixture(1,scheme) for scheme in ("lex","reverse","S68","S72")]
        for m in maps:
            for side in (0,1):
                total=physical=0
                for root in range(15):
                    for off in range(3):
                        for four in occupied_root_C4_source_factors(m,side=side,root=root):
                            fast=exact_original_connected_C6_transfer(
                                m,side=side,root=root,pair_offset=off,four=four)
                            brute,occ=independent_literal_single_C6(
                                m,side,root,off,four)
                            self.assertEqual(
                                fast["two_cross_spoke_accepted_original_Q"],
                                brute.get("two_cross_spoke",0))
                            self.assertEqual(
                                fast["internal_aux_link_accepted_original_Q"],
                                brute.get("internal_aux_link",0))
                            self.assertEqual(
                                fast["two_cross_spoke_occupied_physical_H"],
                                occ.get("two_cross_spoke",0))
                            self.assertEqual(
                                fast["internal_aux_link_occupied_physical_H"],
                                occ.get("internal_aux_link",0))
                            self.assertEqual(fast["accepted_original_connected_C6_Q"],
                                             sum(brute.values()))
                            total+=fast["accepted_original_connected_C6_Q"]
                            physical+=fast["occupied_physical_connected_C6_H"]
                old=full_original_W32_sector_certificate(m,side=side)
                self.assertLessEqual(total,old["original_GF5_A_accepted_by_sector"]["connected_C6"])
                self.assertLessEqual(physical,
                                     old["occupied_opposite_A_physical_H_by_sector"]["connected_C6"])
                self.assertGreaterEqual(total,0)
                if m is maps[0]:
                    self.assertEqual(total,(17,41)[side])
                    self.assertEqual(physical,(504,756)[side])
                print("AA4AJ_W32_DISJOINT_C6",m["s"],side,total,physical,
                      "full_adjacent_plus_disjoint",
                      old["original_GF5_A_accepted_by_sector"]["connected_C6"])

    def test_03_W34_real_original_partial_K14_occupancy_and_holes(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            self.assertEqual(m["a"],14)
            self.assertEqual(comb(14,2)-len(m["right_labels"]),6)
            for side in (0,1):
                for root,off in ((0,0),(1,1),(5,2)):
                    for four in occupied_root_C4_source_factors(
                            m,side=side,root=root)[:3]:
                        z=exact_original_connected_C6_transfer(
                            m,side=side,root=root,pair_offset=off,four=four)
                        brute,physical=independent_literal_single_C6(m,side,root,off,four)
                        self.assertEqual(z["two_cross_spoke_accepted_original_Q"],
                                         brute.get("two_cross_spoke",0))
                        self.assertEqual(z["internal_aux_link_accepted_original_Q"],
                                         brute.get("internal_aux_link",0))
                        self.assertEqual(z["occupied_physical_connected_C6_H"],
                                         sum(physical.values()))
                        old=single_original_A_sector_permanent(
                            m,side=side,root=root,pair_offset=off,four=four)
                        if z["pinned_physical_disjoint"]:
                            self.assertEqual(z["accepted_original_connected_C6_Q"],
                                             old["accepted"]["connected_C6"])
                            self.assertEqual(z["occupied_physical_connected_C6_H"],
                                             old["occupied_physical_H"]["connected_C6"])
                        else:
                            # Actual adjacent physical pinned A/C6 is
                            # genuine, but outside AJ's disjoint domain.
                            self.assertEqual(z["accepted_original_connected_C6_Q"],0)
                            self.assertEqual(z["occupied_physical_connected_C6_H"],0)

    def test_04_symplectic_actual_source_and_independent_physical_relabels(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        for side in (0,1):
            orig=full_original_W32_sector_certificate(m,side=side)
            transformed=full_original_W32_sector_certificate(changed,side=side)
            self.assertEqual(orig["original_GF5_A_accepted_by_sector"],
                             transformed["original_GF5_A_accepted_by_sector"])
            # AJ counts only DISJOINT-pinned C6, a strict subfamily
            # of the full connected-C6 physical A sector of AA4-AI.
            totals=[]
            for model in (m,changed):
                total=0
                for root in range(15):
                    for off in range(3):
                        for four in occupied_root_C4_source_factors(
                                model,side=side,root=root):
                            z=exact_original_connected_C6_transfer(
                                model,side=side,root=root,pair_offset=off,four=four)
                            total+=z["accepted_original_connected_C6_Q"]
                totals.append(total)
            self.assertEqual(totals[0],totals[1])
            self.assertGreater(totals[0],0)
            self.assertLessEqual(totals[0],(40,58)[side])

    def test_05_all_h_source_degree_bound_and_finite_rooted_slices(self):
        for h in (1,2,3,8,19,25):
            s=1<<h
            z=sparse_true_original_C6_upper_bound(s)
            self.assertEqual(z["two_cross_spoke_upper"],48*(s+1)**2)
            self.assertEqual(z["internal_aux_link_upper"],192*(s+1))
            self.assertEqual(z["connected_C6_upper"],
                             48*(s+1)**2+192*(s+1))
        for scheme in ("random","lex"):
            m=fixture(2,scheme)
            cap=sparse_true_original_C6_upper_bound(m["s"])
            for side in (0,1):
                four=occupied_root_C4_source_factors(m,side=side,root=0)[0]
                for off in range(3):
                    z=exact_original_connected_C6_transfer(
                        m,side=side,root=0,pair_offset=off,four=four)
                    self.assertLessEqual(z["two_cross_spoke_accepted_original_Q"],
                                         cap["two_cross_spoke_upper"])
                    self.assertLessEqual(z["internal_aux_link_accepted_original_Q"],
                                         cap["internal_aux_link_upper"])

    def test_06_reject_fabricated_original_factors_and_bad_physical_patterns(self):
        m=zero_split_original_W32()
        for kwargs in (dict(),dict(side=2),dict(root=15),
                       dict(pair_offset=3),dict(four=(0,1,2,3))):
            with self.assertRaises(ValueError):
                exact_original_connected_C6_transfer(m,**kwargs)
        e0,e1=(0,1),(2,3)
        with self.assertRaises(ValueError):
            sector_shapes_by_literal_edges((e0,e1), (e0,e1))
        with self.assertRaises(ValueError):
            sector_shapes_by_literal_edges(((0,1),(1,2)),((0,1),(1,2)))
        with self.assertRaises(ValueError):
            sparse_true_original_C6_upper_bound(3)
        with self.assertRaises(ValueError):
            exact_original_connected_C6_transfer(
                dict(m,right_labels=((0,1),)*15),four=(1,2,3,4))


if __name__=="__main__":
    unittest.main()
