# TOM-002 — Theorem-level source and transfer audit: OM-116 / OM-140

Status: **SOURCE CLAIMS AUDITED / DIRECT TRANSFER NO-GO**  
Date: **2026-10-08**  
Program: [issue #37](https://github.com/definitely-stable/Mathlab/issues/37), separately from LENT-001 G2B and HYP-002 #25.  
External pin: [openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb)  
Prior registry: [OM-116](catalog/INDEX.md#om-116), [OM-140](catalog/INDEX.md#om-140)

## Research integrity summary

This review reads the **original, pinned manuscript LaTeX source** at statement and selected proof-step level, including the *previously missed positive-characteristic manuscript* in the same OM-116 family. The external papers' entire proofs have **not been independently checked**, and Mathlab **did not run Lean or Comparator**. All claims remain `EXTERNAL_MANUSCRIPT_CLAIM`, not Mathlab theorems. Citations below refer to the first-party sources, not derivative secondary summaries.

| Area | Primary claim established *as the author's exact statement* | Bar to transferring to Mathlab | Decision |
| --- | --- | --- | --- |
| OM-116, char 0 | One rational tuple detects every nonzero division-free noncommutative formula of size ≤s, n variables, over **any characteristic-zero field**, with matrix dimension ≤2ns² | Recipe divides by integer r; denominators can vanish in GF(p) | **NO-GO naïve reduction** |
| OM-116, char p | **Separate October 4 manuscript** claims one explicit tuple in `Mat_D(F_p)^n`, `D=O(n³s⁶)`, uniformly for extensions and p=2 | Solves a **different PIT operation**. No ASET cardinality bound follows. Selected `lean/docs/116.md` doesn't list this positive-char theorem as a comparator | **SOURCE EXISTS; NO NEW PIT EXISTENCE TARGET** |
| OM-140 | For each fixed A>0, one-pass Gaussian linear learner with M≤Ad² persistent bits and 2/3 spherical-prior success at angle ε needs `T≥c_A d log(1/ε)` | Random real-Gaussian measurements, sphere prior and approximate angular estimation ≠ discrete finite-field exact updates, maintained-state certificates or cell probes | **NO-GO direct lower-bound reuse** |

## A. OM-116: statements, proof dependencies and positive-characteristic correction

### A1. Primary manuscript for characteristic zero

Sources:
- [Introduction and main theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/introduction.tex)
- [Acyclic formula representation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/formula-systems.tex)
- [Iterated integral encoding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/iterated-integrals.tex)
- [Wronskian/multiplicity argument](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/multiplicity.tex)
- [Matrix construction, cost, proof conclusion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/construction.tex)
- [Lean scope 116](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/116.md) · [FormulaHitting comparator manifest](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/FormulaHitting.json) · [named solution module](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Algebra/FormulaHitting/Hitting.lean).

**Main statement (author).** Given integers `n,s≥1`, a deterministic algorithm constructs `(T_1,…,T_n)∈Mat_D(Q)^n` with `D≤2ns²`, each entry encoded with polynomial bit complexity. For every characteristic-zero field F and every **nonzero** `f∈F⟨x_1,…,x_n⟩` given by a *division-free ordered noncommutative formula* of size at most s, `f(T_1,…,T_n)≠0`. No inverse-gates, unrestricted shared DAGs, commutative quotient or finite-field guarantee is part of this statement.

**Selected proof skeleton (author; not re-proved):**
1. Turn the formula into an acyclic coefficient system on ≤2s states (formula-systems).
2. Encode words as iterated integral power series using `J_i(a)=∫_0^z a(t)/(t+i)dt`; order of letters matters and word series are linearly independent (iterated-integrals).
3. Apply a characteristic-zero Wronskian / multiplicity bound to the nonzero resulting series, obtaining `ord_0(h_f)≤(n−1) C(2s,2)+2s−1≤2ns²−1`.
4. Truncate Taylor coefficients to `D=2ns²` and represent the integral operators by rational matrices
   `(T_i)_(r,c)=(-1)^(r−c−1)/(r i^(r−c))` when `0≤c<r<D`, otherwise 0. Nonzero truncated series forces a nonzero first column of `f(T)`.
5. Matrix printing and rational arithmetic have a separate explicit polynomial **bit** bound; selected Lean comparator `OAI.NCHitting.universal_hitting` covers the universal-hitting statement, while author Lean scope explicitly excludes separate construction-time/dimension estimates from this selected theorem.

**Exact obstruction to an invalid GF(p) deduction:**

- For `n=1,s=2,D=8,i=1,r=3,c=2`, the construction has a `1/3` entry; it is undefined in characteristic 3. Even where a rational reduction exists, the characteristic-zero Wronskian reasoning does not transfer: in characteristic p the independent series `1,z^p` have identically zero Wronskian.
- This **does not prove that positive-characteristic hitting points are impossible**, only that this particular field-homomorphism / derivative argument is not uniform in p. See the next subsection.

### A2. Previously omitted October 4 positive-characteristic construction (critical correction)

Source: [author manuscript package](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/README.md), [main TeX](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/main.tex), [Theorem 1.1 statement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/introduction.tex), [characteristic-independent word encoding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/words.tex), [shift systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/systems.tex), [order bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/order.tex), [construction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/construction.tex) and [primary PDF](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf).

**Main statement (author).** A single deterministic machine, given promised prime `p` in *binary* and positive `n,s` in *unary*, produces `D=O(n³s⁶)` matrices over the **prime field F_p**. The same tuple detects every nonzero size-s division-free noncommutative formula with arbitrary scalar coefficients over **any extension field of characteristic p**. Both output length and running time are polynomial in `n+s+log₂(p)+1` in the stated bit-complexity model. This includes p=2, with no assumption `p>s`.

**Separate proof strategy described in the author source:** a multiplicative shift encoding of words avoids dividing by integers; finite shift systems and characteristic-independent order estimates replace integration/Wronskians; the author constructs finite matrices and descends from a rational-function coefficient field to the prime field. The class extends to specific acyclic path programs. These proof steps were inspected in their source sections but not rederived line by line.

**Lean-scope mismatch:** the pinned [`lean/docs/116.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/116.md) and `FormulaHitting.json` list a *characteristic-zero rational tuple* and separate *rational formula hitting lists*. They do **not** list a positive-characteristic theorem as a selected comparator result. Thus it is **incorrect** to say "positive-characteristic case has no author manuscript"; also **incorrect** to claim the October 4 theorem was independently Lean-validated by our inspection. The scope is narrower than the family headline.

**Implication for HYP-002.** This is polynomial **identity testing** of formula representations, not construction of maximal bounded-support column families with injective `d≤2` *commutative additive subset sums*. A hypothetical reduction would need to specify:
- how each ASET collision becomes a nonzero formula with a size bound;
- how a hitting tuple provides a non-collision *capacity upper/lower bound* rather than simply a test for one fixed polynomial;
- how evaluation state, matrix dimension, field size, support w and bit cost transfer.
None is supplied. **NO DIRECT ASET theorem**; at most a secondary methodological comparator for encoding finite-field algebraic identities.

**Earlier primary prior art:** [Raz–Shpilka, 2005, deterministic PIT for noncommutative formulas/ABPs](https://doi.org/10.1007/s00037-005-0188-8). Their result is an established deterministic **representation-aware** test; a *single oblivious matrix tuple* is a different black-box objective. This distinction must survive any novelty claim.

## B. OM-140: exact streaming-memory theorem and its dependency shape

Sources:
- [Author primary model and theorem, introduction.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/introduction.tex)
- [Local mass estimates](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/local-mass.tex)
- [Exact projection-density bounds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/projection.tex)
- [Backward block lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/blocks.tex)
- [Finite-state stream propagation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/streaming.tex)
- [Reflection and final lower-bound proof](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/sections/endpoint.tex)
- [Author Lean scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/140.md) · [MemoryPrecision comparator](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/MemoryPrecision.json) and [solution module](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Probability/MemoryPrecision/Main.lean) · [NoiselessRegression comparator](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/NoiselessRegression.json).

**Exact author model:** unknown `S` uniformly distributed on `S^{d−1}`; independent `x_t~N(0,I_d)`; observation `(x_t, ⟨x_t,S⟩)` is real-valued and noiseless. One-pass learner keeps one of ≤`2^M` persistent states between samples; per-step computation and fresh randomization are unrestricted; current observation can be used completely, but old observations cannot be revisited. The output depends only on terminal state, stopping index and fresh randomness. Stopping before a predetermined *finite* horizon T is allowed. The output is unit-length and scored by **angular** error.

**Main source theorem:** for each **fixed** `A>0`, there exist `c_A>0,d_A` such that for `d≥d_A`, `M≤A d²`, `0<ε≤1/10`, and uniform-sphere prior success at least 2/3, the horizon must satisfy

`T ≥ c_A d log(1/ε)`.

The constant depends on fixed A; there is no uniform claim when `A=A(d)→∞`. For `M=o(d²)`, the corollary gives an absolute c eventually. "All signals" success implies the average-prior premise, not conversely.

**Selected dependency outline (author; not independently proved):**
1. Terminal state cannot remember signal beyond finite label, so spherical caps bound localized success mass at scale `ε` (local-mass).
2. Gaussian projection densities and a Hölder argument yield a **backward block** propagation bound. With N destination labels its scale changes roughly by a factor `exp(Cd/a) N^(1/(a q))`, where `a≈d/2`, `q≈d/8`; this quantifies *information lost to finite memory*.
3. Propagate over `B≈T/q` blocks, bounding maximum success by `(2 ε exp(C(1+A)B))^a`; force `T=Ω_A(d log(1/ε))` for sufficiently fine accuracy.
4. For coarse/constant accuracy, reflect S across the Gaussian row span: both `S` and its reflection give the same observations. This produces a separate baseline `T>d/4` for success 2/3, completing all `0<ε≤1/10`.

**Two invalid transfers:**
- The learner's finite-state **bit count** is not a count of arbitrary exact real registers. Without the bit constraint, d linearly independent Gaussian equations determine the unknown vector almost surely once the pairs are retained, so the lower bound cannot be quoted for unlimited-precision persistent registers.
- Gaussian random linear observations + approximate angular recovery are **not** finite-field point updates + exact unchanged certificates. No reduction from O01's maintained DAG input state to this spherical measurement model is supplied. A `Ω(d log(1/ε))` sample bound is not a `Ω(log n)` update time/cell-probe bound.

**Primary pre-2026 nearest comparators (model mismatches stated):**
- [Sharan–Sidford–Valiant, STOC 2019 / arXiv:1904.08544](https://arxiv.org/abs/1904.08544): Gaussian linear regression with **small nonzero noise**, subquadratic memory, `Ω(d log log(1/ε))` sample bound in specified accuracy regime. Do **not** describe it as the same noiseless theorem.
- [Dagan–Kur–Shamir, 2019, arXiv:1902.03498](https://arxiv.org/abs/1902.03498): streaming linear prediction/regression and quadratic-scale memory lower bounds in their own model. Does not entail the stated 2026 epsilon-sensitive result as written.

## C. Finite falsification oracles — what they do *not* show

`research/test_tom_transfer.py` tests:
- the `1/3` coefficient of the **char-zero** hitting recipe cannot be reduced mod 3;
- rational coefficients with invertible denominators can be reduced to GF(5);
- the Wronskian of independent `1,z^p` is zero in characteristic p;
- two explicitly retained full-rank exact equations recover a 2D unit signal; this only demonstrates the importance of the **bit** memory constraint, and does not simulate an OM-140 Gaussian distribution;
- a finite-label count is a trivial pigeonhole baseline, not a new information-theoretic theorem.

They are **counterexamples to invalid model transfers, not to either OM author's result**, and cannot verify the global OM-116/OM-140 theorems.

## D. Scientific and product decision / next allowable step

| Candidate transfer | Mathematical verdict | Product verdict |
| --- | --- | --- |
| Use OM-116 char-zero construction directly over GF(3), GF(5) | **REFUTED** (division undefined) | STOP direct reduction |
| Claim nobody has positive-characteristic universal hitting tuple | **FALSE as source claim**: Oct 4 OM-116 manuscript reports one | STOP as "new Mathlab theorem" |
| Use OM-116 hitting theorem to deduce `A_q^{set}(m,3,2)=Θ_q(m²)` | **UNSUPPORTED** (PIT vs extremal support problem) | NO-GO without explicit reduction |
| Use OM-140 memory/sample theorem as O01 DAG certificate lower bound | **UNSUPPORTED** (distribution/output/operation/cost mismatch) | NO-GO without explicit reduction |
| Reuse **research discipline** (exact model, resource counters, no-vacuity, matched lower bound) | **GO as method**, not theorem | Yes, for HYP-002 prior-art and O01 triage |

### Concurrent Mathlab status check (HYP-002)

The authoritative [HYP-002-B quadratic theorem](HYP-002-B-QUADRATIC-THEOREM.md) **already proves** `A_q^set(m,3,2)=Theta_q(m²)` for each fixed odd prime power q using a prefix-pair C4 argument and a Steiner-triple lower construction. The older `O_q(m^(5/2))` upper and `HYP-002-D CONJECTURE` in Phase-A material are superseded historical results. Scientific novelty and finite leading-constant improvements remain under audit in [issue #25](https://github.com/definitely-stable/Mathlab/issues/25); that issue is **not** waiting for a proof of the exponent.

The separate [HYP-002-C decoder evidence](HYP-002-C-EVIDENCE.md) records **STOP_STANDALONE_DENSE_TWO_ID** for its narrow index-free two-ID use case. TOM-002's external theorems neither overturn the quadratic capacity result nor provide a Rust-product GO.

**Research verdict TOM-002:** no mathematically justified direct transfer into a new Rust primitive. This is a useful negative research result and a correction of the OM-116 source catalog. **Do not open a speculative PIT crate** on the basis of a family already asserting the primitive's existence. Continue [HYP-002 #25](https://github.com/definitely-stable/Mathlab/issues/25) within a precisely stated three-cell ASET model, or close O01 if no new maintained-state memory/probe bound survives its separate prior-art audit.

**No publication novelty, full paper proof recheck, or independent Lean proof verification is claimed.**
