# HYP-105 #230 — AA4-ANNBA: a uniform all-h ANNEALED \(\Omega(s^6)\) original GF(5) B/A floor

**Status:** rigorous all-\(h\) *conditional first-moment theorem*, **NOT** root Branch A/B/C, **NOT** exact full \(R_3\), and **NOT** a lower bound valid for every completed correlated \(g\). All original incidence IDs, typed pair maps, true source pencils and 51 full GF(5) four-nonzero checksum palette remain as in #230. Neither a new ASET exponent nor a bound on total signed events follows.

## Theorem (uniform in every adversarial f and frozen source assignment)

Let \(s=2^h,\ h\ge1\), \(V=(s+1)(s^2+1)\), \(d=s+1\), \(a=\min\{t:\binom t2\ge V\}\), \(M=\binom a2\), and \(m=M-V<a-1\). Let \(f:P(W(3,s))\to E(K_a)\) be **any globally injective complete** typed point-label map. Choose **any** \(b\) different ORIGINAL source-line factors \(J\subseteq L(W(3,s))\) and prescribe **any** distinct physical pair labels \(g_J:J\to E(K_a)\). Give all other \(V-b\) ORIGINAL source lines a uniformly random injection into the remaining \(M-b\) physical pair labels, WITHOUT replacement. This defines one fully legal completed source-line map \(g\); the point labels, frozen line labels and true source incidence tensor are fixed, not random.

Set \((x)_6=x(x-1)\cdots(x-5)\), and, with a value of zero when \(d-b<6\), define
\[
\begin{aligned}
 Q_4(a,m)&=\big[3\binom{a-2}{4}-2m\binom{a-4}{2}\big]_+,\\
 T_6(d,b)&=\binom{d-b}{2}(d-b-2)(d-b-3)(d-b-4)(d-b-5),\\
 A_6(a,b)&=\big[70\binom a6-28b\binom{a-2}{4}\big]_+,\\
 p_A(a,b)&=\frac{6!\,A_6(a,b)}{(M-b)_6}.
\end{aligned}
\]
The \(p_A\) fraction is set to zero if fewer than six available physical pairs remain; the overall lower bound is zero if fewer than six eligible source flags can be selected. The bracket \([z]_+\) denotes \(\max(0,z)\).

Then **for every \(s\), every such fixed \(f\), every frozen source set \(J\), and every frozen physical assignment \(g_J\)**,
\[
\boxed{\quad
 \mathbb E_{g\mid g_J}\,
 U_{B{\rm-left}/A{\rm-right}}(f,g)
 \ \ge\ V\;Q_4(a,m)\;T_6(d,b)\;p_A(a,b).
 \quad} \tag{ANNBA}
\]
The count is of **SIX DISTINCT ORIGINAL incidence IDs**, ONCE per sixset, and the tag is the historically accepted **strictly positive GF(5) B-left/A-right** class, not an auxiliary unphysical motif.

For any sequence \(b_s=o(s)\) of nonnegative frozen ORIGINAL line-factor counts, the exact displayed lower bound has
\[
 V Q_4 T_6 p_A = (140-o(1))s^6,
 \qquad s=2^h\longrightarrow\infty.
 \tag{ANN140}
\]
Consequently
\[
\liminf_{h\to\infty}
 \inf_{f,J,g_J\colon\,|J|=b_s}
 \frac{\mathbb E_{g\mid g_J}U_{B{\rm-left}/A{\rm-right}}(f,g)}
      {s^6}\ge140 .
\]
The infimum is over ACTUAL legal fully injective \(f\), choices of true source-line factors \(J\), and actual legal frozen right pair labels. This uniform statement is a conditional **annealed** theorem; the infimum over arbitrary *completed* \(g\) has NOT been interchanged with expectation. The deterministic probabilistic-method consequence is only: for each \(f,J,g_J\), **at least one** legal completion \(g\) has \(U_{B/A}\) at least the stated expectation floor. It is not a same-map adversarial all-\(g\) lower bound.

## Proof I: lower count of ORIGINAL left B-source configurations

Fix an ORIGINAL point \(p\in P(W(3,s))\). Its image \(f(p)\) is one physical edge \(\{u,v\}\). On the other \(a-2\) physical symbols, there are exactly \(3\binom{a-2}{4}\) simple labelled four-cycles: choose four vertices and remove one of the three perfect matchings from their complete six-edge graph. At most \(m\) pair edges in ALL of \(K_a\) are missing from the image of \(f\). Each missing edge on the \(a-2\) allowed coordinates belongs to exactly \(2\binom{a-4}{2}\) candidate four-cycles (the fixed edge is present in two of the three possible C4s on each choice of two further vertices). By the union bound, there remain at least \(Q_4(a,m)\) physical C4s whose FOUR pair edges are all occupied by \(f\).

A surviving C4 determines FOUR distinct ORIGINAL point factor IDs \(p_1,p_2,p_3,p_4\) by global injectivity of \(f\); these are different from \(p\), since the C4 vertices are disjoint from the endpoint symbols of \(f(p)\). The source consists of the genuine \(d\)-regular \(W(3,s)\) incidence tensor. Every original point \(p_i\) has exactly \(d=s+1\) different incident ORIGINAL line-factor IDs, and therefore exactly \(d\) different ORIGINAL incidence flag IDs. The frozen source set \(J\) contains \(b\) ORIGINAL lines, so at least \(d-b\) incident lines at **every** point lie outside \(J\).

First choose TWO different such line factors \(\ell_0,\ell_1\notin J\) incident with repeated \(p\), in \(\binom{d-b}{2}\) or more ways. Next, choose one \(\ell_i\notin J\) at each of the C4-owned points \(p_1,\dots,p_4\), requiring all six chosen original lines to be DISTINCT. At the \(i\)-th singleton point, at most \(i+1\) lines have already been selected (two at \(p\), then one at each previous singleton); therefore there are at least
\[
 (d-b-2)(d-b-3)(d-b-4)(d-b-5)
\]
choices in sequence. Source-line incidence coincidences across the distinct point pencils can only reduce the number of *forbidden* choices, never invalidate this worst-case lower bound. There is no assumed independence of source incidence flags or Sp(4,s) symmetry of the arbitrary \(f\).

Every resulting selection consists of SIX distinct original flags,
\[
 (p,\ell_0),(p,\ell_1),(p_1,\ell_2),
 (p_2,\ell_3),(p_3,\ell_4),(p_4,\ell_5).
\]
The ORIGINAL left source-factor multiplicities are exactly \(B=(2,1,1,1,1)\), and the physical left projection is **one doubled pair edge plus one disjoint C4**, therefore degree two on SIX distinct physical coordinates. Conversely its unique repeated factor \(p\) and the unique disjoint physical C4 recover this construction. Different choice orders do not overcount: the four C4 factor IDs are assigned to their unique physical pair edges and traversed in one canonical order. Distinct choices of genuine source-line IDs yield distinct original flag ID sets. Thus there are at least \(V Q_4(a,m) T_6(d,b)\) different genuine left B original sixsets whose SIX distinct line factors all lie outside \(J\).

**No source girth or GQ spectrum is used** in this construction beyond genuine simple regular pencils; the source must still be the true \(W(3,s)\) for the theorem to be within root #230's model.

## Proof II: uniform injection into ORIGINAL right A on six labels

For the SIX distinct selected source lines outside \(J\), the uniform completion maps them into a uniform ordered six-tuple of DIFFERENT physical pair edges drawn from \(E(K_a)\setminus g_J(J)\). Every one of the \((M-b)_6\) ordered tuples has the **same** probability; correlations of assignments to remaining unselected source lines do not alter this marginal.

The count of all six-edge simple 2-regular labelled physical graphs on six coordinate vertices is exactly \(70\): sixty connected C6 and ten disjoint two-triangle configurations. The unrestricted physical pair alphabet \(K_a\) therefore has \(70\binom a6\) possible six-edge 2-factor subsets. An arbitrary single forbidden physical edge belongs to exactly \(28\binom{a-2}{4}\) of them: on any selected six vertices containing its endpoints, count its incidence across the 70 K6 2-factors by edge-transitivity, \(70\times6/\binom62=28\). By the union bound over \(b\) already-occupied frozen pair edges, at least \(A_6(a,b)\) acceptable right-side six-edge sets survive. Every surviving set has \(6!\) ordered assignments to the named SIX original source-line IDs.

Thus, without replacement and without treating f and g as independently random,
\[
  \Pr(\text{right type A physical degree-two}\mid f,g_J;
       \ell_0,\ldots,\ell_5)
  \ge p_A(a,b).
\]
For **every** such event, the original right source-factor partition is A, left is B, and both physical projections have exactly six degree-two coordinates: the historical original GF(5) classifier returns **B-left/A-right**, accepted with strictly positive full-palette weight. The conditional expectation of a sum of sixset indicators equals the sum of their conditional probabilities; linearity needs no independence between different sixsets. This proves (ANNBA).

## Proof III: asymptotic leading coefficient exactly 140

Since \(V=(s+1)(s^2+1)\sim s^3\) and \(M=\binom a2\) is the first available pair alphabet covering \(V\), one has \(a^2\sim2V\), \(a\sim\sqrt2\,s^{3/2}\), and \(m=M-V<a-1=O(a)\). Consequently
\[
 Q_4(a,m)\sim 3a^4/24=a^4/8.
\]
For \(b_s=o(s)\),
\[
 T_6(d,b_s)\sim\frac12 s^6.
\]
Also \(b_s=o(s)=o(a^2)\), so \(A_6(a,b_s)\sim70a^6/720\) and \((M-b_s)_6\sim(a^2/2)^6=a^{12}/64\). Thus
\[
 p_A(a,b_s)\sim4480/a^6.
\]
Multiply:
\[
 V\cdot\frac{a^4}{8}\cdot\frac{s^6}{2}
   \cdot\frac{4480}{a^6}
 =\frac{280V}{a^2}\,s^6
 =(140+o(1))s^6.
\]
All constants and quantifiers are uniform in the *actual* arbitrary fixed f and actual frozen legal g_J; the asymptotic uses only \(s\), \(a\), and \(b_s\).

In particular, since the accepted necessary third-risk floor charges **45600** per ORIGINAL B-left/A-right sixset,
\[
 \mathbb E_{g\mid g_J}\big[51^6 R_3(f,g)\big]
 \ \ge\ 45600 \, VQ_4T_6p_A,
\]
provided the previously accepted pointwise necessary full-51-palette GF(5) weight applies to each sixset and \(R_3\) is the full positive risk as in the root. This is **an annealed lower estimate** only; it cannot be used to exclude any deterministic correlated family with \(R_3\) small.

## Reproducible independent falsifiers and exact finite control

Implemented by \`research/hyp105_allh_annealed_BA_floor.py\` with pure exact integers and \`fractions.Fraction\`: no Monte Carlo, no float fit, no diagonal projection or synthetic sixsets. The independent \`research/test_hyp105_allh_annealed_BA_floor.py\` performs:

1. Independent full K6 AND K7 2-factor enumeration from six pair-edge combinations; exactly \(70\binom a6\) physical 2factors and exactly \(28\binom{a-2}{4}\) containing each physical edge.
2. Adversarial missing-edge occupancies of K8 compared against the conservative C4 destruction union bound.
3. Actual original \(W(3,2)\) lex and reverse-line controls: separately enumerate all historical 10,935 left B sixset candidates by immutable ORIGINAL flag IDs, restrict to distinct ORIGINAL right source line factors, and compute the **EXACT** uniform-injection probability by an independent physical 2-factor oracle. Repeat with one actual frozen source line and forbidden physical pair.
4. All-h closed-form arithmetic at dyadic \(s=2,4,8,\ldots,1024\), no numerical fit. Nonfrozen explicit positive floor at \(s\ge8\); for 12 frozen genuine source-line factors, positive guaranteed bound from \(s\ge32\), because the line-avoidance construction requires \(d-b\ge6\).
5. Fail-closed malformed source pair labels, illegal freeze counts and dyadic powers.

Dedicated GitHub-hosted workflow \`.github/workflows/hyp105-allh-annealed-BA.yml\` re-runs the independent scientific oracle on exact PR head. The full Research pipeline also exercises these tests without source geometry beyond W32.

### Scope and original no-go resolution

This is **not** Branch A: \(\inf_{f,g} S_s(f,g)\) could still be \(o(s^6)\) for cleverly correlated **completed** \(g\), even though \(\mathbb E_{g\mid g_J}S_s(f,g)\ge(140-o(1))s^6\) for every fixed \(f\) and bounded frozen \(J\). It is **not** Branch B: no such infinite negative family is constructed. It is **not** model-equivalent Branch C: the theorem proves a first moment, not a restricted iff reduction of the adversarial infimum. The result does prove that a strategy searching for complete low-S maps must exploit atypical/global assignment correlations; mere source sparsity, or a large collection of unused line pair labels, cannot suppress the unconditional uniform-completion first moment.

**Next proof gate:** develop an **adversarial lower bound** comparing a fixed completed map's B/A count to its own other six classes, or an exact deterministic discrepancy/variance certificate controlling the lower tail of the B/A sum across global injective completions. First-moment positivity alone does not supply such a comparison.

**Provenance:** [root issue #230](https://github.com/definitely-stable/Mathlab/issues/230), [#666 conditional D6 extensions](https://github.com/definitely-stable/Mathlab/pull/666), [#668 exhaustive seven-class W34 comparison](https://github.com/definitely-stable/Mathlab/pull/668); the present Draft is stacked on #668 and does not alter parent results.
