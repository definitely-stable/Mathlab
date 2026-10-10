"""HYP-105 B3.2-E1-C2: exact degree-two Johnson projection of B/A overlap.

A general k=6 weighted hypergraph intersection decomposition, not a
new hypergraph discrepancy theorem or a uniform GQ obstruction.
For arbitrary legal original-right injections g, the source is padded
with zeros to physical K=binom(a,2) abstract vertices. Any injection
extends to a permutation of K vertices, so the standard Johnson
orthogonal decomposition applies without assuming GQ symmetry.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def _valid_a(a):
    if type(a) is not int or a < 6:
        raise ValueError("physical coordinate alphabet a must be >=6")
    return a


def target_degree_two_data(a):
    """Exact W0/W1/W2/degree>=3 energies of the physical T_a target."""
    a = _valid_a(a)
    K = comb(a, 2)
    N = comb(K, 6)
    T = 70 * comb(a, 6)
    pair_total = comb(K, 2)
    pair_adjacent = K * (a - 2)
    pair_disjoint = pair_total - pair_adjacent
    qA = 7 * comb(a-3, 3)
    qD = 14 * comb(a-4, 2)
    qbar = Fraction(15*T, pair_total)
    assert pair_adjacent*qA+pair_disjoint*qD == 15*T
    lam2 = comb(K-4, 4)
    w0sq = Fraction(T*T, N)
    w2sq = (pair_adjacent*(qA-qbar)**2
            + pair_disjoint*(qD-qbar)**2) / lam2
    higher = Fraction(T) - w0sq - w2sq
    if higher < 0:
        raise AssertionError("negative target Johnson >=3 energy")
    return {
        "a": a, "K": K, "N": N, "T": T,
        "target_codegree_adjacent": qA,
        "target_codegree_disjoint": qD,
        "target_codegree_mean": qbar,
        "physical_adjacent_pair_count": pair_adjacent,
        "physical_disjoint_pair_count": pair_disjoint,
        "adjacent_pair_fraction": Fraction(pair_adjacent,pair_total),
        "johnson_lambda2": lam2,
        "target_w0_norm_squared": w0sq,
        "target_w1_norm_squared": Fraction(0),
        "target_w2_norm_squared": w2sq,
        "target_w_ge3_norm_squared": higher,
        "target_w2_zero": a == 9,
    }



def physical_three_edge_type(triple):
    """Five S_a types of THREE distinct physical K_a edge labels."""
    e=tuple(triple)
    if len(e)!=3 or len(set(e))!=3:
        raise ValueError("exactly three distinct physical pair edges required")
    degree=Counter(x for edge in e for x in edge)
    shape=tuple(sorted(degree.values(),reverse=True))
    key=(len(degree),shape)
    mapping={
        (3,(2,2,2)):"triangle",
        (4,(2,2,1,1)):"path_P4",
        (4,(3,1,1,1)):"star_K1_3",
        (5,(2,1,1,1,1)):"path_P3_plus_edge",
        (6,(1,1,1,1,1,1)):"matching_3",
    }
    if key not in mapping:
        raise AssertionError("unknown simple three-physical-pair orbit")
    return mapping[key]


def target_order_three_data(a):
    """All-a target W3 by five exact physical triple-edge S_a orbits.

    The target q3 values 1/2/0/5/8 on K6 were established in C0;
    the binomial embedding to a physical K_a is exact. The W3
    projection uses triple incidence after removing W0, W1=0 and W2.
    """
    t=target_degree_two_data(a)
    K=t["K"]
    lam2=t["johnson_lambda2"]
    lam3=comb(K-6,3)
    mean=Fraction(t["T"],t["N"])
    A=t["target_codegree_adjacent"]
    D=t["target_codegree_disjoint"]
    bar=t["target_codegree_mean"]
    # (orbit cardinality, adjacent label pairs within triple, codegree)
    orbits={
        "triangle":(comb(a,3),3,comb(a-3,3)),
        "path_P4":(12*comb(a,4),2,2*comb(a-4,2)),
        "star_K1_3":(4*comb(a,4),3,0),
        "path_P3_plus_edge":(30*comb(a,5),1,5*(a-5)),
        "matching_3":(15*comb(a,6),0,8),
    }
    if sum(x[0] for x in orbits.values())!=comb(K,3):
        raise AssertionError("physical triple orbits not a partition")
    residual={}
    third_energy=Fraction(0)
    for name,(count,adjacent,q3) in orbits.items():
        two_pair_weight=Fraction(adjacent*(A-bar)+(3-adjacent)*(D-bar),
                                 lam2)
        h=(Fraction(q3)-comb(K-3,3)*mean
           -comb(K-5,3)*two_pair_weight)
        residual[name]=h
        third_energy+=count*h*h/lam3
    fourth_or_higher=(t["target_w_ge3_norm_squared"]-third_energy)
    if fourth_or_higher<0:
        raise AssertionError("negative target W>=4 squared energy")
    return {
        **t,
        "johnson_lambda3":lam3,
        "target_three_orbits":orbits,
        "target_three_harmonic_residual":residual,
        "target_w3_norm_squared":third_energy,
        "target_w_ge4_norm_squared":fourth_or_higher,
    }


def _checked_source(weights, K):
    """Sparse source on first V<=K abstract vertices, then zero padded."""
    if type(K) is not int or K < 6:
        raise ValueError("K must be at least 6")
    if not hasattr(weights, "items"):
        raise ValueError("source weights must be a mapping")
    canonical = {}
    for R, w in weights.items():
        if type(w) is not int or w < 0:
            raise ValueError("nonnegative integer multiplicities required")
        try:
            z = frozenset(R)
        except TypeError as e:
            raise ValueError("invalid source hyperedge") from e
        if len(z) != 6 or any(type(i) is not int or not 0<=i<K for i in z):
            raise ValueError("six distinct abstract vertices in range required")
        if z in canonical:
            raise ValueError("duplicate sixset after canonicalization")
        if w:
            canonical[z]=w
    return canonical


def source_johnson_energy(weights, K):
    """Squared orthogonal norms W0/W1/W2/W>=3 using exact moments only.

    q_ij := sum_{R superseteq {i,j}}m(R).
    Subtract the W0 pair codegree and the W1 pair codegree from q_ij.
    The resulting row-sum-zero pair tensor r lies in Johnson W2.
    The I_2 I_2^T eigenvalue on row-sum-zero pair tensors is
    lambda2=C(K-4,4). Thus ||m_2||^2=sum r_ij^2/lambda2.
    """
    w = _checked_source(weights, K)
    N=comb(K,6)
    M=sum(w.values())
    squared=sum(x*x for x in w.values())
    degrees=[0]*K
    pairs=Counter()
    for R, value in w.items():
        for i in R:
            degrees[i]+=value
        for pair in combinations(sorted(R),2):
            pairs[pair]+=value
    mean=Fraction(M,N)
    delta=[Fraction(x)-Fraction(6*M,K) for x in degrees]
    lam1=comb(K-2,5)
    betas=[x/lam1 for x in delta]
    q0=comb(K-2,4)*mean
    q1scale=comb(K-3,4)
    residual={}
    for i,j in combinations(range(K),2):
        residual[(i,j)]=(Fraction(pairs[(i,j)])-q0
                         -q1scale*(betas[i]+betas[j]))
    row_sums=[Fraction(0) for _ in range(K)]
    for (i,j),val in residual.items():
        row_sums[i]+=val
        row_sums[j]+=val
    if any(x for x in row_sums):
        raise AssertionError("Johnson W2 pair residual row sums not zero")
    lam2=comb(K-4,4)
    w0sq=Fraction(M*M,N)
    w1sq=sum(x*x for x in delta)/lam1
    w2sq=sum(x*x for x in residual.values())/lam2
    higher=Fraction(squared)-w0sq-w1sq-w2sq
    if higher < 0:
        raise AssertionError("negative source Johnson >=3 norm squared")
    return {
        "K":K, "M":M, "N":N, "source_norm_squared":squared,
        "w0_norm_squared":w0sq, "w1_norm_squared":w1sq,
        "w2_norm_squared":w2sq, "w_ge3_norm_squared":higher,
        "degree_vector":tuple(degrees),
        "pair_marginals":pairs,
        "w2_pair_residuals":residual,
        "w1_betas":tuple(betas),
    }


def _checked_right_map(right_labels, a, weights):
    a=_valid_a(a)
    allowed=set(combinations(range(a),2))
    try:
        labels=tuple(tuple(e) for e in right_labels)
    except TypeError as e:
        raise ValueError("right labeling invalid") from e
    if len(labels)>comb(a,2) or len(labels)<6 or len(set(labels))!=len(labels):
        raise ValueError("right injection cardinality/uniqueness invalid")
    if any(e not in allowed for e in labels):
        raise ValueError("not a legal physical unordered pair injection")
    if any(max(R)>=len(labels) for R in weights):
        raise ValueError("original right vertex has no physical label")
    return labels


def is_target_sixset(physical_six):
    """Direct independent degree-two membership; no materialized T_a."""
    degrees=Counter(v for e in physical_six for v in e)
    return len(degrees)==6 and all(x==2 for x in degrees.values())


def exact_overlap_decomposition(weights, right_labels, *, a=6,
                                with_source_norms=True):
    """Exact for EVERY right injection, no random-right averaging.

    U=mu+U2+U>=3; no W1 target component since T_a is a 1-design.
    U2=(qA-qD)/lambda2*(adjacency-weighted original source
       pair marginal - 15*M * physical adjacent-pair fraction).
    The arbitrary map g is allowed to destroy GQ concurrence.
    """
    a=_valid_a(a)
    K=comb(a,2)
    w=_checked_source(weights,K)
    labels=_checked_right_map(right_labels,a,w)
    t=target_degree_two_data(a)
    mass=sum(w.values())
    q=Counter()
    exact=0
    for R,x in w.items():
        edges=tuple(labels[i] for i in sorted(R))
        if is_target_sixset(edges):
            exact+=x
        for p in combinations(sorted(R),2):
            q[p]+=x
    adjacent_source_pair_mass=sum(
        count for (i,j),count in q.items()
        if len(set(labels[i]) & set(labels[j]))==1)
    expected=Fraction(mass*t["T"],t["N"])
    second=(Fraction(t["target_codegree_adjacent"]
                     -t["target_codegree_disjoint"],
                     t["johnson_lambda2"])
            *(adjacent_source_pair_mass
              -15*mass*t["adjacent_pair_fraction"]))
    higher=Fraction(exact)-expected-second
    out={
        "a":a,"K":K,"original_vertices":len(labels),
        "source_mass":mass,"overlap_exact":exact,
        "uniform_injection_mean":expected,
        "correlated_degree2_contribution":second,
        "degree_ge3_contribution":higher,
        "adjacent_source_pair_mass":adjacent_source_pair_mass,
        "source_pair_total":15*mass,
        "johnson_identity_exact":expected+second+higher==exact,
        "universal_all_correlated_positive_lower_proved":False,
    }
    if with_source_norms:
        source=source_johnson_energy(w,K)
        second_square_bound=source["w2_norm_squared"]*t["target_w2_norm_squared"]
        higher_square_bound=(source["w_ge3_norm_squared"]
                             *t["target_w_ge3_norm_squared"])
        if second*second>second_square_bound or higher*higher>higher_square_bound:
            raise AssertionError("orthogonal Johnson Cauchy bound falsified")
        out.update({
            "source_w1_norm_squared":source["w1_norm_squared"],
            "source_w2_norm_squared":source["w2_norm_squared"],
            "source_w_ge3_norm_squared":source["w_ge3_norm_squared"],
            "target_w2_norm_squared":t["target_w2_norm_squared"],
            "target_w_ge3_norm_squared":t["target_w_ge3_norm_squared"],
            "degree2_absolute_square_bound":second_square_bound,
            "degree_ge3_absolute_square_bound":higher_square_bound,
            "square_bound_checked":True,
            "nonnegative_global_lower_certified":(
                expected*expected>4*max(second_square_bound,higher_square_bound)),
        })
        # Sufficient, deliberately conservative: mu>2max(sqrt(B2),sqrt(B3))
        # => mu>sqrt(B2)+sqrt(B3), so overlap positive under all g.
    return out


def finite_W32_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    cases={}
    for scheme in ("lex","reverse-line"):
        model=pair_labeled_symplectic(1,scheme)
        weights=source_weighted_BA_hypergraph(model)
        labels=list(model["right_labels"])
        variants={"identity":labels}
        if scheme=="reverse-line":
            other=list(labels)
            other[4],other[13]=other[13],other[4]
            variants["original_line_swap_4_13"]=other
        for label,g in variants.items():
            data=exact_overlap_decomposition(weights,g,a=6)
            cases[scheme+"/"+label]={key:str(value) if isinstance(value,Fraction)
                else value for key,value in data.items()
                if key not in ("source_pair_total",)}
    return {
        "target_K6":{k:str(v) if isinstance(v,Fraction) else v
                     for k,v in target_degree_two_data(6).items()},
        "target_K9_W2_zero":target_degree_two_data(9)["target_w2_zero"],
        "finite_cases":cases,
        "all_h_GQ_obstruction":False,
    }


if __name__=="__main__":
    print(json.dumps(finite_W32_report(),sort_keys=True,indent=2))
