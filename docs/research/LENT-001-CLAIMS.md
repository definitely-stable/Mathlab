# LENT-001 — claim registry

| ID | Status | Statement / role | Novelty status |
|---|---|---|---|
| LENT-A | THEOREM | \(N_d(V)\le B_q(m,dw)\) in the frozen deterministic exact additive model | **NOT CLAIMED** |
| LENT-B2 | DERIVED RESULT | binary entropy locality bound under near-entropy state size | **NOT CLAIMED** |
| LENT-Bq | DERIVED RESULT | q-ary entropy locality bound using \(\alpha_q(\varepsilon)\) | **NOT CLAIMED** |
| LENT-C | ASYMPTOTIC RESULT | elementary fixed-\((d,w)\) binary consequence \(m=\Omega(V^{1/w})\) | **NOT CLAIMED; likely weaker than known sparse-matrix bounds** |
| ASET-DEF | DEFINITION | \(A_q^{\mathrm{set}}(m,w,d)\): maximum \(V\) for support-\(w\) columns with all subset sums of sets of size at most \(d\) distinct | **PRIMARY G1 OBJECT; NOVELTY OPEN** |
| ASET-SIGNED | DERIVED RESULT / G1A PROOF TARGET | ASET exactness iff there is no nonzero \(\varepsilon\in\{-1,0,1\}^V\) with \(n_+\le d\), \(n_-\le d\), and \(\sum_i\varepsilon_i a_i=0\) | **NOVELTY NOT CLAIMED** |
| ASET-BINARY | DERIVED RESULT | for \(q=2\), ASET exactness iff there is no nonempty GF(2) dependency among at most \(2d\) columns | **KNOWN-TERRITORY BASELINE** |
| ASET-QGT2 | RESEARCH TARGET | for \(q>2\), classify the gap between restricted signed relations and arbitrary-coefficient small-column independence | **OPEN / G1A** |
| LENT-D | DERIVED RESULT | per-prefix locality lower bound for a precisely defined nested family | **NOT A PURE NESTED-TAX RESULT** |
| LENT-NESTED-LOCAL | CONJECTURE | one nested family that is near-optimal at several capacities and has bounded update locality pays an additional simultaneous penalty | **OPEN / SECONDARY** |
| LENT-MIXED | DERIVED RESULT | mixed-alphabet reachable-state bound \(\sum_{|J|\le dw}\prod_{j\in J}(q_j-1)\) | **NOT CLAIMED** |
| LENT-QGROW | CONJECTURE / pending lemma cleanup | uniform simplified alphabet-growth form \(\log q=\Omega(\log(V/d)/w)\) | **OPEN** |
| LENT-A2-SHARP | CONJECTURE REJECTED AS DEFAULT TARGET | sharp binary extremal asymptotic | **BLOCKED by direct sparse parity-check overlap** |
| LENT-NESTED-SHARP | DEPRIORITIZED CONJECTURE | pure nestedness tax without an update-locality condition | **DEPRIORITIZED by rate-compatible-code prior art** |
| LENT-JOINT | DEFERRED CONJECTURE | communication + locality + computation lower bound | **MODEL NOT FROZEN** |

## Rules

"Mathematically proved" and "new" are independent fields.

No row may be promoted to a novelty claim by changing only the proof status.

No neighboring coding/additive-combinatorics result may be marked "equivalent" without a definition-level reduction.

For q-ary work, arbitrary field coefficients and restricted signed coefficients must remain separate notions unless an equivalence is actually proved.
