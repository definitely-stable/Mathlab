"""HYP-105 #230 AA4-AN: TRUE original bilateral D pair -> six-Q port completion.

Fix TWO genuinely different W(3,s) original incidence flags (p,l),(q,m)
with p!=q and l!=m, such that each pair of globally injected typed
physical original factor edge labels shares EXACTLY one coordinate.

On EACH typed physical projection the existing two physical edges form
a degree-2 closed center and leave two distinct degree-1 port endpoints.
To complete a six-coordinate degree-2 GF5 leafless projection with four
further ORIGINAL incidence flags, the four physical pair edges on the
remaining five vertices have port degrees 1,1 and three new degrees 2,2,2.

EXHAUSTIVE undirected loopless multigraph classification:
   P5                 six orders of the three new vertices;
   K2 + C3            one;
   P3 + doubled K2    three choices of the cherry's new midpoint.
That is EXACTLY 10*C(a-3,3) formal physical completions PER TYPE,
before globally occupied factor images and original incidence matching.

All-h source-Hall transfer: for each pair of physically occupied
point-side and line-side four-factor multiset completions, count each
genuine ORIGINAL six-incidence-ID Q formed by a perfect matching of
the four original source point factor slots to the four original source
line factor slots in the same ORIGINAL W(3,s) incidence relation.
Deduplicate repeated factor slots by genuine original six-ID Q.
Then select only true seven positive GF5 classes, rejecting unaligned
A/A original Q. This is an exact identity, NOT an all-map lower.

W32 full globally bijective physical K6 permits all 10x10=100 paired
physical completion templates for EVERY true AA4-AL D pair.
Nevertheless some genuinely original D pairs have no selected Q.
A new finite certificate distinguishes empty original Hall source
matchings from A/A unaligned nonselected projection matches.

The structural theorem is all-h. Finite explicit enumeration is W32
ONLY; W34 checks membership of independent local valid true original
B/A Q without pretending to enumerate all >million pattern pairs.
"""
from collections import Counter
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    _different_true_flag_physically_bilateral,
    original_D_pair_index,six_Q_anchored_D_pairs)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import _projection_source_type


def physical_edge(u,v):
    if u==v:raise ValueError("simple physical edge only")
    return (u,v) if u<v else (v,u)


def all_h_port_completion_count(s):
    """All h exact 3-category formal physical completions per D-pair/type."""
    from hyp105_issue230_d6aa4al_global_original_coordinate_transport import _parameters
    V,d,a=_parameters(s)
    n=comb(a-3,3)
    return {
        "s":s,"V":V,"a":a,
        "physical_new_coordinate_triples":n,
        "physical_P5_paths":6*n,
        "physical_K2_plus_C3":n,
        "physical_P3_plus_parallel_K2":3*n,
        "physical_all_one_typed_residual_completions":10*n,
        "physical_all_two_typed_candidate_pairs_before_original_Hall":100*n*n,
        "physical_pattern_capacity_is_NOT_an_original_six_Q_lower":True,
        "all_complete_injected_original_f_g_all_h_structural":True,
    }


def true_original_D_physical_ports(inc,left,right,pair):
    """Canonical actual original flag pair and typed closed center + ports."""
    pair=tuple(pair)
    if len(pair)!=2 or pair[0]>=pair[1] or pair[0]<0 or pair[1]>=len(inc):
        raise ValueError("unordered two distinct true original incidence indices")
    if not _different_true_flag_physically_bilateral(*pair,inc,left,right):
        raise ValueError("not an actual bilateral compatible AA4-AL D pair")
    def one(src_labels,side):
        e0=tuple(src_labels[inc[pair[0]][side]])
        e1=tuple(src_labels[inc[pair[1]][side]])
        c=tuple(set(e0)&set(e1))
        if len(c)!=1:
            raise AssertionError("globally injected genuine source factors share one coordinate")
        return c[0],next(x for x in e0 if x!=c[0]),next(x for x in e1 if x!=c[0])
    return (one(left,0),one(right,1))


def _pattern_edges(ports,new_triple):
    """Ten and ONLY ten canonical degree-profile 4-edge physical multisets."""
    center,a,b=ports
    x,y,z=tuple(sorted(new_triple))
    if len({center,a,b,x,y,z})!=6:
        raise ValueError("all six physical coordinates distinct")
    for order in permutations((x,y,z)):
        h0,h1,h2=order
        yield "P5",tuple(sorted((
            physical_edge(a,h0),physical_edge(h0,h1),
            physical_edge(h1,h2),physical_edge(h2,b))))
    yield "K2+C3",tuple(sorted((
        physical_edge(a,b),physical_edge(x,y),
        physical_edge(x,z),physical_edge(y,z))))
    for mid in (x,y,z):
        others=tuple(k for k in (x,y,z) if k!=mid)
        double=physical_edge(*others)
        yield "P3+2K2",tuple(sorted((
            physical_edge(a,mid),physical_edge(b,mid),
            double,double)))


def _strict_occupied_half_patterns(ports,a,inv):
    """Globally fixed map: don't fabricate inverse original source factors."""
    blocked=frozenset(ports)
    other=tuple(v for v in range(a) if v not in blocked)
    entries=[]
    seen=set()
    formal=Counter()
    occupied=Counter()
    for triple in combinations(other,3):
        for tag,edges in _pattern_edges(ports,triple):
            formal[tag]+=1
            if edges in seen:raise AssertionError("physical residual multigraph generated twice")
            seen.add(edges)
            if any(e not in inv for e in edges):
                continue
            occupied[tag]+=1
            entries.append((tag,tuple(inv[e] for e in edges),edges))
    exact=10*comb(a-3,3)
    if len(seen)!=exact or sum(formal.values())!=exact:
        raise AssertionError("physical completion three-topology count wrong")
    return tuple(entries),dict(formal),dict(occupied)


def physical_D_pair_half_patterns(model,pair,*,side):
    """All-h physical-only actual occupied half patterns for ONE real D pair."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed physical original source point/line side")
    ports=true_original_D_physical_ports(inc,left,right,pair)[side]
    inv={tuple(e):i for i,e in enumerate((left,right)[side])}
    entries,formal,occ=_strict_occupied_half_patterns(ports,a,inv)
    return {
        "source_side":side,"actual_original_pair":tuple(pair),
        "ports":ports,"physical_formal_topology_counts":formal,
        "physical_occupied_topology_counts":occ,
        "physical_formal_total":sum(formal.values()),
        "physical_occupied_total":len(entries),
        "physical_global_injection_missing_reject":
            sum(formal.values())-len(entries),
        "globally_occupied_true_original_source_factor_patterns":entries,
        "genuine_original_Hall_matching_positivity_NOT_PROVED":True,
    }


def _original_four_flag_completions(inc_index,pair,left_pattern,right_pattern):
    """Physical half-pattern => at most 24 ORIGINAL valid 4-flag matches.

    Deduplicates repeated source factor slots (parallel K2) by actual
    six-distinct ORIGINAL incidence-ID Q. No source forest substitution.
    """
    left_sources=left_pattern[1]
    right_sources=right_pattern[1]
    result=set()
    pinned=set(pair)
    for right_perm in set(permutations(right_sources)):
        indices=[]
        for p,l in zip(left_sources,right_perm):
            idx=inc_index.get((p,l))
            if idx is None or idx in pinned:
                break
            indices.append(idx)
        else:
            Q=tuple(sorted(tuple(pair)+tuple(indices)))
            if len(set(Q))==6:
                result.add(Q)
    return result


def exact_original_D_pair_six_Q_funnel(model,pair,*,retain_selected=True):
    """Exact all-h genuine-original two-type physical->Hall->seven funnel.

    Cost per fixed D pair O(C(a-3,3)^2*100*24) brute but exact;
    no claim of scalable all-global polynomial algorithm for s large.
    Source matching only counts true original incidence IDs.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    pair=tuple(pair)
    ports=true_original_D_physical_ports(inc,left,right,pair)
    invs=({tuple(e):i for i,e in enumerate(left)},
          {tuple(e):i for i,e in enumerate(right)})
    half=[]
    for side in (0,1):
        entries,formal,occupied=_strict_occupied_half_patterns(
            ports[side],a,invs[side])
        half.append((entries,formal,occupied))
    physically_paired=len(half[0][0])*len(half[1][0])
    inc_index={tuple(edge):i for i,edge in enumerate(inc)}
    original_both_proj=set()
    tags={}
    bad_aa=set()
    for left_pattern in half[0][0]:
        for right_pattern in half[1][0]:
            for Q in _original_four_flag_completions(
                    inc_index,pair,left_pattern,right_pattern):
                if Q in original_both_proj:continue
                original_both_proj.add(Q)
                lk=_projection_source_type(Q,inc,0)
                rk=_projection_source_type(Q,inc,1)
                tag=independent_joint_classify(
                    Q,lk,rk,inc,left,right)
                if tag is None:
                    if (lk,rk)!=("A","A"):
                        raise AssertionError("all non-AA actual source projection pairs selected")
                    bad_aa.add(Q)
                else:
                    tags[Q]=tag
    if len(tags)+len(bad_aa)!=len(original_both_proj):
        raise AssertionError("genuine original seven class partition")
    total=all_h_port_completion_count(s)
    assert half[0][1]==half[1][1] and sum(half[0][1].values())==total[
        "physical_all_one_typed_residual_completions"]
    if len(original_both_proj)>24*physically_paired:
        raise AssertionError("more Q than physical matching permutations")
    return {
        "s":s,"actual_original_D_pair":pair,
        "point_side_occupied_physical_pattern_count":len(half[0][0]),
        "line_side_occupied_physical_pattern_count":len(half[1][0]),
        "physical_double_completion_candidate_pairs":physically_paired,
        "actual_original_six_Q_both_leafless_physical_projections":
            len(original_both_proj),
        "actual_original_six_Q_unaligned_AA_rejected":len(bad_aa),
        "actual_original_positive_seven_GF5_six_Q_extensions":len(tags),
        "actual_original_positive_seven_GF5_by_tag":dict(Counter(tags.values())),
        "selected_ORIGINAL_six_incidence_ID_Q_tags":tags if retain_selected else None,
        "unaligned_AA_original_six_Q":bad_aa if retain_selected else None,
        "all_h_exact_original_D_pair_extension_algorithm":True,
        "all_map_positive_extension_lower_NOT_PROVED":True,
    }


def original_Q_D_anchor_residual_kind(model,pair,Q,*,side):
    """For ANY valid original D-anchored six-Q, identify actual residual P5 etc.

    Efficient local W34 audit: does not enumerate all its many candidate
    new physical triples/pairs.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed source side 0/1")
    Q=tuple(sorted(Q));pair=tuple(pair)
    if len(Q)!=6 or len(set(Q))!=6 or not set(pair).issubset(Q):
        raise ValueError("actual true original six different IDs must contain real D pair")
    port=true_original_D_physical_ports(inc,left,right,pair)[side]
    residual=tuple(sorted(tuple((left,right)[side][inc[i][side]])
                          for i in Q if i not in pair))
    used=set(port)
    for edge in residual: used.update(edge)
    if len(used)!=6:
        raise ValueError("original source Q does not have 6-coordinate leafless projection")
    triple=tuple(sorted(used-set(port)))
    for tag,physical in _pattern_edges(port,triple):
        if physical==residual:
            return tag
    raise ValueError("residual physical pair-edge multigraph has wrong degrees")


def exact_true_original_W32_D_funnel_census(model,*,reference_seven=True):
    """All genuine original D pairs: distinct PHYSICAL/Hall/GF5 failures.

    W32 only; computed directly D-FIRST, with historical Q-first
    complete-seven cross-check optional. The table distinguishes:
       ZERO original BOTH-projection six-ID Q;
       positive original BOTH-projection Q but ZERO selected seven GF5;
       at least ONE positively selected genuine seven-GF5 Q.
    This partition is exact and exclusive; a physical six-Q compatible
    with both projections can still be unaligned A/A and nonselected.
    """
    from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import original_D_pair_index
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("exact full original source D census W32 only")
    D=original_D_pair_index(model)
    sum_hall=sum_aa=sum_selected=0
    failure=Counter()
    selected_by_tag=Counter()
    for pair in sorted(D):
        z=exact_original_D_pair_six_Q_funnel(
            model,pair,retain_selected=False)
        assert z["physical_double_completion_candidate_pairs"]==100
        H=z["actual_original_six_Q_both_leafless_physical_projections"]
        R=z["actual_original_six_Q_unaligned_AA_rejected"]
        S=z["actual_original_positive_seven_GF5_six_Q_extensions"]
        if H!=R+S:raise AssertionError("source/Hall/seven exact partition")
        sum_hall+=H;sum_aa+=R;sum_selected+=S
        selected_by_tag.update(z["actual_original_positive_seven_GF5_by_tag"])
        if H==0:
            failure["no_original_Hall_six_Q"]+=1
        elif S==0:
            failure["original_six_Q_only_unaligned_AA"]+=1
        else:
            failure["has_seven_positive_original_six_Q"]+=1
    if sum(failure.values())!=len(D):
        raise AssertionError("distinct genuine D pair partition not exhaustive")
    if reference_seven:
        from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
            exact_W32_original_seven_pair_extension_certificate)
        h=exact_W32_original_seven_pair_extension_certificate(
            model,independent_oracle=True)
        if (sum_selected!=h["E_original_extension_incidences"] or
            failure["has_seven_positive_original_six_Q"]!=h[
                "D_covered_by_at_least_one_selected_original_six_Q"] or
            len(D)!=h["D_unordered_actual_original_bilateral_two_flag_pairs"]):
            raise AssertionError("independent complete original 62370-seven-Q source oracle")
    return {
        "s":s,"D_all_actual_original_compatible_flag_pairs":len(D),
        "physical_two_side_templates_PER_true_original_D_pair":100,
        "total_occupied_both_side_physical_template_pair_incidence":100*len(D),
        "original_BOTH_leafless_source_matched_six_Q_pair_charge":sum_hall,
        "original_UNALIGNED_AA_rejected_six_Q_pair_charge":sum_aa,
        "original_SELECTED_positive_seven_six_Q_pair_charge":sum_selected,
        "D_pair_stage_partition":dict(failure),
        "D_uncovered_by_selected_SEVEN":(
            failure["no_original_Hall_six_Q"]+
            failure["original_six_Q_only_unaligned_AA"]),
        "seven_original_selected_charge_by_class":dict(selected_by_tag),
        "all_D_pairs_original_physical_completions_occupied_W32":True,
        "each_D_pair_uniform_selected_extension_false_finite":(
            failure["no_original_Hall_six_Q"]+
            failure["original_six_Q_only_unaligned_AA"]>0),
        "all_h_s6_lower_NOT_PROVED":True,
    }
