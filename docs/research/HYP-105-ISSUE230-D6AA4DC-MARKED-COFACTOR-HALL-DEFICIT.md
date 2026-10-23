# HYP-105 / #230 — AA4-DC: exact ORIGINAL marked source cofactor/Hall-deficit identity and all-h quantitative alternative

**SCIENTIFIC DRAFT; scoped partial theorem, NOT an A/B/C solution.** Strict child of [AA4-DB #628](https://github.com/definitely-stable/Mathlab/pull/628) with frozen parent HEAD `ca8f860a763581d107dd851b3918cf4a339e55c3`. Genuinely ORIGINAL symplectic W(3,2^h), six distinct immutable source incidence IDs, complete globally injected typed f,g into MINIMAL physical K_a with unrestricted cross-map correlation, and all seven historical GF(5) classes unchanged.

## 1. Precise unsolved obstruction after AA4-DB

AA4-DB proves for every dyadic h>=96, every original host and arbitrary complete correlated f,g, every pair of halfcuts X,Y of size k=floor(a/2): at least `s^7/2^15` genuinely ORIGINAL crossing incidence-flag mass across distinct actual nonincident original P3 anchors p--l0--q--l. Both physical images f(p),f(q) and g(l),g(l0) are disjoint, every counted original crossing SOURCE point-spoke i to SOURCE line-spoke j survives both doubled-image exclusions, and BOTH spokes participate in at least one ACTUALLY occupied physical C4 source-factor completion on their respective typed maps. However, this does NOT imply the other original factors in the paired C4 triples have a genuine source perfect matching.

Our selected next mathematically meaningful step is to identify the missing source correlation **exactly** and reduce each potentially accepted original B/B-overlap six-ID motif to a unique TRUE source 2×2 incidence cofactor. We do not falsely promote one crossed original flag to a source 3-matching.

## 2. Original matrix theorem, all h>=1 (no probability or random maps)

Take one actually occupied point physical C4 completion triple P={p0,p1,pc}, ordered with the TWO genuine ORIGINAL point spoke factor IDs p0,p1 first and one genuine ORIGINAL point physical center factor pc last; similarly L={l0,l1,lc} for the original LINE factor pair map g. All six ORIGINAL source factor IDs are distinct by globally typed injection (three in each separate type). Original GQ incidence matrix B[P,L] is the ACTUAL 3×3 binary matrix of incidence in genuine W(3,s). Its source bipartite incidence graph is a FOREST on these six vertices: genuine source GQ incidence girth is EIGHT, whereas every cycle on a 3+3 bipartite graph has length at most six.

In particular, `per_3(B)∈{0,1}` (two different perfect matchings would create a C4 or C6). For each **spoke-to-spoke genuine ORIGINAL incidence** B_ij=1 with i,j∈{0,1}, let `c_ij=per_2(B with row i and column j deleted)`. Then `c_ij∈{0,1}`, and `B_ij*c_ij=1` **if and only if that very original spoke-spoke incidence extends to the UNIQUE true original 3×3 perfect matching**.

Define for this one pair of physically OCCUPIED C4 source triples

```
t(B) = sum_(i,j<2) B_ij                                      (MARKED source crossflags)
e(B) = sum_(i,j<2) B_ij per_2(B without row i/col j)         (EXTENDIBLE true crosses)
d(B) = t(B)-e(B) >=0.                                        (SOURCE cofactor deficit)
u(B) = per_3(B) ∈{0,1}.                                    (historical actual 3matching)
```

A true original perfect matching uses **at least ONE** spoke↔spoke incidence: two point spokes cannot both match the single line center. It uses **at most TWO**: there are only two line spokes. Therefore for EVERY actual true-original C4 pair

```
t(B) = d(B)+e(B),       u(B)<=e(B)<=2u(B).                  (DC.1)
```

Crucially, when u(B)=1, *additional marked crossing flags not belonging to the unique matching* may still contribute to d(B). Therefore d is a **marked 2×2-COFACTOR deficit**, not merely the number of ZERO-permanent C4 pairs.

Exact independent source Hall defect: if u(B)=0, Hall's theorem says a nonempty subset of original point factors has fewer true-original line neighbors than its cardinality; at size 3 the obstruction is either an isolated point or a pair of points whose combined original neighbors have size <=1 (or a missing full line neighborhood). This is a genuine ORIGINAL source-incidence Hall witness, not synthetic physical neighbor incidence. A positive marked source flag, even with all six source factor vertices individually nonisolated, can coexist with a zero true-original 3matching: binary forest
```
[[1,0,0],
 [1,0,0],
 [1,1,1]]
```
has two genuine-looking marked flags, all six point/line vertices nonisolated, no 4/6 cycle, and fails Hall for the first two point source factors. This is a **combinatorial obstruction pattern** compatible with genuine source GQ girth; asserting it occurs at a specific actual W(3,s) physical completion requires independent original finite evidence. AA4-CV already has an actual infinite original single-anchor zero-matching family, but without forcing marked flags.

## 3. NEW exact ORIGINAL historical B/B-overlap marked-cofactor energy reduction

For the SAME one globally fixed complete original f,g and any set of genuine nonincident original source p,l anchors (or all in physical halfcuts), enumerate ALL paired physically occupied original C4 completion triples of AA4-CR, with NO redraw and true six original flags. Define sums T,E,D,U of t,e,d,u over these actual C4 pairs. When enumerating ALL C4 triples with no artificial sampling, `U=U_BBo(f,g;X,Y)` is **exactly the number of accepted historical original B/B-overlap six-flag Q sets with anchors in the cuts**, because AA4-CR established an exact source-3path→physical C4×C4 matching bijection with no duplicate true ORIGINAL Q.

Summing DC.1 gives the new anchored exact identity

```
T = D + E;     U_BBo <= E <= 2U_BBo;
therefore            D+U_BBo <=T<=D+2U_BBo.            (DC.2)
```

Also count `T_support`: the number of DISTINCT actual anchored true-original spoke-to-spoke incidence flags (p,l;i,j) for which there EXISTS at least one paired occupied physical C4 completion containing both source spokes. Because T sums marked real-source flags over *each* valid completion PAIR, `T>=T_support`. For **ALL original cut anchors**, AA4-DB's new `T_BOTH_C4` counts exactly `T_support`. Thus for **EVERY** dyadic h>=96 and arbitrary fully complete globally injected correlated f,g and any physical halfcuts,

```
D(f,g;X,Y) + 2 U_BBo(f,g;X,Y)
     >= T(f,g;X,Y)
     >= T_support(f,g;X,Y)
     >= s^7/2^15.                                     (DC.3)
```

**Consequently an exact quantified ALL-h ALTERNATIVE** (h>=96, each individual legal f,g and physical halfcuts):

```
EITHER     U_BBo(f,g;X,Y) >= s^7/2^17,
OR         D(f,g;X,Y)    >= s^7/2^16.                (DC.4)
```

Proof: if U is below one quarter of the `s^7/2^15` candidate mass threshold then `2U` is below half, forcing D >=half. There is NO lower bound on U in the second alternative. The theorem does **NOT** close Branch A or B or C for all seven GF5 classes, but isolates the exact outstanding SOURCE obstacle as a macroscopic true-original marked-cofactor/Hall deficit. An original sixflag B/B-overlap count is a positive class of historical S; knowing either OR without forcing first OR or compensating second OR **does not prove** an S lower.

## 4. Why this is a genuine research step, not new Hall's theorem

The Hall theorem, permanent Laplace cofactor identity, and GQ incidence girth8/acyclic 3+3 graph are classical. The contribution is **scoped exact accounting** that links AA4-DB's genuinely occupied *two-C4 SAFE original source flag mass* to the specific historical accepted original sixflag B/B-overlap U, with an unusually tight factor 2 and an explicit ALL-map all-h (but unresolved) quantitative alternative.

The new defect D is an operational target that can be audited on actual correlated global embeddings. A future proof MUST show D cannot dominate for all maps, or else that the large D forces enough TRUE ORIGINAL incidence contribution among the OTHER six historical GF5-positive classes. Mere source spoke incidence, physical four-cycles, matrix rank or girth8 **cannot** replace this last missing source matching argument.

## 5. Three independent source tests and exact-head acceptance gates

- `research/hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit.py`: actual ORIGINAL source incidence matrices of occupied C4×C4 triples; marked 2×2 cofactors, source row Hall-witness and the exact T=D+E, U<=E<=2U identity. Reject synthetic fake 3×3 incidence cycles of length 4/6. Distinguish marked-cofactor deficits on ZERO-matching vs already MATCHING physical C4 pairs.
- `research/test_hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit.py`: exhaust all 512 binary 3×3 candidate matrices and retain only original-GQ-girth admissible forests, compare cofactors against independently enumerated actual row/line permutations; assert there are all-nonisolated Hall-defective marked forests. For true W32 lex/S72 three halfcuts, compare the COMPLETE actual original historical Q count against existing independent AA4-CR original `original_BBo_exact_three_matching_transfer`, and check that DISTINCT anchored marked crossflags support equals independently computed AA4-DB BOTH-C4 source flag mass. For true W34 lex/random chosen fixed genuine source anchors, compare all candidate paired physical C4s, exact E/D/T and U against TWO differently implemented enumerators (independent source permutation and AA4-CR canonical accepted Q). W38 lex/random explicitly PARTIAL at most eight chosen actual C4 triples per side and four real source anchors, not presented as exhaustive original GF5 Q. Big exact integer h1..110 all-h dichotomy thresholds, fail-closed wrong typed source labels or malformed matrices/cuts/sampling.
- Dedicated isolated GitHub-hosted workflow with six jobs MUST be all SUCCESS on current exact PR HEAD; Proof Audit, INDEX and Full Research inspected separately. Neither finite tests nor a green CI constitute an independent qualified mathematical referee. Draft remains additive and unmerged.

Prior art: [Hall's marriage theorem](https://discrete.openmathbooks.org/dmoi4/sec_matchings.html) and classical generalized quadrangle girth8; see Brouwer–Haemers *Spectra of Graphs* (2012). No broad new standalone marriage theorem claim.

**ROOT #230 remains `OPEN_WITH_FORMAL_BLOCKER`.** Next AA4-DD should estimate the true ORIGINAL marked-deficit D in terms of actual source-incidence projection tensors, or prove crossclass GF5 compensation of D on the SAME frozen global f,g. Any claimed root A must be a uniform actual all-seven S>=c s^6 proof (not only the conditional DC.4 alternative). Independent qualified scientific review and frozen ancestors required before merging scientific Draft.
