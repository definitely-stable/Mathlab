"""Independent genuine original W(3,2^h) collinearity and bad-path mass tests."""
from itertools import combinations
from math import comb, isqrt
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cy_second_moment_original_raw import (
    original_cut_frobenius_second_moment,
)
from hyp105_issue230_d6aa4cz_collinearity_badpath_mass import (
    allh_original_collinearity_badpath_arithmetic,
    original_collinear_overlap_from_actual_source_flags,
    original_cut_badpath_mass_certificate,
)


def direct_original_collinear_source_pair_from_coordinate_stars(labels, source_neighbors, dual_neighbors):
    """Independent PHYSICAL-COORDINATE-first ORIGINAL collinearity witness.

    One actual source factor per pair label. Any two distinct pair labels
    sharing a physical coordinate share EXACTLY one; summing across the
    stars cannot double-count ordered original source pairs.
    """
    a=max(max(e) for e in labels)+1
    buckets={u:tuple(i for i,e in enumerate(labels) if u in e) for u in range(a)}
    full_total=0
    per_star=[]
    V=len(labels)
    d=len(source_neighbors[0])
    source_collinearity={i:frozenset(q for j in source_neighbors[i]
                     for q in dual_neighbors[j] if q!=i) for i in range(V)}
    for u,ids in buckets.items():
        # SOURCE ORIGINAL collinearity graph, NOT a physical pair overlap surrogate
        e=sum(q in source_collinearity[p] for p in ids for q in ids if p!=q)
        star_size=len(ids)
        # Source point graph eigenvalues k_GQ=s(s+1), ±(s+1).
        s=d-1
        self_bound=s*d*star_size*star_size+d*star_size*V
        if e*V>self_bound:
            raise AssertionError("genuine original GQ eigenvalue induced-star upper violated")
        if star_size> a-1:
            raise AssertionError("physical K_a cannot contain more than a-1 pair images touching u")
        per_star.append((star_size,e))
        full_total+=e
    return {"ordered_original_source_collinear_and_physically_overlapping":full_total,
            "individual_source_star_witness":tuple(per_star)}


def direct_original_bad_full_projection_count(model):
    """Every source p and all real nonincident l, immutable original 3path."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    p_bad=l_bad=0
    for p in range(V):
        for l in range(V):
            if l in pl[p]:continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            p_bad+=not set(f[p]).isdisjoint(f[q])
            l_bad+=not set(g[l]).isdisjoint(g[l0])
    return p_bad,l_bad


def independent_original_cut_bad_mask_flag_census(model,X,Y):
    """All real ORIGINAL source flag IDs, every true nonincident anchor."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    P=tuple(p for p in range(V) if set(f[p])<=set(X))
    L=tuple(l for l in range(V) if set(g[l])<=set(Y))
    flags=tuple(model["incidences"])
    bad_left=bad_right=bad_count=bad_mass=good_mass=incident_mass=nonincident=good_positive=0
    for p in P:
        for l in L:
            c=sum(i!=p and j!=l and set(f[i])<=set(X) and set(g[j])<=set(Y)
                  and bool(set(f[i])&set(f[p])) and bool(set(g[j])&set(g[l]))
                  for i,j in flags)
            if l in pl[p]:
                incident_mass+=c
                continue
            nonincident+=1
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            b1=bool(set(f[p])&set(f[q]))
            b2=bool(set(g[l])&set(g[l0]))
            bad_left+=b1
            bad_right+=b2
            bad_count+=b1 or b2
            if b1 or b2:
                bad_mass+=c
            else:
                good_mass+=c
                good_positive+=c>0
    return bad_left,bad_right,bad_count,bad_mass,good_mass,incident_mass,nonincident,good_positive


class AA4CZTrueOriginalBadPathCollinearity(unittest.TestCase):
    def test_01_exact_allh_strong_nonincident_double_disjoint_mass_and_count(self):
        for h in range(1,76):
            z=allh_original_collinearity_badpath_arithmetic(h)
            s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(z["both_typed_nonincident_bad_P3_upper"],
                             4*s*d*(V+s*(a-1)))
            self.assertEqual(z["simple_both_typed_bad_P3_upper"],8*s*d*V)
            if h>=60:
                self.assertTrue(z["proven_for_all_h_ge_60"])
                self.assertLessEqual(s*(a-1),V)
                self.assertGreaterEqual(d*k,(1<<29)*s*s)
                self.assertGreaterEqual(k*k,8192*s*s)
                self.assertGreater(z["simplified_exponent_floor_s11half_integer"],0)
                # Exact integer Cauchy ratio gate: (badT/T)^2 <=1/4.
                self.assertGreaterEqual(d*k,4*(1<<27)*s*s)
            else:self.assertFalse(z["proven_for_all_h_ge_60"])
            if h in (24,48,56,59,60,64,75):
                print("AA4CZ_TRUE_ALLH_GATES",h,"s",s,
                      "a",a,"k",k,"bad_no_extrapolation_upper",
                      z["both_typed_nonincident_bad_P3_upper"],
                      "double_disjoint_raw_positive_lower",
                      z["simplified_exponent_floor_s11half_integer"],flush=True)

    def test_02_independent_full_source_collinearity_star_identity_W32_W34_W38(self):
        for power,schemes in ((1,("lex","S72")),(2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                direct_p=direct_original_collinear_source_pair_from_coordinate_stars(f,pl,lp)
                direct_l=direct_original_collinear_source_pair_from_coordinate_stars(g,lp,pl)
                from_module_p=original_collinear_overlap_from_actual_source_flags(f,pl,lp)
                from_module_l=original_collinear_overlap_from_actual_source_flags(g,lp,pl)
                self.assertEqual(
                    direct_p["ordered_original_source_collinear_and_physically_overlapping"],
                    from_module_p["ordered_true_original_collinear_physical_overlap"])
                self.assertEqual(
                    direct_l["ordered_original_source_collinear_and_physically_overlapping"],
                    from_module_l["ordered_true_original_collinear_physical_overlap"])
                self.assertLessEqual(
                    direct_p["ordered_original_source_collinear_and_physically_overlapping"],
                    2*(s+1)*(V+s*(a-1)))
                self.assertLessEqual(
                    direct_l["ordered_original_source_collinear_and_physically_overlapping"],
                    2*(s+1)*(V+s*(a-1)))
                print("AA4CZ_INDEPENDENT_GQ_COLLINEARITY_SPECTRAL_STAR",
                      s,scheme,"originalPOINT",from_module_p["ordered_true_original_collinear_physical_overlap"],
                      "originalLINE",from_module_l["ordered_true_original_collinear_physical_overlap"],flush=True)

    def test_03_independent_full_W32_W34_actual_gq_unique_projection_bad_count(self):
        for power,schemes in ((1,("lex","S72")),(2,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                pbad,lbad=direct_original_bad_full_projection_count(model)
                bp=original_collinear_overlap_from_actual_source_flags(f,pl,lp)
                bl=original_collinear_overlap_from_actual_source_flags(g,lp,pl)
                # Every TRUE original collinear (p,q) determines exactly
                # s nonincident genuine LINEs l with source projection q.
                # EXACT equality (not only the analytic envelope).
                self.assertEqual(pbad,s*bp["ordered_true_original_collinear_physical_overlap"])
                self.assertEqual(lbad,s*bl["ordered_true_original_collinear_physical_overlap"])
                print("AA4CZ_FULL_TRUE_ORIGINAL_PROJECTION",s,scheme,
                      "point_bad",pbad,"line_bad",lbad,"collinear_source_factors",
                      bp["ordered_true_original_collinear_physical_overlap"],flush=True)

    def test_04_complete_W32_original_every_anchor_doubled_bad_mass_vs_direct_flags(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,*_=_validated_original(model)
            k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))),
                  (tuple(range(1,k+1)),tuple(range(a-k-1,a-1))))
            for ci,(X,Y) in enumerate(cuts):
                c=original_cut_badpath_mass_certificate(model,X,Y)
                direct=independent_original_cut_bad_mask_flag_census(model,X,Y)
                expect=(c["actual_bad_left_P3"],c["actual_bad_right_P3"],
                        c["actual_bad_union_nonincident_P3"],
                        c["actual_original_raw_bad_path_mass"],
                        c["actual_original_raw_good_nonincident_double_disjoint_mass"],
                        c["actual_original_raw_incident_path_mass"],
                        c["actual_genuine_original_nonincident_cut_P3"],
                        c["actual_original_double_disjoint_nonincident_raw_positive_P3"])
                self.assertEqual(direct,expect)
                self.assertLessEqual(c["actual_bad_union_nonincident_P3"],
                                     c["source_genuine_projection_bad_anchor_upper_from_collinearity"])
                self.assertLessEqual(c["actual_original_raw_bad_path_mass"]**2,
                                     c["actual_bad_union_nonincident_P3"]*c["all_original_raw_Q"])
                print("AA4CZ_INDEPENDENT_FULL_ORIGINAL_W32",scheme,ci,
                      "rawT",c["all_original_raw_T"],
                      "bad_mass",c["actual_original_raw_bad_path_mass"],
                      "good_nonincident_mass",c["actual_original_raw_good_nonincident_double_disjoint_mass"],
                      "good_nonincident_positive",
                      c["actual_original_double_disjoint_nonincident_raw_positive_P3"],flush=True)

    def test_05_actual_original_W34_W38_two_typed_global_maps_varied_cuts(self):
        for power,schemes in ((2,("lex","random")),(3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,*_=_validated_original(model)
                k=a//2
                cuts=((tuple(range(k)),tuple(range(a-k,a))),
                      (tuple(range(a-k,a)),tuple(range(k)))) if power==2 else (
                      (tuple(range(k)),tuple(range(a-k,a))),)
                for ci,(X,Y) in enumerate(cuts):
                    c=original_cut_badpath_mass_certificate(model,X,Y)
                    z=original_cut_frobenius_second_moment(
                        model,X,Y,independent_flag_pair_oracle=True)
                    self.assertEqual(c["all_original_raw_T"],z["original_raw_spoke_first_moment_T"])
                    self.assertEqual(c["all_original_raw_Q"],z["original_raw_spoke_second_moment_Q"])
                    self.assertEqual(c["all_original_raw_Q"],z["independent_original_source_flag_pair_Gram_Q"])
                    self.assertLessEqual(c["actual_bad_left_P3"],
                        s*c["source_collinear_physical_overlap_ordered_POINT"])
                    self.assertLessEqual(c["actual_bad_right_P3"],
                        s*c["source_collinear_physical_overlap_ordered_LINE"])
                    self.assertEqual(c["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
                    print("AA4CZ_TRUE_ORIGINAL_MANY_ANCHOR",s,scheme,ci,
                          "bad",c["actual_bad_union_nonincident_P3"],
                          "original_bad_raw_mass",c["actual_original_raw_bad_path_mass"],
                          "genuine_double_disjoint_nonincident_raw_mass",
                          c["actual_original_raw_good_nonincident_double_disjoint_mass"],
                          "genuine_double_disjoint_nonincident_RAWpositive",
                          c["actual_original_double_disjoint_nonincident_raw_positive_P3"],flush=True)

    def test_06_failclosed_original_source_injection_geometry_and_dyadic(self):
        for h in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                allh_original_collinearity_badpath_arithmetic(h)
        model=fixture(1,"lex")
        for X,Y in (((0,0,1),(3,4,5)),((0,1,9),(3,4,5)),
                    ((0,1),(3,4,5)),((0,1,2),(3,4,True))):
            with self.assertRaises(ValueError):
                original_cut_badpath_mass_certificate(model,X,Y)
        broken=dict(model)
        f=list(model["left_labels"])
        f[0]=f[1]
        broken["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            original_cut_badpath_mass_certificate(broken)


if __name__=="__main__":
    unittest.main()
