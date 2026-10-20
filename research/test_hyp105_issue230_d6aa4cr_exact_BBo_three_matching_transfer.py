"""AA4-CR independent original Q referees for exact GQ B/B-overlap 3x3 permanent."""
from collections import Counter
from itertools import permutations
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    GF5_BBO_WEIGHT,
    c4_completions_from_single_and_doubled,
    exact_three_by_three_incidence_matching,
    original_nonincident_threepath,
    original_BBo_exact_three_matching_transfer,
    original_dual_model_immutable_source_Q,
)
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import (
    _validated_original, macro_path_cut,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)


def _independent_true_original_id_referee(model, results):
    s,V,a,inc,f,g,_,_ = (
        __import__("hyp105_issue230_d6aa4bh_local_seven_compensation",
                   fromlist=["_original_source"])._original_source(model))
    ids=results["actual_distinct_original_sixflag_Q_sets"]
    assert len(ids)==results["historical_accepted_original_BBo_sixflag_Q"]
    for Q in ids:
        assert len(Q)==len(set(Q))==6
        assert classify_seven_all_a_original_Q(Q,f,g,inc)=="B/B-overlap"
        pp=Counter(inc[j][0] for j in Q)
        ll=Counter(inc[j][1] for j in Q)
        assert sorted(pp.values())==[1,1,1,1,2]
        assert sorted(ll.values())==[1,1,1,1,2]
        p2=next(k for k,v in pp.items() if v==2)
        l2=next(k for k,v in ll.items() if v==2)
        assert sum(inc[j]==(p2,l2) for j in Q)==1
    return True


class AA4CRExactOriginalBBoMatchingGate(unittest.TestCase):
    def _w32_all(self,scheme):
        model=fixture(1,scheme)
        result=original_BBo_exact_three_matching_transfer(model)
        old=seven_census(model,independent_checks=False,witness_sets=True)
        exact=frozenset(Q for Q,typ in old["sets"].items()
                        if typ=="B/B-overlap")
        got=frozenset(result["actual_distinct_original_sixflag_Q_sets"])
        self.assertEqual(got,exact)
        self.assertEqual(result["historical_accepted_original_BBo_sixflag_Q"],
                         old["seven_class_motif_counts"]["B/B-overlap"])
        self.assertEqual(result["actual_unique_NONINCIDENT_original_3path_anchors"],
                         15*(15-3))
        self.assertEqual(result["historical_accepted_GF5_weighted_numerator"],
                         GF5_BBO_WEIGHT*len(exact))
        self.assertEqual(result["three_by_three_source_PERMANENT_one"],len(got))
        self.assertTrue(_independent_true_original_id_referee(model,result))
        dual=original_dual_model_immutable_source_Q(model)
        reverse=original_BBo_exact_three_matching_transfer(dual)
        self.assertEqual(reverse["actual_distinct_original_sixflag_Q_sets"],
                         result["actual_distinct_original_sixflag_Q_sets"])
        print("AA4CR_TRUE_W32_FULL_BBO",scheme,
              {k:v for k,v in result.items() if k!="actual_distinct_original_sixflag_Q_sets"},
              "independent_legacy_Q_set_equal",True,
              "point_LINE_full_duality_equal",True,flush=True)

    def test_01_original_W32_lex_ALL_BBo_against_complete_independent_historical_Q_IDs(self):
        self._w32_all("lex")

    def test_02_original_W32_S72_ALL_BBo_against_complete_independent_historical_Q_IDs(self):
        self._w32_all("S72")

    def test_03_original_W32_cut_real_source_paths_physically_zero_transfer(self):
        X=(0,1,2);Y=(3,4,5)
        for scheme,anchors in (("lex",8),("S72",7)):
            model=fixture(1,scheme)
            old=macro_path_cut(model,X,Y)
            z=original_BBo_exact_three_matching_transfer(
                model,point_cut=X,line_cut=Y)
            self.assertEqual(z["actual_unique_NONINCIDENT_original_3path_anchors"],
                             old["unique_original_simple_3path_count"])
            self.assertEqual(z["actual_unique_NONINCIDENT_original_3path_anchors"],anchors)
            self.assertEqual(z["historical_accepted_original_BBo_sixflag_Q"],0)
            self.assertEqual(z["historical_accepted_GF5_weighted_numerator"],0)
            print("AA4CR_W32_CUT_PHYSICAL_ZERO",scheme,
                  "source3paths",anchors,
                  "source_BBo_Q",anchors*5056,
                  "historically_accepted_BBo_Q",0,flush=True)

    def _higher_real_partial(self,power,scheme,budget):
        model=fixture(power,scheme)
        s,V,a,f,g,pl,lp=_validated_original(model)
        pairs=tuple((p,l) for p in range(min(V,12))
                    for l in range(min(V,12))
                    if l not in pl[p])[:budget]
        self.assertTrue(pairs)
        z=original_BBo_exact_three_matching_transfer(
            model,anchor_pairs=pairs)
        rev=original_BBo_exact_three_matching_transfer(
            original_dual_model_immutable_source_Q(model),
            anchor_pairs=tuple((l,p) for p,l in pairs))
        self.assertEqual(z["actual_distinct_original_sixflag_Q_sets"],
                         rev["actual_distinct_original_sixflag_Q_sets"])
        self.assertEqual(z["actual_unique_NONINCIDENT_original_3path_anchors"],
                         len(pairs))
        self.assertTrue(_independent_true_original_id_referee(model,z))
        self.assertEqual(z["three_by_three_source_PERMANENT_one"],
                         z["historical_accepted_original_BBo_sixflag_Q"])
        self.assertEqual(z["three_by_three_source_PERMANENT_zero"]+
                         z["three_by_three_source_PERMANENT_one"],
                         z["paired_two_sided_C4_templates"])
        self.assertLessEqual(z["historical_accepted_original_BBo_sixflag_Q"],
                             len(pairs)*4*((a-4)*(a-5)//2)**2)
        print("AA4CR_TRUE_ORIGINAL_PARTIAL_SOURCE_ANCHORS",power,scheme,
              {k:v for k,v in z.items() if k!="actual_distinct_original_sixflag_Q_sets"},
              "dual_source_point_LINE_equal",True,flush=True)

    def test_04_original_W34_lex_true_source_partial_3path_permanent_duality(self):
        self._higher_real_partial(2,"lex",72)

    def test_05_original_W34_random_true_source_partial_3path_permanent_duality(self):
        self._higher_real_partial(2,"random",72)

    def _full_real_original_W34_BBo_census(self,scheme,expected):
        model=fixture(2,scheme)
        r=original_BBo_exact_three_matching_transfer(
            model,collect_original_Q=True)
        self.assertEqual(r["actual_unique_NONINCIDENT_original_3path_anchors"],
                         85*(85-5))
        self.assertEqual(r["historical_accepted_original_BBo_sixflag_Q"],expected)
        self.assertEqual(r["historical_accepted_GF5_weighted_numerator"],
                         GF5_BBO_WEIGHT*expected)
        self.assertTrue(_independent_true_original_id_referee(model,r))
        self.assertEqual(r["three_by_three_source_PERMANENT_one"],expected)
        print("AA4CR_TRUE_W34_FULL_ORIGINAL_BBO",scheme,
              {k:v for k,v in r.items() if k!="actual_distinct_original_sixflag_Q_sets"},
              "exact_independent_AA4CP_W34_root_class_regression",expected,flush=True)

    def test_07_genuine_original_W34_lex_ALL_BBo_against_AA4CP_full_root_class(self):
        # Independent right-FIRST C++ source-to-LEFT GF5 join AA4-CP
        # measured exact historic W34 lex B/B-overlap = 22,111.
        self._full_real_original_W34_BBo_census("lex",22111)

    def test_08_genuine_original_W34_random_ALL_BBo_against_AA4CP_full_root_class(self):
        # Independent original W34 random complete f/g root census:
        # historic B/B-overlap class = 24,168.
        self._full_real_original_W34_BBo_census("random",24168)

    def test_06_original_W38_true_source_sample_and_malformed_GQ_guards(self):
        # On W38 choose one NONTRIVIAL source P3 whose four actual
        # physical edges are pairwise disjoint in BOTH typed pair maps.
        # The first 0,0 lex anchor alone could give a vacuous zero
        # before exercising the actual 3x3 permanent oracle.
        model38=fixture(3,"lex")
        _,V,_,f38,g38,pl38,lp38=_validated_original(model38)
        witness=None
        for p in range(min(V,15)):
            for l in range(V):
                if l in pl38[p]:
                    continue
                path=original_nonincident_threepath(p,l,pl38,lp38)
                q=path[1][0]
                l0=path[0][1]
                if set(f38[p]).isdisjoint(f38[q]) and set(g38[l]).isdisjoint(g38[l0]):
                    witness=(p,l)
                    break
            if witness is not None:
                break
        self.assertIsNotNone(witness)
        z=original_BBo_exact_three_matching_transfer(model38,anchor_pairs=(witness,))
        rev=original_BBo_exact_three_matching_transfer(
            original_dual_model_immutable_source_Q(model38),
            anchor_pairs=((witness[1],witness[0]),))
        self.assertEqual(z["physical_disjoint_original_3path_anchors"],1)
        self.assertGreater(z["paired_two_sided_C4_templates"],0)
        self.assertEqual(z["actual_distinct_original_sixflag_Q_sets"],
                         rev["actual_distinct_original_sixflag_Q_sets"])
        self.assertTrue(_independent_true_original_id_referee(model38,z))
        print("AA4CR_TRUE_ORIGINAL_W38_NONVACUOUS_MATCHING",witness,
              {k:v for k,v in z.items() if k!="actual_distinct_original_sixflag_Q_sets"},flush=True)
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        with self.assertRaises(ValueError):
            original_BBo_exact_three_matching_transfer(model,anchor_pairs=((0,0),(0,0)))
        p,l=next((p,l) for p in range(V) for l in range(V) if l in pl[p])
        with self.assertRaises(ValueError):
            original_BBo_exact_three_matching_transfer(model,anchor_pairs=((p,l),))
        with self.assertRaises(ValueError):
            original_BBo_exact_three_matching_transfer(model,point_cut=(0,0))
        with self.assertRaises(ValueError):
            original_BBo_exact_three_matching_transfer(model,anchor_pairs=((-1,0),))
        with self.assertRaises(ValueError):
            exact_three_by_three_incidence_matching((0,0,1),(0,1,2),pl)
        with self.assertRaises(ValueError):
            original_nonincident_threepath(-1,0,pl,lp)
        self.assertEqual(c4_completions_from_single_and_doubled(
            (0,1),(1,2),{e:i for i,e in enumerate(f)},a),())


if __name__=="__main__":
    unittest.main()
