# UCT-004 G2-A — sound-witness influence packing and a sharp randomized parity endpoint

**Snapshot:** 2026-10-09. **Issue:** [#87](https://github.com/definitely-stable/Mathlab/issues/87). Parent [UCT-002 #77](https://github.com/definitely-stable/Mathlab/issues/77), [UCT-003 read/write #82](https://github.com/definitely-stable/Mathlab/issues/82). **Status: SELF-CONTAINED DERIVED_CLASSICAL / PROOF-CHECKED FINITE ORACLES / NO ORIGINAL NONFACTORIZING GENERAL THEOREM.** This is a rigorously priced *partial* dynamic model, not a complete authenticated distributed protocol.

## 1. Exact trust and cost contract — no hidden oracles

Let X be finite. The persistent representation is a deterministic binary encoding M:X→{0,1}^m. Updates e=(x,y) change the set of physical stored cells S_e={c:M(x)_c≠M(y)_c}, with locality |S_e|≤w. (This is **changed** cells, not read/write accesses, execution time, or charged word writes.) Fix a public query index j and a Boolean observable f_j:X→{0,1}. Assume X contains every state used in the proof. Query receives **only** the fixed claim a∈{0,1}, a finite prover string π of ≤b bits, public protocol/j, and independent private verifier coins R. It adaptively reads stored bit cells of M(x), at most p bit probes. The verifier is permitted arbitrary computation on π in the lower-bound model, but the *physical size, time to read π, prover generation work, authenticated trust root, and online publication timing* are separately **unpriced by the theorem** and MUST be charged in a real product/protocol.

**Soundness:** for every x,j and every (a,π) with a≠f_j(x), Pr_R[V^{M(x)}(j,a,π)=accept]≤δ. This is universal over malicious witnesses, **not** merely the honest prover's distribution.

**Completeness:** for every x,j there exists a fixed π_xj (selected independently of R), with a=f_j(x), such that Pr_R[V^{M(x)}(j,a,π_xj)=accept]≥1−α.

Assume 0≤α,δ≤1; when α+δ≥1 the lower bound is vacuous. External keys, roots, reference snapshots, commitments or update transcripts must be encoded in M or counted as separately accessed state. If prover sees the current R before choosing π, the proof below does NOT apply without stronger adaptive soundness. The verifier reads a public claim a and a finite witness π, so **the theorem does not lower bound the number of bits the verifier must read from π**.

## 2. Theorem G2-1 — probabilistic soundness forces observable update reads

Fix x,j, a=f_j(x), and **one honest witness** π with acceptance at x ≥1−α. Let y∈X have f_j(y)≠f_j(x). Run V(j,a,π) on M(x) and M(y) using identical coins R.

**THEOREM (DERIVED_CLASSICAL):**

    Pr_R[old-state V touches S_(x,y)] ≥ 1−α−δ.              (G2-1)

**Proof.** Couple both executions with one R. Until a cell differing between M(x) and M(y) is probed, both adaptive programs see identical answers, take identical branches and either accept/reject identically or probe the next identical address. Therefore their final acceptance indicators can differ only when the old-state trace touches S_(x,y). Their marginal acceptance probabilities differ by at least (1−α)−δ because (a,π) is an honest acceptable claim at x but *the same fixed (a,π)* is a malicious incorrect claim at y. Bounding the difference by the probability of touching the difference support proves (G2-1). QED.

**Zero error corollary.** If α=δ=0, every accepted old-state query path for the honest witness must intersect S_(x,y). This extends UCT-003's deterministic influence transversal to untrusted proof witnesses under *perfect soundness*. It is a basic indistinguishable-transcript argument, not a new cryptographic theorem.

## 3. Theorem G2-2 — fractional update-support packing lower bound

For a fixed x,j define the set of all **sensitive alternatives** Y(x,j)={y∈X:f_j(y)≠f_j(x)}. It is legitimate to restrict to any finite selected subset Y' of **allowed one-step outgoing update neighbors** x→y (the more general any-y form does not price how difficult it is to reach y). Let S_y={c:M(x)_c≠M(y)_c}.

Define the fractional packing number of the update-support hypergraph:

    ν*(Y') = max Σ_{y∈Y'} λ_y
    subject to λ_y≥0,
               Σ_{y:c∈S_y} λ_y ≤ 1   for every cell c∈[m].

If any S_y=∅ while α+δ<1, soundness/completeness are inconsistent; otherwise ν* is finite (may be 0 when Y'=∅). The pair (x,j,π) uses **one common fixed honest witness** for all sensitive alternatives; do NOT switch π separately for each y.

**THEOREM (DERIVED_CLASSICAL):**

    p ≥ E_R[number of distinct code cells read]
      ≥ (1−α−δ) ν*(Y').                                        (G2-2)

**Proof.** For any feasible nonnegative weights λ, Theorem G2-1 yields
(1−α−δ)Σ_y λ_y ≤Σ_y λ_y Pr[R touches S_y].
For each actual read set A_R, Σ_y λ_y 1{A_R ∩ S_y≠∅} ≤Σ_{c∈A_R} Σ_{y:c∈S_y} λ_y ≤|A_R|. Take expectation, then maximize over feasible λ. Any at-most-p-probe algorithm reads ≤p distinct cells. QED.

This is a **fractional hitting/packing / classical randomized-certificate adversary converse**, not an independently novel general theorem. Even when ν*>ν (integral packing), **no source novelty** follows: classical fractional block sensitivity / randomized certificate complexity and LP duality address analogous inequalities. Primary source/model ledger: [G2-A source audit](UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md).

## 4. Sharp endpoint: full prefix parity with physical write budget one

Let X=F₂^n with all coordinate toggles x→x⊕e_i, and require **all n prefix parity queries**. From [UCT-003 rigidity](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md), every injective binary representation with at most one changed bit per input toggle must be a fixed permutation/injection of the raw input coordinates, complemented by public constants. For the full-prefix claim f_n(x)=⊕_{i=1}^n x_i, all n outgoing bit-toggle supports S_i are disjoint singletons. Thus ν*=n, so every verifier with private independent coins, completeness≥1−α, soundness≤δ, and any finite untrusted witness length obeys:

    p ≥ n (1−α−δ).                                              (G2-3)

For α=δ=0, p≥n **even with arbitrarily long untrusted witness**. For α=0, soundness δ≥1−p/n. This is not an unconditional cost bound for bit-addressing multi-bit words, cryptographic SNARKs, or protocols with additional authenticated state.

**An exact matching upper construction for α=0.** Store the n raw input bits (w=1, m=n). Prover supplies a **claimed entire n-bit string** π=s and a claimed parity bit a=⊕s_i; any false-parity witness differs from actual x in at least one bit. Verifier checks π parity locally (unpriced CPU but counted in an end-to-end ledger as O(n) work), uniformly samples p distinct positions without replacement and reads/compares those p actual stored bits. It accepts iff every probed bit matches s. Correct π=x is always accepted (α=0). A wrong-parity π differing in t≥1 places passes with probability

    C(n−t,p)/C(n,p) ≤ C(n−1,p)/C(n,p) = 1−p/n.                 (G2-4)

So (G2-3) is **exactly tight** at α=0 for every integer 0≤p≤n, in this frozen private-coin model. The protocol has **b=n bits of prover communication**, O(n) witness read/parity computation, Θ(p) memory bit probes, and prover may require O(n) access to x. Do not misrepresent p as total verification work. The trusted state can be updated by flipping the labeled input index. No cryptographic hash assumptions are used.

This sharp result also shows why a *free arbitrary-length untrusted proof* is not a substitute for sound data access: reducing p to a fixed fraction forces a corresponding nonzero soundness error. Nonetheless the actual annotation bytes here scale linearly in n, so the frontier DOES NOT give a novel optimum for fully charged (b,p,update-time) protocols.

## 5. An adversarial falsifier: two writes permit one probe for single parity

Store M(x)=(x_1,...,x_n, ⊕_i x_i). Every original input toggle flips **two** code coordinates (its raw bit plus the global parity cache). A single full-parity query reads the last bit (p=1), even with perfect exactness and no prover. All sensitive one-step support sets share that final cell: ν*=1, not n. Hence the tempting extrapolation p≥n/w is already FALSE for one parity query when w=2. This counterexample is valid because it serves **one** query; it does not magically answer every prefix parity with one read and two writes. Any resource bound must specify the *entire* joint query suite.

Likewise, an uncharged authenticated root or trusted external memo can store that global parity independently of M, rendering (G2-1) inapplicable. This is a model mismatch, not a counterexample to its proof.

## 6. Remaining genuinely original frontier — still OPEN

G2-A closes a necessary proof/certificate connection; it **does NOT** establish a strong new multi-resource theorem. Next mathematical challenge under [UCT-004 issue #87](https://github.com/definitely-stable/Mathlab/issues/87):

- Choose a *natural* full dynamic prefix-query or authenticated batch-commit task where full update/write accesses, proof publication/generation/maintenance, all verifier computation, memory m, message b, p bits/cells and soundness δ are actually charged.
- Compare an explicitly quantified candidate with **Pătraşcu–Tarniţă 2007** dynamic bit-probe partial sums, **Aaronson 2008** randomized certificate complexity, **Ambainis et al. 2021** fractional adversary equivalence, **Ghosh–Shah 2024** online MA, **Ben-David–Kothari 2026** randomized vs deterministic certificate separation, and **Ko 2026** dynamic Multiphase cell probes.
- Seek a **nonfactorizing inequality** beyond the corresponding known same-model bounds, preferably a family with matching upper construction; otherwise issue a precise STOP and pivot to a different original structural principle. Never assert p≥n for w>1 based on G2-3.
- G2 finite independent checks are in `research/test_uct004_sound_witness.py`; exhaustive tests do not certify asymptotic novelty.

**Status decision:** G2-A DERIVED_CLASSICAL PROVED; universal original G2 theorem OPEN; no release, Rust crate or security claim.
