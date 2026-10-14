"""EICE-003-I: TRUE original middle-incidence four-quadrant arm geometry.

I1: all-h iff for a coherent five-source 2x2 physical NB3 template:
four arms have a unique middle-corner contact, arranged 2+2 in one of
two opposite pairs, with four DISTINCT outer left and right coordinates.
I2: exact bipartite pair-match candidate capacity; every true allblocked
source family is one of these templates, with its ORIGINAL identities.
I3: at most TWO oriented physical 2x2 squares for one fixed middle
source e and unordered 5-source set; at most TEN across all 5 possible
middle sources. Better than the previous all-h coarse 20.
I4: exact per-middle heavy-source necessary counting from F5/F6.

This does NOT establish o(s^4) per-middle allblocked sources, an all-h
seven-GF5 transfer, or Branch A/B.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_five_source_blocked_search import (
    FiveSourceSearch, exact_five_source_coherence
)
from hyp105_issue230_four_anchor_capacity import (
    FourAnchorCapacity, all_h_blocked_plaquette_reservoir
)
from hyp105_issue230_spectral_source_fibres import (
    exact_middle_double_star_fibre
)
from hyp105_issue230_source_plaquettes import status_of_cell

OPPOSITE=((0,3),(1,2))  # four cells (x0,y0), (x0,y1), (x1,y0), (x1,y1)


def original_midpoint_quadrants(ctx,e):
    """Partition ORIGINAL four-arm source pool by UNIQUE physical corner.

    Each external original e'=(p,l) has p!=p2, l!=l2. Its actual f(p)
    shares exactly ONE x with f(p2), actual g(l) exactly ONE y with
    g(l2). Therefore it touches exactly one middle physical vertex
    in the combined two-diagonal physical representation of its source.
    """
    base=exact_middle_double_star_fibre(ctx,e)
    p2,l2=ctx.inc[e]
    fx=ctx.f[p2]
    gy=ctx.g[l2]
    groups=[[] for _ in range(4)]
    for i in base["eligible_four_arm_matching_pool_original_incidence_ids"]:
        p,l=ctx.inc[i]
        xx=set(ctx.f[p]) & set(fx)
        yy=set(ctx.g[l]) & set(gy)
        if len(xx)!=1 or len(yy)!=1:
            raise AssertionError("external ORIGINAL source has nonunique middle corner")
        x,y=next(iter(xx)),next(iter(yy))
        ix=0 if x==fx[0] else 1
        iy=0 if y==gy[0] else 1
        # Store actual OUTSIDE physical partner coordinates (not source ids).
        px=next(z for z in ctx.f[p] if z!=x)
        py=next(z for z in ctx.g[l] if z!=y)
        if px in fx or py in gy:
            raise AssertionError("external source reused central physical coordinate")
        groups[2*ix+iy].append((i,px,py))
    if (sum(map(len,groups))!=
            base["eligible_four_arm_matching_pool_size"]):
        raise AssertionError("original four-corner source partition lost an incidence")
    return tuple(tuple(sorted(q)) for q in groups)


def valid_original_two_arm_pairs(quadrant):
    """Two true original arm incidences with distinct external x AND y."""
    records=[]
    for a,b in combinations(quadrant,2):
        # Same ORIGINAL p or same ORIGINAL line produces repeated outer
        # physical partner x/y at the common physical central corner.
        if a[1]==b[1] or a[2]==b[2]:
            continue
        records.append(((a[0],b[0]),frozenset((a[1],b[1])),
                        frozenset((a[2],b[2]))))
    return records


def exact_local_middle_capacity(ctx,e, *,
                                exact_cross=True,
                                max_pair_comparisons=3_000_000,
                                retain_families=False):
    """Source-local exact capacity of all geometrically possible 5-ID 2x2.

    This counts coherent physical 2x2 source TEMPLATE families, WITHOUT
    requiring original q/r endpoints be nonincident, clean or blocked.
    The pair-product count is the rigorous pre-cross upper; exact_cross
    eliminates overlap of four external left/right coordinates.
    """
    if type(max_pair_comparisons) is not int or max_pair_comparisons<0:
        raise ValueError("nonnegative exact cross matching budget required")
    groups=original_midpoint_quadrants(ctx,e)
    pairs=[valid_original_two_arm_pairs(g) for g in groups]
    pre=sum(len(pairs[i])*len(pairs[j]) for i,j in OPPOSITE)
    exact=0
    inspected=0
    families=[] if retain_families else None
    for i,j in OPPOSITE:
        for src_a,x_a,y_a in pairs[i]:
            for src_b,x_b,y_b in pairs[j]:
                inspected+=1
                if inspected>max_pair_comparisons:
                    raise ValueError("exact source four-quadrant compatibility budget exceeded")
                if not x_a.isdisjoint(x_b) or not y_a.isdisjoint(y_b):
                    continue
                exact+=1
                if retain_families:
                    ids=tuple(sorted((e,)+src_a+src_b))
                    if len(set(ids))!=5:
                        raise AssertionError("I1 true original five-source IDs not distinct")
                    families.append(ids)
    if not exact_cross:
        # No silent lower-bound claim if this option is disabled:
        # simply return pair-product upper and no accepted exact count.
        exact=None
        families=None
    elif inspected!=pre:
        raise AssertionError("exact original source pair-product census lost cases")
    if families is not None and len(families)!=len(set(families)):
        raise AssertionError("I1 duplicate true source five-incidence family for one middle")
    return {
        "middle_original_source_id":e,
        "true_corner_arm_source_counts":tuple(map(len,groups)),
        "true_corner_matching_pair_counts":tuple(map(len,pairs)),
        "pair_product_pre_cross_upper":pre,
        "unique_x_y_coordinate_disjoint_five_source_templates":exact,
        "strict_cross_coordinate_comparisons":inspected,
        "I1_true_middle_source_2x2_template_equivalence":True,
        "I2_coordinate_cross_compatibility_enforced":exact_cross,
        "exact_families":tuple(families) if families is not None else None,
        "actual_internal_blocking_or_GF5_positivity_inferred":False,
    }


def true_five_source_middle_template(ctx,e,ids):
    """Independent O(5) exact membership in opposite-corner template class."""
    source=tuple(sorted(ids))
    if len(source)!=5 or len(set(source))!=5 or e not in source:
        return False
    p2,l2=ctx.inc[e]
    fx,gy=ctx.f[p2],ctx.g[l2]
    buckets=defaultdict(list)
    for sid in source:
        if sid==e:
            continue
        p,l=ctx.inc[sid]
        if p==p2 or l==l2:
            return False
        ix=set(ctx.f[p]) & set(fx)
        iy=set(ctx.g[l]) & set(gy)
        if len(ix)!=1 or len(iy)!=1:
            return False
        x,y=next(iter(ix)),next(iter(iy))
        corner=(0 if x==fx[0] else 1)*2+(0 if y==gy[0] else 1)
        partner_x=next(t for t in ctx.f[p] if t!=x)
        partner_y=next(t for t in ctx.g[l] if t!=y)
        if partner_x in fx or partner_y in gy:
            return False
        buckets[corner].append((sid,partner_x,partner_y))
    if not any(len(buckets[i])==len(buckets[j])==2 and
               sum(len(z) for z in buckets.values())==4
               for i,j in OPPOSITE):
        return False
    return (len({r[1] for bucket in buckets.values() for r in bucket})==4
            and len({r[2] for bucket in buckets.values() for r in bucket})==4)


def conditional_improved_source_packing(s,theta):
    """I3/I4 all-h source bound with exact 2 orientations per fixed middle."""
    q=all_h_blocked_plaquette_reservoir(s,theta)
    P=Fraction(q["explicit_oriented_allblocked_true_GQ_plaquette_count_lower"])
    N=(s+1)**2*(s*s+1)
    return {
        "s":s,"theta":str(Fraction(theta)),
        "max_oriented_plaquettes_per_fixed_middle_and_five_source_family":2,
        "max_oriented_plaquettes_per_five_source_family_all_middles":10,
        "distinct_true_original_five_source_families_lower":str(P/10),
        "at_least_one_middle_original_source_families_lower":str(P/(2*N)),
        "valid_only_on_same_EICE002_stationary_Gstar_and_source_global_maps":True,
        "o_s4_capacity_or_GF5_transfer_proved":False,
        "root_Branch_A_proved":False,
    }


def finite_quadrant_report(model, *, max_path_cells=3_000_000,
                           exhaustive_all_middle=True,
                           compare_sample=8,
                           exact_pair_budget=3_000_000):
    ctx=EndpointEnergy(model)
    full=FiveSourceSearch(model).census(
        export_true_five_source_families=True,
        max_physical_nb3_cells=max_path_cells)
    source=full.pop("TRUE_ORIGINAL_five_source_families")
    # Exhaustive means ALL true original e. A partial result must be
    # explicitly labeled (never an all-source capacity claim).
    middles=list(range(ctx.N)) if exhaustive_all_middle else sorted({
        e for f in source for e in f["original_middle_source_ids"]})
    local_cache={}
    total_pre=total_exact=0
    upper_max=exact_max=0
    top=[]
    for e in middles:
        r=exact_local_middle_capacity(
            ctx,e,max_pair_comparisons=exact_pair_budget)
        local_cache[e]=r
        total_pre+=r["pair_product_pre_cross_upper"]
        total_exact+=r["unique_x_y_coordinate_disjoint_five_source_templates"]
        upper_max=max(upper_max,r["pair_product_pre_cross_upper"])
        exact_max=max(exact_max,r["unique_x_y_coordinate_disjoint_five_source_templates"])
        top.append((e,r["unique_x_y_coordinate_disjoint_five_source_templates"]))
    observed_counts=Counter()
    for f in source:
        ids=tuple(f["original_incidence_ids"])
        for e in f["original_middle_source_ids"]:
            if e not in local_cache:
                raise AssertionError("real source middle excluded from capacity audit")
            if not true_five_source_middle_template(ctx,e,ids):
                raise AssertionError("ACTUAL original blocked 5-source family not 4-quadrant compatible")
            observed_counts[e]+=1
    for e,count in observed_counts.items():
        if count>local_cache[e]["unique_x_y_coordinate_disjoint_five_source_templates"]:
            raise AssertionError("actual blocked 5-source family exceeds full physical template capacity")
    # Strong independent oracle: enumerated source-family candidates really
    # have a coherent 5-ID BOTH-diagonal graph and a proper 2x2 square.
    checked=0
    for e,_ in sorted(top,key=lambda a:(-a[1],a[0])):
        if checked>=compare_sample:
            break
        r=exact_local_middle_capacity(ctx,e,
            max_pair_comparisons=exact_pair_budget,retain_families=True)
        if not r["exact_families"]:
            continue
        ids=r["exact_families"][0]
        coherent=exact_five_source_coherence(model,ids,ctx=ctx)
        if coherent is None:
            raise AssertionError("I1 source quadrant template failed paired coherence")
        oracle,_,_=coherent
        sq=oracle.census(max_plaquettes=50,max_paths=2000,
                         independent_paths=True,independent_plaquettes=True)
        if sq["total_2x2_plaquettes"]<1:
            raise AssertionError("I1 source template failed true physical 2x2 existence")
        checked+=1
    return {
        "status":"RESTRICTED_THEOREM_I",
        "s":ctx.s,"a":ctx.a,"N":ctx.N,
        "all_true_middle_source_incidences_audited":len(middles),
        "full_true_middle_census":exhaustive_all_middle,
        "true_blocked_five_source_families":len(source),
        "true_original_middle_sources_with_blocked_families":len(observed_counts),
        "true_blocked_family_middle_observation_count":sum(observed_counts.values()),
        "all_middle_source_pair_product_template_upper_sum":total_pre,
        "all_middle_source_exact_geometric_template_count_sum":total_exact,
        "largest_single_middle_pair_product_upper":upper_max,
        "largest_single_middle_exact_template_capacity":exact_max,
        "largest_observed_true_blocked_family_count_per_middle":max(observed_counts.values(),default=0),
        "top_five_exact_capacity_middle_original_ids":sorted(top,key=lambda a:(-a[1],a[0]))[:5],
        "independent_both_diagonals_proper_square_template_validations":checked,
        "I3_sharpened_five_source_orientation_ceiling":10,
        "actual_GF5_positive_sixset_capacity_proved":False,
        "uniform_o_s4_true_blocking_capacity_proved":False,
        "root_Branch_A_proved":False,
    }


def report():
    from hyp105_issue230_projection import fixture
    r=[]
    for scheme in ("lex","reverse","S68","S72"):
        d=finite_quadrant_report(fixture(1,scheme),compare_sample=2)
        d["scheme"]=scheme
        r.append(d)
    for scheme in ("lex","random"):
        d=finite_quadrant_report(fixture(2,scheme),compare_sample=5)
        d["scheme"]=scheme
        r.append(d)
    return {"status":"RESTRICTED_THEOREM_I","root_A":"OPEN","maps":r}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
