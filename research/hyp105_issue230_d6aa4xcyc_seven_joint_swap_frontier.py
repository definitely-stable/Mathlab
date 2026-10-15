"""HYP-105 / issue #230 / D6-AA4-X-CYC: exact genuine-original seven-class
deterministic one-line-label-transposition frontier for W(3,2).

ALL-h support theorem (not an all-h obstruction): for any fixed global f
and any complete g, exchanging physical labels of two ORIGINAL source
lines u,v changes the accepted-class indicator of an ORIGINAL six-incidence
set Q only if at least one of its actual line endpoints is u or v.
Consequently the S, D6 and selected GF5 weighted numerator differences
are EXACT sums over that sparse original flag-supported family.

Finite implementation: retain ALL 62,370 genuine ORIGINAL left physical
sixset candidates for a fixed true W(3,2) f, classify the corresponding
true six incidence IDs under ONE globally coherent g, then visit EVERY
105 transposition of the 15 original line labels. No independent maps
per sixset, no new hypothetical source incidences, no stochastic sampling,
and no unconditional min_{f,g} assertion.
"""
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, physical_column_dual,
    is_connected_column_cycle,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model, exact_ONE_side_original_projection_index,
    exact_two_sided_original_seven_join,
)

DEGREE_TWO_PACKED = sum(2 << (4 * c) for c in range(6))
SOURCE_TYPES = {
    (1, 1, 1, 1, 1, 1): "A",
    (2, 1, 1, 1, 1): "B",
    (2, 2, 2): "C",
}
NON_AA_CLASS = {
    ("A", "B"): "A-left/B-right",
    ("B", "A"): "B-left/A-right",
    ("A", "C"): "C/A",
    ("C", "A"): "C/A",
    ("B", "C"): "C/B",
    ("C", "B"): "C/B",
}


def packed_physical_edge(edge):
    """Six 4-bit degree lanes: no carry, since exactly six edges are summed."""
    u, v = edge
    if not (type(u) is int and type(v) is int and 0 <= u < v < 6):
        raise ValueError("canonical physical K6 pair required")
    return (1 << (4 * u)) + (1 << (4 * v))


def original_line_swap_support(Q, incidences, u, v):
    """Exact all-h indicator of whether swapping ORIGINAL lines can affect Q."""
    if len(Q) != 6 or len(set(Q)) != 6 or u == v:
        raise ValueError("six distinct ORIGINAL incidence IDs and distinct lines required")
    return any(incidences[j][1] in (u, v) for j in Q)


@dataclass(frozen=True)
class OriginalRow:
    original_Q: tuple
    original_lines: tuple
    left_kind: str
    right_source_kind: str
    non_AA_GF5_tag: str | None
    left_connected_C6_dual: tuple | None


class ExactRightLineSwapFrontier:
    """Finite true W32 full-global-g sparse derivative evaluator."""

    def __init__(self, model):
        inc, f, g = strict_true_W32_model(model)
        self.model = model
        self.incidences = inc
        self.fixed_f = f
        self.base_g = g
        one_side = exact_ONE_side_original_projection_index(model, 0)
        if len(one_side["candidate_sixset_map"]) != 62370:
            raise AssertionError("left genuine-original 62,370 candidate universe drift")
        self.rows = []
        self.support = [set() for _ in range(15)]
        for Q, lk in one_side["candidate_sixset_map"].items():
            ls = tuple(inc[j][1] for j in Q)
            profile = tuple(sorted(Counter(ls).values(), reverse=True))
            rk = SOURCE_TYPES.get(profile)
            if rk == "C" and lk == "C":
                raise AssertionError("true original GQ girth-eight C/C forbidden")
            tag = NON_AA_CLASS.get((lk, rk))
            if lk == rk == "B":
                pcounts = Counter(inc[j][0] for j in Q)
                lcounts = Counter(ls)
                p0 = next(x for x, n in pcounts.items() if n == 2)
                l0 = next(x for x, n in lcounts.items() if n == 2)
                both = sum(inc[j] == (p0, l0) for j in Q)
                if both not in (0, 1):
                    raise AssertionError("actual original B/B repeated endpoints invalid")
                tag = "B/B-overlap" if both else "B/B-disjoint"
            dual = None
            if lk == rk == "A":
                raw = physical_column_dual(inc, f, tuple(inc[j][0] for j in Q))
                if raw is None:
                    raise AssertionError("fixed true left A half missing physical 2factor")
                if is_connected_column_cycle(raw):
                    dual = raw
            row = OriginalRow(Q, ls, lk, rk, tag, dual)
            i = len(self.rows)
            self.rows.append(row)
            for l in set(ls):
                self.support[l].add(i)
        if len(self.rows) != 62370:
            raise AssertionError("incomplete true-original point-labelled left Q index")
        self.base_packed = tuple(packed_physical_edge(e) for e in g)
        self.base_tags = tuple(self._tag(r, g, self.base_packed)
                               for r in self.rows)
        self.base_counts = Counter(t for t in self.base_tags if t is not None)
        self.base = self._result(self.base_counts, None, 0, 0)

    def _tag(self, row, g, packed):
        if row.right_source_kind is None:
            return None
        if sum(packed[l] for l in row.original_lines) != DEGREE_TWO_PACKED:
            return None
        if row.left_kind == row.right_source_kind == "A":
            if row.left_connected_C6_dual is None:
                return None
            right = physical_column_dual(
                self.incidences, g, row.original_lines)
            if right != row.left_connected_C6_dual:
                return None
            return "D6"
        return row.non_AA_GF5_tag

    @staticmethod
    def _result(counts, swap, affected, changed):
        c = {tag: counts[tag] for tag in R3_CERTIFIED_FLOORS}
        if any(v < 0 for v in c.values()):
            raise AssertionError("negative original accepted GF5 class count")
        d6 = c["D6"]
        non_aa = sum(c.values()) - d6
        weight = sum(c[tag] * R3_CERTIFIED_FLOORS[tag] for tag in c)
        return {
            "swap_source_LINE_IDs": swap,
            "true_original_seven_classes": c,
            "D6": d6,
            "non_AA": non_aa,
            "S_seven": non_aa + d6,
            "selected_GF5_51palette_certified_numerator": weight,
            "affected_original_left_Q": affected,
            "changed_original_accepted_tags": changed,
        }

    def swap(self, u, v):
        if (type(u) is not int or type(v) is not int
                or not 0 <= u < v < 15):
            raise ValueError("two ordered different ORIGINAL line factors in 0..14 required")
        new_g = list(self.base_g)
        new_g[u], new_g[v] = new_g[v], new_g[u]
        new_packed = list(self.base_packed)
        new_packed[u], new_packed[v] = new_packed[v], new_packed[u]
        modified = self.support[u] | self.support[v]
        counts = self.base_counts.copy()
        changed = 0
        for i in modified:
            old = self.base_tags[i]
            new = self._tag(self.rows[i], new_g, new_packed)
            if old == new:
                continue
            changed += 1
            if old is not None:
                counts[old] -= 1
            if new is not None:
                counts[new] += 1
        result = self._result(counts, (u, v), len(modified), changed)
        if not (result["affected_original_left_Q"] > 0 and
                result["affected_original_left_Q"] < len(self.rows)):
            raise AssertionError("sparse true source-line swap support failure")
        return result

    def full_recount(self, swapped=None):
        """Independent of sparse-delta path: recompute all 62,370 original rows."""
        g = list(self.base_g)
        if swapped is not None:
            u, v = swapped
            g[u], g[v] = g[v], g[u]
        packed = tuple(packed_physical_edge(e) for e in g)
        counts = Counter()
        for row in self.rows:
            tag = self._tag(row, g, packed)
            if tag is not None:
                counts[tag] += 1
        return self._result(counts, swapped, len(self.rows), 0)

    def legacy_join_recount(self, swapped=None, historical=True):
        """Fully separate two-sided 62,370+62,370 hash-join and GF5 history."""
        g = list(self.base_g)
        if swapped is not None:
            u, v = swapped
            g[u], g[v] = g[v], g[u]
        other = {**self.model, "right_labels": tuple(g)}
        independent = exact_two_sided_original_seven_join(
            other, independent_history=historical)
        return {
            "D6": independent["physical_A_A_genuine_D6_only"],
            "S_seven": independent["accepted_seven_GF5_original_S"],
            "non_AA": independent["accepted_seven_GF5_original_S"]
                     - independent["physical_A_A_genuine_D6_only"],
            "selected_GF5_51palette_certified_numerator":
                independent["selected_GF5_51palette_certified_numerator"],
            "true_original_seven_classes":
                independent["accepted_seven_GF5_original_Q_by_tag"],
        }

    def exhaustive_105_neighbor_frontier(self):
        all_rows = [self.base]
        all_rows.extend(self.swap(u, v) for u, v in combinations(range(15), 2))
        if len(all_rows) != 1 + comb(15, 2):
            raise AssertionError("not all 105 global right transpositions examined")
        def tie_key(row):
            return (row["S_seven"], row["D6"],
                    tuple(row["swap_source_LINE_IDs"] or ()))
        by_score = sorted(all_rows, key=tie_key)
        zero = [x for x in all_rows if x["D6"] == 0]
        pairs = sorted(set((x["D6"], x["non_AA"]) for x in all_rows))
        frontier = [(d, n) for d, n in pairs
                    if not any((d1 <= d and n1 <= n and
                                (d1 < d or n1 < n))
                               for d1, n1 in pairs)]
        witnesses = []
        for d, n in frontier:
            candidate = min((r for r in all_rows
                             if r["D6"] == d and r["non_AA"] == n),
                            key=tie_key)
            witnesses.append(candidate)
        return {
            "scope": "W(3,2), fixed complete original point f, all 105 global line-label transpositions plus identity",
            "neighbors_checked": 105,
            "complete_global_line_bijections_compared": 106,
            "baseline": self.base,
            "min_S_witness": by_score[0],
            "min_D6_zero_nonAA_witness":
                min(zero, key=tie_key) if zero else None,
            "D6_zero_labelings_in_exact_neighborhood": len(zero),
            "D6_positive_labelings_in_exact_neighborhood":
                sum(r["D6"] > 0 for r in all_rows),
            "distinct_D6_nonAA_pairs": len(pairs),
            "pareto_frontier": witnesses,
            "min_S_over_one_swap_neighborhood_only_NOT_global": True,
            "all_h_adversarial_seven_class_obstruction_PROVED": False,
            "all_h_counterexample_family_PROVED": False,
        }


def report(schemes=("S68", "S72")):
    data = {}
    for scheme in schemes:
        oracle = ExactRightLineSwapFrontier(fixture(1, scheme))
        independent = oracle.legacy_join_recount(historical=True)
        for key in ("D6", "non_AA", "S_seven",
                    "selected_GF5_51palette_certified_numerator",
                    "true_original_seven_classes"):
            if oracle.base[key] != independent[key]:
                raise AssertionError("true historical GF5 baseline mismatch: " + key)
        x = oracle.exhaustive_105_neighbor_frontier()
        for chosen in (x["min_S_witness"],
                       x["min_D6_zero_nonAA_witness"]):
            if chosen is not None:
                swap = chosen["swap_source_LINE_IDs"]
                counted = oracle.legacy_join_recount(swap, historical=True)
                for key in independent:
                    if chosen[key] != counted[key]:
                        raise AssertionError("independent historical optimum mismatch: "+key)
        data[scheme] = x
    return {
        "slice": "HYP105-ISSUE230-D6-AA4-X-CYC-SEVEN-CLASS-LOCAL-SWAP-FRONTIER",
        "all_h_exact_sparse_swap_derivative_identity": True,
        "finite_true_original_W32_exact_full_105_transpositions": True,
        "fixed_f_source_LINE_label_permutations_only": True,
        "root_A": "OPEN", "root_B": "OPEN", "root_C": "OPEN",
        "schemes": data,
    }


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--scheme", choices=("S68", "S72"))
    opts = parser.parse_args()
    value = report((opts.scheme,) if opts.scheme else ("S68", "S72"))
    print(json.dumps(value, indent=2, sort_keys=True))
