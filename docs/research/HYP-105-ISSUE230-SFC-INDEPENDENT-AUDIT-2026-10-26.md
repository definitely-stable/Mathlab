# HYP-105 / #230: independent SFC audit and middle/end posting bound

Date: 2026-10-26. Audited baseline: `e32d42f9b98d978387fa20b22ce6a6ff1d81a8c7`, the current scientific Draft PR #648 source. This is an independent derivation and finite falsification exercise within the same agent session, **not an independent qualified human mathematical referee**. Root status remains **OPEN_WITH_FORMAL_BLOCKER**.

## Repository and issue reconciliation

The existing local clean PR #648 branch was fast-forwarded by nine commits from `26001265` to the baseline above. Previously untracked `AGENTS.md` and `sites/` were preserved. The older PR #647 branch remains available, and `main` stays at `89c8a4988881da26af514591584fcc8e43071a83`.

The latest issue [#230 SFC update](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6400542033) requests separate control of shared-one-flag and disjoint-six-flag collisions. The issue still quantifies over **all** correlated fixed maps. The latest seven PR descriptions (#642–648) were examined: the existential/random-orbit conclusions in #642/#644 cannot establish that universal infimum; #643's displaced-flux narrative supplies no coupled six-motif inequality. Drafts #645–647 acknowledge blockers but retain stale numerical/path-universe claims. The [#647 discussion](https://github.com/definitely-stable/Mathlab/pull/647#issuecomment-6398168756) explicitly points to narrow [#648](https://github.com/definitely-stable/Mathlab/pull/648). Accordingly this continuation uses the corrected #648 source model, where the W(3,4) projected witness value is 5261 and the rejected auxiliary floor 5768 is not reused. This is not a Branch B counterexample or a global minimum claim.

Live GitHub Actions queries for **exact baseline SHA** found all three runs completed successfully: [Research #40214446504](https://github.com/definitely-stable/Mathlab/actions/runs/40214446504), [specialized #40214446520](https://github.com/definitely-stable/Mathlab/actions/runs/40214446520), and [INDEX #40214446489](https://github.com/definitely-stable/Mathlab/actions/runs/40214446489). Those results apply to the baseline, not the subsequent local changes. The #648 comments/review timeline returned no entries; CI does not supply a qualified proof review.

## Audited claims

The [SFC reversal-orbit lemma](HYP-105-SIXFLAG-PATH-COLLISIONS.md) is sound under its stated properness and typed global injection assumptions. In each coordinate projection a proper path is a simple three-edge path; two such paths with the same endpoint pair sharing two edges must coincide. Both coordinate paths are therefore fixed by two shared source flags. Their positional pairing determines the third source flag; the only two directed realizations of a source-flag triple are full reversals. Thus distinct reversal-orbits at the same original nonincident endpoint share at most one original flag, and

\[
Q=2P+8(C_0+C_1),\qquad
C_1=\sum_{q,r,\alpha}\binom{m_\alpha(q,r)}2
\]

follow. The argument concerns original incidence IDs, not accepted GF(5) six-incidence classes.

## New deterministic posting split

Retain the SFC definitions for every \(s=2^h\), \(h\ge1\), and all legal correlated complete injections. Fix an original nonincident endpoint \((q,r)\) and an original source flag \(\alpha=(p,l)\). In a proper coordinate three-path, its middle edge is disjoint from the endpoint coordinate pair and each end edge meets that pair in exactly one coordinate. Consequently:

- If \(f(p)\cap f(q)=g(l)\cap g(r)=\varnothing\), every occurrence of \(\alpha\) is in the middle.
- If both intersections have size one, every occurrence is at an end.
- Otherwise its posting occupancy is zero. In particular, source point/line equality gives no proper occurrence.

These sectors are disjoint for a fixed posting. Define \(C_{1,\mathrm{mid}}\) and \(C_{1,\mathrm{end}}\) by restricting the exact posting formula accordingly. Then \(C_1=C_{1,\mathrm{mid}}+C_{1,\mathrm{end}}\).

### Uniform middle occupancy: \(m_\alpha(q,r)\le4\)

Write \(f(q)=\{A,B\}\), \(f(p)=\{C,D\}\), with all four symbols distinct. The outer source point IDs must be among the at most four occupied crossedges \(AC,AD,BC,BD\). Likewise there are at most four outer source line IDs from the crossedges between \(g(r)\) and \(g(l)\). Each middle orbit uses two outer source incidences. These incidences determine one another by complementing the crossedge on both sides, so different middle orbits use disjoint pairs of outer incidences.

The bipartite original source incidence graph induced on these at most four points and four lines has at most eight edges. Indeed, a forest has at most seven edges. Otherwise source girth eight forces a cycle of length eight, using every available vertex; any additional edge is a chord and creates a four- or six-cycle. Hence \(2m_\alpha(q,r)\le8\). Missing coordinate labels only remove vertices or incidences. Source girth eight follows from the classical symplectic GQ axiom, with an explicit all-h proof in [B1.0](HYP-105-G5-C3-B1-0-SYMPLECTIC-GF4.md), section 1; it is not inferred from finite GF(2)/GF(4) checks.

Every reversal-orbit has exactly one middle flag, giving

\[
\sum_{\mathrm{mid}}m_\alpha(q,r)=P/2,\qquad
\boxed{C_{1,\mathrm{mid}}\le\tfrac34P.}
\]

This is unconditional; \(C_{1,\mathrm{mid}}=O(s^6)\) would follow **conditionally** from a separate \(P=O(s^6)\) theorem, which is still unavailable.

### Exact end occupancy and remaining obstruction

For an end posting let \(v_0\) be the corner made of the two unique shared coordinates, \(v_1\) the opposite corner of the flag rectangle, and \(v_3\) the opposite corner of the endpoint rectangle. Orient every orbit so \(\alpha\) is first. Its only free corner is \(v_2\). Thus its occupancy is exactly the number of

\[
v_2\in\Gamma_H(v_1)\cap\Gamma_H(v_3)
\]

for which all four first coordinates, and all four second coordinates, are distinct. The end posting is a proper common-neighbor count; it need not satisfy the middle constant bound. Since \(v_0\in\Gamma_H(v_1)\) and properness excludes \(v_0\),

\[
m_\alpha(q,r)\le\min\{\deg_H(v_1)-1,\deg_H(v_3)\}\le\Delta_H-1.
\]

There are exactly two end-flag appearances per orbit, so \(\sum_{\mathrm{end}}m=P\). Consequently

\[
\boxed{C_{1,\mathrm{end}}\le\tfrac12(\Delta_H-2)P,\quad
C_1\le\left(\tfrac12\Delta_H-\tfrac14\right)P.}
\]

If \(P=0\), all quantities vanish. If \(P>0\), some proper path exists, hence \(\Delta_H\ge2\). The already established [AA4-DEG bound](HYP-105-PHYSICAL-DEGREE-ENERGY.md) gives \(\Delta_H=O(s^2)\), leaving only \(C_1=O(s^2P)\). Even assuming \(P=O(s^6)\), this yields \(O(s^8)\), too weak for the required \(O(s^6)\). This is a limitation of this upper bound, not a counterexample to a better theorem.

## Executed independent finite checks

Command `python -m unittest discover -s research -p test_hyp105_sixflag_pair_collision.py` at baseline: **4 tests passed** in 1.885 seconds.

A separate Python 3.13 stdin program reconstructed the physical graph from genuine original flags, enumerated directed paths and compressed actual vertex-sequence reversals, without calling the SFC census. For every nonzero posting it separately reconstructed the sixteen possible middle placements or the proper common-neighbor end join; both matched the posting count exactly. It checked all position classifications and the bounds above. The output was:

| Genuine source/map | P | Middle appearances | End appearances | C1 middle | C1 end | max middle | max end |
|---|---:|---:|---:|---:|---:|---:|---:|
| W(3,2), seed 41 | 986 | 493 | 986 | 53 | 201 | 3 | 4 |
| W(3,2), seed 91 | 860 | 430 | 860 | 45 | 126 | 3 | 3 |
| W(3,4), explicit certificate | 58730 | 29365 | 58730 | 240 | 8805 | 3 | 4 |

The independent stdin check also exhausted all 256 unions of complementary edge pairs in a 4-by-4 original incidence model. Rejecting four- and six-cycles left the histogram `{0: 1, 1: 8, 2: 24, 3: 32, 4: 8}` by number of complete pairs; maximum **4**. This checks the combinatorial cap, not realizability of every such matrix in a particular GQ. The branch test now persists this exhaustive falsifier using independent breadth-first alternate-path cycle checks. The census also verifies each observed middle posting by direct placement and each end posting by a proper common-neighbor join. The three independently obtained rows above are frozen as regressions.

In the supplied W(3,4) witness, end postings account for 8805/9045 shared-one collisions. No asymptotic inference follows from that single finite witness.

## Source pinning and next proof gate

Baseline SHA-256 hashes of exact Git blob bytes (LF), before the follow-up implementation. The run record separately hashes executed Windows checkout bytes, whose CRLF line endings differ:

| Source | SHA-256 |
|---|---|
| `docs/research/HYP-105-SIXFLAG-PATH-COLLISIONS.md` | `4ad305a5acb45fa2b0ec4b12695bf6ac770c97c95fd08acdb26c61a2ade522cc` |
| `research/hyp105_sixflag_pair_collision.py` | `bd2d9e1e4a28ebb1d0803fe0b5eb9b23d0b364f0bcead8da83bcda957598882c` |
| `docs/research/HYP-105-PHYSICAL-DEGREE-ENERGY.md` | `fe0b97847993f7368cea36d5690b1351cee960f5b6d7528db7131bd8aa0debfc` |
| `research/hyp105_b1_symplectic.py` | `62d4e274e7ed7772d892f18aaa3d0852cfe7a2c36687b23f2ba48910afb292f1` |
| `research/hyp105_w34_adversarial_certificate.json` | `792b10d997b831b1c6f2e53df2ceff5dfdb604c2b23edb22350f56bf408101af` |

Next target: directly bound the aggregate proper endpoint codegree collision energy \(C_{1,\mathrm{end}}\), retaining the same original nonincident endpoint conditioning and the same correlated maps. In parallel the six-distinct-flag sector \(C_0\), upper/lower control of \(P\), and transfer to seven GF(5)-accepted source sixsets remain independent open requirements. Stop any attempted root promotion if a step substitutes an unweighted endpoint fraction, assumes independent labels, or identifies candidate six-flag path pairs with accepted GF(5) motifs without proof.

The reproducible [local run record](../../research/hyp105_issue230_sfc_occupancy_run_20261026.json) records source hashes, exact commands, model-identifier availability, outputs and local checks. Mathlab MCP tools were absent, so live Mathlab reporting could not be delivered. No custom connection or production identity was created.

Local continuation validation: **37 tests passed** across the six related invariant, certificate, endpoint, variance, degree-energy and SFC suites, including the two new posting/cycle falsifiers. `research/catalog.py --check`, `research/known_registry.py --check`, `research/literature.py --check` and `git diff --check` all returned exit code 0. The run record preserves their actual outputs. New logic stays in the existing census; callers, certificate fixtures and hosted workflow commands remain compatible. No new dependency, scientific catalog promotion or site update was needed.

No full repository suite, hosted CI for the new local diff, Lean formalization, or qualified external referee was supplied by this audit; no publication or scientific acceptance field was changed.
