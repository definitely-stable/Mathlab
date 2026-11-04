"""Permanent EXACT true W34 25/26 source-ID frozen-core census bounds.

The exhaustive negative GF5 signed witnesses live in workflow artifacts
and are reproduced on FINAL HEAD by the mandatory specialist matrix.
The permanent summary is a strict provenance/census guard, not a full
multi-variable 0-to-3 GF5 assignment or an all-h theorem.
"""
import copy
from hashlib import sha256
import json
from math import comb,prod
from pathlib import Path
import unittest

from hyp105_frozen_core_fiber import real_source,input_text,RISKS
from hyp105_original_event_cover import normalize_edges,covers

ROOT=Path(__file__).parent
PERMANENT=ROOT/"hyp105_w34_frozen_core_domain_certificates.json"
PARENT=ROOT/"hyp105_w34_original_event_cover_certificates.json"


def verify_saved_summary(doc):
    parent=json.loads(PARENT.read_text(encoding="utf-8"))
    if (doc["schema"]!=
        "mathlab.hyp105.W34-true-original-min-cover-frozen-core-51-domains.v1"
        or doc["source_parent_721_exact_SHA"]!=
          "25178580d7c820bdfc0c909c4f72df70ad38d2c2"
        or doc["root_A_B_C_closed"] is not False
        or doc["full_zero_to_three_multi_source_assignments_constructed"] is not False
        or doc["source_specialist_run_id"]!=41867605339
        or set(doc["schemes"])!=set(RISKS)):
        raise AssertionError("permanent scientific provenance changed")
    for name,(r2,d3,r3,minimum) in RISKS.items():
        z=doc["schemes"][name]
        p=parent["schemes"][name]
        model,indices,columns,supports,T=real_source(name)
        if (z["edited_source_IDs"]!=list(T) or len(T)!=minimum or
            z["fixed_original_ID_count"]!=425-len(T) or
            z["complete_original_F_pairs"]!=comb(425-len(T),2) or
            z["complete_original_F_triples"]!=comb(425-len(T),3) or
            z["original_source_context_sha256"]!=
                sha256(input_text(name).encode("utf-8")).hexdigest()):
            raise AssertionError("source input reconstruction or fixed core drift")
        events=(p["initial_R2_true_original_signed_partitions"]+
                p["initial_R3_true_original_signed_partitions"])
        if not covers(normalize_edges(a+b for a,b in events),T):
            raise AssertionError("initial TRUE original source cover missing")
        shards=z["source_shards"]
        if (len(shards)!=4 or set(x["shard"] for x in shards)!=set(range(4))
            or set(i for sh in shards for i in sh["verified_original_source_ids"])
                !=set(T)
            or sum(len(sh["verified_original_source_ids"]) for sh in shards)
                !=len(T)):
            raise AssertionError("not a complete exactly-four-shard original map")
        for sh in shards:
            if sh["verified_original_source_ids"]!=[
                i for i in T if i%4==sh["shard"]]:
                raise AssertionError("noncanonical original-shard selected IDs")
        rows=z["all_source_palette_local_domains"]
        if (len(rows)!=len(T) or
            [r["source_ID"] for r in rows]!=list(T) or
            any(type(r["allowed_p2_p3"]) is not int or
                type(r["blocked_p2_p3"]) is not int or
                r["allowed_p2_p3"]+r["blocked_p2_p3"]!=51 or
                not 0<=r["allowed_p2_p3"]<=51 for r in rows)):
            raise AssertionError("not a complete exact 51-palette census")
        values=[r["allowed_p2_p3"] for r in rows]
        if (z["min_domain"]!=min(values) or
            z["max_domain"]!=max(values) or
            z["total_51_pattern_tests"]!=51*minimum or
            z["sum_allowed_p2_p3_single_source_domains"]!=sum(values) or
            z["source_ids_with_empty_domain"]!=[
                r["source_ID"] for r in rows if not r["allowed_p2_p3"]] or
            z["formal_upper_bound_on_CSP_assignments_after_frozen_core_filter"]
                !=str(prod(values))):
            raise AssertionError("wrong exact full source domain arithmetic")
        if (name=="lex" and (min(values),max(values),sum(values))!=(6,32,463)):
            raise AssertionError("lex source-domain regression")
        if (name=="reverse-line" and
            (min(values),max(values),sum(values))!=(11,28,479)):
            raise AssertionError("reverse-line source-domain regression")
    return True


class TrueOriginalW34FrozenCoreSummaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=json.loads(PERMANENT.read_text(encoding="utf-8"))

    def test_permanent_true_original_f_g_and_full_minimum_cover_domains(self):
        self.assertTrue(verify_saved_summary(self.doc))

    def test_missing_original_source_id_fails_closed(self):
        doc=copy.deepcopy(self.doc)
        doc["schemes"]["lex"]["all_source_palette_local_domains"].pop()
        with self.assertRaises(AssertionError):
            verify_saved_summary(doc)

    def test_false_empty_or_broken_51_domain_fails_closed(self):
        doc=copy.deepcopy(self.doc)
        doc["schemes"]["reverse-line"][
            "all_source_palette_local_domains"][0]["allowed_p2_p3"]=0
        with self.assertRaises(AssertionError):
            verify_saved_summary(doc)

    def test_unknown_all_h_claim_cannot_be_promoted(self):
        doc=copy.deepcopy(self.doc)
        doc["root_A_B_C_closed"]=True
        with self.assertRaises(AssertionError):
            verify_saved_summary(doc)

if __name__=="__main__":
    unittest.main()
