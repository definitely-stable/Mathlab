"""AA4-BI: true-original seven-GF5 source-CHERRY moments on FIXED full f,g.

All h genuine W(3,2^h) mathematical identity on each physical (P,L)
sixcoordinate mask: J-AA = M1-M2+M3-M4, with Mj the sum over genuine
joined six ORIGINAL incidence sets Q of binom(c(Q),j), and
c(Q) = sum_p binom(deg_Q(p),2) + sum_l binom(deg_Q(l),2).
Crucial original source GQ girth 8 implies c in {0,1,2,3,4};
c=0 is A/A, c>=1 is HISTORICALLY ACCEPTED non-AA seven-GF5.

Root-facing lower for every FULLY FIXED original f,g:
  S[P,L] >= D6[P,L] + M1[P,L]**2 / M2raw[P,L]
where M2raw=sum c(Q)**2, if nonzero; also >=D6 + M1/4.
Exact selected GF5-weighted necessary numerator for non-AA class
can be reconstructed from c=1,2,3,4 histogram + B/B overlap charge.

Prior scalar S=J-AA+D6 from #534/#573 and D6 squarefree trace
from #572 explicitly credited. The mathematical advance is the
source cherry differential moment AND nonlinear variance-sensitive
lower certificate, not a root A/B/C minimax resolution.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,product
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import (
    _original_source,_physical_point_2factors,physical_sixmask_of_original_flags)
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

_CHERRY_TO_CLASS={1:"B/A or A/B",2:"B/B",3:"C/A",4:"C/B"}
_SHARP_LOWER_RATIO=Fraction(49050,4)
_SHARP_UPPER_RATIO=Fraction(45600,1)


def genuine_original_source_cherries(ids,inc):
    """Exact original source cherry count without physical classification.

    Requires six different true original incidence flag IDs. Returns
    point and LINE repeated-factor pair counts and B/B original shared
    flag-ID overlap. The incidence model must be TRUE source (caller).
    """
    q=tuple(ids)
    if len(q)!=6 or len(set(q))!=6 or any(
        type(i) is not int or not 0<=i<len(inc) for i in q
    ):
        raise ValueError("six DISTINCT actual original incidence flag IDs required")
    counts=[]
    repeated=[]
    for side in (0,1):
        freq=Counter(inc[i][side] for i in q)
        vals=tuple(sorted(freq.values()))
        if vals not in ((1,1,1,1,1,1),(1,1,1,1,2),(2,2,2)):
            raise ValueError("not six-coordinate physical source A/B/C profile")
        counts.append(sum(comb(n,2) for n in freq.values()))
        repeated.append({source for source,n in freq.items() if n==2})
    cp,cl=counts
    if (cp,cl)==(3,3):
        raise AssertionError("true W(3,s) GQ girth eight forbids original C/C")
    c=cp+cl
    if c>4:
        raise AssertionError("true ORIGINAL factor source-cherry cap 4")
    overlap=0
    if (cp,cl)==(1,1):
        p=next(iter(repeated[0]))
        l=next(iter(repeated[1]))
        overlap=sum(inc[i]==(p,l) for i in q)
        if overlap not in (0,1):
            raise AssertionError("genuine original source simple incidence repeated")
    return {"point_cherries":cp,"line_cherries":cl,
            "total_source_cherries":c,
            "BB_same_true_original_flag_overlap":overlap,
            "source_class_from_cherry_count":_CHERRY_TO_CLASS.get(c,"A/A")}


def _sector_stats(charges):
    """Class-free exact positive source-cherry moments and sharp bounds."""
    hist=Counter(c for c,cp,cl,ov in charges)
    if hist and any(c not in range(5) for c in hist):
        raise AssertionError("real GQ source cherry cap violated")
    J=len(charges)
    M=tuple(sum(comb(c,j) for c,_,_,_ in charges) for j in range(1,5))
    raw2=sum(c*c for c,_,_,_ in charges)
    nonAA=J-hist[0]
    inc_exc=M[0]-M[1]+M[2]-M[3]
    if nonAA!=inc_exc or raw2!=M[0]+2*M[1]:
        raise AssertionError("source cherry Newton/inclusion-exclusion identity false")
    bboverlap=sum(ov for c,cp,cl,ov in charges if c==2)
    if bboverlap>hist[2]:
        raise AssertionError("BB source incidence overlap greater than BB events")
    risk=(45600*hist[1]+
          R3_CERTIFIED_FLOORS["B/B-overlap"]*bboverlap+
          R3_CERTIFIED_FLOORS["B/B-disjoint"]*(hist[2]-bboverlap)+
          R3_CERTIFIED_FLOORS["C/A"]*hist[3]+
          R3_CERTIFIED_FLOORS["C/B"]*hist[4])
    second_bound=(Fraction(M[0]*M[0],raw2) if raw2 else Fraction(0))
    if not (Fraction(M[0],4)<=second_bound<=nonAA):
        raise AssertionError("true all-h cherry Cauchy lower violated")
    if not(_SHARP_LOWER_RATIO*M[0]<=risk<=_SHARP_UPPER_RATIO*M[0]):
        raise AssertionError("accepted GF5 51-pattern weight cherry sandwich false")
    return {
        "six_original_incidence_join":J,
        "AA_six_original_factor_distinct":hist[0],
        "nonAA_seven_GF5_positive_source_cherry_exact":nonAA,
        "source_cherry_histogram_c0_through4":
            {i:hist[i] for i in range(5)},
        "source_cherry_binomial_moments_M1_to_M4":M,
        "source_cherry_square_moment":raw2,
        "BB_overlapping_original_source_flag_count":bboverlap,
        "GF5_51palette_nonAA_certified_numerator":risk,
        "nonAA_from_moment_exact_inclusion_exclusion":inc_exc,
        "nonAA_from_first_second_Cauchy_lower":second_bound,
        "nonAA_from_first_moment_universal_lower":Fraction(M[0],4),
        "weighted_GF5_source_cherry_ratio_lower":_SHARP_LOWER_RATIO*M[0],
        "weighted_GF5_source_cherry_ratio_upper":_SHARP_UPPER_RATIO*M[0],
    }


def true_original_fixed_pair_source_cherry_fiber(model,P):
    """Independently count source-cherry energy in one POINT physical P fiber.

    Source-first true GQ incidence flags, not historical accepted-tag
    oracle and not the previous AA4-BH CLASSIFY-every-Q routine.
    The right physical LINE image is the SAME full already-fixed g.
    Per-fiber physical L group stores only original source cherry
    multiplicity data, never labels Q as positive via GF5 lookup.
    """
    s,V,a,inc,f,g,by_point,_=_original_source(model)
    P=tuple(P)
    if len(P)!=6 or len(set(P))!=6 or any(
        type(c) is not int or not 0<=c<a for c in P
    ):
        raise ValueError("six distinct actual typed point physical coordinates")
    P=tuple(sorted(P))
    inverse={edge:p for p,edge in enumerate(f)}
    byL=defaultdict(list)
    unilateral=0
    for physical_edges in _physical_point_2factors(P,set(inverse)):
        p_mult=Counter(inverse[e] for e in physical_edges)
        choices=[]
        for p,n in sorted(p_mult.items()):
            if n==1:choices.append(tuple((i,) for i in by_point[p]))
            elif n==2:choices.append(tuple(combinations(by_point[p],2)))
            else:raise AssertionError("2regular physical degree implies source occupancy <=2")
        for tup in product(*choices):
            q=tuple(sorted(i for bucket in tup for i in bucket))
            if len(set(q))!=6:
                raise AssertionError("six original incidence IDs repeated")
            unilateral+=1
            L=physical_sixmask_of_original_flags(q,inc,g)
            if L is None:continue
            c=genuine_original_source_cherries(q,inc)
            byL[L].append((c["total_source_cherries"],
                           c["point_cherries"],c["line_cherries"],
                           c["BB_same_true_original_flag_overlap"]))
    outputs={}
    for L,charges in sorted(byL.items()):
        z=_sector_stats(charges)
        z["original_physical_six_POINT_mask"]=P
        z["original_physical_six_LINE_mask"]=L
        outputs[L]=z
    return {
        "s":s,"V":V,"a":a,"P":P,
        "unilateral_original_source_sixflag_candidates":unilateral,
        "sectors":outputs,
        "all_h_source_moment_mathematical_identity":True,
        "actual_computational_GQ_order_only":s,
        "seven_class_root_A_B_C_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def all_h_original_source_cherry_equivalent_obstruction(s):
    """Exact all-h symbolic theorem; no gigantic synthetic W(3,s) model.

    For ALL actual f,g, arbitrary fixed full original maps, each
    local fiber has 0<=c<=4, M1²/M2raw <= N_nonAA <= M1,
    N_nonAA=M1-M2+M3-M4.
    The original seven GF5 count S = N_nonAA + D6.
    Thus Branch A/B threshold S~s6 is equivalent, up to factor 4,
    to source-cherry first moment + squarefree D6 physical trace.
    This is a candidate REDUCTION of proof targets, not yet an
    accepted root C (requires a nontrivial GQ quantitative bound).
    """
    if type(s) is not int or s<2 or s & (s-1):
        raise ValueError("genuine original dyadic W(3,s) only")
    V,a,K,m=_params(s)
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,
        "all_original_source_incidence_host_W3_required":True,
        "all_two_typed_full_injections_f_g_may_be_correlated":True,
        "source_factor_multiplicity_at_most_two_on_each_sixcoordinate_projection":True,
        "true_GQ_C_C_source_incidence_forbidden":True,
        "possible_joined_original_source_cherry_counts":(0,1,2,3,4),
        "exact_nonAA_cherry_moment_inclusion_exclusion":
            "NONAA=M1-M2+M3-M4",
        "sharp_first_moment_bounds":
            "M1/4 <= NONAA <= M1",
        "sharpened_Cauchy_bound":
            "M1**2 / (M1+2*M2) <= NONAA when M1>0",
        "exact_root_seven_sum":
            "S=NONAA+Tr_squarefree_A_D_six/12",
        "root_A_omega_s6_equivalent_up_to_factor_4_to":
            "M1 + Tr_squarefree_A_D_six/12 = Omega(s6)",
        "root_B_little_o_s6_equivalent_up_to_factor_4_to":
            "M1 + Tr_squarefree_A_D_six/12 = o(s6)",
        "minimum_nonAA_51_palette_ratio_to_M1":_SHARP_LOWER_RATIO,
        "maximum_nonAA_51_palette_ratio_to_M1":_SHARP_UPPER_RATIO,
        "no_original_all_fixed_positive_lower_proved":True,
        "no_infinite_counterfamily_proved":True,
        "root_branch_C_not_accepted":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
