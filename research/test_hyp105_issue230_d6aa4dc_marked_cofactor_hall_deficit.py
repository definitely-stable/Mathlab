"""Independent actual ORIGINAL 3x3 Hall cofactor and BBo GF5 census gates."""
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
    original_BBo_exact_three_matching_transfer,
)
from hyp105_issue230_d6aa4db_occupied_c4_spoke_flag_mass import (
    original_cut_occupied_c4_source_flag_certificate,
)
from hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit import (
    original_three_by_three_cofactor_certificate,
    exact_original_C4_marked_cofactor_energy,
    allh_original_marked_cofactor_dichotomy_arithmetic,
)


def independent_all_possible_source_matchings(rows):
    return tuple(t for t in permutations(range(3))
                 if all(rows[i][t[i]] for i in range(3)))


def no_genuine_original_4cycle(rows):
    return all(sum(rows[i][j] and rows[ii][j] for j in range(3))<2
               for i,ii in combinations(range(3),2))


def direct_original_fixed_anchor_marked_source_flag_mass(model, p,l):
    """Independent canonical source 6flag brute, no AA4-DC cofactor algorithm."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    path=original_nonincident_threepath(p,l,pl,lp)
    q,l0=path[1][0],path[0][1]
    if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
        return {"T":0,"E":0,"D":0,"U":0,"C4pairs":0}
    pf={tuple(sorted(e)):i for i,e in enumerate(f)}
    lg={tuple(sorted(e)):j for j,e in enumerate(g)}
    pt=c4_completions_from_single_and_doubled(f[p],f[q],pf,a)
    lt=c4_completions_from_single_and_doubled(g[l],g[l0],lg,a)
    T=E=D=U=pairs=0
    for points in pt:
        for lines in lt:
            pairs+=1
            # Independent genuine original source index/permutation matching
            matchings=tuple(p for p in permutations(lines)
                            if all(j in pl[i] for i,j in zip(points,p)))
            if len(matchings)>1:
                raise AssertionError("original GQ 3x3 has multiple distinct true source perfect matchings")
            U+=bool(matchings)
            # SPOKE is an image incident with a physical endpoint of
            # the original single source factor. The center is not.
            pp=tuple(i for i in points if bool(set(f[i])&set(f[p])))
            ll=tuple(j for j in lines if bool(set(g[j])&set(g[l])))
            if len(pp)!=2 or len(ll)!=2:
                raise AssertionError("not a real source physical C4 triple")
            marked=sum(j in pl[i] for i in pp for j in ll)
            ext=sum(i in pp and j in ll
                    for matching in matchings for i,j in zip(points,matching))
            T+=marked
            E+=ext
            D+=marked-ext
    return {"T":T,"E":E,"D":D,"U":U,"C4pairs":pairs}


def sample_original_anchors(model,count,cut=None):
    s,V,a,f,g,pl,lp=_validated_original(model)
    X,Y=(None,None) if cut is None else cut
    out=[]
    for p in range(V):
        if X is not None and not set(f[p])<=set(X):continue
        for l in range(V):
            if l in pl[p] or Y is not None and not set(g[l])<=set(Y):
                continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
            out.append((p,l))
            if len(out)>=count:return tuple(out)
    return tuple(out)


class AA4DCActualOriginalMarkedCofactor(unittest.TestCase):
    def test_01_exhaustive_512_binary_forests_independent_Hall_and_marks(self):
        accepted=positive=failmarked=all_nonisolated_fails=0
        for bits in range(1<<9):
            rows=tuple(tuple((bits>>(3*i+j))&1 for j in range(3)) for i in range(3))
            matchings=independent_all_possible_source_matchings(rows)
            if len(matchings)>1 or not no_genuine_original_4cycle(rows):
                continue
            z=original_three_by_three_cofactor_certificate(rows)
            accepted+=1
            mark=sum(rows[i][j] for i in (0,1) for j in (0,1))
            matched=sum(i in (0,1) and matching[i] in (0,1)
                        for matching in matchings for i in range(3))
            self.assertEqual(z["true_original_3x3_permanent"],len(matchings))
            self.assertEqual(z["original_C4_pair_spoke_spoke_marked_flags"],mark)
            self.assertEqual(z["true_original_2x2_cofactor_extendible_spoke_flags"],matched)
            self.assertEqual(z["original_source_Hall_rejected_spoke_cross_flags"],mark-matched)
            positive+=bool(matchings)
            failmarked+=not matchings and mark>0
            all_nonisolated_fails+=(
                not matchings and mark>0 and
                all(sum(row)>=1 for row in rows)
                and all(sum(rows[i][j] for i in range(3))>=1 for j in range(3))
            )
            if not matchings:
                h=z["minimal_true_original_Hall_deficiency"]
                self.assertLess(len(h["original_source_line_neighbor_columns"]),
                                len(h["original_source_point_row_subset"]))
            else:self.assertIsNone(z["minimal_true_original_Hall_deficiency"])
        self.assertGreater(accepted,100)
        self.assertGreater(positive,0)
        self.assertGreater(failmarked,0)
        self.assertGreater(all_nonisolated_fails,0)
        # An acyclic, all-six-nonisolated, actual SOURCE graph candidate
        # has true marked original flags and ZERO 3matching due Hall.
        forest=((1,0,0),(1,0,0),(1,1,1))
        z=original_three_by_three_cofactor_certificate(forest)
        self.assertEqual(z["true_original_3x3_permanent"],0)
        self.assertEqual(z["original_C4_pair_spoke_spoke_marked_flags"],2)
        self.assertEqual(len(z["minimal_true_original_Hall_deficiency"]["original_source_point_row_subset"]),2)
        print("AA4DC_ALL_TRUE_GQ_ADMISSIBLE_3X3_FORESTS",
              "total",accepted,"perfect_matching",positive,
              "marked_positive_but_no_matching",failmarked,
              "all_six_nonisolated_still_no_matching",all_nonisolated_fails,flush=True)

    def test_02_exact_dyadic_h1_110_original_marked_matching_deficit_dichotomy(self):
        for h in range(1,111):
            z=allh_original_marked_cofactor_dichotomy_arithmetic(h)
            s=z["s"]
            self.assertEqual(z["V"],(s+1)*(s*s+1))
            self.assertLess(comb(z["a"]-1,2),z["V"])
            self.assertGreaterEqual(comb(z["a"],2),z["V"])
            if h>=96:
                self.assertTrue(z["allh_gate_h_ge_96"])
                self.assertEqual(z["original_minimum_marked_source_flag_mass_denominator"],1<<15)
                self.assertEqual(z["either_true_original_BBo_U_lower_denominator"],1<<17)
                self.assertEqual(z["or_original_marked_Hall_deficit_D_lower_denominator"],1<<16)
                for U,D in ((0,s**7//(1<<15)+1),
                            (s**7//(1<<17)+1,0)):
                    self.assertTrue((1<<17)*U>=s**7 or (1<<16)*D>=s**7)
            else:self.assertFalse(z["allh_gate_h_ge_96"])
            self.assertTrue(z["uniform_positive_sevenclass_S_not_proven"])
            if h in (60,95,96,100,110):
                print("AA4DC_DYADIC_GF5_UNCLOSED_DICHOTOMY",
                      h,"root","OPEN_WITH_FORMAL_BLOCKER",
                      "minimum_true_marked_flag_mass",s**7//(1<<15),
                      flush=True)

    def test_03_true_original_W32_all_cut_complete_C4_pair_census_independent_parent(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))),
                  (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))))
            for ci,(X,Y) in enumerate(cuts):
                z=exact_original_C4_marked_cofactor_energy(
                    model,point_cut=X,line_cut=Y)
                canonical=original_BBo_exact_three_matching_transfer(
                    model,point_cut=X,line_cut=Y,collect_original_Q=False)
                db=original_cut_occupied_c4_source_flag_certificate(model,X,Y)
                self.assertEqual(z["source_original_3x3_perfect_matching_BBo_U"],
                                 canonical["historical_accepted_original_BBo_sixflag_Q"])
                self.assertEqual(z["C4_pairs_examined"],
                                 canonical["paired_two_sided_C4_templates"])
                self.assertGreaterEqual(z["source_occupied_C4_source_cross_flag_mark_mass_T"],
                                        db["both_occupied_physical_C4_TRUE_original_cross_source_flag_mass"])
                self.assertEqual(
                    z["distinct_original_spoke_cross_source_flags_with_two_actual_C4_witnesses"],
                    db["both_occupied_physical_C4_TRUE_original_cross_source_flag_mass"])
                self.assertEqual(
                    z["source_occupied_C4_source_cross_flag_mark_mass_T"],
                    z["source_2x2_cofactor_extendible_flag_mass_E"]+
                    z["source_Hall_defective_C4_spoke_flag_mass_D"])
                print("AA4DC_ALL_REAL_ORIGINAL_W32",scheme,ci,
                      "physical_C4_pairs",z["C4_pairs_examined"],
                      "marked_T",z["source_occupied_C4_source_cross_flag_mark_mass_T"],
                      "extendible_E",z["source_2x2_cofactor_extendible_flag_mass_E"],
                      "Hall_defect_D",z["source_Hall_defective_C4_spoke_flag_mass_D"],
                      "historical_original_BBo_Q",z["source_original_3x3_perfect_matching_BBo_U"],
                      flush=True)

    def test_04_true_original_W34_full_C4_subset_vs_independent_permutation(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            k=a//2;cut=(tuple(range(k)),tuple(range(a-k,a)))
            anchors=sample_original_anchors(model,8,cut)
            self.assertGreaterEqual(len(anchors),4)
            z=exact_original_C4_marked_cofactor_energy(model,anchor_pairs=anchors,
                                                       point_cut=cut[0],line_cut=cut[1])
            canonical=original_BBo_exact_three_matching_transfer(
                model,anchor_pairs=anchors,point_cut=cut[0],line_cut=cut[1],
                collect_original_Q=False)
            self.assertEqual(z["source_original_3x3_perfect_matching_BBo_U"],
                             canonical["historical_accepted_original_BBo_sixflag_Q"])
            self.assertEqual(z["C4_pairs_examined"],canonical["paired_two_sided_C4_templates"])
            direct={"T":0,"E":0,"D":0,"U":0,"C4pairs":0}
            for p,l in anchors:
                x=direct_original_fixed_anchor_marked_source_flag_mass(model,p,l)
                for key in direct:direct[key]+=x[key]
            for key,actual in (
                ("T","source_occupied_C4_source_cross_flag_mark_mass_T"),
                ("E","source_2x2_cofactor_extendible_flag_mass_E"),
                ("D","source_Hall_defective_C4_spoke_flag_mass_D"),
                ("U","source_original_3x3_perfect_matching_BBo_U"),
                ("C4pairs","C4_pairs_examined")
            ):
                self.assertEqual(z[actual],direct[key])
            self.assertGreater(z["C4_pairs_examined"],0)
            self.assertGreater(z["source_occupied_C4_source_cross_flag_mark_mass_T"],0)
            self.assertGreater(z["source_Hall_defective_C4_spoke_flag_mass_D"],0)
            print("AA4DC_REAL_ORIGINAL_W34",scheme,
                  "anchors",len(anchors),"C4_pairs",z["C4_pairs_examined"],
                  "T",direct["T"],"E",direct["E"],"D",direct["D"],"U",direct["U"],
                  "Hall_failure",z["first_actual_original_marked_C4_Hall_failure"],
                  flush=True)

    def test_05_true_original_W38_stated_PARTIAL_pair_sampling_not_promoted(self):
        for scheme in ("lex","random"):
            model=fixture(3,scheme)
            s,V,a,f,g,pl,lp=_validated_original(model)
            anchors=sample_original_anchors(model,4)
            self.assertEqual(len(anchors),4)
            x=exact_original_C4_marked_cofactor_energy(model,anchor_pairs=anchors,
                                                       max_triples_per_side=8)
            self.assertTrue(x["PR_scope_partial_source_C4_sampling"])
            self.assertLessEqual(x["C4_pairs_examined"],4*8*8)
            self.assertTrue(x["mathematical_exact_identity_T_equals_D_plus_E"])
            self.assertTrue(x["mathematical_exact_original_BBo_le_E_le_2BBo"])
            self.assertEqual(x["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            print("AA4DC_REAL_ORIGINAL_W38_SCOPED_PARTIAL",scheme,
                  "C4pairs",x["C4_pairs_examined"],
                  "T",x["source_occupied_C4_source_cross_flag_mark_mass_T"],
                  "D",x["source_Hall_defective_C4_spoke_flag_mass_D"],
                  "U",x["source_original_3x3_perfect_matching_BBo_U"],flush=True)

    def test_06_false_original_source_inputs_cuts_caps_fail_closed(self):
        for rows in (((1,0,0),(0,0,0)),((1,0,0),(0,0,0),(1,0,2)),
                     ((True,0,0),(0,0,0),(0,0,0))):
            with self.assertRaises(ValueError):
                original_three_by_three_cofactor_certificate(rows)
        with self.assertRaises(ValueError):
            original_three_by_three_cofactor_certificate(((1,1,0),(1,1,0),(0,0,1)))
        model=fixture(1,"lex")
        for value in (True,0,-1,1.5):
            with self.assertRaises(ValueError):
                exact_original_C4_marked_cofactor_energy(
                    model,max_triples_per_side=value,anchor_pairs=((0,0),))
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(3,4,True))):
            with self.assertRaises(ValueError):
                exact_original_C4_marked_cofactor_energy(
                    model,point_cut=X,line_cut=Y,anchor_pairs=())
        dup=dict(model);p=list(model["left_labels"]);p[1]=p[0];dup["left_labels"]=tuple(p)
        with self.assertRaises(ValueError):
            exact_original_C4_marked_cofactor_energy(dup,anchor_pairs=())


if __name__=="__main__":
    unittest.main()
