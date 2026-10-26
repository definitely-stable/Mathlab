"""Index named original factor partitions separately from physical projections.

No new positivity claim is made. Powers are independent-uniform-label
necessary leaflessness UPPER exponents, not bounds for correlated maps.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from hyp105_g5e2b3_forests import (
    restricted_growth_partitions, profile_for, projection_power_loss,
    six_projection_coefficients, is_six_factor_forest, integer_partitions,
)


def independent_forest(left, right):
    """A separate DFS graph-cycle oracle, not union-find."""
    edges = tuple(zip(left, right))
    if len(set(edges)) != 6:
        return False, 0
    adj = {}
    for p, l in edges:
        u, v = ("P", p), ("L", l)
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    visited, components = set(), 0
    def visit(u, parent):
        visited.add(u)
        for v in adj[u]:
            if v == parent:
                continue
            if v in visited or not visit(v, u):
                return False
        return True
    for u in adj:
        if u not in visited:
            components += 1
            if not visit(u, None):
                return False, components
    return True, components


def main(output_dir=None):
    outdir = Path(output_dir) if output_dir is not None else Path("/tmp/issue230-partition-index")
    outdir.mkdir(parents=True, exist_ok=True)
    parts = restricted_growth_partitions()
    assert len(parts) == 203
    rows, powers, leading_profiles = [], Counter(), Counter()
    for i, left in enumerate(parts):
        for j, right in enumerate(parts):
            forest, nc = independent_forest(left, right)
            assert forest == is_six_factor_forest(left, right)
            lp, rp = profile_for(left), profile_for(right)
            ll, rl = projection_power_loss(lp), projection_power_loss(rp)
            if not forest or ll is None or rl is None:
                continue
            assert nc == len(lp)+len(rp)-6
            power = Fraction(3*nc+6)-ll-rl
            assert power <= 6
            strata = "leading" if power == 6 else "subleading_necessary"
            powers[str(power)] += 1
            if strata == "leading":
                leading_profiles[f"{lp}/{rp}"] += 1
            rows.append(dict(
                index=f"L{i:03d}-R{j:03d}",
                left_original_partition="".join(map(str, left)),
                right_original_partition="".join(map(str, right)),
                left_original_profile="+".join(map(str, lp)),
                right_original_profile="+".join(map(str, rp)),
                source_forest_components=nc,
                left_physical_polynomial_key="+".join(map(str, lp)),
                right_physical_polynomial_key="+".join(map(str, rp)),
                independent_uniform_expected_upper_power=str(power),
                stratum=strata,
                physical_projection_and_GF5_signature="not_identified_by_source_partition",
            ))
    counts = Counter(row["stratum"] for row in rows)
    assert counts == {"leading": 631, "subleading_necessary": 11032}
    ledger = outdir / "original_partitions.csv"
    with ledger.open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    physical = {
        "+".join(map(str, profile)): {
            "named_factor_multiplicity_profile": profile,
            "physical_projection_falling_factorial_coefficients": {
                str(v): str(c) for v, c in six_projection_coefficients(profile)
            },
            "positive_GF5_weight_computed_here": False,
        }
        for profile in integer_partitions(6)
    }
    (outdir / "physical_projection_polynomials.json").write_text(
        json.dumps(physical, indent=2, sort_keys=True)+"\n")
    report = dict(
        named_endpoint_partitions_per_side=len(parts),
        source_partition_pairs_checked_by_two_forest_methods=len(parts)**2,
        indexed_rows=len(rows), stratum_counts=counts,
        independent_uniform_expected_upper_powers=powers,
        leading_original_profile_pairs=leading_profiles,
        ledger_sha256=hashlib.sha256(ledger.read_bytes()).hexdigest(),
        source_partitions_are_not_physical_projection_signatures=True,
        universal_correlated_risk_bound_proved=False,
    )
    (outdir / "partition-index-results.json").write_text(
        json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
