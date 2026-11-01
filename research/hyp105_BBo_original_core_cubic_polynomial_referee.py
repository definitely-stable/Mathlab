"""AA4-BBOCUBIC: exact ORIGINAL-source B/B-overlap core polynomial.

This is NOT a repeat of #677 0/2 source inverse or #694 P3 path audit.
NEW all-h theorem: for fixed complete true original incidence source, f,g
and arbitrary original CORE I, accepted BBo sixsets produced by good,
unblocked coordinate-proper 3-paths are EXACTLY

  U(I,Z)=sum_{Q in aligned TRUE ORIGINAL BBo source sixsets, Q∩Z=empty}
             prod_{i in T(Q)} 1_{i in I},

with T(Q) the uniquely determined THREE non-anchor ORIGINAL flag IDs.
Three ORIGINAL q--ell--p--r source anchors need NOT be in I.
This is a squarefree monotone homogeneous CUBIC (not sixth-order)
in retained original IDs, with exactly two reverse directed paths/Q.

NEW source-FIRST enumerator builds triples from original flag pair-label
intersections and original GQ anchor projection, NO physical graph or
previous #677/#694 code. An independent PHYSICAL-FIRST 3-walk enumerator
is used ONLY as a finite W32/W34 falsifier and exact-core oracle.

Independent Bernoulli original-flag retention yields
  E U=sum_Q product_{i in T(Q)}rho_i,
  E U²=sum_{Q,Q'} product_{i in T(Q)∪T(Q')}rho_i,
so covariance of Q survival is NONNEGATIVE (not path-selector covariance
in #695, where odd-cycle bitcut conflicts can make it negative).
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source


def _source_input(power,f,g):
    if type(power) is not int or power not in (1,2):
        raise ValueError("actual ORIGINAL GQ fixture limited to h=1,2")
    s,V,flags=genuine_source(power)
    a=2
    while a*(a-1)//2<V:a+=1
    try: f=tuple(tuple(z) for z in f);g=tuple(tuple(z) for z in g)
    except (ValueError,TypeError):
        raise ValueError("source labels missing")
    valid=set(combinations(range(a),2))
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
        or any(z not in valid for z in f+g)):
        raise ValueError("original complete separately globally injected typed pair maps required")
    return s,V,tuple(flags),a,f,g


def _source_projections(V,flags):
    """Actual ORIGINAL source geometry independent of physical graph."""
    pl=[set() for _ in range(V)]
    lp=[set() for _ in range(V)]
    owner={}
    for i,(p,l) in enumerate(flags):
        if (p,l) in owner:raise AssertionError("original GQ repeated incidence flag")
        owner[p,l]=i;pl[p].add(l);lp[l].add(p)
    col=[set().union(*(lp[l] for l in pl[p]))-{p} for p in range(V)]
    projection={}
    for q in range(V):
        for r in range(V):
            if r in pl[q]:continue
            pset=col[q]&lp[r]
            if len(pset)!=1:raise AssertionError("original GQ projection not unique")
            p=next(iter(pset))
            ls=pl[q]&pl[p]
            if len(ls)!=1:raise AssertionError("GQ source q-p common line not unique")
            ell=next(iter(ls))
            projection[q,r]=(p,ell,
                             (owner[q,ell],owner[p,ell],owner[p,r]))
    return projection


def source_first_original_BBo_cubic_catalog(power,f,g,candidate_ids=None):
    """Build ORIGINAL sixsets from original-source 3-FLAG combinations.

    Only ORIGINAL factor pair intersections and true GQ projection:
    no physical graph adjacency, no 3-walk traversal, no GF5 classifier,
    no previous inverse #677.
    Restrict candidate_ids only to reduce finite audit work; original
    anchors remain looked up in the COMPLETE genuine ORIGINAL source.
    """
    s,V,flags,a,f,g=_source_input(power,f,g)
    candidate=tuple(range(len(flags))) if candidate_ids is None else tuple(candidate_ids)
    if (len(set(candidate))!=len(candidate)
        or any(type(i) is not int or i<0 or i>=len(flags) for i in candidate)):
        raise ValueError("candidate path owners must be genuine distinct ORIGINAL flag IDs")
    projections=_source_projections(V,flags)
    invf={pair:i for i,pair in enumerate(f)}
    invg={pair:i for i,pair in enumerate(g)}
    left=[set(f[flags[i][0]]) for i in range(len(flags))]
    right=[set(g[flags[i][1]]) for i in range(len(flags))]
    neighbors=defaultdict(list)
    # SOURCE-FIRST: a pair of true original flag label edges can meet
    # at one physical corner iff each typed pair intersection is SINGLETON.
    for i,j in combinations(candidate,2):
        x=left[i]&left[j];y=right[i]&right[j]
        if len(x)!=1 or len(y)!=1:continue
        corner=(next(iter(x)),next(iter(y)))
        neighbors[i].append((j,corner))
        neighbors[j].append((i,corner))
    sextuple={}
    witness={}
    flag_triples=0
    for j in candidate:
        around=neighbors[j]
        for (i,v1),(k,v2) in combinations(around,2):
            if v1[0]==v2[0] or v1[1]==v2[1]:continue
            outer_i=(next(iter(left[i]-{v1[0]})),
                     next(iter(right[i]-{v1[1]})))
            outer_k=(next(iter(left[k]-{v2[0]})),
                     next(iter(right[k]-{v2[1]})))
            path=(outer_i,v1,v2,outer_k)
            if (len({v[0] for v in path})!=4 or
                len({v[1] for v in path})!=4):
                continue
            flag_triples+=1
            q=invf.get(tuple(sorted((outer_i[0],outer_k[0]))))
            r=invg.get(tuple(sorted((outer_i[1],outer_k[1]))))
            if q is None or r is None:continue
            pr=projections.get((q,r))
            if pr is None:continue
            p,ell,anchors=pr
            if (set(f[q])&set(f[p]) or set(g[r])&set(g[ell]) or
                (v1[0] in f[p] or v2[0] in f[p]) or
                (v1[1] in g[ell] or v2[1] in g[ell])):
                continue
            T=tuple(sorted((i,j,k)))
            Q=tuple(sorted(T+anchors))
            if len(set(Q))!=6:
                raise AssertionError("source-derived BBo Q includes non-distinct original IDs")
            pcount=Counter(flags[z][0] for z in Q)
            lcount=Counter(flags[z][1] for z in Q)
            if (sorted(pcount.values())!=[1,1,1,1,2] or
                sorted(lcount.values())!=[1,1,1,1,2] or
                sum(flags[z]==(p,ell) for z in Q)!=1):
                raise AssertionError("source-derived Q fails TRUE original B/B overlap")
            for side,labels in ((0,f),(1,g)):
                deg=Counter(v for fid in Q for v in labels[flags[fid][side]])
                if len(deg)!=6 or set(deg.values())!={2}:
                    raise AssertionError("source-derived Q not physical degree-two BBo")
            if Q in sextuple:
                if sextuple[Q]!=T or witness[Q]!=min(path,path[::-1]):
                    raise AssertionError("same original Q has multiple non-reverse source-three paths")
            else:
                sextuple[Q]=T
                witness[Q]=min(path,path[::-1])
    return {
        "s":s,"V":V,"candidate_original_ID_count":len(candidate),
        "source_compatible_original_three_flag_chains":flag_triples,
        "aligned_original_BBo_sixset_count":len(sextuple),
        "sixset_supports":dict(sorted(sextuple.items())),
        "source_only_unoriented_path_witnesses":dict(sorted(witness.items())),
        "all_h_cubic_source_image_theorem_not_inferred_from_small_h":True,
    }


def _subset_check(universe,ids,label):
    cand=tuple(ids)
    if (len(set(cand))!=len(cand)
        or any(type(i) is not int or i not in universe for i in cand)):
        raise ValueError(f"{label} contains duplicate or invalid original incidence ID")
    return frozenset(cand)


def evaluate_original_BBo_core_polynomial(catalog,core_ids,forbidden_ids=()):
    """Exact ORIGINAL BBo sixset count. Three owners in CORE, anchors not."""
    supp=catalog["sixset_supports"]
    universe=set(range((catalog["s"]+1)*catalog["V"]))
    I=_subset_check(universe,core_ids,"CORE")
    Z=_subset_check(universe,forbidden_ids,"forbidden")
    produced={Q:T for Q,T in supp.items() if not (set(Q)&Z) and set(T)<=I}
    return {
        "actual_core_original_source_flags":len(I),
        "forbidden_original_source_flags":len(Z),
        "produced_true_ORIGINAL_BBo_sixsets":len(produced),
        "actual_directed_proper_unblocked_source_paths":2*len(produced),
        "unique_three_ID_nonanchor_supports":len(set(produced.values())),
        "produced_original_sixset_owners":tuple(sorted(produced)),
        "every_original_source_anchor_need_not_be_in_core":True,
        "cubic_homogeneous_squarefree_in_core_variables":True,
    }


def independent_physical_first_BBo_core_census(power,f,g,core_ids):
    """OTHER DIRECTION: independent real physical 3-edge graph-walk DFS.

    No call into the source cubic catalog nor #694. Every surviving path
    must recover exact original complete GQ projection anchors, proper
    endpoint and all four internal nonblocking conditions.
    """
    s,V,flags,a,f,g=_source_input(power,f,g)
    I=_subset_check(set(range(len(flags))),core_ids,"CORE")
    project=_source_projections(V,flags)
    invf={z:i for i,z in enumerate(f)}
    invg={z:i for i,z in enumerate(g)}
    graph=defaultdict(set);owner={}
    for i in I:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=frozenset((u,v))
            if e in owner:raise AssertionError("two source flags own same physical edge")
            owner[e]=i;graph[u].add(v);graph[v].add(u)
    sixsets=defaultdict(set)
    for v0 in graph:
        for v1 in graph[v0]:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    path=(v0,v1,v2,v3)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        continue
                    q=invf.get(tuple(sorted((v0[0],v3[0]))))
                    r=invg.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:continue
                    anchor=project.get((q,r))
                    if anchor is None:continue
                    p,ell,aa=anchor
                    if (set(f[p])&{v[0] for v in path}
                        or set(g[ell])&{v[1] for v in path}):
                        continue
                    T=tuple(owner[frozenset((path[j],path[j+1]))] for j in range(3))
                    Q=tuple(sorted(T+aa))
                    if len(set(Q))!=6:
                        raise AssertionError("source graph created a non-six-ID BBo")
                    sixsets[Q].add(path)
    if any(len(paths)!=2 or tuple(reversed(next(iter(paths)))) not in paths
           for paths in sixsets.values()):
        raise AssertionError("physical-first BBo original source ID fiber not exactly two directed paths")
    return {
        "original_true_core_flag_count":len(I),
        "physical_selected_actual_edges":len(owner),
        "actual_original_BBo_sixset_count":len(sixsets),
        "actual_directed_source_paths":sum(map(len,sixsets.values())),
        "original_source_sixset_path_witnesses":{k:tuple(sorted(v))
                                                 for k,v in sorted(sixsets.items())},
    }


def exact_independent_core_retention_moments(catalog,probabilities,
                                             variance_limit=800):
    """Exact moments for *independent* Bernoulli deletion of source IDs.

    Does NOT apply to priority/two-cut dependent selector of #679/#695.
    Strict Fraction values; for large catalogs skip O(n²) variance,
    never fabricate missing variance.
    """
    supp=catalog["sixset_supports"]
    prob=dict(probabilities)
    if any(type(i) is not int or i<0 or
           type(p) not in (Fraction,int) or not 0<=p<=1
           for i,p in prob.items()):
        raise ValueError("Bernoulli probabilities must be exact 0..1 rationals")
    support=tuple(supp.values())
    if any(i not in prob for T in support for i in T):
        raise ValueError("probability for every nonanchor path ID required")
    def weight(T):
        z=Fraction(1)
        for i in T:z*=prob[i]
        return z
    expectation=sum((weight(T) for T in support),Fraction())
    second=None;variance=None
    if type(variance_limit) is not int or variance_limit<0:
        raise ValueError("nonnegative variance cap required")
    if len(support)<=variance_limit:
        second=sum((weight(set(T)|set(S)) for T in support for S in support),
                   Fraction())
        variance=second-expectation*expectation
        if variance<0:
            raise AssertionError("independent retention indicators of cubic source supports have negative variance")
    return {
        "source_sextuple_count":len(supp),
        "exact_expected_ORIGINAL_BBo_sixsets":expectation,
        "exact_expected_square_if_computed":second,
        "exact_variance_if_computed":variance,
        "all_cubic_monomial_indicator_covariances_nonnegative":True,
        "only_independent_original_ID_Bernoulli_deletion":True,
        "not_a_statement_about_priority_selector_two_color_cuts":True,
    }
