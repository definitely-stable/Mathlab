# UCT-005 D1-B1 — primary theorem-scope transfer firewall (partial audit)

**Date:** 2026-10-10. Parent: [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223), [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105). Predecessor [D1-B0 F1 model](UCT-005-G3-B2-D1B0-F1-COST-AND-PIN-FREEZE.md).

**Classification:** CANONICAL_20_WORKS_AUDITED_BY_EVIDENCE_LEVEL / THREE_PRIMARY_THEOREM_STATEMENTS_READ / REPRODUCIBLE_GF2_QUERY_INTERFACE_BARRIER / NO_FULL_PROOFS_REDERIVED / NO_NONFACTORIZING_LOWER_BOUND / UCT005_ROOT_OPEN_UNPROVED.

This stage records a *strict source-to-task applicability filter*, not a paper-proof reproduction or a theorem for Byzantine F1. [Machine-readable matrix](UCT-005-G3-B2-D1B1-TRANSFER-MATRIX.json) records 20 canonical source IDs, immutable identity, primary link, inspected evidence level, exact missing reduction, and applicability class. [Validation and finite oracle](../../research/uct005_d1b1_source_gate.py) plus [independent tests](../../research/test_uct005_d1b1_source_gate.py) reject accidental rename/duplicate ID, source promotion, and unsupported direct dynamic transfers. Canonical bibliography remains untouched.

## 1. Four text-level barriers inspected beyond publication abstracts

**LIT-112 Pătraşcu–Demaine (2006).** Read [full author PDF §2.1, Theorems 2.1 and 2.2](https://people.csail.mit.edu/mip/papers/loglb/loglb.pdf). Theorem 2.1 derives tradeoffs for partial sums with update delta bit-size at least proportional to cell word-size `b`; this is **not** justified for one-bit `SET(i,b)`. Theorem 2.2 accounts for `delta=o(b)` for integer partial sums with explicit `log(b/delta)` term. In §3.1 the authors explicitly cite Fredman–Saks for the older **GF(2)** case, which is the relevant classical special case. Do not quote the strong Theorem 2.1 as an authenticated binary F1 cost bound, or multiply it by a separate independent crypto bound.

**LIT-119 Ko (ECCC TR26-047, revised 7 October 2026).** Read [revised original, Theorem 1.1, §3, and footnote on p.2](https://eccc.weizmann.ac.il/report/2026/047/revision/1/download). Theorem 1.1 lower-bounds a **Multiphase** data structure for arbitrary GF(2) inner product under `m=n^(1+Omega(1))` and a subpolynomial update-time assumption. The text explicitly states the improved bound for *range parity itself* remains open. Do **not** equate the Multiphase's arbitrary query family with contiguous 1D intervals, and do not turn `t_tot` into physical page writes or communication without reduction. This is a high-priority hard-adaptive-query tool, not a direct F1 theorem.

**LIT-159 Tas–Boneh (AFT 2023).** Read [proceedings PDF §§3,6, Definition 4, Theorem 5 and Remark 6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol282-aft2023/LIPIcs.AFT.2023.29/LIPIcs.AFT.2023.29.pdf). Theorem 5 assumes a **proof-binding dynamic VC** with a security event and proof-update complexity `g2(k)=O(k^(1-nu))`, and concludes a lower bound on global update information `g1(k)=Omega(k^nu)`; the security-error dependence is material. It is not a theorem about *bytes of GC page movement* or the number of immutable PIN versions. The paper explicitly excludes publicly available updated positions/diffs from its auxiliary update-information metric, whereas F1 charges writer updates and reader catch-up. Claim transfer only after these cost categories are reconciled.

**LIT-359 Guruswami–Lyu–Yuan (arXiv:2507.22265).** Inspected [original full-text HTML](https://arxiv.org/html/2507.22265v1) and stated static data-structure / `NC0` / semi-random-CSP scope. No dynamic `SET`, anchor freshness, history retention, or page GC statement. Record **METHOD_ONLY**, never `APPLICABLE`.

LIT-354 DSST [author-hosted original](https://www.cs.cmu.edu/~sleator/papers/making-data-structures-persistent.pdf) was checked for the persistence scope; efficient versioned node representation is an **upper comparator** and does not imply an authenticated/durable page GC theorem. Other sources are presently **abstract- or bibliography-level only** in the matrix; their main proof quantifiers are NOT certified. In particular LIT-111, 156–158, 199–200, 349–353, 355–356, 358, 068 need detailed theorem-level review before use as proof premises.

## 2. An exact, independently falsifiable interface obstacle

An arbitrary GF(2) inner product with one n-bit state is a parity query `<m,x>` with any mask `m in {0,1}^n`. A single nonempty contiguous `RANGE_PARITY(l,r)` on the **same coordinates** supports only `n(n+1)/2` different nonzero masks, whereas the general inner product supports `2^n-1`. For n>=3 the latter is strictly larger.

More strongly, under an explicit restriction to XOR of `k` ordinary contiguous range-query answers without reencoding state or changing dimensions, the **exact minimum k** equals the number `runs(m)` of maximal consecutive 1-blocks in the mask. Proof: extend the mask by zero at both ends; it has precisely `2 runs(m)` boundary transitions. XOR of k interval masks introduces at most 2k boundary transitions, so k>=runs(m). Query each maximal 1-block to attain equality. An alternating mask needs `ceil(n/2)` intervals. This demonstrates why the naive constant-cost query-identity reduction of an arbitrary matrix row or Multiphase inner product to one interval is invalid.

This interface observation is classical and **is not a lower bound on general reductions**: a reduction may change the dimension, preprocess and encode the state, use extra trusted information, batch queries, alter the operation sequence or consume other priced resources. The finite oracle exhaustively tests masks n<=9, independent boundary counts and all state/query answers n<=6.

## 3. Source transfer and proof acceptance rules

- A source classified `REDUCTION_REQUIRED` has *no theorem transfer to F1 yet*, even if it has a strong theorem for its own service.
- `CLASSICAL_SUBTASK_ONLY` means a restricted parity workload embeds as a query subtask; it does not eliminate a charged anchor, trusted reader state, proof bytes or page-size scaling.
- `CONDITIONAL_UPPER` is a potential Pareto comparator; **not** a lower bound or same-task implementation until all operations and resources have been mapped.
- `SECURITY_NONTRANSFER` indicates fork/covert/BFT semantics require a trust reduction before being substituted for independently anchored global LATEST. `METHOD_ONLY` permits technique research but no direct inequality.
- All assertions of `APPLICABLE` must carry a numbered theorem, all quantifiers, reduction proof, update/query alphabet conversion, word/page cost mapping, treatment of randomization and setup, complete trusted memory and anchor/PIN costs. No such full F1 transfer is established yet.

## 4. Next stage with mandatory falsification order

**D1-B1 continuation:** read primary *proof* statements of LIT-111, 156–158, 199–200, 352–353, 358, and expand the matrix to proof-level conditions. The present work is accepted only as a preliminary barrier, not completion of the whole full-text audit.

**D1-B2:** compare paid trusted replica, snapshots, authenticated Merkle aggregate/Fenwick, persistent path-copy/DSST, WAL/LSM generations, VC, Cauchyproofs and IVC on exactly the same F1 workload. Split peak versus amortized `U_w`, `Q_r`, `M` and `GC_w`, including PIN races and H-dependent catch-up.

**D1-B3:** only after these upper points, write a concrete asymptotic joint H1+H2 inequality under a fixed family of update/PIN/query distributions; reject candidates contradicted by the existing F1 upper frontier or reducible to the conjunction of applicable classical theorems.

**No new UCT-005 root theorem: OPEN_UNPROVED.**
