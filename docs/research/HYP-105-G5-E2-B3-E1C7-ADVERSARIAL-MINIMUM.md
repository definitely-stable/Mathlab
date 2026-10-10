# HYP-105 B3.2-E1-C7 — deterministic sixset-permutation minimum with certified finite search

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stack: C0 #249 (merged) → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7.

**STATUS: RESTRICTED_THEOREM_C / EXACT_FINITE_DECISION / CI PENDING.** The new oracle decides ONLY B-left/A-right overlap for ONE fixed original GQ-left embedding f and ONE occupied right physical image F, with a true simultaneous bijection g of *all* right factor vertices. It does not decide the seven-family S_s, the minimization over all f,F, or an all-h asymptotic bound.

## 1. Fixed f,F optimization and all-h relaxation

Let V=(s+1)(s²+1), Ω=binom([V],6), nonnegative m_f:Ω→N, and t_F:Ω→{0,1}. The latter is the physically occupied six-edge 2-regular target of C5. The original-right bijection π∈S_V acts simultaneously on every sixset, giving

```text
U_B/A(f,π;F)= Σ_{R∈Ω} m_f(R) t_F(π R).
OPT(f,F) = min_{π∈S_V} U_B/A(f,π;F).
```

For **all V≥6**, with N=C(V,6), t=|T(F)|, and the N source multiplicities sorted as w_1≤...≤w_N **including N−|supp(m_f)| zeros**, the following deterministic relaxation is exact for the *larger* group S_N of arbitrary permutations of sixset cells:

```text
OPT(f,F) ≥ L_rearr(m_f,T_F):=Σ_{i=1}^{t} w_i ≥ 0.
```

Proof: every genuine vertex permutation induces a permutation of all N sixset cells, but not conversely. Minimizing over S_N selects any t source cells, hence exactly the t lightest source values. The relaxation can be zero even for a strongly positive genuine OPT, so it is NOT a universal obstruction theorem.

## 2. Correct partial-assignment lower certificate

For a partial *injective* assignment p:D→F of k original right vertices and a source original sixset R, set I=p(R∩D) and O=p(D\R). Every sixset A in the occupied index alphabet compatible with p satisfies I⊆A and A∩O=∅. Conversely EVERY such A can be realized as p'(R) by at least one FULL bijection p' extending p: map the |R\D| remaining original vertices in R to A\I, and the rest to the remaining positions.

The total number of compatible image sixsets is exactly

```text
N_R(p)=C(V−k,6−|I|).
c_R(p)=#{A∈T(F): I⊆A, A∩O=∅}.
```

In particular 0≤c_R(p)≤N_R(p). If c_R(p)=N_R(p), **every** extension contributes m_f(R); otherwise nothing is inferred from this R. Thus

```text
L_forced(p) = Σ_{R: c_R(p)=N_R(p)} m_f(R)
              ≤ min_{p' extends p} U_B/A(f,p';F).
```

This is a correct fixed-branch, all-completion lower bound with NONNEGATIVE terms, valid for any finite V and any genuine/nonnegative source. Once a term is forced it remains forced after extending p. The implementation computes it with integer bitmasks, exact binomial coefficients, and memoized (I,O) completion checks. It never treats independent C4 frozen-pair completions as independent permutations: every branch extends exactly ONE common map.

## 3. Finite exhaustive protocol and sound result types

For practical bounded enumeration, the exact solver is deliberately restricted to **6≤V≤9**. Original factors are ordered by weighted sixset incidence for pruning, but the actual result is an arbitrary true original→occupied permutation. An initial identity/reversal gives a genuine *upper* witness. The solver prunes only if L_forced(p)≥best known upper. Its three outcomes are:

- `ZERO_WITNESS`: a concrete permutation with exact overlap 0; nonnegativity alone proves minimum 0 (regardless of unvisited branches).
- `CERTIFIED_MINIMUM`: positive best candidate with either exhausted branch tree or equality to the all-sixset rearrangement lower bound.
- `UNKNOWN_BUDGET`: node limit reached before a proof; `certified_lower ≤ OPT ≤ witness_upper`, and `exact_minimum=None`. **No proof** from a positive best witness alone.

All returned witness values are checked by independent direct source-target sextet recounts. A separate implementation exhaustively enumerates all 7!=5,040 or 8!=40,320 genuine full permutations for independent cross-validation (NOT a sampling claim), including dense positive-pigeonhole fixtures, sparse zero fixtures, and fail-closed budget cuts.

## 4. Genuine W(3,2) report and remaining blocker

The true left GQ incidence census, right physical K6 target (70 sextets), and actual fixed lex/reverse-line bijections are reused from C0/C5. For V=15, N=5005 the solver **does NOT** attempt 15! and makes **no** claim of minimum. It reports the rearrangement floor, source support, target support, and actual independent fixed overlaps (expected historical controls 98 lex and 77 reverse-line). The rearrangement floor is zero because over 70 original sixsets have zero source weight; the observed *positive* overlaps are **not** evidence of a positive worst-case minimum.

This is a **formal obstruction to support-only proofs**, not a counterexample to a genuine GQ all-g bound. Even a certified positive minimum for one f,F would not establish a universal all-f,F or seven-family result. A zero for one f,F would invalidate the proposed universal B/A-only bound but NOT universal `S_seven` since other six-motif families could contribute.

## 5. Acceptance and next decision

The reference is [C7 code](../../research/hyp105_g5e2b3e1c7_adversarial_minimum.py), with [independent 7!/8! enumeration](../../research/test_hyp105_g5e2b3e1c7_adversarial_minimum.py). A dedicated GitHub-hosted `hyp105-c7-contract` workflow and a full Research step provide exact-PR-HEAD acceptance gates. No new asymptotic GQ theorem is claimed; the rearrangement/pigeonhole and finite constraint-search facts are elementary.

**Next mathematical gate:** derive an additional *GQ-source-specific*, physical-occupancy-specific necessary crossing inequality not erased by the zero-heavy relaxation; prove it for ALL h and EVERY correlated g, or construct a valid infinite original-factor family with the full seven-class risk estimated. Parent #230 stays **OPEN_WITH_FORMAL_BLOCKER**; no R3/ASET exponent claim.
