# UCT-004 G2-C — exact nonlinear sound-witness cover theorem (finite representation model)

**Snapshot:** 2026-10-09. **Issue:** [#93](https://github.com/definitely-stable/Mathlab/issues/93). **Evidence:** self-contained **DERIVED_CLASSICAL** equivalence, independent finite exact oracles. The conjectured closed form for all n,p is **NOT PROVED**, and publication novelty is **NOT VERIFIED**. The prior G2-A linear theorem has [separate restricted assumptions](UCT-004-G2-A-SOUND-WITNESS-PACKING.md).

## 1. One exact noninteractive private-coin model

State x∈{0,1}^n is stored as n input bits. This is the natural complete coordinate-toggle representation (physical update writes w=1, with no uncharged root/history). Public query is the parity of **all** n bits; a prover supplies a public claimed answer a∈{0,1} and one **fixed-length** b-bit witness π selected **before** the verifier's private randomness R. The verifier has only x as a bit-probe oracle, can make ≤p adaptive bit reads, and returns accept/reject. For every true (x,a=parity(x)) there must exist a witness accepted with probability **1** (perfect completeness). For every wrong a and every π the acceptance probability must be ≤δ for a uniform δ<1 (**nontrivial soundness**, not a fixed target 1/3). The verifier can use arbitrary nonlinear predicates, adaptivity and unbounded computation on π; proof communication, randomness, instruction/program size and verifier CPU are not bounded by p, hence no end-to-end new-theorem claim.

Define parity class X_a={x∈{0,1}^n:⊕_i x_i=a}. Fix 1≤p≤n. Call a nonempty H⊆X_a **p-separable** if:

    for every y∈X_(1-a), there exists S_y⊆[n], |S_y|≤p,
    such that for every x∈H: x restricted to S_y != y restricted to S_y.    (C1)

The empty set may be treated as trivially separable, but is unnecessary for coverings. It is crucial that S_y may depend on y **and on H**, not on the unknown honest x, and a chosen verifier coin selects it independently of the input's returned data.

Let κ_a(n,p) be the smallest number of p-separable nonempty sets H whose union equals X_a. Bit-flipping any fixed coordinate sends X_0 to X_1 and preserves all p-projections, so κ_0(n,p)=κ_1(n,p). Denote the common value κ(n,p).

## 2. Master G2-C finite model theorem (exact equivalence)

**THEOREM G2-C1 (DERIVED_CLASSICAL).** A fixed-length b-bit noninteractive private-coin protocol with perfect completeness, worst-case p input-bit probes and *some* uniform soundness δ<1 exists **if and only if**

    κ(n,p) <= 2^b.                                                       (C2)

Hence the exact minimal fixed witness length, without charging program/prover cost, is

    b_min(n,p) = ceil(log2 κ(n,p)).                                      (C3)

**Necessity.** Fix a claim a and a witness π. Let H_(a,π) be the set of true-a inputs accepted with probability 1 when given π. These honest sets cover X_a by perfect completeness. If H is nonempty and y has the opposite parity, the verifier accepts wrong (a,π) at y with probability ≤δ<1, so a positive-measure set of coins rejects at y. Every x∈H is accepted with probability 1, and H is finite; intersecting their full-measure acceptance coin sets with the rejection set for y gives at least one coin outcome r on which the verifier rejects y but accepts **all** x∈H. On its adaptive execution over y at this fixed r, the verifier reads at most p coordinates S_y. Were any x∈H identical to y on S_y, an inductive identical-read-transcript argument would force it to take the same adaptive branches and also reject, contradiction. Thus S_y satisfies (C1). There are only 2^b possible π strings for a fixed a, so X_a is covered by at most 2^b separable H. QED.

**Sufficiency.** Choose for each a a covering H_(a,k), k=1..K, with K≤2^b, and pad k to b bits. The protocol on claim a and witness k samples one **opposite-parity** state y uniformly from X_(1-a); in the public hard-coded table for that (a,k,y) select one separating set S_y promised by (C1). Probe x on all coordinates in S_y and **accept iff** x restricted to S_y is *different* from y restricted to S_y. If x∈H_(a,k), the comparison differs for every y and the verifier always accepts. For any actual opposite-parity input x, the random sampled y equals x with probability 1/|X_(1-a)|=2^(1-n), in which case the verifier certainly rejects, regardless of k. Therefore all malicious witnesses satisfy

    δ <= 1-2^(1-n) < 1; completeness alpha=0.                            (C4)

The construction is finite, permits adaptive verifiers (but uses **nonadaptive** tests in this direction), uses at most p **data** probes, and has unbounded precomputed/public model tables and Θ(n) verifier coin bits. It does **not** say that δ is a practical constant such as 1/3; if n grows, (C4) approaches 1, which is unacceptable for most cryptographic uses. QED.

**Exactness warning:** Equation (C2) is an operational covering *characterization*, not an efficient way to compute κ, an asymptotic closed-form optimal b, or a theorem about computationally bounded adversaries.

## 3. Special cases, bounds, and the nonlinear rank fallacy

- For p=n, H=X_a itself is n-separable (read all n bits to detect wrong y), κ=1 and b_min=0. This is sharp.
- For p=1, each p-separable H has at most **one** element: if x≠z are same-parity states, choose a differing coordinate i, y=x⊕e_i. Any one-coordinate projection of y matches x except possibly at i, where it matches z. Thus no one-coordinate projection excludes both x and z. Consequently κ=2^(n-1) and b_min=n-1, consistent with G2-A.
- Partition the n bits into g=ceil(n/p) blocks of size≤p. Fix the parities of the first g−1 blocks as witness bits and use the claimed global parity for the last. The 2^(g−1) corresponding affine sets are p-separable and cover X_a; thus

    κ(n,p) <= 2^(ceil(n/p)-1),  b_min(n,p)<=ceil(n/p)-1.                 (C5)

**HISTORICAL G2-C LIMITATION, NOW PARTIALLY RESOLVED BY G2-D (2026-10-09):** the all-n equality for **witness bits** b_min=ceil(n/p)−1 is now PROVED even for nonlinear/adaptive verification by reducing every p-separable fiber to isolated p-CNF and applying PPZ's classical coding lemma. See [G2-D](UCT-004-G2-D-ALL-N-PPZ-PROOF-BITS.md). **The stronger exact integer covering equality κ(n,p)=2^(ceil(n/p)−1) for nondivisible n/p remains CONJECTURE.** G2-A was previously restricted to linear one-check GF(2) tests.

For n=4,p=3, the six even-weight-two strings form one p-separable H, whereas every affine GF(2) linear-check fiber of rank ≥ceil(4/3)=2 has size≤4. Thus the rank proof **cannot be transplanted** to arbitrary H even though the eventual κ(4,3) equals 2. This falsifier is checked separately by `research/test_uct004_nonlinear_scope.py`.

## 4. Exact finite table and independent verification gate

The following κ values are **finite exact computational results**, not asymptotic formulas:

| n | p | number κ(n,p) | minimum b bits | largest one-proof p-separable fiber |
|---|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 | 1 |
| 3 | 1 | 4 | 2 | 1 |
| 3 | 2 | 2 | 1 | 2 |
| 4 | 1 | 8 | 3 | 1 |
| 4 | 2 | 2 | 1 | 4 |
| 4 | 3 | 2 | 1 | 6 |
| 5 | 1 | 16 | 4 | 1 |
| 5 | 2 | 4 | 2 | 4 |
| 5 | 3 | 2 | 1 | 8 |
| 5 | 4 | 2 | 1 | 12 |

**Method:** exhaust all nonempty subsets H of X_0 (at n=5 there are 2^16−1=65,535 candidate sets), for each opposite y exhaust all nonempty coordinate subsets S of size≤p and test (C1); keep inclusion-maximal p-separable H; solve exact finite set cover over all 2^(n−1) true states, and independently check selected coverings and failure of any smaller cover. The complement X_1 gives the same results by coordinate translation. Implementation: `research/test_uct004_nonlinear_cover.py` (Python stdlib only; hosted CI) and an independently written small JS enumeration as an upstream falsification oracle. The independent CI oracle result is mandatory before accepting the displayed numbers as verified.

The maximum one-proof fiber **is not** generally 2^(n-ceil(n/p)): for n=4,p=3 it is 6>4, and n=5,p=4 it is 12>8. This is a strict finite model counterexample to a dangerously appealing extension of the affine-rank argument.

## 5. Source and scientific novelty barriers

- **2026 primary** [Kayal–Laplante–Larroque–Prūsis–Vihrovs, *Certification complexity of Boolean functions*, ECCC TR26-206 (Sep 22 2026)](https://eccc.weizmann.ac.il/report/2026/206/): abstract already formalizes operational certification and connections to classical randomized certification; the full source proof has **NOT** been independently compared theorem-by-theorem here. This is a serious PRIOR_ART novelty gate, not external verification of (C2).
- [Ben-David–Kothari 2026, arXiv:2609.15063](https://arxiv.org/abs/2609.15063) shows (authors' abstract) that bounded-error randomized query complexity need not dominate deterministic certificates, and must not be confused with perfect-completeness untrusted witness soundness.
- Aaronson 2008 randomized certificate complexity, Ambainis et al. 2021 fractional adversary equivalence, and ordinary nondeterministic decision-tree certificate covers are essential earlier bases.
- PCPP/proximity proof literature studies rejection on **far** incorrect inputs; a one-bit parity flip is distance 1/n and requires our exact adversarial model.

**Decision:** G2-C1 is a useful **DERIVED_CLASSICAL exact characterization** of a restricted proof game. Exact κ values n≤5 are FINITE_EXACT once CI passes. **No claim of a new worldwide strong theorem**, no original general closed form, no Rust/crate/public API. The next actually hard theorem must either prove κ(n,p)'s closed form with nonclassical methods and a strict overlap audit, or more promisingly introduce **fully priced** program/witness maintenance/time, authenticated state and repeated adaptive queries to escape the free-table protocol (C4).

## 7. G2-D cross-reference — what was actually resolved later (2026-10-09)

The later [ALL-n nonlinear verifier PPZ proof](UCT-004-G2-D-ALL-N-PPZ-PROOF-BITS.md) shows that the **minimum b-bit proof length** from (C3) equals **ceil(n/p)−1 for every n,p**, by an independent reconstruction of the classical 1999 isolated-CNF coding lemma. It provides bounds **ceil(2^(n/p−1))≤κ(n,p)≤2^(ceil(n/p)−1)**. These establish the exact b even though they may NOT determine κ itself; when p|n the bounds on κ also coincide, but for nondivisible ratios a gap can remain. Prior G2-C finite κ table still stands. The genuinely original fully priced online verification theorem and general exact κ remain OPEN.
