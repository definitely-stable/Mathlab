"""HYP-105 E2-B3.1-B1: exhaustive five-by-six GF5 six-column motifs.

For SIX factor-disjoint incidence columns, suppose the left physical
coordinate graph has SIX DISTINCT edges of K5, uses all five vertices
with minimum degree two; the right has SIX DISTINCT K6 edges on six
vertices with degree two. Up to physical-coordinate relabeling there
are EXACTLY THREE K5 graphs. Right column-dual graphs are 70 two-factors
(C6 or 2*C3). Enumerating 3*70*10=2100 representative signed classes
classifies *every* such image for any s=2^h. Swapping colors is symmetric.

An independent all-nonzero GF5 flow-count algorithm exploits Fourier
orthogonality, eliminates coordinate duals, fixes one gauge dual
variable and quotients multiplicative GF5* scaling. It evaluates only
782 integer dual assignments per six-column template; no complex
arithmetic, 51^6 brute force or assumed nowherezero positivity.

The complete FACTOR-MATCHING six-flow classification was ALREADY accepted
in PR #214. This is a genuinely INDEPENDENT verifier of its v=5,w=6
coefficient and a sharper fixed-label U56 quantitative corollary.
Nonmatching factor-forest motifs remain OPEN. No ASET exponent.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from fractions import Fraction
from math import comb, factorial
import json

from hyp105_g5e2b3b1_critical_flows import two_factors, SIGNS
from hyp105_g5e2b3_forests import six_projection_coefficients

FIVE_PALETTE = tuple(combinations(range(5), 2))
SIX_PALETTE = tuple(combinations(range(6), 2))
RIGHT_FACTORS = two_factors()

def five_graph_types():
    """Exhaustive simple six-edge degree>=2 K5 graphs modulo S5.

    All six physical pair labels must be distinct (factor matching).
    A degree-one physical coordinate would force its GF5 weight to zero.
    """
    permutations5 = tuple(permutations(range(5)))
    orbits = Counter()
    for e in combinations(FIVE_PALETTE, 6):
        degree = Counter(x for pair in e for x in pair)
        if len(degree) != 5 or min(degree.values()) < 2:
            continue
        canonical = min(
            tuple(sorted(tuple(sorted((perm[u], perm[v])))
                         for u, v in e))
            for perm in permutations5)
        orbits[canonical] += 1
    if len(orbits) != 3 or sum(orbits.values()) != 85 or (
            sorted(orbits.values()) != [10,15,60]):
        raise AssertionError("complete K5 six-edge min-degree2 census changed")
    return tuple(sorted(orbits.items()))


def _dual_orbits():
    """Gauge lambda[0]=0 and quotient all nonzero GF5 scalar multiples.

    5^5 states: one zero state + (5^5-1)/4=781 nonzero orbits.
    """
    out=[]
    for tail in product(range(5),repeat=5):
        first=next((x for x in tail if x),None)
        if first is not None and first != 1:
            continue
        lam=(0,)+tail
        factor=(1 if first is None else
                4 if sum(lam)%5==0 else -1)
        out.append((lam,factor))
    if len(out)!=782 or sum(factor == 1 for _,factor in out)!=1:
        raise AssertionError("GF5 gauge/scalar orbit size mismatch")
    return tuple(out)

DUAL_ORBITS=_dual_orbits()


@lru_cache(maxsize=None)
def _coordinate_character_factor(values):
    """Integer sum over mu in GF5 of product(4 if mu=r_i else -1).

    Each original nonzero GF5 variable contributes 4 if its additive
    Fourier phase vanishes, and -1 otherwise. Exact for EVERY positive
    coordinate degree, including repeated incidence multiplicities.
    """
    d=len(values)
    if not 1<=d<=6 or any(not isinstance(x,int) or not 0<=x<5
                          for x in values):
        raise ValueError("coordinate must have 1..6 valid GF5 phases")
    cnt=Counter(values)
    return (sum((4**n)*((-1)**(d-n)) for n in cnt.values())
            + (5-len(cnt))*((-1)**d))


def exact_dual_GF5_six_flow(supports, signs, *, dimension=None):
    """Exact full 51-pattern signed six-column GF5 weight count.

    Original constraints:
      sum_{c in S_i} w_ic = 4   for each column i
      sum_{i:c in S_i} signs_i*w_ic = 0   for each coordinate c
      all w_ic in GF5*, four distinct positions per column.

    Fourier duals lambda_i (columns) and mu_c (coordinates) have
      prod_{(i,c)} psi(lambda_i+signs_i*mu_c) * zeta^(-4 sum lambda_i)
      / 5^(6+C), psi(x)=4 if x=0 else -1.
    Eliminate mu_c, giving local integer Phi_c. Balanced signs allow
    gauge lambda_i -> lambda_i+signs_i*z (sum lambda unchanged);
    fix lambda_0=0 and divide by 5^(5+C).
    Phi is invariant under lambda -> alpha*lambda for alpha in GF5*.
    On each nonzero scalar orbit: sum lambda==0 contributes 4*productPhi;
    sum lambda!=0 contributes -productPhi (all four fifth roots sum -1).
    The zero orbit contributes productPhi once. Therefore the quotient
    numerator is an INTEGER and must divide 5^(5+C).
    This identity holds for ANY six distinct four-support columns;
    finite 5/6 census below is a specialization.
    """
    supports=tuple(tuple(s) for s in supports)
    signs=tuple(signs)
    if len(supports)!=6 or len(signs)!=6 or signs.count(1)!=3 or (
            signs.count(-1)!=3):
        raise ValueError("six columns and balanced three plus / three minus")
    if (any(len(row)!=4 or len(set(row))!=4 or
            any(not isinstance(c,int) or c<0 for c in row)
            for row in supports) or
            len({tuple(sorted(row)) for row in supports})!=6):
        raise ValueError("six distinct valid four-coordinate supports required")
    if dimension is not None and (dimension<4 or any(
            c>=dimension for row in supports for c in row)):
        raise ValueError("invalid ambient coordinate bound")
    incidence=defaultdict(list)
    for i,row in enumerate(supports):
        for c in row:
            incidence[c].append(i)
    members=tuple(tuple(ids) for _,ids in sorted(incidence.items()))
    if sum(map(len,members))!=24:
        raise AssertionError("missing full four-support incidence")

    dual_sum=0
    for lam,scalar_weight in DUAL_ORBITS:
        phases=tuple((-signs[i]*lam[i])%5 for i in range(6))
        value=scalar_weight
        for ids in members:
            value*=_coordinate_character_factor(tuple(phases[i]
                                                     for i in ids))
        dual_sum+=value
    denominator=5**(5+len(members))
    q,rem=divmod(dual_sum,denominator)
    if rem or not 0<=q<=51**6:
        raise AssertionError("GF5 integer Fourier count not a valid probability")
    return q


def five_six_supports(left_edges, right_two_factor):
    """Physical left K5 pair edges, right 2-factor on the six column IDs."""
    if len(left_edges)!=6 or len(set(left_edges))!=6:
        raise ValueError("six distinct left physical pairs required")
    if len(right_two_factor)!=6:
        raise ValueError("right 2-factor should have six coordinate edges")
    right=[[] for _ in range(6)]
    for physical,(u,v) in enumerate(right_two_factor):
        if not (0<=u<v<6):
            raise ValueError("right dual column edge invalid")
        right[u].append(5+physical)
        right[v].append(5+physical)
    if any(len(row)!=2 for row in right):
        raise ValueError("right graph is not a 2-factor")
    supports=tuple(tuple(sorted(left_edges[i]+tuple(right[i])))
                   for i in range(6))
    if any(len(s)!=4 for s in supports):
        raise AssertionError("not four-support")
    return supports


@lru_cache(maxsize=1)
def five_six_complete_census():
    """All 2100 representatives for the full K5(min-degree2) x 2-factor class.

    Under point/line matching, each six column is a distinct physical
    pair-edge on each side. All left 5-coordinate simple graph embeddings
    are isomorphic to one of three graph types. Fix the left physical
    graph's lex edge order as the six column IDs. Every right 2-factor
    can be one of the 70 labeled dual column graphs; every unordered
    balanced sign has a unique representative with column 0 positive,
    yielding ten masks. These representatives cover every actual image,
    including color-swapped images. NO six-column W(3,s) multiplicity
    is counted or bounded here.
    """
    by_type=[]
    total_positive=total_zero=0
    all_min=None
    for left,physical_graph_orbit_size in five_graph_types():
        positive=zero=0
        minimum=None
        maximum=0
        sum_flow=0
        positive_sample=None
        for factor in RIGHT_FACTORS:
            supports=five_six_supports(left,factor)
            for sign_mask in SIGNS:
                signs=tuple(1 if sign_mask & (1<<i) else -1 for i in range(6))
                weight=exact_dual_GF5_six_flow(supports,signs,dimension=11)
                if weight:
                    positive+=1
                    if positive_sample is None:
                        positive_sample=(supports,signs,weight)
                else:
                    zero+=1
                minimum=weight if minimum is None else min(minimum,weight)
                maximum=max(maximum,weight)
                sum_flow+=weight
        if positive+zero!=700:
            raise AssertionError("incomplete right graph/sign census")
        total_positive+=positive
        total_zero+=zero
        all_min=minimum if all_min is None else min(all_min,minimum)
        by_type.append({
            "left_K5_physical_edges":left,
            "unlabeled_graph_orbit_size_on_K5":physical_graph_orbit_size,
            "right_2factor_cases":len(RIGHT_FACTORS),
            "unordered_balanced_sign_cases":len(SIGNS),
            "positive_cases":positive,"zero_cases":zero,
            "minimum_exact_GF5_flow":minimum,
            "maximum_exact_GF5_flow":maximum,
            "sum_exact_flows_over_representatives":sum_flow,
            "witness":positive_sample,
        })
    # Independent cross-certificate against the ALREADY ACCEPTED complete
    # 610x610 matching-census coefficient (PR #214). Each K5 coordinate
    # graph represents 6 * orbit_size distinct canonical named-column
    # projections: orbit_size labeled K5 edge sets, 6! named edge orders,
    # and divide by 5! relabelings of physical symbols.
    # The 70 right two-factors and 10 sign partitions sum is invariant
    # under relabeling six named columns, so it is enough to compute it
    # once per K5 graph isomorphism type.
    coefficient_56=6*sum(
        entry["unlabeled_graph_orbit_size_on_K5"] *
        entry["sum_exact_flows_over_representatives"]
        for entry in by_type)
    labeled_signed_56=6*sum(
        entry["unlabeled_graph_orbit_size_on_K5"]*700
        for entry in by_type)
    if coefficient_56!=4578391800 or labeled_signed_56!=357000:
        raise AssertionError("independent 782-state Fourier sum disagrees with "
                             "accepted 5486-orbit full matching coefficient")
    if len(by_type)!=3 or total_positive+total_zero!=2100:
        raise AssertionError("five/six motif census incomplete")
    if (total_zero or total_positive!=2100 or all_min!=10950 or
            [x["minimum_exact_GF5_flow"] for x in by_type]
            !=[14400,10950,11685]):
        raise AssertionError("five/six positivity/fixed integer minimum falsified")
    return {"scope":"all-h finite-template matching 5x6 and 6x5 only",
            "five_physical_graph_shapes":3,
            "physical_K5_six_edge_graphs_min_degree2":85,
            "right_two_factors":70, "balanced_sign_partitions":10,
            "total_representative_signed_cases":2100,
            "positive_representative_signed_cases":total_positive,
            "zero_representative_signed_cases":total_zero,
            "universal_per_event_GF5_flow_lower":all_min,
            "independent_full_matching_C_5_6":coefficient_56,
            "independent_full_matching_5_6_signed_mass":labeled_signed_56,
            "accepted_full_matching_prior":"HYP-105 E2-B3.1-B1 PR #214",
            "independent_fourier_cross_certificate":True,
            "per_matched_six_set_risk_numerator_lower":10*all_min,
            "by_type":by_type,
            "complete_other_six_motifs":False,
            "all_h_R3_upper_proved":False,
            "new_ASET_exponent_proved":False}


def falling(n,k):
    result=1
    for j in range(k):
        result*=n-j
    return result


def five_six_all_h_expected_obstruction(s):
    """Model-scoped universal fixed-label floor + independent-label lower.

    Let U56(f,g) be the count of factor-disjoint 6-sets with one physical
    projection a simple six-edge min-degree2 K5 graph and other a simple
    six-coordinate 2-factor. Count both 5x6 and 6x5, disjoint cases.
      R3 >= (10*10950/51^6) * U56, for EVERY individual f,g (all h).

    Independent uniform pair injections:
      p5 = 510*(a)_5/(K)_6, p6 = 70*(a)_6/(K)_6,
      E[U56] = 2*M6(G_s)*p5*p6  (M6 exact matching count).
    The existing factor-matching bound gives Omega(s^(9/2)) risk
    *only* for independent random labels; this subleading contribution
    does not supersede existing Omega(s^6) from 6x6 motifs.
    """
    if not isinstance(s,int) or s<2 or s&(s-1):
        raise ValueError("s=2^h >=2")
    v=(s+1)*(s*s+1)
    delta=s+1
    n=delta*v
    a=2
    while comb(a,2)<v:
        a+=1
    k=comb(a,2)
    if dict(six_projection_coefficients((1,)*6)).get(5)!=510 or (
            dict(six_projection_coefficients((1,)*6)).get(6)!=70):
        raise AssertionError("independent E2-B3.0 projection polynomial disagrees")
    p5=Fraction(510*falling(a,5),falling(k,6))
    p6=Fraction(70*falling(a,6),falling(k,6))
    lower_matching=Fraction(1)
    for j in range(6):
        lower_matching*=Fraction(n-2*j*delta,j+1)
    expectation_lower=2*lower_matching*p5*p6
    return {
        "s":s,"a":a,"K":k,"N":n,
        "P5_exact":str(p5),"P6_exact":str(p6),
        "exact_random_U56_formula":"2*M6(G_s)*P5*P6",
        "matched_factor_six_sets_lower":str(lower_matching),
        "random_E_U56_lower":str(expectation_lower),
        "random_expected_R3_lower_from_U56":
            str(expectation_lower*Fraction(109500,51**6)),
        "all_h_individual_R3_floor":"R3 >= 109500*U56/51^6",
        "random_R3_contribution_scale":"Omega(s^(9/2)), subleading vs 6x6",
        "all_h_R3_upper_proved":False,
        "new_ASET_exponent_proved":False,
    }


def report():
    census=five_six_complete_census()
    return {
        "classification":{
            k:v for k,v in census.items() if k!="by_type"
        },
        "physical_graph_types":[{
            k:v for k,v in entry.items() if k!="witness"
        } for entry in census["by_type"]],
        "exact_closed_GF5_dual_orbit_states":len(DUAL_ORBITS),
        "matching_random_bounds":[
            five_six_all_h_expected_obstruction(s) for s in (2,4,8)
        ],
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
