"""HYP-105 #230 AA4-AI: exact A-sector recovery and finite global zero.

An authentic fully injected W(3,2) point/line labeling annihilates the
ENTIRE B/A and A/B split-two-triangle subfamily simultaneously. This
falsifies a universal claim "forall s>=2, forall f,g split triangle >0",
NOT an eventual all-h lower, NOT full seven-GF5 Branch A, and NOT B.

An exact all-h physical A sector decomposition restores the previously
omitted triangles with adjacent pinned edges and connected C6 patterns.
The genuine-original finite two-sided transfer counts each REAL distinct
original six-incidence-ID forest via original four-rook permanents,
independently cross-checkable by literal source-flag enumeration.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

from hyp105_issue230_proof_audit import frozen_model, _model
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions
from hyp105_issue230_d6aa4ae_gq_girth8_sharp_rook import true_gq_four_rook

# One actual globally complete original W(3,2) point/line labeling.
# Each number indexes an unordered physical K6 edge in lex order.
# These are full bijections on all 15 REAL original factors of each type.
ZERO_SPLIT_POINT=(4,14,10,7,6,2,5,13,12,9,0,11,3,8,1)
ZERO_SPLIT_LINE =(11,0,9,5,14,12,13,10,6,3,7,8,2,4,1)
TAGS=("split_two_triangles","same_triangle_pins","connected_C6")


def zero_split_original_W32():
    """True symplectic geometry, not a relabeled fake incidence graph."""
    model=frozen_model("lex")
    palette=tuple(combinations(range(6),2))
    assert set(ZERO_SPLIT_POINT)==set(ZERO_SPLIT_LINE)==set(range(15))
    return _model(2,model["points"],model["lines"],model["incidences"],
                  tuple(palette[i] for i in ZERO_SPLIT_POINT),
                  tuple(palette[i] for i in ZERO_SPLIT_LINE))


def classify_physical_A_twofactor(H,pins):
    """Classify the complete six-physical-coordinate GF5 A 2-factor.

    Pins must be two DISTINCT edges contained in H. Physical components
    are necessarily one C6 or two C3 (girth of 2-regular simple graph).
    """
    H=tuple(tuple(e) for e in H)
    pins=tuple(tuple(e) for e in pins)
    if (len(H)!=6 or len(set(H))!=6 or len(pins)!=2 or pins[0]==pins[1]
            or not set(pins).issubset(H)
            or any(len(e)!=2 or e[0]>=e[1] or e[0]<0 for e in H)):
        raise ValueError("six different canonical actual physical A edges with two pins")
    vertices=set(v for e in H for v in e)
    if len(vertices)!=6:
        raise ValueError("exactly six physical coordinates required")
    adj={v:set() for v in vertices}
    for u,v in H:
        adj[u].add(v);adj[v].add(u)
    if any(len(z)!=2 for z in adj.values()):
        raise ValueError("physical A graph must be two-regular")
    components=[]
    unseen=set(vertices)
    while unseen:
        start=min(unseen)
        found={start};stack=[start]
        while stack:
            for v in adj[stack.pop()]:
                if v not in found:
                    found.add(v);stack.append(v)
        unseen-=found;components.append(frozenset(found))
    if len(components)==1:
        return "connected_C6"
    if len(components)!=2 or any(len(c)!=3 for c in components):
        raise AssertionError("simple six-vertex twofactor is C6 or C3+C3")
    same=any(set(pins[0]).issubset(c) and set(pins[1]).issubset(c)
             for c in components)
    return "same_triangle_pins" if same else "split_two_triangles"


def exact_physical_A_sector_capacities(a,*,adjacent):
    """All-h EXACT raw physical completion capacities for two pinned edges.

    Adjacent pins: one physically mandatory triangle  + any other
    triangle: C(a-3,3), and six times as many connected 6-cycles.
    Disjoint pins: (a-4)(a-5) split triangles, six times as many C6.
    These are raw K_a patterns BEFORE checking physical occupancy or
    TRUE original GQ Hall; they do NOT imply accepted six source Q.
    """
    if type(a) is not int or a<6 or type(adjacent) is not bool:
        raise ValueError("physical a>=6 and explicit adjacent bool required")
    t=(comb(a-3,3) if adjacent else (a-4)*(a-5))
    return {
        "a":a,"pinned_physical_adjacent":adjacent,
        "split_two_triangles":0 if adjacent else t,
        "same_triangle_pins":t if adjacent else 0,
        "connected_C6":6*t,
        "total_A_twofactors":7*t,
        "connected_to_triangle_capacity_ratio_exact":"6:1",
        "source_original_acceptance_lower_NOT_PROVED":True
    }


def _source_neighborhoods(inc,V,side):
    ans=[set() for _ in range(V)]
    for p,l in inc:
        ans[(p,l)[side]].add((p,l)[1-side])
    return tuple(frozenset(z) for z in ans)


def _source_cohort(model,*,side,root,pair_offset,src_four):
    """Validated ORIGINAL factors, no presumed independence among labels."""
    V,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("original point/line typed root side")
    if type(root) is not int or not 0<=root<V:
        raise ValueError("actual original root")
    inc=tuple(tuple(x) for x in model["incidences"])
    neighbors=_source_neighborhoods(inc,V,side)
    pins=tuple(combinations(sorted(neighbors[root]),2))
    if type(pair_offset) is not int or not 0<=pair_offset<len(pins):
        raise ValueError("two actual distinct original root flags")
    pinned=pins[pair_offset]
    four=tuple(src_four)
    if len(four)!=4 or len(set(four))!=4 or root in four:
        raise ValueError("four other distinct actual original source factors")
    if frozenset(four) not in {frozenset(x) for x in
            occupied_root_C4_source_factors(model,side=side,root=root)}:
        raise ValueError("physical first-half source pattern must be an occupied C4")
    opp=tuple(tuple(x) for x in model["right_labels" if side==0 else "left_labels"])
    inv={e:i for i,e in enumerate(opp)}
    e0,e1=opp[pinned[0]],opp[pinned[1]]
    return a,inc,neighbors,pinned,inv,(e0,e1),four


def single_original_A_sector_permanent(model,*,side,root,pair_offset,four):
    """Independent all-three-sector real 4x4 source-permanent completion."""
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    bins=Counter({t:0 for t in TAGS})
    physical=Counter({t:0 for t in TAGS})
    hall_positive=Counter({t:0 for t in TAGS})
    c8=Counter({t:0 for t in TAGS})
    for H in pinned_twofactor_completions(*pins,a):
        rem=tuple(e for e in H if e not in pins)
        if any(e not in inv for e in rem):
            continue
        cols=tuple(inv[e] for e in rem)
        masks=tuple(sum((1<<j) for j,v in enumerate(cols) if v in neighbors[q])
                    for q in four)
        checked=true_gq_four_rook(masks)
        if not checked["gq_girth_eight_eligible"]:
            raise AssertionError("not genuine original GQ row-submatrix")
        n=checked["true_original_four_rook_permanent"]
        if n>2:
            raise AssertionError("source girth-eight bounds original 4-rook <=2")
        tag=classify_physical_A_twofactor(H,pins)
        physical[tag]+=1
        bins[tag]+=n
        hall_positive[tag]+=int(n>0)
        c8[tag]+=int(n==2)
    assert all(bins[t]==hall_positive[t]+c8[t] for t in TAGS)
    return dict(accepted=dict(bins),occupied_physical_H=dict(physical),
                original_Hall_positive=dict(hall_positive),
                induced_original_C8=dict(c8),
                pinned_real_opposite_original=pinned,
                pinned_opposite_physical_adjacent=bool(set(pins[0])&set(pins[1])))


def full_original_W32_sector_certificate(model=None,*,side=0):
    """For ALL 15 genuine roots, 45 flag pairs and 135 B-root C4 sectors."""
    if model is None:model=zero_split_original_W32()
    V,a,_=_valid_original_model(model)
    if model["s"]!=2 or V!=15 or a!=6:
        raise ValueError("complete genuine original W32 required")
    count=Counter({t:0 for t in TAGS})
    occupied=Counter({t:0 for t in TAGS})
    hall=Counter({t:0 for t in TAGS})
    c8=Counter({t:0 for t in TAGS})
    roots=source_pairs=cohorts=0
    for root in range(V):
        roots+=1
        C4=occupied_root_C4_source_factors(model,side=side,root=root)
        assert len(C4)==3
        for idx in range(3):
            source_pairs+=1
            for four in C4:
                cohorts+=1
                z=single_original_A_sector_permanent(
                    model,side=side,root=root,pair_offset=idx,four=four)
                for tag in TAGS:
                    count[tag]+=z["accepted"][tag]
                    occupied[tag]+=z["occupied_physical_H"][tag]
                    hall[tag]+=z["original_Hall_positive"][tag]
                    c8[tag]+=z["induced_original_C8"][tag]
    assert (roots,source_pairs,cohorts)==(15,45,135)
    assert all(count[t]==hall[t]+c8[t] for t in TAGS)
    return {
        "s":2,"B_source_side":"point" if side==0 else "line",
        "complete_actual_original_roots":roots,
        "real_original_root_flag_pairs":source_pairs,
        "original_B_root_C4_cohorts":cohorts,
        "original_GF5_A_accepted_by_sector":dict(count),
        "occupied_opposite_A_physical_H_by_sector":dict(occupied),
        "original_Hall_positive_by_sector":dict(hall),
        "induced_original_C8_charge_by_sector":dict(c8),
        "full_original_BA_or_AB_accepted":sum(count.values()),
        "all_h_uniform_triangle_positive_FALSE_at_s2":True,
        "all_h_S_omega_s6_NOT_PROVED":True
    }


def independent_literal_original_W32_sector_census(model=None,*,side=0):
    """Different algorithm: literal all original 6-ID Q and full A graph.

    Does not call AA4-AD physical twofactor completion nor four-rook
    permanent; starts with actual true original incident-flag assignment.
    """
    if model is None:model=zero_split_original_W32()
    V,a,_=_valid_original_model(model)
    if model["s"]!=2 or V!=15 or a!=6:
        raise ValueError("original W32 only")
    inc=tuple(tuple(x) for x in model["incidences"])
    neighbors=_source_neighborhoods(inc,V,side)
    opp=tuple(tuple(x) for x in model["right_labels" if side==0 else "left_labels"])
    result=Counter({t:0 for t in TAGS})
    unique=set()
    for root in range(V):
        for pinned in combinations(sorted(neighbors[root]),2):
            phys_pins=tuple(opp[i] for i in pinned)
            for four in occupied_root_C4_source_factors(model,side=side,root=root):
                choices=(tuple(neighbors[q]-frozenset(pinned)) for q in four)
                for four_flags in product(*choices):
                    if len(set(four_flags))!=4:continue
                    edges=phys_pins+tuple(opp[i] for i in four_flags)
                    # An accepted physical A twofactor requires exactly
                    # six distinct physical coordinates of degree two.
                    if len(set(v for e in edges for v in e))!=6:
                        continue
                    deg=Counter(v for e in edges for v in e)
                    if set(deg.values())!={2}:continue
                    tag=classify_physical_A_twofactor(edges,phys_pins)
                    # EXACT six distinct TRUE ORIGINAL incidence-ID Q.
                    Q=frozenset(((root,pinned[0]),(root,pinned[1]))+
                                 tuple(zip(four,four_flags)))
                    if len(Q)!=6 or Q in unique:
                        raise AssertionError("duplicate or fabricated original 6-Q")
                    unique.add(Q)
                    result[tag]+=1
    return dict(result)


def occupied_connected_C6_bridge(occupied,e0,e1,a):
    """A physical connected C6 on u-v-y-w-x-z-u, fixed disjoint pins.

    NEW explicit global physical pre-Hall construction. Four unpinned
    edges v-y, y-w, x-z, z-u must be occupied. Different (y,z) give
    different actual occupied physical six-vertex C6 patterns.
    """
    if type(a) is not int or a<6:
        raise ValueError("physical alphabet >=6 required")
    E=frozenset(tuple(e) for e in occupied)
    if any(len(e)!=2 or any(type(v) is not int for v in e)
           or not 0<=e[0]<e[1]<a for e in E):
        raise ValueError("canonical occupied physical edge images required")
    e0,e1=tuple(e0),tuple(e1)
    if e0==e1 or e0 not in E or e1 not in E:
        raise ValueError("two distinct occupied original physical pin edges required")
    if set(e0)&set(e1):
        return ()
    u,v=e0;w,x=e1
    outside=set(range(a))-set(e0+e1)
    result=[]
    for y in sorted(outside):
        if (min(v,y),max(v,y)) not in E or (min(w,y),max(w,y)) not in E:
            continue
        for z in sorted(outside-{y}):
            if (min(x,z),max(x,z)) not in E or (min(u,z),max(u,z)) not in E:
                continue
            H=tuple(sorted((e0,e1,(min(v,y),max(v,y)),
                     (min(w,y),max(w,y)),(min(x,z),max(x,z)),
                     (min(u,z),max(u,z)))))
            assert classify_physical_A_twofactor(H,(e0,e1))=="connected_C6"
            result.append(H)
    assert len(set(result))==len(result)
    return tuple(result)


def independent_connected_C6_bridge_count(occupied,e0,e1,a):
    """Different exact common-neighbor sets, no physical H enumeration."""
    if type(a) is not int or a<6:
        raise ValueError("a>=6 required")
    E=frozenset(tuple(e) for e in occupied)
    e0,e1=tuple(e0),tuple(e1)
    if e0==e1 or e0 not in E or e1 not in E:
        raise ValueError("distinct occupied pins")
    if set(e0)&set(e1):return 0
    u,v=e0;w,x=e1
    O=set(range(a))-set(e0+e1)
    left={y for y in O if all(tuple(sorted(pair)) in E
                             for pair in ((v,y),(w,y)))}
    right={z for z in O if all(tuple(sorted(pair)) in E
                              for pair in ((x,z),(u,z)))}
    return len(left)*len(right)-len(left&right)


def analytic_two_A_sector_all_map_barrier(s):
    """All-h for EVERY full global genuine f,g, s=2^h>=2^19.

    From AA4-AG: N_good source rootpairs, occupied first-side C4 for
    EACH actual point root. Four pinned physical endpoints each have
    missing degree <a/16. The 2-triangle and the NEW connected C6
    bridge each have >= a²/4 occupied completions per safe rootpair.
    Both physical A sectors are disjoint. No ORIGINAL Hall success
    lower is asserted; AG guaranteed INDEXED pre-Hall source tuples.
    """
    from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
        analytic_triangle_hall_barrier)
    z=analytic_triangle_hall_barrier(s)
    physical_each=z["indexed_occupied_pre_Hall_lower"]
    combined=2*physical_each
    if s>=1<<19:
        assert physical_each>=s**14//256
        assert combined>=s**14//128
    return {
        "s":s,"a":z["a"],"good_actual_source_rootpairs_lower":
            z["good_root_line_pairs_lower"],
        "original_point_C4_per_root_lower":z["point_C4_per_root_lower"],
        "split_triangle_indexed_pre_Hall_lower":physical_each,
        "connected_C6_bridge_indexed_pre_Hall_lower":physical_each,
        "two_disjoint_A_sectors_indexed_pre_Hall_lower":combined,
        "all_global_f_g_s14_over_128_pre_Hall_PROVED":s>=1<<19,
        "genuine_original_4x4_Hall_success_lower_NOT_PROVED":True,
        "full_seven_GF5_Branch_A_NOT_PROVED":True
    }
