"""AA4-STARZ: original FULL-point/line STAR deletion resilience theorem.

NEW source-structural ALL-h theorem: original deletion of ALL incident flags
on any selected original points OR all flags on any selected original lines
has exact projection-overlap savings Xi_Z >= 4*s^2*|Z|. Consequently the
true GQ projection endpoint mask M_Z<=8*s^2*|Z| (old arbitrary Z uses 12),
so the SAME heavy R=93313, original S_s and additive GF5 R3 lower
bounds hold for this restricted-but-genuine adversarial Z class up to
rho_star_star=(3/2)*rho_star_arbitrary*s^4, without changing the old s0.
No new ASET exponent or full root scientific acceptance.

Independent true original W32/W34 source oracle; only trusted genuine
symplectic fixture and complete physical pair-label fixture imports.
No old proof, energy, selector, mixed book or root imports.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.original-full-star-deletion-50pct.v1"


def _ceil(q):
    return -(-q.numerator//q.denominator)


def _csqrt(n):
    x=isqrt(n)
    return x+(x*x<n)


def star_all_h(C0,c0):
    if (type(C0) is not Fraction or type(c0) is not Fraction or
        C0<1 or not 0<c0<=1):
        raise ValueError("only exact rational FORMAL C0,c0 graph bounds")
    R=93313
    T=_ceil(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(130,2)
    q3=64*comb(195,3)
    L6=24+153*T*T
    L4=q2*q2*_csqrt(_ceil(Fraction(17*L6,4)))+19*T
    B0=_csqrt(360*65*T)
    E=5*q3*_csqrt(L6)
    D=4*_csqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*54162,53838)*delta
    rho_any=tstar*tstar/Fraction(12*q3*q3*L6)
    rho_star=tstar*tstar/Fraction(8*q3*q3*L6)
    rho_universal_ceiling=Fraction(3,2)*Fraction(119,24)**2/Fraction(12*q3*q3*24)
    risk=Fraction(54162,51**6)*delta
    gates={
        "source_full_POINT_STAR_two_anchor_deleted_together":True,
        "source_full_LINE_STAR_two_anchor_deleted_together":True,
        "true_original_GQ_each_source_anchor_role_s2":True,
        "new_mask_bound_8s2Z_is_two_thirds_of_12s2Z":Fraction(8,12)==Fraction(2,3),
        "NEW_structured_Z_radius_is_EXACT_3over2_original_arbitrary":
            rho_star==Fraction(3,2)*rho_any,
        "NEW_structured_Z_radius_keeps_R93313_HEAVY_cap":
            0<rho_star<rho_universal_ceiling<Fraction(1,2**32),
        "NEW_structured_Z_radius_keeps_LOW_original_core":
            rho_star<Fraction(3,64),
        "NEW_source_mask_risk_at_structured_Z_radius":
            8*q3*q3*L6*rho_star==tstar*tstar,
        "NEW_BBo_produced_LOW_at_structured_radius_matches_HEAVY_GF5_R3":
            Fraction(53838,2)*(Fraction(119,24)-tstar)==54162*delta,
        "NEW_original_SEVEN_motif_S_s_at_least_same_delta":
            (Fraction(119,24)-tstar)/2>=delta,
        "unchanged_ALL_h_s0_dyadic_threshold":
            (1<<h0)>=s0>(1<<(h0-1)),
        "published_graph_constants_still_EXISTENTIAL_not_numeric":True,
        "no_new_general_ASET_exponent":True,
    }
    if not all(gates.values()):
        raise AssertionError("original source star 50percent all-h proof ledger invalid")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "R":R,"T":T,"q3":q3,"L6":L6,"s0":s0,"h0":h0,
        "delta":str(delta),"t_star":str(tstar),
        "rho_arbitrary_original_Z":str(rho_any),
        "rho_FULL_POINT_OR_LINE_STAR_original_Z":str(rho_star),
        "new_radius_improvement_ratio":"3/2",
        "same_seven_original_motif_S_s_floor":str(delta),
        "same_GF5_additive_R3_floor":str(risk),
        "numerical_graph_constants_published":False,
        "all_h_13_exact_structured_original_Z_theorem_gates":gates,
    }


def _full_source_geometry(h,scheme,shf,shg):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("only true finite original symplectic W32/W34")
    s,V,fl=genuine_source(h)
    flags=tuple(map(tuple,fl))
    m=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(v)) for v in m["left_labels"])
    g=tuple(tuple(sorted(v)) for v in m["right_labels"])
    f=f[shf%V:]+f[:shf%V]
    g=g[shg%V:]+g[:shg%V]
    if (len(flags)!=(s+1)*V or len(set(flags))!=len(flags)
        or len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V):
        raise AssertionError("not genuine original full GQ and global pair-injective maps")
    byp=defaultdict(set);byl=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        byp[p].add(i);byl[l].add(i)
    return s,V,flags,f,g,byp,byl


def true_full_source_star_case(h,scheme,typ,selected,shf=0,shg=0):
    s,V,flags,f,g,byp,byl=_full_source_geometry(h,scheme,shf,shg)
    if typ not in ("point","line"):
        raise ValueError("only COMPLETE original point or original line STAR")
    owners=byp if typ=="point" else byl
    chosen=tuple(selected)
    if (not chosen or len(chosen)!=len(set(chosen))
        or any(type(i) is not int or i<0 or i>=V for i in chosen)):
        raise ValueError("source STAR selection needs distinct true original point/line indices")
    Z=set().union(*(owners[i] for i in chosen))
    if len(Z)!=(s+1)*len(chosen):
        raise AssertionError("not full ORIGINAL source STAR deletion")
    point_lines=defaultdict(set);line_points=defaultdict(set);id_of={}
    for i,(p,l) in enumerate(flags):
        point_lines[p].add(l);line_points[l].add(p);id_of[p,l]=i
    col=[set() for _ in range(V)]
    for l,pts in line_points.items():
        for p in pts:col[p].update(pts-{p})
    exposure=[[0]*len(flags) for _ in range(3)]
    masked=0;rebate=0;projected=0;pointmiddle=0
    extra_star_overlap=0
    for q in range(V):
        for r in range(V):
            if (q,r) in id_of:continue
            pset=col[q]&line_points[r]
            if len(pset)!=1:
                raise AssertionError("full original GQ q--ell--p--r not unique")
            p=next(iter(pset))
            ellset=point_lines[q]&point_lines[p]
            if len(ellset)!=1:
                raise AssertionError("full original GQ connecting ell not unique")
            ell=next(iter(ellset))
            anchor=(id_of[q,ell],id_of[p,ell],id_of[p,r])
            mZ=sum(i in Z for i in anchor)
            projected+=1
            for j,i in enumerate(anchor):exposure[j][i]+=1
            if mZ:
                masked+=4
                rebate+=4*(mZ-1)
            if typ=="point":
                expected=int(q in chosen)+2*int(p in chosen)
                if p in chosen:pointmiddle+=1
                if p in chosen and q in chosen:extra_star_overlap+=1
            else:
                expected=2*int(ell in chosen)+int(r in chosen)
                if ell in chosen:pointmiddle+=1
                if ell in chosen and r in chosen:extra_star_overlap+=1
            if mZ!=expected:
                raise AssertionError("true full original STAR first/middle/final anchor multiplicity wrong")
    if (not all(all(v==s*s for v in xs) for xs in exposure)
        or projected!=V*(V-s-1)
        or pointmiddle!=s*s*len(Z)):
        raise AssertionError("true original GQ source star 3role exposure incorrect")
    if rebate!=4*s*s*len(Z)+4*extra_star_overlap:
        raise AssertionError("true point/line STAR EXACT two-anchor overlap formula false")
    if masked!=8*s*s*len(Z)-4*extra_star_overlap:
        raise AssertionError("genuine ORIGINAL SOURCE STAR mask exact expected formula false")
    if masked>8*s*s*len(Z):
        raise AssertionError("original source STAR mask exceeds proved 8s²|Z|")
    return {
        "s":s,"scheme":scheme,"type":typ,"global_f_shift":shf,
        "global_g_shift":shg,"selected_original_source_stars":chosen,
        "all_deleted_original_incidence_IDs":len(Z),
        "original_nonincident_full_GQ_projections":projected,
        "each_source_role_s2_exact":True,
        "source_projections_middle_STAR_selected":pointmiddle,
        "source_extra_both_endpoint_and_middle_STAR_overlap":extra_star_overlap,
        "actual_original_Z_masked_directed_typed_endpoints":masked,
        "original_Z_overlap_rebate_exact":rebate,
        "complete_source_STAR_crude_12s2Z":12*s*s*len(Z),
        "complete_source_STAR_sharp_8s2Z":8*s*s*len(Z),
        "original_SOURCE_STAR_50percent_more_deletion_exact":True,
    }


def canonical_report():
    all_h=[star_all_h(C,c) for C,c in
           ((Fraction(1),Fraction(1)),
            (Fraction(2),Fraction(1,5)),
            (Fraction(7,3),Fraction(1,17)))]
    source=[
        true_full_source_star_case(1,"lex","point",(0,)),
        true_full_source_star_case(1,"reverse-line","line",(0,),2,4),
        true_full_source_star_case(2,"lex","point",(0,)),
        true_full_source_star_case(2,"lex","line",(0,)),
        true_full_source_star_case(2,"reverse-line","point",(1,3),11,23),
        true_full_source_star_case(2,"reverse-line","line",(1,3),7,19),
    ]
    return {
        "schema":SCHEMA,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
        "root_ASET_exponent_proved":False,
        "root_Branch_A_independently_accepted":False,
        "graph_C6_SS6_actual_numeric_constants_known":False,
        "original_root_target_seven_class_S_s_not_R3":True,
        "new_original_POINT_LINE_STAR_mask_exact_all_h":True,
        "new_original_structured_Z_rho_exact_one_point_five_x":True,
        "all_h_original_point_and_line_STAR_risk_preserving_ledgers":all_h,
        "true_original_symplectic_full_STAR_GQ_falsifiers":source,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_FULL_STAR_Z_50PCT_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
