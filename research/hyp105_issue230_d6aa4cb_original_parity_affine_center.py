"""AA4-CB: true-original GF(2) edge-boundary affine parity screen.

ALL genuine original symplectic W(3,2^h), h>=1, and every complete
globally injective, arbitrarily correlated physical POINT f / LINE g.
Six DISTINCT true original incidence IDs Q are invariant across whole
source LINE-factor image swaps. The right physical edge-degree PARITY
vector is an affine GF(2)^a function of source LINE swap bits.

Any historical selected positive seven-GF5 acceptance implies ZERO
right degree parity and 2-regularity on EXACTLY SIX vertices. These
two nested right-physical screens yield computable, fixed-(f,g)
absolute highpass envelopes that can be strictly smaller than the
prior original f-only abstract N3 eta6=15/16.

This is an a posteriori original UNCHANGED map certificate, NOT
a uniform positive Omega(s^6) conclusion or Branch A/B/C.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,
)
from hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel import (
    AA4CA_EXACT_ABSTRACT_N3_ETA6,
    original_W32_f_only_all_seven_exact_n3_envelope,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def _edge_boundary(edge):
    """Unsigned physical pair-edge boundary in GF(2) physical vertices."""
    a,b=edge
    return (1<<a) ^ (1<<b)


def _gf2_rank(columns):
    """True finite F2 Gaussian elimination, independent of equation rhs."""
    pivots={}
    for v in columns:
        x=v
        while x:
            k=x.bit_length()-1
            if k in pivots:
                x^=pivots[k]
            else:
                pivots[k]=x
                break
    return len(pivots)


def _source_parity_raw(Q,inc,g,pairs):
    """Exact local affine GF2 condition for original right physical 2-factor.

    Input is already validated by outer public entrypoint. Each source
    LINE image has the SAME pair-edge at all its original incidences,
    and an entire source transposition swaps BOTH images globally.
    """
    line_counts=Counter(inc[j][1] for j in Q)
    used=tuple(i for i,(u,v) in enumerate(pairs)
               if line_counts[u] or line_counts[v])
    base=0
    for j in Q:
        base^=_edge_boundary(g[inc[j][1]])
    deltas=tuple(
        (_edge_boundary(g[pairs[i][0]]) ^ _edge_boundary(g[pairs[i][1]]))
        if (line_counts[pairs[i][0]]+line_counts[pairs[i][1]])%2 else 0
        for i in used)
    rank=_gf2_rank(deltas)
    boundary=[base]*(1<<len(used))
    for y in range(1,len(boundary)):
        bit=y&-y
        boundary[y]=boundary[y^bit]^deltas[bit.bit_length()-1]
    allowed=tuple(i for i,v in enumerate(boundary) if v==0)
    if allowed and len(allowed)!=(1<<(len(used)-rank)):
        raise AssertionError("original parity-zero right maps must be affine GF2 coset")
    return used,deltas,base,rank,allowed


def _right_two_factor_local(Q,inc,g,pairs,used,y):
    """Literal ORIGINAL six incidence right six-edge physical 2-factor.

    Does NOT classify historical source GF5. Uses the SAME real SOURCE
    Q at each globally coherent swap vertex, including repeated lines.
    """
    toggle=frozenset(used[j] for j in range(len(used)) if y>>j&1)
    changed={}
    for i in toggle:
        u,v=pairs[i]
        changed[u]=g[v]
        changed[v]=g[u]
    d=Counter(vertex for j in Q
              for vertex in changed.get(inc[j][1],g[inc[j][1]]))
    return len(d)==6 and all(v==2 for v in d.values())


def _screen_error(support,k,*, all_centers):
    """Two-sided signed highpass kernel envelope on a NECESSARY support.

    Let b(y) be the unknown ACTUAL historical original GF5 0/1
    indicator, with b(y)=0 outside screen. For EACH cube vertex x,
    local Fourier degree>3 residual is
         2^-k sum_{y in screen} b(y) K_k(x xor y).
    Split by positive/negative kernel coefficients and maximize.
    This bound is valid for all Boolean patterns without assuming
    independent Q or new original geometric symmetry.
    """
    if k<=3:return Fraction(0)
    K=high_degree_boolean_kernel(k)
    active=frozenset(support)
    if any(type(j) is not int or j<0 or j>=1<<k for j in active):
        raise ValueError("invalid local source-packet support mask")
    maxi=0
    for x in (range(1<<k) if all_centers else (0,)):
        pos=sum(max(0,K[x^y]) for y in active)
        neg=sum(max(0,-K[x^y]) for y in active)
        maxi=max(maxi,pos,neg)
    return Fraction(maxi,1<<k)


def genuine_original_Q_parity_sixcube(model,Q,pairs,*, verify_historical=True):
    """Independently falsifiable exact GF2 parity affine profile of ONE Q."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6:raise ValueError("six disjoint genuine source LINE swaps")
    Q=tuple(Q)
    if len(Q)!=6 or len(set(Q))!=6 or any(
        type(j) is not int or j<0 or j>=len(inc) for j in Q
    ):
        raise ValueError("exact six DISTINCT original incidence IDs")
    used,deltas,base,rank,allowed=_source_parity_raw(Q,inc,g,pairs)
    degree2=tuple(y for y in allowed
                  if _right_two_factor_local(Q,inc,g,pairs,used,y))
    if not set(degree2)<=set(allowed):
        raise AssertionError("2regular physical graph must have even vertex degree")
    tag=immutable_original_sixflag_class(Q,inc)
    historic=()
    if verify_historical:
        accepted=[]
        for y in range(1<<len(used)):
            changed=apply_disjoint_factor_swaps(
                g,pairs,tuple(used[j] for j in range(len(used))
                              if y>>j&1))
            got=classify_seven_prechecked(Q,f,changed,inc)
            if got is not None and got!=tag:
                raise AssertionError("genuine Q historical class is immutable")
            if got is not None:accepted.append(y)
        historic=tuple(accepted)
        if not set(historic)<=set(degree2):
            raise AssertionError("historical seven-GF5 acceptance failed physical parity screen")
    k=len(used)
    return {
        "same_six_original_incidence_Q":Q,
        "original_possible_historical_class":tag,
        "touched_original_LINE_packet_indices":used,
        "original_full_right_map_GF2_boundary":base,
        "onebit_original_source_GF2_boundary_deltas":deltas,
        "exact_GF2_column_rank":rank,
        "parity_zero_affine_coset":allowed,
        "zero_parity_state_count":len(allowed),
        "physical_right_2regular_states":degree2,
        "historically_accepted_original_GF5_states":historic,
        "local_parity_center_absolute_highpass_upper":
            _screen_error(allowed,k,all_centers=False),
        "local_parity_ALL_VERTEX_absolute_highpass_upper":
            _screen_error(allowed,k,all_centers=True),
        "local_2regular_center_absolute_highpass_upper":
            _screen_error(degree2,k,all_centers=False),
        "local_2regular_ALL_VERTEX_absolute_highpass_upper":
            _screen_error(degree2,k,all_centers=True),
        "valid_for_every_correlated_original_f_g":True,
    }


def true_original_W32_g_conditioned_all_seven_center(model,pairs):
    """G-QUENCHED per-original-Q parity and physical 2factor Fourier bound.

    62,370 true left eligible original six-incidence IDs are enumerated
    once. Only immutable historical POSSIBLE seven classes and k>=4
    can contribute at highpass order. Parity/2factor tests do NOT call
    historical GF5 classifier and do NOT redraw a local source Q.
    Uniform all-vertex and original x=0 envelopes both produced.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite exact original W32 physical K6 source oracle only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6:raise ValueError("six disjoint source LINE image pairs")
    original_f_only=original_W32_f_only_all_seven_exact_n3_envelope(model,pairs)
    weights=R3_CERTIFIED_FLOORS
    perclass=Counter()
    status=Counter()
    accum={label:Fraction(0) for label in (
        "parity_original_center","parity_uniform",
        "right_2factor_original_center","right_2factor_uniform")}
    touched=0
    for Q,_ in selected_left_six(model):
        tag=immutable_original_sixflag_class(Q,inc)
        if tag not in weights:continue
        used,deltas,base,rank,parity=_source_parity_raw(Q,inc,g,pairs)
        k=len(used)
        if k<=3:continue
        touched+=1
        perclass[(tag,k)]+=1
        status[("rank",k,rank)]+=1
        status[("parity_empty",k,len(parity)==0)]+=1
        degree2=tuple(y for y in parity if
            _right_two_factor_local(Q,inc,g,pairs,used,y))
        status[("two_factor_empty",k,len(degree2)==0)]+=1
        weight=weights[tag]
        accum["parity_original_center"]+=weight*_screen_error(
            parity,k,all_centers=False)
        accum["parity_uniform"]+=weight*_screen_error(
            parity,k,all_centers=True)
        accum["right_2factor_original_center"]+=weight*_screen_error(
            degree2,k,all_centers=False)
        accum["right_2factor_uniform"]+=weight*_screen_error(
            degree2,k,all_centers=True)
    parent=original_f_only["new_AA4CA_E"]
    # Even-degree and 2regular are NECESSARY but not SUFFICIENT for
    # actual historical accepted GF5 patterns. Old parent eta_k
    # supplies independent TRUE ORIGINAL universal source constraints.
    # Their MIN on each per-Q would be even sharper; summing MIN after
    # the aggregate gives a valid, albeit less sharp, common bound.
    for label in accum:
        accum[label]=min(parent,accum[label])
    if not (accum["right_2factor_original_center"]<=
            accum["parity_original_center"] and
            accum["right_2factor_uniform"]<=accum["parity_uniform"] and
            accum["parity_original_center"]<=accum["parity_uniform"] and
            accum["right_2factor_original_center"]<=accum["right_2factor_uniform"]):
        raise AssertionError("original geometric support nesting invalid")
    return {
        "s":s,"V":V,"a":a,
        "genuine_original_6packet_pairs":pairs,
        "source_Q_high_order_candidates":touched,
        "source_historical_class_by_original_touch_count":dict(perclass),
        "GF2_source_boundary_rank_histogram":dict(status),
        "parent_original_f_only_all_seven_E":parent,
        "true_original_g_quenched_all_seven_envelopes":accum,
        "exact_g_conditional_parity_linear_system_each_Q":True,
        "original_LEFT_physical_f_is_unchanged":True,
        "original_RIGHT_full_g_is_unchanged_at_center":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
