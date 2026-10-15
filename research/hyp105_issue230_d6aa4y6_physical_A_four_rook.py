"""HYP-105 / issue #230 / D6-AA4-Y6: exact SAME-Q ORIGINAL B/A
opposite physical A gate as a 4x4 forbidden-C4 rook permanent.

ALL-h theorem: Fix a real ORIGINAL repeated point/line source p, two
distinct actual original root incidences (p,l1),(p,l2), a physically
realized B-root complementary C4 on four other globally labeled source
factors q1..q4, and the one COMPLETE opposite physical map g.
A positive historical B/A GF5 Q is uniquely given by a 2-regular
six-edge physical 2-factor H containing g(l1),g(l2), all four other
edges of H occupied by actual original opposite source factors, and
a perfect matching between q1..q4 and those four opposite factors in
the REAL ORIGINAL incidence graph.

The selected 4x4 0/1 original GQ incidence submatrix has no K2,2
because true GQ incidence girth is eight. Its permanent <=3 (not 4!=24).
The exact historical per-root C4 physical A acceptance is the SUM of
these 4x4 permanents over all physical 2-factors H with the pinned pair
present and all four other physical edges occupied. Physical # such H
in FULL K_a is 7*C(a-3,3) for adjacent pinned edges and
14*C(a-4,2) for disjoint pinned edges. Hence an ALL-h CONDITIONAL
upper of 3 times that physical capacity PER realized B-root C4.
No positive lower on the opposite physical-A acceptance and no
all-h S=Omega(s^6) root proof.

FINITE genuine W32: 45 rooted true source two-flag cohorts x 3
complementary B-source C4 patterns x 2 original typed sides,
all complete globally injected S68/S72/lex/reverse maps.
Independently verify the exact 2factor×permanent identity against
Y5's different literal 3^4 original-incidence Q enumeration and
AA4-Q historical GF5 full 62,370 half original six-ID join.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb
import argparse
import json

from hyp105_issue230_d6aa4y3_original_source_star_capacity import original_parameters
from hyp105_issue230_d6aa4y5_rooted_BA_forest_matching import (
    _physical_root_C4_source_patterns,genuine_W32_rooted_BA_forest)


PERMS4=tuple(permutations(range(4)))


def k22_free_four_rows(rows):
    """4 given sets of actual ORIGINAL source-factor neighbors."""
    if len(rows)!=4:
        raise ValueError("exactly 4 different source factors on B physical C4")
    return all(len(set(rows[i]) & set(rows[j]))<=1
               for i in range(4) for j in range(i+1,4))


def original_four_by_four_incidence_permanent(rows,columns):
    """Each row = real ORIGINAL source neighbor set of ONE q_i, columns
    = 4 different globally identified actual opposite source factors.
    No physical-edge pseudo Q; columns fixed under ONE global map.
    """
    if len(rows)!=4 or len(columns)!=4 or len(set(columns))!=4:
        raise ValueError("4 true original q_i and 4 distinct opposite source factors")
    if not k22_free_four_rows(rows):
        raise ValueError("not a genuine GQ no-original-4cycle incidence submatrix")
    matrix=tuple(tuple(int(columns[j] in rows[i]) for j in range(4))
                 for i in range(4))
    score=sum(all(matrix[i][perm[i]] for i in range(4)) for perm in PERMS4)
    if not 0<=score<=3:
        raise AssertionError("universal genuine GQ K2,2-free 4x4 permanent bound violated")
    return score


def exhaustive_four_by_four_K22_free_permanent_certificate():
    """FINITE purely combinatorial theorem checker independent of any
    GQ fixture, enumerates all 2^16 4x4 matrices with exact integer
    row masks. This supports the simple row-degree mathematical proof
    in the MD; no graph sampled or assumed generic.
    """
    hist=Counter()
    max_p=0
    witness=None
    for word in range(1<<16):
        rows=tuple((word>>(4*i))&15 for i in range(4))
        if any((rows[i]&rows[j]).bit_count()>1
               for i in range(4) for j in range(i+1,4)):
            continue
        score=sum(all(rows[i]&(1<<perm[i]) for i in range(4))
                  for perm in PERMS4)
        hist[score]+=1
        if score>max_p:
            max_p=score
            witness=rows
    if sum(hist.values())!=18521 or max_p!=3 or dict(hist)!={
            0:11993,1:5688,2:744,3:96}:
        raise AssertionError("independent 16bit K2,2-free perfect-matching universe drift")
    return {
        "all_binary_4_by_4_matrices_exhausted":65536,
        "genuine_GQ_K22_free_4x4_matrices":18521,
        "permanent_histogram":dict(sorted(hist.items())),
        "maximum_permanent":max_p,
        "sharp_source_incidence_matrix_four_bit_row_masks":witness,
        "all_h_original_GQ_any_4_by_4_submatrix_PERMANENT_le_3_PROVED":True,
    }


def physical_2factor_containing_two_occupied_edges(a,first,second):
    """Independent exhaustive finite physical 2-factor enumerator.
    Cap a<=7 intentionally: universal large-a proof uses exact
    binomial formulas, NEVER enumerates K_a in ALL-h runtime.
    """
    if type(a) is not int or not 6<=a<=7:
        raise ValueError("physical brute oracle only K6/K7; use all-h closed formulas")
    if len(first)!=2 or len(second)!=2:
        raise ValueError("two canonical physical unordered source edge pairs required")
    e1=tuple(first);e2=tuple(second)
    if not (0<=e1[0]<e1[1]<a and 0<=e2[0]<e2[1]<a) or e1==e2:
        raise ValueError("two different globally injected canonical physical pairs required")
    out=[]
    for six in combinations(range(a),6):
        e=tuple(combinations(six,2))
        if e1 not in e or e2 not in e:
            continue
        for selected in combinations(e,6):
            if e1 not in selected or e2 not in selected:
                continue
            degree=Counter(v for edge in selected for v in edge)
            if len(degree)==6 and all(n==2 for n in degree.values()):
                out.append(frozenset(selected))
    if len(set(out))!=len(out):
        raise AssertionError("physical twofactor repeated")
    return out


def original_all_h_two_pinned_physical_A_capacity(s,relation):
    s,d,V,a,K=original_parameters(s)
    if relation=="adjacent":
        n=7*comb(a-3,3)
    elif relation=="disjoint":
        n=14*comb(a-4,2)
    else:
        raise ValueError("distinct opposite physical source edges adjacent/disjoint only")
    return {
        "s":s,"a":a,"relation":relation,
        "physical_2_regular_A_completion_patterns_full_Ka":n,
        "per_realized_B_root_C4_original_GF5_physical_A_upper":3*n,
        "exact_zero_possible_for_opposite_physical_A_gate":True,
        "conditional_on_one_REALIZED_B_physical_C4":True,
        "original_source_GQ_girth_K22_permanent_at_most_3":True,
        "all_h_universal_seven_motif_lower_PROVED":False,
    }


def independent_historical_BA_rooted_gate(
        q_sources,pinned_opposite,neighbors,other_labels,phys_patterns):
    """EXACT nonnegative sum of actual 4x4 GQ incidence permanents
    over physical 2factor completions of fixed opposite root flags.
    Returns accepted selected historical B/A motifs for ONE actual
    original B-root physical C4 and its pinned two real root flags.
    """
    if len(q_sources)!=4 or len(set(q_sources))!=4:
        raise ValueError("need four different actual original singly-used B factors")
    if len(pinned_opposite)!=2 or len(set(pinned_opposite))!=2:
        raise ValueError("root uses TWO distinct actual original flags")
    if len(other_labels)!=len(set(map(tuple,other_labels))):
        raise ValueError("global physical opposite pair map must be injected")
    if any(type(q) is not int or not 0<=q<len(neighbors)
           for q in q_sources):
        raise ValueError("all four actual source IDs must index real original neighbor sets")
    g=tuple(tuple(edge) for edge in other_labels)
    e1,e2=(g[q] for q in pinned_opposite)
    if not 0<=e1[0]<e1[1] or not 0<=e2[0]<e2[1] or e1==e2:
        raise ValueError("noncanonical two actual original opposite label pairs")
    inverse={edge:i for i,edge in enumerate(g)}
    value=0
    examined=0
    occupied=0
    nonzero=0
    positive_value_histogram=Counter()
    for factor in phys_patterns:
        if e1 not in factor or e2 not in factor:
            raise AssertionError("caller physical 2factor did not contain both pinned source labels")
        examined+=1
        needed=tuple(sorted(factor-{e1,e2}))
        if len(needed)!=4 or any(edge not in inverse for edge in needed):
            continue
        occupied+=1
        line_factors=tuple(inverse[edge] for edge in needed)
        pm=original_four_by_four_incidence_permanent(
            tuple(neighbors[q] for q in q_sources),line_factors)
        value+=pm
        if pm:
            nonzero+=1
            positive_value_histogram[pm]+=1
    return {
        "accepted_original_GF5_BA_for_this_REALIZED_root_C4":value,
        "physical_A_2factor_completions_containing_two_pinned_edges":examined,
        "physically_globally_occupied_2factor_completions":occupied,
        "positive_original_GQ_permanent_2factor_completions":nonzero,
        "permanent_positive_histogram":dict(sorted(positive_value_histogram.items())),
        "universal_source_matching_sharp_bound_3_applied":True,
    }


def genuine_W32_BA_physical_gate_full(scheme):
    """Compare an INDEPENDENT new opposite-physical 2factor×GQ rook
    enumerator to (a) Y5 independent literal original-root Q oracles
    and (b) historical full true ORIGINAL 51-palette GF5 classification.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4q_two_sided_seven_join import (
        strict_true_W32_model,exact_two_sided_original_seven_join)
    model=fixture(1,scheme)
    inc,left,right=strict_true_W32_model(model)
    original_y5=genuine_W32_rooted_BA_forest(scheme)
    history=exact_two_sided_original_seven_join(model,independent_history=True)
    opposite_source_maps=(right,left)
    source_maps=(left,right)
    all_patterns=tuple(physical_2factor_containing_two_occupied_edges(
        6,(0,1),(0,2)))
    if len(all_patterns)!=7:
        raise AssertionError("K6 fixed adjacent pair 2factor census incorrect")
    byside={}
    for side in (0,1):
        B_labels=source_maps[side]
        A_labels=opposite_source_maps[side]
        bysource=[[] for _ in range(15)]
        neighbors=[set() for _ in range(15)]
        for j,edge in enumerate(inc):
            bysource[edge[side]].append(j)
            neighbors[edge[side]].add(edge[1-side])
        Q=original_y5["per_historical_GF5_BA_tag"][
            "B-left/A-right" if side==0 else "A-left/B-right"]
        expected_cohorts={
            (rec["root"],tuple(rec["actual_root_incidence_IDs"])):rec
            for rec in Q["top_source_forest_cohorts"]}
        # Reconstruct ALL cohorts independently; Y5's top subset is
        # supplementary, the actual full truth is checked in aggregate
        # by a completely independent historical ORIGINAL join below.
        counts=Counter()
        samples=[]
        for root in range(15):
            for root_pair in combinations(bysource[root],2):
                pins=tuple(inc[j][1-side] for j in root_pair)
                if len(set(pins))!=2:
                    raise AssertionError("genuine GQ repeated source flags have distinct opposite endpoints")
                pinned_physical=tuple(A_labels[z] for z in pins)
                relation=("adjacent" if set(pinned_physical[0])&
                          set(pinned_physical[1]) else "disjoint")
                full_A=physical_2factor_containing_two_occupied_edges(
                    6,*pinned_physical)
                expected=7 if relation=="adjacent" else 14
                if len(full_A)!=expected:
                    raise AssertionError("historical original fixed two edge physical 2factor mismatch")
                total=0;gate_nonzero=0;completions=0;permanent_1=Counter()
                for c4 in _physical_root_C4_source_patterns(B_labels,root):
                    outcome=independent_historical_BA_rooted_gate(
                        c4,pins,neighbors,A_labels,full_A)
                    total+=outcome[
                        "accepted_original_GF5_BA_for_this_REALIZED_root_C4"]
                    completions+=outcome[
                        "physical_A_2factor_completions_containing_two_pinned_edges"]
                    gate_nonzero+=outcome[
                        "positive_original_GQ_permanent_2factor_completions"]
                    for k,v in outcome["permanent_positive_histogram"].items():
                        permanent_1[int(k)]+=v
                    counts["physical_B_C4_root_patterns"]+=1
                counts["all_root_flag_cohorts"]+=1
                counts["B_A_GF5_accepted_via_new_2factor_4rook"]+=total
                counts["potential_root_physical_A_twofactors"]+=completions
                counts["nonzero_source_GQ_permanent_A_completions"]+=gate_nonzero
                counts[f"pair_{relation}"]+=1
                for k,v in permanent_1.items():
                    counts[f"permanent_{k}_nonzero_patterns"]+=v
                if total==0:
                    counts["root_cohorts_with_zero_actual_GF5_acceptance"]+=1
                else:
                    counts["root_cohorts_with_positive_actual_GF5_acceptance"]+=1
                if len(samples)<5:
                    samples.append({
                        "root":root,
                        "two_true_original_incidence_IDs":tuple(root_pair),
                        "two_real_opposite_source_factors":pins,
                        "physical_pinned_relation":relation,
                        "accepted_by_INDEPENDENT_2factor_permanent":total,
                        "physically_possible_2factor_tests_for_three_C4s":completions,
                    })
        tag="B-left/A-right" if side==0 else "A-left/B-right"
        if counts["B_A_GF5_accepted_via_new_2factor_4rook"]!=(
                history["accepted_seven_GF5_original_Q_by_tag"][tag]):
            raise AssertionError("NEW SAME-Q physical 2factor four-rook acceptance differs from independent historical GF5 exact six-Q census")
        if counts["B_A_GF5_accepted_via_new_2factor_4rook"]!=(
                Q["historical_positive_GF5_accepted_BA_six_IDs"]):
            raise AssertionError("NEW 2factor four-rook and independent Y5 literal Q source+physical-A counts differ")
        if counts["all_root_flag_cohorts"]!=45 or counts["physical_B_C4_root_patterns"]!=135:
            raise AssertionError("ALL real ORIGINAL root flags and physical B C4s missing")
        if counts["root_cohorts_with_positive_actual_GF5_acceptance"]!=(
                Q["cohorts_with_positive_historical_GF5"]):
            raise AssertionError("NEW 2factor four-rook accepted physical root cohort support differs from Y5")
        byside[tag]={
            "original_B_root_side":"point" if side==0 else "line",
            "rooted_cohorts_exhaustively_checked":45,
            "true_original_B_physical_C4_patterns_examined":135,
            "accepted_historical_GF5_by_exact_four_rook_2factor":
                counts["B_A_GF5_accepted_via_new_2factor_4rook"],
            "historical_GF5_independent_Y5_and_AA4Q_agree":True,
            "physically_possible_K6_A_2factors_checked":
                counts["potential_root_physical_A_twofactors"],
            "nonzero_true_original_incidence_permanent_physical_2factors":
                counts["nonzero_source_GQ_permanent_A_completions"],
            "nonzero_permanent_1_2_3_histogram":{
                str(k):counts[f"permanent_{k}_nonzero_patterns"]
                for k in (1,2,3)},
            "rooted_cohorts_with_zero_historical_GF5":
                counts["root_cohorts_with_zero_actual_GF5_acceptance"],
            "rooted_cohorts_with_positive_historical_GF5":
                counts["root_cohorts_with_positive_actual_GF5_acceptance"],
            "rooted_cohorts_with_adjacent_opposite_physical_pins":
                counts["pair_adjacent"],
            "rooted_cohorts_with_disjoint_opposite_physical_pins":
                counts["pair_disjoint"],
            "first_five_true_original_rooted_witnesses":samples,
        }
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y6-ORIGINAL-PHYSICAL-A-FOUR-ROOK-JOIN",
        "scheme":scheme,
        "real_original_global_complete_K6_maps":True,
        "all_h_exact_BA_physical_2factor_x_original_4rook_identity_PROVED":True,
        "independent_4_by_4_GQ_no_K22_permanent_le_3_PROVED":True,
        "per_historical_BA_tag":byside,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


def report():
    certificate=exhaustive_four_by_four_K22_free_permanent_certificate()
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y6-ALL-H-4ROOK-PHYSICAL-A-GATE",
        "all_h_exact_rooted_BA_2factor_4rook_join_PROVED":True,
        "all_h_permanent_4x4_K22_free_sharp_three_PROVED":True,
        "K22_free_four_by_four_certificate":certificate,
        "physical_two_pinned_completion_symbolic":[
            {"s":1<<h,
             "adjacent":original_all_h_two_pinned_physical_A_capacity(
                 1<<h,"adjacent"),
             "disjoint":original_all_h_two_pinned_physical_A_capacity(
                 1<<h,"disjoint")}
            for h in range(1,15)],
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    args=ap.parse_args()
    output=genuine_W32_BA_physical_gate_full(args.scheme) if args.scheme else report()
    print(json.dumps(output,indent=2,sort_keys=True))
