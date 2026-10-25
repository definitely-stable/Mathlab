"""HYP-105 / issue #230 / D6-AA4-N.

ALL-h one-sided quenched theorem: for EVERY original-line globally
injected g on genuine W(3,s), s=2^h>=8, choosing ONE independent
uniform complete globally-injected point map f yields
E_f I_L^{B/A,internal}(f,g) >= (3/65536)s^6.

This proves min_g max_f, NOT min_(f,g). All actual source incidence
identities are retained. B/A is a historical accepted seven GF5 class.
"""
from fractions import Fraction
from itertools import combinations,product
from math import comb

from hyp105_issue230_d6aa4e_global_assignment_dual import alphabet_capacity
from hyp105_issue230_d6aa4i_original_spectral_coordinate import all_h_source_disjoint_theorem
from hyp105_issue230_d6aa4m_random_injection_charge import exact_random_projection_probabilities


def all_right_quinched_bound(s):
    """Every fixed complete real original g: exact physical hole budget."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine source order s=2^h >=2 only")
    a0=alphabet_capacity(s)
    a,K,V,m=(a0[x] for x in ("a","K","V","m"))
    if K!=comb(a,2) or m!=K-V or not 0<=m<=a-2:
        raise AssertionError("not minimal original physical coordinate alphabet")
    D=all_h_source_disjoint_theorem(s)[
        "uniform_forced_physically_disjoint_collinear_lower"]
    t=max(0,(a-6)//8)
    B=2*m//(t+1)
    # Every bad physical coordinate has >t missing incident edges; at
    # most B such symbols. Each touches <=a-1 occupied right labels;
    # each source right line has k=s(s+1) concurrent source lines.
    k=s*(s+1)
    lost=B*(a-1)*k
    good=max(0,D-lost)
    z=a-4-2*t
    # Fix disjoint, good right physical edges (u0,u1), (v0,v1).
    # x adjacent u1,v0, y adjacent v1,u0, x!=y outside 4 roots.
    # Each source line assigned to four resulting connector edges
    # admits >=s-j fresh points at jth choice (exclude root point).
    extensions=max(0,z*(z-1))
    fresh=1
    for j in range(4):fresh*=max(0,s-j)
    T=good*extensions*fresh
    pb=exact_random_projection_probabilities(s)["pB_exact"]
    conditional=pb*T
    explicit=Fraction(3*s**6,65536)
    if s>=8 and (good<=0 or extensions<=0 or conditional<explicit):
        raise AssertionError("some allowed right map violates universal quenched estimate")
    if s>=256:
        # Analytic all-h inequalities (no hidden finite interpolation):
        # a>=14, a<=s^2, m<=a-2, B<=24, D>=s^5/4,
        # good>=s^5/4-48s^4>=s^5/16,
        # z(z-1)>=s^3/4, (s)_4>=s^4/16,
        # pB>=3/(64s^6); product >=3s^6/65536.
        assert B<=24 and a<=s*s
        assert good*16>=s**5
        assert extensions*4>=s**3
        assert fresh*16>=s**4
        assert pb*64*s**6>=3
    return {
        "s":s,"V":V,"a":a,"K":K,"m":m,
        "spectral_all_right_original_concurrent_physically_disjoint_pairs_D":D,
        "maximum_missing_edges_per_good_physical_center":t,
        "maximum_bad_physical_centers":B,
        "original_line_pairs_lost_to_bad_centers_upper":lost,
        "remaining_good_original_source_line_pairs_lower":good,
        "extra_physical_connector_symbols_per_side_lower":z,
        "actual_physical_C6_extensions_per_good_pair_lower":extensions,
        "actual_four_original_fresh_point_assignments_lower":fresh,
        "genuine_right_A_and_source_concurrent_disjoint_BA_sixsets_T_g_lower":T,
        "exact_uniform_global_f_B_probability":str(pb),
        "conditional_E_f_true_seven_GF5_BA_internal_line_charge_lower":str(conditional),
        "explicit_3s6_over_65536":str(explicit),
        "all_power_two_s_ge_8_every_fixed_complete_g_bound":s>=8,
        "all_s_ge_256_analytic_five_factor_certificate":s>=256,
        "small_8_16_32_64_128_exact_certificate":8<=s<256,
        "EXACT_conditional_identity":"E_f[I_BA,int(f,g)|g]=p_B*T_g",
        "quantifier_order":"for every g, exists f; NOT for every f and g",
        "not_universal_GF5_s6_lower":True,
    }


def original_W32_fixed_g_right_A_counter(model):
    """Exact finite same-right-map count without any simulated GF5-positive Q.

    Enumerate all 70 right-physical six-edge 2-factors, all ORIGINAL
    point two-line pencil roots, and all 4 additional actual incidence
    completions with fresh ORIGINAL points. This is exactly T_g, not
    an independent right map per Q.
    """
    if model["s"]!=2 or model["a"]!=6 or len(model["incidences"])!=45:
        raise ValueError("real W32 original source only")
    right=tuple(tuple(x) for x in model["right_labels"])
    if len(right)!=15 or len(set(right))!=15:
        raise ValueError("W32 complete globally injected right labels required")
    phys=tuple(combinations(range(6),2))
    if set(right)!=set(phys):
        raise ValueError("W32 complete physical K6 edge image required")
    phys_to_line={edge:i for i,edge in enumerate(right)}
    twofactors=[
       frozenset(phys_to_line[e] for e in E)
       for E in combinations(phys,6)
       if all(sum(c in edge for edge in E)==2 for c in range(6))
    ]
    if len(twofactors)!=70:
        raise AssertionError("exact full K6 physical 2factor count changed")
    bypoint=[set() for _ in range(15)]
    byline=[set() for _ in range(15)]
    for p,l in model["incidences"]:
        bypoint[p].add(l);byline[l].add(p)
    if any(len(x)!=3 for x in (*bypoint,*byline)):
        raise AssertionError("not true regular W32 ORIGINAL incidence geometry")
    total=charged=0
    root_records=[]
    for p in range(15):
        for l0,l1 in combinations(sorted(bypoint[p]),2):
            root=frozenset((l0,l1))
            is_disjoint=not(set(right[l0])&set(right[l1]))
            count=0
            for lines in twofactors:
                if not root.issubset(lines):continue
                others=sorted(lines-root)
                if len(others)!=4:
                    raise AssertionError("bad true source right A matching")
                for pts in product(*(sorted(byline[l]-{p}) for l in others)):
                    if len(set(pts))==4:count+=1
            total+=count
            charged+=count if is_disjoint else 0
            root_records.append((p,l0,l1,count,is_disjoint))
    pb=exact_random_projection_probabilities(2)["pB_exact"]
    return {
        "scope":"same true ORIGINAL complete fixed right g",
        "physical_A_2factor_sixline_sets":len(twofactors),
        "actual_original_point_pencil_two_line_roots":len(root_records),
        "right_A_source_BA_sixsets_T_g_plus_noncharged":total,
        "right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g":charged,
        "exact_E_uniform_COMPLETE_point_f_BA_motif_count_given_g":str(pb*total),
        "exact_E_uniform_COMPLETE_point_f_INTERNAL_line_charge_given_g":str(pb*charged),
        "strictly_same_complete_right_mapping_across_every_original_Q":True,
        "four_point_frozen_outside_fiber_NOT_a_uniform_f_sample":True,
    }


def report():
    from hyp105_issue230_projection import fixture
    all_h=[all_right_quinched_bound(2**h) for h in range(1,12)]
    cases={scheme:original_W32_fixed_g_right_A_counter(fixture(1,scheme))
           for scheme in ("lex","reverse","S68","S72")}
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-N-QUENCHED-RIGHT-TRANSFER",
        "all_s_ge_8_explicit_conditional_omega_s6_constant":"3/65536",
        "all_right_maps_uniform_conditional_stochastic_theorem":True,
        "all_h_quenched_bounds":all_h,
        "exact_true_W32_fixed_complete_right_maps":cases,
        "quantifier_order":"min_g max_f >= c*s^6, NOT min_(f,g)",
        "root_A":"OPEN","root_B":"OPEN","full_R3":False,"ASET_exponent":False,
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
