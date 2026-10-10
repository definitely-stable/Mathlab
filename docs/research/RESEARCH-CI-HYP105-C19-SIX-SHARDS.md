# Research CI: C19-stack six-shard, lossless 115-command hosted workflow

2026-10-11. CI-only follow-up to scientific C19 PR #312 (branch research/hyp105-b32e1c19-two-anchor-support-barrier). Reuses the independently fully green source CI adaptation #306 on the C16 stack. **Do NOT merge to main ahead of scientific C1-C19 ancestors, and do not equate CI with the all-h theorem.**

## Exact preservation evidence

- Monolithic Research on the C19 scientific branch contains EXACTLY 107 (name,run) command pairs (inherited from C1-C15 plus existing research primitives).
- Successful six-shard PR #306 contains all these 107 original command pairs UNCHANGED, plus two explicit C16 tests/report commands =109.
- C17, C18 and C19 each contribute TWO explicit dedicated steps (independent tests + actual script report): 6 NEW (name,run) pairs.
- New six-shard workflow therefore holds **115 distinct exact named checks**. None of the former 107 was removed/altered, and all six additions are explicit. Existing full unittest discovery also remains present.
- Independent workflow guard research/test_ci_research_six_shards.py pins all 115 unique name/run pairs (sorted FNV1a64 0xf36018665597438c), 6 GitHub-hosted ubuntu-latest Python setup jobs, heavy census placement and fail-closed seventh aggregate verdict. An intentional future step change must update the fingerprint under review, never silently discard a check.

## Jobs and budgets

| Job | Named script checks | Timeout |
|---|---:|---:|
| lent-001-foundation | 26 | 20 min |
| research-hyp105-foundation | 23 | 30 min |
| research-hyp105-exact-census | 13 | 90 min |
| research-catalog-and-primitives | 15 | 20 min |
| research-hyp105-coupled-low | 20 | 75 min |
| research-hyp105-coupled-exact | 18 (C11–C19) | 90 min |
| **research-full-suite** | aggregate only | 5 min |

Every compute job checks out the same PR HEAD and uses only GitHub-hosted runners. The aggregate job uses if: always() and needs all six shards; CANCELLED, SKIPPED or FAILED results are rejected. Only all six jobs + aggregate SUCCESS for the **exact same SHA** constitutes full Research workflow acceptance. The independent C17, C18, C19 dedicated contracts additionally need exact-head SUCCESS as appropriate, and INDEX CI must not be replaced by unrelated results.

## Why this structure

The old monolithic Research job's 10-minute budget cancelled genuinely heavyweight math work. PR #277 originally preserved only the older 77 research commands; C1-C15 appended another 30. PR #306 established a lossless 109-command six-job workflow on C16 and already achieved exact-head hosted full Research SUCCESS. This downstream adaptation incorporates C17–C19 WITHOUT dropping any historical HYP/UCT/INDEX/TOM/LIT proof check. This CI-only refactor does not change mathematical test bodies or the proof scope.

**Acceptance gate remains OPEN** until every shard including the added C19 report passes on this exact CI-only branch HEAD. The positive all-h S=Omega(s^6) issue #230 remains unresolved, and a passing C19 local-block zero-bound diagnostic is NOT its solution.
