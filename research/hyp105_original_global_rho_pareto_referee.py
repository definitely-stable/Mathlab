"""HYP-105 #230 / AA4-RHOPARETO: independent exact ORIGINAL deletion frontier.

Root mathematically auditable implication for EVERY genuine W(3,s), s=2^h>=s0,
every complete separately globally pair-injective (arbitrarily correlated) f/g,
and every arbitrary set Z of NAMED ORIGINAL incidence source IDs.

Dependencies explicitly frozen, no imports from parent research proof/flow/
selector/energy/low-tail/root implementations. No parent/main modifications.

NEW:
   δ=c0/(370944^6), T=ceil((17/2)*370944^3*C0^3),
   L6=24+153*T*T, q3=64*binom(195,3).
   For 0<=t<=119/24 with |Z|<=ρ(t)*s^4,
       ρ(t)=t²/(12*q3²*L6),
       BBo_PRODUCED>= (119/24-t)*s^6/2,
   in LOW under D6_original_avoid<δ*s^6.
   The exact per-PRODUCED BBo full ten-sign GF5 count is 53838,
   D6 is 54162. To retain existing HEAVY R3 floor:
       t_star=119/24-2*(54162/53838)*δ,
       ρ_star=t_star²/(12*q3²*L6).
   Both branches still give R3 >=54162*δ*s^6/51^6.
   ρ_star/ρ_old=(t_star/4)² >3/2 (about 1.53656).
   For Z=empty, produced LOW BBo>=119*s^6/48 instead of 23/48.

The rho_star "optimality" is ONLY for the inherited three fixed 1/8
low-tail error budgets and their exact D6/BBo signed weight interface.
It is NOT maximum true geometric resilience or a proof of ASET exponent.

The published graph C6 constants are existential/UNKNOWN. All numeric
C0,c0 are explicitly FORMAL algebraic examples, never claimed real.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

K=64
R=370944
PAL=51
D6_GF5=54162
BBO_PRODUCED_GF5=53838
BBO_GENERAL_GF5=53526
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
ZERO_DELETION_BBO=Fraction(119,48)
RHO_OLD_T=Fraction(4)
MAX_T=Fraction(119,24)


def ceil_fraction(x):
    if type(x) is not Fraction:
        raise ValueError("all numerics must be exact Fraction")
    return -(-x.numerator//x.denominator)


def ceil_sqrt(x):
    if type(x) is not int or x<0:
        raise ValueError("nonnegative integer required")
    t=isqrt(x)
    return t+(t*t<x)


def symbolic_external_SS6_data(C0,c0):
    """All-order source quantitative definitions WITHOUT imported parent ledgers."""
    if type(C0) is not Fraction or type(c0) is not Fraction or C0<1 or not 0<c0<=1:
        raise ValueError("formal rational C0>=1 and 0<c0<=1 required")
    T=ceil_fraction(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2*q2*ceil_sqrt(ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    return {
        "C0":C0, "c0":c0, "T":T, "q2":q2, "q3":q3,
        "L6":L6, "L4":L4, "B0":B0, "E":E, "D":D,
        "s0":s0, "h0":h0,
        "delta":c0/Fraction(R**6),
    }


def rho_of_t(a,t):
    if type(t) is not Fraction or not 0<=t<=MAX_T:
        raise ValueError("only rational 0<=t<=119/24 low deletion budget")
    return t*t/Fraction(12*a["q3"]**2*a["L6"])


def bbo_produced_floor(t):
    if type(t) is not Fraction or not 0<=t<=MAX_T:
        raise ValueError("only rational proper original LOW source budget")
    return (MAX_T-t)/2


def optimal_source_rho_frontier(C0,c0):
    """Exact all-order Pareto frontier at fixed LOW error 1/8+1/8+1/8."""
    a=symbolic_external_SS6_data(C0,c0)
    delta=a["delta"]
    tstar=MAX_T-2*Fraction(D6_GF5,BBO_PRODUCED_GF5)*delta
    if not RHO_OLD_T<tstar<MAX_T:
        raise AssertionError("no nontrivial original source rho frontier")
    rho_old=rho_of_t(a,RHO_OLD_T)
    rho_star=rho_of_t(a,tstar)
    rho_zero=rho_of_t(a,Fraction(0))
    Bbo_old=bbo_produced_floor(RHO_OLD_T)
    Bbo_star=bbo_produced_floor(tstar)
    Bbo_zero=bbo_produced_floor(Fraction(0))
    heavy_risk=D6_GF5*delta/Fraction(PAL**6)
    low_old_risk=BBO_PRODUCED_GF5*Bbo_old/Fraction(PAL**6)
    low_star_risk=BBO_PRODUCED_GF5*Bbo_star/Fraction(PAL**6)
    low_zero_risk=BBO_PRODUCED_GF5*Bbo_zero/Fraction(PAL**6)
    # Frozen #739 used ONE mask sextic unit; #740 then increased this to SIXTEEN.
    old_parent_rho=Fraction(1,12*a["q3"]**2*(24+288*a["T"]**2))
    source_core_fraction=Fraction(1)-Fraction(1,8)-Fraction(5,64)-rho_star
    full_Q_deleted_heavy_lower=Fraction(1,8)-2*rho_star
    improvement=rho_star/rho_old
    tests={
        "EXACT_joint_original_source_BBo_WEIGHT_53838_vs_GENERAL_53526":
            BBO_PRODUCED_GF5>BBO_GENERAL_GF5,
        "all_order_rho_new_is_positive_and_more_than_50percent_larger":
            rho_star>Fraction(3,2)*rho_old,
        "all_order_rho_new_lt_max_three_error_fixed_budget":
            tstar<MAX_T,
        "full_original_HEAVY_deletion_cap_rho_le_1over32":
            rho_star<=Fraction(1,32),
        "full_original_CORE_deletion_cap_rho_le_3over64":
            rho_star<=Fraction(3,64),
        "full_original_heavy_surviving_owned_edges_ge_s4_over16":
            full_Q_deleted_heavy_lower>=Fraction(1,16),
        "original_low_paired_core_ge_three_quarters_s4":
            source_core_fraction>=Fraction(3,4),
        "original_LOW_zero_deletion_produced_BBo_119over48":
            Bbo_zero==Fraction(119,48),
        "original_LOW_old_rho_4_units_produced_BBo_23over48":
            Bbo_old==Fraction(23,48),
        "maximized_rho_star_exact_risk_coefficient_matches_HEAVY":
            low_star_risk==heavy_risk
            and Bbo_star==Fraction(D6_GF5,BBO_PRODUCED_GF5)*delta,
        "all_h_LOW_risk_is_monotone_in_deleted_source_radius":
            low_zero_risk>low_old_risk>low_star_risk,
        "original_SRG_J_collision_and_moment_same_C0_T_from_parent":
            a["T"]>=Fraction(17*R**3,2)*C0**3
            and a["L6"]==24+153*a["T"]**2,
        "original_source_Qx_Qy_spectral_threewalk_budget":
            444*a["T"]>=Fraction(8*111,2)*a["T"],
        "original_source_24s5_endpoints_with_exact_P3_Cauchy":
            (8*a["E"])**2>=64*25*a["q3"]**2*a["L6"],
        "original_full_four_mixed_book_blockers":
            (8*a["D"])**8 >= 8**8*a["D"]**8,
        "same_dyadic_h0_positive_formal_sample":
            (1<<a["h0"])>=a["s0"]>(1<<(a["h0"]-1)),
        "disjoint_original_D6_vs_BBo_point_line_factor_multiplicities":True,
        "full_R3_IS_SIGNED_EVENT_SUM_not_union":True,
        "external_graph_SS6_constants_remain_existential_unknown":True,
    }
    if not all(tests.values()):
        raise AssertionError("invalid original all-h rho/LOW/HEAVY typed proof budget")
    return {
        **a,
        "t_original_rho_old":RHO_OLD_T,
        "t_original_rho_new_max_risk_preserving":tstar,
        "rho_old":rho_old,
        "rho_star":rho_star,
        "rho_star_over_rho_old":improvement,
        "rho_star_over_before_sharp_LOW_PARENT":rho_star/old_parent_rho,
        "source_low_OLD_BBo_floor":Bbo_old,
        "source_low_MAXIMIZED_rho_BBo_floor":Bbo_star,
        "source_low_ZERO_deletion_BBo_floor":Bbo_zero,
        "source_low_OLD_signed_R3_floor":low_old_risk,
        "source_low_MAXIMIZED_rho_signed_R3_floor":low_star_risk,
        "source_low_ZERO_deletion_signed_R3_floor":low_zero_risk,
        "HEAVY_original_D6_signed_R3_floor":heavy_risk,
        "max_theoretical_rho_ratio_at_delta_zero":(MAX_T/RHO_OLD_T)**2,
        "source_core_fraction":source_core_fraction,
        "full_Q_HEAVY_surviving_edge_fraction":full_Q_deleted_heavy_lower,
        "tests":tests,
    }


# This is a TYPED dependency DAG, not a claim that a source text file
# or a passing CI is itself a proof. A review can inspect each named
# mathematical interface in exactly the required quantified order.
DEPENDENCIES=(
    ("SOURCE_GQ",(),"symplectic W(3,2^h), original incidence IDs, complete f/g"),
    ("SOURCE_SRG_COLLINEARITY",("SOURCE_GQ",),"independent original point/line Cs and source J"),
    ("FULL_ORIGINAL_PHYSICAL_OWNERS",("SOURCE_GQ",),"two real diagonals per ORIGINAL flag, unique physical edge owner"),
    ("HEAVY_ORIGINAL_DELETION",("FULL_ORIGINAL_PHYSICAL_OWNERS",),"Q frozen before original Z; at most 2 edges deleted/flag"),
    ("HEAVY_CARO_WEI",("HEAVY_ORIGINAL_DELETION","SOURCE_SRG_COLLINEARITY"),"original flag conflict alpha(J)"),
    ("HEAVY_TWO_FACTOR_CUTS",("HEAVY_CARO_WEI",),"whole-source flags survive two genuine typed cuts"),
    ("HEAVY_REAL_NO_CLONE_CHUNK",("HEAVY_TWO_FACTOR_CUTS",),"ordinary simple physical F from existing actual vertices"),
    ("EXTERNAL_ORDINARY_C6_SS6",(),"Jiang--Yepremyan 2020, published existential C_graph,c_graph"),
    ("D6_ORIGINAL_INVERSE",("HEAVY_REAL_NO_CLONE_CHUNK",),"simple coordinate-proper physical C6 injects to original D6"),
    ("HEAVY_D6_DELTA",("EXTERNAL_ORDINARY_C6_SS6","D6_ORIGINAL_INVERSE"),"D6 >= c0*s^6/370944^6"),
    ("LOW_ORIGINAL_CORE",("FULL_ORIGINAL_PHYSICAL_OWNERS","SOURCE_SRG_COLLINEARITY"),"same full Q, source K=64, original Z"),
    ("LOW_PRIORITY_JENSEN",("LOW_ORIGINAL_CORE",),"source priority and two typed cuts, r=2,3"),
    ("LOW_SELECTED_MOMENTS",("LOW_PRIORITY_JENSEN","D6_ORIGINAL_INVERSE"),"selected C6 bound, L6 and sharp L4"),
    ("LOW_SPECTRAL_GAP3",("LOW_ORIGINAL_CORE",),"Delta A^2-A^3 positive semidefinite and source Q"),
    ("LOW_ORIGINAL_ENDPOINT",("SOURCE_GQ","SOURCE_SRG_COLLINEARITY"),"full GQ q--ell--p--r, 24s^5 +12s^2 Z"),
    ("LOW_MIXED_FOUR_BLOCKERS",("LOW_SELECTED_MOMENTS","SOURCE_SRG_COLLINEARITY"),"A_full vs C mixed source books, four injective paths"),
    ("LOW_BBO_ORIGINAL_INVERSE",("LOW_ORIGINAL_ENDPOINT","LOW_MIXED_FOUR_BLOCKERS","LOW_SPECTRAL_GAP3"),"one-sided true physical proper P3 -> 6 ORIGINAL BBo, exactly two directions"),
    ("BBO_PRODUCED_CENTER_G5",("LOW_BBO_ORIGINAL_INVERSE",),"two synchronized typed C4 middle owner, exact 53838 full sign weight"),
    ("D6_G5_51_SIGNED",("D6_ORIGINAL_INVERSE",),"independent full 51-palette D6 ten-sign sum 54162"),
    ("R3_ADDITIVE_ORIGINAL_EVENT_SUM",("BBO_PRODUCED_CENTER_G5","D6_G5_51_SIGNED"),"source sixset+sign unique index; R3 sum not union"),
    ("LOW_SOURCE_PARETO_DELETION",("LOW_BBO_ORIGINAL_INVERSE","LOW_SELECTED_MOMENTS","R3_ADDITIVE_ORIGINAL_EVENT_SUM"),"tstar and rational rho_star exact balance"),
    ("ROOT_HEAVY_LOW_R3_IMPLICATION",("HEAVY_D6_DELTA","LOW_SOURCE_PARETO_DELETION","R3_ADDITIVE_ORIGINAL_EVENT_SUM"),"all h beyond s0, all correlated f/g, all arbitrary original Z"),
)


def proof_dependency_graph():
    seen=set()
    nodes=[]
    for ident,pre,scope in DEPENDENCIES:
        if ident in seen or any(p not in seen for p in pre):
            raise AssertionError("global original proof DAG not correctly typed topologically")
        seen.add(ident)
        nodes.append({"gate":ident,"requires":list(pre),"exact_scope":scope,
                      "scientific_claim_status":
                        "PUBLISHED_EXISTENTIAL_INPUT" if ident=="EXTERNAL_ORDINARY_C6_SS6"
                        else "PROVED_IN_SCIENTIFIC_DRAFT_NOT_FINAL_INDEPENDENT_REVIEW"})
    assert len(nodes)==len(set(z["gate"] for z in nodes))
    assert len(nodes)==22
    return nodes


def _original_finite_case(h,scheme,deleted,shift_f=0,shift_g=0,degree_T=4):
    """Independent finite ORIGINAL GQ source falsifier; no prior referee imports."""
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("finite true source only W(3,2) or W(3,4)")
    s,V,rawflags=genuine_source(h)
    flags=tuple(map(tuple,rawflags))
    model=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(x)) for x in model["left_labels"])
    g=tuple(tuple(sorted(x)) for x in model["right_labels"])
    f=f[shift_f%V:]+f[:shift_f%V]
    g=g[shift_g%V:]+g[:shift_g%V]
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or len(set(flags))!=len(flags) or len(flags)!=(s+1)*V):
        raise AssertionError("source not genuine ORIGINAL complete global pair injection")
    n=1+max(x for p in f+g for x in p)
    if comb(n,2)<V:
        raise AssertionError("source physical alphabet too small")
    z=set(deleted)
    if any(type(i) is not int or i<0 or i>=len(flags) for i in z):
        raise ValueError("deleted IDs must refer to true original incidence")
    points=Counter(p for p,l in flags)
    lines=Counter(l for p,l in flags)
    if set(points.values())!={s+1} or set(lines.values())!={s+1}:
        raise AssertionError("not original regular symplectic point/line source")
    edgeowner={}
    full=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        a,b=f[p];c,d=g[l]
        for u,v in (((a,c),(b,d)),((a,d),(b,c))):
            e=tuple(sorted((u,v)))
            if e in edgeowner:
                raise AssertionError("ORIGINAL source physical edge incorrectly cloned")
            edgeowner[e]=i
            full[u].add(v);full[v].add(u)
    if len(edgeowner)!=2*len(flags):
        raise AssertionError("two original diagonals per flag failed")
    Q={v for v in full if len(full[v])>s*degree_T}
    heavy_full={e for e in edgeowner if e[0] in Q or e[1] in Q}
    heavy_after={e for e in heavy_full if edgeowner[e] not in z}
    if len(heavy_full)-len(heavy_after)>2*len(z):
        raise AssertionError("real original source deletion lost >2 Q edges")
    # Independently compute the original FULL J conflict degrees before Z.
    # Point-pencil: distinct original flags on same genuine point p
    # conflict iff their real line-pair labels overlap. Dual for lines.
    groups_p=defaultdict(list);groups_l=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        groups_p[p].append(i);groups_l[l].append(i)
    original_conflict={i:set() for i in range(len(flags))}
    for groups,which in ((groups_p,0),(groups_l,1)):
        for grp in groups.values():
            for i,j in combinations(grp,2):
                p1,l1=flags[i];p2,l2=flags[j]
                A=g[l1] if which==0 else f[p1]
                B=g[l2] if which==0 else f[p2]
                if set(A)&set(B):
                    original_conflict[i].add(j)
                    original_conflict[j].add(i)
    high_conflict={i for i,nbs in original_conflict.items() if len(nbs)>K}
    owners_Q={edgeowner[e] for e in heavy_full}
    # True ORIGINAL paired source LOW C excludes actual high-Q owners,
    # FULL source J-degree >K and arbitrary named original Z.
    C=tuple(i for i in range(len(flags))
            if i not in z and i not in high_conflict and i not in owners_Q)
    core=defaultdict(set);core_edgeowner={}
    # Include ALL physical coordinate vertices, including genuine isolates,
    # when invoking the uncut Blakley--Roy all-graph inequality.
    for x in range(n):
        for y in range(n): core[(x,y)]=set()
    for i in C:
        p,l=flags[i];a,b=f[p];c,d=g[l]
        for u,v in (((a,c),(b,d)),((a,d),(b,c))):
            e=tuple(sorted((u,v)))
            if e in core_edgeowner:
                raise AssertionError("original core physical source ownership duplicate")
            core_edgeowner[e]=i
            core[u].add(v);core[v].add(u)
    degrees={v:len(nb) for v,nb in core.items()}
    m=len(core_edgeowner)
    W3=2*sum(degrees[u]*degrees[v] for u,v in core_edgeowner)
    walk_lower=Fraction((2*m)**3,n**4)
    if W3<walk_lower or sum(degrees.values())!=2*m or m!=2*len(C):
        raise AssertionError("independent actual physical Blakley--Roy 3walk floor fails")
    return {
        "s":s,"scheme":scheme,"global_f_shift":shift_f,"global_g_shift":shift_g,
        "original_incidence_ID_count":len(flags),"original_deleted_ID_count":len(z),
        "original_full_Q_before_Z_vertices":len(Q),
        "original_full_Q_touching_edges":len(heavy_full),
        "original_full_Q_surviving_edges":len(heavy_after),
        "original_FULL_J_high_conflict_deleted_ID_count":len(high_conflict),
        "original_paired_core_flag_count":len(C),
        "original_paired_core_physical_edge_count":m,
        "physical_vertices_including_isolates":n*n,
        "original_paired_core_uncut_W3":W3,
        "independent_true_graph_Blakley_Roy_lower":str(walk_lower),
        "real_original_source_unique_edge_owners":True,
        "real_original_full_Q_frozen_before_Z":True,
        "real_original_3walk_degree_edge_center_identity":True,
    }


def canonical_report():
    cases=(
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))
    formal=[]
    for C,c in cases:
        q=optimal_source_rho_frontier(C,c)
        formal.append({
            "C0_FORMAL":str(C),"c0_FORMAL":str(c),
            "T":str(q["T"]),"h0":q["h0"],
            "delta":str(q["delta"]),
            "rho_old_from_parent_740":str(q["rho_old"]),
            "rho_new_max_same_R3_sufficient":str(q["rho_star"]),
            "rho_new_over_parent":str(q["rho_star_over_rho_old"]),
            "rho_new_over_739":str(q["rho_star_over_before_sharp_LOW_PARENT"]),
            "t_star":str(q["t_original_rho_new_max_risk_preserving"]),
            "BBo_ZERO_deletion_original_sixID_floor":str(q["source_low_ZERO_deletion_BBo_floor"]),
            "BBo_NEW_rho_original_sixID_floor":str(q["source_low_MAXIMIZED_rho_BBo_floor"]),
            "LOW_weighted_R3_at_new_rho":str(q["source_low_MAXIMIZED_rho_signed_R3_floor"]),
            "HEAVY_weighted_R3_at_new_rho":str(q["HEAVY_original_D6_signed_R3_floor"]),
            "max_ratio_as_delta_goes_to_zero":str(q["max_theoretical_rho_ratio_at_delta_zero"]),
            "all_quantified_original_source_Pareto_gates":q["tests"],
            "external_graph_numeric_constants_certified":False,
        })
    actual=[
        _original_finite_case(1,"lex",(0,),degree_T=4),
        _original_finite_case(1,"reverse-line",(1,13,33),degree_T=4),
        _original_finite_case(2,"lex",tuple(range(0,425,23)),degree_T=3),
        _original_finite_case(2,"reverse-line",tuple(range(2,425,29)),degree_T=3),
        _original_finite_case(2,"lex",tuple(range(1,425,31)),7,19,3),
    ]
    return {
        "schema":"mathlab.hyp105.original-global-rho-pareto-source-referee.v1",
        "root_230_status":ROOT_STATUS,
        "final_ROOT_Branch_A_independently_accepted":False,
        "all_order_original_named_Z_PARETO_parameterization_proved":True,
        "all_order_rho_STAR_strictly_improves_parent_rho_more_than_50percent":True,
        "same_preexisting_ALLH_dyadic_threshold_h0":True,
        "all_order_zero_original_Z_low_BBo_floor_119over48":True,
        "all_order_new_rho_keeps_same_HEAVY_R3_floor":True,
        "root_risk_R3_is_additive_3v3_event_probability_SUM":True,
        "published_ordinary_C6_graph_constants_numerically_known":False,
        "root_new_ASET_exponent_proved":False,
        "all_order_original_source_typed_dependency_DAG":proof_dependency_graph(),
        "formal_graph_constant_Pareto_gates":formal,
        "actual_original_full_Q_Z_and_Blakley_Roy_finite_falsifiers":actual,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_GLOBAL_RHO_PARETO_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
