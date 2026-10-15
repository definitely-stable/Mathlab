# HYP-105 — start here

**Assign or resume mathematical research:** give the reader **one link** — [HYP-105 Research Work Brief](AGENT-BRIEF.md). It defines the root A/B/C objective, how to inspect the *current* GitHub research frontier (including parallel Draft stacks), which scientific evidence to retain, and what verified handoff to return. A separate prompt only needs to specify a particular slice/PR if one is intended; otherwise the brief instructs selection of the next unresolved mathematical step.

**Use this page as a reference index**, not as the assignment or a live status board. Details below describe research infrastructure and source imports, some historically: they do **not** prove that the most recently mentioned Draft PR is still the active frontier.

| Need | Go to |
|---|---|
| Delegate the next mathematical step | [AGENT-BRIEF.md](AGENT-BRIEF.md) |
| Verify live branches, heads, CI and status | [Living Context](LIVING-CONTEXT.md) |
| Read durable proof statements, formulas, dependencies and no-go scopes | [Results](registry/RESULTS.md), [Formulas](registry/FORMULAS.md), [Proof Graph](registry/PROOF-GRAPH.md) |
| Review provenance or decide how to integrate stacked PRs | [Evidence & No-Go](EVIDENCE-AND-NOGO.md), [Integration Plan](INTEGRATION-PLAN.md) |

Root mathematics: [#230](https://github.com/definitely-stable/Mathlab/issues/230); parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169). The issue text is the normative model and Branch A/B/C gate. A CI success is not a theorem proof.

## Live branch and PR inventory

The repository `main` is **not** necessarily the latest research branch: many HYP-105 results are stacked in unmerged Draft PRs. Verify current HEADs and base links from GitHub rather than reusing a historical status summary.

Using Python 3.12 and a GitHub API token with read-only repository access:

```bash
GITHUB_TOKEN=... python -m research.rcp.github_inventory \
  --repo definitely-stable/Mathlab \
  --output /tmp/mathlab-rcp
```

Produces `inventory.json` (full open-PR record, parent DAG, exact head/base SHAs, scoped CI and diagnostics) and `inventory.md` (human-readable HYP-105 open PR and ancestry index). `--checks-all` optionally verifies GitHub check runs for **every open PR**; this makes additional API requests, so it is not the default. Each `--check-pr` must identify a currently open PR. Missing CI examination means `NOT_INSPECTED`, not success. `UNKNOWN` means no checks returned for the selected SHA.

GitHub REST pagination is followed to completion and duplicates fail closed. The result is explicitly **non-atomic**, because GitHub can change while multiple API pages are read. Exact HEAD check successes only cover the queried SHA; they do not independently validate mathematical claims. Missing/deleted open parents, base SHA drift and forks are reported instead of silently inferred.

## How to continue research safely

1. Read the unchanged root Branch A/B/C target in issue #230.
2. Build a fresh inventory and inspect the latest relevant PR, parent SHA, proof document and check runs.
3. Read any superseding statements and known counterexamples (see [known/stopped registry](../KNOWN-AND-STOPPED-RESEARCH.md) and [decisions](../DECISIONS.md)).
4. Identify the *precise* missing lemma or counterfamily without upgrading a conditional or finite result to a universal theorem.
5. Preserve source ORIGINAL six distinct incidence IDs, true W(3,2^h), typed global injections, physical projections and GF(5) palette semantics.

## RCP implementation

Tracking: [HYP105-OPS-001 #474](https://github.com/definitely-stable/Mathlab/issues/474).
This page documents RCP-001-A inventory, RCP-001-B Claim Registry, and RCP-001-C evidence escrow/no-go capabilities below. **It is not a live deployment or merge-status report.** Resolve branch HEADs, CI status and milestone acceptance from current GitHub metadata and tracking issue #474. Proof-impact analysis, semantic Research Delta and workflow consolidation are tracked as separate future slices; never infer their availability from the plan alone.

Validate locally or on GitHub-hosted CI:

```bash
python -m unittest research.test_rcp_inventory -v
```

## Structured claims and proof links

RCP-001-B adds the [Claim Registry](CLAIM-REGISTRY.md): explicit mathematical quantifiers, shared model definitions, immutable identifiers, SHA-pinned source proof blobs, DAG dependencies and non-implication boundaries. Rebuild the current deterministic research claim index with `python -m research.rcp.claim_index --output /tmp/rcp-claims --verify-sources` (GitHub API read token recommended). The claim index records draft-stage mathematics, **not** independent acceptance; the open PR ancestry/CI inventory is provided by RCP-001-A above.

## Durable evidence and negative results

RCP-001-C adds the [Evidence & No-Go Ledger](EVIDENCE-AND-NOGO.md): permanently identifiable Git object escrow of selected five proof documents, corresponding oracle and test sources and two frozen witness fixtures, as well as five machine-linked non-implication/no-go records. Run `python -m research.rcp.evidence_ledger --output /tmp/rcp001c` for an offline SHA-verified index or add `--verify-originals` to cross-check the 17 original files at their exact GitHub commit references. These gates verify byte identity, not the correctness or novelty of mathematical assertions; root #230 stays OPEN.

## Current research context and delta

RCP-001-D adds [Living Research Context](LIVING-CONTEXT.md): fresh L0/L1/L2 GitHub + mathematics + escrow views, a sealed snapshot and semantic change reports. From repository root run:

```bash
GITHUB_TOKEN=... python -m research.rcp.context_builder \
  --output /tmp/hyp105-current --check-claim-prs
```

The resulting `snapshot.json` has a SHA-256 self-integrity check and non-atomic provenance flags. Compare with a previous `snapshot.json` using `python -m research.rcp.context_delta --before OLD --after NEW --output DIR`. Do not substitute a cached snapshot for a current GitHub query; do not infer global mathematical acceptance, merge, or CI success from a changed timestamp.

## Proof impact, structured mathematical documentation and integration

RCP-001-E introduces the [Proof Impact audit](PROOF-IMPACT.md), five versioned [structured research Markdown registers](registry/RESULTS.md), the [formula catalog](registry/FORMULAS.md) and an [ordered integration plan](INTEGRATION-PLAN.md). Unlike the transient L0/L1/L2 GitHub snapshots, the registered formulas, quantifiers, proof dependencies, source SHA pins, limitations and research protocol are retained in Git. After editing the mathematical JSON sources, regenerate via `python -m research.rcp.structured_docs --write`; CI checks parity with `--check`. Proof impact can identify registered downstream re-review obligations but does not independently diagnose contradictions or establish Root A/B/C.

## Research coverage and next proof imports

The A→E provenance and proof-impact infrastructure is integrated into `main`. [RCP-COV-001](COVERAGE-BACKFILL.md) adds a live, non-promoting research-coverage audit: run `python -m research.rcp.coverage_audit --snapshot /tmp/hyp105-current/snapshot.json --output /tmp/hyp105-coverage`. It lists all currently *tagged* open research PRs without registered proof claims, pinning their observed SHA and linking to exact sources. A missing registry entry is not mathematical rejection, and a title match is not a theorem. Import new proof/evidence records with explicitly correct quantifier order and retained Git bytes before scientific acceptance.

## Newly registered scientific AA4-Q source (proof status remains draft)

[RCP-AA4Q original seven-GF(5) join and C/C girth import](AA4Q-IMPORT.md) stores two separately scoped all-h deterministic claims, the original proof/oracle/test Git blobs from [scientific PR #476](https://github.com/definitely-stable/Mathlab/pull/476), exact independent SHA-256 pins, two formula entries, and a W32 one-side-marginal non-identification no-go. The five [permanent structured research Markdown registers](registry/RESULTS.md) are regenerated and GitHub-hosted CI verifies byte parity. Mathematical status remains `DOCUMENTED_IN_DRAFT / NOT_REVIEWED`; no claim of root Branch A/B/C proof acceptance is made.

## Original D6 fixed-side conditional theorem import

See [AA4-R-CYC provenance](AA4RCYC-IMPORT.md): source [research PR #480](https://github.com/definitely-stable/Mathlab/pull/480) is pinned by original Git blob SHA-1 and independently computed SHA-256, with three scoped mathematical claims, four LaTeX formulas and an explicit expectation-to-pointwise no-go. In particular, `forall f, E_g[D6(f,g)|f] >= s^6/8` and its genuine GQ dual are NOT claims about `inf_(f,g) S_s(f,g)`. Rebuild `registry/*.md` using `python -m research.rcp.structured_docs --write` and check the exact bytes using `--check`. The original scientific PR remains separate and unreviewed.

## Root-conditioned Fréchet method barrier (AA4-S)

See [AA4-S original source no-go import](AA4S-IMPORT.md): registered all-h true original point-root B/A (and dual A/B) unilateral Fréchet lower **equals zero** for every full legal global f,g,p, while the true finite W(3,2) source can retain positive jointly accepted GF5 motifs. The result limits a *proof method*, not the conjectured universal seven-class lower. Evidence and three LaTeX formulas flow into `registry/{RESULTS,FORMULAS,PROOF-GRAPH,PROTOCOLS,RESEARCH-MATRIX}.md` through `python -m research.rcp.structured_docs --write` and `--check`; source scientific PR #479 stays independently unreviewed.

## Original 60-position aligned D6 tensor and all-h conditional bound

[AA4-T provenance and exact-scope protocol](AA4T-IMPORT.md) registers the genuine original six-incidence positional 60-cycle tensor from scientific Draft PR #484. Five source-pinned claims separate the exact deterministic D6 inner product, one-complete-global-map expectation, every-fixed-side conditional lower for all h>=1, its original GQ dual, and true finite W(3,2) mean-versus-realization witness. The 1/98304 all-h bound is **weaker** than the earlier 1/8 AA4-R-CYC bound for h>=3. None implies an every-(f,g) seven-class minimax. Permanent formulas F-017..021 and proof links are generated into `registry/*.md` and validated by read-only CI after initial synchronization.

## Original six-forest nine-cell transportation and source corpus

See [AA4-U original source-forest evidence import](AA4U-IMPORT.md), pinned to scientific Draft PR #486: all-h genuine source six-edge forests, exactly nine BOTH-sides A/B/C eligible path cells (C/C forbidden), deterministic abstract per-cell Fréchet lower, and finite full W32 original 45-choose-6 source census. The finite S68/S72 zero-relaxed-bound but positive original seven-GF5 charge is a **proof-method limitation**, not a minimax counterfamily. Four scoped claims, five formulas, one new no-go and original Git-escrow SHA256 are mirrored to `registry/*.md` from canonical structured JSON. Independent scientific review and root #230 remain OPEN.

## Original-line shared D6 gluing (AA4-U-CYC)

The [AA4-U-CYC registry import](AA4UCYC-IMPORT.md) pins the genuine original six-incidence **two-event conditional** D6 gluing formula from source PR #487, an anchored 21,186-candidate W(3,2) row, exact original proof/oracle/test SHA records, and an overlap-cardinality-only no-go. It does not imply a complete second moment or an all-(f,g) universal GF5 lower. Formula and claim pages are generated into the five committed `registry/*.md` documents.
