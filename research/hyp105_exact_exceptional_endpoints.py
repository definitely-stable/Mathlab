"""HYP-105 AA4-EXCEND: exact original endpoint partition and 21*s^5 cap.

EVERY dyadic s=2^h>=64, complete fixed arbitrarily correlated global
injections f,g into the SAME minimal physical K_a-pair alphabet:
 M=binom(a,2), V=(s+1)(s^2+1), N=V(s+1),
 Omega={actual ORIGINAL nonincident point q, line r pairs},
 BL,BR are the original GQ end-bad projection populations,
 J=|BL intersection BR|.

Consider ALL ORDERED physical endpoint pairs
 (v0=(x,y),v3=(z,w)) with x!=z,y!=w. Exact disjoint partition:
 missing physical pair labels      = 4*(M*M-V*V)
 occupied but ORIGINAL incident    = 4*N
 original nonincident end-bad      = 4*(2*s*(Mf+Mg)-J)
 remaining original nonincident good = 4*(V*(V-s-1)
                                         -2*s*(Mf+Mg)+J).
TOTAL = 4*M*M. The first three populations are the exact
exceptional endpoint universe, even for COMPLETELY correlated f,g.

Previous #672 union used <=64*s^5. New independent all-h cap
  E_exc <= 4*(M*M-V*V)+4*N+16*s*C_s <=21*s^5
for ALL dyadic s>=64 (proof in corresponding manuscript).
The original/source bad-projection overlap J is NEVER assumed zero.
This is a strict two-sided physical pair occupancy union count, not
an iid or source-random endpoint claim.

With exact #679 selector, #680 sixth moment and #681 improved improper
paths, the exact exceptional weighted-path inequality becomes:
   P3_mass_on_exceptional <=sqrt(21)*sigma3^-1*sqrt(L6)*s^(11/2).
No path-frequency uniformity or independence is assumed.
We give an explicit *sufficient* integer s0 bound for the already-
stated Branch A proof conditional on its OTHER existing lemmas; no
qualified external acceptance or changes to ancestors are implied.

W32/W34 source-first and independent physical-endpoint-first finite
oracles check the partition and every original source GQ projection.
"""

from collections import Counter
from itertools import combinations, product
from math import comb, isqrt


def _min_a_for_V(V):
    if type(V) is not int or V<1:
        raise ValueError("V positive integer")
    a=(1+isqrt(1+8*V))//2
    while a*(a-1)//2<V:a+=1
    if (a-1)*(a-2)//2>=V:
        raise AssertionError("physical alphabet nonminimal")
    return a


def _ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative integer")
    x=isqrt(n)
    return x+(x*x<n)


def allh_exact_exceptional_envelope(s):
    """Analytic all-h 21s5 upper from *minimal* physical alphabet.

    No source GQ enumeration at high h. Enforces dyadic s>=64. All
    comparisons are exact integers. Mathematical all-h argument in
    manuscript; dyadic ladder tests are only implementation controls.
    """
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("dyadic s>=64 required")
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    a=_min_a_for_V(V)
    M=comb(a,2)
    Cs=(s*s+1)*(s*s+a-2)
    missing=4*(M*M-V*V)
    incident=4*N
    endbad_upper=16*s*Cs
    bound=missing+incident+endbad_upper
    if not (M>=V and M-V<a-1):
        raise AssertionError("minimal physical alpha occupancy fact wrong")
    # All-h trial alphabet a<=ceil(3s sqrt(s)/2):
    # binom(ceil(t),2) >= (9/8)s^3-(3/4)s sqrt(s) >=V.
    # Since a is integer, a<=t+1 and s sqrt(s)>=512:
    # a <= (97/64)*s*sqrt(s). Check without floating point.
    if (64*a)**2>(97*s)**2*s:
        raise AssertionError("all-h a<=97s sqrt(s)/64 bound failed")
    if bound>21*s**5:
        raise AssertionError("uniform 21s^5 exceptional endpoint cap failed")
    return {
        "s":s,"a":a,"V":V,"N":N,"M":M,"Cs":Cs,
        "missing_physical_pairs_exact":missing,
        "original_incident_pairs_exact":incident,
        "original_endbad_pairs_upper":endbad_upper,
        "new_exceptional_population_upper":bound,
        "all_h_uniform_exceptional_cap":21*s**5,
        "old_672_uniform_exceptional_cap":64*s**5,
        "new_21_over_old_64_ratio":"21/64",
        "combinatorial_all_h_proof_required_not_finite_extrapolation":True,
    }


def finite_true_original_endpoint_partition(power,f,g):
    """TRUE ORIGINAL W32/W34: SOURCE-FIRST disjoint endpoint partition.

    Enumerates all original q,r with genuine q--ell--p--r projection;
    independent of physical endpoint loops and precomputed results.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_physical_degree_energy import minimal_alphabet,_verify_typed_injections
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite genuine source W32/W34 only")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    point_books=[[0]*a for _ in range(V)]
    line_books=[[0]*a for _ in range(V)]
    for p,ell in flags:
        pencils[p].add(ell)
        through[ell].add(p)
        for y in g[ell]:point_books[p][y]+=1
        for x in f[p]:line_books[ell][x]+=1
    Mf=sum(comb(n,2) for row in line_books for n in row)
    Mg=sum(comb(n,2) for row in point_books for n in row)
    collinear=[set().union(*(through[ell] for ell in pencils[p]))-{p}
               for p in range(V)]
    fsets=tuple(map(set,f));gsets=tuple(map(set,g))
    counters=Counter()
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:
                counters["incident_source"]+=1
                continue
            projection=collinear[q]&through[r]
            if len(projection)!=1:
                raise AssertionError("original GQ nonincident projection nonunique")
            p=next(iter(projection))
            ell=pencils[q]&pencils[p]
            if len(ell)!=1:
                raise AssertionError("original GQ projection intermediate source line invalid")
            ell=next(iter(ell))
            L=bool(fsets[q]&fsets[p])
            R=bool(gsets[r]&gsets[ell])
            counters["nonincident_source"]+=1
            counters["bad_left_source"]+=L
            counters["bad_right_source"]+=R
            counters["bad_both_source"]+=L and R
            counters["bad_union_source"]+=L or R
            counters["good_source"]+=not(L or R)
    if counters["bad_left_source"]!=2*s*Mf or (
        counters["bad_right_source"]!=2*s*Mg):
        raise AssertionError("independent original point/line collision books disagree")
    if counters["incident_source"]!=len(flags) or (
        counters["nonincident_source"]!=V*V-len(flags)):
        raise AssertionError("complete original source q,r population invalid")
    M=comb(a,2)
    parts={
        "missing_physical":4*(M*M-V*V),
        "original_incident":4*len(flags),
        "original_nonincident_endbad":4*counters["bad_union_source"],
        "original_nonincident_good":4*counters["good_source"],
    }
    if sum(parts.values())!=4*M*M:
        raise AssertionError("all ordered physical endpoint universe not partitioned")
    if (parts["original_nonincident_endbad"]!=
        4*(2*s*(Mf+Mg)-counters["bad_both_source"])):
        raise AssertionError("bad ORIGINAL endpoint intersection included incorrectly")
    return {
        "s":s,"V":V,"a":a,"M":M,"N":len(flags),
        "M_f_FULL":Mf,"M_g_FULL":Mg,
        "original_bad_left":counters["bad_left_source"],
        "original_bad_right":counters["bad_right_source"],
        "original_bad_intersection_J":counters["bad_both_source"],
        "original_bad_union":counters["bad_union_source"],
        "source_first_four_way_endpoint_partition":parts,
        "source_first_total_ordered_distinct_coordinate_pairs":4*M*M,
        "no_statistical_or_path_endpoint_uniformity_assumed":True,
    }


def finite_independent_physical_endpoint_partition(power,f,g):
    """PHYSICAL-FIRST every ordered (v0,v3) for x!=z,y!=w.

    Builds f^-1,g^-1 from physical simple K_a labels; classifies the
    4M² oriented pairs without source book populations. Original
    projections are reconstructed solely from incidence geometry.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_physical_degree_energy import minimal_alphabet,_verify_typed_injections
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite true W32/W34 only")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    invf={frozenset(edge):p for p,edge in enumerate(f)}
    invg={frozenset(edge):ell for ell,edge in enumerate(g)}
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    for p,ell in flags:
        pencils[p].add(ell)
        through[ell].add(p)
    C=[set().union(*(through[ell] for ell in pencils[p]))-{p}
       for p in range(V)]
    fsets=tuple(map(set,f));gsets=tuple(map(set,g))
    counts=Counter()
    for x in range(a):
        for z in range(a):
            if x==z:continue
            q=invf.get(frozenset((x,z)))
            for y in range(a):
                for w in range(a):
                    if y==w:continue
                    r=invg.get(frozenset((y,w)))
                    if q is None or r is None:
                        counts["missing_physical"]+=1
                    elif r in pencils[q]:
                        counts["original_incident"]+=1
                    else:
                        projected=C[q]&through[r]
                        if len(projected)!=1:
                            raise AssertionError("independent physical-original projection broken")
                        p=next(iter(projected))
                        mid=pencils[q]&pencils[p]
                        if len(mid)!=1:
                            raise AssertionError("physical-first GQ anchor line nonunique")
                        ell=next(iter(mid))
                        if fsets[q]&fsets[p] or gsets[r]&gsets[ell]:
                            counts["original_nonincident_endbad"]+=1
                        else:
                            counts["original_nonincident_good"]+=1
    if sum(counts.values())!=4*comb(a,2)**2:
        raise AssertionError("physical-first all ordered endpoint pairs undercounted")
    # Every class must exist as a zero-inclusive slot: at W(3,2)
    # minimal K_6 is fully occupied (M=V=15), so missing=0.
    return {key:counts[key] for key in (
        "missing_physical","original_incident",
        "original_nonincident_endbad","original_nonincident_good")}


def finite_genuine_core_path_endpoint_mass(power,f,g,core_ids=None):
    """Original retained source physical graph; direct proper 3walk endpoint mass.

    Important: exact source-universe size is UNWEIGHTED. Prove the
    weighted bound by Cauchy, without replacing mass by fraction.
    """
    from hyp105_full_physical_degree_tail import genuine_source,physical
    from hyp105_physical_degree_energy import minimal_alphabet,_verify_typed_injections
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite real original W32/W34 only")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    ids=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if len(set(ids))!=len(ids) or any(type(i) is not int or i<0 or i>=len(flags)
                                      for i in ids):
        raise ValueError("genuine distinct original core IDs required")
    graph,_=physical(ids,flags,f,g)
    flookup={frozenset(z):p for p,z in enumerate(f)}
    glookup={frozenset(z):r for r,z in enumerate(g)}
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    for p,ell in flags:pencils[p].add(ell);through[ell].add(p)
    collinear=[set().union(*(through[l] for l in pencils[p]))-{p}
               for p in range(V)]
    fsets=tuple(map(set,f));gsets=tuple(map(set,g))
    endpoint_weights=Counter()
    for v0 in graph:
        for v1 in graph[v0]:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    corners=(v0,v1,v2,v3)
                    if len({v[0] for v in corners})==4 and (
                        len({v[1] for v in corners})==4):
                        endpoint_weights[(v0,v3)]+=1
    masses=Counter()
    for ((x,y),(z,w)),weight in endpoint_weights.items():
        q=flookup.get(frozenset((x,z)))
        r=glookup.get(frozenset((y,w)))
        if q is None or r is None:
            klass="missing_physical"
        elif r in pencils[q]:
            klass="original_incident"
        else:
            project=collinear[q]&through[r]
            if len(project)!=1:
                raise AssertionError("core proper path genuine projection nonunique")
            p=next(iter(project))
            ell=next(iter(pencils[p]&pencils[q]))
            klass=("original_nonincident_endbad" if (
                fsets[q]&fsets[p] or gsets[r]&gsets[ell]
            ) else "original_nonincident_good")
        masses[klass]+=weight
    universe=finite_true_original_endpoint_partition(power,f,g)[
        "source_first_four_way_endpoint_partition"]
    E=universe["missing_physical"]+universe["original_incident"]+(
        universe["original_nonincident_endbad"])
    badmass=sum(masses[k] for k in (
        "missing_physical","original_incident","original_nonincident_endbad"))
    Frobenius=sum(x*x for x in endpoint_weights.values())
    if badmass*badmass>E*Frobenius:
        raise AssertionError("Cauchy bound on weighted exceptional 3paths false")
    return {
        "s":s,"original_core_flags":len(ids),
        "physical_proper_path_total":sum(masses.values()),
        "physical_exceptional_path_weight":badmass,
        "physical_endpoint_proper_Frobenius_squared":Frobenius,
        "exact_unweighted_exceptional_endpoint_universe":E,
        "explicit_Cauchy_integer_inequality_verified":True,
        "path_weight_is_NOT_assumed_uniform_in_original_source_pairs":True,
        "physical_endpoint_weight_by_four_classes":dict(masses),
    }


def recomputed_allh_dense_branch_s0(K,T):
    """Safe integer all-h sufficient threshold incorporating #679--#681.

    T is an INTEGER >=1 chosen at least as large as the exact parent
    tail constant (possibly by ceiling); K is the same source conflict
    maximum degree. The mathematical parent tail and original D6
    dichotomy remain assumed; this is not an independent proof of them.
    ceil_sqrt bounds all irrational intermediate constants from ABOVE.
    """
    if type(K) is not int or K<0 or type(T) is not int or T<1:
        raise ValueError("K>=0 integer, T>=1 integer required")
    sigma2_inv=16*(K+1)**2
    sigma3_inv=64*(K+1)**3
    L6=24+288*T*T
    L4upper=2*sigma2_inv**2*_ceil_sqrt(8*L6)+40*T
    B0upper=64*_ceil_sqrt((K+1)*T)
    E2=21*sigma3_inv**2*L6  # new L_E^2, not old 64*... squared.
    thresholds={
        "parent_and_exceptional_geometric_min":64,
        "new_improper_three_loss":816*T,
        "new_exceptional_weighted_loss":144*E2,
        "new_internal_mixed_blocker_loss":
            48**8*(B0upper*T*L4upper)**4,
    }
    s0=max(thresholds.values())
    return {
        "K":K,"T":T,
        "new_L6":L6,
        "new_sigma2_inv":sigma2_inv,
        "new_sigma3_inv":sigma3_inv,
        "new_L4_integer_upper":L4upper,
        "conservative_B0_integer_upper":B0upper,
        "new_exceptional_LE_squared":E2,
        "exact_safe_s0_conservative_integer":s0,
        "exact_s0_threshold_components":thresholds,
        "total_good_BBo_lower_for_s_ge_s0":"s^6/8 under parent tail/core inputs",
        "all_source_f_g_quantifiers_preserved":True,
        "s0_requires_original_parent_tail_input_C_c":True,
        "no_external_peer_review_or_root_acceptance":True,
    }
