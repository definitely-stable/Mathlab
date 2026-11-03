"""Exact deterministic original GF5 extraction tests on actual W32/W34."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_gf5_original_sixid_flow_referee import (
    planted_original_bb_overlap,planted_original_d6,
    gf5_flow_inclusion_exclusion,
)
from hyp105_full_physical_degree_tail import planted_original_k44
from hyp105_BBo_original_core_cubic_polynomial_referee import (
    source_first_original_BBo_cubic_catalog,
)
from hyp105_original_gf5_deterministic_extraction_referee import (
    PALETTES,SIGNS,DENOM,_completion_count,_motif_conditional_mass,
    prepare_original_family,unconditional_original_mass,
    deterministic_gf5_assign,direct_original_signed_events,
    worst_case_zero_certificate_size,
)


class ExactOriginalGF5Deterministic(unittest.TestCase):
    def test_51_nonzero_checksum_4_palettes_and_first_moment_threshold(self):
        self.assertEqual(len(PALETTES),51)
        self.assertEqual(len(set(PALETTES)),51)
        self.assertEqual(len(SIGNS),10)
        self.assertTrue(all(len(p)==4 and all(1<=x<=4 for x in p)
                            and sum(p)%5==4 for p in PALETTES))
        self.assertEqual(DENOM,51**6)
        self.assertEqual(worst_case_zero_certificate_size(),324882)
        self.assertLess(Fraction(324882*54162,DENOM),1)
        self.assertGreaterEqual(Fraction(324883*54162,DENOM),1)

    def test_real_W32_BBo_exact_flow_and_deterministic_zero(self):
        w=planted_original_bb_overlap(1)
        f=prepare_original_family(1,w["f"],w["g"],[w["ids"]])
        self.assertEqual([m["kind"] for m in f["motifs"]],["BBo-produced"])
        m=f["motifs"][0]
        self.assertEqual(_motif_conditional_mass(m,{}),Fraction(53838,DENOM))
        self.assertEqual(sum(gf5_flow_inclusion_exclusion(
                         tuple((i,j) for i,_si,j,_sj in m["edges"]),plus)
                         for plus in SIGNS),53838)
        r=deterministic_gf5_assign(f)
        self.assertEqual(r["conditioned_exact_signed_event_count"],0)
        self.assertEqual(r["direct_checked_original_signed_events"],())
        self.assertEqual(len(r["deterministic_original_palette_assignment"]),6)
        self.assertEqual(r["baseline_exact_expected_signed_events"],
                         Fraction(53838,DENOM))
        self.assertEqual(direct_original_signed_events(
            f,r["deterministic_original_palette_assignment"]),())

    def test_real_W34_D6_and_BBo_independent_original_source_sextuples(self):
        for maker,kind,num in ((planted_original_d6,"D6",54162),
                                (planted_original_bb_overlap,"BBo-produced",53838)):
            w=maker(2)
            f=prepare_original_family(2,w["f"],w["g"],[w["ids"]])
            self.assertEqual([m["kind"] for m in f["motifs"]],[kind])
            self.assertEqual(_motif_conditional_mass(f["motifs"][0],{}),
                             Fraction(num,DENOM))
            r=deterministic_gf5_assign(f)
            self.assertEqual(r["conditioned_exact_signed_event_count"],0)
            self.assertLess(r["baseline_exact_expected_signed_events"],1)
            self.assertEqual(len(r["stepwise_exact_risk_trace"]),6)

    def test_overlapping_same_map_true_W34_K44_selected_source_sextuples(self):
        f,g,ids=planted_original_k44()
        catalog=source_first_original_BBo_cubic_catalog(2,f,g,ids)
        Q=tuple(catalog["sixset_supports"])
        self.assertGreaterEqual(len(Q),2)
        selected=Q[:min(4,len(Q))]
        family=prepare_original_family(2,f,g,selected)
        self.assertTrue(all(m["kind"]=="BBo-produced" for m in family["motifs"]))
        self.assertTrue(any(set(q)&set(r) for q,r in combinations(selected,2)))
        result=deterministic_gf5_assign(family,max_motifs=8)
        self.assertEqual(result["selected_ORIGINAL_sixset_count"],len(selected))
        self.assertEqual(result["baseline_exact_expected_signed_events"],
                         Fraction(len(selected)*53838,DENOM))
        self.assertEqual(result["conditioned_exact_signed_event_count"],0)
        self.assertTrue(result["zero_selected_motif_signed_events"])
        self.assertEqual(direct_original_signed_events(
            family,result["deterministic_original_palette_assignment"]),())

    def test_exact_affine_completions_vs_brute_last_unassigned_palette(self):
        w=planted_original_d6(1)
        family=prepare_original_family(1,w["f"],w["g"],[w["ids"]])
        m=family["motifs"][0]
        # This oracle counts only 51 possible last vertex palettes directly,
        # not using residual IE on the final remaining column.
        for final in (0,2,5):
            initial={i:PALETTES[(i*7+3)%51] for i in range(6) if i!=final}
            fixed=tuple(sorted(initial.items()))
            for sign in SIGNS:
                expected=0
                for pal in PALETTES:
                    combo=dict(initial);combo[final]=pal
                    sig=tuple(1 if k in sign else -1 for k in range(6))
                    if all((sig[i]*combo[i][slot_i]+
                            sig[j]*combo[j][slot_j])%5==0
                           for i,slot_i,j,slot_j in m["edges"]):
                        expected+=1
                self.assertEqual(_completion_count(m["edges"],sign,fixed),
                                 expected)

    def test_fail_closed_incomplete_illegal_or_wrong_original_sextuples(self):
        w=planted_original_bb_overlap(1)
        f=prepare_original_family(1,w["f"],w["g"],[])
        self.assertEqual(unconditional_original_mass(f),0)
        self.assertEqual(deterministic_gf5_assign(f)
                         ["conditioned_exact_signed_event_count"],0)
        with self.assertRaises(ValueError):
            prepare_original_family(1,w["f"],w["g"],
                                    [w["ids"],w["ids"]])
        with self.assertRaises(ValueError):
            prepare_original_family(1,w["f"],w["g"],[w["ids"][:5]])
        with self.assertRaises(ValueError):
            prepare_original_family(1,w["f"][:-1],w["g"],[w["ids"]])
        with self.assertRaises(ValueError):
            prepare_original_family(1,(w["f"][0],)*w["V"],w["g"],[w["ids"]])
        with self.assertRaises(ValueError):
            prepare_original_family(3,w["f"],w["g"],[w["ids"]])
        with self.assertRaises(ValueError):
            deterministic_gf5_assign(prepare_original_family(
                1,w["f"],w["g"],[w["ids"]]),max_motifs=0)


if __name__=="__main__":
    unittest.main()
