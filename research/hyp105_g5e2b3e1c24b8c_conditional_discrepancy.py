"""HYP-105 C24-B8-C: exact fixed-f right conditional mean, anchor orbit gate.

For each ORIGINAL W(3,2^h), an arbitrary complete LEFT global injection f
is fixed; RIGHT g is uniformly drawn from all complete physical K_a-edge
injections. No independence is asserted across distinct source sixsets.

ALL-h:
  * Conditional mean E_g S(f,g) from f-eligible original source fibers.
  * Conditioning on one g(line) physical edge changes no expectation.
  * Conditioning on two distinct line images has EXACTLY two possible
    values: intersecting physical edges and disjoint physical edges.
  * These values satisfy a sharp rational orbit-weighted mean identity.
  * A right-side original C=(2,2,2) triple cannot survive adjacent
    physical assignments of any two of its three lines.
Not an ALL-f/g positive lower, not full GF5 R3 or ASET.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, perm

from hyp105_g5e2b3e1c24b8a_physical_tensor import (
    TAGS, physical_factor_state, source_profile,
)
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import (
    PROFILE_C, profile_probability, d6_signature_probability,
)


def source_right_mean(six, fixed_left, host_coordinates):
    """Exact E_g X_J(f,g), uniformly across all complete global RIGHT maps."""
    t = source_profile(six)
    if t is None:
        return Fraction(0)
    left_ok, left_sig = physical_factor_state(six, fixed_left, left=True)
    if not left_ok:
        return Fraction(0)
    if t == "D6":
        return (d6_signature_probability(host_coordinates)
                if left_sig is not None else Fraction(0))
    rprof = tuple(sorted(Counter(l for _, l in six).values(), reverse=True))
    return profile_probability(host_coordinates, rprof)


def right_mean_from_compiled_left(source, host_coordinates):
    """Exact fixed-f mean, using ORIGINAL source multiplicities, no per-J maps.

    B2 compile_left records (tag, sorted six right lines, D6 left sig, count)
    collapse only sources with the same globally fixed f profile, and retain
    original DISTINCT six-incidence set multiplicity. No assumption of sixset
    independence or right factor-map independence.
    """
    if (type(host_coordinates) is not int or host_coordinates < 6
            or not isinstance(source,dict)
            or "records" not in source or "static_eligible" not in source):
        raise ValueError("valid original LEFT compiled source and host required")
    expected = Counter()
    population = Counter()
    expanded = 0
    for tag, right_lines, signature, multiplicity in source["records"]:
        if (tag not in TAGS or type(multiplicity) is not int or multiplicity <= 0
                or len(right_lines)!=6):
            raise ValueError("invalid tagged ORIGINAL left source fiber")
        if tag == "D6":
            if signature is None:
                raise ValueError("D6 needs original connected LEFT dual signature")
            p = d6_signature_probability(host_coordinates)
        else:
            rp = tuple(sorted(Counter(right_lines).values(),reverse=True))
            p = profile_probability(host_coordinates,rp)
        expected[tag] += multiplicity*p
        population[tag] += multiplicity
        expanded += multiplicity
    if expanded!=source["static_eligible"]:
        raise AssertionError("compressed original source multiplicities lost")
    return {
        "host_coordinates":host_coordinates,
        "original_static_left_eligible":expanded,
        "by_tag_population":{t:population[t] for t in TAGS},
        "by_tag_expected":{t:expected[t] for t in TAGS},
        "conditional_right_mean":sum(expected.values(),Fraction(0)),
        "exact_uniform_complete_right_injection_mean":True,
        "does_not_bound_minimum_or_signed_discrepancy":True,
    }


def right_mean_from_independent_sixsets(sources, fixed_left, host_coordinates):
    """Independent uncompressed original LEFT set source; NOT a sample of all J.

    The caller must provide EVERY original sixset physically eligible
    under THIS fixed f, not only those accepted by one particular g.
    """
    total = Fraction(0)
    by_tag = Counter()
    population = Counter()
    n=0
    for six in sources:
        n+=1
        tag=source_profile(six)
        if tag is None:
            continue
        value=source_right_mean(six,fixed_left,host_coordinates)
        # D6 left physically eligible but disconnected is zero.
        if not value:
            continue
        total+=value
        by_tag[tag]+=value
        population[tag]+=1
    return {"source_candidates_examined":n,
            "conditional_right_mean":total,
            "by_tag_expected":{t:by_tag[t] for t in TAGS},
            "by_tag_population":{t:population[t] for t in TAGS},
            "no_source_independence_or_sample_extrapolation":True}


def _edge_universe(a):
    if type(a) is not int or a < 6:
        raise ValueError("physical host must have integer a>=6")
    return tuple(combinations(range(a),2))


def _validated_pins(a, pins):
    edges=_edge_universe(a)
    accepted=set(edges)
    if (not isinstance(pins,dict)
            or any(type(l) is not int or not isinstance(e,tuple) or e not in accepted
                   for l,e in pins.items())
            or len(set(pins.values()))!=len(pins)):
        raise ValueError("pins must assign distinct original lines to distinct K_a edges")
    return edges


def pinned_source_right_probability(six, fixed_left, host_coordinates, pins,
                                    *, max_states=100000):
    """Exact conditional expectation of ONE source given full-map right pins.

    Enumerate only the UNKNOWN original lines of THIS source, without
    treating any original sixsets or other global line assignments as
    independent. The distribution of source-line images is uniformly
    injective among the remaining physical edges. Limit prohibits
    accidentally huge completion enumeration; this is a proof oracle,
    not an all-h polynomial-time algorithm.

    For <=1 pin, coordinate transitivity proves equality to unpinned mean
    without enumeration. For >=2 pins, enumerate k <=6 unknown source lines.
    """
    edges = _validated_pins(host_coordinates, pins)
    if type(max_states) is not int or max_states < 1:
        raise ValueError("positive exact enumeration budget required")
    if len(pins) > len(edges):
        raise ValueError("more pins than host edges")
    if len(pins) <= 1:
        return source_right_mean(six,fixed_left,host_coordinates)
    t=source_profile(six)
    if t is None:
        return Fraction(0)
    left_ok,left_sig = physical_factor_state(six,fixed_left,left=True)
    if not left_ok or (t=="D6" and left_sig is None):
        return Fraction(0)
    source_lines=tuple(sorted({l for _,l in six}))
    missing=tuple(l for l in source_lines if l not in pins)
    available=tuple(e for e in edges if e not in set(pins.values()))
    count=perm(len(available),len(missing)) if len(available)>=len(missing) else 0
    if not count:
        raise ValueError("pins leave too few physical edges for ORIGINAL source")
    if count>max_states:
        raise ValueError("exact conditional completion budget exceeded")
    accepted=0
    for remaining in permutations(available,len(missing)):
        mapping=dict(pins)
        mapping.update(zip(missing,remaining))
        right_ok,right_sig=physical_factor_state(six,mapping,left=False)
        if t=="D6":
            accepted+=int(right_sig is not None and right_sig==left_sig)
        else:
            accepted+=int(right_ok)
    return Fraction(accepted,count)


def two_edge_orbit_certificate(six, fixed_left, host_coordinates,
                               first_line, second_line, *, max_states=100000):
    """TWO complete-right-map pin orbits: adjacent vs vertex-disjoint edges.

    Any fixed physical edge is conjugate to (0,1) under coordinate S_a.
    With (0,1) pinned, an edge for second_line has two coordinate-orbits:
      2(a-2) edges sharing one endpoint and C(a-2,2) disjoint edges.
    The right score (including D6 signatures) is invariant under physical
    coordinate relabeling on RIGHT ALONE, so the two conditional means are
    EXACT orbit values. The conditional average is the unpinned mean.
    """
    if (type(first_line) is not int or type(second_line) is not int
            or first_line == second_line):
        raise ValueError("two distinct ORIGINAL right lines required")
    a=host_coordinates
    adjacent = pinned_source_right_probability(
        six,fixed_left,a,{first_line:(0,1),second_line:(0,2)},
        max_states=max_states)
    disjoint = pinned_source_right_probability(
        six,fixed_left,a,{first_line:(0,1),second_line:(2,3)},
        max_states=max_states)
    one_pin=pinned_source_right_probability(
        six,fixed_left,a,{first_line:(0,1)},max_states=max_states)
    unconditional=source_right_mean(six,fixed_left,a)
    m=comb(a,2)
    adjacent_weight=2*(a-2)
    disjoint_weight=comb(a-2,2)
    if (adjacent_weight+disjoint_weight!=m-1 or
            one_pin != unconditional or
            adjacent*adjacent_weight+disjoint*disjoint_weight !=
            (m-1)*unconditional):
        raise AssertionError("exact first-pin zero and two physical-edge orbit identity failed")
    tag=source_profile(six)
    right_lines={l for _,l in six}
    rp=tuple(sorted(Counter(l for _,l in six).values(),reverse=True))
    if (tag is not None and rp==PROFILE_C
            and first_line in right_lines and second_line in right_lines
            and adjacent != 0):
        raise AssertionError("repeated-right-C 3-edge matching forbids intersecting pinned edges")
    return {
        "tag":tag,"original_right_profile":rp,
        "single_pin_mean":one_pin,"unconditional_mean":unconditional,
        "two_adjacent_pins_mean":adjacent,
        "two_disjoint_pins_mean":disjoint,
        "adjacent_second_edge_count":adjacent_weight,
        "disjoint_second_edge_count":disjoint_weight,
        "complete_second_edge_options":m-1,
        "orbit_weighted_identity_verified":True,
        "no_worst_case_floor_or_independent_sixsets_inferred":True,
    }


def exact_centered_discrepancy(mean, observed_score):
    """Signed distance of one observed complete g to E_g S(f,g)."""
    if (not isinstance(mean,Fraction)
            or type(observed_score) is not int or observed_score < 0):
        raise ValueError("exact rational expectation and nonnegative integer score required")
    signed=mean-observed_score
    return {"conditional_right_mean":mean,"one_global_right_score":observed_score,
            "signed_mean_minus_score":signed,"below_mean":signed>0,
            "not_uniform_lower_or_concentration":True}
