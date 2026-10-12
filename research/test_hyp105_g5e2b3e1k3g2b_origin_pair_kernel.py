"""K3-G2-B independent GQ-tensor and source-pair falsifiers."""
from collections import Counter
from itertools import combinations
import unittest
from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2b_origin_pair_kernel import (
    inc_tables,closure_tensor,cross_origin_certificate,CLASSES
)
from hyp105_g5e2b3e1k3g2_source_coincidence import source_coincidence_certificate


def inverse_third_coordinate_tensor(model,side):
    """Independent anchor-first and physical-third-coordinate census."""
    P,L=inc_tables(model)
    labels=model["right_labels"] if side=="line" else model["left_labels"]
    by_edge={frozenset(pair):i for i,pair in enumerate(labels)}
    origin_sets=L if side=="line" else P
    out=[Counter() for _ in labels]
    for i,(x,y) in enumerate(labels):
        for third in range(model["a"]):
            if third in (x,y):
                continue
            j=by_edge.get(frozenset((x,third)))
            k=by_edge.get(frozenset((y,third)))
            if j is None or k is None:
                continue
            common=origin_sets[j]&origin_sets[k]
            if len(common)>1:
                raise AssertionError("two original source intersections")
            for q in common:
                out[i][q]+=1
    return out


def independent_anchor_kernel(model,side,T):
    """Scan ALL anchor incident physical edges rather than pair candidate set."""
    P,L=inc_tables(model)
    labels=model["left_labels"] if side=="line" else model["right_labels"]
    anchors=L if side=="line" else P
    pencils=P if side=="line" else L
    classes=Counter()
    same=0
    for anchor,bucket in enumerate(T):
        on=anchors[anchor]
        for q,n in bucket.items():
            if q in on:
                same+=n*n
        for q,r in combinations(sorted(bucket),2):
            count=0
            for p in on:
                x,y=labels[p]
                count+=int((x in labels[q] and y in labels[r]) or
                           (y in labels[q] and x in labels[r]))
            if count==0:
                continue
            if q in on and r in on:
                kind="both_on_anchor"
            elif q in on or r in on:
                kind="one_on_anchor"
            elif pencils[q]&pencils[r]:
                kind="off_anchor_collinear"
            else:
                kind="off_anchor_noncollinear"
            classes[kind]+=bucket[q]*bucket[r]*count
    return same,classes


class K3G2BTests(unittest.TestCase):
    def test_closure_tensor_by_two_independent_directions(self):
        for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                              (2,"lex",None),(2,"random",20261011)):
            m=gq_pair_model(h,scheme,seed)
            for side in ("line","point"):
                cert=closure_tensor(m,side)
                other=inverse_third_coordinate_tensor(m,side)
                self.assertEqual(cert["T"],other)
                self.assertEqual(cert["closed"],sum(map(lambda x:sum(x.values()),other)))
                self.assertLessEqual(cert["closed"],cert["source_wedges"])
                self.assertLessEqual(cert["source_wedges"],cert["host_wedges"])
                self.assertLessEqual(cert["host_wedges"],cert["host_upper"])

    def test_original_pair_kernel_and_geometry_independent(self):
        for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                              (2,"lex",None),(2,"random",20261011)):
            m=gq_pair_model(h,scheme,seed)
            cert=cross_origin_certificate(m)
            for side in ("line","point"):
                T=inverse_third_coordinate_tensor(m,side)
                same,parts=independent_anchor_kernel(m,side,T)
                self.assertEqual(same,cert[side]["J_same"])
                for klass in CLASSES:
                    self.assertEqual(parts[klass],cert[side]["geometry"][klass])
                self.assertEqual(sum(parts.values()),cert[side]["J_cross"])
            baseline=source_coincidence_certificate(m)
            self.assertEqual(cert["J_cross"],baseline["J_cross_source"])
            self.assertEqual(cert["J_same"],baseline["J_source_same"])
            self.assertLessEqual(cert["J_cross"],cert["cross_origin_candidate_upper"])
            self.assertFalse(cert["universal_cross_o_s6_proved"])

    def test_host_wedge_vs_original_meeting_oracle(self):
        m=gq_pair_model(2,"random",20261011)
        P,L=inc_tables(m)
        for side in ("line","point"):
            labels=m["right_labels"] if side=="line" else m["left_labels"]
            orig=L if side=="line" else P
            host=source=0
            for i,j in combinations(range(len(labels)),2):
                if len(set(labels[i])&set(labels[j]))==1:
                    host+=1
                    meet=orig[i]&orig[j]
                    self.assertLessEqual(len(meet),1)
                    if meet:
                        source+=1
            cert=closure_tensor(m,side)
            self.assertEqual(host,cert["host_wedges"])
            self.assertEqual(source,cert["source_wedges"])

    def test_fail_closed(self):
        m=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            closure_tensor(m,max_wedges=0)
        with self.assertRaises(RuntimeError):
            cross_origin_certificate(m,max_pairs=0)
        with self.assertRaises(ValueError):
            closure_tensor(m,side="none")
        with self.assertRaises(ValueError):
            closure_tensor(m,max_wedges=True)
        with self.assertRaises(ValueError):
            cross_origin_certificate(m,max_pairs=-1)

if __name__=="__main__":
    unittest.main()
