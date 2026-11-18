"""AA4-HEAVY-SRG-DENSITY: sharper all-h ORIGINAL HEAVY via true physical F.

Proof is in manuscript. Local finite cases use only the independent genuine
symplectic source constructor, NEVER historical heavy/selector/root calculators.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb, isqrt
import json

SCHEMA="mathlab.hyp105.heavy-srg-physical-density.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
H_FIXED=32
K_FIXED=10
ALPHA=(Q(1,64),Q(1,64),Q(15,16))
R_OLD=93312


def ceilq(q):
    if type(q) is not Q:
        raise TypeError("exact rational only")
    return -(-q.numerator//q.denominator)


def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative integer required")
    t=isqrt(n)
    return t+int(t*t<n)


def envelope(H):
    """Genuine GQ s>=2**H, H fixed EVEN >=8 BEFORE f/g."""
    if type(H) is not int or H<8 or H%2:
        raise ValueError("even source scale H>=8 required")
    M=(1+Q(1,2**(2*H)))*(1+Q(23,16*2**(H//2)))
    A=2*(1+Q(1,2**H))*(1+Q(1,2**(2*H)))+Q(23,4*2**(3*H//2))+Q(4,2**(3*H))
    lam=Q(1,16)
    reciprocal=32*A*(lam+4*M)/lam**2
    R=ceilq(reciprocal)
    if not (Q(1)<M<Q(35,32) and Q(2)<A<Q(9,4)
            and 0<R<R_OLD and Q(R)>=reciprocal):
        raise AssertionError("symbolic source/physical HEAVY envelope failed")
    return dict(H=H,M=M,A=A,lambda_heavy=lam,R=R,
                alpha_coeff=lam**2/(lam+4*M),
                selected_coeff=lam**2/(4*(lam+4*M)),
                density_coeff=lam**2/(32*A*(lam+4*M)))


def formal_root(H,K,C0,c0):
    """Conditional root using #775 LOW, re-deriving all constants independently.

    Published external ordinary C6 constants are existential, not these probes.
    """
    if type(K) is not int or K<0 or type(C0) is not Q or type(c0) is not Q:
        raise ValueError("exact K and external formal rationals only")
    if C0<1 or not (0<c0<=1):
        raise ValueError("inadmissible formal external graph constants")
    z=envelope(H)
    c=Q(7,8)-4*z["M"]/Q(K+1)
    if c<=0:
        raise ValueError("nonpositive source CORE from true J bound")
    # NEW: reuse the same sharp original minimal-alphabet a² < A_H*s³
    # in Blakley–Roy: W3 >= (4|C|)^3/a^4 > (4*c)^3/A_H²*s^6.
    # Parent #775 used the coarser 9/4 physical alphabet coefficient.
    w=(4*c)**3/(z["A"]**2)
    R=z["R"]
    T=ceilq(Q(17*R**3,2)*C0**3)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*ceil_sqrt(ceilq(Q(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    alpha=ALPHA
    thresholds=(ceilq(Q(111*T,2)/(alpha[0]*w)),
                ceilq((Q(E)/(alpha[1]*w))**2),
                ceilq((Q(D)/(alpha[2]*w))**8))
    s0=max(2**H,64,*thresholds)
    delta=c0/Q(R**6)
    bbo=w*(1-sum(alpha))/2
    if bbo<=delta:
        raise AssertionError("root minimax LOW margin lost")
    if not (Q(111*T,2)<=alpha[0]*w*s0 and
            Q(E)**2 <= (alpha[1]*w)**2*s0 and
            Q(D)**8 <= (alpha[2]*w)**8*s0):
        raise AssertionError("three LOW errors did not fit")
    return dict(H=H,K=K,R=R,T=T,L6=L6,L4=L4,B0=B0,E=E,D=D,
                q2=q2,q3=q3,core=c,W3_floor=w,
                delta=delta,BBo_floor=bbo,
                s0=s0,h0=(s0-1).bit_length(),
                threshold_coord=thresholds[0],
                threshold_endpoint=thresholds[1],
                threshold_mixed_blocker=thresholds[2],
                external_C6_numeric_constants_known=False,
                inherited_LOW_lemmas_independently_accepted=False,
                root_PROVED_A=False)


def _a(V):
    a=2
    while comb(a,2)<V:
        a+=1
    return a


def _e(u,v):
    if u==v:
        raise AssertionError("physical diagonal loop")
    return tuple(sorted((u,v)))


def original_heavy_case(s,mode,T=1):
    """Small-order genuine FULL GQ physical F construction and no-clone referee.

    T=1 is a diagnostic and NOT the astronomical theorem T from formal_root.
    All source f/g maps are separately globally pair-injective and complete.
    """
    if s not in (2,4) or type(T) is not int or T<1:
        raise ValueError("only genuine diagnostic W32/W34 with T>=1")
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    flags=tuple(genuine_symplectic_source(s))
    V=(s+1)*(s*s+1)
    a=_a(V)
    pairs=tuple(combinations(range(a),2))[:V]
    f=pairs
    if mode=="lex":
        g=pairs
    elif mode=="reverse":
        g=pairs[::-1]
    elif mode=="shift":
        g=pairs[7:]+pairs[:7]
    else:
        raise ValueError("unknown original correlated label mode")
    if len(set(f))!=V or len(set(g))!=V or len(flags)!=(s+1)*V:
        raise AssertionError("not full genuine injected ORIGINAL GQ")
    owners={}
    per=[]
    adj=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        x,z=f[p]; y,w=g[l]
        ee=(_e((x,y),(z,w)),_e((x,w),(z,y)))
        if len(set(ee))!=2 or set(ee[0])&set(ee[1]):
            raise AssertionError("not two disjoint opposite real diagonals")
        for edge in ee:
            if edge in owners:
                raise AssertionError("one physical edge owned by multiple original flags")
            owners[edge]=i
            u,v=edge
            adj[u].add(v); adj[v].add(u)
        per.append(ee)
    if len(owners)!=2*len(flags):
        raise AssertionError("missing original physical edges")
    Qheavy={v for v in adj if len(adj[v])>T*s}
    touch={e:i for e,i in owners.items() if set(e)&Qheavy}
    ids=sorted(set(touch.values()))
    if not ids or not Qheavy:
        raise AssertionError("diagnostic nonvacuous HEAVY fixture missing")
    if len(ids)*2<len(touch):
        raise AssertionError("distinct ORIGINAL heavy owners below E/2")
    # Literal source-pencil J, not a synthetic physical edge conflict graph.
    byp=defaultdict(list);byl=defaultdict(list)
    for i in ids:
        p,l=flags[i];byp[p].append(i);byl[l].append(i)
    J={i:set() for i in ids}
    for groups,side in ((byp,0),(byl,1)):
        for row in groups.values():
            for i,j in combinations(row,2):
                x=g[flags[i][1]] if side==0 else f[flags[i][0]]
                y=g[flags[j][1]] if side==0 else f[flags[j][0]]
                if set(x)&set(y):
                    J[i].add(j);J[j].add(i)
    edgesJ=sum(len(v) for v in J.values())//2
    remaining=set(ids);ind=[]
    while remaining:
        i=min(remaining,key=lambda k:(len(J[k]&remaining),k))
        ind.append(i)
        remaining.difference_update(J[i]|{i})
    if Q(len(ind))<Q(len(ids)**2,len(ids)+2*edgesJ):
        raise AssertionError("diagnostic Caro-Wei witness below Jensen lower")
    if any(j in J[i] for i,j in combinations(ind,2)):
        raise AssertionError("source pencil J independence false")
    selected=tuple(ind)
    colors=[]
    for side,lab in ((0,f),(1,g)):
        bits={}
        def score():
            return sum((2*int(bits[x]!=bits[y]) if x in bits and y in bits else 1)
                       for i in selected for x,y in (lab[flags[i][side]],))
        last=len(selected)
        for symbol in range(a):
            bits[symbol]=0
            c0=score()
            bits[symbol]=1
            c1=score()
            bits[symbol]=0 if c0>=c1 else 1
            new=score()
            if new<last:
                raise AssertionError("conditional expected retained owners dropped")
            last=new
        nextsel=tuple(i for i in selected
                      if bits[lab[flags[i][side]][0]]!=bits[lab[flags[i][side]][1]])
        if 2*len(nextsel)<len(selected):
            raise AssertionError("cut kept less than half of WHOLE source owners")
        selected=nextsel
        colors.append(bits)
    if not selected:
        raise AssertionError("both cuts removed original heavy owners")
    for i in selected:
        p,l=flags[i]
        if colors[0][f[p][0]]==colors[0][f[p][1]] or colors[1][g[l][0]]==colors[1][g[l][1]]:
            raise AssertionError("typed physical cut violated")
    selected_graph={e:owners[e] for i in selected for e in per[i]}
    if len(selected_graph)!=2*len(selected):
        raise AssertionError("source owner lost paired diagonals")
    witnesses=[]
    for i in selected:
        options=[(e,v) for e in per[i] for v in e if v in Qheavy]
        if not options:
            raise AssertionError("source owner lost genuine heavy edge witness")
        edge,v=min(options)
        witnesses.append((i,edge,v))
    bit=0 if sum(colors[0][v[0]]==0 for _,_,v in witnesses)*2>=len(witnesses) else 1
    Rset={v for v in Qheavy if colors[0][v[0]]==bit}
    r=len(Rset)
    if not r:
        raise AssertionError("no actual heavy root corner")
    Yset=sorted({v for edge in selected_graph for v in edge
                 if colors[0][v[0]]!=bit
                 and any(u in Rset for u in edge)})
    if not Yset:
        raise AssertionError("no actual opposite physical endpoints")
    blocks=[set(Yset[i:i+r]) for i in range(0,len(Yset),r)]
    scored=[(sum((u in Rset and v in B) or (v in Rset and u in B)
                 for u,v in selected_graph),idx)
            for idx,B in enumerate(blocks)]
    m,chosen=max(scored)
    Fedges={e:source for e,source in selected_graph.items()
            if (e[0] in Rset and e[1] in blocks[chosen])
            or (e[1] in Rset and e[0] in blocks[chosen])}
    if m!=len(Fedges):
        raise AssertionError("real physical F is not the chosen block")
    vF=len(Rset)+len(blocks[chosen])
    if not (0<m and vF<=2*r and vF<=2*len(Qheavy) and
            8*a*a*m >= len(selected)*vF
            and 4*a*a*m >= len(selected)*r
            and all(e in owners and owners[e]==src and src in selected for e,src in Fedges.items())):
        raise AssertionError("real F missing no-clone HEAVY density certificate")
    return dict(s=s,scheme=mode,diagnostic_T=T,original_flags=len(flags),
                physical_full_edges=len(owners),physical_Q_vertices=len(Qheavy),
                real_heavy_edges=len(touch),heavy_unique_owners=len(ids),
                source_J_edges=edgesJ,independent_owners=len(ind),
                after_two_cuts_owners=len(selected),physical_selected_edges=len(selected_graph),
                true_F_edges=m,true_F_vertices=vF,source_pair_alphabet=a,
                F_density=str(Q(m,vF)),
                direct_source_density=str(Q(len(selected),8*a*a)),
                real_F_no_clone=True,source_J_independent=True,
                retains_both_original_diagonals_before_F=True)


def canonical_certificate():
    env=envelope(H_FIXED)
    rows=[original_heavy_case(s,mode) for s in (2,4)
          for mode in ("lex","reverse","shift")]
    probes=[]
    for C0,c0 in ((Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17))):
        b=formal_root(H_FIXED,K_FIXED,C0,c0)
        probes.append(dict(C0_FORMAL=str(C0),c0_FORMAL=str(c0),
                           R=b["R"],K=b["K"],h0=b["h0"],
                           delta=str(b["delta"]),BBo=str(b["BBo_floor"]),
                           numeric_constants_verified=False))
    return dict(schema=SCHEMA,issue=230,parent_pr=775,head_scope="Z_EMPTY",
                status=ROOT_STATUS,root_PROVED_A=False,ASET_claimed=False,
                H=env["H"],new_R=env["R"],previous_R=R_OLD,
                M_H=str(env["M"]),A_H=str(env["A"]),
                improved_D6_coefficient_factor=str(Q(R_OLD,env["R"])**6),
                all_h_HEAVY_no_clone_density_proof_in_manuscript=True,
                physical_label_maps_arbitrarily_correlated_in_theorem=True,
                external_C6_numerical_constants_NOT_established=True,
                inherited_LOW_lemma_acceptance_still_open=True,
                genuine_original_finite_cases=rows,
                formal_not_published_graph_probes=probes)


if __name__=="__main__":
    print("AA4_HEAVY_SRG_PHYSICAL_DENSITY_CERTIFICATE="+json.dumps(
        canonical_certificate(),sort_keys=True,separators=(",",":")))
