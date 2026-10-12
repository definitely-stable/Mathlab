"""HYP-105 E1-K3-G2-O: all-a H3 physical orbit formula and real GQ triple coupling.

Proves an exact third Johnson harmonic for five three-pair physical shapes
and four original GQ line-intersection triple shapes. A coupled integer
4x5 tensor for each genuine ORIGINAL weighted B-left sixsource records
all twenty weighted source triples, with the true dual tested separately.
Level-three source/target contraction is checked two independent ways:
the original-sixset triple-orbit ledger and the harmonic inner product.

Also proves GQ intersection graph strongly regular (V,s(s+1),s-1,s+1)
and a source-support bound w_f(R) <= (s+1)^4*e_GQ(R) for all legal h.
The remaining ranks 4..6 are NOT bounded geometrically and P2/P7
are NOT proved. W32 complete finite C0/B0 certificate only.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph,
    physical_target_three_point_orbits,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    target_low_harmonics, exact_target_johnson_decomposition,
    source_energy_ge3, spectral_overlap_certificate,
    physical_pair_indices, six_image_index, rat,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model, exact_two_family_point, _anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    gq_pair_model,
)

PHYSICAL_SHAPES=(
    "triangle","path_P4","star_K1_3",
    "path_P3_plus_edge","matching_3",
)


def physical_triple_shape(edges):
    """All five simple unlabeled three-distinct-edge graphs (isolates ignored)."""
    edges=tuple(tuple(e) for e in edges)
    if (len(edges)!=3 or len(set(edges))!=3 or
            any(len(e)!=2 or e[0]>=e[1] or e[0]<0 for e in edges)):
        raise ValueError("three distinct canonical unordered physical edges")
    deg=Counter(v for edge in edges for v in edge)
    r=len(deg)
    if r==3:
        if sorted(deg.values())!=[2,2,2]:
            raise AssertionError("triangle shape invalid")
        return "triangle"
    if r==4:
        if sorted(deg.values())==[1,1,1,3]:
            return "star_K1_3"
        if sorted(deg.values())==[1,1,2,2]:
            return "path_P4"
    if r==5 and sorted(deg.values())==[1,1,1,1,2]:
        return "path_P3_plus_edge"
    if r==6 and all(d==1 for d in deg.values()):
        return "matching_3"
    raise AssertionError("unclassified three-edge physical shape")


def target_rank3_orbits(a):
    """ALL a>=6 exact unique harmonic h3 on the five physical triple orbits.

    Let H2(A)=sum_{pairs B subset A}h2(B).
    Triple down-marginal of H2 lifted to the sixslice is
    C(K-5,3)*H2(A); triple down-marginal of H0 is C(K-3,3)*p.
    Since the rank-three up/down eigenvalue is C(K-6,3),
    h3(A)=[c3(A)-p*C(K-3,3)-C(K-5,3)*H2(A)]/C(K-6,3).
    """
    low=target_low_harmonics(a)
    K=low["K"]
    lam3=comb(K-6,3)
    if not lam3:
        raise ValueError("rank-three denominator zero")
    shape=physical_target_three_point_orbits(a)["target_triple_label_orbits"]
    adjacency={
        "triangle":3,"path_P4":2,"star_K1_3":3,
        "path_P3_plus_edge":1,"matching_3":0,
    }
    coeff={}
    triple_pop=0
    for name in PHYSICAL_SHAPES:
        count=shape[name]["orbit_cardinality"]
        c=shape[name]["codegree"]
        adj=adjacency[name]
        H2=adj*low["h2_adj"]+(3-adj)*low["h2_dis"]
        coeff[name]=Fraction(
            c-low["density"]*comb(K-3,3)-comb(K-5,3)*H2,
            lam3)
        triple_pop+=count
    if triple_pop!=comb(K,3):
        raise AssertionError("five physical triple orbits are not complete")
    E3=lam3*sum((shape[n]["orbit_cardinality"]*coeff[n]**2
                  for n in PHYSICAL_SHAPES),Fraction(0))
    E4plus=low["E_ge3"]-E3
    if E4plus<0 or sum(
            (shape[n]["orbit_cardinality"]*coeff[n]
             for n in PHYSICAL_SHAPES),Fraction(0)):
        raise AssertionError("rank-three mean-zero energy / orbit invalid")
    return {
        "a":a,"K":K,"lambda3":lam3,
        "orbit_sizes":{n:shape[n]["orbit_cardinality"]
                       for n in PHYSICAL_SHAPES},
        "target_triple_codegrees":{n:shape[n]["codegree"]
                                   for n in PHYSICAL_SHAPES},
        "h3":coeff,"E3":E3,"E_ge4":E4plus,
    }


def target_H3_on_six(six,physical_edges,h3):
    if len(six)!=6 or len(set(six))!=6 or any(
            type(i) is not int or not 0<=i<len(physical_edges)
            for i in six):
        raise ValueError("six distinct physical pair-edge indices required")
    return sum((h3[physical_triple_shape(
        physical_edges[i] for i in triple)]
        for triple in combinations(six,3)),Fraction(0))


@lru_cache(maxsize=12)
def _true_gq_intersection(s,incidences,V):
    """Independent finite validator for exact GQ(s,s) line-intersection SRG."""
    if (type(s) is not int or s<2 or type(V) is not int or
            V!=(s+1)*(s*s+1)):
        raise ValueError("balanced GQ(s,s) expected")
    delta=s+1
    left=[set() for _ in range(V)]
    right=[set() for _ in range(V)]
    unique=set()
    for p,l in incidences:
        if (type(p) is not int or type(l) is not int or
                not 0<=p<V or not 0<=l<V or (p,l) in unique):
            raise ValueError("original GQ incidence invalid")
        unique.add((p,l))
        left[p].add(l)
        right[l].add(p)
    if (len(incidences)!=V*delta or
            any(len(x)!=delta for x in left+right)):
        raise AssertionError("GQ original regular degree violated")
    near=[set() for _ in range(V)]
    pair_anchor={}
    for p,lines in enumerate(left):
        for u,v in combinations(sorted(lines),2):
            if (u,v) in pair_anchor:
                raise AssertionError("two GQ lines sharing two points")
            pair_anchor[(u,v)]=p
            near[u].add(v)
            near[v].add(u)
    k=s*delta
    if any(len(N)!=k for N in near):
        raise AssertionError("GQ line intersection regularity violated")
    for u,v in combinations(range(V),2):
        common=len(near[u]&near[v])
        expected=s-1 if v in near[u] else s+1
        if common!=expected:
            raise AssertionError("GQ strongly regular parameters violated")
    triangles=V*comb(delta,3)
    wedges=V*comb(k,2)-3*triangles
    single=(V*k//2)*(V-2*k+s-1)
    empty=comb(V,3)-triangles-wedges-single
    if (min(triangles,wedges,single,empty)<0 or
            triangles+wedges+single+empty!=comb(V,3)):
        raise AssertionError("GQ four triple-shape populations invalid")
    return {
        "s":s,"V":V,"k":k,"lambda":s-1,"mu":s+1,
        "edge_count":V*k//2,
        "triple_populations":(empty,single,wedges,triangles),
        "adjacency":tuple(frozenset(x) for x in near),
    }


def gq_line_geometry(model):
    V=model["v_right"]
    if model["v_left"]!=V:
        raise ValueError("balanced genuine original GQ source required")
    return _true_gq_intersection(model["s"],tuple(model["incidences"]),V)


def gq_sixsource_guard(weights,geom):
    """ALL-h source support inequality, validated for real original sixsources.

    Each B-left six-incidence support has precisely one doubled original
    left point, whose two right lines MUST intersect, and four other
    distinct left origins, at most Delta choices per remaining line.
    A pair of intersecting right lines has unique left common point.
    Thus w_f(R) <= (s+1)^4 * #intersecting original right-line pairs in R.
    """
    adjacency=geom["adjacency"]
    cap_unit=(geom["s"]+1)**4
    by_pair_count=Counter()
    total=0
    tightness=Fraction(0)
    for R,w in weights.items():
        if (type(w) is not int or w<0 or len(R)!=6 or
                any(type(i) is not int or not 0<=i<geom["V"] for i in R)):
            raise ValueError("legal nonnegative original sixline weights")
        n=sum(v in adjacency[u] for u,v in combinations(sorted(R),2))
        if w>cap_unit*n:
            raise AssertionError("GQ sixth-order incidence cherry cap violated")
        if w and not n:
            raise AssertionError("positive sixsource on pairwise skew GQ lines")
        by_pair_count[n]+=w
        total+=w
        if n:
            tightness=max(tightness,Fraction(w,cap_unit*n))
    return {
        "mass":total,"nonzero_original_pair_count_classes":
            dict(sorted(by_pair_count.items())),
        "max_weight_over_GQ_cherry_cap":rat(tightness),
        "all_h_sixsource_GQ_cherry_cap_valid":True,
    }


def _source_H3_and_energy(weights,labels,*,a):
    """Independent physical source H3 projection from 0/1/2/3 marginals."""
    K=comb(a,2)
    palette=physical_pair_indices(a)
    labels=tuple(tuple(x) for x in labels)
    low=source_energy_ge3(weights,labels,a=a)
    degree=Counter()
    pairdegree=Counter()
    tripledegree=Counter()
    for R,w in weights.items():
        S=six_image_index(R,labels,palette)
        for i in S:
            degree[i]+=w
        for B in combinations(S,2):
            pairdegree[B]+=w
        for A in combinations(S,3):
            tripledegree[A]+=w
    c0=Fraction(low["mass"],comb(K,6))
    lam1=comb(K-2,5)
    lam2=comb(K-4,4)
    lam3=comb(K-6,3)
    h1={
        e:Fraction(degree[e]-c0*comb(K-1,5),lam1)
        for e in range(K)
    }
    h2={
        B:Fraction(
            pairdegree[B]-c0*comb(K-2,4)-
            comb(K-3,4)*(h1[B[0]]+h1[B[1]]),lam2)
        for B in combinations(range(K),2)
    }
    h3={}
    for A in combinations(range(K),3):
        h3[A]=Fraction(
            tripledegree[A]-c0*comb(K-3,3)-
            comb(K-4,3)*sum(h1[v] for v in A)-
            comb(K-5,3)*sum(h2[B] for B in combinations(A,2)),
            lam3)
    down=Counter()
    for A,v in h3.items():
        if v:
            for B in combinations(A,2):
                down[B]+=v
    if any(down.values()):
        raise AssertionError("source rank-three Johnson down-kernel invalid")
    E3=lam3*sum((v*v for v in h3.values()),Fraction(0))
    E4plus=Fraction(*low["E_ge3"].as_integer_ratio())-E3
    if E4plus<0:
        raise AssertionError("source rank four-to-six residual energy negative")
    return h3,E3,E4plus


def original_GQ_third_coupling(model, weights=None):
    """Two independent rank-three checks plus four-by-five GQ/physical tensor."""
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("complete ORIGINAL weighted source gate is W32/K6 only")
    geom=gq_line_geometry(model)
    weights=source_weighted_BA_hypergraph(model) if weights is None else weights
    guard=gq_sixsource_guard(weights,geom)
    shape=target_rank3_orbits(6)
    labels=model["right_labels"]
    palette=physical_pair_indices(6)
    physical_edges=tuple(combinations(range(6),2))
    tensor=Counter()
    direct=Fraction(0)
    for R,w in weights.items():
        if not w:
            continue
        if len(R)!=6:
            raise ValueError("exact original sixsource rank required")
        S=six_image_index(R,labels,palette)
        for orig in combinations(sorted(R),3):
            phys_ids=tuple(sorted(palette[labels[v]] for v in orig))
            gq_edges=sum(v in geom["adjacency"][u]
                         for u,v in combinations(orig,2))
            if not 0<=gq_edges<=3:
                raise AssertionError("original GQ triple edge count invalid")
            ps=physical_triple_shape(physical_edges[i] for i in phys_ids)
            tensor[(gq_edges,ps)]+=w
            direct+=w*shape["h3"][ps]
    if sum(tensor.values())!=20*guard["mass"]:
        raise AssertionError("coupled original geometric 4x5 triple mass lost")
    h3src,E3src,E4src=_source_H3_and_energy(
        weights,labels,a=6)
    lam3=shape["lambda3"]
    projection=lam3*sum((
        value*shape["h3"][physical_triple_shape(physical_edges[i]
                   for i in A)]
        for A,value in h3src.items()),Fraction(0))
    spectrum=spectral_overlap_certificate(weights,labels)
    C3=Fraction(*spectrum["signed_ranks"][3])
    if direct!=projection or direct!=C3:
        raise AssertionError("original/physical rank-three tensor != orthogonal contraction")
    C456=sum((Fraction(*x) for x in spectrum["signed_ranks"][4:]),
             Fraction(0))
    Et456=shape["E_ge4"]
    if C456*C456>E4src*Et456:
        raise AssertionError("rank four-to-six Cauchy-Schwarz invalid")
    return {
        "gq_geometry":{
            k:val for k,val in geom.items() if k!="adjacency"
        },
        "original_GQ_sixsource_guard":guard,
        "coupled_original_GQ_4x5_tensor":{
            str(n):{t:tensor[(n,t)] for t in PHYSICAL_SHAPES}
            for n in range(4)
        },
        "tensor_triple_mass":sum(tensor.values()),
        "third_J_harmonic_correlation":rat(direct),
        "independent_triple_projection":rat(projection),
        "sixsource_spectrum_third_level":spectrum["signed_ranks"][3],
        "remaining_four_to_six":rat(C456),
        "source_E3":rat(E3src),"source_E_ge4":rat(E4src),
        "target_E3":rat(shape["E3"]),"target_E_ge4":rat(Et456),
        "rank_four_to_six_CS_bound_squared":rat(E4src*Et456),
        "P2_universal_proved":False,
    }


def report():
    rank3={}
    for a in (6,9,14):
        x=target_rank3_orbits(a)
        rank3[str(a)]={
            k:({name:rat(y) for name,y in v.items()}
               if k=="h3" else
               rat(v) if isinstance(v,Fraction) else v)
            for k,v in x.items()
        }
    # Do not count the 223-map corpus. Two genuine ORIGINAL models,
    # both with complete independent B0/C0 plus original dual source.
    models=[
        ("lex",gq_pair_model(1,"lex")),
        ("hardest-M",swapped_labeling(_anchors()[0][1],"left",13,14)),
    ]
    reports=[]
    for name,model in models:
        p=exact_two_family_point(model)
        direct=original_GQ_third_coupling(model)
        dual=original_GQ_third_coupling(dual_model(model))
        if (p["U_BA"],p["U_AB"])!=(
                spectral_overlap_certificate(
                    source_weighted_BA_hypergraph(model),
                    model["right_labels"])["actual_U"],
                spectral_overlap_certificate(
                    source_weighted_BA_hypergraph(dual_model(model)),
                    model["left_labels"])["actual_U"]):
            raise AssertionError("independent original/dual C0-B0 rank check")
        reports.append({
            "name":name,"U_BA":p["U_BA"],"U_AB":p["U_AB"],
            "S_seven":p["S_seven"],"P2_margin":p["two_family_minus_mu"],
            "original_BA":direct,"actual_GQ_dual_AB":dual,
        })
    return {
        "slice":"HYP-105-E1-K3-G2-O",
        "all_a_third_harmonic_orbits":rank3,
        "original_true_GQ_models":reports,
        "all_h_GQ_intersection_and_cherry_cap_theorem":True,
        "all_h_P2_proved":False,"all_h_P7_proved":False,
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
