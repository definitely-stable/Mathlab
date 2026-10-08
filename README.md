# Mathlab

Mathlab is a verification-first repository for mathematical research developed with explicit claim status, executable falsification/checking artifacts, and a path to formal proof.

The repository deliberately separates:

- mathematical statements from novelty claims;
- exact finite results from asymptotics;
- theorem-derived evidence from empirical evidence;
- research artifacts from publication-ready preprints;
- informal proofs from Lean-checked formalizations.

The operating pattern is adapted from the evidence discipline used in `definitely-stable/deltameter` and the manuscript/supporting-artifact separation visible in `openai/math`. Text and claims are original to this repository.

## Research discovery and evidence catalog

[Indexed research across Mathlab, DELSK, DeltaMeter, openai/math](docs/research/catalog/INDEX.md) — curated Russian summaries, immutable source pins, related results and verification levels. [Registry and maintenance rules](docs/research/catalog/README.md).

## Current research

### LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

Issue: #1.

`LENT-001` is a stable historical research identifier. The former public label **Locality–Entropy Trilemma** is deprecated: the accepted theorem is a state-space/update-locality tradeoff, not a general three-way impossibility theorem.

Research-program label: **Exact Additive Sketch Locality Frontier**.

Baseline theorem label: **Sparse-Update Hamming-Ball Bound for Exact Additive Set Sketches**.

We study additive sketches

```text
Phi(S) = sum_{x in S} a_x,  a_x in F_q^m
```

with worst-case exact injectivity for all `|S| <= d` and update columns satisfying `|supp(a_x)| <= w`.

The finite baseline is

```text
sum_{i=0}^d C(V,i)
    <=
sum_{j=0}^{min(dw,m)} C(m,j) (q-1)^j.
```

This bound is useful as an impossibility framework but is **not claimed novel**.

### Active post-foundation target — ASET

G1 now focuses on the exact sparse subset-sum extremal object

[
A_q^{\mathrm{set}}(m,w,d),
]

the maximum universe size for support-(w) vectors in (mathbb F_q^m) such that all subset sums of sets of size at most (d) are distinct.

The exact collision relation uses coefficients in ({-1,0,1}) with separate bounds on the number of positive and negative coefficients.

This matters because:

- for (q=2), the model collapses to known small-column GF(2) independence and strongly overlaps sparse parity-check literature;
- for (q>2), arbitrary-coefficient small-column independence is stronger than the exact set-sum condition and must not be treated as equivalent;
- classical Sidon/B_h/dissociated objects require a definition-level map before importing results;
- Mathlab locality is update/write locality, not LCC/LDC query locality.

G1A/G1B and G2A are complete. Active task:
[#14](https://github.com/definitely-stable/Mathlab/issues/14) — G2B
hard-support evidence. G2B-A yields exact A_3^set(4,2,2)=7 and certified
10<=A_5^set(3,2,2)<=15. The q=5 exact maximum remains unknown.

Research extensions: [HYP-001 (#24)](https://github.com/definitely-stable/Mathlab/issues/24)
provides a classical-order two-cell capacity proof; [HYP-002 (#25)](https://github.com/definitely-stable/Mathlab/issues/25)
has a derived sharp Theta_q(m²) result for fixed odd q; its earlier
conjecture is discharged. [Corrected Phase-B proof](docs/research/HYP-002-B-QUADRATIC-THEOREM.md)
and [historical Phase-A record](docs/research/HYP-001-002-LOCALITY-TRANSITION.md).
Neither target is a publication novelty claim.

HYP-002-C [affine two-ID decoder issue #34](https://github.com/definitely-stable/Mathlab/issues/34)
provides a table-free recovery construction under the promise of no more
than two distinct active IDs. [Product gate and overload collision](docs/research/HYP-002-C-AFFINE-DECODER-PROTOCOL.md)
show why dense trit state is not competitive with directly storing
two canonical IDs for this narrow task. No Rust crate is authorized.

Independent [TOM-001](https://github.com/definitely-stable/Mathlab/issues/15)
continues falsification-first scouting. TOM-001-C is an elementary STOP
novelty baseline, not a crate or theorem selection.

The next gate is not "prove a new theorem immediately". It is to freeze these boundaries, build the exact source-to-claim map, and only then decide whether ASET has a genuinely new sharp regime.

## Documentation authority

Read in this order:

1. [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)
2. [docs/research/README.md](docs/research/README.md)
3. [docs/research/LENT-001-PROTOCOL.md](docs/research/LENT-001-PROTOCOL.md)
4. [docs/research/LENT-001-G1A-PROTOCOL.md](docs/research/LENT-001-G1A-PROTOCOL.md)
5. [docs/research/LENT-001-CLAIMS.md](docs/research/LENT-001-CLAIMS.md)
6. [docs/research/LENT-001-G1-CORRECTIONS.md](docs/research/LENT-001-G1-CORRECTIONS.md)
7. [docs/research/LENT-001-FOUNDATION.md](docs/research/LENT-001-FOUNDATION.md)
8. [docs/research/LENT-001-PRIOR-ART.md](docs/research/LENT-001-PRIOR-ART.md)
9. [docs/research/DECISIONS.md](docs/research/DECISIONS.md)
10. [docs/research/OPEN-QUESTIONS.md](docs/research/OPEN-QUESTIONS.md)
11. [docs/ROADMAP.md](docs/ROADMAP.md)

Executable artifacts live under [research/](research/). Publication-ready material, when it exists, is promoted under [preprints/](preprints/). Formalization status is tracked under [lean/](lean/).

## Claim labels

Repository prose must distinguish:

- **THEOREM**
- **DERIVED RESULT**
- **EXACT NUMERICAL RESULT**
- **ASYMPTOTIC RESULT**
- **EMPIRICAL RESULT**
- **CONJECTURE**
- **PRIOR-ART**

A theorem can be accepted before Lean formalization, but its formalization status must remain explicit. A novelty claim requires the separate prior-art gate.

## Principles

1. Freeze definitions before searching for favorable statements.
2. Counterexamples and negative results are first-class outputs.
3. CI can falsify or verify finite artifacts; CI does not by itself prove a general theorem.
4. Exact arithmetic is preferred whenever practical.
5. Randomized evidence is never relabeled as worst-case proof.
6. Historical statements remain traceable after corrections.
7. Preprints are promotion artifacts, not scratchpads.
