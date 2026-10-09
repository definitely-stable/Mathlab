"""HYP-105 E2-B3.2-C: projectively canonical Pluecker line ranks + cyclic shifts.

Genuine finite-field / exterior-square data, not a symplectic-group orbit
quotient or an all-h good ASET family. The classical Pluecker injection
G(2,4)->PG(5,q) is BASIS-INDEPENDENT and injective.

For ANY point-order bijection P->[V] and line-order bijection L->[V],
define g_t(l) = pair_unrank((line_rank(l)+t)%V) and
f(p)=pair_unrank(point_rank(p)), all in the same abstract K_a palette
but physically disjoint coordinate blocks. Each incidence (p,l)
has equality f(p)=g_t(l) for exactly ONE shift t. Thus across V shifts
the total equality incidences is N=V*(s+1), and the minimizing shift
has at most s+1 equality incidences. Since V>s+1, g_t cannot equal
f(pi(l)) for ANY incidence-perfect-matching pi. This is a new restricted
all-h *nonalignment certificate*, NOT a bound on D_s, R2, R3 or ASET.

Executable GF2/GF4 only, as the repository's symplectic_gq is capped.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import (
    pair_alphabet_size, unrank_pair, pair_labeled_symplectic,
)
from hyp105_g5e2b3b2_coincident_cycles import exact_coincident_c6, check_input

SCHEMES = ("plucker-lex-mincollision", "plucker-frobenius-mincollision",
           "plucker-lex-zero")
WEDGE_PAIRS = tuple(combinations(range(4), 2))


def plucker_wedge(u, v, field):
    """Normalized 6-minor exterior bivector of independent GF(q)^4 vectors."""
    if len(u) != 4 or len(v) != 4:
        raise ValueError("two four-dimensional vectors required")
    if any(not isinstance(x, int) or not 0 <= x < field.q
           for x in tuple(u)+tuple(v)):
        raise ValueError("coordinates must be field elements")
    minors = tuple(field.mul(u[i], v[j]) ^ field.mul(u[j], v[i])
                   for i, j in WEDGE_PAIRS)
    pivot = next((w for w in minors if w), None)
    if pivot is None:
        raise ValueError("dependent vectors do not determine a line")
    inverse = field.inv(pivot)
    return tuple(field.mul(w, inverse) for w in minors)


def exact_isotropic_klein_check(p, field):
    """Classical, explicit Pluecker+isotropy equations in this project.

    Coordinate order (01,02,03,12,13,23).
    Klein: p01*p23 + p02*p13 + p03*p12 = 0.
    W(3,q) imposed by symplectic u0*v2+u2*v0+u1*v3+u3*v1
    gives p02+p13 = 0 (char 2).
    """
    if len(p) != 6:
        return False
    return ((p[1] ^ p[4]) == 0 and
            (field.mul(p[0], p[5]) ^
             field.mul(p[1], p[4]) ^
             field.mul(p[2], p[3])) == 0)


def canonical_line_pluckers(field, points, lines):
    """One normalized exterior bivector per totally isotropic line.

    Distinct lines MUST be injective by classical Klein correspondence;
    the finite assertion is independently falsifiable at h=1,2.
    """
    result=[]
    for line in lines:
        if len(line)<2 or len(set(line))!=len(line):
            raise ValueError("line needs >=2 distinct projective points")
        u,v=points[line[0]],points[line[1]]
        plucker=plucker_wedge(u,v,field)
        if not exact_isotropic_klein_check(plucker,field):
            raise AssertionError("not a totally isotropic Klein point")
        result.append(plucker)
    if len(set(result)) != len(lines):
        raise AssertionError("Klein line injection failed")
    return tuple(result)


def incidence_shift_histogram(point_ranks,line_ranks,incidences):
    """How many factor incidences physically IDENTIFY point and line pair."""
    v=len(point_ranks)
    if v<2 or len(line_ranks)!=v or set(point_ranks)!=set(range(v)) or (
            set(line_ranks)!=set(range(v))):
        raise ValueError("expected two complete [V] rank bijections")
    hist=[0]*v
    if len(set(incidences))!=len(incidences):
        raise ValueError("duplicate incidences")
    for p,l in incidences:
        if not 0<=p<v or not 0<=l<v:
            raise ValueError("invalid factor incidence")
        hist[(point_ranks[p]-line_ranks[l])%v] += 1
    if sum(hist)!=len(incidences):
        raise AssertionError("every incidence must determine unique shift")
    return tuple(hist)


def rank_labels(field,points,lines,incidences,scheme):
    """All-h algebraic definition, hosted evaluation capped to GF2/GF4.

    Pluecker lex/frobenius are bijective ordering keys; the tie-free
    exterior projective signatures guarantee uniqueness. Min-collision
    shift chosen using incidence graph is deterministic (smallest tie).
    """
    if scheme not in SCHEMES:
        raise ValueError("unsupported Pluecker control")
    v=len(points)
    if len(lines)!=v:
        raise ValueError("balanced point/line GQ required")
    pkeys=tuple(points)
    if len(set(pkeys)) != v:
        raise ValueError("point projective representatives not distinct")
    po=sorted(range(v),key=lambda i:pkeys[i])
    point_rank=[-1]*v
    for rank,p in enumerate(po):
        point_rank[p]=rank

    bivectors=canonical_line_pluckers(field,points,lines)
    frobenius="frobenius" in scheme
    if frobenius:
        # Frobenius automorphism x->x^2 is a GF(2)-semilinear bijection
        # of GF(2^h); it does NOT claim to be Sp(4,q)-equivariant here.
        keys=tuple(tuple(field.mul(z,z) for z in biv) for biv in bivectors)
    else:
        keys=bivectors
    lo=sorted(range(v),key=lambda i:keys[i])
    line_rank=[-1]*v
    for rank,l in enumerate(lo):
        line_rank[l]=rank

    hist=incidence_shift_histogram(point_rank,line_rank,incidences)
    mincount=min(hist)
    shift=(0 if scheme.endswith("-zero") else hist.index(mincount))
    rank_shifted=[(r+shift)%v for r in line_rank]
    equal=hist[shift]
    degrees=Counter(p for p,_ in incidences)
    degree=next(iter(degrees.values()))
    if set(degrees.values())!={degree} or len(degrees)!=v:
        raise ValueError("regular point degree required")
    line_degree=Counter(l for _,l in incidences)
    if set(line_degree.values())!={degree} or len(line_degree)!=v:
        raise ValueError("regular line degree required")
    if sum(hist)!=degree*v or mincount>degree or v<=degree:
        raise AssertionError("all-h incidence shift average proof failed")
    if scheme!="plucker-lex-zero" and equal>degree:
        raise AssertionError("nonalignment minimizer failed")
    if len(set(rank_shifted))!=v:
        raise AssertionError("line shift not injective")
    return {
        "point_ranks":tuple(point_rank), "line_ranks":tuple(line_rank),
        "shift":shift, "shift_histogram":hist,
        "min_possible_incidence_equalities":mincount,
        "actual_incidence_equalities":equal,
        "maximum_all_h_minimizer_equalities":degree,
        "proves_no_incidence_perfect_pair_alignment":equal < v,
        "bivectors":bivectors,
    }


def plucker_shift_model(power,scheme="plucker-lex-mincollision"):
    """Explicit distinct split 2+2 physical GF5 column supports (h=1,2)."""
    if power not in (1,2):
        raise ValueError("finite hosted GQ enumeration restricted to GF2/GF4")
    field,points,lines,incidences=symplectic_gq(power)
    ranked=rank_labels(field,points,lines,incidences,scheme)
    v=len(points)
    a=pair_alphabet_size(v)
    left=tuple(unrank_pair(rank,a) for rank in ranked["point_ranks"])
    right=tuple(unrank_pair((rank+ranked["shift"])%v,a)
                for rank in ranked["line_ranks"])
    result={
        "h":power,"s":field.q,"m":2*a,"a":a,"v":v,"N":len(incidences),
        "scheme":scheme, "points":points,"lines":lines,
        "incidences":incidences,
        "left_labels":left,"right_labels":right,
        "supports":tuple(left[p]+tuple(a+x for x in right[l])
                         for p,l in incidences),
        "plucker_shift":ranked["shift"],
        "actual_incidence_pair_equalities":
            ranked["actual_incidence_equalities"],
        "minimum_over_shift_pair_equalities":
            ranked["min_possible_incidence_equalities"],
        "maximum_proved_minshift_pair_equalities":
            ranked["maximum_all_h_minimizer_equalities"],
        "no_incidence_aligned_perfect_matching":
            ranked["proves_no_incidence_perfect_pair_alignment"],
        "all_h_nonalignment_theorem_proved":
            scheme.endswith("-mincollision"),
        "all_h_injection_definition_proved":True,
        "all_h_R2_bound_proved":False,
        "all_h_R3_upper_bound_proved":False,
        "new_ASET_exponent_proved":False,
    }
    check_input(result)
    if len(set(result["supports"]))!=result["N"]:
        raise AssertionError("duplicate physical supports")
    return result


def bounded_report():
    result=[]
    for h in (1,2):
        for scheme in SCHEMES:
            model=plucker_shift_model(h,scheme)
            risk=exact_coincident_c6(model)
            result.append({
                "s":model["s"],"N":model["N"],"m":model["m"],
                "scheme":scheme, "shift":model["plucker_shift"],
                "equal_incidence_pairs":model["actual_incidence_pair_equalities"],
                "no_incidence_perfect_matching":
                    model["no_incidence_aligned_perfect_matching"],
                "all_h_nonalignment_theorem":
                    model["all_h_nonalignment_theorem_proved"],
                "exact_D_s":risk["exact_coincident_C6_factor_matchings_D"],
                "physical_left_C6":risk["left_physical_C6_cycles_examined"],
                "R3_obstruction_lower_numerator":
                    risk["exact_GF5_flow_weight_per_agreeing_cycle"] *
                    risk["exact_coincident_C6_factor_matchings_D"],
                "R3_obstruction_lower_denominator":51**6,
                "joint_R2_R3_theorem_proved":False,
            })
    return {
        "scope":"EXACT GF2/GF4 D_s for all-h explicitly injectable Pluecker rank maps",
        "classical_prior_art":"Klein/Pluecker embedding, not a new geometry theorem",
        "all_h_no_incidence_matching_alignment_for_minshift":True,
        "complete_R3_positive_motif_bound":False,
        "new_ASET_exponent_proved":False,
        "cases":result,
    }


if __name__=="__main__":
    print(json.dumps(bounded_report(),sort_keys=True,indent=2))
