"""HYP-105 #230 AA4-AG: all-f,g occupied physical triangle mass / Hall barrier.

For s=2^h >=2^19 and every true W(3,s) globally injected typed
point/line physical pair maps f,g, the INDEXED count of (real point p,
two real distinct flags, occupied point-C4, occupied line 2-triangle H)
is at least s^14/256, BEFORE real-original four-rook Hall acceptance.
No deterministic accepted GF5 lower is claimed.
"""
from collections import Counter
from itertools import combinations
from math import comb, isqrt
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_d6aa4ae_gq_girth8_sharp_rook import true_gq_four_rook

def minimal_alphabet(s):
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("true s=2^h, h>=1 required")
    V = (s+1)*(s*s+1)
    a = (1+isqrt(1+8*V))//2
    if comb(a,2)<V:
        a+=1
    assert comb(a-1,2)<V<=comb(a,2)
    return V,a,comb(a,2)-V

def analytic_triangle_hall_barrier(s):
    """Whole-map counting. GQ original intersecting-line pair is unique."""
    V,a,m=minimal_alphabet(s)
    N=V*comb(s+1,2)
    # At most floor(32*m/a) vertices have hole-degree >=a/16.
    hot=min(a,(32*m)//a)
    assert hot<=32
    adjacent=a*comb(a-1,2)
    bad=adjacent+hot*(a-1)*(V-1)
    good=max(0,N-bad)
    C4=max(0,3*comb(a-2,4)-m*(a-4)*(a-5))
    # Every four GOOD pinned physical endpoints have hole-degree <a/16.
    # Two disjoint occupied triangles are then constructible.
    triangles=(a*a+3)//4
    lower=good*C4*triangles
    if s>=1<<19:
        assert a>=32 and 2*V<=a*a<=4*s**3
        assert 2*bad<=N
        assert 128*C4>=a**4
        assert lower>=s**14//256
    return dict(s=s,V=V,a=a,m=m,original_root_line_pairs=N,
                high_hole_vertices_upper=hot,adjacent_edge_pairs=adjacent,
                bad_root_line_pairs_upper=bad,good_root_line_pairs_lower=good,
                point_C4_per_root_lower=C4,
                line_triangles_per_good_rootpair_lower=triangles,
                indexed_occupied_pre_Hall_lower=lower,
                all_f_all_g_s14_over_256_PROVED=s>=1<<19,
                original_Hall_positive_s6_lower_NOT_PROVED=True,
                full_seven_GF5_omega_s6_NOT_PROVED=True)

def _validate_edges(occupied,e0,e1,a):
    if type(a) is not int or a<6:
        raise ValueError("a>=6 required")
    E=frozenset(tuple(e) for e in occupied)
    if any(len(e)!=2 or any(type(x) is not int for x in e)
           or not 0<=e[0]<e[1]<a for e in E):
        raise ValueError("canonical occupied edges required")
    e0,e1=tuple(e0),tuple(e1)
    if e0==e1 or e0 not in E or e1 not in E:
        raise ValueError("two different occupied pinned edges required")
    return E,e0,e1

def occupied_two_triangles(occupied,e0,e1,a):
    """Independent literal y,z exhaustive construction for finite a."""
    E,e0,e1=_validate_edges(occupied,e0,e1,a)
    if set(e0)&set(e1):
        return ()
    u,v=e0;w,x=e1
    outside=set(range(a))-set(e0+e1)
    ans=[]
    for y in sorted(outside):
        for z in sorted(outside-{y}):
            edges=tuple(tuple(sorted(p)) for p in ((u,y),(v,y),(w,z),(x,z)))
            if all(e in E for e in edges):
                ans.append(tuple(sorted((e0,e1)+edges)))
    assert len(ans)==len(set(ans))
    return tuple(ans)

def independent_common_neighbors(occupied,e0,e1,a):
    """Physical triangles count: |Y||Z|-|Y intersect Z|."""
    E,e0,e1=_validate_edges(occupied,e0,e1,a)
    if set(e0)&set(e1):
        return 0
    outside=set(range(a))-set(e0+e1)
    Y={i for i in outside if all(tuple(sorted((i,u))) in E for u in e0)}
    Z={i for i in outside if all(tuple(sorted((i,u))) in E for u in e1)}
    return len(Y)*len(Z)-len(Y&Z)

def original_triangle_hall_cohort(model,*,side=0,root=0,pair_offset=0,max_C4=3):
    """TRUE GQ source incidence, one f,g, exact triangle Hall/C8 identity."""
    V,a,_=_valid_original_model(model)
    inc=tuple(tuple(z) for z in model["incidences"])
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed side must be point=0/line=1")
    if type(root) is not int or not 0<=root<V:
        raise ValueError("actual original root required")
    if type(max_C4) is not int or not 1<=max_C4<=100:
        raise ValueError("positive bounded finite C4 sample required")
    flags=[i for i,e in enumerate(inc) if e[side]==root]
    pairs=tuple(combinations(flags,2))
    if type(pair_offset) is not int or not 0<=pair_offset<len(pairs):
        raise ValueError("real pair of distinct original flags required")
    pinned=pairs[pair_offset]
    opposite=tuple(inc[j][1-side] for j in pinned)
    labels=tuple(tuple(e) for e in model["right_labels" if side==0 else "left_labels"])
    E=frozenset(labels)
    inv={edge:i for i,edge in enumerate(labels)}
    e0,e1=labels[opposite[0]],labels[opposite[1]]
    H=occupied_two_triangles(E,e0,e1,a)
    count=independent_common_neighbors(E,e0,e1,a)
    assert len(H)==count
    source_C4=occupied_root_C4_source_factors(model,side=side,root=root)
    neighbors=[set() for _ in range(V)]
    for p,l in inc:
        neighbors[(p,l)[side]].add((p,l)[1-side])
    seen=failed=double=accepted=0
    witness_types=Counter()
    for four in source_C4[:max_C4]:
        for h in H:
            rest=tuple(e for e in h if e not in (e0,e1))
            assert len(rest)==4 and all(e in inv for e in rest)
            cols=tuple(inv[e] for e in rest)
            rows=tuple(sum((1<<j) for j,t in enumerate(cols)
                           if t in neighbors[q]) for q in four)
            check=true_gq_four_rook(rows)
            assert check["gq_girth_eight_eligible"]
            perm=check["true_original_four_rook_permanent"]
            seen+=1;accepted+=perm
            if perm==2:
                assert check["exactly_two_perfect_matchings_implies_original_C8"]
                double+=1
            if perm==0:
                failed+=1
                for k in range(1,5):
                    failures=[]
                    for idx in combinations(range(4),k):
                        mask=0
                        for j in idx:mask|=rows[j]
                        if mask.bit_count()<k:
                            failures.append(k-mask.bit_count())
                    if failures:
                        witness_types[(k,max(failures))]+=1
                        break
                else:
                    raise AssertionError("Hall failure requires nonempty cut")
    assert accepted==seen-failed+double
    return dict(s=model["s"],side=side,root=root,pinned_original_flags=pinned,
                disjoint_pinned_physical_edges=not bool(set(e0)&set(e1)),
                physical_C4_total=len(source_C4),
                physical_C4_sampled=min(max_C4,len(source_C4)),
                occupied_two_triangles_per_C4=count,
                independent_triangle_count=len(H),
                indexed_occupied_triangle_candidates=seen,
                original_Hall_failed=failed,original_Hall_positive=seen-failed,
                induced_original_C8_extra=double,
                accepted_original_GF5_restricted=accepted,
                canonical_Hall_deficits={str(k):v for k,v in sorted(witness_types.items())},
                adversarial_all_g_Hall_lower_NOT_PROVED=True)
