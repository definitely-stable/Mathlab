# UCT-005 D1-C3 — multi-epoch conditional causal rank and shared-information STOP

2026-10-11 | [issue #319](https://github.com/definitely-stable/Mathlab/issues/319) | predecessors [D1-C2 #311](https://github.com/definitely-stable/Mathlab/issues/311), [D1-C1 #307](https://github.com/definitely-stable/Mathlab/issues/307) | [D1-C #302](https://github.com/definitely-stable/Mathlab/issues/302) | [root #105](https://github.com/definitely-stable/Mathlab/issues/105).

**EXACT_RESTRICTED_CLASSICAL_GF2_RANK / FALSE_ADDITIVE_CUT / NO_F1_NONFACTORIZING_LOWER / OPEN_UNPROVED_ROOT.**

## 1. Frozen finite service and paid side-information conditioning

Let n≥1, H≥0. Unknown initial author bits are x_0,…,x_(n−1). The H SET coordinates i_1,…,i_H are fixed and PUBLIC. Payloads b_1,…,b_H are additional *independently selectable* input variables. SET replaces one bit and may be a no-op; the author is serialized. This fixed-schedule experiment is **not** a distribution of adaptive operations. The two reader identifiers 0/1 label queries but are not extra independent input variables.

Each named query q=(reader,t,l,r), 0≤t≤H, 0≤l<r≤n, reads parity of the actual state after the first t operations. For each coordinate j, denote z_{t,j} its last writer: x_j when untouched and b_k for the largest k≤t with i_k=j otherwise. The raw GF(2) row is

    a_q = XOR_{j=l}^{r-1} unit(z_{t,j}).

If a specified subset of b_k values has been transferred to the verifier as **public and paid** information, remove their columns from the row and XOR their known contributions into a fixed output offset. Do not remove a secret b_k merely because the author knows it or because a server may have it: that information transfer must be accounted for in an actual F1 proof.

## 2. Exact conditional answer-spectrum lemma — CLASSICAL / no novelty

Let M be the matrix of remaining rows for a fixed finite query family Q and a fixed public coordinate schedule. Let r=rank_GF2(M). Vary every unknown input bit freely. The complete response vector is an affine linear image of the secret input, and therefore has **exactly 2^r** distinct realizable values. Consequently a deterministic error-free *one-shot* encoder/decoder that answers ALL named queries using at most s bits of accessible trusted information and at most b bits in its total input-dependent untrusted response transcript (including all real side channels) must satisfy s+b≥r. The injection proof is simply linear map rank plus pigeonhole. The statement excludes probabilistic cryptographic soundness, malicious-server completeness, free program-dependent advice, and any unpaid verifier-known update log.

This is **not** a theorem of n+H independent historic pages, physical writes, per-query probes, full F1 authenticated storage, network signatures, GC retention, bounded adversarial failures, crash durability, or a nonlinear/time-distributed Pareto frontier. A rank-r encoding is an abstract answer-only quotient; making it an online *authenticated F1 protocol* would require charged update maintenance, SHA/proof machinery, reader freshness and trusted PIN retention. One cannot promote the same classically tight injectivity result to a new UCT root.

## 3. Exact reuse and erasure counterexamples

- **Duplicate readers**: n=3, H=0, both independent readers observe all three singleton ranges at epoch 0. Individual reader ranks are 3+3=6; the *joint* rank is 3. One physical set of source data can answer both in the honest answer-only projection, although both F1 PIN root tokens, registration and query communication must still be paid.
- **Across epochs, one unchanged bit**: n=2, H=3, all SETs overwrite coordinate 1, while four historical queries ask only coordinate 0. Epoch ranks sum to 4; joint rank is 1. Counting a new independent bit on every epoch overcounts.
- **Real independent history**: n=1, H=3, the initial bit and each of three private SET payloads vary independently and each epoch is observed once. Joint rank is 4; this is *not* a theorem of four physical P-byte pages and does not automatically guarantee that a malicious server returns all epochs.
- **Known author payloads**: under the same schedule when all three SET values are delivered as paid side information, the rank of remaining unknowns is 1 (only the initial bit), not 4. Query output offsets are retained.
- **Erased dependency**: only the last epoch is queried after three overwrites of one bit. The joint rank is 1 because earlier independent inputs cannot affect any requested answer.

The first two are explicit falsifiers of **naive sum of per-cut / per-reader independent storage or write lower bounds**. Multiple cuts may refer to exactly the same paid cell or digest; any new lower bound must account for reuse by a proven dependence or disjointness argument. Here rank computes *information that must be distinguishable somewhere*; it does **not** prove which resource must hold it.

## 3A. Sharp formula for complete interval families — CLASSICAL

If the query family contains **all** half-open intervals at each epoch in a named set E (possibly observed by either reader), all singleton intervals are present, so the joint row span is exactly the span of the basis units indexed by **distinct live last-writer unknown symbols** visible at at least one t in E. Thus the exact conditional rank is the size of that provenance-symbol union, not the sum of the epoch-by-epoch sizes. A standalone oracle derives this count from literal last-writer identifiers, independently of matrix Gaussian elimination. If E contains **all** epochs 0,…,H, each independently variable initial x_j and every hidden SET payload b_t is visible at least once; rank=n+H−k for k publicly paid SET payload values. With an incomplete interval query family, the count of symbols appearing in a row is only a bound, not an equality: [0,2) over two unknown bits has row support size 2 but joint rank 1. These are elementary basis/rank facts, *not* physical storage or authenticated-history lower bounds.

## 4. Reproducible evidence and novelty firewall

The [executable rank model](../../research/uct005_d1c3_causal_rank.py) builds last-writer GF(2) rows. The [independent tests](../../research/test_uct005_d1c3_causal_rank.py) use separate literal array-valued SET execution with all assignments, not the matrix constructor, and exhaust n≤3, H≤3, every schedule, all named historical half-open intervals and overlapping second-reader observations, and all subsets of paid-public SET payloads. The test also checks sparse families, invalid metadata, no-op trajectories, and reported unknown F1 cost axes.

The accepted F1 cost coordinate set is taken from [F1-MODEL](UCT-005-G3-B2-D1B0-F1-MODEL.json). None of the n,H,lambda,epsilon,P parameterization or independent full F1 resource quantities is deduced from this answer-only projection. All undiscovered F1 cost axes are JSON null rather than zero. The frozen SHA256/P-byte F1 simulator is an upper/reference construction only.

Historical source boundary: Fredman–Saks (1989), Pătraşcu–Demaine (2006), DSST persistence (1989), memory checking BEGKN/BKV (1994, 2024/2025), SUNDR (2004), Tas–Boneh (2023), Abusalah et al. (EUROCRYPT 2026) all have distinct theorem models; a model-preserving reduction to the fully priced Byzantine F1 service is not established here. This restricted result is elementary GF(2) linear rank plus information counting, not priority over these papers or a new theorem.

## 5. Exact D1-C decision

**C3-01: FALSE** — sum of isolated reader/epoch ranks is not a valid independent joint-information lower.

**C3-02: ACCEPT_RESTRICTED_CLASSICAL** — exact conditional joint rank and the one-shot information floor under fully specified transcript access.

**C3-03: OPEN_UNFORMULATED** — an *original strictly nonfactorizing* lower bound involving jointly paid online update reads/writes, remote pages, query proof bytes, two offline reader states, trusted freshness, retained PIN epochs and GC has neither a frozen valid formula nor an all-horizon security and primary-literature transfer proof. Do not call the computed rank such a lower.

**Next allowed science:** define an actual adaptive hard schedule/distribution with bounded honest completeness and full (s,S,U_r,U_w,U_delta,Q_r,B_pi,C_author,C_reader,G,V,A,T,M,GC_r,GC_w,GC_free,F,lambda,epsilon,P) accounting, then try a proof or strict countermodel. Require a strict same-model asymptotic gap beyond elementary one-shot rank and already applicable sources; otherwise record SCOPED_STOP without renaming known bounds. Root #105 stays **OPEN_UNPROVED**.
