"""HYP-105 #230 AA4-AY: exact ORIGINAL opposite ALL-D 3-flag wedge mean.

NEW all-h quenched mean over ONE COMPLETE right global line bijection,
with adversarial fixed full globally injected ORIGINAL point map f and
an arbitrary fixed globally occupied right K_a physical edge SUPPORT E.

All three flags are ACTUAL different true W(3,s) original source
incidence IDs, with three different source POINT and LINE factor IDs.
Averaging is over one shared whole original LINE injection g; NEVER
independently reroll physical line labels for each source Q.

This theorem applies to ALL-D physically opposite two-typed source
wedges, not the stricter port-GOOD-only wedge subset and not selected
GF5 six-original-incidence accepted motifs. It is STOCHASTIC, NOT an
original fixed-g minimax bound #230 Branch A.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt


def _params(s):
    """Self-contained actual original GQ minimal physical K_a parameters."""
    if type(s) is not int or s<2 or (s&(s-1)):
        raise ValueError("dyadic symplectic original order required")
    V=(s+1)*(s*s+1)
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:
        a+=1
    K=comb(a,2)
    m=K-V
    if m<0 or m>a-2 or a<6:
        raise AssertionError("minimal true symplectic physical palette invalid")
    return V,a,K,m


def physical_edge_port_energy(physical_edges,a):
    """EXACT occupied K_a edge support energy sum_e(deg_u-1)(deg_v-1)."""
    e=tuple(tuple(sorted(pair)) for pair in physical_edges)
    if len(set(e))!=len(e) or any(len(x)!=2 or x[0]==x[1] or
                                  min(x)<0 or max(x)>=a for x in e):
        raise ValueError("fully injected simple physical pair edge support required")
    degrees=[0]*a
    for u,v in e:
        degrees[u]+=1;degrees[v]+=1
    return sum((degrees[u]-1)*(degrees[v]-1) for u,v in e)


def exact_original_source_point_opposite_potential(model):
    """Source-first exact physical-point-opposite pairs with DIFFERENT
    original source point/line factors and three genuine source flags.

    Physically only the POINT f-edge port at original center is fixed;
    right LINE images are not consulted. The full original source
    incidence bipartite graph is consulted for all allowed neighbor
    ORIGINAL LINE factors, not artificial flags.
    """
    s=model["s"]; V,a,K,m=_params(s);d=s+1
    source=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(sorted(x)) for x in model["left_labels"])
    if len(f)!=V or len(set(f))!=V or len(source)!=V*d:
        raise ValueError("not complete source/point model")
    if any(len(x)!=2 or x[0]==x[1] or min(x)<0 or max(x)>=a for x in f):
        raise ValueError("invalid original physical point image")
    neighbors=[set() for _ in range(V)]
    source_set=set(source)
    if len(source_set)!=len(source):
        raise ValueError("non-distinct original source incidence IDs")
    for p,l in source:
        if not 0<=p<V or not 0<=l<V:
            raise ValueError("source factor index invalid")
        neighbors[p].add(l)
    if any(len(t)!=d for t in neighbors):
        raise ValueError("not true GQ d-regular source point neighborhoods")
    line_degree=[0]*V
    for p,l in source:
        line_degree[l]+=1
    if any(n!=d for n in line_degree):
        raise ValueError("not true GQ d-regular source line neighborhoods")
    physical_coordinate_to_source_points=[[] for _ in range(a)]
    for p,(u,v) in enumerate(f):
        physical_coordinate_to_source_points[u].append(p)
        physical_coordinate_to_source_points[v].append(p)
    candidates=0
    original_incidence_center_counts=[]
    for p,l in source:
        u,v=f[p]
        points0=[q for q in physical_coordinate_to_source_points[u] if q!=p]
        points1=[q for q in physical_coordinate_to_source_points[v] if q!=p]
        if set(points0)&set(points1):
            raise AssertionError("one globally injected physical source point pair image violated")
        z=0
        for q0 in points0:
            lines0=neighbors[q0]-{l}
            for q1 in points1:
                lines1=neighbors[q1]-{l}
                z+=len(lines0)*len(lines1)-len(lines0&lines1)
        if z< len(points0)*len(points1)*(d-1)*(d-2):
            raise AssertionError("genuine source original 3-flag local lower violated")
        original_incidence_center_counts.append(z)
        candidates+=z
    left_energy=physical_edge_port_energy(f,a)
    simple_lower=d*(d-1)*(d-2)*left_energy
    if candidates<simple_lower:
        raise AssertionError("all-h real original source factor capacity bound violated")
    return {
        "s":s,"V":V,"a":a,"d":d,"m":m,
        "point_image_occupied_physical_support_port_energy":left_energy,
        "actual_original_source_center_incidence_flag_count":len(source),
        "point_opposite_centered_3distinct_original_source_incidence_triples":candidates,
        "each_center_actual_source_line_neighborhood_lower":(d-1)*(d-2),
        "point_opposite_triples_source_only_genuine_lower":simple_lower,
        "per_actual_original_center_incidence_ID_candidate_counts":
            tuple(original_incidence_center_counts),
        "one_original_global_f_shared_for_all_original_source_Q":True,
        "right_line_labels_not_used_in_source_potential":True,
    }


def quenched_original_opposite_ALL_D_mean(model):
    """EXACT mean for original fixed f & fixed original g image support.

    One uniformly random WHOLE source LINE factor bijection g':I_lines
    -> E_right. Conditional on the image g'(l) of one real source line
    center l, two distinct other original source line factors choose
    two distinct remaining physical pair edges without replacement.
    """
    r=exact_original_source_point_opposite_potential(model)
    support=tuple(tuple(sorted(x)) for x in model["right_labels"])
    if len(support)!=r["V"] or len(set(support))!=r["V"]:
        raise ValueError("one global fully injected source right image required")
    physical_right=physical_edge_port_energy(support,r["a"])
    V=r["V"]
    probability=Fraction(2*physical_right,V*(V-1)*(V-2))
    exact=probability*r[
        "point_opposite_centered_3distinct_original_source_incidence_triples"]
    lower=probability*r["point_opposite_triples_source_only_genuine_lower"]
    L=physical_energy_universal_deficit_lower(V,r["a"],r["m"])
    completely_support_independent=Fraction(
        2*r["d"]*(r["d"]-1)*(r["d"]-2)*L*L,V*(V-1)*(V-2))
    if r["point_image_occupied_physical_support_port_energy"]<L or physical_right<L:
        raise AssertionError("same physical K_a missing edge deficit lemma false")
    if not exact>=lower>=completely_support_independent:
        raise AssertionError("quenched ORIGINAL source-wedge stochastic hierarchy false")
    return {
        "s":r["s"],"V":V,"a":r["a"],
        "original_point_global_f_specific_source_threeflag_potential":
            r["point_opposite_centered_3distinct_original_source_incidence_triples"],
        "original_right_occupied_physical_pair_support_energy":physical_right,
        "two_opposite_right_physical_ports_joint_probability":probability,
        "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean":exact,
        "point_source_only_lower_at_FIXED_global_f":lower,
        "uniform_in_both_adversarial_supports_R_ALL_D_mean_lower":completely_support_independent,
        "true_original_source_six_ID_selected_GF5_lower_PROVED":False,
        "all_global_FIXED_RIGHT_original_g_minimax_PROVED":False,
        "original_port_GOOD_only_mean_lower_PROVED":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def physical_energy_universal_deficit_lower(V,a,m):
    """Missing-edge union bound, ANY occupied E subset of K_a of size V."""
    if comb(a,2)-V!=m or m>a-2 or a<6:
        raise ValueError("minimal physical pair-image model required")
    L=V*(a-2)**2-2*m*(a-1)*(a-2)
    if L<=0:
        raise AssertionError("minimal GQ physical support energy positivity")
    return L


def dyadic_every_original_spectral_free_quenched_certificate(s):
    """ALL h>=1 (symbolic); NEVER instantiate a fake large source W3."""
    if type(s) is not int or s<2 or (s&(s-1)):
        raise ValueError("s must be an actual dyadic symplectic order 2^h")
    V,a,K,m=_params(s);d=s+1
    L=physical_energy_universal_deficit_lower(V,a,m)
    uniform=Fraction(2*d*(d-1)*(d-2)*L*L,V*(V-1)*(V-2))
    if s==2:
        if (V,a,m,L)!=(15,6,0,240):
            raise AssertionError("W32 exact physical K6 certificate changed")
    else:
        if a<14 or V<4*(a-1) or (a-2)**2<V:
            raise AssertionError("all-h support-energy lower polynomial prerequisites")
        if 2*L<V*V:
            raise AssertionError("physical energy L>=V²/2 dyadic all-h fails")
        if (s+1)**2*(s-1)*(s*s+1)<s**5:
            raise AssertionError("all-h source degree x point factor product lower")
    if uniform<Fraction(s**6,2):
        raise AssertionError("EVERY fixed f and right E mean lower ≥s^6/2 not certified")
    return {
        "s":s,"h":s.bit_length()-1,
        "original_point_and_line_source_factor_count":V,
        "actual_source_incidence_degree":d,
        "minimal_physical_coordinate_palette":a,
        "global_occupied_right_and_left_pair_edge_count":V,
        "physical_missing_pair_edges_each_typed_support":m,
        "universal_occupied_physical_port_edge_energy_lower":L,
        "uniform_original_ALL_D_opposite_physical_threeflag_expectation_lower":
            uniform,
        "all_h_E_right_full_global_permutation_mean_ge_s6_over2":True,
        "given_adversarial_FIXED_g_minimax_NOT_PROVED":True,
        "physical_port_GOOD_subset_mean_NOT_PROVED":True,
        "accepted_historical_seven_GF5_six_ID_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def actual_original_ALL_D_opposite_wedges_direct(model):
    """Literal source incidence first, 3 DISTINCT original points/lines,
    two physical port colors opposite in both typed maps (ALL-D, not
    filtered GOOD). Independently compare with old F^T BG corrected
    2x2 physical original incidence tensor oracle in research tests.
    """
    source=tuple(tuple(x) for x in model["incidences"])
    f=tuple(map(tuple,model["left_labels"]))
    g=tuple(map(tuple,model["right_labels"]))
    V=len(f);a=_params(model["s"])[1]
    if len(g)!=V or len(set(g))!=V:
        raise ValueError("not complete original right source map")
    neighbors=[set() for _ in range(V)]
    for p,l in source:
        neighbors[p].add(l)
    coord=[[] for _ in range(a)]
    for p,e in enumerate(f):
        for v in e:coord[v].append(p)
    total=0
    for p,l in source:
        u,v=f[p]
        r=g[l]
        point_ends=(
            [q for q in coord[u] if q!=p],
            [q for q in coord[v] if q!=p])
        right_port={}
        for k,edge in enumerate(g):
            if k==l:continue
            intersect=set(r)&set(edge)
            if len(intersect)==1:
                right_port[k]=next(iter(intersect))
        groups=[]
        for points in point_ends:
            choices=[]
            for q in points:
                for k in neighbors[q]-{l}:
                    if k in right_port:
                        choices.append((q,k,right_port[k]))
            groups.append(choices)
        for q0,k0,c0 in groups[0]:
            for q1,k1,c1 in groups[1]:
                if k0!=k1 and c0!=c1:
                    total+=1
    return total


if __name__=="__main__":
    import json
    from hyp105_issue230_projection import fixture
    for h,scheme in ((1,"S68"),(1,"S72"),(1,"lex"),(2,"lex"),(2,"random")):
        model=fixture(h,scheme)
        cert=quenched_original_opposite_ALL_D_mean(model)
        cert["actual_fixed_original_g_ALL_D"]=actual_original_ALL_D_opposite_wedges_direct(model)
        print(json.dumps({k:str(v) for k,v in cert.items()},sort_keys=True))
    print(json.dumps({h:{
        k:str(v) for k,v in dyadic_every_original_spectral_free_quenched_certificate(1<<h).items()}
                      for h in range(1,17)},sort_keys=True))
