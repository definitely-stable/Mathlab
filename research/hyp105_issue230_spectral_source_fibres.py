"""EICE-003-H: exact original incidence spectral 'double physical-star' fibres.

H1: for true GQ W(3,s), C=BB^T obeys C^2-2s C=(s+1)J.
H2: every four-outer-source five-incidence blocked plaquette with
middle ORIGINAL incidence e lies in the true point-line double
physical-pair overlap fibre F_e. Expander mixing gives |F_e|=O(s²).
H3: all-h CONDITIONAL heavy-middle-source criterion from EICE-003-G G4
and F5/F6: if theta_I>=epsilon>0 then some middle original incidence
supports Omega_epsilon(s^4) distinct blocked original five-source sets.
The fibre cap alone DOES NOT rule this out.
H4: exhaustive finite TRUE W32/W34 source-family + fibre diagnostic.

NO universal o(s^4) bound, no GF5 positive sixset transfer or Branch A.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, isqrt
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_five_source_blocked_search import (
    FiveSourceSearch, conditional_all_h_distinct_five_source_lower,
)


def exact_incidence_spectral_polynomial(ctx):
    """Full integer W(3,s) incidence biadjacency proof falsifier.

    B B^T has diagonal s+1, offdiagonal 1 iff two TRUE original
    points are collinear. Check (B B^T)^2-2s B B^T=(s+1)J.
    """
    s,V=ctx.s,ctx.v
    rows=ctx.point_lines
    C=[[s+1 if p==q else int(bool(rows[p]&rows[q]))
         for q in range(V)] for p in range(V)]
    for p in range(V):
        for q in range(V):
            squared=sum(C[p][k]*C[k][q] for k in range(V))
            if squared-2*s*C[p][q]!=s+1:
                raise AssertionError('H1 TRUE original GQ spectral polynomial failed')
    return dict(
        original_point_count=V, original_line_count=V,
        verified_integer_polynomial='(B B^T)^2 - 2s B B^T = (s+1) J',
        trivial_incidence_singular_value=s+1,
        nontrivial_incidence_singular_value_squared=2*s,
        zero_eigenspace_allowed=True,
        all_V_squared_entries_checked=V*V,
    )


def source_forest_signature(ctx, ids):
    """Any <=7 actual ORIGINAL W(3,s) incidence edges induce a forest.

    Nonempty five-source footprint is a forest because girth>=8.
    """
    ids=tuple(sorted(ids))
    if len(ids)!=len(set(ids)) or not ids:
        raise ValueError('unique nonempty TRUE original source IDs required')
    points=Counter()
    lines=Counter()
    graph=defaultdict(set)
    for i in ids:
        if type(i) is not int or not (0<=i<ctx.N):
            raise ValueError('invalid true original incidence source ID')
        p,l=ctx.inc[i]
        points[p]+=1
        lines[l]+=1
        graph[('p',p)].add(('l',l))
        graph[('l',l)].add(('p',p))
    if len(ids)<8:
        unseen=set(graph)
        components=0
        while unseen:
            components+=1
            start=unseen.pop()
            stack=[start]
            while stack:
                for nxt in graph[stack.pop()]:
                    if nxt in unseen:
                        unseen.remove(nxt)
                        stack.append(nxt)
        if len(ids)!=len(graph)-components:
            raise AssertionError('H2 source GQ girth8 five-incidence forest violated')
    else:
        components=None
    return dict(edge_count=len(ids),original_point_count=len(points),
                original_line_count=len(lines),
                original_components=components,
                original_point_degree_sequence=tuple(sorted(points.values(),reverse=True)),
                original_line_degree_sequence=tuple(sorted(lines.values(),reverse=True)),
                acyclic_original_forest=len(ids)<8)


def exact_middle_double_star_fibre(ctx, e):
    """TRUE e=(p2,l2) double physical-star source coincidence set.

    An original e'=(p,l) is eligible iff f(p) meets f(p2) AND
    g(l) meets g(l2). This equals the set of source incidences
    with at least one of their four physical diagonal endpoints
    in the 2x2 coordinate corner grid f(p2) x g(l2).
    """
    if type(e) is not int or not 0<=e<ctx.N:
        raise ValueError('true middle ORIGINAL source incidence required')
    p2,l2=ctx.inc[e]
    fp2=set(ctx.f[p2])
    gl2=set(ctx.g[l2])
    P={p for p in range(ctx.v) if fp2.intersection(ctx.f[p])}
    L={l for l in range(ctx.v) if gl2.intersection(ctx.g[l])}
    band={i for i,(p,l) in enumerate(ctx.inc) if p in P and l in L}
    if e not in band:
        raise AssertionError('middle ORIGINAL source absent from own fibre')
    if len(P)>2*ctx.a-3 or len(L)>2*ctx.a-3:
        raise AssertionError('minimal injective K_a pair-star bound broken')
    corners={x*ctx.a+y for x in fp2 for y in gl2}
    by_physical=set()
    for i,(p,l) in enumerate(ctx.inc):
        xs=ctx.f[p]
        ys=ctx.g[l]
        endpoint_set={x*ctx.a+y for x in xs for y in ys}
        if corners&endpoint_set:
            by_physical.add(i)
    if by_physical!=band:
        raise AssertionError('H2 TRUE ORIGINAL double-star is not paired-diagonal corner band')
    x,y=len(P),len(L)
    # Exact biregular bipartite incidence expander mixing:
    # (E V - (s+1)xy)^2 <= 2s x(V-x)y(V-y)
    V=ctx.v
    observed=len(band)
    deviation=observed*V-(ctx.s+1)*x*y
    spectral_squared=2*ctx.s*x*(V-x)*y*(V-y)
    if deviation*deviation>spectral_squared:
        raise AssertionError('H1/H2 exact integer TRUE GQ spectral mixing violated')
    root=isqrt(spectral_squared)
    if root*root<spectral_squared:
        root+=1
    spectral_upper=((ctx.s+1)*x*y+root)//V
    if observed>spectral_upper:
        raise AssertionError('H2 exact integer spectral upper failed')
    # An independent exact witness identity uses the original line pencils.
    by_line_pencil=sum(len(ctx.line_points[l]&P) for l in L)
    if by_line_pencil!=observed:
        raise AssertionError('H2 independent original line-point fibre census failed')
    return dict(
        e=e,
        original_middle_incidence=(p2,l2),
        physical_coordinate_corner_count=len(corners),
        true_original_point_star_size=x,
        true_original_line_star_size=y,
        original_double_star_incidence_count=observed,
        original_double_star_incidence_ids=tuple(sorted(band)),
        original_point_star_ids=tuple(sorted(P)),
        original_line_star_ids=tuple(sorted(L)),
        exact_integer_expander_mixing_lhs=deviation*deviation,
        exact_integer_expander_mixing_rhs=spectral_squared,
        original_spectral_upper_floor=spectral_upper,
        independent_original_line_pencil_count=by_line_pencil,
        source_star_capacity_spectrum_valid=True,
        unconditional_positive_GF5_sixset_transfer_proved=False,
    )


def necessary_heavy_middle_five_source(s,theta):
    """H3: some original midpoint supports >= reservoir / N families.

    Counts ORIGINAL five-source sets with a genuine recorded middle, not
    arbitrary subsets. Requires the same valid all-h EICE-002 physical
    coherent stationary G* and theta. Does not prove upper incompatibility.
    """
    data=conditional_all_h_distinct_five_source_lower(s,theta)
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    return dict(
        s=s,theta=str(Fraction(theta)),true_original_incidence_count=N,
        heavy_middle_distinct_five_family_count_lower=str(
            Fraction(data["distinct_true_original_five_incidence_sets_lower"])/N),
        possible_middle_ids_per_five_source_at_most=5,
        proof_by_assigning_each_true_five_source_family_one_realized_middle=True,
        prerequisite_same_map_EICE002_F5_F6_G4=True,
        proposed_uniform_o_s4_middle_source_upper_proved=False,
        root_Branch_A_proved=False,
    )


def finite_fibre_and_family_report(model, *, exact_polynomial=True,
                                   max_paths=3_000_000):
    ctx=EndpointEnergy(model)
    polynomial=exact_incidence_spectral_polynomial(ctx) if exact_polynomial else None
    full=FiveSourceSearch(model).census(
        max_physical_nb3_cells=max_paths,
        export_true_five_source_families=True,
        independent_witness_oracle=True)
    families=full.pop("TRUE_ORIGINAL_five_source_families")
    if len(families)!=full["distinct_original_five_incidence_blocked_source_families"]:
        raise AssertionError('H3 complete TRUE source-family export mismatch')
    if any(len(f['original_incidence_ids'])!=5 for f in families):
        raise AssertionError('H3 exported blocked ORIGINAL source family not five IDs')
    fibre_cache={}
    middle_counts=Counter()
    role_counts=Counter()
    middle_four_arm_sets=defaultdict(set)
    profile_counts=Counter()
    max_possible_four=0
    for fam in families:
        ids=tuple(fam["original_incidence_ids"])
        fs=source_forest_signature(ctx,ids)
        profile=(fs["original_point_degree_sequence"],
                 fs["original_line_degree_sequence"],
                 fs["original_components"])
        profile_counts[str(profile)]+=1
        for e in fam["original_middle_source_ids"]:
            if e not in ids:
                raise AssertionError('H3 realized middle source outside true five family')
            if e not in fibre_cache:
                fibre_cache[e]=exact_middle_double_star_fibre(ctx,e)
            band=set(fibre_cache[e]["original_double_star_incidence_ids"])
            if not set(ids).issubset(band):
                raise AssertionError('H2 every 5-source arm must lie in middle double star')
            middle_counts[e]+=1
            for other in ids:
                if other!=e:
                    role_counts[other]+=1
            middle_four_arm_sets[e].add(tuple(i for i in ids if i!=e))
            max_possible_four=max(max_possible_four,
                comb(len(band)-1,4) if len(band)>=5 else 0)
    if sum(middle_counts.values())<len(families):
        raise AssertionError('H3 original middle source coverage lost')
    if sum(middle_counts.values())!=sum(len(f['original_middle_source_ids'])
                                       for f in families):
        raise AssertionError('H3 true source-middle family incidence mismatched')
    if any(len(v)!=middle_counts[e] for e,v in middle_four_arm_sets.items()):
        raise AssertionError('H3 deduplicated source-middle quadruples disagree')
    all_fibres=[exact_middle_double_star_fibre(ctx,e) for e in range(ctx.N)]
    full_capacity=max(x["original_double_star_incidence_count"] for x in all_fibres)
    max_used=max((x["original_double_star_incidence_count"] for x in fibre_cache.values()),
                 default=0)
    return {
        "scope":"Finite globally injected TRUE W(3,s) source maps; no all-h extrapolation",
        "s":ctx.s,"a":ctx.a,"V":ctx.v,"N":ctx.N,
        "source_gq_polynomial_verified":polynomial,
        "exhaustive_original_middle_orientations":full[
            "oriented_middle_edges_examined"],
        "source_families_distinct":len(families),
        "oriented_true_four_blocked_squares":full[
            "locally_coherent_allfour_original_plaquettes"],
        "mask_channels":full["locally_coherent_blocking_channels"],
        "distinct_middle_sources_with_blocked_families":len(middle_counts),
        "maximum_distinct_five_families_per_middle_original_incidence":max(
            middle_counts.values(),default=0),
        "mean_five_families_per_ALL_original_middle_incidence":str(
            Fraction(sum(middle_counts.values()),ctx.N)),
        "top_10_middle_original_sources":middle_counts.most_common(10),
        "max_spectral_source_fibre_size_ALL_true_middle_incidences":full_capacity,
        "max_spectral_source_fibre_size_used_by_blocked_family":max_used,
        "max_comb_four_arm_capacity_per_used_middle":max_possible_four,
        "source_forest_profiles":dict(sorted(profile_counts.items())),
        "top_10_shared_outer_original_source_ids":role_counts.most_common(10),
        "empirical_middle_fibre_uniform_o_s4_cap_proved":False,
        "universal_GF5_sixset_transfer_proved":False,
        "root_Branch_A_proved":False,
    }


def report():
    from hyp105_issue230_projection import fixture
    out=[]
    for scheme in ("lex","reverse","S68","S72"):
        data=finite_fibre_and_family_report(fixture(1,scheme))
        data["scheme"]=scheme
        out.append(data)
    for scheme in ("lex","random"):
        data=finite_fibre_and_family_report(fixture(2,scheme))
        data["scheme"]=scheme
        out.append(data)
    return {"status":"RESTRICTED_THEOREM_H","root_A":"OPEN","maps":out}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
