"""AA4-LOW-MOMENT-EXACT: scalable all-order ORIGINAL priority-to-Jensen audit.

Exact common-neighbor-correlation probability for 1,2,3 distinct
pairwise nonconflicting ORIGINAL source owners, without exponential
subset-DP cap or pretending different path events are independent.

The mathematical formula uses only uniform independent priorities.
Finite true W(3,2)/W(3,4) source examples import solely the independently
constructed original symplectic incidence fixture, never old selector code.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import json

SCHEMA="mathlab.hyp105.original-low-moment-exact-priority.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K_ROOT=64


def _validate(nbr, owners):
    owners=tuple(owners)
    n=len(nbr)
    r=len(owners)
    if r<1 or r>3 or len(set(owners))!=r:
        raise ValueError("one to three distinct named ORIGINAL owners required")
    if any(type(i)!=int or i<0 or i>=n for i in owners):
        raise ValueError("owner out of source")
    if any(i in nbr[i] for i in owners):
        raise ValueError("self-conflict is illegal")
    if any(j in nbr[i] or i in nbr[j] for i,j in combinations(owners,2)):
        raise ValueError("owners of proper paths must be source J-independent")
    return owners


def priority_probability(nbr, owners):
    """Exact Fraction for ONE shared ORIGINAL global priority permutation.

    No restriction on size of the union of source conflict neighborhoods.
    Each external neighbor w has bit-mask of owners it conflicts with.
    Integrate external uniform priorities conditional on 2/3 target
    owner priorities, on all r! owner order simplices. At most 6 terms.
    """
    owners=_validate(nbr,owners)
    r=len(owners)
    mask_count=Counter()
    u=set()
    for i,o in enumerate(owners):
        for w in nbr[o]:
            if w<0 or w>=len(nbr) or o not in nbr[w]:
                raise ValueError("source conflict graph must be symmetric")
            u.add(w)
    if u&set(owners):
        raise ValueError("a retained path has conflicting owners")
    for w in u:
        mask=sum(1<<i for i,o in enumerate(owners) if w in nbr[o])
        if mask==0:
            raise AssertionError("external neighbor missing its owner")
        mask_count[mask]+=1
    b=r+len(u)
    if b<r:
        raise AssertionError("invalid original neighborhood")
    total=Fraction(0)
    for ordering in permutations(range(r)):
        # c[k] = external source neighbors whose LATEST constrained
        # original path owner is the k'th one in increasing priority.
        c=[0]*r
        for mask,n in mask_count.items():
            latest=max(j for j,i in enumerate(ordering) if mask&(1<<i))
            c[latest]+=n
        # Substitute z_j=1-t_(r+1-j). On the simplex
        # 0<z1<...<zr<1, integral prod(z_j**c_(r+1-j))
        # = prod_j 1/(j + c_r + ... + c_(r+1-j)).
        prefix=0
        term=Fraction(1)
        for j in range(1,r+1):
            prefix+=c[r-j]
            term/=prefix+j
        total+=term
    sufficient=Fraction(1,comb(b,r))
    # Condition on all external ORIGINAL priorities. Each target owner
    # survives independently given those priorities, with conditional
    # probability equal to the minimum of its neighbors' priorities.
    # These nonnegative minimum functions are ALL coordinatewise
    # nondecreasing in the independent external priorities.
    # The elementary product-measure monotone-covariance (Harris)
    # inequality therefore gives E(prod minimum_i)>=prod E(minimum_i)
    # =prod 1/(degree_J(owner_i)+1). NO source event independence assumed.
    degree_product=Fraction(1)
    for o in owners:
        degree_product/=len(nbr[o])+1
    harris_root=Fraction(1,(K_ROOT+1)**r)
    # For highly OVERLAPPING source neighborhoods the first-r
    # bound may exceed the degree-product bound; neither dominates
    # pointwise. The true priority probability dominates BOTH.
    if not (0<sufficient<=total<=1 and degree_product<=total):
        raise AssertionError("exact priority breaks source bounds")
    if degree_product<harris_root:
        raise AssertionError("root K64 assumption is violated; prune J first")
    return dict(owners=owners,b=b,mask_counts=tuple(sorted(mask_count.items())),
                exact=total,first_r_sufficient=sufficient,
                exact_beyond_sufficient=total-sufficient,
                source_degree_product_harris=degree_product,
                exact_beyond_degree_product=total-degree_product,
                universal_K64_harris=harris_root,
                physical_two_cut_probability=Fraction(1,4**r),
                exact_path_survival=total/Fraction(4**r),
                harris_degree_path_survival=degree_product/Fraction(4**r),
                harris_K64_path_survival=harris_root/Fraction(4**r),
                global_K64_survival_floor=Fraction(1,4**r*comb(r*(K_ROOT+1),r)))


def exact_subset_priority(nbr, owners, cap=15):
    """Independent complete integer linear-extension DP for small cases."""
    owners=_validate(nbr,owners)
    U=set(owners)
    for o in owners:
        U.update(nbr[o])
    U=tuple(sorted(U))
    if len(U)>cap:
        raise ValueError("cross-check only, not a mathematical cap")
    idx={x:i for i,x in enumerate(U)}
    predecessors=[0]*len(U)
    for o in owners:
        for w in nbr[o]:
            predecessors[idx[w]] |= 1<<idx[o]
    dp={0:1}
    full=(1<<len(U))-1
    for mask in range(full):
        if mask not in dp:
            continue
        for j in range(len(U)):
            if (mask&(1<<j))==0 and (predecessors[j]&mask)==predecessors[j]:
                next_mask=mask|(1<<j)
                dp[next_mask]=dp.get(next_mask,0)+dp[mask]
    return Fraction(dp[full],factorial(len(U)))


def exact_direct_permutations(nbr,owners,cap=8):
    """Third independently defined brute force of all local priorities."""
    owners=_validate(nbr,owners)
    U=set(owners)
    for o in owners:
        U.update(nbr[o])
    U=tuple(sorted(U))
    if len(U)>cap:
        raise ValueError("only small whole-priority brute force")
    n=good=0
    for perm in permutations(U):
        pos={o:i for i,o in enumerate(perm)}
        n+=1
        if all(pos[o]<pos[w] for o in owners for w in nbr[o]):
            good+=1
    return Fraction(good,n)


def _pairs(V):
    a=2
    while comb(a,2)<V: a+=1
    return a,tuple(combinations(range(a),2))[:V]


def genuine_original_model(s,mode):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("finite true symplectic source only s=2 or 4")
    flags=genuine_symplectic_source(s)
    V=(s+1)*(s*s+1)
    a,base=_pairs(V)
    f=base
    if mode=="lex":
        g=base
    elif mode=="reverse":
        g=tuple(reversed(base))
    elif mode=="shift":
        g=base[1:]+base[:1]
    else:
        raise ValueError("unknown globally injected original map")
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("invalid named ORIGINAL flags")
    byp=defaultdict(list)
    byl=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        byp[p].append(i)
        byl[l].append(i)
    nbr=[set() for _ in flags]
    for groups,other,ix in ((byp,g,1),(byl,f,0)):
        for ids in groups.values():
            for i,j in combinations(ids,2):
                if set(other[flags[i][ix]]) & set(other[flags[j][ix]]):
                    nbr[i].add(j)
                    nbr[j].add(i)
    edgeowner={}
    adj=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        x,k=f[p]
        y,z=g[l]
        for u,v in (((x,y),(k,z)),((x,z),(k,y))):
            key=tuple(sorted((u,v)))
            if key in edgeowner:
                raise AssertionError("physical cloned source owner")
            edgeowner[key]=i
            adj[u].add(v)
            adj[v].add(u)
    if len(edgeowner)!=2*len(flags):
        raise AssertionError("one of two ORIGINAL opposite diagonals absent")
    return dict(s=s,V=V,a=a,flags=flags,f=f,g=g,nbr=nbr,
                physical_edgeowner=edgeowner,adj=adj,
                full_source_J_edges=sum(len(v) for v in nbr)//2,
                full_max_J=max(len(v) for v in nbr))


def _proper_paths(model,r,cap):
    """Actual ORIGINAL uncut physical proper 2/3paths; no fake edge graph."""
    adj=model["adj"]
    owner=model["physical_edgeowner"]
    n=0
    for start in sorted(adj):
        stack=[(start,)]
        while stack:
            v=stack.pop()
            if len(v)==r+1:
                ids=tuple(owner[tuple(sorted((v[i],v[i+1])))]
                          for i in range(r))
                if len(set(ids))!=r:
                    raise AssertionError("reused source on proper physical path")
                if any(j in model["nbr"][i] for i,j in combinations(ids,2)):
                    raise AssertionError("source conflict on coordinate-proper path")
                yield v,ids
                n+=1
                if n>=cap:
                    return
                continue
            for w in sorted(adj[v[-1]],reverse=True):
                if all(w[0]!=u[0] and w[1]!=u[1] for u in v):
                    stack.append(v+(w,))


def sample_exact_weighted_jensen(s,mode,r,cap=350):
    """Exact ONE shared-priority marginal path-weight matrix on true source.

    When cap limits the paths, the endpoint P and L matrices are restricted
    to the *same* path sample. This does not purport to exhaust W34 paths.
    """
    model=genuine_original_model(s,mode)
    if r not in (2,3):
        raise ValueError("proper physical 2/3walks only")
    counts=Counter()
    lower=defaultdict(Fraction)
    lower_harris=defaultdict(Fraction)
    p_cache={}
    min_sufficient_gain=Fraction(1)
    improvement=0
    high_b=0
    n=0
    for vertices,owners in _proper_paths(model,r,cap):
        ep=(vertices[0],vertices[-1])
        counts[ep]+=1
        key=tuple(sorted(owners))
        if key not in p_cache:
            p_cache[key]=priority_probability(model["nbr"],key)
        item=p_cache[key]
        p=item["exact_path_survival"]
        lower[ep]+=p
        lower_harris[ep]+=item["harris_degree_path_survival"]
        if item["exact_beyond_sufficient"]>0:
            improvement+=1
        high_b=max(high_b,item["b"])
        n+=1
    if not n:
        raise AssertionError("no proper true source physical paths")
    K=model["full_max_J"]
    global_r_sigma=Fraction(1,4**r*comb(r*(K+1),r))
    root_sigma=Fraction(1,4**r*comb(r*(K_ROOT+1),r))
    mass=sum((v*v for v in counts.values()),0)
    weighted_mass=sum((v*v for v in lower.values()),Fraction(0))
    harris_mass=sum((v*v for v in lower_harris.values()),Fraction(0))
    harris_true_sigma=Fraction(1,4**r*(K+1)**r)
    harris_root_sigma=Fraction(1,4**r*(K_ROOT+1)**r)
    harris_true_mass=harris_true_sigma**2*mass
    harris_root_mass=harris_root_sigma**2*mass
    uniform_mass=global_r_sigma**2*mass
    global_mass=root_sigma**2*mass
    if not (weighted_mass>=harris_mass>=harris_true_mass>=uniform_mass
            and harris_true_mass>=harris_root_mass>=global_mass):
        raise AssertionError("exact source Jensen below NEW Harris bound")
    # A correct expected path matrix needs ONE *global* shared selector;
    # linearity is enough for its per-path exact marginal probability.
    return dict(s=s,mode=mode,r=r,sampled_source_proper_paths=n,
                source_original_flags=len(model["flags"]),
                physical_original_diagonals=2*len(model["flags"]),
                actual_full_source_J_edges=model["full_source_J_edges"],
                max_original_J_degree=K,
                largest_actual_local_neighborhood_b=high_b,
                distinct_true_owner_sets=len(p_cache),
                paths_strict_priority_improvement=improvement,
                endpoint_energy_P_r=mass,
                exact_marginal_weighted_endpoint_energy=str(weighted_mass),
                harris_degree_weighted_endpoint_energy=str(harris_mass),
                harris_uniform_true_K_endpoint_energy=str(harris_true_mass),
                harris_uniform_K64_endpoint_energy=str(harris_root_mass),
                uniform_true_K_endpoint_energy=str(uniform_mass),
                uniform_K64_endpoint_energy=str(global_mass),
                exact_global_K64_lower=str(root_sigma),
                NEW_HARRIS_uniform_K64_lower=str(harris_root_sigma),
                exact_first_r_unconditional_conjunction_not_assumed=True,
                physical_color_cut_r_probability=str(Fraction(1,4**r)),
                actual_exact_priority_marginal_is_shared_global_permutation=True,
                no_joint_path_independence_assumed=True,
                sampled_not_claimed_exhaustive=n==cap)


def abstract_mask_case(r,mask_counts):
    """Scalable exact local probability with full r(K+1) source universe."""
    if r not in (2,3):
        raise ValueError("r=2,3 only")
    nbr=[set() for _ in range(r+sum(mask_counts.values()))]
    k=r
    for mask,m in mask_counts.items():
        if mask<=0 or mask>=(1<<r) or type(m)!=int or m<0:
            raise ValueError("illegal original source conflict mask")
        for _ in range(m):
            for j in range(r):
                if mask&(1<<j):
                    nbr[j].add(k)
                    nbr[k].add(j)
            k+=1
    p=priority_probability(nbr,tuple(range(r)))
    if sum(mask_counts.values())+r <= 12:
        if exact_subset_priority(nbr,tuple(range(r)))!=p["exact"]:
            raise AssertionError("priority integration != independent subset DP")
    return dict(r=r,b=p["b"],mask_counts=tuple(sorted(mask_counts.items())),
                priority=str(p["exact"]),sufficient=str(p["first_r_sufficient"]),
                source_harris_degree_product=str(p["source_degree_product_harris"]),
                full_path_survival=str(p["exact_path_survival"]),
                strict_improvement=p["exact"]>p["first_r_sufficient"],
                exact_above_harris=p["exact"]>=p["source_degree_product_harris"],
                all_h_factorization_exact=True)


def certificate():
    toy=[
        abstract_mask_case(2,{1:1,2:1}),
        abstract_mask_case(2,{3:1}),
        abstract_mask_case(3,{1:2,2:1,4:2,3:1,7:1}),
        abstract_mask_case(3,{7:192}),
        abstract_mask_case(3,{1:64,2:64,4:64}),
        abstract_mask_case(3,{3:64,5:64,6:64}),
    ]
    # The max union has b=3+192=195, without a DP exponential wall.
    assert max(x["b"] for x in toy)==195
    assert any(x["strict_improvement"] for x in toy)
    real=[sample_exact_weighted_jensen(s,mode,r) for s,mode,r in (
        (2,"lex",2),(2,"reverse",3),(4,"lex",2),
        (4,"reverse",3),(4,"shift",3))]
    assert all(Fraction(x["exact_marginal_weighted_endpoint_energy"])>=
               Fraction(x["harris_degree_weighted_endpoint_energy"])>=
               Fraction(x["harris_uniform_true_K_endpoint_energy"])>=
               Fraction(x["uniform_true_K_endpoint_energy"])
               for x in real)
    return dict(schema=SCHEMA,issue=230,parent_pr=770,
                status=ROOT_STATUS,
                root_PROVED_A=False,ASET_exponent_claimed=False,
                all_h_priority_mask_simplex_identity_proved_in_manuscript=True,
                all_h_no_b20_or_exponential_subset_DP_restriction=True,
                all_h_shared_priority_exact_marginal_valid=True,
                all_h_Harris_positive_association_degree_product_PROVED_in_manuscript=True,
                all_h_K64_sharp_reciprocal_q2=16*65**2,
                all_h_K64_sharp_reciprocal_q3=64*65**3,
                all_h_harris_uniform_lower_stronger_than_first_r=True,
                all_h_weighted_endpoint_Jensen_upper_via_selected_moment=True,
                all_h_NO_path_independence_assumed=True,
                all_h_original_C6_to_D6_and_GLOBAL_moment_dependencies_remain_open=True,
                abstract_real_source_conflict_mask_cases=toy,
                genuine_original_W32_W34_weighted_marginal_cases=real)


if __name__=="__main__":
    print("AA4_LOW_MOMENT_EXACT_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
