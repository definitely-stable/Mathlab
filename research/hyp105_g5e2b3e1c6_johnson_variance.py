"""HYP-105 B3.2-E1-C6: complete Johnson harmonic energy of ONE shared g.

This is a CLASSICAL S_V/Johnson scheme calculation, applied to the GQ
weighted original-right hypergraph and physical occupied target. It is
an exact independently checkable bridge between C5 seven-intersection
moments and all Johnson degrees 0..min(6,V-6); NOT a deterministic
all-correlated GQ crossing or new general spectral theorem.
"""
from fractions import Fraction
from math import comb
import json

from hyp105_g5e2b3e1c5_common_bijection import (
    sixset_intersection_spectrum,common_bijection_moments,
    physical_occupied_target,occupied_target_uniform_floor,
    fixed_map_overlap,
)
from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph


def johnson_sixset_energies(weights, V):
    """Exact squares of orthogonal W_r from 7 squared marginal moments.

    A_k=sum_{Q:|Q|=k} (sum_{R superset Q} weights[R])**2.
    For the k->6 inclusion matrix, its I_k^* I_k eigenvalue on W_r is
      B_{k,r}=C(6-r,k-r)*C(V-k-r,6-k), r<=k.
    So A_k=sum_{r<=k} B_{k,r} E_r, a triangular system.
    V>=12 permits all seven W0..W6 levels; V=7..11 has only
    0..min(6,V-6) irreducibles. All operations integer/Fraction.
    """
    d=sixset_intersection_spectrum(weights,V)
    A=d["binomial_squared_marginal_moments"]
    rank=min(6,V-6)
    energies=[]
    for k in range(rank+1):
        previous=sum(
            comb(6-r,k-r)*comb(V-k-r,6-k)*energies[r]
            for r in range(k)
        )
        eigen=comb(V-2*k,6-k)
        if eigen<=0:
            raise AssertionError("Johnson incidence eigenvalue zero")
        v=(Fraction(A[k])-previous)/eigen
        if v<0:
            raise AssertionError("negative Johnson squared projection energy")
        energies.append(v)
    if sum(energies)!=sum(int(v)**2 for v in weights.values()):
        raise AssertionError("all harmonic energies fail Parseval")
    dim=tuple(comb(V,r)-comb(V,r-1) if r>0 else 1
              for r in range(rank+1))
    if any(x<=0 for x in dim):
        raise AssertionError("invalid Johnson representation multiplicity")
    return {
        "V":V,"ranks":tuple(range(rank+1)),
        "squared_J_r_norms":tuple(energies),
        "irreducible_dimensions":dim,
        "squared_marginal_moments":A,
        "mean_hyperedge_weight":Fraction(d["mass"],comb(V,6)),
        "W0_squared_norm":energies[0],
        "W1_zero": len(energies)>1 and energies[1]==0,
        "full_Johnson_orthogonality_and_Parseval":True,
    }


def common_permutation_harmonic_variance(source,target,V):
    """Schur orthogonality + exact random transposition eigenvalues.

    Under ONE uniform Pi in S_V, all W_r permutation representations
    are inequivalent irreducibles (Johnson scheme multiplicity-free).
    Mean E U = M*T/C(V,6).
    Var U = sum_{r>=1} ||m_r||² ||t_r||² / dim(W_r).
    For uniformly sampled transposition tau independent of Pi,
      (1/2) E_(Pi,tau) [(U(Pi*tau)-U(Pi))²]
       = sum_{r>=1} alpha_r * Var_r,
      alpha_r = r*(V+1-r)/C(V,2).
    This is an EXACT mean-field transposition Dirichlet identity.
    """
    left=johnson_sixset_energies(source,V)
    right=johnson_sixset_energies({R:1 for R in target},V)
    n=comb(V,6)
    if len(right["squared_J_r_norms"])!=len(left["squared_J_r_norms"]):
        raise AssertionError("Johnson ranks differ")
    d=left["irreducible_dimensions"]
    contribution=tuple(
        left["squared_J_r_norms"][r]*right["squared_J_r_norms"][r]/d[r]
        for r in range(1,len(d)))
    variance=sum(contribution,Fraction(0))
    mu=Fraction(sum(source.values())*len(target),n)
    old=common_bijection_moments(source,target,V)
    if mu!=old["one_common_right_bijection_mean"]:
        raise AssertionError("C5 mean and C6 mean differ")
    if variance!=old["one_common_right_bijection_variance"]:
        raise AssertionError("C5 seven-overlap second moment != C6 harmonic spectrum")
    rates=tuple(Fraction(r*(V+1-r),comb(V,2))
                for r in range(1,len(d)))
    energy=sum((a*b for a,b in zip(rates,contribution)),Fraction(0))
    source_centered=sum(left["squared_J_r_norms"][1:],Fraction(0))
    target_centered=sum(right["squared_J_r_norms"][1:],Fraction(0))
    global_cauchy_square=source_centered*target_centered
    return {
        "V":V,"mean_one_common_pi":mu,
        "variance_one_common_pi":variance,
        "per_degree_variance_contribution":contribution,
        "johnson_swap_contraction_rates":rates,
        "random_swap_dirichlet_half_mean_square":energy,
        "global_centered_source_squared_norm":source_centered,
        "global_centered_target_squared_norm":target_centered,
        "deterministic_fixed_g_cauchy_error_squared_upper":
            global_cauchy_square,
        "global_cauchy_uniform_positive_gate":
            mu>0 and mu*mu>global_cauchy_square,
        "W1_target_zero":right["W1_zero"],
        "source_johnson_energies":left["squared_J_r_norms"],
        "target_johnson_energies":right["squared_J_r_norms"],
        "independent_global_moment_agreement":True,
        "one_common_right_permutation":True,
        "all_correlated_g_lower_proved":False,
    }


def W32_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    F=tuple((i,j) for i in range(6) for j in range(i+1,6))
    target=physical_occupied_target(6,F)
    index={e:i for i,e in enumerate(F)}
    reports={}
    for kind in ("lex","reverse-line"):
        model=pair_labeled_symplectic(1,kind)
        source=source_weighted_BA_hypergraph(model)
        c=common_permutation_harmonic_variance(source,target,15)
        perm=tuple(index[e] for e in model["right_labels"])
        actual=fixed_map_overlap(source,target,perm)
        reports[kind]={
            "actual_fixed_g_BA_overlap":actual,
            "global_mean":str(c["mean_one_common_pi"]),
            "global_variance":str(c["variance_one_common_pi"]),
            "degree2_to_degree6_variance":tuple(str(x) for x in
                 c["per_degree_variance_contribution"][1:]),
            "random_swap_dirichlet_half":str(c["random_swap_dirichlet_half_mean_square"]),
            "global_centered_fixed_g_cauchy_gate":
                 c["global_cauchy_uniform_positive_gate"],
            "no_all_right_omega_s6":True,
        }
    return {
        "finite_W32":reports,
        "all_h_occupied_random_mean":{
            str(s):str(occupied_target_uniform_floor(s)["one_common_right_bijection_mean_lower"])
            for s in (2,4,8,16,32,64,128)},
        "global_all_correlated_BA_obstruction_proved":False,
    }


if __name__=="__main__":
    print(json.dumps(W32_report(),indent=2,sort_keys=True,default=str))
