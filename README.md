# Mathlab

Mathlab is a verification-first repository for mathematical research developed with explicit claim status, executable falsification/checking artifacts, and a path to formal proof.

The repository deliberately separates:

- mathematical statements from novelty claims;
- exact finite results from asymptotics;
- theorem-derived evidence from empirical evidence;
- research artifacts from publication-ready preprints;
- informal proofs from Lean-checked formalizations.

The operating pattern is adapted from the evidence discipline used in `definitely-stable/deltameter` and the manuscript/supporting-artifact separation visible in `openai/math`. Text and claims are original to this repository.

## Current research

### LENT-001 — Locality–Entropy Trilemma for Exact Additive Set Sketches

Issue: #1.

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

This bound is mathematically elementary and is **not claimed novel**. In the binary case the extremal problem maps directly to sparse parity-check matrices / bounded-column-weight codes, where substantial prior art already exists.

Likely novelty, if any, must survive a dedicated prior-art gate around q-ary restricted-coefficient dependencies, nested/prefix-optimal families, nonuniform alphabets, or joint computation/communication/locality lower bounds.

## Documentation authority

Read in this order:

1. [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)
2. [docs/research/README.md](docs/research/README.md)
3. [docs/research/LENT-001-PROTOCOL.md](docs/research/LENT-001-PROTOCOL.md)
4. [docs/research/LENT-001-CLAIMS.md](docs/research/LENT-001-CLAIMS.md)
5. [docs/research/LENT-001-FOUNDATION.md](docs/research/LENT-001-FOUNDATION.md)
6. [docs/research/LENT-001-PRIOR-ART.md](docs/research/LENT-001-PRIOR-ART.md)
7. [docs/research/DECISIONS.md](docs/research/DECISIONS.md)
8. [docs/research/OPEN-QUESTIONS.md](docs/research/OPEN-QUESTIONS.md)
9. [docs/ROADMAP.md](docs/ROADMAP.md)

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
