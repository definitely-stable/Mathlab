# HYP-105 / #230 — AA4-BBOCUBIC: exact ORIGINAL-core cubic B/B-overlap image polynomial

**Scientific Draft**, stacked STRICTLY on frozen [#699](https://github.com/definitely-stable/Mathlab/pull/699), exact parent HEAD \`03d564f182f43713767eb7120e431d52ad2c37be\`. No merges, parent/main modifications or issue closure; root remains \`OPEN_WITH_FORMAL_BLOCKER\`. The new contribution is NOT the already proved 0/2 inverse of [#677](https://github.com/definitely-stable/Mathlab/pull/677) or the independent path mass census [#694](https://github.com/definitely-stable/Mathlab/pull/694). It is the **exact, simultaneously valid for every original core** source-support polynomial, with a new independent source-first algorithm and exact random-deletion moments.

## 1. Finite/all-h theorem and exact scope

Fix an ACTUAL ORIGINAL symplectic W(3,s) with s=2^h, complete actual original point/line incidence flag IDs \(\mathcal F\), and independently globally pair-injective but arbitrarily correlated fixed maps f (original points) and g (original lines) into the *minimal* physical pair alphabet. The full original source incidence graph, not a selected/trimmed CORE, determines the unique source projection \(q-\ell-p-r\) for any nonincident original (q,r). A selected physical CORE \(H_I\) contains BOTH genuine opposite-corner physical diagonals for every retained ORIGINAL flag ID \(i\in I\subseteq\mathcal F\), with no invented flags or reassignments.

A **valid original B/B-overlap source sextuple \(Q\)** has six distinct ORIGINAL flag IDs, exactly one original point p repeated twice, exactly one original line ell repeated twice, and includes the genuine original source flag (p,ell) at their intersection. Its unique original anchor is

\[
A(Q)=\{(q,\ell),(p,\ell),(p,r)\}.
\]

The three remaining actual original flag IDs \(T(Q)=Q\setminus A(Q)\) form a source-factor matching: their original point IDs and original line IDs are each pairwise distinct. The two projected point-side and line-side physical degree-two factors consist of a doubled anchor pair and a disjoint simple C4 on four distinct coordinate symbols. Removing the one original anchor edge f(q), respectively g(r), reconstructs a unique source-edge-labelled P4 on each typed coordinate side, as rigorously proved in [#677](https://github.com/definitely-stable/Mathlab/pull/677).

Define \(\mathcal Q_{aligned}(f,g)\) as the family of these TRUE ORIGINAL B/B-overlap sextuples whose **three non-anchor source flag IDs** have the same ordered P4 edge sequence on both typed sides up to a simultaneous reversal; this is a property of original source incidence and both fixed typed maps, **not** a property of any particular core. For any forbidden ORIGINAL flag-ID subset \(Z\subseteq\mathcal F\), let \(\mathcal Q_Z=\{Q\in\mathcal Q_{aligned}:Q\cap Z=\emptyset\}\).

**The new exact universal original-core polynomial** is

\[
\boxed{
U_{\mathrm{produced}}(I,Z)=
\sum_{Q\in\mathcal Q_Z}\ \prod_{i\in T(Q)}\mathbf1_{\{i\in I\}},
\qquad
P_{\mathrm{unblocked,dir}}(I,Z)=2\,U_{\mathrm{produced}}(I,Z).
}\tag{BC1}
\]

This counts **distinct produced ORIGINAL B/B-overlap sixsets**, not all GF5-accepted original sextuples, and the second identity counts the actual **directed** good, unblocked coordinate-proper three-edge physical paths with the permitted ORIGINAL sixsets. It is an exact 3-homogeneous squarefree monotone polynomial in the retained CORE ORIGINAL ID indicator variables, with nonnegative integer coefficients after aggregating sextuples with identical three-ID support.

**Proof.** From any candidate ORIGINAL Q, its repeated p and ell uniquely force its three original anchor IDs and thus the remaining three non-anchor IDs T. The two typed P4 chains are determined by the six fixed source label pairs and are compatible in zero or exactly two reverse-oriented physical three-edge paths (#677, independently reconstructed by the new module). Each path uses exactly the three ORIGINAL ID owners T and *none* of the three anchor IDs as physical edges. The endpoint pair labels decode q and r, and the source projection uses the three genuine full-source anchor flags regardless of their presence in CORE. The doubled physical anchor f(p) and g(ell) are disjoint from the complete four-coordinate paths, so neither an exceptional endpoint nor internal blocked coordinate occurs. Therefore both source-backed directed paths exist in the real H_I **iff** all three T IDs are present in I; additionally a separately specified explicit forbiddance of ANY original ID in Q kills both paths. Conversely every actual good/unblocked proper three-edge physical core path has unique genuine ORIGINAL source edge owners T and the uniquely projected original q-ell-p-r anchor; it therefore gives one Q in \(\mathcal Q_Z\), and every Q has exactly the two reversal preimages, not more. This proves (BC1) for ALL h and all permitted correlated maps and selected cores. The proof uses the historical inverse theorem as an independently verified structural input, not finite-h induction.

**Important core/anchor distinction:** the condition is \(T(Q)\subseteq I\), NOT \(Q\subseteq I\). Requiring all three anchor source flags to have survived CORE trimming would incorrectly remove valid B/B-overlap image sextuples from the lower bound. Likewise removing an anchor ID from I has **no effect** on the corresponding monomial; putting an ID into the separately defined forbidden source set Z **does** remove Q. CORE membership and explicit forbidden ORIGINAL IDs must never be silently identified.

## 2. New source-ID hypergraph picture and monotonicity

Aggregate the catalog by the unordered three-ID supports \(T\subseteq\mathcal F\):

\[
c_T = \#\{Q\in\mathcal Q_Z:T(Q)=T\},\quad
U_{\mathrm{produced}}(I,Z)=\sum_{T\in\binom{\mathcal F}3}c_T\prod_{i\in T}\mathbf1_{\{i\in I\}}.
\tag{BC2}
\]

The \(c_T\) are nonnegative integers, not random variables. Multiple genuine ORIGINAL sextuples may share the same physical three-path owners but have different full-source anchor sextuples; the unique source endpoint closure in this model normally pins the anchor, and the new implementation explicitly fails if it detects conflicting ORIGINAL closures.

Consequences hold for *every* original core:

* If \(I\subseteq J\) then \(U(I,Z)\le U(J,Z)\), because all coefficients are nonnegative; no derivative of a physical graph needed.
* Each deleted single ORIGINAL source ID i changes U by the exact number of surviving source sextuples with \(i\in T(Q)\). Its influence is entirely controlled by the three-edge support hypergraph.
* Core selection does **not** require anchors to be selected; actual full original geometry is queried for source closure separately.
* All assertions are about the B/B-overlap **image subcount**. No claim is made about universal cubic degree improving the asymptotic sextic obstruction, the other six GF5 classes, or an independent proof of the entire dense-core moment inequalities.

## 3. New exact Bernoulli CORE-deletion first/second moments

Only in a SEPARATE random-subset experiment, independently retain each ORIGINAL ID \(i\) with probability \(\rho_i\in[0,1]\), while f,g and the full ORIGINAL source remain fixed. Then (BC1) gives

\[
\boxed{
\mathbb E U
=\sum_{Q\in\mathcal Q_Z}\prod_{i\in T(Q)}\rho_i,
\qquad
\mathbb E U^2
=\sum_{Q,Q'\in\mathcal Q_Z}
\prod_{i\in T(Q)\cup T(Q')}\rho_i.
}\tag{BC3}
\]

The variance is exactly the difference. In the uniform case \(\rho_i=\rho\),

\[
\mathbb E U=\rho^3|\mathcal Q_Z|,\qquad
\operatorname{Cov}(\mathbf1_{\{T(Q)\subset I\}},
 \mathbf1_{\{T(Q')\subset I\}})
=\rho^{6-|T(Q)\cap T(Q')|}-\rho^6\ge0.
\tag{BC4}
\]

Thus these **CORE Bernoulli survival monomials** are nonnegatively correlated; the full variance is a combinatorial weighted overlap spectrum of the three-ID supports. This does NOT imply positive covariance for the *dependent original priority + two typed-bitcut selector* of #679/#695, which can exhibit negative physical-path-pair covariance. Mixing these two probability spaces would be invalid. These new exact moments are a research tool for selecting/adversarially pruning ORIGINAL core flags, not a free solution of the existing all-h dense-core error budget.

## 4. Truly independent source-first and physical-first finite falsifiers

The new standalone \`research/hyp105_BBo_original_core_cubic_polynomial_referee.py\` does **not** import #677's original inverse, #694's physical path image census, the GF5 classifier, or the historical sixth-moment source oracle. It uses only \`genuine_source\` to load ACTUAL original W32/W34 incidence as a trusted input. Its two algorithms have different iterated objects:

1. **SOURCE-FIRST original-flag compatibility graph.** For every pair of actual ORIGINAL flag IDs, intersect their two fixed f/g factor pair labels; if both intersections are singletons, record the uniquely common physical coordinate corner but do **not** construct physical graph adjacency. For every center source ID j, pair compatible original IDs i,k that touch *opposite* typed endpoints of j and yield four distinct coordinate symbols on both sides. Reconstruct q,r from the outer two typed pair endpoints; look up the unique FULL genuine source q-ell-p-r anchor, exclude four internal anchor blocks, construct and validate all six distinct actual ORIGINAL flag IDs, exactly one source B/B-overlap profile and two degree-two typed physical projections. Index each accepted Q by its unique three original non-anchor ID support T. This forms \`Q↦T\` independently of physical graph walks.
2. **PHYSICAL-FIRST independent exact original source audit.** For arbitrary retained ORIGINAL ID core I, independently insert BOTH actual physical diagonals of every original core flag into a simple physical graph, then enumerate its real directed three-edge physical walks. Reject non-proper coordinate repetitions, missing/incident/source-bad full original endpoint closures and all four internal blocks, recover the three true original edge owners and all three full-source anchor IDs. Check every six-ID sextuple has exactly TWO directed physical witness paths (reversals). Compare the **entire set of original sextuple keys** against the SOURCE-FIRST polynomial evaluated at core I, not only scalar counts.

The new tests cover multiple TRUE full-original W32 globally injected arbitrary correlated maps and W34 full plus sparse original cores, original anchor IDs genuinely absent from core, forbidding anchors separately, 128 different true ORIGINAL W32 core subsets with source-first ↔ physical-first sets required equal EACH time, and exact first and second moments of those 128 cores both under uniform and nonuniform independent Bernoulli retention. The protected original W34 K4,4 source is included as a potentially ZERO BBo control (it is primarily a D6 fixture; a zero here is not treated as an illegitimate failure), and malformed source IDs/noninjective typed maps fail closed.

**STOP / acceptance:** (BC1)–(BC4) are deterministic and probabilistic identities with all-h combinatorial proofs and independent finite falsifiers. No universal new \(s^6\) lower bound, new ASET exponent, numerical external graph \(C_{\rm graph},c_{\rm graph}\), completed full #230 acceptance or third-party mathematical peer review is asserted. Ancestors and main remain untouched. Keep every scientific Draft unmerged and root #230 \`OPEN_WITH_FORMAL_BLOCKER\`. Next legitimate acceptance action after exact-head CI: independent adversarial audit of whole **dense-core mixed FULL/CORE 4th-moment error** at arbitrary correlated f,g (not just scalar constants), then qualified independent extremal-combinatorics review of complete theorem.