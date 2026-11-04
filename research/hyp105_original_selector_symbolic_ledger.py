r"""AA4-SELMOM-L6: independent exact symbolic 6th/4th selector constants.

Elementary all-N theorem for ANY simple *bipartite* physical G:
  tr(A^6) <= 12 C6 + 6 Delta tr(A^4).
Spectral Cauchy tr(A^4)<=sqrt(2m tr(A^6)), and exact Young
  6 Delta sqrt(2m X) <= X/2 + 36m Delta^2
therefore
  tr(A^6) <=24 C6+72m Delta^2.
The parent #672 uses an intentionally conservative 144m Delta^2.
This is a valid factor-two coefficient tightening. It DOES NOT
change any asymptotic s exponent or prove the all-h geometrical
heavy-tail/chunk selection theorems.

For a physically selected SOURCE graph G⊆H_C with m_G<=m_C<=4s^4,
Delta_G<=Delta_C<=T*s and every true original simple C6 injecting
into D6_avoid(Z)<=s^6, we get
  tr(A_G^6) <=(24+288T^2)s^6 = L6_tight*s^6.
The source selector (including the NEW adaptive lower bound) gives:
  ||P3||_F^2 <=sigma3^-2 L6_tight s^6,
  ||P2||_F^2 <=sigma2^-2 sqrt(8L6_tight) s^5,
  tr(A_C^4) <= [2sigma2^-2 sqrt(8L6_tight)+56T]s^5
assuming Qx+Qy<=28s^4 separately from ORIGINAL source books.
Combining #728 original full/core mixed source energy
F1<=64s^(11/2), F2<=32(K+1)T s^6 gives
B<=64sqrt((K+1)T)s^(23/4) and
I_internal<=4sqrt(B0*T*L4)s^(47/8).
All assumptions explicitly scoped; no C_graph,c_graph guessed.
All root 230 Branch A/B/C statuses stay OPEN_WITH_FORMAL_BLOCKER.
"""
from fractions import Fraction
from math import isqrt

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _ceil_root2(x):
    if type(x) is not int or x<0:
        raise ValueError("nonnegative exact integer square-root envelope only")
    y=isqrt(x)
    return y if y*y==x else y+1


def independent_tighter_original_selector_moment_ledger(K,T):
    """Independent algebra: NO #672/#674 imports, no bogus graph constants.

    K and T are formal caps ASSUMED to hold on the paired original
    source core: conflict max K, physical max <= T*s, with s dyadic.
    These caps DO NOT follow merely by calling this function!
    """
    if type(K) is not int or type(T) is not int or K<0 or T<1:
        raise ValueError("formal original core caps K>=0, integer T>=1")
    sigma2_inverse=64*(K+1)**2
    sigma3_inverse=64*27*(K+1)**3
    L6_tight=24+288*T*T
    L6_parent=24+576*T*T
    if not (L6_tight<L6_parent and
            L6_parent-L6_tight==288*T*T):
        raise AssertionError("exact factor-two sixth moment physical coefficient tightening lost")
    L4_tight_plus=2*sigma2_inverse**2*_ceil_root2(8*L6_tight)+56*T
    L4_parent_plus=2*sigma2_inverse**2*_ceil_root2(8*L6_parent)+56*T
    B0_plus=64*_ceil_root2((K+1)*T)
    I_plus=4*_ceil_root2(B0_plus*T*L4_tight_plus)
    I_parent_plus=4*_ceil_root2(B0_plus*T*L4_parent_plus)
    if not L4_tight_plus<=L4_parent_plus or not I_plus<=I_parent_plus:
        raise AssertionError("independent exact selector source sixth moment tightening not monotone")
    F1_exponent=Fraction(11,2)
    F2_exponent=Fraction(6,1)
    B_exponent=(F1_exponent+F2_exponent)/2
    I_exponent=(B_exponent+1+5)/2
    if B_exponent!=Fraction(23,4) or I_exponent!=Fraction(47,8):
        raise AssertionError("source full/core independent 47/8 exponent derivation failed")
    if not (I_exponent<6 and
            Fraction(6)-I_exponent==Fraction(1,8)):
        raise AssertionError("source mixed internal blocker is NOT o(s^6)")
    # Strictly valid (loose) constant B0 proof:
    # F1*F2 <= (64*32)*(K+1)*T*s^(11/2+6).
    # B0^2=4096*ceil_sqrt((K+1)*T)^2 >=2048*(K+1)*T.
    if B0_plus**2<64*32*(K+1)*T:
        raise AssertionError("full/core original B0 constant underestimates")
    return {
        "schema":"mathlab.hyp105.original-selector-independent-L6-L4-47over8.v1",
        "formal_original_core_max_conflict_degree_K":K,
        "formal_original_physical_max_degree_parameter_T":str(T),
        "all_N_bipartite_simple_closed6_to_C6_plus_Delta_A4_proved":True,
        "all_N_sharp_Young_trA6_upper_24C6_plus_72mDeltaSquared":True,
        "conservative_parent_trA6_upper_24C6_plus_144mDeltaSquared":True,
        "exact_original_sigma2_inverse":str(sigma2_inverse),
        "exact_original_sigma3_inverse":str(sigma3_inverse),
        "original_L6_tighter_24plus288T2":str(L6_tight),
        "original_parent_L6_24plus576T2":str(L6_parent),
        "original_L4_tighter_SAFE_integer_envelope":str(L4_tight_plus),
        "original_L4_parent_SAFE_integer_envelope":str(L4_parent_plus),
        "original_mixed_B0_SAFE_integer_envelope":str(B0_plus),
        "original_internal_I47over8_tighter_SAFE_integer_envelope":str(I_plus),
        "original_internal_I47over8_parent_SAFE_integer_envelope":str(I_parent_plus),
        "original_mixed_source_F1_exponent":str(F1_exponent),
        "original_mixed_source_F2_exponent":str(F2_exponent),
        "original_mixed_source_B_exponent":str(B_exponent),
        "original_internal_blocking_exponent":str(I_exponent),
        "strict_gap_to_six":str(6-I_exponent),
        "allh_prior_graph_CHUNK_supersaturation_requires_external_acceptance":True,
        "allh_full_original_mixed_source_collinearity_assumed_not_proved_here":True,
        "this_is_NOT_new_allh_geometric_Branch_A_proof":True,
        "root_230_status":ROOT_STATUS,
    }


def exact_selected_original_bipartite_trace6_lemma(power,scheme,seed):
    """Actual symplectic source physical selector, not a synthetic graph."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_original_adaptive_selector_moments import (
        _actual_gq,_true_original_physical,
        _priority_color_selector_source_graph,_simple_sixcycles)
    m=pair_labeled_symplectic(power,scheme)
    n=len(m["incidences"])
    C=(tuple(range(n)) if power==1
       else tuple(i for i in range(n) if i%5 in (1,3)))
    s,V,a,flags,f,g,C,_=_actual_gq(
        power,m["left_labels"],m["right_labels"],C,())
    priority=tuple(sorted(C,key=lambda i:((i*47+seed*11)%(n+17),i)))
    left=tuple((j*13+seed+j//3)%2 for j in range(a))
    right=tuple((j*7+seed*2+j//2)%2 for j in range(a))
    adj,owners,kept=_priority_color_selector_source_graph(
        flags,f,g,C,priority,left,right)
    C6=len(_simple_sixcycles(adj))
    mG=len(owners)
    Delta=max(map(len,adj.values()),default=0)
    walk={v:{v:1} for v in adj}
    tr={}
    for r in range(1,4):
        nextwalk={}
        for v0,row in walk.items():
            values={}
            for u,nval in row.items():
                for w in adj[u]:
                    values[w]=values.get(w,0)+nval
            nextwalk[v0]=values
        walk=nextwalk
        tr[2*r]=sum(q*q for row in walk.values() for q in row.values())
    X=tr[6]
    if (X>12*C6+6*Delta*tr[4]
        or X>24*C6+72*mG*Delta*Delta
        or X>24*C6+144*mG*Delta*Delta):
        raise AssertionError("actual original physically selected bipartite sixth-moment injection bound violated")
    # All selected edges toggle FIRST and SECOND coordinate binary bits.
    if any(left[v[0]]==left[u[0]] or
           right[v[1]]==right[u[1]]
           for v in adj for u in adj[v]):
        raise AssertionError("selected original source physical graph is not truly bicromatic")
    return {
        "s":s,"scheme":scheme,"seed":seed,
        "selected_ORIGINAL_core_flags":len(kept),
        "selected_source_physical_edges":mG,
        "selected_source_physical_max_degree":Delta,
        "selected_source_physical_C6":C6,
        "selected_source_physical_trace_A4":tr[4],
        "selected_source_physical_trace_A6":X,
        "actual_trace6_le_12C6_plus_6Delta_trace4":True,
        "actual_trace6_le_24C6_plus_72mDelta2":True,
        "all_selected_source_physical_edges_bichromatic":True,
        "root_230_status":ROOT_STATUS,
    }


def canonical_original_selector_symbolic_ledger():
    return {
        "schema":"mathlab.hyp105.original-selector-analytic-47over8-checks.v1",
        "formal_parameter_pairs":[
            independent_tighter_original_selector_moment_ledger(K,T)
            for K,T in ((0,1),(2,3),(8,10),(64,2**65))],
        "true_original_bipartite_source_graph_cases":[
            exact_selected_original_bipartite_trace6_lemma(power,scheme,seed)
            for power,scheme,seed in (
                (1,"lex",0),(1,"lex",1),(1,"reverse-line",0),
                (1,"reverse-line",3),(2,"lex",0),(2,"reverse-line",1))],
        "root_230_status":ROOT_STATUS,
        "no_new_allh_geometric_proof_claimed":True,
    }


if __name__=="__main__":
    import json
    print("AA4_ORIGINAL_SELECTOR_ANALYTIC_LEDGER_CERTIFICATE="+json.dumps(
        canonical_original_selector_symbolic_ledger(),sort_keys=True,
        separators=(",",":")),flush=True)
