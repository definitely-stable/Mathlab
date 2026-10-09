# ALG-001 G0 — dynamic rank and observation-cost separation

**Status (2026-10-09):** RESTRICTED_INFORMATION_LEMMA / FINITE_GF_ORACLE / RANK_ALGORITHM_PRIOR_ART / G1_NONFACTORIZING_OPEN / NO_RUST. [Issue #134](https://github.com/definitely-stable/Mathlab/issues/134), paired [DAG-002 #133](https://github.com/definitely-stable/Mathlab/issues/133).

## 1. Audited claims and precise nontransfer

- [LIT-195, Jan van den Brand, Vishal Kumar, Daniel J. Zhang, *Dynamic Rank, Basis, and Matching*, ICALP 2026](https://doi.org/10.4230/LIPIcs.ICALP.2026.45). Publisher abstract: `Õ(r^1.405)` **per entry-update** for dynamic rank, `Õ(r^1.528+z)` **per column-update** where `z` is number of changed entries. Includes basis/full-rank submatrix maintenance and matching size for specified algebraic models. **Their upper bounds are not state-bit lower bounds.** This document neither replicates their proof nor challenges it.
- Earlier original prior art: [van den Brand–Nanongkai–Saranurak, *Dynamic Matrix Inverse: Improved Algorithms and Matching Conditional Lower Bounds*, 2019](https://arxiv.org/abs/1905.05067) concerns dynamic inverse and conjecture-dependent performance barriers; [Frandsen–Frandsen, *Dynamic Matrix Rank*, 2009](https://pure.au.dk/portal/en/publications/dynamic-matrix-rank/) studies operation count and algebraic lower bounds. Confirm source identity before separate bibliographic import; **not represented as independently reproved**.
- [DAG-002 restricted observer theorem](DAG-002-G0-IMMUTABLE-REACHABILITY.md): explicit output-vector distinguishability with no external source probes. It uses the same classical counting proof, *not an independent result*.

## 2. Two different computational tasks

**Rank-only:** matrix `A∈GF(q)^{m×n}`; output scalar `rank(A)`; legal updates specified separately: one entry or a whole column. Measure arithmetic operations, initial work, field cardinality, randomized error, input bit storage and whether a basis is materialized.

**Coordinate-observation:** `A_S = [1_S(0),...,1_S(n−1)]∈GF(2)^{1×n}` for nonempty `S⊆[n]`; query `Q_i(A_S)=A_S[0,i]`. Under the local immutable prior-observer model, old query-key labels `L_i` and decoder are fixed, latest input-dependent state consists only of `b`-bit new label and `g`-bit manifest, and **no remote matrix reads** are allowed. The set of required answer vectors has `2^n−1` possibilities.

**Lemma ALG-001-G0-L1 (elementary rank-one observation capacity).** For `n≥2`, every `A_S` above has rank exactly 1 while any exact fixed-width endpoint-label+manifest observer for its `n` coordinate queries has `b+g≥ceil(log₂(2^n−1))=n`.

**Proof.** A nonzero row over a field has rank one. Coordinate queries recover precisely its ordered entries, so distinct `S` must have distinct observable `(label,manifest)` pairs. There are `2^n−1` required vectors but at most `2^{b+g}` pairs. For `n≥2`, `2^{n−1}<2^n−1≤2^n`, yielding `b+g≥n`. QED. For `n=1`, the nonzero-row subfamily contains only one state and the bound is **zero**. If the all-zero row is also included, the state family has `2^n` possibilities, including rank zero.

**Why this is NOT a dynamic-rank lower bound:** for the *rank-only* query the value is constant (=1) on all nonzero rows, so zero input-dependent bits suffices to answer rank within that **promised restricted family**. The observed `n`-bit lower bound arises entirely from the **stronger coordinate-output requirement**, not from matrix rank or update time. If `A_S` is stored in untrusted/source remote memory and query `i` reads a cell, the local label may be empty; those cells/probes must be priced. A transition from `S=∅` to an arbitrary `S` usually changes **many** entries, so this argument is not the one-entry update complexity in LIT-195.

**Lemma ALG-001-G0-L2 (classical rank perturbation).** Over any field, one entry update `A→A+δe_i e_j^T` changes rank by at most one. Proof by `rank(X+Y)≤rank(X)+rank(Y)` for both directions, using `rank(δe_i e_j^T)≤1`. The GF(2)/GF(3) finite tests check this lemma; no novel result claimed.

## 3. Mathematical interfaces and fully charged future costs

`(F,m,n,r,update_type,z,Π,E,S,B,G,P,U,W,V)`:

- `F`: field; `m,n` matrix dimensions, `r` actual current rank; `update_type`: entry vs column vs rank-one; `z`: changed entries.
- `Π` preprocessing work; `E` arithmetic operations/update; `S` input/external data bits; `B` auxiliary mutable state bits; `G` globally trusted manifest bits.
- `P` remote probes/query; `U,W` logical and physical bytes written/update; `V` signed/authenticated verifier proof bytes, trusted state, soundness error and online horizon.

Do **not** treat `Õ(r^1.405)` (arithmetic work) as a lower bound on `B+G`; do **not** infer a `Ω(n)` update bound from an `n`-bit observation code unless output materialization and prior state reuse are explicitly priced. Rank-only queries and full-basis-output queries have different observables; dimensions and field remain typed.

## 4. Oracle and G1 decision

- Exhaustively compute independent modular Gaussian-elimination rank over GF(2)/GF(3) on all 2×2 matrices and all 3×3 GF(2) matrices; check each single entry update changes rank by at most one.
- Enumerate every nonzero binary row `A_S` for `n=2..8`, assert rank=1 and unique coordinate-output vectors, and confirm `ceil(log₂(2^n−1))=n`. Include `n=1` counterexample. Include rank-only baseline with zero varying information.
- Cross-check `DAG-002` masks `S` produce the same observable vectors, but do not couple the two independent implementations by sharing a rank helper.
- Stop any theorem proposal that rephrases the trivial injectivity of outputs, classical rank-one perturbation, or SEA 2025 chain-label correctness. G1 must attempt a genuinely mixed bound `information + probes + real updates + trust` under a single fixed adversary and counter-constructions; if it factors into known results, STOP.

**Decision:** `ELEMENTARY_SAME_RANK_OUTPUT_BARRIER_PROVED` / `KNOWN_RANK_PERTURBATION_REPRODUCED` / `NO_DYNAMIC_RANK_LOWER_BOUND` / `G1_JOINT_THEOREM_OPEN` / `NO_RUST`.
