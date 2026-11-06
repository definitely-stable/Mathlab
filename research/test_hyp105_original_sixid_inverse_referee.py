"""Independent original six-ID inverse red-team tests; root #230 remains open."""
import json
import unittest
from pathlib import Path

from hyp105_original_sixid_inverse_referee import (
    bbo_structure, canonical_referee, geometry, independent_cycles,
    inverse_bbo, inverse_d6, original_seeded_d6, owned_graph,
    physical_first_bbo, source_case, exhaustive_original_W32_BBo_left_B_scan,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


ROOT = Path(__file__).parent


def low_rows():
    return json.loads((ROOT/"hyp105_original_lowtail_alln_energy_certificates.json").read_text())["genuine_true_original_cases"]


def heavy_rows():
    return json.loads((ROOT/"hyp105_original_deletion_adaptive_heavy_tail_certificates.json").read_text())["genuine_source_cases"]


class TestActualOriginalSixIdInverse(unittest.TestCase):
    def test_complete_true_original_lowtail_two_orientations(self):
        result=canonical_referee()
        self.assertEqual(result["schema"],"mathlab.hyp105.original-sixID-inverse-referee.v1")
        self.assertFalse(result["root_Branch_A_unconditionally_accepted"])
        self.assertTrue(result["BBo_inverse_is_not_all_class_surjectivity"])
        self.assertEqual([(z["s"],z["scheme"],z["original_BBo_sixsets"])
                          for z in result["genuine_original_lowtail"]],
                         [(2,"lex",1),(2,"reverse-line",0),
                          (4,"lex",1534),(4,"reverse-line",463)])
        self.assertEqual(len(result["genuine_original_heavy"]),3)
        self.assertTrue(all(z["physical_D6_C6"]>=1
                            for z in result["genuine_original_heavy"]))

    def test_own_source_topology_and_independent_historical_GF5(self):
        for z in low_rows():
            c=source_case({2:1,4:2}[z["s"]],z["scheme"])
            geo=geometry(c)
            C=z["original_core_source_IDs"]
            Z=z["deleted_original_flag_IDs"]
            _,owner=owned_graph(c,C)
            subset=z["real_positive_original_BBo_six_IDs"][:25]
            for ids in subset:
                with self.subTest(s=z["s"],scheme=z["scheme"],ids=ids):
                    topo=bbo_structure(ids,c,geo,Z)
                    self.assertIsNotNone(topo)
                    self.assertEqual(
                        classify_seven_prechecked(ids,c["f"],c["g"],c["flags"]),
                        "B/B-overlap")
                    inverse=inverse_bbo(ids,c,geo,C,Z,owner)
                    self.assertEqual(len(inverse),2)
                    self.assertEqual(inverse[0],inverse[1][::-1])
                    self.assertTrue(set(topo["iso"])<=set(C))
                    self.assertFalse(set(topo["anchors"])&set(Z))

    def test_original_BBo_projection_anchor_is_NOT_forced_into_CORE(self):
        rows=low_rows()
        cases=[z for z in rows if z["s"]==4]
        found=0
        for z in cases:
            c=source_case(2,z["scheme"])
            geo=geometry(c)
            C=set(z["original_core_source_IDs"])
            Z=set(z["deleted_original_flag_IDs"])
            for ids in z["real_positive_original_BBo_six_IDs"]:
                topo=bbo_structure(ids,c,geo,Z)
                if topo is None or all(a in C for a in topo["anchors"]):
                    continue
                inv=inverse_bbo(ids,c,geo,C,Z)
                self.assertEqual(len(inv),2)
                self.assertTrue(any(a not in C for a in topo["anchors"]))
                # Source anchor is REAL but outside C: deleting just that
                # original flag ID must kill this sixset, not relabel it.
                outside=next(a for a in topo["anchors"] if a not in C)
                self.assertEqual(inverse_bbo(ids,c,geo,C,Z|{outside}),())
                found+=1
                break
        self.assertEqual(found,2)

    def test_actual_original_D6_source_only_single_unoriented_C6(self):
        positives=[]
        for z in heavy_rows():
            if z.get("empty_tail"):
                continue
            c=source_case({2:1,4:2}[z["s"]],z["scheme"])
            for source in z["true_original_D6_six_flag_IDs_selected"]:
                with self.subTest(s=z["s"],scheme=z["scheme"],ids=source):
                    self.assertEqual(
                        classify_seven_prechecked(source,c["f"],c["g"],c["flags"]),
                        "D6")
                    inverse=inverse_d6(source,c,z["deleted_original_flag_IDs"])
                    self.assertEqual(len(inverse),1)
                    adj,owner=owned_graph(c,source)
                    self.assertIn(inverse[0],independent_cycles(adj))
                    self.assertEqual(inverse_d6(source,c,z["deleted_original_flag_IDs"],owner),
                                     inverse)
                    self.assertEqual(inverse_d6(source,c,list(source)[:1]),())
                    positives.append(source)
        self.assertEqual(len(positives),3)

    def test_genuine_original_seeded_colored_selector_C6_injection(self):
        for z in heavy_rows():
            if not z.get("true_original_D6_six_flag_IDs_selected"):
                continue
            c=source_case({2:1,4:2}[z["s"]],z["scheme"])
            for seed in z["true_original_D6_six_flag_IDs_selected"]:
                result=original_seeded_d6(c,seed,z["deleted_original_flag_IDs"])
                self.assertGreaterEqual(result["selected_source"],6)
                self.assertEqual(result["physical_edges"],2*result["selected_source"])
                self.assertGreaterEqual(result["physical_C6"],1)
                self.assertIn(tuple(seed),result["sixsets"])

    def test_actual_original_BBo_with_permuted_correlated_right_labels(self):
        z=next(z for z in low_rows() if z["s"]==4 and z["scheme"]=="reverse-line")
        C=z["original_core_source_IDs"];Z=z["deleted_original_flag_IDs"]
        for shift in (1,17):
            with self.subTest(shift=shift):
                c=source_case(2,"reverse-line",shift=shift)
                geo=geometry(c)
                result=physical_first_bbo(c,geo,C,Z)
                self.assertGreater(result["proper"],0)
                self.assertEqual(result["produced_directed"],2*len(result["sets"]))
                for ids in sorted(result["sets"])[:10]:
                    self.assertEqual(len(inverse_bbo(ids,c,geo,C,Z)),2)
                    self.assertEqual(classify_seven_prechecked(
                        ids,c["f"],c["g"],c["flags"]),"B/B-overlap")

    def test_exhaustive_original_W32_all_BBo_source_vs_image(self):
        # Independent source-first ALL 10,935 actual ORIGINAL LEFT-B
        # candidate flag sixsets, checked against the independently built
        # actual full physical path image and the historical GF5 classifier.
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                z=exhaustive_original_W32_BBo_left_B_scan(scheme)
                self.assertEqual(z["complete_original_LEFT_B_source_candidates"],10935)
                self.assertEqual(
                    (z["all_original_BBo_sixsets"],
                     z["original_BBo_sixsets_with_physical_3path"],
                     z["original_BBo_source_sixsets_without_aligned_physical_3path"]),
                    {"lex":(8,2,6),"reverse-line":(7,0,7)}[scheme])
                self.assertIsNotNone(z["first_nonimage_six_original_IDs"])
                self.assertTrue(z["original_BBo_inverse_0_or_2_for_ALL_full_source_sixsets"])
                self.assertEqual(
                    z["all_original_BBo_sixsets"],
                    z["original_BBo_sixsets_with_physical_3path"]+
                    z["original_BBo_source_sixsets_without_aligned_physical_3path"])
                model=pair_labeled_symplectic(1,scheme)
                historical=set()
                for ids,_ in selected_left_six(model):
                    if classify_seven_prechecked(
                            ids,model["left_labels"],model["right_labels"],
                            model["incidences"])=="B/B-overlap":
                        historical.add(ids)
                self.assertEqual(z["all_original_BBo_sixsets"],len(historical))
                if z["first_nonimage_six_original_IDs"] is not None:
                    ids=tuple(z["first_nonimage_six_original_IDs"])
                    self.assertIn(ids,historical)
                    case=source_case(1,scheme)
                    self.assertEqual(inverse_bbo(
                        ids,case,geometry(case),range(45)),())
                case=source_case(1,scheme)
                physical=physical_first_bbo(case,geometry(case),range(45),())
                self.assertEqual(z["original_BBo_sixsets_with_physical_3path"],
                                 len(physical["sets"]))

    def test_source_sixid_malformed_and_deletion_refusals(self):
        z=next(z for z in low_rows() if z["s"]==2 and z["scheme"]=="lex")
        c=source_case(1,"lex");geo=geometry(c)
        ids=tuple(z["real_positive_original_BBo_six_IDs"][0])
        for bad in (ids[:5],ids[:5]+ids[:1],(-1,)+ids[1:]):
            with self.assertRaises(ValueError):
                inverse_bbo(bad,c,geo,z["original_core_source_IDs"])
            with self.assertRaises(ValueError):
                inverse_d6(bad,c)
        for dropped in ids:
            self.assertEqual(
                inverse_bbo(ids,c,geo,z["original_core_source_IDs"],{dropped}),())
        with self.assertRaises(ValueError):
            source_case(3,"lex")
        with self.assertRaises(ValueError):
            source_case(2,"lex",1.5)

    def test_source_original_sixset_cannot_be_overcounted_by_c6_rotation(self):
        z=next(z for z in heavy_rows()
               if z["s"]==4 and z["scheme"]=="lex")
        c=source_case(2,"lex")
        for seed in z["true_original_D6_six_flag_IDs_selected"]:
            first=inverse_d6(seed,c)
            self.assertEqual(len(first),1)
            for rotation in range(6):
                ordered=seed[rotation:]+seed[:rotation]
                self.assertEqual(inverse_d6(ordered,c),first)
            self.assertEqual(inverse_d6(list(reversed(seed)),c),first)


if __name__=="__main__":
    unittest.main()
