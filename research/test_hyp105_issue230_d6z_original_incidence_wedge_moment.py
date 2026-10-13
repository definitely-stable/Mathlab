"""D6-Z: independent ORIGINAL incidence wedge/adjacency and seven-class audit."""
import unittest
from itertools import combinations,permutations
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb

from hyp105_issue230_d6z_original_incidence_wedge_moment import (
    physical_wedge_sixset,validated_original_regular_model,
    sharp_two_sided_wedge_moment_envelope,explicit_wedge_moment_extremizers,
    source_collinearity_adjacency,actual_original_W32_seven_proxy_report,
    report,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6y_capacity_adjacency_cut import (
    graph_adjacency_count,sharp_adjacency_image_bound
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,classify_seven_prechecked
)


def independent_pair_intersections(incidences,labels,side):
    value=0
    for i in range(len(incidences)):
        for j in range(i+1,len(incidences)):
            p=incidences[i][side]
            q=incidences[j][side]
            value+=len(set(labels[p])&set(labels[q]))
    return value


def independent_six_local_wedge(incidences,labels,side):
    return sum(len(set(labels[incidences[i][side]])&
                   set(labels[incidences[j][side]]))
               for i,j in combinations(range(6),2))


def independent_all_collinear_pairs(E,side):
    scope=defaultdict(set)
    for p,l in E:
        u,v=(p,l) if side==0 else (l,p)
        scope[v].add(u)
    joined=set()
    for neighbors in scope.values():
        for x,y in combinations(sorted(neighbors),2):
            if (x,y) in joined:
                raise AssertionError("original partial linearity violated")
            joined.add((x,y))
    return joined


class D6ZOriginalWedgeTests(unittest.TestCase):
    def test_exact_all_h_wedge_transport_formula_and_two_sided_extremizers(self):
        for h in range(1,7):
            s=2**h
            z=sharp_two_sided_wedge_moment_envelope(s)
            V,D,a=z["V"],z["Delta"],z["a"]
            N=V*D
            Amax=sharp_adjacency_image_bound(s)[
                "sharp_max_occupied_adjacent_unordered_pairs"]
            self.assertEqual(z["original_total_incidences"],N)
            self.assertEqual(z["six_incidence_subsets_count"],comb(N,6))
            self.assertEqual(z["pair_incidence_to_sixset_multiplicity"],
                             comb(N-2,4))
            self.assertEqual(z["same_original_typed_factor_pair_wedge"],
                             2*V*comb(D,2))
            self.assertEqual(z["physical_image_adjacency_max_sharp"],Amax)
            self.assertLessEqual(z["physical_image_adjacency_min_sharp"],Amax)
            self.assertEqual(z["global_original_sixset_wedge_sum_min_sharp"],
                comb(N-2,4)*(2*V*comb(D,2)+D*D*z[
                    "physical_image_adjacency_min_sharp"]))
            self.assertTrue(z["holds_for_both_independent_ORIGINAL_typed_sides"])
            self.assertTrue(z["not_GF5_positive_seven_count_lower"])
        for s in (2,4,8):
            witness=explicit_wedge_moment_extremizers(s)
            V=witness["V"]
            for side in ("point","line"):
                for ext in ("min","max"):
                    labels=witness[
                        f"{ext}_original_{side}_image_labels"]
                    self.assertEqual(len(labels),V)
                    self.assertEqual(len(set(labels)),V)
                    expected=sharp_two_sided_wedge_moment_envelope(s)[
                        f"physical_image_adjacency_{ext}_sharp"]
                    self.assertEqual(graph_adjacency_count(
                        labels,witness["s"] if False else
                        parameters(s)["a"]),expected)

    def test_independent_every_incidence_pair_W32_W34_moment_identity(self):
        for h in (1,2):
            model=fixture(h,"lex")
            p,L,R,E=validated_original_regular_model(model)
            D,V,N=p["Delta"],p["V"],len(E)
            for side,labels in ((0,L),(1,R)):
                brute=independent_pair_intersections(E,labels,side)
                formula=2*V*comb(D,2)+D*D*graph_adjacency_count(labels,p["a"])
                self.assertEqual(brute,formula)
                aggregate=brute*comb(N-2,4)
                z=sharp_two_sided_wedge_moment_envelope(2**h)
                self.assertLessEqual(z[
                    "global_original_sixset_wedge_sum_min_sharp"],aggregate)
                self.assertLessEqual(aggregate,z[
                    "global_original_sixset_wedge_sum_max_sharp"])

    def test_all_six_subsets_independent_small_host_double_count(self):
        # Unrelated finite toy host, explicitly count every six-subset,
        # including repeated ORIGINAL factors at different incidence positions.
        E=((0,0),(0,1),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3))
        L=((0,1),(0,2),(1,2),(2,3))
        R=((0,2),(0,3),(1,3),(1,2))
        for side,labels in ((0,L),(1,R)):
            by_six=sum(independent_six_local_wedge(Q,labels,side)
                       for Q in combinations(E,6))
            by_pairs=independent_pair_intersections(E,labels,side)*comb(6,4)
            self.assertEqual(by_six,by_pairs)
        for Q in combinations(E,6):
            w=physical_wedge_sixset(Q,L,R)
            self.assertEqual(w["left"]["wedge"],
                             independent_six_local_wedge(Q,L,0))
            self.assertEqual(w["right"]["wedge"],
                             independent_six_local_wedge(Q,R,1))

    def test_original_W32_source_collinearity_and_random_image_transport(self):
        model=fixture(1,"S68")
        p,L,R,E=validated_original_regular_model(model)
        z=source_collinearity_adjacency(model)
        for side,labels,coordinate in (("left",L,0),("right",R,1)):
            src=independent_all_collinear_pairs(E,coordinate)
            self.assertEqual(len(src),p["V"]*comb(p["Delta"],2))
            actual=sum(bool(set(labels[x])&set(labels[y])) for x,y in src)
            self.assertEqual(z[side][
                "physical_adjacent_original_collinear_pairs"],actual)
            self.assertEqual(Fraction(z[side][
                "exact_image_conditioned_uniform_permutation_expected"]),
                Fraction(len(src)*graph_adjacency_count(labels,p["a"]),
                         comb(p["V"],2)))
            self.assertEqual(Fraction(z[side][
                "exact_image_conditioned_uniform_permutation_expected"]),
                Fraction(180,7))
        # Independently enumerate ALL 4! permutations on a toy ORIGINAL
        # pair graph and verify its image-conditioned collinear-pair mean.
        labels=((0,1),(0,2),(1,2),(2,3))
        src={(0,1),(1,2),(0,3)}
        outcomes=[]
        for perm in permutations(labels):
            outcomes.append(sum(bool(set(perm[i])&set(perm[j]))
                                for i,j in src))
        physical_pairs=sum(bool(set(a)&set(b))
                           for a,b in combinations(labels,2))
        self.assertEqual(Fraction(sum(outcomes),len(outcomes)),
                         Fraction(len(src)*physical_pairs,comb(4,2)))

    def test_physical_wedge_six_insufficient_for_large_alphabets(self):
        # Seven-vertex physical TREE: physical degree sequence 3,2,2,2,1,1,1
        # has sum_c C(degree,2)=6, but NOT six active degree-two coords.
        tree=((0,1),(0,2),(0,3),(1,4),(2,5),(3,6))
        q=tuple((i,i) for i in range(6))
        physical=tree+((4,5),)
        w=physical_wedge_sixset(q,physical,physical)
        self.assertEqual(w["left"]["wedge"],6)
        self.assertEqual(w["right"]["wedge"],6)
        self.assertEqual(w["left"]["distinct_physical_coordinates"],7)
        self.assertFalse(w["two_sided_regular_proxy"])

    def test_true_original_W32_two_side_proxy_contains_strict_false_positives(self):
        result=actual_original_W32_seven_proxy_report()
        self.assertEqual([x["scheme"] for x in result],["S68","S72"])
        for x,expected in zip(result,(68,72)):
            self.assertEqual(x["original_sixsets_left_candidate_census"],62370)
            self.assertEqual(x["true_original_seven_GF5_positive_count"],expected)
            self.assertGreater(x["proxy_false_positives"],0)
            self.assertEqual(
                x["two_sided_physical_degree_two_proxy"]-expected,
                x["proxy_false_positives"])
            self.assertEqual(sum(x["false_positive_types"].values()),
                             x["proxy_false_positives"])
            self.assertEqual(sum(x["seven_positive_by_exact_class"].values()),
                             expected)
            self.assertEqual(x["left_right_global_image_adjacency"],[60,60])
            model=fixture(1,x["scheme"])
            self.assertEqual(
                seven_census(model,independent_checks=False)["S_seven"],
                expected)
            p,L,R,E=validated_original_regular_model(model)
            for key,should_accept in (
                ("true_positive_original_sixset_witness",True),
                ("false_positive_original_sixset_witness",False)):
                Q=tuple(tuple(t) for t in x[key])
                ids=tuple(sorted(E.index(edge) for edge in Q))
                status=classify_seven_prechecked(ids,L,R,E) is not None
                self.assertEqual(status,should_accept)
                self.assertTrue(physical_wedge_sixset(Q,L,R)[
                    "two_sided_regular_proxy"])
        self.assertNotEqual(result[0]["true_original_seven_GF5_positive_count"],
                            result[1]["true_original_seven_GF5_positive_count"])
        # Same FULL physical K6 image on each typed side, and same left f.
        l0,r0,_,_=validated_original_regular_model(fixture(1,"S68"))
        l1,r1,_,_=validated_original_regular_model(fixture(1,"S72"))
        self.assertEqual(l0,l1)
        self.assertEqual(set(r0),set(r1))
        self.assertEqual(set(l0),set(r1))

    def test_fail_closed_original_missing_rows_and_invalid_six(self):
        m=fixture(1,"lex")
        a={**m,"incidences":list(m["incidences"])[:-1]}
        with self.assertRaises(ValueError):
            validated_original_regular_model(a)
        a={**m,"right_labels":list(m["right_labels"])[:-1]}
        with self.assertRaises(ValueError):
            validated_original_regular_model(a)
        _,L,R,E=validated_original_regular_model(m)
        with self.assertRaises(ValueError):
            physical_wedge_sixset(tuple(E[0] for _ in range(6)),L,R)
        with self.assertRaises(ValueError):
            physical_wedge_sixset(E[:5],L,R)
        with self.assertRaises(ValueError):
            physical_wedge_sixset(E[:5]+((123,13),),L,R)
        with self.assertRaises(ValueError):
            explicit_wedge_moment_extremizers(8,max_V=50)

    def test_machine_contract_keeps_root_and_novelty_gate_open(self):
        z=report()
        self.assertEqual(z["theorem"],
                         "ALL-H-EXACT-ORIGINAL-SIXSET-WEDGE-TRANSPORT")
        self.assertEqual(z["original_point_and_line_typed_images"],
                         "BOTH-EXACT-ALL-H")
        self.assertEqual(z["all_h_wedge_moment_envelope"],"TWO-SIDED-SHARP")
        self.assertFalse(z["global_image_only_determines_original_seven_GF5_S"])
        self.assertFalse(z["two_sided_physical_regular_proxy_sufficient_for_GF5_seven"])
        self.assertTrue(z["not_new_graph_extremal_theory"])
        self.assertTrue(z["not_universal_positive_GF5_bound"])
        self.assertEqual((z["Branch_A"],z["Branch_B"]),("OPEN","OPEN"))
        self.assertEqual(len(z["all_h_envelopes"]),6)


if __name__=="__main__":
    unittest.main()
