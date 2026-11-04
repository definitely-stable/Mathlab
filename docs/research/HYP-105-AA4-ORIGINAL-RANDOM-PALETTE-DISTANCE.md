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

**This is a probability of ONE specified signed event**, not the probability of the union of ten dependent signs and not the expected sum of all ten. In particular, the sharper 54,162 / 53,526 all-ten **expected signed event counts** must NOT be substituted as probabilities in this argument. We deliberately use the rigorous minimum 5175 to avoid this mistake.

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
