# HYP-105 / #230 — AA4-CB: original fixed-(f,g) GF(2) incidence-boundary filter and seven-class center certificate

**SCIENTIFIC DRAFT**, strict child of [AA4-CA #601](https://github.com/definitely-stable/Mathlab/pull/601), pinned parent exact HEAD efb95dd2f1fb876f4b93ff2c0109ce6fb337c687. No changes to main or accepted scientific claim registries. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN_WITH_FORMAL_BLOCKER.

## What is genuinely new here / what is prior

Root requires genuine symplectic original W(3,s), s=2^h,h>=1, complete globally injective typed physical pair-edge point f and line g maps with ARBITRARY correlations, the SAME SIX DISTinct original source incidence IDs Q on BOTH typed physical projections and all SEVEN historical positive GF(5) classes. The quantity W is only the historically necessary 51-column selected GF5 weighted **seven-class subtotal** (not entire R3/R2).

[#587](https://github.com/definitely-stable/Mathlab/pull/587) already proves Walsh degree≤6 under whole-original-LINE source-factor image swaps; [#590](https://github.com/definitely-stable/Mathlab/pull/590) already proves original Q-local swap support. [#597](https://github.com/definitely-stable/Mathlab/pull/597) already provides an f-only conditional all-seven original-center highpass certificate. [#599](https://github.com/definitely-stable/Mathlab/pull/599) proves single-edge swap exclusion, [#600](https://github.com/definitely-stable/Mathlab/pull/600) proves genuine right physical 2-regular at-most-three neighbors, and immediate parent [#601](https://github.com/definitely-stable/Mathlab/pull/601) proves the SHARP **abstract independent+N3** Boolean sixcube highpass constant η6=15/16, and retains η4=1/2,η5=15/16. ALL of those original-source general facts are credited and NOT replicated as inventions.

**NEW AA4-CB scoped result:** for the SAME complete original pair (f,g) and each true-source sixflag Q, the right PHYSICAL edge-degree parity at all 64 full g swaps is an exact **affine map over GF(2)**. Its zero set is either empty or an affine coset of computable dimension k−r. Right historical GF5 acceptance is supported in that coset, and even more tightly in the literal right physical 2-regular sub-support. This yields **strictly map-conditioned, source-local, all-SEVEN weighted highpass center and uniform-map certificates** by screening impossibilities WITHOUT evaluating the historical right GF5 seven-class acceptance itself. General graph boundary operators, GF(2) cycle spaces, Gaussian elimination and the Walsh kernel are classical mathematical tools; this is the specific genuine-original fixed-pair filtered research construction, not a claim of their invention.

## Precise all-h original data and unchanged-map quantifiers

Fix arbitrary h>=1, s=2^h, genuine W(3,s), and ANY complete globally injected original typed physical pair-edge maps f,g into E(K_a), a minimal such that binom(a,2)>=V=(s+1)(s²+1). No independence or automorphism symmetry is assumed. Fix SIX PAIRWISE DISJOINT pairs P_i={u_i,v_i} of TRUE ORIGINAL source LINE-factor IDs. Toggling any subset x∈{0,1}^6 transposes the ENTIRE original pair-edge images g(u_i),g(v_i), defining ONE complete original LINE map g^x at each vertex. Occupied right physical edges, original incidence flag IDs and original f are identical across ALL 64 vertices.

Fix Q, an unordered set of SIX DISTINCT REAL ORIGINAL incidence IDs, with the same Q used to project physically left and right. Each source right LINE ID ℓ may appear with multiplicity m_Q(ℓ)≥0 in this same Q. Define the physical GRAPH boundary \(\partial\{a,b\}=e_a+e_b\in\mathrm{GF}(2)^a\) for a genuine physical unordered pair edge, and

\[
b_Q=\bigoplus_{(p,\ell)\in Q}\partial g(\ell)
\quad\text{and}\quad
d_{Qi}=(m_Q(u_i)+m_Q(v_i)\bmod2)\,[\,\partial g(u_i)\oplus\partial g(v_i)\,].
\]

**All-h theorem CB-AFFINE:**

\[
\boxed{\partial_{\rm right}(Q,g^x)
=b_Q\oplus\bigoplus_{i=1}^6 x_i d_{Qi}.}
\tag{CB-1}
\]

Only k≤6 swap packets actually touched by Q are needed in its local Boolean cube, and the other six−k global swaps do not change Q. The proof is linearity of GF(2) edge boundary and the fact that toggling a WHOLE original LINE-factor physical image pair changes every occurrence of each source LINE consistently. The formula remains correct when a true original LINE source factor occurs TWICE in Q or Q contains BOTH factor IDs of the same swap packet: the changes cancel correctly modulo two. This is why replacing genuine Q by six independently redrawn edges would break the model and is forbidden.

Let D_Q be the local GF(2) matrix with columns d_Qi for touched packets i. Let r_Q be its rank and define the **right even-degree support**

\[
\mathcal P_Q(g)=\{y\in\{0,1\}^{k_Q}:D_Q y=b_Q\}.
\]

Then \(\mathcal P_Q(g)\) is either EMPTY (the original selected Q can never have any historically accepted right 2-regular projection under any of these full global g swaps), or an AFFINE coset of \(\ker D_Q\), containing EXACTLY \(2^{k_Q-r_Q}\) local states. This is finite linear algebra, valid all h and for arbitrarily correlated complete original (f,g).

Define the even more restrictive **literal physical right 2-factor support**

\[
\mathcal T_Q(g)=\{y\in\mathcal P_Q(g):
\text{six projected right physical edges have exactly six vertices of degree two}\}.
\]

For a historical positive seven-class original-source-immutable Q, let I_Q(y)∈{0,1} be its true original GF5 selected acceptance at complete global map g^y. Then for EVERY y,

\[
\boxed{I_Q(y)=1\Longrightarrow y\in\mathcal T_Q(g)\subseteq\mathcal P_Q(g).}
\tag{CB-2}
\]

Both necessary supports are computed using the ORIGINAL globally injected g and TRUE original source Q, NOT the GF5 accepted classifier or fictitious high-h source geometry. In particular, if \(\mathcal P_Q=\varnothing\), the Q makes NO contribution to ANY Walsh order in this sixcube, including the zero and low orders. This is a concrete new *original-map conditioned* obstruction, unlike parent f-only highpass estimates which still count such impossible Q.

## New original-center and all-vertex signed-kernel envelope

For k=k_Q and the classical degree>3 local Walsh kernel from #597,

\[
K_k(z)=\sum_{\substack{T\subseteq[k]\\|T|\ge4}}(-1)^{|T\cap z|},
\]

let X be ANY necessary support containing the actual accepted state set \(\{y:I_Q(y)=1\}\), for example X=P_Q or X=T_Q. For any desired local cube reference vertex x, the exact local highpass value is

\[
R_Q(x)=2^{-k}\sum_{y\in X}I_Q(y)K_k(x\oplus y).
\]

Since 0≤I_Q(y)≤1 (and vanishes outside X), the following **two-sided** support envelope is mathematically exact as an inequality:

\[
\boxed{
|R_Q(x)|\le L_k(X,x):=
2^{-k}\max\bigg\{
\sum_{y\in X}[K_k(x\oplus y)]_+,\;
\sum_{y\in X}[-K_k(x\oplus y)]_+
\bigg\}.}
\tag{CB-3}
\]

For k≤3, the highpass is identically zero. Define both a center-specific L_k(X,0) and a uniform \(L_k^{\max}(X)=\max_x L_k(X,x)\). All are computed with exact signed integers/Fractions from at most 64 local global right states. As X shrinks, the bound NEVER increases. This is a genuine *a posteriori* original-g structural restriction; **it does not assert that arbitrary subsets of X are physically realizable historical GF5 motifs**.

For each genuine original Q whose unchanged physical LEFT f-projection is historically six-coordinate eligible and whose immutable source type c(Q) is one of the SEVEN accepted GF5 classes, let w_c be the fixed historical positive 51-column necessary GF5 weights

\[
w=(5643,\;45600,\;45600,\;43320,\;49050,\;51750,\;45010).
\]

The all-seven historical selected GF5 source score is \(W(x)=\sum_Q w_{c(Q)} I_Q(x)\), **using each SAME Q on both sides and one WHOLE g^x**.

For a given ORIGINAL fixed physical pair f,g, let

\[
E^{P}_{f,g}(x)=\sum_{Q:k_Q\ge4}w_{c(Q)}L_{k_Q}(\mathcal P_Q(g),x|_{D_Q}),\quad
E^{T}_{f,g}(x)=\sum_{Q:k_Q\ge4}w_{c(Q)}L_{k_Q}(\mathcal T_Q(g),x|_{D_Q}).
\]

Then for ALL h and all x simultaneously,

\[
\boxed{|W(x)-P_{\le3}W(x)|\le E^T_{f,g}(x)\le E^P_{f,g}(x).}
\tag{CB-4}
\]

For a single uniform envelope take the sum of each Q's max over x rather than evaluating a global max, giving an explicit bound \(E^T_{f,g,\rm uniform}\le E^P_{f,g,\rm uniform}\) holding for ALL 64 global vertices. The center-specific E(0) is at least as strong for the UNCHANGED input. The per-Q true original GF5 universal physical constraints from #601 may also be intersected with these support bounds (or conservatively cap aggregate E by #601's old f-only E) without changing validity. Our finite W32 implementation computes **min(parent f-only E, each of the four g-conditioned aggregate envelopes)**: this is conservative compared to summing per-Q minima, but preserves their correct nesting and yields a strict data-driven improvement whenever the new original-g screens exclude enough source Q.

In particular on the ORIGINAL unchanged full f,g,

\[
\boxed{
W(f,g)=P_{\le3}W(0)+R_{>3}W(0)
\ge\max\{0,\;P_{\le3}W(0)-E^T_{f,g}(0)\}.
}
\tag{CB-5}
\]

This is the first explicit **unchanged-g right GRAPH-boundary filtered** version in this research chain; it cannot be derived from f-only envelopes without using the actual original g. The P≤3 term remains a SIGNED all-seven historical zero/low-order expression whose desired universal positive \(\Omega(s^6)\) margin is NOT established.

## Independent falsifiers and test scope

The additive dedicated GitHub-hosted three-job workflow covers:

1. Exact GF(2) column rank and local-affine coset dimension on authentic original W32 lex/S72 source Q of historical possible seven-class types and 4,5,6 touched original LINE image swap packets. Independently produce ALL local complete globally swapped right maps via the existing independent original whole-map transposition routine. Literal physical degree-parity of SAME six source incidence IDs is checked directly at every local state, without invoking the new affine calculation. Parity coset counts are 0 or exactly \(2^{k-r}\). Historical real GF5 original acceptance is independently confirmed to be a SUBSET of the actual right physical 2factor states and thus of zero-parity states, not the other way around.
2. A second direct signed Walsh-kernel positive/negative support-sum oracle verifies center-specific and ALL-vertex parity/physical-2regular bounds against independently evaluated local supports (not source-GQ enumeration).
3. Full TRUE symplectic original W32/K6 lex and S72 selected historical seven-class left-eligible source sixflag sets: compute map-conditioned ALL SEVEN f,g weighted 51-column E^P and E^T, plus prior #601 f-only upper for comparison, with NO complete historical right GF5 classifier in the support pass.
4. Independently, the complete original 64-map seven_census historical GF5 weighted source score from #597–601 provides the exact signed degree4+5+6 residual at every vertex. Confirm the tighter right-support **uniform** bounds at all 64 vertices and the stronger center-specific bounds against the actual ORIGINAL unchanged state. A positive-margin claim is accepted only if it actually passes the historical original census.
5. Change the ENTIRE globally injected original right g label assignment while preserving left f and the occupied right palette. Assert parent f-only E is invariant while every new parity/g-conditioned bound remains valid; DO NOT assume a particular map perturbation must strictly change the numerical E.
6. Negative genuine source: invalid six DISTINCT incidence IDs, overlapping or missing packets, malformed complete physical g injection, fake W34-as-W32 finite census, bad local state supports fail closed.
7. TRUE symplectic W34 GF4 with nononto physical K14 palettes lex/random, real source incidence IDs, each sixpacket source Q with genuine LINE IDs one per packet; independently compare the affine parity coset to all 64 complete global right image assignments. This is a finite source-GQ falsifier, not a fabricated high-h model.

The all-h proof is algebraic and does not claim an efficient \(\Theta(s^{?})\) enumeration of all original six-Q candidates at huge h. The W32 complete search is finite evidence ONLY; tests cannot prove the all-h existence/positivity root hypothesis.

## Why this is closer to root #230 but still only a partial theorem

Unlike successive bounds on the **abstract maximum norm** of one sixth-order indicator, CB-1 and CB-2 identify candidate original sixflag Q that are impossible under **the particular unmodified correlated physical right g**, and quantify their exact zero-parity coset by rank. The original source f and g appear together in the verified W32 all-seven lower certificate, not in a hypothetical independently repaired map. This could materially reduce the sign-uncertainty in concrete models and isolate true low-order problematic Q.

However this remains an a posteriori **conditional** lower bound. It proves NEITHER all-fixed-pair \(W(f,g)=\Omega(s^6)\) Branch A, NOR an infinite genuine correlated original W3 family with o(s^6) Branch B, NOR the exact full model-equivalent restricted inequality specified by Branch C. Since root #230 counts unweighted sum of seven motif multiplicities while the historical necessary R3 numerator W uses positive weights, even a lower on W would require relating the two (which is straightforward by fixed positive min/max weights), but the missing positive **universal low-order margin** is still fundamental. No full R3/ASET strict extraction exponent follows.

Keep Scientific Draft, not merged. Require exact final HEAD dedicated GitHub-hosted CI, INDEX, Proof Audit, Full Research, and **independent mathematical referee** of the parity-occurrence multiplicity and signed support-to-center argument plus accepted parent #601/#600/#599/#597 proof chain. Classical GF(2) graph incidence and Walsh theory cited to avoid any spurious general novelty claim (see O'Donnell *Analysis of Boolean Functions*, arXiv:2105.10386).


## Exact original unchanged W32 evidence: first nonvacuous lower in this seven-class center-kernel stack

The GH-hosted **REAL ORIGINAL** symplectic W(3,2)/physical complete K6 full-map historical seven-GF5 census independently reports the following exact integers and fractions on the SAME initial global map f,g and six TRUE disjoint original LINE-factor image-swap packets (0,1),(2,3),(4,5),(6,7),(8,9),(10,11):

| Full genuine original W32 maps | lex | S72 |
|---|---:|---:|
| Actual historically selected original Q with k_Q≥4 source swaps | 33,046 | 34,180 |
| Prior #601 original f-only seven-class E_f | 8,113,433,771/16 | 3,883,420,431/8 |
| NEW parity-conditioned original CENTER E^P(0) | 711,282,039/32 | 665,944,131/32 |
| NEW parity-conditioned UNIFORM E^P | 441,004,815/16 | 478,795,125/16 |
| NEW physical RIGHT 2-factor original CENTER E^T(0) | **23,948,391/4** | **75,391,507/16** |
| NEW physical RIGHT 2-factor UNIFORM E^T | 131,302,517/16 | 155,092,423/16 |
| ACTUAL original low-order P≤3 W(0) | 90,904,087/8 | 105,103,511/32 |
| ACTUAL signed original high-order R>3 W(0) | −1,097,727/8 | −27,991/32 |
| ACTUAL original selected seven-class weighted W(f,g) | 11,225,795 | 3,283,610 |
| NEW rigorously certified unchanged original W(f,g) lower | **43,007,305/8 > 0** | **0** |

The lower lex number follows exactly from **the proven source-specific two-sided Walsh support inequality**, with no use of its actual historical acceptance to build the new right-only error:

\[
\frac{90,904,087}{8}-\frac{23,948,391}{4}
=\boxed{\frac{43,007,305}{8}}
=5,375,913.125.
\]

The original lex historical W equals 11,225,795, so the certified lower is correct and NONVACUOUS. All seven historical GF5 weights are at most 51,750, so the original unweighted sum of selected seven positive sixflag multiplicities obeys the concrete, **finite ORIGINAL W32-specific** consequence

\[
\boxed{S_2(f_{\mathrm{lex}},g_{\mathrm{lex}})
\ge \left\lceil \frac{43,007,305}{8\cdot51,750}\right\rceil=104.}
\]

The unweighted W32 ≥104 statement is not the root ALL-h theorem; here s=2 is FIXED and the input is ONE specific complete globally injected physical f,g labeling. This is nonetheless a substantive advance over the previous entire absolute original f-only highpass certificate chain #597–601, which returned ZERO on this same lex map. The difference is that AA4-CB uses the **actual unmodified right physical assignment g** to eliminate absent-parity and absent-right-2factor source states *before* budgeting the signed highpass.

For S72 the new right-only center error is still larger than its low-order P≤3 value, so **the positive margin does not follow** even though the actual W is positive. The method therefore proves no universal original-center positivity even for all W32 f,g, much less all dyadic h. The map-conditioned parity center error is larger than its nested 2-factor center error in both genuine examples; the improvement is independent of historical source class acceptance on the RIGHT because only raw physical vertex degrees are screened.

These exact values are pinned as Fraction regressions on the FINAL child head, and the whole independent historical all-seven 64-map census is a separate falsifier rather than the source of the geometric error itself. The additional true-original repeated-LINE source flag test deliberately selects source Q with BOTH source LINE factors of a packet, including two occurrences of each, verifying that the affine GF2 delta cancels according to multiplicities. The true W34 GF4 nononto K14 test separately verifies the same algebra on 64 COMPLETE original global right assignments without pretending to compute giant-h source sixflag counts.
