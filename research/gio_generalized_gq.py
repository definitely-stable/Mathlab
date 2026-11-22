"""GIO-001.3: axiomatic GQ(s,t) balance theorem ledger and independent fixtures.

Source-flag geometry, not a substitute synthetic SRG. External graph C6
constants are existential; sample rational parameters are FORMAL ONLY.
No physical PC or undocumented numerical graph constant is needed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import comb, gcd, isqrt
from pathlib import Path
import argparse
import json

from gio_resilience import (
    source_first_d6, source_first_bbo, physical_bbo, greedy_pack,
)
from hyp105_aa4_branch_a_integrated_referee import (
    physical_d6, source_d6, historical_bbo, flow_catalog,
)

SCHEMA="mathlab.gio003.balanced-axiomatic-gq.v1"


def ceil(z):
    z=Q(z)
    return -(-z.numerator//z.denominator)


def sqrtceil(z):
    n=ceil(z)
    if n<0:
        raise ValueError("square-root budget must be nonnegative")
    v=isqrt(n)
    return v+(v*v<n)


def balanced_ledger(balance=1,C0=Q(1),c0=Q(1)):
    """No numerical external theorem constants are asserted.

    If max(s,t) <= B * min(s,t), take b=ceil(B) first.
    All integer envelopes below hold for every r=min(s,t)>=r0,
    independently of characteristic and the actual GQ realization.
    """
    if type(balance) is not int or balance<1:
        raise ValueError("positive integral balance upper bound required")
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("exact admissible external existential parameters only")
    b=balance
    v=(b+1)**3
    n0=(b+1)**4
    a0=2*v+2
    A0=a0*a0
    j0=(b*b+1)*a0+b*v
    J0=2*j0
    rho_cap=Q(1,32)
    K=16*J0+1
    c=Q(1,2)
    assert Q(7,8)-rho_cap-Q(2*J0,K+1)>c
    w=(4*c)**3/Q(A0*A0)
    R=512*A0*(1+64*J0)
    T=ceil(8*n0*R**3*C0**3)
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    Q0=8*n0+4*J0
    L6=1+ceil(36*n0*T*T)
    L4=q2*q2*sqrtceil(n0*L6)+Q0*T
    missing=4*(2*a0*v+a0*a0)
    end0=missing+4*n0+8*b*J0
    E=q3*sqrtceil(end0*L6)
    g0=2*v*b*(b+1)+4*(b+1)*j0+2*(b+1)*v*a0
    book0=16*(b+1)*n0*g0
    BK=sqrtceil(book0*(K+1)*T)
    D=4*sqrtceil(BK*T*L4)
    improper=3*T*Q0
    delta=min(c0/Q(R**6),w/4)
    err=w/8
    rho=min(rho_cap,err**2/Q(12*b*b*q3*q3*L6))
    r0=max(2**32,ceil(Q(improper)/err),
           ceil((Q(E)/err)**2),ceil((Q(D)/err)**8))
    assert 0<rho<=rho_cap and 0<delta<=w/4
    assert 12*b*b*rho*q3*q3*L6<=err*err
    assert improper<=err*r0 and E*E<=err*err*r0
    assert D**8<=err**8*r0
    assert 8*n0*R**3*C0**3<=T
    assert (4*c)**3==8

    return dict(schema=SCHEMA,FORMAL_ONLY=True,
        external_numeric_constants_unknown=True,
        balance_upper=b,C0=str(C0),c0=str(c0),
        V_upper=v,N_upper=n0,alphabet_upper=a0,
        physical_vertex_upper=A0,typed_collinearity_conflict_upper=j0,
        combined_J_upper=J0,
        max_source_conflict_degree=K,
        R=R,T=str(T),Q0=Q0,q2=q2,q3=q3,
        L6=str(L6),L4=str(L4),endpoint_upper=end0,
        pencil_square_upper=g0,book_square_upper=book0,
        book_sqrt_BK=str(BK),E=str(E),D=str(D),
        improper_coefficient=str(improper),
        core_lower=str(c),walk_lower=str(w),
        rho_cap=str(rho_cap),rho=str(rho),delta=str(delta),
        error_budget_each=str(err),sufficient_integer_r0=str(r0),
        geometric_characteristic_assumed=False,
        finite_checks_are_not_asymptotic_proof=True,
        new_unrestricted_ASET_exponent=False)


def validate_asymptotic_domain(s,t,Z_size,ledger):
    """No existence claim for GQ(s,t); only an algebraic domain guard."""
    if any(type(z) is not int for z in (s,t,Z_size)):
        raise ValueError("s,t,Z_size must be exact integers")
    if min(s,t)<int(ledger["sufficient_integer_r0"]) or Z_size<0:
        raise ValueError("outside proven sufficiently large order")
    r=min(s,t)
    if max(s,t)>int(ledger["balance_upper"])*r:
        raise ValueError("unequal parameters exceed fixed balance")
    if Z_size>Q(ledger["rho"])*r**4:
        raise ValueError("adversarial deletion budget exceeded")
    return r


def prime_projective(v,q):
    index=next(i for i,z in enumerate(v) if z%q)
    inv=pow(v[index],-1,q)
    return tuple((z*inv)%q for z in v)


def symplectic_prime(q):
    """Independent PG(3,q) isotropic projective lines, q=2 or odd prime 3."""
    if q not in (2,3):
        raise ValueError("only exact independent GF(2)/GF(3) fixtures")
    pts=tuple(sorted({prime_projective(v,q)
                      for v in product(range(q),repeat=4) if any(v)}))
    ids={p:i for i,p in enumerate(pts)}
    lines=set()
    for i,j in combinations(range(len(pts)),2):
        u=pts[i];v=pts[j]
        bracket=(u[0]*v[2]-u[2]*v[0]+u[1]*v[3]-u[3]*v[1])%q
        if bracket:
            continue
        line={j}
        for a in range(q):
            w=tuple((u[k]+a*v[k])%q for k in range(4))
            line.add(ids[prime_projective(w,q)])
        assert len(line)==q+1
        lines.add(tuple(sorted(line)))
    return dict(s=q,t=q,lines=tuple(sorted(lines)),origin="independent_PG3_GF"+str(q))


def elliptic_minus_24():
    """Elliptic Q^-(5,2) with Witt index 2: 27 singular pts, 45 lines.

    Coordinates (x0,x1,...,x5); Q=x0+x0*x1+x1+x2*x3+x4*x5.
    Every totally singular line has three nonzero vectors u,v,u xor v.
    """
    def value(z):
        x=[(z>>i)&1 for i in range(6)]
        return x[0]^x[1]^(x[0]&x[1])^(x[2]&x[3])^(x[4]&x[5])
    pts=tuple(x for x in range(1,64) if value(x)==0)
    assert len(pts)==27
    loc={v:i for i,v in enumerate(pts)}
    lines=set()
    for a,b in combinations(pts,2):
        c=a^b
        if c in loc:
            lines.add(tuple(sorted((loc[a],loc[b],loc[c]))))
    assert len(lines)==45
    return dict(s=2,t=4,lines=tuple(sorted(lines)),
                origin="independent_Qminus5_2_GF2")


def dual_geometry(g):
    Vp=max(p for line in g["lines"] for p in line)+1
    around=[set() for _ in range(Vp)]
    for ell,line in enumerate(g["lines"]):
        for p in line:
            around[p].add(ell)
    return dict(s=g["t"],t=g["s"],
        lines=tuple(tuple(sorted(z)) for z in around),
        origin="dual_of_"+g["origin"])


def imported_symplectic_4():
    """Different upstream W(3,4) constructor, algebraically independently checked."""
    from hyp105_low_publication_partition_referee import genuine_gq
    g=genuine_gq(4)
    return dict(s=4,t=4,lines=tuple(g["lines"]),
                origin="upstream_independent_GF4_isotropic_lines")


def geometry(kind):
    if kind=="W32":
        return symplectic_prime(2)
    if kind=="W33":
        return symplectic_prime(3)
    if kind=="Qminus24":
        return elliptic_minus_24()
    if kind=="dualQminus42":
        return dual_geometry(elliptic_minus_24())
    if kind=="W34":
        return imported_symplectic_4()
    raise ValueError("unknown genuine GQ fixture")


def structure(g):
    """Reconstruct GQ axiom from incidence alone; never assume SRG suffices."""
    s,t=g["s"],g["t"]
    lines=tuple(g["lines"])
    Vp=(s+1)*(s*t+1);Vl=(t+1)*(s*t+1)
    assert len(lines)==Vl and all(len(z)==s+1 and len(set(z))==s+1 for z in lines)
    assert set(x for z in lines for x in z)==set(range(Vp))
    on=[set() for _ in range(Vp)]
    neighbors=[set() for _ in range(Vp)]
    pairline={}
    for ell,L in enumerate(lines):
        for p in L:
            on[p].add(ell);neighbors[p].update(set(L)-{p})
        for a,b in combinations(L,2):
            key=(min(a,b),max(a,b))
            assert key not in pairline
            pairline[key]=ell
    assert all(len(z)==t+1 for z in on)
    projection={}
    for q in range(Vp):
        for r,L in enumerate(lines):
            if q in L:
                continue
            feet=neighbors[q].intersection(L)
            assert len(feet)==1, ("GQ unique projection failure",g["origin"],q,r,feet)
            p=next(iter(feet))
            ell=pairline[min(q,p),max(q,p)]
            projection[q,r]=(p,ell)
    assert len(projection)==Vp*(Vl-t-1)
    flags=tuple(sorted((p,l) for l,L in enumerate(lines) for p in L))
    lookup={v:i for i,v in enumerate(flags)}
    assert len(flags)==(s+1)*(t+1)*(s*t+1)
    return dict(g,Vp=Vp,Vl=Vl,lines=lines,on=on,neighbors=neighbors,
                projection=projection,flags=flags,flag_to_id=lookup)


def strongly_regular_data(g):
    """Check all ordered common-neighbor counts, not an assumed spectrum."""
    s,t=g["s"],g["t"]
    P=structure(g)
    for p in range(P["Vp"]):
        assert len(P["neighbors"][p])==s*(t+1)
        for q in range(P["Vp"]):
            common=len(P["neighbors"][p]&P["neighbors"][q])
            if q==p:
                expect=s*(t+1)
            elif q in P["neighbors"][p]:
                expect=s-1
            else:
                expect=t+1
            assert common==expect
    dual=structure(dual_geometry(g))
    for p in range(dual["Vp"]):
        assert len(dual["neighbors"][p])==t*(s+1)
        for q in range(dual["Vp"]):
            common=len(dual["neighbors"][p]&dual["neighbors"][q])
            expect=t*(s+1) if q==p else (t-1 if q in dual["neighbors"][p] else s+1)
            assert common==expect
    return dict(points=P["Vp"],lines=P["Vl"],flags=len(P["flags"]),
       point_parameters=[P["Vp"],s*(t+1),s-1,t+1],
       line_parameters=[P["Vl"],t*(s+1),t-1,s+1],
       distinct_nonincident_projections=len(P["projection"]),
       both_source_SRG_checked_directly=True)


def min_labels(V):
    a=2
    while comb(a,2)<V:
        a+=1
    return a,tuple(combinations(range(a),2))[:V]


def model(kind,scheme="lex"):
    G=structure(geometry(kind)); Vp,Vl=G["Vp"],G["Vl"]
    aP,fp=min_labels(Vp);aL,gp=min_labels(Vl)
    if scheme=="lex":
        f=fp;g=gp
    elif scheme=="reverse":
        f=fp;g=gp[::-1]
    elif scheme=="correlated":
        def step(v):
            return next(k for k in range(2,v) if gcd(k,v)==1)
        sf,sg=step(Vp),step(Vl)
        f=tuple(fp[(sf*i+1)%Vp] for i in range(Vp))
        g=tuple(gp[(sg*i+3)%Vl] for i in range(Vl))
    else:
        raise ValueError("unknown map correlation")
    assert len(set(f))==Vp and len(set(g))==Vl
    return dict(G,kind=kind,scheme=scheme,aP=aP,aL=aL,a=max(aP,aL),
        f=f,g=g,point_by_pair={z:i for i,z in enumerate(f)},
        line_by_pair={z:i for i,z in enumerate(g)})


def adversarial_anchor_damage(m,Z):
    Z=set(Z)
    if any(type(i) is not int or i<0 or i>=len(m["flags"]) for i in Z):
        raise ValueError("only actual original flag IDs may be deleted")
    s,t=m["s"],m["t"]
    direct=set()
    for (q,r),(p,ell) in m["projection"].items():
        a={m["flag_to_id"][z] for z in ((q,ell),(p,ell),(p,r))}
        if a&Z:
            direct.add((q,r))
    expanded=set()
    for i in Z:
        p,l=m["flags"][i]
        L=m["lines"][l]
        left={(p,r) for foot in L if foot!=p for r in m["on"][foot] if r!=l}
        mid={(q,r) for q in L if q!=p for r in m["on"][p] if r!=l}
        right={(q,l) for ell in m["on"][p] if ell!=l
               for q in m["lines"][ell] if q!=p}
        assert len(left)==len(mid)==len(right)==s*t
        assert not (left&mid or left&right or mid&right)
        expanded.update(left|mid|right)
    assert direct==expanded
    assert len(direct)<=3*s*t*len(Z)
    return len(direct),4*len(direct)


def collinearity_conflict_certificate(m):
    """Direct flag conflict set equals independent typed collinearity census."""
    n=len(m["flags"]);P=m["Vp"];L=m["Vl"]
    def grouped(which):
        d=defaultdict(list)
        for i,(p,l) in enumerate(m["flags"]):
            d[(p,l)[which]].append(i)
        return d
    J=set()
    for p,ids in grouped(0).items():
        for i,j in combinations(ids,2):
            a=m["flags"][i][1];b=m["flags"][j][1]
            if set(m["g"][a])&set(m["g"][b]):
                J.add((i,j))
    for ell,ids in grouped(1).items():
        for i,j in combinations(ids,2):
            a=m["flags"][i][0];b=m["flags"][j][0]
            if set(m["f"][a])&set(m["f"][b]):
                J.add((i,j))
    ecolf=sum(bool(set(m["f"][p])&set(m["f"][q]))
              for p in range(P) for q in m["neighbors"][p] if p<q)
    line_adj=[set() for _ in range(L)]
    for ls in m["on"]:
        for a in ls:
            line_adj[a].update(ls-{a})
    ecolg=sum(bool(set(m["g"][a])&set(m["g"][b]))
              for a in range(L) for b in line_adj[a] if a<b)
    assert len(J)==ecolf+ecolg

    def grams(labels,neighbors,theta,k,mu,e_col):
        V=len(labels)
        counts=Counter(x for p in labels for x in p)
        q=sum(sum(x in labels[q] for q in neighbors[p])**2
              for x in counts for p in range(V))
        rhs=2*V*(k-mu)+2*(theta-mu)*e_col+mu*sum(d*d for d in counts.values())
        assert q==rhs
        return q
    gf=grams(m["f"],m["neighbors"],m["s"]-1,m["s"]*(m["t"]+1),
             m["t"]+1,ecolf)
    gg=grams(m["g"],line_adj,m["t"]-1,m["t"]*(m["s"]+1),
             m["s"]+1,ecolg)
    r=min(m["s"],m["t"]);b=ceil(Q(max(m["s"],m["t"]),r))
    led=balanced_ledger(b)
    assert ecolf<=led["typed_collinearity_conflict_upper"]*r**4
    assert ecolg<=led["typed_collinearity_conflict_upper"]*r**4
    assert len(J)<=led["combined_J_upper"]*r**4
    assert gf*gf<=led["pencil_square_upper"]**2*r**11
    assert gg*gg<=led["pencil_square_upper"]**2*r**11
    return dict(J=len(J),e_col_point=ecolf,e_col_line=ecolg,
                G_point=gf,G_line=gg,unequal_typed_Gram_identity_checked=True)


@lru_cache(maxsize=8)
def finite_case(kind,scheme="lex"):
    m=model(kind,scheme);N=len(m["flags"])
    structural=strongly_regular_data(geometry(kind))
    spectral=collinearity_conflict_certificate(m)
    full=frozenset(range(N))
    # Genuine original labels are unchanged under the deletion mask.
    # W34's full 425-owner census was independently established in #791;
    # here only a bounded but still genuine original subgeometry is enumerated.
    A=full if kind!="W34" else frozenset(i for i in full if i%3==0)
    pd=physical_d6(m,A);sd=source_first_d6(m,A)
    assert pd==sd
    pb=physical_bbo(m,A);sb=source_first_bbo(m,A)
    assert pb==sb
    assert not (set(pd)&set(pb))
    masks={"none":set(),"one":{0},
           "point_star":{i for i,(p,l) in enumerate(m["flags"]) if p==0},
           "line_star":{i for i,(p,l) in enumerate(m["flags"]) if l==0},
           "mixed":{i for i,(p,l) in enumerate(m["flags"]) if p==0 or l==0},
           "separated":{0,N//2}}
    checks=[]
    for name,Z in masks.items():
        damage,oriented=adversarial_anchor_damage(m,Z)
        assert oriented==4*damage<=12*m["s"]*m["t"]*len(Z)
        if name=="one":
            assert damage==3*m["s"]*m["t"]
        # Independent real deleted-flag physical oracle vs source-side
        # filtering of the full original finite six-ID family.
        live=A-Z
        d=physical_d6(m,live)
        b=physical_bbo(m,live)
        assert d=={k:v for k,v in sd.items() if not (set(k)&Z)}
        assert b=={k:v for k,v in sb.items() if not (set(k)&Z)}
        packing=greedy_pack(set(d)|set(b))
        assert all(set(k)<=live for k in packing)
        checks.append(dict(mask=name,removed=len(Z),
            damaged_nonincident_projections=damage,
            damaged_oriented_endpoint_pairs=oriented,
            surviving_D6=len(d),surviving_produced_BBo=len(b),
            independent_censuses_agree=True,disjoint_packing=len(packing)))
    return dict(kind=kind,scheme=scheme,
      s=m["s"],t=m["t"],aP=m["aP"],aL=m["aL"],
      original_flags=N,structural=structural,spectral=spectral,
      D6=len(pd),produced_BBo=len(pb),
      all_source_first_physical_first_equal=True,
      masks=checks)


def certificate():
    ledgers=[balanced_ledger(b,c,d) for b,c,d in (
        (1,Q(1),Q(1)),(2,Q(1),Q(1)),(3,Q(7,3),Q(1,17)))]
    fixtures=[finite_case(z) for z in ("W32","W33","Qminus24",
                                         "dualQminus42","W34")]
    flow=flow_catalog()
    assert flow["palette"]==51 and flow["d6_alternating"]==5643
    assert min(flow["bbo_sign_counts"])>=5175
    return dict(schema=SCHEMA,issue=793,meta_issue=790,
       scientific_foundations=[230,791],
       base_main_sha="f4355154ee70ea6d776b1b5f320c2e174238603c",
       claim="BALANCED_GQ_RESILIENCE_PROOF_CANDIDATE_T1_T2",
       formal_ledgers=ledgers,finite_cases=fixtures,
       independent_GF5=flow,
       finite_checks_are_not_all_order_proof=True,
       no_existence_claim_for_arbitrary_s_t=True,
       no_T3_abstract_incidence_theorem=True,
       no_unrestricted_ASET_improvement=True,
       external_peer_review_received=False)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="gio003-generalized-gq-certificate.json")
    args=ap.parse_args()
    x=certificate()
    Path(args.out).write_text(json.dumps(x,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("GIO003_BALANCED_GQ_CERTIFICATE="+json.dumps(x,sort_keys=True))
