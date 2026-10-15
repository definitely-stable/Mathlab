"""HYP-105 #230 Y-CYC independent genuine ORIGINAL mixed-swap support tests."""
import unittest
from itertools import combinations
from collections import Counter
from pathlib import Path

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model, exact_ONE_side_original_projection_index)
from hyp105_issue230_d6aa4ycyc_bilateral_original_matrix import (
    TAGS,MOVES,ROWS,HEADERS,engine_input,mixed_original_two_side_support,
    source_model_at,parse_exact_native_tsv,score_key)


class GenuineOriginalYcycTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=fixture(1,"S68")

    def test_001_genuine_source_45_incidences_and_global_bijections(self):
        inc,f,g=strict_true_W32_model(self.model)
        self.assertEqual(len(inc),45)
        self.assertEqual(len(f),len(g))
        self.assertEqual(len(MOVES),106)
        self.assertEqual(ROWS,11236)
        self.assertEqual(len(engine_input(self.model).splitlines()),75)
        for i,j in ((0,0),(1,1),(45,87),(105,105)):
            m=source_model_at(self.model,i,j)
            strict_true_W32_model(m)
            self.assertEqual(set(m["left_labels"]),set(f))
            self.assertEqual(set(m["right_labels"]),set(g))

    def test_002_source_only_mixed_locality_predicate(self):
        inc=self.model["incidences"]
        left=exact_ONE_side_original_projection_index(self.model,0)
        q=list(left["candidate_sixset_map"])
        self.assertEqual(len(q),62370)
        for Q in q[::511]:
            m1=(0,1);m2=(0,1)
            indicator=mixed_original_two_side_support(Q,inc,m1,m2)
            manual=any(inc[j][0] in m1 for j in Q) and any(
                inc[j][1] in m2 for j in Q)
            self.assertEqual(indicator,manual)
        with self.assertRaises(ValueError):
            mixed_original_two_side_support((0,0,1,2,3,4),inc,(0,1),(0,1))
        with self.assertRaises(ValueError):
            mixed_original_two_side_support(q[0],inc,(0,0),(0,1))

    def test_003_historical_full_original_indicator_mixed_support(self):
        inc=self.model["incidences"]
        selected=list(exact_ONE_side_original_projection_index(
            self.model,0)["candidate_sixset_map"])[::743]
        for i,j in ((1,1),(1,50),(87,105)):
            maps={
                (0,0):self.model,
                (i,0):source_model_at(self.model,i,0),
                (0,j):source_model_at(self.model,0,j),
                (i,j):source_model_at(self.model,i,j),
            }
            for Q in selected:
                tags={}
                for key,m in maps.items():
                    tags[key]=classify_seven_prechecked(
                        Q,m["left_labels"],m["right_labels"],inc)
                for tag in TAGS:
                    ind=lambda key: int(tags[key]==tag)
                    delta=ind((i,j))-ind((i,0))-ind((0,j))+ind((0,0))
                    if not mixed_original_two_side_support(
                            Q,inc,MOVES[i],MOVES[j]):
                        self.assertEqual(delta,0)
                if not mixed_original_two_side_support(
                        Q,inc,MOVES[i],MOVES[j]):
                    weighted=lambda key: R3_CERTIFIED_FLOORS.get(tags[key],0)
                    self.assertEqual(
                        weighted((i,j))-weighted((i,0))-
                        weighted((0,j))+weighted((0,0)),0)

    def test_004_full_matrix_schema_and_51palette_weights(self):
        base="\t".join(HEADERS)
        good=[]
        for i in range(106):
            for j in range(106):
                good.append("\t".join(map(str,(i,j,0,1,1,0,0,0,0,2,91200))))
        matrix=parse_exact_native_tsv(base+"\n"+"\n".join(good))
        self.assertEqual(len(matrix),ROWS)
        self.assertEqual(matrix[105,105]["S"],2)
        self.assertEqual(matrix[105,105]["weight"],91200)
        with self.assertRaises(AssertionError):
            parse_exact_native_tsv(base+"\n"+"\n".join(good[:-1]))
        broken=good.copy()
        broken[-1]=broken[0]
        with self.assertRaises(AssertionError):
            parse_exact_native_tsv(base+"\n"+"\n".join(broken))
        invalid=good.copy()
        invalid[1]=invalid[1].replace("\t91200","\t91201")
        with self.assertRaises(AssertionError):
            parse_exact_native_tsv(base+"\n"+"\n".join(invalid))

    def test_005_fail_closed_nonphysical_or_repeated_maps(self):
        for point,line in ((-1,0),(0,106),(True,1),(1,3.0)):
            with self.assertRaises(ValueError):
                source_model_at(self.model,point,line)
        m=source_model_at(self.model,1,1)
        self.assertNotEqual(m["left_labels"],self.model["left_labels"])
        self.assertNotEqual(m["right_labels"],self.model["right_labels"])
        self.assertEqual(
            {frozenset(x) for x in m["left_labels"]},
            {frozenset(x) for x in self.model["left_labels"]})

    def test_006_no_false_all_h_root_or_constant_inference(self):
        self.assertEqual(len(TAGS),7)
        self.assertEqual(sum(1 for x in TAGS if x=="D6"),1)
        self.assertEqual(R3_CERTIFIED_FLOORS["D6"],5643)
        self.assertEqual(R3_CERTIFIED_FLOORS["B-left/A-right"],45600)
        self.assertEqual(R3_CERTIFIED_FLOORS["A-left/B-right"],45600)
        self.assertTrue(score_key({"S":5,"D6":0,
            "point_move_id":0,"line_move_id":0}) <
            score_key({"S":5,"D6":1,
            "point_move_id":1,"line_move_id":0}))


if __name__=="__main__":
    unittest.main()
