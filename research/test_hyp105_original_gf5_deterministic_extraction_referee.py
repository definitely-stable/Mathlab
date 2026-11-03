"""Exact deterministic original GF5 extraction tests on actual W32/W34."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_gf5_original_sixid_flow_referee import (
    planted_original_bb_overlap,planted_original_d6,
    gf5_flow_inclusion_exclusion, _fill_f_g,
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

    def test_two_actual_overlapping_W34_original_BBo_on_same_fixed_maps(self):
        # Build TWO distinct real ORIGINAL source q--ell--p--r sextuples,
        # reusing ONE genuinely identical source owner flag i0.
        # No synthetic flags, no independent palette per sextuple.
        w=planted_original_bb_overlap(2)
        flags=w["flags"]
        V=w["V"]
        first=tuple(w["ids"])
        shared=first[3]
        usedp={flags[i][0] for i in first}
        usedl={flags[i][1] for i in first}
        pencils=[set() for _ in range(V)]
        through=[set() for _ in range(V)]
        flags_id={flag:i for i,flag in enumerate(flags)}
        for p,line in flags:
            pencils[p].add(line)
            through[line].add(p)
        collinear=[set().union(*(through[line] for line in pencils[q]))-{q}
                   for q in range(V)]
        chosen=None
        for q in range(V):
            if q in usedp:continue
            for r in range(V):
                if r in usedl or r in pencils[q]:continue
                anchors=collinear[q]&through[r]
                if len(anchors)!=1:
                    raise AssertionError("actual W34 projection not unique")
                p=next(iter(anchors))
                links=pencils[q]&pencils[p]
                if len(links)!=1:
                    raise AssertionError("genuine connecting W34 line missing")
                ell=next(iter(links))
                if p in usedp or ell in usedl:continue
                fresh_p=usedp|{q,p}
                fresh_l=usedl|{r,ell}
                match=[]
                for j,(u,line) in enumerate(flags):
                    if u not in fresh_p and line not in fresh_l:
                        match.append(j)
                        fresh_p.add(u);fresh_l.add(line)
                        if len(match)==2:break
                if len(match)==2:
                    chosen=(q,p,ell,r,tuple(match))
                    break
            if chosen is not None:break
        self.assertIsNotNone(chosen)
        q,p,ell,r,extra=chosen
        second=(flags_id[q,ell],flags_id[p,ell],flags_id[p,r],
                shared,*extra)
        self.assertEqual(len(set(second)),6)
        self.assertEqual(set(first)&set(second),{shared})
        # First source path owners are (0,1),(1,2),(2,3).
        # The second path shares its FIRST owner (0,1), and uses
        # two NEW owners (1,6),(6,7), with endpoint (0,7).
        # Its NEW FULL anchor factors are (8,9), outside path symbols.
        fs={flags[i][0]:w["f"][flags[i][0]] for i in first}
        gs={flags[i][1]:w["g"][flags[i][1]] for i in first}
        fs[q]=(0,7);fs[p]=(8,9)
        gs[r]=(0,7);gs[ell]=(8,9)
        for idx,pair in zip(extra,((1,6),(6,7))):
            u,line=flags[idx]
            fs[u]=pair;gs[line]=pair
        a=14
        f,g=_fill_f_g(V,a,fs,gs)
        family=prepare_original_family(2,f,g,(first,second))
        self.assertEqual(
            [m["kind"] for m in family["motifs"]],
            ["BBo-produced","BBo-produced"])
        out=deterministic_gf5_assign(family,max_motifs=8)
        self.assertEqual(out["selected_ORIGINAL_sixset_count"],2)
        self.assertEqual(out["baseline_exact_expected_signed_events"],
                         Fraction(2*53838,DENOM))
        self.assertEqual(out["conditioned_exact_signed_event_count"],0)
        self.assertTrue(out["zero_selected_motif_signed_events"])
        self.assertEqual(len(out["deterministic_original_palette_assignment"]),11)
        self.assertEqual(direct_original_signed_events(
            family,out["deterministic_original_palette_assignment"]),())

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
