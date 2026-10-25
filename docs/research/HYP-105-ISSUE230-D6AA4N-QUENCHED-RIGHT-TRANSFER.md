# HYP-105 / issue #230 — D6-AA4-N: uniform quenched-right ORIGINAL GF(5) B/A transfer

**New mathematical result: a genuine ALL-h \(s=2^h\ge8\) guarantee of order \(\Omega(s^6)\) for the EXPECTED internal source-line GF(5) charge after holding an ARBITRARY globally injected right labeling \(g\) fixed and averaging over one uniform complete global left labeling \(f\). Quantifiers: \(\min_g\max_f\), NOT \(\min_{f,g}\).**

Strict Draft research stack on fully green [AA4-M PR #468](https://github.com/definitely-stable/Mathlab/pull/468), pinned parent SHA \`3b7aee7a8764f4ebc4abee073a592aaaa45bca74\`. The root HYP-105 Branch A/B remains OPEN. This is not a universal all-\(f,g\) seven-GF5 motif lower, ASET exponent, full R3 or infinite counterfamily. Do not modify main or merge.

## 1. The precise conditional identity: freeze the entire original-line map

For arbitrary real ORIGINAL symplectic \(W(3,s)\), let \(V=(s+1)(s^2+1)\), \(d=s+1\), and \(a\) minimal with \(K=\binom a2\ge V\). Let \(g\) be **any fixed complete globally injective mapping** from all \(V\) original lines to physical unordered coordinate pairs in \(K_a\). Let \(f\) be chosen uniformly among all complete globally injective original POINT mappings, independent of \(g\). Both physical maps are shared across ALL original incidence sets \(Q\): no artificial independent map per Q.

Write \(\mathcal B_A\) for the set of SIX DIFFERENT true original incidence IDs with exactly one point occurring twice and four other points each once (point type B), and six distinct original line factors (line type A). Given the fixed \(g\), define \(T_g\) as the number of these TRUE original \(\mathcal B_A\) sets whose six \(g\)-assigned original line physical edges form an A-type two-regular simple six-edge graph on exactly six physical coordinates **and** whose two original lines incident with the repeated original point have DISJOINT physical labels. \(T_g\) is a nonnegative integer determined *solely by the original geometry and the ONE fixed map \(g\)*.

By AA4-M's exact complete-injection marginal, for each of these true ORIGINAL Q, the probability its FIVE distinct point-factor physical labels form the correct B-type half is

\[
p_B(s)=\frac{K\binom{a-2}4\,3\,4!}{(K)_5}.
\]

The full original seven-GF5 positional classifier accepts every simultaneous B-left/A-right Q, without any extra physical-P3 constraint. Since the source line A condition and actual internal original line-pair disjointness are already fixed by \(g\), linearity of expectation gives the **EXACT all-h identity for EVERY fixed \(g\)**:

\[
\boxed{\mathbb E_f[I_L^{BA,\mathrm{int}}(f,g)\mid g]=p_B(s)\,T_g.}
\]

This is a ONE-SIDED conditional average, not even the AA4-M simultaneous mean over \((f,g)\). It can fail to give a positive lower for an INDIVIDUAL \(f\). We now prove \(T_g\) is large for EVERY fixed \(g\) when \(s=2^h\ge8\).

## 2. First all-h ORIGINAL source/physical input — spectrally forced pairs

AA4-I independently proved that EVERY actual globally injected original-line map has at least

\[
D_L(g)\ge D_s:=
\frac{V(s^2-s+2)}2-(s^2+1)(a-1)
\]

pairs of original concurrent lines whose two assigned physical edges are DISJOINT. For \(s\ge4\), \(D_s\ge s^5/4\).

Let \(m=K-V\) be the number of MISSING physical edges in the (otherwise complete) right physical-image graph. Minimality of the alphabet gives the crucial **exact** \(0\le m\le a-2\), not an arbitrary sparse graph.

Choose an integer \(t=\lfloor(a-6)/8\rfloor\). Call a physical coordinate *bad* if its degree in the missing-edge graph is greater than \(t\). The sum of missing degrees equals \(2m\), so at most

\[
B=\left\lfloor\frac{2m}{t+1}\right\rfloor
\]

physical coordinates are bad. At most \(B(a-1)\) source original line factors have a physical edge label containing a bad coordinate. The genuine original line concurrence graph is \(k=s(s+1)\)-regular. Thus no more than \(B(a-1)k\) original concurrent line pairs are incident to one of these potentially bad source factors. Consequently at least

\[
R_s:=\max\{0,D_s-B(a-1)k\}
\]

original concurrent physically-disjoint line pairs have ALL FOUR physical endpoints good, for EVERY \(g\). This uses the TRUE original line concurrence graph and TRUE globally injected source line labels: it is neither a pseudo-image fractional bound nor a mere random-model statement.

## 3. Construct complete physical six-cycles for EVERY retained source pair

Take one retained original concurrent line pair \(\ell_0,\ell_1\) meeting at the TRUE original point \(p\). Their disjoint physical edges under the fixed right injection are \((u_0,u_1)\) and \((v_0,v_1)\), with four distinct physical endpoints, all good. Fix canonical source-ID and ordered physical-endpoint orientations.

Choose a new coordinate \(x\) outside these four endpoints such that the physical edges \((u_1,x)\) and \((x,v_0)\) both occur in the actual occupied image of \(g\). Since both \(u_1\) and \(v_0\) have at most \(t\) missing incident edges, at least \(z=a-4-2t\) choices of \(x\) exist. Similarly choose \(y\) such that \((v_1,y)\) and \((y,u_0)\) are occupied; at least \(z\) candidates. Requiring \(x\ne y\) leaves at least \(z(z-1)\) ordered pairs \((x,y)\).

The **SIX genuine occupied physical edges** \((u_0,u_1),(u_1,x),(x,v_0),(v_0,v_1),(v_1,y),(y,u_0)\) form a simple \(C_6\). Because all six belong to ONE right physical image under the SAME globally injected \(g\), they correspond to six different TRUE original line factors, including \(\ell_0,\ell_1\). No physical-coordinate or source factor can be chosen independently for different \(Q\) in this construction.

For each of the other four original line factors \(\ell'_j\), choose a TRUE original point \(q_j\) on that line, different from the root point \(p\) and different from previous \(q_i\). Each original line contains \(s+1\) points, so there are at least \(s-j\) possibilities at step \(j=0,1,2,3\). Thus each chosen physical cycle yields at least

\[
(s)_4=s(s-1)(s-2)(s-3)
\]

genuine six-incidence ORIGINAL Q with exactly the B(point)/A(line) source pattern and guaranteed right physical A condition. The true root point is unique (the point appearing twice), its original two-line pair is unique, and fixing the canonical oriented original root edges makes the added \(x,y\) unique from the right physical six-edge image. Thus **there is no overcount across roots or ordered connector choices**.

We obtain the all-h REAL-GQ and REAL-PHYSICAL image theorem

\[
\boxed{T_g\ge R_s\, z(z-1)(s)_4}
\]

whenever \(z\ge2\), and hence the exact conditional lower

\[
\boxed{\mathbb E_f I_L^{BA,\mathrm{int}}(f,g)\ge p_B(s)R_s z(z-1)(s)_4.}
\]

It holds for EVERY complete right injection \(g\), with only one random complete left injection \(f\).

## 4. A uniform **explicit** \(s^6\) constant for every fixed \(g\)

For \(s=2^h\ge256\), the following are simultaneous elementary consequences of the genuine alphabet model and the AA4-I spectral source-pair theorem:

- \(a\ge14\), \(a\le s^2\), \(0\le m\le a-2\), \(t+1>(a-6)/8\), hence \(B\le24\).
- \(D_s\ge s^5/4\) and \(B(a-1)k\le24s^2\cdot2s^2=48s^4\). Since \(s\ge256\), \(R_s\ge s^5/16\).
- \(z=a-4-2t\ge a/2\), \(z-1\ge a/4\); \(a^2\ge2V\ge2s^3\). Thus \(z(z-1)\ge s^3/4\).
- For \(s\ge8\), \((s)_4\ge s^4/16\).
- Minimal \(K\le2V\le4s^3\). Also for \(a\ge14\), \(\binom{a-2}4\ge a^4/384\), \(a^2\ge2K\), and \((K)_5\le K^5\). Therefore \(p_B\ge 3/(64s^6)\).

Their product yields the explicit all-right inequality

\[
\boxed{\forall\,s=2^h\ge256,\ \forall\,g\text{ complete},\
\mathbb E_f I_L^{BA,\mathrm{int}}(f,g)\ge\frac{3}{65536}s^6.}
\]

For the only remaining powers \(8,16,32,64,128\), the same **exact integer** formula \(R_s z(z-1)(s)_4\) with the exact rational \(p_B\) is directly evaluated and verified \(\ge3s^6/65536\). The finite rows are independently pinned in unit tests:

| \(s\) | \(a\) | \(m\) | \(D_s\) | \(R_s\) lower | \(z\) |
|---:|---:|---:|---:|---:|---:|
| 8 | 35 | 10 | 14,755 | 2,515 | 25 |
| 16 | 94 | 2 | 504,748 | 504,748 | 68 |
| 32 | 261 | 105 | 16,544,525 | 14,897,165 | 195 |
| 64 | 731 | 510 | 534,146,375 | 500,741,575 | 547 |
| 128 | 2,057 | 931 | 17,148,295,225 | 16,910,654,521 | 1,541 |

**NEW rigorous all-h theorem (s>=8):**

\[
\boxed{\forall g\,\ \mathbb E_{f\ \mathrm{uniform\ complete}}
I_L^{BA,\mathrm{int}}(f,g)\ \ge\ \frac{3}{65536}s^6.}
\]

In particular, for EACH adversarial fixed \(g\) there exists SOME complete globally injected \(f\) with real true seven-GF5 internal B/A line charge of order \(s^6\). This proves \(\min_g\max_f I_L^{BA,\mathrm{int}}\ge(3/65536)s^6\).

**CRITICAL logic boundary:** This DOES **NOT** prove \(\min_{f,g}I_L^{BA,\mathrm{int}}\ge cs^6\) or the root seven-GF5 HYP-105 universal \(\min_{f,g}S_s\ge cs^6\). The adversary in Branch A chooses BOTH maps together and can choose a nonuniform particularly bad \(f\) after the same \(g\). A positive conditional mean still permits exceptional low-charge \(f\). Do not reverse the \(\min/\max\) quantifiers, do not assert a universal all-label GF5 R3/ASET improvement.

## 5. Real W32 original incidence and physical image independent gate

On the TRUE 45-incidence W(3,2) host, all 15 original point-pencil roots and their 3 pairs of genuine original lines are enumerated. For any globally injected complete ORIGINAL right map \(g\) (K6 uses ALL 15 physical edges), independently enumerate all 70 unlabeled physical degree-two six-edge A-subgraphs on K6. Every selected six-source-line right A pattern with one true two-line root pencil has exactly four additional real original lines. Enumerate all assignments of four other genuine original point-line incidences to those four lines, with four new DISTINCT original points different from the repeated root point. This counts exactly, without physical point labels:

- \(N_A(g)\): original point-B/line-A Q with fixed right A.
- \(T_g\): the subset additionally having the two ROOT original concurrent lines physically DISJOINT.

For each fixed \(g\), independently check the exact conditional identities

\[
\mathbb E_f S_{B/A}(f,g)=p_B N_A(g),\qquad
\mathbb E_f I_L^{BA,\mathrm{int}}(f,g)=p_B T_g.
\]

Test true W32 fixed right fixtures lex/reverse/S68/S72 plus multiple independently shuffled complete right-label bijections, using the ONE fixed \(g\) for every original Q. These are genuine exact finite fixed-right conditional expectations, NOT sample means of the earlier 24 frozen-outside point permutations. For s=2 this slice does not make an all-g uniform bound: the analytic missing-image/spectral threshold only proves it for s>=8.

## 6. Research implication: where exactly the remaining obstruction lies

AA4-M obtained an averaged both-maps GF5 internal B/A source charge \((84+o(1))s^6\) (and high-charge existence for some globally injected pair f,g). AA4-N is **substantially stronger in QUANTIFIER STRUCTURE**: each arbitrary choice of the entire right/source-line physical image g still permits a globally injected point-map response f having large true internal GF5 charge. Neither proof requires independent per-Q physical maps or a path-only/P3 proxy. EICE-003-I/PR #465 and local-transfer PR #466 remain separate valid warnings about local matching sources and blocked source squares.

The precise open problem is now the **adversarial left-map suppression**: can a complete globally injected f drive B/A internal charge below \(cs^6\) for a fixed g, despite a positive uniform-complete-f conditional expectation and every required true source-physical right cycle? This calls for higher-order original source-to-physical transport, point factor interactions and an adversarial lower bound, not another expectation over random point labels. Positive concentration around the mean would still need to rule out *every* exceptional f to establish Branch A.

Four new files in separate child Draft, GitHub-hosted all-h/five small exact rows and independent genuine W32 right-fixed oracle, INDEX, Proof Audit, Full Research must all succeed on final SHA before technical acceptance. Independent mathematical peer review remains OPEN. No main changes/merge/root issue closure.
