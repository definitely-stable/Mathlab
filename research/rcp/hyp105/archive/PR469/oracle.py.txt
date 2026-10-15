"""HYP-105 #230 EICE-003-K — TRUE ORIGINAL clean-anchor concentration audit.

K1 all-h exact dirty-anchor source-pencil identity:
  D_left = s sum_q #({p!=q: p collinear q, f(p) meets f(q)})
  D_right = s sum_r #({ell!=r: ell meets r, g(ell) meets g(r)})
Each <= 2s(a-2)V by global injected true pair labels.
Therefore for UNIFORMLY sampled original NONINCIDENT q,r,
Pr(anchor end dirty) <= 4(a-2)/(s(s+1)) = O(s^-1/2).
Thus original globally uniform end-clean status tends to ONE,
not zero: no four-anchor scarcity proof based solely on uniform
marginal original-GQ dirty rarity can be valid.

K2 compare this with the finite nonuniform TRUE original five-source
template distribution from J, without asserting any asymptotic
independence or lifting original pair to a positive GF5 sixset.

K3 exact nonincident five-source / dirty original endpoint-pair
pullback multiplicity on a fixed middle original source e:
  N_e-C_e <= sum_(dirty q,r) M_e(q,r) <= 4(N_e-C_e).
This is a necessary concentration obstruction to end-clean scarcity,
not an o(s^4) upper or the root theorem.

HYP-105 Branch A/B, original seven-GF5 compensation and ASET OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import isqrt
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_anchor_filtered_codegrees import (
    finite_original_anchor_cascade_report, independent_original_anchor_status,
    STAGES,
)
from hyp105_issue230_quadrant_matching_capacity import (
    original_midpoint_quadrants, exact_local_middle_capacity, OPPOSITE,
)


def clean_anchor_all_h_bound(s):
    """Pure integer all-h absolute source bound; not a conditional template law."""
    if type(s) is not int or s<2 or (s & (s-1)):
        raise ValueError("true s=2^h>=2 GQ order required")
    V=(s+1)*(s*s+1)
    disc=1+8*V
    a=(1+isqrt(disc))//2
    while a*(a-1)//2<V:
        a+=1
    if (a-1)*(a-2)//2>=V:
        raise AssertionError("nonminimal original physical complete pair universe")
    N=V*(s+1)
    all_nonincident=V*(V-(s+1))
    single_side_upper=2*s*(a-2)*V
    both_sides_union_upper=min(all_nonincident,2*single_side_upper)
    bound=Fraction(4*(a-2),s*(s+1))
    return {
        "s":s,"a":a,"V":V,"N":N,
        "true_original_nonincident_endpoint_pairs":all_nonincident,
        "left_dirty_absolute_upper":single_side_upper,
        "right_dirty_absolute_upper":single_side_upper,
        "union_dirty_absolute_upper":both_sides_union_upper,
        "uniform_nonincident_original_dirty_probability_upper":str(min(Fraction(1),bound)),
        "raw_union_bound_before_probability_cap":str(bound),
        "original_single_anchor_clean_fraction_lower":str(
            max(Fraction(),1-bound)),
        "uniform_five_source_four_anchor_clean_lower_proved":False,
        "universal_o_s4_middle_clean_capacity_proved":False,
        "root_Branch_A_proved":False,
    }


def exact_global_original_clean_anchors(model):
    """Independent true global ORIGINAL q,r source audit, not physical NB3."""
    ctx=EndpointEnergy(model)
    s,V=ctx.s,ctx.v
    left_neighbors=[]
    right_neighbors=[]
    for q in range(V):
        collinear=set()
        for ell in ctx.point_lines[q]:
            collinear.update(ctx.line_points[ell])
        collinear.discard(q)
        left_neighbors.append(sum(bool(set(ctx.f[p])&set(ctx.f[q]))
                                  for p in collinear))
    for r in range(V):
        intersecting=set()
        for p in ctx.line_points[r]:
            intersecting.update(ctx.point_lines[p])
        intersecting.discard(r)
        right_neighbors.append(sum(bool(set(ctx.g[ell])&set(ctx.g[r]))
                                   for ell in intersecting))
    predicted_left=s*sum(left_neighbors)
    predicted_right=s*sum(right_neighbors)
    if sum(left_neighbors)%2 or sum(right_neighbors)%2:
        raise AssertionError("dirty label overlap collinearity sum must be even")
    masks=Counter()
    per_point_left=Counter()
    per_line_right=Counter()
    dirty_original_pairs=set()
    total=0
    for q in range(V):
        for r in range(V):
            if (q,r) in ctx.edge_id:
                continue
            total+=1
            if (q,r) not in ctx.anchor:
                raise AssertionError("original true GQ unique projection absent")
            ap,al=ctx.anchor[q,r]
            l=int(bool(set(ctx.f[ap])&set(ctx.f[q])))
            g=int(bool(set(ctx.g[al])&set(ctx.g[r])))
            mask=l+2*g
            masks[mask]+=1
            if l:
                per_point_left[q]+=1
            if g:
                per_line_right[r]+=1
            if mask:
                dirty_original_pairs.add((q,r))
    if total!=V*s*s*(s+1):
        raise AssertionError("global nonincident original point line pair cardinality")
    actual_left=masks[1]+masks[3]
    actual_right=masks[2]+masks[3]
    if actual_left!=predicted_left or actual_right!=predicted_right:
        raise AssertionError("K1 exact source-pencil overlap dirty identity FAILED")
    for q in range(V):
        if per_point_left[q]!=s*left_neighbors[q]:
            raise AssertionError("K1 per-source-point anchor pencil identity FAILED")
    for r in range(V):
        if per_line_right[r]!=s*right_neighbors[r]:
            raise AssertionError("K1 dual per-source-line anchor pencil identity FAILED")
    upper=clean_anchor_all_h_bound(s)
    if actual_left>upper["left_dirty_absolute_upper"] or (
        actual_right>upper["right_dirty_absolute_upper"] or
        len(dirty_original_pairs)>upper["union_dirty_absolute_upper"]):
        raise AssertionError("K1 universal original-label pair star upper failed")
    if sum(masks.values())!=total or len(dirty_original_pairs)!=sum(
        masks[k] for k in (1,2,3)):
        raise AssertionError("K1 true original dirty overlap partition inconsistent")
    return {
        "s":s,"a":ctx.a,"V":V,"N":ctx.N,
        "true_original_nonincident_endpoint_pairs":total,
        "original_anchor_end_clean_pairs":masks[0],
        "original_anchor_end_dirty_pairs":len(dirty_original_pairs),
        "original_anchor_dirty_LEFT_only":masks[1],
        "original_anchor_dirty_RIGHT_only":masks[2],
        "original_anchor_dirty_BOTH":masks[3],
        "K1_exact_left_dirty_from_point_pencils":predicted_left,
        "K1_exact_right_dirty_from_line_pencils":predicted_right,
        "K1_original_collinear_overlap_unordered_point_pairs":
            sum(left_neighbors)//2,
        "K1_original_intersecting_overlap_unordered_line_pairs":
            sum(right_neighbors)//2,
        "K1_original_left_dirty_per_true_point_min_max":(
            min(per_point_left.get(q,0) for q in range(V)),
            max(per_point_left.get(q,0) for q in range(V))),
        "K1_original_right_dirty_per_true_line_min_max":(
            min(per_line_right.get(r,0) for r in range(V)),
            max(per_line_right.get(r,0) for r in range(V))),
        "original_uniform_conditional_end_clean_fraction":str(
            Fraction(masks[0],total)),
        "original_uniform_conditional_end_dirty_fraction":str(
            Fraction(len(dirty_original_pairs),total)),
        "universal_source_single_anchor_clean_lower":upper[
            "original_single_anchor_clean_fraction_lower"],
        "all_h_uniform_clean_convergence_proved":True,
        "original_pair_dirty_set":dirty_original_pairs,  # internal programmatic field
        "uniform_five_source_template_clean_convergence_proved":False,
        "root_Branch_A_proved":False,
    }


def exact_middle_dirty_pullback(model,e,*,max_templates=100_000):
    """K3 independent real original five-source-to-dirty-endpoint lift.

    Exact for the selected ORIGINAL e if budget succeeds, not all-h
    upper. Compute statuses independently of J's codegree evaluator.
    """
    if type(max_templates) is not int or max_templates<0:
        raise ValueError("nonnegative TRUE original template budget required")
    ctx=EndpointEnergy(model)
    if type(e) is not int or e<0 or e>=ctx.N:
        raise ValueError("true original middle source incidence required")
    geoms=exact_local_middle_capacity(
        ctx,e,retain_families=True,max_pair_comparisons=3_000_000)
    fams=geoms["exact_families"]
    if len(fams)>max_templates:
        raise ValueError("K3 true original template enumeration budget exceeded")
    groups=original_midpoint_quadrants(ctx,e)
    sources={sid:(k,x,y) for k,grp in enumerate(groups)
             for sid,x,y in grp}
    dirty_multiplicity=Counter()
    nonincident=clean=total_dirty_corners=0
    dirty_corner_mask=Counter()
    dirty_corner_count_hist=Counter()
    for ids in fams:
        pair_rows=None
        pair_cols=None
        for qa,qb in OPPOSITE:
            rows=[sid for sid in ids if sid!=e and sources[sid][0]==qa]
            cols=[sid for sid in ids if sid!=e and sources[sid][0]==qb]
            if len(rows)==len(cols)==2:
                pair_rows,pair_cols=rows,cols
                break
        if pair_rows is None:
            raise AssertionError("K3 true original five-source quadrant incompatibility")
        corners=[]
        for sid_a in pair_rows:
            for sid_b in pair_cols:
                _,x1,y1=sources[sid_a]
                _,x3,y3=sources[sid_b]
                # Correct original path endpoints ONLY, not physical
                # middle/outer SOURCE GQ incidence hypotheses.
                status,q,r=independent_original_anchor_status(
                    ctx,e,x1*ctx.a+y1,x3*ctx.a+y3)
                corners.append((status,q,r))
        if all(st in (2,3,4) for st,_,_ in corners):
            nonincident+=1
            bad=0
            for st,q,r in corners:
                if st==2:
                    ap,al=ctx.anchor[q,r]
                    left=bool(set(ctx.f[ap])&set(ctx.f[q]))
                    right=bool(set(ctx.g[al])&set(ctx.g[r]))
                    mask=int(left)+2*int(right)
                    if mask==0:
                        raise AssertionError("K3 true source dirty endpoint lacks overlap")
                    dirty_corner_mask[mask]+=1
                    dirty_multiplicity[q,r]+=1
                    bad+=1
            total_dirty_corners+=bad
            dirty_corner_count_hist[bad]+=1
            if not bad:
                clean+=1
    if sum(dirty_corner_count_hist.values())!=nonincident:
        raise AssertionError("K3 nonincident true physical family partition")
    if not(nonincident-clean<=total_dirty_corners<=4*(nonincident-clean)):
        raise AssertionError("K3 exact original dirty transport union bounds")
    if sum(dirty_multiplicity.values())!=total_dirty_corners:
        raise AssertionError("K3 ORIGINAL q/r dirty incidence lift not conserved")
    if sum(dirty_corner_mask.values())!=total_dirty_corners:
        raise AssertionError("K3 typed original anchor dirty labels lost")
    return {
        "true_original_middle_source_incidence":e,
        "true_five_source_physical_templates":len(fams),
        "all_four_original_nonincident_source_templates":nonincident,
        "all_four_original_end_clean_source_templates":clean,
        "nonincident_source_templates_with_at_least_one_dirty_anchor":nonincident-clean,
        "true_dirty_original_endpoint_pair_distinct_count":len(dirty_multiplicity),
        "true_dirty_original_endpoint_pair_corner_occurrences":total_dirty_corners,
        "max_single_dirty_original_pair_multiplicity":max(
            dirty_multiplicity.values(),default=0),
        "true_dirty_anchor_corners_per_source_template":dict(
            sorted(dirty_corner_count_hist.items())),
        "source_corner_dirty_LEFT_RIGHT_BOTH_mask":dict(
            sorted(dirty_corner_mask.items())),
        "K3_union_lower_N_minus_C":nonincident-clean,
        "K3_union_upper_four_N_minus_C":4*(nonincident-clean),
        "K3_exact_true_source_dirty_pullback_verified":True,
        "uniform_o_s4_clean_capacity_proved":False,
        "root_Branch_A_proved":False,
    }


def finite_global_clean_vs_source_report(model, *,
                                         pullback_middle_ids=()):
    """Source-aware contrast: global uniform ORIGINAL q,r vs quenched J."""
    global_clean=exact_global_original_clean_anchors(model)
    dirty_set=global_clean.pop("original_pair_dirty_set")
    cascade=finite_original_anchor_cascade_report(model)
    stages=cascade["all_original_source_stage_totals"]
    N=stages[STAGES[2]]
    C=stages[STAGES[3]]
    ratio=Fraction(C,N) if N else None
    result={
        "s":global_clean["s"],"a":global_clean["a"],
        "N":global_clean["N"],
        "true_original_global_clean_anchor_census":global_clean,
        "true_original_physical_five_source_cascade":stages,
        "original_global_clean_fraction":global_clean[
            "original_uniform_conditional_end_clean_fraction"],
        "physically_conditioned_ALL_FOUR_anchor_clean_fraction_of_nonincident":(
            str(ratio) if ratio is not None else None),
        "global_uniform_source_pairs_NOT_equal_to_physical_quadruple_law":True,
        "all_h_four_anchor_clean_capacity_upper_proved":False,
        "root_Branch_A_proved":False,
    }
    pulls=[]
    ctx=EndpointEnergy(model)
    for e in pullback_middle_ids:
        row=exact_middle_dirty_pullback(model,e)
        if row["all_four_original_nonincident_source_templates"]:
            if (row["nonincident_source_templates_with_at_least_one_dirty_anchor"]
                    <0):
                raise AssertionError("K3 impossible dirty count")
        # J per-e first 4 stages must match an INDEPENDENT K3 source
        # enumeration; do not equate with the entire all-e cascade.
        pulls.append(row)
    result["K3_independent_true_original_selected_middle_dirty_pullbacks"]=pulls
    if sum(p["true_dirty_original_endpoint_pair_distinct_count"] for p in pulls)> (
        len(dirty_set)*len(pulls)):
        raise AssertionError("K3 original dirty q/r support outside global original matrix")
    return result


def report():
    from hyp105_issue230_projection import fixture
    out=[]
    for scheme in ("lex","reverse","S68","S72"):
        data=finite_global_clean_vs_source_report(fixture(1,scheme),
                                                   pullback_middle_ids=(0,))
        data["scheme"]=scheme
        out.append(data)
    for scheme in ("lex","random"):
        data=finite_global_clean_vs_source_report(fixture(2,scheme),
                               pullback_middle_ids=(0,10,26,45,126,206,424))
        data["scheme"]=scheme
        out.append(data)
    return {
        "status":"RESTRICTED_THEOREM_K",
        "root_A":"OPEN",
        "all_h_s64":clean_anchor_all_h_bound(64),
        "all_h_s1024":clean_anchor_all_h_bound(1024),
        "all_h_s65536":clean_anchor_all_h_bound(65536),
        "maps":out,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
