# UCT-004 G2-D — ALL-n exact nonlinear witness length via PPZ isolated-CNF coding

**Date:** 2026-10-09. **Issue:** [#98](https://github.com/definitely-stable/Mathlab/issues/98); parent [G2-C #93](https://github.com/definitely-stable/Mathlab/issues/93). **Status: PROVED_DERIVED_CLASSICAL (not an original scientific lower-bound discovery).** The PPZ coding lemma is **prior art (1999)**, the parity CNF/circuit connection is **prior art (2022)**. The application is a rigorous, separately scoped bridge to Mathlab's operational verifier-cover model, with no Rust or product API.

## I. One frozen noninteractive verification experiment

n≥1. Input x∈{0,1}^n is stored as n raw input bits (equivalently, under [UCT-003](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md) in any injective representation of the complete n-toggle hypercube with at most **one physically changed stored bit per coordinate toggle**, up to a public bit permutation and offset). Public Boolean claim a∈{0,1} asserts parity(x)=a. The prover supplies a **fixed b-bit untrusted message π**, chosen *before* an independent **private verifier random seed R**. The verifier may perform arbitrary computation and make **at most p adaptive bit probes** to x, 1≤p≤n. Witness length b excludes the separate claimed answer bit a.

- **Perfect completeness:** for every true pair (x,a=parity(x)) there is one π such that Pr_R[accept(x,a,π)]=1.
- **Universal strict soundness:** there exists **one δ<1** such that for every false pair (y,a≠parity(y)) and every π∈{0,1}^b, Pr_R[accept(y,a,π)]≤δ.
- Fixed public program/tables may have exponential size; random coins, CPU, proof creation, full-proof-bit parsing and communication are **not charged by p**. Thus the theorem is not end-to-end, online-Merlin–Arthur, proximity/cryptographic, word-cell-probe or robust to a prover observing R.

Let κ(n,p) be the exact minimum number of p-separable subsets needed to cover **one parity class**, as proved equal to proof-message capacity in [G2-C](UCT-004-G2-C-NONLINEAR-PROOF-COVER.md), where H⊆X_a is **p-separable** when every opposite-parity y has some |S_y|≤p with y restricted to S_y different from the restriction of *every* x∈H. The choice of S_y may depend on y and H but not the unknown true x.

## II. Lemma A — a p-separable fiber embeds in an isolated p-CNF

**LEMMA (SELF-CONTAINED).** Every nonempty p-separable H⊆X_a is contained in the satisfying-assignment set of some Boolean CNF F_H over **only the n data bits**, with **each clause width at most p**, such that every satisfying input has parity a. Hence every satisfying assignment of F_H is **isolated**: flipping any one input bit makes it unsatisfying.

**Proof.** For each y∈X_(1−a), choose S_y guaranteed by p-separability. Form the clause

    C_y(z) := OR_(i∈S_y) (z_i != y_i).

It is false exactly if z agrees with y in all S_y. Because each x∈H differs from y on S_y, every x∈H satisfies every C_y. But y violates C_y, so F_H:=AND_(y∈X_(1−a)) C_y rejects every opposite-parity state. Every satisfying state z therefore has parity a, and each immediate Hamming neighbor z⊕e_i has opposite parity and is rejected. Every clause has width≤p, and |H|≤|SAT(F_H)|. QED.

**Connection back to the actual verifier.** The G2-C finite transcript-coupling equivalence, under perfect completeness + δ<1, proves that every honest witness fiber H_(a,π) is p-separable even for **adaptive nonlinear** verification with arbitrary private-coin distributions: choose for each opposite y one positive-measure rejection coin that belongs simultaneously to the full-measure acceptance events for all finitely many x∈H. The rejected y-path probes a separating S_y. No linearity, fixed query plan or finite coin support is required.

## III. Lemma B — PPZ isolated-solution bound, with independent proof

**LEMMA (Paturi–Pudlák–Zane 1999, CLASSICAL).** If a CNF F on n Boolean variables has clause width at most p≥1 and **all its satisfying assignments are isolated**, then

    |SAT(F)| ≤ 2^(n−n/p).                                      (PPZ)

**Self-contained probabilistic proof.** Fix satisfying x. Since x is isolated, x⊕e_i is unsatisfying for each i. Some clause C_i of F is true under x *only* by its literal on coordinate i: otherwise x⊕e_i would still satisfy it and all other clauses. Choose one such **critical clause** for each i, length l_i≤p. Now run the standard PPZ procedure: pick a uniformly random variable permutation σ; assign variables in that order, using the value **forced** by a unit clause whenever present, otherwise toss an independent fair bit. Along the trajectory matching x, if coordinate i is processed **last among the variables of its critical clause C_i**, it is forced correctly. For each fixed σ let f_x(σ) be the number of forced decisions along the x trajectory. Conditional on σ, the probability the procedure outputs x is exactly 2^(−(n−f_x(σ))) (forced decisions along x are consistent; aborts off the trajectory are irrelevant). Every i-last event forces i, so

    E_σ f_x(σ) ≥ Σ_i Pr_σ[i last among C_i]
               = Σ_i 1/l_i ≥ n/p.

Because u→2^u is convex, Jensen yields

    Pr[PPZ outputs x] = 2^(−n) E_σ 2^(f_x(σ))
                      ≥ 2^(−n+n/p).

PPZ emits **at most one assignment per run**, so the output events for distinct satisfying x are disjoint. Summing these lower bounds over all satisfying x gives |SAT(F)|·2^(−n+n/p)≤1. QED.

This proves exactly the isolated-solution quantitative fact used from [PPZ, *Satisfiability Coding Lemma*, CJTCS 1999](https://doi.org/10.4086/cjtcs.1999.011); it does not independently reprove the complete original PPZ paper. The 2022 [Emdin–Kulikov–Mihajlin–Slezkin *CNF Encodings of Parity*](https://doi.org/10.4230/LIPIcs.MFCS.2022.47) uses the same isolated solution lemma and analyzes nondeterministic parity CNF depth-three formulas. Its **maximum clause width counts auxiliary-guess literals as well**; our selected-witness clauses C_y contain *only data bits*, so one must not equate the two width budgets without a translation.

## IV. Main theorem — sharp proof bits for EVERY n,p even under nonlinear/adaptive verification

**THEOREM G2-D (DERIVED_CLASSICAL, EXACT for the frozen model).** For every n≥1 and 1≤p≤n, the minimum fixed-size untrusted proof length for **perfect completeness and any uniformly strict soundness δ<1** is exactly

    +--------------------------------------------------+
    | b_min(n,p) = ceil(n/p) − 1.                       | (D1)
    +--------------------------------------------------+

**Necessity.** For fixed a, each proof value π induces an honest fiber H_(a,π) of states accepted with probability one. These fibers cover X_a of size 2^(n−1). By G2-C transcript necessity, each nonempty H is p-separable. By Lemmas A+B,

    |H_(a,π)| ≤ 2^(n−n/p).

There are ≤2^b proof strings. Therefore

    2^(n−1) ≤ 2^b · 2^(n−n/p),
    b ≥ n/p − 1.

As b is an integer, b≥ceil(n/p)−1.

**Sufficiency, sharp construction.** Let g=ceil(n/p). Partition the n input coordinates into g nonempty disjoint blocks, each of size≤p. The honest prover sends the parities of the first g−1 blocks (exactly b=g−1 bits). Given the claimed full parity a, the verifier infers the parity of the last block, uses private coins to sample one block uniformly and checks its actual parity with ≤p data probes. Every true state has an honest perfectly accepted proof; for any false claim and any π, the claimed vector of g block parities has the wrong XOR, so at least one block's claimed parity differs. Acceptance is ≤1−1/g<1. Hence b_min≤g−1, matching necessity. QED.

**Warning on soundness strength:** When g→∞ the constructed δ=1−1/g→1, **not a fixed nontrivial constant** such as 1/3. Earlier G2-A gives p≥n(1−α−δ) for complete unit-write parity, which separately obstructs low p at fixed δ. The theorem D1 quantifies over protocols with *some* δ<1; do not advertise it as an optimal b bound with δ fixed independently of n.

**Warning on costs:** The real verifier reads b proof bits and computes a block parity; the honest prover must obtain/maintain the block parities, and any authenticated commitment/root is a separately charged persistent object. D1 is a mathematical bit-probe/witness-storage frontier and not a fully priced distributed system design.

## V. THE DISTINCT OPEN QUESTION: exact κ(n,p) versus exact b

Lemma A+B gives

    ceil( 2^(n/p−1) ) ≤ κ(n,p) ≤ 2^(ceil(n/p)−1).       (D2)

D1 follows from (D2) **even when the two bounds do not coincide** because b_min=ceil(log2 κ). Thus the previously tempting general conjecture

    κ(n,p) ?= 2^(ceil(n/p)−1)

is **still OPEN**, not implied by D1. In particular:
- p=n: κ=1, b=0.
- p=1: κ=2^(n−1), b=n−1.
- p divides n: κ=2^(n/p−1) **EXACT for every such pair**, from matching D2.
- n/2≤p<n: κ=2, b=1.
- n=7,p=2: (D2) allows 6≤κ≤8, though it already certifies b_min=3. A claimed exact κ=8 in this case needs independent combinatorial proof or exhaustive certificate, not an exponent-rounded witness argument.
- n=4,p=3: a non-linear fiber of size 6 is consistent with PPZ's floor(2^(8/3))=6, refuting an incorrect affine-rank fiber cap 4; κ=2 remains exact.

## VI. Novelty and further theorem bricks

**THEOREM status:** exact b_min is **PROVED_DERIVED_CLASSICAL**, not certified worldwide novelty. The proof is an exact-scoped application of PPZ isolated-CNF coding + nondeterministic cover representation. The input-to-CNF reduction is written out to avoid importing stronger assumptions from the source. It does NOT imply an original general local-read/write/prover/annotation-cost theorem beyond all known literature. It resolves Mathlab's *internal* all-n nonlinear **witness-bit** research gap, but not exact κ or stronger fixed-soundness tradeoffs.

**NEXT (G2-E novelty gate):** Find the exact κ gap for non-divisible n/p; separately freeze online proof-generation cost, verifier processing and update-access in a real joint model, compare [CNF Encodings of Parity 2022](https://doi.org/10.4230/LIPIcs.MFCS.2022.47), [PPZ 1999](https://doi.org/10.4086/cjtcs.1999.011), [dynamic bit probes 2007](https://doi.org/10.1016/j.tcs.2007.02.058), online-MA and 2026 certification complexity **before** claiming originality. An exact short proof under unpriced verifier/program work is insufficient as a strong original paper target.

**Reproducibility:** `research/test_uct004_ppz_all_n.py` independently enumerates every small p-projection CNF, verifies isolation/critical clauses, checks PPZ per-solution probabilities, tests all integer (n,p) bounds to n=128, p=1/n/divisibility endpoints and constructs all honest/malicious block witnesses in finite cases. Executable tests do not prove the all-n theorem; the deductive argument does.
