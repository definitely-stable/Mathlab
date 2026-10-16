"""AA4-AS: literal original W32/w34 threeflag->three-extra Hall seven-GF5."""
import unittest
from collections import Counter,defaultdict
from itertools import combinations

from hyp105_issue230_d6aa4as_threeflag_hall_frontier import (
    all_h_threeflag_physical_completion_formula,
    original_opposite_wedge_context,prepare_original_opposite_wedge,
    _threeflag_residuals,independent_physical_threeflag_degree_oracle,
    exact_original_opposite_threeflag_six_Q_funnel)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    exact_original_rainbow_D6_cycle_transfer)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independently_all_good_opposite_original_wedges(ctx):
    """Source-center-first two actual neighbor edge scans, no Hall/complete Q."""
    result=set()
    for center,row in enumerate(ctx["good_neighbors"]):
        for a,b in combinations(row,2):
            i,pc,lc=a;k,pd,ld=b
            if pc==pd or lc==ld:
                continue
            result.add((center,)+tuple(sorted((i,k))))
    return tuple(sorted(result))


def independently_original_seven_Q_wedge_membership(ctx,selected):
    """TRUE Q-FIRST independent original six-ID membership oracle."""
    good=ctx["GOOD"]
    colors=ctx["G"]["edge_colors"]
    target=defaultdict(dict)
    for Q,tag in selected.items():
        for center in Q:
            for i,k in combinations(sorted(j for j in Q if j!=center),2):
                e1=tuple(sorted((center,i)))
                e2=tuple(sorted((center,k)))
                if e1 not in good or e2 not in good:
                    continue
                pc,lc=colors[e1]
                pd,ld=colors[e2]
                if pc==pd or lc==ld:
                    raise AssertionError("selected genuine ORIGINAL six-Q GOOD wedge not two-typed opposite")
                target[(center,i,k)][Q]=tag
    return target


class OriginalThreeFlagHall(unittest.TestCase):
    def test_01_exact_all_h_T_P_formal_residual_numbers(self):
        for h in (1,2,3,4,7,12,14,24,35,60):
            s=1<<h
            z=all_h_threeflag_physical_completion_formula(s)
            a=z["a"]
            self.assertEqual(z["triangle_T_three_new_coordinate_templates"],
                             (a-3)*(a-4)*(a-5)//6)
            self.assertEqual(z["path_P_two_new_coordinate_templates"],
                             3*(a-4)*(a-5)//2)
            self.assertEqual(z["path_P_A_sixcycle_templates"],
                             (a-4)*(a-5))
            self.assertEqual(z["path_P_B_doubled_source_factor_templates"],
                             (a-4)*(a-5)//2)
            self.assertTrue(z["triangle_triangle_ALL_h_no_positive_original_GF5"])
            self.assertTrue(z["physical_completion_not_actual_original_source_Hall_lower"])
        for bad in (0,True,-2,3):
            with self.assertRaises(ValueError):
                all_h_threeflag_physical_completion_formula(bad)

    def test_02_independent_triple_multigraph_K6_K7_K8_T_P_10_new_coordinate(self):
        triangle=dict(kind="T",physical_original_threefactor_edges=(
            (0,1),(0,2),(1,2)),
            pinned_physical_coordinates=(0,1,2),free_ports=(2,2))
        path=dict(kind="P",physical_original_threefactor_edges=(
            (0,1),(0,2),(1,3)),
            pinned_physical_coordinates=(0,1,2,3),free_ports=(2,3))
        for a in (6,7,8):
            for kind,ports in (("T",triangle),("P",path)):
                construction=list(_threeflag_residuals(ports,a))
                concrete={edges for tag,edges in construction}
                brute=independent_physical_threeflag_degree_oracle(a,ports)
                self.assertEqual(concrete,brute)
                self.assertEqual(len(concrete),len(construction))
                target=(len(list(combinations(range(a-3),3))) if kind=="T"
                        else 3*len(list(combinations(range(a-4),2))))
                self.assertEqual(len(concrete),target)
                if kind=="P":
                    tags=Counter(x for x,_ in construction)
                    self.assertEqual(tags["P_A_sixcycle"],
                                     2*len(list(combinations(range(a-4),2))))
                    self.assertEqual(tags["P_B_C4_plus_double"],
                                     len(list(combinations(range(a-4),2))))

    def test_03_all_five_complete_genuine_original_W32_wedges_Q_FIRST_match(self):
        expected_R={"dual_zero":870,"lex":1105,"reverse":1013,
                    "S68":697,"S72":750}
        expected_charge={"dual_zero":40,"lex":237,"reverse":68,
                         "S68":6,"S72":11}
        for scheme,m in [("dual_zero",zero_split_original_W32())]+[
             (s,fixture(1,s)) for s in ("lex","reverse","S68","S72")]:
            ctx=original_opposite_wedge_context(m)
            truth=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
            target=independently_original_seven_Q_wedge_membership(ctx,truth)
            wedges=independently_all_good_opposite_original_wedges(ctx)
            self.assertEqual(len(wedges),expected_R[scheme])
            self.assertTrue(set(target).issubset(wedges))
            tag_charge=Counter()
            by_typed_shape=Counter()
            Hall=reject=physical_pairs=0
            for wedge in wedges:
                z=exact_original_opposite_threeflag_six_Q_funnel(
                    m,wedge,context=ctx,require_good=True)
                self.assertEqual(z["selected_true_original_six_incidence_ID_Q_tags"],
                                 target.get(wedge,{}))
                shape=(z["point_physical_wedge_kind"],z["line_physical_wedge_kind"])
                by_typed_shape[shape]+=1
                formal=[1 if k=="T" else 3 for k in shape]
                self.assertEqual(sum(z["point_formal_threefactor_patterns"].values()),formal[0])
                self.assertEqual(sum(z["line_formal_threefactor_patterns"].values()),formal[1])
                self.assertEqual(z["physical_two_side_occupied_pattern_pairs"],
                                 formal[0]*formal[1])
                self.assertEqual(
                    z["genuine_original_both_leafless_three_additional_flag_Hall_Q_count"],
                    z["genuine_original_unaligned_AA_rejected_Q_count"]+
                    z["genuine_original_positive_selected_seven_GF5_six_Q_count"])
                if shape==("T","T"):
                    self.assertEqual(z["genuine_original_positive_selected_seven_GF5_six_Q_count"],0)
                tag_charge.update(z["genuine_original_seven_tag_histogram"])
                Hall+=z["genuine_original_both_leafless_three_additional_flag_Hall_Q_count"]
                reject+=z["genuine_original_unaligned_AA_rejected_Q_count"]
                physical_pairs+=z["physical_two_side_occupied_pattern_pairs"]
            self.assertEqual(sum(tag_charge.values()),expected_charge[scheme])
            self.assertEqual(sum(len(x) for x in target.values()),expected_charge[scheme])
            self.assertEqual(tag_charge["B/B-disjoint"],0)
            self.assertEqual(tag_charge["C/A"],0)
            self.assertEqual(tag_charge["C/B"],0)
            print("AA4AS_TRUE_W32",scheme,"REAL_good_opposite_wedges",len(wedges),
                  "typed_shape_counts",dict(sorted(by_typed_shape.items())),
                  "physically_occupied_two_sided_template_pairs",physical_pairs,
                  "true_original_Hall_six_Q_wedge_charge",Hall,
                  "original_AA_unaligned_rejection_charge",reject,
                  "original_selected_seven_six_Q_wedge_charge",sum(tag_charge.values()),
                  "positive_seven_tag_wedge_charge",dict(tag_charge))

    def test_04_real_original_W34_positive_D6_wedge_source_Hall_membership(self):
        # No synthetic W34 full seven-GF5 census; only genuine
        # source verified independent AA4-AQ D6 witnesses.
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            sample=exact_original_rainbow_D6_cycle_transfer(
                m,roots=(0,1,2),max_rainbow_sixcycles=1)
            self.assertEqual(sample["double_rainbow_D6_original_Q_count"],1)
            ctx=original_opposite_wedge_context(m)
            Q,cycle=next(iter(sample["exact_true_original_six_ID_D6_Q_to_unique_cycle"].items()))
            wedge=(cycle[0],)+tuple(sorted((cycle[1],cycle[-1])))
            z=exact_original_opposite_threeflag_six_Q_funnel(
                m,wedge,context=ctx)
            self.assertEqual((z["point_physical_wedge_kind"],
                              z["line_physical_wedge_kind"]),("P","P"))
            self.assertEqual(sum(z["point_formal_threefactor_patterns"].values()),135)
            self.assertEqual(sum(z["line_formal_threefactor_patterns"].values()),135)
            self.assertEqual(z["selected_true_original_six_incidence_ID_Q_tags"][Q],"D6")
            self.assertGreaterEqual(z["genuine_original_positive_selected_seven_GF5_six_Q_count"],1)
            print("AA4AS_TRUE_W34_PARTIAL",scheme,"wedge",wedge,
                  "positive_source_D6_original_six_Q",Q,
                  "original_Hall_matching_count",z[
                    "genuine_original_both_leafless_three_additional_flag_Hall_Q_count"],
                  "globally_occupied_physical_double_templates",z[
                    "physical_two_side_occupied_pattern_pairs"])

    def test_05_true_source_symplectic_and_independently_typed_physical_relabel(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        profiles=[]
        for model in (m,changed):
            ctx=original_opposite_wedge_context(model)
            shape=Counter()
            for w in independently_all_good_opposite_original_wedges(ctx):
                x=prepare_original_opposite_wedge(ctx,w,require_good=True)
                shape[(x[0]["kind"],x[1]["kind"])]+=1
            profiles.append(shape)
        self.assertEqual(profiles[0],profiles[1])

    def test_06_strict_real_original_source_and_non_opposite_bad_wedges(self):
        m=zero_split_original_W32()
        ctx=original_opposite_wedge_context(m)
        good_wedges=independently_all_good_opposite_original_wedges(ctx)
        self.assertTrue(good_wedges)
        with self.assertRaises(ValueError):
            prepare_original_opposite_wedge(ctx,(-1,0,1))
        with self.assertRaises(ValueError):
            prepare_original_opposite_wedge(ctx,(0,1,1))
        with self.assertRaises(ValueError):
            prepare_original_opposite_wedge(ctx,(0,3,2))
        found=False
        for center,row in enumerate(ctx["good_neighbors"]):
            for a,b in combinations(row,2):
                if a[1]==b[1] or a[2]==b[2]:
                    w=(center,)+tuple(sorted((a[0],b[0])))
                    with self.assertRaises(ValueError):
                        prepare_original_opposite_wedge(ctx,w)
                    found=True
                    break
            if found:break
        self.assertTrue(found)
        for corrupted in (dict(m,left_labels=((0,1),)*15),
                          dict(m,right_labels=((0,1),)*15),
                          dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                original_opposite_wedge_context(corrupted)


if __name__=="__main__":
    unittest.main()
