# HYP-105 / issue #230 — D6-T: global assignment-dual certificate and degree-one NO-GO

**2026-10-13. RESTRICTED_THEOREM_C plus formal proof-method NO-GO. Branch A / B OPEN.** Child Draft strictly stacked on four-GitHub-hosted-green D6-S [PR #418](https://github.com/definitely-stable/Mathlab/pull/418), pinned parent HEAD `bd1e353228f124f21dc1c87f23ccae3610786543`. No `main` mutation; do not merge and do not close #230/#176/#169.

## 1. Stop extending permutation-local optimality as a surrogate for the root theorem

D6-P through D6-S identified TRUE original-W32 one-/two-/three-factor right-label phenomena. S68 is a strict finite right-local minimum under **all** permutations of support size at most three; S72 has the unique improving oriented 3-cycle (1,7,9) reverse with S:72→68 and a selected GF5 necessary numerator reduction of 179530. These are mathematically exact finite facts, but do not control arbitrary correlated f,g or a coherent infinite family.

D6-Q established that even for EVERY fixed left f and EVERY admissible right physical image E, the **average** over bijections of original right lines into E has nontrivial leading `(455/3-o(1))s^6` positive mass. This gives no bound on the **minimum** over bijections. It is now necessary to model the global all-different constraint on both original sides and produce a certificate whose every logical premise is independently checkable.

The present stage builds that certificate interface and establishes a precise mathematical NO-GO for its simplest degree-one instance. It does **not** assert a nonzero universal all-h bound.

## 2. The exact ALL-h original global primal

Let s=2^h, h>=1, the genuine ORIGINAL symplectic GQ W(3,s) have V=(s+1)(s²+1) points and V lines, and K=binom(a,2)>=V available unordered physical coordinate-pair labels with minimal a. Let `P` and `L` be ORIGINAL point and line factor sets and `Q` be the collection of **unordered distinct six-subsets of ORIGINAL GQ incidences**. For each Q define

    chi_Q(f|P(Q),g|L(Q)) ∈ {0,1}

as the indicator that the six original incidences give one of the already accepted seven strictly positive GF5 classes under the current globally injective left/right pair maps. The classifier includes BOTH C/A, C/B orientations, aligned D6 incidence-column dual, and original B/B repeated-point/right-line incidence-position overlap/disjoint. Each local factor depends on at most six ORIGINAL point labels and at most six ORIGINAL line labels (at most twelve original variables in total), with all original incidence positions retained.

Then identically, for ALL finite h and arbitrary correlated complete injections f and g,

    S_seven(f,g)=sum_{Q} chi_Q(f,g).

The accepted necessary GF5 R3 lower numerator uses a nonnegative coefficient depending on the one accepted class: `Y_7(f,g)=sum_Q c_class(Q) chi_Q(f,g)`, with coefficients D6=5643, two B/A orientations=45600, C/A=43320, C/B=49050, B/B-overlap=51750, B/B-disjoint=45010. **This is NOT total R3 and NOT a full upper bound on R3.**

Each original map is an INJECTIVE assignment of its V typed ORIGINAL vertices into K physical pair labels. The two sides have separate injectivity constraints; a physical pair may be used by one left factor and by one right factor, because their types differ. The exact global minimization over two independent K-column rectangular assignment matrices with degree-up-to-12 nonnegative factors is a 0-1 higher-order assignment problem. It is **not** a linear assignment problem until the dual relaxation described next is applied.

## 3. THEOREM T1: exact, globally sound projected-marginal assignment dual

Consider any finite collection of nonnegative integer ORIGINAL local factors `F_c` whose scope contains `r_c` distinct original vertices in both sides combined, `1<=r_c<=12` (the empty constant case r=0 is handled separately). Each has an EXACT COMPLETE local truth table over **all locally injective** physical assignments from its left ORIGINAL scope into its designated left image alphabet, and from its right ORIGINAL scope into its designated right image alphabet. Global complete ORIGINAL injections restrict to one of these local choices. No other geometric assumptions are needed for the inequality itself.

For each factor set

    b_c = min_phi F_c(phi),
    m_(c,i,e) = min_{phi:phi(i)=e} F_c(phi),

with i any ORIGINAL site in the scope, and e any physical pair image allowed on the same typed side. Since every locally injective tuple of r factors satisfies `m_(c,i,phi(i))<=F_c(phi)`, averaging gives the rigorous **pointwise local dual inequality**

    F_c(phi) >= b_c + (1/r_c) sum_{i in scope(c)}
                              [m_(c,i,phi(i)) - b_c].

The 1/r normalization is essential: simply summing all r projected minima would in general overcount. Let D=lcm(1,2,...,12)=27720, an integer multiple of each possible r. Define scaled nonnegative single-site potential coefficients

    A_(c,i,e) = (D/r_c) [m_(c,i,e)-b_c].

For each side separately, aggregate all local potentials `A_(i,e)=sum_{c containing i} A_(c,i,e)`. Let `M_L` be the EXACT minimum cost of assigning all ORIGINAL left points injectively to K left physical pair labels with cost matrix A^L; define `M_R` analogously for the ORIGINAL right lines. Let `B=D sum_c b_c`.

Then for EVERY complete globally injective pair f,g,

    D * sum_c F_c(f,g)
         >= B + M_L + M_R.

In particular, the **globally valid exact rational lower certificate** is

    L_dual = (B+M_L+M_R)/27720.

If one can rigorously construct and verify local tables for every ORIGINAL six-incidence Q and prove `L_dual>=c s^6` with uniform c>0 for all h, this would suffice for Branch A. But T1 is only a **certificate framework**, not a result that such a positive dual exists. It is also not a complete hierarchy: the inequality is one particular feasible degree-one separable dual and may be far from the true minimum.

The Hungarian matching stage is exact and uses integer arithmetic (including negative artificial test costs), with independent brute-force comparisons on small rectangular matrices. The implementation validates EVERY row of every supplied local factor truth table against the locally injective assignment domain and independently checks the pointwise inequality. It refuses incomplete or unaffordably large local tables; an arbitrary incomplete list of constraints is not accepted as an exhaustive certificate. The full ORIGINAL all-h 12-local truth tables are **not generated** and no W34/W38 full seven-family S is manufactured.

## 4. THEOREM T2: this particular unconditional degree-one dual is IDENTICALLY ZERO for the root sixset objective

This is a substantive negative result about the **proof method**. It does **not** disprove Branch A and does not produce a correlated small-S assignment.

Fix ANY original six-incidence subset Q, ANY single ORIGINAL left point or right line factor vertex i appearing in Q, and ANY prescribed physical pair label e for that vertex on its own typed side. Its OPPOSITE typed side has no prescribed labels. We show that it has a locally injective assignment making the six-incidence physical projection **NOT** two-regular on exactly six coordinates:

- If an ORIGINAL factor vertex on the opposite side appears at least three times among the six incidence positions, every physical pair assignment gives degree at least 3 to each endpoint of that repeated pair. Thus the needed degree-two condition fails immediately.
- Otherwise all opposite-side ORIGINAL factor multiplicities are at most 2. There are then at least three distinct ORIGINAL opposite-side factors. Map three of them injectively to the physical pair edges (0,1),(0,2),(0,3) in K_a. The physical coordinate 0 appears at least three times across six positions. Extend the partial assignment injectively to all remaining ORIGINAL factors using unused K_a pair labels. This is always possible since a>=6, K>=15 and at most six distinct local factors are assigned.

Either way the opposite projection is invalid, so Q contributes ZERO to every accepted GF5-positive class, regardless of the prescribed single factor label e. Furthermore that locally injective assignment can be extended to a complete ORIGINAL injection because K>=V. Hence

    b_Q = 0,
    m_(Q,i,e) = 0

for **every** original Q, every single original site i, every permitted physical image e, and for both unweighted and certified weighted nonnegative positive-class factors.

Therefore on the exact UNCONDITIONED BOTH-SIDES ORIGINAL root problem, ALL degree-one coefficients A_(Q,i,e) vanish, the Hungarian minima M_L=M_R=0, and the D6-T projected-marginal dual lower bound is exactly

    L_dual(full arbitrary f,g) = 0

for EVERY h>=1.

This is a rigorous **NO-GO for this degree-one projection relaxation alone**: it can NEVER prove the desired nontrivial all-h positive Omega(s^6) lower bound. It does NOT mean that the true minimum of S is zero and does NOT imply the infinite-counterfamily Branch B. It forces any substantive global proof certificate to couple **at least two site labels, include cross-side conditional structure, or introduce stronger nonlocal constraints** beyond these single-site minima.

The executable `physical_non_two_regular_star_witness` independently constructs this obstruction for arbitrary six original factor endpoints and a>=6; tests use TRUE original W32 incidence sixsets of left types A/B/C and physical alphabets a=6,14,35.

## 5. Conditional exact finite positive dual: global injectivity can still matter

A globally zero UNCONDITIONED two-sided degree-one dual can become nonzero after freezing f and a large part of g, because the opposite-side escape used in T2 is no longer available. An elementary exact synthetic example illustrates real global coupling: three distinct ORIGINAL right variables are bijectively assigned physical images 0,1,2, and there are three one-site factors `F_i=1[g(i)=0]`. Each factor separately has minimum 0, but global injectivity implies `sum_i F_i=1` for every permutation. The verified Hungarian-based dual achieves exactly 1. This is strictly stronger than adding the three independent local minima, which would incorrectly give 0.

A separate exact NO-GO sanity test uses two opposite third-order parity factors on the three assignments. Their sum is identically 1, but **each one-site projection minimum remains zero**, and the degree-one dual correctly returns only 0. This independently demonstrates why higher-order global couplings cannot be assumed solved by T1.

On the REAL ORIGINAL GQ W(3,2), for frozen S68 and S72 left maps f, freeze ALL 15 right physical pair labels except those on a chosen three-ORIGINAL-line set T. Specifically:

- S68: T=(3,11,12), the best supported 3-cycle from D6-S, baseline S=68.
- S72: T=(1,7,9), the exact three-cycle escape witness from D6-S, baseline S=72, reverse oriented assignment reduces S to 68.

Each T has exactly THREE distinct currently occupied physical right pair edges. There are **3!=6 complete and globally injective assignments** obtained by bijectively reassigning those edges to T, with every other right factor frozen. Compile ALL **62,370** original left-selected six-incidence candidates from D6-P. Partition all their position-aware cylinder factors by the EXACT ORIGINAL right-line support intersection `U=R(c)∩T`; there are at most 2^3=8 support groups. For each group and every locally injective map U→the same three physical pair edges, evaluate the exact sum of accepted original GF5-positive sixsets and, separately, their certified weighted necessary GF5 numerator. Every assignment U→E_T can be extended to one of the six complete permutations of T. Hence each group truth table is COMPLETE and physically valid even if an intermediate partial implementation holds overlapping frozen physical labels outside the group: no such overlapping labels appear in the group's incidence cylinders.

This gives an EXACT local-table factorization of full original positive seven-S and selected GF5 numerator on that conditioned six-state orbit, independently cross-checked against the original census. Run T1's projected-marginal dual and the exact all-3! primal min, and record the **certified duality gap** (nonnegative). The dual can be below the true orbit min, even if the true conditional S is positive. The finite min is NOT the global 15! right-permutation minimum, a two-sided f,g minimum, or an all-h result.

### Acceptance methodology

- Independent brute-force integer rectangular assignment oracle versus pure-Python Hungarian on multiple matrices (including negative artificial costs).
- Exact full local truth-row validation with fail-closed checks on missing rows, invalid noninjective rows, negative and bool objective costs, insufficient physical images, and over-budget local tables.
- Strict synthetic positive global-injectivity certificate `0 local minima → exact dual 1`, and synthetic third-order parity obstruction `global optimum 1 but dual 0`.
- TRUE original W32 A/B/C incidence-side star-construction proof-method falsifiers at a=6/14/35.
- TRUE original complete W32 right maps S68/S72, all six complete right assignments on specified T; exact equality of every local-factor sum with compiled seven-cylinder census. Independently cross-check initial and S72 72→68 three-cycle witness against original full incidence `seven_census`. Exact rational dual floor must NEVER exceed any actual global assignment cost.
- Require final HEAD D6-T dedicated Contract, INDEX, Proof Audit, full Research GitHub-hosted SUCCESS, and separate independent mathematical review before accepting. No main mutation, no PR merges, #230/#176/#169 remain OPEN.

## 6. Next genuinely viable global theorem gate — D6-U

T2 eliminates **unconditioned single-site projected-marginal positivity** as a route to Branch A. Meaningful next methods must preserve simultaneous left/right assignment geometry at minimum degree 2 or higher: e.g., cross-side paired factor marginals, a higher-level Sherali–Adams/Lasserre feasibility relaxation on BOTH typed permutation matrices, an exact global dual with jointly evaluated pair coordinates, or a coherent explicit infinite small-S family. Such attempts MUST supply a sound positive certificate or an explicit no-go against a precise relaxation; continuing to enumerate small W32 orbit local minima alone will not resolve #230.

**Branch A OPEN / Branch B OPEN.** No universal `Omega(s^6)` theorem claimed, no coherent infinite `o(s^6)` counterfamily, no full R3 upper, no ASET exponent. The positive conditional T1 floor and true W32 3-factor examples are only scoped finite certificates.
