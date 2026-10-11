"""HYP-105 C24-B8-E: exact complete-injection pair-feature Gram and L2 gate.

No assumption of independent original source sixsets or sampled lines.  Under
ONE uniform complete g, the physical K_a edge-line-graph adjacency indicators
form a three-eigenspace Johnson-scheme Gram matrix. This module constructs the
exact orthogonal linear projection of the seven-score onto their span from
B8-D's exact all-h influence matrix. NOT a pointwise discrepancy bound.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c24b8d_two_line_influence import adjacency_probability


def _host(a, n):
    if (type(a) is not int or a < 6 or type(n) is not int
            or n < 4 or n > comb(a, 2)):
        raise ValueError("integer K_a host a>=6 and 4<=n<=C(a,2) required")
    return comb(a, 2)


def exact_pair_gram_parameters(a, n):
    """ALL-h closed-form pair covariance and its 3 Johnson eigenspaces.

    E_n=C(n,2), the three multiplicities are 1, n-1, n(n-3)/2.
    L(K_a) is regular on m=C(a,2) vertices of degree 2(a-2).
    Uniform injection of the n original lines preserves the four-edge
    marginal; hence the parameters depend on m but NOT on fixed LEFT f.
    """
    m = _host(a, n)
    p = adjacency_probability(a)
    variance = p * (1-p)
    same = variance
    share = -variance / (m-2)
    disjoint = 2*variance / ((m-2)*(m-3))
    eig0 = variance * (m-n)*(m-n-1) / ((m-2)*(m-3))
    eig1 = variance * (m-1)*(m-n) / ((m-2)*(m-3))
    eig2 = variance * (m-1)/(m-3)
    if not (eig0 >= 0 and eig1 >= 0 and eig2 > 0):
        raise AssertionError("uniform complete-injection Gram is not PSD")
    return {
        "m_physical_edges":m, "n_original_lines":n,
        "p_adj":p, "variance":variance,
        "cov_same":same, "cov_share_one":share,
        "cov_disjoint":disjoint,
        "eigenvalues":(eig0,eig1,eig2),
        "multiplicities":(1,n-1,n*(n-3)//2),
        "rank":sum(k for eig,k in zip((eig0,eig1,eig2),
                                      (1,n-1,n*(n-3)//2)) if eig),
    }


def exact_gram_entry(a, n, e, h):
    params=exact_pair_gram_parameters(a,n)
    if (e[0] >= e[1] or h[0] >= h[1] or
            any(type(x) is not int or x < 0 or x >= n for x in (*e,*h))):
        raise ValueError("two canonical distinct original right-line pairs required")
    shared=len(set(e).intersection(h))
    if shared==2:
        return params["cov_same"]
    if shared==1:
        return params["cov_share_one"]
    return params["cov_disjoint"]


def exact_pair_projection(influences, a, n):
    """Orthogonal L2 projection for b_e = Cov(S,Z_e)=p(1-p) I_e.

    Decompose b into trivial, n-1 vertex, and n(n-3)/2 row-zero parts.
    Divide by the corresponding exact Gram eigenvalue; zero eigenspaces
    must have zero b component (otherwise the input is not realizable).
    Compute and verify Gram*coefficients==b without dense inversion.
    """
    par=exact_pair_gram_parameters(a,n)
    pairs=tuple(combinations(range(n),2))
    if not isinstance(influences,dict) or set(influences)!=set(pairs):
        raise ValueError("a full canonical unordered line-pair influence matrix is needed")
    if any(type(influences[e]) not in (int,Fraction) for e in pairs):
        raise ValueError("every influence must be an exact rational")
    v=par["variance"]
    b={e:v*Fraction(influences[e]) for e in pairs}
    row={i:sum((b[(min(i,j),max(i,j))]
                for j in range(n) if j!=i),Fraction(0))
         for i in range(n)}
    scalar=sum(b.values(),Fraction(0))/len(pairs)
    vertex={i:row[i]-(n-1)*scalar for i in range(n)}
    if sum(vertex.values(),Fraction(0)):
        raise AssertionError("pair decomposition lost centered vertex mass")
    comps=[]
    for i,j in pairs:
        b0=scalar
        b1=(vertex[i]+vertex[j])/(n-2)
        comps.append((b0,b1,b[(i,j)]-b0-b1))
    eig=par["eigenvalues"]
    coefficients={}
    norms=[Fraction(0),Fraction(0),Fraction(0)]
    for e,components in zip(pairs,comps):
        coefficient=Fraction(0)
        for t,component in enumerate(components):
            norms[t]+=component*component
            if eig[t]:
                coefficient+=component/eig[t]
            elif component:
                raise ValueError("influences violate a zero-variance pair feature identity")
        coefficients[e]=coefficient
    projected_variance=sum(
        (norms[k]/eig[k] for k in range(3) if eig[k]),Fraction(0))
    if projected_variance!=sum(
            (b[e]*coefficients[e] for e in pairs),Fraction(0)):
        raise AssertionError("orthogonal Johnson decomposition failed")
    # Independent L(K_n) incidence form of the full Gram matrix.
    total=sum(coefficients.values(),Fraction(0))
    rows={i:sum((coefficients[(min(i,j),max(i,j))]
                 for j in range(n) if j!=i),Fraction(0))
          for i in range(n)}
    share,dis=par["cov_share_one"],par["cov_disjoint"]
    eig2=par["eigenvalues"][2]
    for i,j in pairs:
        reconstructed=(eig2*coefficients[(i,j)]
                       +(share-dis)*(rows[i]+rows[j])+dis*total)
        if reconstructed!=b[(i,j)]:
            raise AssertionError("Gram*coefficients != original covariance")
    if n==par["m_physical_edges"] and (
            any(rows.values()) or total!=0):
        raise AssertionError("full physical-edge bijection lost zero-row projection")
    return {
        "params":par, "coefficients":coefficients,
        "mean_zero":True,
        "component_covariance_norms":tuple(norms),
        "projected_variance":projected_variance,
        "exact_orthogonality_all_pair_features":True,
        "does_not_bound_pointwise_residual":True,
    }


def evaluate_projection(projection, physical_right_injection, a):
    """Exact P_2(g)=sum gamma_ij (Z_ij(g)-p) for one WHOLE g."""
    coefficients=projection["coefficients"]
    n=projection["params"]["n_original_lines"]
    _host(a,n)
    if (not isinstance(physical_right_injection,(list,tuple))
            or len(physical_right_injection)!=n):
        raise ValueError("one complete original right global injection required")
    images=tuple(physical_right_injection)
    valid=set(combinations(range(a),2))
    if (any(not isinstance(edge,tuple) or edge not in valid for edge in images)
            or len(set(images))!=n):
        raise ValueError("right global images must be canonical distinct K_a edges")
    p=projection["params"]["p_adj"]
    value=sum((coef*(int(bool(set(images[i])&set(images[j])))-p)
               for (i,j),coef in coefficients.items()),Fraction(0))
    return value


def exact_residual_witness(projection, mean, observed_score,
                           physical_right_injection, a):
    """Finite coherent-g witness of NONZERO nonlinear pair-feature residual.

    R(g)=S(g)-mu-P_2(g) is orthogonal to every centered pair feature in
    L2(uniform complete g), but |R(g)| alone is NOT a variance or an all-h
    positive S lower.  It is a valid pointwise lower on ||R||_infinity.
    """
    if type(observed_score) is not int or observed_score < 0 or not isinstance(mean,Fraction):
        raise ValueError("exact rational mean and nonnegative integer global score needed")
    value=evaluate_projection(projection,physical_right_injection,a)
    residual=Fraction(observed_score)-mean-value
    return {
        "mean":mean,"score":observed_score,
        "pair_linear_projection_at_g":value,
        "signed_centered_score":Fraction(observed_score)-mean,
        "nonlinear_pair_feature_residual_at_g":residual,
        "certified_residual_infinity_norm_floor":abs(residual),
        "actual_seven_score_not_pair_linear" : residual!=0,
        "no_uniform_s6_or_R3_inference":True,
    }
