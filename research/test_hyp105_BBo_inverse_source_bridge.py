"""Independent exhaustive ORIGINAL-source to physical-path inverse BBo referee."""
from collections import Counter
import json
from pathlib import Path
import unittest

from hyp105_BBo_inverse_source_bridge import (
    _oriented_three_edge_factor_paths,
    inverse_original_BBo_paths,
    independent_inverse_W32_census,
)
from hyp105_bbo_resilience import avoidance_certificate
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source,physical
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


class TestIndependentOriginalBBoInverse(unittest.TestCase):
    def test_complete_historical_W32_five_globally_reassigned_g_independent_paths(self):
        m=pair_labeled_symplectic(1,"lex")
        original_flags=m["incidences"]
        g0=tuple(m["right_labels"])
        for shift in (0,1,3,7,11):
            with self.subTest(shift=shift):
                g=tuple(g0[(i+shift)%len(g0)] for i in range(len(g0)))
                inverse=independent_inverse_W32_census(m,right_labels=g)
                forward=avoidance_certificate(
                    1,m["left_labels"],g)
                actual=set(map(tuple,forward["produced_sixsets"]))
                self.assertEqual(
                    set(inverse["inverse_paths_by_original_sixset"]),actual)
                self.assertEqual(
                    inverse["directed_inverse_source_paths"],
                    2*len(actual))
                self.assertGreater(inverse["eligible_inverse_sixsets"],0)
                self.assertEqual(
                    inverse["historical_original_BBo_sixsets"],
                    inverse["eligible_inverse_sixsets"]+
                    inverse["ineligible_inverse_sixsets"])
                # Independent source-owner physical check: each of the
                # inverse paths has three real retained flag edges.
                graph,owner=physical(
                    range(len(original_flags)),original_flags,
                    m["left_labels"],g)
                for ids,paths in inverse["inverse_paths_by_original_sixset"].items():
                    self.assertEqual(len(paths),2)
                    for corners,ids3 in paths:
                        self.assertEqual(len(corners),4)
                        self.assertTrue(all(
                            corners[j+1] in graph[corners[j]]
                            for j in range(3)))
                        self.assertEqual(
                            tuple(owner[tuple(sorted((corners[j],
                                    corners[j+1])))] for j in range(3)),ids3)

    def test_true_W32_different_core_and_forbidden_original_six_ID_masks(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        total=len(m["incidences"])
        for forbidden,core in (
                ((),tuple(range(total))),
                ((0,),tuple(i for i in range(total) if i!=0)),
                ((0,1,2),tuple(i for i in range(total)
                                if i not in (0,1,2) and i%3)),
                (tuple(range(0,total,7)),tuple(i for i in range(total)
                                 if i%2 and i%7)),
                ((),())):
            with self.subTest(forbidden=len(forbidden),core=len(core)):
                inv=independent_inverse_W32_census(
                    m,core_ids=core,deleted_ids=forbidden)
                fw=avoidance_certificate(
                    1,f,g,forbidden,core_ids=core)
                self.assertEqual(
                    set(inv["inverse_paths_by_original_sixset"]),
                    set(map(tuple,fw["produced_sixsets"])))
                self.assertEqual(
                    inv["directed_inverse_source_paths"],
                    fw["unblocked_paths_avoiding_all_six_forbidden_ids"])
                for ids,paths in inv["inverse_paths_by_original_sixset"].items():
                    self.assertEqual(len(paths),2)
                    self.assertFalse(set(ids)&set(forbidden))
                    self.assertTrue(set(paths[0][1])<=set(core))

    def test_W34_ancillary_projections_outside_core_and_deleted_original_flags(self):
        m=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        _,_,flags=genuine_source(2)
        f,g=m["f"],m["g"]
        for forbidden,core in (
                ((0,),tuple(i for i in range(len(flags)) if i%3 and i!=0)),
                (tuple(range(0,len(flags),17)),tuple(i for i in range(len(flags))
                        if i%3 and i%17))):
            with self.subTest(Z=len(forbidden)):
                forward=avoidance_certificate(
                    2,f,g,forbidden,core)
                self.assertGreater(
                    forward["accepted_original_BBo_subcount_avoiding_Z"],0)
                self.assertGreater(
                    forward["surviving_paths_with_anchor_outside_core"],0)
                for six in forward["produced_sixsets"]:
                    paths=inverse_original_BBo_paths(
                        six,flags,f,g,core_ids=core,deleted_ids=forbidden)
                    self.assertEqual(len(paths),2)
                    self.assertEqual(paths[1][0],tuple(reversed(paths[0][0])))
                    self.assertEqual(paths[1][1],tuple(reversed(paths[0][1])))

    def test_nonoverlap_genuine_source_sixsets_and_invalid_original_IDs_fail_closed(self):
        m=pair_labeled_symplectic(1,"lex")
        flags,f,g=m["incidences"],m["left_labels"],m["right_labels"]
        sample_bbo=None
        checked_other=Counter()
        for ids,kind in selected_left_six(m):
            if kind!="B":continue
            tag=classify_seven_prechecked(ids,f,g,flags)
            if tag=="B/B-overlap" and sample_bbo is None:
                sample_bbo=ids
            elif tag=="B/B-disjoint" and checked_other["disjoint"]<25:
                self.assertEqual(
                    inverse_original_BBo_paths(ids,flags,f,g),())
                checked_other["disjoint"]+=1
            if sample_bbo is not None and checked_other["disjoint"]==25:
                break
        self.assertIsNotNone(sample_bbo)
        self.assertEqual(checked_other["disjoint"],25)
        self.assertEqual(
            len(inverse_original_BBo_paths(sample_bbo,flags,f,g)),2)
        for bad in ((True,)+sample_bbo[1:],(-1,)+sample_bbo[1:],
                    sample_bbo[:5],sample_bbo[:5]+(45,),
                    (sample_bbo[0],)*6):
            with self.assertRaises(ValueError):
                inverse_original_BBo_paths(bad,flags,f,g)
        with self.assertRaises(ValueError):
            inverse_original_BBo_paths(
                sample_bbo,flags,f,g,core_ids=(0,0))
        with self.assertRaises(ValueError):
            inverse_original_BBo_paths(
                sample_bbo,flags,f,g,deleted_ids=(0,0))
        self.assertEqual(
            inverse_original_BBo_paths(
                sample_bbo,flags,f,g,core_ids=()),())

    def test_independently_inverse_chain_four_symbols_reversal(self):
        m=pair_labeled_symplectic(1,"lex")
        original=m["incidences"]
        f,g=m["left_labels"],m["right_labels"]
        for ids,kind in selected_left_six(m):
            if kind!="B":continue
            if classify_seven_prechecked(ids,f,g,original)!="B/B-overlap":
                continue
            pp=Counter(original[i][0] for i in ids)
            ll=Counter(original[i][1] for i in ids)
            p=next(x for x,n in pp.items() if n==2)
            ell=next(x for x,n in ll.items() if n==2)
            anchor=tuple(i for i in ids if original[i][0]==p or
                         original[i][1]==ell)
            self.assertEqual(len(anchor),3)
            remaining=[i for i in ids if i not in anchor]
            for side,labels in ((0,f),(1,g)):
                chains=_oriented_three_edge_factor_paths(
                    remaining,original,labels,side)
                self.assertEqual(len(chains),2)
                self.assertEqual(
                    chains[0][0],tuple(reversed(chains[1][0])))
                self.assertEqual(
                    chains[0][1],tuple(reversed(chains[1][1])))
            break
        else:
            self.fail("true W32 original BBo witness missing")


if __name__=="__main__":
    unittest.main()
