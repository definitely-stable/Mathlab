"""Permanent independent true-original W34 two-edit binary CSP certificate.

The complete per-tuple 28D signed witnesses and all two-source relation
matrices are rerun on FINAL HEAD in hosted source jobs and stored as
artifacts. This unit test independently checks the committed complete
625-edge combinatorial summary and governance; it does not replace the
full signed physical GF5 source rehash in the specialist matrix.
"""
import copy
from itertools import combinations
import json
from math import comb
from pathlib import Path
import unittest

from hyp105_frozen_core_fiber import real_source
from hyp105_w34_twoedit_binary_csp import exact_ac3

HERE=Path(__file__).parent
CERT=HERE/"hyp105_w34_twoedit_binary_csp_certificates.json"
PREVIOUS=HERE/"hyp105_w34_frozen_core_domain_certificates.json"
EXPECT={"lex":(25,300,102462,101100,1362,463),
        "reverse-line":(26,325,110024,108753,1271,479)}


def verify_permanent_summary(z):
    parent=json.loads(PREVIOUS.read_text(encoding="utf-8"))
    if (z["schema"]!=
        "mathlab.hyp105.original-W34-full-two-editable-binary-CSP-certificate.v1"
        or z["scientific_parent_722_exact_SHA"]!=
            "10958b04a2bd62f258b95e22f294ea222622a292"
        or z["full_two_source_W34_matrix_first_proof_run"]!=41875839319
        or z["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or z["all_h_root_A_B_C_proved"]
        or z["joint_true_Gf5_zero_ASET_from_binary_only"]
        or set(z["schemes"])!=set(EXPECT)):
        raise AssertionError("false theorem promotion or input provenance drift")
    for scheme,expected in EXPECT.items():
        n,pairs,alltuples,allowed,blocked,one_total=expected
        current=z["schemes"][scheme]
        model,indices,columns,supports,T=real_source(scheme)
        old=parent["schemes"][scheme]
        if (tuple(T)!=tuple(current["actual_original_source_cover"]) or
            len(T)!=n or
            current["parent_722_exact_HEAD"]!=
                "10958b04a2bd62f258b95e22f294ea222622a292" or
            current["original_true_W34_N"]!=425 or
            current["complete_GF5_dimension"]!=28 or
            current["all_true_frozen_original_ID_count"]!=425-n or
            current["all_two_editable_source_pairs_checked"]!=pairs or
            pairs!=comb(n,2)):
            raise AssertionError("not true 425-source min-cover binary CSP")
        D={int(i):tuple(v) for i,v in current[
            "source_singleton_frozen_domains"].items()}
        if (set(D)!=set(T) or
            sum(len(v) for v in D.values())!=one_total or
            any(not v or tuple(sorted(set(v)))!=v or
                any(not 0<=p<51 for p in v) for v in D.values())):
            raise AssertionError("not original complete 51-palette F domain")
        for i in T:
            oldcount=next(x["allowed_p2_p3"] for x in old[
                "all_source_palette_local_domains"] if x["source_ID"]==i)
            if oldcount!=len(D[i]):
                raise AssertionError("changed original physical source fiber")
        edge_sizes=current["source_pairwise_relation_sizes"]
        ids=set(str(i)+","+str(j) for i,j in combinations(T,2))
        if (set(edge_sizes)!=ids or
            any(type(v) is not int or not 0<=v<=len(D[
                int(k.split(",")[0])])*len(D[int(k.split(",")[1])])
                for k,v in edge_sizes.items()) or
            sum(edge_sizes.values())!=allowed or
            current["all_source_domain_pair_tuples_checked"]!=alltuples or
            current["all_exact_signed_2v2_3v3_pair_tuples_surviving"]!=allowed or
            current["all_exact_signed_pair_tuples_excluded"]!=blocked or
            alltuples!=allowed+blocked or
            current["pairs_with_zero_valid_tuples"] or
            current["arc_consistency"]["removals"]):
            raise AssertionError("binary pairwise physical GF5 universe lost")
        arc=current["arc_consistency"]
        if (arc["rounds"]!=1 or arc["empty_ids"] or
            {int(k):v for k,v in arc["domains"].items()} !=
            {i:list(D[i]) for i in T} or
            current["claim_about_full_joint_source_0to3_GF5_ASET"] or
            current["claim_about_all_h_seven_motifs"] or
            current["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"):
            raise AssertionError("false arc-consistency or proof scope")
        # Pair relations are a strict NECESSARY filter, not a 25/26-source
        # full final valid GF5 assignment.
    return True


class RealW34PermanentBinaryCSPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(CERT.read_text(encoding="utf-8"))

    def test_full_true_625_original_source_binary_graph_sizes(self):
        self.assertTrue(verify_permanent_summary(self.saved))

    def test_premature_all_h_theorem_fails(self):
        changed=copy.deepcopy(self.saved)
        changed["all_h_root_A_B_C_proved"]=True
        with self.assertRaises(AssertionError):
            verify_permanent_summary(changed)

    def test_missing_actual_original_source_pair_fails(self):
        changed=copy.deepcopy(self.saved)
        changed["schemes"]["lex"][
            "source_pairwise_relation_sizes"].pop("3,19")
        with self.assertRaises(AssertionError):
            verify_permanent_summary(changed)

    def test_false_arcc_consistency_removal_fails(self):
        changed=copy.deepcopy(self.saved)
        changed["schemes"]["reverse-line"]["arc_consistency"][
            "removals"].append({
                "removed_source_ID":3,
                "removed_palette":0,
                "unsupporting_neighbor_source_ID":4,
            })
        with self.assertRaises(AssertionError):
            verify_permanent_summary(changed)


if __name__=="__main__":
    unittest.main()
