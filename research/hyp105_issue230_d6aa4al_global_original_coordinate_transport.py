"""HYP-105 #230 / AA4-AL: ALL-GLOBAL ORIGINAL two-type transport energy.

For TRUE ORIGINAL W(3,2^h), h>=1, and EVERY pair of complete,
globally injective typed physical K_a-edge maps f (point factors) and
g (line factors), form the physical-coordinate incidence transport

    M[c,d] = #{actual ORIGINAL flags (p,l): c in f(p), d in g(l)}
           = F^T B G[c,d].

Four coordinate-cells per original source flag. Its EXACT second
moment, minus both types of source-degenerate flag pairs, counts
ORDERED pairs of distinct genuine ORIGINAL flags (p,l),(q,m) with
p!=q, l!=m, f(p) intersect f(q) != empty and
g(l) intersect g(m) != empty. Distinct physical pair images make
each good pair have exactly ONE common coordinate on each side.

By Cauchy and the original source degree d=s+1:
    GOOD >= 16 V^2 d^2/a^2 - 4 V d^2 >= 2 V d^2 >= 2 s^5,
    V=(s+1)(s^2+1), a=min {a:C(a,2)>=V}, s>=2.
A sharper exact two-margin ANOVA certificate adds nonnegative
physical-coordinate degree imbalance energies.

This is a new honest original six-motif FRONTIER: an all-f,g
Omega(s^5) guarantee on compatible PAIRS of source flags, NOT
an Omega(s^6) count of selected six-flag GF5 Q. Three-flag
collisions can violate the physical degree-two GF5 projection gate.

The ORIGINAL W(3,s) incidence singular spectrum is
  d (multiplicity 1), sqrt(2s) (m=s(s+1)^2/2), 0 (remainder).
Standard GQ strongly-regular spectral prior art is not new.
A one-cell spectral expander-mixing lower is nonpositive for ALL
possible physical center fibers at every s>=2, even though the
GLOBAL nonnegative second-moment collision energy is large.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model


def _parameters(s):
    if type(s) is not int or s<2 or s & (s-1):
        raise ValueError("genuine original W(3,2^h), h>=1, required")
    V=(s+1)*(s*s+1)
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    assert comb(a-1,2)<V<=comb(a,2)
    return V,s+1,a


def all_h_global_original_transport_theorem(s):
    """All h, all globally injected f,g: exact rational lower and spectrum.

    The spectral fact is the CLASSICAL original GQ(s,s) collinearity
    strongly-regular eigenvalue identity, used as an independent
    diagnostic. The pair lower uses ONLY actual source d-regularity
    plus full global typed physical edge injection, not expansion.
    """
    V,d,a=_parameters(s)
    m_pos=s*(s+1)**2//2
    m_zero=V-1-m_pos
    assert 1+m_pos+m_zero==V and m_zero>=0
    lower=Fraction(16*V*V*d*d,a*a)-4*V*d*d
    assert lower>=2*V*d*d>=2*s**5

    # The centered incidence mixing bound for a physical fiber with
    # 1<=t,u<=a-1 is
    # e(U,W)>=d*t*u/V-sqrt(2s*t*(1-t/V)*u*(1-u/V)).
    # It is NEVER strictly positive from this inequality alone:
    # d² t u <= 2s (V-t)(V-u).
    # The most demanding possible case is t=u=a-1.
    # For s>=4 use a-1<=s² and V-a+1 >=s³, d<=5s/4.
    # For s=2 verify integer directly.
    assert (a-1<=s*s and V-a+1>=s**3 and
            16*d*d*s**4<=25*s**6 <=32*s**7
           ) if s>=4 else s==2 and a==6
    local_blind=d*d*(a-1)**2<=2*s*(V-a+1)**2
    assert local_blind
    return {
        "s":s,"V":V,"d":d,"a":a,"physical_palette_size":comb(a,2),
        "global_edge_image_missing":comb(a,2)-V,
        "F_transpose_B_G_shape":(a,a),
        "incidence_singular_values_squared_multiplicity":{
            str(d*d):1,str(2*s):m_pos,"0":m_zero},
        "genuine_original_source_collinearity_SRG_eigenvalues":{
            str(s*(s+1)):1,str(s-1):m_pos,str(-d):m_zero},
        "uniform_ordered_DISTINCT_source_point_line_flag_pair_lower":lower,
        "simple_explicit_ordered_good_pair_lower":2*s**5,
        "all_physical_center_cell_spectral_mixing_lower_NONPOSITIVE":local_blind,
        "all_complete_global_f_g_original_pair_lower_PROVED":True,
        "ALL_SIX_original_incidence_GF5_Omega_s6_NOT_PROVED":True,
        "infinite_counterfamily_NOT_PROVED":True
    }


def _actual_strict_original_transport(model):
    V,a,_=_valid_original_model(model)
    s=model["s"];d=s+1
    V0,d0,a0=_parameters(s)
    if (V,a)!=(V0,a0):
        raise ValueError("minimal real original physical alphabet required")
    f=tuple(tuple(e) for e in model["left_labels"])
    g=tuple(tuple(e) for e in model["right_labels"])
    inc=tuple(tuple(e) for e in model["incidences"])
    if len(inc)!=V*d or len(set(inc))!=V*d:
        raise ValueError("actual original source flag count")
    neighbors_p=[[] for _ in range(V)]
    neighbors_l=[[] for _ in range(V)]
    for p,l in inc:
        if not (0<=p<V and 0<=l<V):
            raise ValueError("actual original incidence outside source")
        neighbors_p[p].append(l)
        neighbors_l[l].append(p)
    if any(len(x)!=d for x in (*neighbors_p,*neighbors_l)):
        raise ValueError("actual genuine original source degree")
    return s,V,d,a,f,g,inc,neighbors_p,neighbors_l


def _degenerate_source_flag_ordered_pairs(f,g,neighbors_p,neighbors_l):
    """Exact all-global source repetition subtractions, not crude caps."""
    bad_p=0
    for p,ls in enumerate(neighbors_p):
        r=Counter(c for l in ls for c in g[l])
        # Each source p physical image has precisely two distinct
        # physical coordinates, so duplicate-p flags count twice.
        bad_p+=2*sum(n*(n-1) for n in r.values())
    bad_l=0
    for l,ps in enumerate(neighbors_l):
        r=Counter(c for p in ps for c in f[p])
        bad_l+=2*sum(n*(n-1) for n in r.values())
    return bad_p,bad_l


def exact_original_global_transport(model):
    """Exact ORIGINAL cross-type coordinate tensor and pair-energy.

    Costs O(Vd+a²) after the actual original model exists; checks the
    true original incidences, globally injected physical maps,
    four contributions per actual original flag, exact source-
    repetition correction, both transportation marginals and
    the ANOVA row+column energy lower, without f/g resampling.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    M=[[0]*a for _ in range(a)]
    for p,l in inc:
        for c in f[p]:
            for k in g[l]:
                M[c][k]+=1
    row=tuple(sum(R) for R in M)
    col=tuple(sum(M[c][k] for c in range(a)) for k in range(a))
    point_fiber=tuple(sum(c in e for e in f) for c in range(a))
    line_fiber=tuple(sum(k in e for e in g) for k in range(a))
    assert sum(map(sum,M))==4*V*d
    assert row==tuple(2*d*t for t in point_fiber)
    assert col==tuple(2*d*t for t in line_fiber)
    assert sum(point_fiber)==sum(line_fiber)==2*V
    T=4*V*d
    second=sum(v*v for R in M for v in R)
    bad_p,bad_l=_degenerate_source_flag_ordered_pairs(f,g,np,nl)
    assert 0<=bad_p<=2*V*d*(d-1)
    assert 0<=bad_l<=2*V*d*(d-1)
    good=second-T-bad_p-bad_l
    assert good>=0 and not good%2

    baseline=Fraction(T*T,a*a)
    # Exact ANOVA decomposition of a*a numerical transport cells:
    # sum M² >= (sum row_i² + sum col_j²)/a - T²/a².
    two_margin=Fraction(sum(x*x for x in row)+sum(x*x for x in col),a)-baseline
    centered_F=sum((Fraction(t,1)-Fraction(2*V,a))**2 for t in point_fiber)
    centered_G=sum((Fraction(t,1)-Fraction(2*V,a))**2 for t in line_fiber)
    asserted_two_margin=baseline+Fraction(4*d*d,a)*(centered_F+centered_G)
    assert two_margin==asserted_two_margin
    assert second>=two_margin>=baseline
    th=all_h_global_original_transport_theorem(s)
    assert good>=th["uniform_ordered_DISTINCT_source_point_line_flag_pair_lower"]
    stronger=two_margin-4*V*d*d
    assert good>=stronger
    return {
        "s":s,"V":V,"a":a,"d":d,
        "cross_physical_coordinate_transport_matrix":tuple(tuple(R) for R in M),
        "point_physical_fiber_sizes":point_fiber,
        "line_physical_fiber_sizes":line_fiber,
        "transport_row_marginals":row,"transport_col_marginals":col,
        "total_four_per_original_flag_transport":T,
        "transport_squared_Frobenius_energy":second,
        "ordered_source_same_original_point_subtraction":bad_p,
        "ordered_source_same_original_line_subtraction":bad_l,
        "exact_ordered_DISTINCT_source_flag_pair_bilateral_physical_collision":good,
        "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision":good//2,
        "all_f_g_Cauchy_uniform_lower":th[
            "uniform_ordered_DISTINCT_source_point_line_flag_pair_lower"],
        "two_margin_ANOVA_energy_lower":two_margin,
        "physical_fiber_degree_variance_gain":
            Fraction(4*d*d,a)*(centered_F+centered_G),
        "refined_all_f_g_original_pair_lower":stronger,
        "source_repetition_exact_not_inferred_independence":True,
        "global_complete_original_maps":True,
        "positive_seven_GF5_sixset_lower_NOT_PROVED":True
    }


def independent_original_flag_pair_oracle(model):
    """Different source-first algorithm: enumerate distinct genuine 2 flags.

    Does NOT form M or use transport tensor/Cauchy/ANOVA. Each pair is
    counted once as unordered actual 2-source-flag Q, after requiring
    genuinely distinct physical ORIGINAL source points AND lines.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    good=0
    for i in range(len(inc)):
        p,l=inc[i]
        for j in range(i+1,len(inc)):
            q,m=inc[j]
            if p!=q and l!=m and set(f[p])&set(f[q]) and set(g[l])&set(g[m]):
                good+=1
    return good


def independent_true_original_incidence_spectrum_certificate(model):
    """Finite exact GQ BB^T = d I + A and SRG 3-eigen polynomials.

    All h spectral multiplicities derived from classical GQ parameters.
    The finite source actual GQ is NOT replaced by synthetic regular
    incidence, and the test checks the TRUE VxV multiplication identities
    without external numerical eigendecomposition.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    A=[[0]*V for _ in range(V)]
    for ps in nl:
        for p in ps:
            for q in ps:
                if p!=q:A[p][q]=1
    assert all(sum(R)==s*d for R in A)
    for i in range(V):
        for j in range(V):
            shared=len(set(np[i])&set(np[j]))
            assert shared==(d if i==j else A[i][j])
            # Classical W(3,s) SRG (V,k,lambda,mu).
            common=sum(A[i][t] and A[t][j] for t in range(V))
            expect=(s*d if i==j else s-1 if A[i][j] else s+1)
            assert common==expect
    return {
        "s":s,"V":V,
        "all_true_original_BBT_equals_dI_plus_A":"PASS",
        "all_true_original_A_squared_SRG_mu_lambda":"PASS",
        "rank_of_original_source_B":1+s*d*d//2,
        "source_nullspace_dimension":V-1-s*d*d//2,
        "spectral_unexpanded_local_cell_lower_NONPOSITIVE":
            all_h_global_original_transport_theorem(s)[
                "all_physical_center_cell_spectral_mixing_lower_NONPOSITIVE"],
        "no_seven_GF5_Branch_A_claim":True
    }
