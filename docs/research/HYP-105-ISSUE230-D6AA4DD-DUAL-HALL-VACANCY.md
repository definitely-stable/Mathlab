# HYP-105 #230 — AA4-DD: exact dual-invariant TRUE ORIGINAL four-class Hall-vacancy mass and a new uniform obstruction alternative

**Scientific DRAFT, scoped partial result, NOT a Branch A/B/C proof.**
Frozen strict scientific parent [AA4-DC #629](https://github.com/definitely-stable/Mathlab/pull/629) HEAD `92ed1a2fc5a20793f1d6511d4005ef601895cac4`.
The source is genuinely ORIGINAL symplectic W(3,s), s=2^h, all typed globally injected complete original point f and line g physical pair maps into the SAME minimal K_a, any f/g correlations. Exactly the same immutable six original incidence-ID subsets and seven historically accepted GF(5) motif classes as root #230; main remains untouched.

## 1. Re-evaluation: what AA4-DC has NOT proved

AA4-DC showed exact original occupied physical C4-pair marked-source incidence energy `T=D+E`, `U_BBo<=E<=2U_BBo` and a universal h>=96 `D+2U_BBo>=s^7/2^15` for EVERY correlated complete original factor map and any two physical coordinate halfcuts (original source *anchors* in cuts, all original physical completion triples enumerated). It gives

```
U_BBo>=s^7/2^17  OR  D>=s^7/2^16.                 (DD.0)
```

Finite true original W(3,4), eight selected ORIGINAL nonincident double-disjoint anchors under `lex` yielded T=9,971, E=82, D=9,889, U=60. It is therefore scientifically unjustified to set D=0, assume D=o(T), or infer any unrestricted BBo lower merely from a marked true original incidence and two physically occupied C4s.

New objective: represent EACH individual ORIGINAL source-cofactor failure by a precise **source factor/dual source factor vacancy**, with an exact balanced energy decomposition that does not depend on which of POINT or LINE is tested first. This is a refinement of the quantified open obstruction, not a claim that its mass is bounded above or compensated.

## 2. Original 2×2 source Hall-vacancy theorem AA4-DD.1 (every h>=1)

For one genuinely occupied original POINT physical C4 triple and LINE C4 triple on one genuine source P3 anchor, order the three TRUE original source point factor IDs as (p_spoke0,p_spoke1,p_center) and line IDs as (l_spoke0,l_spoke1,l_center). The actual original source incidence matrix B∈{0,1}^{3×3} has girth8, is acyclic on these six genuine original source factors, and `per3(B)∈{0,1}`.

Take a TRUE ORIGINAL marked incidence B_ij=1 between physical SPOKES i,j∈{0,1}. Its residual true-original 2×2 incidence matrix is formed from the other point spoke `1-i`, original point center `2`, other line spoke `1-j`, original line center `2`:

```
               LINE other-spoke  LINE center
POINT other-spoke     A               B
POINT center          C               D

cofactor c_ij = A*D + B*C ∈{0,1}.
```

**Lemma DD.1:** when `c_ij=0` the remaining 2×2 TRUE original incidence submatrix has at least one **zero row OR zero column**. This follows *exactly* from the 2×2 Hall condition: if both rows and columns had positive degree, there would be a perfect matching. The four possible original witness FACTORS are:

- `POINT_other_spoke`: other original POINT spoke is genuinely nonincident to BOTH remaining original LINE factors.
- `POINT_center`: original POINT C4 center is genuinely nonincident to BOTH remaining original LINE factors.
- `LINE_other_spoke`: other original LINE spoke is genuinely nonincident to BOTH remaining original POINT factors.
- `LINE_center`: original LINE C4 center is genuinely nonincident to BOTH remaining original POINT factors.

Multiple ORIGINAL vacancies can occur simultaneously (e.g. all-zero residual 2×2 gives four) and simply charging the first detected one would break exact POINT↔LINE symmetry. **No new original incidence edge may be inferred from the occupied physical C4 pair.** An absent edge is an absence in the true original W(3,s) source incidence relation.

Define for every nonextendible marked original crossing (i,j) its nonempty witness set `Z(B;i,j)` among these four types. Distribute exactly **one unit** of its original marked cofactor defect evenly across those types:

```
weight_t(B;i,j) = 1[t∈Z(B;i,j)] / |Z(B;i,j)|.
```

All denominators divide 12 (LCM(1,2,3,4)), so computer implementation stores integer TWELFTHS without floating point or uncontrolled rounding.

## 3. NEW exact dual-invariant four-class SOURCE defect identity

Sum `weight_t` over every actual occupied POINT physical C4 × LINE physical C4 ORIGINAL factor triple pair, every actual original SOURCE nonincident three-flag anchor, and every true ORIGINAL spoke-to-spoke incidence flag B_ij=1 with cofactor0, on one fixed full correlated f,g and physical cuts. For type t denote this nonnegative rational sum `D_t(f,g;X,Y)`.

**Theorem AA4-DD.2 (every h>=1, arbitrary actual original W(3,s), arbitrary globally correlated complete original f,g, any source-anchor cuts or subset):**

```
D= D_POINT_other_spoke + D_POINT_center
 + D_LINE_other_spoke + D_LINE_center,                  (DD.2)

T= E + sum_t D_t,       U_BBo<=E<=2U_BBo.              (DD.3)
```

Each term counts ACTUAL original source absence certificates on physical C4 original triple pairs; D_t is not a historical accepted GF5 positive six-original-incidence-ID motif, nor a disjoint count of distinct source Qs. T,D,E count **completion-pair multiplicities**, as in AA4-DC; never silently convert them to counts of unweighted distinct original incidence-ID sets.

**Exact dual invariance.** Swapping ORIGINAL POINT and ORIGINAL LINE types, swapping f and g, and reversing the original incidence relation maps each genuinely original source P3 to its genuine dual and transposes B. Hence

```
D_POINT_other_spoke(f,g)=D_LINE_other_spoke(g,f)^dual,
D_POINT_center(f,g)=D_LINE_center(g,f)^dual,
```

and conversely. U,T,D,E are unchanged under this full proper dualization with cuts/anchors swapped. The fractional split prevents arbitrary preferred typed orientation when an original cofactor has multiple vacancy witnesses.

## 4. New rigorous ALL-h quantified five-way alternative AA4-DD.3

For **EVERY** h>=96,s=2^h, genuine W(3,s), arbitrary full globally injected original typed f,g, arbitrary correlations and ANY two k=floor(a/2) physical halfcuts X,Y:

```
EITHER   historical U_BBo(f,g;X,Y) >= s^7/2^17,
OR       at least ONE typed original source Hall vacancy class
         D_t(f,g;X,Y) >= s^7/2^18.                      (DD.4)
```

**Proof:** Parent AA4-DC gave `D+2U_BBo>=s^7/2^15`. If the first branch fails, `2U_BBo<s^7/2^16`, so `D>s^7/2^16`. By the exact four-way identity DD.2 and pigeonhole, `max_t D_t>=D/4>s^7/2^18`. No independence, physical random labellings, original Sp(4,s) automorphism choice or finite-h extrapolation. The h>=96 threshold is inherited conservatively from AA4-DA and AA4-DB, not a new improved asymptotic threshold.

**CRITICAL ROOT NON-IMPLICATION:** DD.4 is an *either positive ORIGINAL BBo or large ORIGINAL zero-incidence obstruction* result, not a lower bound on any other historical positive GF(5) class. The large-vacancy branch may hold for every f,g without a positive BBo lower (unless one establishes a new compensation theorem on the SAME fixed global maps). This is NOT PROVED_A, COUNTEREXAMPLE_B or root-equivalent C. No strict R3/ASET exponent follows.

## 5. Why the precise vacancy type matters to the next proof

Unlike a generic numeric “Hall deficit”, each DD type points to concrete geometrically checkable source factors:

- The POINT other-spoke / POINT center vacancies are instances of an ORIGINAL point whose entire incidence to a prescribed pair of ACTUAL original lines is absent.
- The LINE other-spoke / LINE center vacancies are exact dual originals: an ORIGINAL line missing both of two prescribed actual original points.

The original GQ point-line incidence degree d=s+1 versus V~s³ makes such misses plausible, even in physically dense C4s. Any future attempt to bound D by a purely physical hole-count or by counting just ONE source cross-flag is therefore structurally incomplete. A real theorem must either correlate the **chosen physical C4 factors** with additional TRUE original incidence edges or show their vacancies force accepted positive GF5 motifs among the other six classes under the SAME global pair maps.

There is no claimed universal bound D_t=o(s^7), no claimed source correlation/independence, and no reinterpretation of D_t as positive original sixflag Q.

## 6. Exact independent experiments / falsifiers and provenance

- `research/hyp105_issue230_d6aa4dd_dual_hall_vacancy.py`: uses actual ORIGINAL W3 source matrices attached to fully occupied physical C4 factor triples, strictly validates 2×2 zero-minor witness possibilities, allocates exact integer TWELFTHS, and accumulates four typed original source deficits with one fixed f/g, original immutable source incidence and a canonical source P3 projection. Source input is explicitly a chosen anchor set; a C4 cap is marked PARTIAL to avoid overclaiming all-W38 historical BBo.
- `research/test_hyp105_issue230_d6aa4dd_dual_hall_vacancy.py`: exhaustively checks ALL 512 3×3 binary matrices and filters the 328 genuine-GQ-girth-admissible forests, with independently computed 2×2 residual perfect matchings and zero-row/zero-column witness types, TWELFTHS and exact transpose duality. On TRUE original W32 lex/S72, full typed ORIGINAL dual models and swapped source anchor pairs check that all four fractional energies transpose correctly and accepted original BBo matches a SEPARATE independent canonical original sixflag Q oracle. On TRUE original W34 lex/random, 8 original nonincident source anchors per map and ALL actual physical C4 triple pairs are audited against parent AA4-DC independent marking/cofactor summation with positive witness type evidence. Genuine W38 lex/random only 4 real original anchors and the first 8×8 completed source triples per anchor: **explicitly PARTIAL**. Exact h1..110 dyadic arithmetic gates, malformed original source factor injection/invalid cuts/non-GQ 3×3 minors fail closed.
- Dedicated six GitHub-hosted isolated test jobs at exact PR HEAD are required before calling software validation successful; full Research and Proof Audit status reported separately. A green proof audit is NOT independent qualified mathematical peer review.

**Prior art boundary:** Hall's marriage condition, 2×2 permanents and finite-GQ incidence girth 8 are classical (e.g. Godsil–Royle, *Algebraic Graph Theory*, 2001, section on generalized quadrangles; Hall's original theorem). The **new project-specific partial claim** is the globally fixed typed-physical pair embedding, historical GF5 BBo marked-energy, dual-invariant four-way SOURCE obstruction decomposition together with the inherited all-h quantitative alternative. It is not a new general mathematical theory of perfect matchings.

**Next AA4-DE:** Pick and bound at least one dominant type `D_t` using the ORIGINAL GQ projection and physical C4 center-source-factor tensor, or exhibit a rigorous map-preserving injection from a large `D_t` into genuine ORIGINAL *other-class* GF5-positive six-incidence-ID sets with bounded multiplicity. A merely numerical correlation of D_t with other motif counts on finite W32/W34 is NOT a universal compensation theorem.

Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`. Leave AA4-DD Scientific Draft, no main merge or accepted registry changes until independently reviewed and all ancestor proof gates are satisfied.
