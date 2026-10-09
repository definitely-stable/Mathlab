# HYP-105 G5-C3-B0 — Exact dual duad–syntheme geometry as a structured pair-label testbed

Date: 2026-10-09 · parent G5-C [#106](https://github.com/definitely-stable/Mathlab/issues/106), G5-C3 [#119](https://github.com/definitely-stable/Mathlab/issues/119), earlier [C3-A](HYP-105-G5-C3-A-STRUCTURED-LABEL-SEARCH.md).

**CLASSICAL_FINITE_GEOMETRY_RECONSTRUCTED / SOURCE_DISCOVERED / FINITE_GF5_EXACT / NO_ALL_S_CONSTRUCTION / NO_NEW_EXPONENT / NO_RUST.**

## 1. The mathematical question, not merely another permutation

C3-A showed that arbitrary point/line pair-label swaps reduce GF5 signed-trade support counts in **one** W(3,2), m=12 example; accepted ASET subfamily size remained 20. C2-D showed independent uniformly random pair-label assignments have expected T6=Omega(m^4) along infinite GQ(s,s), with **no all-labeling lower** or concentration theorem. The best next research objective is to replace arbitrary pair-label assignments with **geometrically canonical, correlated** left/right pair labels and establish whether any structural reduction persists uniformly as s grows. For s=2, there is a pre-existing explicit combinatorial realization of the symplectic GQ(2,2), called the *doily*.

**Verified primary source and priority:** [*Magic Three-Qubit Veldkamp Line and Veldkamp Space of the Doily*, Symmetry 12(6), 963 (2020), §2](https://www.mdpi.com/2073-8994/12/6/963), DOI [10.3390/sym12060963](https://doi.org/10.3390/sym12060963), explicitly defines duads as 2-subsets of a six-element set and synthemes as partitions into three disjoint duads. The 15 duads and 15 synthemes form the published GQ(2,2) point–line incidence structure. Also [AMS, *Tutte–Coxeter Graph*, 2015](https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/) explains the same 15+15 construction and the exceptional outer automorphism of S6. **No originality claim** for this representation, its six special 5-subsets, duality, or the named combinatorial objects.

This 2020 DOI was checked against Mathlab's LIT catalog on 2026-10-09 and was not present at discovery; this document imports a primary-source link and model/provenance now. **Canonical LIT identity/indexing remains a separate gate while independent IMPORT-005 #127 edits the shared bibliography; do not claim it has already been assigned an ID.**

## 2. Exact GQ(2,2) combinatorial reconstruction algorithm

The existing W(3,2) fixture has fifteen nonzero vectors of GF(2)^4 as points and fifteen symplectic isotropic projective lines, each containing three points. Construct the point **collinearity graph** C_P: distinct points are adjacent precisely if they lie on a common isotropic line. Construct the dual line **intersection graph** C_L: two distinct lines are adjacent iff they intersect in a point. Both are 15-vertex, degree-six graphs; in the classical duad model, the collinearity graph is the disjointness graph on K6's 15 edges.

**Finite exact G5-C3-B0 lemma.** Exhaustively enumerating all C(15,5)=3003 five-subsets of each graph and testing every internal pair against adjacency yields **exactly six independent five-sets** of C_P (classical ovoids) and exactly six independent five-sets of C_L (classical spreads). Each vertex belongs to exactly two of these six sets, and each two of the six sets intersect in exactly one vertex. Thus label those six objects 0..5; the membership pair for each original point/line is an unordered duad from K6, and the map of fifteen point (respectively line) vertices onto the 15 duads is bijective.

**Proof/certification boundary:** the statement for this **fixed finite W(3,2)** is proved by transparent exhaustive enumeration over the full finite universe of possible five-subsets, with the independent original symplectic GF(2)^4 incidence oracle. It is also a published classical geometry representation (see primary source above). The finite enumerator is a mathematical certificate when run and cross-checked; **it is not a symbolic proof for all generalized quadrangles GQ(s,s)** and cannot be promoted to an infinite-family construction. In particular the order s=2 is exceptional (S6 outer automorphism); one cannot automatically represent arbitrary GQ(s,s) with both part vertices labeled by all pairs on only O(s^(3/2)) coordinate symbols using this six-object trick.

**Independent model check:** Every existing isotropic line becomes a triple of pairwise disjoint point-duads covering all six symbols, i.e. a syntheme. Enumerate independently the 15 perfect matchings of K6 via recurrence (take smallest remaining symbol, pair it with each other remaining symbol, recurse) and require equality with the recovered 15 synthemes. Check all 15*15 incidence predicates individually: original point lies on line iff its duad is one of that syntheme's three pairs. Repeat the dual assertion for line-duads incident through each point. Confirm 45 original edges and abstract girth eight.

### 2.1 Exact no-go for the naive FULL-duad transfer beyond s=2

**Elementary theorem (specific full-duad model only).** Suppose for some generalized quadrangle GQ(s,s), s>=2, there is an integer a such that **ALL** its (s+1)(s²+1) point vertices are bijective with **ALL** binom(a,2) duads of an a-symbol alphabet and two distinct points are collinear **if and only if** the corresponding duads are disjoint. Then s=2 and a=6. Thus the exact doily model cannot be reproduced wholesale by merely replacing six symbols with a growing alphabet for any s>=3.

**Proof.** A point of GQ(s,s) lies on s+1 lines, each with s other points; distinct lines through a point meet only there. Its collinearity graph therefore has V=(s+1)(s²+1) vertices and degree D=s(s+1). The disjointness graph of all K_a duads has V'=binom(a,2) vertices and D'=binom(a-2,2). Both invariants must agree. Subtraction gives binom(a,2)-binom(a-2,2)=2a-3=V-D=(s+1)(s²-s+1)=s³+1; hence 2a=s³+4. For odd s, the right side is odd and no integer a exists. For even s>=4, a=(s³+4)/2>=s³/2, hence binom(a,2)>s³+s²+s+1=V (the inequality is already strict at s=4 and grows monotonically), contradicting V'=V. At s=2, a=6 satisfies both conditions: 15 duads and six disjoint duads adjacent to each duad. QED.

**Nontransfer caveat:** this proof forbids only a **full, exact graph isomorphism** between GQ(s,s) point collinearity and the disjointness graph of *all* duads. It does NOT preclude injection into a selected proper subset of K_a pairs, a different collinearity-to-pair relation, signed coordinate weights, correlated two-sided labels, or more general ASET constructions. In particular the G5-B arbitrary graph realization theorem survives intact and must not be misquoted as contradicted by this narrower result. The finite/exact parameter calculation is independently regression-tested for orders 2,3,4,5,8,16,32,64.

## 3. A fully specified, finite and interpretable left/right labeling

Use ovoid-membership pairs as the left 15-pair bijection and spread-membership pairs as the right 15-pair bijection, with each six-member family sorted deterministically by its original graph-vertex IDs. This is a reproducible, nonuniform and geometrically derived **pair** of label bijections, rather than ad hoc random pair assignments.

Each of the original 45 incidence edges becomes one all-one four-support GF5 column in m=12 coordinates, containing two labels in L and two in R. Because both assignments are bijections, the underlying factor graph is still the same girth-eight W32. But the true coordinate-level signed trades must be enumerated: the geometry does not imply signed injectivity.

Executable: [research/hyp105_g5c3b0_doily_geometry.py](../../research/hyp105_g5c3b0_doily_geometry.py). It independently reconstructs two kinds of five-subset memberships, calls the fast exact base-five collision census **and the independently implemented C2 full-vector collision oracle**, constructs a certified GF5 ASET subfamily by rational alteration, then optionally performs a **bounded** swap descent from the geometric labels. Exact output is a JSON data record including the geometric T4/T6, finite ASET cardinality, bounded result, budget, and explicit full left/right 15-label maps. An optimization score improvement is not automatically an ASET cardinality improvement; neither finite result establishes an exponent.

Run on GitHub-hosted CI:

    python research/hyp105_g5c3b0_doily_geometry.py --rounds 4 --probes 8

Independent executable checks: [research/test_hyp105_g5c3b0_doily_geometry.py](../../research/test_hyp105_g5c3b0_doily_geometry.py). The reference enumerates all 15 K6 perfect matchings independently from the W32 graph, verifies all 225 incidence truth-values, both six-family reconstructions, unit support/field arithmetic and complete direct GF5 subset sums of sizes 0..3 for the full extracted subfamily, plus independently enumerated signed +/-1 kernels only on bounded held-out six-column selections (avoiding the 3^N blow-up). Exact original source geometry and code provenance remain separate assertions.

### 3.1 Frozen exact finite W32 geometric evidence and non-monotone tradeoff

[GitHub Research #1125](https://github.com/definitely-stable/Mathlab/actions/runs/37897378969) completed **SUCCESS** (26 workflow steps) after scoping the exponential signed kernel check to six-column held-out selections; full-family ASET subset sums remain directly checked exhaustively. For the reproducible geometry-derived left/right bijections, ambient m=12 with 45 original distinct GF5 unit four-support columns:

| Finite signed-sum quantity | C3-A optimized arbitrary pair labels (m=12) | B0 canonical doily-derived labels (m=12) |
| --- | ---: | ---: |
| Inclusion-minimal four-column supports T4 | 42 | **0** |
| Inclusion-minimal six-column supports T6 | 1580 | **2100** |
| GF5 ASET subfamily extracted and independently certified | 20 | **18** |

The doily geometry yields an **exact absence of four-column signed trades** in the fixed W32 labeling: T4=0 by exhaustive complete finite oracle. It **does not imply ASET** because 2100 minimal three-vs-three six-column supports remain. The no-swap bounded four-round/eight-probe descent returned the same values (33 total census evaluations, zero strictly accepted swaps under heuristic T6+16*T4); this is not proof of local optimality, especially not across all 210 possible vertex-pair swaps or the enormous full pair-label quotient.

The two explicit geometry-derived pair-label bijections are frozen as follows:

    L=(0,9,14,3,7,8,4,11,12,13,10,6,2,5,1)
    R=(0,9,14,3,8,4,7,11,6,12,1,13,5,10,2)

**Central falsification:** eliminating **all** T4 supports can INCREASE T6 and DECREASE the actually extracted ASET cardinality. A conjecture that minimizing T4 is sufficient to improve the ASET bound is invalid; any all-s construction must jointly control T4 and T6, and ultimately all weighted imbalance trade types if transferred to unrestricted ASET. These numbers are only m=12; no general growth exponent or new 12/5 comparison is proved. Regression tests pin T4/T6/valid subset size and the exact label maps.

## 4. All-s gate, competing approaches, and stop condition

What follows mathematically from B0:
- The fixed order-2 W32 has a *source-backed*, exactly recovered natural coordinate-pair pair of bijections.
- Any explicit finite signed-trade counts, after independent hosted evidence, can be compared fairly with the previous seed=1 C3-A T4=42, T6=1580 while preserving graph girth and m=12.
- The real G5-C3-B goal is still a new **uniform-in-s** family over GQ(s,s), s=2^h, with provable counts for **both** T4 and T6. C2's sufficient alteration conditions b4<52/15 and b6<4 are **unproved**; uniform random labels have E[T6]=Omega(m^4), not a universal deterministic lower.

A serious next proof path must (i) parametrize pair-label maps algebraically for all s, (ii) classify synchronized projected alternating 4/6-coordinate circuits under the geometric incidence relation, (iii) count *distinct minimal column supports* rather than sign witnesses with explicit upper constants and quantified s, (iv) independently verify finite s=2 and a next nontrivial s using exact or mathematically justified fast oracles, and (v) compare with the known ASET exponent and published theorems. Spectral estimates on individual incidence edges alone do not bound joint six-edge trade counts. If the exceptional order-2 duad model fails to generalize, record **STOP_DOILY_SPECIAL_CASE_FOR_UNIFORM_EXPONENT** for this strategy only; keep weighted full ASET G5-C #106/#95 open.

Reference model controls: [Naor–Verstraëte 2008 author full paper](https://web.math.princeton.edu/~naor/homepage%20files/PARITY.pdf), LIT-152, gives prior full ASET O_q(m^(8/3)); [Lefmann 2005](https://doi.org/10.1017/S0963548304006625), LIT-043, gives A_lin lower Omega_q(m^(12/5)(log m)^(1/5)). No proven growing ASET/linear ratio and no Rust product authorization.
