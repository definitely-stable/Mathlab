# RESEARCH-INDEX-003 — OpenAI Math primary-package / statement audit

Status: **SOURCE-PACKAGE VERIFIED; THEOREMS NOT INDEPENDENTLY VERIFIED**  
Date: **2026-10-08**  
Issue: [#30](https://github.com/definitely-stable/Mathlab/issues/30)  
Normative registry: [registry.json](registry.json)  
Frozen external revision: [openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb)

> **2026-10-08 follow-up / correction (OM-116):** The original selected `lean/docs/116.md` is limited to the characteristic-zero hitting tuple and rational formulas, but **the same family also contains a separate 2026-10-04 author manuscript claiming a construction in every positive characteristic**. See [TOM-002 theorem-level audit](../TOM-002-OM116-OM140-THEOREM-AUDIT.md). This document's claim about the *selected Lean scope* remains correct; it must **not** be read as saying no positive-characteristic paper exists. The additional theorem has not been independently verified by Mathlab.

## Scope of source checking

For each of the ten selected families the following first-party records were read or checked against the **frozen** external SHA:

1. `CONTENTS.md` (author collection's broad family summary) and `lean/docs/<family>.md` (author's specific formalization **scope and exclusions**).
2. The `preprints/<paper>/README.md` author/package citation and its related actual PDF filename **in the repository directory** (GitHub tree listing, not just a syntactically plausible URL); additional main PDFs under families 113/115/116 also checked as present.
3. At least one `lean/ComparatorChallenges/<challenge>.json`: names a `challenge_module`, `solution_module`, exact `theorem_names` and permitted axioms. Selected challenge and solution files were also inspected for families 108/113/114/116/135/140, **without building or running the comparator**.
4. A typed conceptual relationship to a Mathlab/Delsk/DeltaMeter question and a concrete missing-model warning in the registry.

**Limits**: The actual proofs in the PDF manuscripts have **not been read in full or independently rederived** in this import. The corresponding Lean proof-library closure has **not been compiled or checked with Comparator** on our CI. `ComparatorChallenges/*.lean` are challenge skeletons which may contain `sorry` while a manifest names a separate `solution_module`; the mere presence (or presence of `sorry` in the skeleton) is **not** a sufficient success/failure signal. Only a real comparator invocation with recorded SHA, logs, theorem names and axiom report would strengthen that evidence. All ten records remain `EXTERNAL_MANUSCRIPT_CLAIM/source_catalog`, not `THEOREM` and not `repository_proof`.

The PDF paths are provenance links and existence checks; **not proof verification**. The initial automated discovery did not substitute external derivative indexes for upstream first-party statements.

## Source-to-claim matrix and deliberate mismatches

| ID | Specific checked family and principal source | What the selected Lean scope states | Crucial model boundary / anti-claim |
| --- | --- | --- | --- |
| [OM-108](INDEX.md#om-108) | [Permanent cubic border determinantal bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/108.md) | Complex-field exact/border determinant lower bound; separate initial-form lemma | Not a general arithmetic/ABP lower bound; ABP corollaries outside selected formalization |
| [OM-113](INDEX.md#om-113) | [Matching count + entropy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/113.md) | FPRAS with exact zero detection; entropy inequalities on feasible matchings | An approximate counter is **not** an exact polynomial-time counter; distinct selected theorem files |
| [OM-114](INDEX.md#om-114) | [Common matroid base counting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/114.md) | FPRAS for **matroids** of equal rank with independence oracles | Family headline says integer **polymatroid** bases; that extension is **NOT** the theorem selected in this Lean scope |
| [OM-115](INDEX.md#om-115) | [Contingency tables](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/115.md) | Exact expected-polynomial sampler and distinct bounded-cell FPRAS counting statement | Do not conflate almost-sure termination, worst-case time, counting and sampling |
| [OM-116](INDEX.md#om-116) | [Noncommutative identity testing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/116.md) | A universal rational matrix hitting tuple for bounded division-free formulas over **characteristic zero**, plus rational-formula hitting lists | Broad family headline suggests all characteristics; does **not** transfer to odd-prime ASET/GF(q) without a separate positive-characteristic audit |
| [OM-117](INDEX.md#om-117) | [Uniform sparsest cut SDP](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/117.md) | Existence of a near-sqrt-log SDP integrality-gap sequence | Not a complexity-theoretic hardness theorem for approximation |
| [OM-131](INDEX.md#om-131) | [Switch-chain mixing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/131.md) | Graph-switch chain TV mixing at most `2 n^8` for specified simple-graph model | Family's exact uniform sampler is **outside** selected theorem statements |
| [OM-135](INDEX.md#om-135) | [Depth-five IMM circuits](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/135.md) | Characteristic-zero lower bound and explicitly bounded all-field upper construction | Neither a word-RAM performance result nor a bound for unrestricted circuits |
| [OM-139](INDEX.md#om-139) | [Log-concave oracle sampling](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/139.md) | Upper `C_epsilon d^epsilon` and lower `c log d` **oracle queries** under normalized Hessian assumptions | Unbounded computation allowed between exact value/gradient queries; no Rust CPU complexity bound |
| [OM-140](INDEX.md#om-140) | [Memory/sample bounds for Gaussian regression](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/140.md) | `O(d^2)` persistent bits require `Omega(d log 1/epsilon)` noiseless Gaussian samples at stated success | This is a stochastic inference and angular-error model, **not** automatically a lower bound for exact delta/ASET/zero-effect certificates |

For all rows, open the [registry](registry.json) to see **separately pinned** preprint PDF(s), author package README and Comparator challenge manifest. Every row's metadata is explicitly marked not independently re-proven.

## Relevance ranking for Mathlab (research utility, not novelty rank)

**High — mathematical-method transfer only:**
- **OM-116**: separate characteristics and exact algebraic identity tests. Strong comparator for HYP-002/GF(q), but the selected positive-characteristic extension is missing; cannot infer ASET capacity.
- **OM-140**: explicitly charged persistent memory. Useful discipline when forming O01 cell-probe/update models; no straightforward reduction.
- **OM-108 and OM-135**: genuine *kind* of theorem to aim for — constrained-model lower bound with hard assumptions and matching/up-to-exponent upper construct. No new theorem transferred.

**Medium — independent finite/combinatorial methods:**
- **OM-113/114/115**: FPRAS/exact-sampler guarantee discipline, probability and oracle models; helpful to compare with exact enumerative LENT G2B evidence.
- **OM-117/131**: graph structures, relaxation and mixing; mainly background/negative model examples.
- **OM-139**: explicit reminder that query complexity does not imply wall-clock performance.

These are *conceptual navigation edges*, not implication edges. **No theorem eligible for publication or Rust crate authorization has been selected by this import.**

## Follow-on proof audit gate — do not auto-promote

To upgrade even one OM item from source_catalog requires:
- primary PDF paper-level reading including definitions, exact theorem and proof dependencies;
- named Lean comparator challenge + solution, exact hash, successful `lake env comparator` report, axiom audit (and permitted assumptions);
- mapping between the paper theorem, chosen Lean theorem and intended Mathlab model; independent counterexample or reduction search;
- explicit separate decision on mathematical relevance, external correctness and world-literature novelty.

This is not reasonably achieved by importing all papers or by checking a repository tree.

**RESEARCH-INDEX-003 decision: IMPORT_SCOPED_PRIMARY_METADATA, NO CLAIM PROMOTION.**
