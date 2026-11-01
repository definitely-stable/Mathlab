"""AA4-MIXENERGY: new exact source collinearity-energy / FULL-CORE Cauchy referee.

All-h ORIGINAL symplectic GQ incidence identity
 A_P^2=(s^2-1)I-2A_P+(s+1)J
forces, for ANY fixed complete globally injected original f:
  Gamma_f = sum_x ||A_P 1_{S_x}||^2
          = 2V(s²-1) - 4 M_f + (s+1)*sum_x |S_x|².
Original source point/line books M_f are not assumed independent of
physical labels or CORE.

The ORIGINAL mixed FULL/CORE first-CS factor F1 is exactly an occupancy-
weighted part of Gamma, with weights 0,1,2. Thus F1<=2Gamma_f.
For dyadic s>=64, a<=97/64 s sqrt(s) and
 F1<= 7*s^(11/2)   (historical 64*s^(11/2)).
Combine unchanged F2<=32(K+1)T s^6 to obtain
 B<=15 sqrt((K+1)T) s^(23/4), vs historical 64 sqrt.
Original maximal physics and external graph constants unchanged.

Finite module constructs TRUE W32/W34 original point-line incidence
from genuine_source only, never imports previous mixed-blocker/spectral
code. Independently computes source collinearity squared energy as
actual C1_S coordinate matrix, full original M_f, exact source
tensor F1/F2/Phi, and Cauchy/degree-product chain; reconstructs
source FIRST mixed blocker triples and checks Phi-Psi=unique triples.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt

from hyp105_full_physical_degree_tail import genuine_source


def _minimal_a(V):
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def allh_original_mixed_energy_envelope(s):
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("dyadic actual W(3,s) s>=64 required")
    V=(s+1)*(s*s+1)
    a=_minimal_a(V)
    d=s+1
    if (64*a)**2 > 97**2*s**3:
        raise AssertionError("all-h minimal alphabet envelope fails")
    # Exact proof with u=1/sqrt(s)<=1/8:
    # V/s^3 <=(65/64)*(4097/4096), d/s<=65/64,
    # (a-1)/(s sqrt(s))<=97/64. No floating point.
    R=Fraction(65,64)*Fraction(4097,4096)
    C=4*R/Fraction(8)+4*Fraction(65,64)*R*Fraction(97,64)
    if C>=7:
        raise AssertionError("all-h exact envelope not below seven")
    return {
        "s":s,"V":V,"a_minimal":a,"d":d,
        "exact_rational_all_h_coeff_bound":C,
        "new_first_mixed_CS_factor_F1_upper_coefficient":7,
        "historical_F1_upper_coefficient":64,
        "F2_original_unchanged_coefficient":32,
        "new_B0_multiplier":15,
        "historical_B0_multiplier":64,
        "new_B0_over_old":Fraction(15,64),
        "new_internal_error_over_old":None,
        "source_book_energy_anti_correlation":True,
        "all_h_proof_not_a_finite_numerical_extrapolation":True,
    }


def _check_input(power,f,g,ids):
    if type(power) is not int or power not in (1,2):
        raise ValueError("real W32/W34 only for independent finite referee")
    s,V,flags=genuine_source(power)
    a=_minimal_a(V)
    legal=set(combinations(range(a),2))
    try: f=tuple(tuple(p) for p in f);g=tuple(tuple(p) for p in g)
    except (TypeError,ValueError):
        raise ValueError("complete ORIGINAL factor pair maps missing")
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
        or any(p not in legal for p in f+g)):
        raise ValueError("complete original typed pair injection in MINIMAL alphabet")
    core=tuple(range(len(flags))) if ids is None else tuple(ids)
    if len(set(core))!=len(core) or any(
        type(i) is not int or i<0 or i>=len(flags) for i in core):
        raise ValueError("CORE must contain genuine distinct original incidence IDs")
    return s,V,flags,a,f,g,core


def original_mixed_source_energy_referee(power,f,g,core_ids=None):
    s,V,flags,a,f,g,I=_check_input(power,f,g,core_ids)
    pencils=[set() for _ in range(V)]
    lines=[set() for _ in range(V)]
    lookup={}
    for i,(p,l) in enumerate(flags):
        if (p,l) in lookup:raise AssertionError("duplicated ORIGINAL source incidence")
        lookup[p,l]=i;pencils[p].add(l);lines[l].add(p)
    col=[set().union(*(lines[l] for l in pencils[p]))-{p} for p in range(V)]
    if any(len(c)!=s*(s+1) for c in col):
        raise AssertionError("genuine original collinearity valency invalid")
    # Independently verify source GQ SRG identity on ALL ordered points.
    for p in range(V):
        for q in range(V):
            want=(s*(s+1) if q==p else
                  (s-1 if q in col[p] else s+1))
            if len(col[p]&col[q])!=want:
                raise AssertionError("true original GQ collinearity A² axiom violated")
    S=[set() for _ in range(a)]
    for p,(x,z) in enumerate(f):
        S[x].add(p);S[z].add(p)
    star_sizes=tuple(map(len,S))
    if sum(star_sizes)!=2*V or max(star_sizes)>a-1:
        raise AssertionError("original point pair-label star populations invalid")
    Cx=[[len(col[p]&S[x]) for p in range(V)] for x in range(a)]
    gamma=sum(z*z for row in Cx for z in row)
    # Completely independent ORIGINAL f-book, line-pencil collision population.
    Mf=0
    for ell in range(V):
        freq=Counter(coord for p in lines[ell] for coord in f[p])
        Mf+=sum(comb(v,2) for v in freq.values())
    # Independent combinatorial point-pair-major original collinearity book.
    m_pair=sum(bool(set(f[p])&set(f[q])) for p in range(V) for q in col[p])//2
    if Mf!=m_pair:
        raise AssertionError("original point-pair-major book differs from source line-pencil book")
    gamma_formula=2*V*(s*s-1)-4*Mf+(s+1)*sum(k*k for k in star_sizes)
    if gamma!=gamma_formula:
        raise AssertionError("NEW original spectral collinearity energy exact formula false")
    # Source-first FULL and selected CORE physical right coordinate pencils.
    R=[Counter() for _ in range(V)]
    R0=[Counter() for _ in range(V)]
    for i,(p,l) in enumerate(flags):
        R[p].update(g[l])
    for i in I:
        p,l=flags[i];R0[p].update(g[l])
    if any(sum(row.values())!=2*(s+1) for row in R):
        raise AssertionError("full original source pencil line count not regular")
    # Both physical diagonals, ACTUAL unique source owner.
    graph=defaultdict(set)
    owner={}
    for i in I:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=frozenset((u,v))
            if e in owner:raise AssertionError("two original IDs share physical edge")
            owner[e]=i;graph[u].add(v);graph[v].add(u)
    if len(owner)!=2*len(I):
        raise AssertionError("source original flag paired physical diagonals lost")
    Delta=max((len(z) for z in graph.values()),default=0)
    # Matrix K=R_full * R_CORE^T. Both FULL and CORE really share
    # exact source y symbols; no assumption anchor p retained in CORE.
    K={}
    for p in range(V):
        for u in range(V):
            if not R0[u]:
                continue
            val=sum(v*R0[u][y] for y,v in R[p].items())
            if val:K[p,u]=val
    phi=F1=F2=Ksum=0
    # Source-oriented EXACT outer contraction; each occupied f(u) has
    # two orientations (x,k), and p in S_k. Cf1 original collinearity.
    for u,(a0,b0) in enumerate(f):
        for x,k in ((a0,b0),(b0,a0)):
            for p in S[k]:
                c=Cx[x][p]
                z=K.get((p,u),0)
                phi+=c*z
                F1+=c*c
                F2+=z*z
                Ksum+=z
    if F1>2*gamma:
        raise AssertionError("mixed first Cauchy energy exceeds 2 original C-energy")
    # Exact source-side FULL/CORE physical corner degrees, including
    # ALL a*a grid cells, not a subset determined by original flags.
    degree_product=0
    totalfull=totalcore=0
    for x in range(a):
        for y in range(a):
            df=sum(R[p][y] for p in S[x])
            dc=sum(R0[p][y] for p in S[x])
            degree_product+=df*dc
            totalfull+=df
            totalcore+=dc
    if (Ksum!=degree_product or totalfull!=4*(s+1)*V
        or totalcore!=4*len(I) or Ksum>Delta*totalfull):
        raise AssertionError("independent original mixed FULL/CORE degree-product identity failed")
    # Independently enumerate full-source nonincident projection
    # records, with the actual CORE first physical edge, NO K tensor.
    Psi=0
    triples=set()
    for i in I:
        u,lam=flags[i]
        for x,k in ((f[u][0],f[u][1]),(f[u][1],f[u][0])):
            for y,t in ((g[lam][0],g[lam][1]),(g[lam][1],g[lam][0])):
                for p in S[k]:
                    for q in S[x]&col[p]:
                        z=f[q][0] if f[q][1]==x else f[q][1]
                        for r in pencils[p]:
                            if y not in g[r]:continue
                            if r in pencils[q]:
                                Psi+=1
                                continue
                            w=g[r][0] if g[r][1]==y else g[r][1]
                            triples.add(((x,y),(k,t),(z,w)))
    if phi-Psi!=len(triples):
        raise AssertionError("FULL/CORE phi-psi is not real source nonincident triple count")
    # Unconditional exact Cauchy bounds, then unaltered source max cap.
    if phi*phi>F1*F2 or F1<0 or F2<0:
        raise AssertionError("independent original mixed FULL/CORE Cauchy failed")
    corecap=max((v for row in R0 for v in row.values()),default=0)
    maxK=max(K.values(),default=0)
    if (maxK>2*(s+1)*corecap or F2>maxK*Ksum):
        raise AssertionError("source mixed FULL/CORE K cap failed")
    deficit=(2*gamma-F1)
    if deficit<0:raise AssertionError("source pair-star index loss negative")
    return {
        "s":s,"V":V,"a":a,"original_core_source_IDs":len(I),
        "original_pencil_book_Mf":Mf,
        "source_f_coordinate_stars":star_sizes,
        "source_collinearity_squared_energy":gamma,
        "source_collinearity_exact_anti_book_formula":gamma_formula,
        "original_source_first_factor_F1":F1,
        "source_index_restriction_loss":deficit,
        "original_mixed_second_factor_F2":F2,
        "original_mixed_phi":phi,
        "original_mixed_incident_psi":Psi,
        "actual_source_mixed_nonincident_blocker_triples":len(triples),
        "source_book_kernel_full_core_cross_Ksum":Ksum,
        "independent_physical_corner_degree_product":degree_product,
        "actual_true_original_both_diagonals":len(owner),
        "physical_max_degree":Delta,
        "actual_core_pencil_coordinate_cap":corecap,
        "actual_mixed_K_max":maxK,
        "exact_source_formula_passed":True,
        "exact_direct_first_cauchy_passed":True,
        "original_full_core_not_independently_relabelled":True,
    }
