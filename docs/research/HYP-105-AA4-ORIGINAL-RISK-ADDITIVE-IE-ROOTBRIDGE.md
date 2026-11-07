# HYP-105 / #230 — AA4-RISKIE: exact original six-ID additive risk and independent all-100 GF(5) inclusion–exclusion referee

**Scientific Draft** — strict child of frozen, fully-green [#740](https://github.com/definitely-stable/Mathlab/pull/740), parent HEAD \`120742c45dadec6e1edc46d03ed8df6898165e9e\`. Fix **every** genuine original symplectic \(W(3,s)\), \(s=2^h\), with separately complete globally pair-injected original point/line label maps \(f,g\), in arbitrary correlation, and **any** adversarial set Z of original incidence flag IDs. No randomization of f/g, cloning of physical vertices or substitution of synthetic sixsets. This is an independent mathematical audit of the final original-GF(5) risk interface and a new algorithmic 100-signed-case certificate; it is **not** automatic acceptance of the whole Branch A, ASET exponent, merge, root closure or an assertion of numerical supersaturation constants.

## 1. MAJOR RESOLUTION: the actual accepted R3 is an **ADDATIVE EVENT-COUNT EXPECTATION**, not a union probability

The question left open by the preceding #740 report — whether overlapping six-column weighted collisions invalidate the claimed lower bound — is answered definitively by the **frozen primary Mathlab definition**, not by choosing a new interpretation:

- [G5-E0-BOUNDARY-FLOWS.md](HYP-105-G5-E0-BOUNDARY-FLOWS.md), E0.3, defines \(R_k(B_m)=\sum_{\{P,Q\}, |P|=|Q|=k,P\cap Q=\varnothing}\Pr(\sum_{i\in P}w_i=\sum_{i\in Q}w_i)\).
- [G5-E2-B3-B1B-FIVE-SIX-EXACT.md](HYP-105-G5-E2-B3-B1B-FIVE-SIX-EXACT.md), Section 1, explicitly distinguishes the risk SUM of probabilities of **distinct unsigned** \(3v3\) events from their union probability.
- The accepted finite seven-family [G5-E2-B3-E1A](HYP-105-G5-E2-B3-E1A-FIXED-LEADING-MOTIFS.md) already uses this exact risk SUM to obtain positive per-original-six-ID lower bounds.

Thus in a fixed original source with N named incidence columns \(\mathcal I\), assign to each i **independently** one of the exact 51 GF(5) nonzero support-four coefficient patterns \(w_i=(w_{ic})_{c\in S_i}\) satisfying \(\sum_cw_{ic}=4\pmod5\). A collision event has an index

\[
\boxed{\mathcal E=(Q,\{P,Q\setminus P\}),\qquad
Q\in\binom{\mathcal I}{6},\quad P\in\binom Q3.}
\tag{R1}
\]

The two sign sides are **unordered**, because \(\sum_Pw_i=\sum_{Q\setminus P}w_i\) is invariant under swapping them. For each increasing original six-ID ordering \(i_0<\dots<i_5\), impose the **lowest ID \(i_0\) in the plus side**. Choose the remaining two plus IDs from five: precisely \(\binom52=10\) sign masks. Denote these by \(M_{10}\).

For the original six-ID set Q and sign mask \(\varepsilon\), let \(F(Q,\varepsilon)\) be the number of actual independent 51-pattern choices of those six source columns that satisfy every physical GF(5) coordinate cancellation equation. Its marginal event probability is **exactly \(F(Q,\varepsilon)/51^6\)**, even when Q overlaps other sixsets or physical supports share coordinate symbols. **By DEFINITION**, not by the union bound,

\[
\boxed{ R_3(f,g)=\frac1{51^6}
\sum_{Q\in\binom{\mathcal I}{6}}
\sum_{\varepsilon\in M_{10}}
F(Q,\varepsilon). }
\tag{R2}
\]

This indexed sum is the expected **number** of signed 3v3 collision events under independent column-coefficient sampling. Linearity of expectation never assumes collision-event independence. Crucially this is **not** \(\Pr(\bigcup\mathcal E)\) and NOT the probability of even one collision. The only risk interpretation relevant to the original first-moment alteration method is the expected number of bad events.

Every Q is a set of six **distinct ORIGINAL source incidence IDs**, never an ordered path, a physical source graph edge, an \(S_6\) orbit or a sign partition. For distinct Q the ordered pair \((Q,\varepsilon)\) differs automatically; every sign mask is counted once after factoring global sign inversion. Thus no \(6!\), \(2\), \(12\) or physical C6 rotation/reversal divisor may be applied when passing the genuine six-ID abundances to R3. The preceding #734 LOW source threepath produces each real original BBo sixset twice under physical directed path reversal; **that factor 2 was already consumed in its sixset count and must NOT appear again in the risk formula**.

### 1.1. Explicit TRUE ORIGINAL evidence that a union-probability interpretation would be WRONG

The new independently reconstructed original \(W(3,2)\) **lex** source contains two GF(5)-positive B/B-overlap six-ID motifs

\[
Q_1=\{2,10,20,33,35,36\},\qquad
Q_2=\{6,7,21,25,32,34\}.
\]

They are DISJOINT ORIGINAL incidence-ID sets. Let \(A_i\) mean that **at least one** of the ten unsigned balanced-sign events is satisfied on \(Q_i\). Every exact full-51 per-sixset signed weight is positive. The combined typed physical dual graphs of these motifs are connected (proved below), so the ten signs are mutually exclusive **within** each fixed sixset. Thus \(\Pr(A_i)=p_i=(\sum_\varepsilon F(Q_i,\varepsilon))/51^6>0\).

The coefficient choices for Q1 and Q2 are **independent because the source COLUMN ID sets are disjoint**, even though their physical coordinate alphabets are globally shared. Therefore

\[
\Pr(A_1\cup A_2)=p_1+p_2-p_1p_2
< p_1+p_2.
\]

The source risk \(R_3\) contributes \(p_1+p_2\) (plus every other indexed event), **not** that union probability. The code certifies the two genuine original sixsets, their independent exact GF5 weights, \(p_1,p_2\), their strictly positive intersection \(p_1p_2\), and the exact rational difference. This directly disproves an erroneous root review requirement that the events must have disjoint outcomes before their probabilities can be added.

## 2. NEW completely independent 2^12-edge GF(5) inclusion–exclusion oracle

The earlier original GF5 parent [#735](https://github.com/definitely-stable/Mathlab/pull/735) verified the 10-sign D6 and 90-sign BBo weights by a spanning-tree chord-flow algorithm and by partial 51³-vs-51³ meet-in-the-middle checks. **This slice independently rederives and evaluates ALL 100 original signed templates** through finite-field matrix rank plus inclusion–exclusion; the new main production code imports neither the old tree/chord code, Fourier implementation nor previous GF5 result tables.

For each fixed ORIGINAL sixset Q whose first and second physical factors each touch exactly six physical coordinates, every touched physical coordinate has incidence degree exactly two among the SIX distinct original columns. It becomes one distinguishable edge \(e=uv\) of a **dual multigraph** \(\Gamma_Q\) on six vertices (one per original source ID). There are 6 physical coordinates per factor, **12 physically distinct dual edges**, and degree four at every column vertex. Repeated original pair labels contribute **two parallel dual edges**, each carrying an independent GF5 nonzero variable; they must NEVER be collapsed.

Fix any orientation, choose \(z_e=\varepsilon_u w_{u,e}\in\mathbb F_5^\times\) at the oriented first endpoint. The physical signed collision equation imposes the opposite value at the second endpoint. The original column checksum-four conditions become the prescribed divergence

\[
\boxed{ B_\Gamma z=b_\varepsilon,\quad
(b_\varepsilon)_u=4\varepsilon_u\pmod5,\quad
z_e\ne0\text{ for all 12 edges}.}
\tag{R3}
\]

Every solution z corresponds **bijectively** to one valid ordered assignment of the six original 51-pattern coefficient vectors. Therefore \(F(Q,\varepsilon)\) is exactly the number of nonzero boundary-compatible GF5 flows on the (possibly multiple-edge) six-column \(\Gamma_Q\).

For a subset \(D\subseteq E(\Gamma)\) of dual edges forcibly set to zero, let \(H=\Gamma-D\) have c(H) connected components and \(|E(H)|=12-|D|\). The ordinary oriented incidence matrix of H has rank \(6-c(H)\) over \(\mathbb F_5\). The boundary vector is in its image iff

\[
\sum_{u\in C}(b_\varepsilon)_u\equiv0\pmod5
\quad\text{for every component }C\text{ of H}.
\]

If compatible, precisely \(5^{|E(H)|-6+c(H)}\) edge assignments (including zero values on H) satisfy the boundary. By ordinary inclusion–exclusion, the exact count of **nowhere-zero** original coefficient assignments is

\[
\boxed{
F(Q,\varepsilon)=
\sum_{D\subseteq E(\Gamma)}
(-1)^{|D|}
\mathbf1_{\{\text{component-wise boundary compatibility}\}}\,
5^{12-|D|-6+c(\Gamma-D)}.
}
\tag{R4}
\]

There are precisely **2^12 = 4096 deleted-edge sets** per dual template, irrespective of actual h, f/g correlation or number of source flags; Python integers and a six-vertex DSU compute each of their ranks exactly. Even if the inclusion–exclusion terms have opposite signs, the final integer must satisfy \(0\le F\le51^6\). This independent derivation specializes the **previously published** b-compatible nowhere-zero-flow counting identity (Fu–Ren–Wang, *Counting flows of b-compatible graphs*, Advances in Applied Mathematics 168 (2025), 102901), already recognized in Mathlab [E0](HYP-105-G5-E0-BOUNDARY-FLOWS.md). We claim independent **verification and source translation**, NOT discovery of finite-group flow inclusion–exclusion.

## 3. Why EXACTLY NINE genuine BBo source shapes, and all 100 signs are covered

An ORIGINAL B/B-overlap sixset has exactly ONE original point p occurring in two of its flags, exactly ONE original line ell occurring in two flags, and exactly ONE **shared original flag** (p,ell) at that intersection. Label those six original source-column positions so the repeated ORIGINAL point occupies columns 0,1 and the repeated line occupies 0,2.

On the first typed physical factor the repeated original point label is the same physical pair for columns 0 and 1, yielding **two parallel distinct dual-coordinate edges 0–1**. The remaining four ORIGINAL source points are different, with globally pair-injective pair labels, and must meet the remaining FOUR physical coordinate symbols two-at-a-time. Their simple degree-two dual graph on column vertices 2,3,4,5 is a C4, of which there are exactly THREE distinct unoriented possibilities. The second typed factor similarly has two parallel edges 0–2 plus one of THREE C4 possibilities on original source-column positions 1,3,4,5.

Thus there are **3×3=9 complete BBo dual templates up to relabeling of six named ORIGINAL source positions**, each with ten globally-unordered balanced signs, hence **all 90 exact signed BBo cases**. The analogous aligned D6 matching case has identical simple C6 dual graphs on the two factors, giving the same simple six-cycle twice (with physical coordinates distinct by their factor type) and ten sign cases. All 10 abstract dual graph templates are connected.

The new inclusion–exclusion oracle checks all 100 signs and produces

\[
\boxed{\sum_{\varepsilon\in M_{10}}F(D6,\varepsilon)=54162,}
\qquad
\boxed{\min_{\text{9 BBo templates}}\sum_{\varepsilon\in M_{10}}F(BBo,\varepsilon)=53526.}
\tag{R5}
\]

ALL 100 sign weights are strictly positive. Their exact full coefficient table and SHA256 digest are stored in the fail-closed hosted JSON. Tests compare the entire digest and selected actual original templates against the previous **mathematically different** tree/chord evaluator, **TEST ONLY**. The independent main production implementation does not import, read or reuse any older GF5 code or numerical tables.

### 3.1. A second useful all-order structural fact: connected dual ⇒ same-sixset signs disjoint

For one fixed sixset Q with a connected dual \(\Gamma_Q\), suppose the SAME nonzero original coefficient assignment satisfied two signed cancellations \(\varepsilon,\eta\). On every physical dual edge uv we would have

\[
\varepsilon_u w_{u,e}=-\varepsilon_v w_{v,e},
\quad
\eta_u w_{u,e}=-\eta_v w_{v,e}.
\]

As all coefficient entries are **nonzero**, division in GF5 gives
\(\varepsilon_u\eta_u=\varepsilon_v\eta_v\) for each edge uv. Connectivity forces \(\varepsilon_u\eta_u\) to be one constant \(\pm1\) on ALL six source columns; hence \(\eta=\varepsilon\) or \(\eta=-\varepsilon\). Since signs are normalized globally up to complement, these two indices are **the SAME event**.

Therefore within any fixed D6/BBo sixset its ten normalized balanced-sign events are pairwise disjoint. This yields the interpretation of their ten-sign sum as the probability of a collision *somewhere on that particular sixset*; it is a stronger model property but is **not needed** for the additive definition of full R3. Across different sixsets — as the real W32 disjoint-source witness above shows — event intersections generally occur. The full source risk remains a SUM, not the union probability.

## 4. Final exact conditional bridge of the heavy/LOW ORIGINAL sixset theorem to R3

Let \(D_{6,\bar Z}\) count the **distinct named original incidence-ID sixsets** that are aligned and GF5-positive D6, and \(BBo_{\bar Z}\) count the original B/B-overlap class, both avoiding arbitrary named original Z. Their original source point and line degree profiles are different:

- D6 has SIX distinct source points and SIX distinct source lines;
- BBo has ONE twice-used source point and ONE twice-used source line (with their unique intersection flag).

They are therefore **disjoint collections of Q keys**, with no possible duplication. The two direct independent all-100 signed GF5 template floors (R5), together with the correct definition (R2), now give the full **ALL-ORDER NONASYMPTOTIC RISK LOWER**, for EVERY permissible fixed correlated \(f,g\) and every named source Z:

\[
\boxed{
R_3(f,g)\ge
\frac{54162\,D_{6,\bar Z}(f,g)
      +53526\,BBo_{\bar Z}(f,g)}
{51^6}.}
\tag{R6}
\]

There is **no multiplicative penalty** from sharing original source columns or physical coordinates across Q, and NO assumption of independence of the actual collision events. This is simply summing nonnegative terms of the exact original model's definition over two disjoint subclasses of event keys. It is not a lower bound on a union probability.

The separately proved original all-order source heavy/no-clone theorem #739 with the stricter original full-Q deletion radius #740 establishes **conditionally on the genuine, positively existential published ordinary graph \(C_6\) supersaturation theorem and the stated original source geometry/cycle lifts** that for all sufficiently large dyadic \(s\), every admissible fixed correlated pair \(f,g\) and every adversarial \(|Z|\le\rho s^4\),

\[
\text{HEAVY}\implies D_{6,\bar Z}\ge\delta s^6,
\qquad
\text{LOW}\implies
\left(D_{6,\bar Z}\ge\delta s^6\right)
\ \text{or}\ \left(BBo_{\bar Z}\ge\frac{23}{48}s^6\right),
\tag{R7}
\]
where \(K=64\), \(R=370944\), \(C_0\ge\max(1,C_{\rm graph})\), \(0<c_0\le\min(1,c_{\rm graph})\) are **formal rigorous bounds on the unknown positive published graph theorem constants** (not invented numerical values),

\[
T=\Big\lceil\tfrac{17}{2}R^3C_0^3\Big\rceil,
\quad q_r=4^r\binom{r(K+1)}r,
\quad L_6=24+153T^2,
\quad \rho=\frac{16}{12q_3^2L_6},
\quad\delta=\frac{c_0}{R^6}.
\]

The full LOW constants \(L_4,B_0,E,D,s_0\) and their exact 810/840/847 *formal only* dyadic examples are independently reconstructed in the new source root lemma and crosschecked against #740 **only in a separate unit test**. Since \(c_0\le1\),

\[
\frac{53526\cdot23}{48}\gg54162\delta,
\]

and the branch-aware original risk implication is

\[
\boxed{
R_3(f,g)\ge
\frac{54162\,c_0}{370944^6\,51^6}\,s^6
}\tag{R8}
\]

for the stated original source assumptions and ALL dyadic \(s\ge s_0(C_0,c_0)\). The coefficient is an absolute positive number once one chooses **actual valid** bounds on the existential published graph constants; the formal probes do not establish their numerical values. The statement is a true **conditional composition** of individually stated source lemmas, not yet a full independently signed-off all-order root theorem.

### Why not automatically mark root #230 PROVED_A?

The original scientific governance of issue #230 explicitly requires independent mathematical proof of **all** source and physical lifts, source deletion/selector estimates, external theorem applicability and full proof dependency composition, not merely a green CI or a correct risk-event algebra identity. This slice now independently proves the R3 additive/no-overcount interface and independently rederives all 100 requisite GF5 exact weights; **the final global all-order source theorem is still a Draft under independent review**. This audit does not assert the stronger strict ASET extraction exponent, exclude methods other than this GQ alteration model, or close upstream #176/#169.

## 5. Genuine source examples, negative tests and artifact acceptance

The new main certificate reconstructs **nine independently named genuine ORIGINAL W32/W34 six-ID source examples**, including both W32 lex BBo disjoint positive sixsets, W32 reverse-line independently shifted f/g, W34 lex and reverse-line and separately shifted f/g genuine BBo witnesses, and all THREE positive genuine W34 D6 source seed sixsets. Each witness is classified from its **actual original point/line multiplicities and actual global physical pair incidence**, not assigned its class by the historical classifier. The twelve actual physical typed-coordinate dual edges are built directly from the six original source flag supports. A completely separate 4096-subgraph inclusion–exclusion calculation recomputes all ten GF5 signed event probabilities for each sample.

The negative tests reject duplicate/orphan source flag IDs, invalid six-column support or pair-label graphs, misidentified A/A 2C3 as D6, fake numerical graph constants, global sign complement counted twice, illegal untyped point/line coupling, and any disagreement with the exact 51-pattern palette.

Specialized GitHub-hosted Ubuntu 24.04/Python 3.12 workflow runs **13 independent tests** plus a strict complete original-source symbolic-root-and-100-GF5-template JSON artifact; INDEX and full Research must be verified on the **same final PR HEAD** before engineering acceptance. A nonvacuous genuine W32 dual-source event intersection falsifier is compulsory in the CI proof, not an optional illustration.

**Scientific STOP / NEXT gate:** this final independent risk model audit **removes the false overlap/union-probability blocker**. The only remaining root work should be an independent *line-by-line proof-dependency acceptance review* of the all-order original high/low source construction and original six-ID D6/BBo lifts, plus the correct logical normalization of existential external graph theorem constants. Until that audit is accepted, **root #230 stays OPEN_WITH_FORMAL_BLOCKER; no merge, no ASET exponent**.
