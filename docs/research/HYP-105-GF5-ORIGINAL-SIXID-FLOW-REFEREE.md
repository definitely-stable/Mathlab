# HYP-105 / #230 — AA4-GF5REF: independent 51-palette GF(5) source-six-ID acceptance referee

**Status: separate scientific Draft, not independent human peer review.** This slice is stacked on frozen [AA4-ROOTREF #686](https://github.com/definitely-stable/Mathlab/pull/686), parent exact SHA `2f8c4392791234a25c90ad5bfdbbef75fe6bbeda`. It does not rewrite parent mathematical manuscripts, merge a scientific stack, close root #230, or claim a new ASET exponent.

## The exact missing bridge

The previously established all-map Branch A argument is conditional upon historical positive GF(5) six-original-ID classes: the coincident physical matching `D6` has necessary per-source-sixset probability at least `5643/51^6`, and the source `B/B-overlap` class has per-original-sixset **sum of ten unsigned balanced-sign events** probability at least `51750/51^6`. These are numerical **finite algebra** inputs, not structural all-h multiplicity assertions. This referee independently rederives the two critical constants from the **actual permitted 51-pattern GF(5) checksum-4 palette**, using two mathematically different exact algorithms and genuine `W(3,2)`, `W(3,4)` ORIGINAL incidence-ID examples.

The mathematical result is conditional only on six source flags having the certified physical/source partition, and is itself **uniform for every h and every legal fixed correlated map**: the numerical coefficient depends on the 12-edge six-column colored multigraph, never on an independence or randomness assumption about the *pair maps*.

### 1. Full original palette, six named columns and the signed graph

For one original flag (one physical column), the four coefficient entries are `(a_0,a_1,b_0,b_1)∈{1,2,3,4}^4` with

```
a_0+a_1+b_0+b_1 == 4 mod 5.
```

There are **51** such entries (verified independently by all `4^4=256` tuples), so six independently weighted columns have exactly `51^6` equiprobable allowed choices. The **original six incidence IDs are fixed**, and each chosen original point/line factor is mapped by the complete typed globally injected physical pair maps f,g. Each physical coordinate appears twice in the accepted leading 6+6 profiles. For each physical coordinate, connect the two **named original column IDs** that use it; keep the six left and six right coordinate edges distinctly colored, even if they become parallel in the six-column multigraph.

Fix an unordered global-sign 3-vs-3 trade. Represent the ten balanced sign partitions canonically by a plus triple containing named column 0, so there are `binom(5,2)=10` cases. For column `i`, set `sigma_i=+1` or `-1`, and let its boundary demand be `b_i=4*sigma_i (mod5)`. At any physical coordinate belonging to two columns i,j, signed coefficient cancellation forces

```
sigma_i*weight_(i,e) + sigma_j*weight_(j,e) == 0 mod 5.
```

Choose one arbitrary orientation for each of the twelve coordinate edges e and identify the nonzero signed coefficient at its tail with `x_e∈GF(5)*`. Then cancellation determines the corresponding coefficient at its head as `-x_e`. The six per-column checksum-4 constraints become exactly the six oriented incidence equations

```
B_H*x = b,          x∈(GF(5)*)^12.
```

This is a bijection in BOTH directions: any original admissible four-nonzero-checksum-4 coefficient assignment with the chosen sign mask gives one nowhere-zero graph flow, and each such flow reconstructs exactly the original four coefficient values. A graph coefficient must **never** be multiplied by an unearned factor of 10, 2, 6!, automorphisms, 51, or any physical coordinate re-labeling multiplicity.

## 2. Two independent exact methods

**A. Edge-deletion inclusion/exclusion.** For every subset A of the 12 distinctly colored coordinate edges, let `c(A)` count connected components on all six named column vertices (including isolates), and `b(C)=Σ_(i∈C)b_i`. Rank of the oriented incidence matrix on A is `6-c(A)`. Consequently

\[
F(H,\sigma)=\sum_{A\subseteq E(H)}
 (-1)^{12-|A|}
 \boldsymbol{1}\{b(C)=0\;\forall C\in\pi_0(A)\}
 5^{|A|-6+c(A)}.\tag{GF5-IE}
\]

All 4096 terms are computed as exact integers by a new independently written component-union/rank enumerator. Parallel edges retain distinct indices. This is inclusion/exclusion over **zero edge currents**, not an assumption that positive flow merely follows from structural leaflessness.

**B. Direct nowhere-zero spanning-tree solver.** The true colored six-column multigraph is connected. Select a deterministic spanning tree with five edges, leaving exactly seven independently chosen chords. Explicitly enumerate `4^7=16,384` assignments of NONZERO chord currents. For every assignment, subtract its signed incidence contribution from `b`; eliminate tree leaves to solve uniquely for all five tree currents. Accept iff all solved tree currents are nonzero. This oracle performs **no inclusion/exclusion, component-rank counting, Fourier summation or lookup of the historical minima**. Exact equality of its count with (GF5-IE) is a strong falsifier of sign conventions, parallel-edge handling and checksum-4 offsets.

No floating point is used in either oracle.

## 3. Complete B/B-overlap 90-case signed certificate

Each 6-coordinate B projection has exactly one ORIGINAL repeated factor, giving a **double coordinate edge** between the corresponding two named original columns, plus a simple four-cycle on the remaining four named columns. For a true original `B/B-overlap` sixset the repeated left-point pair and right-line pair share **exactly one original incidence column**: take left repeated pair `{0,1}`, right repeated pair `{0,2}` without loss of source-ID renaming. There are exactly three distinct physical C4s on the four remaining left columns and three on the remaining right columns. Therefore the complete finite class is **3×3×10=90** named **signed** cases.

**New independently reconstructed exact integer table:**

| Quantity | Certified exact count |
|---|---:|
| C4/C4 colored physical templates | 9 |
| Unordered balanced 3-vs-3 signs per template | 10 |
| Positive GF5 signed cases | **90 / 90** |
| Minimum flow count per one sign | **5,175** |
| Maximum flow count per one sign | **5,535** |
| Sum over ten signs, three templates | **53,838** each |
| Sum over ten signs, six templates | **53,526** each |
| Sum over all 90 cases | **482,670** |

For every true B/B-overlap original sixset, its physical dual C4/C4 belongs to one of these nine templates after a common permutation of **named columns** preserving both original factor types. All ten unordered sign partitions are positive. As each is a distinct signed collision event counted in the accepted risk quantity R3, **without assuming independence between the ten events**, its exact necessary GF5 floor is

\[
\boxed{R_3(\text{one ORIGINAL B/B-overlap sixset})
 \ge 10\cdot5175/51^6 =51750/51^6.}\tag{GF5-BBO}
\]

This is precisely the historical coefficient used in root #230. The complete signed exact sum `482670` also matches the fixed-forest-class total from merged #224; this is **new independent recomputation**, not an oracle lookup. A per-shape sum may be 53526 or 53838, so claiming the universal numerator equals 51750 would be incorrect; that number is a **lower floor**.

## 4. Coincident matching physical C6/C6 → D6

For six **distinct ORIGINAL point and line factor IDs** (one matching of six ORIGINAL flags) whose left and right named-column adjacency graphs are both the SAME single C6, the graph H is the union of two color-distinct copies of that C6. The canonical alternating sign triple `{0,2,4}` gives

\[
\boxed{F(C_6^{\rm left}\cup C_6^{\rm right},\{0,2,4\})=5643.}\tag{GF5-D6}
\]

The second independent direct tree-chord enumerator verifies **exactly 5643** as well; all ten canonical sign masks have positive flows, with values between 5265 and 5643. Since the alternating event is a single valid 3-vs-3 signed collision of the original six source IDs, its contribution alone gives `5643/51^6`. No unjustified multiplication by ten or by 60 physical cycles is made for this floor.

## 5. Independently PLANTED genuine ORIGINAL source-ID witnesses

The finite referee imports only the preexisting **true W(3,2^h) original incidence generator**, not any historical GF5 classifier or flow oracle. On both `h=1,2`, it constructs:

1. **B/B overlap:** choose a true ORIGINAL nonincident (q,r), find its genuinely unique projection `q--ell--p--r`, and add three source-disjoint genuine ORIGINAL flag IDs `(u_i,lambda_i)`. Choose f(q) to close a physical four-cycle on coordinates 0,1,2,3, choose f(u1),f(u2),f(u3) along its three physical edges, choose f(p)={4,5}; dually choose g(r),g(lambda_i) on the C4 and g(ell)={4,5}. Extend **both** maps to complete, globally injected typed pair assignments. The six ORIGINAL flags now have precisely one doubled point p and one doubled line ell, meeting at **the same actual original flag** (p,ell). Rebuild the 12-edge column flow graph from those actual original flag IDs and physical coordinate memberships — not from one of the nine abstract templates. Check all ten GF5 signs and the two independent exact oracles.
2. **D6:** choose six disjoint TRUE original flag IDs greedily, assign their six distinct point and line factor maps to the same physical six-cycle and extend both maps globally and injectively. Rebuild the flow graph from actual source flags, check alternating coefficient exactly 5643 with both methods.

These are finite **adversarial positive witnesses**, ensuring that the numeric tests do not pass vacuously on fake synthetic factors or zero physical motifs. They check original-ID semantics and complete arbitrary-correlated typed maps; finite `h=1,2` examples do not prove the infinite root obstruction by themselves.

## 6. Mathematical acceptance boundary and explicit non-implications

This slice independently verifies the precise **GF(5) algebraic input** used by ROOTREF:

\[
51^6R_3(f,g)\ge5643 D_6(f,g)+51750 U_{BB,\rm overlap}(f,g)
\]

as a **necessary subfamily floor**, for every fixed legal pair f,g and all dyadic h whenever these accepted original sixset projections occur. The source GF5 flow bijection is purely combinatorial and its 12-edge universe is fixed-size; the statement extends uniformly in h because its proof never enumerates the full original W(3,s). Other positive motif classes, the complete R3 and R2, and different ASET constructions are not evaluated here.

**This does not independently review** the `D6+U_BBo>=delta*s^6` geometric all-map obstruction; that belongs to #659/#672/#684–686 and still awaits a qualified external referee. Nor does it establish that arbitrarily chosen six flags realize these physical projections, or turn all-h finite GF5 positivity into an all-h upper bound. Full historical 631 named leading forest types and the remaining subleading classes are NOT recounted; only the two exact classes on which the root Branch A proof ultimately rests are audited.

### Reproduction and CI gates

- `research/hyp105_gf5_original_sixid_flow_referee.py`: new independent IE and tree-chord GF5 solvers; all 90 B/B signed graphs; genuinely original W32/W34 BBo and D6 planted source-ID projections.
- `research/test_hyp105_gf5_original_sixid_flow_referee.py`: all 51 palette tuples, signed class minima/maximum/total, two independent oracle checks, source-flag preservation for every genuine witness, complete point/line injections, named-column relabeling invariance, fail-closed bad-ID/illegal-mask tests.
- `.github/workflows/hyp105-gf5-original-sixid-flow-referee.yml`: GitHub-hosted Ubuntu 24.04 / Python 3.12, exact SHA; plus full `Research` and `INDEX` jobs where triggered.
- Keep `#230=OPEN_WITH_FORMAL_BLOCKER` and scientific PR Draft until qualified review of the entire **geometric** argument, not merely this finite algebraic bridge.
