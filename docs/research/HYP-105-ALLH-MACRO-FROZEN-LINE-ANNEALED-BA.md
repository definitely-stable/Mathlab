# HYP-105 / #230 — AA4-MFREEZE: conditional annealed GF(5) B/A survives a **macroscopic** number of frozen ORIGINAL line labels

**New all-\(h\) theorem; root remains OPEN_WITH_FORMAL_BLOCKER.** Scientific Draft, dependent on [AA4-ANNBA #669](https://github.com/definitely-stable/Mathlab/pull/669). No all-completed-\(g\) assertion, full \(R_3\) bound, new ASET exponent or root Branch A/B/C promotion.

## 1. The gap in AA4-ANNBA

The exact predecessor [#669](https://github.com/definitely-stable/Mathlab/pull/669) proves a uniform conditional \((140-o(1))s^6\) lower expectation of original GF(5) B-left/A-right sixsets when only \(b=o(s)\) ORIGINAL source line factor labels are frozen. Its six-distinct-source-line generator pessimistically subtracts **all b frozen lines from EVERY original point pencil**, obtaining \(d-b\) free choices. This becomes vacuous when \(b\ge d-5\), even though there are \(V=(s+1)(s^2+1)\sim s^3\) original lines and a typical pencil can remain almost unfrozen.

The following theorem repairs **that exact step**, using the true original point–line incidence first moment. It does NOT exchange first moment and adversarial minimum.

## 2. Statement — exact all-h uniform conditional lower bound

Let \(s=2^h\) with \(h\ge1\), \(d=s+1\), \(V=d(s^2+1)\), \(a=\min\{t:\binom t2\ge V\}\), \(M=\binom a2\). Fix an **arbitrary** complete globally injective physical pair-label map
\(f:P(W(3,s))\to E(K_a)\). Fix **any** \(b\) DIFFERENT ORIGINAL source lines \(J\subset L(W(3,s))\), \(0\le b\le V\), and **any** globally injected legal frozen right physical labels \(g_J:J\to E(K_a)\). Complete all remaining original source lines using **one uniformly random injection without replacement** into \(E(K_a)\setminus g_J(J)\).

For each integer threshold \(0\le k\le d\), set
\[
\begin{aligned}
G_k&=\left[V-\left\lfloor\frac{bd}{k+1}\right\rfloor\right]_+, &
q_k&=d-k,\\
Q_k&=\left[3\binom{a-2}{4}
       -2(M-G_k)\binom{a-4}{2}\right]_+,\\
T_k&=\binom{q_k}{2}(q_k-2)(q_k-3)(q_k-4)(q_k-5)
      \quad\text{if }q_k\ge6,\quad 0\text{ otherwise},\\
P_{a,b}&=\frac{720\left[70\binom a6-
                  28b\binom{a-2}{4}\right]_+}{(M-b)_6},
\end{aligned}
\]
where \(P_{a,b}=0\) if \(M-b<6\), \([z]_+=\max(0,z)\), and \((x)_6\) is the falling factorial.

**All-h theorem (universal quantification of frozen input; conditional first moment of the completion):**
\[
\boxed{
\quad \mathbb E_{g\mid g_J}
  U_{B\text{-left}/A\text{-right}}(f,g)
  \ \ge\ \max_{0\le k\le d-6}\;G_k\,Q_k\,T_k\,P_{a,b}.
\quad}\tag{MFREEZE}
\]
When the max has no eligible \(k\), its value is zero. This is an exact rational lower bound for **SIX DISTINCT genuine ORIGINAL incidence IDs ONCE**, individually positively accepted in the historical GF(5) 51-palette B/A class. Every point/line source factor in the proof is a real factor of the same fixed \(W(3,s)\) and the same six flags are seen by both physical halves.

For \(b=0,k=0\), the formula is **exactly the AA4-ANNBA lower formula**. Taking a maximum over all \(k\) never weakens that valid baseline.

## 3. Proof — original regular source-pencil incidence transfer

For each genuine original point \(p\) let
\(t_p=\#\{\ell\in J:(p,\ell)\text{ is one of the genuine source flags}\}\).
Because **each original line of \(W(3,s)\) is incident with exactly \(d\) ORIGINAL points**, independently of physical labels,
\[
  \sum_{p\in P(W(3,s))}t_p=bd. \tag{1}
\]
If \(t_p>k\), then \(t_p\ge k+1\); hence there are at most \(\lfloor bd/(k+1)\rfloor\) such original point factors. Thus at least \(G_k\) genuine **good** original points have at most \(k\) frozen lines in their original pencils, or at least \(q_k=d-k\) UNFROZEN genuine source line IDs each. No random source geometry or independence assumption is used.

The globally injected physical point map \(f\) takes the set of good original points to at least \(G_k\) DIFFERENT K_a edges, so **at most \(M-G_k\)** pair-label edges of \(K_a\) are *not images of good source points*. Fix ANY good genuine point \(p\) with physical image edge \(\{u,v\}\). On the other \(a-2\) coordinate symbols, there are exactly \(3\binom{a-2}{4}\) simple C4s. Each unavailable good-point-label edge destroys at most \(2\binom{a-4}{2}\) of them, by choosing the other two physical symbols and either of the two four-cycles containing a specified edge. The union bound gives at least \(Q_k\) surviving pair-coordinate-disjoint 4-cycles. Each surviving C4 identifies **four other DISTINCT good ORIGINAL point factors** \(p_1,\ldots,p_4\) because physical f is globally injective. Each \(p_i\) has at least \(q_k\) genuine source lines outside J.

Choose TWO distinct true original source line factors outside J incident with \(p\), in at least \(\binom{q_k}{2}\) ways, then one original line incident with each of the four distinct C4 points, avoiding J and **every previously used original line ID**. The \(i\)-th singleton source point has at least \(q_k-(i+1)\) possible new source lines, because at most \(i+1\) actual ORIGINAL line IDs have been selected. This yields \(T_k\) genuine six-ID source selections. The original point multiplicities are exactly B, and the left physical degree-two projection is a doubled pair edge disjoint from a single simple C4, using **exactly six physical coordinates**.

The constructed source sixsets are **all distinct**: recover the unique original point repeated twice; its repeated physical pair edge; and the unique C4 source point set. A fixed cycle is a SET of its four physical edges, not four cyclic starting positions. The selected flag IDs then recover the six ORIGINAL line IDs uniquely. Therefore there are at least \(G_kQ_kT_k\) distinct genuine left-B candidates whose SIX original source line IDs are all distinct and outside the frozen J.

For every such sixset, the uniform injection assigning physical right pair labels to the six ORIGINAL unfrozen source line factors is a uniform **ordered without-replacement six-tuple** from the \(M-b\) unused K_a edges, regardless of all other source flags or the fixed complete f. The exact number of six-edge 2-regular graphs on six K_a physical vertices is \(70\binom a6\): exactly 70 C6-or-two-triangles subgraphs per physical six-symbol set. A forbidden frozen physical edge lies in exactly \(28\binom{a-2}{4}\) of them. Thus at least \([70\binom a6-28b\binom{a-2}4]_+\) six-edge physical two-factors survive, each with \(6!=720\) ordered assignments. Every surviving event makes the right physical projection A (six different ORIGINAL source line factors, exactly six physical degree-two symbols), while the left is the genuine B construction above. The historical classifier accepts this original sixset as positive GF(5) B-left/A-right.

Linearity of expectation yields (MFREEZE). **All physical labels are globally injected and all six flags refer to the SAME original source incidences**; no independent random maps, synthetic physical graph, matched orbit quotient or adversarial-to-annealed transfer is introduced.

## 4. Stronger uniform all-h asymptotic: b=o(V), not merely b=o(s)

Let \(b_s=o(V_s)\), \(V_s=(s+1)(s^2+1)\asymp s^3\), and let \(\rho_s=b_s/V_s\to0\). Select for sufficiently large \(s\)
\[
 k_s=\left\lceil d\sqrt{\rho_s}+\sqrt d\right\rceil
 \quad\text{with } d=s+1,
\]
so \(k_s=o(d)\) and \(k_s\le d-6\). For \(\rho_s=0\), \(k_s=0\) also suffices. By (1),
\[
 \frac{V-G_{k_s}}V\le
 \frac{\rho_s d}{k_s+1}\le\sqrt{\rho_s}\to0,
\qquad q_{k_s}=d-o(d).
\]
Moreover \(M-V=O(a)=o(V)\), so
\[
 Q_{k_s}\sim\frac{a^4}{8},
 \quad T_{k_s}\sim\frac{d^6}{2},
 \quad P_{a,b_s}\sim\frac{4480}{a^6},
 \quad V\sim\frac{a^2}{2}.
\]
These approximations are **uniform in every legal fixed f, every true source line set J, every frozen legal right assignment g_J**: only \(s\) and \(b_s\) occur in the certified lower expression. Consequently the displayed lower bound is
\[
 \boxed{
  \liminf_{h\to\infty}
  \inf_{\substack{\text{complete legal }f,\;
                   J,\;g_J\\ |J|=b_s}}
  \frac{\mathbb E_{g\mid g_J}
      U_{B\text{-left}/A\text{-right}}(f,g)}{s^6}
  \ge140
  \qquad\text{for every }b_s=o(V_s).
 }\tag{MACRO140}
\]
In particular this applies when \(b_s=s^2\), enormously beyond predecessor's \(b_s=o(s)\) regime. It is **not** a statement about a completed adversarial \(g\).

## 5. Positive density frozen: b≈rho V with rho<1/6

Fix \(0<\rho<1/6\) and let \(b_s=\lfloor\rho V_s\rfloor\). Choose a constant \(4\rho<\alpha<1\), and set \(k_s=\lfloor\alpha(s+1)\rfloor\). Then
\[
 G_{k_s}\ge (1-\rho/\alpha-o(1))V,\qquad
 Q_{k_s}\ge (1-4\rho/\alpha-o(1))\,\frac{a^4}{8},
\]
\[
 T_{k_s}\ge ((1-\alpha)^6-o(1))\,\frac{s^6}{2},
 \quad
 P_{a,b_s}\ge \left(\frac{1-6\rho}{(1-\rho)^6}
              -o(1)\right)\frac{4480}{a^6}.
\]
Here the physical right denominator \((M-b)_6\) accounts **correctly for without-replacement assignments from a fractionally depleted palette**, hence the explicit \((1-\rho)^{-6}\) term. The union bounds are conservative and become strict only asymptotically. Therefore
\[
\boxed{
 \liminf_{h\to\infty}
 \inf_{f,J,g_J:\ |J|=\lfloor\rho V_s\rfloor}
 \frac{\mathbb E_{g\mid g_J}U_{B/A}(f,g)}{s^6}
 \ge c_{\rho,\alpha}
 :=140\frac{
  (1-\rho/\alpha)(1-4\rho/\alpha)(1-\alpha)^6(1-6\rho)
 }{(1-\rho)^6}>0
 }\tag{MACRO-RHO}
\]
for **every** \(0<\rho<1/6\), by the explicit admissible \(\alpha=(1+4\rho)/2\). In particular for \(\rho=1/16\), \(\alpha=1/2\),
\[
c_{1/16,1/2}
=\frac{1225}{2048}\left(\frac{16}{15}\right)^6
>\frac{1225}{2048}>0.
\]
This is a genuine positive-density *conditional first-moment robustness* result over ANY original frozen source line factors and their legal assignments, not a pointwise all-g statement. The critical \(\rho<1/6\) here comes only from a coarse union bound on right physical 2-factors, not a demonstrated sharp threshold.

## 6. Implemented independent evidence and STOP

- \`research/hyp105_allh_macro_freeze_BA.py\`: exact integer/Fraction formula, optimize over all integer original-pencil thresholds \(0\le k\le d-6\), fail-closed typed injections and freeze counts, and explicit macroscopic freeze examples. Baseline \(b=0,k=0\) algebraically equals the independent #669 formula.
- \`research/test_hyp105_allh_macro_freeze_BA.py\`: genuine original symplectic W32/W34 source-pencil first-moment and Markov bad-point verification for every k; independently enumerated actual physical four-cycles on GOOD f source-factor labels in a separate degree-regular combinatorial test host; explicit six different original line factors; dyadic exact formula tests including \(b_s=s^2\) and \(b_s=\lfloor V/16\rfloor\); model validation errors. **The synthetic regular host is explicitly only a finite algebraic falsifier, not claimed to be W(3,8) or a new source theorem.** For the real model the source input is always the genuine \(W(3,2^h)\).
- \`.github/workflows/hyp105-allh-macro-freeze-BA.yml\`: GitHub-hosted Python 3.12 exact-head checks, independent of user's local PC.
- Exact full Research and INDEX CI required before scientific acceptance. Draft stays open pending independent mathematical proof referee.

**Formal limitation:** \(\mathbb E_{g\mid g_J} U_{B/A}\ge c s^6\) even after freezing \(c'V\) original right labels does NOT give \(\inf_{f,g} S_s(f,g)=\Omega(s^6)\). An adversary can still choose a completed \(g\) in a rare lower tail. No Branch A/B/C, no exact \(R_3\), no ASET exponent. This partial theorem rules out explaining the lack of fixed-map positivity solely through *macroscopically many but not too dense* frozen right source labels: a uniform injection on the rest still has order-\(s^6\) accepted B/A in expectation. Next high-value target: control the conditional **lower tail of the B/A count** under such macroscopic freezes, or demonstrate genuine all-map seven-class compensation for atypical completed maps. Beware earlier #487 overlap-signature results: joint right-cycle probabilities can depend on the shared original line positions, not only their overlap cardinality.
