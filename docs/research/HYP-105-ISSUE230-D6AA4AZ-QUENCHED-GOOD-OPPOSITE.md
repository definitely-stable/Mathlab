# HYP-105 / #230 — AA4-AZ: true-original GOOD opposite-port wedges, exact fixed-f/right-support mean, ≥s⁶/128 for h≥5

**Scientific status: proved partial quenched-expectation lemma, NOT #230 Branch A/B/C.** Strictly stacked Research Draft child of [AA4-AY #560](https://github.com/definitely-stable/Mathlab/pull/560) pinned original parent HEAD a1098204561548a1521bbdd734333f8de4b7cac7. Preserve genuine source symplectic W(3,s), s=2^h; V=(s+1)(s²+1) genuine point factors and V line factors; d=s+1 genuine incidences at each factor; EXACTLY THREE different source incidence flag IDs in every counted wedge, with three distinct original point IDs and three distinct original line IDs. Keep one fixed complete globally injected point physical pair-edge map f and one physically occupied right image support E_r size V. Average over ONE uniformly random COMPLETE globally injected right original LINE map g onto that fixed E_r. No per-motif right-edge rerandomization; all source triples see the same globally coherent g.

## 1. New scope relative to parents and prior work

The previous [#560](https://github.com/definitely-stable/Mathlab/pull/560) exactly factored the quenched physical opposite three-original-flag mean for ALL-D, without the strict globally GOOD port filter. Parent #554 supplied the TRUE original complete source-corrected four-cell physical transport for all D; parent #538 and #543 defined GOOD globally via the AA4-AO bad physical coordinates; #556/#557 already established the **deterministic local** sharp 2×2 minority bound for GOOD port triangles, but DID NOT prove the global two-sided positive minority product for EVERY fixed original f,g. [#544](https://github.com/definitely-stable/Mathlab/pull/544) already proved much stronger stochastic six-original-ID **D6** abundance using whole global permutations; we do NOT claim priority for random labeling or a completed GF5 theorem.

The new advancement is an exact **GOOD-FILTERED** counterpart of the ALL-D quenched threeflag factorization, with a uniform explicit all-h-large lower despite adversarial missing physical K_a edges and their resulting bad coordinate sets. It remains an *expectation over a different full global g*, not a uniform lower at the adversarial given original g.

## 2. EXACT globally bad/clean coordinate semantics

For a completely globally injected unordered physical pair-image support E⊂E(K_a), |E|=V, K=binom(a,2), m=K−V≤a−2, define missing-coordinate degrees m_v=|\{w:\{v,w\}\notin E\}|. AA4-AO defines bad physical coordinates exactly by

\[
\mathrm{Bad}(E)=\{v:16m_v\ge a\}.
\]

Since Σ_v m_v=2m<2a, |\mathrm{Bad}(E)|≤31. Define the **induced clean occupied support** E°={ {u,v}∈E : u,v∉Bad(E)} and rooted physical two-port edge energy

\[
T_\circ(E)=\sum_{\{u,v\}\in E^\circ}
(\deg_{E^\circ}(u)-1)(\deg_{E^\circ}(v)-1).
\]

Every genuine-original bilateral D pair (p,l) ↔ (q,k) uses exactly ONE common point physical coordinate and one common line physical coordinate, with different original point/line factors. AA4-AR classifies a pair as GOOD precisely when the TWO OUTER physical point coordinates (the nonshared endpoints of f(p),f(q)) and the TWO OUTER physical line coordinates (the nonshared endpoints of g(l),g(k)) avoid the corresponding Bad sets. This is a **support-only** criterion on whether coordinates are bad: Bad(E_r) is FIXED as g permutes original LINE source factors among the SAME globally occupied right E_r.

Take two D neighbors of a source center (p,l) in the two OPPOSITE physical point ports and in the two OPPOSITE physical line ports. Write its point physical edge f(p)={u,v}, and those of neighbors {u,w_0} and {v,w_1}. For BOTH pairs to be GOOD, we must have u,v,w_0,w_1 all nonbad, since each D pair checks its two **outer** point coordinates. This is equivalent to all three actual point physical pair edges lying in E_f°. The same iff holds independently on the original line-side image support E_r° for the three original source LINE factor images of center and neighbors. Thus all genuinely GOOD two-typed opposite source wedges are EXACTLY all original source-opposite triples of #560 restricted to CLEAN induced graph support on BOTH typed sides; there is no extra per-pair criterion omitted.

## 3. True-original fixed-f GOOD source potential and exact quenched factorization

Fix any genuine original point map f and center real incidence (p,l). Restrict possible outer TRUE original point factors q0,q1 to those whose pair images share the first and second respective point center physical endpoints while f(p),f(q0),f(q1) all belong to E_f°. Because f is a FULL injection, q0≠q1 and both differ from p. Choose actual original incident source LINE factors k0,k1 via q0 and q1 with k0≠l,k1≠l,k0≠k1. There are no invented source incidences.

Let B_good(f) be the number of such genuine original centered 3-incidence tuples across the full true W(3,s). A TRUE W(3,s) source point has exactly d original LINE neighbors. After excluding l and previously chosen k0, for each clean physical opposite pair of outer original points, at least (d−1)(d−2) genuine original source line choices remain. Each occupied clean physical center edge {u,v} has (deg°u−1)(deg°v−1) ordered opposite point-port physical outer edge pairs, and each original point p is a center of exactly d genuine original flags. Therefore

\[
\boxed{B_{\mathrm{good}}(f)\ge d(d-1)(d-2)T_\circ(E_f).}
\]

Choose ONE uniformly random COMPLETE globally injected right original LINE source-factor bijection g onto E_r. Each fixed triple (l,k0,k1) of different original LINE factors has a UNIFORM ordered triple of distinct physical occupied right edges; because the globally bad line vertices depend only on the occupied right support, the number of favorable ordered triples is exactly 2 T°(E_r), NOT T(E_r) and NOT a separately sampled per-original-wedge event. Thus the EXACT conditional quenched identity

\[
\boxed{
\mathbb E_{g:\mathrm{im}(g)=E_r}
R_{\mathrm{GOOD,opposite}}(f,g)
=\frac{2 B_{\mathrm{good}}(f)T_\circ(E_r)}
{V(V-1)(V-2)}.
}
\]

Every source wedge appearing in R_GOOD has THREE actual source point and THREE actual source line factor IDs and three distinct TRUE original incidence IDs. This agrees definitionally with the previous exact GOOD 2×2 physical four-cell original D graph wedge count R=Σ_i(x00x11+x01x10) from #543/#556, not the broader ALL-D R of #560.

No independence between two wedges, point/line source maps, or six-ID motifs is asserted; linearity of expectation suffices.

## 4. Universal clean physical support energy lower for h≥5

Let s=2^h≥32. Then the minimal true physical alphabet a≥261, m≤a−2 and b=|Bad(E)|≤31. Take any t=a−31 CLEAN coordinate symbols. Then t≥230≥128, t≥a/2, and m≤2t. The induced occupied graph on those t clean physical coordinates has at least binom(t,2)−m actual occupied pair edges. Expanding the rooted two-port products and dropping nonnegative missing-degree products exactly as in #560 yields

\[
T_\circ(E)\ge
\Bigl(\binom t2-m\Bigr)(t-2)^2
-2m(t-1)(t-2).
\]

For t≥128 and m≤2t, the following universal rational inequalities hold:

\[
\binom t2-m\ge\frac7{16}t^2,\qquad
(t-2)^2\ge\frac9{10}t^2,\qquad
2m(t-1)(t-2)\le 4t^3\le\frac{t^4}{32}.
\]

Consequently the lower is at least (7/16·9/10−1/32)t^4 > t^4/4. Since t≥a/2 and the minimal palette satisfies a(a−1)≥2V (hence a²≥2V),

\[
\boxed{T_\circ(E)\ge\frac{t^4}{4}
\ge\frac{a^4}{64}\ge\frac{V^2}{16}.}
\]

Every inequality applies to ANY globally occupied typed physical image support E of size V, no assumed geometry of holes, no required physical coordinate permutation automorphism, and no stochastic assumption.

For h=1..4 this particular robust all-h argument is NOT claimed; in small palettes a bad-coordinate vertex may consume a large fraction of physical coordinates. Even though exact finite original W32/W34 GOOD samples are available, do not extrapolate them to a universal lower at small h without a separate proof.

Combining both globally fixed typed support clean energy floors with the exact quenched identity,

\[
\begin{split}
\mathbb E_g R_{\mathrm{GOOD,opposite}}(f,g)
&\ge \frac{2d(d-1)(d-2)T_\circ(E_f)T_\circ(E_r)}
{V(V-1)(V-2)}\\
&\ge \frac{d(d-1)(d-2)V}{128}\\
&\ge\boxed{\frac{s^6}{128}},\qquad s=2^h\ge32.
\end{split}
\]

The last inequality is exact algebra, since d=s+1 and V=(s+1)(s²+1), and

\[
d(d-1)(d-2)V=s\,(s+1)^2(s-1)(s^2+1)
=s\,(s^5+s^4-s-1)
\ge s^6\quad(s\ge2).
\]

**Mathematical status:** uniform-in-f-and-right-support lower on the EXPECTATION over a whole globally random other g, NOT a fixed-g deterministic R_GOOD lower; this theorem does not prove \(\inf_{f,g}S_s(f,g)\ge c s^6\).

## 5. Two independent types of original-source falsifiers

Four additive research files: source code, independent nine-group tests, this mathematical proof, and a GitHub-hosted dedicated workflow.

1. Independent literal real W32 S68/S72/lex/reverse 45 actual source incidence flags and real symplectic GF4 W34 lex/random 425 actual source incidence flags; enumerate TRUE original clean point-opposite three-source-flag events independently of the combinatorial formula, using real neighbor original LINE source IDs. No artificial fake large W3 incidence graph.
2. Calculate physical Bad(E) and induced clean support T° from scratch by full K_a set subtraction, independent of the source helper and previous AA4-AO logic. Explicitly check for BOTH typed support images.
3. Independent FULL ordered right physical support triple enumeration: 15×14×13=2730 true original W32 K6 physical choices and 85×84×83=592620 true original W34 GF4 nononto K14 choices, with all three different original LINE source indices represented by distinct physical images and all three pair edges in induced clean E°. Compare count to 2T°/V(V−1)(V−2). No mistaken 2T°/(|E°|)_3 denominator.
4. Independently count the actual fixed-g original three-flag physically GOOD opposite wedges from the previous colored true-original D graph (two complementary typed colors, source flags distinct) and separately from its literal original pairwise source-ID wedge reference. Test the exact distinction between mean over global g and given arbitrary fixed g; no pointwise inequality against expectation is asserted.
5. h1..34,40,48,64,80 exact integer dyadic supports and closed-form good floor h≥5; adversarial physical missing pair-edge configurations including star-shaped holes for genuine s=32 physical K261; exact whole original LINE factor swapping / independent global physical RIGHT coordinate relabel invariance of support-based expectation; reject malformed physical injection.
6. Compare the expected GOOD-only count to the broader exact ALL-D mean from #560, verifying the GOOD subset expectation is no greater. Do not treat GOOD original threeflag count as accepted historical GF5 sixflag Q count.

### Prior-art boundary and what remains

Global random permutation ordered-marginal formulas and missing-edge union bounds are standard; no broad originality claim or independent external prior-art novelty verification is made. The #538/#543 globally bad/GOOD original port definitions, #554 true original four-bin incidence tensor, #556/#557 local sharp twoport minority theorem, #559 mixed-cell source caps, #560 broader ALL-D global right average, and #544 original GF5 D6 stochastic result remain credited.

**The fundamental deterministic source geometry hole remains:** the given f,g may align their respective globally good original point/line physical port minority supports so that few center source flags have both, even when the quenched expectation is ≥s⁶/128. Nothing above bounds \(\sum_{i\text{ original}}\min P_i\min L_i\) below at the given global pair. In the genuine W34 random example the observed GOOD physically opposite count is just 10, despite many ALL-D opposite wedges, illustrating sharp sensitivity to coordinated source/physical labeling. Additional original source 3×3 residual Hall and seven-positive-GF5 six-incidence acceptance remain separate barriers. Root #230 Branch A/B/C OPEN_WITH_FORMAL_BLOCKER, no R3/ASET exponent, independent mathematical referee needed, keep Draft unmerged.

**Next proof-relevant direction:** seek a TRUE original fixed-f,g relative-deviation bound or combinatorial anti-alignment constraint for the GOOD port minority-product that uses jointly coherent W(3,s) incidence structure. A concentration/mean calculation alone, even for GOOD, cannot establish a lower for every adversarial g; generic bounded differences are not claimed to bridge the missing quantifier.


## 6. Exact TRUE ORIGINAL finite GOOD versus mean regression witnesses

The first clean corrected source HEAD [dedicated GitHub-hosted run #38887677561](https://github.com/definitely-stable/Mathlab/actions/runs/38887677561) completed BOTH mathematical jobs **SUCCESS**. An initial earlier HEAD failed because the source point center p occurs in both physical port candidate lists; the algorithm was corrected to SKIP p in both lists before enumerating outer original point factors. This was an actual source enumeration implementation bug, not an issue with the theorem's exclusion condition, and tests independently verify its correction. The final HEAD then hard-pins five exact rational observed versus globally-quenched evidence rows.

All rows: a genuine original source W(3,s), ONE globally complete point physical map f held fixed, ONE globally complete original line g in the "given" column, and a truly global random original line map g' sharing exactly g's occupied physical edge support for the mean. The historical #543/#556 TRUE ORIGINAL GOOD D edge definition is used, and the present theorem is for the physically *opposite* pair of its two original D neighbors at a source flag center.

| Genuine original typed physical f,g fixture | Actually given ORIGINAL fixed-g GOOD opposite R(f,g) | Exact E over ONE complete globally sampled original right g' | Right induced clean physical port energy T°(E_r) |
|---|---:|---:|---:|
| W32 S68 | 697 | 87056/91 (~956.66) | 240 |
| W32 S72 | 750 | 87056/91 (~956.66) | 240 |
| W32 lex | 1,105 | 88992/91 (~977.93) | 240 |
| W34 lex (true GF4, nononto K14) | 3,544 | 4784352/1411 (~3,390.75) | 2,880 |
| W34 random (true GF4, nononto K14) | 10 | 87376/9877 (~8.85) | 240 |

The exact right sample space under original W32 is all 15·14·13=2730 ordered distinct image edge triples of a complete global g'; under true original W34 it is 85·84·83=592,620 ordered triples on a global right image set with six missing physical K14 edge labels. The independent tests literally enumerate every triple; the expected count is an exact rational finite sum rather than Monte Carlo or resampling individually per original source Q.

**Scientific caution:** for the SAME real original W34 random global fixture the much broader ALL-D fixed source 3flag opposite count is 46,996 and its quenched whole-g mean 131596825/2822 (~46,633), but the strictly GOOD opposite wedge count at the ACTUAL fixed original g is only 10 and its corresponding mean is <9. This is a direct genuine-original finite illustration of the essential physical BAD-coordinate/GQ label-placement loss, not an all-h counterfamily. The h>=5 result proves a good-expected-value lower uniformly for arbitrary original f and right support but does not elevate it to a fixed adversarial original g lower. The h=2 example is outside the all-h-large ≥s⁶/128 proof range; its exact positive small-h expectation is evidence only.

The final source/test/code/proof stack independently checks dyadic h=5..80 symbolic integer support floors, actual source line neighborhoods, literal source-point 3flag enumeration, entire ordered right physical edge triples, typed physical right-coordinate relabel invariance, adversarial physical missing-edge shapes, and independent fixed-g genuine original GOOD two-port tensor wedge identity. Full CI success on exact final SHA and separate independent mathematical referee acceptance are still needed; no original selected six-ID GF5 R3 or root #230 Claim A/B/C promotion.
