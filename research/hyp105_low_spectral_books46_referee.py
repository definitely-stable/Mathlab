"""HYP-105 #230: independent original W(3,s) mixed-book spectral 46 referee.

The all-h proof is in the accompanying manuscript. This module checks its
exact rational coefficient and rebuilds the TRUE original W32/W34
FULL-A/CORE-C books, source SRGs, Gram energies and physical trace from scratch.
Only the independent *geometry fixture* of the frozen parent #784 is imported;
NO previous spectral, book, root, Jensen or four-blocker algorithm is imported.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json

from hyp105_low_publication_partition_referee import model, endpoint_status

SCHEMA = "mathlab.hyp105.low-spectral-books46-publication.v1"
STATUS = "OPEN_WITH_FORMAL_BLOCKER"
PARENT = 784
H = 32
K = 10
R = 33281


def qceil(x):
    if type(x) is not F:
        raise TypeError("exact Fraction required")
    return -(-x.numerator // x.denominator)


def sqrt_ceil(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative exact integer required")
    r = isqrt(n)
    return r + (r*r != n)


def all_h_bound():
    """Prove by polynomial monotonicity for ALL s=2^h>=2^32, fixed f/g.

    Original strongly regular collinearity matrix A obeys
    A²=(s²-1)I-2A+(s+1)J.  For each typed map f, put
    d_x=number of ORIGINAL factors carrying physical symbol x and
    G_f=sum_(p,x) [# original collinear factors q with x in f(q)]².
    G_f=2V(s²-1)-4e_col(f)+(s+1)sum_x d_x²
       <=2V(s²-1)+2V(s+1)(a-1).
    Minimal a and sqrt(2V/s³)<10/7 imply
       a-1 < (10/7)s^(3/2)+1.
    Thus, with u=1/s and t=1/sqrt(s),
       G_f/s^(11/2) < 2v[t+(1+u)(10/7+t³)]
       v=(1+u)(1+u²).
    Independently source book:
       Bx² <=16(s+1)(K+1)|A| Delta G_f,
    and for ROOT A=I: |A|<=nu*s4, Delta<=T*s.
    All terms nonnegative and monotone in u,t, so Bx²/
       [(K+1)*T*s^(23/2)]
       < 32(1+u) nu v [t+(1+u)(10/7+t³)].
    Evaluate at u<=2^-32, t<=2^-16: <46. Dual g identical.
    """
    u = F(1,2**32)
    t = F(1,2**16)
    v = (1+u)*(1+u*u)
    nu = (1+u)**2*(1+u*u)
    sqrt_margin = F(10,7)**2-2*v
    bound = 32*(1+u)*nu*v*(t+(1+u)*(F(10,7)+t**3))
    if not (sqrt_margin>0 and 45<bound<46):
        raise AssertionError("exact GQ Gram 46 coefficient failed")
    return dict(
        fixed_H=H,
        strict_sqrt_2V_bound_margin=str(sqrt_margin),
        exact_Gf_s11_2_coefficient_bound=str(
            2*v*(t+(1+u)*(F(10,7)+t**3))),
        exact_Bx_squared_coefficient_bound=str(bound),
        certified_book_squared_integer_coefficient=46,
        inherited_previous_book_squared_integer_coefficient=360,
        original_GQ_nonprincipal_positive_eigenvalue="s-1",
        valid_all_dyadic_s_at_least_2_to_32=True,
        arbitrary_fixed_correlated_global_f_g=True,
        root_only_Z_empty_core_degree_K_at_most_10=True,
        external_graph_C6_constants_numeric_unknown=True,
        root_PROVED_A=False)


def original_collinear(m):
    """Independent dual point/line original simple collinearity graphs."""
    V=m["V"]
    pc=[set() for _ in range(V)]
    lc=[set() for _ in range(V)]
    pts=[set() for _ in range(V)]
    for ell, orig_line in enumerate(m["lines"]):
        L=set(orig_line)
        for p in orig_line:
            pc[p].update(L-{p})
            pts[p].add(ell)
    for lines_through in pts:
        for a,b in combinations(sorted(lines_through),2):
            lc[a].add(b)
            lc[b].add(a)
    s=m["s"]
    for graph in (pc,lc):
        if any(len(z)!=s*(s+1) for z in graph):
            raise AssertionError("actual original GQ SRG degree mismatch")
        for p in range(V):
            for q in range(p+1,V):
                actual=len(graph[p]&graph[q])
                expected=s-1 if q in graph[p] else s+1
                if actual!=expected:
                    raise AssertionError("actual original dual GQ lambda/mu mismatch")
    return (pc,lc)


def grams(labels, col, s):
    """Independent direct SRG Gram and separate source incidence identity."""
    V=len(labels)
    fibres=defaultdict(set)
    for p,pair in enumerate(labels):
        if len(set(pair))!=2:
            raise AssertionError("bad typed original physical pair")
        for x in pair:
            fibres[x].add(p)
    if len(set(labels))!=V:
        raise AssertionError("noninjective complete original f/g")
    d2=sum(len(v)**2 for v in fibres.values())
    energy=0
    e_col=0
    for x,pids in fibres.items():
        for p in range(V):
            c=len(col[p]&pids)
            energy+=c*c
        e_col+=sum(len(col[p]&pids) for p in pids)//2
    formula=2*V*(s*s-1)-4*e_col+(s+1)*d2
    if energy!=formula:
        raise AssertionError("source-first and direct GQ SRG-Gram disagree")
    a=max(x for pair in labels for x in pair)+1
    if d2>2*V*(a-1):
        raise AssertionError("original complete pair fibre occupancy violation")
    if energy>2*V*(s*s-1)+2*V*(s+1)*(a-1):
        raise AssertionError("universal original source SRG Gram cap violated")
    return dict(d2=d2,e_col=e_col,G=energy,formula=formula,
                fibre_count=len(fibres),max_fibre=max(map(len,fibres.values())),
                spectrum_upper=2*V*(s*s-1)+2*V*(s+1)*(a-1)), fibres


def full_source_degrees(m):
    """Actual physical degrees of FULL allowed A and smaller paired C."""
    degA=Counter()
    degC=Counter()
    for flag in m["flags"]:
        if flag in m["z"]:
            continue
        p,ell=flag
        for x in m["f"][p]:
            for y in m["g"][ell]:
                degA[x,y]+=1
                if flag in m["C"]:
                    degC[x,y]+=1
    return degA,degC


def actual_source_conflict_max(m):
    """TRUE original owner J_C only; do not assert diagnostic K=10."""
    core=set(m["C"])
    neighbors={i:set() for i in core}
    byp=defaultdict(list)
    byl=defaultdict(list)
    for f in core:
        byp[f[0]].append(f)
        byl[f[1]].append(f)
    for keys,side in ((byp,0),(byl,1)):
        for entries in keys.values():
            for a,b in combinations(entries,2):
                intersect=(set(m["g"][a[1]])&set(m["g"][b[1]])
                           if side==0 else
                           set(m["f"][a[0]])&set(m["f"][b[0]]))
                if intersect:
                    neighbors[a].add(b)
                    neighbors[b].add(a)
    return max((len(x) for x in neighbors.values()),default=0)


def source_book(m, side, col, G, Kc, degA, degC):
    """Independent source-FIRST mixed source book B, F1, F2 and Theta.

    side=0 original POINT primary f (y=original second-symbol);
    side=1 original LINE primary g (x=original first-symbol).
    All A owners, including GQ anchors, remain separate from CORE C.
    """
    s=m["s"]
    V=m["V"]
    A=[flag for flag in m["flags"] if flag not in m["z"]]
    C=set(m["C"])
    prim=m["f"] if side==0 else m["g"]
    sec=m["g"] if side==0 else m["f"]
    RA=[Counter() for _ in range(V)]
    RC=[Counter() for _ in range(V)]
    have=set()
    for p,ell in A:
        i,j=(p,ell) if side==0 else (ell,p)
        for sym in sec[j]:
            RA[i][sym]+=1
            if (p,ell) in C:
                RC[i][sym]+=1
                have.add(i)
    symbols=defaultdict(set)
    for i,lab in enumerate(prim):
        for x in lab:
            symbols[x].add(i)
    Bx=F1=F2=Theta=0
    maxK=0
    for u in sorted(have):
        for x,k in ((prim[u][0],prim[u][1]),
                    (prim[u][1],prim[u][0])):
            for p in symbols[k]:
                c=len(col[p]&symbols[x])
                z=sum(n*RC[u].get(y,0) for y,n in RA[p].items())
                maxK=max(maxK,z)
                Bx+=c*z
                F1+=c*c
                F2+=z*z
                Theta+=z
    physical_Theta=sum(d*degC.get(key,0) for key,d in degA.items())
    Delta=max(degC.values(),default=0)
    e=Counter()
    e["source_book_B"]=Bx
    e["F1"]=F1
    e["F2"]=F2
    e["Theta_source"]=Theta
    e["Theta_physical"]=physical_Theta
    e["max_mixed_entry"]=maxK
    e["Kc"]=Kc
    e["Delta"]=Delta
    if Theta!=physical_Theta:
        raise AssertionError("FULL-A/CORE-C physical/source cross contraction broken")
    if maxK>2*(s+1)*(Kc+1):
        raise AssertionError("original J CORE clique bound on K_AC broken")
    if F1>2*G:
        raise AssertionError("source-book F1 original SRG Gram failure")
    if F2>2*(s+1)*(Kc+1)*Theta:
        raise AssertionError("source-book F2 original pair conflict cap failure")
    if Theta>4*len(A)*Delta:
        raise AssertionError("FULL A physical degree contraction cap failure")
    if Bx*Bx>F1*F2:
        raise AssertionError("literal source B Cauchy inequality failure")
    if Bx*Bx>16*(s+1)*(Kc+1)*len(A)*Delta*G:
        raise AssertionError("uniform original source book bridge failure")
    return dict(e)


def physical_fourth_and_blockers(m, left_book, right_book):
    """Independent physical adjacency fourth trace and four blockers (no old book oracle)."""
    adj=m["adj"]
    d=max((len(v) for v in adj.values()),default=0)
    a2=Counter()
    for u,neigh in adj.items():
        for v in neigh:
            for w in adj[v]:
                a2[u,w]+=1
    tr4=sum(c*c for c in a2.values())
    I=[0,0,0,0]
    union=0
    for u,neigh in adj.items():
        for v in neigh:
            for w in adj[v]:
                for t in adj[w]:
                    path=(u,v,w,t)
                    if (len({z[0] for z in path})!=4 or
                        len({z[1] for z in path})!=4):
                        continue
                    st,info=endpoint_status(m,u,t)
                    if st!="good":
                        continue
                    q,r,p,ell,_=info
                    mask=(v[0] in m["f"][p],w[0] in m["f"][p],
                          v[1] in m["g"][ell],w[1] in m["g"][ell])
                    for i,on in enumerate(mask):
                        I[i]+=bool(on)
                    union+=any(mask)
    if I[0]!=I[1] or I[2]!=I[3]:
        raise AssertionError("original point and line physical blocker reversal broken")
    Bx=left_book["source_book_B"]
    By=right_book["source_book_B"]
    for idx,b in ((0,Bx),(1,Bx),(2,By),(3,By)):
        if I[idx]**2>b*d*tr4:
            raise AssertionError("source-book physical fourth-moment blocker failed")
    if union>sum(I):
        raise AssertionError("four source blocker union was not bounded")
    return dict(actual_trace_A4=tr4,actual_Delta=d,
                four_blocker_cardinalities=I,
                four_blocker_union=union,
                point_source_Bx=Bx,line_source_By=By)


def scenario(s, scheme, core):
    m=model(s,scheme,core)  # ONLY geometry fixture from independent parent
    pc,lc=original_collinear(m)
    gp,_=grams(m["f"],pc,s)
    gl,_=grams(m["g"],lc,s)
    da,dc=full_source_degrees(m)
    kc=actual_source_conflict_max(m)
    bx=source_book(m,0,pc,gp["G"],kc,da,dc)
    by=source_book(m,1,lc,gl["G"],kc,da,dc)
    phys=physical_fourth_and_blockers(m,bx,by)
    return dict(s=s,scheme=scheme,core=core,
                source_Gf=gp,source_Gg=gl,source_JC_max_degree=kc,
                true_original_A_size=len(m["flags"])-len(m["z"]),
                true_paired_C_size=len(m["C"]),
                true_physical_A_C_cross_Theta=sum(da[v]*dc.get(v,0) for v in da),
                point_book=bx,line_book=by,physical=phys)


def exact_root_formal(C0,c0):
    """Only FORMAL unknown ordinary C6 graph constants; calculate improvement."""
    if type(C0) is not F or type(c0) is not F or C0<1 or not (0<c0<=1):
        raise ValueError("C0/c0 are unknown published graph theorem constants")
    u=F(1,2**H)
    M=(1+u*u)*(1+F(23,16*2**(H//2)))
    nu=(1+u)**2*(1+u*u)
    A=(2*(1+u)*(1+u*u)
       +F(23,4*2**(3*H//2))+F(4,2**(3*H)))
    c=F(7,8)-4*M/(K+1)
    w=(4*c)**3/A**2
    if c<=0 or w<=0:
        raise AssertionError("original true LOW surviving CORE lower bound lost")
    T=qceil(F(17*R**3,2)*C0**3)
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L6=24+qceil(36*nu*T*T)
    L4=q2*q2*sqrt_ceil(qceil(nu*L6))+17*T
    old_book=sqrt_ceil(360*(K+1)*T)
    new_book=sqrt_ceil(46*(K+1)*T)
    old_endpoint=5*q3*sqrt_ceil(L6)
    new_endpoint=q3*sqrt_ceil(17*L6)
    old_blockers=4*sqrt_ceil(old_book*T*L4)
    new_blockers=4*sqrt_ceil(new_book*T*L4)
    a1=F(1,64)
    a2=F(1,64)
    a3=F(15,16)
    universal_floor=qceil(F(49*T)/(a1*w))
    def threshold(E,D):
        return max(2**H,64,universal_floor,
                   qceil((F(E)/(a2*w))**2),
                   qceil((F(D)/(a3*w))**8))
    prev=threshold(old_endpoint,old_blockers)
    new=threshold(new_endpoint,new_blockers)
    h_prev=(prev-1).bit_length()
    h_new=(new-1).bit_length()
    if (not new_book<old_book or not new_endpoint<old_endpoint
            or not new_blockers<old_blockers or new>=prev
            or h_new>h_prev):
        raise AssertionError("strict original LOW book threshold improvement lost")
    delta=c0/F(R**6)
    if not w/64>delta:
        raise AssertionError("formal original root LOW floor does not dominate HEAVY")
    return dict(C0_FORMAL_UNKNOWN=str(C0),c0_FORMAL_UNKNOWN=str(c0),
        R=R,root_K=K,fixed_H=H,
        common_global_source_T=str(T),
        book_B0_historical_360=str(old_book),
        book_B0_NEW_46=str(new_book),
        L6=str(L6),L4=str(L4),
        endpoint_coefficient_old_24=str(old_endpoint),
        endpoint_coefficient_NEW_17=str(new_endpoint),
        fourblocker_D_old=str(old_blockers),
        fourblocker_D_NEW=str(new_blockers),
        root_previous_h0=h_prev,root_NEW_h0=h_new,
        dyadic_h_gained=h_prev-h_new,
        numeric_external_graph_constants_known=False,
        original_ROOT_PROVED_A=False)


def certificate():
    cases=[]
    for s in (2,4):
        for scheme,core in (("lex","full"),("reverse","full"),
                            ("correlated","full"),("lex","even"),
                            ("reverse","deleted")):
            cases.append(scenario(s,scheme,core))
    return dict(schema=SCHEMA,status=STATUS,issue=230,parent_pr=PARENT,
                new_all_h_original_source_Gram_book_46=all_h_bound(),
                genuine_original_independent_source_books=cases,
                FORMAL_external_C6_constants_scenarios=[
                    exact_root_formal(*p) for p in
                    ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17)))],
                independent_FULL_A_not_equal_CORE_C=True,
                independent_original_JC_K_observed_not_assumed_10=True,
                low_selector_expected_moments_inherited_not_independently_refereed=True,
                global_HYP105_root_PROVED_A=False)


if __name__=="__main__":
    print("AA4_LOW_SPECTRAL_BOOKS46_CERTIFICATE="+
          json.dumps(certificate(),sort_keys=True,separators=(",",":")))
