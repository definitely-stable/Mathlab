"""AA4-CK — true original W3 GF5 D6 dual-cycle single-global-POINT-swap spectral energy.

Pure exact integer spectrum of the 60-state Schreier transposition graph
of six labeled original incidence-column Hamiltonian C6 dual graphs:
adjacency A counts each of the 15 single transpositions of six REAL
original POINT source-factor complete physical image assignments.
A has integer eigenvalues (15,5,0,-3,-9), multiplicities (1,18,16,20,5),
L=15I-A has (0,10,15,18,24). Exact integer polynomial annihilator
and traces independently certify eigenvalues without float/numpy.

For any fixed genuine original W(3,2^h), h>=1, ANY correlated complete
globally injected typed f,g and ANY six genuine distinct POINT factor
IDs forming a physical C6 on f, the EXACT historical seven-class
accepted weighted source-POINT-A fiber T(C)=B+5643 H(C) obeys

  4/3 Var_C(T) <= E_{C,tau} (T(C^tau)-T(C))^2 <= 16/5 Var_C(T)

where the E is over 60 labeled C6s and 15 fully legal WHOLE-original
POINT factor image transpositions at each C. The 15-swap averaging
operator contracts centered L2 by <=3/5. Sharp for arbitrary real
functions on the 60-state graph, NOT claimed W3 histogram sharpness.

No independence or per-Q redraw; this theorem is NOT a uniform
positive lower bound for the entire original fixed-map seven-GF5 S.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    PERMS, W_D, original_cycle_orbit, original_point_A_fiber,
    original_maximal_D6_fan, complete_original_f_orbit,
    _six_position_dual_cycle,
)
from hyp105_issue230_d6aa4cj_global_point_swap_dual_flow_ledger import (
    original_two_point_global_swap,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

N=60
DEGREE=15
TRANSPOSITIONS=tuple(combinations(range(6),2))
EIGEN_A=(15,5,0,-3,-9)
EIGEN_MULT=(1,18,16,20,5)
EIGEN_L=(0,10,15,18,24)


def _cycle_from_order(order):
    if len(order)!=6 or set(order)!=set(range(6)):
        raise ValueError("six labeled ORIGINAL incidence positions required")
    return frozenset(frozenset((order[i],order[(i+1)%6]))
                     for i in range(6))


def transposed_original_dual(cycle,i,j):
    if type(i) is not int or type(j) is not int or not 0<=i<6 or not 0<=j<6 or i==j:
        raise ValueError("one of the 15 distinct original incidence-position transpositions required")
    if len(cycle)!=6 or any(len(edge)!=2 or not set(edge)<=set(range(6)) for edge in cycle):
        raise ValueError("actual six-position Hamiltonian dual required")
    swap={i:j,j:i}
    transformed=frozenset(
        frozenset(swap.get(k,k) for k in edge) for edge in cycle)
    if transformed not in CANONICAL_CYCLES:
        raise ValueError("invalid source dual cycle or transposition")
    return transformed


def _cycle_ordering():
    cycles={_cycle_from_order(p) for p in permutations(range(6))}
    if len(cycles)!=N:
        raise AssertionError("there must be precisely 60 undirected labeled sixcycles")
    return tuple(sorted(cycles,key=lambda z:tuple(sorted(
        tuple(sorted(e)) for e in z))))


CANONICAL_CYCLES=_cycle_ordering()
CYCLE_INDEX={c:i for i,c in enumerate(CANONICAL_CYCLES)}


def original_sixcycle_transposition_adjacency():
    """EXACT weighted 60x60 integer S6/D6 Schreier adjacency."""
    A=[[0]*N for _ in range(N)]
    physical_overlap=Counter()
    multiplicities=Counter()
    for n,c in enumerate(CANONICAL_CYCLES):
        for i,j in TRANSPOSITIONS:
            d=transposed_original_dual(c,i,j)
            k=CYCLE_INDEX[d]
            if k==n:raise AssertionError("one transposition cannot fix a labeled sixcycle")
            A[n][k]+=1
            physical_overlap[len(c & d)]+=1
        if sum(A[n])!=DEGREE:
            raise AssertionError("15 actual original POINT swaps expected at every cycle")
        multiplicities[tuple(sorted(x for x in A[n] if x))]+=1
    if any(A[i][j]!=A[j][i] for i in range(N) for j in range(N)):
        raise AssertionError("the original whole-point swap graph must be symmetric")
    if dict(physical_overlap)!={4:720,2:180}:
        raise AssertionError("original six-position dual transposition overlaps changed")
    if set(multiplicities)!={(1,)*9+(2,)*3}:
        raise AssertionError("each dual must have 9 single and 3 double neighbors")
    return tuple(tuple(row) for row in A)


ADJACENCY=original_sixcycle_transposition_adjacency()


def _matmul(a,b):
    n=len(a)
    if n==0 or len(b)!=n or any(len(row)!=n for row in a+b):
        raise ValueError("equal square integer matrices required")
    out=[[0]*n for _ in range(n)]
    for i,arow in enumerate(a):
        for k,value in enumerate(arow):
            if value:
                brow=b[k]
                for j,v in enumerate(brow):
                    if v:out[i][j]+=value*v
    return tuple(tuple(row) for row in out)


def _fraction_vandermonde_multiplicities(eigenvalues,traces):
    """Unique eigen multiplicities from five exact power traces."""
    n=len(eigenvalues)
    mat=[[Fraction(val**k) for val in eigenvalues]+[Fraction(traces[k])]
         for k in range(n)]
    for pivot in range(n):
        nonzero=next((row for row in range(pivot,n)
                      if mat[row][pivot]),None)
        if nonzero is None:
            raise AssertionError("distinct rational eigenvalues required")
        mat[pivot],mat[nonzero]=mat[nonzero],mat[pivot]
        scale=mat[pivot][pivot]
        mat[pivot]=[v/scale for v in mat[pivot]]
        for row in range(n):
            if row==pivot:continue
            mul=mat[row][pivot]
            if mul:
                mat[row]=[a-mul*b for a,b in zip(mat[row],mat[pivot])]
    return tuple(mat[i][-1] for i in range(n))


def exact_original_sixcycle_spectrum_certificate():
    """Integer matrix MINIMAL polynomial plus exact trace-unique eig multiplicities.

    This is an independent finite 60x60 rational spectral proof, not
    a floating-point numerical eigenvalue approximation.
    """
    A=ADJACENCY
    eye=tuple(tuple(int(i==j) for j in range(N)) for i in range(N))
    trace=[]
    power=eye
    for k in range(5):
        trace.append(sum(power[i][i] for i in range(N)))
        power=_matmul(power,A)
    if tuple(trace)!=(60,0,1260,1440,96300):
        raise AssertionError("exact original dual adjacency power traces changed")
    mat=eye
    for root in EIGEN_A:
        factor=tuple(tuple(A[i][j]-(root if i==j else 0)
                          for j in range(N)) for i in range(N))
        mat=_matmul(mat,factor)
    if any(v for row in mat for v in row):
        raise AssertionError("EXACT polynomial annihilator P(A) must vanish INTEGERS")
    mult=_fraction_vandermonde_multiplicities(EIGEN_A,trace)
    if mult!=tuple(Fraction(m) for m in EIGEN_MULT):
        raise AssertionError("original dual eigen multiplicities not independently certified")
    # Symmetric real A + squarefree annihilating polynomial => all
    # eigenvalues among five integer roots. Five power traces uniquely
    # determine multiplicities; hence exact full spectrum.
    return {
        "original_sixposition_dual_cycle_states":N,
        "actual_global_source_POINT_transpositions_per_state":DEGREE,
        "distinct_neighbor_cycle_states_per_state":12,
        "single_weight_neighbors":9,
        "double_weight_neighbors":3,
        "original_dual_edge_overlap_transposition_counts":{4:720,2:180},
        "integer_power_traces":tuple(trace),
        "exact_integer_annihilating_polynomial_zero":True,
        "adjacency_eigenvalues":EIGEN_A,
        "eigen_multiplicities":tuple(int(v) for v in mult),
        "laplacian_eigenvalues":EIGEN_L,
        "laplacian_nonconstant_gap":10,
        "max_laplacian_eigen":24,
        "sharp_abstract_Adirichlet_ratio_bounds":(Fraction(4,3),Fraction(16,5)),
        "sharp_abstract_centered_averaging_L2_operator_norm":Fraction(3,5),
        "all_h_original_histogram_extremizer_realizability_NOT_claimed":True,
    }


def exact_GF5_sixcycle_histogram_energy(hist,baseline=0):
    """Genuine original fiber score on 60 cycles; one full f swap acts on labels."""
    if type(baseline) is not int or baseline<0 or any(
        c not in CYCLE_INDEX or type(v) is not int or v<0 for c,v in hist.items()
    ):
        raise ValueError("valid ORIGINAL nonnegative right dual histogram and baseline required")
    value=tuple(baseline+W_D*hist.get(c,0) for c in CANONICAL_CYCLES)
    mean=Fraction(sum(value),N)
    var=sum(((v-mean)**2 for v in value),Fraction())/N
    # EXACT rational: integer sum before the Fraction denominator.
    # Never permit intermediate float division of potentially huge
    # historical GF5 weighted original sixflag counts.
    drift=Fraction(sum((
        (value[CYCLE_INDEX[transposed_original_dual(c,i,j)]]-value[k])**2
        for k,c in enumerate(CANONICAL_CYCLES)
        for i,j in TRANSPOSITIONS),0),N*DEGREE)
    if not Fraction(4,3)*var<=drift<=Fraction(16,5)*var:
        raise AssertionError("true original historical GF5 D6 violated exact spectral gap")
    local=tuple(Fraction(sum(ADJACENCY[k][j]*value[j] for j in range(N)),DEGREE)
                for k in range(N))
    smoothed_var=sum(((v-mean)**2 for v in local),Fraction())/N
    if smoothed_var>Fraction(9,25)*var:
        raise AssertionError("single genuine source POINT swap averaging not spectral-contractive")
    pos=neg=0
    for k,c in enumerate(CANONICAL_CYCLES):
        for i,j in TRANSPOSITIONS:
            delta=value[CYCLE_INDEX[transposed_original_dual(c,i,j)]]-value[k]
            pos+=max(delta,0)
            neg+=max(-delta,0)
    if pos!=neg:
        raise AssertionError("global actual original f swap transposition involution flux imbalance")
    if (var==0)!=(drift==0):
        raise AssertionError("original dual signed drift zero iff histogram constant")
    return {
        "source_original_GF5_score_by_labeled_cycle":value,
        "fixed_original_right_histogram_support":sum(x>0 for x in hist.values()),
        "histogram_original_sixflag_total":sum(hist.values()),
        "weighted_invariant_B_C_baseline":baseline,
        "exact_original_f_orbit_mean":mean,
        "exact_original_f_orbit_variance":var,
        "exact_original_single_full_POINT_swap_mean_squared_GF5_delta":drift,
        "exact_single_swap_averaging_variance":smoothed_var,
        "actual_original_global_swap_positive_signed_total":pos,
        "actual_original_global_swap_negative_signed_total":neg,
        "exact_spectral_4over3_lower_verified":True,
        "exact_spectral_16over5_upper_verified":True,
        "exact_spectral_three_fifths_averaging_contraction_verified":True,
        "arbitrary_fixed_original_center_positive_NOT_PROVED":True,
    }


def original_true_sixpoint_fiber_spectral_energy(model,points):
    """Same complete ORIGINAL f,g and real six-ID Q as previous AA4-CI."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    data=original_point_A_fiber(model,points)
    result=exact_GF5_sixcycle_histogram_energy(
        data["right_cyclic_dual_hist"],data["original_baseline_B_C_weighted"])
    if result["exact_original_f_orbit_variance"]!=data["original_exact_orbit_variance"]:
        raise AssertionError("true original 720-f-orbit variance differs from 60-state dual spectrum")
    if result["exact_original_f_orbit_mean"]!=data["original_exact_orbit_mean"]:
        raise AssertionError("true original 720-f-orbit mean differs from dual histogram")
    return result,data


def independent_original_GF5_full_factor_transposition_oracle(model,points):
    """EVERY 60 original left labeled duals ×15 COMPLETE POINT swaps.

    Independent direct historical six-ID classifier, not reuse of
    dual histogram or spectral adjacency in its classification.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    result,fiber=original_true_sixpoint_fiber_spectral_energy(model,points)
    by_perm,_=original_cycle_orbit(f,points)
    reps={}
    for i,c in enumerate(by_perm):
        reps.setdefault(c,PERMS[i])
    if len(reps)!=N:raise AssertionError("not all genuine labeled duals reached")
    Qs=tuple(Q for Q,typ,cycle in fiber["eligible_actual_original_Q"])
    def literal(full_f):
        return sum(R3_CERTIFIED_FLOORS.get(
            classify_seven_all_a_original_Q(Q,full_f,g,inc),0) for Q in Qs)
    raw_scores={}
    actual_drift=0
    for c,perm in reps.items():
        fp=complete_original_f_orbit(f,points,perm)
        old=literal(fp)
        raw_scores[c]=old
        if old!=result["source_original_GF5_score_by_labeled_cycle"][CYCLE_INDEX[c]]:
            raise AssertionError("DIRECT genuine original historical seven-GF5 source-Q disagree with spectral score")
        for i,j in TRANSPOSITIONS:
            changed=original_two_point_global_swap(fp,points[i],points[j])
            new=literal(changed)
            expected=result["source_original_GF5_score_by_labeled_cycle"][
                CYCLE_INDEX[transposed_original_dual(c,i,j)]]
            if new!=expected:
                raise AssertionError("DIRECT true original full f POINT-image swap GF5 != one dual transposition score")
            actual_drift+=(new-old)**2
    if Fraction(actual_drift,N*DEGREE)!=result["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"]:
        raise AssertionError("independent genuine original all900 whole-point swap squared flux != spectral norm")
    return {"s":s,"V":V,"a":a,"real_original_Q_in_fiber":(s+1)**6,
            "physically_right_eligible_original_Q":len(Qs),
            "60_real_original_global_f_cycle_representatives":len(raw_scores),
            "900_real_original_global_POINT_swaps_verified":N*DEGREE,
            "actual_original_GF5_exact_energy":result["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"],
            "exact_spectral_certificate":result,
            "original_source_hypothesis_status":"OPEN_WITH_FORMAL_BLOCKER"}


def original_allh_maximal_named_D6_fan_energy(power):
    """One genuine ORIGINAL AA4-CH fan, concentration at one dual C6."""
    z=original_maximal_D6_fan(power)
    s,V,a,inc,f,g,_,_=_original_source(z["normal_model"])
    points=z["point_ids"]
    H=Counter()
    for Q in z["fan"]:
        right=tuple(g[inc[next(j for j in Q if inc[j][0]==p)][1]]
                    for p in points)
        cyc=_six_position_dual_cycle(right)
        if cyc is None:raise AssertionError("genuine original D6 Q must have a labeled C6")
        H[cyc]+=1
    m=s+1
    if len(H)!=1 or list(H.values())!=[m]:
        raise AssertionError("all original AA4-CH named Q must have SAME physical right dual C6")
    energy=exact_GF5_sixcycle_histogram_energy(H)
    var=Fraction(59,3600)*(W_D*m)**2
    mean_squared=Fraction(1,30)*(W_D*m)**2
    if energy["exact_original_f_orbit_variance"]!=var or (
        energy["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"]!=mean_squared):
        raise AssertionError("all-h symbolic single-dual-support AA4-CH named fan energy wrong")
    return {"s":s,"named_genuine_original_Q_count":m,
            "symbolic_exact_orbit_variance":var,
            "symbolic_exact_single_global_POINT_swap_mean_squared_GF5_delta":mean_squared,
            "squared_energy_to_variance_ratio":Fraction(120,59),
            "history_is_named_fan_NOT_whole_original_S":True}
