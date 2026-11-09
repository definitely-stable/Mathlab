"""AA4-PAIRRANK: TRUE ORIGINAL W(3,s) joint-priority/two-cut exact covariance referee.

Mathematical all-order result, for any two coordinate-proper directed 3paths
on true source-owned physical CORE (possibly same path):
  P(both selected) = PRIORITY(union original owners) * COLOR_f(S) * COLOR_g(S).
PRIORITY(S)=0 if S contains a genuine J conflict. Otherwise it is a finite
permutation sum with at most |S|! terms, even if the total original source
or each neighborhood is enormous. The global source priorities are SHARED
between paths, as are the first and second physical symbol cuts.

For a fixed order pi of distinct original owners S (earliest to latest),
c_j counts outside neighbors whose LATEST owner-neighbor under pi is pi[j].
Then the probability all S beat their actual original J neighbors is exactly:
  sum_{pi} product_{j=0}^{k-1} 1 / ((k-j) + sum_{t=j}^{k-1} c_t).
Factor independence is ONLY between one priority experiment and the TWO
typed physical symbol binary cuts, NOT between two path survival events.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-selector-exact-pair-covariance.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K_PROOF=64


def true_source(s,scheme="lex",core="full"):
    if type(s) is not int or s not in (2,4):
        raise ValueError("Only true original W(3,2) and W(3,4) finite GQ tests")
    V=(s+1)*(s*s+1)
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    a=2
    while comb(a,2)<V:a+=1
    pairs=list(combinations(range(a),2))
    f=pairs[:V]
    g=pairs[:V]
    if scheme=="reverse":
        g=g[::-1]
    elif scheme=="shift":
        f=f[3:]+f[:3]
        g=g[7:]+g[:7]
    elif scheme!="lex":
        raise ValueError("Only globally pair-injective fixed correlations")
    if core=="full":
        C=tuple(range(len(flags)))
    elif core=="even":
        C=tuple(range(0,len(flags),2))
    elif core=="sparse":
        C=tuple(i for i in range(len(flags)) if i%5 in (0,2,3))
    else:
        raise ValueError("Original core must retain both physical diagonals")
    assert len(flags)==(s+1)*V and len(f)==len(g)==V
    assert len(set(f))==V and len(set(g))==V
    J=[set() for _ in flags]
    pencilP=defaultdict(list)
    pencilL=defaultdict(list)
    for i in C:
        p,l=flags[i]
        pencilP[p].append(i)
        pencilL[l].append(i)
    for pencil,other in ((pencilP,g),(pencilL,f)):
        for ids in pencil.values():
            for i,j in combinations(ids,2):
                p1,l1=flags[i]
                p2,l2=flags[j]
                pa=other[l1 if pencil is pencilP else p1]
                pb=other[l2 if pencil is pencilP else p2]
                if set(pa)&set(pb):
                    J[i].add(j)
                    J[j].add(i)
    physical_owner={}
    adj=defaultdict(set)
    for i in C:
        p,l=flags[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e=tuple(sorted((u,v)))
            if e in physical_owner:
                raise AssertionError("physical edge has duplicate original owner")
            physical_owner[e]=i
            adj[u].add(v)
            adj[v].add(u)
    if len(physical_owner)!=2*len(C):
        raise AssertionError("TRUE original flag lost a REAL physical diagonal")
    dmax=max((len(J[i]) for i in C),default=0)
    if dmax>K_PROOF:
        raise AssertionError("finite source violates K64 low prerequisite")
    return {"s":s,"V":V,"a":a,"flags":flags,"f":tuple(f),"g":tuple(g),
            "C":C,"J":J,"adj":adj,"physical_owner":physical_owner,
            "source_max_conflict_degree":dmax}


def original_proper_paths(c,max_paths=None):
    """Enumerate TRUE directed physical proper 3walks, no historical path import."""
    adj=c["adj"]
    owner=c["physical_owner"]
    out=[]
    for v0 in sorted(adj):
        for v1 in sorted(adj[v0]):
            for v2 in sorted(adj[v1]):
                if (v2[0] in (v0[0],v1[0]) or
                    v2[1] in (v0[1],v1[1])):
                    continue
                for v3 in sorted(adj[v2]):
                    vs=(v0,v1,v2,v3)
                    if len(set(v[0] for v in vs))!=4 or len(set(v[1] for v in vs))!=4:
                        continue
                    os=tuple(owner[tuple(sorted((vs[j],vs[j+1])))] for j in range(3))
                    if len(set(os))!=3 or any(j in c["J"][i] for i,j in combinations(os,2)):
                        raise AssertionError("proper physical path source owners not conflict-free")
                    out.append((vs,os))
                    if max_paths is not None and len(out)>=max_paths:
                        return out
    return out


def _priority_formula_uncached(owners,J):
    S=tuple(sorted(set(owners)))
    if not S:
        return Fraction(1)
    if any(j in J[i] for i,j in combinations(S,2)):
        return Fraction(0)
    outside=set().union(*(J[i] for i in S)) - set(S)
    touched={i:tuple(o for o in S if i in J[o]) for i in sorted(outside)}
    if any(not ns for ns in touched.values()):
        raise AssertionError("neighbor without owner")
    k=len(S)
    total=Fraction(0)
    for order in permutations(S):
        pos={o:j for j,o in enumerate(order)}
        c=[0]*k
        for nbrs in touched.values():
            c[max(pos[o] for o in nbrs)]+=1
        denom=1
        tail=0
        for j in range(k-1,-1,-1):
            tail+=1+c[j]
            denom*=tail
        total+=Fraction(1,denom)
    if not 0<total<=1:
        raise AssertionError("exact true ORIGINAL rank integral out of range")
    return total


def _typed_cut_exact(owners,c,side):
    """2^(components-number_of_used_symbols), or 0 on an ODD cycle."""
    f_or_g=c["f"] if side=="point" else c["g"]
    ij=0 if side=="point" else 1
    edges={tuple(f_or_g[c["flags"][i][ij]]) for i in owners}
    graph=defaultdict(set)
    for a,b in edges:
        if a==b:raise AssertionError("original injected factor pair loop")
        graph[a].add(b)
        graph[b].add(a)
    coloring={}
    comps=0
    for start in graph:
        if start in coloring:continue
        comps+=1
        coloring[start]=0
        stack=[start]
        while stack:
            x=stack.pop()
            for y in graph[x]:
                if y not in coloring:
                    coloring[y]=1-coloring[x]
                    stack.append(y)
                elif coloring[y]==coloring[x]:
                    return Fraction(0)
    return Fraction(1,2**(len(graph)-comps))


def exact_joint(owners,c):
    S=tuple(sorted(set(owners)))
    priority=_priority_formula_uncached(S,c["J"])
    if not priority:
        return Fraction(0)
    return priority*_typed_cut_exact(S,c,"point")*_typed_cut_exact(S,c,"line")


def exact_cut_bruteforce(S,c,side):
    f_or_g=c["f"] if side=="point" else c["g"]
    ij=0 if side=="point" else 1
    pairs={tuple(f_or_g[c["flags"][i][ij]]) for i in S}
    used=sorted(set(x for e in pairs for x in e))
    if len(used)>14:raise ValueError("bruteforce color oracle limited to 14 symbols")
    good=0
    for assignment in product((0,1),repeat=len(used)):
        d=dict(zip(used,assignment))
        if all(d[x]!=d[y] for x,y in pairs):
            good+=1
    return Fraction(good,2**len(used))


def exact_priority_subset_dp(owners,J,max_nodes=17):
    """INDEPENDENT ordinal-linear-extension bitmask oracle, no integral/permutations."""
    S=tuple(sorted(set(owners)))
    if any(j in J[i] for i,j in combinations(S,2)):return Fraction(0)
    U=set(S)
    for o in S:U.update(J[o])
    U=tuple(sorted(U))
    if len(U)>max_nodes:
        raise ValueError("local closed source neighborhood too large for independent DP")
    idx={o:j for j,o in enumerate(U)}
    predicates=[0]*len(U)
    for i in S:
        for x in J[i]:
            predicates[idx[x]]|=1<<idx[i]
    @lru_cache(None)
    def count(mask):
        if mask==(1<<len(U))-1:
            return 1
        s=0
        for j in range(len(U)):
            if not (mask>>j)&1 and (predicates[j]&mask)==predicates[j]:
                s+=count(mask|(1<<j))
        return s
    return Fraction(count(0),factorial(len(U)))


def _cut_priority_realization(c,priority,cutf,cutg):
    """Real actual selector for one globally shared priority and two typed cuts."""
    picked=set()
    for i in c["C"]:
        p,l=c["flags"][i]
        if (all(priority[i]<priority[j] for j in c["J"][i])
            and cutf[c["f"][p][0]]!=cutf[c["f"][p][1]]
            and cutg[c["g"][l][0]]!=cutg[c["g"][l][1]]):
            picked.add(i)
    return picked


def exact_pair_referee(p1,p2,c,bruteforce=False):
    os1=p1[1];os2=p2[1]
    a=exact_joint(os1,c)
    b=exact_joint(os2,c)
    both=exact_joint(os1+os2,c)
    cov=both-a*b
    S=tuple(sorted(set(os1+os2)))
    if bruteforce:
        lhs=_priority_formula_uncached(S,c["J"])
        rhs=exact_priority_subset_dp(S,c["J"])
        if lhs!=rhs:raise AssertionError("integral joint source priority vs independent poset DP")
        for side in ("point","line"):
            if _typed_cut_exact(S,c,side)!=exact_cut_bruteforce(S,c,side):
                raise AssertionError("independent exhaustive cut mismatched exact bipartite components")
    return {"p1":a,"p2":b,"joint":both,"cov":cov,
            "same_owners":set(os1)==set(os2),
            "shared_original_owners":len(set(os1)&set(os2)),
            "source_conflict_pair":any(j in c["J"][i] for i,j in
                combinations(S,2)),
            "point_cut":_typed_cut_exact(S,c,"point"),
            "line_cut":_typed_cut_exact(S,c,"line"),
            "source_priority":_priority_formula_uncached(S,c["J"])}


def _fraction_float(q):
    return round(float(q),12)


def _pair_summary(x,y,stat):
    return {"physical_path1":[list(v) for v in x[0]],
            "physical_path2":[list(v) for v in y[0]],
            "original_ID_owners1":list(x[1]),
            "original_ID_owners2":list(y[1]),
            "marginal1":str(stat["p1"]),
            "marginal2":str(stat["p2"]),
            "joint":str(stat["joint"]),
            "covariance":str(stat["cov"]),
            "shared_original_owners":stat["shared_original_owners"],
            "source_conflict":stat["source_conflict_pair"],
            "point_cut":str(stat["point_cut"]),
            "line_cut":str(stat["line_cut"]),
            "source_priority":str(stat["source_priority"])}


def find_original_covariance_witnesses(paths,c,search_cap=180):
    """Find source-grounded + and - distinct-path examples, prioritized shared endpoints."""
    pool=paths[:search_cap]
    found={}
    by_end=defaultdict(list)
    for x in pool:
        by_end[(x[0][0],x[0][-1])].append(x)
    candidates=[]
    for arr in by_end.values():
        candidates.extend(combinations(arr[:15],2))
    # Later add general overlapping path pairs, important negative scope.
    candidates.extend(combinations(pool[:95],2))
    for x,y in candidates:
        if x==y:continue
        k=(x[1],y[1])
        # Same physical path reversed is permitted as distinct directed path.
        r=exact_pair_referee(x,y,c)
        if r["cov"]>0 and "positive" not in found:
            found["positive"]=_pair_summary(x,y,r)
        if r["cov"]<0 and "negative" not in found:
            found["negative"]=_pair_summary(x,y,r)
        if r["joint"]==0 and r["p1"]>0 and r["p2"]>0 and "zero_joint" not in found:
            found["zero_joint"]=_pair_summary(x,y,r)
        if ("positive" in found and "negative" in found and
            "zero_joint" in found):
            break
    if "positive" not in found or "negative" not in found:
        raise AssertionError("failed to find actual ORIGINAL positive and negative covariance")
    return found


def exact_endpoint_moments(paths,c,hard_limit=100000):
    """All endpoint bins, exact E||X||² and ||EX||² with fully correlated selection."""
    byend=defaultdict(list)
    for physical,os in paths:
        byend[physical[0],physical[-1]].append(os)
    joint_cache={}
    P_cache={}
    expectation_norm2=Fraction(0)
    selected_second=Fraction(0)
    pair_occurrences=0
    one_sum=Fraction(0)
    covariance_by_overlap={"shared_original_owner":Fraction(0),
                           "disjoint_original_owners":Fraction(0)}
    covariance_signs=Counter()
    zero_joint_reasons=Counter()
    total_covariance=Fraction(0)
    for endpoint in sorted(byend):
        arr=byend[endpoint]
        freq=Counter(tuple(sorted(os)) for os in arr)
        for os in freq:
            if os not in P_cache:
                P_cache[os]=exact_joint(os,c)
        mean=sum((mult*P_cache[os] for os,mult in freq.items()),Fraction(0))
        expectation_norm2+=mean*mean
        one_sum+=mean
        ss=list(freq.items())
        for i,(a,na) in enumerate(ss):
            for b,nb in ss[i:]:
                n=na*nb*(1 if a==b else 2)
                pair_occurrences+=n
                if pair_occurrences>hard_limit:
                    raise ValueError("exact full tensor too large for bounded CI")
                owners=tuple(sorted(set(a)|set(b)))
                if owners not in joint_cache:
                    joint_cache[owners]=exact_joint(owners,c)
                joint=joint_cache[owners]
                selected_second+=n*joint
                covariance=joint-P_cache[a]*P_cache[b]
                total_covariance+=n*covariance
                overlap="shared_original_owner" if set(a)&set(b) else "disjoint_original_owners"
                covariance_by_overlap[overlap]+=n*covariance
                sign=("positive" if covariance>0 else
                      "negative" if covariance<0 else "zero")
                covariance_signs[sign]+=n
                if not joint:
                    if any(j in c["J"][i] for i,j in combinations(owners,2)):
                        zero_joint_reasons["original_source_J_conflict"]+=n
                    elif not _typed_cut_exact(owners,c,"point"):
                        zero_joint_reasons["original_point_label_odd_cycle"]+=n
                    elif not _typed_cut_exact(owners,c,"line"):
                        zero_joint_reasons["original_line_label_odd_cycle"]+=n
                    else:
                        raise AssertionError("positive exact priority/cuts gave zero joint")
    proper2=sum(len(a)**2 for a in byend.values())
    if pair_occurrences!=proper2:
        raise AssertionError("full endpoint pair multiplicities not conserved")
    if total_covariance!=selected_second-expectation_norm2:
        raise AssertionError("exact ALL ORIGINAL endpoint pair covariances fail variance identity")
    if sum(covariance_by_overlap.values())!=total_covariance:
        raise AssertionError("source-owner overlap covariance ledger does not close")
    if sum(covariance_signs.values())!=pair_occurrences:
        raise AssertionError("positive/negative/zero covariance pair partition fails")
    if selected_second<expectation_norm2:
        raise AssertionError("Jensen violated on ORIGINAL exact selection")
    if not selected_second<=proper2:
        raise AssertionError("selected second moment cannot exceed full paths squared")
    if not 0<=one_sum<=len(paths):
        raise AssertionError("impossible proper physical expected path count")
    return {"proper_directed_P3":len(paths),"unique_ordered_endpoints":len(byend),
            "actual_full_P3_frobenius2":proper2,
            "exact_ordered_physical_path_pairs":pair_occurrences,
            "exact_jensen_mean_norm2":str(expectation_norm2),
            "exact_selected_second_moment":str(selected_second),
            "exact_variance_sum":str(selected_second-expectation_norm2),
            "exact_all_pairwise_covariances_sum":str(total_covariance),
            "ordered_path_pair_covariance_sign_counts":dict(covariance_signs),
            "ordered_path_pair_zero_joint_causes":dict(zero_joint_reasons),
            "exact_covariance_by_shared_source_owner":{
                key:str(value) for key,value in covariance_by_overlap.items()},
            "exact_mean_total_path_count":str(one_sum),
            "second_over_jensen_ratio":str(selected_second/expectation_norm2)
               if expectation_norm2 else "undefined",
            "source_owner_union_probabilities_cached":len(joint_cache),
            "exact_priority_and_coloring_no_path_independence":True}


def canonical_report():
    baseline=true_source(2,"lex","full")
    proper=original_proper_paths(baseline)
    # Full true-original W32 endpoint tensor, not arbitrary 50-path sample.
    full=exact_endpoint_moments(proper,baseline)
    witnesses=find_original_covariance_witnesses(proper,baseline)
    for key in ("positive","negative","zero_joint"):
        if key in witnesses:
            x=witnesses[key]
            owners=tuple(x["original_ID_owners1"]+x["original_ID_owners2"])
            if (_priority_formula_uncached(owners,baseline["J"])!=
                exact_priority_subset_dp(owners,baseline["J"],max_nodes=22)):
                raise AssertionError("independent full original source ordinal oracle")
            for side in ("point","line"):
                if _typed_cut_exact(owners,baseline,side)!=exact_cut_bruteforce(owners,baseline,side):
                    raise AssertionError("exhaustive actual two-factor bits differ")
    cases=[]
    for s,scheme,core,cap in (
        (2,"lex","full",None),
        (2,"reverse","full",None),
        (2,"shift","even",None),
        (4,"lex","even",160),
        (4,"reverse","even",160),
        (4,"shift","sparse",160),
    ):
        c=true_source(s,scheme,core)
        paths=original_proper_paths(c,max_paths=cap)
        if not paths:
            raise AssertionError("true ORIGINAL source sample empty")
        for path,os in paths[:12]:
            if exact_joint(os,c)<=0:
                raise AssertionError("genuine original proper path has zero marginal")
            if (c["source_max_conflict_degree"]<=K_PROOF and
                exact_joint(os,c)<Fraction(1,64*comb(3*(K_PROOF+1),3))):
                raise AssertionError("published all-h source selector floor violated")
        cases.append({"s":s,"scheme":scheme,"core":core,
            "flags":len(c["flags"]),"retained_original_CORE_flags":len(c["C"]),
            "original_pair_alphabet_size":c["a"],
            "actual_physical_paired_diagonal_edges":len(c["physical_owner"]),
            "actual_source_J_max_degree":c["source_max_conflict_degree"],
            "complete_real_source_proper_directed_3paths":len(paths) if cap is None else None,
            "deterministic_sampled_proper_directed_3paths":len(paths)})
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,
        "finite_actual_original_W32_lex_full_second_moment":full,
        "actual_original_both_sign_covariance_witnesses":witnesses,
        "true_original_source_cases":cases,
        "all_h_joint_priority_integral_formula_claimed":True,
        "all_h_two_color_bipartite_formula_claimed":True,
        "all_h_new_branch_A_exponent_claimed":False,
        "old_independence_of_paths_assumed":False}


if __name__=="__main__":
    print("AA4_PAIRRANK_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
