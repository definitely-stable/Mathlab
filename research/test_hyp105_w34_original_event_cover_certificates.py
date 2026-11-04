"""Independent committed full ORIGINAL W34 signed hypergraph certificate checks.

Checks complete saved physical source equations, original pair collisions,
disjoint source packing, concrete original-ID cover, and lower-bound
provenance. Exhaustive full 12.7m-triple COMPLETENESS is separately gated
by the specialized hosted physical source enumeration on the same HEAD.
"""
from itertools import combinations
import json
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_external_triple_r3_referee import exact_gf5_original_vectors
from hyp105_original_event_cover import (
    normalize_edges,canonical_signed_partition,covers,
    verify_disjoint_packing,bounded_exact_cover)

ROOT=Path(__file__).parent
RESULTS={"lex":(1,475,54,27,24,27),
         "reverse-line":(0,61,61,29,26,26)}


def _independent_pair_events(columns):
    by_signature={}
    collisions=set()
    pairs=0
    for i,j in combinations(range(len(columns)),2):
        signature=tuple((a+b)%5 for a,b in zip(columns[i],columns[j]))
        for old in by_signature.get(signature,()):
            if set(old)&{i,j}:
                raise AssertionError("duplicate singleton source column")
            collisions.add(tuple(sorted((old,(i,j)))))
        by_signature.setdefault(signature,[]).append((i,j))
        pairs+=1
    if pairs!=90100:
        raise AssertionError("did not exhaust original physical 2-subset sums")
    return tuple(sorted(collisions))


class OriginalW34EventCoverCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads((ROOT/
            "hyp105_w34_original_event_cover_certificates.json"
        ).read_text(encoding="utf-8"))
        cls.parent=json.loads((ROOT/
            "hyp105_w34_zero_incidence_erasure_certificates.json"
        ).read_text(encoding="utf-8"))

    def test_metadata_and_all_original_source_arrays(self):
        c=self.cert
        self.assertEqual(c["scientific_parent_PR"],720)
        self.assertEqual(c["source_parent_PR"],719)
        self.assertEqual(c["github_actions_exact_full_original_census_run_id"],41856319439)
        self.assertEqual(c["actual_true_original_W34_N"],425)
        self.assertEqual(c["physical_GF5_dimension"],28)
        self.assertEqual(c["original_triplet_census_per_scheme"],12704100)
        self.assertEqual(c["root_status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertTrue(c["no_all_h_theorem"])
        self.assertTrue(c["no_asymptotic_exponent"])
        self.assertEqual(set(c["schemes"]),set(RESULTS))

    def test_direct_28D_original_events_and_independent_complete_pairs(self):
        for scheme,(r2,d3,r3,edits,lower,upper) in RESULTS.items():
            with self.subTest(scheme=scheme):
                z=self.cert["schemes"][scheme]
                parent=self.parent["scheme_results"][scheme]
                model=pair_labeled_symplectic(2,scheme)
                before=tuple(parent["original_source_425_legal_palette_indices_before"])
                ids,columns=exact_gf5_original_vectors(model,before)
                self.assertEqual(ids,tuple(range(425)))
                self.assertEqual(len(set(columns)),425)
                self.assertTrue(all(len(v)==28 and sum(v)%5==4
                                    and sum(x!=0 for x in v)==4 for v in columns))
                self.assertEqual(z["initial_complete_D2_D3_TRUE_R3"],[r2,d3,r3])
                self.assertEqual(z["all_original_triples_exactly_audited"],12704100)
                e2=tuple(canonical_signed_partition(e,2)
                         for e in z["initial_R2_true_original_signed_partitions"])
                e3=tuple(canonical_signed_partition(e,3)
                         for e in z["initial_R3_true_original_signed_partitions"])
                self.assertEqual((len(e2),len(e3)),(r2,r3))
                self.assertEqual(len(set(e2)),r2)
                self.assertEqual(len(set(e3)),r3)
                self.assertEqual(_independent_pair_events(columns),tuple(sorted(e2)))
                for es in (e2,e3):
                    for a,b in es:
                        self.assertEqual(
                            tuple(sum(columns[x][j] for x in a)%5
                                  for j in range(28)),
                            tuple(sum(columns[x][j] for x in b)%5
                                  for j in range(28)))
                edges=normalize_edges(a+b for es in (e2,e3)
                                     for a,b in es)
                self.assertEqual(len(edges),z["distinct_original_ID_hyperedges"])
                trace=[e["original_source_flag_ID"]
                       for e in parent["exact_global_source_palette_edit_trace"]]
                self.assertEqual(trace,z["existing_719_true_original_source_edits"])
                self.assertEqual(len(set(trace)),edits)
                self.assertTrue(covers(edges,trace))
                pack=tuple(tuple(x) for x in
                           z["vertex_disjoint_original_event_packing"])
                self.assertEqual(verify_disjoint_packing(edges,pack),
                                 z["packing_certified_lower"])
                chosen=z["explicit_original_ID_hitting_set"]
                self.assertTrue(covers(edges,chosen))
                self.assertEqual(len(chosen),z["hitting_set_certified_upper"])
                self.assertEqual((z["transversal_certified_lower"],
                                  z["hitting_set_certified_upper"]),(lower,upper))
                self.assertGreaterEqual(lower,len(pack))
                self.assertLessEqual(upper,edits)
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertTrue(z["cover_is_NOT_a_proven_clean_GF5_palette_schedule"])
                self.assertTrue(z["no_asymptotic_exponent"])

    def test_independent_dual_certificate_and_bounded_lower_proof(self):
        for scheme in RESULTS:
            z=self.cert["schemes"][scheme]
            edges=normalize_edges(
                a+b for name in (
                    "initial_R2_true_original_signed_partitions",
                    "initial_R3_true_original_signed_partitions")
                for a,b in z[name])
            if scheme=="reverse-line":
                # Fully independent short primal/dual certificate:
                # 26 pairwise disjoint event edges and 26 chosen IDs.
                self.assertEqual(z["packing_certified_lower"],26)
                self.assertEqual(z["hitting_set_certified_upper"],26)
                self.assertEqual(z["bounded_exact_search_status"],"EXACT")
            else:
                # For lex 23 disjoint edges alone prove only 23.
                # Re-run *complete* k=23 branch rejection; k=24 was
                # NOT completed, so the honest result is [24,27].
                self.assertEqual(z["packing_certified_lower"],23)
                self.assertEqual(z["exhaustively_refuted_cardinalities"],[23])
                self.assertEqual(z["bounded_exact_search_status"],"BOUNDED")
                run=bounded_exact_cover(
                    edges,upper_cover=z["explicit_original_ID_hitting_set"],
                    max_nodes=250000)
                # New incidence-containment kernel independently
                # finishes k=23,24 UNSAT and finds a true k=25 cover.
                self.assertEqual((run["status"],run["lower"],run["upper"]),
                                 ("EXACT",25,25))
                self.assertEqual(run["exhausted_depths"],(23,24))


if __name__=="__main__":
    unittest.main()
