"""GIO-003/T3-B: template-certified obstruction under arbitrary incidence edits.

SOURCE SCOPE: a genuine balanced GQ is a *fixed spanning witness* on the same
point and line sets. The edited incidence system need not satisfy GQ axioms,
regularity, girth or projections. Historical six-ID source motifs are checked
on the edited source independently of any new projection choice.

The asymptotic implication is a corollary of merged #799, not a new general
spectral theorem. Numeric graph C6 inputs in sample ledgers are FORMAL ONLY.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
import argparse
import json
import random

from gio_generalized_gq import model, balanced_ledger
from gio_resilience import source_first_d6, source_first_bbo, greedy_pack
from hyp105_aa4_branch_a_integrated_referee import (
    source_d6, historical_bbo, flow_catalog,
)

SCHEMA = "mathlab.gio003.t3b.edit-certified.v1"
BASE_MAIN = "f42aa108a2f9e15dadebf5c45fa4923cc435742b"


def typed_adjacency(pairs):
    """Independent literal port-graph check; indices are SIX source owners."""
    if len(pairs) != 6 or any(len(pair) != 2 or pair[0] == pair[1] for pair in pairs):
        return None
    port = defaultdict(list)
    for i, pair in enumerate(pairs):
        for symbol in pair:
            port[symbol].append(i)
    if len(port) != 6 or any(len(ids) != 2 for ids in port.values()):
        return None
    return tuple(sorted(tuple(sorted(ids)) for ids in port.values()))


def is_six_cycle(edges):
    """Connected 2-regular simple graph on the six original owner positions."""
    if edges is None or len(set(edges)) != 6 or any(a == b for a, b in edges):
        return False
    adjacency = [set() for _ in range(6)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    if any(len(x) != 2 for x in adjacency):
        return False
    visited = {0}
    todo = [0]
    while todo:
        p = todo.pop()
        for q in adjacency[p]:
            if q not in visited:
                visited.add(q)
                todo.append(q)
    return len(visited) == 6


def literal_historical_class(source_flags, point_labels, line_labels):
    """Independent historical D6/BBo recognizer with NO GQ projection oracle.

    Note: 'produced aligned' is a provenance certificate from the old GQ.
    Here BBo means the historical source *structural* class, not a newly
    constructed path of the edited non-GQ geometry.
    """
    if len(source_flags) != 6 or len(set(source_flags)) != 6:
        return None
    p, l = zip(*source_flags)
    dx = typed_adjacency([point_labels[z] for z in p])
    dy = typed_adjacency([line_labels[z] for z in l])
    if dx is None or dy is None:
        return None
    if len(set(p)) == len(set(l)) == 6 and dx == dy and is_six_cycle(dx):
        return "D6"
    cp, cl = Counter(p), Counter(l)
    if sorted(cp.values()) == sorted(cl.values()) == [1, 1, 1, 1, 2]:
        rp = next(k for k, n in cp.items() if n == 2)
        rl = next(k for k, n in cl.items() if n == 2)
        if (rp, rl) in source_flags:
            return "BBo_historical"
    return None


def switch_with_forced_four_cycle(m):
    """Two-edge switch which CERTIFIABLY destroys GQ on all thick fixtures.

    Choose noncollinear p,q. Let L_q through q, project p onto L_q via
    a different line E and foot u!=q. Choose L_p through p, L_p!=E.
    Replace (p,L_p),(q,L_q) by (p,L_q),(q,L_p).
    Cycle p-E-u-L_q-p survives: 3 old flags plus one inserted flag.
    """
    if m["s"] < 2 or m["t"] < 2:
        raise ValueError("require a thick GQ")
    P = m["Vp"]
    for p in range(P):
        for q in range(P):
            if q == p or q in m["neighbors"][p]:
                continue
            for lq in sorted(m["on"][q]):
                foot, join = m["projection"][p, lq]
                assert foot != q and p not in m["lines"][lq]
                for lp in sorted(m["on"][p] - {join}):
                    removed = frozenset(((p, lp), (q, lq)))
                    added = frozenset(((p, lq), (q, lp)))
                    old = set(m["flags"])
                    if len(removed) != 2 or len(added) != 2:
                        continue
                    if not removed <= old or added & old:
                        continue
                    edited = (old - removed) | added
                    witness = ((p, join), (foot, join),
                               (foot, lq), (p, lq))
                    assert all(x in edited for x in witness)
                    assert len(set(witness)) == 4
                    assert p != foot and join != lq
                    return dict(removed=removed, added=added,
                                four_cycle=witness,
                                noncollinear_points=(p, q))
    raise AssertionError("no valid source edge-switch found")


def verify_edit(m, removed, added):
    """Fail-closed named source edit certificate with fixed factor labels."""
    old = set(m["flags"])
    removed, added = frozenset(removed), frozenset(added)
    if not removed <= old:
        raise ValueError("removed flags must belong to the fixed GQ witness")
    if added & old:
        raise ValueError("added flags must not belong to original GQ witness")
    if not added.isdisjoint(removed):
        raise ValueError("a removed flag is not a new insertion")
    if any(type(p) is not int or type(l) is not int or not 0 <= p < m["Vp"]
           or not 0 <= l < m["Vl"] for p, l in added):
        raise ValueError("insertions must use existing typed factor vertices")
    if len(set(m["f"])) != m["Vp"] or len(set(m["g"])) != m["Vl"]:
        raise ValueError("point/line labels must be globally injective")
    if comb(m["aP"], 2) < m["Vp"] or comb(m["aP"]-1, 2) >= m["Vp"]:
        raise ValueError("point alphabet is not minimal")
    if comb(m["aL"], 2) < m["Vl"] or comb(m["aL"]-1, 2) >= m["Vl"]:
        raise ValueError("line alphabet is not minimal")
    edited = frozenset((old - removed) | added)
    return dict(original=frozenset(old), edited=edited,
                removed=removed, added=added,
                witness_to_edited=frozenset(old & edited),
                added_flags=len(added), deleted_GQ_flags=len(removed),
                original_count=len(old), edited_count=len(edited))


def actual_missing_projections(edited, point_count, line_count):
    """Exact missed (point,line) pairs on any edited source, even with C4/C6.

    Counts existence of at least one length-three path, NOT uniqueness.
    Does not reuse the frozen old GQ 'projection' dict.
    """
    per_line = [set() for _ in range(line_count)]
    per_point = [set() for _ in range(point_count)]
    for p,l in edited:
        if type(p) is not int or type(l) is not int or not 0 <= p < point_count or not 0 <= l < line_count:
            raise ValueError("edited source endpoint outside original factors")
        per_line[l].add(p)
        per_point[p].add(l)
    adjacent = [set() for _ in range(point_count)]
    for p in range(point_count):
        for ell in per_point[p]:
            adjacent[p].update(per_line[ell]-{p})
    missing = set()
    for q in range(point_count):
        for r in range(line_count):
            if q not in per_line[r] and not (adjacent[q] & per_line[r]):
                missing.add((q,r))
    return missing


def independent_signature_check(m, edited, source_ids, expected_class):
    """Two classification implementations and identity-of-support checksum.

    Uses literal new source tuple -> different IDs for old preserved names;
    never borrows the original GQ projection table for the edited class.
    """
    names = tuple(m["flags"][i] for i in source_ids)
    if not set(names) <= edited:
        raise AssertionError("a deleted original column survived")
    literal = literal_historical_class(names, m["f"], m["g"])
    if literal != expected_class:
        raise AssertionError(("historical shape lost", expected_class, literal))
    new_order = tuple(sorted(edited))
    new_ids = {flag: j for j, flag in enumerate(new_order)}
    new_model = dict(m, flags=new_order, flag_to_id=new_ids)
    selected = tuple(sorted(new_ids[x] for x in names))
    if expected_class == "D6":
        assert source_d6(new_model, selected) is not None
        assert not historical_bbo(new_model, selected)
    elif expected_class == "BBo_historical":
        assert historical_bbo(new_model, selected)
        assert source_d6(new_model, selected) is None
    else:
        raise ValueError("unknown class")
    # Fixed factor maps => the actual GF5 support/coordinate incidence
    # signature is identical before and after any source insertion.
    signature = tuple(sorted((m["f"][p], m["g"][l]) for p, l in names))
    other = tuple(sorted((new_model["f"][p], new_model["g"][l])
                         for p, l in names))
    assert signature == other
    return True


def finite_case(kind, scheme="lex"):
    m = model(kind, scheme)
    sw = switch_with_forced_four_cycle(m)
    edit = verify_edit(m, sw["removed"], sw["added"])
    assert len(edit["edited"]) == len(m["flags"])  # regular two-edge switch
    assert edit["added"] - edit["original"] == edit["added"]
    # Independently verify actual degrees, the new literal cycle, and that
    # no old GQ incidence point/line label has changed.
    source_on = Counter(p for p, l in edit["edited"])
    source_per_line = Counter(l for p, l in edit["edited"])
    assert set(source_on.values()) == {m["t"]+1}
    assert set(source_per_line.values()) == {m["s"]+1}
    assert len(source_on) == m["Vp"] and len(source_per_line) == m["Vl"]
    assert all(z in edit["edited"] for z in sw["four_cycle"])
    assert len({p for p, _ in sw["four_cycle"]}) == 2
    assert len({l for _, l in sw["four_cycle"]}) == 2
    assert any(z in sw["added"] for z in sw["four_cycle"])
    switched_missing = actual_missing_projections(edit["edited"],m["Vp"],m["Vl"])
    assert len(switched_missing) <= (3*m["s"]*m["t"]+1)*len(sw["removed"])

    ids = frozenset(range(len(m["flags"])))
    D = source_first_d6(m, ids)
    B = source_first_bbo(m, ids)
    assert not set(D).intersection(B)
    # Check independently the old sixset signature class BEFORE using it
    # as a certified stable witness in the edited geometry.
    alive = {i for i in ids if m["flags"][i] in edit["edited"]}
    old_d = [k for k in sorted(D) if set(k) <= alive]
    old_b = [k for k in sorted(B) if set(k) <= alive]
    for key in old_d:
        assert independent_signature_check(m, edit["edited"], key, "D6")
    for key in old_b:
        assert independent_signature_check(m, edit["edited"], key, "BBo_historical")
    assert all(len(k) == 6 for k in old_d+old_b)
    # Additional adversarial deletion may hit original or inserted flags.
    rng = random.Random(793*37 + 11*m["s"] + m["t"])
    candidate = tuple(sorted(edit["edited"]))
    cases = [
        ("none", frozenset()),
        ("new_only", sw["added"]),
        ("old_one", frozenset((m["flags"][0],))),
        ("mixed", frozenset((m["flags"][0],)) | sw["added"]),
        ("source_sample", frozenset(rng.sample(candidate, min(4, len(candidate))))),
    ]
    post = []
    for title, U in cases:
        available = edit["edited"] - U
        filtered_d = [k for k in old_d if all(m["flags"][i] in available for i in k)]
        filtered_b = [k for k in old_b if all(m["flags"][i] in available for i in k)]
        # Independent source filter done from full original family, not from
        # the previously filtered family (checks deletion composition).
        from_full_d = [k for k in D if all(m["flags"][i] in available for i in k)]
        from_full_b = [k for k in B if all(m["flags"][i] in available for i in k)]
        assert set(filtered_d) == set(from_full_d)
        assert set(filtered_b) == set(from_full_b)
        for key in filtered_d:
            assert literal_historical_class(
                tuple(m["flags"][i] for i in key), m["f"], m["g"]) == "D6"
        for key in filtered_b:
            assert literal_historical_class(
                tuple(m["flags"][i] for i in key), m["f"], m["g"]) == "BBo_historical"
        actual_missing=actual_missing_projections(available,m["Vp"],m["Vl"])
        removed_old=edit["original"]-available
        assert len(actual_missing) <= (3*m["s"]*m["t"]+1)*len(removed_old)
        packed = greedy_pack(set(filtered_d)|set(filtered_b))
        assert all(len(x) == 6 for x in packed)
        used = set()
        for motif in packed:
            assert not used.intersection(motif)
            used.update(motif)
        post.append(dict(mask=title, removed_after_edit=len(U),
                         surviving_D6=len(filtered_d),
                         surviving_certified_BBo=len(filtered_b),
                         greedy_original_disjoint_packing=len(packed),
                         contains_inserted_flag=bool(U & sw["added"]),
                         actual_missing_projections=len(actual_missing),
                         removed_original_GQ_flags_total=len(removed_old),
                         bounded_by_3st_plus_one=True))
    return dict(kind=kind, scheme=scheme, s=m["s"], t=m["t"],
                original_flags=len(m["flags"]), edited_flags=len(edit["edited"]),
                switch_removed=tuple(sorted(sw["removed"])),
                switch_added=tuple(sorted(sw["added"])),
                explicit_four_cycle=sw["four_cycle"],
                original_D6=len(D), original_produced_BBo=len(B),
                edited_certified_D6=len(old_d),
                edited_certified_BBo=len(old_b),
                literal_and_independent_historical_classifier_agree=True,
                new_geometry_has_four_cycle=True,
                switched_missing_projections=len(switched_missing),
                switched_missing_3st_plus_one_bound=(3*m["s"]*m["t"]+1)*2,
                point_and_line_degrees_preserved=True,
                post_edit_masks=post)


def symbolic_transfer_ledger(b, C0=Q(1), c0=Q(1)):
    """Logical corollary parameters, NOT numerical published constants."""
    original = balanced_ledger(b, C0, c0)
    rho = Q(original["rho"])
    eta = rho/2
    delta = Q(original["delta"])
    p = Q(5175, 51**6)
    assert eta > 0 and eta*2 == rho and delta > 0
    # To exhibit the explicit two-flag non-GQ switch on an asymptotic
    # GQ family, ensure 2 <= eta*r^4 with a true exact integer root.
    target = (2/eta).__ceil__()
    rs = isqrt(isqrt(target))
    while rs**4 < target:
        rs += 1
    switch_r0 = max(int(original["sufficient_integer_r0"]), rs)
    assert eta*switch_r0**4 >= 2
    assert switch_r0 >= int(original["sufficient_integer_r0"])
    return dict(balance=b, FORMAL_ONLY=True,
                external_C6_numeric_constants_unknown=True,
                C0=str(C0), c0=str(c0), inherited_GQ_rho=str(rho),
                edited_source_deletion_radius_eta=str(eta),
                surviving_lower_delta=str(delta),
                r0=str(original["sufficient_integer_r0"]),
                sufficient_non_GQ_two_switch_r0=str(switch_r0),
                explicit_infinite_family="W(3,2^h) with h sufficiently large",
                original_change_gate="|I_GQ minus I_edited| <= eta*r^4",
                extra_deletion_gate="|U| <= eta*r^4",
                union_gate="|Z|+|U intersect I_GQ| <= 2*eta*r^4 = rho*r^4",
                all_insertions_allowed_without_new_spectral_claim=True,
                packing_lower="floor(eta*r^4/6)+1",
                iid_GF5_sign_probability_min=str(p),
                iid_GF5_chernoff="exp(-p*m/8)",
                exact_GF5_R3_floor_per_source_witness=str(Q(5643,51**6)),
                no_new_external_numerical_constants=True)


def certificate():
    examples = [finite_case(name) for name in
                ("W32", "W33", "Qminus24", "dualQminus42")]
    ledgers = [symbolic_transfer_ledger(b) for b in (1,2,3)]
    flow = flow_catalog()
    assert flow["palette"] == 51
    assert flow["d6_alternating"] == 5643
    assert min(flow["bbo_sign_counts"]) >= 5175
    return dict(schema=SCHEMA, issue=793, meta_issue=790, root_issue=230,
                base_main_sha=BASE_MAIN,
                claim="PROVED_GQ_TEMPLATE_EDIT_TRANSFER_NOT_GENERAL_ABSTRACT_T3",
                proof_input="accepted #793 T1/T2 uniform original-flag deletion resilience",
                finite_examples=examples, formal_ledgers=ledgers,
                GF5=dict(palette=51,D6_sign=5643,BBo_min_sign=5175),
                no_new_C6_spectral_estimate=True,
                no_non_template_T3_theorem=True,
                no_general_ASET_improvement=True,
                no_external_human_referee=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="gio003-t3b-edit-transfer.json")
    a = p.parse_args()
    obj = certificate()
    Path(a.out).write_text(json.dumps(obj, sort_keys=True, indent=2)+"\n",
                           encoding="utf-8")
    print("PASS_GIO003_T3B_EDIT_TRANSFER_CERTIFICATE")
