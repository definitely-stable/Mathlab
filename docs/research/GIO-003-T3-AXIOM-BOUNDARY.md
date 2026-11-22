# GIO-001.3 / G6-A — incidence-axiom boundary, exact projection defects and independent falsifiers

**Parent:** [#793](https://github.com/definitely-stable/Mathlab/issues/793); **meta:** [#790](https://github.com/definitely-stable/Mathlab/issues/790). **Frozen main base:** `f42aa108a2f9e15dadebf5c45fa4923cc435742b` (postmerged #799/T1+T2, #798/resilience). All changes are additive in a narrow branch. The present claim is **PROVED_RESTRICTED_AXIOM_BOUNDARY**, not the full T3 abstract six-motif obstruction and not new ASET growth.

## 1. Separate exactly what GQ contributed

The accepted [T1/T2 proof](GIO-003-GENERALIZED-INCIDENCE.md) works in the **actual** original flag model. It uses two distinct kinds of input:
1. Geometric facts proved via GQ: source sizes and bidegrees, no four-/six-cycles in the *source* incidence graph, unique full-geometry projections with literal three original anchors, bounded original point/line collinearity and mixed source books.
2. Analytic/physical facts: independent typed pair-injective labels, two real physical diagonals per source flag, unique physical-edge owner, conflict graph `J`, Caro–Wei heavy harvest, two global cuts, published ordinary graph `C6` supersaturation, one common LOW owner selector, moment/endpoint/book bounds and injective original `C6` / at-most-two-to-one produced BBo inverses.

Replacing GQ by a source graph with `N=Theta(r^4)`, `|P|,|L|=Theta(r^3)` and degrees `Theta(r)` is **not** a theorem: the projection and inverse gates below must still be paid. A generic spectral statement alone also does not imply them.

## 2. PROVED: girth-eight makes multi-projection impossible

A finite *simple* typed incidence system is a bipartite graph on points `P` and lines `L` with no duplicate original flags. A three-flag projection for a nonincident pair `(q,R)` is
`(q,E), (p,E), (p,R)`, with `q != p`, `E != R`, all flags real.

**Lemma U (at most one projection).** If the incidence graph has girth at least eight (no cycles of length four or six), every nonincident pair has *at most* one three-flag projection.

**Proof.** Let two distinct simple three-edge paths connect `q` and `R`. If their internal point or internal line agrees, their union contains a four-cycle (or the two paths coincide). Otherwise, the union is a simple six-cycle. Either contradicts the girth hypothesis. No regularity or GQ spectrum is used.

**Explicit converse falsifier for a proposed bounded-multiplicity extension.** Take three points `0,1,2` and three lines `{0,1},{1,2},{0,2}`. There are no four-cycles, but for every point and its opposite line there are **two** projections and a literal incidence six-cycle. Thus `multiplicity <= 2` is *not* a weakening compatible with retaining source girth-eight. Allowing genuine multi-projection requires new treatment of six-cycles and the historical six-ID inverse; simply selecting the first projection is not a valid carry-over of #799.

## 3. PROVED: Moore saturation recovers all GQ projections

**Lemma M (rigidity of the exact regular envelope).** Suppose `s,t>=1` are integers, every point has incidence degree `t+1`, every line has `s+1` points, girth is at least eight, and
`|P|=(s+1)(st+1)`, `|L|=(t+1)(st+1)`.
Then every nonincident point-line pair admits exactly one three-flag projection; with the usual thickness `s,t>=2`, this is exactly the GQ incidence axiom.

**Proof.** Fix point `q`. Its `t+1` incident lines have `s` other points each. The absence of four-cycles makes the resulting `s(t+1)` points distinct. From each, `t` other lines are available. If two resulting paths reached the same line `R`, they would make a four- or six-cycle; hence the `st(t+1)` endpoints are all different and nonincident with `q`. But `|L|-(t+1)=st(t+1)`. All nonincident lines must therefore be attained exactly once. No geometry-specific SRG theorem is assumed.

**Critical consequence.** Keeping *all* exact GQ vertex counts, point/line biregularity and girth-eight does **not** enlarge the mathematical class. A claimed T3 based on those assumptions would only restate T1/T2 in abstract syntax. Actual generalization must weaken at least one of exact size, bidegree, full projection coverage or girth. Merely weakening characteristic/field is already done by #799.

## 4. PROVED: universal selected-projection deletion lemma

Let `D` be an arbitrary set of nonincident source point-line pairs with a fixed, **single chosen real projection** `pi(q,R)` consisting of three distinct existing flags for each pair in `D`. It may be partial; if the graph has six-cycles, the selected projection is a *choice*, not an assertion that the historical BBo inverse remains valid.

Let `U=(P x L)\(I union D)` be the missing-projection set, and for flag `e` define
`load_pi(e)=|{(q,R) in D: e is one of pi(q,R)'s three flags}|`.
Write `Lambda=max_e load_pi(e)`.

For any **adversarial** original flag deletion `Z subset I` (including a deletion chosen after the labels and projection selector), the pairs invalidated by the selected anchors satisfy

`|{u in D: pi(u) intersects Z}| <= sum_(e in Z) load_pi(e) <= Lambda |Z|`.

Therefore, if `|U|<=E r^5`, `Lambda<=L r^2`, and `|Z|<=rho r^4`, the *missing plus newly damaged* endpoints total at most

`E r^5 + L rho r^6`.

For complete independently pair-injective 2-symbol typed maps `f,g`, there are four distinct oriented off-coordinate physical endpoint representatives per original `(q,R)`; the corresponding projected endpoint budget is at most

`4E r^5 + 4L rho r^6`.

**Proof:** the damaged set is the union over deleted flags of their inverse projection fibres. Union bound gives the inequality, with no independent deletion, no random labeling and no use of GQ spectrum. Fourfold lifting uses the *original map injection*, not arbitrary coordinate re-use. These are exact deterministic statements, but they **do not** imply the full T3 `Omega(r^6)` motif bound: physical proper paths, original six-ID inverses and subleading mixed-book moments remain separate proof obligations.

For genuine GQ(s,t), the selected full projection has exact `load_pi(e)=3st` for **every** original flag, so the lemma specializes to `12st|Z|`, exactly matching #799.

## 5. Two independent stress constructions

### C1: disjoint double of a true GQ

Take two disjoint copies of any genuine GQ(s,t), including all point and line vertices. This retains simple incidence, **the same bidegrees** and girth-eight, and has
`|P|=2V_P`, `|L|=2V_L`, `N=2(s+1)(t+1)(st+1)=Theta_b(r^4)`.
The pair-label alphabets would still have product `Theta_b(r^3)`, but independent conflict/spectral and motif-inverse bounds are not claimed.

Every across-component point/line pair has no three-edge projection. Exactly
`2V_P V_L=2(s+1)(t+1)(st+1)^2=Theta_b(r^6)`
nonincident pairs are missing. For equal orders, the fraction of all nonincident pairs with missing projection tends to **1/2**. Thus bidegree bounds, scale, linearity, and girth-eight by themselves do **not** give the needed `O_b(r^5)` exceptional-endpoint budget. This is a counterexample **to that proposed implication**, not a counterexample to the historical motif bound.

### C2: puncture one actual GQ flag

Remove a single incidence `e=(p,R)` while preserving all point/line vertices and all other named incidences. The source ceases to be bidegree-regular / GQ but retains girth-eight. The original nonincident pairs that lose their unique three-flag projection number exactly `3st` by the exact per-flag load. In addition, the formerly incident pair `(p,R)` becomes nonincident without any surviving projection: a new path would require a second line through `p` and a distinct point of `R`, contradicting original GQ linearity. Thus the new projection defect is **exactly `3st+1`**. This gives a genuine finite-family *near-GQ but non-GQ* source example with sparse defects, though its resilient motif theorem already follows from #793 by treating the missing flag as a deletion. Do **not** present it as an independently new obstruction theorem.

## 6. Real T3 hypothesis/dependency DAG (not silently completed)

| Gate | Candidate abstract obligation | Current outcome |
|---|---|---|
| A0 | `N=Theta(r^4)`, `|P|,|L|=Theta(r^3)`; minimal injective typed pair labels | needs family assumptions |
| A1 | original conflict `e(J)=O(r^4)`, suitable fibre/Gram bounds | not implied by A0/girth |
| A2 | real two-diagonal owner lift, GQ-source-free `C6 -> original D6` inverse | not generalized yet |
| A3 | selected partial original three-flag projection with defect `O(r^5)`, max flag load `O(r^2)` | **deletion lemma proved here**; not inferred from size/girth |
| A4 | one shared LOW priority/cut selector, proper walk and tr(A)^4/tr(A)^6 moments | inherited only in GQ scope |
| A5 | mixed FULL/CORE source books and inner-error `o(r^6)` | major unproved abstract input |
| A6 | bounded original 3path to **produced aligned historical BBo six-ID** inverse | new source compatibility proof required |
| A7 | quantified HEAVY/LOW constants chosen before maps, deletions and order | follows only if A0–A6 are proved with correct constants |

**Next permissible mathematical slice:** G6-B should seek a genuinely sufficient non-GQ assumption set for A1, A2, A4, A5 and A6, or an exact counterexample to a proposed missing implication. A non-GQ partial-geometry `pg(s,t,alpha>1)` permits multiple projections and so entails source six-cycles; historical BBo templates cannot be transported without rederivation.

## 7. Independent evidence, prior art, and acceptance boundary

`research/gio_t3_axiom_boundary.py` is a stand-alone **incidence-first** oracle. It does not call `structure()`, `strongly_regular_data()`, or source/physical motif classification to certify the new lemmas. It checks every (point,line) pair and every possible joining foot. A separate test oracle enumerates all literal length-three source walks, and a second deletion oracle inverts the flag-to-endpoint relation. Genuine cases: W(3,2), W(3,3), Q^-(5,2) as GQ(2,4), and its dual GQ(4,2). Each is also doubled and single-flag-punctured; a literal incidence hexagon proves the multiplicity failure. Certificate: `mathlab.gio003.t3-axiom-boundary.v1`.

The notions of partial geometries, generalized quadrangles, incidence girth and Moore bounds are **classical prior art**. References: [partial geometries and GQ = pg(s,t,1)](https://cage.ugent.be/~fdc/intensivecourse2/haemers_extensie.pdf); [incidence graphs and bipartite Moore graphs](https://discretemath.imp.fu-berlin.de/DMIII-2019/finite_geometry.pdf). These lemmas are a *scoped dependency audit and exact failure boundary*, not a priority claim of novel graph theory. The existing GQ-specific scientific proof remains unchanged.

**Acceptance classification:** independently proved restricted combinatorial lemmas with exact finite counterexamples, subject to PR-head GitHub-hosted specialist, INDEX and Research. **T3 remains OPEN**; no universal abstract `Omega(r^6)` established; no new ASET exponent; no external human referee or Lean proof; no main merge in this slice. All example numerical constants are exact combinatorics, not assumed published supersaturation constants.
