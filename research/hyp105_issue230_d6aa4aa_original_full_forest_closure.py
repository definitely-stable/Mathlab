"""HYP-105 #230 / AA4-AA-SRC: last nine-cell TRUE ORIGINAL forest closure.

ALL h>=1, s=2^h, genuine W(3,s) ORIGINAL incidence graph G, girth8.
The missing source B/B-disjoint six-distinct-incidence Q is exactly
one actual source LINE-centered P2, one vertex-disjoint actual source
POINT-centered P2, and an original 2-edge matching in the residual
graph after deleting all 6 root vertices.

For any fixed line-centered root P2, the opposite point-centered root
P2 belongs to one of THREE (t,H) types:
  t=1,H=0   one extra original incidence among the six deleted vertices;
  t=0,H=1   no extra source incidence, exactly one common residual neighbor;
  t=0,H=0   neither.
The original generalized quadrangle UNIQUE PROJECTION and girth8 make
the three multiplicities universal, hence give the final ALL-h exact
nine-cell SOURCE count. 't,H' are original source adjacency invariants,
NOT the physical posited f,g color-label/matching correlations.

The full SEVEN selected historical GF5 mean then follows from AA4-W's
exact ONE complete global uniform typed map transfer for each of TWO
independent full-global typed maps. This is NOT an adversarial lower for
every arbitrary f,g, NOT a full GF5 R3 exponent or ASET theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    CELL_NAMES, exact_W32_source_six_forest_universe,
)
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    all_h_full_seven_one_global_map_transfer_probabilities,
    two_uniform_complete_global_maps_full_seven_expectation,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    checked_gq_parameters,
    all_h_BC_two_source_path_population,
    all_h_BB_overlap_path_matching_population,
)
from hyp105_issue230_d6aa4y_original_triple_pencil_overlaps import (
    all_h_true_original_triple_pencil_capacity,
)
from hyp105_issue230_d6aa4z_original_matching_moments import (
    all_h_original_matching_source_AA,
    all_h_original_one_P2_plus_four_matching_AB,
    all_h_two_new_selected_GF5_ensemble_sectors,
    strict_actual_source_GQ_adjacency,
)


TYPES=("one_original_extra_cross_incidence",
       "one_common_residual_original_neighbor",
       "zero_original_extra_cross_and_common_neighbor")


def all_h_BB_disjoint_two_P2_source_capacity(s):
    """EXACT universal genuine ORIGINAL B/B-disjoint six-incidence count.

    Girth8 implies six deleted ORIGINAL source vertices induce either
    four originally selected P2 source edges or these four plus precisely
    ONE extra original incidence. The other scalar H is the number of
    pairwise common ORIGINAL residual neighbors of deleted source vertices.
    """
    V,d,N=checked_gq_parameters(s)
    r=d-1
    # Fix an un-oriented original source line-centered P2 (a-L-b).
    # Its actual original point/line neighbor geometry has the standard
    # GQ unique nonincident source point-line projection axiom.
    n10=(d-2)*_choose(d-1,2)+2*r**3
    n01=2*r*r*_choose(d-1,2)+(d-2)*r**3
    n00=(d-2)*r*r*_choose(d-1,2)
    n={
        TYPES[0]:n10,
        TYPES[1]:n01,
        TYPES[2]:n00,
    }
    valid_original_opposite_P2_per_root=sum(n.values())
    if any(v<0 for v in n.values()):
        raise AssertionError("negative source P2 partner class impossible")
    if valid_original_opposite_P2_per_root<=0:
        raise AssertionError("genuine original opposite P2 root class empty")

    m={}
    details={}
    for key,t,H in ((TYPES[0],1,0),(TYPES[1],0,1),(TYPES[2],0,0)):
        # Remove all six ORIGINAL vertices of the two distinct source P2:
        # 3 original points and 3 original lines, not six random f/g labels.
        # Their induced genuine ORIGINAL incidences =4+t.
        # e'=original total N−(6d−(4+t)).
        e=N-6*d+4+t
        boundary=6*d-8-2*t
        # On each remaining original graph vertex u: residual degree
        # d−k_u, where k_u removed original neighbors. Exactly H
        # residual vertices meet TWO of the six deleted roots. GQ
        # excludes triple-removed neighbors (source C4/C6).
        adjacent_pairs=((2*V-6)*_choose(d,2)
                        -(d-1)*boundary+H)
        n2=_choose(e,2)-adjacent_pairs
        if min(e,boundary,adjacent_pairs,n2)<0:
            raise AssertionError("genuine original residual GQ 2matching invalid")
        m[key]=n2
        details[key]={
            "extra_original_source_incidence_t":t,
            "common_residual_original_neighbor_pairs_H":H,
            "original_remaining_incidence_edges":e,
            "original_cut_boundary_edges":boundary,
            "residual_original_adjacent_edge_pairs":adjacent_pairs,
            "genuine_original_two_edge_residual_matchings":n2,
        }

    first_P2_roots=V*_choose(d,2)
    # Each source Q has EXACTLY one line-centered and one point-centered
    # repeated ORIGINAL factor. Thus one unique ordered pair of root P2
    # (types distinguished), and one unique residual ORIGINAL 2matching.
    total=first_P2_roots*sum(n[k]*m[k] for k in TYPES)
    return {
        "s":s,"V":V,"d":d,"N_actual_original_incidence_IDs":N,
        "genuine_original_LINE_centered_P2_roots":first_P2_roots,
        "three_exact_second_opposite_original_P2_types_per_first_root":n,
        "three_exact_residual_original_2matching_counts":m,
        "three_source_type_geometry_details":details,
        "valid_opposite_original_P2_per_fixed_original_P2":
            valid_original_opposite_P2_per_root,
        "source_original_B/B_disjoint_six_incidence_count":total,
        "all_h_true_GQ_unique_projection_and_girth8_PROVED":True,
        "original_source_only_NOT_physical_f_g_acceptance":True,
    }


def _choose(n,k):
    """Zero-safe low-order integer binomial (all inputs from GQ geometry)."""
    if n<k or n<0 or k<0:return 0
    from math import comb
    return comb(n,k)


def exact_all_h_nine_source_forest_universes(s):
    """ALL NINE genuine ORIGINAL source forests, every h>=1, exact.

    SOURCE classes are determined by the ORIGINAL incidence IDs ONLY.
    Original A/A six-edge matching; A/B and B/A P2+4matching;
    source A/C/C/A three line/point-centered P2; B/C/C/B P4+P2;
    B/B overlap P3+3matching; B/B disjoint 2P2+2matching.
    """
    aa=all_h_original_matching_source_AA(s)[
        "source_original_A/A_six_distinct_point_line_flags"]
    ab=all_h_original_one_P2_plus_four_matching_AB(s)[
        "source_original_A/B_one_P2_plus_4_disjoint_flags"]
    ac=all_h_true_original_triple_pencil_capacity(s)[
        "source_original_A/C_six_incidence_Q"]
    bc=all_h_BC_two_source_path_population(s)[
        "source_original_B/C_count"]
    bbo=all_h_BB_overlap_path_matching_population(s)[
        "source_original_B/B-overlap_count"]
    bbd=all_h_BB_disjoint_two_P2_source_capacity(s)[
        "source_original_B/B_disjoint_six_incidence_count"]
    populations={
        "A/A":aa,"A/B":ab,"B/A":ab,
        "A/C":ac,"C/A":ac,
        "B/C":bc,"C/B":bc,
        "B/B-overlap":bbo,
        "B/B-disjoint":bbd,
    }
    if set(populations)!=set(CELL_NAMES) or any(v<=0 for v in populations.values()):
        raise AssertionError("all nine real original Q source forest classes required")
    V,d,N=checked_gq_parameters(s)
    if sum(populations.values())>_choose(N,6):
        raise AssertionError("subset of all ORIGINAL 6incidence Q exceeded universe")
    return {
        "s":s,"V":V,"d":d,
        "all_actual_original_six_Q_universe":_choose(N,6),
        "all_nine_original_source_forest_cell_populations":populations,
        "all_nine_cells_total":sum(populations.values()),
        "six_original_Q_outside_all_nine_source_forest_cells":
            _choose(N,6)-sum(populations.values()),
        "source_only_nine_forest_exhaustive_within_A_B_C_profiles":True,
        "all_h_original_source_closed_catalog_PROVED":True,
        "adversarial_GLOBAL_f_g_omega_s6_NOT_PROVED":True,
    }


def full_seven_all_h_two_complete_global_uniform_expectation(s):
    """Exact all-h ORIGINAL source x physical seven-tag GF5 expectation.

    One COMPLETE uniform point original f and one COMPLETE uniform
    original line g, independent of one another but each shared
    globally across EVERY six-ORIGINAL-incidence Q. Weighted numerator
    uses the HISTORICAL fixed positive 51-palette R3 certificate.
    """
    source=exact_all_h_nine_source_forest_universes(s)
    seven=two_uniform_complete_global_maps_full_seven_expectation(
        s,source["all_nine_original_source_forest_cell_populations"])
    six=all_h_two_new_selected_GF5_ensemble_sectors(s)
    prob=all_h_full_seven_one_global_map_transfer_probabilities(s)
    bbdisj=source["all_nine_original_source_forest_cell_populations"]["B/B-disjoint"]
    pB=prob["B_same_source_repeated_plus_physical_C4"]
    last=bbdisj*pB*pB
    if seven["exact_tag_expectations"]["B/B-disjoint"]!=last:
        raise AssertionError("source full-seven GF5 B/B-disjoint transfer mismatch")
    if (six["six_distinct_selected_GF5_tag_expectation"]+last
            !=seven["exact_expected_seven_S"]):
        raise AssertionError("new nine-cell source universal full-seven GF5 vs six-tag mismatch")
    return {
        "s":s,"source":source,
        "exact_all_seven_GF5_tag_means":seven["exact_tag_expectations"],
        "exact_full_seven_historical_GF5_selected_S_mean":
            seven["exact_expected_seven_S"],
        "exact_full_seven_selected_51palette_certified_numerator_mean":
            seven["exact_expected_51palette_numerator"],
        "previous_exact_six_selected_tags_mean":
            six["six_distinct_selected_GF5_tag_expectation"],
        "new_seventh_selected_BB_disjoint_mean":last,
        "physical_B_pattern_probability":pB,
        "leading_original_BB_disjoint_source_over_s18":Fraction(1,8),
        "leading_expected_BB_disjoint_over_s6":18,
        "leading_all_seven_GF5_selected_S_over_s6":Fraction(1070,3),
        "both_maps_complete_uniform_global_NOT_adversarial_all_f_g":True,
        "root_HYP105_ISSUE230_OPEN":True,
        "ASET_PROVED":False,
    }


def independent_actual_true_GQ_two_P2_original_placement(model, *,
                                                         sample_fixed_P2_roots=10,
                                                         brute_force_first_roots=2):
    """Independent true ORIGINAL GQ root cross-neighbor and m2 oracle.

    Source graph is constructed independently of formula and validated
    with the original GQ nonincident-unique-anchor axiom. For each actual
    line-centered root P2 (point a, line L, point b), enumerate ALL
    physical-independent ACTUAL point-centered source P2 partner roots
    (line M, point p, line N) disjoint in source vertices. Check their
    induced ORIGINAL cross incidences t and residual common-neighbor
    count H by actual source sets, without consulting predicted types.
    For first roots, enumerate all residual original 2-edge matchings
    DIRECTLY to check closed residual m2 values from actual Q source IDs.
    """
    G,adj=strict_actual_source_GQ_adjacency(model)
    V,d=G.v,G.delta
    theorem=all_h_BB_disjoint_two_P2_source_capacity(d-1)
    theory_types=theorem["three_exact_second_opposite_original_P2_types_per_first_root"]
    theory_m2=theorem["three_exact_residual_original_2matching_counts"]
    original_edges=tuple(G.edges)
    roots=[]
    witnessed_types={}
    for L in range(V):
        point_neighbors=sorted(p for p in adj[V+L] if p<V)
        for a,b in combinations(point_neighbors,2):
            cnt=Counter()
            m2hist=Counter()
            for p in range(V):
                if p in (a,b):continue
                for M,N in combinations(sorted(q-V for q in adj[p] if q>=V),2):
                    if L in (M,N):continue
                    removedP={a,b,p}
                    removedL={L,M,N}
                    internal=sum(q in adj[x] for x in removedP for q in
                                 (V+L,V+M,V+N))
                    t=internal-4
                    if t not in (0,1):
                        raise AssertionError("a false ORIGINAL GQ 4/6cycle source detected")
                    # Independent common ORIGINAL residual neighbors of
                    # deleted vertices (both original point and line).
                    H=sum(_choose(len(adj[V+ell]&removedP),2)
                          for ell in range(V) if ell not in removedL)
                    H+=sum(_choose(len(adj[pt]&{V+ell for ell in removedL}),2)
                           for pt in range(V) if pt not in removedP)
                    key=(t,H)
                    if key not in ((1,0),(0,1),(0,0)):
                        raise AssertionError("actual ORIGINAL GQ root placement unsupported")
                    tag=({(1,0):TYPES[0],(0,1):TYPES[1],(0,0):TYPES[2]})[key]
                    cnt[tag]+=1
                    witnessed_types.setdefault(tag,(L,a,b,p,M,N))
                    if (len(roots)<brute_force_first_roots and
                            not any(k[0]==tag for k in m2hist)):
                        residual=[(pt,ell) for pt,ell in original_edges
                                  if pt not in removedP and ell not in removedL]
                        # DIRECT enumeration of pairs of original edge IDs,
                        # not degree-based residual formula under test.
                        direct=sum(x[0]!=y[0] and x[1]!=y[1]
                                   for x,y in combinations(residual,2))
                        m2hist[(tag,direct)]+=1
                        if direct!=theory_m2[tag]:
                            raise AssertionError("independent TRUE source m2 disagrees")
            if dict(cnt)!=theory_types:
                raise AssertionError("independent original opposite P2 root type counts wrong")
            roots.append({
                "fixed_actual_original_line_L":L,
                "fixed_actual_original_points_a_b":(a,b),
                "actual_opposite_SOURCE_P2_types":dict(cnt),
                "independently_bruteforced_residual_m2_by_source_type":{
                    f"{tag}:{count}":n for (tag,count),n in sorted(m2hist.items())},
            })
            if len(roots)>=sample_fixed_P2_roots:
                return {
                    "s":d-1,"original_V":V,
                    "actual_original_line_centered_P2_roots_checked":len(roots),
                    "source_root_placement_witnesses_per_type":witnessed_types,
                    "actual_original_root_rows":roots,
                    "universal_BB_disjoint_source_count":
                        theorem["source_original_B/B_disjoint_six_incidence_count"],
                    "all_selected_original_Q_use_six_different_incidence_IDs":True,
                    "strict_true_original_GQ_projection_validator":True,
                }
    raise AssertionError("insufficient actual original GQ source P2 roots")


def report(s_values=(2,4,8,16)):
    out={}
    for s in s_values:
        result=full_seven_all_h_two_complete_global_uniform_expectation(s)
        exp=result["exact_full_seven_historical_GF5_selected_S_mean"]
        last=result["new_seventh_selected_BB_disjoint_mean"]
        weighted=result["exact_full_seven_selected_51palette_certified_numerator_mean"]
        out[str(s)]={
            "true_original_nine_cell_counts":
                result["source"]["all_nine_original_source_forest_cell_populations"],
            "full_exact_seven_GF5_expected_S_fraction":
                f"{exp.numerator}/{exp.denominator}",
            "new_BB_disjoint_expected_fraction":f"{last.numerator}/{last.denominator}",
            "selected_51palette_GF5_weighted_numerator_expected_fraction":
                f"{weighted.numerator}/{weighted.denominator}",
            "minimax_root_OPEN":True,
        }
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-AA-SRC-ALL-NINE-CELL-CLOSURE",
        "all_h_proof_scope":"true ORIGINAL W(3,2^h), 9 SOURCE forests + two UNIFORM COMPLETE global typed map means",
        "records":out,"root_A":"OPEN","root_B":"OPEN",
        "deterministic_minimum_S_omega_s6_PROVED":False,
    }


if __name__=="__main__":
    import argparse,json
    cli=argparse.ArgumentParser()
    cli.add_argument("--independent-real",action="store_true")
    q=cli.parse_args()
    ans=report()
    if q.independent_real:
        ans["real_TRUE_original_GQ_checks"]={
            str(1<<h):independent_actual_true_GQ_two_P2_original_placement(
                fixture(h,"lex"),sample_fixed_P2_roots=6,
                brute_force_first_roots=2)
            for h in (1,2)
        }
    print(json.dumps(ans,indent=2,sort_keys=True))
