# Mathlab dependency-aware execution plan — 2026-10-11

**Dated roadmap; NOT LIVE issue or CI status.** Derived from the immutable 55-issue snapshot and later 58-open-issue delta. Dependencies are ordering constraints; impact×tractability alone does not establish scientific priority. Only GitHub-hosted runners.

| Phase | Owner | Required predecessor | Next allowed action | Acceptance / STOP gate |
| --- | --- | --- | --- | --- |
| P0-1 | PR #257 | Original 55 snapshot + new delta | Preserve archive, validate 58=55+5−2; sync branch to current main | Exact-head focused + full Research, independent review, post-merge main CI |
| P0-2 | #293 (closed), PR #277 | Current 45-min Research baseline | Audit preservation of all 77 commands under four hosted jobs | Aggregate CI green, no dropped tests, cancelled ≠ PASS |
| P0-3 | PR #256 | #244/#254 already CLOSED as scoped uppers | Reconcile historical statuses in the separate research registry | No false live state or root novelty promotion |
| P0-4 | PR #263 | Typed source-of-truth rules of #256/#257 | Derived graph and scalable AI research retrieval | Stable IDs, typed proof edges, no second authoritative registry |
| P1-1 | #223, #252 | Merged #248/#258/#265/#272/#283/#287 | Independently reconcile same two-reader F1 cost axes and retained historical PINs | Unknowns are null, not zero; no full Pareto |
| P1-2 | PR #290 | Accepted F3-A/F2 and current full Research | Retarget stacked F3-B to main, validate 3-model ledger | Same transcript, audit/GC/trust charges, exact-head green |
| P1-3 | #295 / PR #294 | Accepted #290 | Speculative old-SHA invalid/withheld final-page abort tests, paid staged writes/drops | No trusted commit on invalid digest; durability remains open |
| P1-4 | #297 | Explicit no-speculation model; #295 as countermodel outside contract | Prove/falsify deferred-output state–read inequality with paid advice/root and primary prior art | Exact quantifiers and source audit, scoped STOP or proof; not UCT root |
| P1-5 | #255 / PR #259 | Full-vector rather than single-bit authentication | Check total trusted writer/reader/PIN authority budget | Independent membership counterexample, no universal extrapolation |
| P1-6 | #247 / PR #250, #142/#147/#154 | Current canonical catalog and source identities | Import only unique primary sources and reconcile historical ID assumptions | No LIT ID reuse, DOI/arXiv dedup, generated index parity |
| P2-1 | #230 / PR #296 | C0 #249 and C1→C13 sequential gates; parallel #280 separately | Review restricted C14 true joint GQ branch and exact finite oracles | All-h correlated Ω(s⁶) or infinite valid counterfamily; otherwise OPEN |
| P2-2 | #161 and #267–#276 | Explicit update model + stacked dependencies | Test read/local/write cut against append-sink and old-old edge regimes | Scoped theorem or explicit prior-art/reduction STOP |
| P2-3 | #183/#211 | Paid remote physical page/RAM/highwater/GC semantics | Bounded-slack and crash-prefix counterexamples | Exact gate, no SSD/NAND inference |
| P2-4 | #195 | Frozen temporal authenticated Boolean/negative proof output | Independent proof/read/update accounting | No conflation of parity, reachability and witness enumeration |
| P3 | UCT #105/#223/#234 | Same-model full price vector and source audit | Seek genuinely nonfactorizing joint lower bound | Formal proof, novelty audit and falsifiers, or scoped STOP |

## Merge firewall

Never merge downstream stacked branches out of order. Verify head/base SHAs immediately before acceptance; run focused + full exact-head GitHub-hosted CI, not historical checks on another SHA. Do not silently skip long HYP exhaustive cases. Require post-merge main CI independently. Keep canonical theorem tree UCT-005 **OPEN_UNPROVED** until mathematical and prior-art acceptance—not a passing dashboard or merged implementation.

**No automatic issue closure, bibliography rewrite or production change.** Original `ISSUE-TRIAGE-SNAPSHOT.json` and 2026-10-10 maintenance plan are immutable evidence; this document is the dated successor and can itself become stale.
