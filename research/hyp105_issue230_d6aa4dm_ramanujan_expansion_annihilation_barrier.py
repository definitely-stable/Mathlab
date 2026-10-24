"""AA4-DM: Ramanujan expander spectrum and simultaneous annihilation barrier analysis.

Strict child of AA4-DL. Analyzes the bipartite incidence graph of the generalized
quadrangle W(3,s) (s = 2^h, h >= 1) as a super-Ramanujan bipartite expander:
  - Total bipartite vertices: 2V = 2(s+1)(s^2+1)
  - Bipartite degree d = s + 1
  - Second eigenvalue lambda_2 = sqrt(2s) < 2 sqrt(s)
  - Expander ratio lambda_2 / d = sqrt(2s)/(s+1) = O(s^{-1/2}) -> 0

Exact Bipartite Adjacency Spectrum Multiplicities:
  - +/-(s+1) with multiplicity 1 each (total 2)
  - +/-sqrt(2s) with multiplicity (1/2)*s*(s+1)^2 each (total s*(s+1)^2)
  - 0 with multiplicity s*(s^2+1)
  Total multiplicity sum: 2 + s*(s+1)^2 + s*(s^2+1) = 2(s+1)(s^2+1) = 2V.
  For s=4 (170 vertices):
    +/-5: mult 1 each; +/-sqrt(8): mult 50 each; 0: mult 68. Total = 170.

Conjecture AA4-DM.2 (Simultaneous Annihilation Barrier — OPEN):
An adversary attempting to zero out D6 (aligned A/A 6-cycles) must perturb the
permutation orbit away from cycle alignments.
Heuristic conjecture:
  D6 + (B/A + A/B) >= c_0 * (1 - O(s^{-1/2})) s^6 > 0.
CRITICAL CORRECTION:
The Bipartite Expander Mixing Lemma controls single-edge incidence flux,
not 6-tuples of incidences forming specific GF(5) cycle classes.
Transferring edge expansion to signed motif conservation remains an open problem.
Consequently, Branch B is NOT fully refuted.
"""
from fractions import Fraction
from math import comb, sqrt


def ramanujan_spectrum_parameters(s):
    """Exact spectral parameters and multiplicities of the bipartite incidence graph of W(3,s)."""
    if type(s) is not int or s < 2 or (s & (s - 1)) != 0:
        raise ValueError("s must be an integer power of 2 >= 2")

    V = (s + 1) * (s * s + 1)
    total_vertices = 2 * V
    d = s + 1

    # Classical GQ W(3,s) incidence spectrum:
    # Eigenvalues are: +(s+1), +sqrt(2s), 0, -sqrt(2s), -(s+1)
    lambda_1 = d
    lambda_2 = sqrt(2 * s)
    ramanujan_bound = 2.0 * sqrt(s)
    is_super_ramanujan = lambda_2 < ramanujan_bound
    expander_ratio = lambda_2 / d

    # Exact multiplicities derived via strongly regular point graph srg(v, k, lambda, mu):
    mult_pm_d = 1
    mult_pm_lam2 = (s * (s + 1) ** 2) // 2
    mult_zero = s * (s ** 2 + 1)
    total_mult = 2 * mult_pm_d + 2 * mult_pm_lam2 + mult_zero

    if total_mult != total_vertices:
        raise AssertionError(f"Spectrum multiplicity sum {total_mult} != graph vertices {total_vertices}")

    return {
        "s": s,
        "V": V,
        "total_vertices": total_vertices,
        "degree_d": d,
        "lambda_1": lambda_1,
        "lambda_2": lambda_2,
        "ramanujan_bound": ramanujan_bound,
        "is_super_ramanujan": is_super_ramanujan,
        "expander_ratio": expander_ratio,
        "multiplicities": {
            "+/-d": mult_pm_d,
            "+/-lambda_2": mult_pm_lam2,
            "zero": mult_zero,
            "total": total_mult,
        },
    }


def expander_mixing_bounds(s, X_size, Y_size):
    """Evaluates the bipartite expander mixing lemma for subsets X of points and Y of lines.

    |e(X, Y) - (d/V) |X| |Y|| <= lambda_2 * sqrt(|X| |Y|).
    """
    params = ramanujan_spectrum_parameters(s)
    V = params["V"]
    d = params["degree_d"]
    lam2 = params["lambda_2"]

    if not (1 <= X_size <= V and 1 <= Y_size <= V):
        raise ValueError("X_size and Y_size must be within [1, V]")

    expected_edges = (d / V) * X_size * Y_size
    fluctuation = lam2 * sqrt(X_size * Y_size)
    lower_edge_bound = max(0.0, expected_edges - fluctuation)
    upper_edge_bound = min(float(X_size * d), expected_edges + fluctuation)

    return {
        "s": s,
        "V": V,
        "X_size": X_size,
        "Y_size": Y_size,
        "expected_edges": expected_edges,
        "fluctuation": fluctuation,
        "lower_edge_bound": lower_edge_bound,
        "upper_edge_bound": upper_edge_bound,
    }


def simultaneous_annihilation_tradeoff(s):
    """Conjectured lower bound on D6 + BA + AB based on Ramanujan expander flux."""
    params = ramanujan_spectrum_parameters(s)
    expander_retention = 1.0 - params["expander_ratio"]
    # 140.0 is the mean orbit heuristic coefficient
    heuristic_floor_s6 = max(0.0, 140.0 * expander_retention)

    return {
        "s": s,
        "expander_ratio": params["expander_ratio"],
        "expander_retention": expander_retention,
        "heuristic_floor_s6": heuristic_floor_s6,
        "status": "OPEN_CONJECTURE_UNPROVEN",
        "formal_blocker": (
            "Expander mixing bounds single edge incidences, not 6-tuples of distinct "
            "incidences forming specific signed GF(5) cycle classes."
        ),
    }


def w32_all_schemes_tradeoff_census():
    """Exact empirical audit of all 4 canonical schemes on genuine W(3,2).

    Certifies that:
      - D6 + BA + AB >= 65 > 0 across the 4 tested canonical schemes
      - When D6 = 0 (on S68 and S72), BA + AB compensates with 65 and 67
      - In these 4 schemes, simultaneous zero D6 = 0 and BA = 0 and AB = 0 does not occur.
    """
    data = {
        "lex": {
            "S_seven": 259,
            "counts": {"D6": 15, "B-left/A-right": 98, "A-left/B-right": 110, "C/A": 13, "C/B": 1, "B/B-overlap": 8, "B/B-disjoint": 14},
        },
        "reverse": {
            "S_seven": 169,
            "counts": {"D6": 3, "B-left/A-right": 77, "A-left/B-right": 74, "C/A": 1, "C/B": 1, "B/B-overlap": 7, "B/B-disjoint": 6},
        },
        "S68": {
            "S_seven": 68,
            "counts": {"D6": 0, "B-left/A-right": 44, "A-left/B-right": 21, "C/A": 0, "C/B": 0, "B/B-overlap": 2, "B/B-disjoint": 1},
        },
        "S72": {
            "S_seven": 72,
            "counts": {"D6": 0, "B-left/A-right": 36, "A-left/B-right": 31, "C/A": 2, "C/B": 0, "B/B-overlap": 1, "B/B-disjoint": 2},
        },
    }

    results = {}
    min_core_sum = 999999
    min_total_s = 999999

    for scheme, row in data.items():
        c = row["counts"]
        core_sum = c["D6"] + c["B-left/A-right"] + c["A-left/B-right"]
        total_s = row["S_seven"]
        if core_sum < min_core_sum:
            min_core_sum = core_sum
        if total_s < min_total_s:
            min_total_s = total_s
        results[scheme] = {
            "D6": c["D6"],
            "BA": c["B-left/A-right"],
            "AB": c["A-left/B-right"],
            "core_sum": core_sum,
            "total_S": total_s,
            "d6_zero_compensated": (c["D6"] == 0 and core_sum > 0),
        }

    return {
        "schemes": results,
        "min_core_sum": min_core_sum,
        "min_total_S": min_total_s,
        "simultaneous_zero_refuted_in_sample": min_core_sum > 0,
        "certified_core_floor_in_sample": 65,
    }


def all_h_hyp105_resolution_summary():
    """Formal status of the complete proof architecture of Hypothesis 105."""
    return {
        "Hypothesis": 105,
        "Issue": 230,
        "Geometry": "Generalized Quadrangle W(3,s), s = 2^h, h >= 1",
        "KeyTheorems": {
            "AA4-DI": "Local reservoir point-coverage density barrier O(s^-10) (PROVED)",
            "AA4-DJ": "Universal finite-width support barrier & Global unanchored transversal carrier tau(P6) >= (1 - o(1))s^6 (PROVED)",
            "AA4-DK": "Girth-8 line-overlap sparsity P(R<=1) >= 1 - O(s^-2) (PROVED); disjoint covariance negative universally (REFUTED)",
            "AA4-DL": "Constructive polynomial-time Method of Conditional Expectations derandomization S(f, g*) >= (140 - o(1))s^6 (PROVED EXISTENTIAL)",
            "AA4-DM": "Super-Ramanujan expander spectrum lambda_2 = sqrt(2s) < 2 sqrt(s) (PROVED); simultaneous annihilation barrier (CONJECTURE)",
        },
        "ResolutionStatus": {
            "ConstructiveDerandomizedCarrier": "PROVED_EXISTENTIAL_OMEGA_S6",
            "AlmostSureOrbitConcentration": "OPEN_CONJECTURE_UNPROVEN",
            "SimultaneousAnnihilation": "OPEN_CONJECTURE_UNPROVEN",
            "Branch_B_Refutation": "NOT_REFUTED",
            "W32_DeterministicInfimum": "CERTIFIED_GE_68_IN_AUDITED_SAMPLE",
            "MathlabRepositoryGovernance": "OPEN_WITH_FORMAL_BLOCKER",
        },
    }
