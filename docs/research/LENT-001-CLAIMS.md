# LENT-001 — claim registry

| ID | Status | Statement / role | Novelty status |
|---|---|---|---|
| LENT-A | THEOREM | \(N_d(V)\le B_q(m,dw)\) in the frozen deterministic exact additive model | **BASELINE / NOT CLAIMED** |
| LENT-B2 | DERIVED RESULT | binary entropy locality bound under near-entropy state size | **NOT CLAIMED** |
| LENT-Bq | DERIVED RESULT | q-ary entropy locality bound using \(\alpha_q(\varepsilon)\) | **NOT CLAIMED** |
| LENT-C | ASYMPTOTIC RESULT | elementary fixed-\((d,w)\) binary consequence \(m=\Omega(V^{1/w})\) | **NOT CLAIMED; known sparse-code territory nearby** |
| ASET-DEF | DEFINITION | \(A_q^{\mathrm{set}}(m,w,d)\): max V for support≤w columns with all subset sums through d distinct | **USEFUL PARAMETERIZATION; OBJECT-LEVEL NOVELTY NOT CLAIMED** |
| ASET-SIGNED | DERIVED RESULT | ASET iff no legal \(\{-1,0,1\}\) relation with \(n_+,n_-\le d\) | **PROVED / NOT CLAIMED** |
| ASET-BINARY | DERIVED RESULT | q=2 ASET iff no nonempty GF(2) dependency among ≤2d columns | **KNOWN-TERRITORY BASELINE** |
| ASET-BCC | PRIOR-ART MAPPING | binary ASET without hard support bound is exactly bounded-contention coding (BCC) | **KNOWN OBJECT** |
| ASET-QARY-SIGNATURE | PRIOR-ART MAPPING | finite-field bounded-active user identification from signature sums is established signature-code territory | **KNOWN BROAD OBJECT** |
| ASET-LIN-IMPLIES | DERIVED RESULT | arbitrary-coefficient independence of every ≤2d column set implies ASET | **PROVED / NOT CLAIMED** |
| ASET-Q3-SEP | DERIVED RESULT / EXACT WITNESS | q=3 ASET can hold despite an ordinary short linear dependency | **PROVED / NOT CLAIMED** |
| ASET-Q5-SEP | DERIVED RESULT / EXACT WITNESS | q=5 ASET can hold despite arbitrary-coefficient short linear dependence | **PROVED / NOT CLAIMED** |
| ASET-CHAR2-BLOCK | DERIVED RESULT | for \(q=2^s\), ASET is exactly a block-sparse binary short-dependency/BCC problem after basis expansion | **PROVED IN G1B / NOT CLAIMED** |
| ASET-SPARSE-SHARP | RESEARCH TARGET | determine the sharp finite-field signature frontier under hard \(|supp(a_i)|\le w\) | **OPEN / PRIMARY G1B NOVELTY CANDIDATE** |
| ASET-CHAR2-SHARP | RESEARCH TARGET | classify sharp block-sparse BCC/parity-check behavior for \(q=2^s\) | **OPEN / AUDIT 03** |
| ASET-ODD-SHARP | RESEARCH TARGET | classify hard-support ASET in odd characteristic, including q=3 side-bound and q>3 coefficient restrictions | **OPEN / AUDIT 03** |
| LENT-D | DERIVED RESULT | per-prefix sparse-update bound for a precise nested family | **NOT A PURE NESTED-TAX RESULT** |
| LENT-NESTED-LOCAL | CONJECTURE | simultaneous near-optimal nested prefixes with bounded update locality pay an additional penalty | **OPEN / SECONDARY** |
| LENT-MIXED | DERIVED RESULT | mixed-alphabet reachable-state count | **NOT CLAIMED** |
| LENT-QGROW | CONJECTURE | simplified uniform alphabet-growth form | **OPEN** |
| LENT-A2-SHARP | REJECTED AS DEFAULT TARGET | sharp binary extremal asymptotic as a new object | **STOPPED** |
| LENT-NESTED-SHARP | DEPRIORITIZED CONJECTURE | pure nestedness tax | **DEPRIORITIZED** |
| LENT-JOINT | DEFERRED CONJECTURE | communication + locality + independent computation resource | **MODEL NOT FROZEN** |

## Claim policy after G1B Audit 02

The repository must not claim that exact bounded-active subset identification
or finite-field signature coding is new.

Any future novelty claim must use the hard support parameter \(w\)
essentially and survive comparison against sparse parity-check, BCC,
constant-weight adder/signature, detecting-matrix, and support-constrained
additive-combinatorics literature.

"Mathematically proved" and "new" remain independent fields.
