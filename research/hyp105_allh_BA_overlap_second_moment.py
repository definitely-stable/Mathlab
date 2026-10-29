"""AA4-BA2: EXACT all-h B-left/A-right conditional pair kernel and second moment.

NO use of independent Bernoulli flags or independent opposite g maps.
For one globally uniform complete original source-line injection g and
ANY FIXED legal complete point-side f, consider all actual original
six-incidence source sets Q with:
  - left historical B structure and six physical degree-two symbols;
  - six DISTINCT actual original source-line IDs;
  - (optionally) all lines outside a fixed frozen original source-line J.
Their right historical A acceptance event is precisely: the six
different right K_a pair images form a 2-regular six-edge graph on six
different physical symbols (one C6 or two C3).

For Q,Q', their joint success probability depends only on
r=|L(Q) intersection L(Q')|, NOT on cycle positions or original-point
sharing, since the right A event is symmetric in the six line ID names.

The unrestricted joint kernel is calculated EXACTLY for EVERY integer
a>=6 from two K6 two-factor templates (C6 and 2*C3), their 7 overlap-
vertex cases, and binomial polynomial in a. All coefficients integer.
For a frozen right pair set F, the same formula holds with an exact
finite coefficient N_r(a,F) (count ordered right 2factor pairs avoiding
F and intersecting in r physical pair edges). Brute independent finite
F oracle is provided for a=6,7; no all-h efficient frozen kernel claimed.

This proves a QUENCHED-IN-f exact conditional second-moment identity
(all dyadic h, genuine original W(3,s)), and an exact Paley-Zygmund
probability lower bound, NOT a positive lower bound at every completed
correlated g, full R3, or root Branch A/B/C result.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

from hyp105_allh_annealed_BA_floor import falling


def twofactors_on_six(vertices):
    """Independent exact 70 K6 edge-set 2factors (60 C6, ten 2*C3)."""
    v=tuple(vertices)
    if len(v)!=6 or len(set(v))!=6:
        raise ValueError("six different physical vertices required")
    edges=tuple(combinations(v,2))
    factors=[]
    for candidate in combinations(edges,6):
        degrees=Counter(z for e in candidate for z in e)
        if len(degrees)==6 and all(degrees[x]==2 for x in v):
            factors.append(frozenset(candidate))
    if len(factors)!=70 or len(set(factors))!=70:
        raise AssertionError("K6 twofactor count must equal 70")
    return tuple(factors)


def factor_components(edges):
    """For a true 2-factor on six symbols, the cycle sizes are (6,) or (3,3)."""
    adj={}
    for u,v in edges:
        adj.setdefault(u,set()).add(v)
        adj.setdefault(v,set()).add(u)
    if len(adj)!=6 or any(len(x)!=2 for x in adj.values()):
        raise ValueError("not a simple K6 twofactor")
    remaining=set(adj)
    sizes=[]
    while remaining:
        root=min(remaining)
        stack=[root];component={root}
        while stack:
            for z in adj[stack.pop()]:
                if z not in component:
                    component.add(z);stack.append(z)
        remaining-=component
        sizes.append(len(component))
    return tuple(sorted(sizes))


@lru_cache(None)
def K6_overlap_vertex_templates():
    """Small integer constants A[type][k][r], validated exhaustively.

    Select exactly k old vertices out of FIRST factor's six symbols,
    append 6-k NEW named vertex symbols (6,7,...) to create the SECOND
    factor's six-vertex support; enumerate all 70 its twofactors.
    All 2factor pairs have exactly k common PHYSICAL vertices; count
    their common PHYSICAL pair edges by r. No random approximation.
    """
    base=twofactors_on_six(range(6))
    exemplars={}
    multiplicities=Counter()
    for x in base:
        kind=factor_components(x)
        multiplicities[kind]+=1
        exemplars.setdefault(kind,x)
    if multiplicities!=Counter({(6,):60,(3,3):10}):
        raise AssertionError("60 connected cycles and ten two-triangles expected")
    out={}
    for kind,F in exemplars.items():
        counts=[[0]*7 for _ in range(7)]
        for k in range(7):
            for old in combinations(range(6),k):
                second_support=tuple(old)+tuple(range(6,12-k))
                for G in twofactors_on_six(second_support):
                    r=len(F&G)
                    counts[k][r]+=1
        if any(sum(counts[k])!=comb(6,k)*70 for k in range(7)):
            raise AssertionError("vertex-intersection template not exhaustive")
        out[kind]=tuple(tuple(row) for row in counts)
    return out


def unrestricted_twofactor_pair_intersection_counts(a):
    """EXACT all-a integer N_r for ordered two-factor PAIRS with |F∩G|=r.

    First choose six physical vertices of F: C(a,6), pick first
    physical twofactor (60 C6 or ten 2C3). For its second twofactor
    G choose k old support vertices and 6-k new from a-6, then choose
    the canonical set of its six physical pair edges, counted by the
    K6 template. N_r(a) is valid also when a<12, with C(n,k)=0 if n<k.
    """
    if type(a) is not int or a<6:
        raise ValueError("physical coordinate alphabet must have a>=6")
    T=K6_overlap_vertex_templates()
    C={kind:60 if kind==(6,) else 10 for kind in T}
    nr=[0]*7
    for kind,table in T.items():
        for k in range(7):
            choose_new=comb(a-6,6-k) if a-6>=6-k else 0
            for r in range(7):
                nr[r]+=comb(a,6)*C[kind]*table[k][r]*choose_new
    total=70*comb(a,6)
    if sum(nr)!=total*total or any(n<0 for n in nr):
        raise AssertionError("all-a twofactor pair polynomial partition invalid")
    if nr[5]:
        raise AssertionError("different degree-2 six-edge sets cannot differ in just 1 edge")
    return tuple(nr)


def _validate_forbidden(a, frozen_pairs):
    F=tuple(tuple(z) for z in frozen_pairs)
    if len(set(F))!=len(F) or any(
            len(z)!=2 or type(z[0]) is not int or type(z[1]) is not int or
            not 0<=z[0]<z[1]<a for z in F):
        raise ValueError("frozen physical right pairs must be distinct legal edges")
    return frozenset(F)


def independent_small_frozen_pair_kernel(a, frozen_pairs=()):
    """Independent brute force ORIGINAL right-label kernel, a=6 or 7.

    This is an oracle for the all-h polynomial (empty F), AND a true
    finite exact extension of its conditional F-residual identity.
    """
    if type(a) is not int or a not in (6,7):
        raise ValueError("full pair-pair direct check supports only a=6,7")
    F=_validate_forbidden(a,frozen_pairs)
    factors=[]
    for support in combinations(range(a),6):
        for S in twofactors_on_six(support):
            if not S&F:
                factors.append(S)
    nr=[0]*7
    for x in factors:
        for y in factors:
            nr[len(x&y)]+=1
    if sum(nr)!=len(factors)**2:
        raise AssertionError("independent pair-of-physical-2factors census failed")
    return tuple(nr)


def conditional_right_A_pair_probabilities(a, frozen_pairs=()):
    """Return exact P_r=Pr(two right A acceptances | overlap r).

    With zero F the exact all-a compressed template formula applies;
    with nonzero frozen F the direct independent a=6,7 finite oracle
    supplies exact N_r. At general a,F the valid all-h statement is
    P_r=N_r(a,F)*r!*(6-r)!^2/(M-|F|)_(12-r); formula remains true,
    but this implementation deliberately does NOT claim a fast
    polynomial frozen-F evaluator.
    """
    if type(a) is not int or a<6:
        raise ValueError("a must be at least six")
    F=_validate_forbidden(a,frozen_pairs)
    nr=(independent_small_frozen_pair_kernel(a,F)
        if F else unrestricted_twofactor_pair_intersection_counts(a))
    M=comb(a,2)-len(F)
    out=[]
    for r,n in enumerate(nr):
        den=falling(M,12-r)
        p=(Fraction(n*factorial(r)*factorial(6-r)**2,den)
           if den else Fraction(0))
        if not 0<=p<=1:
            raise AssertionError("joint probability outside [0,1]")
        out.append(p)
    # P_6 equals one-event probability: source Q,Q' share six
    # right line IDs, hence the same historical right A event.
    single=Fraction(720*nr[6],falling(M,6)) if M>=6 else Fraction(0)
    if out[6]!=single:
        raise AssertionError("same-source-line-support right event identity")
    return tuple(out)


def source_support_overlap_pairs(original_source_line_masks, V):
    """EXACT ordered pair overlap r for a weighted set of ORIGINAL B 6sets.

    Each source candidate has one mask with exactly SIX distinct actual
    original source-line factor IDs in [0,V). Different ORIGINAL
    incidence-sixsets can have the same 6-line mask and MUST each count:
    use multiplicity rather than deduplicating original source sets.
    """
    if type(V) is not int or V<6:
        raise ValueError("V must be number of ORIGINAL source line factors")
    masks=tuple(original_source_line_masks)
    if any(type(mask) is not int or mask<0 or mask.bit_length()>V
           or mask.bit_count()!=6 for mask in masks):
        raise ValueError("each true original source sixset needs six line IDs")
    weights=Counter(masks)
    ordered=[0]*7
    for x,wx in weights.items():
        for y,wy in weights.items():
            ordered[(x&y).bit_count()]+=wx*wy
    if sum(ordered)!=len(masks)**2:
        raise AssertionError("original source support pair census missing entries")
    return tuple(ordered)


def exact_BA_second_moment_from_masks(masks,V,a,*,frozen_pairs=()):
    """EXACT joint source-label second moment, deterministic fixed f.

    The original B candidate family must already have been fully and
    canonically verified for that f and source W(3,s), with all its
    original sixsets using six distinct source line factors outside
    the frozen J (if present). This function checks only their line-ID
    supports, not a claimed geometry from arbitrary input masks.
    """
    masks=tuple(masks)
    overlaps=source_support_overlap_pairs(masks,V)
    P=conditional_right_A_pair_probabilities(a,frozen_pairs)
    first=Fraction(len(masks))*P[6]
    second=sum((count*p for count,p in zip(overlaps,P)),Fraction(0))
    variance=second-first*first
    if variance<0:
        raise AssertionError("negative source-original B/A second moment variance")
    pz=first*first/second if second else Fraction(0)
    if not 0<=pz<=1:
        raise AssertionError("Paley-Zygmund exact value outside [0,1]")
    return {
        "source_left_B_original_sixsets_with_six_distinct_lines":len(masks),
        "original_ordered_sixset_pairs_by_common_source_lines":overlaps,
        "right_physical_twofactor_pair_counts_by_common_edges":(
            independent_small_frozen_pair_kernel(a,frozen_pairs)
            if frozen_pairs else
            unrestricted_twofactor_pair_intersection_counts(a)
        ),
        "right_A_pair_joint_probabilities_by_source_line_overlap":P,
        "E_original_BA":first,
        "E_original_BA_squared":second,
        "variance_original_BA":variance,
        "Paley_Zygmund_probability_original_BA_positive_lower":pz,
        "all_h_exact_conditional_second_moment_identity":True,
        "adversarial_all_g_lower_proved":False,
        "root_A_B_C_proved":False,
    }


def genuine_W32_left_B_source_masks(scheme="lex", frozen_original_lines=()):
    """True symplectic W(3,2), independent historical left-six enumerator.

    DO NOT replace this source with a sample/independent synthetic graph.
    The historical selected_left_six engine enumerates every physically
    accepted ORIGINAL six-incidence left B exactly once.
    """
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    m=pair_labeled_symplectic(1,scheme)
    J=frozenset(frozen_original_lines)
    if any(type(z) is not int or not 0<=z<m["v"] for z in J):
        raise ValueError("invalid frozen ORIGINAL line ID")
    flags=m["incidences"]
    masks=[]
    for ids,kind in selected_left_six(m):
        if kind!="B":
            continue
        lines=tuple(flags[i][1] for i in ids)
        if len(set(lines))!=6 or any(z in J for z in lines):
            continue
        masks.append(sum(1<<z for z in lines))
    return m,tuple(masks)


def certified_true_W32_BA_pair_moment(scheme="lex", frozen_original_lines=()):
    """Original W32 exact source support join; g random ONE full injection."""
    m,masks=genuine_W32_left_B_source_masks(scheme,frozen_original_lines)
    F=tuple(m["right_labels"][z] for z in frozen_original_lines)
    result=exact_BA_second_moment_from_masks(
        masks,m["v"],m["a"],frozen_pairs=F)
    result.update({
        "source": "true original W(3,2) symplectic incidence, not K6 proxy",
        "fixed_point_labels_scheme":scheme,
        "frozen_original_source_line_ids":tuple(frozen_original_lines),
        "frozen_physical_right_pairs":F,
        "no_asymptotic_inference_from_W32":True,
    })
    return result
