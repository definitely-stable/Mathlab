# LENT-001 — claim registry

| ID | Status | Statement / role | Novelty status |
|---|---|---|---|
| LENT-A | THEOREM | \(N_d(V)\le B_q(m,dw)\) in the frozen deterministic exact additive model | **NOT CLAIMED** |
| LENT-B2 | DERIVED RESULT | binary entropy locality bound under near-entropy state size | **NOT CLAIMED** |
| LENT-Bq | DERIVED RESULT | q-ary entropy locality bound using \(\alpha_q(\varepsilon)\) | **NOT CLAIMED** |
| LENT-C | ASYMPTOTIC RESULT | elementary fixed-\((d,w)\) binary consequence \(m=\Omega(V^{1/w})\) | **NOT CLAIMED; likely weaker than known sparse-matrix bounds** |
| ASET-DEF | DEFINITION | \(A_q^{\mathrm{set}}(m,w,d)\): maximum \(V\) for support-\(w\) columns with all subset sums through size \(d\) distinct | **PRIMARY G1 OBJECT; NOVELTY OPEN** |
| ASET-SIGNED | DERIVED RESULT | ASET exactness iff no nonzero \(\varepsilon\in\{-1,0,1\}^V\) has \(n_+\le d\), \(n_-\le d\), and zero weighted sum | **PROVED IN G1A; NOVELTY NOT CLAIMED** |
| ASET-BINARY | DERIVED RESULT | for \(q=2\), ASET exactness iff no nonempty GF(2) dependency exists among at most \(2d\) columns | **PROVED IN G1A; KNOWN-TERRITORY BASELINE** |
| ASET-LIN-IMPLIES | DERIVED RESULT | arbitrary-coefficient independence of every at-most-\(2d\) column set implies ASET exactness over every field | **PROVED IN G1A; NOVELTY NOT CLAIMED** |
| ASET-Q3-SEP | DERIVED RESULT / EXACT WITNESS | \(q=3,m=1,d=1,\{1,2\}\) is ASET-exact but linearly dependent | **PROVED / NOVELTY NOT CLAIMED** |
| ASET-Q5-SEP | DERIVED RESULT / EXACT WITNESS | \(q=5,m=1,d=1,\{1,2\}\) is ASET-exact but linearly dependent | **PROVED / NOVELTY NOT CLAIMED** |
| ASET-QGT2-SHARP | RESEARCH TARGET | classify the sharp extremal gap between ASET and arbitrary-coefficient sparse small-column independence | **OPEN / G1B NOVELTY GATE** |
| LENT-D | DERIVED RESULT | per-prefix sparse-update bound for a precisely defined nested family | **NOT A PURE NESTED-TAX RESULT** |
| LENT-NESTED-LOCAL | CONJECTURE | one nested family near-optimal at several capacities with bounded update locality pays an additional simultaneous penalty | **OPEN / SECONDARY** |
| LENT-MIXED | DERIVED RESULT | mixed-alphabet reachable-state bound \(\sum_{|J|\le dw}\prod_{j\in J}(q_j-1)\) | **NOT CLAIMED** |
| LENT-QGROW | CONJECTURE / pending lemma cleanup | simplified uniform alphabet-growth form | **OPEN** |
| LENT-A2-SHARP | REJECTED AS DEFAULT TARGET | sharp binary extremal asymptotic | **BLOCKED by sparse parity-check overlap** |
| LENT-NESTED-SHARP | DEPRIORITIZED CONJECTURE | pure nestedness tax without update-locality constraint | **DEPRIORITIZED** |
| LENT-JOINT | DEFERRED CONJECTURE | communication + locality + computation lower bound | **MODEL NOT FROZEN** |

## Rules

"Mathematically proved" and "new" are independent fields.

No row may be promoted to a novelty claim by changing only proof status.

No neighboring coding/additive-combinatorics result may be marked equivalent
without a definition-level reduction.

Arbitrary field coefficients and restricted signed coefficients remain
separate notions unless an equivalence is actually proved.
