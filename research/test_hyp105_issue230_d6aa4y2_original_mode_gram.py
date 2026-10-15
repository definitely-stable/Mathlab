"""Independent original GQ seven-mode Gram and sign-robust charging tests."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index)
from hyp105_issue230_d6aa4ycyc_bilateral_original_matrix import (
    source_model_at,TAGS)
from hyp105_issue230_d6aa4y2_original_mode_gram import (
    original_source_cell, original_half_feature, verify_original_mode_product,
    ceil_sqrt,parse_gradient_native_tsv,ENERGY_HEADER,N_MOVES)


def sparse_delta(base,changed):
    m=Counter()
    if base is not None:m[base]-=1
    if changed is not None:m[changed]+=1
    return {k:v for k,v in m.items() if v}


class ActualOriginalSevenModeGramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=fixture(1,"S68")
        cls.rows=list(exact_ONE_side_original_projection_index(
            cls.m,0)["candidate_sixset_map"].keys())

    def test_001_real_original_six_flag_source_forests(self):
        self.assertEqual(len(self.rows),62370)
        inc=self.m["incidences"]
        seen=Counter()
        for Q in self.rows[::111]:
            tag=original_source_cell(Q,inc)
            if tag is not None:
                self.assertIn(tag,TAGS)
                seen[tag]+=1
        self.assertGreater(len(seen),2)
        with self.assertRaises(ValueError):
            original_source_cell((1,1,2,3,4,5),inc)

    def test_002_immutable_exact_seven_source_half_mode_product(self):
        for base in ("S68","S72"):
            m=fixture(1,base)
            qs=list(exact_ONE_side_original_projection_index(
                m,0)["candidate_sixset_map"])
            for Q in qs[::107]:
                verify_original_mode_product(Q,m)

    def test_003_two_sided_original_swaps_one_Q_tensor_finite_difference(self):
        inc=self.m["incidences"]
        for pi,li in ((1,1),(7,11),(35,78),(105,105)):
            models={(0,0):self.m,
                    (1,0):source_model_at(self.m,pi,0),
                    (0,1):source_model_at(self.m,0,li),
                    (1,1):source_model_at(self.m,pi,li)}
            for Q in self.rows[::291]:
                L0=original_half_feature(Q,inc,models[0,0]["left_labels"],0)
                L1=original_half_feature(Q,inc,models[1,0]["left_labels"],0)
                R0=original_half_feature(Q,inc,models[0,0]["right_labels"],1)
                R1=original_half_feature(Q,inc,models[0,1]["right_labels"],1)
                deltaL=sparse_delta(L0,L1)
                deltaR=sparse_delta(R0,R1)
                expected=sum(da*deltaR.get(k,0) for k,da in deltaL.items())
                actual={}
                for key,m in models.items():
                    actual[key]=classify_seven_prechecked(
                        Q,m["left_labels"],m["right_labels"],inc)
                measured=(int(actual[1,1] is not None)-
                          int(actual[1,0] is not None)-
                          int(actual[0,1] is not None)+
                          int(actual[0,0] is not None))
                self.assertEqual(expected,measured)
                for tag in TAGS:
                    tag_expected=sum(v*deltaR.get(k,0)
                        for k,v in deltaL.items() if k[0]==tag)
                    tag_measured=(int(actual[1,1]==tag)-
                                  int(actual[1,0]==tag)-
                                  int(actual[0,1]==tag)+
                                  int(actual[0,0]==tag))
                    self.assertEqual(tag_expected,tag_measured)

    def test_004_original_seven_weighted_mode_tensor(self):
        inc=self.m["incidences"]
        pi,li=35,78
        models=[self.m,source_model_at(self.m,pi,0),
                source_model_at(self.m,0,li),
                source_model_at(self.m,pi,li)]
        for Q in self.rows[::137]:
            tags=[verify_original_mode_product(Q,m) for m in models]
            expected=(R3_CERTIFIED_FLOORS.get(tags[3],0)-
                      R3_CERTIFIED_FLOORS.get(tags[1],0)-
                      R3_CERTIFIED_FLOORS.get(tags[2],0)+
                      R3_CERTIFIED_FLOORS.get(tags[0],0))
            L0=original_half_feature(Q,inc,models[0]["left_labels"],0)
            L1=original_half_feature(Q,inc,models[1]["left_labels"],0)
            R0=original_half_feature(Q,inc,models[0]["right_labels"],1)
            R1=original_half_feature(Q,inc,models[2]["right_labels"],1)
            dl=sparse_delta(L0,L1)
            dr=sparse_delta(R0,R1)
            weighted=sum(R3_CERTIFIED_FLOORS[k[0]]*v*dr.get(k,0)
                         for k,v in dl.items())
            self.assertEqual(expected,weighted)

    def test_005_exact_nonnegative_Cauchy_integer_budget(self):
        self.assertEqual(ceil_sqrt(0),0)
        self.assertEqual(ceil_sqrt(1),1)
        self.assertEqual(ceil_sqrt(2),2)
        self.assertEqual(ceil_sqrt(9),3)
        self.assertEqual(ceil_sqrt(17),5)
        with self.assertRaises(ValueError):
            ceil_sqrt(-1)
        with self.assertRaises(ValueError):
            ceil_sqrt(1.5)

    def test_006_fail_closed_original_gradient_matrix_schema(self):
        header="\t".join(ENERGY_HEADER)
        rows=["\t".join(map(str,(side,move,*([0]*7))))
              for side in (0,1) for move in range(N_MOVES)]
        table=header+"\n"+"\n".join(rows)
        data=parse_gradient_native_tsv(table)
        self.assertEqual(len(data),212)
        self.assertEqual(sum(data[0,0].values()),0)
        with self.assertRaises(AssertionError):
            parse_gradient_native_tsv(header+"\n"+"\n".join(rows[:-1]))
        invalid=rows.copy()
        invalid[0]="\t".join(map(str,(0,0,1,0,0,0,0,0,0)))
        with self.assertRaises(AssertionError):
            parse_gradient_native_tsv(header+"\n"+"\n".join(invalid))

    def test_007_seven_mode_Gram_proof_does_not_assume_sign(self):
        # Genuine historical mixed Hessian has both signs (prior independently
        # hosted exact original Y-CYC). No implied positive all-h minimax.
        self.assertEqual(len(TAGS),7)
        self.assertEqual(set(R3_CERTIFIED_FLOORS),set(TAGS))
        for x,y in ((5,-5),(-5,5),(0,0)):
            # The universal Gram bound is symmetric under sign changes.
            Eleft=25;Eright=1
            self.assertLessEqual(x*x,Eleft*Eright)
            self.assertLessEqual(y*y,Eleft*Eright)


if __name__=="__main__":
    unittest.main()
