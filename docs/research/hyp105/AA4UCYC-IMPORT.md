# HYP-105 / RCP-AA4-U-CYC — exact original-line D6 pair gluing

Research source: [scientific Draft PR #487](https://github.com/definitely-stable/Mathlab/pull/487), exact pinned source commit [1502844a49cea1631206b2b68144c65f879fc4c0](https://github.com/definitely-stable/Mathlab/commit/1502844a49cea1631206b2b68144c65f879fc4c0). Scientific root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains open; provenance infrastructure is tracked under [#474](https://github.com/definitely-stable/Mathlab/issues/474).

## Claim 1 — exact all-h conditional D6 pair kernel

For genuine original \(W(3,s)\), \(s=2^h\) with \(h\ge1\), fix a **single complete globally injected** source-point map \(f\) and two genuine six-distinct-original-incidence sets \(Q_0,Q_1\), each with six different original points and lines and an accepted connected left-side physical \(C_6\). Let \(r=|L(Q_0)\cap L(Q_1)|\) be the number of actual ORIGINAL source-line factors shared by both sets and let \(\tau\) be the canonical cyclic source-line gluing signature. A **single** uniformly random complete globally injected source-line map \(g\) is used for both events, rather than independently generated labels per sixset.

\[
\boxed{
\Pr_g[D_6(Q_0)\land D_6(Q_1)\mid f,Q_0,Q_1]
=\frac{(a)_6}{(K)_{12-r}}\sum_{k=0}^6 c_{\tau,k}(a-6)_k,
\quad K=\binom a2.
}
\]

The coefficients \(c_{\tau,k}\) count **nonnegative integer** canonical second-cycle physical-coordinate assignments with exactly \(k\) fresh colors, satisfying equality of physical pair labels on each genuinely shared source line and distinctness across all nonshared source line factors. The source's 13,327 canonical assignments form an alphabet-independent finite enumeration. This is a conditional probability / expected joint indicator identity, not a deterministic D6 count lower.

The valid gluing signature \(\tau\), not the overlap cardinality \(r\) alone, determines the answer. At \(r=6\), identical cyclic edge adjacency makes the two events identical while distinct adjacency makes their intersection impossible. Genuine \(r=2\) examples can likewise be compatible with strictly positive joint probability or incompatible with probability exactly zero. This is recorded separately as `HYP105-NG-AA4UCYC-OVERLAP-SIZE-INSUFFICIENT`.

## Claim 2 — finite true W(3,2) anchored row, NOT full second moment

For the **single finite** original \(W(3,2)\), frozen complete source-point mappings S68/S72, and the same fixed true original six-incidence anchor \(Q_0=(0,5,7,10,13,39)\), the source gives:

| Finite genuine-original object | Exact source count |
|---|---:|
| Candidate ORIGINAL left-connected \(C_6\) sixsets \(Q_1\) | 21,186 |
| Canonical original-line-cycle signatures | 112 |
| Positive joint \(D_6(Q_0)\land D_6(Q_1)\) probabilities | 6,192 |
| Zero joint probabilities | 14,994 |
| Anchored probability sum over all \(Q_1\) | \(19457/10810800\) |
| \(\mathbb E_g[D_6\mid D_6(Q_0),f]\) | \(19457/2160\) |

The anchored row is **one of the 21,186 rows** in the full pair matrix. It is **not** \(\mathbb E_g[D_6(f,g)^2]\), not a global conditional variance, and not an infinite family of adversarial global maps. The preceding scientific PR #485 supplies the disjoint-line sector; the current source #487 handles overlapping original lines without treating same-\(r\) signatures as identical. Its original finite source witness is retained, but the catalog import does not rerun its extensive genuine-source oracle.

## Registered provenance and regeneration

Two registered claims: `HYP105-AA4UCYC-SHARED-LINE-D6-KERNEL` (all-h conditional expectation of joint indicators) and `HYP105-AA4UCYC-W32-ANCHORED-ROW` (finite \(h=1\) only). Both remain `DOCUMENTED_IN_DRAFT`, `NOT_REVIEWED`, `NOT_ASSESSED` and `ROOT_BRANCHES_OPEN`.

Archive with exact Git blob SHA and independently calculated SHA-256:

- `research/rcp/hyp105/archive/PR487/proof.md` — original source proof.
- `research/rcp/hyp105/archive/PR487/oracle.py.txt` — original cyclic gluing oracle.
- `research/rcp/hyp105/archive/PR487/independent_test.py.txt` — original genuine source and brute-force tests.

Receipt `HYP105-EV-AA4UCYC.json` contains exact origin file paths, source commit, SHA-1 object IDs and documented original GitHub-hosted test command. Independent SHA-256 pins are in `research/rcp/hyp105/sha256-pins.json`. Formulas `HYP105-F-027` through `HYP105-F-029` and all claims/no-go are deterministically rendered into five committed Git-versioned Markdown files (`RESULTS.md`, `FORMULAS.md`, `PROOF-GRAPH.md`, `PROTOCOLS.md`, `RESEARCH-MATRIX.md`).

~~~bash
python -m unittest research.test_rcp_aa4ucyc_import -v
python -m research.rcp.structured_docs --check
python -m research.rcp.evidence_ledger --output /tmp/aa4ucyc-provenance
~~~

Research root #230 is NOT settled by the source result, even if source CI or archive CI succeeds. Mathematical acceptance and novelty assessment are separate from byte-level/source-provenance validation.
