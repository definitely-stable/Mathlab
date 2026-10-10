# HYP-105 B3.2-E1-C8 — all-h frozen-fiber rearrangement hierarchy and exact finite interval

Date: 2026-10-10. Parent [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stack: #249 C0 merged → #260 C1 → #261 C2 → #266 C3 → #269 C4 → #273 C5 → #278 C6 → #279 C7 adversarial minimum → **C8**. Companion independent [#280](https://github.com/definitely-stable/Mathlab/pull/280) is a *different parallel C7* conditional-expectation selector, **not** an integrated dependency.

**STATUS RESTRICTED_THEOREM_C / ALL-V-EXACT_RELAXATION / FINITE_STAR_EXACT / PR_HEAD_CI_PENDING.** This applies to B-left/A-right six-incidence motifs only, one FIXED left GQ embedding f and one FIXED right occupied physical edge image F. Not a theorem about all f,F or the seven-class S_s.

## 1. Model-preserving conditional orbit fibers

For all h≥1 and s=2^h, let V=(s+1)(s²+1). Original right factors form [V]. Fixed legitimate left embedding f determines the nonnegative sixset multiplicity m_f(R), with zero weights for sixsets outside its support. A fixed occupied image F of V distinct physical K_a edges determines the indicator t_F(Q) on six physical-right edge sextets that form a simple 2-regular graph on six coordinate vertices.

For a FULL original→occupied bijection g∈S_V, all original factors use ONE COMMON mapping; their weighted B/A intersection is

```text
U(g)=Σ_{R∈C([V],6)} m_f(R) t_F(g(R)).
```

Fix a subset D⊆[V], |D|=k, and a partial injection p:D→[V]. For each A⊆D, define the source/target conditional classes:

```text
X_A = {R∈C([V],6): R∩D=A}
Y_A = {Q∈C([V],6): Q∩p(D)=p(A)}
N_A = |X_A|=|Y_A|=C(V−k,6−|A|)
t_A = |T(F)∩Y_A|.
```

Every full completion g of p maps X_A BIJECTIVELY onto Y_A (not independent maps among classes). Sort all N_A integer source weights in X_A, including implicit zeros:

```text
w_(A,1)≤...≤w_(A,N_A).
L_D(p) = Σ_{A⊆D} Σ_{j=1}^{t_A} w_(A,j).
```

**Theorem, all V≥6 and every nonnegative sixset source/target:** for every g⊇p,
`U(g)≥L_D(p)`. Proof: g sends exactly t_A source positions of each X_A into the target in Y_A. Their weight sum is at least the t_A smallest class weights. Sum over disjoint classes. Relaxing each induced bijection to an arbitrary permutation independently can only DECREASE the minimum, never increase it.

Define `L_D=min_{injective p:D→[V]} L_D(p)`. Then

```text
L_empty = rearrangement_lower_bound_C7
L_D ≤ min_g U(g).
L_D ≤ L_E for D⊆E (refinement cannot weaken a per-map lower bound).
L_[V] = min_g U(g) (exact, but V! enumeration).
```

Proof of monotonicity: under any extension p' of p, the refined independent per-class assignment constraints are a subset of those allowed for p. Thus `L_E(p')≥L_D(p'|D)`. Minimize over extensions. For fixed k, exhaustive search takes (V)_k = V!/(V−k)! partial maps; a hard `max_prefixes` gate refuses insufficient budgets rather than returning partial minima as universal certificates.

Implementation: [reference](../../research/hyp105_g5e2b3e1c8_fiber_rearrangement.py) computes per-fiber zero multiplicities from binomial cardinalities, stores only positive weights, and enumerates exactly ALL injective prefix images. [Independent tests](../../research/test_hyp105_g5e2b3e1c8_fiber_rearrangement.py) compare a separate brute sixset-cell subset-minimum for V7, full 8! original-map minima grouped by pinned images, nested bound inequalities, and genuine GQ W32 source/target controls.

## 2. A true deterministic interval (C8 lower + C5 expected-upper)

From C5's ONE common uniform permutation expectation,

```text
mu = E_g U(g) = M_f * |T(F)| / C(V,6)
```

where M_f=Σ_R m_f(R). At least one g has integer value ≤ floor(mu). Therefore for the SAME fixed f,F

```text
L_D ≤ min_g U(g) ≤ floor(mu).
```

This upper is **existential**, not an explicit g unless a separate selector constructs and recounts one; it is also only B/A, not the full seven-class risk. When both bounds agree, the exact minimum is proved without enumerating V! maps. A different #280 PR constructs an independent conditional-mean selector; C8 uses only the previously proven C5 unconditional mean, so it does not depend on #280's unfinished integration.

## 3. Strict finite K8 star separation, exact without 8! enumeration

Set V=8. Identify each sixset R with the complementary two-edge R^c. Let source and target both consist of the 7 complements of a star of K8 centered at original vertex 0, all source weights 1.

A full S8 permutation transports this star to a star centered at g(0). Two different stars share exactly one edge, identical centers share seven, so U(g)=1 or 7. The C7 global rearrangement floor is zero (21 source zero sixsets, seven target cells). Conditioning only on D={0} yields

```text
L_D(0→0)=7;
L_D(0→j)=1, j≠0;
L_D=1.
M_f=7, |T|=7, N=C(8,6)=28;
floor(E U)=floor(49/28)=1.
```

Thus `1 ≤ min_g U(g) ≤ 1`: EXACT minimum 1, witnessed and independently checked by all 40320 full permutations as an optional falsifier. Both the strengthened lower and the expectation upper are needed; no S8 factorial proof search is needed to establish it analytically.

This is an elementary generic K8 star example, **NOT** a legal W(3,2) GQ left embedding nor a physical K_a 2-factor target. It proves the strictness of the generic conditional-relaxation hierarchy only.

## 4. Genuine W(3,2) diagnostic and missing asymptotic step

Reuse original GQ B/A source m_f of C0 (mass 5000, support 3076 on C(15,6)=5005 sixsets) and genuine occupied full physical K6 target |T(F)|=70. Test both lex/reverse-line left f with actual physical-right map g. Their fixed overlap remains 98 and 77 respectively. The C5 existential upper is `floor(5000*70/5005)=69`, i.e. SOME other correlated right map for each fixed f,F has B/A ≤69; neither fixed historical map need be the minimizing one.

For D=∅, (0), (0,1), the oracle computes three monotonically nondecreasing *universal over right g* lower values L_D for the fixed f,F using exactly 1,15,210 partial right-image assignments; each must be ≤ the true min and ≤ the known concrete fixed-right U. **Numerical low-pin lower values are evidence only after exact PR-head CI; no a priori positivity or W32 optimum is claimed.** The source is very sparse relative to C(15,6), so small-k relaxations may remain zero and may not separate legitimate GQ correlation.

## 5. Acceptance, prior art, next formal blocker

Conditional weighted rearrangement and the expectation method are elementary combinatorial optimization/probabilistic-method tools; no new general representation-theory, Johnson, or conditional-expectation theorem is claimed. New engineering contribution is an exact scope-controlled GQ-specific research gate with independent original/physical falsifiers and fail-closed prefix enumeration.

- **Acceptance pending** exact PR HEAD hosted `hyp105-c8-contract` + full Research SUCCESS, then merge only after #279 and earlier C1–C6 are accepted sequentially. #280 is a parallel C7 that needs separate reconciliation.
- **Never infer** `inf_{f,g} S_seven(f,g)=Ω(s^6)`, a genuine infinite B counterfamily, full GF5 R3, or ASET exponent from these results.
- **C9 proof gate:** find a GQ-/physical-completion-specific structural invariant giving L_D=Ω(s^6) with k small enough for all-h proof, OR formally prove why every bounded-k family cannot certify such a positive floor, then study stronger orbit/correlation constraints. A finite W32 numerical positive lower for fixed f,F alone would not close #230.

## C9 subsequent correction — two-pin method cannot certify all-h positive B/A floor

[C9 proof](HYP-105-G5-E2-B3-E1C9-TWO-PIN-ZERO-BARRIER.md) shows that for EVERY s=2^h>=16, every legal GQ source f, every physical occupied F, and EVERY original pinned subset of size <=2 with ANY injective images, the **C8 per-fiber independent rearrangement bound** is identically zero. This overrides any interpretation of the C8 low-pin hierarchy as a plausible asymptotic positive obstruction; the finite star example remains a true generic K8 toy outside the GQ model. This does NOT imply the actual minimum is zero. Next proof step must couple physical remaining-line constraints or use >=3 pins with stronger GQ structure.
