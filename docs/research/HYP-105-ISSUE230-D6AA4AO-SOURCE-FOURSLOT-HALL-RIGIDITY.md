# HYP-105 #230 — AA4-AO: genuine original four-slot Hall rigidity and a sharp D-port source multiplier

**Research-only Draft, no Branch A/B/C resolution.** Strict child of [AA4-AN physical-port original Hall funnel PR #533](https://github.com/definitely-stable/Mathlab/pull/533), pinned parent HEAD \`a53db527acbc0a3c5f8ee65e7d326361ba31e2a9\`. Genuine original source W(3,s), s=2^h≥2, two independent complete but globally injected typed physical source-pair maps f,g, fixed unmodified for every source flag, source-D anchor and six-ID Q. Missing physical K_a pairs remain missing. **All formulas refer to genuine six DISTINCT original incidence flag IDs and to the SAME Q on both types.**

## 1. Prior-art boundary and the actual new mathematical step

Parent [#533](https://github.com/definitely-stable/Mathlab/pull/533) has already proved the complete **three residual physical 4-edge templates** for any genuinely bilateral D two-flag anchor, 10·C(a−3,3) per typed physical side, and already built an all-h exact original 4-slot source-Hall *up-to-24-permutations* matcher for physically occupied point/line residual templates. It also already classified the unique GF5 failure among bilateral physically 2-regular D-anchored Q: unaligned/non-D6 A/A. Parallel [#534](https://github.com/definitely-stable/Mathlab/pull/534) implements an independent original D-first one-side and then opposite-type check, with the same J=E+R exact identity. Neither result is relabeled new here.

[AA4-AE #512](https://github.com/definitely-stable/Mathlab/pull/512) **already** proved for FOUR DISTINCT original point factors and FOUR DISTINCT original line factors in a genuine original symplectic GQ W(3,s) that their 4×4 incidence permanent is **at most TWO**, with equality precisely for an induced original incidence C8. This is not a new theorem in this slice.

**NEW AA4-AO1:** extend the old true-original four-distinct-factor permanent theorem to the PHYSICALLY IMPORTANT residual 4-source-slot multiplicity profiles involving a repeated original source factor: for two occupied physical port templates, if at least one typed side uses a physical C4 plus a repeated 2-cycle, the number of DIFFERENT genuine original **four-incidence-flag** completions of their source-factor multisets is **at most ONE**. This holds ALL dyadic orders and EVERY global map, not merely observed finite W32. The key is an alternating-cycle argument on two candidate true original *sets of four different incidence edges* with the SAME source-factor degree profiles.

**NEW AA4-AO2:** combine the new strict source rigidity with parent #533 exact physically occupied port templates. For any genuine D anchor and fixed maps, if the two point/line template counts are \(A_P,B_P,A_L,B_L\), with A the 7·C(a−3,3) simple-source modes in FULL K_a and B the 3·C(a−3,3) repeated-source modes, then the exact original D-anchored joint 2-regular Hall charge \(H_D\) satisfies

\[
\boxed{0\le H_D\le 2 A_P A_L+A_PB_L+B_PA_L+B_PB_L}.
\]

This is an unconditional all-h/all-map **source-Hall UPPER**, not a lower. In full K_a, writing \(t=\binom{a-3}{3}\), it yields \(H_D\le149 t^2\), a factor \(2400/149>16\) reduction from the parent's former brute 24·100·t² per-template enumeration upper. No claim of tightness for actual full original maps simultaneously saturating all slots, and no \(E_D>0\) proof.

## 2. Exact original four-slot source matching definition and multiplicity group quotient

Fix ONE genuine original D-compatible two-flag pair \((p_0,\ell_0),(p_1,\ell_1)\) from true W(3,s). After choosing **ONE occupied point physical port completion** and **ONE occupied line physical port completion** from #533, invert their physical residual edge labels through the SAME globally injected point and line maps. This produces four actual original point-source factor slots \(P=(P_1,\dots,P_4)\) and four original line-source slots \(L=(L_1,\dots,L_4)\). Each slot multiset has EXACTLY one of two profiles:

- **A**: four DISTINCT original source factors, multiplicity partition \((1,1,1,1)\), arising from residual C6 or 2C3 physical topology.
- **B**: three DISTINCT original source factors, one appearing TWICE, partition \((2,1,1)\), arising from residual C4 plus physically doubled C2.

A valid original four-flag completion is an UNORDERED set \(R\) of FOUR DIFFERENT true original point-line incidence flag IDs with point-factor and line-factor multiplicity multisets exactly \(P,L\), respectively. Their union with the fixed two genuine D incidence IDs has SIX DISTINCT original source flag IDs; the physical port disjointness prevents reusing either anchored source factor on its typed side.

Let \(I\subseteq P_\mathrm{original}\times L_\mathrm{original}\) be the ORIGINAL symplectic incidence relation, and \(\mathsf{valid}(\pi)\) indicate that the four pairs \((P_i,L_{\pi(i)})\) for a permutation \(\pi\in S_4\) each belong to I and are **FOUR DISTINCT actual ORIGINAL incidence IDs**, disjoint from the two anchored original flag IDs. This extra distinctness is ESSENTIAL: a repeated original source point and a repeated original source line might otherwise contribute the SAME original incidence ID twice, illegally making a six-multiset rather than six DIFFERENT original incidence IDs.

The point slot-stabilizer has order \(\prod_p \mathrm{mult}_P(p)!\in\{1,2\}\); the line slot-stabilizer has order \(\prod_\ell \mathrm{mult}_L(\ell)!\in\{1,2\}\). For valid distinct-flag assignments the combined slot relabeling group acts FREELY on labeled permutations, hence EVERY different unordered original four-flag set is generated exactly

\[
g(P,L)=\left(\prod_p \mathrm{mult}_P(p)!\right)
       \left(\prod_\ell \mathrm{mult}_L(\ell)!\right)
\in\{1,2,4\}
\]

times. In particular the mathematically exact globally shared SOURCE 4-slot Hall count is

\[
\boxed{
N_{\mathrm{orig}}(P,L)=
\frac1{g(P,L)}
\sum_{\pi\in S_4}\mathbf1_{\mathsf{valid}(\pi)}.
}
\]

This normalization is **NOT** valid if duplicate original source incidence flags were retained; the implementation explicitly forbids them, asserts integrality, and independently matches the quotient against a **second, EDGE-FIRST** enumeration of all four-source-incidence subsets matching the required original point/line source multiplicity counts.

## 3. NEW all-h repeated-source matching rigidity theorem via true original GQ girth eight

**Theorem:** For ANY two four-source-slot multisets P,L with profiles A or B, any REAL original symplectic W(3,s) incidence graph of girth EIGHT, and any complete globally injected typed f,g:

\[
\boxed{
N_{\mathrm{orig}}(P,L)\le
\begin{cases}
2,&(P,L)\text{ have source multiplicity profiles A/A},\\
1,&\text{at least one profile is B}.
\end{cases}
}
\]

The A/A theorem, including C8 equality, is **preexisting PR #512**. The new implication is the B/A, A/B and B/B bound ONE.

**Proof of new part (no probabilistic assumptions).** Suppose two DIFFERENT sets \(R_0,R_1\) of exactly FOUR true original incidence edges have the SAME required multiplicities of every real original point-source factor and of every real original line-source factor (determined by the two fixed global physical inverse-image four-slot multisets P,L). Color edges in \(R_0\setminus R_1\) red and in \(R_1\setminus R_0\) blue. At each actual original point or line source vertex, the number of red and blue edges is EQUAL, because both four-edge sets have exactly identical endpoint multiplicity counts. Thus the red/blue edge union is an alternating Eulerian bipartite subgraph, and if nonempty contains an alternating SIMPLE cycle in the TRUE original source incidence graph.

Genuine symplectic generalized quadrangle W(3,s) has original incidence girth EIGHT: simple original point-line cycles of lengths FOUR and SIX do not exist. Therefore any nonempty alternating cycle needs at least EIGHT distinct original incidence edges, four red and four blue. But each of \(R_0,R_1\) contains only FOUR source edges total. Hence the two sets must be disjoint, using every edge of both, and their union must be one 8-cycle through exactly FOUR DISTINCT source points and FOUR DISTINCT source lines.

That is impossible if **either** P or L repeats an original source factor: a degree-four source matching whose union is a single simple C8 uses the four distinct source factors exactly once in each color on BOTH types; the common endpoint multiplicity profile must be A on each type. Contradiction. So if at least one profile B, there cannot exist TWO distinct original four-flag completing sets. Ergo \(N_{\mathrm{orig}}\in\{0,1\}\) under every allowed globally correlated original labeling. QED.

This proof is **about genuine original incidence IDs**, not physical edge multisets alone. Even if a source factor repeats in a physical C4+C2, its two selected original flags remain different; the rigidity theorem counts distinct original FOUR-flag sets, not the 24 labeled permutations and not original source C8 automorphism orbits.

## 4. NEW all-h full original D-pair physically joint 2-regular source-Hall UPPER

The parent #533 already guarantees a one-to-one dictionary between an actual original D-anchored six-ID subset Q with both physical typed projections degree TWO and an occupied **point physical residual port template** plus an occupied **line physical residual port template**, together with an actual original source matching of four remaining flag IDs. One physical residual template is A iff all its four inverse original source factor labels are DISTINCT, otherwise B iff one inverse label occurs twice.

For a fixed genuinely bilateral D pair define:
- \(A_P\), \(B_P\): counts of actually OCCUPIED first-side point physical residual port patterns of the A and B types, under the ONE original global f;
- \(A_L\), \(B_L\): analogous second-side line patterns under the ONE original global g.

The A/A physical-template pairs number \(A_PA_L\), each with at most TWO actual ORIGINAL 4-flag perfect source matchings by preexisting #512. The remaining A/B, B/A, B/B pairs number \(A_PB_L+B_PA_L+B_PB_L\), each with at most ONE actual original four-flag matching by NEW AO-1. Summing nonnegative contributions over disjoint physical-template pairs yields

\[
\boxed{
H_D(f,g)\le
2A_PA_L+A_PB_L+B_PA_L+B_PB_L.
}
\]

For a complete globally bijective K_a physical source factor label palette, parent #533 established exact full physical port pattern capacities \(A_P=A_L=7\binom{a-3}3\), \(B_P=B_L=3\binom{a-3}3\). With \(t=\binom{a-3}{3}\):

\[
\boxed{
H_D(f,g)\le(2\cdot49+2\cdot21+9)t^2=149t^2.
}
\]

Compared to counting at most 4!=24 labeled permutations for each of \((10t)^2=100t^2\) physical two-side template pairs, this is a rigorous reduction from 2400t² to 149t², **strictly more than a factor 16**. Because actual incomplete K_a images have fewer occupied physical templates, the bound using actual A/B occupied counts is STRICTER than simply substituting full K_a capacities. The selected-seven GF5 extension charge E obeys \(0\le E_D\le H_D\), as does the complementary unaligned A/A rejection charge R, but \(H_D=E_D+R_D\) does NOT imply a positive lower on E when R may dominate.

**Exact status:** the new source matching rigidity restricts the *possibility* of multiple original Q per occupied physical template, but does NOT certify any Hall-positive original Q or selected GF5 positive six-Q for every D pair. The finite true-original W32 D-pair failures from #533 remain.

## 5. Strong independent source falsifiers and genuine original W32–W38 checks

1. An independent **EDGE-FIRST** all four-incidence-subset enumeration, which does NOT use source slot permutations or their stabilizer quotient, checks every physically/source factor profile A/A, B/A, A/B, B/B across ALL 2^16 abstract 4×4 (and exact corresponding 3×4 / 4×3 / 3×3) binary original local incidence matrices, selecting only local matrices with **NO C4 OR C6 cycles** (the authentic GQ necessary local condition). Histograms of the genuine original SOURCE Hall complete-set count across these locally GQ-eligible matrices:

| Source factor profile | Local GQ short-cycle-free binary matrices with zero Q | Exactly one valid four-source-incidence set | Exactly TWO |
|---|---:|---:|---:|
| A/A | 11,321 | 4,824 | 72 |
| B/A | 1,496 | 360 | **0** |
| A/B | 1,496 | 360 | **0** |
| B/B | 302 | 26 | **0** |

   The A/A C8 row and max 2 are **previous #512**, not new; the B-containing rows and max 1 are the new source slot cases. GQ invalid C4/C6 matrices are rejected even when a naive multiset permanent would be large. Each local incidence source matrix is a NECESSARY possible GQ induced subgraph, not a claim every locally short-cycle-free small matrix embeds in W(3,s) for a particular fixed dyadic order.

2. Complete **five genuine W(3,2)** global fixed two-typed physical K6 maps: dual-zero, lex, reverse, S68 and S72, EVERY ACTUAL original D source pair (~277 per scheme), EVERY 100 occupied point/line physical port template pairs for each D, and EVERY true source 4-slot matching. Verify each pair-template contributes ≤1 when B on either side or ≤2 when A/A; validate the exact source slot-orbit quotient, and compare full resulting Hall charge against independently established parent #533 genuine W32 source-first funnel census H: dual-zero 736, lex 1,504, reverse 986, S68 492, S72 599. The new all-h per-D complete physical K6 upper equals 149, regardless of global map; actual H is much smaller. An optional full template-by-template **INDEPENDENT parent original source six-Q matching** is checked on a genuine W32 D anchor, with equality of actual original SIX different flag ID sets.

3. Genuine W(3,4) and W(3,8) original symplectic source models, lex/random globally complete but nononto K14 (six unoccupied physical pairs per typed image) or K35 (ten missing), respectively: sample occupied point/line residual physical port templates of both A and B profile types for actual D anchors; verify 0/1 or 0/1/2 and compare each independently to EDGE-FIRST true source incidence 4-flag subset enumeration (not 24 source slot permutations). No claim to exhaust millions of W38 bilateral port template pairs.

4. A genuine ORIGINAL source symplectic transvection W(3,2) plus independent point-side/line-side physical coordinate relabelings preserves the exact template A/B counts, source-Hall H, incidence C8 double-match counts and four-profile source matching histogram under TRANSPORT of the exact SAME actual source two-flag D pair. Negative malformed original source incidence, noninjective globally assigned physical source pair maps, synthetic source C4/C6, invalid source-slot multiplicities and illegal re-use of original incidence ID fail explicitly.

5. All dyadic orders h=1..80: exact BigInteger physical minimal alphabet a, original parameters V,d, physical port total capacities \(A=7t,B=3t\), and source Hall upper 149t² vs previous 2400t², with explicit flag that ALL selected-seven GF5 root lower remains unproved.

### NEW AO-3: actual ORIGINAL W(3,2) Hall charge split by source factor multiplicity and D6 alignment

The complete genuine W32 full-source D-pair census from two independently implemented original-source algorithms has been extended to partition **EVERY accepted bilateral physically 2-regular D-anchor-to-six-Q INCIDENCE** according to its ORIGINAL residual four-factor point/line multiplicity profile. Entries are source **D-anchor incidence charges**, not the number of unique source six-Q and not the count of valid slot permutations (which differ by multiplicity denominators 1, 2, 4).

| Same fixed true ORIGINAL W32 global f,g maps | Residual A/A actual original matching charge | Residual A/B | Residual B/A | Residual B/B | Total original bilateral physical 2-regular Hall \(H\) | Rejected unaligned A/A \(R\) | Aligned A/A D6 charge \(H_{AA}-R\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| dual-zero | 578 | 75 | 73 | 10 | 736 | 572 | **6** |
| lex | 1,077 | 213 | 193 | 21 | 1,504 | 987 | **90** |
| reverse | 758 | 118 | 102 | 8 | 986 | 740 | **18** |
| S68 | 413 | 27 | 50 | 2 | 492 | 413 | **0** |
| S72 | 524 | 38 | 36 | 1 | 599 | 524 | **0** |

The historical seven-GF5 classifier selects **every** genuine bilateral D-anchored source A/B, B/A and B/B original Q. For A/A it selects precisely aligned connected original-source flag-position D6. Thus, for ANY dyadic W(3,s) and any complete original globally injected typed f,g,

\[
\boxed{
E_{\mathrm{seven}}^{(D)}
=
H_{A/B}^{(D)}+H_{B/A}^{(D)}+H_{B/B}^{(D)}
+H_{A/A,\mathrm{aligned\ D6}}^{(D)}
}
\]

and
\[
H_{A/A}^{(D)}
=R_{\mathrm{unaligned\ A/A}}^{(D)}
+H_{A/A,\mathrm{aligned\ D6}}^{(D)}.
\]

Parent #530 already proved that every true D6 six-ID Q has EXACTLY SIX compatible D anchors, so the last term equals \(6S_{\mathrm{D6}}\), with \(S_{\mathrm{D6}}\) counting unique actual original aligned D6 sixsets under the SAME pair of global typed physical maps. This is a **new joint audit and source-profile-resolved exact charge ledger** of already-known selected GF5 algebra, not a new lower-bound theorem. It is independently checked against existing full original W32 Q-FIRST historical GF5 charge and full physical D-FIRST source matching.

This refined ledger pinpoints the two distinct global obstructions: (i) most physically occupied port templates have **NO genuine original source four-matching** (new AO-1 bounds their positive multiplicity by 0/1/2), and (ii) most genuine original A/A four-matchings may lie in **unaligned physically 2-regular A/A** instead of aligned D6. Stronger universal lower estimates on raw physical port patterns alone would not remove either obstruction.

## 6. Decision, acceptance, next mathematically open gate

**New restricted all-h result:** original source GIRTH-EIGHT ensures unique-or-zero real four-incidence SOURCE matchings for residual physical port template factor-slot profiles B/A, A/B, B/B; correct exact source slot permutation stabilizer quotient including repeated-factor collisions; new universally valid \(H_D\le 2A_PA_L+A_PB_L+B_PA_L+B_PB_L\) and full palette \(\le149\binom{a-3}3^2\) bound. Source profile A/A upper two and original C8 equality are credited to #512. All source graph statements are for TRUE original W(3,2^h) and all global f,g, not just finite W32.

**Not proved:** a universal \(E_D>0\) for each D, the all-f,g selected seven-class \(\Omega(s^6)\) Branch A theorem, an infinite genuine original full global counterfamily with \(S=o(s^6)\) Branch B, an independently strong Branch C reduction with positive transfer, full R3/ASET exponent, or an existence claim for large-h configurations attaining the 149t² upper. Large physical template counts and strong original per-template UPPERS cannot substitute for any positive source Hall acceptance LOWER.

**Next meaningful actual AA4-AP gate:** derive a globally uniform positive lower on \(\sum_{D}H_D-\sum_D R_D\) (original aligned positive E), or the true original zero-D-anchor selected mass U (parent #530). A source-incidence spectral, Hall, cycle-transport or switching theorem proving that the *actual globally correlated paired physical templates* contain sufficiently many ORIGINAL source-matchable and **positive GF5** four-incidence matchings is still required. This slice reduces the maximum multiplicity of such matches but gives no existence from arbitrary maps.

**Integration:** keep four additive code/test/math-Markdown/GitHub-hosted workflow files in strict Draft child of #533, pinned SHA. Exact FINAL-head dedicated + INDEX + Proof Audit + Full Research successful evidence and independent mathematical referee are required before scientific acceptance, canonical SHA-pinned claim registration/regeneration of five derived Markdown pages, stack retarget/merge, or closure of #230. None of these imply permission to merge a still unreviewed scientific Draft. Never hand-edit generated registry files.
