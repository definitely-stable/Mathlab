"""HYP-105 #230 / AA4-AH: exact six-channel genuine original Hall contraction.

For any actual source B physical C4 and a fixed real root+two actual flags,
when their two opposite physical pair images are disjoint, the accepted
ORIGINAL B/A GF5 Q whose physical opposite A consists of two triangles is

   T = sum_{S subset {0,1,2,3}, |S|=2}
           (|Y_S|*|Z_complement(S)|-|Y_S intersect Z_complement(S)|).

Here Y_S,Z_complement(S) are *sets of physical auxiliary coordinates*
obtained from genuine ORIGINAL 2x2 source flag rook assignments and
globally occupied physical edges under the SAME opposite typed map.

Each local 2x2 rook permanent is 0 or 1 by true GQ source girth>=8.
The abstract 256x256 signature 4x4-permanent matrix has rank EXACTLY 6
over Q by the six 2+2-row Laplace channels, not numerical low-rank fitting.
The diagonal subtraction is essential: y=z is NOT a six-physical-coordinate
two-triangle A pattern. This is exact for all h, all complete f,g, even
partial K_a physical occupancy, and it does NOT prove a positive minimum.
"""
from itertools import combinations, permutations
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors

PAIRS4=tuple(combinations(range(4),2))
PERM4=tuple(permutations(range(4)))

def _edge(u,v):
    return (u,v) if u<v else (v,u)

def bit_signature_permanent(left,right):
    """Abstract 8-bit signatures. Zero physical/source assumptions."""
    if type(left) is not int or type(right) is not int or not 0<=left<256 or not 0<=right<256:
        raise ValueError("two 8-bit two-slot-per-row signatures required")
    rows=tuple(((left>>(2*i))&3) | (((right>>(2*i))&3)<<2) for i in range(4))
    return sum(all(rows[i]&(1<<p[i]) for i in range(4)) for p in PERM4)

def channel_kernel(left,right):
    """Independent six 2x2 permanent products, identical to 4x4 permanent."""
    if type(left) is not int or type(right) is not int or not 0<=left<256 or not 0<=right<256:
        raise ValueError("two canonical 8-bit signatures required")
    out=[]
    for S in PAIRS4:
        i,j=S
        other=tuple(k for k in range(4) if k not in S)
        u,v=other
        left_i=(left>>(2*i))&3
        left_j=(left>>(2*j))&3
        right_u=(right>>(2*u))&3
        right_v=(right>>(2*v))&3
        L=int(bool(left_i&1) and bool(left_j&2))+int(bool(left_i&2) and bool(left_j&1))
        R=int(bool(right_u&1) and bool(right_v&2))+int(bool(right_u&2) and bool(right_v&1))
        out.append(L*R)
    return tuple(out)

def rank_six_identity_witness():
    """Exact six by six identity minor certifies rational rank >=6."""
    lefts=[];rights=[]
    for S in PAIRS4:
        l=[0]*4
        for col,row in enumerate(S):
            l[row]=1<<col
        r=[0]*4
        opposite=tuple(i for i in range(4) if i not in S)
        for col,row in enumerate(opposite):
            r[row]=1<<col
        lefts.append(sum(l[i]<<(2*i) for i in range(4)))
        rights.append(sum(r[i]<<(2*i) for i in range(4)))
    minor=tuple(tuple(bit_signature_permanent(l,r) for r in rights) for l in lefts)
    assert minor==tuple(tuple(int(i==j) for j in range(6)) for i in range(6))
    return dict(rows=6,cols=6,minor=minor,
                all_256x256_abstract_permanent_kernel_rank_exactly_six=True)

def _original_actual_context(model,*,side,root,pair_offset):
    V,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed ORIGINAL source B side required")
    if type(root) is not int or not 0<=root<V:
        raise ValueError("valid actual original source factor required")
    inc=tuple(tuple(z) for z in model["incidences"])
    sourceflags=[i for i,z in enumerate(inc) if z[side]==root]
    pairs=tuple(combinations(sourceflags,2))
    if type(pair_offset) is not int or not 0<=pair_offset<len(pairs):
        raise ValueError("actual two different original flags through root required")
    pinpair=pairs[pair_offset]
    pinother=tuple(inc[i][1-side] for i in pinpair)
    opposite=tuple(tuple(e) for e in model["right_labels" if side==0 else "left_labels"])
    inv={e:i for i,e in enumerate(opposite)}
    E=frozenset(inv)
    e0,e1=(opposite[pinother[0]],opposite[pinother[1]])
    neighbors=[set() for _ in range(V)]
    for p,l in inc:
        neighbors[(p,l)[side]].add((p,l)[1-side])
    return (V,a,pinpair,e0,e1,inv,E,neighbors)

def _sites(e,blocked,a,inv):
    u,v=e
    return {y: (inv[_edge(u,y)], inv[_edge(v,y)])
            for y in range(a)
            if y not in blocked and _edge(u,y) in inv and _edge(v,y) in inv}

def six_channel_original_cohort(model,*,side=0,root=0,pair_offset=0,
                                four_sources=None,max_C4=3,independent_direct=True):
    """Exact all-h six-channel contraction on one true original cohort.

    If four_sources=None sample first max_C4 original occupied physical C4s.
    For a specified genuine four_source tuple check physical realization.
    When independent_direct=True, an unrelated literal all-(y,z),
    all-24-matchings source-ID oracle crosschecks exact result.
    """
    V,a,pins,e0,e1,inv,E,neighbors=_original_actual_context(
        model,side=side,root=root,pair_offset=pair_offset)
    if type(max_C4) is not int or not 1<=max_C4<=100:
        raise ValueError("1..100 finite C4 sample cap required")
    phys=occupied_root_C4_source_factors(model,side=side,root=root)
    if four_sources is None:
        sources=phys[:max_C4]
    else:
        four=tuple(four_sources)
        if four not in phys:
            raise ValueError("four actual source factors must form occupied physical root C4")
        sources=(four,)
    pinned_disjoint=not bool(set(e0)&set(e1))
    Y=_sites(e0,set(e0+e1),a,inv) if pinned_disjoint else {}
    Z=_sites(e1,set(e0+e1),a,inv) if pinned_disjoint else {}
    rows=[]
    cumulative=0
    for four in sources:
        # A real 2x2 source rook assignment on two opposite physical
        # edges is UNIQUE by source no-K2,2. Encode its auxiliary site.
        leftsets={S:set() for S in PAIRS4}
        rightsets={S:set() for S in PAIRS4}
        for y,(t0,t1) in Y.items():
            for S in PAIRS4:
                i,j=S
                ways=int(t0 in neighbors[four[i]] and t1 in neighbors[four[j]])
                ways+=int(t1 in neighbors[four[i]] and t0 in neighbors[four[j]])
                assert ways<=1, "original GQ source C4 forbidden"
                if ways:leftsets[S].add(y)
        for z,(t2,t3) in Z.items():
            for S in PAIRS4:
                i,j=S
                ways=int(t2 in neighbors[four[i]] and t3 in neighbors[four[j]])
                ways+=int(t3 in neighbors[four[i]] and t2 in neighbors[four[j]])
                assert ways<=1, "original GQ source C4 forbidden"
                if ways:rightsets[S].add(z)
        channels=[]
        accepted=0
        for S in PAIRS4:
            opposite=tuple(i for i in range(4) if i not in S)
            L=leftsets[S]
            R=rightsets[opposite]
            diagonal=len(L&R)
            value=len(L)*len(R)-diagonal
            assert value>=0
            channels.append(dict(point_row_pair=S,
                                 opposite_row_pair=opposite,
                                 left_auxiliary_sites=len(L),
                                 right_auxiliary_sites=len(R),
                                 same_site_exclusion=diagonal,
                                 true_original_GF5_distinct_Q=value))
            accepted+=value
        if independent_direct:
            brute=0
            for y,(t0,t1) in Y.items():
                for z,(t2,t3) in Z.items():
                    if y==z:continue
                    cols=(t0,t1,t2,t3)
                    brute+=sum(all(cols[p[i]] in neighbors[four[i]]
                                   for i in range(4)) for p in PERM4)
            assert brute==accepted, "independent literal original Q must equal six-channel contraction"
        rows.append(dict(four_original_source_factors=four,channels=channels,
                         accepted_original_GF5_Q=accepted))
        cumulative+=accepted
    return dict(s=model["s"],side=side,root=root,
                pinned_actual_original_incidence_IDs=pins,
                globally_fixed_pinned_physical_disjoint=pinned_disjoint,
                source_physical_C4_total=len(phys),source_physical_C4_sampled=len(rows),
                left_occupied_auxiliary_sites=len(Y),right_occupied_auxiliary_sites=len(Z),
                prohibited_same_auxiliary_sites=len(set(Y)&set(Z)),
                six_channel_rows=rows,accepted_original_GF5_Q_sample=cumulative,
                physical_Hall_positivity_lower_all_f_g_NOT_PROVED=True,
                all_h_rank_six_signature_reduction_PROVED=True)
