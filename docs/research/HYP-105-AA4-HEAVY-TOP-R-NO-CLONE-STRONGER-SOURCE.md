# HYP-105 #230 — AA4-HEAVY-TOP-R: independent source-owner → Caro–Wei → two cuts → REAL top-degree F without cloning

**Scientific status:** NEW all-order constructive HEAVY lemma, conditional only on the independently verified original W(3,s) source/SRG bound from parent [#775](https://github.com/definitely-stable/Mathlab/pull/775) and the already separately stated ordinary simple-graph C6 supersaturation theorem. The **genuinely new** step eliminates the historical factor TWO lost to rounding the number of partition blocks: select up to r actual opposite-bit physical vertices with the largest degrees into the r genuine heavy vertices. Together with the sharper fixed-H32 original source conflict bound from #775, this reduces the rigorous HEAVY denominator from **R=93312 to R=37441**, and strengthens the sextic HEAVY constant by **exactly (93312/37441)^6 >239×**. Also updates the SAME global HEAVY/LOW conditional root ledger, not only HEAVY in isolation.

**Strict ancestry:** direct Draft child of frozen [#775](https://github.com/definitely-stable/Mathlab/pull/775) exact parent SHA 1d84380b8450e62ec3d72ed2209cfaf55eecb8a1. All original source, graph and physical formulas apply to the TRUE symplectic W(3,s), s=2^h, and ANY two FIXED complete separately globally pair-injective f,g with arbitrary correlation. No random f/g, fake source flags, independent path assumptions, physical vertex duplication, edge reconstruction or graph blow-up. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**, not PROVED_A or a new ASET extraction exponent. No ancestor/main edits or merges.

## 1. Freeze ROOT quantifiers and provenance BEFORE the selector

Fix one even H>=8 (our worked case H=32), then arbitrary but fixed **existential** numerical graph constants C0>=max(1,C_graph), 0<c0<=min(1,c_graph), whose values are unknown from the published ordinary C6 graph theorem (Jiang–Yepremyan 2020, r=2,k=3). Independently fixed s=2^h>=2^H, arbitrary separately globally pair-injective correlated f,g. The root needs only Z=empty, so none of the HEAVY owner counts pays a source deletion penalty, and the LOW branch is unchanged except for the required SAME T/delta update below.

Let original W(3,s) have N=(s+1)^2(s²+1) named flags i=(p,ell). Let a be the MINIMAL physical alphabet with binom(a,2)>=(s+1)(s²+1). Each original named i owns exactly two opposite vertex-disjoint *real* diagonals of its f(p)×g(ell) rectangle. A physical undirected edge has UNIQUE original flag owner because its coordinate differences determine the full f and g pairs and both maps are injected. Hence the FULL physical H has exactly 2N different simple edges and total physical degree 4N. The fixed true source original conflict graph J is the named incidence-pencil graph from #737/#775, not a conflict graph of physical copies.

From parent #775's independently PROVED genuine GQ/SRG bound, for all s>=2^H and any fixed f,g,

\[
\boxed{e(J)<2M_Hs^4,\quad
M_H=(1+2^{-2H})(1+\frac{23}{16\cdot2^{H/2}}).}
\tag{HC-1}
\]

This is a source-SRG hypothesis of the present proof, not an empirical W32/W34 fit.

Choose the same HEAVY/LOW degree parameter T globally before f,g. Freeze full H and define Q={v:deg_H(v)>Ts}, and E_T=number of actual undirected H edges with >=1 endpoint in Q. These are FULL graph degrees. HEAVY is E_T>=s4/8; the complementary LOW is E_T<s4/8. In HEAVY, every named flag owns at most TWO of these physical edges, so the set L of their **distinct real original source flag IDs** satisfies

\[
\boxed{|L|\ge E_T/2\ge s^4/16.}
\tag{HC-2}
\]

No need to recompute Q after source deletion Z because root takes Z=empty.

## 2. Independently derive Caro–Wei with the NEW exact source cap

The induced original J[L] has at most e(J)<2M_H s4 edges. Give each named ORIGINAL flag independent uniform priority and take those that have earlier priority than every ORIGINAL neighbor in J[L]. This selects an independent original flag set with expected size

\[
\sum_{i\in L}\frac1{\deg_{J[L]}(i)+1}
\ge\frac{|L|^2}{|L|+2e(J[L])}
\ge\frac{(s^4/16)^2}{s^4/16+4M_Hs^4}
=\boxed{\frac{s^4}{16(1+64M_H)}}.
\tag{HC-3}
\]

The second inequality is exactly Cauchy. The third follows because x²/(x+4M_H s4) is increasing for positive x, and |L|>=s4/16. We need no random source maps and cannot replace real edge owners with cloned source vertices.

A **constructive** deterministic independent-set extraction gives at least the Caro–Wei potential: repeatedly choose a minimum-degree remaining named source J-vertex, add it, and delete it and its neighbors. For remaining graph G, let Φ(G)=sum_v1/(deg_G(v)+1). If v has minimum current degree d, every removed neighbor u has degree>=d, so its contribution is <=1/(d+1); there are at most d+1 removed vertices. Deleting them decreases Φ by at most 1 (remaining degrees shrink and therefore remaining reciprocal contributions rise). Hence the greedy method chooses at least Φ(initial) original independent flags. The program audits this exact Fraction potential decrease on true source J without importing previous heavy code.

## 3. Two coherent ORIGINAL WHOLE-owner physical bit cuts

Let I0 be the genuine original independent set from HC-3. Independently assign fair binary bits to the actual **first-coordinate alphabet symbols**. For a fixed ORIGINAL f(p) unordered pair {x,x'}, the probability that it is bichromatic is exactly 1/2, regardless of how many other source pairs overlap x or x'. Linearity of expectation ensures a fixed coloring retains >=half the **whole original flag owners**. Repeat on the TRUE second-coordinate alphabet for g(ell), retaining >=half again, while preserving conflict freedom and the first coloring. Therefore there is one single pair of fixed, globally coherent typed bit cuts and an independent original selected flag set S such that

\[
\boxed{|S|\ge\frac14|I_0|
     \ge \frac{s^4}{64(1+64M_H)}.}
\tag{HC-4}
\]

For any selected flag its TWO real opposite physical diagonals cross both typed bits; neither old original labels nor physical endpoints were re-generated. We independently derandomize each cut by the exact integer conditional expectation of the number of retained whole flags: an unresolved true pair contributes doubled expectation 1, a fully resolved bichromatic pair contributes 2, and a monochromatic pair contributes 0. One bit assignment is always at least the former mean; this is a deterministic formal counterpart to HC-4.

## 4. NEW all-order graph lemma, no partition and NO rounding loss

**Top-r degree lemma (arbitrary real finite bipartite graphs):** Given any actual simple bipartite graph on disjoint vertex subsets R and Y, with r=|R|>=1, y=|Y|>=1 and total existing cross-edges E, choose the subset Ystar of **min(r,y) distinct ACTUAL vertices of Y with highest integer degree into R**. Then

\[
\boxed{
e(R,Y_\star)\ge E\min(1,r/y).
}
\tag{TOP-1}
\]

**Proof:** for y>=r, order all nonnegative actual degrees d1>=...>=dy. The prefix mean (d1+...+dr)/r is at least the mean (d1+...+dy)/y, since every one of the omitted degrees is no larger than the smallest included value. Thus prefix sum >=rE/y. For y<r, select all Y and keep exactly E edges, proving the same formula. This lemma is valid even if r<y and y is not divisible by r. It does not require source regularity, independent edges or integer chunk counts. The choice uses only actual physical vertices and edges.

**Why old source construction loses a factor:** the previous #739/#744/#750 HEAVY proof divided Y into at most ceil(y/r)<=2n/r blocks, then selected the heaviest block. This guarantees only >=Er/(2n). TOP-1 **directly** guarantees >=Er/n for every y<=n when r<=n, recovering the exact lost factor two. The gain is UNIFORM, not merely a good empirical labeling.

### Apply TOP-1 to genuine HEAVY selected source graph

For each i∈S choose ONE of its actual surviving/full Q-touching physical diagonal edges e_i and ONE real heavy endpoint q_i∈Q of that edge. Because each physical edge has a unique named ORIGINAL owner, all e_i are different. Split the selected endpoints q_i by the already fixed FIRST typed bit. At least |S|/2 heavy witnesses have one same bit b.

Let R_Q={v∈Q:the real first-coordinate bit of v equals b}, r=|R_Q|>=1, and Y={real physical corners v:the bit of first coordinate v differs from b}, with y=|Y|<=n=a². Every one of those >=|S|/2 distinct witness edges crosses from REAL R_Q to REAL Y, because both typed cuts were fixed for the entire source owner. Let E be the actual total of **all selected SOURCE physical edges** between those two sets. Then E>=|S|/2.

Apply TOP-1: choose Ystar⊆Y, |Ystar|=min(r,y), with largest TRUE physical degrees into R_Q. Since r<=n and y<=n,

\[
e(R_Q,Y_\star)\ge E\min(1,r/y)\ge Er/n
\ge\frac{|S|r}{2n}.
\tag{HC-5}
\]

Take the **literal ordinary physical induced bipartite subgraph** F with genuine vertices R_Q∪Ystar and their existing ORIGINAL source-selected cross-edges. Every F edge is a real previously owned physical diagonal; no cloned vertex, source flag, physical edge or synthesized adjacency is permitted. An original source owner may have only ONE of its original two diagonals in F; this is a proper edge-deleted subgraph of the whole-flag source graph, not a claim F itself remains paired.

\[
v(F)\le r+\min(r,y)\le2r,
\qquad
\frac{e(F)}{v(F)}\ge\frac{|S|}{4n}.
\tag{HC-6}
\]

Use n=a²≤(9/4)s³ for s>=64 and HC-4:

\[
\boxed{
\frac{e(F)}{v(F)}
\ge\frac{s}{576(1+64M_H)}
\ge\frac{s}{R_H},
\quad
R_H:=\left\lceil576(1+64M_H)\right\rceil.
}
\tag{HC-7}
\]

The **exact H=32 rational computation** gives

\[
576(1+64M_{32})
=\frac{176809219594662774687400143}
       {4722366482869645213696}
\in(37440,37441).
\]

Hence **R_32=37441**, compared to the old deletion-free R=93312, with NO added assumptions beyond already independently accepted parent #775's source-J bound and the genuine real-source selector.

The full ORIGINAL H has physical degree sum 4N≤(17/4)s⁴ for s>=64. Because every actual Q vertex has full degree >Ts, q=|Q|<4N/(Ts), and r<=q. Thus on precisely these original physical vertices

\[
\boxed{
v(F)\le2r\le2|Q|<
\frac{8N}{Ts}\le\frac{17}{2}\frac{s^3}{T}.
}
\tag{HC-8}
\]

This is the SAME vertex bound as the parent proofs. Critically, **neither** F nor its true physical vertices depend on invented normalized copies, a synthetic bipartite incidence blowup or an edge multiplicity. The graph is simple.

## 5. Exact ordinary C6 supersaturation and TRUE ORIGINAL D6 source inverse

Choose once, before s,f/g, the UNKNOWN BUT EXISTING ordinary graph C6 constants C0,c0. With the NEW R=37441 set the SAME global branch parameter

\[
\boxed{T=\left\lceil\frac{17}{2}R^3C_0^3\right\rceil,
\qquad\delta=\frac{c_0}{R^6}.}
\tag{HC-9}
\]

The two exact ordinary-graph inequalities HC-7 and HC-8 imply

\[
\left(\frac{e(F)}{v(F)}\right)^3
\ge (s/R)^3
\ge C_0^3 v(F),
\]

so the published ordinary simple-graph supersaturation hypothesis e(F)>=C0 v(F)^(4/3) applies to THIS unchanged real F. Therefore the published theorem gives at least c0(e/v)^6>=δs6 simple UNORIENTED physical sixcycles.

Because all F edges come from the original independent source S and both fixed typed bit cuts, the previously independently audited all-h distance-1/2/3 properness and **unique lift from unordered six ORIGINAL incidence IDs** of [#772](https://github.com/definitely-stable/Mathlab/pull/772) applies unchanged to F (including after physical edge deletion). So

\[
\boxed{\mathrm{HEAVY}\Longrightarrow
  D_6(f,g)\ge \#C_6(F)\ge
  \frac{c_0}{37441^6}s^6.}
\tag{HC-10}
\]

The strict source-sixset injection does not divide C6 by 6, 12 or 6!, and does not assert a source-motif surjection. Our new HEAVY coefficient improves the previous c0/93312^6 by

\[
\boxed{
\frac{\delta_{\mathrm{new}}}{\delta_{\mathrm{old}}}
=\left(\frac{93312}{37441}\right)^6
\approx239.63.
}
\tag{HC-11}
\]

This is a stronger **sufficient sextic constant**, not a new exponent or a numerical value of the unpublished graph C6 parameters.

## 6. Recompute the SAME full original conditional ROOT HEAVY/LOW ledger

A stronger HEAVY source density with smaller R must propagate to the OTHER branch before any universal root statement. Do not replace R while leaving its original T, Q or LOW moment budget frozen. Retain the fixed source H=32, K=10, and original #773 asymmetrical non-Z three-error allocation alpha=(1/64,1/64,15/16). Parent #771's mathematically proved one-global-source-priority Harris/Jensen with K=10 yields q2=1936 and q3=85184. Parent #775's independently checked original source spectral bound gives

\[
c_{10,32}=\frac78-\frac{4M_{32}}{11}>0,\quad
w_{10,32}=\frac{16}{81}(4c_{10,32})^3.
\]

For the **same NEW T** from HC-9 and under LOW D6<δs6, the inherited all-h source physical moments and block bounds are

\[
L_6=24+153T^2,\quad
L_4=q_2^2\left\lceil\sqrt{\lceil17L_6/4\rceil}\right\rceil+19T,
\]
\[
B_0=\lceil\sqrt{360(K+1)T}\rceil,\quad
E=5q_3\lceil\sqrt{L_6}\rceil,\quad
D=4\lceil\sqrt{B_0TL_4}\rceil.
\tag{ROOT-1}
\]

The resulting universal conditional sufficient threshold is

\[
\boxed{s_0=\max\{2^{32},64,
\lceil111T/(2\alpha_1w)\rceil,
\lceil(E/(\alpha_2w))^2\rceil,
\lceil(D/(\alpha_3w))^8\rceil\}.}
\tag{ROOT-2}
\]

For every dyadic s>=s0, if the inherited LOW original source spectral moment/endpoint/full-A-vs-C mixed-book and P3→BBo six-ID inverses withstand full independent proof review, then LOW with small D6 produces

\[
BBo_{\rm produced}\ge\frac12w(1-\alpha_1-\alpha_2-\alpha_3)s^6
>\delta s^6
\]
and HEAVY, LOW-large-D6, LOW-small-D6 give the SAME original *unweighted* seven-disjoint-class S_s>=δs6. No arbitrary source deletion Z, GF5 R3, B75 or ASET exponent is invoked.

**New exact conditional source ledger (all C0,c0 are FORMAL placeholders, not numerically known graph constants):**

| FORMAL (C0,c0) | Old #775 R=93312 root h0 | NEW R=37441 root h0 | Dyadic orders saved |
|---|---:|---:|---:|
| (1,1) | 667 | **628** | 39 |
| (2,1/5) | 697 | **658** | 39 |
| (7/3,1/17) | 704 | **664** | 40 |

The 39–40 lower dyadic exponent only describes hypothetical sufficient size thresholds in a conditional algebraic proof. It is NOT a realizable numerical asymptotic threshold for the unknown external C0/c0, and not a new s6 exponent. The actual universally quantified c0 remains unknown, but its **relative** improvement HC-11 is exact and independent of any numerical value.

## 7. Independent source program and scientific falsifiers

New standalone research/hyp105_original_heavy_top_degree_referee.py imports ONLY the independently constructed **genuine symplectic** W(3,2)/W(3,4) ORIGINAL source fixture from hyp105_original_defect_factor_referee.genuine_symplectic_source. It imports NO prior HEAVY, Caro–Wei, two-cut, source-J, BBo, sixthwalk, ROOT or GF5 modules.

- Rebuild the entire original named-flag point/line pencil J by literal overlap and independently count it by ORIGINAL point/line collinearity: e(J)=e_col(f)+e_col(g), with true complete globally injected correlated lex/reverse/shift maps.
- Construct the entire original FULL physical graph with exactly TWO different vertex-disjoint original diagonals per named flag, ensure every physical edge has exactly one named source owner and degree sum exactly 4N. Freeze full Q_T BEFORE source selection, find distinct actual heavy edge owners without edge-ID substitution.
- Construct source J independent Caro–Wei set by min residual degree; check exact rational Phi potential decrement≤1 at each step and the full-original Caro–Wei Cauchy lower. Derandomize BOTH typed coordinate colorings by exact integer conditional expectation, preserving WHOLE source flags and both original diagonals.
- Assign actual surviving heavy witness edge AND endpoint for each selected source; take majority by fixed first-coordinate bit, create the literal R_Q and all opposite physical Y coordinates, and select its highest actual-degree min(r,y) vertices. Independently verify the stronger **unrounded** bound e_F>=e(R,Y)r/n, v_F<=2r and e_F/v_F>=|S|/(4n), with all F physical edges a literal subset of original source selected edges and their exact source owner IDs.
- Enumerate genuine real physical simple C6 in every diagnostic winning F by independent graph-first DFS, reject coordinate-improper cycles and any repeated unordered original six-ID image. Zero finite C6 is HONESTLY reported, never treated as a proof of the external supersaturation theorem.
- An entirely separate **ABSTRACT** all-graph exhaustive top-r oracle checks ALL 255 nonempty bipartite 2×4 edge subsets and an E=4, r/y=1/2 *equality witness*. This is an adversarial check of the NEW top-r lemma only, explicitly not a synthetic replacement for true GQ provenance.
- Finite true W32/W34 diagnostic s=2,4 and T=0..3 samples may not satisfy the enormous all-h HEAVY cutoff; these tests are genuine source-structural falsifiers, not extrapolations. Includes negative empty-heavy, illegal T, malformed external C0/c0, genuine source J, independent source selection and two-cut invariants. A strict CI capsule checks NEW R=37441, old R=93312 and all three formal all-h conditional h0 and root/ASET STOP flags.

**Acceptance gate:** This manuscript establishes the all-h HEAVY owner/Caro–Wei/two-cut/top-r no-clone F construction as a new independently auditable combinatorial proof, conditional on the already proved true GQ-SRG original J input from #775. It imports external C6 supersaturation strictly as an existential theorem and original C6→D6 six-ID inverse from #772 as separately proved local steps. The global ROOT issue #230 is NOT promoted to PROVED_A: genuine full-Q LOW selected fourth/sixth moment, mixed full-original A/CORE C blockers, endpoint and P3→produced ORIGINAL BBo inverses remain to be **independently accepted all-h**.

**Next allowed scientific review:** selected LOW simple bipartite sixth-walk / fourth-energy interface, then the genuine mixed full-A/CORE-C four-blocker envelope and exact source BBo inverse, then end-to-end root proof DAG. No main/ancestor merges or issue closure from passing finite GitHub CI.
