# HYP-105 / Issue #230 — AA4-DICHOTOMY: all-h ORIGINAL source proper-P3 covariance sign and quantitative factor-four theorem

**Scope and governance.** Scientific Draft, strictly stacked on immutable [#752](https://github.com/definitely-stable/Mathlab/pull/752), parent SHA 89bf409edd363d37314fac6566c15d4134be1041. The parent independently supplied an exact rational joint probability for any two physical original-source 3paths. The present result is a NEW **universal all-order sign characterization and quantitative covariance lower bound** for any two **same ordered physical endpoint** coordinate-proper 3paths. It does NOT rely on a finite W32 empirical pattern to prove the universal statement. The new exact source algorithm independently builds true original point-line flags, source J, both real physical diagonals, path pairs and priority/typed-cut probabilities using only the original true symplectic source generator from #748, without importing #752 source computations. Issue #230 stays OPEN_WITH_FORMAL_BLOCKER; no main, parents, merges or purported ASET exponent.

## 1. Quantified exact original-source theorem

For ANY dyadic s=2^h, take the true symplectic W(3,s) with its named ORIGINAL incidence flags I, complete separately globally pair-injected fixed f:P→binom([a],2), g:L→binom([a],2) with arbitrary mutual correlation, arbitrary adversarial deleted original flag IDs Z and arbitrary paired remaining physical core C⊆I\Z. Each retained flag owns BOTH true opposite physical rectangle diagonals. Let J_C be the original source conflict graph: two distinct retained source flags conflict if they share a TRUE original point and their physical g-line labels intersect, or share a TRUE original line and their physical f-point labels intersect. The LOW construction has max degree K=64, but this theorem does not require that bound.

Draw ONE uniform random source-priority permutation on C and independently TWO typed uniform binary physical symbol colorings. A true original flag survives if it is a strict local priority minimum in J_C and its original f and original g pair labels BOTH cross their respective cuts; BOTH physical diagonals of each retained flag survive WHOLE.

Fix two directed coordinate-proper actual physical CORE 3paths γ,η with the **same ordered physical first and last vertices (v0,v3)**. Each path has four pairwise distinct first physical symbols and four pairwise distinct second physical symbols, three unique actual original flag owners with pairwise nonconflicting source J IDs. Their individual survival probabilities p_γ,p_η are strictly positive.

Let S=S_γ∪S_η be the union of all distinct REAL ORIGINAL owner IDs, |S|≤6. Let H_f(S),H_g(S) be the actual two undirected **physical symbol label-pair** graphs whose edges are the named original f/g factor pairs of the flags in S, with any duplicated factor pair collapsed. Then exactly one of the following applies:

**INCOMPATIBLE**: S contains a true source J edge, or H_f(S) is nonbipartite, or H_g(S) is nonbipartite. In this case

\[
\boxed{\Pr(\gamma,\eta\text{ survive})=0,\quad
\operatorname{Cov}(1_\gamma,1_\eta)=-p_\gamma p_\eta<0.}
\tag{D-1}
\]

**COMPATIBLE**: S is independent in true J_C AND both H_f(S),H_g(S) are bipartite. In this case

\[
\boxed{\Pr(\gamma,\eta\text{ survive})\ge4p_\gamma p_\eta,\quad
\operatorname{Cov}(1_\gamma,1_\eta)\ge3p_\gamma p_\eta>0.}
\tag{D-2}
\]

Thus for pairs with the SAME ordered physical endpoints there are **NO zero covariances** and no negative covariances of nonzero joint survival. The negative-sign locus is EXACTLY the source-conflict-or-odd-factor-cycle obstruction locus. The lower 4 is independent of s, f/g correlations, Z, the physical core, and the source conflict maximum K.

The theorem applies to the original SOURCE of the actual LOW selector used in #230. It neither asserts that all proper path pairs are compatible nor that the sign of a covariance for paths with arbitrary DIFFERENT endpoints has the same quantitative factor 4.

## 2. The complete all-h proof: exact factorization, PRIORITY POSITIVE ASSOCIATION

For any original owner set S, denote by E_J(S) the event that all owners in S beat ALL their true J_C neighbors in the ONE shared uniform source-priority permutation. For either typed alphabet side h=f or g, denote by E_h(S) the event that every actual true original physical label pair h(i), i∈S, crosses the ONE shared fair binary coloring of side h. The original priority experiment and the two typed color experiments are independent, but different paths are not. Therefore:

\[
\Pr(\gamma,\eta\text{ both survive})
=\Pr(E_J(S))\Pr(E_f(S))\Pr(E_g(S)).
\tag{D-3}
\]

If S contains a source J edge, E_J(S) is impossible: neither of the two conflicting ORIGINAL owners can be earlier than the other. If H_h(S) has an odd cycle, E_h(S) is impossible because alternating two colors around an odd cycle reverses the starting color. This proves the zero joint probability of D-1, while p_γp_η>0 because each path individually uses a true conflict-free three-flag proper physical x and y path.

Now assume S is J-independent. Replace the uniform random original source permutation with iid continuous uniform priorities T_i∈(0,1) for all retained flags; almost surely this produces exactly the same uniform order. Define independent transformed uniforms

\[
Y_i=1-T_i\quad(i\in S),\qquad
Y_j=T_j\quad(j\notin S).
\]

All Y_i remain mutually independent and identically distributed uniform on (0,1). Every local-source-priority condition for a path owner i∈S and a true original conflict neighbor j∉S becomes

\[
T_i<T_j\iff (1-Y_i)<Y_j\iff Y_i+Y_j>1.
\]

Because S is independent, NO condition has both its endpoints in S. Therefore **both** E_J(S_γ) and E_J(S_η) are coordinatewise nondecreasing events in the SAME independent product vector Y, not just separate monotone events under different transformations.

For any two coordinatewise nondecreasing functions of independent scalar uniforms, Harris's elementary product-order association inequality gives E(FG)≥EF·EG. One can prove it by induction on the independent coordinates: for a single scalar U,

\[
2\operatorname{Cov}(F(U),G(U))
=\mathbb E[(F(U)-F(U'))(G(U)-G(U'))]\ge0
\]

for an independent U', since both differences have matching signs; condition successively on all other coordinates and iterate. No random f/g labels, source path independence, asymptotic limit or external concentration theorem is needed.

Consequently

\[
\boxed{p_J(S_\gamma\cup S_\eta)
\ge p_J(S_\gamma)\,p_J(S_\eta)}
\tag{D-4}
\]

whenever the true ORIGINAL owner union is J-independent. This inequality is uniform for ANY finite original source conflict graph, any size of the owners and any overlap or shared outside J neighbors.

**Negative-scope caution.** If S contains a J edge, there is no shared coordinatewise monotonicity transform respecting both local-minimum events: they are mutually exclusive, and D-4 generally fails. This is exactly one of the mutually exclusive categories in D-1. Claiming unconditional source-priority positive association would be false.

## 3. The complete all-h proof: each typed physical cut gives at least factor TWO

For h=f or g, the r=3 proper original physical path γ corresponds to three ACTUAL pair edges h(i_1),h(i_2),h(i_3) forming the simple 3-edge path on its four distinct typed physical coordinates. The first physical symbol of this factor path is the first symbol of v0 and its last symbol is the corresponding symbol of v3; this is true even for different source flags with arbitrarily correlated h maps. Thus its factor constraint graph H_h(S_γ) is a connected four-vertex tree, with rank three for the GF(2) linear equations b_u⊕b_v=1. Exactly 2 of 2⁴ local binary assignments satisfy all three crossings, so

\[
c_h(S_\gamma)=2^{-3}=1/8,\qquad c_h(S_\eta)=1/8.
\]

Both factor constraint graphs contain the **SAME TWO DISTINCT typed physical endpoint symbols**, because the two whole physical 3paths share ordered v0 and v3 and each has distinct typed physical endpoints. Their union therefore has at most 4+4−2=6 used factor symbols and is connected. In the compatible case it is bipartite. Its exact GF(2) equation rank is

\[
r_h(S)=v_h(S)-1\le5.
\]

The true joint coloring probability is exactly c_h(S)=2^{-r_h(S)}, with freely chosen bits on all unused alphabet symbols canceling from the normalized fraction. Hence

\[
\boxed{\frac{c_h(S)}{c_h(S_\gamma)c_h(S_\eta)}
=2^{6-r_h(S)}\ge2.}
\tag{D-5}
\]

The first and second typed physical color cuts are independent of EACH OTHER, but each is SHARED across both paths. Multiplying (D-4) and both copies of (D-5) proves the unconditional factor 4 in D-2:

\[
\frac{\Pr(\gamma,\eta\text{ both survive})}
{\Pr(\gamma\text{ survives})\Pr(\eta\text{ survives})}
=
\underbrace{\frac{p_J(S)}{p_J(S_\gamma)p_J(S_\eta)}}_{\ge1}
\underbrace{2^{6-r_f(S)}}_{\ge2}
\underbrace{2^{6-r_g(S)}}_{\ge2}
\ge4.
\tag{D-6}
\]

This **explicit multiplicative decomposition** proves that every compatible same-endpoint pair has strictly POSITIVE covariance, no matter how their ORIGINAL incidence flags, physical labels, original source conflict neighborhoods or actual deleted Z are correlated.

### Stronger instance-specific factor

Equation D-6 gives a computable stronger bound for each compatible pair: its exact physical color amplification alone is \(2^{12-r_f(S)-r_g(S)}\ge4\), with any further gain from the exact original priority correlation. The new finite algorithm records the distribution of \(2^{10-r_f(S)-r_g(S)}\) — the integer power-of-two EXTRA factor above the guaranteed four. Such stronger instance-specific gains are not asserted uniform across all original f/g; the universal guarantee remains four.

## 4. NEW exact original LOW second-moment decomposition into compatible and incompatible pairs

Let P3(u,v) be the true unselected coordinate-proper physical path count in the genuine ORIGINAL paired CORE, and X_ω(u,v) the number retained under ONE shared source selector. For each original path γ define its exact marginal p_γ>0, and fix ordered physical endpoints. Write \(\mathcal C_{u,v}\) for pairs of paths with compatible owner and typed factor union and \(\mathcal B_{u,v}\) for all incompatible pairs, where pairs are ORDERED and include identical path pairs.

Define the exact rational weight sums

\[
G:=\sum_{u,v}\sum_{(\gamma,\eta)\in\mathcal C_{u,v}}
p_\gamma p_\eta,\qquad
B:=\sum_{u,v}\sum_{(\gamma,\eta)\in\mathcal B_{u,v}}
p_\gamma p_\eta.
\]

By expanding the square of the actual endpoint expectations,

\[
\boxed{\|\mathbb EX_\omega\|_F^2=G+B.}
\tag{D-7}
\]

By the exact original joint identity, incompatibles contribute ZERO to the selected second moment while the all-h factor-four theorem yields

\[
\boxed{\mathbb E\|X_\omega\|_F^2
\ge4G=4(\|\mathbb EX_\omega\|_F^2-B).}
\tag{D-8}
\]

The actual variance gap decomposes without any fake path independence:

\[
\mathbb E\|X_\omega\|_F^2-\|\mathbb EX_\omega\|_F^2
=\sum_{\rm compatible}
(\Pr(\gamma,\eta)-p_\gamma p_\eta)
-\sum_{\rm incompatible}p_\gamma p_\eta
\ge3G-B.
\tag{D-9}
\]

The full variance is also nonnegative by Jensen. Thus the true selected proper-path tensor moment has an **INSTANCE-AWARE quantitative compatible-path contribution**, rather than merely a qualitative covariance sign. In the root LOW proof, \(\mathbb E\|X\|_F^2\le L_6s^6\) from the independent selected bipartite sixth-walk theorem can be combined to obtain

\[
\boxed{\|\mathbb EX\|_F^2\le\tfrac14L_6s^6+B.}
\tag{D-10}
\]

However D-10 is a genuinely stronger universal source estimate ONLY if the incompatible pair-weight B can be bounded uniformly below the old Jensen loss. It is NOT legitimate to drop B. No new original six-motif \(\Omega(s^6)\) exponent or improved \(q_3\) constant is claimed from the current finite examples. This explicitly identifies the next mathematical bottleneck: upper bound the genuinely incompatible same-endpoint original path-pair weight under all fixed correlated f,g without assuming they are independent.

## 5. Independent COMPLETE true-original W32 census and W34 falsification

The new algorithm, separate from predecessor #752 calculations, builds all genuine symplectic W(3,2)/W(3,4) ORIGINAL flags using only the independently checked original finite source constructor; reconstructs fixed complete globally pair-injective lex/reverse/shift f/g maps, original point and line pencil source conflict J, BOTH true physical opposite diagonals per flag, ORIGINAL named source-ID core and Z, and full directed physical coordinate-proper P3 paths. No historical LOW, selector, graph, covariance or GF5 code is imported by its main referee.

For each same-endpoint actual original path pair, independently classify by the disjoint priority source J→first typed odd cycle→second typed odd cycle→compatible sequence. Compute the actual original rank-priority rational integral, both independent typed GF2 color ranks, full exact joint probability, exact covariance and original marginal products. Verify D-1–D-6 for **EVERY** actual same-endpoint path pair, not a statistical fraction. The new tests also consult #752's independently written joint-source probability algorithm **TEST ONLY**, to detect implementation agreement/failure in known source witnesses; the main implementation never imports it.

For the complete W(3,2) lex source, the known prior population (to be independently regenerated by the new code) consists of 45 true ORIGINAL incidence flags, 90 physical edges, all 1346 directed physical proper 3paths and exactly 4370 ordered same-endpoint path pairs split as follows:

| True-original W32 exact class | Number of directed path pairs |
| --- | ---: |
| Compatible, necessarily positive covariance with joint≥4 marginal product | 2386 |
| Original source J conflict, exactly negative covariance | 1348 |
| J-compatible original point-symbol odd-cycle | 464 |
| J-compatible first-color-compatible original line-symbol odd-cycle | 172 |
| Total | 4370 |

The full previous exact selected second moment must be recovered **independently**:

\[
\mathbb E\|X\|_F^2
=\frac{2464778346891846823}{3826102303457280000},\quad
\|\mathbb EX\|_F^2
=\frac{170009657654496199}{164130319761408000000}.
\]

The separate NEW quantitative compatible source-floor ledger records exact G, B, all factor-four boost exponents, the universal \(4G\) floor, and a new independent signed sum of covariances equal to the difference between the two fractions above. In particular the number 1984 negative covariances is **fully explained by the three mutually exclusive genuine-source obstructions**, not an unexplained empirical sign pattern. Each of the four types has a concrete actual directed physical path pair and named ORIGINAL incidence IDs.

Additional true-original W32 full reversed labels and adversarial named original 17-step deletion Z are completely enumerated, while three W(3,4) independent correlated maps and retained original even/Z17 CORE configurations use EXPLICIT deterministic path and same-endpoint pair samples only, without falsely promoting a partial W34 count to a full source moment.

## 6. Scientific acceptance and next permitted proof step

**New rigorous all-h statements:** original source local-minimum priority positive association for any J-compatible set of two path-owner populations; exact typed physical-cut factor-two for compatible proper 3paths with same physical endpoints, hence exact all-order negative-if-and-only-if ORIGINAL J/factor-odd-cycle and quantitative fourfold positive-survival dichotomy. The exact weighted compatible/incompatible second-moment decomposition D-7–D-10 is an algebraic consequence valid for ANY fixed correlated legal original f/g and named deletion Z. The finite original source program is a falsifier of implementation and source compatibility, not the source of the universal proof.

**Unclosed scientific dependency:** no uniform bound on the bad pair-weight B has yet been established. The previous original LOW energy, true GQ mixed A/C four blocker and seven-class original GF5 risk proof DAG remains subject to its stated independent line-by-line acceptance. Root Issue #230 stays OPEN_WITH_FORMAL_BLOCKER; neither stack merges nor a new ASET extraction exponent are justified.

**Next allowed action:** derive a deterministic bound on B from the actual original J source collision budget, typed physical odd-cycle structure and shared-endpoint original path tensor. Test it for arbitrary fixed correlated f/g and ORIGINAL Z. Such a bound, together with D-10, could yield a non-vacuous improvement to the all-h LOW sixth-moment constant. Do NOT discard bad pairs or equate source risk with a union probability.
