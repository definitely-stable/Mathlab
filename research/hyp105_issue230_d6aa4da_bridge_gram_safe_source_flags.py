"""AA4-DA: genuine original W(3,s) BRIDGE-GRAM bound on RAW->SAFE loss.

For all dyadic h>=96, all original symplectic GQ W(3,2^h), ALL
globally injected complete, arbitrarily correlated typed physical pair
maps and ANY two physical halfcuts, at least s^7/2^14 genuine original
incidence mass persists between physically SAFE source spokes of true
original NONINCIDENT, doubled-disjoint P3 anchors; >=s^(11/2)/2^35
distinct anchors have at least one SAFE genuine original incidence.

We DO NOT claim two actually occupied physical C4 centers or an
ORIGINAL 3x3 perfect matching / accepted historical six-ID GF5 motif.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb, isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath
from hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion import (
    original_cut_doubled_exclusion_certificate,
)
from hyp105_issue230_d6aa4cz_collinearity_badpath_mass import (
    allh_original_collinearity_badpath_arithmetic,
    original_cut_badpath_mass_certificate,
)


def allh_original_bridge_gram_safe_arithmetic(h):
    """Exact arbitrary precision dyadic falsifier, analytical argument in proof."""
    z=allh_original_collinearity_badpath_arithmetic(h)
    s,V,a,k,d=(z[t] for t in ("s","V","a","k","d"))
    # Source graph and physical alphabet conservative simple bounds:
    # a-2 <= 2*s^(3/2), k<=s^(3/2), d<=2s, V<=2s^3.
    # For both typed loss directions, a single source-collinear
    # ordered P3 bridge-triple count <= 4V*s*d <=16s^5.
    # Fixed projection q and bridge factor i can admit <=a-2 p,
    # so sum_{q,i} r(q,i)^2 <= (a-2)*4Vsd <=32s^(13/2).
    # K_g=M A_g M^T and K_f=M^T A_f M have Frobenius norm <=
    # 2kd^2 +4dk sqrt(2s)+2s sqrt(2kV) <=32s^(7/2).
    # One side loss <=sqrt(32)*32 s^(27/4)<192s^(27/4);
    # both sides <=384s^(27/4).
    #
    # On good double-disjoint source nonincident P3 AA4-CZ Traw
    # >=dVk²/2048 >= s^7/8192. At h>=96:
    # 384s^(27/4)<=s^7/16384, so SAFE >=s^7/16384.
    # Q_global <=64sVk³<=128s^(17/2), giving #SAFE-positive
    # >=s^(11/2)/2^35, with NO occupation or 3x3 matching inference.
    if h>=96:
        if not (
            (a-2)**2 <=4*s**3
            and 4*k*k<=4*s**3
            and V<=2*s**3 and d<=2*s
            and 4*k*k>=s**3
            and s>=(384*16384)**4
            and (4*V*s*d)*(a-2)<=32*s**6*isqrt(s)
        ):
            raise AssertionError("all-h AA4-DA bridge Gram exponent/constant gate invalid")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"d":d,
        "typed_bridge_triplet_number_bound_exact":4*V*s*d,
        "typed_bridge_triplet_max_multiplicity_upper":a-2,
        "typed_bridge_multiplicity_square_sum_upper":4*V*s*d*(a-2),
        "allh_each_typed_bridge_loss_upper_quarter_exponent_numerator":192,
        "allh_both_typed_bridge_loss_upper_quarter_exponent_numerator":384,
        "allh_global_raw_double_disjoint_mass_lower_numerator":s**7,
        "allh_global_raw_double_disjoint_mass_lower_denominator":8192,
        "allh_global_SAFE_original_flag_mass_lower_numerator":s**7,
        "allh_global_SAFE_original_flag_mass_lower_denominator":16384,
        "allh_SAFE_positive_nonincident_double_disjoint_P3_lower_squared_numerator":s**11,
        "allh_SAFE_positive_nonincident_double_disjoint_P3_lower_squared_denominator":1<<70,
        "allh_SAFE_positive_nonincident_double_disjoint_P3_floor_integer":
            isqrt(s**11)//(1<<35),
        "allh_gate_h_ge_96":h>=96,
        "original_complete_C4_and_source_3x3_matching_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _bridge_factors(left,right,inverse):
    """EXACT four physical bridge-pair labels for disjoint original images."""
    left,right=frozenset(left),frozenset(right)
    if not left.isdisjoint(right):
        return ()
    return tuple(i for u,v in product(left,right)
                 if (i:=inverse.get(tuple(sorted((u,v))))) is not None)


def original_cut_bridge_gram_certificate(model,X=None,Y=None):
    """Finite TRUE ORIGINAL SOURCE point/dual line bridge loss majorant.

    Computes exact sum over SOURCE collinear ordered p,q and their 0..4
    available physical bridge original point IDs i, weighted by
    K_g(q,i)=(M A_g M^T)[q,i], plus its true-source dual for L.
    The ACTUAL exact SAFE deletion is measured independently by CX.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    prior=original_cut_badpath_mass_certificate(model,X,Y)
    cx=original_cut_doubled_exclusion_certificate(model,X,Y)
    px=frozenset(i for i in range(V) if set(f[i])<=set(X))
    ly=frozenset(j for j in range(V) if set(g[j])<=set(Y))
    pf={p:frozenset(i for i in px if i!=p and bool(set(f[p])&set(f[i]))) for p in px}
    gl={l:frozenset(j for j in ly if j!=l and bool(set(g[l])&set(g[j]))) for l in ly}
    inv_f={tuple(sorted(e)):i for i,e in enumerate(f)}
    inv_g={tuple(sorted(e)):j for j,e in enumerate(g)}
    if len(inv_f)!=V or len(inv_g)!=V:
        raise AssertionError("all original typed source physical factor images must be injected")
    @lru_cache(None)
    def K_g(q,i):
        # Every line on actual original point q, every original line
        # on actual source point i. Physical g overlaps iff A_g=1.
        return sum(len(gl[l].intersection(pl[i])) for l in pl[q] if l in ly)
    @lru_cache(None)
    def K_f(l0,j):
        # Dual: original points incident with actual source lines l0,j.
        return sum(len(pf[p].intersection(lp[j])) for p in lp[l0] if p in px)

    def typed_bridge_total(labels,inverse,sources,dual,Gram):
        total=0
        multiplicity=defaultdict(int)
        candidate_count=0
        checked_oriented_source_collinear=0
        for p in range(V):
            neighbors=set()
            for intermediate in sources[p]:
                neighbors.update(dual[intermediate])
            neighbors.discard(p)
            if len(neighbors)!=s*(s+1):
                raise AssertionError("not genuine GQ original oriented collinear source pair set")
            for q in neighbors:
                checked_oriented_source_collinear+=1
                bridge=_bridge_factors(labels[p],labels[q],inverse)
                if len(bridge)>4:
                    raise AssertionError("more than four K_a coordinate bridge edges")
                for i in bridge:
                    candidate_count+=1
                    multiplicity[q,i]+=1
                    total+=Gram(q,i)
        if candidate_count>4*V*s*(s+1):
            raise AssertionError("source typed 4-bridge triple bound invalid")
        if max(multiplicity.values(),default=0)>a-2:
            raise AssertionError("fixed projection source-pair bridge multiplicity exceeds a-2")
        if sum(n*n for n in multiplicity.values())>candidate_count*(a-2):
            raise AssertionError("original source bridge multiplicity CS bound invalid")
        return {
            "true_original_collinear_oriented_pairs_checked":checked_oriented_source_collinear,
            "real_source_typed_bridge_triples":candidate_count,
            "max_bridge_multiplicity_at_source_projection_and_source_bridge":
                max(multiplicity.values(),default=0),
            "bridge_multiplicity_squared_sum":sum(n*n for n in multiplicity.values()),
            "original_MAgMt_or_dual_MtAfM_Gram_exact_weighted_majorant":total,
        }

    left=typed_bridge_total(f,inv_f,pl,lp,K_g)
    right=typed_bridge_total(g,inv_g,lp,pl,K_f)
    actual_raw=prior["actual_original_raw_good_nonincident_double_disjoint_mass"]
    actual_safe=cx["SAFE_original_source_incidence_mass_double_disjoint"]
    actual_loss=cx["exact_original_source_incidence_loss"]
    if actual_raw !=cx["raw_original_source_incidence_mass_double_disjoint"]:
        raise AssertionError("original source before/after filtered raw provenance mismatch")
    if actual_raw-actual_safe!=actual_loss:
        raise AssertionError("real original RAW SAFE source flag partition invalid")
    Lbound=left["original_MAgMt_or_dual_MtAfM_Gram_exact_weighted_majorant"]+right[
        "original_MAgMt_or_dual_MtAfM_Gram_exact_weighted_majorant"]
    if Lbound<actual_loss:
        raise AssertionError("genuine original bridge-Gram bound undercounts actual original lost flags")
    if s>=1<<96:
        z=allh_original_bridge_gram_safe_arithmetic(s.bit_length()-1)
        if actual_safe*16384<s**7:
            raise AssertionError("universal actual ORIGINAL SAFE cross-flag mass theorem false")
        if (1<<35)**2*cx["double_disjoint_SAFE_spoke_positive_anchors"]**2<s**11:
            raise AssertionError("universal true ORIGINAL SAFE-positive P3 source support theorem false")
    return {
        "s":s,"V":V,"a":a,"k":k,
        "original_genuine_double_disjoint_nonincident_P3":prior["actual_genuine_original_nonincident_cut_P3"]-prior["actual_bad_union_nonincident_P3"],
        "true_original_double_disjoint_RAW_incidence_mass":actual_raw,
        "true_original_double_disjoint_SAFE_incidence_mass":actual_safe,
        "exact_original_RAW_to_SAFE_flag_loss":actual_loss,
        "independent_original_left_bridge_Gram":left,
        "independent_original_right_bridge_Gram":right,
        "total_true_original_bridge_Gram_loss_majorant":Lbound,
        "original_safe_positive_double_disjoint_nonincident_P3":
            cx["double_disjoint_SAFE_spoke_positive_anchors"],
        "original_3x3_perfect_matching_NOT_DEDUCED":True,
        "original_historical_GF5_sixflag_NOT_DEDUCED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
