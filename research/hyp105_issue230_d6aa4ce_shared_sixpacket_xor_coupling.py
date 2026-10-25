"""AA4-CE: all-h TRUE-ORIGINAL sixpacket shared physical-mask coupling.

Fix six pairwise disjoint actual original LINE-factor image-swap packets,
one complete globally injected original f,g and the SAME original
six-incidence-ID Q over all 64 complete globally swapped right maps.

For sixth-sensitive source Q (one selected LINE per packet), define its
source orientation t_Q. The right physical six-edge 2-factor predicate is
R_g(x XOR t_Q), with ONE common 64-bit physical mask R_g. Consequently:
- all original Q right physical 2factor masks are exact XOR translates;
- joint admissibility of any two Q is a real shared-mask autocorrelation;
- same-map weighted sixth-sensitive historical GF5 positives W_6(x)
  are bounded pointwise by B(x)=sum_t H_f(t)R_g(x XOR t);
- the latter is an exact XOR convolution with Fourier factorization;
- physical GF2 syndrome classes give genuine cross-Q exclusions.

This is a NECESSARY 2factor surrogate, not historical GF5 equivalence.
No independence of Q, source IDs, or f/g; not root Branch A/B/C.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps, validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    original_six_packet_source_line_A,
    physical_right_is_six_vertex_two_regular,
)
from hyp105_issue230_d6aa4cb_original_physical_parity_code import (
    gf2_rank, parity_columns_from_12_images, syndrome,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

DIM = 6
N = 1 << DIM
DEFAULT_PACKETS = ((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


def fwht64(values):
    """Pure integer unnormalized XOR Walsh transform, self-inverse / 64."""
    if len(values) != N or any(type(v) is not int for v in values):
        raise ValueError("expected exactly 64 integer inputs")
    out = list(values)
    width = 1
    while width < N:
        for left in range(0, N, 2*width):
            for j in range(width):
                a, b = out[left+j], out[left+j+width]
                out[left+j], out[left+j+width] = a+b, a-b
        width <<= 1
    return tuple(out)


def _inverse64(spectrum):
    transformed = fwht64(spectrum)
    if any(z % N for z in transformed):
        raise AssertionError("integer inverse XOR Walsh transform inconsistent")
    return tuple(z // N for z in transformed)


def xor_convolution64(a, b):
    """Exact B(x)=sum_t a(t)b(x xor t), no independence assumptions."""
    if len(a) != N or len(b) != N or any(
        type(v) is not int or v < 0 for v in tuple(a)+tuple(b)
    ):
        raise ValueError("64 nonnegative integer source/mask entries required")
    result = _inverse64(tuple(x*y for x,y in zip(fwht64(a),fwht64(b))))
    if any(v < 0 for v in result):
        raise AssertionError("nonnegative convolution cannot be negative")
    return result


def physical_right_mask_for_packets(original_g, packets):
    """ONE common right 2-factor mask, independently of original Q."""
    g = tuple(original_g)
    pairs = validate_disjoint_factor_swaps(len(g), packets)
    if len(pairs) != DIM or len(set(g)) != len(g):
        raise ValueError("six packets and one complete injective right map required")
    chosen = tuple((tuple(g[u]),tuple(g[v])) for u,v in pairs)
    edges = [tuple(sorted(e)) for pair in chosen for e in pair]
    if any(len(e) != 2 or e[0] == e[1] for e in edges) or len(set(edges)) != 12:
        raise ValueError("twelve globally distinct physical unordered edges required")
    mask = []
    for x in range(N):
        degree = Counter(v for j in range(DIM)
                         for v in chosen[j][(x >> j) & 1])
        mask.append(int(len(degree) == 6 and all(k == 2 for k in degree.values())))
    columns = parity_columns_from_12_images(chosen)
    rank = gf2_rank(columns)
    baseline = 0
    for edge,_ in chosen:
        baseline ^= (1 << edge[0]) ^ (1 << edge[1])
    for x,v in enumerate(mask):
        if v and syndrome(columns,x) != baseline:
            raise AssertionError("true 2factor violates physical GF2 parity")
    if rank == 1 and any(mask):
        raise AssertionError("rank-one physical 2factor contradicts AA4-CC")
    return {"mask":tuple(mask),"columns":columns,"rank":rank,
            "baseline_parity":baseline,"packet_edges":chosen,
            "active_right_states":sum(mask)}


def orientation_of_true_original_Q(Q,inc,packets,V):
    """Source LINE used by Q in each true original disjoint source packet."""
    pairs = validate_disjoint_factor_swaps(V,packets)
    if len(pairs) != DIM or not original_six_packet_source_line_A(
        Q,inc,pairs,V
    ):
        raise ValueError("require six distinct original flags, one LINE per packet")
    lines = frozenset(inc[j][1] for j in Q)
    t = sum((1 << i) for i,(u,v) in enumerate(pairs) if v in lines)
    if any((u in lines) == (v in lines) for u,v in pairs):
        raise AssertionError("expected exactly one original LINE per packet")
    return t


def autocorrelation64(mask):
    """A(delta)=sum_x mask(x)mask(x xor delta); exact Fourier square check."""
    if len(mask) != N or any(type(z) is not int or z not in (0,1)
                             for z in mask):
        raise ValueError("64 actual physical Boolean mask values required")
    ac = _inverse64(tuple(z*z for z in fwht64(mask)))
    if any(a < 0 for a in ac) or ac[0] != sum(mask):
        raise AssertionError("autocorrelation identity failed")
    return ac


def physical_cross_Q_certificate(mask, t, u, columns=None):
    """Joint physical eligibility of Q,Q' for ONE uniform COMPLETE map x."""
    ac = autocorrelation64(mask)
    delta = t ^ u
    simultaneous = ac[delta]
    if columns is not None and syndrome(columns,delta) and simultaneous:
        raise AssertionError("different physical parity syndromes cannot coincide")
    return {
       "relative_orientation":delta,
       "joint_possible_complete_right_maps":simultaneous,
       "joint_physical_probability":Fraction(simultaneous,N),
       "single_physical_probability":Fraction(sum(mask),N),
       "physical_covariance":Fraction(simultaneous,N)-
           Fraction(sum(mask)**2,N*N),
       "incompatible_syndromes_imply_zero":(
           columns is None or not syndrome(columns,delta) or simultaneous == 0),
    }


def source_orientation_histogram_W32(model,packets):
    """True original f-side left-eligible sixth-packet Q, no g re-draw."""
    s,V,a,inc,f,g,_,_ = _original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite source histogram oracle only original W32")
    pairs = validate_disjoint_factor_swaps(V,packets)
    if len(pairs)!=DIM:raise ValueError("six packets")
    H=[0]*N; Qs=[]
    weighted = Counter()
    for Q,_ in selected_left_six(model):
        if not original_six_packet_source_line_A(Q,inc,pairs,V):
            continue
        tag=immutable_original_sixflag_class(Q,inc)
        if tag not in R3_CERTIFIED_FLOORS:
            raise AssertionError("true sixth-packet Q missing immutable selected GF5 class")
        t=orientation_of_true_original_Q(Q,inc,pairs,V)
        w=R3_CERTIFIED_FLOORS[tag]
        H[t]+=w
        weighted[tag]+=1
        Qs.append((tuple(Q),t,w,tag))
    if len(Qs) != (351 if model.get("scheme")=="lex" else 301) and (
        len(Qs) not in (351,301)
    ):
        raise AssertionError("true original W32 selected sixpacket Q census drift")
    return {"orientation_mass":tuple(H),"source_Q":tuple(Qs),
            "candidate_Q_count":len(Qs),
            "total_source_weight":sum(H),
            "source_class_histogram":dict(weighted),
            "f_only_orientation_distribution":True}


def shared_sixpacket_W32_certificate(model,packets=DEFAULT_PACKETS,
                                    verify_all_Q=False):
    """Global f source histogram convolved with ONE physical right g mask.

    All historical Q retain their original six incidence IDs and original
    point f and LINE g are the SAME globally injected maps.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    packets=validate_disjoint_factor_swaps(V,packets)
    hist=source_orientation_histogram_W32(model,packets)
    shared=physical_right_mask_for_packets(g,packets)
    H=hist["orientation_mass"]; R=shared["mask"]
    B=xor_convolution64(H,R)
    direct=tuple(sum(H[t]*R[x^t] for t in range(N)) for x in range(N))
    if B!=direct:
        raise AssertionError("independent direct convolution and Walsh disagree")
    ac=autocorrelation64(R)
    raw_pair_numerator=sum(H[t]*H[u]*ac[t^u]
                           for t in range(N) for u in range(N))
    if raw_pair_numerator != sum(z*z for z in B):
        raise AssertionError("shared multi-Q correlation identity failed")
    eta_mass = Counter()
    for t,amt in enumerate(H):
        if amt: eta_mass[syndrome(shared["columns"],t)] += amt
    # Physical parity equation from AA4-CB/CC: only one source class
    # with syndrome(beta) xor D*x can be physically eligible at x.
    beta=shared["baseline_parity"]
    # Distinct source Q in DIFFERENT syndrome classes can never jointly
    # pass right physical 2factor on the SAME original complete g^x.
    # Since source weights are positive, these integer quantities measure
    # exact ordered-class/excluded orientation-pair WEIGHT products, not
    # historical accepted GF5 counts or a universal motif lower bound.
    forbidden_syndrome_pairs=(
        sum(H)**2-sum(v*v for v in eta_mass.values()))//2
    forbidden_physical_orientations=sum(
        H[t]*H[u] for t in range(N) for u in range(t+1,N)
        if ac[t^u] == 0)
    # Unweighted GQ six-incidence-ID pair certificate. These are genuine
    # DISTINCT Q pairs, not label-orbit counts or weighted mass proxies.
    count_by_t=Counter(t for _Q,t,_w,_class in hist["source_Q"])
    count_by_syndrome=Counter()
    for t, n in count_by_t.items():
        count_by_syndrome[syndrome(shared["columns"],t)]+=n
    Qn=hist["candidate_Q_count"]
    forbidden_syndrome_Q_pairs=(
        Qn**2-sum(n*n for n in count_by_syndrome.values()))//2
    forbidden_physical_Q_pairs=sum(
        count_by_t[t]*count_by_t[u]
        for t in range(N) for u in range(t+1,N) if ac[t^u] == 0)
    if forbidden_physical_Q_pairs < forbidden_syndrome_Q_pairs:
        raise AssertionError("exact physical Q pair obstruction must dominate parity")
    if forbidden_physical_orientations < forbidden_syndrome_pairs:
        raise AssertionError("literal physical pair exclusion must dominate parity")
    for x in range(N):
        potentially_eligible=eta_mass.get(beta ^ syndrome(shared["columns"],x),0)
        if B[x]>potentially_eligible:
            raise AssertionError("one-original-g parity class mass bound violated")
    if verify_all_Q:
        full_maps = tuple(apply_disjoint_factor_swaps(
            g,packets,tuple(i for i in range(DIM) if x >> i & 1))
            for x in range(N))
        actual=[0]*N
        for Q,t,w,tag in hist["source_Q"]:
            for x in range(N):
                literal=physical_right_is_six_vertex_two_regular(Q,inc,full_maps[x])
                if int(literal)!=R[x^t]:
                    raise AssertionError("same original Q right 2factor is NOT shared XOR translate")
                historical=classify_seven_prechecked(Q,f,full_maps[x],inc)
                if historical is not None:
                    if historical!=tag or not literal:
                        raise AssertionError("historical seven GF5 not subset of shared physical support")
                    actual[x]+=w
        if any(actual[x]>B[x] for x in range(N)):
            raise AssertionError("historical sixpacket selected GF5 violates shared upper envelope")
    else:
        actual=None
    return {
       "original_s":s,"original_source_Q_count":hist["candidate_Q_count"],
       "source_total_weight":hist["total_source_weight"],
       "source_histogram_H":H,
       "right_physical_R":R,
       "right_physical_active_states":sum(R),
       "global_right_parity_rank":shared["rank"],
       "weighted_source_parity_groups":dict(eta_mass),
       "forbidden_distinct_syndrome_weighted_Q_pairs":forbidden_syndrome_pairs,
       "forbidden_distinct_orientation_physical_Q_pairs":forbidden_physical_orientations,
       "total_unordered_source_Q_pairs":Qn*(Qn-1)//2,
       "forbidden_distinct_syndrome_source_Q_pairs":forbidden_syndrome_Q_pairs,
       "forbidden_distinct_orientation_physical_source_Q_pairs":forbidden_physical_Q_pairs,
       "xor_convolution_upper_B":B,
       "center_physical_upper_B0":B[0],
       "uniform_mean_B":Fraction(sum(B),N),
       "expected_mean_B":Fraction(sum(H)*sum(R),N),
       "uniform_second_moment_B":Fraction(sum(z*z for z in B),N),
       "pair_autocorrelation":ac,
       "true_original_six_touch_weighted_GF5_scores":tuple(actual) if actual else None,
       "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
