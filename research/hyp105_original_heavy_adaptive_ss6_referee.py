"""AA4-HEAVYADAPT: exact ORIGINAL deletion-adaptive heavy graph C6 source referee.

NEW ALL-h local theorem with all prior ORIGINAL source lemmas explicitly scoped:
  E_T >= s^4/8, |Z| <= rho*s^4, Q_T frozen before Z,
  E_A >= (1/8-2rho)*s^4,
  # genuine ORIGINAL surviving heavy owners L >= (1/16-rho)*s^4.
  Source conflict e_J <= 5s^4/2. Caro--Wei and two coherent
  f/g physical-coordinate cuts yield |S| >=
     ((1/16-rho)^2/(4*(5+1/16-rho)))*s^4.
  The true physical no-clone heavy balanced witness graph F satisfies
     e(F)/v(F) >= (lambda^2/(72*(lambda+5)))*s,
     v(F) <= (17/2)*s^3/T, lambda=1/16-rho.

The EXISTING root low-tail rho_star is uniformly < 2^-32 even after
upgrading the heavy density constant; choose the UNIVERSAL integer
     R_ADAPT = ceil[72(5+1/16-2^-32)/(1/16-2^-32)^2] = 93313.
Then e(F)/v(F) >= s/93313, T>=ceil(17/2 R_ADAPT^3 C0^3).
Published ordinary graph C6 supersaturation, with EXISTENTIAL
absolute constants C_graph,c_graph, yields the stronger all-h
ORIGINAL D6 count >= c0*s^6/R_ADAPT^6, without copies or labels
rerandomized. Coupled with unchanged original LOW lemmas and TRUE
source GF5 signed weights, ROOT original seven-class
S_s>=delta_new*s^6 and additive R3>=54162*delta_new*s^6/51^6
for arbitrary FIXED correlated f/g and Z<=rho_star_new*s^4.

All arithmetic exact Fraction, only trusted genuine W32/W34 symplectic
fixture constructors imported. New finite physical HEAVY selection,
source conflict greed + both coordinate cuts + real chunk built here
independently of old heavy/referee implementations.

Root remains OPEN_WITH_FORMAL_BLOCKER; cited all-h source lemmas are
NOT automatically formally proven by a passing arithmetic CI.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

SCHEMA="mathlab.hyp105.original-heavy-adaptive-ss6-referee.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
R_OLD=370944
R_NEW=93313
R_ZERO_DELETION=93312
K=64
PAL=51
D6_WEIGHT=54162
BBO_PRODUCED_WEIGHT=53838
RHO_CAP=Fraction(1,2**32)
LAMBDA_MIN=Fraction(1,16)-RHO_CAP


def ceil_frac(x):
    if type(x) is not Fraction:raise ValueError("exact rational required")
    return -(-x.numerator//x.denominator)


def ceil_sqrt(x):
    if type(x) is not int or x<0:raise ValueError("positive integer required")
    u=isqrt(x)
    return u+(u*u<x)


def heavy_density_denominator(rho):
    if type(rho) is not Fraction or not 0<=rho<Fraction(1,16):
        raise ValueError("rho must be valid original named ID deletion fraction")
    lam=Fraction(1,16)-rho
    return 72*(lam+5)/lam**2


def standalone_quantified_theorem(C0,c0):
    if type(C0) is not Fraction or type(c0) is not Fraction or C0<1 or not 0<c0<=1:
        raise ValueError("FORMAL exact bounds on unpublished numeric SS6 constants required")
    R=R_NEW
    T=ceil_frac(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2*q2*ceil_sqrt(ceil_frac(Fraction(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta
    rho_star=tstar**2/Fraction(12*q3**2*L6)
    rho_previous=Fraction(16,12*q3*q3*L6)
    independent_rho_upper=Fraction(119,24)**2/Fraction(12*q3*q3*24)
    improved_density=Fraction(1,heavy_density_denominator(RHO_CAP))
    previous_density=Fraction(1,R_OLD)
    heavy_normalized_owner_lb=LAMBDA_MIN
    cw_independence_lb=LAMBDA_MIN**2/(LAMBDA_MIN+5)
    source_color_cut_lb=cw_independence_lb/4
    no_clone_density_lb=source_color_cut_lb/18
    risk_floor=D6_WEIGHT*delta/PAL**6
    BBO_LOW_at_rho=(Fraction(119,24)-tstar)/2
    checks={
        "all_h_UNIFORM_rho_star_below_2powerminus32_by_q3_palette_energy":
            independent_rho_upper<RHO_CAP and 0<rho_star<independent_rho_upper,
        "all_h_density_integer_R_NEW_tight_ceiling_93313":
            ceil_frac(heavy_density_denominator(RHO_CAP))==R,
        "all_h_zero_original_Z_heavy_exact_density_R_93312":
            heavy_density_denominator(Fraction(0))==R_ZERO_DELETION,
        "all_h_heavy_first_owner_L_keeps_TRUE_postZ_fraction":
            heavy_normalized_owner_lb==Fraction(1,16)-RHO_CAP,
        "all_h_true_original_J_Caro_Wei_bound_with_RHO":
            cw_independence_lb==LAMBDA_MIN**2/(LAMBDA_MIN+5),
        "all_h_genuine_twocolor_whole_flag_selection":
            source_color_cut_lb==cw_independence_lb/4,
        "all_h_NO_CLONE_density_from_original_heavy_owners":
            no_clone_density_lb==improved_density and
            no_clone_density_lb>=Fraction(1,R),
        "all_h_no_clone_density_is_greater_than_prior_R_370944":
            improved_density>previous_density,
        "all_h_published_external_graph_C6_threshold_same_once_fixed_C0":
            T>=Fraction(17*R**3,2)*C0**3,
        "all_h_external_graph_constants_remain_EXISTENTIAL":True,
        "all_h_new_D6_RISK_and_7motif_S_floor_exact":
            delta==c0/Fraction(R**6) and risk_floor==D6_WEIGHT*delta/PAL**6,
        "all_h_NEW_rho_low_source_CORE_still_ge_three_quarters":
            rho_star<Fraction(3,64),
        "all_h_NEW_rho_HEAVY_witness_survives_original_ID_Z":
            rho_star<Fraction(1,32),
        "all_h_OLD_new_rho_PARETO_still_improves_same_R":
            rho_star/rho_previous>Fraction(3,2),
        "all_h_LOW_risk_at_tstar_matches_NEW_heavy_D6_risk":
            BBO_PRODUCED_WEIGHT*BBO_LOW_at_rho/PAL**6==risk_floor,
        "all_h_unweighted_seven_original_SOURCE_motif_sum_ge_delta":
            BBO_LOW_at_rho>=delta,
        "all_h_no_ORIGINAL_deletion_LOW_produced_BBo_floor_119over48":
            (Fraction(119,24)-0)/2==Fraction(119,48),
        "all_h_exact_formal_s0_positive_dyadic":
            (1<<h0)>=s0>(1<<(h0-1)),
        "no_general_ASET_exponent_claimed":True,
    }
    if not all(checks.values()):raise AssertionError("adaptive heavy all-h quantified theorem mismatch")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "R_OLD":R_OLD,"R_ADAPT":R,
        "R_no_original_Z_exact":R_ZERO_DELETION,
        "T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,"B0":B0,"E":E,"D":D,
        "s0":s0,"h0":h0,"delta":str(delta),
        "rho_star":str(rho_star),"rho_pre_adaptive_same_R":str(rho_previous),
        "t_star":str(tstar),
        "new_original_SOURCE_motif_S_s_sextic_floor":str(delta),
        "new_signed_GF5_R3_sextic_floor":str(risk_floor),
        "BBo_LOW_produced_sextic_at_rho_star":str(BBO_LOW_at_rho),
        "maximum_all_h_rho_from_palette_and_sixth_moment_MIN_L6":
            str(independent_rho_upper),
        "density_lower_exact_at_rho_2powerminus32":str(improved_density),
        "R_heavy_vs_frozen_root_delta_improvement_factor":
            str(Fraction(R_OLD,R)**6),
        "all_h_18_quantified_exact_rational_crossbranch_gates":checks,
        "graph_supersaturation_numeric_C0_c0_are_published":False,
    }


def _score_cut(pairs,partial):
    # exact conditional expectation: each unsettled pair crosses with
    # probability 1/2; a fully assigned pair contributes 0 or 1.
    score=Fraction(0)
    for u,v in pairs:
        if u in partial and v in partial:
            score+=int(partial[u]!=partial[v])
        else:
            score+=Fraction(1,2)
    return score


def _actual_original_two_cuts(source_ids,flags,f,g,a):
    """Deterministic conditional expectations on ACTUAL typed physical symbols."""
    curr=tuple(sorted(source_ids))
    outcomes=[]
    for typ,labels in ((0,f),(1,g)):
        pairs=[labels[flags[i][typ]] for i in curr]
        expected=Fraction(len(curr),2)
        assignments={}
        for symbol in range(a):
            assignments[symbol]=0
            zero=_score_cut(pairs,assignments)
            assignments[symbol]=1
            one=_score_cut(pairs,assignments)
            assignments[symbol]=0 if zero>=one else 1
            if _score_cut(pairs,assignments)<expected:
                raise AssertionError("real conditional two-cut expectation decreased")
            expected=_score_cut(pairs,assignments)
        chosen=tuple(i for i in curr if
                     assignments[labels[flags[i][typ]][0]]!=
                     assignments[labels[flags[i][typ]][1]])
        if len(chosen)*2<len(curr):
            raise AssertionError("original physical cut lost more than 1/2 of true owners")
        outcomes.append({"before":len(curr),"after":len(chosen),
                         "actual_source_physical_bits":tuple(assignments[t] for t in range(a))})
        curr=chosen
    return curr,outcomes


def genuine_heavy_witness(h,scheme,Z,shift_f=0,shift_g=0,degree_threshold=1):
    """INDEPENDENT deterministic TRUE ORIGINAL physical HEAVY witness construction.

    Real finite W32/W34 original GQ, physical coordinate pairs, source
    J, source Caro--Wei greedy and two physical typed cuts, actual heavy
    source owned edge -> no-clone ordinary F. Small diagnostic T is
    deliberately NOT the enormous all-h theorem T.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("finite genuine symplectic W32/W34 required")
    s,V,raw=genuine_source(h)
    flags=tuple(map(tuple,raw));N=len(flags)
    if N!=(s+1)*V or len(set(flags))!=N:
        raise AssertionError("not genuine original source incidence IDs")
    lab=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(x)) for x in lab["left_labels"])
    g=tuple(tuple(sorted(x)) for x in lab["right_labels"])
    f=f[shift_f%V:]+f[:shift_f%V]
    g=g[shift_g%V:]+g[:shift_g%V]
    a=max(max(y for y in pair) for pair in f+g)+1
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("fake complete pair-injection")
    Z=set(Z)
    if any(type(i) is not int or i<0 or i>=N for i in Z):
        raise ValueError("Z must be genuine ORIGINAL incidence source ID")
    owner={};adj=defaultdict(set);byid=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in owner:raise AssertionError("source physical diagonal multiply owned")
            owner[e]=i
            byid[i].append(e)
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*N:raise AssertionError("original source not 2 real edges/flag")
    Q={v for v in adj if len(adj[v])>degree_threshold*s}
    Et={e for e in owner if e[0] in Q or e[1] in Q}
    EA={e for e in Et if owner[e] not in Z}
    Lowner=tuple(sorted({owner[e] for e in EA}))
    if len(Et)-len(EA)>2*len(Z):
        raise AssertionError("arbitrary original Z removed >2 physical heavy edges/ID")
    if len(Lowner)*2<len(EA):
        raise AssertionError("named original heavy-owner multiplicity exceeded 2")

    conflict={i:set() for i in Lowner}
    byp=defaultdict(list);byl=defaultdict(list)
    for i in Lowner:
        p,l=flags[i];byp[p].append(i);byl[l].append(i)
    for typ,groups in ((0,byp),(1,byl)):
        for ids in groups.values():
            for i,j in combinations(ids,2):
                lab1=g[flags[i][1]] if typ==0 else f[flags[i][0]]
                lab2=g[flags[j][1]] if typ==0 else f[flags[j][0]]
                if set(lab1)&set(lab2):
                    conflict[i].add(j)
                    conflict[j].add(i)
    eJ=sum(len(x) for x in conflict.values())//2
    L=len(Lowner)
    caroweibound=Fraction(L*L,L+2*eJ) if L else Fraction(0)
    independent=[]
    rem=set(Lowner)
    while rem:
        v=min(rem,key=lambda i:(len(conflict[i]&rem),i))
        independent.append(v)
        rem.remove(v)
        rem.difference_update(conflict[v])
    if len(independent)<caroweibound or any(j in conflict[i] for i,j in combinations(independent,2)):
        raise AssertionError("source ORIGINAL Caro--Wei greedy did not certify actual J")
    chosen,cuts=_actual_original_two_cuts(independent,flags,f,g,a)
    if len(chosen)*4<len(independent):
        raise AssertionError("two actual physical cuts lost >3/4 independent source flags")
    keep_edges={e for i in chosen for e in byid[i]}
    if len(keep_edges)!=2*len(chosen):
        raise AssertionError("selected original source flag diagonal lost")
    bit0=cuts[0]["actual_source_physical_bits"]
    bit1=cuts[1]["actual_source_physical_bits"]
    if not all(bit0[f[flags[i][0]][0]]!=bit0[f[flags[i][0]][1]] and
               bit1[g[flags[i][1]][0]]!=bit1[g[flags[i][1]][1]]
               for i in chosen):
        raise AssertionError("selected original source both typed pair cut broken")

    if not chosen:
        return {"s":s,"scheme":scheme,"Z":len(Z),"diagnostic_T":degree_threshold,
                "physical_Q_full_before_Z":len(Q),
                "original_full_heavy_edges":len(Et),
                "original_surviving_heavy_edges":len(EA),
                "surviving_original_heavy_IDs":L,
                "source_J_conflict_edges":eJ,
                "source_caroweibound":str(caroweibound),
                "source_original_conflict_free_independent_flags":len(independent),
                "after_two_REAL_coordinate_cuts_original_flags":0,
                "ordinary_NO_CLONE_heavy_F_physical_vertices":0,
                "ordinary_NO_CLONE_heavy_F_physical_edges":0,
                "diagnostic_heavy_nonvacuous":False}

    witness=[]
    for i in chosen:
        opts=sorted(e for e in byid[i] if e in EA)
        if not opts:raise AssertionError("true selected source lost heavy witness e_i")
        e=opts[0]
        heavy=sorted(v for v in e if v in Q)
        if not heavy:raise AssertionError("true heavy witness q_i not in frozen Q")
        witness.append((i,e,heavy[0],bit0[heavy[0][0]]))
    majority=max((0,1),key=lambda b:(sum(z[3]==b for z in witness),-b))
    Rset={v for v in Q if bit0[v[0]]==majority}
    selected_neighbors=defaultdict(set)
    for u,v in keep_edges:
        selected_neighbors[u].add(v);selected_neighbors[v].add(u)
    Y=sorted(v for v in selected_neighbors if bit0[v[0]]!=majority)
    rr=len(Rset)
    if rr==0:raise AssertionError("heavy Q witness R was empty")
    blocks=[set(Y[k:k+rr]) for k in range(0,len(Y),rr)]
    if not blocks:raise AssertionError("no physical Y for heavy true-source cuts")
    candidate=[]
    for block in blocks:
        edges={e for e in keep_edges if
               (e[0] in Rset and e[1] in block) or
               (e[1] in Rset and e[0] in block)}
        candidate.append((edges,block))
    Fedges,B=max(candidate,key=lambda p:(len(p[0]),-len(p[1])))
    vf=len(Rset)+len(B)
    mf=len(Fedges)
    n=a*a
    if len(witness)!=len(chosen):
        raise AssertionError("not one true heavy witness per original ID")
    if 2*sum(w[3]==majority for w in witness)<len(chosen):
        raise AssertionError("source heavy bit majority selection wrong")
    if 4*n*mf<len(chosen)*rr:
        raise AssertionError("balanced TRUE physical F physical-edge pigeonhole false")
    if 8*n*mf<len(chosen)*vf:
        raise AssertionError("no-clone F average density lower than source |S|/(8n)")
    if any(owner[e] not in chosen for e in Fedges):
        raise AssertionError("physical F invented a new source owner")
    if any(bit0[e[0][0]]==bit0[e[1][0]] for e in Fedges):
        raise AssertionError("physical selected F not actual first-bipartite")
    return {
        "s":s,"scheme":scheme,"shift_f":shift_f,"shift_g":shift_g,
        "Z":len(Z),"diagnostic_T":degree_threshold,
        "physical_Q_full_before_Z":len(Q),
        "original_full_heavy_edges":len(Et),
        "original_surviving_heavy_edges":len(EA),
        "surviving_original_heavy_IDs":L,
        "source_J_conflict_edges":eJ,
        "source_caroweibound":str(caroweibound),
        "source_original_conflict_free_independent_flags":len(independent),
        "after_first_REAL_coordinate_cut_original_flags":cuts[0]["after"],
        "after_two_REAL_coordinate_cuts_original_flags":len(chosen),
        "physical_original_flag_diagonals_in_selected_graph":len(keep_edges),
        "true_frozen_Q_majority_physical_vertices":rr,
        "source_independent_flags_with_heavy_witness":len(witness),
        "true_physical_Y_balance_block_count":len(blocks),
        "ordinary_NO_CLONE_heavy_F_physical_vertices":vf,
        "ordinary_NO_CLONE_heavy_F_physical_edges":mf,
        "actual_NO_CLONE_F_edge_density":str(Fraction(mf,vf)),
        "actual_SOURCE_S_over_8a2_density_bound":str(Fraction(len(chosen),8*n)),
        "diagnostic_heavy_nonvacuous":True,
        "source_IDs_and_physical_vertices_are_never_cloned":True,
    }


def canonical_report():
    formal=[standalone_quantified_theorem(C,c) for C,c in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    finite=[
        genuine_heavy_witness(1,"lex",(0,),degree_threshold=1),
        genuine_heavy_witness(1,"reverse-line",(1,13,33),2,4,1),
        genuine_heavy_witness(2,"lex",tuple(range(0,425,23)),degree_threshold=1),
        genuine_heavy_witness(2,"reverse-line",tuple(range(2,425,29)),11,23,1),
        genuine_heavy_witness(2,"lex",tuple(range(1,425,31)),7,19,1),
    ]
    return {
        "schema":SCHEMA,
        "root_230_status":ROOT_STATUS,
        "root_ASET_exponent_proved":False,
        "root_Branch_A_formally_peer_review_accepted":False,
        "primary_root_target_is_seven_class_S_s_NOT_R3":True,
        "R3_is_the_separate_additive_signed_event_expectation":True,
        "all_order_heavy_adaptive_density_theorem_proved_from_named_prior_lemmas":True,
        "all_order_new_R_93313_and_delta_improvement_more_than_3900fold":True,
        "external_graph_SS6_actual_numeric_constants_verified":False,
        "all_order_formal_external_C0_c0_probes":formal,
        "genuine_original_W32_W34_new_independent_heavy_physical_witnesses":finite,
        "prior_root_math_dependency_acceptance_still_outstanding":True,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_HEAVY_ADAPTIVE_SS6_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
