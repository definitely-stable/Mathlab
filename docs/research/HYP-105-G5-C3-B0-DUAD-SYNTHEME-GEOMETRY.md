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

## 3. A fully specified, finite and interpretable left/right labeling

Use ovoid-membership pairs as the left 15-pair bijection and spread-membership pairs as the right 15-pair bijection, with each six-member family sorted deterministically by its original graph-vertex IDs. This is a reproducible, nonuniform and geometrically derived **pair** of label bijections, rather than ad hoc random pair assignments.

Each of the original 45 incidence edges becomes one all-one four-support GF5 column in m=12 coordinates, containing two labels in L and two in R. Because both assignments are bijections, the underlying factor graph is still the same girth-eight W32. But the true coordinate-level signed trades must be enumerated: the geometry does not imply signed injectivity.

Executable: [research/hyp105_g5c3b0_doily_geometry.py](../../research/hyp105_g5c3b0_doily_geometry.py). It independently reconstructs two kinds of five-subset memberships, calls the fast exact base-five collision census **and the independently implemented C2 full-vector collision oracle**, constructs a certified GF5 ASET subfamily by rational alteration, then optionally performs a **bounded** swap descent from the geometric labels. Exact output is a JSON data record including the geometric T4/T6, finite ASET cardinality, bounded result, budget, and explicit full left/right 15-label maps. An optimization score improvement is not automatically an ASET cardinality improvement; neither finite result establishes an exponent.

Run on GitHub-hosted CI:

    python research/hyp105_g5c3b0_doily_geometry.py --rounds 4 --probes 8

Independent executable checks: [research/test_hyp105_g5c3b0_doily_geometry.py](../../research/test_hyp105_g5c3b0_doily_geometry.py). The reference enumerates all 15 K6 perfect matchings independently from the W32 graph, verifies all 225 incidence truth-values, both six-family reconstructions, unit support/field arithmetic and the actual absence of signed +/-1 collisions in the extracted subfamily. Exact original source geometry and code provenance remain separate assertions.

## 4. All-s gate, competing approaches, and stop condition

What follows mathematically from B0:
- The fixed order-2 W32 has a *source-backed*, exactly recovered natural coordinate-pair pair of bijections.
- Any explicit finite signed-trade counts, after independent hosted evidence, can be compared fairly with the previous seed=1 C3-A T4=42, T6=1580 while preserving graph girth and m=12.
- The real G5-C3-B goal is still a new **uniform-in-s** family over GQ(s,s), s=2^h, with provable counts for **both** T4 and T6. C2's sufficient alteration conditions b4<52/15 and b6<4 are **unproved**; uniform random labels have E[T6]=Omega(m^4), not a universal deterministic lower.

A serious next proof path must (i) parametrize pair-label maps algebraically for all s, (ii) classify synchronized projected alternating 4/6-coordinate circuits under the geometric incidence relation, (iii) count *distinct minimal column supports* rather than sign witnesses with explicit upper constants and quantified s, (iv) independently verify finite s=2 and a next nontrivial s using exact or mathematically justified fast oracles, and (v) compare with the known ASET exponent and published theorems. Spectral estimates on individual incidence edges alone do not bound joint six-edge trade counts. If the exceptional order-2 duad model fails to generalize, record **STOP_DOILY_SPECIAL_CASE_FOR_UNIFORM_EXPONENT** for this strategy only; keep weighted full ASET G5-C #106/#95 open.

Reference model controls: [Naor–Verstraëte 2008 author full paper](https://web.math.princeton.edu/~naor/homepage%20files/PARITY.pdf), LIT-152, gives prior full ASET O_q(m^(8/3)); [Lefmann 2005](https://doi.org/10.1017/S0963548304006625), LIT-043, gives A_lin lower Omega_q(m^(12/5)(log m)^(1/5)). No proven growing ASET/linear ratio and no Rust product authorization.
