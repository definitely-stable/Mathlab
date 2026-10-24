"""Two independent original W3 historical GF5 source sixflag bridge referees."""

from collections import Counter,defaultdict
from itertools import combinations
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4dg_two_external_A_bridge import (
    original_two_external_A_completion_catalogue,A_SIDE_POSITIVE_CLASSES,
)
from hyp105_issue230_d6aa4dh_constant_multiplicity_inverse import (
    inverse_original_typed_ABC_C4_representations,
    inverse_true_original_historical_A_Q_bridge_certificate,
    allh_original_A_bridge_reuse_caps,
    ORIGINAL_HISTORICAL_A_CLASS_CAPS,
)


def physical_six_original_factors_into_Qids(labels,edges):
    inverse={tuple(e):i for i,e in enumerate(labels)}
    return tuple(inverse[tuple(sorted(e))] for e in edges)


def independent_forward_original_A_source_Q_provenance(model,
                                                      limit_reservoirs=12):
    """INDEPENDENT forward AA4-DG ORIGINAL source 6-ID C4-pair census.

    Source IMMUTABLE incidence flags generated DIRECTLY from real
    P x L original SOURCE factor sets; no inverse helper called.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    inc=tuple(model["incidences"])
    source_flag={(i,j):z for z,(i,j) in enumerate(inc)}
    pi={e:i for i,e in enumerate(f)}
    li={e:i for i,e in enumerate(g)}
    Q_provenance=defaultdict(set)
    classes=Counter()
    pairs_examined=0
    for p in range(V):
        for l in range(V):
            if l in pl[p]:continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            PT=c4_completions_from_single_and_doubled(f[p],f[q],pi,a)
            LT=c4_completions_from_single_and_doubled(g[l],g[l0],li,a)
            for pc in PT:
                for lc in LT:
                    if pairs_examined>=limit_reservoirs:
                        return Q_provenance,classes,pairs_examined
                    pairs_examined+=1
                    P5=tuple(sorted((p,q,*pc)))
                    L5=tuple(sorted((l,l0,*lc)))
                    PA=original_two_external_A_completion_catalogue(f,p,q,pc)
                    LA=original_two_external_A_completion_catalogue(g,l,l0,lc)
                    # factor-side A combinations from ACTUALLY OCCUPIED
                    # physical images; B/C sides kept original-local.
                    source_sets=(
                        ((P,L5) for P in PA),
                        ((P5,L) for L in LA),
                        ((P,L) for P in PA for L in LA),
                    )
                    accepted_here=set()
                    for candidates in source_sets:
                        for P,L in candidates:
                            flag_ids=tuple(source_flag[i,j] for i in P for j in L
                                           if (i,j) in source_flag)
                            for six in combinations(flag_ids,6):
                                Q=tuple(sorted(six))
                                if Q in accepted_here:continue
                                kind=classify_seven_all_a_original_Q(Q,f,g,inc)
                                if kind in A_SIDE_POSITIVE_CLASSES:
                                    accepted_here.add(Q)
                                    Q_provenance[Q].add((p,l,tuple(pc),tuple(lc)))
                                    classes[kind]+=1
    return Q_provenance,classes,pairs_examined


class AA4DHConstantOriginalSourceInverse(unittest.TestCase):
    def test_01_exact_full_K6_A_hexagon_vs_two_triangles_B_C_inverse_bounds(self):
        labels=tuple(combinations(range(6),2))
        A6=physical_six_original_factors_into_Qids(
            labels,((0,1),(1,2),(2,3),(3,4),(4,5),(0,5)))
        A22=physical_six_original_factors_into_Qids(
            labels,((0,1),(1,2),(0,2),(3,4),(4,5),(3,5)))
        B5=physical_six_original_factors_into_Qids(
            labels,((0,1),(1,2),(2,3),(0,3),(4,5)))
        C3=physical_six_original_factors_into_Qids(
            labels,((0,1),(2,3),(4,5)))
        cases=(
            ("A-hexagon",A6,"A",24),
            ("A-triangles",A22,"A",0),
            ("B-C4",B5[:-1]+(B5[-1],B5[-1]),"B",4),
            ("C-three-pairs",tuple(i for x in C3 for i in (x,x)),"C",24),
        )
        for name,src,profile,count in cases:
            z=inverse_original_typed_ABC_C4_representations(labels,src)
            self.assertEqual(z["profile"],profile)
            self.assertEqual(len(z["representations"]),count)
            for doubled,base,triple in z["representations"]:
                images=tuple(labels[i] for i in (base,*triple))
                deg=Counter(v for e in images for v in e)
                self.assertEqual(len(deg),4)
                self.assertEqual(set(deg.values()),{2})
                self.assertFalse(set(labels[doubled])&set(deg))
            print("AA4DH_PHYSICAL_SOURCE_INVERSE",name,"actual",count,flush=True)
        caps=allh_original_A_bridge_reuse_caps()
        self.assertEqual(caps["D6"],576)
        self.assertEqual(caps["A-left/B-right"],96)
        self.assertEqual(caps["B-left/A-right"],96)
        self.assertEqual(caps["C/A"],576)

    def test_02_independent_brute_all_source_K6_C4_representations_for_A_B_C(self):
        labels=tuple(combinations(range(6),2))
        inv={e:i for i,e in enumerate(labels)}
        support=(
            tuple(inv[e] for e in ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))),
            tuple(inv[e] for e in ((0,1),(1,2),(2,3),(0,3),(4,5))),
            tuple(inv[e] for e in ((0,1),(2,3),(4,5))),
        )
        multisets=(support[0], support[1]+(support[1][-1],),
                   tuple(z for i in support[2] for z in (i,i)))
        all_ids=range(len(labels))
        # BRUTE every original-source physical 4cycle, doubled edge
        # and 3-factor C4 triad; check cardinalities and exact SOURCE
        # factor-appearance intersection conditions, independent of
        # A/B/C mathematical inverse implementations.
        for src in multisets:
            seq=set(src)
            brute=set()
            for doubled in seq:
                for base in all_ids:
                    for triad in combinations(tuple(i for i in all_ids if i!=base),3):
                        cycle=(base,*triad)
                        edges=[labels[i] for i in cycle]
                        deg=Counter(v for e in edges for v in e)
                        if len(deg)!=4 or set(deg.values())!={2}:continue
                        if any(set(labels[doubled])&set(edge) for edge in edges):continue
                        local={base,doubled,*triad}
                        # A typed inverse requires 4 local source
                        # factors in 6-Q support; B/C match the
                        # EXACT historical six-factor appearances
                        # supplied by the physical C4+ doubled pair.
                        source_mult=Counter(src)
                        if len(source_mult)==6:
                            condition=(doubled in seq and len(local&seq)==4 and
                                       len(local-seq)==1 and
                                       len(seq-local)==2)
                        elif len(source_mult)==5:
                            condition=(source_mult[doubled]==2 and
                                       len(seq&local)==5)
                        else:
                            condition=(source_mult[doubled]==2 and
                                       sum(source_mult[k]==2 for k in local)==3)
                        if condition:
                            brute.add((doubled,base,tuple(sorted(triad))))
            z=inverse_original_typed_ABC_C4_representations(labels,src)
            self.assertEqual(set(z["representations"]),brute)
            print("AA4DH_INDEPENDENT_DIRECT_PHYSICAL_4CYCLE_BRUTE",
                  z["profile"],len(brute),flush=True)

    def test_03_TRUE_original_W32_lex_S72_forward_inverse_historical_six_IDs(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            Qw,classes,pairs=independent_forward_original_A_source_Q_provenance(
                model,limit_reservoirs=12)
            self.assertEqual(pairs,12)
            self.assertGreater(len(Qw),0)
            seen=Counter()
            for Q,provenance in Qw.items():
                inv=inverse_true_original_historical_A_Q_bridge_certificate(model,Q)
                self.assertLessEqual(
                    inv["original_source_ACTUAL_nonincident_P3_paired_C4_reuse_count"],
                    ORIGINAL_HISTORICAL_A_CLASS_CAPS[
                        inv["historical_true_original_GF5_label"]])
                if not provenance.issubset(set(inv["actual_true_original_source_P3_C4_representations"])):
                    self.fail("AA4DH SOURCE INVERSE LOST ORIGINAL Q "
                        +repr({"scheme":scheme,"source_Q":Q,
                               "class":inv["historical_true_original_GF5_label"],
                               "source_point_profile":inv["original_POINT_side_profile"],
                               "source_line_profile":inv["original_LINE_side_profile"],
                               "point_inverse_n":inv["POINT_inverse_occupied_original_C4_representation_count"],
                               "line_inverse_n":inv["LINE_inverse_occupied_original_C4_representation_count"],
                               "forward_missing":sorted(provenance-
                                   set(inv["actual_true_original_source_P3_C4_representations"])),
                               "source_expected_typed_inversions":tuple(
                                  (original_nonincident_threepath(p,l,
                                       _validated_original(model)[5],
                                       _validated_original(model)[6])[1][0],
                                   p,pc,
                                   original_nonincident_threepath(p,l,
                                       _validated_original(model)[5],
                                       _validated_original(model)[6])[0][1],
                                   l,lc)
                                  for p,l,pc,lc in sorted(provenance)[:3]),
                               "inverse_POINT_first":inverse_original_typed_ABC_C4_representations(
                                  _validated_original(model)[3],
                                  tuple(model["incidences"][z][0] for z in Q)
                                  )["representations"][:24],
                               "inverse_LINE_first":inverse_original_typed_ABC_C4_representations(
                                  _validated_original(model)[4],
                                  tuple(model["incidences"][z][1] for z in Q)
                                  )["representations"][:24],
                               "inverse_first":inv["actual_true_original_source_P3_C4_representations"][:5]}))
                self.assertLessEqual(len(provenance),
                    inv["original_source_ACTUAL_nonincident_P3_paired_C4_reuse_count"])
                seen[inv["historical_true_original_GF5_label"]]+=len(provenance)
            self.assertEqual(dict(seen),dict(classes))
            print("AA4DH_REAL_ORIGINAL_W32_FORWARD_INVERSE_C6_BRIDGE",scheme,
                  "examined_paired_C4",pairs,
                  "distinct_TRUE_source_six_ID_Q",len(Qw),
                  "historical_A_classes",dict(classes),flush=True)

    def test_04_TRUE_original_W34_selected_source_sixflags_positive_not_synthetic(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            Qw,classes,pairs=independent_forward_original_A_source_Q_provenance(
                model,limit_reservoirs=3)
            self.assertEqual(pairs,3)
            for Q,p in Qw.items():
                z=inverse_true_original_historical_A_Q_bridge_certificate(model,Q)
                self.assertTrue(p.issubset(
                    set(z["actual_true_original_source_P3_C4_representations"])))
            print("AA4DH_W34_GENUINE_FIXED_GLOBAL_MAP_TRUE_SOURCE_Q",
                  scheme,"C4pairs",pairs,"Q",len(Qw),
                  "class",dict(classes),flush=True)

    def test_05_real_W38_partial_and_allh_source_factor_profile_bound(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            Qw,classes,pairs=independent_forward_original_A_source_Q_provenance(
                model,limit_reservoirs=2)
            self.assertEqual(pairs,2)
            for Q,provenance in Qw.items():
                inv=inverse_true_original_historical_A_Q_bridge_certificate(model,Q)
                self.assertTrue(provenance.issubset(
                    set(inv["actual_true_original_source_P3_C4_representations"])))
            print("AA4DH_GENUINE_ORIGINAL_W38_STRICTLY_PARTIAL",scheme,
                  "C4pairs",pairs,"original_Q_count",len(Qw),flush=True)

    def test_06_failclosed_invalid_source_Q_and_fake_global_injection(self):
        model=fixture(1,"lex")
        s,V,a,f,g,pl,lp=_validated_original(model)
        for bogus in ((0,0,1,2,3,4),(0,1,2,3,4,True),
                      (0,1,2,3,4,V*(s+1))):
            with self.assertRaises(ValueError):
                inverse_true_original_historical_A_Q_bridge_certificate(model,bogus)
        invalid_mult=((0,0,0,1,2,3),(0,1,2,3,4),("1",1,2,3,4,5))
        for q in invalid_mult:
            with self.assertRaises(ValueError):
                inverse_original_typed_ABC_C4_representations(f,q)
        forged=list(f);forged[0]=forged[1]
        with self.assertRaises(ValueError):
            inverse_original_typed_ABC_C4_representations(forged,(0,1,2,3,4,5))
        fake=dict(model);fake["left_labels"]=tuple(forged)
        with self.assertRaises(ValueError):
            inverse_true_original_historical_A_Q_bridge_certificate(
                fake,(0,1,2,3,4,5))


if __name__=="__main__":
    unittest.main()
