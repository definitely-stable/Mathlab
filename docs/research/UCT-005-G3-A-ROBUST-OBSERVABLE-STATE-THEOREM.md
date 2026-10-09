# UCT-005 G3-A — Robust Observable-State Reachability Theorem (ROST)

Date: 2026-10-09 · [root UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) · [G3 #164](https://github.com/definitely-stable/Mathlab/issues/164).

**Scientific classification:** PROVED_MODEL_SCOPED_COMPOSITION / ROBUST_SPHERE_PACKING_CLASSICAL / ADAPTIVE_SUPPORT_CLASSICAL / SPARSE_TRADE_TRANSLATION_PROVED / FINITE_ORACLES / ORIGINAL_ASYMPTOTIC_ROOT_OPEN / NO_RUST.

## 0. A real common mathematical object, not a renaming

We seek ONE set of hypotheses and a single strong necessary inequality that has genuinely different, correctly typed consequences for algebraic sparse states, dynamic structures, online graph observations and fault-tolerant answers. The theorem below is self-contained and proved. Its constituent geometric and coding arguments are classical, so **it is NOT a discovery of a globally novel lower bound**. G3-B is tasked with obtaining an additional *nonfactorizing multi-epoch theorem* beyond it.

### Parameter types

- Finite directed **online update graph** \(\mathcal T=(X,E)\). An edge means a legal update; no unpriced information about its label is available to queries.
- Fixed initial state \(x_0\), integer update horizon \(d\), reachable set \(\mathcal R_d(x_0)\) via at most \(d\) allowed updates.
- A representation \(\phi:X\to\Sigma^m\), \(|\Sigma|=q\ge2\), **same** public representation and same fixed \(\phi(x_0)\) for every state. Every allowed edge changes at most \(w\) **remote symbols** in Hamming distance. This is NOT a bound on physical I/O instructions, bytes, updater source reads or crash durability.
- Reliable input-dependent local metadata \(h:X\to\{0,1\}^H\), fixed-width and *fully charged*. The metadata may change between epochs; no hidden trusted roots, cached past or free update log.
- A fixed suite of \(t\ge1\) public, stateless queries \(f_j:X\to Y_j\). Their joint observable signature \(O(x)=(f_1(x),\dots,f_t(x))\) ranges over \(K=|O(\mathcal R_d(x_0))|\) values. Outputs need not be Boolean.
- A deterministic, same-program-per-index query decoder \(\mathcal D_j\) can read \(h(x)\), public code and at most \(p\) **adaptive \(q\)-ary symbol probes** of one remote word \(z\), then must answer \(f_j(x)\) correctly for **every** adversarial \(z\) satisfying \(d_H(z,\phi(x))\le e\). Corruptions occur to **one shared final remote word** and the trusted label is not corrupted. The adversary knows the algorithm and may choose any \(e\) remote symbols. Query indices, code and old labels are not update-dependent side channels; if they are, their state-dependent bits must be charged.
- No computational cryptography, private-coin/Monte Carlo error, Byzantine proof witnesses, input-dependent public look-up table, update-operation payload leaked to a reader, or dynamic reset. These would need separate extensions. Public code/table size, update CPU and setup are unbounded here, not a promised product-level protocol.

Define the \(q\)-ary ball volume

\[
V_q(s,r)=\sum_{i=0}^{\min(s,r)}{s\choose i}(q-1)^i,
\qquad T_q(p)=\sum_{i=0}^{p-1}q^i,\qquad M=\min(m,tT_q(p)).
\]

For \(p=0\), \(T_q(0)=0\); \(V_q(0,r)=1\).

## 1. One major theorem, three interlocking consequences

### Theorem ROST-A: robust reachable-observability and local-probe capacity

For each \(x_0\) and horizon \(d\), every service as above satisfies

\[
\boxed{
K\ \le\ 2^H
\max_{0\le s\le M}
\left\lfloor
\frac{V_q(s,dw+e)}{V_q(s,e)}
\right\rfloor,
\qquad
M=\min\left(m,t\sum_{i=0}^{p-1}q^i\right).
}
\tag{ROST-A}
\]

**Stronger exact packing form.** Put

\[
A_q^{\mathrm{ball}}(s,r,\delta)=
\max\left\{|C|:\ C\subseteq B_q(0,r)\subseteq\Sigma^s,\
d_H(u,v)\ge\delta\ \forall u\ne v\in C\right\}.
\]

Then, without any approximation,

\[
\boxed{
K\le 2^H\max_{0\le s\le M}
A_q^{\mathrm{ball}}\left(s,dw,2e+1\right).
}
\tag{ROST-A*}
\]

Both are **necessary**, not sufficient. They do not imply a polynomial-time encoding or achievable matching code for a dynamic graph.

**Proof (complete, elementary).** Pick one reachable state representing each of the \(K\) different signatures; partition these representatives by trusted label \(\ell=h(x)\). Fix one \(\ell\). The \(t\) query algorithms with fixed \(\ell\) are fixed deterministic \(q\)-ary decision trees, each of depth at most \(p\). The entire tree at each depth \(i\) has at most \(q^i\) probe nodes, hence the **union** \(A_\ell\) of every address any of the \(t\) queries could probe, over **all possible corrupted word values**, has size \(s_\ell\le M\). Crucially \(A_\ell\) depends on the trusted label \(\ell\), **not** on the represented state within this group.

Every reachable \(x\) lies within \(d\) update edges of \(x_0\). Each edge changes at most \(w\) remote symbols, so by triangle inequality \(\phi(x)\) is within Hamming distance \(dw\) of the common baseline \(\phi(x_0)\). Its projection \(c_x=\phi(x)|_{A_\ell}\) is therefore inside the radius-\(dw\) Hamming ball centered at \(\phi(x_0)|_{A_\ell}\).

Take two representatives \(x\ne y\) **with different joint signatures but the same** \(\ell\). Suppose \(d_H(c_x,c_y)\le2e\). There exists a projected word \(z_A\) at Hamming distance \(\le e\) from each projection (partition the mismatching positions into two groups of size at most \(e\); choose \(z_A\)'s symbols from the corresponding endpoint). Form two full remote corruptions by replacing *only* \(A_\ell\)-coordinates of \(\phi(x)\) and of \(\phi(y)\) by the same \(z_A\). Each corruption changes \(\le e\) remote coordinates. Because all query probe addresses lie in \(A_\ell\), all \(t\) decision trees see **identical** probe responses on the two corrupted words and return identical signatures; but the required signatures differ. Contradiction. Thus the projections have pairwise distance at least \(2e+1\).

This is an injective code in the radius-\(dw\) ball, giving \(|C_\ell|\le A_q^{ball}(s_\ell,dw,2e+1)\). Radius-\(e\) spheres centered on \(C_\ell\) are pairwise disjoint and, by triangle inequality, are contained within the radius-\((dw+e)\) ball around the initial projected word. Hence \(|C_\ell|V_q(s_\ell,e)\le V_q(s_\ell,dw+e)\). There are at most \(2^H\) trusted label values. Sum and bound each group by the largest feasible \(s\le M\); obtain ROST-A* and ROST-A. QED.

**Boundary case checks:** \(e=0\) yields the G1-A/G1-B reachable-state Hamming capacity with adaptive query support, not an original theorem. \(p=0\) yields \(K\le2^H\). \(w=0\) yields \(K\le2^H\) irrespective of \(p\). If corruption touches trusted metadata, if the decoders have a state-dependent uncharged oracle, or if corrupted words are not required to be decoded exactly, this theorem may be false. The global input/state domain can contain millions of states with the same signature; use the observable quotient \(K\), not \(|X|\) without proof of injectivity.

**Strict finite strengthening:** set \(q=2,m=M=8,dw=2,e=1,H=0\). The classical no-error reachable-ball bound gives \(K\le V_2(8,2)=37\). Standard unconstrained Hamming packing gives \(K\le\lfloor 2^8/V_2(8,1)\rfloor=28\). **ROST-A gives \(K\le\lfloor V_2(8,3)/V_2(8,1)\rfloor=\lfloor 93/9\rfloor=10\)**. This is strictly stronger for this *same* restricted, exact, robust task; it remains a direct classical sphere-packing argument, not an original scientific novelty claim. Need \(p\) and \(t\) large enough that \(M=8\) for this numerical comparison.

### Theorem ROST-B: sparse additive state/reconstruction = signed near-trade exclusion

Let \(q\) be a prime power, \(A\in\mathbb F_q^{m\times n}\), each column supported in at most \(w\) coordinates. Let \(U_d=\{u\in\{0,1\}^n:|u|_0\le d\}\), where \(0,1\) denote field elements, and let \(\phi(u)=Au\). Assume the observer must reconstruct **the entire** sparse \(u\) exactly after up to \(e\) corrupted output symbols (unrestricted reads, no trusted auxiliary labels). Then such a decoder exists, with unbounded computation, **if and only if**

\[
\boxed{
\operatorname{wt}\big(A(u-v)\big)\ge2e+1
\quad\text{for every distinct }u,v\in U_d.
}
\tag{ROST-B}
\]

Proof: necessity is the same intersecting-radius-\(e\)-balls argument. Sufficiency follows because the radius-\(e\) Hamming balls around the finite codewords \(Au\) are disjoint; define an exact nearest-unique codeword decoder within those balls. Since each \(u\) uses at most \(d\) columns of support at most \(w\), every \(Au\) belongs to the radius-\(dw\) ball. Consequently

\[
\boxed{
\left(\sum_{i=0}^{\min(d,n)}{n\choose i}\right)V_q(m,e)
\le V_q(m,dw+e).
}
\tag{ROST-B-capacity}
\]

This is a **necessary** bound; sparse supports/sign restrictions may impose stricter extremal limits.

For \(e=0\), criterion \(\ker A\cap(U_d-U_d)=\{0\}\) is exactly the signed-trade/no sparse-subset-sum-collision condition underlying LENT-001, HYP-001/002/105 and ASET. For \(e>0\), it forbids **near trades** with a nonzero syndrome of Hamming weight at most \(2e\), a natural extension to robust exact deltas. An arbitrary GF(q) linear combination with coefficient 2 is *not* necessarily a difference of two distinct \(\{0,1\}\)-subsets; preserve the precise signed-difference alphabet and cardinality constraints. Over nonprime finite fields, field arithmetic is not integer arithmetic modulo q.

Countermodels: identity matrix \(A=I_n\) is collision-free for \(e=0\) and all \(d\), but fails even \(e=1\) because unit vectors have distance 1 from zero. Conversely, GF(2), \(m=6,n=2,d=1,w=3\), columns \(111000\), \(000111\), codewords \(\{0,111000,000111\}\) have pairwise distances \(3,3,6\) and permit \(e=1\) correction; finite oracle rechecks both claims. **This does not prove a new exponent for 4-sparse GF(5) ASET or a new code family.**

**Observation quotient:** if the requested output is \(C Au\), not complete \(u\), different sparse states with the same requested output may share an encoding; bound \(K=|\{CAu:u\in U_d\}|\) and distinguish only pairs whose requested outputs differ. This subsumes the information-only part of UCT-005 G2-B2's exact shared broadcast quotient when code/setup assumptions match; it does **not** include untrusted prover soundness or all-client freshness.

### Theorem ROST-C: temporal transport constraint (typed side condition)

For each update edge \(x\to y\) for which \(h(x)=h(y)\), and any query index \(j\) whose correct output changes, let \(R_j(x)\) be the remote addresses actually read by the deterministic query on the **uncorrupted** old word \(\phi(x)\). Let \(W_{x,y}\) be coordinates changed between \(\phi(x)\) and \(\phi(y)\). Then \(R_j(x)\cap W_{x,y}\ne\emptyset\). Proof: if every old-address value is unchanged, the same deterministic adaptive query follows identical branches after the update and cannot change its answer. Thus \(|W_{x,y}|\) is at least the transversal number of \(\{R_j(x):f_j(x)\ne f_j(y)\}\). This is exactly UCT-003's **classical influence lemma**; it is not a new independent component. If trusted \(h\) changes on this edge, the query may learn the new answer from it alone, and the unqualified inequality fails.

ROST-A controls **reachable information capacity under faults and restricted probes**; ROST-B characterizes **additive exact/robust uniqueness via trades**; ROST-C separately controls **how each semantic change is physically transported**. They share a typed state/update/query model. They are not claimed to constitute a new indecomposable lower bound, nor do they account for updater reads, proof maintenance, CPU work, application-level caching or crash recovery.

## 2. Connections across Mathlab — precise rather than rhetorical

| Existing Mathlab research | Relationship to ROST | What is proved or still missing |
| --- | --- | --- |
| UCT-001/002 | DIRECT_SPECIALIZATION, \(e=0\), no separate free read-only oracle; underlying graph update reachability | UCT-002 has a distinct annotation + arbitrary external oracle model, so must align observations before transferring exact constants |
| UCT-003 | DIRECT_CLASSICAL_COMPONENT — ROST-C | Adaptive influence/transversal, not robustness or cryptographic soundness |
| DAG-002/ALG-001 G0/G1-A/G1-B | DIRECT_SPECIALIZATION at \(d=1,e=0\) with fixed-prefix single update; GF(2) rank-one observation | Do NOT call rank computation the same service as recovering all matrix coordinates |
| LENT-001, ML-001/006/007 | DIRECT_ADDITIVE_SPECIALIZATION — ROST-B \(e=0\) when exact sparse subset-sum recovery requested | Finite-field alphabet, sparse update support and true differences must match |
| HYP-001/002/105 and ASET | DIRECT_SPARSE-TRADE-TRANSLATION — ROST-B and forbidden signed differences | Extremal cardinality/exponent for constant \(w\) needs independent new combinatorics |
| UCT-005 G2-B1/B2 | REDUCTION_REQUIRED — parity DAG's linear influence matrix becomes observable quotient \(K\) | Broadcast communication is not remote bit probes, and reader initialization must be priced |
| UCT-004 nonlinear witness covers; HYP-103 | REQUIRES_DISTINCT_PROOF-SOUNDNESS_MODEL — local corruption decoding is not untrusted malicious witness verification | Private coins, proof selection, constant soundness and asymmetric trust remain separate |
| TOM-003 overwrite/trust and INDEX-001 RASK/LSM | REDUCTION_REQUIRED for logical state update and query only | Durable page flushes, interval operations, crash/rollback and GC cannot be inferred from Hamming symbol edits |
| HYP-101 incremental hashing and DAG recomputation | REDUCTION_REQUIRED for Boolean observable outputs and logical state | CPU hashing, collision probability and semantic cancellation not bounded by bit-cell packing alone |
| TOM-005/006 and DELSK delta/base choice | APPLICATION/COST-MODEL_ONLY — every legal exact transformation can be made an update edge | Encoded COPY/ADD wire bytes and optimizer proof costs not consequences of ROST-A |
| DeltaMeter/GF(2)-F-PCSA | DIRECT_ADDITIVE_OBSERVABLE_SPECIALIZATION only for exact linear parity snapshots | Approximate F2 estimation, randomized reliability and system benchmark outside error-free deterministic model |
| Dynamic graphs/online algorithms, caching | REDUCTION_REQUIRED; finite state/update/query graph is shared formal language | Competitive ratios, Markov workloads, randomized policies and edge/graph-specific lower bounds need extra hypotheses |
| Imported openai/math manuscripts and OM records | EXTERNAL_EVIDENCE_ONLY until a concrete assumption-preserving reduction | No implication from presence in same bibliography |
| Cryptographic vector commitments / memory checking / UCT-005 root | ROBUST_CORRUPTION_IS_NOT_CRYPTOGRAPHIC_SECURITY | Byzantine proof, rollback freshness, computational soundness, update witnesses, trusted state and codebook must be priced |
| INDEX-001 range crash oracle | COUNTERMODEL against treating remote-symbol Hamming delta as physical write/recovery cost | WAL, fsync, page writes and recovery cost are distinct units |

**Summary of coverage:** ROST is a precise common *mathematical trunk* for several independently proven families and a usable connector to many others, NOT a theorem whose conclusion logically implies every one of the repository's 61 registry records (many are empirical studies, protocol audits or unrelated external mathematics). Preserve separate parent/child theorem authorities.

## 3. Falsification and novelty gates

### G3-A: independently test the proved classical composition

- Exhaustively enumerate binary/q-ary small codewords in radius-\(r\) balls, compare separately implemented max distance-\(2e+1\) packing and the sphere-volume ratio; test \(q=2,3\), \(m\le4\) (bounded).
- Test structural support for deterministic adaptive query trees of depth \(p=0,1,2\), including early stops, duplicated addresses and multiple queries. The size bound uses all **potential** branches, not just observed probe trace.
- Enumerate GF(2), GF(3), GF(5) sparse subset-sum families for small matrices; compare direct independent exact-decode-vs-near-trade condition and corruption balls. Include the identity-vs-repetition cases.
- Demonstrate \(K\le10\) finite example from classical joint local packing vs 37 without error and 28 ordinary global Hamming. Explicitly note this bound can be loose vs exact feasible dynamic storage codes.
- Out-of-model controls: remote memory corruption with untrusted local root; probabilistic bounded-error decoders; uncharged source-array probes; query algorithm depending on update payload; physical disk and malicious proof. **Do not silently count these as success cases.**

### G3-B: actual potentially original central theorem (OPEN)

The full UCT-005 root needs a natural family \(\mathcal T_n\), an explicit online service and **same-model strict separation** stronger than *both* ROST and the best applicable LULDC, memory-checking, dynamic cell-probe, authenticated data-structure, locally-decodable-code and coding-theory bounds. Extend to a common task with:
\[
(S_{\rm trusted},S_{\rm remote},U_{\rm read},U_{\rm write},Q_{\rm probe},
B_{\rm proof},C_{\rm communication},T_{\rm program},V_{\rm verifier},
\epsilon,\lambda,\text{horizon}).
\]
Focus on genuine multi-epoch transitions with preserved proof freshness and adversarial observers. Establish a **nonfactorizing inequality** with a strict asymptotic advantage over an explicitly audited same-model baseline, or **STOP_NOVELTY**. The general G3-A estimate is a robust information-theory bridge, but not a new foundational scientific impossibility theorem. No \(\mathrm{GF}(5)\) exponent improvement, Rust crate or product claim follows automatically.

## 4. Original source anchors / prior art

- UCT-002, UCT-003, G1-B and UCT-005: [Mathlab audited prior papers](UCT-005-ROOT-THEOREM-PROGRAM.md).
- [Standard coding-theory Hamming sphere packing](https://doc.sagemath.org/html/en/reference/coding/sage/coding/code_bounds.html) and [S. Johnson (1972), constant-weight code bounds](https://doi.org/10.1016/0012-365X(72)90027-1) mean that ROST-A's ball packing is **classical**.
- [Chandran–Kanukurthi–Ostrovsky, locally updatable and locally decodable codes, TCC 2014](https://www.microsoft.com/en-us/research/publication/locally-updatable-and-locally-decodable-codes/) directly couples update and read locality under its precise Prefix Hamming corruption model. Not necessarily identical to our worst-case fixed remote e-symbol corruption model.
- [Fredman–Saks, 1989](https://doi.org/10.1145/73007.73040), [Pătraşcu–Demaine, 2006](https://doi.org/10.1137/S0097539705447256) and [Ko, 2026 Boolean Multiphase](https://eccc.weizmann.ac.il/report/2026/047/) already deliver strong dynamic lower bounds for typed tasks, not automatically ROST's general input family.
- [Blum–Evans–Gemmell–Kannan–Naor memory checking](https://doi.org/10.1109/SFCS.1991.185352), [Boyle–Komargodski–Vafa 2024](https://doi.org/10.1145/3618260.3649686), [Tas–Boneh efficient VC updates AFT 2023](https://doi.org/10.4230/LIPIcs.AFT.2023.29): security-specific obstacles cannot be replaced by q-ary sphere packing.
- All source claims are publisher/author model-level anchors; original published proofs not independently reproduced here.

**No newly numbered LIT entries:** #147, #154 and concurrent #132/index imports retain authority for canonical primary-source promotions; adding overlapping identities in this proof PR would threaten provenance.
