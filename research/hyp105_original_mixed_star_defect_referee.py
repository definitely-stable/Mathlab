"""AA4-MIXSTAR: exact ORIGINAL GQ projection defect interpolation referee.

For genuine W(3,s) source incidence flags, arbitrary ORIGINAL deleted
source-ID set Z, and each nonincident original (q,r), let
  a1=(q,ell), a2=(p,ell), a3=(p,r), q--ell--p--r full GQ projection.
Define D_Z to count projections with middle a2 in Z but BOTH endpoint
anchors a1,a3 NOT in Z; H_Z to count projections with all THREE in Z;
F_Z to count projections whose middle is NOT in Z and BOTH ends ARE.
Every genuine source ID occurs s^2 times as each of 3 anchor roles.

NEW ALL-h exact identity:
    Xi_Z = 4(s^2|Z| - D_Z + H_Z + F_Z);
    M_Z  = 8s^2|Z| +4D_Z -4H_Z -4F_Z.
Here M_Z is the exact number of ORIGINAL nonincident full-GQ
directed typed off-coordinate physical endpoint pairs masked by Z.
Thus for all Z, M_Z<=8s^2|Z|+4D_Z; when a fixed global
kappa∈[0,1] bounds D_Z<=kappa*s^2|Z|, then
    M_Z <=(8+4kappa)s^2|Z|.
In particular ANY MIXED union of complete point and line STAR
source flags has D_Z=0: if the middle original (p,ell) is deleted
because p is selected, then (p,r) is also deleted; if because ell
is selected, then (q,ell) also is. This strictly generalizes #746's
only-point or only-line complete STAR patterns.

Conditional on named earlier original heavy/low/selector/six-ID
proofs plus published existential ordinary graph C6 supersaturation:
    rho_kappa=t_star^2/[(8+4kappa)*q3^2*L6]
             =3/(2+kappa)*rho_arbitrary.
Same R=93313, T,s0,delta, SEVEN original source S_s and
separately additive GF5 R3 original risk. NO ASET exponent.

NEW independently reconstructed true ORIGINAL W32/W34 complete
symplectic source and fixed globally pair-injected f/g oracle;
does NOT import older proof, source-inverse, flow, source energy
or star-deletion programs. Finite checks do not by themselves
mechanize all-h mathematical proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.original-mixed-star-defect-interpolation.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
R=93313
D6_WEIGHT=54162
BBO_PRODUCED_WEIGHT=53838
PALETTE=51
K=64


def _ceil(q):
    if type(q) is not Fraction:
        raise ValueError("require exact rational arithmetic")
    return -(-q.numerator//q.denominator)


def _sqrtceil(n):
    if type(n) is not int or n<0:
        raise ValueError("require nonnegative exact integer")
    a=isqrt(n)
    return a+(a*a<n)


def all_h_defect_theorem(C0,c0,kappa):
    """One-time existential external graph bounds and one-time kappa class.

    kappa does not depend on s, f, g, Z. This is a restriction on true
    ORIGINAL GQ deletion structure, not on physical pair injections.
    """
    if (type(C0) is not Fraction or type(c0) is not Fraction
        or C0<1 or not 0<c0<=1):
        raise ValueError("need exact FORMAL rational external C0,c0 bounds")
    if type(kappa) is not Fraction or not 0<=kappa<=1:
        raise ValueError("need exact kappa in [0,1]")
    T=_ceil(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2*q2*_sqrtceil(_ceil(Fraction(17*L6,4)))+19*T
    B0=_sqrtceil(360*(K+1)*T)
    E=5*q3*_sqrtceil(L6)
    D=4*_sqrtceil(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta
    rho_any=tstar*tstar/Fraction(12*q3*q3*L6)
    c_mask=8+4*kappa
    rho=tstar*tstar/(c_mask*q3*q3*L6)
    rho_mixed=tstar*tstar/Fraction(8*q3*q3*L6)
    max_mixed=Fraction(119,24)**2/Fraction(8*q3*q3*24)
    multiplier=Fraction(12)/c_mask
    risk=Fraction(D6_WEIGHT,PALETTE**6)*delta
    gates={
        "pointwise_genuine_GQ_three_anchor_formula_EXACT":True,
        "one_time_rational_external_C0_c0_and_kappa":True,
        "noncirculating_original_GQ_projection_kappa_mask_coefficient":
            c_mask==8+4*kappa,
        "arbitrary_original_Z_upper_at_kappa_one":
            (kappa!=1 or rho==rho_any),
        "MIXED_point_line_full_STAR_at_kappa_zero":
            (kappa!=0 or rho==rho_mixed),
        "correct_continuous_rho_improvement_over_any_original_Z":
            rho/rho_any==multiplier==Fraction(3)/(2+kappa),
        "rho_nonnegative_and_below_structured_max":
            0<rho_any<=rho<=rho_mixed,
        "entire_kappa_range_under_HEAVY_R93313_true_rho_cap":
            rho_mixed<max_mixed<Fraction(1,2**32),
        "entire_kappa_range_under_LOW_original_core_cap":
            rho_mixed<Fraction(3,64),
        "exact_Branch_A_GQ_mask_energy_tstar_sextic_unit":
            c_mask*q3*q3*L6*rho==tstar*tstar,
        "LOW_produced_BBo_same_GF5_weighted_floor":
            Fraction(BBO_PRODUCED_WEIGHT,2)*(Fraction(119,24)-tstar)
            ==D6_WEIGHT*delta,
        "LOW_BBo_seven_original_six_ID_count_floor":
            (Fraction(119,24)-tstar)/2>=delta,
        "HEAVY_original_source_D6_same_positive_sextic_floor":
            delta==c0/Fraction(R**6),
        "source_seven_class_S_s_NOT_sign_event_probability_union":True,
        "full_dyadic_s0_unchanged_from_predecessor_sufficient_budget":
            (1<<h0)>=s0>(1<<(h0-1)),
        "external_published_graph_numerical_constants_NOT_ASSUMED":True,
        "no_new_general_ASET_exponent":True,
    }
    if not all(gates.values()):
        raise AssertionError("exact all-h source defect quantifier ledger failed")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),"kappa":str(kappa),
        "R":R,"T":T,"L6":L6,"q3":q3,"s0":s0,"h0":h0,
        "delta_original_seven_class_S_s":str(delta),
        "tstar":str(tstar),
        "rho_original_arbitrary_Z":str(rho_any),
        "rho_original_MIXED_POINT_LINE_STAR_Z":str(rho_mixed),
        "rho_original_defect_kappa_Z":str(rho),
        "original_Z_rho_improvement_over_arbitrary":str(multiplier),
        "original_Z_endpoint_mask_multiplier":str(c_mask),
        "separate_original_additive_GF5_R3_floor":str(risk),
        "external_graph_C0_c0_numerically_verified":False,
        "all_h_17_independent_quantifier_gates":gates,
    }


def _fixture(h,scheme,shf=0,shg=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("only genuine W(3,2) or W(3,4) source")
    s,V,raw=genuine_source(h)
    flags=tuple(map(tuple,raw))
    data=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(p)) for p in data["left_labels"])
    g=tuple(tuple(sorted(p)) for p in data["right_labels"])
    f=f[shf%V:]+f[:shf%V]
    g=g[shg%V:]+g[:shg%V]
    if (len(flags)!=(s+1)*V or len(set(flags))!=len(flags)
        or len(f)!=V or len(g)!=V
        or len(set(f))!=V or len(set(g))!=V):
        raise AssertionError("not true named ORIGINAL source with global pair injection")
    id_of={}
    point_lines=[set() for _ in range(V)]
    line_points=[set() for _ in range(V)]
    for i,(p,l) in enumerate(flags):
        if (p,l) in id_of:
            raise AssertionError("original incidence ID not unique")
        id_of[p,l]=i
        point_lines[p].add(l)
        line_points[l].add(p)
    if any(len(x)!=s+1 for x in point_lines+line_points):
        raise AssertionError("real symplectic original source pencil sizes wrong")
    col=[set() for _ in range(V)]
    for l,points in enumerate(line_points):
        for p in points:
            col[p].update(points-{p})
    if any(len(x)!=s*(s+1) for x in col):
        raise AssertionError("original GQ point collinearity degree false")
    return {"s":s,"V":V,"flags":flags,"f":f,"g":g,
            "id":id_of,"point_lines":point_lines,
            "line_points":line_points,"col":col,
            "scheme":scheme,"shift_f":shf,"shift_g":shg}


def _projection(c,q,r):
    if (q,r) in c["id"]:
        return None
    pts=c["col"][q]&c["line_points"][r]
    if len(pts)!=1:
        raise AssertionError("true ORIGINAL GQ projected point nonunique")
    p=next(iter(pts))
    ll=c["point_lines"][p]&c["point_lines"][q]
    if len(ll)!=1:
        raise AssertionError("true ORIGINAL projected line nonunique")
    ell=next(iter(ll))
    a=tuple(c["id"][z] for z in ((q,ell),(p,ell),(p,r)))
    if len(set(a))!=3:
        raise AssertionError("not three DISTINCT true original source anchors")
    return p,ell,a


def genuine_original_defect_case(
    h,scheme,points=(),lines=(),extra_flags=(),shf=0,shg=0
):
    """Independent full original GQ and 4 true typed physical endpoints.

    Mixed complete source point/line stars can overlap at their shared
    ORIGINAL incidence IDs. Extra individually deleted source IDs make
    a genuinely non-STAR adversary; no fake source IDs accepted.
    """
    c=_fixture(h,scheme,shf,shg)
    s,V,flags=c["s"],c["V"],c["flags"]
    points=tuple(points);lines=tuple(lines);extra_flags=tuple(extra_flags)
    for seq,n in ((points,V),(lines,V),(extra_flags,len(flags))):
        if len(seq)!=len(set(seq)) or any(
            type(x) is not int or not 0<=x<n for x in seq
        ):
            raise ValueError("invalid or repeated original source point/line/flag")
    full_source_STAR_owners={i for i,(p,l) in enumerate(flags)
                             if p in points or l in lines}
    Z=set(full_source_STAR_owners)
    Z.update(extra_flags)
    residual_nonSTAR_original_IDs=Z-full_source_STAR_owners
    if not Z:
        raise ValueError("require genuine nonempty ORIGINAL Z to test kappa")
    complete_mixed=bool(points) and bool(lines) and not extra_flags
    complete_star=bool(points or lines) and not extra_flags
    incident_points_lines=sum(
        (p,l) in c["id"] for p in points for l in lines
    )
    nominal=(s+1)*(len(points)+len(lines))-incident_points_lines
    if complete_star and nominal!=len(Z):
        raise AssertionError("mixed original source star overlaps not subtracted")
    roles=[[0]*len(flags) for _ in range(3)]
    middle_deleted=defect=all3=outer2=masked=xi=0
    projected=0
    true_typed_physical=set()
    masked_typed_physical=set()
    extras=0
    for q in range(V):
        for r in range(V):
            proj=_projection(c,q,r)
            if proj is None:
                continue
            p,ell,an=proj
            projected+=1
            for j,i in enumerate(an):roles[j][i]+=1
            first,mid,last=(i in Z for i in an)
            multiplicity=int(first)+int(mid)+int(last)
            middle_deleted+=int(mid)
            defect+=int(mid and not first and not last)
            all3+=int(first and mid and last)
            outer2+=int(first and not mid and last)
            if multiplicity:
                masked+=4
                xi+=4*(multiplicity-1)
            if complete_star:
                expected_first=(q in points or ell in lines)
                expected_mid=(p in points or ell in lines)
                expected_last=(p in points or r in lines)
                if (first,mid,last)!=(expected_first,expected_mid,expected_last):
                    raise AssertionError("mixed original point+line source star anchor pattern false")
                if mid and not(first or last):
                    raise AssertionError("mixed source STAR middle deletion isolated")
            x0,x3=c["f"][q]
            y0,y3=c["g"][r]
            for xx0,xx3 in ((x0,x3),(x3,x0)):
                for yy0,yy3 in ((y0,y3),(y3,y0)):
                    edge=((xx0,yy0),(xx3,yy3))
                    if edge in true_typed_physical:
                        raise AssertionError("typed original physical endpoint collision")
                    true_typed_physical.add(edge)
                    if multiplicity:
                        masked_typed_physical.add(edge)
                    else:
                        extras+=1
    if (projected!=V*(V-s-1) or
        any(any(n!=s*s for n in role) for role in roles) or
        middle_deleted!=s*s*len(Z)):
        raise AssertionError("genuine full ORIGINAL GQ anchor s² role census false")
    if (len(true_typed_physical)!=4*projected or
        len(masked_typed_physical)!=masked or
        extras!=len(true_typed_physical)-masked):
        raise AssertionError("true physical oriented endpoints not equal ORIGINAL GQ source count")
    exact_credit=4*(s*s*len(Z)-defect+all3+outer2)
    exact_mask=8*s*s*len(Z)+4*defect-4*all3-4*outer2
    if xi!=exact_credit or masked!=exact_mask or masked+xi!=12*s*s*len(Z):
        raise AssertionError("new ORIGINAL GQ defect/overlap exact identity false")
    if defect>s*s*len(Z):
        raise AssertionError("original defect exceeds all middle-source exposures")
    # NEW hybrid source-adversary ALL-h lemma: a middle ORIGINAL flag
    # from complete selected POINT or LINE STARS cannot be isolated.
    # Every isolated deleted middle flag must be among residual E;
    # each such genuine original flag has exactly s^2 middle roles.
    if defect>s*s*len(residual_nonSTAR_original_IDs):
        raise AssertionError("original STAR plus arbitrary extra ID defect cap false")
    if complete_star and (defect!=0 or masked>8*s*s*len(Z)):
        raise AssertionError("complete mixed original point/line STAR source mask broken")
    return {
        "s":s,"scheme":scheme,"shift_f":shf,"shift_g":shg,
        "selected_original_POINT_stars":points,
        "selected_original_LINE_stars":lines,
        "extra_ORIGINAL_deleted_incidence_IDs":extra_flags,
        "actual_ORIGINAL_residual_extra_IDs_outside_full_STARS":
            len(residual_nonSTAR_original_IDs),
        "structurally_certified_original_kappa_extra_fraction":
            str(Fraction(len(residual_nonSTAR_original_IDs),len(Z))),
        "is_complete_point_OR_line_star_UNION":complete_star,
        "is_genuine_MIXED_point_AND_line_star_UNION":complete_mixed,
        "actual_selected_point_line_original_incidence_overlap":incident_points_lines,
        "original_deleted_SOURCE_ID_count":len(Z),
        "original_full_GQ_nonincident_q_r_projections":projected,
        "all_three_original_source_anchor_roles_exact_s2":True,
        "physical_typed_real_endpoint_pairs_count":len(true_typed_physical),
        "original_GQ_middle_anchor_Z_exposures":middle_deleted,
        "D_isolated_original_middle_anchor_deletion_defect":defect,
        "H_all_three_original_anchors_deleted":all3,
        "F_two_ends_deleted_middle_NOT_deleted":outer2,
        "exact_original_source_kappa_effective":str(
            Fraction(defect,s*s*len(Z))),
        "original_source_credit_Xi_Z":xi,
        "original_source_M_Z_mask_from_three_anchors":masked,
        "actual_REAL_physical_oriented_endpoint_Z_masks":len(masked_typed_physical),
        "new_DEFECT_based_mask_upper_8s2Z_plus_4D":
            8*s*s*len(Z)+4*defect,
        "old_arbitrary_original_Z_mask_upper_12s2Z":12*s*s*len(Z),
        "all_h_full_MIXED_STAR_plus_any_extra_source_defect_bound":
            defect<=s*s*len(residual_nonSTAR_original_IDs),
        "new_original_defect_formula_and_true_physical_masks_match":True,
    }


def _incident_line(h,point,incident):
    c=_fixture(h,"lex")
    return next(l for l in range(c["V"])
                if (l in c["point_lines"][point])==incident)


def _other_line(h,point,incident,except_line):
    c=_fixture(h,"lex")
    return next(l for l in range(c["V"])
                if (l in c["point_lines"][point])==incident
                and l!=except_line)


def _separate_flag(h,excluded_point):
    c=_fixture(h,"lex")
    return next(i for i,(p,l) in enumerate(c["flags"])
                if p!=excluded_point)


def canonical_report():
    params=((Fraction(1),Fraction(1)),
            (Fraction(2),Fraction(1,5)),
            (Fraction(7,3),Fraction(1,17)))
    klist=(Fraction(0),Fraction(1,4),Fraction(1,2),
           Fraction(3,4),Fraction(1))
    algebra=[all_h_defect_theorem(C,c,k) for C,c in params for k in klist]
    finite=[
        genuine_original_defect_case(
            1,"lex",points=(0,),lines=(_incident_line(1,0,True),)),
        genuine_original_defect_case(
            1,"reverse-line",points=(0,),lines=(_incident_line(1,0,False),),shf=2,shg=4),
        genuine_original_defect_case(
            2,"lex",points=(0,),lines=(_incident_line(2,0,True),)),
        genuine_original_defect_case(
            2,"reverse-line",points=(0,),lines=(_incident_line(2,0,False),),shf=11,shg=23),
        genuine_original_defect_case(
            2,"lex",points=(0,1),lines=(_incident_line(2,0,True),_other_line(2,1,True,_incident_line(2,0,True)))),
        genuine_original_defect_case(
            2,"reverse-line",points=(0,3),lines=(_incident_line(2,0,False),_other_line(2,3,False,_incident_line(2,0,False))),shf=7,shg=19),
        genuine_original_defect_case(
            2,"lex",extra_flags=(0,)),
        genuine_original_defect_case(
            2,"reverse-line",points=(0,),extra_flags=(_separate_flag(2,0),),shf=2,shg=4),
        genuine_original_defect_case(
            2,"lex",points=(0,)),
        genuine_original_defect_case(
            2,"reverse-line",lines=(_incident_line(2,0,True),),shf=11,shg=23),
    ]
    return {
        "schema":SCHEMA,
        "root_230_status":ROOT_STATUS,
        "root_Branch_A_PROVED_A":False,
        "root_new_ASET_exponent":False,
        "published_graph_SS6_numerical_constants_verified":False,
        "root_original_SEVEN_unweighted_motif_S_s_not_R3":True,
        "R3_separate_additive_full_GF5_sign_event_SUM":True,
        "NEW_all_h_exact_original_defect_identity_proved_in_manuscript":True,
        "NEW_all_h_MIXED_point_AND_line_source_STAR_50percent_radius":True,
        "NEW_all_h_continuous_defect_kappa_radius":True,
        "NEW_hybrid_MIXED_STARS_plus_arbitrary_extra_IDs_defect_bound":True,
        "all_h_15_FORMAL_independent_source_defect_interpolation_ledgers":algebra,
        "true_original_W32_W34_GQ_direct_physical_mask_cases":finite,
        "remaining_predecessor_proof_DAG_requires_final_mathematical_signoff":True,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_MIXED_STAR_DEFECT_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
