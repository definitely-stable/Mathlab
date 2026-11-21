"""Integrated Branch A: independent source/cycle lift, direct GF5 flow and exact root ledger.

Only the genuine original symplectic geometry fixture from #784 is reused.
No historical cycle classifier, signed Fourier evaluator or moment calculator
is used. Finite tests are falsifiers of the accompanying all-h proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import isqrt
import json

from hyp105_low_publication_partition_referee import model

SCHEMA = "mathlab.hyp105.branch-a-integrated.v1"
STATUS = "OPEN_WITH_FORMAL_BLOCKER"  # repository acceptance is distinct from proof candidate


def canonical_cycle(v):
    t = tuple(v)
    return min(
        w[i:]+w[:i] for w in (t,t[::-1]) for i in range(len(t)))


def actual_edges(m, ids):
    """Real owner graph constructed directly from original named flags."""
    adj=defaultdict(set); own={}
    for i in ids:
        p,l=m["flags"][i]
        a,b=m["f"][p]; c,d=m["g"][l]
        for u,v in (((a,c),(b,d)),((a,d),(b,c))):
            e=tuple(sorted((u,v)))
            assert e not in own
            own[e]=i
            adj[u].add(v);adj[v].add(u)
    return adj,own


def typed_dual(pairs):
    """Original column adjacency MULTIGRAPH, not physical graph."""
    fibres=defaultdict(list)
    for i,pair in enumerate(pairs):
        if len(set(pair))!=2:
            raise ValueError("invalid unique-symbol support pair")
        for sym in pair:
            fibres[sym].append(i)
    if len(fibres)!=6 or any(len(z)!=2 for z in fibres.values()):
        return None
    return sorted(tuple(sorted(z)) for z in fibres.values())


def source_d6(m, ids):
    """Historical B3.2 D6 requires two coincident dual labelled C6."""
    ids=tuple(sorted(ids))
    if len(ids)!=6 or len(set(ids))!=6:
        return None
    p,l=zip(*(m["flags"][i] for i in ids))
    if len(set(p))!=6 or len(set(l))!=6:
        return None
    x=[m["f"][j] for j in p]; y=[m["g"][j] for j in l]
    dx=typed_dual(x);dy=typed_dual(y)
    if dx is None or dx!=dy or len(set(dx))!=6:
        return None
    a=defaultdict(set)
    for i,j in dx:
        a[i].add(j);a[j].add(i)
    if set(a)!=set(range(6)) or any(len(z)!=2 for z in a.values()):
        return None
    order=[0,min(a[0])]
    while len(order)<6:
        q=a[order[-1]]-{order[-2]}
        if len(q)!=1:
            return None
        k=q.pop()
        if k in order:
            return None
        order.append(k)
    if order[0] not in a[order[-1]]:
        return None
    corners=[]
    for i,j in zip(order,order[1:]+order[:1]):
        xx=set(x[i])&set(x[j]);yy=set(y[i])&set(y[j])
        assert len(xx)==len(yy)==1
        corners.append((xx.pop(),yy.pop()))
    assert len({i for i,j in corners})==len({j for i,j in corners})==6
    return canonical_cycle(corners)


def physical_d6(m, ids=None, rainbow_only=True):
    if ids is None:
        ids=range(len(m["flags"]))
    adj,own=actual_edges(m,ids)
    cycles=set()
    for start in sorted(adj):
        def extend(path):
            if len(path)==6:
                if start in adj[path[-1]] and path[1]<path[-1]:
                    cycles.add(tuple(path))
                return
            for v in adj[path[-1]]:
                if v<=start or v in path:
                    continue
                if rainbow_only and (v[0] in {z[0] for z in path}
                                     or v[1] in {z[1] for z in path}):
                    continue
                extend(path+[v])
        extend([start])
    ret={}
    for cycle in cycles:
        key=tuple(sorted(own[tuple(sorted((u,v)))]
                         for u,v in zip(cycle,cycle[1:]+cycle[:1])))
        if rainbow_only:
            assert len(set(key))==6 and key not in ret
            assert source_d6(m,key)==canonical_cycle(cycle)
        ret[key]=canonical_cycle(cycle)
    return ret


def factor_first_d6(m):
    """Second completely distinct census: physical x-factor cycle, source lines."""
    left=defaultdict(set);p_id={}
    for p,(x,y) in enumerate(m["f"]):
        left[x].add(y);left[y].add(x)
        p_id[tuple(sorted((x,y)))]=p
    incid=defaultdict(list)
    for i,(p,l) in enumerate(m["flags"]):
        incid[p].append(i)
    result={}
    for x0 in sorted(left):
        def extend(xs):
            if len(xs)==6:
                if x0 not in left[xs[-1]] or xs[1]>=xs[-1]:
                    return
                ps=[p_id[tuple(sorted((u,v)))] for u,v in zip(xs,xs[1:]+xs[:1])]
                for ids in product(*(incid[p] for p in ps)):
                    cy=source_d6(m,ids)
                    if cy is not None:
                        k=tuple(sorted(ids))
                        assert k not in result
                        result[k]=cy
                return
            for nxt in sorted(left[xs[-1]]):
                if nxt>x0 and nxt not in xs:
                    extend(xs+[nxt])
        extend([x0])
    return result


def gf5_nonzero_flows(edges, positives):
    """Direct spanning-tree elimination of nonzero GF5 edge currents.

    Each edge is one physical symbol appearing in two named source columns.
    Orient low -> high, and impose signed checksum 4 at each source column.
    Enumerate the seven non-tree currents; tree demands force the rest.
    No Fourier characters, polynomial evaluation, cached palette counts.
    """
    edges=[tuple(sorted(e)) for e in edges]
    if len(edges)!=12 or any(a==b or a<0 or b>5 for a,b in edges):
        raise ValueError("12 valid dual edges required")
    if len(positives)!=3 or not set(positives)<=set(range(6)):
        raise ValueError("balanced signs required")
    seen={0};order=[0];tree=set();par={}
    for v in order:
        for idx,(a,b) in enumerate(edges):
            if a==v and b not in seen:
                other=b
            elif b==v and a not in seen:
                other=a
            else:
                continue
            seen.add(other);order.append(other)
            tree.add(idx);par[other]=(v,idx)
    if len(seen)!=6 or len(tree)!=5:
        raise ValueError("connected six-column dual required")
    chords=[i for i in range(12) if i not in tree]
    base=[4 if i in positives else -4 for i in range(6)]
    count=0
    for currents in product(range(1,5),repeat=7):
        d=base[:]
        for idx,z in zip(chords,currents):
            a,b=edges[idx]
            d[a]-=z;d[b]+=z
        for j in reversed(order[1:]):
            v,_=par[j]
            if d[j]%5==0:
                break
            d[v]+=d[j]
        else:
            assert d[0]%5==0
            count+=1
    return count


def flow_catalog():
    cyc=[(j,(j+1)%6) for j in range(6)]
    d6=gf5_nonzero_flows(cyc+cyc,{0,2,4})
    # Columns: q-ell, p-ell, p-r, owner1, owner2, owner3.
    # x: repeated (1,2) twice and C4(0,3,4,5);
    # y: repeated (0,1) twice and C4(2,3,4,5).
    bx=[(1,2)]*2+[(0,3),(3,4),(4,5),(5,0)]
    by=[(0,1)]*2+[(2,3),(3,4),(4,5),(5,2)]
    bbo=[gf5_nonzero_flows(bx+by,{0,*tail})
         for tail in combinations(range(1,6),2)]
    palette=sum(sum(z)%5==4 for z in product(range(1,5),repeat=4))
    assert palette==51 and d6==5643 and sum(bbo)==53838
    assert min(bbo)>=5175
    return dict(palette=palette,d6_alternating=d6,bbo_sign_counts=bbo,
                bbo_balanced_total=sum(bbo),bbo_historical_floor=51750)


def proper_bbo_from_physical(m):
    """Independent actual GQ source anchor recovery without parent classifier."""
    adj,_=actual_edges(m,range(len(m["flags"])))
    owned=m["owned"]
    result=defaultdict(set)
    for a in adj:
        for b in adj[a]:
            for c in adj[b]:
                for d in adj[c]:
                    path=(a,b,c,d)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        continue
                    q=m["point_by_pair"].get(tuple(sorted((a[0],d[0]))))
                    r=m["line_by_pair"].get(tuple(sorted((a[1],d[1]))))
                    if q is None or r is None or (q,r) not in m["projection"]:
                        continue
                    p,l=m["projection"][q,r]
                    if set(m["f"][p])&{v[0] for v in path} or set(m["g"][l])&{v[1] for v in path}:
                        continue
                    anc=[m["flag_to_id"][j] for j in ((q,l),(p,l),(p,r))]
                    resid=[owned[tuple(sorted((u,v)))] for u,v in zip(path,path[1:])]
                    ids=tuple(sorted(anc+resid))
                    assert len(set(ids))==6
                    assert historical_bbo(m,ids)
                    result[ids].add(path)
    assert all(len(v)==2 and next(iter(v))[::-1] in v for v in result.values())
    return result


def actual_bbo_flow_topology(m,ids,path):
    """Check the actual produced source template, not just an abstract graph."""
    a,b,c,d=path
    q=m["point_by_pair"][tuple(sorted((a[0],d[0])))]
    r=m["line_by_pair"][tuple(sorted((a[1],d[1])))]
    p,l=m["projection"][q,r]
    ordered=[m["flag_to_id"][z] for z in ((q,l),(p,l),(p,r))]
    ordered += [m["owned"][tuple(sorted((u,v)))] for u,v in zip(path,path[1:])]
    assert sorted(ordered)==list(ids)
    flags=[m["flags"][i] for i in ordered]
    x=typed_dual([m["f"][p] for p,l in flags])
    y=typed_dual([m["g"][l] for p,l in flags])
    assert x==sorted([(1,2),(1,2),(0,3),(3,4),(4,5),(0,5)])
    assert y==sorted([(0,1),(0,1),(2,3),(3,4),(4,5),(2,5)])
    return True


def historical_bbo(m,ids):
    """B/B overlap structural class in accepted merged E1A."""
    if len(ids)!=6 or len(set(ids))!=6:
        return False
    f=[m["flags"][i] for i in ids]
    p,l=zip(*f)
    cp=Counter(p);cl=Counter(l)
    if sorted(cp.values())!=[1,1,1,1,2] or sorted(cl.values())!=[1,1,1,1,2]:
        return False
    rp=next(i for i,n in cp.items() if n==2)
    rl=next(i for i,n in cl.items() if n==2)
    if (rp,rl) not in f:
        return False
    return (typed_dual([m["f"][i] for i in p]) is not None and
            typed_dual([m["g"][i] for i in l]) is not None)


def source_bbo_inverse(m,ids):
    if not historical_bbo(m,ids):
        return set()
    fs={i:m["flags"][i] for i in ids}
    p=next(k for k,n in Counter(i[0] for i in fs.values()).items() if n==2)
    l=next(k for k,n in Counter(i[1] for i in fs.values()).items() if n==2)
    q=next(a for a,b in fs.values() if b==l and a!=p)
    r=next(b for a,b in fs.values() if a==p and b!=l)
    if m["projection"].get((q,r))!=(p,l):
        return set()
    residual=[i for i,(a,b) in fs.items() if a!=p and b!=l]
    assert len(residual)==3
    # Try the six ORIGINAL owner orders, recover actual middle coordinates
    # solely by intersections, without enumerating walks in a physical graph.
    out=set()
    for i,j,k in permutations(residual):
        x=[set(m["f"][fs[v][0]]) for v in (i,j,k)]
        y=[set(m["g"][fs[v][1]]) for v in (i,j,k)]
        coords=[]
        for pairs,closure in ((x,set(m["f"][q])),(y,set(m["g"][r]))):
            b=pairs[0]&pairs[1];c=pairs[1]&pairs[2]
            if len(b)!=1 or len(c)!=1 or b==c:
                break
            a=pairs[0]-b;d=pairs[2]-c
            if len(a)!=1 or len(d)!=1 or a|d!=closure:
                break
            v=tuple(next(iter(z)) for z in (a,b,c,d))
            if len(set(v))!=4:
                break
            coords.append(v)
        if len(coords)==2:
            out.add(tuple(zip(*coords)))
    return out


def source_first_bbo_w32(m):
    result={}
    assert m["s"]==2
    incid=defaultdict(list)
    for i,(p,l) in enumerate(m["flags"]):
        incid[p].append(i)
    # Exactly one repeated physical point pair, disjoint C4 on remaining symbols.
    for p,pair in enumerate(m["f"]):
        syms=sorted(set(range(m["a"]))-set(pair))
        x0=syms[0]
        for seq in permutations(syms[1:]):
            if seq[0]>=seq[-1]:
                continue
            cyc=(x0,)+seq
            ps=[m["point_by_pair"][tuple(sorted((a,b)))]
                for a,b in zip(cyc,cyc[1:]+cyc[:1])]
            for twice in combinations(incid[p],2):
                for rest in product(*(incid[q] for q in ps)):
                    ids=tuple(sorted(twice+rest))
                    if not historical_bbo(m,ids):
                        continue
                    paths=source_bbo_inverse(m,ids)
                    if paths:
                        assert ids not in result and len(paths)==2
                        result[ids]=paths
    return result


def root_exact_ledger(C0=Q(1),c0=Q(1)):
    if type(C0)!=Q or type(c0)!=Q or C0<1 or not 0<c0<=1:
        raise ValueError("formal existential theorem constants only")
    def ceil(x):
        x=Q(x);return -(-x.numerator//x.denominator)
    def sc(n):
        n=ceil(n);r=isqrt(n);return r+(r*r<n)
    u=Q(1,2**32);t=Q(1,2**16)
    v=(1+u)*(1+u*u);nu=(1+u)*v
    M=(1+u*u)*(1+Q(23,16)*t)
    A=2*v+Q(23,4)*t**3+4*t**6
    R=ceil(256*A*(1+64*M))
    assert R==33281 and 2*v<Q(10,7)**2
    assert 8*(nu+M)<17 and 24*(nu+M)<49
    endpoint=16*(1+u*u)*(1+2*t)+16*v*t+16*u*u+4*u*nu
    book=32*(1+u)*nu*v*(t+(1+u)*(Q(10,7)+t**3))
    assert endpoint<17 and book<46 and 4*nu<Q(17,4)
    K=10
    c=Q(7,8)-4*M/(K+1);w=(4*c)**3/(A*A)
    assert c>0 and w/64 > Q(1,R**6)
    T=ceil(Q(17,2)*R**3*C0**3)
    delta=c0/R**6
    q2=16*(K+1)**2; q3=64*(K+1)**3
    L6=1+ceil(36*nu*T*T)  # new expected_C6 <= D6/1024
    L4=q2*q2*sc(nu*L6)+17*T
    E=q3*sc(17*L6);B=sc(46*(K+1)*T);D=4*sc(B*T*L4)
    alpha=Q(1,64);beta=Q(15,16)
    s0=max(2**32,64,ceil(49*T/(alpha*w)),ceil((E/(alpha*w))**2),ceil((D/(beta*w))**8))
    h0=(s0-1).bit_length()
    ss=2**h0
    assert 49*T <= alpha*w*ss
    assert E**2 <= (alpha*w)**2*ss
    assert D**8 <= (beta*w)**8*ss
    assert w/64>delta
    return dict(FORMAL_ONLY=True,C0=str(C0),c0=str(c0),R=R,K=K,T=str(T),
                q2=q2,q3=q3,L6=str(L6),L4=str(L4),B=str(B),E=str(E),D=str(D),
                delta=str(delta),sufficient_h0=h0,endpoint=str(endpoint),book=str(book),
                expected_C6_cut_upper="1/1024",sixth_D6_coefficient="3/128",
                theorem_constants_numeric_unknown=True)


def verify_positive_cycle_cuts(m,ids):
    cy=source_d6(m,ids)
    assert cy is not None
    xp=sorted({x for x,y in cy});yp=sorted({y for x,y in cy})
    assert len(xp)==len(yp)==6
    cuts=0
    for mask in range(2**12):
        bx={x:(mask>>i)&1 for i,x in enumerate(xp)}
        by={y:(mask>>(i+6))&1 for i,y in enumerate(yp)}
        if all(bx[u[0]]!=bx[v[0]] and by[u[1]]!=by[v[1]]
               for u,v in zip(cy,cy[1:]+cy[:1])):
            cuts+=1
    assert cuts==4
    return dict(original_ids=list(ids),coherent_global_cut_successes=cuts,
                cut_assignments=4096,probability=str(Q(cuts,4096)))


def certificate():
    flow=flow_catalog()
    cases=[]
    for scheme in ("lex","reverse","correlated"):
        m=model(2,scheme,"full")
        d=physical_d6(m); f=factor_first_d6(m)
        assert d==f
        b=proper_bbo_from_physical(m)
        sb=source_first_bbo_w32(m)
        assert dict(b)==sb
        assert set(b).isdisjoint(d)
        assert all(actual_bbo_flow_topology(m,ids,next(iter(paths))) for ids,paths in b.items())
        cut=verify_positive_cycle_cuts(m,next(iter(d))) if d else None
        cases.append(dict(s=2,scheme=scheme,D6=len(d),produced_BBo=len(b),
                          two_independent_D6_censuses_equal=True,
                          two_independent_BBo_censuses_equal=True,
                          nonzero_cycle_cut=cut))
    # A genuinely nonzero W34 witness via physical-first rainbow DFS,
    # independent of historical seed / fixture rank assumptions.
    m=model(4,"lex","full");adj=m["adj"]
    def find():
        for u in sorted(adj):
            def rec(path):
                if len(path)==6:
                    if u in adj[path[-1]]:
                        return tuple(path)
                    return None
                for v in sorted(adj[path[-1]]):
                    if v[0] not in {x for x,y in path} and v[1] not in {y for x,y in path}:
                        z=rec(path+[v])
                        if z is not None:return z
                return None
            z=rec([u])
            if z is not None:return z
        raise AssertionError("no positive real W34 cycle")
    cyc=find()
    ids=tuple(sorted(m["owned"][tuple(sorted((u,v)))]
                     for u,v in zip(cyc,cyc[1:]+cyc[:1])))
    assert source_d6(m,ids)==canonical_cycle(cyc)
    assert len(physical_d6(m,ids))==1
    return dict(schema=SCHEMA,status=STATUS,issue=230,parent_pr=786,
                mathematical_candidate="TWO_CLASS_BRANCH_A_COMPLETE_PROOF",
                repository_PROVED_A=False,
                direct_nonzero_palette_flow=flow,
                genuine_W32_two_independent_source_censuses=cases,
                genuine_W34_positive_cycle=verify_positive_cycle_cuts(m,ids),
                formal_root_ledgers=[root_exact_ledger(a,b) for a,b in
                    ((Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17)))],
                external_published_theorem="Jiang-Yepremyan 2020, DOI 10.1017/S0963548320000206",
                external_constants_numeric_unknown=True,
                no_new_ASET_exponent=True)


if __name__=="__main__":
    print("AA4_BRANCH_A_INTEGRATED_CERTIFICATE="+json.dumps(certificate(),sort_keys=True))
