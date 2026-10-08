# LENT-001-G1B — characteristic-two extremal sandwich

Status: **DERIVED RESULT / NOVELTY NOT CLAIMED**

Let

\[
q=2^s.
\]

For every positive m,w,d,s,

\[
\boxed{
A_2(m,w,d)
\le
A_{2^s}^{\mathrm{set}}(m,w,d)
\le
A_2(sm,sw,d)
}.
\]

## Lower bound

Take a binary ASET family in \(\mathbb F_2^m\) with support at most w and
embed \(\mathbb F_2=\{0,1\}\) into \(\mathbb F_{2^s}\).

All subset-sum equalities and supports are preserved. Therefore every binary
family is also a valid \(2^s\)-ary family, proving

\[
A_2(m,w,d)
\le
A_{2^s}^{\mathrm{set}}(m,w,d).
\]

## Upper bound

Fix an \(\mathbb F_2\)-basis of \(\mathbb F_{2^s}\) and expand coordinates:

\[
\beta:\mathbb F_{2^s}^m\to\mathbb F_2^{sm}.
\]

The characteristic-two reduction preserves ASET exactness.

A q-ary vector with at most w nonzero coordinates expands to a binary vector
of Hamming weight at most sw. Hence the expanded family is a binary ASET
family with parameters \((sm,sw,d)\), proving

\[
A_{2^s}^{\mathrm{set}}(m,w,d)
\le
A_2(sm,sw,d).
\]

## Interpretation

Characteristic-two ASET cannot escape binary sparse parity-check/BCC theory
merely by enlarging the field.

The binary upper relaxation forgets the stronger block structure: the sw
possible nonzero bits originate from at most w field-coordinate blocks.

A block-aware theorem may sharpen the sandwich, but broad characteristic-two
novelty cannot ignore known binary sparse-code bounds.
