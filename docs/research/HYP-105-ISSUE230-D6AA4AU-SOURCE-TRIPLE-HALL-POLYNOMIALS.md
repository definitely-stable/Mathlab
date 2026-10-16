# HYP-105 / issue #230 — AA4-AU: exact four-sector ORIGINAL 3×3 Hall polynomials and the six source threeflag motif census

**Research-only. Strict Draft child of AA4-AT #551, parent frozen at \`c8d0c9acf1fac141fcda063eea9a5f7e2c22939e\`.** This research concerns genuine ORIGINAL symplectic W(3,s), s=2^h≥2, with fixed separate globally injected point and line physical factor image maps f,g. Every true original source Q contains six DISTINCT actual point-line incidence flag IDs. No physical map is sampled again after selecting an original wedge. The issue #230 universal seven-GF5 positive sixset inequality S_s(f,g)=Omega(s^6), and the issue's possible infinite counterfamily Branch B, remain OPEN.

## 1. Precise missing theorem after AA4-AT

AA4-AT proved each occupied residual three-point-factor/three-line-factor physical template pair has at most ONE genuine source Hall-compatible set of three added original incidence IDs, by the classical girth-eight original GQ forest. But its leaf-peeling algorithm left the original Hall indicator \`eta(A,B)\` as an algorithmic black box. AA4-AU extracts **four explicit, bounded-degree source incidence polynomials** for the entire exact local Hall gate, and then identifies a second genuine original triple population at order s^6 which exists without ANY physical randomization. The two results are deliberately not conflated: ORIGINAL source 3-flag abundance is not physically compatible good original D-wedge abundance, and a positive Hall polynomial is not final accepted seven-GF5.

Let \(V=(s+1)(s^2+1)\), \(d=s+1\), \(N=Vd\) be actual original source point count, line/point valency and original incidence-flag count. For a given actual pinned original 3-flag wedge w and one pair of globally occupied AA4-AS typed residual three-factor source multisets, let \(P\) be the original point-source factors (3 slots) and \(L\) be the original line-source factors (3 slots). Each type has either three distinct factors (A) or two factors with multiplicities 2+1 (B): three copies of one factor (C) cannot appear in the AA4-AS T/P physical 2-regular residuals. Construct the genuine original source binary incidence entry

    b(p,l) = 1 iff (p,l) is a TRUE ORIGINAL W(3,s) incidence flag
                      AND its ID is NOT among the three pinned flags;
             = 0 otherwise.

All expressions below use the SAME actual original source incidence b and same globally fixed f,g that selected P,L.

## 2. NEW exact all-h FOUR original source Hall-polynomial formulas

The genuine original forest-Hall indicator \(\eta_w(P,L)\) equals exactly one of the following algebraic integer polynomials:

**A/A — three different original points p1,p2,p3, and three different original lines l1,l2,l3:**

\[
\boxed{\eta_{AA}=\sum_{\pi\in S_3}\prod_{i=1}^{3} b(p_i,\ell_{\pi(i)})}.
\]

This is the permanent of the TRUE ORIGINAL pinned-excluded 3×3 incidence submatrix, computed as SIX 0/1 triple products. It takes value 0 or 1: two distinct perfect matchings in one bipartite graph would create an alternating C4 or C6, impossible in the actual original GQ's incidence forest.

**A/B — three original points p1,p2,p3; repeated original LINE \(\ell_2\) occurring twice and single line \(\ell_1\) once:**

\[
\boxed{\eta_{AB}=\sum_{i=1}^{3} b(p_i,\ell_1)\prod_{j\ne i}b(p_j,\ell_2)}.
\]

Each term assigns the single line to one original point and assigns the repeated line to two DIFFERENT remaining original point factors; source factor repetition is allowed, repeated use of the SAME original incidence flag ID is NOT. Two terms simultaneously positive would give four ORIGINAL source incidences forming a forbidden C4.

**B/A — repeated original POINT \(p_2\) occurring twice, single point \(p_1\) once; three distinct original lines \(\ell_1,\ell_2,\ell_3\):**

\[
\boxed{\eta_{BA}=\sum_{i=1}^{3} b(p_1,\ell_i)\prod_{j\ne i}b(p_2,\ell_j)}.
\]

This is the exact point-line dual of A/B and is likewise 0 or 1 in a genuine W(3,s).

**B/B — repeated original point p2 and repeated original line l2, plus single p1 and single l1:**

\[
\boxed{\eta_{BB}=b(p_2,\ell_2)\,b(p_2,\ell_1)\,b(p_1,\ell_2)}.
\]

The only possible three-source-incidence configuration is the REAL original three-edge point-line PATH P4 through central original flag (p2,l2). The source point p2 is incident with two distinct source line factors, and l2 with two distinct point factors. The physical factor's two occurrences are different **actual original source incidence FLAG IDs**. The forbidden fourth corner (p1,l1) need not be tested: if it existed, the real original GQ would contain a C4; such an extra source incidence is impossible on these four ORIGINAL source factors.

All four polynomials are **exact source forest-Hall indicators \(\eta\in\{0,1\}\)** in real W(3,s), not a probabilistic lower bound. A fake K2,2 or sixcycle source incidence input with two matching terms is detected and rejected, never treated as original W(3,s). Even true eta=1 needs full six-ID source flag completion, source factor physical compatibility and final seven-GF5 classification to count for the original hypothesis.

This refines AA4-AT's same-genuine-source forest leaf algorithm with explicit formulas and isolates exactly which ORIGINAL incidence products must be forced positive in an eventual globally correlated all-f,g Hall density proof. The formulas also validate source factor multiplicities B without any illicit original incidence flag duplication.

## 3. NEW all-h FULL genuine-original three-flag source motif population theorem

Consider ALL unordered THREE-DISTINCT-INCIDENCE-ID original source flag subsets \(\{e_1,e_2,e_3\}\) without any physical f/g conditions yet. There are exactly SIX possible original source factor multiplicity classes:

| Source point / line multiplicity | True original source three-incidence structure | EXACT all-h cardinality |
|---|---|---|
| A/A | Three independent point-line incidence edges (3-matching) | \(\binom N3-2V\binom d3-2V\binom d2(N-3d+2)-N(d-1)^2\) |
| A/B | Two flags on one original line, third on NEW point and NEW line | \(V\binom d2(N-3d+2)\) |
| B/A | Same original pattern, point-line dual | \(V\binom d2(N-3d+2)\) |
| B/B | Genuine original three-incidence P4 path; center one original flag | \(N(d-1)^2=N s^2\) |
| A/C | Three original flags incident with the SAME line | \(V\binom d3\) |
| C/A | Three original flags incident with the SAME point | \(V\binom d3\) |

They partition **exactly** all \(\binom N3\) unordered distinct original flag triples. No residual other case, including B/C or C/C, can occur with distinct original flag IDs: if all three flags use the same original line, they necessarily have three DISTINCT original points, and conversely. The classes reflect source incidence structure, NOT the later GF5 seven-class selection on SIX flags.

**Proof independent of physical labels:** A/C and C/A choose the central original factor among V and three distinct original incidences among its d source neighbors: V*C(d,3). For A/B, choose the repeated ORIGINAL line among V and TWO different incident original points among d, then choose a THIRD true original incidence flag whose point is different from both chosen source points and whose line differs from repeated line. There are EXACTLY \(N-(d+2(d-1))=N-3d+2\) such original source flags, because source point degrees and line degrees are d and the two selected source points belong to the repeated line. B/A is dual. For B/B, choose the UNIQUE original middle incidence flag (p,l) of the 3-edge P4 path among N genuine source flags. Pick one of the d-1 other genuine original point neighbors of l and one of the d-1 other line neighbors of p. Their three distinct source incidence flags determine a unique B/B 3-edge source P4; the central edge is uniquely characterized by being incident with both source factors of multiplicity two. Total exactly \(N(d-1)^2\). A/A is the remaining complement inside all \(\binom N3\) distinct source flag triples. No random original source relabel, no physical image assumption.

**Important unconditional corollary:** In REAL ORIGINAL W(3,s), independently of arbitrary later physical maps f,g,

\[
\boxed{\#\{\text{three-edge ORIGINAL source B/B P4 paths}\}
 = (s+1)^2(s^2+1)s^2\ \ge\ s^6.}
\]

This is an **all-h positive ORIGINAL SOURCE three-flag population** of order s6, separate from the AA4-AR globally guaranteed good physical D-graph wedges of order s6. It is NOT an all-global physically complementary B/B wedge lower, because the physical overlap constraints involving f,g can destroy eligible ports, and is NOT the original seven-GF5 selected six-ID S_s lower. Never present original source P4 mass as accepted original GF5.

For s=2, actual original W(3,2): N=45, original source factor profile counts [A/A=10560, A/B=1710, B/A=1710, B/B=180, A/C=15, C/A=15], total C(45,3)=14190. For s=4, actual original W(3,4): N=425, [11995200,350200,350200,6800,850,850], total C(425,3)=12704100. These are source populations, not numerically observed accepted GF5 sixclasses.

## 4. Independence, exact arithmetic and full-genuine-source validation

Versioned \`research/hyp105_issue230_d6aa4au_source_triple_hall_polynomials.py\` implements:
1. \`exact_original_threeflag_Hall_incidence_polynomial\`: independent of AA4-AT forest leaf method, with separate four-pattern candidate edge-product expansion and source pinned exclusion. Produces EXACT canonical six-original-ID Q or None; any multiple-match fake C4/C6 original source adjacency is rejected rather than falsely accepted. Pattern A/A permanent six terms, A/B and B/A three terms each, B/B one forced term;
2. \`all_h_original_threeflag_source_motif_population\`: exact arbitrary-power-of-two closed original source triple population using only genuine GQ counts V,d,N. Uses large Python integers only; does NOT materialize gigantic fake W3s;
3. \`literal_true_original_W32_source_threeflag_motif_census\`: independently enumerates all 14190 source incidence flag triples in genuine W32 and checks all six multiplicity class integers, not using the symbolic formula for counting;
4. \`literal_true_original_source_BB_P4_audit\`: independently enumerates EVERY genuine original source B/B P4 triple in genuine W32 or W34 starting from original central incidence flags, checks both source point and source line repetition and unique Q identity; counts 180 in W32 and 6800 in W34;
5. \`literal_true_original_source_AB_audit\`: independently starts from pairs of true original flags on the same source line then scans a third genuine flag on new original point and line; checks all exact 1710 W32 and 350200 W34 source A/B triplets.

The separate independent verification \`research/test_hyp105_issue230_d6aa4au_source_triple_hall_polynomials.py\` compares, ON EACH globally occupied AA4-AS original typed residual threefactor point+line physical pair, **THREE mathematically different genuine original source Hall methods:** new direct Boolean four-sector polynomial; AA4-AT point-line original incidence FOREST LEAF pruning; historical AA4-AS 3! original point-line factor slot permutational Hall. Every method must produce the SAME true six original incidence flag ID Q or NONE. For all FIVE globally bijective genuine W32 fixed physical point/line map pairs (dual-zero, lex, reverse, S68, S72), examine EVERY GOOD two-typed opposite source 3-flag wedge and ALL its globally occupied physical template pairs; total original source Hall incidence charges must remain previously verified 150,505,232,46,85 respectively. Audit pattern-typed numbers A/A, A/B, B/A and B/B separately; freeze exact values from independent hosted CI rather than guessing.

On real W34 symplectic GF4 with global physically injected K14 typed maps lex/random (six missing physical image edges each), restrict to ONE genuine independently accepted original source D6 six-ID Q and its pinned opposite wedge per scheme, then compare all occupied residual pairs under all three source Hall methods and retain known 11/12 true original Hall Q among 11025/13200 physical templates. No full W34 original seven-GF5 census claimed. True original symplectic automorphisms and separately typed physical coordinate permutations preserve every four-case source polynomial Hall outcome distribution; forged original source models, unphysical source factor slots and fake C4/C6 sources rejected in intended test scope.

## 5. Novelty / scientific boundary and next AA4-AV gate

The GQ girth-eight incidence condition and forest uniqueness (AA4-AT) are CLASSICAL. The fact that a forest 3×3 permanent has at most one nonzero term and standard path/star counts are classical combinatorial observations, **not invented by this project**. AA4-AU's research contribution is the explicit original globally correlated source Hall polynomial transfer aligned with AA4-AS real three-pinned-flag residual physical templates, independent source-Hall Boolean verification and exact genuine W3 all-h six-sector SOURCE triple population with an unconditional B/B source P4 s6 lower. It is a closed-form SOURCE incidence gate and an exact source population accounting step, **NOT a solution of original HYP-105 #230**.

The genuine difficult remaining theorem is still to force **enough of the source-incidence-polynomial successes to occur INSIDE allowed, physically opposite, not-T/T AA4-AR good original wedges** and to pass final seven-GF5 selected Q. Large unconditional SOURCE P4 population alone does not imply surviving physical f,g correlations. If these positive fractions cannot be proved for all f,g, investigate genuine correlated all-h original counterfamily, or independently prove lower bound for positive zero-good-wedge sixclass U that the whole wedge method does not cover. No invented absolute lower for accepted original sevenclass S_s is warranted.

Maintain strict stacked Draft child atop AA4-AT #551, original #230 OPEN, no main merge, full Hosted dedicated/INDEX/Proof Audit/Full Research exact HEAD and independent mathematical referee separate.
