# UCT-005 G4-A1–A3 — executable classical bridge and transfer firewalls

**Scientific status:** DERIVED_CLASSICAL / EXACT_FINITE_COUNTERMODELS / ROOT_OPEN_UNPROVED.
**Owner:** [UCT-005 G4 #234](https://github.com/definitely-stable/Mathlab/issues/234); parent [#105](https://github.com/definitely-stable/Mathlab/issues/105).
**Source baseline:** main fcd6c6a76c88e7d3e89adad0acbe10deb1063d0d (2026-10-10). Commit-based dates and historic PR statuses are contextual, not a dynamic status authority.
**Scope:** deterministic finite *total* transition systems, binary histories with fixed AS_OF pin sets, exact additive subset recovery over Z/qZ and small forward-edge DAGs. **Not** a Byzantine/authentication, crash/atomicity, source-probe, proof-size, page-I/O, randomized-sketch or DNA indel theorem.

## A1: future-observation equivalence and the invalid one-probe transfer

Let \(X\) be finite, \(\Sigma\) a nonempty public finite alphabet, \(T_a:X\to X\) total deterministic for each \(a\in\Sigma\), and \(O:X\to Y\) the named exact query output (a tuple for multiple queries).

Define \(x\sim_h y\) if and only if \(O(T_u(x))=O(T_u(y))\) for all words \(u\in\Sigma^{\le h}\). Equivalently, \(\sim_0=\ker O\), and
\[
x\sim_{h+1}y \iff O(x)=O(y)\ \land\
 \bigwedge_{a\in\Sigma}T_a(x)\sim_h T_a(y).
\]
The equivalence classes refine monotonically with \(h\). They are **not** generally transition-congruent at a fixed finite \(h\):
\(x\sim_{h+1}y\Rightarrow T_a(x)\sim_h T_a(y)\) is valid, but replacing the right-hand horizon by \(h+1\) needs another premise. Classical Myhill–Nerode/Moore refinement, not a novel theorem.

Assume a deterministic encoding \(c(x)=(h(x),\phi(x))\) with at most \(b\) trusted bits and \(m\) q-ary remote symbols; exact query and online update routines use **only** the encoded state and public operation, and each update changes at most \(w\) remote symbols (all trusted bits counted in \(b\)). For states reachable in \(\le d\) updates from \(x_0\), equal encodings imply future equivalence (induct under every public continuation), so
\[
|R_d(x_0)/\sim_h|\le 2^b V_q(m,dw),\quad
V_q(m,r)=\sum_{i=0}^{\min(m,r)}{m\choose i}(q-1)^i.
\]
The proof is a final-memory Hamming-ball counting argument: every reachable \(\phi(x)\) belongs to \(B_{dw}(\phi(x_0))\), and a trusted label contributes at most \(2^b\) choices. **This does not imply a stronger bounded-probe ROST estimate for future observations.**

### Explicit falsifier of an invalid ROST-A substitution

States are (u,v)∈{0,1}² stored in two distinct remote binary cells; legal publicly labelled operations are flip_u, flip_v, swap(u,v). The **single current query** reads only u (one fixed bit probe). Under the present-query signature there are K_present=2 classes. Under the all-words-of-length-at-most-one future signature there are K_future=4 classes because the observer may choose the paid swap first and then read u. (All states can be reached from 00 in two flips.)

The **incorrect** transfer keeping a future p=1,t=1 read budget would yield M=1 and \(K_\text{future}\le V_2(1,1)=2\), contradicted by 4. This does **not** refute immediate ROST, nor the weaker bound \(K_\text{future}\le V_2(2,4)=4\). The swap's remote reads and writes were not included in the one-probe budget. Exact source-of-error: treating legal continuation work as a free observation.

Two independent implementations are checked: horizon-by-horizon partition refinement vs complete enumeration of all public operation words (all total machines of 1–3 states, two operations, all Boolean observation maps, h=0..3). Tests also reject partial/invalid transition tables instead of quietly changing the contract.

## A2: exact historical-answer quotient; why epoch horizon is not retention entropy

For H independent writes of one binary data cell, a final fixed SET(0) equalizes the current state. An AS_OF pin set \(\Pi\subseteq \{0,\dots,H-1\}\) yields \(K_\Pi=2^{|\Pi|}\) distinct historical answer vectors, **if no further state-dependent archive/help is accessible without being charged**. Consequently exact deterministic storage accessible to the answering party needs at least \(|\Pi|\) bits. The counting proof is by injectivity of the signature map and pigeonhole.

With H=5 and all five pins, K=32. With only pins {0,4}, K=4. This explicitly defeats the false extrapolation that two fixed pinned epochs necessarily require \(\Omega(H)\) bits as H grows. Metadata identifying the epochs, all charged client input and root/version descriptions must be included in any real physical/cryptographic implementation.

This proves no physical page lower bound, no fresh latest guarantee and no authenticated per-epoch proof complexity. F1 #223/#235 remain the sole owners of priced historical PIN/GC model research.

## A3: DAG provenance semiring versus GF(2) cancellation

Let G be the four-vertex forward-edge DAG with edges (s,a), (a,t), (s,b), (b,t).
Exactly two source→target paths exist. Counting paths in natural numbers returns 2;
reducing path count modulo 2 returns 0; Boolean reachability is TRUE.

An independently implemented directed graph traversal computes Boolean reachability; a separate forward topological dynamic program counts paths in integers. All forward-edge DAGs up to n=5 (2^{10} edge-subsets for n=5) are checked for equivalence between positive integer path count and Boolean reachability; a specific diamond graph certifies the failure of mod-2 equivalence.

Sufficient abstract algebraic preservation condition: a zerosumfree semiring without zero divisors maps a finite sum of path products of nonzero edge weights to nonzero **iff** a path exists. In GF(2), 1+1=0; in GF(5), 1+(-1)=0. Arbitrary field-valued path sums therefore do not preserve Boolean existence. This is a classic semiring support observation (PODS provenance LIT-252); it is not a new bridge from HYP-105 GF(5) signed trades to certified negative reachability.

## Robust sparse-subset-sum feasibility, scoped to ASET

Fix q=5, d≥1, distinct legal subsets of columns with cardinality ≤d **including the empty subset**. Suppose every nonempty column has Hamming support ≤w, and all distinct subset-sum encodings have distance ≥2e+1 (so up to e adversarial *symbol substitutions* are corrected). Empty versus singleton requires weight(column)≥2e+1, hence **w≥2e+1**. For w=4 and e≥2 no nonempty column family exists; that capacity is zero. For e=1 the weight-3 disjoint-support block construction supplies \(\lfloor m/3\rfloor\) columns and min subset-sum distance 3 for d=3 (indeed for any d).

Tests enumerate all single columns over Z/2Z and Z/5Z at m≤4 to reject e=2; compare pairwise Hamming distance to independent complete corruption-ball intersection for q≤3,m≤3,e≤1; test disjoint construction n≤4 at q=5.

**Do not transfer to** GF5 scalar-linear independence, channel indels, erasures, approximate sketches, or historical cryptographic integrity. The e=1 extremal capacity and original HYP-105 exponent remain OPEN.

## Typed bridge register

| Source → destination | Edge type | Exact preservation | Non-transfer / falsifier |
|---|---|---|---|
| Myhill–Nerode/Moore → G4 A1 | CLASSICAL_DIRECT | Exact deterministic *total* operations; all future named queries, matched horizon | Fixed-h quotient not generally transition-congruent |
| LENT/UCT-001/ROST Hamming ball → A1 | CLASSICAL_INGREDIENT | Bounded remote *symbol changes*, exact encoded updater, no free state-dependent helper | Does not preserve ROST bounded **current** probe budget; two-bit paid swap |
| Historical observation quotient → A2 | CLASSICAL_DIRECT | Fixed pin-query family and charged side information | Two pins do not imply Ω(H) information for H elapsed epochs |
| Signed subset sums → one-error ASET gate | CLASSICAL_DIRECT | Empty/singleton included, Hamming substitution channel, column support w | For w=4,e≥2 impossible; e=1 still unsolved asymptotically |
| Integer path counts → DAG Boolean reachability | DIRECT_FINITE_FOR_NONNEGATIVE_INTEGER_WEIGHTS | Forward DAG, positive integer path counts | GF2 evaluation cancels two paths; GF5 can cancel signed weights |
| Future quotient → F1 PIN/GC | REDUCTION_REQUIRED | Must add paid author updates, independently pinned roots, malicious server, authenticated latest anchor, physical pages | No transfer of query/proof/GC bounds yet |
| TKG semiring provenance → GF5 signed flows | REDUCTION_REQUIRED | Need a proven query-predicate-preserving semiring map and update semantics | Zero-sum cancellation prevents universal Boolean support |
| INDEX physical compressed recourse → F1 | REDUCTION_REQUIRED | Same allocator, pages, RAM, versions, query contract, adversarial model | Raw/indirection and fully trusted replica are countermodels to naive universal transfer |

**Novelty gate:** these are elementary/known restricted constructions and falsifiers. They do not establish UCT-005's original multi-resource Pareto frontier; no source full-proof audit, no signed cryptographic theorem, no physical SSD claims.

## Reproducibility

- Script: \`python research/uct005_g4_bridge_oracles.py\`
- Independent tests: \`python -m unittest discover -s research -p 'test_uct005_g4_bridge_oracles.py' -v\`
- GitHub-hosted workflow: \`.github/workflows/uct005-g4-bridge-oracles.yml\` (ubuntu-latest, Python 3.x).
- The root \`research\` workflow already discovers \`test_*.py\`; neither it nor the F1 workflow must be modified.

**Next slice:** only after independent hosted tests, implement a fully charged time-expanded F1 model and propose one falsifiable **nonfactorizing** bound or explicit STOP via #223. Research completeness of this atlas is not theorem novelty.


## Typed machine-readable bridge atlas (G4-B0)

The companion [G4 typed bridge register](UCT-005-G4-TYPED-BRIDGES.json) enumerates **16** scoped links across UCT/ROST, LENT/ASET, HYP-105, provenance/DAG, TKG, INDEX, TOM, incremental hashing, DeltaMeter, DNA channels and F1 verification. **This is 16 documented edges, NOT 16 independently proved reductions.** Only the records classified CLASSICAL_DIRECT or PROOF_INGREDIENT assert restricted, classical derivations; COUNTERMODEL records explicitly block invalid arrows; REDUCTION_REQUIRED and APPLICATION_ONLY remain unproved.

A separate fail-closed test \`research/test_uct005_g4_bridge_register.py\` rejects unknown type values, absent preconditions, duplicate IDs, blank resource mappings, and promotion of an unproved REDUCTION_REQUIRED edge to CLASSICAL_DIRECT without separately changing its acceptance contract. This is **registry hygiene**, not machine-verification of a proof. Scientific advancement of an edge requires source theorem assumptions, an independently audited reduction and preservation of security/error/resource units; textual classification alone cannot establish it.

The hosted workflow now discovers both \`test_uct005_g4_bridge_oracles.py\` and \`test_uct005_g4_bridge_register.py\`. The repository's general Research CI discovers all \`test_*.py\`.


## Additional scope falsifiers — fixed horizon and DNA indels

**Finite-horizon noncongruence:** X={0,1,2}, O=(0,0,1), one total operation T=(2,1,2). At horizon 0, states 0 and 1 are indistinguishable; after T their outputs differ (1 versus 0). Therefore the fixed-h equivalence relation is not automatically transition invariant. The independent future-trace oracle also checks all small-machine refinement equations.

**DNA one-deletion counterexample:** two length-six words \`ACACAC\` and \`CACACA\` have Hamming distance **6**, yet deletion of the initial A from the former and deletion of the final A from the latter both produce the five-symbol observation \`CACAC\`. Their one-deletion corruption balls intersect, so even a pair of words with this large Hamming separation is **not** a one-deletion-correcting code. This is an elementary edit-channel counterexample, not a biological experiment or a new DNA code theorem.

Both are now tested independently; the original 11 finite tests expand to **13** finite checks (in addition to 3 register-schema checks). GitHub-hosted acceptance must target the latest commit, not a previously successful run.
