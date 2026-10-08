# LENT-001-G1B — final source-to-claim matrix

Status: **CLOSED — SPLIT_BY_CHARACTERISTIC**

Issue: #6

## Direct model classes

| Source / class | Model relation | Hard support | G1B effect |
|---|---|---:|---|
| Bounded-Contention Coding, Censor-Hillel et al. | binary ASET without support restriction | no | binary object-level novelty STOP |
| Ericson–Levenshtein modulo-2 superimposed codes | binary modular bounded-active identification | not the target | binary prior-art baseline |
| Poltyrev–Snyders restricted-access sum-mod-2 MAC | richer binary modular active-user model | not the target | binary prior-art baseline |
| Goseling–Stefanović–Popovski finite-field signatures | bounded-active identities recoverable from \(\mathbb F_q\) sum | not optimized as hard w | q-ary object-level novelty STOP |
| Fan et al. constant-weight signature codes | zero-error/support-constrained signature extremals under weighted/ordinary adder models | yes | proves generic sparse-signature idea is known |
| Chang et al. additive separable matrices | d-sparse exact recovery under standard arithmetic | source-dependent | ordinary-addition super-class comparator |
| constant-column-weight OR group testing | hard tests-per-item | yes | non-equivalent arithmetic/guarantee |
| Han–Yildiz–Hassibi (2026) support-constrained parity checks | arbitrary parity-check masks; mask-optimal minimum distance over sufficiently large fields | arbitrary masks, including column restrictions | strong support-constrained coding baseline |

## Additive-combinatorics classes

| Class | Relation to ASET | G1B effect |
|---|---|---|
| dissociated / free sets | stronger, all-order signed uniqueness | construction/baseline neighbor |
| h-free | stronger because one collision side may be unrestricted | not equivalent |
| \(B_h^*\) / weak Sidon | fixed-cardinality distinct-summand uniqueness | ASET implies these; converse absent |
| q=3 Sidon / 2-cap | includes repeated-summand constraints | not equivalent to ASET d=2 |
| constant-weight binary \(B_2\) sequences | hard weight + ordinary pair-sum uniqueness | strong sparse-additive neighbor |

## Sparse linear-code classes

| Source / class | Relation | Transfer |
|---|---|---|
| Lefmann sparse parity-check matrices | arbitrary-coefficient short independence with bounded column support | constructions lower-bound ASET; q>2 upper bounds do not automatically transfer |
| Naor–Verstraete sparse parity-check bounds | binary/sparse-code extremal neighbor | binary baseline |
| Bshouty–Mazzawi (0,1)-matrices over \(\mathbb Z_p\) | short arbitrary-coefficient independence with near-optimal row count | communication baseline; no small column-weight theorem |
| support-constrained parity-check masks (2026) | optimum arbitrary-linear minimum distance for a fixed support mask over sufficiently large fields | mask-level baseline, not odd-ASET equivalence |

## Field classification

| Regime | Structural result | G1B decision |
|---|---|---|
| q=2 | ASET = binary short-dependency/BCC; sparse parity-check prior art | STOP primary novelty lane |
| q=2^s, s>1 | exact block-binary reduction and sandwich \(A_2(m,w,d)\le A_q^{set}(m,w,d)\le A_2(sm,sw,d)\) | DEPRIORITIZE / secondary block-aware problem |
| q=3 | coefficient set already ±1; side bounds remain distinct | CONTINUE in G2 |
| odd q>3 | coefficient restriction + side bounds both remain | CONTINUE in G2; primary lane |

## Surviving candidate

No object-level novelty is claimed.

The surviving candidate is the **sharp hard-support odd-characteristic
finite-field signature frontier**:

\[
A_q^{\mathrm{set}}(m,w,d),
\qquad
q\text{ odd},
\]

with fixed or genuinely small \(w\).

G2 must now decide whether this candidate supports a theorem worth proving.
