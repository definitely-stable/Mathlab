# UCT-005 G3-B1 — Multi-epoch trajectory packing, complete restricted proof and novelty STOP

**Date:** 2026-10-09 · [UCT-005 root #105](https://github.com/definitely-stable/Mathlab/issues/105) · [G3 #164](https://github.com/definitely-stable/Mathlab/issues/164) · [this slice #175](https://github.com/definitely-stable/Mathlab/issues/175).

**Scientific status:** `RESTRICTED_CLASSICAL_TEMPORAL_PACKING_PROVED / INDEPENDENT_FINITE_ORACLES / STRICT_FINITE_COMPARISON / NO_NEW_ASYMPTOTIC_LOWER_BOUND / CRYPTO_AND_PHYSICAL_UPDATE_PROBES_NOT_PROVED / ROOT_OPEN_UNPROVED`. This result strengthens some deliberately separate application of G3-A's individual-epoch sphere volumes, but is not claimed to be a novel cryptographic memory-checking or cell-probe lower bound. Every resource symbol is scoped.

## 1. Frozen trajectory task and what is actually charged

Fix a q-ary alphabet \(\Sigma\) of size \(q\ge2\), a shared *public*, *input-independent* initial state \(x_0\), and a time-invariant encoding \(\phi:X\to\Sigma^m\). A valid path of **exactly \(d\ge1\) updates** is \(x_0\to x_1\to\cdots\to x_d\). Each edge satisfies

\[
d_H(\phi(x_{j-1}),\phi(x_j))\le w,\qquad j=1,\ldots,d.
\]

Each endpoint \(j\ge1\) has reliable charged local label \(h_j(x_j)\in\{0,1\}^H\), which **may change at every epoch**; the fixed, public epoch index \(j\) may be input to the decoder, but unpriced update coordinates, transcript buffers, client state, precomputed history-dependent codebooks or unrevealed side channels may not. The same frozen code/program, remote address space and public queries apply to all paths. A decoder starts with only \(j,h_j,\) and the ability to read the **current** remote word (no stored old probes). There are \(t\ge1\) public deterministic query programs \(D_{j,a}\), \(a\in[t]\); each issues at most \(p\ge0\) *adaptive* q-ary remote probes. Decoder programs can depend on \(j\) but not on a private path. The joint desired observable at epoch \(j\) is \(O_j(x_j)=(f_{j,1}(x_j),\ldots,f_{j,t}(x_j))\).

**Robustness:** at each epoch, for **every** remote word \(z_j\) with \(d_H(z_j,\phi(x_j))\le e\), the decoders return the exact \(O_j(x_j)\) using only current \(h_j\). Corruptions are freshly and independently selected on each epoch; no persistence across time is needed for the conclusion. Trusted \(h_j\) is never corrupted, and there is no computational soundness, hash, proof oracle, server signature, multi-reader fork, authenticated update receipt, freshness guarantee or stochastic decoder error. If an operation changes a physical word several times and then restores it, it counts as **more physical writes** even though the theorem only bounds the *net* Hamming distance. Update source reads, setup and prover CPU are **not** bounded by the theorem.

Let \(K_{\rm traj}\) be the number of **distinct observable histories**
\[
(O_1(x_1),\ldots,O_d(x_d))
\]
over all legal paths from the **same** \(x_0\). Do not replace \(K_{\rm traj}\) by the number of labelled paths when different paths have the same observable history. A decoder need not reconstruct the path or past state.

Define ball volumes and total address budget
\[
V_q(s,r)=\sum_{a=0}^{\min(s,r)}\binom sa(q-1)^a,\quad
T_q(p)=\sum_{i=0}^{p-1}q^i,\quad
M=\min(m,dtT_q(p)).
\]
If \(p=0\), \(T_q(p)=0\). Labels cost \(H d\) **bits per full trajectory** even if only \(H\) bits exist at any one instant; counting all length-\(d\) label histories is conservative and allows local persistent evolution. A one-shot per-epoch bound alone does not charge this additional temporal information.

## 2. Theorem G3B1-T1: combined walk/tube bound

For the exactly specified deterministic and information-theoretic task above,

\[
\boxed{
K_{\rm traj}\le 2^{Hd}\!
\max_{0\le s\le M}\min\left\{
V_q(s,w)^d,\quad
\left\lfloor
\frac{V_q(s,w+e)V_q(s,w+2e)^{d-1}}
     {V_q(s,e)^d}
\right\rfloor
\right\}.
}
\tag{G3B1-T1}
\]

This is a **necessary information bound**, not a construction, not a general cryptographic theorem and not a full G3-B root proof.

**Self-contained proof.**

1. Select one valid update path for each different observable trajectory (there are \(K_{\rm traj}\)). Partition paths by the entire vector of trusted epoch labels \((h_1,\ldots,h_d)\). At most \(2^{Hd}\) groups exist. Fix one group \(\ell\); the decoders for every \(j,a\) now have their label and epoch inputs fixed and are a collection of \(dt\) deterministic q-ary decision trees, each of depth at most \(p\). Their **union over all possible probe-answer branches**, including those reachable only on corrupted memories, is a fixed remote address set \(A_\ell\) of size \(s\le\min(m,dtT_q(p))=M\). This set is independent of the remaining private update path. It is invalid to bound it by the addresses probed on one good transcript.
2. Project every remote word \(\phi(x_j)\) onto \(A_\ell\), writing \(y_j\in\Sigma^s\). The projected initial word \(y_0\) is common for the group because \(x_0\) was fixed. Each projection transition changes at most \(w\) coordinates; therefore at most \(V_q(s,w)\) choices exist for each \(y_j\) conditioned on \(y_{j-1}\). Distinct observable trajectories in a fixed label group cannot have *identical* projected word sequences: the same deterministic decoders would output the same trajectory. Hence the group's trajectory count is at most \(V_q(s,w)^d\).
3. For each projected sequence \(y=(y_1,\ldots,y_d)\), define its **fresh-corruption tube** \(\mathcal B_e(y)=\{(z_1,\ldots,z_d):d_H(z_j,y_j)\le e\ \forall j\}\). This contains exactly \(V_q(s,e)^d\) tuples. Every projected corruption \(z_j\) can be realized by changing only addresses in \(A_\ell\) of the full word, so the originally assumed global \(e\)-symbol guarantee applies. Tubes of two paths with *different observable trajectories* are disjoint: if a tuple lay in their intersection, every epoch's same deterministic decoders, same label and same corrupted answers would output identical \(O_j\), contradicting a differing observable epoch. **No claim** that disjoint tubes are sufficient for a valid per-epoch query service.
4. Every \((z_1,\ldots,z_d)\in\mathcal B_e(y)\) obeys \(d_H(z_1,y_0)\le w+e\) and \(d_H(z_j,z_{j-1})\le w+2e\) for \(j\ge2\), by the Hamming triangle inequality. Thus all tubes of every group fit inside at most
\[
V_q(s,w+e)V_q(s,w+2e)^{d-1}
\]
q-ary corrupted trajectories. Since the group tubes are disjoint, its count times \(V_q(s,e)^d\) cannot exceed this container. Round down the ratio.
5. Intersect the two necessary bounds per group, maximize over every possible \(s\in[0,M]\), and sum at most \(2^{Hd}\) groups. QED.

**Correct boundary reductions:** \(d=1\) reduces to the single-epoch radius-\(w\) G3-A Hamming-volume capacity for the same models and includes an optional walk-cardinality minimum. \(e=0\) gives the exact remote walk-count bound \(2^{Hd}\max_{s\le M}V_q(s,w)^d\); with full coordinate reads (\(t=s,p=1\)), no trusted labels and all transitions of radius \(w\) permitted, it is achieved by representing the current remote word itself. \(p=0\) yields \(M=0\), hence \(K_{\rm traj}\le 2^{Hd}\); \(w=0\) likewise gives no state-dependent remote history. This establishes a proof **brick**, not originality relative to classical time-expanded Hamming sphere packing.

### Exact integer example — joint bound versus separate G3-A epochs

Take binary \(q=2\), \(m=6\), \(t=6\), \(p=1\) (read six named coordinates), \(d=3\), \(w=1\), \(e=1\), \(H=0\). Hence \(M=6\), and \(V_2(6,1)=7\), \(V_2(6,2)=22\), \(V_2(6,3)=42\), \(V_2(6,4)=57\).

| Distinct observed histories, same parameters | Necessary upper bound |
|---|---:|
| All remote walks, ignoring error correction | \(7^3=343\) |
| Independent per-epoch G3-A volume bounds \( \lfloor22/7\rfloor\lfloor42/7\rfloor\lfloor57/7\rfloor\) | \(3\cdot6\cdot8=144\) |
| **G3B1-T1 time-coupled corrupted tubes** | \(\lfloor22\cdot42^2/7^3\rfloor=\mathbf{113}\) |

Thus \(113<144<343\), a concrete strict gain over *those* two baselines in one frozen model, NOT a demonstrated new asymptotic lower bound, not an optimal number of feasible output trajectories, and not proof that \(K_{\rm traj}=113\) is achievable. Applying stronger classical temporal coding bounds could improve it.

## 3. Three important same-task upper points and adversarial falsifiers

| Identical single-current-state FLIP/READ input task | Trusted information and setup | Remote update / query | Correctness model |
|---|---|---|---|
| Direct \(n\) source-bit array | \(O(1)\) trusted bits, fixed program; \(n\) remote bits; fixed zero genesis | 1 remote bit read+write per FLIP, READ coordinate 1 remote bit read | exact **honest, e=0** only; **not authenticated** |
| Client mirrors \(n\) input bits | \(n\) trusted bits and paid receipt of every authorized flip; remote state optional | client flips local bit, READ 0 remote probes, 0 proof bits | trusted writer/reader **only**, not independent third party; full \(S_{\rm trusted}\) must be charged |
| Fixed-shape authenticated tree / incremental verifiable stateful circuit | trusted root+version; remote hash/digest metadata and \(O(n)\) setup work | typical hash paths and nonzero receipt/proof+verifier work; shape/assumptions-dependent | **conditional computational** binding/soundness, not exact correction of all \(e\) remote faults |

Counterexamples to careless conclusions: old root replay after offline client reconnect is **not prevented by G3B1-T1**; a malicious updater choosing a spurious new root is not secured by collision resistance alone; a q-ary label sequence that tells all answers is charged \(Hd\) bits; direct source-bit read is not e-corruption-robust; lazy recomputation and transcript-dependent public code invalidate assumptions if not charged. The finite oracle is deliberately **not** a SHA-256 or adversarial proof verifier.

## 4. Primary-source novelty and hypothesis transfer matrix

Sources are canonical where already indexed; one new 2026 work has an exact typed source record in [G3-B1 sources](UCT-005-G3-B1-SOURCES.json), awaiting conflict-safe LIT promotion under [#142](https://github.com/definitely-stable/Mathlab/issues/142).

| Actual published work | What can be imported | What CANNOT be concluded |
|---|---|---|
| **LIT-127**, Chandran–Kanukurthi–Ostrovsky, TCC 2014, [DOI](https://doi.org/10.1007/978-3-642-54242-8_21) | Locally updatable/decodable codes and efficient dynamic proofs of retrievability | Their **Prefix Hamming** corruption is not arbitrary independent \(e\) global symbol corruptions; no invented new generic joint updatability barrier |
| **LIT-118**, Deshpande et al., RSA 2005, [DOI](https://doi.org/10.1002/rsa.20069) | Adaptive decoder lower bounds for classical LDCs | Different error probability/codeword model from G3-B1; not the temporal bound verbatim |
| **LIT-133**, leakage-resilient locally decodable/updatable non-malleable codes, I&C 2019, [DOI](https://doi.org/10.1016/j.ic.2019.05.001) | Joint dynamic locality and tamper resistance already extensively studied | Non-malleability/security notion not replaced by tube packing |
| **LIT-157**, Boyle–Komargodski–Vafa STOC 2024 and **LIT-158** covert 2025 | Strong checker local-state versus remote-probe bounds under their exact assumptions | This proof says nothing about malicious accepted proofs or trusted-state freshness |
| **LIT-072**, [STOC 2026 natural-proofs paper](https://doi.org/10.1145/3798129.3800843) | Methodological challenge to broad dynamic lower-bound routes | Conditional barrier is NOT an impossibility of all stronger bounds |
| **G3B1-SRC-01**, Reinhart–Blass–Annighoefer, **Journal of Information Security and Applications 99 (2026)**, [DOI 10.1016/j.jisa.2026.104444](https://doi.org/10.1016/j.jisa.2026.104444) | Journal-publication prior art for *authenticated inputs plus state consistency across multiple iterations* with ADSC-SNARK; 2025 [IACR ePrint 2025/404](https://eprint.iacr.org/2025/404) is **the same underlying paper family**, not a second canonical study | The source is an upper construction, **not** a lower bound or a complete solution to untrusted multi-reader fork/rollback/physical-I/O accounting. Primary journal abstract and institutional publication metadata checked, not independently reproduced formal proofs |

Also relevant: Ko's 2026 Boolean Multiphase cell-probe result (already LIT-119), authenticated ADS G2-B source inventory, G2-B2 proof-bearing broadcast literature, and [G3-A ROST](UCT-005-G3-A-ROBUST-OBSERVABLE-STATE-THEOREM.md). **STOP novelty** for headings like “first unified dynamic update-read-error limit”, “first stateful authenticated computations”, or “new asymptotic lower bound proved.” G3-B1 is classical, restricted proof engineering and model cleanup.

## 5. What is STILL missing for an original nonfactorizing G3-B theorem

A true UCT-005 result still must price together, on the **same natural online service** and **for every epoch**, both physical update reads and writes, query/proof probes, trusted durable state, verifier hash/arithmetic, entire two-way message traffic, crash/fork/replay soundness (under explicit computational or information-theoretic assumptions), public program size and long adaptive horizon.

**Explicit unproved task G3-B2 (not yet conjecture):** choose one dynamic authenticated graph/range aggregation with user-authorized updates and independent subscribers; fix a single writer, shared globally monotonic public epoch service or a fully charged substitute, and bounded local trusted bits for offline verifiers. Compare (i) full replicated trusted state, (ii) local-source/Merkle authentication, (iii) state-consistent succinct proofs (including ADSC-SNARK/UpBARG where its setup assumptions match). Measure a *nonfactorizing* joint frontier strictly outside the known same-model achievable and established lower-bound regions. Define the candidate inequality **only after** finding such a feasible separation. If no such candidate survives, STOP_NOVELTY for the broad UCT-005 root; it is not rescued by repackaging classical ROST/G3B1 packing.

**Evidence:** [computation module](../../research/uct005_g3b1_trajectory.py) and [independent tests](../../research/test_uct005_g3b1_trajectory.py) check exact q-ary ball counts, all small paths, exhaustive e-corruption tubes, independent maximum disjoint families, adaptive support, no-probe/no-write boundary, sharp e=0 walk construction, and the explicit 113-versus-144 numerical separation. This does not prove any unbounded general theorem *by testing*; the five-step argument above supplies the proof. CI is required to validate these files.

**Source audit provenance:** Prior-source claims use publisher or author metadata and abstracts, not line-by-line independent reproductions of the papers' full proofs. The new journal source has [institutional bibliographic confirmation](https://www.ils.uni-stuttgart.de/en/research/publications/). Canonical LIT IDs are **not** assigned while PR #132 controls reserved LIT-205; never overwrite it.
