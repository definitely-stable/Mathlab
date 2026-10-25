# HYP-105 / #230 AA4-WE — weighted physical 3-walk concentration at typed source endpoints

**Status:** DRAFT / finite independently falsifiable evidence; root OPEN_WITH_FORMAL_BLOCKER.

## 1. Precisely typed state space

Fix any dyadic \(s=2^h\), a genuine original symplectic \(W(3,s)\), and two complete, separately injected, arbitrarily correlated typed mappings \(f:P\to\binom{[a]}2\), \(g:L\to\binom{[a]}2\). Write \(V=(s+1)(s^2+1)\), \(U=V(V-s-1)=Vs^2(s+1)\), and

\[
\mathcal E=\{(q,r)\in P\times L:q\notin r\}.
\]

Each \((q,r)\) has one genuine original 3-incidence path \(q-l_0-p-r\). Define **left bad** if \(f(q)\cap f(p)\neq\varnothing\), **right bad** if \(g(l_0)\cap g(r)\neq\varnothing\), and let \(B\subseteq\mathcal E\) be their union.

The previous clean slice proves \(|B|\le4Vs(a-2)=O(s^{11/2})\). This counts **typed original pairs**, not physical paths.

Construct the physical undirected multigraph \(H(f,g)\) with vertices \((x,y)\in[a]^2\). For each genuine original incidence \((p,l)\), with \(f(p)=\{u,v\}\), \(g(l)=\{x,y\}\), insert the **two matching edges**
\((u,x)\!-\!(v,y)\) and \((u,y)\!-\!(v,x)\), counting any parallel edges with source multiplicity.

A directed physical 3-walk \(v_0-v_1-v_2-v_3\) is **proper** iff its four first coordinates are pairwise distinct and independently its four second coordinates are pairwise distinct. Its endpoint first-coordinate pair determines \(q\) via \(f^{-1}\) if occupied; its endpoint second-coordinate pair determines \(r\) via \(g^{-1}\). We count only those with occupied, genuinely **nonincident** \((q,r)\).

Define \(N_3(q,r)\) to be the number of these directed proper physical walks, **including** those later rejected by internal blocking. Define \(P=\sum_{\mathcal E}N_3(q,r)\) and \(M_B=\sum_B N_3(q,r)\).

**Do not silently substitute \(N_3\) with all physical 3-walks, the raw GQ source 3-path count, internal-unblocked paths, or GF(5)-positive original 6-flag motifs.**

## 2. Exact all-h statements: identity, not an asymptotic solution

For uniform random \((q,r)\in\mathcal E\), put \(I_B=1_B(q,r)\). Directly expanding covariance gives the exact deterministic identity

\[
M_B=\frac{|B|}{U}\,P+
U\,\mathrm{Cov}_{\mathcal E}(I_B,N_3).
\]

No independence, randomness of maps, GQ automorphisms or spectral mixing is invoked. A valid universal proof \(M_B=o(s^6)\) via this identity would require **both** \((|B|/U)P=o(s^6)\) and \(U\mathrm{Cov}(I_B,N_3)=o(s^6)\), or suitable signed compensation; neither has been proved.

If an independent **upper** bound on the restricted weighted second moment is available, then

\[
M_B\le\sqrt{|B|\sum_{(q,r)\in B}N_3(q,r)^2}.
\]

Thus a **sufficient, not necessary** asymptotic criterion given \(|B|=O(s^{11/2})\) is \(\sum_B N_3^2=o(s^{13/2})\). Likewise \(\max_{B}N_3=o(s^{1/2})\) suffices. Neither condition is asserted universally. **A lower bound** \(\Omega(s^7)\) on a second moment cannot establish any corresponding upper bound.

### Path blocking implication

Every proper physical path on a **left-bad** \((q,r)\) necessarily uses both first coordinates in \(f(q)\) at the endpoints and therefore intersects \(f(p)\) at the unique original projection midpoint \(p\). The analogous implication holds on the right. Hence **every bad-pair proper physical path is internally blocked**, yielding an exact inclusion and count inequality

\[
M_B\le P_{\mathrm{blocked}}.
\]

The converse is false: good-endpoint pairs can still have blocked physical walks because their intermediate physical coordinates collide with the projected source point or line.

Let \\(I_G\\) be the exact number of such internally blocked **directed proper paths** on good endpoints. Reversing a coordinate-distinct physical directed path preserves the projection and blocked/unblocked status and has no fixed points. Thus the exact **projected physical B/B-overlap surrogate** satisfies the stronger deterministic identity

\\[
2\\,\\mathrm{BBo}_{\\mathrm{proj}}=P-M_B-I_G.
\\]

This is all-h for the specified projection model, NOT an identification with the historical accepted six-*original-incidence*-flag GF(5) class. In the finite W(3,4) witness:
\\[
2\\cdot5261=58730-35616-12592=10522.
\\]

The separate **good-endpoint internal blocking** term \\(I_G\\) is therefore another indispensable P0 obstacle: even if \\(M_B=o(s^6)\\), a universal bound for \\(I_G\\) or a cross-class GF(5) compensation argument is needed.

## 3. Exact independently indexed W(3,4) witness

At the explicit `research/hyp105_w34_adversarial_certificate.json` mapping:

| Measure | Integer count |
|:--|--:|
| Typed nonincident point-line pairs \(U\) | 6,800 |
| Left-bad pairs | 2,408 |
| Right-bad pairs | 2,496 |
| Both bad | 818 |
| Bad union \(|B|\) | 4,086 |
| Good pairs | 2,714 |
| Proper physical directed 3-walks | 70,476 |
| Missing-physical-endpoint projections | 8,306 |
| Original-incident projections | 3,440 |
| Valid original-nonincident path mass \(P\) | 58,730 |
| Bad-pair path mass \(M_B\) | **35,616** |
| Good-pair path mass | 23,114 |
| Left-bad / right-bad / intersection path masses | 21,238 / 21,714 / 7,336 |
| Full \(\sum_{\mathcal E}N_3^2\) | 676,700 |
| Bad / good restricted second moments | 415,704 / 260,996 |
| Source pairs with no eligible physical path | 187 |
| Maximum finite typed-pair multiplicity | 38 |
| Internally blocked physical path mass | 48,208 |
| Internally unblocked physical path mass | 10,522 |
| Additional blocked mass on *good* endpoint pairs | 12,592 |

The **unweighted** bad-pair proportion is \(4086/6800\approx60.088\%\).
The **weighted** bad-path proportion is \(35616/58730\approx60.644\%\).
Their difference is exactly \(35616/58730-4086/6800\), about **0.556 percentage points**. A small difference at \(s=4\) neither proves asymptotic decorrelation nor even a nontrivial universal bound.

Two distinct exact enumerations are implemented and compared for **every one of the 6,800 source nonincident pairs**: (A) physical arc-first directed 3-walk census and source endpoint inversion; (B) a four-corner, per-pair sparse adjacency-multigraph contraction with products of edge multiplicities. Tests also independently permute both physical alphabets and verify every count remains unchanged.

## 4. Next mathematical gate

The actual P0 frontier is to bound **fixed-label path-weighted concentration** on bad original typed pairs, or prove compensating positive historical GF(5) six-original-incidence-ID counts that do not require such a bound. A promise of low **unweighted** \(|B|/U\), finite \(s=4\) moments, random map averaging, and one-sided spectral expansion is not sufficient for universal correlated \(f,g\).

Acceptance: independently reproducible finite counts and conditional identities only, complete exact-head research CI, qualified proof review. **Root A/B/C open; never claim strict R3/ASET improvement**.
