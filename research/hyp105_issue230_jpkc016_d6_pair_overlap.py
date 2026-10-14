"""JPKC-016: exact two-D6 global-injection joint kernel for source-disjoint Q.

J54: H_a = #physical six-cycles in K_a avoiding a fixed 6cycle's
      six edge-pair labels; exact 2^6 inclusion-exclusion, independent
      direct graph-cycle oracle on small physical alphabets.
J55: for two TRUE ORIGINAL 6-incidence matchings with DISJOINT source
      point AND line supports, exact joint D6 probability
      p_D6 * 60 * (12*H_a/(C(a,2)-6)_6)^2. Does NOT assume events
      independent, even if Q and Q' share no original incidence.
J56: exact W32 source *anchored row* overlap histogram
      (shared original points, lines, incidence columns) by independent
      source matching DP over original incidences, not 1.56M^2 pairs.
J57: all-h exact conditional second-moment subkernel and rigorous
      disjoint-pair lower bound; mixed overlap/gluing types remain OPEN.

The full E[D6^2] is NOT computed. Root A/B and ASET remain OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import argparse
import json

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc015_ensemble_d6_capacity import (
    finite_original_geometry, exact_D6_probability_minimal_alphabet,
    original_six_matching_bounds, falling,
    exact_original_W32_six_matchings,
)


def physical_cycle_avoidance_count(a):
    """Exact H_a by inclusion-exclusion of a FIXED physical C6.

    There are 60*C(a,6) undirected physical C6 on six coordinates.
    For each forbidden edge-subset F of one fixed 6cycle:
       F proper => a disjoint union of p path components, k edges,
       t=k+p occupied vertices. Number of 6cycles containing F is
       C(a-t,6-t) * 2**(p-1) * (5-k)!.
    Empty F contributes 60*C(a,6). Full six-edge F contributes 1.
    This uses ONLY physical pairs, never a per-original-incidence label
    independence assumption.
    """
    if type(a)!=int or a<6:
        raise ValueError("physical coordinate alphabet a>=6 required")
    total=0
    for mask in range(64):
        k=mask.bit_count()
        if k==6:
            count=1
        elif not k:
            count=60*comb(a,6)
        else:
            # p is number of runs of selected edges around the 6cycle
            p=sum(bool(mask & (1<<i)) and
                  not bool(mask & (1<<((i-1)%6)))
                  for i in range(6))
            if p<1 or k+p>6:
                raise AssertionError("fixed physical C6 proper-subgraph component error")
            t=k+p
            count=comb(a-t,6-t)*2**(p-1)*factorial(5-k)
        total+=(-1 if k%2 else 1)*count
    if total<0 or total>60*comb(a,6):
        raise AssertionError("inclusion-exclusion physical K_a-minus-C6 cycles invalid")
    return total


def physical_cycle_avoidance_bruteforce(a, *, max_a=9):
    """Independent cycle-edge-set enumeration; NO IE or D6 dual oracle."""
    if type(a)!=int or a<6 or a>max_a or max_a>10:
        raise ValueError("independent brute physical C6 limited to a<=9")
    forbidden={tuple(sorted((i,(i+1)%6))) for i in range(6)}
    allowed=0
    total=0
    for vertices in combinations(range(a),6):
        first=vertices[0]
        for tail in permutations(vertices[1:]):
            if tail[0]>tail[-1]:
                continue
            cyc=(first,)+tail
            edges={tuple(sorted((cyc[i],cyc[(i+1)%6])))
                   for i in range(6)}
            total+=1
            allowed+=int(not(edges&forbidden))
    if total!=60*comb(a,6):
        raise AssertionError("independent physical cycle orientation quotient invalid")
    return {"physical_cycles_total":total,
            "physical_cycles_avoiding_first_C6":allowed}


def disjoint_original_source_D6_joint(a):
    """Exact joint kernel when two ORIGINAL matchings are vertex-disjoint.

    Their point supports are disjoint AND their line supports disjoint,
    so the second Q sees (N-6)_6 ordered images left and right after
    conditioning first Q on D6. The remaining pair alphabet equals
    K_a minus one physical 6cycle on EACH side. Both removed C6 graphs
    have the same isomorphism type even though physical coordinates
    may be relabeled differently. For each of the 60 named six-column
    connected duals D' of Q', there are exactly 12*H_a allowed ordered
    pair-label assignments on each side. Hence conditional p2|D6 =
    60 * (12*H_a/(N-6)_6)^2, exactly.
    """
    if type(a)!=int or a<6:
        raise ValueError("physical coordinate alphabet a>=6 required")
    N=comb(a,2)
    h=physical_cycle_avoidance_count(a)
    single=Fraction(60*falling(a,6)**2,falling(N,6)**2)
    conditional=Fraction(60*(12*h)**2,falling(N-6,6)**2)
    joint=single*conditional
    cov=joint-single*single
    if not 0<joint<=single or not 0<conditional<=1:
        raise AssertionError("global injection disjoint Q pair kernel violates probability axioms")
    return {
        "a":a,"physical_pair_labels_N":N,
        "physical_sixcycles_avoiding_prior_D6_pair_images":h,
        "single_original_matching_D6_probability":str(single),
        "second_D6_conditional_on_first_and_source_disjoint":str(conditional),
        "joint_two_D6_events_source_factor_disjoint":str(joint),
        "covariance_for_two_source_factor_disjoint_events":str(cov),
        "joint_over_independent_product":str(joint/(single*single)),
        "global_pair_label_sampled_without_replacement":True,
        "different_original_matchings_pairwise_independence_claimed":False,
        "overlapping_original_source_factors_joint_kernel_proved":False,
        "root_A_proved":False,"root_B_constructed":False,
    }


def original_W32_anchor_matching(model):
    """Construct one TRUE ORIGINAL six-edge bipartite source matching.

    Independent of all physical f,g and of historical 7-class census.
    """
    edges=tuple(tuple(x) for x in model["incidences"])
    if model.get("s")!=2 or len(edges)!=45:
        raise ValueError("true W32 ORIGINAL incidence host only")
    by_p=defaultdict(list)
    for i,(p,l) in enumerate(edges):
        by_p[p].append((l,i))
    if sorted(by_p)!=list(range(15)) or any(len(x)!=3 for x in by_p.values()):
        raise ValueError("complete genuine W32 original source point degrees required")
    chosen=[]
    used=set()
    def backtrack(p):
        if len(chosen)==6:
            return True
        if p==15 or 15-p<6-len(chosen):
            return False
        for l,eid in sorted(by_p[p]):
            if l in used:
                continue
            used.add(l);chosen.append(eid)
            if backtrack(p+1):
                return True
            chosen.pop();used.remove(l)
        return backtrack(p+1)
    if not backtrack(0):
        raise AssertionError("no six-edge matching in genuine W32 incidence graph")
    return tuple(sorted(chosen))


def original_W32_anchor_overlap_row(model, anchor_Q=None,
                                    *, swapped=False, max_states=100_000):
    """EXACT true W32 source 6-matching overlap tensor for ONE pinned Q0.

    Count Q' by (# common original points, # common original lines,
    # common original INCIDENCE EDGES). State is (used right-lines mask,
    intersection-with-Q0 point count, intersection-with-Q0 edge count);
    original right-line intersection is read from mask at terminal.
    For swapped orientation, the first two signature components swap,
    the source edge overlap remains the same. Independent DP.
    """
    edges=tuple(tuple(x) for x in model["incidences"])
    if model.get("s")!=2 or len(edges)!=45 or len(set(edges))!=45:
        raise ValueError("true ORIGINAL W32 45-edge incidence host required")
    if anchor_Q is None:
        anchor_Q=original_W32_anchor_matching(model)
    if (not isinstance(anchor_Q,tuple) or len(anchor_Q)!=6
            or any(type(i)!=int or not 0<=i<45 for i in anchor_Q)
            or len(set(anchor_Q))!=6):
        raise ValueError("six distinct true ORIGINAL incidence IDs as anchor required")
    if type(max_states)!=int or max_states<1:
        raise ValueError("positive exact anchored overlap DP state budget required")
    point_set={edges[i][0] for i in anchor_Q}
    line_set={edges[i][1] for i in anchor_Q}
    if len(point_set)!=6 or len(line_set)!=6:
        raise ValueError("anchor ORIGINAL incidences must be a genuine bipartite matching")
    anchor_edge=set(anchor_Q)
    by_first=[[] for _ in range(15)]
    for eid,(p,l) in enumerate(edges):
        u,v=(l,p) if swapped else (p,l)
        if not (0<=u<15 and 0<=v<15):
            raise ValueError("original incidence source endpoint invalid")
        by_first[u].append((v,eid))
    if any(len(x)!=3 for x in by_first):
        raise ValueError("true 3-regular W32 original point/line source required")
    known_first=line_set if swapped else point_set
    known_second=point_set if swapped else line_set
    second_mask=sum(1<<l for l in known_second)
    dp={(0,0,0):1}
    for u in range(15):
        next_dp=dp.copy()
        for (mask,overlap_first,overlap_edge),ways in dp.items():
            if mask.bit_count()==6:
                continue
            for v,eid in by_first[u]:
                bit=1<<v
                if mask&bit:
                    continue
                key=(mask|bit,overlap_first+int(u in known_first),
                     overlap_edge+int(eid in anchor_edge))
                next_dp[key]=next_dp.get(key,0)+ways
        if len(next_dp)>max_states:
            raise ValueError("exact true ORIGINAL source overlap DP budget exceeded")
        dp=next_dp
    counts=Counter()
    for (mask,overlap_first,overlap_edge),ways in dp.items():
        if mask.bit_count()!=6:
            continue
        overlap_second=(mask&second_mask).bit_count()
        i,j=((overlap_second,overlap_first) if swapped else
             (overlap_first,overlap_second))
        if not 0<=overlap_edge<=min(i,j)<=6:
            raise AssertionError("ORIGINAL edge overlap exceeds factor intersection")
        counts[(i,j,overlap_edge)]+=ways
    total=sum(counts.values())
    independently=exact_original_W32_six_matchings(model)[
        "true_original_W32_6_matching_count"]
    if total!=independently or counts[(6,6,6)]!=1:
        raise AssertionError("J56 ORIGINAL anchored six-matching overlap partition wrong")
    return {
        "anchor_original_six_incidence_IDs":anchor_Q,
        "swapped_original_bipartition":swapped,
        "source_original_six_matching_population":total,
        "source_factor_disjoint_six_matching_count":counts[(0,0,0)],
        "source_diagonal_original_six_matching_count":counts[(6,6,6)],
        "overlap_signature_to_number_of_original_six_matchings":
            {",".join(map(str,key)):counts[key] for key in sorted(counts)},
        "nonempty_overlap_signatures":len(counts),
        "actual_original_incidence_edge_overlap_retained":True,
        "complete_PAIR_source_overlap_histogram_over_ALL_Q0_claimed":False,
    }


def analytic_disjoint_original_source_sixmatching_min(s):
    """Rigorous min_{true Q} #source sixmatchings disjoint BOTH sides.

    Q uses six original points and six original lines. At most 12*d
    original incidences touch these endpoints. During extension an
    additional j chosen edges prohibit at most 2*j*d further edges.
    For V>22, every factor M-d*(12+2j) positive for j=0..5.
    """
    geo=finite_original_geometry(s)
    M=geo["original_incidence_columns"]
    d=geo["original_degree"]
    v=geo["original_points"]
    if v<=22:
        return {
            "rigorous_uniform_over_Q_source_disjoint_matching_lower":"0",
            "positive_all_h_disjoint_source_count_from_greedy":False,
            "applies_to_s":s,
        }
    numerator=1
    for j in range(6):
        numerator*=M-(12+2*j)*d
    if numerator<=0:
        raise AssertionError("source-disjoint source incidence greedy matching count nonpositive")
    return {
        "rigorous_uniform_over_Q_source_disjoint_matching_lower":
            str(Fraction(numerator,720)),
        "positive_all_h_disjoint_source_count_from_greedy":True,
        "applies_to_s":s,
    }


def ensemble_second_moment_disjoint_sector(s, *,
                                           finite_W32_anchor=False):
    """PROVED lower-sector contribution, not complete E[D6²].

    Exact E[D6²] = sum over all ORDERED pairs (Q,Q') of joint D6
    event probabilities. Every diagonal Q=Q' contributes p. Every
    completely source-factor-disjoint ordered pair contributes
    p_joint. Mixed overlap/gluing types are uncomputed nonnegative.
    Using the uniform per-Q greedy source-disjoint count gives all-h
    proven E[D6²] >= M6*p + M6*Dmin*p_joint. For s=2 Dmin=0;
    one exact finite anchored Q proves TWO ordered offdiagonal terms.
    """
    geo=finite_original_geometry(s)
    p=exact_D6_probability_minimal_alphabet(s)
    kernel=disjoint_original_source_D6_joint(
        geo["minimal_physical_coordinate_symbols"])
    joint=Fraction(kernel["joint_two_D6_events_source_factor_disjoint"])
    source_lower,_=original_six_matching_bounds(s)
    disjoint=analytic_disjoint_original_source_sixmatching_min(s)
    min_per_Q=Fraction(disjoint[
        "rigorous_uniform_over_Q_source_disjoint_matching_lower"])
    second_lower=source_lower*(p+min_per_Q*joint)
    if second_lower<source_lower*p:
        raise AssertionError("new nonnegative source-disjoint pair sector lost")
    answer={
        "s":s,
        "minimum_physical_coordinate_alphabet":
            geo["minimal_physical_coordinate_symbols"],
        "all_h_rigorous_second_moment_disjoint_sector_lower":str(second_lower),
        "source_matching_count_lower_used":str(source_lower),
        "source_disjoint_matching_count_lower_for_every_Q":str(min_per_Q),
        "exact_source_disjoint_joint_D6_probability":str(joint),
        "all_source_overlap_gluing_sectors_computed":False,
        "full_exact_D6_second_moment_computed":False,
        "root_A_proved":False,"root_B_constructed":False,
    }
    if finite_W32_anchor:
        if s!=2:
            raise ValueError("independent finite anchored W32 overlap only at s=2")
        row=original_W32_anchor_overlap_row(fixture(1,"lex"))
        M6=row["source_original_six_matching_population"]
        count=row["source_factor_disjoint_six_matching_count"]
        anchored=Fraction(M6)*p+2*count*joint
        if anchored<second_lower:
            raise AssertionError("genuine fixed anchored source-matching witness lower worsened")
        answer["finite_exact_one_anchor_source_disjoint_count"]=count
        answer["finite_exact_anchored_pair_second_moment_lower"]=str(anchored)
    return answer


def report():
    finite=original_W32_anchor_overlap_row(fixture(1,"lex"))
    mirror=original_W32_anchor_overlap_row(
        fixture(1,"lex"),finite["anchor_original_six_incidence_IDs"],
        swapped=True)
    if (finite["overlap_signature_to_number_of_original_six_matchings"]
            !=mirror["overlap_signature_to_number_of_original_six_matchings"]):
        raise AssertionError("independent swapped ORIGINAL bipartition overlap rows differ")
    return {
        "slice":"JPKC-016",
        "exact_W32_one_anchor_source_overlap_row":finite,
        "independent_swapped_source_overlap_row_verified":True,
        "physical_avoidance_counts":{
            a:physical_cycle_avoidance_count(a)
            for a in (6,7,8,14,35)},
        "W32_exact_source_disjoint_joint":disjoint_original_source_D6_joint(6),
        "all_h_proved_lower_sector":[ensemble_second_moment_disjoint_sector(
            s,finite_W32_anchor=(s==2)) for s in (2,4,8,16)],
        "full_exact_second_moment_claimed":False,
        "all_h_min_global_D6_proved":False,
    }


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--s",type=int)
    args=ap.parse_args()
    row=(ensemble_second_moment_disjoint_sector(
        args.s,finite_W32_anchor=args.s==2)
         if args.s is not None else report())
    print(json.dumps(row,sort_keys=True,indent=2))
