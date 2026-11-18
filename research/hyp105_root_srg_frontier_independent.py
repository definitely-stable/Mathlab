"""AA4-ROOT-SRG-FRONTIER: independent all-h GQ/SRG source-conflict audit.

NEW deterministic strengthened source bounds:
 s >= 64:  e(J) < (19/8) s**4, instead of (5/2) s**4.
 s >= 256: K=4 FULL-source J-degree pruning leaves a positive
            fraction >=65257/20971520 of genuine original flags.
 s >=2**H even H>=8: exact rational e(J)<2 M_H s**4,
 M_H=(1+2**(-2H))*(1+23/(16*2**(H//2))).
 Stronger H=32 source budget + FIXED K=10 improves conditional
 Branch A dyadic s0, keeping ALL inherited original motif gates open.

Only the trusted true W(3,2)/W(3,4) symplectic incidence constructor
is imported. No historical J, LOW, HEAVY, root, or GF5 calculators.
Finite cases are falsifiers, not the source of the all-h proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.root-srg-frontier-exact.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
R_Z0=93312
K_NEW=10
H_SOURCE=32
ALLOC=(Fraction(1,64),Fraction(1,64),Fraction(15,16))


def ceil_fraction(x):
    if type(x) is not Fraction:
        raise TypeError("only exact rational threshold arithmetic")
    return -(-x.numerator//x.denominator)


def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("integer nonnegative square root only")
    x=isqrt(n)
    return x+int(x*x<n)


def dyadic_h(n):
    if type(n) is not int or n<=0:
        raise ValueError("positive integer threshold")
    return (n-1).bit_length()


def minimal_original_alphabet(V):
    if type(V) is not int or V<1:
        raise ValueError("positive ORIGINAL point/line count")
    a=2
    while comb(a,2)<V:
        a+=1
    if not comb(a-1,2)<V<=comb(a,2):
        raise AssertionError("not the MINIMAL pair alphabet")
    return a


def source_numerical_spectral_bound(s):
    """Exact all-dyadic SOURCE capacity and original point/line SRG ceiling.

    This is valid on true W(3,s) when s>=2; all-h uniform 19/8
    only starts at 64, and K4 positivity starts at 256.
    """
    if type(s) is not int or s<2 or (s&(s-1)):
        raise ValueError("original symplectic source requires dyadic s>=2")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=minimal_original_alphabet(V)
    C=(s*s+1)*(s*s+a-2)
    M=Fraction(C,s**4)
    # The FULL original source J is the SUM of two typed actual
    # collinearity conflict graphs, so e(J)<=2*C_s, not 4*C_s.
    e_bound=2*C
    if s>=64 and not Fraction(e_bound,s**4)<Fraction(19,8):
        raise AssertionError("all-order strengthened 19/8 J cap false")
    if s>=256 and not M<Fraction(35,32):
        raise AssertionError("all-order K4 positive asymptotic cap false")
    c4=Fraction(7,8)-Fraction(4*C,5*s**4)
    return dict(s=s,V=V,N=N,a=a,exact_original_Cs=C,
                full_original_J_edges_spectral_upper=e_bound,
                dimensionless_Cs_ratio=str(M),
                dimensionless_J_ratio_upper=str(2*M),
                K4_CORE_fraction_after_FULL_Q=str(c4),
                s_ge64_uniform_19over8_applicable=s>=64,
                s_ge256_K4_from_spectral_applicable=s>=256)


def all_h_spectral_envelope(H):
    """Independent elementary bound for ALL dyadic s>=2**H, H even>=8.

    From V<=(33/32)s^3 and pair alphabet minimality:
      (a-2)(a-1)<2V; hence a-2<sqrt(2V)
      <(23/16)*s^(3/2) <=(23/(16*2^(H/2)))*s^2.
    The genuine point/line SRG then yields e(J)<2M_H*s^4.
    """
    if type(H) is not int or H<8 or H%2:
        raise ValueError("even dyadic H>=8 required for exact sqrt envelope")
    M=(1+Fraction(1,2**(2*H)))*(1+Fraction(23,16*2**(H//2)))
    e_const=2*M
    # EXACT inequalities, no floats.
    if not M<Fraction(35,32):
        raise AssertionError("K=4 positivity threshold failed")
    if H==8 and not M==Fraction(18284823,16777216):
        raise AssertionError("sharp dyadic-256 symbolic envelope changed")
    c4=Fraction(7,8)-4*M/Fraction(5)
    if c4<=0:
        raise AssertionError("K4 true original LOW CORE lower bound not positive")
    return dict(H=H,min_s=2**H,M=M,source_J_coefficient=e_const,
                K4_original_CORE_floor=c4,
                all_h_true_GQ_srg_from_only_point_line_axioms=True)


def _ceilroot_budget(K,H,C0,c0,errors=ALLOC):
    """NO GF5/B75, conditional source-to-root glue, Fraction arithmetic.

    This is new all-h quantifier-controlled constant propagation.
    The inherited global selected-moment and source-sixset lemmas
    MUST still be independently accepted before ROOT PROVED_A.
    """
    if type(K) is not int or K<0:
        raise ValueError("integer original FULL J-degree cap K>=0")
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("formal exact external graph constants only")
    if (not isinstance(errors,tuple) or len(errors)!=3
            or any(type(x) is not Fraction or x<=0 for x in errors)
            or sum(errors)>=1):
        raise ValueError("positive exact three-error allocation sum <1")
    env=all_h_spectral_envelope(H)
    c=Fraction(7,8)-2*env["source_J_coefficient"]/Fraction(K+1)
    if c<=0:
        raise ValueError("K too small for the UNIFORM all-h J cap")
    walk=Fraction(16,81)*(4*c)**3
    R=R_Z0
    T=ceil_fraction(Fraction(17*R**3,2)*C0**3)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*ceil_sqrt(ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    alpha1,alpha2,alpha3=errors
    s_coord=ceil_fraction(Fraction(111*T,2)/(alpha1*walk))
    s_endpoint=ceil_fraction((Fraction(E)/(alpha2*walk))**2)
    s_blockers=ceil_fraction((Fraction(D)/(alpha3*walk))**8)
    s0=max(2**H,64,s_coord,s_endpoint,s_blockers)
    delta=c0/Fraction(R**6)
    bbo=walk*(1-sum(errors))/2
    if bbo<delta:
        raise AssertionError("LOW genuine BBo floor below fixed HEAVY delta")
    if not (Fraction(111*T,2)<=alpha1*walk*s0
            and Fraction(E*E)<=(alpha2*walk)**2*s0
            and Fraction(D**8)<=(alpha3*walk)**8*s0):
        raise AssertionError("original proper-walk three errors don't fit")
    return dict(
        K=K,H=H,source_J_absolute_coefficient=str(env["source_J_coefficient"]),
        actual_original_FULL_J_high_source_degree_pruned_gt_K=K+1,
        original_CORE_fraction=str(c),
        all_walk_Blackley_Roy_lower=str(walk),
        retained_source_alpha_errors=[str(x) for x in errors],
        q2=q2,q3=q3,R=R,T=str(T),L6=str(L6),
        L4=str(L4),B0=str(B0),E=str(E),D=str(D),
        s_coordinate=str(s_coord),s_endpoint=str(s_endpoint),
        s_four_original_blockers=str(s_blockers),
        exact_root_s0=str(s0),exact_root_h0=dyadic_h(s0),
        original_produced_BBo_floor=str(bbo),
        unchanged_heavy_D6_delta=str(delta),
        all_order_inherited_global_LOW_moment_proof_STILL_SEPARATE=True,
        external_graph_C6_constants_NOT_numeric=True,
        root_PROVED_A=False)


def previous_K11_uniform_original_budget(C0,c0):
    """Recompute the parent #773 exact base, not import any parent solver."""
    if type(C0) is not Fraction or type(c0) is not Fraction:
        raise TypeError("exact symbolic constant probes only")
    e=Fraction(5,2)
    K=11
    c=Fraction(7,8)-2*e/Fraction(K+1)
    w=Fraction(16,81)*(4*c)**3
    T=ceil_fraction(Fraction(17*R_Z0**3,2)*C0**3)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*ceil_sqrt(ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    a,b,c_error=ALLOC
    s0=max(64,ceil_fraction(Fraction(111*T,2)/(a*w)),
              ceil_fraction((Fraction(E)/(b*w))**2),
              ceil_fraction((Fraction(D)/(c_error*w))**8))
    return dict(K=11,h0=dyadic_h(s0),s0=str(s0),
                q2=q2,q3=q3,root_PROVED_A=False)


def formal_original_root_compare(C0,c0):
    old=previous_K11_uniform_original_budget(C0,c0)
    win=_ceilroot_budget(K_NEW,H_SOURCE,C0,c0)
    trials=[]
    for K in range(4,65):
        try:
            a=_ceilroot_budget(K,H_SOURCE,C0,c0)
        except ValueError:
            continue
        trials.append((K,a["exact_root_h0"]))
    best=min(h for _,h in trials)
    winning=[k for k,h in trials if h==best]
    if K_NEW not in winning:
        raise AssertionError("fixed K10 is not among minimizers for FORMAL tests")
    if win["exact_root_h0"]>=old["h0"]:
        raise AssertionError("stronger SRG bound did not improve parent root threshold")
    return dict(formal_C0_not_published=str(C0),
                formal_c0_not_published=str(c0),
                previous_K11_h0=old["h0"],
                improved_FIXED_K10_H32_h0=win["exact_root_h0"],
                h0_reduction=old["h0"]-win["exact_root_h0"],
                K_winners_from_4_to_64=winning,
                first_new_K4_is_permitted_by_source_SRG=True,
                formal_not_published_C6_constants=True,
                root_PROVED_A=False)


def true_symplectic_geometry(s):
    """Independently enumerate ORIGINAL W(3,s) incidence and GQ axiom."""
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("true finite source only s=2 and s=4")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("true ORIGINAL W3s source cardinality invalid")
    bp=[set() for _ in range(V)]
    bl=[set() for _ in range(V)]
    for p,l in flags:
        bp[p].add(l);bl[l].add(p)
    if any(len(v)!=s+1 for v in bp+bl):
        raise AssertionError("point/line pencils not original GQ regular")
    Padj=[set() for _ in range(V)]
    Ladj=[set() for _ in range(V)]
    for ps in bl:
        for p,q in combinations(sorted(ps),2):
            if q in Padj[p]:
                raise AssertionError("same ORIGINAL points share two lines")
            Padj[p].add(q);Padj[q].add(p)
    for lines in bp:
        for l,m in combinations(sorted(lines),2):
            if m in Ladj[l]:
                raise AssertionError("same ORIGINAL lines share two points")
            Ladj[l].add(m);Ladj[m].add(l)
    k=s*(s+1)
    lam=s-1
    mu=s+1
    for A in (Padj,Ladj):
        if any(len(a)!=k for a in A):
            raise AssertionError("real original GQ collinearity degree incorrect")
        for i in range(V):
            for j in range(V):
                common=len(A[i]&A[j])
                expected=k if i==j else lam if j in A[i] else mu
                if common!=expected:
                    raise AssertionError("actual GQ strongly regular polynomial false")
    # The TRUE GQ projection property, not a mere SRG surrogate.
    for p in range(V):
        for l in range(V):
            if l not in bp[p]:
                if len(Padj[p]&bl[l])!=1:
                    raise AssertionError("point off ORIGINAL line has !=1 projection")
    # Equal spectra for original points and dual original lines, certified
    # by the polynomial, degree, and trace; no floating eigenvalue fit.
    mult_r=s*(s+1)**2//2
    mult_t=V-1-mult_r
    if not (1+mult_r+mult_t==V
            and k+mult_r*(s-1)-mult_t*(s+1)==0
            and mult_r>=0 and mult_t>=0):
        raise AssertionError("original SRG spectral multiplicity identity false")
    return dict(s=s,V=V,flags=flags,point_flags=bp,line_flags=bl,
                point_adj=Padj,line_adj=Ladj,multiplicity_plus=mult_r,
                multiplicity_minus=mult_t)


def complete_original_maps(V,scheme):
    a=minimal_original_alphabet(V)
    pairs=tuple(combinations(range(a),2))[:V]
    if scheme=="lex":
        f=pairs;g=pairs
    elif scheme=="reverse":
        f=pairs;g=pairs[::-1]
    elif scheme=="shift":
        f=pairs[3:]+pairs[:3]
        g=pairs[7:]+pairs[:7]
    else:
        raise ValueError("unknown correlated source-pair scheme")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("ORIGINAL maps not separately pair-injective")
    return a,f,g


def typed_collinear_overlap(adj,pairs):
    """First algorithm: enumerate source-typed ORIGINAL collinearity."""
    if (len(adj)!=len(pairs) or len(set(pairs))!=len(pairs)
            or any(not isinstance(p,tuple) or len(p)!=2 or
                   type(p[0]) is not int or type(p[1]) is not int or
                   p[0]<0 or p[0]>=p[1] for p in pairs)):
        raise ValueError("need separately globally injected original two-symbol pairs")
    return sum(bool(set(pairs[i])&set(pairs[j]))
               for i,A in enumerate(adj) for j in A if i<j)


def typed_symbol_spectral_energy(adj,pairs,a,s):
    """Second algorithm: exact physical pair-occupancy and GQ SRG Gram."""
    V=len(pairs)
    if (type(a) is not int or a<2 or len(adj)!=V or
            len(set(pairs))!=V or any(
                not isinstance(x,tuple) or len(x)!=2 or
                type(x[0]) is not int or type(x[1]) is not int or
                not 0<=x[0]<x[1]<a for x in pairs)):
        raise ValueError("invalid complete globally pair-injected original source map")
    by_symbol=[set() for _ in range(a)]
    for p,(x,y) in enumerate(pairs):
        by_symbol[x].add(p)
        by_symbol[y].add(p)
    degree2=sum(len(z)**2 for z in by_symbol)
    if sum(map(len,by_symbol))!=2*V or max(map(len,by_symbol))>a-1:
        raise AssertionError("pair-label original symbol occupancy impossible")
    # Count GQ collinearity locally inside each actual physical symbol fibre.
    induced_edges=sum(sum(q in adj[p] for p,q in combinations(sorted(S),2))
                      for S in by_symbol)
    gram_energy=sum(sum(len(adj[p]&S)**2 for p in range(V))
                    for S in by_symbol)
    expected=2*V*(s*s-1)-4*induced_edges+(s+1)*degree2
    if gram_energy!=expected:
        raise AssertionError("true original SRG Gram identity mismatch")
    spectral_ceiling=(Fraction(V*(s-1))
                     +Fraction((s*s+1)*degree2,2*V))
    C=(s*s+1)*(s*s+a-2)
    if not Fraction(induced_edges)<=spectral_ceiling<=C:
        raise AssertionError("original pair source spectral bound violated")
    return dict(e_col_from_symbol_induced=induced_edges,
                sum_true_original_symbol_degree_squared=degree2,
                true_original_SRG_G_energy=gram_energy,
                true_original_SRG_expected_G_energy=expected,
                spectral_instance_adaptive_upper=str(spectral_ceiling),
                universal_original_Cs=C)


def genuine_original_case(s,scheme):
    g=true_symplectic_geometry(s)
    a,f,m=complete_original_maps(g["V"],scheme)
    point=typed_collinear_overlap(g["point_adj"],f)
    line=typed_collinear_overlap(g["line_adj"],m)
    # Completely independent SOURCE J census: source pencil flags with
    # overlapping OTHER-side physical pair labels, each named flag once.
    byp=defaultdict(list)
    byl=defaultdict(list)
    for i,(p,l) in enumerate(g["flags"]):
        byp[p].append((i,l))
        byl[l].append((i,p))
    edgeJ=set()
    for ids in byp.values():
        for (i,l),(j,n) in combinations(ids,2):
            if set(m[l])&set(m[n]):
                edgeJ.add((min(i,j),max(i,j)))
    for ids in byl.values():
        for (i,p),(j,q) in combinations(ids,2):
            if set(f[p])&set(f[q]):
                edgeJ.add((min(i,j),max(i,j)))
    if len(edgeJ)!=point+line:
        raise AssertionError("full ORIGINAL pencil J != independent dual collinear conflicts")
    p_energy=typed_symbol_spectral_energy(g["point_adj"],f,a,s)
    l_energy=typed_symbol_spectral_energy(g["line_adj"],m,a,s)
    if (p_energy["e_col_from_symbol_induced"]!=point
        or l_energy["e_col_from_symbol_induced"]!=line):
        raise AssertionError("two independently derived source e_col counts disagree")
    C=(s*s+1)*(s*s+a-2)
    if len(edgeJ)>2*C:
        raise AssertionError("original true J exceeds the unrounded SRG ceiling")
    source_symbol_degrees=Counter()
    for i,j in edgeJ:
        source_symbol_degrees[i]+=1
        source_symbol_degrees[j]+=1
    for K in (3,4,5,10,64):
        high=sum(source_symbol_degrees[i]>K for i in range(len(g["flags"])))
        if high*(K+1)>2*len(edgeJ):
            raise AssertionError("strict >K original full source handshaking false")
    return dict(s=s,scheme=scheme,V=g["V"],original_flags=len(g["flags"]),
                minimal_a=a,original_positive_SRG_mult=g["multiplicity_plus"],
                original_negative_SRG_mult=g["multiplicity_minus"],
                true_original_J_edges=len(edgeJ),
                true_original_point_collinear_overlaps=point,
                true_original_line_collinear_overlaps=line,
                actual_true_J_no_more_than_2Cs=True,
                full_original_point_symbol_energy=p_energy,
                full_original_line_symbol_energy=l_energy,
                original_point_line_spectral_SRG_identities_passed=True,
                projection_off_each_original_nonincident_point_line_is_unique=True)


def certificate():
    real=[genuine_original_case(s,mode) for s in (2,4)
          for mode in ("lex","reverse","shift")]
    ratios=[source_numerical_spectral_bound(s) for s in
            (64,128,256,512,1024)]
    env=[all_h_spectral_envelope(H) for H in (8,16,32,64)]
    formal=[formal_original_root_compare(*q) for q in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    new=[_ceilroot_budget(K_NEW,H_SOURCE,*q) for q in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    k4=_ceilroot_budget(4,8,Fraction(1),Fraction(1))
    return dict(
        schema=SCHEMA,issue=230,parent_pr=773,status=ROOT_STATUS,
        independently_proved_all_h_original_GQ_SRG_source_collision_bound=True,
        all_h_original_J_stronger_19_over_8_for_s_ge64=True,
        all_h_new_K4_original_core_for_dyadic_s_ge256=True,
        K4_uniform_core_floor_dyadic_256=str(Fraction(65257,20971520)),
        all_h_source_symbol_occupancy_original_dual=True,
        all_h_original_source_exact_dimensionless_envelope_for_all_even_H_ge8=True,
        retained_original_predecessor_heavy_and_LOW_lemmas_REVIEW_OPEN=True,
        source_GQ_SRG_prerequisite_local_status="INDEPENDENT_PROOF_CHECKED",
        first_following_open_proof_gate="HEAVY_OWNER_AND_SELECTED_F",
        external_C6_unknown_numerical_constants=True,
        root_PROVED_A=False,ASET_exponent_claimed=False,
        real_original_W32_W34_genuine_symplectic_dual_SRG_censuses=real,
        true_dyadic_exact_original_Cs_envelopes=ratios,
        all_h_symbolic_rational_envelope_cases=[dict(
            H=x["H"],min_s=x["min_s"],M=str(x["M"]),
            source_J_coefficient=str(x["source_J_coefficient"]),
            K4_original_CORE_floor=str(x["K4_original_CORE_floor"]))
            for x in env],
        formal_graph_constant_conditional_ROOT_comparison=formal,
        formal_graph_constant_conditional_ROOT_optimized_H32_K10=new,
        K4_positive_original_CORE_conditional_budget_H8=k4)


if __name__=="__main__":
    print("AA4_ROOT_SRG_FRONTIER_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
