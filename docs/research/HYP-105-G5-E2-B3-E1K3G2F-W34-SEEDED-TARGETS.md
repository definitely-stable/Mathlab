# HYP-105 E1-K3-G2-F — sound generic seven-family predicate and bounded W(3,4) source-pair completion

Date 2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked child of [Draft PR #378](https://github.com/definitely-stable/Mathlab/pull/378), pinned accepted exact parent `ef846731908b219320919b9a486519c442c4eba0`; parent Contract/INDEX/Research all SUCCESS. Main untouched; no merge.

**Scientific status:** a provably sound general-a accepted seven-family **STRUCTURAL** classifier for six distinct original W(3,s) incidences; a bounded seed-completion algorithm that emits only **genuine accepted positive GF5 targets**, a finite lower Hall certificate for W(3,4), and explicit complete/incomplete semantics. This DOES NOT prove exhaustive W34 accepted-S target counts, a finite NO-GO if search is truncated, `S_s=Omega(s^6)`, or an ASET exponent.

## 1. Genuine original six-column classification, no W32-only assumption

For a six-set I of DISTINCT original incidence columns `(p,l)`, compute physical left/right coordinate degrees from the single globally coherent injective `f,g` mapping. Each half must touch **exactly six physical coordinates**, all degree two, and the multiplicity partition of its ORIGINAL point/line endpoint IDs must be one of:

- A: `1+1+1+1+1+1` (six different original endpoints);
- B: `2+1+1+1+1` (one original endpoint used twice);
- C: `2+2+2` (three original endpoints used twice).

The true accepted seven-family tag is one of D6 (A/A with the SAME connected six-column dual C6), B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap or B/B-disjoint (the latter separated by the intersection of the repeated-original-factor column positions). Reject all other types or incomplete degree-two physical projections.

This is exactly the accepted classifier already used in B0 for W32, now written without any assumption `a=6` or `V=15`. Its class-specific certified strictly positive GF(5) full 51-palette floors `R3_CERTIFIED_FLOORS` were proven for the finite six-column templates independently of s. The new predicate only produces source incidence six-sets from one actual global map and uses no independently re-optimized physical labels.

## 2. Exact seeded completion: find actual targets with two retained ORIGINAL columns

For a Jcross witness w, reconstruct its actual five DIFFERENT original incidence column IDs `S(w)`, including its repeated original anchor. Choose a seed pair `{i,j} subset S(w)`. Enumerate only six-sets containing BOTH seed columns via an increasing-ID backtrack that appends exactly four further distinct original columns.

At each step reject immediately whenever:
- any original point or line appears more than twice;
- a physical coordinate has degree >2;
- a half has >6 distinct physical coordinates;
- the remaining number of columns is insufficient to complete six distinct physical coordinates or repair current degree-one coordinates.

At six distinct original columns, apply the EXACT seven-family classifier to both halves. Every accepted target has both seeds and therefore `|S(w) intersection target| >= 2`; each also carries the previously proven positive GF5 class floor. No proof uses an artificial full-R3-positive motif or repeated-original-column target. If unrestricted, this completion is exhaustive for **all six-sets containing its chosen seed pair**, because the remaining column IDs are enumerated in sorted order and all pruning tests are NECESSARY conditions for acceptance.

Execution uses explicit `max_nodes` and `max_targets` work budgets, both reported. On hitting either, mark the seed **INCOMPLETE**. Any absence of target under incomplete search is explicitly NOT an obstruction or counterexample; any discovered accepted target is nevertheless a certified actual positive six-family motif. Likewise, searching fewer than all ten seed pairs of one five-column witness is not a completeness certificate for its entire >=2-overlap neighborhood.

## 3. Positive-only Hall lower certificate, NOT an unjustified NO-GO

A deterministic bounded W(3,4) pilot selects an explicitly described SUBSET of Jcross witnesses, prioritizing the off-differentfoot-noncollinear heavy class. For each selected witness test a deterministic number of its ten two-column seed pairs, bounded by source-candidate and target budgets. Deduplicate the genuine accepted six-sets globally and build the original five-versus-six column overlap relation. Solve exact unit-capacity bipartite maxflow/mincut and independently construct a concrete injective assignment.

A FULL matching of the selected witnesses proves the corresponding finite source-to-positive-motif charge for that SUBSET. A failed matching or orphan with incomplete candidate searches is only **inconclusive**: more actual acceptable targets may remain unenumerated. Even fully covering all W34 Jcross witnesses in finitely many cases would not prove a universal all-h charging theorem.

## 4. Independent and exact acceptance oracles

- Compare generic structural classifier with accepted B0's independently tested classification on **every one of the 62,370** valid W32 left-2-factor candidate six-sets, for both lex and reverse-line; verify exact seven-family identities.
- Exhaustively enumerate W32 all completions around representatives of ALL SEVEN families with one fixed source-column seed pair and compare EXACT equality with the B0 exhaustive accepted six-set oracle. A seed search reported complete must have NO missed or surplus accepted source six-sets.
- On real W(3,4) lex and randomized coherent global physical maps, accept discovered targets only after reclassification and positive GF5 floor validation. Independently verify matching cardinality vs max-flow and source-column overlap, record explicit assignment SHA256. Finite sampled targets can be additionally tested with the actual signed 782-orbit exact GF5 oracle in the next validation slice.
- Apply independent physical coordinate relabelings on both halves (gauge) to check classification invariant; test that exhausted work budgets do not claim negative results.

GitHub-hosted path-limited Contract only; inherited Research and INDEX. No local/self-hosted runner. Keep Draft pending exact HEAD all three green CI and independent mathematical review.

## 5. Next proof gate E1-K3-G2-G

If bounded W34 search discovers only small positive sets, optimize using exact anchored physical two-factor closure joins and retain work budgets; DO NOT report unmatched selected witnesses as a scientific NO-GO. If it finds complete injections for selected W34 cases, inspect deterministic source→target mapping and identify a symbolic all-h positive motif extension preserving two original columns. Even a universal injection would at most yield `Jcross<=S_s`; establishing `S_s=Omega(s^6)` additionally requires a uniform lower bound on Jcross or a dichotomy yielding many accepted positives when Jcross is small. Branch A/B, full-R3 and the ASET exponent remain open.

## Exact GitHub-hosted results: closure-first search and W(3,4) positive injections

The original pilot [Contract #38210732248](https://github.com/definitely-stable/Mathlab/actions/runs/38210732248) proved the general-a predicate matches B0 across ALL 62,370 W32 left-eligible sixsets (both lex and reverse) and that fully uncapped fixed-seed W32 completions equal the exact B0 oracle. The *initial* W34 pilot used only 2 pair seeds and 20,000 candidate attempts per seed: selected heavy cross-source witnesses covered 1/6 (lex) and 5/6 (random). **These were incomplete searches; the unmatched counts were NOT counterexamples.**

An algorithmic refinement reorders, but **does not filter**, all possible further original incidence columns by descending number of physical coordinates already touched by the seed pair, then original ID. The resulting DFS remains exhaustive if uncapped: changing traversal order does not change the set of four-column completions. For deterministic W34 research pilots, each of 8 selected heavy-class witnesses now receives ALL 10 possible pairs of its 5 distinct original columns, with a 40,000-candidate-node budget and at most 12 targets per seed. This yields the following exact finite positive results from [Contract #38210896197](https://github.com/definitely-stable/Mathlab/actions/runs/38210896197):

| Coherent model | Entire Jcross | Heavy witnesses actually sampled | Genuine accepted S targets found | Distinct accepted target types | Capacity-1 matching |
|---|---:|---:|---:|---|---:|
| W(3,2) lex, small control | 36 | 6 | 58 | A/B; B/A; B/B; C/A; D6 | **6/6** |
| W(3,4) lex | 128 | 8 | **221** | 7 families represented | **8/8** |
| W(3,4) random(seed=20261012) | 75 | 8 | **249** | 6 families represented | **8/8** |

In both W34 runs, all 80 seed-pair searches reached one explicit work/target cap, so **none of those 80 candidate neighborhoods is fully enumerated**. This is deliberately a **positive-only existential certificate**: both eight-witness injections are reproducible and true, while no claim about absent additional targets, full W34 target counts, all 128 or 75 Jcross witnesses, or universal s is licensed.

Additional independent exact-head [Contract #38210952901](https://github.com/definitely-stable/Mathlab/actions/runs/38210952901) PASSED 6 tests, including three fixed REAL W34 six-original-column sets found by the first pilot, with DIRECT 782-dual-orbit GF5 counts over ALL TEN 3v3 sign patterns:

- lex: `(0,41,68,139,189,206)`, class `B-left/A-right`;
- random(seed=20261012): `(0,140,141,197,209,420)`, class `A-left/B-right`;
- random(seed=20261012): `(2,3,284,334,341,379)`, class `B/B-disjoint`.

The independently computed GF5 signed weights are strictly positive for all ten patterns in these cases, and their sum exceeds the accepted per-class 51-palette floor. These are true original W34 global f/g source labels, not standalone abstract templates.

**Scientific conclusion of K3-G2-F:** The candidate rule `>=2` shared original incidence columns now admits honest finite capacity-one injections for sampled W34 witnesses in two coherent physical maps. The result strengthens the finite W32 evidence but leaves the two universal proof obligations open: extend charging uniformly to **all** witnesses and **all** coherent f/g at each h, and derive `S_s=Omega(s^6)` rather than only a conditional `Jcross<=S_s`. No extrapolation from 8 sampled sources.
