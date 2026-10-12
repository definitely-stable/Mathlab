"""K3-G2-N: exact rank-six Johnson harmonics for the ORIGINAL C0 overlap.

All-a analytic result: the physical six-edge two-factor target is a
1-design; its degree-two Johnson component is determined by adjacent
versus disjoint pairs of physical K_a edges. The remaining component
belongs exactly to Johnson levels 3..6, not to an assumed noise floor.

Finite executable decomposition is restricted to K6 (K=15), where
all C(15,6)=5005 physical sixsets are explicitly available. Both B/A
and the ORIGINAL GQ-dual A/B use independent C0 weighted sixsources.
No universal P2/P7, all-h positive minimum, or ASET claim is made.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets, source_weighted_BA_hypergraph,
    exact_BA_overlap, random_injection_expectation,
)
from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model, exact_two_family_point, _anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling


def rat(x):
    x=Fraction(x)
    return [x.numerator,x.denominator]


def target_low_harmonics(a):
    """ALL a>=6: exact H0,H1,H2 target and H>=3 squared energy.

    For K=C(a,2), |T|=70*C(a,6), M=C(K,6), p=|T|/M,
    c_adj=7*C(a-3,3), c_dis=14*C(a-4,2), lambda2=C(K-4,4):
      h2(e,e')=(c_type-p*C(K-2,4))/lambda2.
    The H2 value on a physical sixset S is sum of h2 over 15 pairs.
    Each h2 coefficient has zero one-point down-marginal.
    """
    if type(a) is not int or a<6:
        raise ValueError("physical coordinate alphabet a>=6 required")
    K=comb(a,2)
    M=comb(K,6)
    target_mass=70*comb(a,6)
    p=Fraction(target_mass,M)
    lam2=comb(K-4,4)
    n_adj=a*comb(a-1,2)
    n_dis=3*comb(a,4)
    c_adj=7*comb(a-3,3)
    c_dis=14*comb(a-4,2)
    expectation=p*comb(K-2,4)
    h_adj=(c_adj-expectation)/lam2
    h_dis=(c_dis-expectation)/lam2
    # By physical S_a symmetry, every pair label has a zero down-sum.
    if 2*(a-2)*h_adj+comb(a-2,2)*h_dis!=0:
        raise AssertionError("physical two-orbit H2 is not harmonic")
    E0=Fraction(target_mass*target_mass,M)
    E2=lam2*(n_adj*h_adj*h_adj+n_dis*h_dis*h_dis)
    Ehigh=Fraction(target_mass)-E0-E2
    if Ehigh<0 or n_adj+n_dis!=comb(K,2):
        raise AssertionError("target Johnson energy identity failed")
    return {
        "a":a,"K":K,"M":M,"target_count":target_mass,
        "density":p,"lambda2":lam2,
        "h2_adj":h_adj,"h2_dis":h_dis,
        "E0":E0,"E1":Fraction(0),"E2":E2,"E_ge3":Ehigh,
        "second_level_zero":h_adj==h_dis==0,
    }


def physical_pair_indices(a=6):
    return {e:i for i,e in enumerate(combinations(range(a),2))}


def six_image_index(source, labels, palette):
    """Fail closed on a genuine injective mapping of ORIGINAL sixsets."""
    labels=tuple(tuple(x) for x in labels)
    if len(set(labels))!=len(labels) or any(
            e not in palette for e in labels):
        raise ValueError("distinct unordered physical pair labels required")
    if len(source)!=6 or len(set(source))!=6 or any(
            type(v) is not int or not 0<=v<len(labels) for v in source):
        raise ValueError("six DISTINCT valid original endpoint IDs required")
    return tuple(sorted(palette[labels[v]] for v in source))


def adjacent_pair_count(six, palette_edges):
    """Sum_v binom(deg_S(v),2), equivalent to adjacent edge-pair count."""
    edges=[palette_edges[i] for i in six]
    return sum(bool(set(x)&set(y)) for x,y in combinations(edges,2))


def target_H2_value(six, palette_edges, low):
    if len(six)!=6 or len(set(six))!=6:
        raise ValueError("physical sixset must have six distinct edges")
    adj=adjacent_pair_count(six,palette_edges)
    return adj*low["h2_adj"]+(15-adj)*low["h2_dis"]


def exact_target_johnson_decomposition():
    """K6: 7 orthogonal H_j columns on the COMPLETE J(15,6).

    Extract increasing j via b_j(A)=sum_{S supersets A} residual(S)
    and h_j=b_j/C(15-2*j,6-j). The jth lifted component on S
    is sum_{A subset S, |A|=j} h_j(A). Each h_j is a down-kernel.
    """
    K,k=15,6
    palette=physical_pair_indices(6)
    sets=tuple(combinations(range(K),k))
    targets={tuple(sorted(palette[e] for e in T))
             for T in simple_six_2factor_targets(6)}
    if len(sets)!=5005 or len(targets)!=70:
        raise AssertionError("complete K6 Johnson universe changed")
    residual=[Fraction(int(S in targets)) for S in sets]
    layers=[]
    coefficients=[]
    for j in range(k+1):
        marg=Counter()
        for S,r in zip(sets,residual):
            if r:
                for A in combinations(S,j):
                    marg[A]+=r
        lam=comb(K-2*j,k-j)
        if lam<=0:
            raise AssertionError("invalid Johnson lift eigenvalue")
        h={A:Fraction(marg[A],lam)
           for A in combinations(range(K),j)}
        if j:
            down=Counter()
            for A,value in h.items():
                if value:
                    for sub in combinations(A,j-1):
                        down[sub]+=value
            if any(down.values()):
                raise AssertionError("rank-j coefficient not harmonic")
        comp=tuple(sum((h[A] for A in combinations(S,j)),
                       Fraction(0)) for S in sets)
        residual=[r-c for r,c in zip(residual,comp)]
        layers.append(comp)
        coefficients.append(h)
    if any(residual):
        raise AssertionError("six harmonic lifts did not reconstruct target")
    # Orthogonality is checked independently against all pairwise columns.
    energies=[sum((v*v for v in comp),Fraction(0)) for comp in layers]
    for i in range(7):
        for j in range(i):
            if sum((x*y for x,y in zip(layers[i],layers[j])),
                   Fraction(0)):
                raise AssertionError("nonorthogonal Johnson ranks")
    low=target_low_harmonics(6)
    if (energies[0],energies[1],energies[2])!=(
            low["E0"],low["E1"],low["E2"]):
        raise AssertionError("explicit 0/1/2 target orbit formula failed")
    if sum(energies[3:],Fraction(0))!=low["E_ge3"]:
        raise AssertionError("high-rank target energy mismatch")
    palette_edges=tuple(combinations(range(6),2))
    if any(comp!=target_H2_value(S,palette_edges,low)
           for S,comp in zip(sets,layers[2])):
        raise AssertionError("H2 2-orbit formula differs from projection")
    return sets,tuple(layers),tuple(energies)


@lru_cache(maxsize=1)
def _frozen_target_W32():
    sets,components,energies=exact_target_johnson_decomposition()
    return ({S:idx for idx,S in enumerate(sets)},components,energies)


def source_energy_ge3(weights, labels, *, a):
    """Exact low-rank projections of a zero-padded physical 6-source.

    The physical alphabet size a MUST be explicit. For V<K injections,
    the largest coordinate appearing in occupied pair labels may be less
    than a-1; inferring a from used labels would silently compute WRONG
    Johnson denominators and source energy. Unused K_a pair labels remain
    zero, not removed from J(K,6).
    """
    if type(a) is not int or a<6:
        raise ValueError("explicit physical alphabet a>=6 required")
    labels=tuple(tuple(e) for e in labels)
    palette=physical_pair_indices(a)
    K=comb(a,2)
    if (not 6<=len(labels)<=K or len(set(labels))!=len(labels)
            or any(e not in palette for e in labels)):
        raise ValueError("legal injective K_a physical pair labels required")
    mass=0
    norm=0
    degree=[0]*K
    codegree=Counter()
    used=set()
    for R,w in weights.items():
        if type(w) is not int or w<0:
            raise ValueError("nonnegative integer ORIGINAL weights required")
        S=six_image_index(R,labels,palette)
        if S in used:
            raise ValueError("duplicate six-image from an invalid original source")
        used.add(S)
        mass+=w
        norm+=w*w
        for e in S:
            degree[e]+=w
        for pair in combinations(S,2):
            codegree[pair]+=w
    M=comb(K,6)
    lam1=comb(K-2,5)
    lam2=comb(K-4,4)
    c0=Fraction(mass,M)
    h1=[Fraction(deg-c0*comb(K-1,5),lam1) for deg in degree]
    if sum(h1):
        raise AssertionError("source rank-one down-kernel failed")
    h2={}
    for pair in combinations(range(K),2):
        u,v=pair
        h2[pair]=Fraction(
            codegree[pair]-c0*comb(K-2,4)-
            (h1[u]+h1[v])*comb(K-3,4),lam2)
    # Down-kernel of H2, checked without constructing C(K,6) vectors.
    for v in range(K):
        if sum((h2[min(v,u),max(v,u)] for u in range(K) if u!=v),
               Fraction(0)):
            raise AssertionError("source rank-two down-kernel failed")
    E0=Fraction(mass*mass,M)
    E1=lam1*sum((v*v for v in h1),Fraction(0))
    E2=lam2*sum((v*v for v in h2.values()),Fraction(0))
    Ehigh=Fraction(norm)-E0-E1-E2
    if Ehigh<0:
        raise AssertionError("source high-rank energy negative")
    return {"mass":mass,"norm2":norm,"E0":E0,
            "E1":E1,"E2":E2,"E_ge3":Ehigh}


def spectral_overlap_certificate(weights, labels):
    """Independent rank-by-rank exact overlap, with rigorous CS bound.

    |<W_ge3,T_ge3>|² <= ||W_ge3||² ||T_ge3||².
    A violation of P2 therefore REQUIRES, not follows from,
    U_AB + C2 < sqrt(E_W_ge3 E_T_ge3).
    """
    palette=physical_pair_indices(6)
    if len(labels)!=15:
        raise ValueError("complete W32/K6 source labeling required")
    indices,components,energies=_frozen_target_W32()
    corr=[Fraction(0)]*7
    for R,w in weights.items():
        if type(w) is not int or w<0:
            raise ValueError("nonnegative integer weights required")
        S=six_image_index(R,labels,palette)
        idx=indices[S]
        for j in range(7):
            corr[j]+=w*components[j][idx]
    low=target_low_harmonics(6)
    source=source_energy_ge3(weights,labels,a=6)
    U=exact_BA_overlap(weights,labels,target=simple_six_2factor_targets(6))
    mu=Fraction(source["mass"])*low["density"]
    Eproduct=source["E_ge3"]*low["E_ge3"]
    high=sum(corr[3:],Fraction(0))
    physical_edges=tuple(combinations(range(6),2))
    explicit2=sum((
        w*target_H2_value(six_image_index(R,labels,palette),
                          physical_edges,low)
        for R,w in weights.items()),Fraction(0))
    if (sum(corr,Fraction(0))!=U or corr[0]!=mu or
            corr[1]!=0 or corr[2]!=explicit2 or
            (corr[2]+high)!=U-mu or high*high>Eproduct):
        raise AssertionError("independent exact spectral overlap / CS mismatch")
    return {"actual_U":U,"random_mean":rat(mu),
            "signed_ranks":[rat(x) for x in corr],
            "low_order2":rat(corr[2]),
            "higher_order_3_to_6":rat(high),
            "source_E_ge3":rat(source["E_ge3"]),
            "target_E_ge3":rat(low["E_ge3"]),
            "CS_squared_bound":rat(Eproduct),
            "strict_CS_bound_valid":True}


def report():
    """Two full ORIGINAL GQ coherent maps; no corpus re-run."""
    base=gq_pair_model(1,"lex")
    hard=swapped_labeling(_anchors()[0][1],"left",13,14)
    models=(("lex",base),("hardest-M",hard))
    results=[]
    for name,m in models:
        point=exact_two_family_point(m)
        dual=dual_model(m)
        direct=spectral_overlap_certificate(
            source_weighted_BA_hypergraph(m),m["right_labels"])
        reverse=spectral_overlap_certificate(
            source_weighted_BA_hypergraph(dual),dual["right_labels"])
        if (direct["actual_U"],reverse["actual_U"])!=(
                point["U_BA"],point["U_AB"]):
            raise AssertionError("ORIGINAL dual independent C0/B0 mismatch")
        results.append({
            "name":name,"P2_margin":point["two_family_minus_mu"],
            "S_seven":point["S_seven"],"U_BA":point["U_BA"],
            "U_AB":point["U_AB"],"five_other":point["five_other_family"],
            "original_BA":direct,"original_dual_AB":reverse})
    _,_,energies=_frozen_target_W32()
    low={str(a):{k:(rat(v) if isinstance(v,Fraction) else v)
                 for k,v in target_low_harmonics(a).items()}
         for a in (6,9,14)}
    return {"slice":"HYP-105-E1-K3-G2-N",
            "target_all_a_low_harmonics":low,
            "K6_exact_target_ranks_0_to_6":[rat(x) for x in energies],
            "two_true_original_GQ_models":results,
            "all_h_target_H1_zero_proved":True,
            "all_h_target_H2_orbit_formula_proved":True,
            "all_h_two_family_P2_proved":False,
            "all_h_seven_family_P7_proved":False,
            "branch_A_B":"OPEN"}


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
