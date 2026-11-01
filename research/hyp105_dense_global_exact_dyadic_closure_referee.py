"""AA4-ROOTJOINT: rigorous single-gate all-h dense/heavy original Branch A.

A NEW exact integral dyadic closure integrating independently proved
source-aware core budget #690, stronger source-heavy selector #697,
correct conservative proper-path/selector #672, and new FULL/CORE
internal blocker B0=15*sqrt((K+1)T) from #701.

C_graph,c_graph are existential and NUMERICALLY UNKNOWN. Fraction inputs
are only HYPOTHETICAL mathematical substitution for testing, never
published values. This is a conditional proof ledger, NOT human refereeing.

For actual s=2**h, after the original source selector/dense-core
hypotheses, one has:
  2 U_BBo >= s^6/2 - 84*T*s^5
             - 8*sigma3_inv*sqrt(L6)*s^(11/2)
             - 4*sqrt(B0*T*L4)*s^(47/8).
We certify the three relative losses SUM<=1/4, not independent heuristic
rounded term comparisons, in EXACT rational arithmetic.

Independent finite full ORIGINAL W32/W34 path mass partition oracle
checks original incidence owners and 2-to-1 BBo witness fibers, but
finite h=1,2 are NOT substituted for universal h>=6 proof.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt

from hyp105_full_physical_degree_tail import genuine_source

EPSILON=Fraction(1787,4096)
K=64
SIG2_INV=64*(K+1)**2
SIG3_INV=64*27*(K+1)**3
BUDGET_LOWER=Fraction(7,16)-Fraction(38245,33554432)


def _positive_exact(value):
    if type(value) not in (int,Fraction) or Fraction(value)<=0:
        raise ValueError("positive exact rational placeholders only, NOT graph constants")
    return Fraction(value)


def _ceil_fraction(q):
    q=Fraction(q)
    return -(-q.numerator//q.denominator)


def _ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative integer square root")
    r=isqrt(n)
    return r+(r*r<n)


def _min_original_alphabet(V):
    if type(V) is not int or V<=0:raise ValueError("original positive V")
    a=(1+isqrt(8*V+1))//2
    while a*(a-1)<2*V:a+=1
    while a>2 and (a-1)*(a-2)>=2*V:a-=1
    return a


def actual_source_budget(s):
    """All-h original exact N,Cs and uniform analytic epsilon budget."""
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("dyadic original s>=64 only")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=_min_original_alphabet(V)
    Cs=(s*s+1)*(s*s+a-2)
    actual=Fraction(N,s**4)-Fraction(1,2)-Fraction(Cs,16*s**4)
    if not (EPSILON<BUDGET_LOWER<=actual):
        raise AssertionError("genuine all-h original FULL source eps core budget failed")
    if (64*a)**2>97**2*s**3:
        raise AssertionError("actual original minimal alphabet violates all-h bound")
    return {
        "s":s,"V":V,"original_source_flags":N,"minimal_pair_alphabet":a,
        "exact_original_book_Cs":Cs,
        "exact_epsilon_core_budget":actual,
        "analytically_proved_all_h_lower_budget":BUDGET_LOWER,
        "epsilon_chosen":EPSILON,
        "paired_CORE_edges_lower_if_small_full_tail":
            2*(Fraction(N)-EPSILON*s**4-Fraction(Cs,16)),
        "core_m0_at_least_s4_proved":True,
    }


def _ceil_nth_root(n,k):
    """Exact binary-search ceil integer k-th root, k only 2 or 8."""
    if type(n) is not int or n<0 or k not in (2,8):
        raise ValueError("nonnegative integer root of order 2 or 8")
    if n==0:return 0
    lo,hi=0,1<<((n.bit_length()+k-1)//k)
    while lo<hi:
        m=(lo+hi)//2
        if m**k>=n:hi=m
        else:lo=m+1
    return lo


def _pow2_fractional_upper(remainder,denominator):
    """Exact upper for 2^(r/d) with denominator 256, no floating point."""
    if denominator not in (2,8) or type(remainder) is not int or not 0<=remainder<denominator:
        raise ValueError("root remainder must lie within proper degree")
    numerator=_ceil_nth_root((2**remainder)*(256**denominator),denominator)
    if numerator**denominator<(2**remainder)*(256**denominator):
        raise AssertionError("ceil root bound failed")
    return Fraction(numerator,256)


def _normalized_power_upper(h,num,den):
    """Rational upper bound to s^(num/den)/s^6 for s=2^h."""
    q,r=divmod(h*num,den)
    if 6*h<q:
        raise ValueError("positive root exponent exceeds sextic scale")
    return _pow2_fractional_upper(r,den)/2**(6*h-q)


def _ceil_log2(n):
    if type(n) is not int or n<=0:raise ValueError("positive integer")
    return (n-1).bit_length()


def integrated_dense_closure(C_graph,c_graph,*,prior_B0=False):
    """Return guaranteed all-h 2^h gate for HYPOTHETICAL rational constants.

    priors use SAME improved heavy T and SAME conservative dense path
    moment constants, change ONLY the 64 versus 15 mixed blocker B0.
    """
    C,c=map(_positive_exact,(C_graph,c_graph))
    beta=5*EPSILON**2/(384+40*EPSILON)
    T=max(1,_ceil_fraction(2**19*C**3/beta**3))
    alpha=c*(beta/32)**6
    delta=min(Fraction(1,8),alpha)
    L6=24+576*T*T
    L4=2*SIG2_INV**2*_ceil_sqrt(8*L6)+56*T
    bmult=64 if prior_B0 else 15
    B0=bmult*_ceil_sqrt((K+1)*T)
    E=8*SIG3_INV*_ceil_sqrt(L6)
    D=4*_ceil_sqrt(B0*T*L4)
    if not (beta>EPSILON**2/128 and T>0 and
            0<delta<=Fraction(1,8) and B0>0):
        raise AssertionError("root mixed old/new heavy constants malformed")

    # All-h exact SUFFICIENT upper using each loss <=s^6/12:
    # 84T/s <=1/12, E/s^(1/2)<=1/12, D/s^(1/8)<=1/12.
    s_separate=max(64,1008*T,(12*E)**2,(12*D)**8)
    h_sep=_ceil_log2(s_separate)

    def ledger(h):
        if type(h) is not int or h<6:raise ValueError("dyadic h>=6 only")
        first=Fraction(84*T,2**h)
        second=E*_normalized_power_upper(h,11,2)
        third=D*_normalized_power_upper(h,47,8)
        return first,second,third
    if sum(ledger(h_sep))>Fraction(1,4):
        raise AssertionError("independent sum-of-three gate not implied by individual certificates")

    # Better *joint* criterion; each of the actual three exact radical
    # losses divided by s6 decreases strictly for all real s>0. The
    # upper rational at the FINAL chosen s alone therefore certifies ALL
    # larger s, even if root-rounding fluctuations exist between dyadic h.
    low,hi=6,h_sep
    while low<hi:
        mid=(low+hi)//2
        if sum(ledger(mid))<=Fraction(1,4):hi=mid
        else:low=mid+1
    h=low
    if sum(ledger(h))>Fraction(1,4):
        raise AssertionError("selected joint dyadic bound not certified")
    # Nearby downward exact check; no claim global minimality.
    while h>6 and sum(ledger(h-1))<=Fraction(1,4):
        h-=1
    losses=ledger(h)
    return {
        "epsilon":EPSILON,
        "source_uniform_core_budget":BUDGET_LOWER,
        "original_conflict_max_degree_K":K,
        "new_heavy_original_flag_fraction_beta":beta,
        "hypothetical_C_graph":C,
        "hypothetical_c_graph":c,
        "original_heavy_tail_T":T,
        "heavy_D6_coefficient_alpha":alpha,
        "root_delta":delta,
        "conservative_sigma2_inverse":SIG2_INV,
        "conservative_sigma3_inverse":SIG3_INV,
        "conservative_L6":L6,
        "ceil_fourth_moment_L4":L4,
        "mixed_blocker_B0_conservative_integer":B0,
        "mixed_blocker_coefficient":bmult,
        "exceptional_term_E":E,
        "internal_term_D":D,
        "dyadic_h0_individually_budgeted":h_sep,
        "dyadic_h0_combined_exact_rational":h,
        "joint_certified_relative_losses_upper":losses,
        "joint_certified_remaining_fraction":Fraction(1,2)-sum(losses),
        "core_U_BBo_lower_coefficient":Fraction(1,8),
        "conditional_signed_GF5_R3_floor":
            min(54162*delta,Fraction(53526,8))/51**6,
        "applies_to_all_larger_dyadic_h_by_analytic_monotone_losses":True,
        "graph_constants_ACTUALLY_UNKNOWN_NOT_CERTIFIED":True,
        "branch_A_requires_all_previous_original_geometric_lemmas":True,
        "not_an_external_scientific_referee":True,
    }


def finite_true_original_path_partition(power,f,g,core_ids=None):
    """FULL original projection vs independent physical FIRST path census.

    Actual ORIGINAL W32/W34 sources ONLY; no historical #672/#694 code.
    No claim that s2,s4 satisfies asymptotic source core guarantees.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("real original finite W32/W34 only")
    s,V,flags=genuine_source(power)
    a=_min_original_alphabet(V)
    legal=set(combinations(range(a),2))
    try:f=tuple(tuple(p) for p in f);g=tuple(tuple(p) for p in g)
    except (ValueError,TypeError):raise ValueError("complete pair labels required")
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or
        any(p not in legal for p in f+g)):
        raise ValueError("fixed full separate ORIGINAL f,g pair injections required")
    I=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if (len(set(I))!=len(I) or any(type(i) is not int or
            i<0 or i>=len(flags) for i in I)):
        raise ValueError("valid unique true original core ID subset required")
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    flag_id={}
    for i,(p,l) in enumerate(flags):
        pencils[p].add(l);through[l].add(p);flag_id[p,l]=i
    col=[set().union(*(through[l] for l in pencils[p]))-{p} for p in range(V)]
    projected={}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:continue
            pp=col[q]&through[r]
            if len(pp)!=1:raise AssertionError("source GQ projection not unique")
            p=next(iter(pp))
            ell=pencils[q]&pencils[p]
            if len(ell)!=1:raise AssertionError("original connecting line not unique")
            l=next(iter(ell))
            projected[q,r]=(p,l,(flag_id[q,l],flag_id[p,l],flag_id[p,r]))
    edges={}
    H=defaultdict(set)
    for i in I:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            edge=frozenset((u,v))
            if len(edge)!=2 or edge in edges:
                raise AssertionError("not uniquely sourced ORIGINAL physical edge")
            edges[edge]=i
            H[u].add(v);H[v].add(u)
    finv={pair:i for i,pair in enumerate(f)}
    ginv={pair:i for i,pair in enumerate(g)}
    counts=Counter()
    BBo=defaultdict(set)
    for v0 in H:
        for v1 in H[v0]:
            for v2 in H[v1]:
                for v3 in H[v2]:
                    C=(v0,v1,v2,v3)
                    counts["W3"]+=1
                    if len({v[0] for v in C})!=4 or len({v[1] for v in C})!=4:
                        counts["improper"]+=1
                        continue
                    counts["proper"]+=1
                    q=finv.get(tuple(sorted((v0[0],v3[0]))))
                    r=ginv.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        counts["missing"]+=1;continue
                    if (q,r) not in projected:
                        counts["incident"]+=1;continue
                    p,l,anchors=projected[q,r]
                    if set(f[p])&{v0[0],v3[0]} or set(g[l])&{v0[1],v3[1]}:
                        counts["endbad"]+=1;continue
                    if set(f[p])&{v1[0],v2[0]} or set(g[l])&{v1[1],v2[1]}:
                        counts["internal"]+=1;continue
                    pathowners=tuple(edges[frozenset((C[j],C[j+1]))] for j in range(3))
                    Q=tuple(sorted(pathowners+anchors))
                    if (len(set(Q))!=6 or
                        len({flags[j][0] for j in pathowners})!=3 or
                        len({flags[j][1] for j in pathowners})!=3):
                        raise AssertionError("true original image BBo owner ambiguity")
                    BBo[Q].add(C)
                    counts["unblocked"]+=1
    if counts["W3"]!=sum(counts[k] for k in (
        "improper","missing","incident","endbad","internal","unblocked")):
        raise AssertionError("true original full/core physical W3 mass not conserved")
    if any(len(ps)!=2 or tuple(reversed(next(iter(ps)))) not in ps
           for ps in BBo.values()):
        raise AssertionError("true original BBo sextuple not two directed reverse physical paths")
    if counts["unblocked"]!=2*len(BBo):
        raise AssertionError("actual source BBo two-fold fiber count mismatch")
    deg={u:len(ns) for u,ns in H.items()}
    directW3=sum(deg[u]*deg[v] for u in H for v in H[u])
    if counts["W3"]!=directW3:
        raise AssertionError("independent direct degree-product walk count mismatch")
    return {
        "s":s,"original_source_flags_full":len(flags),
        "original_source_flags_core":len(I),
        "original_physical_edges":len(edges),
        "actual_directed_W3":counts["W3"],
        "improper_directed_W3":counts["improper"],
        "proper_directed_W3":counts["proper"],
        "proper_missing_endpoint":counts["missing"],
        "proper_incident_endpoint":counts["incident"],
        "proper_nonincident_bad_endpoint":counts["endbad"],
        "proper_good_internal_blocked":counts["internal"],
        "proper_good_unblocked":counts["unblocked"],
        "original_BBo_sixset_count":len(BBo),
        "independent_degree_product_W3":directW3,
        "all_seven_source_physical_accounting_classes_exact":True,
        "not_an_sge64_dense_branch_certificate":True,
    }
