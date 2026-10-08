# LENT-001-G1B — Audit 03 hard-support closure protocol

Status: **FROZEN FOR FINAL G1B SOURCE CLOSURE**

Issue: #6

Baseline: main@94d4d0695c26fe947a65e631f492506b2ee228e4

## 1. Objective

Audit 03 is the final targeted prior-art gate before choosing the G1B exit.

Audits 01–02 already establish that binary bounded-active modular
identification is BCC prior art, finite-field bounded-active signature
identification is prior art, and constant-weight exact active-user signatures
exist under ordinary addition.

Therefore Audit 03 searches only for results that materially determine the
sharp dependence on

\[
w=\max_i |\operatorname{supp}(a_i)|.
\]

## 2. Required source classes

Audit 03 must close, in order:

1. block-sparse binary BCC / parity-check results;
2. zero-error sparse finite-field signatures with hard support;
3. bounded-column-weight additive detecting matrices;
4. support-constrained q-ary Sidon, B_h, free, dissociated or signed-sum families;
5. fixed-(d,w) asymptotics.

Noisy low-density signatures, OR group testing, list recovery and average-case
detection are non-equivalent unless an explicit zero-error reduction is proved.

## 3. Search failure is not novelty evidence

The following do not authorize novelty:

- no exact keyword match;
- no result from a web search;
- only surveys or secondary citations;
- a theorem with different arithmetic or support semantics;
- average density instead of hard worst-case support.

A CONTINUE_SPARSE_ASET exit requires a completed reduction map showing that
the strongest neighboring theorems do not already imply the intended sharp
result.

## 4. Mandatory theorem map

For every potentially direct source record:

- arithmetic model;
- active-set domain;
- zero-error / probabilistic guarantee;
- signature alphabet;
- hard support versus average density;
- whether support is per signature, row, block or codeword;
- asymptotic regime;
- construction/lower bound;
- converse/upper bound;
- exact transfer direction to ASET.

## 5. Characteristic-two lane

Use the repository theorem

\[
A_2(m,w,d)
\le
A_{2^s}^{\mathrm{set}}(m,w,d)
\le
A_2(sm,sw,d).
\]

The lower inequality embeds binary columns into the prime subfield.

The upper inequality expands each q-ary coordinate into s binary coordinates;
q-ary support at most w implies binary Hamming weight at most sw.

Thus characteristic-two ASET already inherits ordinary binary sparse-code
upper and lower baselines. A remaining theorem must exploit or sharpen the
block structure.

## 6. Ordinary-addition lane

For fixed integer representatives,

\[
\text{mod-}q\text{ ASET}
\Longrightarrow
\text{ordinary additive separability}.
\]

Hence hard-column-weight upper bounds for an ordinary-addition super-class
may be necessary ASET bounds.

Constructions transfer only when modulo-q wraparound is also excluded.

## 7. G1B v2 exits

### CONTINUE_SPARSE_ASET

Allowed only if a specific support-sensitive theorem target survives all
direct source classes. The decision must name its parameter regime and exact
candidate statement.

### REDUCE_TO_KNOWN_SPARSE_SIGNATURE

Use when a primary source or valid reduction already gives the intended sharp
hard-support frontier.

### SPLIT_BY_CHARACTERISTIC

Use when characteristic two and odd characteristic have genuinely different
closure status.

### STOP_NOT_NOVEL

Use when no meaningful support-sensitive theorem remains.

## 8. Deliverables

- Audit-03 source notes;
- completed final source matrix;
- characteristic-two sandwich proof;
- strongest valid upper/lower baselines per field regime;
- final G1B decision in issue #6;
- synchronized CLAIMS, PRIOR-ART, DECISIONS and ROADMAP.

No preprint promotion occurs inside Audit 03.
