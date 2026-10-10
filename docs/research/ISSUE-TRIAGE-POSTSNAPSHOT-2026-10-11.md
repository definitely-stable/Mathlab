# Mathlab — issue-triage post-snapshot review (2026-10-11)

**Dated evidence, NOT LIVE status.** The 2026-10-10 archived snapshot contains 55 open issues. A later GitHub issues-only query returned 58 open issues and 30 open PRs; the complete ID sets, titles for additions and closed entries are in [ISSUE-TRIAGE-DELTA-2026-10-11.json](ISSUE-TRIAGE-DELTA-2026-10-11.json). Identity conservation: **58 = 55 + 5 newly represented − 2 closed**. The original snapshot and its 20-task execution plan remain immutable. Running an offline validator will not verify contemporary live GitHub state.

## Verified transition / next owner

| Issue | Transition | Action / acceptance |
| --- | --- | --- |
| #244 | CLOSED; implementation PR #248 MERGED | Remove stale “pending COW implementation” action. Accepted only as a scoped authenticated upper comparator. |
| #254 | CLOSED; implementation PR #258 MERGED | Remove stale “segmented allocator to implement” action. Bitmap-only SET savings are not full resource Pareto. |
| #262 | OPEN, absent from archived set | D1-B2-F same-F1 transcript, merged comparator PR #265. Keep scientific owner open: 14-axis resource ledger incomplete. |
| #270 | OPEN, absent | F1 retained PIN history: PR #272 MERGED. Charge independent offline auditing, not an online lower bound. |
| #289 | OPEN, absent | **External engineering tracker:** KytyPS5 `perf/texture-range-index`, Windows GitHub-hosted CI only. No Mathlab main code and no unconditional GPU/FPS inference. |
| #295 | OPEN, absent | F3-C draft PR #294: conditional **speculative** SHA staging before trusted commit. Fail-closed SHA, paid abort writes/drops and crash-prefix model required. |
| #297 | OPEN, absent | F3-D: **non-speculative** deferred-output model and primary-source kill gate; do not transfer the permissive F3-C upper as a theorem for the stronger contract. |

Issue **#293** was created and subsequently CLOSED after the archived checkpoint; because it was absent from both open-issue sets, it is correctly *not* included in their five-item difference. Its Research timeout history matters for CI acceptance. Current main `research.yml` has a 45-minute job limit; this does not turn earlier cancelled workflows into SUCCESS. Open PR #277 proposes a lossless 77-command, four-job GitHub-hosted split; require proof of command preservation and fresh exact-head results.

## Scientific ownership and dependency constraints

**UCT-005 #105 — OPEN_UNPROVED.** F1 scientific owner #223 and separate typed bridge atlas #234 stay open. Scoped merged comparator lineage: #248 COW → #258 segmented allocator → #265 resource reconciliation → #272 PIN reachability; #283 two-pass streamed bitmap and #287 authenticated same-history PIN audit also merged. Draft #290 F3-B is a partial cost ledger; draft #294 F3-C is stacked on #290. New #297 F3-D explicitly forbids the pre-verification untrusted writes allowed by #295. Compare only the same two-reader SET/PIN/LATEST/AS_OF/GC transcript under the *same* trusted authority, hash, remote page, RAM, proof and failure model. Unmeasured cost coordinates remain `null`; there is no universal joint lower bound, strict full-vector Pareto conclusion or durability/security theorem.

**HYP-105 #230 remains OPEN.** C0 #249 MERGED. The dependent chain C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7-A #279 → C8 #284 → C9 #285 → C10 #286 → C11 #288 → C12 #291 → C13 #292 → C14 #296 is not automatically accepted/merged merely because downstream branches exist. C7-B #280 is a parallel branch. Finite W(3,2), exact orbit equality, certified bounded search and restricted motifs do not prove the all-h Ω(s⁶) correlated requirement or a new ASET exponent.

**DAG×ALG #161:** #267→#268→#271→#274 is a dependency stack; #275/#276 are independent studies. APPEND_SINK and arbitrary old-old edge updates need a resource-preserving reduction before theorem transfer. **INDEX #183/#211** and **TKG #195** retain separate physical and authenticated temporal semantics.

## Architectural change for research metadata

- Keep the 55-item JSON, generated dashboard and 2026-10-10 plan as immutable historical evidence.
- Keep each later delta as an **append-only, dated** snapshot. Check complete set arithmetic, duplicate IDs and scientific status, never infer live state from CI.
- PR #256 owns the scoped status registry; reconcile its older #244/#254 active-state references there before calling them live. Do not replace canonical theorem status or infer proof from a merge.
- PR #263 owns a **derived**, typed AI research graph. Links should distinguish `DEPENDS_ON`, `PROVES_SCOPED`, `FALSIFIES`, `APPLICATION_ONLY`, `REDUCTION_REQUIRED`, and `SOURCE_OF`. It is not an alternative authority for GitHub issue state, source IDs or theorem grade.
- Preserve the #257 D1-B conditional-hardness dependency audit and its three added anchors; source metadata and citation do not transfer lower bounds without matching model hypotheses.

## Verification and merge conditions

PR #257 previously passed its [historical focused CI](https://github.com/definitely-stable/Mathlab/actions/runs/38053794737) and [historical full Research CI](https://github.com/definitely-stable/Mathlab/actions/runs/38053794759) at `a7ea6490b8e27869e6c16cdb3b6a7c44811a0878`. Neither is CI evidence for a later commit.

1. Verify the new set delta against the untouched 55-item JSON and test negative mutations.
2. Preserve `OPEN_UNPROVED` for UCT #105 and the scientific open state of HYP #230.
3. Synchronize #257 against current main with no force updates; review its true file diff.
4. Run exact-head focused triage, D1-B audit, full Research and applicable other GitHub-hosted checks.
5. Obtain independent review; only then consider exiting draft. Post-merge main CI must be recorded separately.

[Dependency-aware successor plan](RESEARCH-MAINTENANCE-PLAN-2026-10-11.md). **Rollback:** revert only the dated delta, navigation and validator artifacts; never rewrite the original snapshot, canonical literature identities or theorem tree.
