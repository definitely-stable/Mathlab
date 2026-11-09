"""HYP-105 AA4-CLIQUE: universal ORIGINAL incompatible P3 pair mass bound.

Theorem (every dyadic s, every fixed separately globally pair-injective,
arbitrarily correlated true original f/g, all named source deletions and
paired physical CORE with J maximum degree K<=64):
For actual coordinate-proper directed physical P3 paths sharing their
ORDERED actual physical endpoints, set p_gamma=Pr(gamma retained by ONE
shared ORIGINAL source-priority plus two typed physical symbol cuts).
Let M=sum_{endpoint bins}(sum_gamma p_gamma)^2; B=sum_{endpoint bins}
sum_{incompatible ordered gamma,eta} p_gamma*p_eta.

For each endpoint bin, condition both typed endpoint physical symbols
on start bit 0, end bit 1. Then Pr(gamma selected | endpoints)=4*p_gamma
>=1/[16*(K+1)^3]. A clique of pairwise incompatible paths has <=1
selected member in each realized ORIGINAL source selection, so clique
number omega <= 16*(K+1)^3. Weighted Motzkin-Straus gives
 B/M <= 1 - 1/[16*(K+1)^3],  G/M>=1/[16*(K+1)^3].
This is 16*(K+1)^3 times stronger than #754's epsilon and is
rigorously all-order; NOT enough to prove B/M<3/4.

Independently each typed x-only or y-only opposite-depth collision graph
has clique number <=3: fix arc a->b, its neighbors are arcs whose first
symbol is b OR last symbol is a, and each of those two groups is
independent. Motzkin-Straus gives B_x/M,B_y/M<=2/3. No false
summation of these marginal bounds into B/M<3/4 is permitted.

This source verifier ONLY imports genuine ORIGINAL symplectic incidence
fixture from #748; it rebuilds f,g,J,both physical diagonals, paths,
exact rank probabilities, incompatibility graph, exact clique and all
weighted mass checks independently of prior AA4 research files.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-badpair-clique-motzkin.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K=64
Q=16*(K+1)**3
Q_OLD_EPS_DENOM=256*(K+1)**6


def _actual_source(s, label_scheme="lex", core="full"):
    if type(s) is not int or s not in (2,4):
        raise ValueError("exact symplectic W32/W34 original source only")
    V=(s+1)*(s*s+1)
    flags=tuple(tuple(t) for t in genuine_symplectic_source(s))
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("invalid ORIGINAL GQ named incidence flags")
    a=2
    while comb(a,2)<V:
        a+=1
    allpairs=list(combinations(range(a),2))
    f=list(allpairs[:V]);g=list(allpairs[:V])
    if label_scheme=="reverse":
        g.reverse()
    elif label_scheme=="shift":
        f=f[3:]+f[:3]
        g=g[7:]+g[:7]
    elif label_scheme!="lex":
        raise ValueError("fixed pair-injective mapping required")
    if core=="full":
        ids=tuple(range(len(flags)))
    elif core=="even":
        ids=tuple(range(0,len(flags),2))
    elif core=="Z17":
        ids=tuple(i for i in range(len(flags)) if i%17!=0)
    else:
        raise ValueError("invalid named ORIGINAL core")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("f or g not separately globally pair-injective")
    point=defaultdict(list);line=defaultdict(list)
    for i in ids:
        p,l=flags[i]
        point[p].append(i);line[l].append(i)
    J=[set() for _ in flags]
    for side,books in (("point",point),("line",line)):
        for source_ids in books.values():
            for i,j in combinations(source_ids,2):
                pi,li=flags[i];pj,lj=flags[j]
                pair_i=g[li] if side=="point" else f[pi]
                pair_j=g[lj] if side=="point" else f[pj]
                if set(pair_i)&set(pair_j):
                    J[i].add(j);J[j].add(i)
    if max((len(J[i]) for i in ids),default=0)>K:
        raise AssertionError("original J max degree not under LOW K64")
    owners={};adj=defaultdict(set)
    for i in ids:
        p,l=flags[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            edge=tuple(sorted((u,v)))
            if edge in owners:
                raise AssertionError("true physical edge owned by >1 ORIGINAL ID")
            owners[edge]=i
            adj[u].add(v);adj[v].add(u)
    if len(owners)!=2*len(ids):
        raise AssertionError("not both real source flag diagonals")
    return {"s":s,"flags":flags,"ids":ids,"f":tuple(f),"g":tuple(g),
            "J":J,"owner":owners,"adj":adj,
            "original_pair_alphabet":a,"deleted_Z":len(flags)-len(ids),
            "actual_J_max":max((len(J[i]) for i in ids),default=0)}


def _proper_true_original_p3(c,limit=None):
    result=[]
    for v0 in sorted(c["adj"]):
        for v1 in sorted(c["adj"][v0]):
            for v2 in sorted(c["adj"][v1]):
                if v2[0] in (v0[0],v1[0]) or v2[1] in (v0[1],v1[1]):
                    continue
                for v3 in sorted(c["adj"][v2]):
                    path=(v0,v1,v2,v3)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        continue
                    owner=tuple(c["owner"][tuple(sorted((path[i],path[i+1])))]
                                for i in range(3))
                    if len(set(owner))!=3 or any(j in c["J"][i]
                            for i,j in combinations(owner,2)):
                        raise AssertionError("true coordinate proper path has conflicting owner")
                    result.append((path,owner))
                    if limit is not None and len(result)>=limit:
                        return result
    return result


def _source_joint_priority(S,J):
    """Independent exact original-source priority rank integral for 3 flags."""
    S=tuple(sorted(set(S)))
    if any(j in J[i] for i,j in combinations(S,2)):
        return Fraction(0)
    neighbors=set().union(*(J[i] for i in S)) - set(S)
    witness={z:tuple(i for i in S if z in J[i]) for z in sorted(neighbors)}
    p=Fraction(0)
    k=len(S)
    for order in permutations(S):
        positions={i:j for j,i in enumerate(order)}
        c=[0]*k
        for dep in witness.values():
            c[max(positions[i] for i in dep)]+=1
        den=1
        suffix=0
        for i in range(k-1,-1,-1):
            suffix+=c[i]+1
            den*=suffix
        p+=Fraction(1,den)
    return p


def _original_path_weights(c,paths):
    cache={}
    out=[]
    for path,os in paths:
        S=tuple(sorted(os))
        if S not in cache:
            value=_source_joint_priority(S,c["J"])/64
            pmin=Fraction(1,64*(K+1)**3)
            if not pmin<=value<=Fraction(1,64):
                raise AssertionError("invalid original Harris source path survival")
            cache[S]=value
        out.append(cache[S])
    return out


def _pair_reason(a,b,c):
    pa,owners_a=a
    pb,owners_b=b
    if pa[0]!=pb[0] or pa[-1]!=pb[-1]:
        raise ValueError("same ordered original physical endpoints required")
    U=tuple(sorted(set(owners_a+owners_b)))
    for i,j in combinations(U,2):
        if j in c["J"][i]:
            return "true_original_J_conflict"
    if pa[1][0]==pb[2][0] or pa[2][0]==pb[1][0]:
        return "first_typed_inner_opposite_depth"
    if pa[1][1]==pb[2][1] or pa[2][1]==pb[1][1]:
        return "second_typed_inner_opposite_depth"
    return "compatible"


def _x_conflict(a,b,axis):
    p=a[0];q=b[0]
    return (p[1][axis]==q[2][axis] or p[2][axis]==q[1][axis])


def _clique_number_neighbors(adj):
    """Independent maximal-clique exact bitset Bron-Kerbosch with pivot."""
    n=len(adj)
    if n==0:
        return 0
    nbr=[sum(1<<j for j in row) for row in adj]
    best=1
    def rec(R,P,X):
        nonlocal best
        if not P and not X:
            if R.bit_count()>best:
                best=R.bit_count()
            return
        if R.bit_count()+P.bit_count()<=best:
            return
        union=P|X
        if union:
            pivot=max((j for j in range(n) if (union>>j)&1),
                      key=lambda j:(P&nbr[j]).bit_count())
            candidates=P&~nbr[pivot]
        else:
            candidates=P
        while candidates:
            j=(candidates&-candidates).bit_length()-1
            bit=1<<j
            rec(R|bit,P&nbr[j],X&nbr[j])
            P&=~bit
            X|=bit
            candidates&=~bit
            if R.bit_count()+P.bit_count()<=best:
                return
    rec(0,(1<<n)-1,0)
    return best


def _motzkin_weighted_check(adj,ws):
    """Use exact positive Fraction weights; no external black-box library."""
    n=len(adj)
    if len(ws)!=n or any(w<=0 for w in ws):
        raise ValueError("finite positive path marginal weights required")
    omega=_clique_number_neighbors(adj)
    W=sum(ws,Fraction(0))
    edges=Fraction(0)
    for i in range(n):
        for j in adj[i]:
            if i<j:
                edges+=ws[i]*ws[j]
    bad=2*edges
    if bad>Fraction(omega-1,omega)*W*W:
        raise AssertionError("weighted original Motzkin-Straus violated")
    return omega,bad,W*W


def _original_endpoint_weight_audit(c,paths):
    byendpoint=defaultdict(list)
    for path in paths:
        byendpoint[(path[0][0],path[0][-1])].append(path)
    counts=Counter()
    buckets=Counter()
    largest_pair_family=0
    omega_total=0
    omega_first=0
    omega_second=0
    M=Fraction(0)
    B=Fraction(0)
    G=Fraction(0)
    BX=Fraction(0)
    BY=Fraction(0)
    G_from_actual_omega=Fraction(0)
    full_pair_checks=0
    witnessed={}
    graph_witnesses={}
    for endpoint, group in sorted(byendpoint.items()):
        n=len(group)
        largest_pair_family=max(largest_pair_family,n)
        weights=_original_path_weights(c,group)
        all_adj=[set() for _ in range(n)]
        x_adj=[set() for _ in range(n)]
        y_adj=[set() for _ in range(n)]
        per_G=Fraction(0)
        per_B=Fraction(0)
        for i,j in combinations(range(n),2):
            reason=_pair_reason(group[i],group[j],c)
            if reason!="compatible":
                all_adj[i].add(j);all_adj[j].add(i)
            if _x_conflict(group[i],group[j],0):
                x_adj[i].add(j);x_adj[j].add(i)
            if _x_conflict(group[i],group[j],1):
                y_adj[i].add(j);y_adj[j].add(i)
            if reason not in witnessed:
                witnessed[reason]={"original_owners1":list(group[i][1]),
                    "original_owners2":list(group[j][1]),
                    "physical_path1":[list(v) for v in group[i][0]],
                    "physical_path2":[list(v) for v in group[j][0]]}
        for i in range(n):
            for j in range(n):
                reason="compatible" if i==j else _pair_reason(group[i],group[j],c)
                counts[reason]+=1
                full_pair_checks+=1
                weight=weights[i]*weights[j]
                if reason=="compatible":
                    per_G+=weight
                else:
                    per_B+=weight
        k,bad,m=_motzkin_weighted_check(all_adj,weights)
        kx,bx,_=_motzkin_weighted_check(x_adj,weights)
        ky,by,_=_motzkin_weighted_check(y_adj,weights)
        buckets[k]+=1
        omega_total=max(omega_total,k)
        omega_first=max(omega_first,kx)
        omega_second=max(omega_second,ky)
        if kx>3 or ky>3:
            raise AssertionError("actual oriented-arcs source typed K4 counterexample")
        if k>Q:
            raise AssertionError("global original endpoint-conditioned clique bound false")
        if not per_B==bad or not per_B+per_G==m:
            raise AssertionError("original path pairs/motif edge mass mismatch")
        if per_G<Fraction(1,k)*m:
            raise AssertionError("true original local Motzkin-Straus good lower bound")
        if bx>Fraction(2,3)*m or by>Fraction(2,3)*m:
            raise AssertionError("universal 2/3 single typed bad bound false")
        # A selected source path in the endpoint-conditioned experiment has
        # probability at least 1/[16*(K+1)^3]. A mutually incompatible clique
        # can contain at most one selected path, hence k<=Q.
        G_from_actual_omega+=m/k
        M+=m
        B+=per_B
        G+=per_G
        BX+=bx
        BY+=by
    if not M or G+B!=M:
        raise AssertionError("all original endpoint pair weights not conserved")
    if not (B<=(1-Fraction(1,Q))*M and
            BX<=Fraction(2,3)*M and BY<=Fraction(2,3)*M and
            G>=G_from_actual_omega>=M/Q):
        raise AssertionError("all-h incompatible B source clique certificate false")
    return {
        "s":c["s"],"actual_original_source_flags":len(c["flags"]),
        "retained_original_CORE_flags":len(c["ids"]),
        "deleted_named_original_Z_flags":c["deleted_Z"],
        "actual_original_physical_edges":len(c["owner"]),
        "actual_original_max_J_degree":c["actual_J_max"],
        "proper_directed_P3_scanned":len(paths),
        "physical_ordered_endpoint_bins":len(byendpoint),
        "max_proper_paths_in_one_endpoint_bin":largest_pair_family,
        "ordered_same_end_real_path_pairs":full_pair_checks,
        "all_incompatibility_reasons":dict(counts),
        "exact_weighted_M":str(M),"exact_weighted_B":str(B),
        "exact_weighted_G":str(G),
        "actual_incompatible_ratio_B_over_M":str(B/M),
        "actual_compatible_ratio_G_over_M":str(G/M),
        "exact_first_typed_only_weighted_Bx":str(BX),
        "exact_second_typed_only_weighted_By":str(BY),
        "max_exact_true_original_incompatibility_clique":omega_total,
        "max_exact_first_typed_clique":omega_first,
        "max_exact_second_typed_clique":omega_second,
        "original_endpoint_clique_histogram":dict(sorted(buckets.items())),
        "instance_specific_Motzkin_G_lower":str(G_from_actual_omega),
        "theorem_global_clique_bound_Q":Q,
        "theorem_uniform_Motzkin_G_over_M_lower":str(Fraction(1,Q)),
        "theorem_old_endpoint_conditioned_Jensen_epsilon":str(Fraction(1,Q_OLD_EPS_DENOM)),
        "improvement_factor_vs_previous_epsilon":Q_OLD_EPS_DENOM//Q,
        "first_factor_Bx_at_most_2thirds_M":True,
        "second_factor_By_at_most_2thirds_M":True,
        "root_PROVED_A":False,
        "first_actual_source_witnesses":witnessed,
    }


def _abstract_typed_arc_graph(nsymbols=5):
    arcs=tuple((a,b) for a in range(nsymbols) for b in range(nsymbols) if a!=b)
    adj=[set() for _ in arcs]
    for i,(a,b) in enumerate(arcs):
        for j,(c,d) in enumerate(arcs):
            if i<j and (a==d or b==c):
                adj[i].add(j);adj[j].add(i)
    omega=_clique_number_neighbors(adj)
    if omega!=3:
        raise AssertionError("abstract physical typed arc x1/x2 conflict max clique !=3")
    a=(0,1);b=(1,2);c=(2,0)
    for x,y in combinations((a,b,c),2):
        if not (x[0]==y[1] or x[1]==y[0]):
            raise AssertionError("abstract three-cycle x conflict not tight")
    return {"physical_internal_symbol_alphabet":nsymbols,
       "all_distinct_ordered_internal_arcs":len(arcs),
       "complete_true_abstract_typed_conflict_graph_clique_number":omega,
       "genuine_abstract_three_arc_conflict_witness":[list(a),list(b),list(c)],
       "universal_single_typed_Bx_B_y_over_M_upper":str(Fraction(2,3))}


def _all_abstract_weighted_motzkin_graphs():
    """Independent finite exact rational falsifier, not the all-h proof."""
    n=5
    edges=tuple(combinations(range(n),2))
    tested=0
    strict=0
    equality=0
    max_clique_seen=0
    for mask in range(1<<len(edges)):
        adj=[set() for _ in range(n)]
        for k,(i,j) in enumerate(edges):
            if (mask>>k)&1:
                adj[i].add(j);adj[j].add(i)
        omega=_clique_number_neighbors(adj)
        max_clique_seen=max(max_clique_seen,omega)
        for weights in product((1,2,3),repeat=n):
            W=sum(weights)
            edge_weight=0
            for i,j in edges:
                if j in adj[i]:
                    edge_weight+=weights[i]*weights[j]
            # Exact no floating point: 2*omega*e <= (omega-1)*W^2.
            margin=(omega-1)*W*W-2*omega*edge_weight
            if margin<0:
                raise AssertionError("weighted exact graph Motzkin-Straus falsified")
            if margin==0:equality+=1
            else:strict+=1
            tested+=1
    return {"all_labeled_five_vertex_simple_graphs":1<<len(edges),
            "strict_integer_positive_weight_distributions_per_graph":3**n,
            "exact_graph_weight_inequalities_tested":tested,
            "strict_inequalities":strict,
            "equality_cases":equality,
            "largest_tested_graph_clique":max_clique_seen,
            "exact_all_h_weighted_Motzkin_claim_from_separate_written_proof":True}


def canonical_report():
    rows=[]
    for s,scheme,core,cap in (
        (2,"lex","full",None),
        (2,"reverse","full",None),
        (2,"shift","Z17",None),
        (4,"lex","even",2000),
        (4,"reverse","even",2000),
        (4,"shift","Z17",2000),
    ):
        c=_actual_source(s,scheme,core)
        paths=_proper_true_original_p3(c,cap)
        if not paths:
            raise AssertionError("empty true original physical proper P3 sample")
        row=_original_endpoint_weight_audit(c,paths)
        row["fixed_source_pair_scheme"]=scheme
        row["original_CORE_scheme"]=core
        row["full_actual_original_proper_P3_census"]=cap is None
        rows.append(row)
    if [x["proper_directed_P3_scanned"] for x in rows[:3]]!=[1346,1154,838]:
        raise AssertionError("independent original physical W32 full path census mismatch")
    if [x["ordered_same_end_real_path_pairs"] for x in rows[:3]]!=[4370,2942,1766]:
        raise AssertionError("independent true W32 same endpoint tensor mismatch")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,
        "new_all_h_original_selector_implies_incompatibility_clique_bound":True,
        "new_all_h_original_B_M_motzkin_bound":True,
        "new_all_h_single_typed_Bx_By_two_thirds_bound":True,
        "all_h_original_endpoint_conditioned_clique_Q":Q,
        "all_h_improved_epsilon":str(Fraction(1,Q)),
        "previous_epsilon":str(Fraction(1,Q_OLD_EPS_DENOM)),
        "improvement_factor":Q_OLD_EPS_DENOM//Q,
        "formal_global_root_proof_not_promoted":True,
        "numerical_published_graph_supersaturation_constants_not_claimed":True,
        "true_original_W32_full_W34_partial":rows,
        "independent_typed_arc_K4_free_falsifier":_abstract_typed_arc_graph(),
        "independent_exhaustive_Motzkin_weighted_graph_falsifier":_all_abstract_weighted_motzkin_graphs(),
        "new_fourfold_full_LOW_sixth_moment_claimed":False,
        "target_original_B_over_M_less_than_3_over_4_proved":False,
    }


if __name__=="__main__":
    print("AA4_CLIQUE_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
