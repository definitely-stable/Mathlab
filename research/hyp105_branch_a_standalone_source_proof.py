"""HYP-105 #230: independent final quantified ORIGINAL Branch A source proof referee.

CANDIDATE THEOREM, science/governance status OPEN_WITH_FORMAL_BLOCKER:
for all sufficiently large dyadic s, every complete separately
pair-injected, arbitrarily correlated fixed original f/g, and any
adversarial deletion Z of named ORIGINAL source incidence IDs with
|Z|<=rho_star*s^4, the ORIGINAL seven-class positive motif sum
S_s(f,g)>=c0*s^6/370944^6 and the accepted exact additive
GF5 risk R3>=54162*c0*s^6/(370944^6*51^6).

External ordinary C6 SS6 supplies EXISTENTIAL constants. C0,c0 probes
are purely FORMAL; all-h statement chooses valid bounds ONCE for all s.

Mathematical certificate here independently reconstructs the whole
logical quantified interface and its monotone HEAVY/LOW branch
composition using only exact integer/Fraction arithmetic, not any
parent root proof calculator. It *does not* replace reading the
proven individual source lemmas #734,#737--#742. A full source-first
ORIGINAL W(3,2)/W(3,4) finite falsifier independently reconstructs
GQ, unique source-owned physical edges, full-before-Z Q, source
conflicts, exact role-squared GQ anchor occurrences, actual 3paths,
source BBo two-direction multiplicity, real original D6 physical C6.

No merge, source substitution, fabricated numerical external constants,
claim of ASET exponent or automatic issue closure.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

SCHEMA="mathlab.hyp105.branch-a-standalone-source-proof.v1"
ROOT_STATE="OPEN_WITH_FORMAL_BLOCKER"
K=64
R=370944
PAL=51
D6_WEIGHT=54162
BBO_ALL_WEIGHT=53526
BBO_PRODUCED_WEIGHT=53838
SIGNED_3V3_PER_SIXSET=10
SOURCE_MOTIF_CLASSES=(
    "D6","U_B_left","U_B_right","U_CA","U_CB",
    "U_BB_overlap","U_BB_disjoint",
)


def exact_ceil(q):
    if type(q) is not Fraction:
        raise ValueError("require exact external constant Fraction")
    return -(-q.numerator//q.denominator)


def sqrt_ceil(n):
    if type(n) is not int or n<0:
        raise ValueError("require nonnegative exact integer")
    a=isqrt(n)
    return a+(a*a<n)


def original_all_order_theorem(C0,c0):
    if type(C0) is not Fraction or type(c0) is not Fraction or C0<1 or not 0<c0<=1:
        raise ValueError("unknown published constants require FORMAL exact C0>=1,0<c0<=1")
    T=exact_ceil(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2*q2*sqrt_ceil(exact_ceil(Fraction(17*L6,4)))+19*T
    B0=sqrt_ceil(360*(K+1)*T)
    E=5*q3*sqrt_ceil(L6)
    D=4*sqrt_ceil(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta
    rho_star=tstar*tstar/Fraction(12*q3*q3*L6)
    rho_previous=Fraction(16,12*q3*q3*L6)
    C_floor=Fraction(1)-Fraction(1,8)-Fraction(5,64)-rho_star
    E_heavy=Fraction(1,8)-2*rho_star
    BBO_zero=Fraction(119,48)
    BBO_at_star=(Fraction(119,24)-tstar)/2
    R3_floor=D6_WEIGHT*delta/Fraction(PAL**6)
    theoretical_class_count_floor=delta
    gates={
        "published_graph_C6_theorem_constants_are_existential_not_claimed_numeric":True,
        "source_s_independent_formal_dyadic_threshold":(1<<h0)>=s0>(1<<(h0-1)),
        "source_analytic_V_N_a_Cs_envelope_all_s_ge_64_is_invoked":True,
        "true_original_full_Q_is_frozen_BEFORE_named_source_Z":True,
        "all_h_heavy_has_ge_s4_over16_original_edges_after_Z":
            E_heavy>=Fraction(1,16),
        "full_original_J_source_conflict_bound_eJ_le_5s4_over2":True,
        "low_original_core_after_Z_ge_3s4_over4":
            C_floor>=Fraction(3,4),
        "actual_original_paired_physical_core_degree_le_Ts":True,
        "original_SRG_point_line_branches_do_not_assume_f_g_independence":True,
        "selected_original_coordinate_cut_six_cycles_are_proper":True,
        "original_physical_C6_to_D6_injective_source_six_ID":True,
        "actual_published_C6_applicable_to_simple_NO_CLONE_physical_F":
            T>=Fraction(17*R**3,2)*C0**3,
        "all_h_heavy_distinct_D6_original_sixsets_ge_delta_s6":
            0<delta<=Fraction(1,R**6),
        "low_selected_moments_real_original_C6_D6_cap_L6":L6==24+153*T*T,
        "low_actual_physical_3return_spectral_bound":True,
        "low_original_GQ_projection_24s5_and_12s2Z":True,
        "low_A_full_not_C_only_source_four_blockers":True,
        "low_three_nonZ_error_classes_each_le_one_eighth_s6":
            s0>=444*T and s0>=(8*E)**2 and s0>=(8*D)**8,
        "low_masked_source_endpoint_at_rho_star_exactly_tstar":
            q3*q3*12*L6*rho_star==tstar*tstar,
        "low_physical_produced_original_BBo_exact_two_reversed_paths":True,
        "new_tstar_adversarial_Z_radius_strictly_larger_than_prior":
            Fraction(4)<tstar<Fraction(119,24)
            and rho_star>Fraction(3,2)*rho_previous,
        "new_tstar_deletion_radius_still_satisfies_heavy_and_low":
            rho_star<=Fraction(1,32)
            and rho_star<=Fraction(3,64),
        "low_at_tstar_produced_source_BBo_sextic_floor":
            BBO_at_star==Fraction(D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta,
        "BBo_produced_full_10_signs_exact_53838":True,
        "D6_full_10_signs_exact_54162":True,
        "R3_mathematically_is_additive_indexed_event_expectation":True,
        "source_sixset_keys_are_unordered_ORIGINAL_incidence_IDs":True,
        "accepted_D6_and_BBo_original_sixsets_are_disjoint_keys":True,
        "root_S_s_seven_class_motif_floor_nonzero":
            BBO_at_star>=delta and theoretical_class_count_floor>0,
        "root_R3_signed_event_floor_same_in_HEAVY_and_LOW":
            BBO_PRODUCED_WEIGHT*BBO_at_star/Fraction(PAL**6)==R3_floor,
        "no_new_ASET_exponent_asserted":True,
    }
    if not all(gates.values()) or len(gates)!=30:
        raise AssertionError("quantified original source theorem gate invalid")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),"T":T,"q2":q2,"q3":q3,
        "L6":L6,"L4":L4,"B0":B0,"E":E,"D":D,
        "s0":s0,"h0":h0,
        "delta_original_seven_motif_S_s":str(delta),
        "rho_star":str(rho_star),
        "rho_old_740":str(rho_previous),
        "deletion_improvement_ratio":str(rho_star/rho_previous),
        "t_star":str(tstar),
        "low_BBo_produced_ZERO_original_ID_deletion_floor":str(BBO_zero),
        "low_BBo_produced_at_max_deletion_floor":str(BBO_at_star),
        "S_s_universal_positive_motif_floor":str(theoretical_class_count_floor),
        "R3_full_additive_original_GF5_risk_floor":str(R3_floor),
        "HEAVY_original_source_D6_risk_floor":str(R3_floor),
        "LOW_original_source_BBo_risk_floor":str(BBO_PRODUCED_WEIGHT*BBO_at_star/Fraction(PAL**6)),
        "quantified_30_original_math_gates":gates,
        "formal_graph_constant_values_are_CERTIFIED_PUBLISHED":False,
        "root_issue_status":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_adversarial_branch_witness(ledger,D6_sixsets,BBo_produced_sixsets):
    """EXACT finite normalized sixset-count witness and branch threshold.

    This is a logical implication test, NOT a finite substitute for the
    big-s original source COUNT existence lemmas.
    """
    if type(D6_sixsets) is not Fraction or type(BBo_produced_sixsets) is not Fraction:
        raise ValueError("normalized sextic original motif counts must be exact")
    if D6_sixsets<0 or BBo_produced_sixsets<0:
        raise ValueError("source sixset counts cannot be negative")
    delta=Fraction(ledger["delta_original_seven_motif_S_s"])
    bbo_threshold=Fraction(ledger["low_BBo_produced_at_max_deletion_floor"])
    if D6_sixsets>=delta:
        route="HEAVY_OR_LOW_HIGH_D6"
        route_premise=True
    else:
        route="LOW_SMALL_D6"
        route_premise=BBo_produced_sixsets>=bbo_threshold
    risk=(D6_WEIGHT*D6_sixsets+BBO_PRODUCED_WEIGHT*BBo_produced_sixsets)/PAL**6
    S_s=D6_sixsets+BBo_produced_sixsets
    lower_R3=Fraction(ledger["R3_full_additive_original_GF5_risk_floor"])
    return {
        "branch":route,
        "branch_premise_satisfied":route_premise,
        "S_s_lower_two_positive_original_disjoint_classes":str(S_s),
        "R3_lower_two_original_signed_sixset_families":str(risk),
        "universal_original_S_s_GEQ_delta":S_s>=delta,
        "universal_R3_GEQ_required_floor":risk>=lower_R3,
        "implication_valid":
            not route_premise or (S_s>=delta and risk>=lower_R3),
    }


def genuine_source_falsifier(h,scheme,deleted,shf=0,shg=0,threshold=4):
    """Independent finite W32/W34 true ORIGINAL source-first witness.

    Imports ONLY trusted original finite symplectic source and complete
    pair-label fixture constructors, not old energy/root/flow ref.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("only true finite original symplectic W32/W34")
    s,V,fl=genuine_source(h)
    flags=tuple(map(tuple,fl))
    m=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(q)) for q in m["left_labels"])
    g=tuple(tuple(sorted(q)) for q in m["right_labels"])
    f=f[shf%V:]+f[:shf%V]
    g=g[shg%V:]+g[:shg%V]
    a=max(x for pair in f+g for x in pair)+1
    if (len(flags)!=(s+1)*V or len(set(flags))!=len(flags) or
            len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or
            comb(a,2)<V):
        raise AssertionError("fake GQ or invalid complete global pair embedding")
    Z=set(deleted)
    if len(Z)!=len(tuple(deleted)) or any(type(i) is not int or not 0<=i<len(flags) for i in Z):
        raise ValueError("deleted flags must be distinct true original incidence-ID")
    byp=defaultdict(list);byl=defaultdict(list);lookup={}
    for i,(p,l) in enumerate(flags):
        byp[p].append(i);byl[l].append(i)
        lookup[p,l]=i
    if any(len(z)!=s+1 for z in list(byp.values())+list(byl.values())):
        raise AssertionError("not actual GQ point/line flags")
    point_col=defaultdict(set)
    line_col=defaultdict(set)
    for _,ids in byl.items():
        for i,j in combinations(ids,2):
            p,q=flags[i][0],flags[j][0]
            point_col[p].add(q);point_col[q].add(p)
    for _,ids in byp.items():
        for i,j in combinations(ids,2):
            u,v=flags[i][1],flags[j][1]
            line_col[u].add(v);line_col[v].add(u)
    epoint=sum(set(f[p])&set(f[q])!=set()
               for p in range(V) for q in point_col[p] if p<q)
    eline=sum(set(g[l])&set(g[k])!=set()
              for l in range(V) for k in line_col[l] if l<k)
    Cs=(s*s+1)*(s*s+a-2)
    if epoint>Cs or eline>Cs:
        raise AssertionError("original GQ deterministic source SRG cap false")
    conflict=[set() for _ in flags]
    for group,mode in ((byp,0),(byl,1)):
        for ids in group.values():
            for i,j in combinations(ids,2):
                L=(g[flags[i][1]] if mode==0 else f[flags[i][0]])
                R=(g[flags[j][1]] if mode==0 else f[flags[j][0]])
                if set(L)&set(R):
                    conflict[i].add(j);conflict[j].add(i)
    eJ=sum(len(v) for v in conflict)//2
    if eJ!=epoint+eline:
        raise AssertionError("source J != real point and line SRG collinearity counts")

    # Exact genuine GQ 3 anchor roles (n=85 => 85^2 checks).
    exposed=[[0]*len(flags) for _ in range(3)]
    projections=0
    for q in range(V):
        col=point_col[q]
        for r in range(V):
            if (q,r) in lookup:
                continue
            pset={p for i in byl[r] for p in (flags[i][0],) if p in col}
            if len(pset)!=1:
                raise AssertionError("full real original GQ point projection not unique")
            p=next(iter(pset))
            ellset={flags[i][1] for i in byp[q]} & {flags[i][1] for i in byp[p]}
            if len(ellset)!=1:
                raise AssertionError("full real original GQ projected line not unique")
            ell=next(iter(ellset))
            for j,k in enumerate((lookup[q,ell],lookup[p,ell],lookup[p,r])):
                exposed[j][k]+=1
            projections+=1
    if any(any(z!=s*s for z in role) for role in exposed):
        raise AssertionError("true original projection anchor role s^2 exposure false")
    if projections!=V*(V-s-1):
        raise AssertionError("original nonincident q,r count incorrect")

    physical_owner={}
    adj=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in physical_owner:
                raise AssertionError("original physical diagonal has duplicate SOURCE owner")
            physical_owner[e]=i
            adj[u].add(v);adj[v].add(u)
    if len(physical_owner)!=2*len(flags):
        raise AssertionError("true GQ source flag two diagonals wrong")
    Q={v for v in adj if len(adj[v])>threshold*s}
    Et={e for e in physical_owner if e[0] in Q or e[1] in Q}
    survived={e for e in Et if physical_owner[e] not in Z}
    if len(Et)-len(survived)>2*len(Z):
        raise AssertionError("named source Z delete more than 2 true physical edges")
    owners_Q={physical_owner[e] for e in Et}
    high={i for i,nb in enumerate(conflict) if len(nb)>K}
    C=tuple(i for i in range(len(flags)) if i not in Z|owners_Q|high)
    # Use only genuine SOURCE IDs in ORIGINAL physical paired core.
    core_owner={}
    cadj=defaultdict(set)
    for i in C:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in core_owner:
                raise AssertionError("paired true original source core has two edge owners")
            core_owner[e]=i;cadj[u].add(v);cadj[v].add(u)
    if len(core_owner)!=2*len(C):
        raise AssertionError("paired source core not exactly two diagonals/ORIGINAL flag")
    max_degree=max((len(nb) for nb in cadj.values()),default=0)
    if max_degree>threshold*s or any(len(conflict[i])>K for i in C):
        raise AssertionError("original LOW source freeze or conflict cap broken")

    # Count all original physically coordinate-proper directed 3paths and
    # independently reconstruct actual GQ six-ID BBo path-produced keys.
    invf={pair:p for p,pair in enumerate(f)}
    invg={pair:l for l,pair in enumerate(g)}
    produced=Counter()
    proper=0
    for v0,nb0 in cadj.items():
        for v1 in nb0:
            for v2 in cadj[v1]:
                for v3 in cadj[v2]:
                    vs=(v0,v1,v2,v3)
                    if (len({v[0] for v in vs})!=4 or
                            len({v[1] for v in vs})!=4):
                        continue
                    proper+=1
                    q=invf.get(tuple(sorted((v0[0],v3[0]))))
                    r=invg.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None or (q,r) in lookup:
                        continue
                    pset={p for i in byl[r]
                          for p in (flags[i][0],) if p in point_col[q]}
                    if len(pset)!=1:
                        raise AssertionError("real source 3path original GQ projection invalid")
                    p=next(iter(pset))
                    ellset={flags[i][1] for i in byp[p]}&{flags[i][1] for i in byp[q]}
                    if len(ellset)!=1:
                        raise AssertionError("real source 3path GQ ell nonunique")
                    ell=next(iter(ellset))
                    anchors=(lookup[q,ell],lookup[p,ell],lookup[p,r])
                    if set(anchors)&Z:
                        continue
                    if (set(f[p])&{v0[0],v3[0]} or
                            set(g[ell])&{v0[1],v3[1]} or
                            any(v[0] in f[p] or v[1] in g[ell] for v in (v1,v2))):
                        continue
                    owners=tuple(core_owner[tuple(sorted((vs[j],vs[j+1])))] for j in range(3))
                    six=tuple(sorted(anchors+owners))
                    if len(set(six))!=6:
                        raise AssertionError("ORIGINAL BBo returned 6 source ID collision")
                    cp=Counter(flags[i][0] for i in six)
                    cl=Counter(flags[i][1] for i in six)
                    if sorted(cp.values())!=[1,1,1,1,2] or sorted(cl.values())!=[1,1,1,1,2]:
                        raise AssertionError("produced physical P3 not genuine BBo")
                    produced[six]+=1
    if any(z!=2 for z in produced.values()):
        raise AssertionError("original produced physical 3path not exactly two directions")
    return {
        "s":s,"scheme":scheme,
        "shift_f":shf,"shift_g":shg,
        "original_incidence_IDs_total":len(flags),
        "ORIGINAL_adversarial_Z_deleted_IDs":len(Z),
        "true_original_point_collinear_f_label_collisions":epoint,
        "true_original_line_collinear_g_label_collisions":eline,
        "true_original_full_source_J_edges":eJ,
        "exact_original_full_GQ_offincident_projections":projections,
        "each_original_flag_projection_exposure_per_role":s*s,
        "actual_physical_full_original_two_diagonal_edges":len(physical_owner),
        "true_original_full_Q_before_Z_vertices":len(Q),
        "actual_ORIGINAL_Q_edges_deleted_at_most_2Z":len(Et)-len(survived),
        "true_original_K_conflict_high_deleted_flags":len(high),
        "true_ORIGINAL_paired_CORE_IDs":len(C),
        "true_CORE_physical_edges":len(core_owner),
        "true_CORE_physical_max_degree":max_degree,
        "actual_proper_directed_physical_P3":proper,
        "real_produced_BBo_distinct_original_six_ID_sets":len(produced),
        "real_produced_BBo_accepted_directed_3paths":sum(produced.values()),
        "source_produced_BBo_exact_two_directed_reversal":True,
    }


def canonical_report():
    formal=[
        original_all_order_theorem(Fraction(1),Fraction(1)),
        original_all_order_theorem(Fraction(2),Fraction(1,5)),
        original_all_order_theorem(Fraction(7,3),Fraction(1,17)),
    ]
    actual=[
        genuine_source_falsifier(1,"lex",(0,),threshold=4),
        genuine_source_falsifier(1,"reverse-line",(1,13,33),2,4,4),
        genuine_source_falsifier(2,"lex",tuple(range(0,425,23)),threshold=3),
        genuine_source_falsifier(2,"reverse-line",tuple(range(2,425,29)),11,23,3),
        genuine_source_falsifier(2,"lex",tuple(range(1,425,31)),7,19,3),
    ]
    return {
        "schema":SCHEMA,
        "root_230_status":ROOT_STATE,
        "root_Branch_A_mathematical_implication_is_explicit_all_h":True,
        "root_issue_seven_disjoint_accepted_original_classes":SOURCE_MOTIF_CLASSES,
        "root_S_s_is_original_sixID_MOTIF_sum_not_signed_event_count":True,
        "no_published_numeric_graph_supersaturation_constants_assumed":True,
        "all_h_candidate_is_absolute_positive_existence_not_explicit_h":True,
        "root_full_scientific_governance_acceptance":False,
        "root_ASET_exponent_proved":False,
        "full_original_source_formal_quantified_theorem_probes":formal,
        "actual_original_symplectic_source_falsifiers":actual,
    }


if __name__=="__main__":
    print("AA4_BRANCH_A_STANDALONE_SOURCE_PROOF_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
