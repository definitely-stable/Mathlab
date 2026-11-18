# HYP-105 #230 — AA4-LOW-MOMENT-EXACT: exact shared-priority law, universal Harris sharpening and proper-path Jensen transfer

**Scientific state:** new independently derived **all-order local/moment-transfer theorem**, and a stronger **conditional** root Branch A no-deletion quantitative ledger. This is a strict child of [#770](https://github.com/definitely-stable/Mathlab/pull/770), based on frozen HEAD \`16167ae222e055a6370796901ccc5189f2cce217\`. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) stays **OPEN_WITH_FORMAL_BLOCKER**; no claim that all inherited HEAVY/LOW original geometry, C6→D6, P3→BBo and sixth-moment source inverses have received complete independent acceptance. No changes to main or parent, merge or ASET exponent.

## 1. A previously unnecessary exponential wall: one shared selector, NOT independent paths

Fix an arbitrary finite ORIGINAL source conflict graph J on actual incidence flag IDs, generated for the genuine W(3,s) point/line pencil and arbitrary complete separately pair-injective fixed correlated f,g. Let C be a paired original source core with J-degree at most K (after pruning, K=64), with every flag owning its two actual opposite physical diagonals. Let a coordinate-proper physical r-path gamma, r=2 or 3, have distinct actual original flag owners U={u1,...,ur}. Global pair injection and separate distinct left/right physical path coordinates force the owners to have distinct original point factors and separately distinct line factors, so the owners are pairwise NONADJACENT in J.

Give every retained original source flag ONE independent continuous uniform priority t_w∈[0,1]. The priority selector keeps a flag u precisely when t_u<t_w for every w∈N_J(u). Both physical coordinate-bit cuts are independent from these priorities but NOT independent across physical paths.

The inherited #745 finite exact local priority checker counts linear extensions of the actual precedence DAG on b≤20 original IDs by 2^b subset DP. This was a useful falsifier, but it does not supply an efficient exact **all-h instance-adaptive** probability evaluator when b can be 3(K+1)=195 for K=64. This slice removes that artificial implementation restriction **without changing the mathematical selector**.

## 2. NEW all-order exact closed-form source-priority probability for r=2,3

Let W=(union_i N_J(ui))\U be the external ORIGINAL neighbors. Each w∈W has a nonempty source-neighbor mask S_w={i:w∈N_J(ui)}⊆[r]. Write b=r+|W|, and let n_S count actual original external IDs with this mask (their identities, not just their number, matter for the graph but not for this conditional probability).

Conditioning on the r owner priority ranks t=(t1,...,tr), all external t_w are independently uniform. For a given external w the necessary event t_w>max_{i∈S_w}t_i has conditional probability 1-max_{i∈S_w}t_i. Therefore the **EXACT** common-priority event law is

\[
\boxed{\Pr(E_U)=\int_{[0,1]^r}
      \prod_{\varnothing\ne S\subseteq[r]}
      (1-\max_{i\in S}t_i)^{n_S}\,dt_1\cdots dt_r.}
\tag{EX-1}
\]

No graph automorphism, mean-field assumption, owner independence or external neighbor disjointness is used.

Partition the integration cube by the r! strict orderings pi of owner priorities (ties have measure zero). For an ordering t_(pi1)<...<t_(pir), let c_k(pi) be the number of external neighbors w for which the LATEST among its constrained owners occupies position k in pi. On that simplex EX-1 has integrand ∏_{k=1}^r(1-t_(pik))^{c_k}.

Substitute z_j=1-t_(pi,r+1-j) so 0<z1<...<zr<1. The ordinary nested monomial integral of ∏z_j^{d_j} equals ∏_{j=1}^r [j+∑_{i=1}^j d_i]^{-1}. Thus

\[
\boxed{\Pr(E_U)=
 \sum_{\pi\in S_r}
 \prod_{j=1}^r
 \frac{1}{j+\sum_{i=1}^j c_{r+1-i}(\pi)}.}
\tag{EX-2}
\]

This is an **exact rational** formula, with at most 2 or 6 terms for r=2/3, using at most 2^r−1 neighbor-mask counts, regardless of whether b=5, 20, 195, or larger. For fixed r its arithmetic is constant-size apart from the input mask census. It is mathematically proven for ANY finite conflict graph with pairwise nonadjacent target owners, not just a GQ.

**Small adversarial examples (verify the signs):** two owners with disjoint one-neighbor source neighborhoods have exact joint probability 1/4, while the historical first-2 among b=4 sufficient bound is 1/6. Two owners sharing the SAME one external neighbor have exact joint probability 1/3, while the product of individual 1/2 source probabilities is 1/4. Therefore it is wrong both to declare the source events independent AND to presume that the two *adaptive* lower bounds below are ordered in one universal direction.

## 3. NEW universal positive-association lemma: strengthen q2 and q3, not only finite instances

Condition instead on ALL external neighbor priorities t_w, w∈W. With the external ranks fixed, the OWN target owner priorities t_ui are mutually independent. The conditional event probability for owner ui is

\[
h_i(t_W)=\min_{w\in N_J(u_i)}t_w,
\]

where the empty minimum is 1. Each h_i is a nonnegative coordinatewise NONDECREASING function of the independent external priority variables. Consequently their product is also nondecreasing.

The elementary product-measure positive-covariance lemma (Harris/association) states for two coordinatewise nondecreasing integrable functions F,G of independent real coordinates,

\[
\mathbb E(FG)\ge\mathbb EF\,\mathbb EG.
\]

**An elementary proof with no external black box:** in ONE real coordinate X and independent X', 2Cov(F(X),G(X))=E[(F(X)-F(X'))(G(X)-G(X'))]≥0. Condition successively on independent coordinates, apply this inequality and induct, observing conditional expectations preserve monotonicity. Apply again inductively to the nonnegative increasing functions h_1,...,h_r. Thus

\[
\Pr(E_U)=\mathbb E_{t_W}\prod_{i=1}^r h_i(t_W)
 \ge\prod_{i=1}^r\mathbb E_{t_W}h_i(t_W).
\]

Among the owner ui and its actual d_i=deg_J(ui) source neighbors, each is equally likely to have the minimum uniform priority, so E h_i=1/(d_i+1). Therefore the **NEW all-order deterministic source-only universal theorem** is

\[
\boxed{\Pr(E_U)\ge\prod_{i=1}^r\frac1{d_i+1}
                  \ge(K+1)^{-r}.}
\tag{HA-1}
\]

This proof is valid for every source J, all fixed f/g and all true W(3,2^h). It makes no independence assertion across path events or even across the owner survival events: common neighbors actually create positive association.

The original **first-r sufficient event** gives separately

\[
\Pr(E_U)\ge \binom{b}{r}^{-1}.
\tag{HA-2}
\]

For a PARTICULAR path with strongly shared neighborhoods HA-2 may exceed the degree product in HA-1. Therefore the **best safe local certificate** is their maximum (or the exact EX-2 law). But **for the uniform K=64 bound** HA-1 improves the old worst-case sufficient \(\binom{r(K+1)}r^{-1}\), because for r=2/3 and K≥0,

\[
(K+1)^r \le \binom{r(K+1)}r.
\]

Both physical factor-bit cuts cross each of the r actual proper-path owner pairs with probability exactly 2^(-r) per independent factor, hence exactly 4^(-r) jointly with independent source priority ranks. Thus

\[
\boxed{\Pr(\gamma\text{ survives the actual shared selector})
 \ge4^{-r}\Pr(E_U)
 \ge\frac{1}{4^r\prod_i(d_i+1)}
 \ge\underbrace{\frac1{4^r(K+1)^r}}_{\sigma_r^{\mathrm{H}}}.}
\tag{HA-3}
\]

Define the strengthened universal reciprocal coefficients

\[
\boxed{q_r^{\mathrm{H}}=4^r(K+1)^r.}
\]

For K=64:

| Moment order | Historical q_r = 4^r binom(r(K+1),r) | NEW q_r^H | Reduction |
|---|---:|---:|---:|
| r=2 / fourth | 134,160 | 67,600 | ~1.9846× |
| r=3 / sixth | 77,879,360 | 17,576,000 | ~4.4310× |

These ratios are **universal and proven**, unlike the exact adaptive EX-2 instance probability, whose improvement varies with local source topology.

## 4. NEW all-order exact weighted endpoint Jensen transfer

For each ordered physical endpoint pair (a,b), let G_r(a,b) be the multiset of actual coordinate-proper core r-paths. Let P_r(a,b)=|G_r(a,b)|. Let p_gamma=4^(-r)Pr(E_{owners(gamma)}) be its **exact** survival probability (EX-2), under the SAME one globally shared source priority permutation and SAME two globally shared coordinate cuts.

Define the following completely deterministic nonnegative endpoint matrices:

\[
L_r(a,b)=\sum_{\gamma\in G_r(a,b)}p_\gamma,\quad
H_r(a,b)=4^{-r}\sum_{\gamma\in G_r(a,b)}
           \prod_{i=1}^r(d_{u_i}+1)^{-1}.
\]

Let X_{r,omega}(a,b) count proper r-paths surviving the SINGLE actual global selector omega. Despite shared source flags and colors across paths, linearity gives **exactly** E[X_{r,omega}(a,b)]=L_r(a,b). Jensen on each entry (or variance nonnegativity), plus the matrix fact that X counts a subset of all selected length-r walks and hence is entrywise bounded above by A_{G_omega}^r, gives

\[
\boxed{
(\sigma_r^{\mathrm H})^2\|P_r\|_F^2
\le\|H_r\|_F^2
\le\|L_r\|_F^2
=\|\mathbb E X_{r,\omega}\|_F^2
\le\mathbb E\|X_{r,\omega}\|_F^2
\le\mathbb E\operatorname{tr}(A_{G_\omega}^{2r}).
}
\tag{MO-1}
\]

This hierarchy is all-order exact on the left and is strictly stronger than the old uniform \(q_r^{-2}\|P_r\|_F^2\) lower estimate. In particular, the **NEW universal bound**

\[
\boxed{\|P_r\|_F^2
\le (q_r^{\mathrm H})^2
 \mathbb E\operatorname{tr}(A_{G_\omega}^{2r})}
\tag{MO-2}
\]

holds separately for r=2 and r=3 for every admissible original source and arbitrarily fixed correlated f/g.

**Global moment bridge (conditional on the other inherited lemmas):** every selected physical graph is simple and bipartite from the first physical coordinate cut, so the accepted selected sixth-walk inequality is tr(A^6)≤24 C6+72mΔ². The inherited source six-cycle to distinct ORIGINAL D6 inverse is what supplies C6≤D6, and the LOW assumption D6<δs^6 gives the previously used uniform selected L6s^6. Spectral Cauchy then gives

\[
\operatorname{tr}(A_{G_\omega}^4)
\le\sqrt{\operatorname{tr}(A_{G_\omega}^2)
             \operatorname{tr}(A_{G_\omega}^6)}
\le\sqrt{2m_C L_6}\ s^3.
\]

Since m_C=O(s^4), the right side is O(s^5). Substituting q_r^H into MO-2 improves the unconditional constant in the inherited proper second-/third-path energy controls **without changing the source or the selected random experiment**. The stronger exact matrices H_r and L_r may improve individual correlated instances further but cannot by themselves prove a smaller universal s exponent.

## 5. NEW conditional no-deletion original Branch A threshold ledger

Only **Z=empty** is necessary for issue #230's unweighted seven-class Branch A. Preserve all frozen conditional source geometry and HEAVY/LOW lemmas from [#769](https://github.com/definitely-stable/Mathlab/pull/769), including:

- ORIGINAL no-deletion HEAVY threshold R=93312 and fixed *existential* published ordinary graph C6 supersaturation constants C0≥max(1,C_graph), c0∈(0,min(1,c_graph)];
- actual LOW source |C|≥83s4/104 and its precise Blakley–Roy walk floor W3≥1143574s6/177957;
- independent source FULL A=I, CORE C mixed blockers from [#770](https://github.com/definitely-stable/Mathlab/pull/770), genuine GQ endpoint and physical improper estimates;
- original distinct six-ID P3→BBo two-direction inverse and ordinary physical no-clone C6→D6 inverses, **still separate scientific acceptance tasks**.

For any FORMAL exact rational placeholders C0,c0 satisfying the sign constraints, choose T=ceil(17*93312^3*C0^3/2), L6=24+153T². The historical LOW root arithmetic used

\[
q_2=16\binom{130}2,\qquad q_3=64\binom{195}3.
\]

Replace them by the **proved stronger** constants q2^H=67600, q3^H=17576000, and separately recompute:

\[
\begin{aligned}
L_4^{\mathrm H}
 &= (q_2^{\mathrm H})^2\left\lceil\sqrt{\left\lceil17L_6/4\right\rceil}\right\rceil+19T,\\
B_0&=\left\lceil\sqrt{360(65)T}\right\rceil,\\
E^{\mathrm H}&=5q_3^{\mathrm H}\left\lceil\sqrt{L_6}\right\rceil,\\
D^{\mathrm H}&=4\left\lceil\sqrt{B_0 T L_4^{\mathrm H}}\right\rceil,\\
s_0^{\mathrm H}
 &=\max\{64,444T,(8E^{\mathrm H})^2,(8D^{\mathrm H})^8\}.
\end{aligned}
\tag{ROOT-H}
\]

The new code computes EXACT integer s0 and dyadic h0=ceil(log2 s0), and independently verifies that every NEW ledger cost is no larger and the formal s0 is **strictly smaller** than the matching frozen first-r values for three different FORMAL (C0,c0) input pairs.

**Logical scope:** this is a monotone **conditional improvement** to the old root proof budget, not independent verification of all inherited all-h mathematical prerequisites. The unweighted HEAVY δ=c0/93312^6 does not change; the new q’s reduce LOW/selector error constants and therefore may reduce its sufficient all-h cutoff, without changing the leading s^6 exponent or creating a new ASET exponent. The external graph theorem constants have NOT been numerically identified and are NOT silently replaced with C0=1 or c0=1.

## 6. Scientific falsifiers, exact small combinatorics and source CI

The independent program research/hyp105_original_low_moment_exact_priority.py uses only Python Fraction, combinations, original symplectic incidence fixture, and basic adjacency; it does not import any historical selector, Jensen, HEAVY/LOW, source-sixset or root proof evaluators.

Its standalone exact source priority law EX-2 is crosschecked against TWO independent methods: (1) all local priority permutations, b≤8, and (2) original precedence DAG linear extension integer subset DP, b≤15. These checks include all small r=2 neighbor masks and combinations of all r=3 masks, showing the old first-r and product bounds are incomparable per instance. A mask model with b=195 and all external source neighbors shared exercises EX-2 beyond any 2^20 cap (its owners exceed K=64, clearly marked NOT eligible for the K64 theorem); a second **K64-admissible** mask model has 3×64 disjoint external neighbors, b=195, and exact probability 1/65³, attaining the NEW uniform source Harris bound.

The true ORIGINAL W(3,2) and W(3,4) source models are independently constructed with named flags, two actual opposite physical diagonals per flag, complete separately pair-injective fixed lex/reverse/shift maps, genuine source J and coordinate-proper real physical 2-/3-path owners. For deterministic bounded path samples the code exactly computes the endpoint weighted matrices L_r and H_r, compares their Frobenius energies with both old and new uniform bounds, and marks them explicitly **sampled rather than full-census when capped**. Source probabilities are calculated EXACTLY from one common global-permutation marginal, not from independently resampled owner ranks per path.

The same standalone module computes the complete conditional exact-rational Z0 root moment ledgers with old and NEW q, formal C0/c0 and no manufactured published C6 constants. Dedicated GitHub-hosted specialist workflow runs the exact tests/certificate; INDEX and full Research must succeed on the **same final HEAD** before CI acceptance. All moment/gate status fields reject a false claim that root PROVED_A, B75 or an ASET exponent was established.

**Next mandatory science gate:** independent review of the selected simple bipartite C6→actual six-original-ID D6 inverse and the quantitative global coordinate-return/mixed blocker cost envelopes under the newly sharpened q2/q3. If those all-h lemmas withstand review and root #230's quantifier composition is accepted, Branch A may be eligible for acceptance. Passing finite certificate and green GitHub CI do NOT alone settle this.
