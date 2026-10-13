# HYP-105 / #230 — D6-AA4-A: exact source-forest support and original-position conditional transport

**Status:** restricted all-h source-support theorem + exact W(3,2) finite conditional Fréchet diagnostic. **NOT** PROVED_A, COUNTEREXAMPLE_B, or a positive all-h GF(5) lower bound. No full R3 estimate or ASET exponent.

**Stack:** new Draft strictly based on D6-AA1–AA3 PR #430, exact parent \`a2e6e0e6aa3eb78dc82e4f1a6b3c22d69d5b8cc1\`. That parent is 4/4 GitHub-hosted green. No \`main\` changes and no merges.

## 1. All-h original-source support theorem (AA4-A1)

Consider **six DISTINCT ORIGINAL** incidences \((p_i,\ell_i)\) in true symplectic generalized quadrangle \(W(3,s)\), \(s=2^h, h\ge1\), with separate globally injective typed physical pair maps \(f,g\). If the left and right physical projections each have exactly six coordinates, all of physical multiplicity two, then EVERY original point and line factor occurs at most twice among those six positions: a physical pair repeated three times would contribute degree at least three to both coordinates and destroy physical 2-regularity.

Thus the ORIGINAL bipartite source-incidence graph on those selected edges has maximal degree \(\le 2\). It is also **simple** since the six original incidence IDs differ. A graph of maximal degree two is a union of paths and cycles. \(W(3,s)\) has girth eight, while this subgraph has only six edges, hence it contains **no cycle**. Therefore:

\[
\boxed{\text{two-sided physical 2-regular Q}\Longrightarrow
       \text{six-edge ORIGINAL bipartite source linear forest}.}
\]

This implication holds for every allowed \(h\), not merely the W32 fixture. The converse is false: a source linear forest does not imply any physical projection is 2-regular.

### Exact abstract support mask on the 130-by-130 positional pairs

A degree-two physical projection corresponds to one of exactly 130 named six-position multigraphs in AA1. For each of \(130^2=16\,900\) **ordered** left/right pairs, reconstruct the six ORIGINAL point and line equality partitions by identifying which two-position columns carry **identical physical pairs**. For every position \(i\), pair its original point-partition ID with its original line-partition ID to obtain six abstract source incidences. Reject if an incidence repeats or these six edges form a source cycle. Otherwise accept as an *abstract simple bipartite source forest*.

These conditions produce an exact, independently executable positional mask. They are **necessary** for a real sixset in every W(3,s). They DO NOT claim that every abstract forest/pattern pair embeds into W(3,2) or every finite higher-order geometry.

| Source mask outcome | Count |
|---|---:|
| Abstract-source inadmissible: repeated incidence or cycle | 630 |
| Admissible A/A but not seven positive | 4,840 |
| Admissible D6 | 60 |
| Admissible B-left/A-right | 3,150 |
| Admissible A-left/B-right | 3,150 |
| Admissible C/A | 2,100 |
| Admissible C/B | 1,080 |
| Admissible B/B-overlap | 1,080 |
| Admissible B/B-disjoint | 810 |
| **Total** | **16,900** |

In particular **16,270** positional pairs satisfy the abstract source-forest mask; among them **11,430** fall into the seven accepted families and **4,840** are A/A mismatch. This is a count of abstract **named positional graph pairs**, *not* original sixsets and *not* a positive global bound.

### Structural consequence: no non-A/A physical proxy false positive

If a true ORIGINAL sixset Q is 2-regular on both sides, either it belongs to the seven accepted families, or both typed projections are type A and the D6 graph alignment/connectedness test fails. Indeed B/B equal doubled original positions would repeat an incidence; C/B with an identical doubled incidence would also duplicate it; C/C would induce a forbidden bipartite six-cycle unless an incidence repeats. All other A/B/C combinations satisfy their accepted class predicate.

Thus for any allowed \(h\), \(f\), \(g\),

\[
\boxed{S_s(f,g)=T_s(f,g)-F^{AA}_{s}(f,g),}
\]

where \(T_s\) is the number of distinct ORIGINAL sixsets 2-regular on both physical sides and \(F^{AA}\) is the number of non-D6 A/A two-sided-regular originals. The identity is exact; neither term has yet been universally bounded to imply \(S_s\ge cs^6\). The decomposition clarifies precisely which proxy false positives remain on genuine geometry. Both full original S68/S72 finite censuses must verify it.

### Source linear-forest shapes of the seven families

A/A (including D6) consists of six single-edge components \(1+1+1+1+1+1\). B/A and A/B: \(2+1+1+1+1\). C/A: \(2+2+2\). C/B: \(4+2\). B/B-overlap: \(3+1+1+1\); B/B-disjoint: \(2+2+1+1\). Path length means number of ORIGINAL incidence edges in that component, not physical coordinates. This is all-h true because the source subgraph is a path forest.

## 2. SOURCE-six-position conditioned transport relaxation (AA4-A2)

The AA3 one-sided aggregations discarded the ORIGINAL mapping between source-incidence subsets and physical patterns. Repair **part** of that loss by conditioning on both *exact* ORIGINAL equality partitions of the same ordered six positions. For Q=(e_0,...,e_5), with e_i ordered by ORIGINAL incidence ID, set

\[
\kappa(Q) =
\bigl(\operatorname{partition}(p_0,\ldots,p_5),\ 
      \operatorname{partition}(\ell_0,\ldots,\ell_5)\bigr).
\]

Each partition records precisely which of the six ORIGINAL positions repeat a common typed source factor, with canonical first-occurrence IDs. This retains more information than merely A/B/C source degree profiles, including whether the left and right repeated positions overlap.

For every stratum \(\kappa\), define:
- \(N_\kappa\): the number of **all** distinct-original-incidence sixsets Q with \(\kappa(Q)=\kappa\).
- \(L_\kappa\): the number of those Q that have six degree-two physical coordinates on the LEFT.
- \(R_\kappa\): the analogous count on the RIGHT.

For arbitrary fixed complete injective maps on the same original source geometry, let \(J_\kappa\) denote the number of Q that satisfy both physical predicates. Elementary set inclusion yields

\[
\boxed{\max(0,L_\kappa+R_\kappa-N_\kappa)
       \le J_\kappa\le \min(L_\kappa,R_\kappa).}
\]

The lower bound is **sharp among abstract couplings retaining ONLY the two one-side binary indicator marginals within this stratum**. One explicit integral coupling partitions \(N_\kappa\) abstract items into counts:

\[
J_\kappa^{\min},\quad
L_\kappa-J_\kappa^{\min},\quad
R_\kappa-J_\kappa^{\min},\quad
N_\kappa-L_\kappa-R_\kappa+J_\kappa^{\min}.
\]

All are nonnegative and sum to \(N_\kappa\). This is *not* an assignment of physical pair labels to globally shared original source factors: different Q may be re-paired independently, so this local transportation relaxation does NOT satisfy global compatibility or the D6-X/Y lifted physical-column capacity inequalities.

Crucially, if \(\kappa\) is not A/A, every actual both-regular Q in that stratum falls into one of the seven accepted classes by AA4-A1. Thus the **valid deterministic** necessary lower bound on true S for fixed maps is

\[
S_s(f,g)\ \ge\
\sum_{\kappa:\,\kappa\ne AA}
\max(0,L_\kappa+R_\kappa-N_\kappa).
\]

For A/A the simultaneous physical regularity itself is insufficient: one must also require aligned *connected* six-position graphs. Counting its forced overlap as automatically D6 would be incorrect.

The exact lower bound above holds for arbitrary source hosts under the stated forest/girth conditions, but computing all \(\kappa\) tables at large \(s\) is nontrivial. The hosted finite diagnostic must say whether the selected conditional information alone enforces anything positive on S68/S72. Do not infer an all-h constant from finite results.

## 3. Original W32 falsifier protocol

On the original W(3,2), \(|I|=45\), \(\binom{45}{6}=8,145,060\).
1. Enumerate all 62,370 six-incidence LEFT 2-regular candidates using the existing independent projection-template generator, keeping their original incidence IDs.
2. Independently enumerate all 62,370 RIGHT candidates by dualizing the ORIGINAL incidence relation and swapping typed image maps.
3. Compute a full \(\kappa\)-stratum denominator census by examining **every one of the 8,145,060** original sixsets, **once**, independent of physical pair assignments. Reject partial scans.
4. Calculate exact integer Fréchet floor and explicit two-bit coupling for each source stratum; compare with actual two-sided degree-two proxy counts (S68=331,S72=358) and seven-class original counts (S68=68,S72=72).
5. Independently classify every 2-regular-but-rejected ORIGINAL sixset; by AA4-A1 it must be A/A nonaligned (S68=263,S72=286). Reject any C/C or B/B source false positive.
6. Run all small integer transport marginals by an exhaustive second oracle, and check the complete 16,900 positional support pairs against the established AA1 predicate and independently computed source graph.

A true two-sided regular Q is never double-counted. SOURCE \(\kappa\) keys are based on actual six incidence positions, not on physical-edge automorphism or signed events.

## 4. All-h decision boundary / what AA4 does NOT prove

The theorem controls the support of the joint \(130\times130\) positional tensor and proves a source-partition conditional marginal inequality, but it does **not** impose consistency between different sixsets sharing the same ORIGINAL factor. A zero value of the conditional transport floor on finite W32 would be an exact obstruction to obtaining a positive lower **from this specific reduced information**, not a correlated infinite label construction (Branch B). A positive finite floor would not be an all-h bound.

To prove Branch A one still needs a constant \(c>0\), independent of \(h,f,g\), with

\[
\forall h\ge1\ \forall f,g\text{ globally injective},\
S_{2^h}(f,g)\ge c2^{6h}.
\]

The immediate next direction, if no all-h certificate is obtained, is to lift transport strata with cross-Q ORIGINAL-factor overlap consistency and globally valid occupied-physical-label capacity constraints, **not** another unconditioned pair-graph moment envelope.

**Acceptance:** dedicated GitHub-hosted AA4-A + INDEX + Proof Audit + full Research success on exact final head; independent mathematical review separately; Draft only, no main merges. Branch A/B OPEN; no R3 upper or ASET exponent.
