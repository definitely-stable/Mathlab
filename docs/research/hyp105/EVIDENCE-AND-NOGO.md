# HYP-105 — RCP-001-C: durable evidence and scoped no-go ledger

Tracking: [HYP105-OPS-001 #474](https://github.com/definitely-stable/Mathlab/issues/474). Builds on the [RCP-001-B claim registry](CLAIM-REGISTRY.md). The original scientific [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains open.

## Why a Git archive, not only a CI URL?

GitHub Actions artifacts and logs have finite retention. A URL to a successful job is not a durable mathematical certificate. Additionally, an unmerged research Draft PR may eventually lose its original reachable Git ref if the branch is deleted.

RCP-001-C therefore creates a **byte-exact Git blob escrow**, not a handwritten copy: original source proof, executable oracle and independent tests from five exact research commits, and two frozen witness fixture JSON files from PR #466. Each escrow file is inserted into the infrastructure branch Git tree with the same already-existing Git blob object ID. The escrow bytes are part of the infrastructure PR's content and will remain reachable after integration of that branch into a retained Git history. Until the infrastructure branch is retained/merged, the same caveat applies to the escrow branch itself.

For a PR source n the deterministic escrow names are:

- `research/rcp/hyp105/archive/PRn/proof.md`
- `research/rcp/hyp105/archive/PRn/oracle.py.txt`
- `research/rcp/hyp105/archive/PRn/independent_test.py.txt`
- additional `archive/PR466/fixtures/*.json` for real frozen local witnesses

Archival oracle/test files are stored as `.py.txt`: they are verbatim byte copies, NOT imported into the executable research namespace or presented as additional scientific source modules. The original commit and path remain in each receipt.

## Exactly what is certified

**Byte identity, not mathematical proof.** The local verifier recomputes the *Git blob object SHA-1* on each escrow file from its bytes using Git's object header and compares it to the independently pinned original blob SHA. It additionally compares ordinary SHA-256 against **17 independently pinned digests** in `research/rcp/hyp105/sha256-pins.json`, computed from the first successful GitHub-hosted archive audit. Missing pins, altered digests or changed bytes fail closed. The generated index exports these SHA-256 values for future external deposition. These hashes establish exact byte identity with a pinned repository object; they do NOT establish that the proof is correct, that an oracle is independent, or that CI ran.

An optional GitHub-hosted read-only remote verifier also downloads each original source file at the **exact original commit** using the GitHub contents API, recomputes its Git blob object identity and compares it to the archive. This is independent evidence of original-to-escrow correspondence; no new mathematical theorem is implied.

The recorded replay commands deliberately say `COMMAND_DOCUMENTED_NOT_EXECUTED_BY_RCP_C`. A user may run the original tests after checking out the specified original commit. Source-code hashes and reproduction commands cannot substitute for executing a test.

## Registered evidence and falsifiers

Five evidence receipts link all seven initial RCP-001-B claims: JPKC-015 (#455), local-transfer (#466), EICE-003-K (#469), D6-AA4-N (#470), D6-AA4-O (#471).

Five no-go entries index:

1. Invalid general local P3-to-positive-GF5 transfer (restricted selected 18-incidence counterexample, **not** a global dense EICE or full-map S counterfamily).
2. Invalid proof from alleged scarcity of uniformly sampled original GQ clean anchors (the opposite marginal holds, whereas conditioned four-source physical templates remain open).
3. Invalid upgrade from forall g; E_f >= c to forall f,g >= c.
4. Invalid claim that exact swap-local optimum certifies global minimax of the B/A quintic.
5. Invalid upgrade from uniform (f,g) ensemble expected D6 to pointwise inf_(f,g) D6.

Each no-go identifies its rejected inference, precise witness/sample scope, mathematical basis, limits of what it **does not** refute, conditions under which a new approach may be tried, links to evidence receipts and claim IDs, and a backward compatibility reference to `KNOWN-AND-STOPPED-RESEARCH.json`. This complements, rather than replaces, the pre-existing anti-rediscovery records.

**No-go scope status is NOT a judicial declaration that its associated positive mathematical theorem is invalid.** It protects against a specific unjustified transfer.

## Commands (Python standard library, repo root)

```bash
python -m unittest research.test_rcp_evidence_ledger -v
python -m research.rcp.evidence_ledger --output /tmp/rcp001c
GITHUB_TOKEN=... python -m research.rcp.evidence_ledger \
  --verify-originals --output /tmp/rcp001c
```

Outputs `evidence.json` and `evidence.md` summarize the archived blobs, SHA-256 digests, linked claim IDs and no-go boundaries. The generation is deterministic for a pinned repository tree. These are derived outputs, not manually updated competing source records. GitHub-hosted CI validates both offline escrow integrity and optional remote original-source integrity. Additional independent adversarial cases verify missing, tampered, renamed and falsely upgraded evidence.

## Acceptance and limitations

- All archive paths and source SHA/ref/path/blob identities must agree, and all seven claims must have evidence receipts.
- Existing mathematical/review/novelty statuses are untouched: `DOCUMENTED_IN_DRAFT` and `NOT_REVIEWED`.
- No rooted Branch A/B/C acceptance, no all-label global lower, and no new ASET exponent is claimed.
- GitHub action artifact ZIP is a **convenience export only**, not an authoritative long-term archive. The Git tree is the anchor.
- RCP-001-C does not run the original five historical mathematical test suites or claim they are green at a newly created HEAD; those are separate source-workflow check histories.
- The GitHub archives only cover **selected initial proof and tests**, not all downstream dependencies from the extensive preexisting branch stacks. More certificates can be added incrementally.

Later: RCP-001-D live state and semantic research deltas; RCP-001-E automatic claim impact; RCP-001-F CI consolidation after equivalence tests; RCP-001-G source-to-merged integration provenance.
