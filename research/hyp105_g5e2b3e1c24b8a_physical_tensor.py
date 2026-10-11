"""HYP-105 C24-B8-A: exact all-h physical-motif tensor, no new R3 bound.

For a fixed ORIGINAL six-incidence set J, the six ordinary positive families
have acceptance L_J(f) R_J(g). The D6 family instead has acceptance
sum_sigma L_(J,sigma)(f) R_(J,sigma)(g), with sigma an ordered-column
dual connected six-cycle on the six incidence POSITIONS. This cannot be
replaced with an ordinary binary product.

The mixed finite difference is the dot product of left and right state
differences, an exact identity for any genuine GQ and global injections.
This module does NOT establish Omega(s**6), an infinite counterfamily, or
complete GF(5) R3.
"""
from collections import Counter

A = (1, 1, 1, 1, 1, 1)
B = (2, 1, 1, 1, 1)
C = (2, 2, 2)
TAGS = ("D6", "B-left/A-right", "A-left/B-right", "C/A", "C/B",
        "B/B-overlap", "B/B-disjoint")


def source_profile(six):
    """Assign exactly one original seven-family tag, independently of f,g."""
    six = tuple(six)
    if (len(six) != 6 or len(set(six)) != 6
            or any(not isinstance(x, tuple) or len(x) != 2
                   or any(type(t) is not int for t in x) for x in six)):
        raise ValueError("six distinct original typed integer incidences required")
    pts = Counter(p for p, _ in six)
    lines = Counter(l for _, l in six)
    lp, rp = tuple(sorted(pts.values(), reverse=True)), tuple(sorted(lines.values(), reverse=True))
    if lp == A and rp == A:
        return "D6"
    if lp == B and rp == A:
        return "B-left/A-right"
    if lp == A and rp == B:
        return "A-left/B-right"
    if (lp, rp) in ((A, C), (C, A)):
        return "C/A"
    if (lp, rp) in ((B, C), (C, B)):
        return "C/B"
    if lp == rp == B:
        p = next(p for p in pts if pts[p] == 2)
        l = next(l for l in lines if lines[l] == 2)
        return "B/B-overlap" if (p, l) in six else "B/B-disjoint"
    return None


def physical_factor_state(six, mapping, *, left):
    """Return (eligible, D6 dual-cycle signature or None).

    The physical host may have any coordinate count >=6. Exactly six
    different physical vertices of degree two are required. A signature
    records which ORIGINAL incidence positions intersect at each physical
    coordinate, not an arbitrarily relabeled physical cycle.
    """
    physical = []
    degrees = Counter()
    incident_positions = {}
    for position, (p, l) in enumerate(six):
        e = tuple(mapping[p if left else l])
        if (len(e) != 2 or type(e[0]) is not int or type(e[1]) is not int
                or e[0] < 0 or e[0] >= e[1]):
            raise ValueError("invalid globally assigned physical coordinate pair")
        physical.append(e)
        for x in e:
            degrees[x] += 1
            incident_positions.setdefault(x, []).append(position)
    if len(degrees) != 6 or any(d != 2 for d in degrees.values()):
        return False, None
    # For an ORIGINAL D6 profile, physical pairs are distinct by global
    # injectivity; the six dual edges are a 2-regular graph on six columns.
    edges = tuple(sorted(tuple(sorted(positions)) for positions in incident_positions.values()))
    neighborhood = [set() for _ in range(6)]
    for u, v in edges:
        if u == v:
            raise AssertionError("one source incidence cannot appear twice in one coordinate")
        neighborhood[u].add(v)
        neighborhood[v].add(u)
    visited, stack = {0}, [0]
    while stack:
        for v in neighborhood[stack.pop()]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    # The disconnected two-triangle case is physical but NOT certified D6.
    signature = edges if len(visited) == 6 else None
    return True, signature


def _d6_state_delta(base, swapped):
    """Sparse difference of two one-hot cycle vectors (or the zero vector)."""
    out = Counter()
    if swapped[0] and swapped[1] is not None:
        out[swapped[1]] += 1
    if base[0] and base[1] is not None:
        out[base[1]] -= 1
    return {k: v for k, v in out.items() if v}


def _accepted(tag, left, right):
    if tag is None:
        return 0
    if tag == "D6":
        return int(left[1] is not None and left[1] == right[1])
    return int(left[0] and right[0])


def source_rectangle(six, f0, f1, g0, g1):
    """Four globally coherent maps: direct scores and tensor mixed term.

    D6 uses a dot product in signature space. Every other tag uses the
    product of Boolean eligibility differences, with absolute value <=1.
    """
    tag = source_profile(six)
    if tag is None:
        return None
    left0 = physical_factor_state(six, f0, left=True)
    left1 = physical_factor_state(six, f1, left=True)
    right0 = physical_factor_state(six, g0, left=False)
    right1 = physical_factor_state(six, g1, left=False)
    q00 = _accepted(tag, left0, right0)
    q10 = _accepted(tag, left1, right0)
    q01 = _accepted(tag, left0, right1)
    q11 = _accepted(tag, left1, right1)
    mixed = q11 - q10 - q01 + q00
    if tag == "D6":
        dl, dr = _d6_state_delta(left0, left1), _d6_state_delta(right0, right1)
        product = sum(weight * dr.get(signature, 0) for signature, weight in dl.items())
        joint = bool(dl and dr)
        cap = 2 if joint else 0
    else:
        dl = int(left1[0]) - int(left0[0])
        dr = int(right1[0]) - int(right0[0])
        product = dl * dr
        joint = bool(dl and dr)
        cap = int(joint)
    if product != mixed or abs(mixed) > cap:
        raise AssertionError("independent Boolean rectangle and factorized tensor disagree")
    return {"tag": tag, "direct": (q00, q10, q01, q11),
            "mixed": mixed, "tensor": product, "physical_joint_cap": cap,
            "both_physical_states_change": joint}


def audit_rectangle(sources, f0, f1, g0, g1):
    """Exact finite common-universe census, NOT an asymptotic theorem.

    sources MUST contain every original sixset eligible on the LEFT at
    either f0 or f1. This prevents an unsafe reused f0-only source.
    """
    total = [0, 0, 0, 0]
    by_tag = Counter()
    mixed_by_tag = Counter()
    caps_by_tag = Counter()
    examined = eligible = both_changed = 0
    for six in sources:
        examined += 1
        row = source_rectangle(six, f0, f1, g0, g1)
        if row is None:
            continue
        eligible += 1
        for i, x in enumerate(row["direct"]):
            total[i] += x
        by_tag[row["tag"]] += row["direct"][0]
        mixed_by_tag[row["tag"]] += row["mixed"]
        caps_by_tag[row["tag"]] += row["physical_joint_cap"]
        both_changed += int(row["both_physical_states_change"])
    kappa = total[3] - total[1] - total[2] + total[0]
    if kappa != sum(mixed_by_tag.values()) or abs(kappa) > sum(caps_by_tag.values()):
        raise AssertionError("sixset tensor score/physical exposure accounting mismatch")
    return {"original_sources_considered": examined, "seven_profile_sources": eligible,
            "S_00": total[0], "S_10": total[1], "S_01": total[2], "S_11": total[3],
            "mixed_curvature": kappa, "mixed_by_tag": {t: mixed_by_tag[t] for t in TAGS},
            "physical_joint_change_source_count": both_changed,
            "sharp_sourcewise_physical_cap": sum(caps_by_tag.values()),
            "cap_by_tag": {t: caps_by_tag[t] for t in TAGS},
            "mixed_tensor_identity_exact": True,
            "does_not_imply_positive_all_h_lower_bound": True}
