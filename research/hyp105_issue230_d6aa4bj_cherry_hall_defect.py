"""AA4-BJ: exact TRUE-ORIGINAL source-CHERRY-FIRST 4flag Hall residual.

For EVERY already fixed complete globally injected W(3,s) f,g:
a pair of ACTUAL source flags with one repeated source point (dual: line)
has exactly TWO possible 2regular first-side residual fourflag shapes:
  (B) a simple occupied physical C4, each of 4 distinct source factors
      chooses one of d genuine incidence flags -> d^4,
  (C) two disjoint occupied physical edges each doubled, their two
      distinct original factors choose two original flags each
      -> binom(d,2)^2.

Missing physical pair edges delete at most (a-4)(a-5) C4 and
binom(a-4,2) disjoint-edge pairs per missing edge in the complement of
the anchored pair coordinates. A FULL original 2-sided continuation
must reuse the SAME other four ORIGINAL incidence IDs on the opposite
physical side. The root Hall-failure can be huge.

All-h bounds are UNILATERAL; do not promote to fixed-all-map
accepted seven-GF5 Omega(s^6) or issue #230 Branch A/B/C.
Prior #527 analyzed the physically B/C4 source cohort and a
different opposite-side anchored original Hall UPPER. We extend
to the entire source-cherry FIRST-side reservoir, including
source-C/double-matching, and quantify exact same-Q Hall failure.
"""
from collections import Counter
from itertools import combinations,product
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params


def _full_four_patterns(remaining_vertices, occupied):
    """Physical root-saturated complement: two shapes, no fake GQ."""
    F=set(occupied)
    n4=nmatch=0
    patterns=[]
    for verts in combinations(remaining_vertices,4):
        a,b,c,d=verts
        all_edges={tuple(sorted(edge)) for edge in combinations(verts,2)}
        matchings=(
            ((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c)))
        for raw in matchings:
            matching=tuple(sorted(tuple(sorted(e)) for e in raw))
            cycle=tuple(sorted(all_edges-set(matching)))
            if all(e in F for e in cycle):
                n4+=1
                patterns.append(("C4",cycle))
            if all(e in F for e in matching):
                nmatch+=1
                patterns.append(("DOUBLE_MATCH",matching))
    return n4,nmatch,tuple(patterns)


def cherry_unilateral_all_h_lower(s):
    """Explicit all-h worst-hole bound for EACH genuine original cherry."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine original symplectic dyadic s=2^h>=2 required")
    V,a,K,m=_params(s)
    d=s+1
    n=a-2
    full=3*comb(n,4)
    c4=max(0,full-m*(n-2)*(n-3))
    matching=max(0,full-m*comb(n-2,2))
    lower=d**4*c4+comb(d,2)**2*matching
    if lower<=0:
        raise AssertionError("uniform genuine-original physical cherry residual lower must be positive")
    if 32*lower<s**10:
        raise AssertionError("ALL dyadic original cherry anchors require >=s**10/32 true unilateral sixflags")
    if s==2 and lower!=270:
        raise AssertionError("W32 exact source-cherry anchored unilateral mass must be 270")
    if s>=4 and (c4<=0 or matching<=0):
        raise AssertionError("dyadic s>=4 both physical B/C survivor families required")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,"d":d,
        "K_a_minus_original_root_two_coordinates":n,
        "complete_physical_C4_count_on_complement":full,
        "occupied_physical_C4_per_root_lower":c4,
        "occupied_disjoint_physical_two_edge_matching_per_root_lower":matching,
        "all_h_each_actual_original_cherry_unilateral_fourflag_lower":lower,
        "all_h_uniform_explicit_each_cherry_s10_over32":s**10//32,
        "total_number_actual_original_point_and_LINE_cherry_anchors":
            2*V*comb(d,2),
        "both_types_unilateral_candidate_incidence_lower":
            2*V*comb(d,2)*lower,
        "every_f_g_joint_same_Q_extension_lower_NOT_PROVED":True,
        "all_7_GF5_root_A_B_C_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _other_sixcoordinate_mask(ids,inc,labels,other):
    from collections import Counter
    degree=Counter()
    for j in ids:
        u,v=labels[inc[j][other]]
        degree[u]+=1
        degree[v]+=1
    if len(degree)!=6 or any(val!=2 for val in degree.values()):
        return None
    return tuple(sorted(degree))


def actual_original_cherry_anchor(model,side,source_factor,selected_flags,
                                  *,vertex_foursets=None,collect_first=3):
    """Enumerate ACTUAL anchored original source and physical completions.

    side=0 repeats an original POINT and screens original LINE physical g.
    side=1 repeats an original LINE and screens original POINT physical f.
    Full palette -> full unilateral reservoir. Optional specific distinct
    physical four-coordinate sets in root complement test localized
    finite W34 WITHOUT falsely claiming whole-root census.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed original cherry side 0=point or 1=LINE")
    if type(source_factor) is not int or not 0<=source_factor<V:
        raise ValueError("actual source factor ID in true W3 required")
    actual_by=(byP,byL)[side]
    selected_flags=tuple(selected_flags)
    if len(selected_flags)!=2 or len(set(selected_flags))!=2 or any(
        type(j) is not int or j not in actual_by[source_factor]
        for j in selected_flags
    ):
        raise ValueError("two different ACTUAL source incidence flag IDs through SAME source factor")
    images=(f,g)[side]
    other_images=(g,f)[side]
    anchored_edge=images[source_factor]
    allowed=tuple(v for v in range(a) if v not in anchored_edge)
    if vertex_foursets is None:
        vertices_scope=tuple(combinations(allowed,4))
        complete=True
    else:
        vertices_scope=tuple(tuple(sorted(t)) for t in vertex_foursets)
        if len(set(vertices_scope))!=len(vertices_scope) or any(
            len(t)!=4 or len(set(t))!=4 or
            any(type(v) is not int or v not in allowed for v in t)
            for t in vertices_scope
        ):
            raise ValueError("valid distinct root-disjoint physical 4coordinate subsets required")
        complete=(set(vertices_scope)==set(combinations(allowed,4)))
    inverse={e:i for i,e in enumerate(images)}
    n4=nmatch=0
    unilateral=both=0
    type_counts=Counter()
    examples=[]
    seen=set()
    for verts in vertices_scope:
        c,m,patterns=_full_four_patterns(verts,set(inverse))
        n4+=c
        nmatch+=m
        for kind,pairs in patterns:
            if kind=="C4":
                source_ids=tuple(inverse[e] for e in pairs)
                choices=tuple(tuple((j,) for j in actual_by[p]) for p in source_ids)
                expected=(s+1)**4
            else:
                source_ids=tuple(inverse[e] for e in pairs)
                choices=tuple(tuple(combinations(actual_by[p],2)) for p in source_ids)
                expected=comb(s+1,2)**2
            if len(set(source_ids))!=len(source_ids) or source_factor in source_ids:
                raise AssertionError("fully injected root-complement physical factor IDs must be distinct")
            for grouping in product(*choices):
                flags=tuple(sorted(selected_flags+tuple(x for t in grouping for x in t)))
                if len(flags)!=6 or len(set(flags))!=6:
                    raise AssertionError("six actual genuine original incidence flag IDs required")
                if flags in seen:
                    raise AssertionError("same actual original sixflag Q enumerated twice from one root")
                seen.add(flags)
                unilateral+=1
                if _other_sixcoordinate_mask(flags,inc,other_images,1-side) is not None:
                    both+=1
                    type_counts[kind]+=1
                    if len(examples)<collect_first:examples.append(flags)
            # Avoid abstract source flag multiplicity confusion; this
            # is EXACT original incidence valency, verified upstream.
    expected_unilateral=n4*(s+1)**4+nmatch*comb(s+1,2)**2
    if unilateral!=expected_unilateral:
        raise AssertionError("exact original point/LINE true-source unilateral C4+2C2 count wrong")
    if complete:
        cert=cherry_unilateral_all_h_lower(s)
        if unilateral<cert["all_h_each_actual_original_cherry_unilateral_fourflag_lower"]:
            raise AssertionError("uniform all-h physical missing-edge deletion certificate violated")
    return {
        "s":s,"V":V,"a":a,"side":"POINT" if side==0 else "LINE",
        "original_source_anchor_factor_id":source_factor,
        "two_real_original_flag_IDs":selected_flags,
        "source_original_anchor_physical_pair_edge":anchored_edge,
        "physical_fourcoordinate_subsets_checked":len(vertices_scope),
        "all_complement_foursets_covered":complete,
        "source_original_occupied_C4_residuals":n4,
        "source_original_occupied_double_matching_residuals":nmatch,
        "exact_one_side_original_sixflag_extensions":unilateral,
        "exact_both_sides_same_original_sixflag_accepted_nonAA":both,
        "exact_one_side_to_opposite_side_Hall_failures":unilateral-both,
        "joint_original_source_type_by_anchored_physical_shape":dict(type_counts),
        "example_actual_original_sixflag_Q":tuple(examples),
        "all_seven_GF5_original_sixflag_ROOT_A_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def actual_original_W32_complete_cherry_defect(model):
    """Independent entire W32 CHERRY-FIRST original M1 and Hall defect.

    45 POINT + 45 LINE source anchors, each 270 unilateral ORIGINAL
    complete sixflag Q. Every joined Q contributes exactly its count
    of repeated true original point/LINE factor cherry pairs.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("full original all-anchor source Hall census is W32 ONLY")
    anchors=[]
    by_side=Counter()
    shape_good=Counter()
    fail=Counter()
    for side,by in ((0,byP),(1,byL)):
        for p in range(V):
            for flags in combinations(by[p],2):
                z=actual_original_cherry_anchor(model,side,p,flags)
                anchors.append(z)
                if z["exact_one_side_original_sixflag_extensions"]!=270:
                    raise AssertionError("W32 complete K6 every source cherry must have 270 unilateral choices")
                by_side[z["side"]]+=z["exact_both_sides_same_original_sixflag_accepted_nonAA"]
                fail[z["side"]]+=z["exact_one_side_to_opposite_side_Hall_failures"]
                for k,v in z["joint_original_source_type_by_anchored_physical_shape"].items():
                    shape_good[k]+=v
    joined=sum(by_side.values())
    return {
        "s":s,"true_original_cherry_anchor_count":len(anchors),
        "one_sided_original_sixflag_reservoir_total":
            sum(z["exact_one_side_original_sixflag_extensions"] for z in anchors),
        "two_sided_original_sevenGF5_nonAA_first_cherry_moment":joined,
        "original_two_sided_joint_by_root_type":dict(by_side),
        "original_cherry_Hall_failures_total":sum(fail.values()),
        "original_cherry_Hall_failures_by_side":dict(fail),
        "root_anchored_success_histogram":
            dict(Counter(z["exact_both_sides_same_original_sixflag_accepted_nonAA"] for z in anchors)),
        "fully_nonextendible_actual_original_cherries":
            sum(z["exact_both_sides_same_original_sixflag_accepted_nonAA"]==0 for z in anchors),
        "physical_residual_joint_shape_occurrences":dict(shape_good),
        "one_sided_positive_NOT_enough_for_joint_root_s6":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
