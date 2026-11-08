"""AA4-DEGFACT: original GQ deletion-middle defect from local incidence degrees.

Independent finite W(3,2), W(3,4) symplectic constructors + two counting
oracles. All-h theorem is proved in the accompanying manuscript, NOT by
finite tests. Neither original pair labels nor earlier six-motif code used.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
import random

SCHEMA = "mathlab.hyp105.original-defect-local-degree-factor.v1"


def _mul(a, b, s):
    if s == 2:
        return a & b
    if s != 4:
        raise ValueError("finite oracle supports W(3,2), W(3,4) only")
    v = 0
    for _ in range(2):
        if b & 1:
            v ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # GF(4): x^2+x+1
    return v


def _normalized(vector, s):
    for first in vector:
        if first:
            inv = next(x for x in range(1, s) if _mul(first, x, s) == 1)
            return tuple(_mul(inv, x, s) for x in vector)
    raise ValueError("zero vector is not a projective point")


def _symplectic(a, b, s):
    return (_mul(a[0], b[2], s) ^ _mul(a[2], b[0], s)
            ^ _mul(a[1], b[3], s) ^ _mul(a[3], b[1], s))


def genuine_symplectic_source(s):
    """Build true GQ points and isotropic lines without repository fixtures."""
    if type(s) is not int or s not in (2, 4):
        raise ValueError("use actual characteristic-two finite fields 2 or 4")
    pts = sorted({_normalized(v, s) for v in product(range(s), repeat=4)
                  if any(v)})
    idx = {v: i for i, v in enumerate(pts)}
    lines = set()
    for a, b in combinations(pts, 2):
        if _symplectic(a, b, s):
            continue
        span = frozenset(idx[_normalized(tuple(
            _mul(u, x, s) ^ _mul(v, y, s) for x, y in zip(a, b)), s)]
            for u, v in product(range(s), repeat=2) if u or v)
        if len(span) != s + 1:
            raise AssertionError("isotropic line lost projective points")
        lines.add(tuple(sorted(span)))
    lines = sorted(lines)
    V = (s + 1) * (s*s + 1)
    if len(pts) != V or len(lines) != V:
        raise AssertionError("not true W(3,s) source cardinalities")
    flags = tuple((p, l) for l, line in enumerate(lines) for p in line)
    point_degrees = Counter(p for p, _ in flags)
    if len(flags) != (s + 1)*V or set(point_degrees.values()) != {s + 1}:
        raise AssertionError("not a regular original GQ incidence structure")
    return flags


def _source(s, flags):
    if type(s) is not int or s < 2:
        raise ValueError("s must be an integer >= 2")
    V = (s+1)*(s*s+1)
    flags = tuple(flags)
    if (len(flags) != (s+1)*V or len(set(flags)) != len(flags)
            or any(not isinstance(e, tuple) or len(e) != 2
                   or any(type(x) is not int or x < 0 or x >= V for x in e)
                   for e in flags)):
        raise ValueError("invalid named original incidence IDs")
    point_lines = [set() for _ in range(V)]
    line_points = [set() for _ in range(V)]
    id_of = {}
    for i, (p,l) in enumerate(flags):
        point_lines[p].add(l)
        line_points[l].add(p)
        id_of[p,l] = i
    if any(len(b) != s+1 for b in point_lines+line_points):
        raise ValueError("invalid original GQ point/line pencil degrees")
    return V, flags, point_lines, line_points, id_of


def _deleted(Z, N):
    Z = tuple(Z)
    if (len(Z) != len(set(Z)) or any(type(i) is not int or i < 0 or i >= N
                                      for i in Z)):
        raise ValueError("deleted set must contain DISTINCT valid original IDs")
    return frozenset(Z)


def degree_defect(s, flags, deleted_ids):
    """Exact O(|I|+|Z|) degree-only formula, for genuine W(3,s) input.

    Original source input checking O(|I|) can be amortized: after source
    verification, each new deletion query needs only O(|Z|) operations.
    """
    V, flags, _, _, _ = _source(s, flags)
    Z = _deleted(deleted_ids, len(flags))
    dpoint = Counter(flags[i][0] for i in Z)
    dline = Counter(flags[i][1] for i in Z)
    full_points = {p for p,d in dpoint.items() if d == s+1}
    full_lines = {l for l,d in dline.items() if d == s+1}
    residual = tuple(sorted(i for i in Z if flags[i][0] not in full_points
                            and flags[i][1] not in full_lines))
    contributions = tuple(sorted((i, (s+1-dpoint[flags[i][0]])
                                   *(s+1-dline[flags[i][1]])) for i in Z))
    D = sum(term for _,term in contributions)
    all_stars = (len(residual) == 0)
    if (D == 0) != all_stars:
        raise AssertionError("local factorization STAR iff invariant failed")
    if not (0 <= D <= s*s*len(Z)):
        raise AssertionError("middle original source exposures exceeded")
    return {
        "s": s, "V": V, "original_flags": len(flags), "Z": len(Z),
        "D_local": D, "kappa": str(Fraction(D, s*s*len(Z))) if Z else "0",
        "full_point_stars": tuple(sorted(full_points)),
        "full_line_stars": tuple(sorted(full_lines)),
        "uncovered_original_IDs": residual,
        "union_of_complete_point_line_stars": all_stars,
        "M_upper_from_local_D": 8*s*s*len(Z) + 4*D,
        "original_universal_M_upper": 12*s*s*len(Z),
        "contributions": contributions,
    }


def projection_defect(s, flags, deleted_ids):
    """Independent all nonincident (q,r) GQ projection count oracle.

    Deliberately does NOT use degree_defect or its factor formula.
    """
    V, flags, point_lines, line_points, id_of = _source(s, flags)
    Z = _deleted(deleted_ids, len(flags))
    connecting_line = {}
    for l, ps in enumerate(line_points):
        for p, q in combinations(sorted(ps), 2):
            if (p,q) in connecting_line:
                raise AssertionError("GQ point pair on two original lines")
            connecting_line[p,q] = connecting_line[q,p] = l
    roles = [[0]*len(flags) for _ in range(3)]
    D = H = F = M = projected = 0
    for q in range(V):
        for r in range(V):
            if (q,r) in id_of:
                continue
            possibilities = [(p,connecting_line[q,p]) for p in line_points[r]
                             if (q,p) in connecting_line]
            if len(possibilities) != 1:
                raise AssertionError("true GQ nonincident projection not unique")
            p, ell = possibilities[0]
            anchors = (id_of[q,ell], id_of[p,ell], id_of[p,r])
            if len(set(anchors)) != 3:
                raise AssertionError("original projection anchors repeated")
            for k, i in enumerate(anchors):
                roles[k][i] += 1
            b1,b2,b3 = (a in Z for a in anchors)
            D += int(b2 and not b1 and not b3)
            H += int(b1 and b2 and b3)
            F += int(b1 and not b2 and b3)
            M += 4*int(b1 or b2 or b3)
            projected += 1
    if projected != V*(V-s-1) or any(
            any(x != s*s for x in role) for role in roles):
        raise AssertionError("true original GQ anchor roles not s^2")
    if M != 8*s*s*len(Z)+4*(D-H-F):
        raise AssertionError("independent original full-GQ physical mask identity false")
    return {"D_projection":D,"H":H,"F":F,"M_projection":M,
            "projection_count":projected,"three_roles_s2":True}


def _cases(s, flags):
    V = (s+1)*(s*s+1)
    id_of = {f:i for i,f in enumerate(flags)}
    point0 = {i for i,(p,l) in enumerate(flags) if p==0}
    line0 = {i for i,(p,l) in enumerate(flags) if l==0}
    extra = next(i for i in range(len(flags)) if i not in point0)
    cases = {"empty":set(), "single":{0},"point-star":point0,
             "line-star":line0,"mixed-star":point0|line0,
             "point-star-plus-one":point0|{extra},
             "full-original-I":set(range(len(flags)))}
    l1 = next(l for l in range(V) if (0,l) not in id_of)
    cases["mixed-nonincident-stars"] = point0 | {
        i for i,(p,l) in enumerate(flags) if l==l1}
    cases["incomplete-point-star"] = set(sorted(point0)[:-1])
    rng = random.Random(102305+s)
    for j in range(9 if s==2 else 6):
        prob = (j+1)/14
        cases[f"seeded-adversarial-{j}"]={i for i in range(len(flags))
                    if rng.random()<prob}
    return cases


def canonical_certificate():
    entries=[]
    for s in (2,4):
        flags=genuine_symplectic_source(s)
        for label,Z in _cases(s,flags).items():
            by_degree=degree_defect(s,flags,Z)
            by_projection=projection_defect(s,flags,Z)
            assert by_degree["D_local"] == by_projection["D_projection"]
            assert by_projection["M_projection"] <= by_degree["M_upper_from_local_D"]
            entries.append({"s":s,"case":label,"Z":len(Z),
                 "D":by_degree["D_local"],
                 "kappa":by_degree["kappa"],
                 "is_full_star_union":by_degree["union_of_complete_point_line_stars"],
                 "number_uncovered":len(by_degree["uncovered_original_IDs"]),
                 "M_exact":by_projection["M_projection"],
                 "M_D_upper":by_degree["M_upper_from_local_D"],
                 "original_GQ_roles_s2":by_projection["three_roles_s2"]})
    return {"schema":SCHEMA,"issue":230,"status":"OPEN_WITH_FORMAL_BLOCKER",
            "claim":"ALL-h exact local factorization and iff full STAR union",
            "new_root_A_PROVED":False,"new_ASET_exponent":False,
            "finite_verified_orders":[2,4],"independent_cases":entries}


if __name__ == "__main__":
    print("AA4_ORIGINAL_DEGFACT_CERTIFICATE="+json.dumps(canonical_certificate(),sort_keys=True,separators=(",",":")))
