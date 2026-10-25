"""Independent exact finite falsifiers for Mathlab issue 230; no repo imports."""
from itertools import combinations, product, permutations
from collections import Counter
from fractions import Fraction
import json

PAIRS = tuple(combinations(range(6), 2))
F0 = (13,4,2,14,0,11,1,7,10,6,9,5,12,3,8)
G68 = (12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)
G72 = (12,9,11,2,8,6,0,13,5,14,3,7,4,10,1)

def geometry():
    pts = tuple(v for v in product(range(2), repeat=4) if any(v))
    ix = {v:i for i,v in enumerate(pts)}
    ls = set()
    for i,j in combinations(range(15), 2):
        u,v = pts[i],pts[j]
        if (u[0]*v[2]+u[2]*v[0]+u[1]*v[3]+u[3]*v[1])%2 == 0:
            k = ix[tuple(x^y for x,y in zip(u,v))]
            ls.add(tuple(sorted((i,j,k))))
    ls = tuple(sorted(ls))
    inc = tuple((p,l) for l,line in enumerate(ls) for p in line)
    assert len(ls)==15 and len(inc)==45
    assert Counter(p for p,l in inc)==Counter({p:3 for p in range(15)})
    assert all(len(set(ls[i])&set(ls[j]))<=1 for i,j in combinations(range(15),2))
    for p,line in product(range(15),ls):
        if p not in line:
            assert sum(any(p in other and q in other for other in ls) for q in line)==1
    return pts,ls,inc

def templates():
    out = {'A':[], 'B':[], 'C':[]}
    for es in combinations(range(15),6):
        if Counter(x for e in es for x in PAIRS[e])==Counter({x:2 for x in range(6)}):
            out['A'].append(es)
    for e,pair in enumerate(PAIRS):
        rem = [i for i in range(6) if i not in pair]
        possible = [j for j,q in enumerate(PAIRS) if set(q)<=set(rem)]
        for es in combinations(possible,4):
            if Counter(x for j in es for x in PAIRS[j])==Counter({x:2 for x in rem}):
                out['B'].append((e,e)+es)
    for es in combinations(range(15),3):
        if len({x for e in es for x in PAIRS[e]})==6:
            out['C'].append(tuple(e for e in es for _ in range(2)))
    assert tuple(map(len,out.values()))==(70,45,15)
    return out

TEMPLATES = templates()

def lifts(labels,inc):
    inv={e:p for p,e in enumerate(labels)}
    neigh = [[i for i,(p,l) in enumerate(inc) if p==q] for q in range(15)]
    seen=set()
    for kind,ts in TEMPLATES.items():
        for t in ts:
            mult=Counter(inv[e] for e in t)
            options=[list(combinations(neigh[p],n)) for p,n in mult.items()]
            for groups in product(*options):
                ids=tuple(sorted(i for group in groups for i in group))
                assert ids not in seen
                seen.add(ids)
                yield ids,kind
    assert len(seen)==62370

def projection(ids,labels,inc,side):
    end=tuple(inc[i][side] for i in ids)
    if Counter(x for p in end for x in PAIRS[labels[p]])!=Counter({x:2 for x in range(6)}):
        return None,end
    profile=tuple(sorted(Counter(end).values(),reverse=True))
    kind={(1,1,1,1,1,1):'A',(2,1,1,1,1):'B',(2,2,2):'C'}[profile]
    return kind,end

def seven_tag(ids,kl,pl,kr,pr,f,g):
    if kr is None: return None
    if (kl,kr)==('B','A'): return 'BA'
    if (kl,kr)==('A','B'): return 'AB'
    if {kl,kr}=={'C','A'}: return 'CA'
    if {kl,kr}=={'C','B'}: return 'CB'
    if (kl,kr)==('B','B'):
        p=next(p for p,n in Counter(pl).items() if n==2)
        l=next(l for l,n in Counter(pr).items() if n==2)
        return 'BBo' if {i for i,x in enumerate(pl) if x==p}&{i for i,x in enumerate(pr) if x==l} else 'BBd'
    if (kl,kr)==('A','A'):
        def dual(end,label):
            return tuple(sorted(tuple(i for i,p in enumerate(end) if x in PAIRS[label[p]]) for x in range(6)))
        a,b=dual(pl,f),dual(pr,g)
        if a!=b or len(set(a))!=6: return None
        reached={0}
        while True:
            new=reached|{v for edge in a if set(edge)&reached for v in edge}
            if new==reached: break
            reached=new
        if len(reached)==6: return 'D6'
    return None

def lift_census(f,g,inc):
    weights=Counter(); tags=Counter(); sources=set()
    for ids,kl in lifts(f,inc):
        pl=tuple(inc[i][0] for i in ids)
        pr=tuple(inc[i][1] for i in ids)
        if kl=='B' and len(set(pr))==6:
            weights[tuple(sorted(pr))]+=1
            sources.add(ids)
        kr,pr=projection(ids,g,inc,1)
        tag=seven_tag(ids,kl,pl,kr,pr,f,g)
        if tag: tags[tag]+=1
    return weights,tags,sources

def permanent_source(f,lines,inc):
    # Enumerate independent ORIGINAL right sixsets, their anchor pairs,
    # disjoint physical four-point squares, and 4x4 perfect matchings.
    inv={e:p for p,e in enumerate(f)}
    squares={p:[tuple(inv[e] for e in t[2:]) for t in TEMPLATES['B'] if t[0]==f[p]] for p in range(15)}
    edgeid={e:i for i,e in enumerate(inc)}
    w=Counter(); nperm=Counter(); sources=set()
    for R in combinations(range(15),6):
        for u,v in combinations(R,2):
            intersection=set(lines[u])&set(lines[v])
            if not intersection: continue
            p=next(iter(intersection))
            rest=tuple(l for l in R if l not in (u,v))
            for Q in squares[p]:
                valid=[qs for qs in permutations(Q) if all(q in lines[l] for q,l in zip(qs,rest))]
                assert len(valid)<=2
                nperm[len(valid)]+=1
                for qs in valid:
                    ids=tuple(sorted((edgeid[p,u],edgeid[p,v])+tuple(edgeid[q,l] for q,l in zip(qs,rest))))
                    assert ids not in sources
                    sources.add(ids)
                if valid: w[R]+=len(valid)
    return w,nperm,sources

def report():
    pts,lines,inc=geometry()
    records=[]
    for name,f,g in [('lex',tuple(range(15)),tuple(range(15))),('reverse',tuple(range(15)),tuple(reversed(range(15)))),('old_S72',F0,G72),('old_S68',F0,G68)]:
        w,c,src=lift_census(f,g,inc)
        wp,np,srcp=permanent_source(f,lines,inc)
        assert w==wp and src==srcp
        swapped=tuple((l,p) for p,l in inc)
        wd,cd,_=lift_census(g,f,swapped)
        dual_lines=tuple(tuple(l for p,l in inc if p==q) for q in range(15))
        wdp,ndp,sd=permanent_source(g,dual_lines,swapped)
        assert wd==wdp
        assert c['BA']==cd['AB'] and c['AB']==cd['BA'] and sum(c.values())==sum(cd.values())
        target={tuple(sorted(es)) for es in TEMPLATES['A']}
        overlap=sum(n for R,n in w.items() if tuple(sorted(g[l] for l in R)) in target)
        assert overlap==c['BA']
        dual_overlap=sum(n for Q,n in wdp.items() if tuple(sorted(f[p] for p in Q)) in target)
        assert dual_overlap==c['AB']
        mu=Fraction(2*sum(w.values()),143)
        rec={'name':name,'f':f,'g':g,'source_mass':sum(w.values()),'dual_source_mass':sum(wd.values()),'source_positive_sixsets':len(w),'permanent_histogram':dict(np),'seven_vector':[c[k] for k in ('D6','BA','AB','CA','CB','BBo','BBd')],'S':sum(c.values()),'mu_f':str(mu),'P2_margin':str(c['BA']+c['AB']-mu),'P7_margin':str(sum(c.values())-mu)}
        records.append(rec)
    output={'point_vectors':pts,'lines':lines,'incidences':inc,'records':records,'scope':'finite exact W(3,2); not Branch A/B'}
    return output

if __name__=='__main__':
    print(json.dumps(report(), indent=2, sort_keys=True))
