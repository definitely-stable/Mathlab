# HYP-105 / #230 — AA4-PALDIST: ORIGINAL six-ID packing amplifies random GF(5) risk into palette rarity and recoloring distance

**Scientific status:** rigorous elementary all-\(N\) theorem **conditional on an explicitly given and independently validated ORIGINAL six-flag packing**; an all-\(h\) consequence is *conditional* on the existing scientific Draft [#674](https://github.com/definitely-stable/Mathlab/pull/674) being mathematically valid/accepted, and on the finite-algebra exact 51-palette signed-flow minima [AA4-SIGN10](HYP-105-SHARP-TEN-SIGN-R3-FLOOR.md). This is a new deduction connecting the fixed-map geometric packing frontier to the finite 25/26-change optimization completed in green [PR #725](https://github.com/definitely-stable/Mathlab/pull/725), **not** a new proof of the root all-label geometric obstruction. Do not close #230, claim a new ASET asymptotic exponent, or conflate the random baseline with an arbitrary chosen baseline. No ancestral scientific PR or \`main\` edits.

## 1. Exact model, six ORIGINAL IDs and coefficient law

For every dyadic \(s=2^h\), \(h\ge1\), fix the true symplectic \(W(3,s)\), with \(|P_s|=|L_s|=V=(s+1)(s^2+1)\), \(|I_s|=N=(s+1)V\) genuine ORIGINAL point-line incidences. Fix *both* complete separately globally injective typed physical coordinate-pair maps \(f,g\) into \(E(K_a)\), \(a=\min\{a:\binom a2\ge V\}\), allowing **arbitrary correlations** between their original factor labels. Freeze both maps for the ENTIRE theorem.

At each ORIGINAL incidence flag \(i=(p,\ell)\) choose independently and uniformly one of the **51 legal nonzero checksum4 GF(5) palettes** on its exact two left and two right physical coordinates. All columns have checksum \(4\bmod5\); there are no duplicated/copied source flags, coordinate-resampling or synthetic factor maps.

An accepted ORIGINAL \(D_6\) or \(B/B\)-overlap sixset \(Q\) is a subset of exactly SIX DISTINCT ORIGINAL incidence IDs, using the SAME six IDs for both physical projections, satisfying the established seven-family full-GF5 positive class predicate. Choose one canonically determined unordered balanced signed \(3+3\) partition of its six IDs (e.g. sorted first three positive, remaining three negative). Define \(X_Q\) to mean the actual **full physical GF(5)** signed equality for that chosen partition.

By the full 51-palette signed-flow computation in the separately verified AA4-SIGN10 proof, ALL ten signed partition probabilities are positive:
- every \(D_6\) sign has at least 5265 legal six-palette solutions, out of \(51^6\);
- every \(B/B\)-overlap sign has at least **5175** solutions, out of \(51^6\).

The single chosen event therefore satisfies

\[
\boxed{\Pr(X_Q)\ge q:=\frac{5175}{51^6}
=\frac{575}{1955143089}>0.}\tag{1}
\]

**This is a probability of ONE specified signed event**, not automatically the probability of the union of ten different signs. The previous 54,162 / 53,526 all-ten **expected signed event counts** must NOT be substituted as probabilities WITHOUT first proving that the ten events cannot co-occur. Section 7 NEWLY PROVES this mutual-exclusion property for the D6 and B/B-overlap ORIGINAL source topologies, giving a sharper q10 bound. The one-sign q bound remains a valid independently useful baseline.

## 2. NEW all-\(N\) random palette repair theorem

Let \(Q_1,\ldots,Q_t\) be ANY family of accepted ORIGINAL \(D_6\)/\(B/B\)-overlap sixsets whose SIX-ORIGINAL-ID supports are pairwise disjoint. Do not require their coordinate supports or original point/line factor supports to be disjoint: only original flag IDs matter for the independent coefficient variables. Define \(Y=\sum_{j=1}^t\mathbf 1_{X_{Q_j}}\).

Since the legal GF(5) coefficient choices belong to **six different original flag IDs for each event** and the sixsets are source-ID-disjoint, their random variables are INDEPENDENT, even though their physical coordinate projections can overlap strongly and the two globally fixed maps \(f,g\) can be maximally correlated. Each \(\Pr(X_{Q_j})=p_j\ge q\). Write \(\mu=\sum p_j\ge qt\).

For each particular palette assignment \(\mathbf c\), let \(d(\mathbf c,\mathcal A_{0:3})\) be the minimum number of changed ORIGINAL source coefficient palettes needed to obtain ANY full 0-to-3 source ASET \(\mathbf c'\) on the **same** fixed f,g; if no such final assignment exists, let this distance be \(+\infty\). There are NO restrictions on where edits occur or their order.

**Theorem AA4-PALDIST (independent bad-sixset amplification, any finite original source):**

\[
\boxed{\begin{aligned}
d(\mathbf c,\mathcal A_{0:3})&\ge Y \quad\text{pointwise},\\
\Pr(\mathbf c\in\mathcal A_{0:3})&\le \prod_{j=1}^{t}(1-p_j)
 \le (1-q)^t \le e^{-qt},\\
\Pr\bigl(d(\mathbf c,\mathcal A_{0:3})<qt/2\bigr)&\le e^{-qt/8}.
\end{aligned}}\tag{2}
\]

Also \( \mathbb E\,\min\{d(\mathbf c,\mathcal A_{0:3}),N\}\ge qt\), taking the truncation at \(N\) to make the expectation finite even if no valid assignment exists. This is valid because \(Y\le t\le N/6<N\).

**Proof.** Once a chosen source-disjoint signed event \(X_{Q_j}\) holds in \(\mathbf c\), changing coefficient columns OUTSIDE its six ORIGINAL flag IDs cannot change either side of its full GF(5) signed equality, regardless of all other recolorings. Any valid final source must recolor at least one of its six flags. Because the \(Q_j\) are pairwise ORIGINAL-ID-disjoint, the required changes are distinct across all \(Y\) currently violated groups. Hence every clean final assignment differs in at least \(Y\) original flags. The event of full cleanliness implies no \(X_{Q_j}\), giving the exact product via **independence across source-flag variables**. The lower tail follows from the standard multiplicative Chernoff bound for independent, not necessarily identically distributed, Bernoulli indicators: \(\Pr(Y<\mu/2)\le e^{-\mu/8}\). Since \(\mu\ge qt\), the event \(Y<qt/2\) is a subset of \(Y<\mu/2\). No independence of the TEN sign partitions of one sixset is asserted. QED.

**Counting consequence:** among all \(51^N\) legal global original-source assignments, at most \(51^N(1-q)^t\) produce FULL 0-to-3 ASETs. More generally, the fraction of legal initial palette arrays within original-source Hamming distance \(qt/2\) of **any** valid full final ASET is bounded by \(e^{-qt/8}\). This does not assume or prove that a full final ASET exists.

## 3. Conditional all-\(h\) uniform corollary from Draft #674 — NOT new Branch A

The original six-ID arbitrary-deletion theorem in scientific Draft #674 asserts positive absolute constants \(\rho,\delta\) and a sufficient \(s_0<\infty\), independent of h, f,g, such that deleting ANY map-dependent set \(Z\) of at most \(\rho s^4\) ORIGINAL incidence IDs still leaves accepted \(D_6\) or \(B/B\)-overlap sixsets. Its maximal ORIGINAL-source-ID packing corollary yields

\[
t(f,g)>\frac{\rho}{6}s^4
\qquad(s=2^h\ge s_0,\ \forall\text{ complete correlated }f,g).
\tag{3}
\]

**IF this unaccepted Draft theorem is verified mathematically**, the all-\(N\) theorem above supplies for every allowed correlated complete f,g

\[
\boxed{\Pr_{\mathbf c\sim\mathrm{Unif}(51)^N}
  [\,\mathbf c\text{ is full }0{:}3\text{ ASET}\,]
  \le\exp\Bigl(-\frac{q\rho}{6}s^4\Bigr).}\tag{4}
\]

And

\[
\boxed{\Pr_{\mathbf c}
 [\,d(\mathbf c,\mathcal A_{0:3})<
       \frac{q\rho}{12}s^4\,]
 \le\exp\Bigl(-\frac{q\rho}{48}s^4\Bigr).}\tag{5}
\]

These are **exponential palette anti-concentration and typical required repair radius** bounds, not an all-h theorem about deterministic coefficient assignment **existence** or **nonexistence**. A very rare full ASET can exist, as proven by the explicit 425-source finite constructions in #725. The two specific chosen initial coefficient maps in #725 are NOT sampled uniformly and may have atypically small distances 25/26; there is no contradiction.

The all-h consequence is **dependent on the geometric source deletion theorem in #674**, whose proof in turn uses the previously unaccepted #672 all-map universal sextic obstruction and a published (real, but not numerically calibrated) balanced graph C6 supersaturation theorem. We do not choose fictitious graph constants \(C=c=1\), or replace their unknown numerical values by an arbitrary convenient \(\rho\). No new assertion of \(\mathrm{PROVED\_A}\), \(\mathrm{COUNTEREXAMPLE\_B}\), or \(\mathrm{RESTRICTED\_THEOREM\_C}\) is made; root #230 stays **OPEN_WITH_FORMAL_BLOCKER**.

## 4. Genuine finite W32 and GF(5) falsifiers

\`research/hyp105_original_random_palette_distance.py\` independently rebuilds the original symplectic W(3,2) source with all 45 genuine original incidence IDs and full legal injected \(f,g\), both lex and reverse-line. It uses the already independently audited 62,370 original left-qualifying sixsets / 7-class classifier to collect ALL accepted source D6 / BBo sixsets (historical lex 15+8, reverse-line 3+7). It constructs a deterministic GREEDY maximal SIX-ORIGINAL-flag-ID-disjoint packing, with no claim of maximum cardinality. For EACH chosen original sixset it reconstructs all twelve actual physical coordinate-to-six-source incidences and verifies the probability of its one selected signed GF(5) equality with TWO mathematically different independent oracles:

1. the exact \(2^{12}\) subset inclusion–exclusion rank oracle;
2. the independent \(4^7\) nonzero chord-current enumeration and deterministic spanning-tree GF(5) solver.

The finite report gives source-ID lists, actual signed GF(5) pattern counts, the exact rational product probability that NONE of the chosen signed events occurs under independent uniform legal coefficients, and the full exact Poisson-binomial distribution. The exact probability is an UPPER bound for a full ASET, not its value; the selected signed events can fail even when other types of original 2v2/3v3 conflicts remain.

The hosted tests additionally plant genuine six ORIGINAL D6 and BBo source flags in complete W(3,2) and W(3,4) original geometric incidence sources with full legal global injected maps and verify **all ten** signed partitions from the full physical original 12-coordinate graph, independently of the original seven-census algorithm; test exact two-motif event independence; mutate/reuse original IDs, fake acceptances or signed flow counts; and ensure a formal chosen \(\rho\) without acceptance of #674 cannot silently produce a claimed proven all-h result.

## 5. Acceptance, limitations and next gate

The standalone all-\(N\) theorem requires ONLY one actual accepted physical original 6set packing with verified signed flow counts and independent uniform coefficient choices. It is mathematically separate from the unresolved source geometry. The strong \(\exp(-\Omega(s^4))\) consequence requires peer acceptance of the separately claimed **full ORIGINAL six-ID deletion** statement of Draft #674.

Unlike the #725 finite 25/26 optimum, this proof is UNIFORM IN ORIGINAL GF(5) COEFFICIENT RANDOMNESS on ANY given fixed pair of physical factor maps and does not alter those maps. Its dependence on standard Chernoff is classical, not novel as a concentration inequality. The model-specific contribution is the precise six-ORIGINAL-ID, 51-palette one-signed-event probability and valid separation of random rarity from deterministic finite optimal recoloring.

**Next legitimate scientific gate:** independently validate the foundational all-map #672 → #674 geometric deletion argument, especially the mixed full/core blocker and source-signed D6/BBo positive transfer, and seek an independent qualified mathematical referee. Until then neither the all-h source packing nor the conditional exponential corollary should be marked an accepted root result.


## 6. Independently frozen finite evidence (complete genuine W32 source)

The first hosted specialist successful original-source run is [#41897978383](https://github.com/definitely-stable/Mathlab/actions/runs/41897978383). All five independent GF5/W32/W34 physical and probabilistic theorem tests passed. Full EXACT integer-rational original-source sixset probability results are retained in \`research/hyp105_original_random_palette_distance_certificates.json\`, not converted through IEEE-754 floating point. The final-head permanent replay specialist [#41898227490](https://github.com/definitely-stable/Mathlab/actions/runs/41898227490) succeeded its original five tests AND four negative permanent certificate tests, and replayed both true W32 complete original motif censuses.

| Genuine original W32 complete fixed global maps | Accepted real D6 sixsets | Accepted real BBo sixsets | Original flag-disjoint GREEDY packing | Exact chosen canonical 3v3 signed GF5 counts per packed sixset |
|---|---:|---:|---:|---|
| lex | 15 | 8 | **3** (2 D6, 1 BBo) | (5265,5265,5184) |
| reverse-line | 3 | 7 | **3** (2 D6, 1 BBo) | (5265,5265,5463) |

The six ORIGINAL source flags of each selected sixset are listed explicitly in the permanent JSON certificate; their selected physical GF5 signed event counts match the independent 4096-term edge-deletion oracle AND the separate 4^7 spanning-tree current oracle. The source packings are MAXIMAL under this deterministic greedy source order (no other accepted D6/BBo original sixset avoids their 18 IDs), but are not asserted to have maximum cardinality. Their full exact independent Poisson-binomial coefficient distributions and rational no-event products are also in the immutable certificate. Three specific real source-sixset signed events give only a SMALL finite bound: there is absolutely no claim that this W32 witness alone proves any asymptotic decay.

The parent #725 original W34 25/26 legal zero-source recolors are **specific deterministic** old-to-new coefficient arrays, NOT uniform random GF5 samples. Both phenomena are consistent.


## 7. NEW stronger all-N theorem: ALL TEN original 3v3 signs are mutually EXCLUSIVE for D6/BBo

A general expected count of ten overlapping signed events is NOT a probability of their union. However, the accepted ORIGINAL D6 and B/B-overlap classes have a structural property that makes the TEN SIGN EVENTS for one given sixset **pairwise disjoint**. This precise proof was missing from the initial q=5175 one-sign version. We now establish the stronger fact directly from the true physical source-coordinate dual, without independence assumptions.

### Lemma 7A — no INTERNAL four-original-flag R2 equality

Let \(Q\) consist of six distinct ORIGINAL columns of a genuine accepted \(D_6\) or B/B-overlap sixset, with all **four legal physical nonzero GF5 entries** per source. Each of the SIX coordinates in the left projection, and each of the SIX coordinates in the right projection, appears in exactly TWO original columns. Build the two colored coordinate-dual graphs on the SIX named original source column indices: a dual edge \(ij\) means one true physical coordinate appears in exactly columns \(i,j\). Both colored duals are 2-regular multigraphs on all six named columns.

If some four distinct named original columns could satisfy a physical signed \(2+2\) equality, their four-ID subset \(A\) must be a union of WHOLE CONNECTED COMPONENTS of BOTH colored duals: a dual edge crossing \(A\) and its two-column complement would put a SINGLE nonzero GF5 term in that physical coordinate's signed equation, which cannot equal zero. This necessary condition depends only on genuine physical support, not on the coefficient values.

- For D6, EACH colored dual is the same connected six-cycle. It has NO proper nonempty union of components, so NO four-column support can satisfy a signed 2v2 equality.
- For B/B-overlap, the left dual consists of a doubled pair on named IDs \(A_L=\{0,1\}\) and a simple four-cycle on its complement; the right dual has a doubled pair \(A_R=\{0,2\}\) and a simple four-cycle on its complement. Their repeated two-ID sets intersect in **exactly one ORIGINAL incidence ID**, so their respective closed FOUR-ID subsets \([6]\setminus A_L\) and \([6]\setminus A_R\) are different. There is NO four-ID set simultaneously closed in both colored duals. Therefore NO signed 2v2 physical GF5 equality is possible among any four of these six ORIGINAL columns under ANY legal coefficient choices.

Distinct original incidence IDs also have DISTINCT full physical four-coordinate supports because the same globally fixed f and g are injective on typed original factor labels: equality of supports requires the same original point AND line, hence the same incidence ID. Since all palette entries on their four supports are nonzero, no two selected original source columns can have equal complete 28D/12D GF5 vectors. This proves the singleton (1v1) no-collision premise.

### Lemma 7B — two distinct balanced 3v3 signs on the SAME sixset force R1 or R2

Index the SIX original columns by 0,...,5. The TEN *global-sign-unordered* balanced 3v3 signs have plus-triples \(P\subset[6]\), \(|P|=3\), \(0\in P\), identifying a partition and its complement ONCE. Take two DIFFERENT plus-triples \(P,P'\). Necessarily \(|P\cap P'|=1\) or 2.

The two signed GF5 equalities mean \(2\sum_{i\in P}c_i-\sum_{i=0}^5c_i=0\) and the analogous equation for \(P'\). Subtraction and invertibility of \(2\) in GF5 imply the EXACT equality

\[
 \sum_{i\in P\setminus P'}c_i
 =\sum_{j\in P'\setminus P}c_j.
\]

If \(|P\cap P'|=2\), this is an equal-singleton equality between two DIFFERENT original source columns, impossible by fixed-source support injection. If \(|P\cap P'|=1\), this is an equal **2+2** source equation on four different original column IDs, impossible by Lemma 7A. Thus the original ten signed physical GF5 events are mutually EXCLUSIVE, not merely positively weighted or uncorrelated. QED.

### Theorem AA4-PALDIST-TEN — exact TEN-sign union probability

Because the ten events on ONE sixset cannot co-occur, their probability union is **exactly** the sum of their ten full-51-palette signed GF5 counts divided by \(51^6\). The separate independently verified exact flow arithmetic in AA4-SIGN10 gives, for EVERY accepted original sixset with valid complete global f,g,

\[
\begin{array}{ll}
D_6: & \Pr(\text{at least one balanced 3v3 equality on }Q)
       =\frac{54162}{51^6},\\
B/B\text{-overlap}:&
\Pr(\text{at least one balanced 3v3 equality on }Q)
       \in\{\frac{53526}{51^6},\frac{53838}{51^6}\}.
\end{array}
\tag{6}
\]

Therefore the uniform chosen original MOTIF event probability is at least

\[
\boxed{q_{10}=\frac{53526}{51^6}
             =\frac{17842}{5865429267}
             >10\frac{5175}{51^6}.}\tag{7}
\]

The ten signs within one original motif are **NOT independent**; they are MUTUALLY EXCLUSIVE. Across pairwise ORIGINAL-SIX-ID-disjoint motifs, the UNION events are independent because each uses a disjoint set of six original coefficient variables. Hence the proof of Theorem AA4-PALDIST in Section 2 applies VERBATIM with \(q_{10}\) in place of the weaker \(q\):

\[
\Pr(\text{FULL 0-to-3 ASET})\le (1-q_{10})^t
       \le\exp(-q_{10}t),\qquad
\Pr(d<q_{10}t/2)\le\exp(-q_{10}t/8).
\tag{8}
\]

**Conditional on accepting previously unaccepted geometric Draft #674**, its source-six-ID disjoint packing \(t>\rho s^4/6\) yields the SHARPER all-h corollary, for arbitrary fixed correlated complete global f,g and sufficiently large dyadic s:

\[
\boxed{\Pr(\text{random 51-palette full ASET})\le
          \exp(-q_{10}\rho s^4/6),}\qquad
\boxed{\Pr(d<q_{10}\rho s^4/12)\le
          \exp(-q_{10}\rho s^4/48).}\tag{9}
\]

This is an **order-of-magnitude stronger** coefficient-level obstruction than using any single signed partition, and crucially proves the missing union-probability step. It remains a theorem about **random coefficient rarity**, not deterministic impossibility, and inherits the all-h geometric scope limitation of #674. No new Root #230 acceptance is claimed.

The new source module \`research/hyp105_original_ten_sign_exclusive.py\` independently examines all FIFTEEN possible original four-ID subsets of the true twelve-edge colored dual, explicitly rejecting every possible support-closed four-subset. Its genuine-source W(3,2) and W(3,4) control uses the ORIGINAL globally injected physical f/g maps and both independent 4096-edge-IE / 4^7-tree GF5 flow algorithms to evaluate ALL TEN signs. The independent negative test uses a deliberate ABSTRACT three-doubled-pair dual with a closed four-subset, which must be rejected; that abstract adversary is NOT substituted as original W(3,s) evidence.

The real frozen W32 full packings now receive exact probabilities of the **UNION of ten signed events** for each of their three disjoint genuine original sextuples. All source palettes remain independent over distinct original IDs, not across signs.
