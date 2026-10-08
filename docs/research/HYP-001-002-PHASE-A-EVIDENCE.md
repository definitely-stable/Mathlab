# HYP-001/002 — Phase A finite construction evidence

**Date:** 2026-10-08
**Status:** FINITE CONSTRUCTION / ADVERSARIAL REGRESSION **ACCEPTED**
on [hosted CI run 37762380556](https://github.com/definitely-stable/Mathlab/actions/runs/37762380556).
Tested PR head: fa8d44a93f1cd08d631b58eab65935dff21b59ed.
Parent claims and self-contained argument:
[HYP-001-002-LOCALITY-TRANSITION.md](HYP-001-002-LOCALITY-TRANSITION.md).

## CI verification

- research workflow: SUCCESS;
- 49 unit tests: OK (includes six new locality-transition unit tests);
- research source-catalog validation: PASS (26 entries);
- G0/G1A/G2A, TOM-C and G2B retained and successful;
- HYP001_PROJECTIVE_CONSTRUCTION_PASS;
- HYP002_STEINER_CONSTRUCTION_PASS;
- HYP_ODD_CHARACTERISTIC_BOUNDARY_PASS;
- HYP_FALSIFICATION_CASES_PASS;
- HYP_LOCALITY_PHASE_A_PASS.

## Explicit finite witnesses (all d=2)

| construction | coordinates m | columns V | locality w | sketch fields |
|---|---:|---:|---:|---|
| PG(2,2) point-line incidence | 14 | 21 | 2 | GF(3), GF(5), GF(7) |
| PG(2,3) point-line incidence | 26 | 52 | 2 | GF(3), GF(5), GF(7) |
| Fano STS(7) | 7 | 7 | 3 | GF(3), GF(5), GF(7) |
| Affine STS(9) | 9 | 12 | 3 | GF(3), GF(5), GF(7) |
| Affine STS(27) | 27 | 117 | 3 | GF(3), GF(5) |

All were validated by the existing exact ASET subset-sum oracle.
Smaller fixtures were also checked by a separate pair-sum
enumeration implementation.

### Negative test evidence

- A support-two 4-cycle creates an illegal 2-versus-2 collision.
- A four-triple Pasch configuration is *linear* and ASET exact in
  odd characteristic but collides in GF(2).
- Four explicitly *nonlinear* triples (012),(345),(013),(245)
  have coincident 2-sums in odd characteristic.
- Nonprime q=4/9 and malformed blocks are rejected by the harness.

## Claim boundaries and current decision

The CI evidence shows concrete valid lower-bound witnesses, plus
counterexamples to overly broad model claims.

It does NOT:
- certify the general asymptotic proofs with Lean;
- independently prove a new theorem;
- establish novelty of the C4/STS reductions;
- prove the HYP-002 quadratic upper bound;
- demonstrate a production-grade decoder or Rust crate.

**HYP-001:** DERIVED THETA BASELINE — proof recorded, originality UNKNOWN.
**HYP-002:** CONJECTURE REMAINS OPEN — only Omega(m²)/O(m^(5/2))
brackets derived. Next task #25: model-specific prior-art audit and
sharper upper bound or explicit falsifying construction.

The Phase A acceptance markers cannot promote any claim directly
to manuscript / G4 / Rust implementation.
