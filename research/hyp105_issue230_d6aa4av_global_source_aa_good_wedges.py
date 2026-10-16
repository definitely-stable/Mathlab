"""HYP-105 #230 AA4-AV: universal GOOD D wedge SOURCE A/A and original
two-type physical incidence transport covariance.

NEW all-global true symplectic W(3,s=2^h), h>=16:
  E_good >= E0 - E_bad (AA4-AP exact original source bound);
  W_good_source_AA >= 2 E_good^2/N - (2d-1)*E_good
                    >= s^6/10.
The source-collision correction is sharp as a STRUCTURAL upper:
each original source point or line factor occurs on at most d=s+1
true incidence flag IDs, hence <=2(d-1)*E_good repeated-outer
source-factor GOOD centered wedges. No independence or random f/g.

IMPORTANT: These are REAL ORIGINAL three-flag A/A motifs (three
different source points AND three different source lines) with two
good bilateral D edges. They are not necessarily two-typed
opposite PORT wedges or accepted GF5 sixflag Q. The original SOURCE
B/B reservoir >=s6 from AA4-AU is entirely DISJOINT from EVERY
centered two-D-edge wedge; source B/B cannot be used for this route.

For each center true incidence flag (p,l), exact corrected physical
transport four-bin tensor identity:
 X_(p,l)(c,e) = (F^T B G)_(c,e)
                   - (B G)_(p,e) - (F^T B)_(c,l) + 1
 for c in f(p), e in g(l).
It equals literal true original bilateral D neighbor count in the
two point/line physical intersection port pair (c,e). Thus
 R_all=sum_{(p,l) flag} (X00 X11 + X01 X10)
is the EXACT all-h same-global-f,g two-typed port-opposite wedge
coupling energy. NOT a positive all-f,g lower.
"""
from collections import Counter
from fractions import Fraction
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,_parameters)
from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
    global_good_original_D_spectral_certificate)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph)


def universal_original_AA_good_wedge_lower(s):
    """All-h>=16 EVERY full globally injected actual original W3s f,g.

    Analytic threshold h>=24; h=16..23 eight explicit exact rational
    parameter certificates. h15 NOT certified by this method. Numbers
    depend only on s and previously PROVED AA4-AP D_good lower.
    No huge source GQ instantiated.
    """
    ap=global_good_original_D_spectral_certificate(s)
    V,d=ap["V"],ap["d"]
    a=ap["a"];h=ap["h"]
    N=V*d
    E=ap["globally_port_good_unordered_D_explicit_lower"]
    cauchy=Fraction(2*E*E,N)-(2*d-1)*E
    proved=False
    method="outside_this_proof_range"
    if h>=16:
        if h>=24:
            # From MINIMAL a: (a-1)(a-2)<2V, so a²<2V+3a.
            assert a*a<2*V+3*a
            assert a*a<=4*s**3
            assert 4*d<=5*s
            assert N*s<=s**5+4*s**4  # N <= (1+4/s)s4
            # By 1/(1+x)>=1-x:
            # E0>=2V d² - 6a d²>=2s5-(75/4)s(7/2).
            # For sqrt(s)>=4096 (s>=2^24), bad<=3255*s5/4096.
            assert 4096**2<=s
            assert Fraction(2)-Fraction(75,4*4096**3)-Fraction(3255,4096)>=Fraction(11,10)
            assert E>=Fraction(11,10)*s**5
            # 2E/N-(2d-1) >= (s-49)/5 >= s/10.
            assert s>=98
            assert cauchy>=Fraction(11,100)*s**6
            method="all_h_ge_24_symbolic_analytic_11_over_100"
        else:
            # Only eight finite PARAMETER inequalities, not synthetic
            # W(3,s) enumeration; s values h=16,...,23.
            assert cauchy>=Fraction(s**6,10), ("AA4AV fail",h)
            method="eight_exact_rational_h16_to_h23"
        proved=True
    return dict(
        s=s,h=h,V=V,d=d,a=a,
        N_true_original_incidence_flag_vertices=N,
        E_GOOD_genuine_original_D_lower=E,
        exact_good_source_collision_upper_coefficient=2*(d-1),
        universal_source_AA_good_centered_two_D_edge_wedge_lower=(
            Fraction(s**6,10) if proved else None),
        exact_Cauchy_minus_source_collision_bound=cauchy,
        source_AA_all_global_s6_over_10_PROVED=proved,
        proof_method=method,
        h15_not_certified_from_this_original_good_D_floor=(h==15),
        source_BB_original_P4_reservoir_DISJOINT_from_source_D_wedges=True,
        physically_opposite_two_type_port_fraction_NOT_PROVED=True,
        original_GF5_six_Q_s6_NOT_PROVED=True,
    )


def exact_true_original_good_D_source_multiplicity_partition(model):
    """Actual source flag first, per center collision with repeated OUTER
    original point or line factors; never enumerate six-Q physical tags.

    Source A/A, B/A, A/B mutually disjoint among two GOOD centered
    original D edges. No source B/B triple is possible.
    Complexity O(N+E), independent of outer-neighbor pair brute.
    """
    G,good,nbrs,badP,badL=_good_D_edge_graph(model)
    inc=G["inc"];d=G["s"]+1
    aa=ba=ab=uncolored=0
    deg2=0
    point_collision=0
    line_collision=0
    for center,row in enumerate(nbrs):
        n=len(row)
        total=n*(n-1)//2
        pc=Counter(inc[j][0] for j,c,e in row)
        lc=Counter(inc[j][1] for j,c,e in row)
        dup_p=sum(v*(v-1)//2 for v in pc.values())
        dup_l=sum(v*(v-1)//2 for v in lc.values())
        if max(pc.values(),default=0)>d or max(lc.values(),default=0)>d:
            raise AssertionError("real source factor has more than d incident original flags")
        if dup_p+dup_l>total:
            raise AssertionError("two distinct true original neighbors cannot share both source point and source line")
        aa+=total-dup_p-dup_l
        ba+=dup_p
        ab+=dup_l
        uncolored+=total
        deg2+=n*n
        point_collision+=dup_p
        line_collision+=dup_l
    E=len(good);N=len(inc)
    if uncolored!=aa+ba+ab or deg2!=2*uncolored+2*E:
        raise AssertionError("true original source AA/BA/AB wedge partition")
    if point_collision>(d-1)*E or line_collision>(d-1)*E:
        raise AssertionError("original source repeated-outer factor <= (d-1)*D")
    true_lower=Fraction(2*E*E,N)-(2*d-1)*E
    if aa<true_lower:
        raise AssertionError("source multiplicity corrected original wedge Jensen")
    allh=universal_original_AA_good_wedge_lower(G["s"])
    if allh["source_AA_all_global_s6_over_10_PROVED"]:
        if aa<allh["universal_source_AA_good_centered_two_D_edge_wedge_lower"]:
            raise AssertionError("source AA universal good wedge s6/10 violated")
    return dict(
        s=G["s"],N_true_original_source_incidence_flag_vertices=N,
        true_original_GOOD_D_edges=E,
        source_all_GOOD_centered_two_D_edge_wedges=uncolored,
        source_AA_three_distinct_point_and_line_GOOD_D_wedges=aa,
        source_BA_outer_original_point_collision_GOOD_wedges=ba,
        source_AB_outer_original_line_collision_GOOD_wedges=ab,
        source_BB_good_D_wedges_EXACT=0,
        genuine_original_point_repetition_wedge_upper=(d-1)*E,
        genuine_original_line_repetition_wedge_upper=(d-1)*E,
        sum_true_original_good_degrees_squared=deg2,
        true_source_collision_corrected_Cauchy_floor=true_lower,
        unconditional_all_h_theorem=allh,
        source_only_AA_not_equivalent_to_physically_two_typed_opposite=True,
        selected_GF5_s6_NOT_INFERRED=True,
    )


def independent_literal_true_original_good_D_source_partition(model):
    """A different O(sum deg²) SOURCE FIRST actual W32/W34 wedge referee."""
    G,good,nbrs,badP,badL=_good_D_edge_graph(model)
    if len(G["inc"])>500:
        raise ValueError("literal original 3-flag pair oracle limited W32/W34")
    counts=Counter()
    opposite=Counter()
    inc=G["inc"]
    for center,row in enumerate(nbrs):
        for (j,c,e),(k,f,h) in __import__("itertools").combinations(row,2):
            np=len({inc[t][0] for t in (center,j,k)})
            nl=len({inc[t][1] for t in (center,j,k)})
            shape=("A" if np==3 else "B")+"/"+("A" if nl==3 else "B")
            if shape not in ("A/A","B/A","A/B"):
                raise AssertionError("genuine D-centered source wedge cannot be B/B or C")
            counts[shape]+=1
            if c!=f and e!=h:
                if shape!="A/A":
                    raise AssertionError("source repeated factor incompatible with two-typed physically opposite ports")
                opposite[shape]+=1
    return dict(
        s=G["s"],
        true_original_source_first_literal_GOOD_threeflag_wedge_types=dict(counts),
        genuine_original_opposite_two_typed_good_wedges=sum(opposite.values()),
        opposite_wedges_only_original_source_AA=True,
        actual_original_good_D_source_BB_intersection_ZERO=True,
    )


def exact_original_corrected_two_type_four_bin_transport(model):
    """EXACT ORIGINAL globally correlated physical-source tensor, all h.

    Unlike literal neighbor scanning, obtains all four D-port bins
    directly from the actual globally fixed original source incidence
    coordinate transport M=F^T B G and two marginal correction tensors.
    O(4N+4N) after source W3 data, no second physical label sampling.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    M=[[0]*a for _ in range(a)]
    BGT=[[0]*a for _ in range(V)]  # (BG)_(p,e)
    FBT=[[0]*a for _ in range(V)]  # (F^T B)_(c,l), stored by original line l
    for p,l in inc:
        for c in left[p]:
            for e in right[l]:
                M[c][e]+=1
        for e in right[l]:
            BGT[p][e]+=1
        for c in left[p]:
            FBT[l][c]+=1
    bins=[]
    R=0
    total_degree=0
    wedges=0
    for p,l in inc:
        c0,c1=sorted(left[p])
        e0,e1=sorted(right[l])
        x=(
            M[c0][e0]-BGT[p][e0]-FBT[l][c0]+1,
            M[c0][e1]-BGT[p][e1]-FBT[l][c0]+1,
            M[c1][e0]-BGT[p][e0]-FBT[l][c1]+1,
            M[c1][e1]-BGT[p][e1]-FBT[l][c1]+1,
        )
        if min(x)<0:
            raise AssertionError("true W3 original bilateral D corrected coordinate bin negative")
        bins.append(x)
        total_degree+=sum(x)
        wedges+=sum(x)*(sum(x)-1)//2
        R+=x[0]*x[3]+x[1]*x[2]
    if total_degree%2:
        raise AssertionError("original source flag graph handshake")
    return dict(
        s=s,N_true_original_incidence_flags=len(inc),
        true_original_full_physical_coordinate_transport=tuple(map(tuple,M)),
        true_original_centered_flag_D_2by2_point_line_port_tensor=tuple(bins),
        true_original_all_D_edges=total_degree//2,
        genuine_original_all_D_centered_uncolored_wedges=wedges,
        genuine_original_ALL_D_two_typed_physically_opposite_wedges=R,
        source_original_local_4bin_tensor_M_minus_BG_minus_FB_plus_1_exact=True,
        no_independence_between_fixed_global_point_and_line_f_g=True,
        no_opposite_port_universal_lower_PROVED=True,
        accepted_original_GF5_s6_NOT_PROVED=True,
    )
