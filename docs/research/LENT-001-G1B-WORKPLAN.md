# LENT-001-G1B — work plan

Status: **READY FOR SOURCE INTAKE**

Issue: #6

## Phase A — terminology and definition closure

Priority:

1. k-dissociated / bounded-order dissociated;
2. weak Sidon / restricted \(B_h\);
3. distinct-summand subset-sum systems;
4. sparse parity-check matrices.

For each object, answer only:

- what coefficients are allowed?
- are repeated summands allowed?
- exactly \(h\) or all sizes through \(d\)?
- are unequal-cardinality collisions covered?
- is relation support bounded only in total or separately by sign?
- are generators themselves support-bounded?

Output: no theorem comparison yet; only exact definition maps.

## Phase B — theorem map

For every object surviving Phase A:

- pin the strongest relevant upper bound;
- pin the strongest relevant construction/lower bound;
- record all arithmetic/characteristic restrictions;
- map exponents and parameters to \((q,m,w,d,V)\);
- classify the result as:
  - equivalent;
  - stronger;
  - weaker;
  - incomparable.

## Phase C — ASET reduction audit

For each candidate theorem write a short reduction note answering:

1. can its construction be used directly as an ASET construction?
2. can its upper bound be transferred to ASET?
3. does the reduction preserve the support bound \(w\)?
4. does it preserve the \(d\)-side bounds?
5. does it preserve q/characteristic restrictions?

No answer may be inferred from naming alone.

## Phase D — novelty decision

Construct a final table:

| Regime | Best known lower baseline | Best valid upper baseline | Gap | Novelty status |
|---|---|---|---|---|

At minimum include:

- q=2;
- q=3;
- odd q>3;
- characteristic two q>2 if primary sources distinguish it;
- fixed \(d,w\) regimes where existing sparse-code results have sharp exponents.

Then choose exactly one G1B exit.

## Intake of external deep research

When an external deep-research report is supplied:

1. record it as secondary evidence;
2. extract candidate primary sources;
3. verify the exact theorem in the primary source;
4. populate the source matrix;
5. reject any report-level equivalence not supported by the source.

This lets external research accelerate navigation without becoming repository
authority by itself.
