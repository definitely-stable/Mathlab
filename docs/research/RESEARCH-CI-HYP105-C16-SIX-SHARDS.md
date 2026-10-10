# Research CI: six GitHub-hosted shards for the C16 HYP-105 stack

Date 2026-10-11. Parent scientific PR [C16 #305](https://github.com/definitely-stable/Mathlab/pull/305), parent theorem issue [#230](https://github.com/definitely-stable/Mathlab/issues/230), original standalone CI refactor [#277](https://github.com/definitely-stable/Mathlab/pull/277). **CI-ONLY**, no mathematics, test logic, theorem status, or main changes here.

## Why #277 cannot be merged unchanged into the C16 stack

Original #277 split 77 historical commands of the ten-minute Research job into four independent hosted shards (26/23/13/15). #277 passed its own GitHub-hosted shards on HEAD 7b36f1b2..., but its main-based workflow diverged from the C1-C16 stacked tree. At C16 HEAD 2c6a2d2a..., the monolithic workflow contains 107 named (name, run) command pairs. A direct replacement with old #277 would **silently delete 30 C1-C15 explicit research commands**. Moreover, the C16 exact independent test/report was present only through generic unit discovery and dedicated Contract, not explicit in broad Research.

## Lossless implementation and exact proof of command preservation

This CI-only follow-up branches from the exact C16 head, retaining the C15 ancestor chain, and adapts the already successful #277 four-shard infrastructure. Machine enumeration of the *actual* old and new workflows before the edit established:
- 77 original #277 named (name, run) command pairs match **exactly** among the C16 107 pairs (no missing, no altered command);
- the other 30 pairs are precisely C1-C15 tests/reports (20 for C1-C10, 10 for C11-C15);
- two additional independent C16 script checks are appended (tests and genuine W32 exact report);
- the resulting **109 distinct exact commands** occur once each in six independent Research jobs, versus 107 before. The preexisting 'Unit tests' discovery remains a preserved command, not silently removed or replaced.

| Job | Named research run commands | Runner | Timeout |
|---|---:|---|---:|
| lent-001-foundation | 26 | GitHub-hosted ubuntu-latest | 20 min |
| research-hyp105-foundation | 23 | GitHub-hosted ubuntu-latest | 30 min |
| research-hyp105-exact-census | 13 | GitHub-hosted ubuntu-latest | 90 min |
| research-catalog-and-primitives | 15 | GitHub-hosted ubuntu-latest | 20 min |
| research-hyp105-coupled-low | 20 | GitHub-hosted ubuntu-latest | 75 min |
| research-hyp105-coupled-exact | 12 (10 C11-C15 + 2 C16) | GitHub-hosted ubuntu-latest | 90 min |

**Mandatory seventh verdict job** `research-full-suite` has `if: always()`, waits for all SIX jobs, and fails if ANY is failure, cancellation, or skip. Existing short `lent-001-foundation` success does **not** establish full Research acceptance. Once integrated, repository required-status checks should include `research-full-suite` (ruleset audit), slice-specific C16 Contract, and applicable INDEX checks. No self-hosted runners; no loosened mathematical assertions or skipped commands.

## Regression contract and CI acceptance

Independent `research/test_ci_research_six_shards.py` freezes all 109 (name, run) pairs with an exact sorted source digest (FNV1a64 `c76f9dcee9fa911f`), tests exact command count, no duplicated names, all six hosted Python setup jobs, known correct census/contract placement and fail-closed aggregate dependency. The frozen digest must be updated under review when new deliberate commands are added; the CI does not silently admit removed or altered checks. A checksum is an audit guard, NOT a security signature or proof of mathematics.

Required gate: each of SIX hosted jobs and the aggregate verdict must be SUCCESS on the same exact CI-only PR HEAD; C16 dedicated Contract must also pass on its own exact C16 head. A job timeout, missing dependency or inaccessible source is FAIL/UNKNOWN, never a green scientific result. New independent checkout for each job can uncover formerly implicit artifact dependencies; these are defects, not reasons to omit tests.

## Research decision and branch discipline

No merge to main from this CI-only PR. First confirm hosted SUCCESS, then review ancestry and plan a safe ordered integration of scientific C1–C16, retaining #277 as historical source rather than independently merging conflicting workflow text. Even perfect CI proves only implementation correctness of the tested finite models, not #230 all-h universal bound. OPEN_WITH_FORMAL_BLOCKER persists for HYP-105.
