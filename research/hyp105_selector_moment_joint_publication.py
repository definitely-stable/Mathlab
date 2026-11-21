"""AA4-SELECTOR-MOMENT-JOINT: one GLOBAL original source selector referee.

All-h proof is in accompanying manuscript. Independent exact full-outcome census
on small genuine ORIGINAL W(3,2)/W(3,4) named flag cores.
Imports ONLY the previously independently built real GQ fixture from #784,
NOT any former selector, moment, C6, Gram or Jensen evaluator.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
import json

from hyp105_low_publication_partition_referee import model

SCHEMA="mathlab.hyp105.selector-moment-joint-publication.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
PARENT_PR=785


def conflict(m,a,b):
    """TRUE original pencil conflict, both named flags; not physical overlap."""
    p,l=m["flags"][a]
    q,r=m["flags"][b]
    return (p==q and bool(set(m["g"][l])&set(m["g"][r]))
            or l==r and bool(set(m["f"][p])&set(m["f"][q])))


def independent_source(m,owners):
    return all(not conflict(m,i,j) for i in owners for j in owners if i<j)


def chosen_core(s,scheme):
    """Actual proper 3-walk + an adversarial genuine J-conflicting owner."""
    m=model(s,scheme,"full")
    adj=m["adj"];owned=m["owned"]
    for a in sorted(adj):
        for b in sorted(adj[a]):
            for c in sorted(adj[b]):
                for d in sorted(adj[c]):
                    path=(a,b,c,d)
                    if len({x for x,y in path})!=4 or len({y for x,y in path})!=4:
                        continue
                    own=tuple(owned[tuple(sorted((path[i],path[i+1])))]
                              for i in range(3))
                    if len(set(own))!=3 or not independent_source(m,own):
                        raise AssertionError("proper ORIGINAL owners are not independent")
                    for extra in range(len(m["flags"])):
                        if extra not in own and any(conflict(m,extra,j) for j in own):
                            owners=tuple(sorted(set(own)|{extra}))
                            if len(owners)==4:
                                return m,owners,path
    raise AssertionError("no genuine nontrivial 4-flag selector challenge")


def source_J(m,owners):
    J=[set() for _ in owners]
    for i in range(len(owners)):
        for j in range(i+1,len(owners)):
            if conflict(m,owners[i],owners[j]):
                J[i].add(j);J[j].add(i)
    return J


def selected_original_graph(m,owners,mask):
    """Both diagonals per retained flag, actual physical vertices, no clones."""
    adj=defaultdict(set);source_edges={}
    for i,oid in enumerate(owners):
        if not mask>>i&1:
            continue
        p,l=m["flags"][oid]
        x,z=m["f"][p];y,w=m["g"][l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            edge=tuple(sorted((u,v)))
            if edge in source_edges or u==v:
                raise AssertionError("physical edge not unique source owner")
            source_edges[edge]=oid
            adj[u].add(v);adj[v].add(u)
    if len(source_edges)!=2*mask.bit_count():
        raise AssertionError("whole original owner diagonals lost")
    return adj,source_edges


def proper_matrix(adj,r):
    if r not in (2,3):
        raise ValueError("proper selector only r2/r3")
    paths=Counter()
    for u in adj:
        stack=[(u,(u,))]
        for _ in range(r):
            new=[]
            for cur,path in stack:
                for v in adj[cur]:
                    new.append((v,path+(v,)))
            stack=new
        for end,path in stack:
            if (len({v[0] for v in path})==r+1 and
                len({v[1] for v in path})==r+1):
                paths[u,end]+=1
    return paths


def all_paths(adj,r):
    """Independent directed walk count, full uncut fourth/sixth moments."""
    z=Counter()
    for u in adj:
        curr=Counter({u:1})
        for _ in range(r):
            nxt=Counter()
            for v,n in curr.items():
                for w in adj[v]:
                    nxt[w]+=n
            curr=nxt
        for v,n in curr.items():
            z[u,v]=n
    return z


def traces(adj,edges):
    a2=all_paths(adj,2)
    a3=all_paths(adj,3)
    tr2=2*len(edges)
    tr4=sum(x*x for x in a2.values())
    tr6=sum(x*x for x in a3.values())
    return tr2,tr4,tr6


def simple_C6(adj):
    found=set()
    for u in sorted(adj):
        def walk(path):
            if len(path)==6:
                if path[-1] in adj[path[0]]:
                    vertices=tuple(path)
                    rots=[vertices[i:]+vertices[:i] for i in range(6)]
                    rev=vertices[::-1]
                    rots+= [rev[i:]+rev[:i] for i in range(6)]
                    found.add(min(rots))
                return
            for v in adj[path[-1]]:
                if v not in path:
                    walk(path+[v])
        walk([u])
    return len(found)


def priority_masks(J):
    n=len(J)
    counts=Counter()
    for order in permutations(range(n)):
        rank={i:k for k,i in enumerate(order)}
        mask=sum(1<<i for i in range(n)
                 if all(rank[i]<rank[j] for j in J[i]))
        if any((mask>>i&1) and (mask>>j&1)
               for i in range(n) for j in J[i]):
            raise AssertionError("global local-minimum owners are source-conflicting")
        counts[mask]+=1
    if sum(counts.values())!=factorial(n):
        raise AssertionError("priority experiment not exhaustive")
    return counts


def global_two_cut_masks(m,owners):
    """Exact GLOBAL typed-coloring distribution, same bits across all owners."""
    xset=set();yset=set()
    for i in owners:
        p,l=m["flags"][i]
        xset.update(m["f"][p]);yset.update(m["g"][l])
    xs=sorted(xset);ys=sorted(yset)
    if len(xs)+len(ys)>18:
        raise AssertionError("finite color enumeration must be exhaustive")
    xidx={x:i for i,x in enumerate(xs)}
    yidx={y:i+len(xs) for i,y in enumerate(ys)}
    cnt=Counter()
    for bits in range(1<<(len(xs)+len(ys))):
        mask=0
        for i,oid in enumerate(owners):
            p,l=m["flags"][oid]
            a,b=m["f"][p];c,d=m["g"][l]
            if ((bits>>xidx[a])^(bits>>xidx[b]))&1 and (
                (bits>>yidx[c])^(bits>>yidx[d]))&1:
                mask |=1<<i
        cnt[mask]+=1
    if sum(cnt.values())!=(1<<(len(xs)+len(ys))):
        raise AssertionError("two global typed cuts not exhaustive")
    return cnt,len(xs),len(ys)


def product_selector_distribution(m,owners,J):
    """FULL experiment exact p(omega), no per-path resampling or independence."""
    priorities=priority_masks(J)
    cuts,nx,ny=global_two_cut_masks(m,owners)
    joint=Counter()
    for p,cntp in priorities.items():
        for b,cntb in cuts.items():
            joint[p&b]+=cntp*cntb
    denominator=factorial(len(owners))*(1<<(nx+ny))
    if sum(joint.values())!=denominator:
        raise AssertionError("ONE global selector total probability not 1")
    return {m:Q(n,denominator) for m,n in joint.items()},priorities,cuts,nx,ny


def energy(c):
    return sum(v*v for v in c.values())


def integer_root_formal():
    """Only source moment coefficient exact, no external numeric constants."""
    # q_r sharpened by positive association with a single common priority.
    K=10
    return dict(K=K,q2=16*(K+1)**2,q3=64*(K+1)**3,
                priority_product_source_lower="product_i 1/(1+d_JC(owner_i))",
                proper_path_TWO_global_cut_probability_r2="1/16",
                proper_path_TWO_global_cut_probability_r3="1/64",
                old_heuristic_independent_paths_forbidden=True,
                expected_selected_edges_exact="W_C/2",
                expected_selected_trace2_exact="W_C",
                sixth_expected_bound="24 D6 +36 Delta_C^2 W_C",
                fourth_expected_bound_squared=
                    "W_C*(24 D6 +36 Delta_C^2 W_C)",
                all_h_argument_in_separate_proof=True,
                original_ROOT_PROVED_A=False)


def selected_case(s,scheme):
    m,owners,witness=chosen_core(s,scheme)
    J=source_J(m,owners)
    if not any(J):
        raise AssertionError("selector must have nontrivial source conflict")
    owner_ids={i:k for k,i in enumerate(owners)}
    raw_adj,_=selected_original_graph(m,owners,(1<<len(owners))-1)
    P={r:proper_matrix(raw_adj,r) for r in (2,3)}
    if not P[2] or not P[3]:
        raise AssertionError("actual ORIGINAL proper 2-/3-path missing")
    global_prob,priority,cuts,nx,ny=product_selector_distribution(m,owners,J)
    weights=[Q(1,1+len(J[i])) for i in range(len(owners))]
    W=sum(weights,Q(0))
    actual_Delta=max((len(v) for v in raw_adj.values()),default=0)
    if actual_Delta==0:
        raise AssertionError("genuine selected graph empty")

    exact_r={r:dict() for r in (2,3)}
    for r in (2,3):
        pw=defaultdict(lambda:Q(0))
        priority_lower_valid=True
        path_count=0
        for start in sorted(raw_adj):
            stack=[(start,(start,))]
            for step in range(r):
                next_stack=[]
                for cur,path in stack:
                    for v in raw_adj[cur]:
                        next_stack.append((v,path+(v,)))
                stack=next_stack
            for end,path in stack:
                if (len({v[0] for v in path})!=r+1 or
                    len({v[1] for v in path})!=r+1):
                    continue
                k=0
                for i in range(r):
                    eid=m["owned"][tuple(sorted((path[i],path[i+1])))]
                    k|=1<<owner_ids[eid]
                if k.bit_count()!=r:
                    raise AssertionError("proper path repeated source owner")
                ids=[i for i in range(len(owners)) if k>>i&1]
                if any(j in J[i] for i in ids for j in ids if i<j):
                    raise AssertionError("proper path owners J-conflicting")
                source_probability=Q(sum(n for mask,n in priority.items()
                                        if mask&k==k),factorial(len(owners)))
                lower=Q(1)
                for i in ids:
                    lower*=weights[i]
                if source_probability<lower:
                    priority_lower_valid=False
                cut_probability=Q(sum(n for mask,n in cuts.items() if mask&k==k),
                                  1<<(nx+ny))
                if cut_probability!=Q(1,4**r):
                    raise AssertionError("ONE global cut proper-path probability wrong")
                survival=sum(p for mask,p in global_prob.items() if mask&k==k)
                if survival !=source_probability*cut_probability:
                    raise AssertionError("priority and cut experiment were coupled")
                if survival < lower/(4**r):
                    raise AssertionError("Harris/source overlap lower bound failed")
                pw[start,end]+=lower
                path_count+=1
        if not priority_lower_valid:
            raise AssertionError("global priority product source lower failed")
        exact_r[r]=dict(paths=path_count,weighted_source_Gram=str(energy(pw)),
                        total_unweighted_paths=sum(P[r].values()))
        if len(pw)!=len(P[r]):
            raise AssertionError("unweighted and weighted proper endpoint supports differ")

    outcomes=[]
    for mask,prob in global_prob.items():
        adj,edges=selected_original_graph(m,owners,mask)
        if any((mask>>i&1) and (mask>>j&1) for i in range(len(J)) for j in J[i]):
            raise AssertionError("selected J independence lost")
        tr2,tr4,tr6=traces(adj,edges)
        m_edges=len(edges)
        cycles=simple_C6(adj)
        if cycles:
            # With only four original source owners and J-independent
            # two-cut selected graph, each proper C6 requires 6 IDs.
            raise AssertionError("selected C6 without six original owners")
        Delta=max((len(v) for v in adj.values()),default=0)
        if tr6>12*cycles+6*actual_Delta*tr4:
            raise AssertionError("ordinary bipartite sixth walk SW-1 false")
        if tr6>24*cycles+72*m_edges*actual_Delta**2:
            raise AssertionError("ordinary bipartite sixth walk SW-2 false")
        out=dict(mask=mask,probability=prob,tr2=tr2,tr4=tr4,tr6=tr6,
                 e=m_edges,C6=cycles,
                 proper2=proper_matrix(adj,2),proper3=proper_matrix(adj,3))
        outcomes.append(out)

    mean=lambda key:sum((o["probability"]*o[key] for o in outcomes),Q(0))
    E2,E4,E6,Em=(mean(x) for x in ("tr2","tr4","tr6","e"))
    if Em!=W/2 or E2!=W:
        raise AssertionError("global exact source selected expected-edge rank mass")
    if E6>36*actual_Delta**2*W:
        raise AssertionError("source-sensitive sixth moment fails even with D6=0")
    if E4**2>W*E6:
        raise AssertionError("same global experiment spectral Cauchy fails")
    for r in (2,3):
        EX=defaultdict(lambda:Q(0))
        EX2=Q(0)
        for out in outcomes:
            mat=out["proper2" if r==2 else "proper3"]
            for key,v in mat.items():
                EX[key]+=out["probability"]*v
            EX2+=out["probability"]*energy(mat)
        q=4**r*(max(map(len,J))+1)**r
        weighted=defaultdict(lambda:Q(0))
        for u in sorted(raw_adj):
            stack=[(u,(u,))]
            for _ in range(r):
                nxt=[]
                for v,path in stack:
                    for w in raw_adj[v]:
                        nxt.append((w,path+(w,)))
                stack=nxt
            for v,path in stack:
                if len({w[0] for w in path})!=r+1 or len({w[1] for w in path})!=r+1:
                    continue
                ownerlist=[]
                for j in range(r):
                    oid=m["owned"][tuple(sorted((path[j],path[j+1])))]
                    ownerlist.append(owner_ids[oid])
                vweight=Q(1)
                for i in ownerlist:
                    vweight*=weights[i]
                weighted[u,v]+=vweight
        for key,v in P[r].items():
            if EX[key] < Q(v,q) or EX[key] < weighted[key]/(4**r):
                raise AssertionError("weighted original proper path survival Jensen source")
        lhs=energy(EX)
        if lhs>EX2 or EX2>(E4 if r==2 else E6):
            raise AssertionError("same global selector endpoint Jensen transfer false")
        if (energy(P[r])>q*q*(E4 if r==2 else E6)):
            raise AssertionError("uniform q_r original energy transfer failed")
        if (energy(weighted)>16**r*(E4 if r==2 else E6)):
            raise AssertionError("NEW weighted source degree-sensitive energy transfer")
        exact_r[r].update(q_actual=q,physical_Gram=energy(P[r]),
                          EXPECTED_path_Gram=str(lhs),
                          EXPECTED_selected_proper_energy=str(EX2),
                          weighted_Gram=str(energy(weighted)),
                          lower_uniform_q_energy=str(Q(energy(P[r]),q*q)))
    a2=all_paths(raw_adj,2)
    core_trace4=sum(x*x for x in a2.values())
    proper2=P[2]
    B2={k:v for k,v in a2.items() if k not in proper2}
    if core_trace4!=energy(proper2)+energy(B2):
        raise AssertionError("true uncut core fourth moment false P2+B2")
    Qx=Qy=0
    for (u,v),count in a2.items():
        if u[0]==v[0]:Qx+=count
        if u[1]==v[1]:Qy+=count
    J_edges=sum(len(v) for v in J)//2
    if Qx+Qy!=8*len(owners)+4*J_edges:
        raise AssertionError("true original returns Qx+Qy exact J identity broken")
    if energy(B2)>actual_Delta*(Qx+Qy):
        raise AssertionError("coordinate-improper two-walk energy wrong")
    return dict(s=s,scheme=scheme,source_CORE_flag_count=len(owners),
       original_proper_three_walk_witness=list(witness),
       true_original_SOURCE_J_edges=J_edges,source_J_max_degree=max(map(len,J)),
       priority_outcomes=sum(priority.values()),two_cut_bit_outcomes=sum(cuts.values()),
       global_selected_subset_count=len(global_prob),
       source_W_C=str(W),expected_selected_edges=str(Em),
       expected_selected_trace2=str(E2),
       expected_selected_trace4=str(E4),
       expected_selected_trace6=str(E6),
       full_core_physical_Delta=actual_Delta,
       source_six_cycle_D6=0,
       selected_graph_C6_every_outcome_zero=True,
       EXPECTED_sixwalk_source_bound=str(36*actual_Delta**2*W),
       expected_fourth_Cauchy_squared=str(E4**2),
       expected_fourth_Cauchy_upper=str(W*E6),
       original_CORE_trace4=core_trace4,
       core_proper2_Gram=energy(proper2),
       core_improper2_Gram=energy(B2),
       original_coordinate_return_Qx=Qx,
       original_coordinate_return_Qy=Qy,
       physical_proper_paths=exact_r)


def certificate():
    cases=[]
    for s in (2,4):
        for mode in ("lex","reverse","correlated"):
            cases.append(selected_case(s,mode))
    return dict(schema=SCHEMA,status=STATUS,issue=230,parent_pr=PARENT_PR,
                exact_global_selector_priority_and_TWO_global_typed_cuts=True,
                independent_all_h_source_overlap_product_integral_proof=True,
                NEW_weighted_original_path_energy_transfer=True,
                genuine_original_selected_GQ_cases=cases,
                published_ordinary_graph_C6_constants_numeric_unknown=True,
                all_h_C6_source_original_sixID_inverse_inherited_from_772=True,
                full_original_LOW_PRODUCED_publication_signoff_still_open=True,
                original_ROOT_PROVED_A=False,
                formal_root_quantifier_interface=integer_root_formal())


if __name__=="__main__":
    print("AA4_SELECTOR_MOMENT_JOINT_CERTIFICATE="+
          json.dumps(certificate(),sort_keys=True,separators=(",",":")))
