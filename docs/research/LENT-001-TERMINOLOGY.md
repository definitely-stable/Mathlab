# LENT-001 — terminology policy

Status: **ACTIVE**

Date: 2026-10-08

## Stable identifier

`LENT-001` is retained permanently as the research-family identifier.

It is used by issues, protocol files, evidence artifacts, CI markers, and historical references.

It should not be reinterpreted as a required public acronym.

## Deprecated public terminology

The phrase:

**Locality–Entropy Trilemma**

is deprecated for new public-facing material.

Reasons:

1. the proved finite result is a quantitative state-space/update-locality bound;
2. "trilemma" suggests a stronger generic three-way impossibility statement than has been proved;
3. "locality" and "entropy" have unrelated established meanings in several other fields;
4. a descriptive theorem name is easier to audit against prior art.

Historical uses remain traceable and need not be rewritten when doing so would obscure provenance.

## Preferred terminology

### Research program

**Exact Additive Sketch Locality Frontier**

Guiding question:

> How many exact set identities can a sparse-update additive state encode?

### Baseline theorem

**Sparse-Update Hamming-Ball Bound for Exact Additive Set Sketches**

The finite statement is

[
N_d(V)
=
sum_{i=0}^{d}inom{V}{i}
le
sum_{j=0}^{min(dw,m)}
inom{m}{j}(q-1)^j
=
B_q(m,dw).
]

This theorem is a baseline bound; publication novelty is not claimed.

### Primary extremal direction

**Sparse Bounded-Order Subset-Sum Families**

Primary object:

[
A_q^{mathrm{set}}(m,w,d).
]

This is the current G1/G4 novelty candidate after the binary sparse-parity-check overlap and q-ary model corrections.

## Usage rule

New:

- README headings;
- issue titles;
- roadmap milestones;
- preprint titles;
- theorem names;
- external descriptions

must use the preferred descriptive terminology.

Internal IDs, filenames, protocol IDs and historical CI markers remain `LENT-001`.

## Non-goal

This rename makes no mathematical claim and changes no frozen theorem statement, parameter, proof, evidence result, or prior-art verdict.
