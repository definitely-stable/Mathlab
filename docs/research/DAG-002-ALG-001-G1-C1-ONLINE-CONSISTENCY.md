# DAG-002 × ALG-001 G1-C1 — same-code online transition consistency

**Issue:** [#161](https://github.com/definitely-stable/Mathlab/issues/161), parent [#140](https://github.com/definitely-stable/Mathlab/issues/140), predecessor [G1-B PR #159](https://github.com/definitely-stable/Mathlab/pull/159).
**Scientific status:** DERIVED_CLASSICAL_SAFETY_GAME / STRICT_ONE_SHOT_VS_ONLINE_COUNTERMODEL / NOVELTY_UNPROVED / NO_UCT_ROOT_TRANSFER.
**Scope:** deterministic GF(2) delta updates, fixed exact read-only decoder, binary logical overwrite cells; no encryption, authentication, probability, production DAG claim or durable I/O. Research only.

## 1. Explicit typed model

A fixed public decoder f maps N binary remote cells to n logical output bits. A legal update DELTA(d) from a fixed alphabet D asks the updater to reach a remote word z' with f(z')=f(z) XOR d. Full update-command history, epochs, changing local labels and caches are NOT supplied free to queries or future updates. H=0. Remote cells use ordinary overwrite, NOT atomic XOR/toggle. The fixed codebook, program tables and preprocessing T are not charged in this toy oracle, prohibiting efficiency or general lower-bound claims.

Resource ledger: n output bits, N binary remote cells, W_net changed final cells, W_phys physical overwrite calls (even no-change writes), R_u updater READ operations, P_q query READ operations per output bit, H mutable local bits, T fixed program/codebook bits. W_net <= W_phys. No physical page bytes, address lengths, authenticated proofs, crash recovery or free clock are inferred.

Two intentionally distinct models:

* **C1-a full-read:** updater reads all N cells (R_u<=N suffices) and may choose ANY correct next physical state at Hamming distance <=W_net. Potentially exponential transition-program ROM. Query may read all N cells (P_q<=N).
* **C1-b uniform bounded-read:** one fixed stateless program for EACH delta, same at every epoch, with R_u=0 or 1 read of a fixed bit address; its two possible branches perform no-op or at most one constant-bit overwrite. W_phys<=1 and W_net<=1; N<=3 in the enumerator. The per-command program must work UNIFORMLY over all states of an invariant set, not be chosen afresh based on an uncharged old remote word.

A TARGET(t) update, arbitrary-edge DAG update, append-sink-parent-row, coordinate membership query and matrix rank query are DIFFERENT operation families. Do not silently reuse proofs between them.

## 2. G1-C1-L1: greatest safe fixed point (DERIVED CLASSICAL)

For S={0,1}^N, let

~~~text
F(X) = { z in X: for every d in D there exists z' in X
                  with hd(z,z')<=W and f(z')=f(z) XOR d }.
X_0=S; X_(t+1)=F(X_t); X_inf=intersection_t X_t.
~~~

**Restricted exact lemma.** In the *full-read* model C1-a, there exists a deterministic controller that answers every adversarial finite delta history correctly from z if and only if z belongs to X_inf. Each strict iteration removes >=1 physical state, so stabilization occurs within <=2^N strict rounds. If z survives, select one successor in X_inf for each (z,d), giving a memoryless correct controller. If removed at rank t, the adversary can force failure within <=t steps by induction on removal rank. This is the standard safety-game greatest-fixed-point/positional-strategy principle, NOT an original theorem.

The module implements bottom-up fixed-point deletion. Its independent test reference is a top-down AND-OR game with an unrelated XOR-mask successor enumeration, exhaustively matching all one-bit decoder tables for N<=3, all two-bit decoder tables for N<=2, all W and two delta-alphabet variants. An online winning depth of 2^N coincides with the infinite-horizon kernel.

## 3. G1-C1-F1: one-step capacity is NOT online consistency

Choose n=2, N=3, W_net=1, H=0; binary states are low-bit-first. Define nonlinear decoder:

~~~text
z:  000 001 010 011 100 101 110 111
f:   00  01  10  00  11  00  00  00
D = {00,01,10,11}; initial z=000.
~~~

The four successors z={000,001,010,100} differ by <=1 bit from 000 and realize **all 4 outputs** in one update. Query P_q=3 is sufficient by reading all remote cells. G1-B fixed-history bound is saturated: M=min(3,2*(1+2+4))=3 and V_1(3,1)=1+3=4, so K=4 satisfies K<=2^H*V.

However, after DELTA(11), the only correct successor from 000 is 100 (label 11). Its radius-1 successors {100,000,101,110} have labels {11,00,00,00}. DELTA(01) next requires label 10, impossible. The full-alphabet infinite kernel is empty. If D is restricted to {00,01}, 000 becomes viable. This is a **decoder-specific strict separation**, not a stronger universal parameter inequality: the classical syndrome below works indefinitely with the SAME n,N,W,H. G1-B cannot simply be upgraded to a new asymptotic theorem without structural conditions.

## 4. G1-C1-L2: no-read stateless overwrite is idempotent

For a fixed delta d, an R_u=0 deterministic stateless updater restricted to fixed-address, fixed-value overwrites implements a state map U_d satisfying U_d(U_d(z))=U_d(z). The number of overwrite addresses does not matter provided all assigned values are fixed and the program sees no evolving state. For any legal nonzero GF(2) delta d that may repeat twice, correctness demands f(U_d(z))=f(z) XOR d and f(U_d(U_d(z)))=f(z) XOR d XOR d=f(z). Idempotence makes both physical successor words identical, a contradiction.

Thus R_u>=1 is necessary **only for this stateless blind constant-overwrite primitive**, not for hardware XOR writes, mutable H>0, changing epochs in the code, unpriced side channels or a different update source model. This elementary observation is not publication-novel.

**Exact matching construction:** classical Hamming parity-check columns 01,10,11, N=3. Decoder f(z) XOR-sums present columns. Each nonzero DELTA(d) reads the cell indexed by d, overwrites its complement: R_u=1, W_phys=1, W_net=1. Delta zero does nothing. Every state and every history works. Each coordinate query reads exactly P_q=2 cells; H=0. The independent uniform-program enumeration finds and checks a *single common program per delta* on the entire 8-state invariant. Blind R=0 programs have no such invariant from initial 0. All 4^4 delta sequences and a separate column-parity oracle are checked.

No original code construction is claimed: this control reuses the accepted G1-B syndrome, now with explicit read/write program enumeration.

## 5. Source-to-model barriers (not full independent proof audit)

| Primary work | Verified source-level fact / restriction | Verdict |
| --- | --- | --- |
| [Chandran–Kanukurthi–Ostrovsky, TCC 2014](https://doi.org/10.1007/978-3-642-54242-8_21) | Locally updatable/decodable codes and Prefix Hamming adversarial error model, publisher/author abstract checked | SOURCE_REQUIRES_THEOREM_LEVEL_AUDIT; cannot infer our exact no-error R_u/W_phys bound |
| [Ko, ECCC TR25-156](https://eccc.weizmann.ac.il/report/2025/156/) | One-way communication translation to hard dynamic cell-probe problems under stated distribution/model | NONTRANSFER_UNLESS_REDUCTION to these finite coordinate outputs |
| [Ko, ECCC TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) | Boolean Multiphase and 2.5-round verification; ECCC abstract checked | NONTRANSFER_UNLESS_REDUCTION to general DAG/crypto freshness |
| [Classical safety-game positional strategies](https://link.springer.com/article/10.1007/s00236-020-00374-7) | Known greatest-fixed-point winning-region construction | DERIVED_CLASSICAL; exactly the finite game of L1 |
| [Mathlab G1-B PR #159](https://github.com/definitely-stable/Mathlab/pull/159) | Merged per-history bound and classical syndrome construction | STRICT_DECODER_SPECIFIC_SEPARATION only |
| [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223) | Authentication, epoch freshness, PIN/GC and paid bytes use a DIFFERENT model | REDUCTION_REQUIRED; no root theorem promotion |

This is a deliberately narrow source audit. Full original-paper theorem/hypothesis checks (including TCC 2014, Ko 2025/26, FOCS 2023 dynamic graph) remain open in #161. Canonical LIT imports belong to #147 and are not modified.

## 6. Executable acceptance and next slice

~~~bash
python research/dag002_g1c_online.py
python -m unittest discover -s research -p 'test_dag002_g1c_online.py' -v
~~~

Typed markers: DAG_G1C_ONLINE_ONE_SHOT_COUNTEREXAMPLE_PASS; DAG_G1C_ONLINE_FIXEDPOINT_PASS; DAG_G1C_R0_OVERWRITE_NO_GO_PASS; DAG_G1C_R1_SYNDROME_WITNESS_PASS; NOVELTY_UNPROVED_CLASSICAL_FIXEDPOINT.

Tests are discovered by the preexisting full hosted Research CI; a separate focused hosted workflow runs these exact tests. G1-C1 establishes only a **classical fixed-point criterion, falsified inference, and a matched restricted read-cost observation**. This is NOT an issue #161 acceptance or a root theorem.

**Next G1-C2:** freeze explicitly priced fixed codebook T, arbitrary adaptive updater reads R_u, mutable trusted H, net vs physical writes, query P, and update alphabets with DAG semantics. Attempt a truly joint nonfactorizing theorem only after full primary-source novelty closure. If impossible, record source-backed STOP_THEOREM_NOVELTY and develop the useful C3 algorithmic baseline. No Rust, no cross-repository writes, no auto-merge.
