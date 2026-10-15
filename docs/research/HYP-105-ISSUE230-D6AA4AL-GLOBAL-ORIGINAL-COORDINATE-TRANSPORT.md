# HYP-105 / #230 — AA4-AL: global ORIGINAL point–line coordinate transport and pair-energy frontier

**Research-only Draft stacked child of [AA4-AK PR #524](https://github.com/definitely-stable/Mathlab/pull/524).** Parent pinned exact HEAD \`07999e7dd318ec8a2a0d30e37d258bd9ec6a8488\`. All mathematical quantifiers are over the ACTUAL classical symplectic generalized quadrangle W(3,s), s=2^h>=2, with V=(s+1)(s²+1) REAL point sources, V REAL line sources, N=(s+1)V REAL incidence flag IDs, and two independently TYPED but globally fixed complete injective physical unordered-edge maps f,g into minimal physical K_a with a=min {a:binom(a,2)>=V}. NO map re-drawing per flag/selected Q. NO all-map Omega(s^6) seven-GF5 six-incidence theorem, no Branch B, no ASET exponent. Separate independent referee still required before mathematical acceptance, generated catalogs or merging.

## 1. Why this is the next mathematical step, distinct from the earlier AA4-I spectrum

AA4-AH through AA4-AK EXACTLY decompose true original B/A and A/B six-incidence ID Q into all four possible physical A sectors and give O((s+1)²) genuine-Hall UPPER bounds per real original rooted first-side physical C4. They give no ALL-f,g positive true original LOWER when globally correlated maps vary adversarially.

Earlier \`research/hyp105_issue230_d6aa4i_original_spectral_coordinate.py\` already proves an all-map Omega(s^5) obstruction comparing **one typed source collinearity graph to same-type physical centers**, and uses the classical original incidence spectrum to bound a SAME-center point–line cut. Do not rename or claim that work as new.

**New AA4-AL object**: a single ALL-POINT-COORDINATE by ALL-LINE-COORDINATE transport matrix \`M=F^T B G\` retaining the TWO physical maps and ALL actual ORIGINAL incidence flags simultaneously, not one same-center cut. It admits an exact new GLOBAL Cauchy/ANOVA lower for genuinely ORIGINAL flags with **both different point and different line source IDs**, a corresponding exact source-degeneracy subtraction, plus a rigorous diagnostic that elementary one-cell spectral mixing cannot certify even one incidence in any individual physical-center-pair fiber.

## 2. Main theorem — universal ALL-f,g order s^5 compatible-original-FLAG-PAIR lower

Let \`B[p,l]=1\` iff the REAL ORIGINAL W(3,s) point p lies on source line l. Let \`F[p,c]=1\` iff physical coordinate c belongs to the globally injected original POINT label f(p), and \`G[l,e]=1\` iff physical coordinate e belongs to the globally injected original LINE label g(l). Every row of F and G has exactly TWO 1s, and any two DIFFERENT rows in one map have physical intersection cardinality at most ONE, because an unordered physical pair is globally injected.

Write \`d=s+1\`, \`N=Vd\`, and the ACTUAL original source/physical transfer

    M[c,e] = ∑_{(p,l)∈I(W3s)} F[p,c] G[l,e] = (F^T B G)[c,e].

Every genuine original flag contributes exactly FOUR physical coordinate cells, hence exact invariant

    ∑_{c,e} M[c,e] = 4 V d.

Define \`D(f,g)\` as the ORDERED count of pairs of TWO DIFFERENT actual original flag IDs (p,l),(q,m) satisfying ALL:

    p != q,  l != m,
    f(p) ∩ f(q) != ∅,
    g(l) ∩ g(m) != ∅.

Because f and g are individually globally injected unordered-pair maps, both physical intersections have size EXACTLY one. Therefore \`D(f,g)\` counts each qualifying ORDERED original two-flag pair exactly once (not a fiber-orbit quotient).

Define \`bad_P\` as the subset of ordered distinct flag pairs in the M-energy sharing their ACTUAL original point ID, and \`bad_L\` those sharing their ACTUAL original line ID. No distinct pair of ORIGINAL incidence flags can share both point and line IDs. If \`r_p(e)=#{l ∈ N(p):e∈g(l)}\` and \`r_l(c)=#{p∈N(l):c∈f(p)}\`, exact source-degeneracy subtraction is

    bad_P = 2 ∑_p∑_e r_p(e)(r_p(e)-1),
    bad_L = 2 ∑_l∑_c r_l(c)(r_l(c)-1).

The factor TWO arises from the two physical coordinates in a fixed source point or line label. Thus the exact ALL-f,g identity

    D(f,g) = ∑_{c,e} M[c,e]^2 - 4 V d - bad_P - bad_L.

Why the TRUE original regular degree and global physical injection matter: for every ORIGINAL point p, the d distinct actual incident SOURCE lines have d different physical pair labels. Each pair of those labels can meet at MOST one physical coordinate. Therefore \`∑_e r_p(e)(r_p(e)-1)≤d(d-1)\` and \`bad_P≤2Vd(d-1)\`. By GQ point/line duality the same is true for \`bad_L≤2Vd(d-1)\`. This does NOT require f and g to be statistically independent.

By global Cauchy on the a² real physical cells,

    ∑ M² ≥ (∑M)^2/a² = 16 V² d²/a².

Combining the exact source-degeneracy identity gives the new EVERY-global-MAP original-source-pair theorem:

    D(f,g) ≥ 16 V² d²/a² - 4 V d²
           = 4 V d² (4V/a² - 1).

For s=2, V=15,a=6, 4V/a²=5/3>3/2. For s>=4, V≥85⇒a≥14. Since a is MINIMAL, V>binom(a-1,2), hence

    4V/a² > 2(a-1)(a-2)/a²
           =2-6/a+4/a²
           ≥2-6/14 >3/2.

Therefore **ALL h≥1** and ALL complete globally injected f,g,

    D(f,g) > 2 V(s+1)² ≥ 2 s^5.

D is ORDERED; unordered genuine original two-flag compatible pairs have at least s^5 as a guaranteed integer lower (ceil where necessary). The leading asymptotic in the exact rational lower is

    16V²d²/a² -4Vd² = (4+o(1))s^5.

This is a **new global point–line jointly physical coordinate-collision guarantee**, not the earlier one-type original collinearity result. Cauchy itself is textbook mathematics and not claimed novel; the new specialized claim is its all-f,g true-original-source exact globally coherent two-physical-map contraction with both source-degenerate corrections.

## 3. Stronger exact two-margin physical-degree transport energy

For each physical POINT coordinate c let \`t_c=# {p:c∈f(p)}\`; for each physical LINE coordinate e let \`u_e=# {l:e∈g(l)}\`. Since every original source factor has exactly two physical coordinates, \`∑t_c=∑u_e=2V\`; and because the TRUE original incidence source is degree d on BOTH types,

    row_sum_c(M) = 2d t_c,
    col_sum_e(M) = 2d u_e.

Use orthogonal row/column ANOVA (valid for ANY real a×a matrix) to obtain the stronger exact-energy lower

    ∑ M² ≥ [∑ row_sum_c² + ∑ col_sum_e²]/a
           -(4Vd)²/a².

Equivalently, introducing \`t̄=ū=2V/a\`,

    ∑ M² ≥ 16V²d²/a²
             + (4d²/a)[∑_c(t_c-t̄)² +∑_e(u_e-ū)²].

Thus

    D(f,g) ≥ 16 V²d²/a² -4Vd²
             + (4d²/a)[∑(t_c-t̄)²+∑(u_e-ū)²].

Any uneven physical coordinate coverage under either global injection contributes a rigorously NONNEGATIVE improvement to the original two-type flag-pair collision lower. An exact missing-edge palette with m=binom(a,2)-V can be used to compute those physical fiber degrees; the proof never assumes global physical surjectivity.

The practical computable certificate also subtracts the **ACTUAL exact bad_P and bad_L**, often significantly smaller than the crude 2Vd(d-1) maxima. Independent direct original flag-pair enumeration verifies exact equality, not merely the bound.

## 4. The spectral frontier: why single-cell expander mixing cannot bridge to original Hall

Classical generalized quadrangle (GQ) collinearity is strongly regular with \`(V,k,lambda,mu)=((s+1)(s²+1),s(s+1),s-1,s+1)\`. For its actual ORIGINAL incidence matrix B,

    B B^T = d I + A_P,

where A_P is original point collinearity. Hence EXACT squared singular spectrum

| B singular value squared | Multiplicity |
|---|---:|
| (s+1)² | 1 |
| 2s | s(s+1)²/2 |
| 0 | V-1-s(s+1)²/2 |

This is known classical GQ/spectral graph machinery and was already used in earlier AA4-I; we restate it to audit the NEW ALL-COORDINATE matrix, **not** as a novel general spectral theorem. It yields for arbitrary TRUE original point subset X and true original line subset Y of sizes t,u the conventional bound

    |I(X,Y) - d t u/V|
       ≤ sqrt(2s*t*(1-t/V)*u*(1-u/V)).

A single physical coordinate fiber has t,u≤a-1 (an injected original physical K_a edge-label family uses at most one edge from each physical endpoint to any other physical coordinate). The spectral LOWER

    d t u/V -sqrt(2s*t*(1-t/V)*u*(1-u/V))

is nonpositive for EVERY feasible physical center cell, because

    d²(a-1)² ≤ 2s (V-a+1)².

For s=2 check V=15,d=3,a=6: 225≤400. For s≥4, the minimal physical alphabet satisfies a-1≤s², d=s+1≤5s/4, V-a+1≥s³, so d²(a-1)²≤(25/16)s^6≤2s^7≤2s(V-a+1)². By monotonicity the same obstruction holds for any smaller fiber cardinalities t,u≥1; for t=0 or u=0 the lower is zero.

**NO-GO scope:** Using only THIS standard point/line spectral mixing lower for each individual coordinate-center-pair cannot prove a single genuine original source incidence in ANY selected one cell, much less the four-row Hall positivity of physical B/A. It does NOT prove that the actual cell M[c,e] is zero, and does NOT rule out stronger global spectral tensor/energy inequalities coupling MANY physical center cells. Indeed the new second-moment theorem above proves Ω(s^5) global TRUE original distinct flag PAIRS precisely by such multi-cell accounting.

### Prior-art check (independent external source)

Classical W(q) incidence spectral statements in this slice are NOT claimed new. In particular, Michael William Newman's 2004 University of Waterloo PhD thesis *Independent Sets and Eigenspaces*, Section 3.12, printed pp. 52–53 (PDF pages 63–64), explicitly derives the generalized-quadrangle identity \`N²=(q+1)I+A\`, the SRG equation \`A²=(q²−1)I−2A+(q+1)J\`, the two nontrivial original collinearity eigenvalues \`q−1\` and \`−q−1\`, and \`N²\` squared eigenvalues \`(q+1)²,2q,0\`. This is a direct literature precedent for the spectral input, independently checked here against actual finite ORIGINAL GQ matrices without treating it as a new spectral theorem.

- [Michael William Newman, *Independent Sets and Eigenspaces*, University of Waterloo (2004), original thesis PDF](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/3609ef01-c1e4-44a5-9d01-66a495af811b/content).
- [Generalized quadrangle point-graph eigenvalue derivation, UCSD lecture notes, pp. 17–18](https://www.math.ucsd.edu/~jmoneill/abacus_winter2020.pdf).

New AA4-AL content remains only the specialized TWO-TYPED-global-physical-map ORIGINAL \(F^T B G\) pair-energy source-degeneracy identity, its deterministic \`D>=2s^5\` lower and exact ANOVA variance strengthening, and the precise no-lift warning to #230 seven-GF5 sixsets.

## 5. Precise GF5 six-ID barrier and non-equivalence statement

An ordered pair of genuine original source flags counted in D uses distinct point and line source IDs with at least ONE common physical point-coordinate and ONE common physical line-coordinate. This is a valid TRUE original two-flag incidence configuration under both same global maps. It is NOT necessarily a selected positive GF5 six-flag configuration; THREE chosen original flags sharing a single physical coordinate already violate the degree-two rule of six-physical-coordinate GF5 A patterns. Also the four-sector AA4-AK Hall decompositions require one genuine source doubled B center, four source singleton factors in an occupied physical C4 and additional TRUE original opposite-factor assignments. D counts a different two-ID coincidence and provides no automatic extension through the stringent globally correlated 4-row source Hall gates.

Consequently \`D>=2s^5\` is a valid all-f,g progress theorem on a NEW global invariant, but **does not establish the issue #230 Branch A S_s>=c*s^6, nor its negation/Branch B**. To obtain an equivalent model-reduction Branch C would require a rigorous lifting/charging lemma from distinct two-flag bilateral coordinate collisions to the complete seven positive GF5 six-ID families, with collision multiplicity controls. No such lemma is asserted or silently assumed.

**Next mathematical frontier AA4-AM:** Build the EXACT local-to-global extension/charging incidence tensor of one D-counted two-flag pair into real accepted six-ID B/A,A/B (four-sector AA4-AK), D6 and other five GF5 classes; seek a lower on extendible pairs with an explicit bound on the number of extension witnesses charged to one accepted six-Q. As a falsification route, exhibit full globally injected f,g with many D pairs that are NOT extendible into ANY of the seven positive six-GF5 classes. Only such a new lifting theorem or infinite all-label obstruction would advance Branch A/B/C beyond an auxiliary invariant.

### Finite full-global exact source evidence and direct lifting obstruction

The first GitHub-hosted dedicated [AA4-AL run #38782843269](https://github.com/definitely-stable/Mathlab/actions/runs/38782843269) independently enumerated every unordered pair of TRUE ORIGINAL W(3,2) incidence flag IDs under five different complete globally injected SAME f,g maps and W(3,4) under two globally injected SAME f,g maps with K14 physical holes. It cross-checked the literal source-flag oracle (does not form M) against the exact original F^T B G matrix-source degeneracy equality, all-marginal ANOVA and universal lower:

| ORIGINAL GQ | complete global typed f,g | unordered good source flag pairs D/2 |
|---|---|---:|
| W(3,2) | dual-zero full map from AA4-AI | **277** |
| W(3,2) | lex | **307** |
| W(3,2) | reverse | **300** |
| W(3,2) | S68 | **257** |
| W(3,2) | S72 | **261** |
| W(3,4) | lex, six physical holes per type | **6,529** |
| W(3,4) | random globally fixed full injection, six holes per type | **6,327** |

For W(3,2), a=6 and K6 has exactly 15 globally occupied original source factor physical edges on each type, so physical center fiber degrees are all exactly a-1=5: **the ANOVA imbalance improvement vanishes**, making this an important zero-variance baseline. The uniform global lower is D>=360 ORDERED, i.e. at least 180 unordered; the actual respective D above are 554, 614, 600, 514 and 522 ordered, satisfying it without pretending to be tight.

For W(3,4), a=14, V=85, physical K14 has 91 pairs, so exactly six missing physical point-side images and six missing physical line-side images under either map. The chosen lex map has center-fiber sizes (13,13,13,13,13,13,13,13,13,13,10,10,10,10) on both types, and the random map has nonuniform distinct point and line fibers. The nonnegative ANOVA correction is separately checked exactly.

**Concrete falsifier of a naive lifting lemma**: The very SAME full original W(3,2) dual-zero globally injected f,g maps giving **277** compatible genuine original two-flag pairs have **ZERO** accepted original B/A split-two-triangle Q **AND ZERO** accepted original A/B split-two-triangle Q, as independently exhaustively established in AA4-AI. Thus \`D>0\` (indeed large) cannot imply \`T_split_BA+T_split_AB>0\`, even for all genuine original source roots aggregated together. FULL accepted B/A and A/B on this map remain 46 and 61 and full seven-class S remains 123; this is explicitly **not a finite example with S=0 and not an infinite Branch B counterfamily**. Any useful AA4-AM lifting must account for all FOUR physical A modes and other five GF5/D6 tags, not only the split triangles.

## 6. Independent validation, publication and integration protocol

Versioned proof implementation:
- \`research/hyp105_issue230_d6aa4al_global_original_coordinate_transport.py\`: all-h symbolic exact rational theorem, all-f,g actual original F^T B G matrix and full source-degeneracy/variance certificate, finite true-original GQ BBT/SRG oracle, fully independent original two-flag brute oracle.
- \`research/test_hyp105_issue230_d6aa4al_global_original_coordinate_transport.py\`: tests five COMPLETE genuine W32 fixed global physical map pairs, actual true symplectic W34 with six missing physical unordered-pair images under two distinct lex/random full injections, actual exact BBT/SRG spectrum, source genuine symplectic transvection and two separately permuted physical type coordinates, forged source rejection, exact large-integer s=2^h h up to 50, no fake huge projective geometry.
- \`.github/workflows/hyp105-issue230-d6aa4al-global-original-coordinate-transport.yml\`: four GitHub-hosted jobs, exact final HEAD.
- This detailed structured proof.

Keep child PR **Draft** atop prior AA4-AK #524. Four-job dedicated, INDEX, Proof Audit, Full Research and independent mathematical referee required; no merge to main, no formal RCP accepted theorem JSON or bulk generated catalog regeneration until independent approval. Issue #230 **OPEN**. Classify theorem as an auxiliary ALL-f,g original-source pair-energy bound; do not brand it a full seven-family obstruction or an ASET result.
