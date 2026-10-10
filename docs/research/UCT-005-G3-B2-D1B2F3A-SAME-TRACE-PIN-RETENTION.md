# UCT-005 D1-B2-F3-A — same-transcript authenticated PIN-retention comparator

2026-10-10. Parent [#105](https://github.com/definitely-stable/Mathlab/issues/105), D1 [#223](https://github.com/definitely-stable/Mathlab/issues/223). Dependency: accepted COW [#248](https://github.com/definitely-stable/Mathlab/pull/248), segmented allocator [#258](https://github.com/definitely-stable/Mathlab/pull/258), remote PIN [#253](https://github.com/definitely-stable/Mathlab/pull/253), physical ledger [#265](https://github.com/definitely-stable/Mathlab/pull/265), and merged, hosted-green independent retention [#272](https://github.com/definitely-stable/Mathlab/pull/272). Parallel streamed F2 [#283](https://github.com/definitely-stable/Mathlab/pull/283) is **not** used as accepted dependency.

**Classification:** CONDITIONAL_SAME_TRACE_TWO_AUTHENTICATED_UPPERS / EXACT_FINITE_PAGE_LEDGER / RESEARCH_INPUT / NO_FULL_PARETO / ROOT_OPEN_UNPROVED.

## 1. Missing join and the critical source-index trap

F1's accepted offline PIN audit obtains historical roots from `SnapshotF1Reference.pin_registry`, which is correct for that precise reference. In the accepted **remote PIN bitmap** model `RemotePinBitmapF1`, however, that trusted registry is deliberately empty: the central authority stores only the 40-byte generation/digest, and the historical PIN bits live on an authenticated remote image. Inheriting the plain snapshot auditor without authenticating the bitmap would silently report **zero** historical roots. This slice explicitly rejects that invalid transfer.

`bulk_authenticated_retention_audit` uses `_read_verified_bitmap(audit=True)` to authenticate the full B=ceil(2C/8) byte image under the separately trusted generation/digest, reconstructs both readers' PIN epochs, compares them to independently trusted client tokens, then validates each pinned/latest snapshot against its root, manifest and public fixed-stride epoch slot. Audit page requests/replies, root reads and hash bytes have distinct counters, not free lookups. This is a *bulk* authenticated audit, not an O(P) trusted-scratch stream; `retained_pinned_pages` from the empty inherited registry is NOT read.

## 2. Fully frozen same-F1 trace and direct formulas

For n>=1 GF(2) bits and physical page size P, both models process exactly the same trace:
PIN reader0 at e0; SET x1=0 (toggle); SET x2=min(1,n−1) (no-op new epoch e2); PIN reader1 at e2; SET x3=n−1 (toggle to e3); authenticate LATEST/e0/e2 range parity for every nonempty interval if n<=6 (otherwise the documented three fixed representative ranges); GC; UNPIN reader0/GC; UNPIN reader1/GC. All SET positions are identically frozen, unlike superficially similar previous F1 and D1-B2-D report helpers.

At each stage let E be the **distinct** remote-authority authenticated PIN epochs, L=e3. In immutable full snapshot R, S=ceil(ceil(n/8)/P)+ceil(48/P) complete page images per epoch and M=ceil(ceil(2C/8)/P) remote bitmap pages. After honest GC:

```
K_R = (|E union {L}|)*S + M.
Δ_R = |E minus {L}|*S.
```

For the accepted no-node-ID-reuse segmented COW construction B1, with p_N=ceil(122/P), p_root=ceil(48/P), charged already-issued bitmap segment count M_COW and verified R(e) per-root node-ID reachability:

```
K_COW = |union_e R(e)|*p_N + |E union {L}|*p_root + M_COW.
Δ_COW = N_extra*p_N + |E minus {L}|*p_root
N_extra = Σ_j |union_{e_j<t<=e_{j+1}} Path(SET_t)|.
```

The last equality is the *construction-specific* accepted F1 checkpoint-interval identity, with no-op updates priced. Independent SHA-verified traversal (F1) and charged remote bitmap scan (new audit) are compared to the actual post-GC remote page-image counts. A *second* distinct-R(e) audit is **not** inserted as a free online GC oracle.

All equations count simulated fixed-size complete page transfers, never SSD NAND erase bytes or fsync barriers. PIN capacity C is bounded and epoch PIN statuses persist at the authority via a SHA-binding assumption. Byzantine nonresponse ABORTs; no liveness guarantee.

## 3. New finite falsification gates

[Code](../../research/uct005_d1b2f3a_joint_retention.py) and [independent tests](../../research/test_uct005_d1b2f3a_joint_retention.py) exhaust all binary initial words n=1..5 for P=1,2,64; compare every specified RANGE_PARITY answer and stage; check direct independent R snapshot bitmap page formulas and COW three-update path unions for n=1,2,3,5,33,257. Same-epoch dual-reader historical PIN must pay *two reader tokens but only one remote snapshot*. Remote bitmap digest tampering, root-token disagreement, missing snapshot image and corrupted manifest must ABORT. Offline bitmap reads/hash and separate COW authenticated traversal are charged. Unknown full resource axes are explicit `null`; no synthetic Pareto ranking is possible.

## 4. Scientific STOP and next F3-B

This is a **strictly model-scoped accounting equality for two different accepted implementations on the same task and trace**, not a lower bound on *every* possible service. Do not transfer `2min(B,P)` from pending F2 #283 onto accepted D1-B2-D, or treat COW's advisory bitmap as a trusted PIN registry. There is no proof of full trusted peak RSS, server network framing, verifier/prover computation, durable power-loss recovery, uniform SHA security, or SSD amplification; independent client historical roots and anchor publications remain charged by their own constructors.

After F2 exact-head focused/Research/INDEX/D1-A success and accepted merge, a separate F3-B may price its active/temporary double-image occupancy and conceptual scratch on THIS same trace, then test resource-vector compatibility and crash boundaries. Novel UCT-005 #105 requires a quantified same-model **strictly stronger joint lower bound** with a prior-art transfer, which F3-A intentionally does not claim.
