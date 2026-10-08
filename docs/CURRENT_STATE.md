# CURRENT_STATE

## HYP-103 G0 (issue #70) — classical certificate complexity closure

[HYP-103-G0-CERTIFICATE-REDUCTION.md](research/HYP-103-G0-CERTIFICATE-REDUCTION.md) freezes the exact old-root+batch-overwrite verifier model and proves that minimum authenticated old-bit probes are the minimum hitting set of all opposite-output consistent-input difference sets, i.e. classical promise-domain certificate complexity. [Independent finite regression](../research/test_hyp103_certificates.py) exhaustively cross-checks all Boolean functions of n<=3, all inputs and overwrite batches. The **broad theorem novelty target is STOP_CLASSICAL_CERTIFICATE_REDUCTION**; scoped incomplete proposals need a new costed retained-metadata/verification-work model before reopening. Literature index expands 102 to **108** distinct records with new primary works LIT-103..108. Exact-head GitHub-hosted CI and merge must be verified separately. No Rust, new theorem, or product result.

## TOM-007 (issue #68) — cross-domain falsification and source import

Research documentation now specifies six scoped candidate statements HYP-101..106, primary-source/model-overlap mapping, finite Boolean-DAG/GF(5)/toy-block/snapshot sharing falsifiers and no-prototype STOP/GO decisions. The normative evidence document is [TOM-007-SIX-HYPOTHESIS-AUDIT.md](research/TOM-007-SIX-HYPOTHESIS-AUDIT.md); unit tests are `research/test_tom007_hypotheses.py`. External literature metadata grows from 95 to 102 distinct citations by importing only seven previously absent primary identities. Originality: **NOT ESTABLISHED**; a verified finite witness does NOT imply asymptotic separation or algorithmic optimality. Review and exact-head GitHub-hosted CI are required before acceptance; issue #68 holds the latest CI/merge outcome. No Rust or product change.

## TOM-005 seven-theorem research gate

Issue #59: stages 1/2/3 extended to ALL seven mathematical candidates. Seven constrained proofs and independent finite-oracle models are under a GitHub-hosted CI acceptance gate. Claimed original general theorems: zero; Rust crate: none. Canonical [mathematical audit](research/TOM-005-SEVEN-THEOREM-AUDIT.md). The known/STOP registry is extended from 33 to 40 model-scoped records. Verify current branch/PR status before citing completion.

## Anti-rediscovery research inventory (new audit slice)

The [Known / proved / stopped research registry](research/KNOWN-AND-STOPPED-RESEARCH.md) indexes **40** repository-supported claims across LENT, HYP, TOM, reconciliation and DELSK. A pinned JSON record specifies per-item disposition, what not to repeat, its authority, closest public sources where available and a narrow reopening gate. It distinguishes CLOSED_PROVED, PRIOR_ART, STOP_PRODUCT, SUPERSEDED, MODEL_MISMATCH and DEFER. The separate `research/known_registry.py --check` validator audits paths, schema and deterministic human view. This documents existing decisions; it **does not create any new theorem, source proof or Rust artifact**. Baseline for this slice was live main `269aa27c7f99bc5cf2ae6821d31ad0454620c045`, with main research and independent GF5 certifier green. The research registry PR and merged-main checks are separately required before acceptance.


Last fully verified main checkpoint: 44d8eb0d1feed1b51f30ec16019629816d004bb7, PR #54 merged 2026-10-08. Recheck live SHA when starting a new task.

Current decision: LENT G2_REDUCE_TARGET for new Rust-product originality; TOM-003 D1 and D2 both COMPLETE as explicit negative research/product gates. No new theorem or Rust crate authorized.

## Verified mathematical/research outcomes

- LENT-G2B-B2: exact numerical computer-assisted result A_5^set(3,2,2)=10, verified 10-family and globally complete 11-family DRUP UNSAT certificate. Source docs/research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md; proof SHA256 ffbc5fabb0900acf52e72c41304572eea22f9a5d8c6bd19c2377a038d6e2f748. GitHub-hosted certifier unchanged.
- A_3^set(4,2,2)=7 finite exact. HYP-001/002 local derived exponents valid but source-level originality NOT established. THEOREM-GAP-004 audit PR #52 establishes Lefmann (2005) prior-art construction exponent overlap. No novel asymptotic theorem is claimed.
- TOM-003 D1 (#49 CLOSED): classical Moore/Myhill–Nerode e-essential-bit lower/upper for no-probe untrusted overwrite; externally authenticated old-bit counter requires fully charged verification and external state. STOP_STANDALONE_UNTRUSTED_NO_EFFECT.
- TOM-003 D2 (#53 CLOSED, PR #54 MERGED): independently authenticated source root **and** count, exact SSZ-style helper multiproof, correct old/new root/count transitions, exact structural byte/hash accounting; negative tests for tampering, false old bits, stale roots, duplicate indices and forged initial count. Known prior art (Ethereum SSZ, transparency-dev compact ranges, RFC 9162); NOT a new theorem. Decision STOP_STANDALONE_MERKLE_UPDATE_CRATE.

## Hosted CI evidence (exact merged main)

- [research #37787311399](https://github.com/definitely-stable/Mathlab/actions/runs/37787311399): SUCCESS, 139 tests, 61 curated cross-repository indexed records, literature schema checks and new TOM-003-D2 finite structural/root/trust gates.
- [GF5 DRUP proof #37787311395](https://github.com/definitely-stable/Mathlab/actions/runs/37787311395): SUCCESS, independently checked exact=10 refutation retained.
- [PR #54 review](https://github.com/definitely-stable/Mathlab/pull/54): scope/soundness, conditional SHA-256 security and fixed wire-cost claims audited. All source-level guardrails preserved across simultaneous PR #52.

D2 source docs/research/TOM-003-D2-AUTHENTICATED-OVERWRITE-AUDIT.md, code research/tom_authenticated_overwrite.py, unit tests research/test_tom_authenticated_overwrite.py.

## Remaining work

Issue #15 TOM-001 remains open as research opportunity map. G2 parent #14, HYP #24/#25 remain scoped to source/model and finite prior-art work, not guaranteed theorem novelty.

**Next:** Do not run TOM-003 D3 or create a Rust crate without a **new operation** and best-source gap. The broad authenticated proof operation duplicates standard Merkle multiproofs and source-tested compact range designs. Choose an original-looking different primitive question with a concrete useful workload, before additional theorem engineering. Full verifier source and fresh proof must be charged for future trusted update models.

The post-merge status checkpoint itself is docs-only; its GitHub CI may create a later main SHA while leaving the cited research/certificate evidence at commit 44d8eb0d unchanged.

Last updated: 2026-10-08.
