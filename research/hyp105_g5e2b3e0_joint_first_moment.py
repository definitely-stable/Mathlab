"""HYP-105 B3.2-E0: simultaneous non-strict R2/R3 via one distribution.

Mathematical theorem: if E_uniform_injective R2 = mu2 and
E_uniform_injective R3 = mu3, then a SINGLE injected two-color labeling
obeys R2 <= 2*mu2 and R3 <= 2*mu3 (for positive mu_i).
A lexicographically tie-broken conditional-expectation construction
selects one such labeling. This proves neither efficient construction
nor o(s^6) six-trade risk nor any ASET exponent improvement.

The finite oracle below is a transparent demonstration of conditioning:
it evaluates a bounded table of nonnegative two-objective costs for all
two-sided injections. Cost functions need NOT be actual GF5 risk. Actual
all-h R2/R3 theorem follows from the accepted E2-B2/B3.0 bounds, NOT
from substituting bounded proxy costs for full GF5 risk.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from math import prod
import json


@dataclass(frozen=True)
class FiniteInjectionSpace:
    coordinates: int
    left_vertices: int
    right_vertices: int
    max_outcomes: int = 100_000

    def __post_init__(self):
        if (not all(isinstance(v, int) for v in
                    (self.coordinates, self.left_vertices,
                     self.right_vertices, self.max_outcomes))
                or self.coordinates < 2 or self.left_vertices < 0
                or self.right_vertices < 0 or self.max_outcomes < 1):
            raise ValueError("invalid finite injection dimensions")
        K = self.coordinates * (self.coordinates - 1) // 2
        if max(self.left_vertices, self.right_vertices) > K:
            raise ValueError("not enough unordered coordinate pairs")
        size = (prod(K-j for j in range(self.left_vertices))
                * prod(K-j for j in range(self.right_vertices)))
        if size > self.max_outcomes:
            raise ValueError("finite audit budget exceeded")

    @property
    def palette(self):
        return tuple(combinations(range(self.coordinates), 2))

    @property
    def size(self):
        K = len(self.palette)
        return (prod(K-j for j in range(self.left_vertices))
                * prod(K-j for j in range(self.right_vertices)))

    def completions(self):
        """Every ordered injective pair choice, exactly once, uniform."""
        palette = range(len(self.palette))
        for left in permutations(palette, self.left_vertices):
            for right in permutations(palette, self.right_vertices):
                yield left + right


def _rational_nonnegative(value):
    if isinstance(value, float) or isinstance(value, bool):
        raise ValueError("finite proof requires exact nonnegative rationals")
    try:
        q = Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError("finite proof requires exact rational cost") from exc
    if q < 0:
        raise ValueError("signed/negative event 'risk' is not supported")
    return q


def exact_joint_table(space, risk_oracle):
    """Finite independently checkable exact two-objective risk distribution.

    The oracle is for a complete assignment, not a conditional/historical
    guess. For full HYP-105 one would need the actual full 51^4/51^6 GF5
    signed-event risks, not a chosen 7-column witness sample.
    """
    entries = []
    for labels in space.completions():
        left = labels[:space.left_vertices]
        right = labels[space.left_vertices:]
        pair = risk_oracle(tuple(space.palette[i] for i in left),
                           tuple(space.palette[i] for i in right))
        if len(pair) != 2:
            raise ValueError("risk oracle must provide two objective values")
        entries.append((labels, tuple(_rational_nonnegative(v) for v in pair)))
    if len(entries) != space.size:
        raise AssertionError("injection enumeration lost probability mass")
    return tuple(entries)


def conditional_expectation_certificate(space, risk_oracle,
                                        left_weight=Fraction(1, 2)):
    """Greedy exact conditional expectations, with stable lexicographic ties.

    E[lambda R2/mu2+(1-lambda) R3/mu3] <= 1.
    Conditioning on each chosen left/right coordinate-pair assignment
    preserves uniform probability over remaining allowed injections.
    Chosen prefix has no larger conditional expectation than its parent.
    If mu_i is zero, that nonnegative risk vanishes in every completion.
    """
    lam = _rational_nonnegative(left_weight)
    if not 0 < lam < 1:
        raise ValueError("both objective weights must be strictly positive")
    entries = exact_joint_table(space, risk_oracle)
    mu = tuple(sum((pair[i] for _, pair in entries), Fraction()) /
               len(entries) for i in (0, 1))
    def score(pair):
        return ((lam*pair[0]/mu[0] if mu[0] else Fraction()) +
                ((1-lam)*pair[1]/mu[1] if mu[1] else Fraction()))
    start = sum((score(pair) for _, pair in entries), Fraction()) / len(entries)
    prefix = ()
    current = start
    history = []
    for pos in range(space.left_vertices + space.right_vertices):
        conditional = {}
        for symbol in range(len(space.palette)):
            matching = [(labels, pair) for labels, pair in entries
                        if labels[:pos+1] == prefix+(symbol,)]
            if matching:
                conditional[symbol] = (
                    sum((score(pair) for _, pair in matching), Fraction()) /
                    len(matching))
        if not conditional:
            raise AssertionError("no injective conditional completion")
        symbol = min(conditional, key=lambda x: (conditional[x], x))
        chosen = conditional[symbol]
        if chosen > current:
            raise AssertionError("conditional mean increased; oracle broken")
        prefix += (symbol,)
        history.append({"symbol": symbol, "remaining_mean": chosen})
        current = chosen
    selected = [(labels, pair) for labels, pair in entries if labels == prefix]
    if len(selected) != 1 or score(selected[0][1]) != current:
        raise AssertionError("terminal risk not the conditional expectation")
    chosen_pair = selected[0][1]
    for i, weight in enumerate((lam, 1-lam)):
        if mu[i] == 0 and chosen_pair[i] != 0:
            raise AssertionError("nonnegative zero expectation contradicted")
        if mu[i] and chosen_pair[i] > mu[i] / weight:
            raise AssertionError("Pareto envelope violated")
    return {
        "space_size": len(entries),
        "mean_R2": mu[0], "mean_R3": mu[1],
        "normalized_initial_mean": start,
        "choice_indices": prefix,
        "selected_left": tuple(space.palette[i]
                               for i in prefix[:space.left_vertices]),
        "selected_right": tuple(space.palette[i]
                                for i in prefix[space.left_vertices:]),
        "selected_R2": chosen_pair[0], "selected_R3": chosen_pair[1],
        "terminal_normalized_score": current,
        "lex_conditional_history": tuple(history),
        "same_labels_for_both": True,
        "guaranteed_ratio_R2": Fraction(1)/lam,
        "guaranteed_ratio_R3": Fraction(1)/(1-lam),
        "strict_R3_exponent": False,
        "aset_exponent_improved": False,
    }


def finite_pair_label_diagnostic(left, right):
    """NON-GF5 tiny toy objectives, intentionally NOT full R2/R3.

    Two nonnegative measurable costs depending on the SAME physical-pair
    injections. Cross-half equality compares pair names only, which is
    a controlled proxy like E_t, not a physical GF5 signed trade.
    """
    if len(left) != 2 or len(right) != 3:
        raise ValueError("expected two left and three right factor vertices")
    # Tree-shaped four-incidence graph: (p0,l0), (p0,l1),
    # (p1,l1), (p1,l2).
    inc = ((0, 0), (0, 1), (1, 1), (1, 2))
    matched = sum(left[i] == right[j] for i, j in inc)
    # A second, non-monotonic risk proxy counts opposed shared names.
    cycles = sum(left[0] == right[j] and left[1] == right[k]
                 for j in range(3) for k in range(3) if j != k)
    return Fraction(matched), Fraction(cycles)


def self_report():
    example = conditional_expectation_certificate(
        FiniteInjectionSpace(3, 2, 3), finite_pair_label_diagnostic)
    return {
        "scope": "generic classical first moment applied to accepted HYP-105",
        "uniform_all_h_joint_R2": "exists R2<=2*C2*s^4",
        "uniform_all_h_joint_R3": "same labels R3<=2*C3*s^6",
        "finite_toy_not_GF5_full_risks": True,
        "tiny_space": example["space_size"],
        "tiny_mean_R2": str(example["mean_R2"]),
        "tiny_mean_R3": str(example["mean_R3"]),
        "tiny_selected_R2": str(example["selected_R2"]),
        "tiny_selected_R3": str(example["selected_R3"]),
        "tiny_normalized_score": str(example["terminal_normalized_score"]),
        "tiny_lex_choices": example["choice_indices"],
        "all_h_strict_R3": False,
        "novel_all_h_exponent": False,
    }


if __name__ == "__main__":
    print(json.dumps(self_report(), sort_keys=True, indent=2))
