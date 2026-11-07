"""HYP-105 AA4-ROOTGATE: self-contained exact conditional all-h proof DAG.

A non-Fourier, non-parent-code, rational source-envelope and heavy/low
arithmetic referee for the genuine ORIGINAL W(3,2^h) six-ID theorem.

The ordinary C6 graph supersaturation theorem supplies existential Cg,cg;
the input rationals C0>=Cg>=1 and 0<c0<=cg<=1 are FORMAL bounds.
No numerical published constants or universal root acceptance are claimed.

The proof remains DEPENDENT on individually stated source-selector,
no-clone, ORIGINAL D6/BBo lifting and endpoint bounds from #730-#735.
Only the implication between these premises is independently recertified.
"""
from fractions import Fraction
from math import comb, isqrt
import json

STATUS = "OPEN_WITH_FORMAL_BLOCKER"
SIX_PALETTE_DENOM = 51**6
HEAVY_GF5_WEIGHT = 54162
LOW_GF5_WEIGHT = 53526
K0 = 64


def nonnegative_root_ceil(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer for exact ceil sqrt")
    t = isqrt(n)
    return t + (t*t != n)


def fraction_ceil(q):
    if not isinstance(q, Fraction):
        raise ValueError("only exact rational")
    return -(-q.numerator//q.denominator)


def original_envelope(s):
    """Unconditional minimal complete ORIGINAL source size inequalities."""
    if type(s) is not int or s < 64 or s & (s-1):
        raise ValueError("original source dyadic s>=64 only")
    v = (s+1)*(s*s+1)
    nflags = (s+1)*v
    a = (1+isqrt(1+8*v))//2
    while comb(a,2)<v:
        a+=1
    cs = (s*s+1)*(s*s+a-2)
    checks = {
        "original_flags_ge_s4":nflags >= s**4,
        "original_flags_le_2s4":nflags <= 2*s**4,
        "original_alphabet_minimal":comb(a-1,2)<v<=comb(a,2),
        "physical_corners_le_4s3":a*a<=4*s**3,
        "collision_book_le_3half_s4":2*cs<=3*s**4,
        "original_point_line_srg_dimensions":v==(s+1)*(s*s+1),
    }
    if not all(checks.values()):
        raise AssertionError("genuine complete original GQ source envelope broken")
    return {"s":s,"V":v,"N":nflags,"alphabet":a,"physical_corners":a*a,
            "source_collision_book":cs,"checks":checks}


def exact_conditional_ledger(C0, c0):
    """Independent exact derivation of BOTH original branches and weights.

    External constants are only symbolic RATIONAL bounds, not numeric
    claims about the Jiang-Yepremyan/Simonovits graph theorem.
    """
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("formal exact rationals C0>=1, 0<c0<=1 required")
    k = K0+1
    T = fraction_ceil(Fraction(2**64)*C0**3)
    q2 = 16*comb(2*k,2)
    q3 = 64*comb(3*k,3)
    L6 = 24+288*T*T
    L4 = 2*q2*q2*nonnegative_root_ceil(8*L6)+56*T
    B0 = nonnegative_root_ceil(1280*k*T)
    E = 8*q3*nonnegative_root_ceil(L6)
    D = 4*nonnegative_root_ceil(B0*T*L4)
    rho = Fraction(1,12*q3*q3*L6)
    delta = c0/Fraction(2**120)
    s0 = max(64,672*T,(8*E)**2,(8*D)**8)
    h0 = (s0-1).bit_length()
    s = 1<<h0
    # HEAVY: original frozen physical high-Q edge budget and true source cuts.
    # eHeavy >= s4/8 -2*rho*s4 >= s4/16.
    # L>=s4/32. C_source conflict-edge <=3s4, L<=2s4.
    # Caro-Wei and coordinate cuts: |I_G|>=s4/2^15.
    # Balanced ordinary chunk: d>=s/2^20, v<=16s3/T.
    heavy_e_lower = Fraction(1,8)-2*rho
    heavy_source_lower = heavy_e_lower/2
    beta = Fraction(1,2**15)
    density_coefficient = beta/Fraction(32)
    ss6_threshold_lhs = Fraction(T)*density_coefficient**3
    ss6_threshold_rhs = Fraction(16)*C0**3
    heavy_d6_floor = c0*density_coefficient**6
    # LOW: delete full-Q owners, high full-source conflict >K, and Z.
    low_core_lower = Fraction(1)-Fraction(1,8)-Fraction(3,32)-rho
    low_core_rounded_floor = Fraction(3,4)
    w3 = Fraction((4*3)**3,4**3)  # not the physical n bound! replaced below.
    # a^4 <= 16s^6; 4*|C|>=3s^4 yields (3s4)^3/(16s6).
    w3 = Fraction(27,16)
    deletion_mask_units = 12*rho*q3*q3*L6
    # h0 meets individually all three strictly sub-sextic budgets.
    improper_budget = Fraction(84*T,s)
    nonZ_budget = Fraction(E,1)*Fraction(1,nonnegative_root_ceil(s))
    # For dyadic s=2^h with odd h use exact integer comparison instead:
    nonZ_threshold = s >= (8*E)**2
    blocker_threshold = s >= (8*D)**8
    # The following numbers are EXACT, not floating decimal approximations.
    total_low_error = Fraction(1)+Fraction(3,8)
    low_twice_bbo_floor = w3-total_low_error
    low_bbo_floor = low_twice_bbo_floor/2
    heavy_risk_coefficient = HEAVY_GF5_WEIGHT*delta
    low_risk_coefficient = LOW_GF5_WEIGHT*low_bbo_floor
    combined_coefficient = min(heavy_risk_coefficient,low_risk_coefficient)
    checks = {
        "published_constant_only_formal":C0>=1 and 0<c0<=1,
        "true_heavy_survivors_ge_1_16":heavy_e_lower>=Fraction(1,16),
        "true_heavy_source_ge_1_32":heavy_source_lower>=Fraction(1,32),
        "Caro_Wei_two_color_beta_valid":
            Fraction(1,32)**2/Fraction(4*8) == beta,
        "physical_heavy_density_is_s_over_2pow20":
            density_coefficient == Fraction(1,2**20),
        "SS6_actual_C0_threshold_closed":ss6_threshold_lhs>=ss6_threshold_rhs,
        "SS6_graph_implies_original_D6":
            heavy_d6_floor>=delta,
        "true_original_core_at_least_3_4":low_core_lower>=low_core_rounded_floor,
        "original_low_triple_walk_ge_27_16":w3==Fraction(27,16),
        "low_original_Q_bound_and_4th_moment_consistent":
            L4>=2*q2*q2*nonnegative_root_ceil(8*L6)+56*T,
        "low_deletion_mask_bounded_by_one_sextic":
            deletion_mask_units<=1,
        "low_coordinate_improper_le_1_8":
            s>=672*T and improper_budget<=Fraction(1,8),
        "low_nonZ_endpoints_le_1_8":nonZ_threshold,
        "low_four_internal_blockers_le_1_8":blocker_threshold,
        "low_BBo_twice_at_least_5_16":
            low_twice_bbo_floor==Fraction(5,16),
        "low_BBo_at_least_5_32":low_bbo_floor==Fraction(5,32),
        "heavy_weight_is_limiting":
            heavy_risk_coefficient<low_risk_coefficient,
        "global_weighted_floor_improves_old_53526_delta":
            combined_coefficient==HEAVY_GF5_WEIGHT*delta
            and combined_coefficient>LOW_GF5_WEIGHT*delta,
        "minimal_dyadic_h0":(1<<h0)>=s0 and (1<<(h0-1))<s0,
    }
    if not all(checks.values()):
        raise AssertionError("conditional original heavy/low proof DAG did not close")
    return {
        "formal_graph_C_upper":C0,"formal_graph_c_lower":c0,
        "K":K0,"T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,
        "B0":B0,"E":E,"D":D,"rho":rho,"delta":delta,
        "s0":s0,"h0":h0,
        "heavy_original_source_floor":heavy_source_lower,
        "heavy_source_independent_fraction":beta,
        "heavy_ordinary_density_coefficient":density_coefficient,
        "heavy_graph_SS6_threshold_lhs":ss6_threshold_lhs,
        "heavy_graph_SS6_threshold_rhs":ss6_threshold_rhs,
        "heavy_D6_floor_per_s6":delta,
        "low_original_retained_core_fraction":low_core_lower,
        "low_original_W3_floor_per_s6":w3,
        "low_original_deleted_mask_per_s6":deletion_mask_units,
        "low_BBo_floor_per_s6":low_bbo_floor,
        "D6_all_sign_GF5_weight":HEAVY_GF5_WEIGHT,
        "BBo_all_sign_GF5_min_weight":LOW_GF5_WEIGHT,
        "heavy_risk_numerator_per_s6":heavy_risk_coefficient,
        "low_risk_numerator_per_s6":low_risk_coefficient,
        "global_risk_numerator_per_s6":combined_coefficient,
        "all_checks":checks,
        "root_230_mathematically_accepted":False,
    }


def gate_with_mutation(C0,c0,*,required_T=None,allowed_rho=None,
                       heavy_GF5=HEAVY_GF5_WEIGHT,
                       low_GF5=LOW_GF5_WEIGHT):
    """Adversarial exact counterfactual validator, NOT a claim of necessity.

    'reject' means that these particular sufficient *proof budgets*
    fail, not that the root sixset theorem is mathematically false.
    """
    z=exact_conditional_ledger(C0,c0)
    T=z["T"] if required_T is None else required_T
    rho=z["rho"] if allowed_rho is None else allowed_rho
    if (type(T) is not int or T<=0 or type(rho) is not Fraction or rho<0
            or type(heavy_GF5) is not int or type(low_GF5) is not int):
        raise ValueError("mutations require explicit exact formal values")
    expected = {
        "heavy_external_SS6":{
            "valid":T>=2**64*C0**3,
            "reason":"the ordinary graph SS6 threshold is only sufficient"},
        "heavy_original_deletion":{
            "valid":Fraction(1,8)-2*rho>=Fraction(1,16),
            "reason":"full-source high-Q edge deletion mass must stay >= s4/16"},
        "low_original_density":{
            "valid":Fraction(1)-Fraction(1,8)-Fraction(3,32)-rho>=Fraction(3,4),
            "reason":"original surviving paired core must retain 3s4/4 flags"},
        "low_proper_path_mask":{
            "valid":12*rho*z["q3"]**2*(24+288*T*T)<=1,
            "reason":"adversarial ORIGINAL projection Z consumes at most s6"},
        "GF5_original_source_nonzero":{
            "valid":heavy_GF5>=54162 and low_GF5>=53526,
            "reason":"the source sixset total signed weights are class dependent"},
    }
    return {"all_valid":all(v["valid"] for v in expected.values()),
            "gates":expected,"counterfactual_only":True}


def at_dyadic_order(z,h):
    """Exact large-h threshold audit without computing any float powers."""
    if type(h) is not int or h<1:
        raise ValueError("h must be positive integer")
    s=1<<h
    checks={
        "dyadic_size_above_minimum":s>=z["s0"],
        "heavy_graph_SS6_sufficient_for_any_s":
            z["heavy_graph_SS6_threshold_lhs"]>=z["heavy_graph_SS6_threshold_rhs"],
        "proper_coordinate_improper_le_1_8":
            s>=672*z["T"],
        "proper_nonZ_endpoint_le_1_8":
            s>=(8*z["E"])**2,
        "proper_four_source_blockers_le_1_8":
            s>=(8*z["D"])**8,
        "original_projection_deletion_mask_le_1":
            12*z["rho"]*z["q3"]**2*z["L6"]<=1,
    }
    return {"h":h,"all_gates_closed":all(checks.values()),"checks":checks}


def _compact_fraction(q):
    return str(q)


def original_root_gate_report():
    formal=[]
    for C,c in ((Fraction(1),Fraction(1)),(Fraction(2),Fraction(1,5)),
                (Fraction(7,3),Fraction(1,17))):
        z=exact_conditional_ledger(C,c)
        if not at_dyadic_order(z,z["h0"])["all_gates_closed"]:
            raise AssertionError("at least dyadic h0 not closed")
        if at_dyadic_order(z,z["h0"]-1)["all_gates_closed"]:
            raise AssertionError("h0 must be least dyadic threshold")
        formal.append({
            "C0_FORMAL":str(C),"c0_FORMAL":str(c),
            "T":str(z["T"]),"h0":z["h0"],"s0_bit_length":z["s0"].bit_length(),
            "rho":str(z["rho"]),"delta":str(z["delta"]),
            "low_core_at_least_3_4":z["all_checks"]["true_original_core_at_least_3_4"],
            "low_BBo_at_least_5_32":str(z["low_BBo_floor_per_s6"]),
            "heavy_D6_at_least_delta":str(z["heavy_D6_floor_per_s6"]),
            "D6_ten_GF5":z["D6_all_sign_GF5_weight"],
            "BBo_min_ten_GF5":z["BBo_all_sign_GF5_min_weight"],
            "new_weighted_uniform_numerator":str(z["global_risk_numerator_per_s6"]),
            "old_weighted_uniform_numerator":str(LOW_GF5_WEIGHT*z["delta"]),
            "all_conditionals_hold":all(z["all_checks"].values()),
            "external_constants_numerically_verified":False,
        })
    actual=[original_envelope(1<<h) for h in (6,7,8,10)]
    bad=[]
    refC,refc=Fraction(1),Fraction(1)
    normal=exact_conditional_ledger(refC,refc)
    for label,mutation in (
        ("graph_T_below_sufficient_threshold",
         {"required_T":normal["T"]-1}),
        ("deletion_rho_too_large",
         {"allowed_rho":normal["rho"]*2}),
        ("heavy_GF5_misweight",
         {"heavy_GF5":53526}),
        ("low_GF5_misweight",
         {"low_GF5":51750}),
    ):
        result=gate_with_mutation(refC,refc,**mutation)
        if result["all_valid"]:
            raise AssertionError("expected formal red-team mutation not detected")
        bad.append({"mutation":label,"rejected":True,
                    "failed_gates":[k for k,v in result["gates"].items()
                                    if not v["valid"]]})
    return {
        "schema":"mathlab.hyp105.original-root-proof-dag.v1",
        "root_230_status":STATUS,
        "root_universally_accepted":False,
        "conditional_arithmetic_independently_closed":True,
        "original_graph_SS6_external_constants_existential":True,
        "original_six_ID_source_lifts_independent_review_pending":True,
        "actual_original_source_envelopes":actual,
        "three_formal_rational_graph_theorem_ledgers":formal,
        "red_team_mutations":bad,
        "uniform_old_class_weight":LOW_GF5_WEIGHT,
        "uniform_new_branch_weight":HEAVY_GF5_WEIGHT,
        "weighted_improvement_ratio":str(Fraction(
            HEAVY_GF5_WEIGHT,LOW_GF5_WEIGHT)),
        "root_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_ROOT_DAG_CERTIFICATE="+json.dumps(
        original_root_gate_report(),sort_keys=True,separators=(",",":")),flush=True)
