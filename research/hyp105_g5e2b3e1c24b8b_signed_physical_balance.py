"""HYP-105 C24-B8-B: signed physical-change balance and exact random-map mean.

Algebraic ALL-h facts for the ORIGINAL seven GF(5)-necessary motif families:
  (1) Signed joint physical change = reinforcing - opposing contributions,
      split by static original source tag, with D6 matched cycle signatures.
  (2) Typed swap involutions flip the signed mixed curvature; averaging over
      the entire uniform RIGHT global-injection orbit gives exactly zero.
  (3) Exact expectation of a fixed original six-incidence source under TWO
      independent uniform complete global edge injections follows from
      finite physical two-factor templates, with D6 connected-cycle matching.
These identities do NOT establish a worst-case positive S lower, sign-definite
gradient, all-h R3 upper, or a new ASET exponent.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial, perm

from hyp105_g5e2b3e1c24b8a_physical_tensor import (
    TAGS, physical_factor_state, source_profile, source_rectangle,
)

PROFILE_A = (1, 1, 1, 1, 1, 1)
PROFILE_B = (2, 1, 1, 1, 1)
PROFILE_C = (2, 2, 2)
TEMPLATE_COUNTS = {PROFILE_A: (70, factorial(6)),
                   PROFILE_B: (45, factorial(4)),
                   PROFILE_C: (15, factorial(3))}
SIGN_KEYS = ("gain_gain", "loss_loss", "gain_loss", "loss_gain")


def source_signed_transitions(six, f0, f1, g0, g1):
    """One ORIGINAL source, FOUR complete coherent typed global maps.

    Return signed *matched* physical transitions. D6 is a 60-coordinate
    one-hot state, not a Boolean 2-factor: two +/- transitions may overlap.
    """
    tag = source_profile(six)
    if tag is None:
        return None
    l0, l1 = (physical_factor_state(six, f, left=True) for f in (f0, f1))
    r0, r1 = (physical_factor_state(six, g, left=False) for g in (g0, g1))
    signs = Counter()
    if tag == "D6":
        left, right = Counter(), Counter()
        if l0[1] is not None:
            left[l0[1]] -= 1
        if l1[1] is not None:
            left[l1[1]] += 1
        if r0[1] is not None:
            right[r0[1]] -= 1
        if r1[1] is not None:
            right[r1[1]] += 1
        # A zero difference must NOT be called physical joint change.
        left = {k: v for k, v in left.items() if v}
        right = {k: v for k, v in right.items() if v}
        for sig in left.keys() & right.keys():
            dl, dr = left[sig], right[sig]
            if (dl, dr) == (1, 1):
                signs["gain_gain"] += 1
            elif (dl, dr) == (-1, -1):
                signs["loss_loss"] += 1
            elif (dl, dr) == (1, -1):
                signs["gain_loss"] += 1
            elif (dl, dr) == (-1, 1):
                signs["loss_gain"] += 1
            else:
                raise AssertionError("D6 signature transition outside {-1,+1}")
        physical_cap = 2 if left and right else 0
    else:
        dl, dr = int(l1[0])-int(l0[0]), int(r1[0])-int(r0[0])
        if dl and dr:
            signs[("gain_" if dl > 0 else "loss_") +
                  ("gain" if dr > 0 else "loss")] += 1
        physical_cap = int(bool(dl and dr))
    reinforcing = signs["gain_gain"] + signs["loss_loss"]
    opposing = signs["gain_loss"] + signs["loss_gain"]
    signed = reinforcing - opposing
    # Independent four-Boolean indicator route (different arithmetic).
    corners = source_rectangle(six, f0, f1, g0, g1)
    if (corners is None or corners["mixed"] != signed
            or reinforcing + opposing > physical_cap):
        raise AssertionError("signed transition and independent 4-corner tensor disagree")
    return {"tag": tag, "mixed": signed, "positive": reinforcing,
            "negative": opposing, "matched": reinforcing + opposing,
            "physical_cap": physical_cap,
            "four_scores": corners["direct"],
            "quadrants": {k: signs[k] for k in SIGN_KEYS}}


def exact_signed_fiber_census(sources, f0, f1, g0, g1):
    """Seven static original families, no event-vs-source ambiguity.

    Each J must appear once and contain SIX distinct original incidences.
    If LEFT assignments change, caller must provide union of both source
    populations or the complete ORIGINAL incidence sixset universe.
    """
    rows = Counter()
    positives, negatives, caps = Counter(), Counter(), Counter()
    quadrants = {t: Counter() for t in TAGS}
    seen = set()
    n = 0
    for six in sources:
        key = tuple(sorted(six))
        if key in seen:
            raise ValueError("duplicate ORIGINAL source sixset")
        seen.add(key)
        n += 1
        row = source_signed_transitions(key, f0, f1, g0, g1)
        if row is None:
            continue
        for i, x in enumerate(row["four_scores"]):
            rows[i] += x
        t = row["tag"]
        positives[t] += row["positive"]
        negatives[t] += row["negative"]
        caps[t] += row["physical_cap"]
        quadrants[t].update(row["quadrants"])
    pos, neg = sum(positives.values()), sum(negatives.values())
    cap = sum(caps.values())
    mixed = rows[3]-rows[1]-rows[2]+rows[0]
    if (mixed != pos-neg or pos+neg > cap or
            any(positives[t]-negatives[t] !=
                quadrants[t]["gain_gain"]+quadrants[t]["loss_loss"]-
                quadrants[t]["gain_loss"]-quadrants[t]["loss_gain"]
                for t in TAGS)):
        raise AssertionError("matched signed positive/negative fiber conservation failed")
    return {"original_sixsets_examined": n,
            "four_scores": tuple(rows[i] for i in range(4)),
            "kappa": mixed, "positive_matched": pos, "negative_matched": neg,
            "absolute_matched": pos+neg, "net_cancellation": 2*min(pos,neg),
            "exact_signed_absolute_bound": pos+neg,
            "physical_change_cap": cap, "by_tag": {
                t: {"positive": positives[t], "negative": negatives[t],
                    "signed": positives[t]-negatives[t],
                    "physical_cap": caps[t],
                    "quadrants": {k: quadrants[t][k] for k in SIGN_KEYS}}
                for t in TAGS},
            "all_h_exact_signed_decomposition": True,
            "no_uniform_sign_or_positive_lower_inferred": True}


def swap_orientation_sign_identity(f0, f1, g0, g1, four_scores):
    """ALL-h sign involution for fixed legal original typed transpositions.

    Swapping the orientation of LEFT or RIGHT edge of a four-map rectangle
    negates kappa. Swapping BOTH orientations preserves it. The entire
    right-injection orbit is closed under its global B transposition,
    hence the exact mean over that orbit is ZERO (not a lower bound).
    """
    if f0 == f1 or g0 == g1 or len(four_scores) != 4:
        raise ValueError("two nontrivial typed global swap directions required")
    q00, q10, q01, q11 = four_scores
    k = q11-q10-q01+q00
    flipped_left = q01-q11-q00+q10
    flipped_right = q10-q00-q11+q01
    flipped_both = q00-q01-q10+q11
    if (flipped_left, flipped_right, flipped_both) != (-k, -k, k):
        raise AssertionError("typed swap sign involution")
    return {"signed": k, "left_reversed": flipped_left,
            "right_reversed": flipped_right,
            "both_reversed": flipped_both,
            "uniform_complete_right_orbit_signed_mean": Fraction(0),
            "sign_unconditional_negative_theorem_impossible": True}


def profile_probability(host_coordinates, original_multiplicities):
    """Exact eligibility probability for ONE side under uniform GLOBAL injection.

    Equal-length original factor indices share ONE physical K_a edge.
    Each of k distinct original factors receives a different physical edge.
    This marginal law is uniform without any per-source independent choice.
    """
    if (type(host_coordinates) is not int or host_coordinates < 6
            or original_multiplicities not in TEMPLATE_COUNTS):
        raise ValueError("physical host a>=6 and A/B/C multiplicity required")
    templates, labelings = TEMPLATE_COUNTS[original_multiplicities]
    m = comb(host_coordinates, 2)
    k = len(original_multiplicities)
    return Fraction(comb(host_coordinates, 6)*templates*labelings, perm(m,k))


def d6_signature_probability(host_coordinates):
    """Exact per-FIXED six-position connected dual C6 signature marginal."""
    if type(host_coordinates) is not int or host_coordinates < 6:
        raise ValueError("physical host a>=6 required")
    return Fraction(comb(host_coordinates,6)*factorial(6),
                    perm(comb(host_coordinates,2),6))


def original_source_annealed_probability(six, host_coordinates):
    """True exact random-map mean per original source; not the worst-case inf.

    TWO complete physical-point/line injections are independent uniform
    random injections, while their assignments across distinct original
    sources are strongly correlated. Only cross-SIDE independence is used.
    """
    t = source_profile(six)
    if t is None:
        return Fraction(0)
    if t == "D6":
        p = d6_signature_probability(host_coordinates)
        return 60*p*p
    lc, rc = Counter(p for p,_ in six), Counter(l for _,l in six)
    a = tuple(sorted(lc.values(), reverse=True))
    b = tuple(sorted(rc.values(), reverse=True))
    return profile_probability(host_coordinates,a)*profile_probability(host_coordinates,b)


def exact_annealed_source_expectation(sources, host_coordinates):
    """Linearity-only expected S on a fixed source collection.

    For the FULL true GQ S, sources must be ALL original distinct
    six-incidence subsets, not f0-eligible sources or a chosen sample.
    """
    n=0
    counts=Counter()
    for six in sources:
        n += 1
        t = source_profile(six)
        if t:
            lc = tuple(sorted(Counter(p for p,_ in six).values(),reverse=True))
            rc = tuple(sorted(Counter(l for _,l in six).values(),reverse=True))
            counts[(t,lc,rc)] += 1
    total=Fraction(0)
    contributions={}
    for (t,lp,rp), k in sorted(counts.items()):
        if t == "D6":
            p = d6_signature_probability(host_coordinates)
            term = k*60*p*p
        else:
            term = k*profile_probability(host_coordinates,lp)*profile_probability(host_coordinates,rp)
        contributions[(t,lp,rp)] = term
        total += term
    return {"sources_seen": n, "expected_S": total,
            "contributions": contributions,
            "independent_uniform_complete_left_and_right_injections": True,
            "no_minimum_or_concentration_claim": True}
