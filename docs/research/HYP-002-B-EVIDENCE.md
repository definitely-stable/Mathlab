# HYP-002-B — hosted CI evidence and sharp quadratic proof audit

**Research claim:** DERIVED THEOREM / NOT CLAIMED NOVEL / NOT LEAN-FORMALIZED.

Hosted GitHub Actions:
- Run https://github.com/definitely-stable/Mathlab/actions/runs/37765055502
- Tested head: 6e648f431c258f9cdf8f50776baab31b9f84f3c5
- Conclusion: **SUCCESS**
- All **64 unit tests** passed.
- Cross-repo curated research registry: RESEARCH_INDEX_VALIDATION_PASS, 51 entries.
- Existing G0/G1A/G2A/G2B/TOM and HYP-001/002-A gates succeeded.
- Four explicit new phase-B markers:
  HYP002_QUADRATIC_FINITE_BOUND_PASS,
  HYP002_PREFIX_FIBER_CERTIFICATE_PASS,
  HYP002_BOUNDARY_AND_WITNESS_PASS,
  HYP002_SHARP_EXPONENT_PHASE_B_PASS.

## Finite upper bound and witness checks

For finite field q>=2, r=q-1,

    A_q^set(m,3,2)
        <= r*m + r²*C(m,2)
           + min{ r³*C(m,3), r²*C(m,2)+C(r*m,2) }.

This is a universal closed-form **finite combinatorial upper bound**.
Its argument is mathematical: the canonical prefix-pair/suffix graph
must be C4-free (otherwise a forbidden signed 2+2 sum relation
exists). Each unordered right pair appears in <=1 prefix
neighborhood, giving the combinatorial counting result.

The lower bound for odd q comes from Steiner triple systems,
and the matching asymptotic order is Theta_q(m²).

Checks include:
- rectangle of four distinct columns creates an ASET collision
  for q=2,3,5,7;
- weighted-rectangle cancellation for q=5;
- a family with no prefix C4 that nevertheless has an ASET
  collision: confirms C4 absence is **not sufficient**;
- exhaustive small-case independent G1A oracle implications;
- affine STS(9), STS(27) remain independently ASET exact;
- union-equal pair collections need not violate ASET:
  blocks (012),(013),(014),(023) form an ASET-exact four-column
  example for odd q, but distinct edge-pair unions can coincide;
- 256 families of tripartite unit-encoded words with binary
  coordinate alphabets were checked for ASET versus
  2-separable descendant equivalence over GF(3);
- invalid/malformed columns and unsupported q fail closed.

## Novelty and open questions

The **general exponent is proved within the stated field model**,
but is strongly related to elementary C4-free counting and
published length-three 2-separable code bounds. No scientific
priority or publication originality is asserted; refer to
HYP-002-B-QUADRATIC-THEOREM.md for definition-level audit.

This evidence is **not** a Lean verification, interactive
formal proof, optimized encoder/decoder, or Rust crate prototype.

Next acceptable research: a narrowly scoped leading-constant
or efficient-decoding theorem with rigorous prior-art audit and
end-to-end memory cost model. The original "prove exponent 2"
question is CLOSED MATHEMATICALLY. The issue remains open for
literature/novelty decision only.
