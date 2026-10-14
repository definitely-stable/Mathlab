# HYP-105 issue #230 — D6-AA4-D: joint two-type globally injective completion fibers over all minimal source transversals

**Classification:** all-h exact *conditional* mixed block-completion identity + exhaustive exact original W(3,2) finite all-four-factor zero-feasibility audit around two frozen schemes. Universal Branch A/B OPEN. No claim of a new asymptotic GF(5) lower bound or full R3.

**Stack:** Draft on all-four-hosted-green [D6-AA4-C #436](https://github.com/definitely-stable/Mathlab/pull/436), pinned parent \`714e9806463803d6721cd8e7dbe56f27072fae98\`. Work is branch only, without main edits/merges. #230/#176/#169 remain OPEN.

## 1. Why the AA4-C vertex cover is insufficient to realize zero S

For each of two genuine low-seven-count complete symplectic W(3,2) maps S68, S72, AA4-C independently inspected exact typed ORIGINAL six-incidence positive hypergraphs. Their minimum hitting-set number is exactly four, on points only, lines only, or both types combined; a four-factor hitting set B may touch **every previously positive** Q, yet that does NOT mean there is a physical re-labeling of B which leaves total S zero. Indeed AA4-B had already produced one such source-transversal right block in S72 with zero old positives but full 24-bijection coherent positive minimum 68.

AA4-D resolves the **finite complete radius-four question**, with genuine global factor-label assignments and exact original GQ source geometry, rather than isolated frozen right blocks. This is more than repeating D6-P right swaps: left original point labels AND right line labels are jointly reassignable, and **every** minimum typed size-four source hitting set is audited (not sampled).

## 2. ALL-h mixed ORIGINAL typed block completion theorem

Fix s=2^h, h>=1; V=(s+1)(s^2+1), a minimal with K=C(a,2)>=V, m=K-V. Fix arbitrary full globally injective physical pair labels f on ORIGINAL point factors and g on ORIGINAL line factors of the actual W(3,s). Fix arbitrary typed ORIGINAL blocks B_P⊆P, B_L⊆L, cardinalities b_P and b_L, and all physical assignments outside the blocks.

For the point type, exactly m+b_P physical pair edges are available after freezing V-b_P original point labels. An injective assignment to B_P has \((m+b_P)_{\underline{b_P}}\) legal completions; analogously the line type has \((m+b_L)_{\underline{b_L}}\) completions. They are independently injective **within their types**, with no false cross-type prohibition on reusing the same physical edge, so the product

\[
|\mathcal J(B_P,B_L)| =
(m+b_P)_{\underline{b_P}}\cdot(m+b_L)_{\underline{b_L}}
\]

is the complete number of genuine global coherent physical maps which agree with f,g outside the typed source block.

The exact all-h minimum over these completions is

\[
\boxed{C_{B_P,B_L}(f,g)
=\min_{(f',g')\in\mathcal J(B_P,B_L)}
\sum_{\substack{Q\subseteq I_s\\|Q|=6}}\mathbf1_{\rm seven}(Q;f',g').}
\]

Every such term is defined on the ORIGINAL six DISTINCT source incidences, keeping original physical point and line factor identities and the six-column positional alignment. All corresponding GF5 certified floor sums have an identical exact completion-minimum formulation. Unlike independently minimizing each Q, **one common** f'(p) is shared among every Q using p, and one common g'(ell) among every Q using ell. No factor independence or arbitrary sixset transportation is allowed.

Write \(U_B(f,g)=\#\{Q:\mathbf1_{\rm seven}(Q;f,g)=1,\ T(Q)\cap(B_P\sqcup B_L)=\varnothing\}\) from AA4-C. Its exact source support-invariance theorem yields

\[
\boxed{C_{B_P,B_L}(f,g)\ \ge U_B(f,g).}
\]

This is valid for all h, all f,g, all source blocks, and all legal global typed physical pair maps. It does **not** certify the desired all-h \(\min_{f,g}S_s(f,g)\ge c s^6\).

## 3. Rigorous reduction to minimal source transversals for zero-feasibility within four edits

For a fixed reference f,g, call B a source transversal when it intersects the ORIGINAL source factor support T(Q) of **every currently seven-positive Q**.

If B is **not** a transversal, \(U_B(f,g)\ge1\); thus EVERY globally injective pair (f',g') differing only on B has S(f',g')≥1, no computation of newly created positive Q needed.

If B *is* a transversal, U_B=0 does not decide zero feasibility, so enumerate the full joint injection fiber \(\mathcal J(B_P,B_L)\), including both physical factor types. Its exact minimum S is a decision oracle for this B: if S_min>0, there is NO complete globally injective pair of labels agreeing outside B with S=0; if S_min=0, produce the genuine ORIGINAL f',g' witness (not automatically an infinite h counterexample).

For genuine W(3,2), K=V=15 so m=0. Every legal edited-type completion is a permutation of the previously occupied physical labels of that type **within its edited original factor IDs**. For bP+bL=4, the fiber has exactly bP!·bL! globally legal complete assignments (1,4,6,4,24 respectively for bP=0,1,2,3,4). Keeping all original factor identities fixed outside B makes this an EXHAUSTIVE audit of every globally injective W32 map differing at most on B.

Because every smaller changed source set is contained in some four-factor block, one may partition all C(30,4)=**27,405** four-factor blocks into:
- nontransversals: rigorous old-Q floor U_B≥1, no enumeration needed;
- transversals: enumerate **every** legal bP!bL! physical completion and classify all ORIGINAL sixsets using the exact D6-P six-position cylinder compiler and accepted GF5 class oracle, with multiple independent historical \`seven_census\` comparisons.

It follows pointwise that, for ALL *genuinely globally injective* W32 assignments \((f',g')\) at original typed-factor Hamming distance ≤4 from the fixed S68 or S72 starting map,

\[
\boxed{\quad
S_2(f',g')\ \ge\
\min\left(
\min_{\substack{|B|=4\\B\mathrm{\,nontransversal}}}U_B(f,g),\
\min_{\substack{|B|=4\\B\mathrm{\,transversal}}}
C_{B_P,B_L}(f,g)\right).
\quad}
\]

This is an **exact valid combined lower** (potentially not sharp because the nontransversal arm counts only old retained Q). Report and pin that value **only after an independently verified GitHub-hosted run**, never guess or extrapolate.

### Important interpretive caveat

A W32 result with all four-factor transversals positive proves that *neither S68 nor S72 has any zero-count neighboring map within four edited ORIGINAL point/line factor identities*, and may expose a new coherent-correlations barrier over the entire first permissible edit radius. It says nothing about all complete maps on W32 at larger Hamming distances, nor any s≥4 geometry, nor Branch A/B. Even a finite W32 zero would refute a universal positive all-h inequality as literally stated for all h≥1, but would not itself be an infinite Branch B correlated family.

## 4. Exact hosted implementation and acceptance gate

1. Freeze genuine original S68 and S72 with their complete K6 physical pair bijections and genuine ORIGINAL 45-incidence W32 geometry. Enumerate every selected 62,370 left 2-regular ORIGINAL sixset and independently compare full seven-class tags on each Q against the AA1 positional classifier (including negatives).
2. Build the ORIGINAL typed point/line hypergraph of the seven accepted positive Q, source support bitsets, and classify **every** C(30,4)=27,405 source blocks. Fail closed unless the transversal counts exactly match previously hosted AA4-C: 53 S68; 119 S72.
3. For each true source transversal B, exhaust **all** bP!·bL! genuine two-type globally injective assignments using one original factor label per original identity. Do NOT optimize individual Q separately.
4. For every left type assignment, build the D6-P independent full 62,370-original-sixset positional cylinder compiler once and apply each right completion against every cylinder. Record exact seven-class S and necessary selected GF5 floor numerator across every joint completion. Freeze and verify all per-block minima, split distribution, zero counts, global minimum and genuine achieving labels. Validate several actual completed maps per ORIGINAL split independently using historical \`seven_census\`.
5. Construct the lower bound over ALL 27,405 support blocks, combine the exact transversal coherent minimum with the unchanged-old-positive lower for nontransversals. If the bound is >0, obtain a complete finite uniform-at-edit-radius-four zero-exclusion **relative to each pinned starting map**.
6. Run independent AA4-D, INDEX, Proof Audit and Research GitHub-hosted SUCCESS on exactly final PR HEAD, and require separate mathematical review; no main merge/issue closure automatic.

Expected computational workload is limited to a few thousand legal exact two-type fiber assignments across 172 genuine source transversals for both schemes, not full 15! physical permutations and not a full C(425,6) W(3,4) scan.

**Scientific status:** conditional all-h theorem + finite exhaustive radius-four zero-feasibility relative to pinned S68/S72. No universal \(\Omega(s^6)\) bound, no infinite correlated Branch B, no new total R3/ASET exponent.
