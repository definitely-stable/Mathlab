"""HYP-105 AA4-XPACK: THREE LEVELS of all-map six-motif transversality.

From the same-source arbitrary ORIGINAL-ID deletion theorem AA4-UDEL (#674):
for any true W(3,s), arbitrary legal full separately injected correlated
f,g, if |Z|<=rho*s**4, there are >=delta*s**6 accepted ORIGINAL D6
or B/B-overlap sixsets with all SIX source flags outside Z.

Source ORIGINAL point/line-factors and physical coordinate symbols each
have a provably bounded *incidence FLAG* exposure. Lifting UDEL gives:
- deleting P original points and L original lines costs <=(s+1)(|P|+|L|)
  source flags;
- deleting X physical LEFT coords and Y physical RIGHT coords costs
  <=(s+1)(a-1)(|X|+|Y|) source flags;
- every original accepted D6/BBo sixset occupies <=12 original
  point/line factors, and exactly 12 physical left/right coordinate
  symbols (six per side).
Therefore maximal original-factor-disjoint accepted motif packing is
>rho*s**4/[12(s+1)], and maximal physical-coordinate-disjoint accepted
motif packing >rho*s**4/[12(s+1)(a-1)], for all s>=s0 from #674.
The new floor is conditional on the DRAFTED #674 theorem, NOT a new
external independent proof of root Branch A.

Small finite original-source W(3,2),W(3,4) oracles falsify source
erasure bookkeeping, unchanged historical seven-class classification,
and physical pair-label exposure bounds for arbitrary legal f,g.
"""
from collections import Counter
from fractions import Fraction
from math import comb

from hyp105_allh_annealed_BA_floor import validate_typed_pairs
from hyp105_physical_degree_energy import minimal_alphabet
from hyp105_full_physical_degree_tail import genuine_source
from hyp105_unconditional_original_deletion import (
    exact_unconditional_constants,
)


def validate_factor_and_physical_erasure(s, left_point_ids=(),right_line_ids=(),
                                         left_coordinates=(),right_coordinates=(),
                                         *,point_labels=None,line_labels=None):
    """Return SOURCE flag erasure Z and tight *universal* exposure budgets.

    All IDs are TRUE original W(3,s) factors and two physical coordinate
    alphabets are distinct typed domains. Physical point- and line-pair
    injections f,g are complete and separately globally injected.
    Finite actual flag Z only supported for s=2 or s=4, which is
    explicitly not a high-h asymptotic test.
    """
    if type(s) is not int or s not in (2,4):
        raise ValueError("finite TRUE symplectic GQ erasure oracle only s=2,4")
    if point_labels is None or line_labels is None:
        raise ValueError("full point and line pair injections required")
    V=(s+1)*(s*s+1)
    a=minimal_alphabet(V)
    f=validate_typed_pairs(s,point_labels)
    g=validate_typed_pairs(s,line_labels)
    P=tuple(left_point_ids)
    L=tuple(right_line_ids)
    X=tuple(left_coordinates)
    Y=tuple(right_coordinates)
    for vals,upper in ((P,V),(L,V),(X,a),(Y,a)):
        if any(type(i) is not int or not 0<=i<upper for i in vals):
            raise ValueError("factor/coordinate erasure contains invalid ID")
        if len(set(vals))!=len(vals):
            raise ValueError("erased factor/coordinate IDs must be distinct")
    Ps=set(P);Ls=set(L);Xs=set(X);Ys=set(Y)
    _,_,flags=genuine_source(s.bit_length()-1)
    marked_point={i for i in range(V) if i in Ps or Xs.intersection(f[i])}
    marked_line={j for j in range(V) if j in Ls or Ys.intersection(g[j])}
    physical_point={i for i in range(V) if Xs.intersection(f[i])}
    physical_line={j for j in range(V) if Ys.intersection(g[j])}
    Z=tuple(i for i,(p,ell) in enumerate(flags)
            if p in marked_point or ell in marked_line)
    point_lines=Counter(p for p,ell in flags)
    line_points=Counter(ell for p,ell in flags)
    if set(point_lines.values())!={s+1} or set(line_points.values())!={s+1}:
        raise AssertionError("not the true (s+1)-regular ORIGINAL source")
    # Count physical exposure by ANOTHER method over full source flags.
    direct_Z=tuple(i for i,(p,ell) in enumerate(flags)
            if (p in Ps or ell in Ls
                or any(x in f[p] for x in Xs)
                or any(y in g[ell] for y in Ys)))
    if Z!=direct_Z:
        raise AssertionError("independent source flag erasure methods disagree")
    d=s+1
    marked_factor_budget=d*(len(P)+len(L))
    physical_factor_budget=d*(a-1)*(len(X)+len(Y))
    combined_budget=marked_factor_budget+physical_factor_budget
    if len(physical_point)>(a-1)*len(X) or (
            len(physical_line)>(a-1)*len(Y)):
        raise AssertionError("global injection coordinate-degree bound violated")
    if len(Z)>min(len(flags),combined_budget):
        raise AssertionError("true ORIGINAL six-ID erasure exceeds budget")
    return {
        "s":s,"V":V,"a":a,"original_flags":len(flags),
        "deleted_true_original_point_factors":P,
        "deleted_true_original_line_factors":L,
        "deleted_left_physical_coordinate_symbols":X,
        "deleted_right_physical_coordinate_symbols":Y,
        "source_erasure_original_flag_ids":Z,
        "source_erasure_count":len(Z),
        "point_factor_exposure_upper":marked_factor_budget,
        "physical_coordinate_exposure_upper":physical_factor_budget,
        "combined_exposure_upper":combined_budget,
        "direct_scan_equals_original_factor_union":True,
        "real_W3_geometry_not_sampled":True,
    }


def asymptotic_transversal_hierarchy(s, C_graph=1,c_graph=Fraction(1)):
    """EXACT s-specific universal thresholds, relative to #674's rho.

    External graph constants C,c passed in only as *formal* placeholders
    in CI. Actual balanced Simonovits SS6 theorem provides some
    unknown positive absolute constants. No C=c=1 validity claimed.

    Bound assures S_avoid>=delta*s6 ONLY when s>=s0.
    Factor/coordinate occupancy supports are counted across BOTH typed
    source domains and BOTH distinct physical coordinate domains.
    """
    if type(s) is not int or s<2 or (s&(s-1)):
        raise ValueError("s must be an integer dyadic >=2")
    base=exact_unconditional_constants(C_graph,c_graph)
    rho=base["allowed_original_flag_deletion_density_rho"]
    delta=base["accepted_sixset_all_map_floor_delta"]
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    a=minimal_alphabet(V)
    d=s+1
    # Conservative maximum total erased factor labels, or physical
    # symbol labels, across both typed source domains.
    original_factor_budget=int(rho*s**4//d)
    physical_coordinate_budget=int(rho*s**4//(d*(a-1)))
    original_flag_budget=int(rho*s**4)
    return {
        "s":s,"V":V,"a":a,"N":N,
        "original_flag_deletion_budget":original_flag_budget,
        "source_point_plus_line_factor_deletion_budget":
            original_factor_budget,
        "left_plus_right_physical_symbol_deletion_budget":
            physical_coordinate_budget,
        "guaranteed_surviving_original_D6_plus_BBo_min":
            delta*s**6,
        "strict_lower_original_flag_disjoint_pack":
            rho*s**4/6,
        "strict_lower_original_point_and_line_factor_disjoint_pack":
            rho*s**4/(12*d),
        "strict_lower_left_and_right_physical_symbol_disjoint_pack":
            rho*s**4/(12*d*(a-1)),
        "max_original_factor_labels_per_selected_sixset":12,
        "physical_symbol_labels_per_selected_sixset":12,
        "left_physical_symbol_labels_per_selected_sixset":6,
        "right_physical_symbol_labels_per_selected_sixset":6,
        "requires_s_at_least_s0":base["sufficient_s0_integer"],
        "actual_s_meets_sufficient_threshold":
            s>=base["sufficient_s0_integer"],
        "external_graph_constants_are_formal_inputs_not_claimed_values":True,
        "parent_674_theorem_not_independently_reproved":True,
        "root_branch_A_external_scientific_acceptance":False,
    }


def finite_accepted_genuine_two_class_motifs(
        s,point_labels,line_labels,erased_flag_ids=()):
    """True ORIGINAL W32/W34 full two-class accepted sets after source Z.

    Uses existing independent source-backed exact physical D6 and
    physical path BBo reconstructors. Their output is a SUBFAMILY of
    true original BBo, so we NEVER claim equality with the full class.
    """
    from hyp105_unconditional_original_deletion import (
        finite_original_D6_avoiding_flags,
    )
    from hyp105_bbo_resilience import avoidance_certificate
    q=finite_original_D6_avoiding_flags(
        s.bit_length()-1,point_labels,line_labels,erased_flag_ids)
    p=avoidance_certificate(
        s.bit_length()-1,point_labels,line_labels,erased_flag_ids)
    D=set(map(tuple,q["accepted_original_D6_sixsets"]))
    B=set(map(tuple,p["produced_sixsets"]))
    if D&B:raise AssertionError("accepted ORIGINAL classes D6 and BBo overlap")
    _,_,flags=genuine_source(s.bit_length()-1)
    f=validate_typed_pairs(s,point_labels)
    g=validate_typed_pairs(s,line_labels)
    X={}
    for ids in D|B:
        if len(set(ids))!=6 or set(ids)&set(erased_flag_ids):
            raise AssertionError("six distinct surviving original flags needed")
        ps={flags[i][0] for i in ids}
        ls={flags[i][1] for i in ids}
        lc={x for pnt in ps for x in f[pnt]}
        rc={y for ln in ls for y in g[ln]}
        if len(lc)!=6 or len(rc)!=6:
            raise AssertionError("original accepted sixset touches six physical coordinates per half")
        if len(ps)+len(ls)>12:
            raise AssertionError("accepted original sixset exceeds 12 source factor labels")
        X[ids]=(frozenset(ps),frozenset(ls),frozenset(lc),frozenset(rc))
    return {
        "D6":D,"BBo_verified_subfamily":B,
        "source_and_physical_supports":X,
        "accepted_genuine_GF5_two_class_subcount":len(D)+len(B),
        "does_not_claim_full_BBo_census":True,
    }


def greedy_maximal_packing_by_supports(support_map, kind):
    """Finite REAL source-set packing oracle across both typed halves.

    kind='factors' makes ORIGINAL point/line factors disjoint;
    kind='physical' makes LEFT/RIGHT physical coordinates disjoint.
    No asymptotic count inferred from a small-h greedy result.
    """
    if kind not in ("factors","physical"):
        raise ValueError("packing support kind must be factors or physical")
    i,j=(0,1) if kind=="factors" else (2,3)
    used_left=set();used_right=set();chosen=[]
    for ids,tup in sorted(support_map.items()):
        L,R=tup[i],tup[j]
        if not used_left.intersection(L) and not used_right.intersection(R):
            chosen.append(ids)
            used_left.update(L);used_right.update(R)
    if any(
            not used_left.intersection(x[i]) and not used_right.intersection(x[j])
            for x in support_map.values()):
        raise AssertionError("greedy matching not maximal in typed support hypergraph")
    return {
        "kind":kind,
        "motif_six_original_incidence_IDs":tuple(chosen),
        "count":len(chosen),
        "covered_left_factor_or_coordinate_names":tuple(sorted(used_left)),
        "covered_right_factor_or_coordinate_names":tuple(sorted(used_right)),
        "covered_typed_names_count":len(used_left)+len(used_right),
        "typed_maximal_support_matching_checked":True,
    }
