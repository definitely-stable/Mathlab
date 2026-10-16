"""HYP-105 #230 AA4-AN — exact genuine-original D-FIRST degree-two residual 4-flag transfer.

Independent of the AA4-AM #530 Q-FIRST selected seven-GF5 sixset census.
For ANY actual ORIGINAL W(3,2^h), complete globally injected typed
physical K_a-edge source factor labels f,g and two DISTINCT original
flags (p,l),(q,m) with p!=q,l!=m and adjacent f(p),f(q) AND adjacent
g(l),g(m), fix the point-side physical incident pairs xy,xz.

Every six-edge, SIX-coordinate, PHYSICALLY TWO-REGULAR multigraph
containing these TWO distinct anchored physical edges has exactly ONE
of THREE remaining-edge topologies (five residual vertices):
  1. connected C6: path y-a-b-c-z, (a-3)_3 choices;
  2. separate C3+C3: yz plus triangle a-b-c, C(a-3,3);
  3. C4 plus doubled 2-cycle: y-a-z, twice b-c,
        (a-3)*C(a-4,2).
All auxiliary coordinates outside x,y,z and distinct. Cases mutually
disjoint and exhaustive. NO source incidence or f/g independence used.

Let A1,A2,A3 be numbers of *occupied* physical shapes under the
SAME complete globally injected point factor labeling f (so each
physical edge has a unique actual ORIGINAL point source inverse).
The exact number of unilateral genuine ORIGINAL four-FLAG source
completions after the two fixed actual incidence flags is
  (A1+A2)*d^4 + A3*d^2*C(d,2),
where d=s+1 is the exact TRUE source GQ degree. For A1/A2 there
are four DISTINCT new ORIGINAL point source factors and d genuine
flags at each; for A3 there are two singleton and one twice-selected
true original source factor, d*d*C(d,2). This is EXACT for every
complete global f, even when its physical K_a image has holes.

The D-FIRST evaluator independently constructs actual source flags
from ONLY the physical 4-edge residual shapes and original source
incidence neighborhoods, then tests the opposite same global g
physical degree-two filter and seven historical selected GF5 tags.
The total number of D-to-selected-six incidence charges MUST agree
with Q-FIRST #530 but never accesses its selected sixset lists for
generation. Substantial evidence-only independent algorithm, not
a new uniform selected seven positive lower and not Branch A/B/C.
"""
from collections import Counter
from itertools import combinations,product
from math import comb

from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import original_D_pair_index
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,seven_census,R3_CERTIFIED_FLOORS,
)


def _edge(x,y):
    if x==y:raise ValueError("simple physical pair needs two distinct coordinates")
    return (x,y) if x<y else (y,x)


def rooted_adjacent_physical_twofactor_completions(edge0,edge1,a):
    """No source graph: EXACT one-to-one 3-topology anchored physical
    SIX-coordinate two-regular SIX-edge MULTIGRAPHS, with two fixed
    distinct adjacent edges and four residual edges, counted ONCE.
    """
    edge0=tuple(edge0);edge1=tuple(edge1)
    if (a<6 or edge0==edge1 or
            len(edge0)!=2 or len(edge1)!=2 or
            any(type(x) is not int or x<0 or x>=a for x in edge0+edge1) or
            len(set(edge0)&set(edge1))!=1):
        raise ValueError("two distinct adjacent physical pair edges in K_a a>=6")
    x=next(iter(set(edge0)&set(edge1)))
    y=next(i for i in edge0 if i!=x)
    z=next(i for i in edge1 if i!=x)
    remaining=tuple(t for t in range(a) if t not in (x,y,z))
    for alpha,beta,gamma in product(remaining,repeat=3):
        if len({alpha,beta,gamma})!=3:continue
        yield ("C6",tuple(sorted((
            _edge(y,alpha),_edge(alpha,beta),
            _edge(beta,gamma),_edge(gamma,z)))))
    for triple in combinations(remaining,3):
        alpha,beta,gamma=triple
        yield ("C3+C3",tuple(sorted((
            _edge(y,z),_edge(alpha,beta),
            _edge(alpha,gamma),_edge(beta,gamma)))))
    for alpha in remaining:
        rest=tuple(t for t in remaining if t!=alpha)
        for beta,gamma in combinations(rest,2):
            doubled=_edge(beta,gamma)
            yield ("C4+C2",tuple(sorted((
                _edge(y,alpha),_edge(z,alpha),doubled,doubled))))


def all_h_rooted_D_fourflag_shape_capacity(s):
    """Exact fully OCCUPIED physical palette capacity and TRUE source
    incidence unilateral source-flag extension upper, all s=2^h.
    Non-surjective global maps require occupied-shape census below.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine original W(3,2^h), h>=1")
    V=(s+1)*(s*s+1)
    a=2
    while comb(a,2)<V:a+=1
    d=s+1
    connected=(a-3)*(a-4)*(a-5)
    triangles=comb(a-3,3)
    root_repeat=(a-3)*comb(a-4,2)
    total=(connected+triangles)*d**4+root_repeat*d*d*comb(d,2)
    return {
        "s":s,"V":V,"d":d,"a":a,"K":comb(a,2),
        "physical_pair_image_holes":comb(a,2)-V,
        "complete_Ka_C6_shape_count":connected,
        "complete_Ka_two_C3_shape_count":triangles,
        "complete_Ka_C4_plus_doubled_C2_shape_count":root_repeat,
        "complete_Ka_total_rooted_physical_six_twofactor_shapes":
            connected+triangles+root_repeat,
        "full_Ka_exact_unilateral_four_REAL_original_flags":total,
        "arbitrary_GLOBAL_partial_physical_injection_unilateral_upper":
            total,
        "every_genuine_original_D_pair_positive_true_GF5_extension_NOT_PROVED":True,
        "single_original_source_GQ_incidence_host_required":True,
        "root_issue230_A_B_C_not_closed":True,
    }


def _strict_original_D_pair_model(model,anchor,side):
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("point-side=0, line-side=1")
    if (not isinstance(anchor,(tuple,list)) or len(anchor)!=2
            or any(type(i) is not int or i<0 or i>=len(inc) for i in anchor)
            or anchor[0]==anchor[1]):
        raise ValueError("two different actual original source incidence IDs")
    p,l=inc[anchor[0]];q,m=inc[anchor[1]]
    if (p==q or l==m or
            not(set(f[p])&set(f[q])) or
            not(set(g[l])&set(g[m]))):
        raise ValueError("must be genuine original D-compatible two-flag anchor")
    labels=(f,g)[side]
    factor_ids=(p,q) if side==0 else (l,m)
    anchored_labels=(labels[factor_ids[0]],labels[factor_ids[1]])
    bysource=np if side==0 else nl
    inverse={edge:i for i,edge in enumerate(labels)}
    return s,V,d,a,inc,f,g,bysource,inverse,anchored_labels


def physical_unilateral_D_source_completion_census(model,anchor,*,side=0,
                                                    enumerate_flags=False,
                                                    visitor=None):
    """All occupied rooted physical shapes, exact ORIGINAL 4-flag source
    multiplicities and optional independent flag quadruple traversal.

    'visitor' receives the actual sorted six original incidence IDs,
    one per true source pattern and choice. No precomputed selected-Q
    input is consulted. Constant extra memory when visitor is supplied.
    """
    s,V,d,a,inc,f,g,bysource,inverse,pins=_strict_original_D_pair_model(
        model,anchor,side)
    raw=Counter();occupied=Counter();source_completions=Counter()
    duplicates=0
    check_unilateral=Counter()
    for kind,edges in rooted_adjacent_physical_twofactor_completions(
            *pins,a):
        raw[kind]+=1
        if any(e not in inverse for e in edges):
            continue
        occupied[kind]+=1
        factors=[inverse[e] for e in edges]
        repeats=Counter(factors)
        if kind in ("C6","C3+C3"):
            if sorted(repeats.values())!=[1,1,1,1]:
                raise AssertionError("simple physical four-edge residual source factor quartet")
            w=d**4
        else:
            if sorted(repeats.values())!=[1,1,2]:
                raise AssertionError("C4+double source factor profile")
            w=d*d*comb(d,2)
        source_completions[kind]+=w
        if enumerate_flags:
            slots=[]
            for factor,mult in sorted(repeats.items()):
                slots.append(tuple(combinations(bysource[factor],mult)))
            counter=0
            for selections in product(*slots):
                add=tuple(i for selected in selections for i in selected)
                if len(add)!=4 or len(set(add))!=4:
                    raise AssertionError("real ORIGINAL four distinct extra flag IDs required")
                six=tuple(sorted(tuple(anchor)+add))
                if len(set(six))!=6:
                    raise AssertionError("six different original incidence IDs")
                if visitor is not None:
                    visitor(six,kind)
                counter+=1
            if counter!=w:
                raise AssertionError("physical 2-regular original rooted source multiplicity")
            check_unilateral[kind]+=counter
    totals=all_h_rooted_D_fourflag_shape_capacity(s)
    if dict(raw)!={
        "C6":totals["complete_Ka_C6_shape_count"],
        "C3+C3":totals["complete_Ka_two_C3_shape_count"],
        "C4+C2":totals["complete_Ka_C4_plus_doubled_C2_shape_count"],
    }:
        raise AssertionError("physical K_a rooted shape canonical classification")
    if (enumerate_flags and source_completions!=check_unilateral):
        raise AssertionError("exact source d^4 or d² C(d,2) count disagrees with original actual flags")
    total=sum(source_completions.values())
    if total>totals["full_Ka_exact_unilateral_four_REAL_original_flags"]:
        raise AssertionError("globally physical nononto image exceeded full-Ka factor count")
    return {
        "s":s,"a":a,"V":V,"d":d,"anchor_original_two_incidence_IDs":tuple(anchor),
        "original_source_side":"point" if side==0 else "line",
        "raw_complete_Ka_anchored_physical_2factor_by_shape":dict(raw),
        "actually_occupied_global_physical_2factor_by_shape":dict(occupied),
        "exact_one_side_REAL_original_four_flag_completions_by_shape":
            dict(source_completions),
        "exact_one_side_original_four_FLAG_completions_total":total,
        "all_h_complete_Ka_unilateral_upper":
            totals["full_Ka_exact_unilateral_four_REAL_original_flags"],
        "full_source_original_flag_enumerator_checked":bool(enumerate_flags),
        "selected_seven_GF5_success_from_unilateral_only_NOT_PROVED":True,
    }


def exact_original_W32_D_FIRST_selected_seven(model,*,full_independent=True):
    """Independent genuine ORIGINAL W32 selected-seven extension E oracle.

    Does NOT enumerate the accepted selected sixsets first or call
    seven_census for candidate generation. For each ACTUAL original
    D pair, enumerate physical point-side C6/C3+C3/C4+C2 4-edge
    patterns, inverse original factor labels, REAL original incidence
    flags, enforce opposite physical TWO-REGULARITY, then classify
    the same historical seven positive GF5 classes.

    Optional independent Q-FIRST witness compare only AFTER counts.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a,len(inc))!=(2,15,6,45):
        raise ValueError("strict genuine ORIGINAL W(3,2) full K6 only")
    D=original_D_pair_index(model)
    coverage=Counter()
    selected_by_tag=Counter()
    E_by_tag=Counter()
    accepted_sets=set()
    physical_dual_sets=set()
    bilateral_by_anchored_shape=Counter()
    one_side_total=0
    for anchor in sorted(D):
        hits=0
        def accept(six,shape):
            nonlocal hits
            leftcoords=Counter(c for j in six for c in f[inc[j][0]])
            rightcoords=Counter(c for j in six for c in g[inc[j][1]])
            if not(len(leftcoords)==6 and all(v==2 for v in leftcoords.values())):
                raise AssertionError("D-first emitted FALSE physical degree two point source Q")
            if len(rightcoords)!=6 or any(v!=2 for v in rightcoords.values()):
                return
            physical_dual_sets.add(six)
            bilateral_by_anchored_shape[shape]+=1
            tag=classify_seven_prechecked(six,f,g,inc)
            if tag is None:
                return
            E_by_tag[tag]+=1
            accepted_sets.add(six)
            hits+=1
        data=physical_unilateral_D_source_completion_census(
            model,anchor,side=0,enumerate_flags=True,visitor=accept)
        one_side_total+=data["exact_one_side_original_four_FLAG_completions_total"]
        coverage[anchor]=hits
    E=sum(coverage.values())
    covered=sum(n>0 for n in coverage.values())
    if E!=sum(E_by_tag.values()):
        raise AssertionError("true original D-first source seven signature energy")
    if full_independent:
        from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
            exact_W32_original_seven_pair_extension_certificate,
        )
        baseline=exact_W32_original_seven_pair_extension_certificate(
            model,independent_oracle=True)
        if (E!=baseline["E_original_extension_incidences"]
                or covered!=baseline["D_covered_by_at_least_one_selected_original_six_Q"]
                or len(D)-covered!=baseline["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"]
                or E_by_tag!=Counter(baseline["seven_original_D_extension_E_by_tag"])
                or len(accepted_sets)!=baseline["S_with_positive_D_anchor"]):
            raise AssertionError("INDEPENDENT D-FIRST fourflag physical tensor conflicts with historical Q-FIRST seven selected original W32")
    return {
        "s":s,"V":V,"a":a,
        "genuine_original_D_anchors":len(D),
        "physical_point_only_all_D_unilateral_candidate_fourflag_total":
            one_side_total,
        "both_typed_physical_2regular_D_incidence_total":
            sum(bilateral_by_anchored_shape.values()),
        "both_typed_physical_2regular_D_anchored_shape_histogram":
            dict(bilateral_by_anchored_shape),
        "D_FIRST_seven_accepted_extension_E":E,
        "D_FIRST_accepted_seven_sixsets_WITH_D_anchor":len(accepted_sets),
        "D_FIRST_selected_seven_E_by_tag":dict(E_by_tag),
        "D_FIRST_D_pairs_covered_by_any_selected_seven":covered,
        "D_FIRST_D_pairs_ZERO_seven_extensions":len(D)-covered,
        "D_FIRST_selected_Q_ids_generated_directly_from_real_original_flags":True,
        "INDEPENDENT_historical_Q_FIRST_seven_charge_agreed":bool(full_independent),
        "no_all_map_positive_E_lower_PROVED":True,
    }
