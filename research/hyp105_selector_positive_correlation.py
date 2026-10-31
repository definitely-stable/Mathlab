"""HYP-105 AA4-SELPLUS: exact LOCAL-MINIMUM selector law and 4x/27x gains.

For ANY finite source conflict graph, pairwise NONCONFLICTING target
ORIGINAL flag IDs T of size r=2 or 3 (or any positive r), assign i.i.d.
continuous uniform priorities U_i. The original #672 selector retains a
flag if its priority is strictly less than every conflict neighbor's.

Given the target priority vector t_i, its exact joint survival is
    PROD_(w in N(T)\\T) (1 - MAX_(i in N(w)∩T) t_i).

Since 1-MAX(t_i) = MIN_i (1-t_i) >= PROD_i (1-t_i), integration gives
    Pr(T all selected) >= PROD_(i in T) [1/(deg(i)+1)]
                        >= (K+1)^(-r).
Overlapping original neighborhoods cause POSITIVE, not destructive,
dependence for this nonconflicting local-minimum event.

When the selected ORIGINAL flags are those of a coordinate-proper
physical r-path, independent uniform binary colors of physical
coordinates retain both diagonals of all r flags iff each of the r
left and r right consecutive pair edges is bichromatic. Each physical
coordinate sequence has r+1 distinct symbols, so this occurs with
probability exactly 4^(-r).

Thus every fixed proper original-source 2-path survives with
    sigma2_new = 1/[16 (K+1)^2]    (4x #672 sigma2),
and every fixed proper original-source 3-path survives with
    sigma3_new = 1/[64 (K+1)^3]    (27x #672 sigma3).
No path-to-path independence or random f,g is assumed.

An EXACT rational finite-graph joint probability uses r! permutations
of the TARGET priority ordering. For each order pi, let n_j be the
number of OTHER conflict-neighbor vertices whose LATEST target among
their neighbors is pi[j]. Integrating on the simplex
    0<t_pi[0]<...<t_pi[r-1]<1
gives precisely
    PROD_(j=0..r-1) 1/[SUM_(k=j..r-1) (n_k+1)].
This also handles arbitrarily overlapping target neighborhoods.

All math holds for ANY finite graph. The application to original
W(3,2^h) uses the EXACT source conflict graph and actual ORIGINAL
flags with global pair-injective correlated f,g; its path tests
never claim to prove the all-h core selection by finite extrapolation.
"""
from fractions import Fraction
from itertools import permutations


def exact_joint_local_minimum_probability(conflict, target):
    """EXACT Fraction, no factorial enumeration of all conflict vertices.

    Original target vertex IDs must be mutually nonadjacent. The
    complete undirected source conflict graph must include all vertex
    entries. Works for any r>=1, efficient in r! and neighborhood size.
    """
    T=tuple(target)
    if not T or len(set(T))!=len(T) or any(t not in conflict for t in T):
        raise ValueError("target ORIGINAL flag IDs must be distinct and present")
    nodes=set(conflict)
    for v,ns in conflict.items():
        if v in ns or not set(ns)<=nodes or any(v not in conflict[w] for w in ns):
            raise ValueError("source conflict graph must be undirected, simple, complete")
    chosen=set(T)
    if any(chosen.intersection(conflict[t]) for t in T):
        raise ValueError("target ORIGINAL flags must be pairwise conflict-free")
    neighbors=set().union(*(set(conflict[t]) for t in T))
    answer=Fraction(0)
    for ordered in permutations(T):
        rank={v:i for i,v in enumerate(ordered)}
        n=[0]*len(T)
        for w in neighbors:
            last=max(rank[v] for v in conflict[w] if v in chosen)
            n[last]+=1
        suffix=0
        integral=Fraction(1)
        for j in range(len(T)-1,-1,-1):
            suffix+=n[j]+1
            integral/=suffix
        answer+=integral
    independent=Fraction(1)
    for v in T:
        independent/=len(conflict[v])+1
    if not independent<=answer<=1:
        raise AssertionError("positive association of local minima violated")
    return answer


def local_minimum_lower_probability(conflict, target):
    """Exact FKG-style product lower, with NO independence assumption."""
    T=tuple(target)
    if not T or len(set(T))!=len(T) or any(t not in conflict for t in T):
        raise ValueError("distinct existing source flags required")
    if any(set(T)&set(conflict[t]) for t in T):
        raise ValueError("source path target flags must be pairwise nonconflicting")
    out=Fraction(1)
    for t in T:out/=len(conflict[t])+1
    return out


def improved_path_selector_sigma(K):
    """SAME #672 random selector, provably stronger all-h fixed-K bounds.

    The exact local-minima product proof is independent of dyadic h.
    Only original core maximum CONFLICT degree K enters the floors.
    """
    if type(K) is not int or K<0:
        raise ValueError("original source conflict maximum degree is >=0 integer")
    d=K+1
    old2=Fraction(1,64*d*d)
    old3=Fraction(1,64*27*d**3)
    new2=Fraction(1,16*d*d)
    new3=Fraction(1,64*d**3)
    if new2/old2!=4 or new3/old3!=27:
        raise AssertionError("selector probability gain wrong")
    return {
        "K":K,
        "old_sigma2":old2,
        "new_sigma2":new2,
        "old_sigma3":old3,
        "new_sigma3":new3,
        "sigma2_new_over_old":new2/old2,
        "sigma3_new_over_old":new3/old3,
        "proper_P2_Frobenius_squared_coefficient_old":
            1/(old2*old2),
        "proper_P2_Frobenius_squared_coefficient_new":
            1/(new2*new2),
        "proper_P3_Frobenius_squared_coefficient_old":
            1/(old3*old3),
        "proper_P3_Frobenius_squared_coefficient_new":
            1/(new3*new3),
        "new_P2_Frobenius_upper_gain":16,
        "new_P3_Frobenius_upper_gain":729,
        "selector_requires_original_flag_independent_targets":True,
        "physical_color_cut_probability_two_typed_halves_r2":
            Fraction(1,4**2),
        "physical_color_cut_probability_two_typed_halves_r3":
            Fraction(1,4**3),
        "root_branch_A_full_proof_independent":False,
        "external_scientific_referee_not_supplied":True,
    }


def genuine_original_path_selector_probabilities(power,f,g,core_ids=None,
                                                    r=3,max_paths=20):
    """TRUE W32/W34 original source proper path witness probabilities.

    Finite algebraic falsifier. Every physical edge retains EXACT
    original flag owner, including paired diagonals, and target core
    flags are checked pairwise against the true ORIGINAL conflict graph.
    """
    from hyp105_full_physical_degree_tail import (
        genuine_source,physical,conflict_graph,
    )
    from hyp105_physical_degree_energy import (
        minimal_alphabet,_verify_typed_injections,
    )
    if type(power) is not int or power not in (1,2):
        raise ValueError("true GQ finite oracle supports W32,W34 only")
    if type(r) is not int or r not in (2,3):
        raise ValueError("only selector path moments r=2 and r=3 needed")
    if type(max_paths) is not int or max_paths<1:
        raise ValueError("positive finite path sample count required")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    I=(tuple(range(len(flags))) if core_ids is None else tuple(core_ids))
    if (len(set(I))!=len(I) or
            any(type(i) is not int or not 0<=i<len(flags) for i in I)):
        raise ValueError("original source core contains invalid/duplicated flag IDs")
    graph,owner=physical(I,flags,f,g)
    conflict,_,_=conflict_graph(I,flags,f,g)
    K=max((len(ns) for ns in conflict.values()),default=0)
    sigma=improved_path_selector_sigma(K)[f"new_sigma{r}"]
    results=[]
    seen=set()
    def visit(path):
        if len(path)==r+1:
            targets=tuple(owner[tuple(sorted((path[j],path[j+1])))]
                          for j in range(r))
            if len(set(targets))!=r:
                raise AssertionError("proper source physical path repeated original flag")
            if len({flags[i][0] for i in targets})!=r or (
                len({flags[i][1] for i in targets})!=r):
                raise AssertionError("proper original source path repeats a point/line")
            if any(set(targets)&set(conflict[t]) for t in targets):
                raise AssertionError("proper original flags were conflicting")
            canonical=min(tuple(path),tuple(reversed(path)))
            if canonical in seen:return
            seen.add(canonical)
            exact=exact_joint_local_minimum_probability(conflict,targets)
            product=local_minimum_lower_probability(conflict,targets)
            full=exact/Fraction(4**r)
            if full<sigma or full<product/Fraction(4**r):
                raise AssertionError("real original selector probability bound broken")
            overlap_any=any(
                conflict[targets[i]]&conflict[targets[j]]
                for i in range(r) for j in range(i+1,r))
            results.append({
                "original_flag_IDs_ordered":targets,
                "proper_physical_vertices":tuple(path),
                "priority_exact_joint_probability":exact,
                "priority_degree_product_floor":product,
                "both_typed_coordinate_cut_probability":Fraction(1,4**r),
                "whole_source_flag_path_exact_survival_probability":full,
                "all_h_uniform_sigma_floor":sigma,
                "target_original_degrees":tuple(len(conflict[t]) for t in targets),
                "some_conflict_neighborhood_overlap":overlap_any,
            })
            return
        for w in sorted(graph[path[-1]]):
            if (w not in path and
                all(w[0]!=z[0] and w[1]!=z[1] for z in path)):
                visit(path+(w,))
                if len(results)>=max_paths:return
    for v in sorted(graph):
        visit((v,))
        if len(results)>=max_paths:break
    return {
        "s":s,"V":V,"a":a,"r":r,"original_core_flag_count":len(I),
        "original_core_max_conflict_degree_K":K,
        "original_proper_path_certificates":tuple(results),
        "paths_checked":len(results),
        "new_all_h_uniform_sigma":sigma,
        "not_a_computational_proof_for_all_h":True,
    }
