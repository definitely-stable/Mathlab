"""AA4-AU independent original source polynomial, forest & triple motif census."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4au_source_triple_hall_polynomials import (
    all_h_original_threeflag_source_motif_population,
    exact_original_threeflag_Hall_incidence_polynomial,
    literal_true_original_W32_source_threeflag_motif_census,
    literal_true_original_source_BB_P4_audit,
    literal_true_original_source_AB_audit)
from hyp105_issue230_d6aa4at_original_forest_unique_hall import (
    unique_original_threeflag_forest_Hall)
from hyp105_issue230_d6aa4as_threeflag_hall_frontier import (
    original_opposite_wedge_context,prepare_original_opposite_wedge,
    occupied_original_threeflag_half,_original_threeflag_Hall_completions)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    exact_original_rainbow_D6_cycle_transfer)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def literal_good_opposite(ctx):
    for center,row in enumerate(ctx["good_neighbors"]):
        for a,b in combinations(row,2):
            i,cp,cl=a;k,pd,ld=b
            if cp!=pd and cl!=ld:
                yield (center,)+tuple(sorted((i,k)))


def whole_original_model_polynomial_table(model,*,all_wedges=True,
                                          select_wedge=None):
    """Literal source-pair first, compare explicit Hall polynomial and forest."""
    ctx=original_opposite_wedge_context(model)
    index={e:i for i,e in enumerate(ctx["inc"])}
    wedges=tuple(literal_good_opposite(ctx)) if all_wedges else (select_wedge,)
    table=Counter()
    total=0
    for wedge in wedges:
        ports=prepare_original_opposite_wedge(ctx,wedge,
                                              require_good=all_wedges)
        halves=[occupied_original_threeflag_half(
            ports[i],ctx["a"],ctx["inverses"][i])[0] for i in (0,1)]
        for f in halves[0]:
            for g in halves[1]:
                shape=("B" if "_B_" in f[0] else "A")+"/"+(
                       "B" if "_B_" in g[0] else "A")
                z=exact_original_threeflag_Hall_incidence_polynomial(
                    index,wedge,f,g)
                old=unique_original_threeflag_forest_Hall(index,wedge,f,g)
                legacy=_original_threeflag_Hall_completions(index,wedge,f,g)
                self_witness=z["exact_original_six_DISTINCT_flag_ID_Q"]
                if (self_witness!=old or legacy!=(
                        set() if old is None else {old})):
                    raise AssertionError("three independent original source 3x3 Hall methods disagree")
                if z["original_source_residual_pattern"]!=shape:
                    raise AssertionError("original type A/B classification mismatch globally mapped physical 3-factor source multiplicities")
                table[(shape,"YES" if old is not None else "NO")]+=1
                total+=1
    return ctx,wedges,table,total


class OriginalSourcePolynomialAndTripleMotifs(unittest.TestCase):
    def test_01_all_h_closed_source_threeflag_census_and_positive_BB_s6(self):
        known={
            2:{"A/A":10560,"A/B":1710,"B/A":1710,"B/B":180,"A/C":15,"C/A":15},
            4:{"A/A":11995200,"A/B":350200,"B/A":350200,"B/B":6800,"A/C":850,"C/A":850},
        }
        for h in list(range(1,33))+[35,40,50,60]:
            s=1<<h
            x=all_h_original_threeflag_source_motif_population(s)
            d=s+1;N=x["N_original_incidence_flags"];V=x["V"]
            counts=x["three_DISTINCT_original_source_flag_ID_type_counts"]
            self.assertEqual(counts["B/B"],N*s*s)
            self.assertGreaterEqual(counts["B/B"],s**6)
            self.assertEqual(counts["A/B"],V*(d*(d-1)//2)*(N-3*d+2))
            self.assertEqual(counts["C/A"],V*(d*(d-1)*(d-2)//6))
            self.assertEqual(sum(counts.values()),N*(N-1)*(N-2)//6)
            self.assertTrue(x["original_BB_physically_two_typed_opposite_NOT_PROVED"])
            self.assertTrue(x["original_BB_selected_seven_GF5_NOT_PROVED"])
            if s in known:self.assertEqual(counts,known[s])
        for bad in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_original_threeflag_source_motif_population(bad)

    def test_02_independent_toy_four_pattern_incidence_polynomial_vs_forest(self):
        examples=[
            ("A/A",{(0,0):10,(1,1):11,(2,2):12},(0,1,2),(0,1,2)),
            ("A/B",{(0,0):10,(1,0):11,(2,1):12},(0,1,2),(0,0,1)),
            ("B/A",{(0,0):10,(0,1):11,(1,2):12},(0,0,1),(0,1,2)),
            ("B/B",{(0,0):10,(0,1):11,(1,0):12},(0,0,1),(0,0,1)),
        ]
        for shape,index,p,l in examples:
            first=("A",p,())
            second=("A",l,())
            z=exact_original_threeflag_Hall_incidence_polynomial(
                index,(0,1,2),first,second)
            w=unique_original_threeflag_forest_Hall(index,(0,1,2),
                                                     first,second)
            self.assertEqual(z["original_source_residual_pattern"],shape)
            self.assertEqual(z["exact_source_incidence_polynomial_value"],1)
            self.assertEqual(z["exact_original_six_DISTINCT_flag_ID_Q"],w)
            self.assertEqual(w,(0,1,2,10,11,12))
            # Removing one actual required original flag kills the
            # unique source b-matching in this toy forest.
            for e in index:
                reduced={edge:i for edge,i in index.items() if edge!=e}
                z2=exact_original_threeflag_Hall_incidence_polynomial(
                    reduced,(0,1,2),first,second)
                self.assertEqual(z2["exact_source_incidence_polynomial_value"],0)
        C4={(0,0):10,(0,1):11,(1,0):12,(1,1):13,(2,2):14}
        C6={(0,0):10,(0,1):11,(1,1):12,(1,2):13,
            (2,2):14,(2,0):15}
        for fake in (C4,C6):
            with self.assertRaisesRegex(ValueError,"not a genuine W"):
                exact_original_threeflag_Hall_incidence_polynomial(
                    fake,(0,1,2),("A",(0,1,2),()),("A",(0,1,2),()))
        for invalid in (((0,1), (0,1,2)),((0,0,0),(0,1,2))):
            with self.assertRaises(ValueError):
                exact_original_threeflag_Hall_incidence_polynomial(
                    {(0,0):10},(0,1,2),("A",invalid[0],()),
                    ("A",invalid[1],()))

    def test_03_all_five_true_original_W32_all_occupied_global_physical_pairs(self):
        known={
            "dual_zero":(870,5328,150),
            "lex":(1105,7233,505),
            "reverse":(1013,6351,232),
            "S68":(697,4041,46),
            "S72":(750,4386,85),
        }
        # Freeze exact actual original W32 source Hall pattern successes
        # from separate forest AND 3! source reference, not physical-only
        # residual template occupation. A/A, A/B, B/A, B/B respectively.
        known_four_boolean_Hall={
            "dual_zero":(116,14,17,3),
            "lex":(358,75,70,2),
            "reverse":(182,28,22,0),
            "S68":(40,2,4,0),
            "S72":(74,6,5,0),
        }
        for name,m in [("dual_zero",zero_split_original_W32())]+[
            (k,fixture(1,k)) for k in ("lex","reverse","S68","S72")]:
            ctx,wedges,tbl,total=whole_original_model_polynomial_table(m)
            self.assertEqual((len(wedges),total,
                              sum(n for (t,outcome),n in tbl.items()
                                  if outcome=="YES")),known[name])
            self.assertEqual(tuple(tbl[(label,"YES")] for label in
                         ("A/A","A/B","B/A","B/B")),
                         known_four_boolean_Hall[name])
            for label in ("A/A","A/B","B/A","B/B"):
                self.assertGreater(tbl[(label,"NO")],0)
            print("AA4AU_ORIGINAL_W32",name,"total_source_opposite_wedges",
                  len(wedges),"all_globally_occupied_template_pairs",total,
                  "four_source_pattern_boolean_Hall_table",dict(sorted(tbl.items())))

    def test_04_literal_true_W32_and_W34_original_source_triple_counts(self):
        m=zero_split_original_W32()
        literal=literal_true_original_W32_source_threeflag_motif_census(m)
        self.assertEqual(literal["full_true_original_triples"],14190)
        self.assertEqual(literal["direct_original_source_flag_triple_histogram"][
                             "B/B"],180)
        for s in (2,4):
            model=m if s==2 else fixture(2,"lex")
            bb=literal_true_original_source_BB_P4_audit(model)
            ab=literal_true_original_source_AB_audit(model)
            exact=all_h_original_threeflag_source_motif_population(s)
            self.assertEqual(bb["true_original_BB_incidence_P4_count"],
                             exact["three_DISTINCT_original_source_flag_ID_type_counts"]["B/B"])
            self.assertEqual(ab["true_original_AB_line_repeat_count"],
                             exact["three_DISTINCT_original_source_flag_ID_type_counts"]["A/B"])
            self.assertTrue(bb["independently_source_center_edge_enumerated"])
            print("AA4AU_GENUINE_SOURCE_ALL_TRIPLES",s,
                  exact["three_DISTINCT_original_source_flag_ID_type_counts"])

    def test_05_true_original_W34_partial_positive_D6_sources_complete_polynomials(self):
        expected={"lex":(11025,11),"random":(13200,12)}
        known_four_boolean_Hall={"lex":(8,2,1,0),
                                 "random":(10,0,1,1)}
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            sample=exact_original_rainbow_D6_cycle_transfer(
                model,roots=(0,1,2),max_rainbow_sixcycles=1)
            Q,cycle=next(iter(
                sample["exact_true_original_six_ID_D6_Q_to_unique_cycle"].items()))
            wedge=(cycle[0],)+tuple(sorted((cycle[1],cycle[-1])))
            ctx,wedges,tbl,total=whole_original_model_polynomial_table(
                model,all_wedges=False,select_wedge=wedge)
            positives=sum(n for (_,outcome),n in tbl.items() if outcome=="YES")
            self.assertEqual((total,positives),expected[scheme])
            self.assertEqual(tuple(tbl[(label,"YES")] for label in
                         ("A/A","A/B","B/A","B/B")),
                         known_four_boolean_Hall[scheme])
            self.assertTrue(ctx["s"]==4)
            print("AA4AU_GENUINE_W34_PARTIAL",scheme,"wedge",wedge,
                  "source_D6_Q",Q,"original_pattern_Hall_table",dict(sorted(tbl.items())))

    def test_06_true_source_symplectic_and_independent_physical_type_permutations(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        _,_,original,total=whole_original_model_polynomial_table(m)
        _,_,transformed,trans_total=whole_original_model_polynomial_table(changed)
        self.assertEqual(original,transformed)
        self.assertEqual(total,trans_total)
        for corrupted in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                whole_original_model_polynomial_table(corrupted)


if __name__=="__main__":
    unittest.main()
