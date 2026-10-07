# Open research questions

## Highest priority

1. **q-ary restricted coefficients.** What is the sharp maximum (V) for support-(w) columns in (mathbb F_q^m) such that all subset sums of size at most d are distinct, when collisions only induce ({-1,0,1}) coefficients?

2. **Nested tax beyond pointwise LENT.** Does one common nested/rate-compatible family pay a provable extra factor compared with choosing an optimal independent sketch for each d?

3. **Alphabet-growth theorem.** Turn the implicit
[
log_2qge
alpha_q(arepsilon)log_2N_d/(dw)
]
into the sharpest explicit bound, with a proved uniform estimate on (alpha_q).

4. **Nonuniform cells.** Replace one alphabet q by coordinate alphabets (q_1,dots,q_m). What is the right locality/state counting theorem and what cell-richness measure replaces (mlog q)?

5. **Computation tax.** After freezing a decoder/update model, can communication, locality and total incremental decoding work be lower-bounded jointly?

## Prior-art questions

- Which q-ary (B_h), Sidon-set, superimposed/separable-code, or sparse-matrix results already solve restricted-coefficient variants?
- Are there existing nested syndrome / rate-compatible secure-sketch lower bounds?
- Which locally updatable code lower bounds translate exactly to column-support locality rather than a different update metric?
- What is already known for sparse parity-check matrices over nonbinary fields when only ({-1,0,1}) dependencies matter?

## Construction questions

- Can random constant-weight q-ary columns match the finite Hamming-ball exponent in any nontrivial regime?
- Can spatial coupling/check splitting produce a nested family that matches the pointwise lower bound?
- Is a nonuniform alphabet construction materially better than a uniform q-ary one at the same bit budget?

## Formalization questions

- What Mathlib representation gives the cleanest finite-support cardinality proof?
- Should the first Lean theorem use `Fin m -> ZMod p` for prime q, then generalize to finite fields?
- Can the Hamming-ball count be isolated from field structure and proved over any finite pointed alphabet?
