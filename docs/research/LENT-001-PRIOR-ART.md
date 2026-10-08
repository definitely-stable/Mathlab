# LENT-001 — prior-art audit

Status: **G1 OPEN / G1A COMPLETE / G1B AUDITS 01–02 COMPLETE**.

The key novelty correction after Audit 02 is that the broad exact subset
identification object is established prior art. The only remaining primary
candidate is the **hard support-constrained sharp frontier**.

## 1. Binary: BCC closes unconstrained ASET novelty

Censor-Hillel, Haeupler, Lynch and Médard define an \([M,m,a]\)
Bounded-Contention Code as a set of binary codewords whose XORs are distinct
for every two distinct subsets of size at most \(a\).

This is binary ASET without the hard support bound.

Primary:
https://arxiv.org/abs/1208.6125

Thus binary ASET as an object is known. Sparse parity-check literature
further overlaps the support-constrained binary problem.

## 2. Finite-field bounded-active signatures are established

Goseling, Stefanović and Popovski use signature codes over an
\(\mathbb F_q\) adder channel so that identities of up to \(K\) active users
are recovered from the sum of their signatures.

Primary:
https://arxiv.org/abs/1602.02612

Their construction controls signature length and deliberately uses a large
field; it does not establish the sharp hard-support frontier.

Therefore broad q-ary ASET existence/identity recovery is not new, while
support-sensitive extremality may still be.

## 3. Characteristic two reduces to block-sparse binary coding

For \(q=2^s\), repository proof shows:

\[
\text{ASET}_d
\Longleftrightarrow
\text{no nonempty GF(2) dependency among at most }2d
\]

after basis expansion.

The q-ary support bound becomes at most \(w\) nonzero binary blocks of size
\(s\).

Hence the correct characteristic-two prior-art target is **block-sparse
binary BCC/parity-check coding**.

See:
\`LENT-001-G1B-CHAR2-REDUCTION.md\`.

## 4. Constant-weight exact signatures are also known under ordinary addition

Fan, Darnell and Honary show that suitable constant-weight binary codewords
allow exact identification of any bounded set of active users in the
ordinary binary-adder channel.

DOI:
https://doi.org/10.1109/18.391266

Fan et al. later study constant-weight t-signature codes in a weighted
binary adder model.

Thus "sparse active-user signature" is not itself new.

The remaining arithmetic distinction is ordinary addition versus
finite-field/mod-q addition.

## 5. Low-density signature is established engineering terminology

Low-density signature systems deliberately give each user only a few
nonzero chips, but typically target noisy probabilistic multiuser detection,
not deterministic zero-error subset injectivity.

Example:
Hoshyar, Wathan, Tafazolli (2008),
DOI https://doi.org/10.1109/TSP.2007.909320

This literature is mandatory terminology/engineering context, but not an
ASET theorem by itself.

## 6. Earlier Audit 01 boundaries remain active

Also verified:

- Lefmann q-ary sparse parity-check matrices are stronger than odd-q ASET;
- standard k-dissociated terminology does not mean bounded relation order;
- free/h-free/\(B_h^*\) are close but non-equivalent;
- standard q=3 Sidon/2-cap includes repeated summands;
- constant-weight real-addition \(B_2\) sequences are established;
- additive/quantitative group testing gives standard-arithmetic d-sparse
  separability.

Detailed sources:
\`LENT-001-G1B-AUDIT-01.md\` and
\`LENT-001-G1B-AUDIT-02.md\`.

## 7. Current novelty candidate

Rejected broad claim:

> exact additive bounded-active set identification is new.

Retained narrow candidate:

\[
\boxed{
\textbf{sharp support-constrained finite-field signature frontier}
}
\]

with hard per-element update locality

\[
|\operatorname{supp}(a_i)|\le w.
\]

A successful theorem must use \(w\) essentially and survive comparison with
block-sparse BCC/parity-check, constant-weight adder/signature, detecting
matrix and support-constrained additive-combinatorics results.

## 8. G1B remains OPEN

Audit 03 must close:

1. block-sparse BCC/parity-check results;
2. exact sparse/constant-weight finite-field or modulo-q signature codes;
3. bounded-column-weight quantitative/detecting matrices;
4. support-constrained q-ary \(B_h\)/signed-sum families;
5. fixed-\((d,w)\) sharp asymptotic results.

No manuscript novelty claim is allowed before this closure.
