# HYP-105 / #230 — AA4-AD: exact opposite-side physical-A Hall/permanent transfer for ORIGINAL B/A and A/B

**Research-only, strict genuine original W(3,2^h) all-h theorem, NOT an all-map lower.** Parent [AA4-AC-ROOT PR #509](https://github.com/definitely-stable/Mathlab/pull/509), pinned exact parent commit \`2d410740de54689045f911d011ff1a4776c7697f\`. Parallel [Y5 #507](https://github.com/definitely-stable/Mathlab/pull/507) already supplies the source-only original 4-rook permanent and original B/A first-gate loss decomposition; this new slice handles the **missing second, opposite-physical-A gate**. It does NOT claim Hall's theorem, the 4x4 permanent or known simple-graph two-factor counting as original mathematics. The contribution is their exact ORIGINAL GQ + globally injected physical GF(5) transfer identity, with independent finite falsification.

## 1. Model and the precise missing gate

Let s=2^h, h>=1, V=(s+1)(s²+1), d=s+1, a=min{t:C(t,2)>=V}, K=C(a,2). The source is the actual ORIGINAL symplectic W(3,s) incidence graph I subseteq P×L, not a fabricated regular graph. Complete globally injective typed physical pair maps f:P->E(K_a), g:L->E(K_a) are kept fixed across **ALL** original six-incidence ID sets Q; the image may miss K−V physical edges. Historical selected GF(5) B-left/A-right and A-left/B-right means B on one typed side and physical A on the other, on the **same six original incidence IDs**, not independent per-Q map redraws.

Fix side B=point (dual swaps P,L), an actual ORIGINAL source root p, TWO distinct original incident source flags (p,l₀),(p,l₁), and four distinct other original points q₁,…,q₄ whose four globally fixed f(qᵢ) form a **simple physical four-cycle** on the four coordinates complementary to f(p). This is a realized original B-side physical pattern, not four arbitrarily postulated new labels.

Define genuine source neighborhoods Aᵢ=N_I(qᵢ)\{l₀,l₁}. The four chosen remaining original lines lᵢ must each belong to Aᵢ and be pairwise distinct to form the true original B/A source-forest class. Y5 already counts this first gate exactly by four-rook/permanent inclusion-exclusion. However, to be ACCEPTED the six GLOBAL physical line labels

\[
g(l_0),\ g(l_1),\ g(l_1'),\ g(l_2'),\ g(l_3'),\ g(l_4')
\]

must form a simple physical six-edge, six-coordinate 2-factor (either a connected C6 or two C3). The superscript prime labels the four *new* neighbor assignments and avoids overloading the pinned l₀,l₁. Connected six-position matching between the two physical halves is required for AA/D6 only, **not** here.

## 2. NEW all-h exact TRUE-original opposite physical-A transfer theorem AD-HALL

Let e₀=g(l₀), e₁=g(l₁), distinct actual globally injected physical unordered pairs. Define the finite set

\[
\mathcal F_a(e_0,e_1)
=\{H\subseteq E(K_a): |H|=6,\ H\text{ is a simple 2-factor on exactly 6 physical coordinates},\
e_0,e_1\in H\}.
\]

Each H has four remaining physical edges \(R_H=H\setminus\{e_0,e_1\}\). Write O=im(g), and call H **occupied** if all four remaining physical edges lie in O. Since g is globally injected, occupied H has exactly four distinct *actual original line factors*

\[
(t_1,t_2,t_3,t_4)
=\big(g^{-1}(e):e\in R_H\big).
\]

For occupied H, form a 4×4 ZERO–ONE matrix on the same true source factors and GLOBAL opposite physical labels:

\[
B_H(i,j)={\bf1}\{t_j\in A_i\}.
\]

**Exact all-h identity, for every real W(3,2^h), every complete globally injected f,g, every realized B root/cohort/C4:**

\[
\boxed{
A_{\rm GF5}(p,l_0,l_1,q_1,\ldots,q_4;f,g)
=
\sum_{\substack{H\in\mathcal F_a(e_0,e_1)\\R_H\subseteq O}}
\operatorname{perm}(B_H).
}
\]

Here the left side is the number of **distinct actual six-original-incidence-ID Q** in this fixed physically B-rooted cohort whose opposite *same Q* physical projection is historical A.

**Proof of exact bijection:** each accepted Q assigns four distinct actual original opposite factors t_i∈A_i. Their globally injected images, together with g(l₀),g(l₁), form EXACTLY ONE physical 2-factor H, which is necessarily occupied. Sorting the four other H edges canonically makes an injective assignment equivalent to ONE permutation σ of columns satisfying B_H(i,σ(i))=1; hence it contributes exactly once to perm(B_H). Conversely any occupied H with any 1-permutation yields four actual distinct opposite source factors, genuine actual incident source flags (q_i,t_{σ(i)}), six different actual original incidence IDs, true opposite original source A forest, and the physical A 2factor on precisely those six original Q. Original B-side physical C4 is fixed by the cohort. No inclusion-exclusion approximation or independence assumption occurs.

The same theorem holds verbatim with ORIGINAL point and line roles swapped, yielding A-left/B-right.

## 3. NEW exact Hall-positive feasibility certificate

For each occupied H, let N_H(J)=union of allowed columns for a subset J of the four original q_i rows. Hall's theorem states

\[
\operatorname{perm}(B_H)>0
\quad\Longleftrightarrow\quad
\forall \varnothing\ne J\subseteq[4]:
|N_H(J)|\ge|J|.
\]

A **Hall obstruction witness** is an explicit subset J with |N_H(J)|<|J|. There are at most 15 nonempty J, so checking every H can return a finite, inspectable certificate of why a given physical 2-factor cannot support a true original B/A motif.

Define F_all=#\(\mathcal F_a(e₀,e₁)\), F_occ=#occupied H, F_Hall=#occupied H satisfying Hall, and T=the exact accepted original GF5 cohort count. Then all h and all maps:

\[
\boxed{0\le F_{\rm Hall}\le T\le24F_{\rm Hall},\qquad
T>0\iff F_{\rm Hall}>0.}
\]

**Crucial new failure taxonomy:** a cohort can have many valid genuine original SOURCE B/A forests yet T=0 for (i) absent physical 2-factor completions/unused physical images or (ii) physical completions present but **all** blocked by an original source-neighborhood Hall obstruction. Neither mechanism follows from source-only forest cardinality or a 1-sided physical count.

F_Hall is a conditional H-dependent family of original source matching constraints, not a uniform positive lower. A global all-h lower must prove many occupied Hall-positive completions across the complete typed maps, or must instead use non-BA GF5 modes.

## 4. Exact physical completion capacities and complexity

Two distinct pinned physical edges are either adjacent (3 distinct pinned coordinates) or disjoint (4). Elementary cycle/2triangle enumeration gives all a≥6:

\[
\boxed{
|\mathcal F_a(e_0,e_1)|=
\begin{cases}
7\binom{a-3}{3}, & |e_0\cap e_1|=1,\\[2mm]
14\binom{a-4}{2}, & |e_0\cap e_1|=0.
\end{cases}}
\]

These physical-pattern counts were previously established as class A two-edge pattern capacities in AA4-Y3; we independently regenerate all 60 connected C6 + 10 disconnected 2C3 labeled 6-vertex patterns here, not proclaim a new physical counting theorem. The adjacent/disjoint complexity of this per-cohort second-gate certifier is O(a³)/O(a²), respectively, times a fixed 4×4 Hall/permanent computation (15 row subsets; at most 24 permutations). It never enumerates all C(N,6) original source Q.

The algorithm must NOT treat a partial physical injection image as full E(K_a). Every missing pair image removes affected H, and the output reports F_all, F_occ, F_Hall, T individually.

## 5. Strict independently falsifiable true original checks

1. Independent generation of all K6 six-coordinate two-factors: 60 connected cycles and 10 disjoint two-triangle 2-factors. Exhaust **every** pair of distinct K6, K7 and K8 physical edges; independently check each pinned physical enumeration is exactly the above formula, has six pair-distinct edges and six vertices all degree two.
2. Random and adversarial four-row 0–1 permanent matrices; verify all 15 original source-neighborhood Hall inequalities and equivalence with the 24-permutation literal permanent, including explicit Hall failing subsets.
3. TRUE ORIGINAL W(3,2): for each of the four globally complete S68, S72, lex, reverse label pairs, enumerate all 15 physical B roots ×C(3,2)=45 *ACTUAL ORIGINAL two-flag root cohorts*, and all three physical C4 patterns per cohort, on **both sides**. For each of 135 cohorts per side, recompute T with the theorem, and independently enumerate all \(\le d^4=81\) actual original opposite source assignments without using physical 2-factor completion enumeration or per(H) permanent. Compare T count, the independently implemented historical seven-tag join, and the existing Y5 genuine ORIGINAL source-only counts.
4. W32 source-only vs actual original accepted GF5 anchor baselines, from independently verified Y5:
   - S68: B/A 6098→44; A/B 4740→21.
   - S72: B/A 6098→36; A/B 4864→31.
   - lex: B/A 5000→98; A/B 5793→110.
   - reverse: B/A 5000→77; A/B 4428→74.
5. TRUE ORIGINAL W(3,4) where K=binom(a,2)>V: fix actual genuine source flag pairs and realized physical B C4 from the *globally injected but not onto-all-E(K_a)* labels; independently brute the at most d^4=625 actual opposite source assignments and verify that unused physical pair images cannot masquerade as genuine original factors.
6. Negative models: same physical edge assigned to two source factors; duplicate actual original source flags; two source factors whose physical labels do not form a connected B C4; malformed physical coordinates; wrong original incidence model. Fail closed.

This supplies reproducible exact tables, formulas, tests and a versioned mathematical record; no generated RCP Markdown is hand-edited.

## 6. NEW hosted finite obstruction localization: complete physical K6, original Hall is bottleneck

Exact original W(3,2) physical alphabet E(K6) has K=V=15, so every full original type-specific map is a physical-edge **bijection**. Consequently EVERY six-edge physical two-factor H containing the two pinned opposite images is occupied; F_occ=F_all in ALL cohorts, not merely on average. Still very few physical completions survive the **original source-neighborhood Hall constraints** under actual global f/g.

The following table is the exact summation of 135 actual original B-root/two-flag/C4 cohorts per historical type, derived by this slice's standalone opposite physical 2factor/permanent oracle and **independently verified by direct authentic opposite original neighbor incidence assignments**, plus the preexisting original seven-tag GF5 join:

| TRUE W(3,2) original global scheme | Historical immutable GF5 tag | Genuine original B/A or A/B source-only forests | All physical 2factor completions | Occupied physical 2factors | Hall-positive original completions | Accepted actual six-original-flag GF5 | Cohorts with NO GF5 acceptance /135 |
|---|---|---:|---:|---:|---:|---:|---:|
| S68 | B-left/A-right | 6,098 | 1,386 | 1,386 | **44** | **44** | 100 |
| S68 | A-left/B-right | 4,740 | 1,155 | 1,155 | **21** | **21** | 119 |
| S72 | B-left/A-right | 6,098 | 1,365 | 1,365 | **36** | **36** | 106 |
| S72 | A-left/B-right | 4,864 | 1,155 | 1,155 | **31** | **31** | 113 |
| lex | B-left/A-right | 5,000 | 1,218 | 1,218 | **98** | **98** | 73 |
| lex | A-left/B-right | 5,793 | 1,344 | 1,344 | **109** | **110** | 55 |
| reverse | B-left/A-right | 5,000 | 1,449 | 1,449 | **77** | **77** | 78 |
| reverse | A-left/B-right | 4,428 | 1,344 | 1,344 | **74** | **74** | 75 |

**Precise interpretation:**
- Original source-only forests are a different pre-physical reservoir from the physical completion counts; do NOT divide one by the other as a probability.
- For TRUE W32 *all* full-K6 physical second-side completions are occupied, therefore the observed rejection of almost all H is strictly due to original source-neighborhood **Hall incompatibility** under the jointly fixed original GQ and physical point/line map pair, not vacant physical labels.
- The lex A-left/B-right row gives **110 accepted original Q from only 109 Hall-positive 2factors** because at least one 4×4 incidence matrix has more than one perfect matching. Counting Hall-positive H instead of permanents loses multiplicity: the exact formula requires **permanents**, while Hall provides only the positivity/zero certificate and bounds F_Hall ≤ T ≤ 24F_Hall.
- W32 Hall-zero cohort counts are exact for the 135 cohorts in each tag, NOT all-h zero fractions or asymptotic evidence. These finite observations do not prove a universal positive bound (or global counterexample) for s→∞.

This explicitly isolates the mathematical object that the next research slice must control: the **globally correlated abundance of occupied Hall-positive completion 2factors** across real original roots and physical sectors. No original-source-only counting extension is needed.

---

## 7. Acceptance and next true research gate

**PROVED RESTRICTED ALL-h:** exact opposite-physical-A GF5 accepted original-B-root count via occupied same-H four-rook permanents; exact Hall obstruction iff zero; physical 2-factor capacities (prior known); and explicit per-root finite physical/source-loss taxonomy. These are exact genuine ORIGINAL six-Q statements for all global injections, not abstract random source subsets. The finite experimental tables are **support**, not proof of all-h positivity.

**NOT PROVED:** uniform \(F_{\rm Hall}=\Omega(\dots)\) on arbitrary globally injected maps, deterministic \(\inf_{f,g}S_s=\Omega(s^6)\), infinite adversarial counterfamily, root Branch A/B/C, full R3 or ASET. Source-uniform \(\mathbb E S_s=(1070/3+o(1))s^6\) is unchanged and irrelevant to worst-case without further coupling.

**Next decisive theorem candidate:** use true GQ incidence/JPKC/EICE together with the fact that *one global* opposite injection is reused across all Hall rows and cohorts, to prove a lower bound on the total *occupied Hall-positive physical completion* count in all four symmetry-normalized point/line edge sectors. If such a lower fails, construct actual globally injected counter maps and state the restricted NO-GO. Positional AA/D6 may compensate if BA/AB-only Hall mass vanishes; an unrestricted lower must not silently drop this possibility.

**Integration:** research-only Draft strict child of #509, exact parent HEAD pinned. Require dedicated/INDEX/Proof Audit/Full Research SUCCESS on exact final child and independent mathematical referee. Then register properly scoped mathematical claim, source SHA, proof prerequisites and evidence as canonical RCP JSON and regenerate five structured Markdown registry docs; do not manually change generated docs or merge scientific draft chain to main in this slice. #230 remains OPEN.
