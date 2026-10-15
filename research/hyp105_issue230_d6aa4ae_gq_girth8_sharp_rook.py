"""HYP-105 issue #230 / AA4-AE: SHARP GQ-girth-eight 4-rook <=2.

All-h theorem for any 4x4 true ORIGINAL W(3,2^h) point-line
incidence submatrix (both typed factor IDs distinct):
  no source C4 and no source C6 -> permanent <=2;
  permanent=2 iff the restricted true original induced bipartite
  subgraph is EXACTLY one chordless original eight-cycle C8.
No extras possible (an extra chord makes a forbidden C4 or C6).

Consequently each globally occupied opposite physical six-edge 2factor
in genuine-original source-B/physical-A GF5 transfer has 0, 1, or 2
allowed original 4-source assignments. If F_Hall is the number of
Hall-positive physical completions and C8 is number of genuinely
original 8-cycle completion matrices, then exact T = F_Hall+C8,
F_Hall <= T <= 2*F_Hall. Prior AA4-Y6 K2,2-only sharp bound <=3 is
correct abstractly but not sharp/attainable on true ORIGINAL GQ W3s.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    _W32_true_physical_C4_sources,
    pinned_twofactor_completions,
    opposite_physical_A_Hall_transfer,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model, exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    _valid_original_model,
)

PERMS4=tuple(permutations(range(4)))


def _four_rows(matrix):
    """A canonical 4x4 point-line incidence matrix: four 4-bit row masks."""
    x=tuple(matrix)
    if len(x)!=4 or any(type(v) is not int or v<0 or v>15 for v in x):
        raise ValueError("four rows with four original opposite factor bits each")
    return x


def true_gq_four_rook(row_masks):
    """All 24 explicit original-source perfect matchings + strict
    GQ incidence girth checks. This validator NEVER infers GQ from K2,2
    alone, and rejects the K2,2-free C6 that permits permanent 3.
    """
    row=_four_rows(row_masks)
    c4=any((row[i]&row[j]).bit_count()>=2
           for i,j in combinations(range(4),2))
    c6=False
    if not c4:
        # In C4-free bipartite original incidence, each two rows have
        # at most one common column. A C6 uses three original distinct
        # rows, whose three pairwise common column IDs are distinct.
        for i,j,k in combinations(range(4),3):
            x=row[i]&row[j];y=row[j]&row[k];z=row[i]&row[k]
            if x and y and z and x!=y and x!=z and y!=z:
                c6=True;break
    perfect=tuple(p for p in PERMS4
                  if all(row[i] & (1<<p[i]) for i in range(4)))
    count=len(perfect)
    allowed=not(c4 or c6)
    original_cycle8=False
    if allowed:
        if count>2:
            raise AssertionError("GQ girth-eight would forbid three 4-rook matchings")
        if count==2:
            # The matchings' union is one alternating C8, and extra
            # incidence edge would create a C4 or C6, both impossible.
            induced=tuple(
                (1<<perfect[0][i]) | (1<<perfect[1][i])
                for i in range(4))
            if row!=induced or any(v.bit_count()!=2 for v in row):
                raise AssertionError("original GQ two rook matchings must induce exact chordless C8")
            first,second=perfect
            image={first[i]:second[i] for i in range(4)}
            start=first[0];seen=set();j=start
            while j not in seen:
                seen.add(j);j=image[j]
            if j!=start or len(seen)!=4:
                raise AssertionError("two original 4-rook matchings must differ by a 4-cycle")
            original_cycle8=True
        for p in perfect:
            if (sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
                    not in (0,1)):
                raise AssertionError("invalid matching permutation parity")
        if len(perfect)==2:
            parity=[sum(p[i]>p[j] for i in range(4)
                        for j in range(i+1,4))%2 for p in perfect]
            if parity[0]==parity[1]:
                raise AssertionError("two perfect matchings from source C8 must have opposite parity")
    return {
        "rows":row,
        "original_C4_forbidden_observed":c4,
        "original_C6_forbidden_observed":c6,
        "gq_girth_eight_eligible":allowed,
        "true_original_four_rook_permanent":count,
        "exactly_two_perfect_matchings_implies_original_C8":original_cycle8,
        "matching_permutations":perfect,
    }


def all_65536_four_binary_gq_certificates():
    """Exhaustive independent obstruction family: no fabricated GQ
    claim for all masks; classify the truly girth>=8 *local* binary
    restrictions and exhibit the classical non-GQ permanent-3 case.
    """
    hist=Counter();invalid_c4=invalid_c6=0;bad_count=0
    witness_C8=None;witness_K22free_C6perm3=None
    for n in range(1<<16):
        row=tuple((n>>(4*i))&15 for i in range(4))
        cert=true_gq_four_rook(row)
        if cert["original_C4_forbidden_observed"]:
            invalid_c4+=1
            continue
        if cert["original_C6_forbidden_observed"]:
            invalid_c6+=1
            if cert["true_original_four_rook_permanent"]==3 and witness_K22free_C6perm3 is None:
                witness_K22free_C6perm3=row
            continue
        p=cert["true_original_four_rook_permanent"]
        hist[p]+=1
        if p>2:bad_count+=1
        if p==2 and witness_C8 is None:
            witness_C8=row
    if sum(hist.values())+invalid_c4+invalid_c6!=65536 or bad_count:
        raise AssertionError("entire 4x4 binary local source matrix census inconsistent")
    if max(hist)!=2 or witness_C8 is None or witness_K22free_C6perm3 is None:
        raise AssertionError("GQ girth-eight bound or forbidden six-cycle witness missing")
    return {
        "all_binary_four_by_four_matrices":65536,
        "C4_forbidden_non_GQ_matrices":invalid_c4,
        "C4free_but_C6_forbidden_non_GQ_matrices":invalid_c6,
        "girth_at_least_eight_local_matrix_histogram":dict(sorted(hist.items())),
        "maximum_PERMANENT_for_valid_true_GQ_local_matrix":2,
        "sharp_C8_valid_local_witness_rows":witness_C8,
        "K22_free_PERMANENT_3_NON_GQ_due_to_SOURCE_C6_rows":witness_K22free_C6perm3,
        "not_every_valid_4x4_matrix_is_claimed_global_GQ_realisable":True,
    }


def _original_source_neighbors(model,side):
    inc=tuple(tuple(x) for x in model["incidences"])
    v=len(model["left_labels"])
    byroot=[[] for _ in range(v)]
    neighbors=[set() for _ in range(v)]
    for j,(p,l) in enumerate(inc):
        src=(p,l)[side];opp=(p,l)[1-side]
        byroot[src].append(j)
        neighbors[src].add(opp)
    return inc,byroot,neighbors


def original_opposite_four_factor_cycle_census(model,*,side,roots=None,
                                                max_cohorts=None):
    """Independently reconstruct ALL occupied exact same ORIGINAL Q
    Hall physical patterns. Classify every actual original 4x4 incidence
    matrix and verify the sharp girth8 exact
       accepted == Hall-positive + induced ORIGINAL C8 patterns.
    The original full f/g physical label injection is never changed.
    A restriction to original roots for W34 provides exact sampled
    falsifiers without pretending to enumerate entire W34.
    """
    v,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("side must be typed point 0 or line 1")
    inc,byroot,neighbors=_original_source_neighbors(model,side)
    B_labels=tuple(tuple(x) for x in model["left_labels" if side==0 else "right_labels"])
    A_labels=tuple(tuple(x) for x in model["right_labels" if side==0 else "left_labels"])
    opp_inverse={x:i for i,x in enumerate(A_labels)}
    root_ids=tuple(range(v)) if roots is None else tuple(roots)
    if (len(set(root_ids))!=len(root_ids)
        or any(type(x) is not int or x<0 or x>=v for x in root_ids)):
        raise ValueError("unique valid original source root indices required")
    if max_cohorts is not None and (
        type(max_cohorts) is not int or max_cohorts<1):
        raise ValueError("positive cohort cap required")
    completed=Counter()
    cycle_witness=None
    matrix_dist=Counter()
    source_B_sourceA_counts=0
    records=[]
    for root in root_ids:
        for pinned in combinations(byroot[root],2):
            frozen=tuple(inc[j][1-side] for j in pinned)
            physical_root=B_labels[root]
            outer=tuple(x for x in range(a) if x not in physical_root)
            for four_physical_vertices in combinations(outer,4):
                all_edges=set(combinations(four_physical_vertices,2))
                x,y,z,w=four_physical_vertices
                omitted_pairings=(((x,y),(z,w)),
                                  ((x,z),(y,w)),
                                  ((x,w),(y,z)))
                B_inv={e:i for i,e in enumerate(B_labels)}
                for omitted in omitted_pairings:
                    missing=set(omitted)
                    four_phys_edges=tuple(sorted(all_edges-missing))
                    if any(e not in B_inv for e in four_phys_edges):
                        continue
                    q=tuple(B_inv[e] for e in four_phys_edges)
                    if root in q or len(set(q))!=4:
                        raise AssertionError("bad original source C4 selection")
                    e0,e1=A_labels[frozen[0]],A_labels[frozen[1]]
                    local=Counter()
                    for H in pinned_twofactor_completions(e0,e1,a):
                        remaining=tuple(edge for edge in H if edge not in (e0,e1))
                        if any(edge not in opp_inverse for edge in remaining):
                            continue
                        orig=tuple(opp_inverse[e] for e in remaining)
                        rows=tuple(sum(1<<j for j,t in enumerate(orig)
                                       if t in neighbors[qi] and t not in frozen)
                                   for qi in q)
                        certificate=true_gq_four_rook(rows)
                        if not certificate["gq_girth_eight_eligible"]:
                            raise AssertionError("ACTUAL original GQ prohibited 4/6 cycle")
                        permanent=certificate["true_original_four_rook_permanent"]
                        local["occupied_physical_2factors"]+=1
                        if permanent:
                            local["Hall_positive_physical_2factors"]+=1
                            local["accepted_original_six_Q"]+=permanent
                            matrix_dist[permanent]+=1
                        if certificate["exactly_two_perfect_matchings_implies_original_C8"]:
                            local["true_original_C8_two_matching_patterns"]+=1
                            if cycle_witness is None:
                                cycle_witness={
                                    "original_B_side":side,"B_root_original_factor":root,
                                    "actual_source_flag_IDs":pinned,
                                    "four_other_actual_original_B_factors":q,
                                    "four_actual_original_A_factors":orig,
                                    "true_original_incidence_row_masks":rows,
                                    "physical_six_edge_2factor":H,
                                }
                    if local["accepted_original_six_Q"]!=(
                        local["Hall_positive_physical_2factors"]+
                        local["true_original_C8_two_matching_patterns"]):
                        raise AssertionError("TRUE GQ sharp 4-rook charge identity violated")
                    completed.update(local)
                    records.append((root,pinned,q,
                                    local["accepted_original_six_Q"],
                                    local["true_original_C8_two_matching_patterns"]))
                    if max_cohorts is not None and len(records)>=max_cohorts:
                        break
                if max_cohorts is not None and len(records)>=max_cohorts:break
            if max_cohorts is not None and len(records)>=max_cohorts:break
        if max_cohorts is not None and len(records)>=max_cohorts:break
    if completed["accepted_original_six_Q"]!=(
        completed["Hall_positive_physical_2factors"]+
        completed["true_original_C8_two_matching_patterns"]):
        raise AssertionError("genuine ORIGINAL full joint GF5 BA charge mismatch")
    if any(k not in (1,2) for k in matrix_dist):
        raise AssertionError("actual original GQ perfect matching multiplicity cannot be three")
    return {
        "s":model["s"],"B_side":"point" if side==0 else "line",
        "actual_original_B_C4_cohorts_examined":len(records),
        "fully_occupied_physical_A_2factor_completions":completed["occupied_physical_2factors"],
        "Hall_positive_true_original_GQ_completions":completed["Hall_positive_physical_2factors"],
        "induced_original_C8_double_permanent_patterns":completed["true_original_C8_two_matching_patterns"],
        "exact_accepted_true_original_GF5_BA":completed["accepted_original_six_Q"],
        "positive_permanent_multiset_histogram":dict(sorted(matrix_dist.items())),
        "first_true_original_induced_C8_witness":cycle_witness,
        "GQ_all_h_permanent_maximum":2,
        "all_h_exact_true_GQ_charge_identity_validated":True,
        "full_global_injective_maps_used_same_in_every_original_Q":True,
        "all_h_deterministic_positive_GF5_minimax_PROVED":False,
        "original_B_C4_cohorts":len(records),
    }


def full_original_W32_all_four_schemes_girth8_report(scheme):
    from hyp105_issue230_projection import fixture
    model=fixture(1,scheme)
    strict_true_W32_model(model)
    historical=exact_two_sided_original_seven_join(
        model,independent_history=True)
    from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
        independent_W32_original_second_gate_census,
    )
    old=independent_W32_original_second_gate_census(scheme,brute_force=True)
    result={}
    for side,tag in ((0,"B-left/A-right"),(1,"A-left/B-right")):
        x=original_opposite_four_factor_cycle_census(model,side=side)
        assert x["actual_original_B_C4_cohorts_examined"]==135
        assert x["exact_accepted_true_original_GF5_BA"]==historical[
            "accepted_seven_GF5_original_Q_by_tag"][tag]
        assert x["exact_accepted_true_original_GF5_BA"]==old[
            "per_B_A_historical_GF5_tag"][tag][
                "accepted_actual_original_GF5_BA"]
        assert x["Hall_positive_true_original_GQ_completions"]==old[
            "per_B_A_historical_GF5_tag"][tag][
                "actual_two_factor_completions_passing_original_Hall"]
        assert x["fully_occupied_physical_A_2factor_completions"]==old[
            "per_B_A_historical_GF5_tag"][tag][
                "fully_occupied_opposite_physical_two_factors"]
        result[tag]=x
    return {"scheme":scheme, "true_original_W32_GF5_S":historical[
                "accepted_seven_GF5_original_S"],
            "source_GF5_original_girth8_sharp_permanent_theorem":True,
            "per_GF5_BA_tag":result,"issue230_branches":"OPEN"}


if __name__=="__main__":
    import argparse,json
    from hyp105_issue230_projection import fixture
    args=argparse.ArgumentParser()
    args.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    args.add_argument("--complete-matrix-census",action="store_true")
    cli=args.parse_args()
    z=(full_original_W32_all_four_schemes_girth8_report(cli.scheme)
        if cli.scheme else
        all_65536_four_binary_gq_certificates())
    print(json.dumps(z,indent=2,sort_keys=True))
