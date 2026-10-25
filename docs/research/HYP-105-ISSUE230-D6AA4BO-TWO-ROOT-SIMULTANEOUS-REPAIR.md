# HYP-105 / #230 — AA4-BO: simultaneous repair of TWO genuine original source cherries

**Scientific DRAFT.** Strict child of [AA4-BN #580](https://github.com/definitely-stable/Mathlab/pull/580), frozen exact parent HEAD `3bed5dd6f38c82821255fd7658463d89ecb74270`. [Parallel #581](https://github.com/definitely-stable/Mathlab/pull/581) concerns improved **individual** three-image-swap repair only for h>=22, not the two-root theorem here. The underlying one-root four-swap constructions [#578](https://github.com/definitely-stable/Mathlab/pull/578)/[#579](https://github.com/definitely-stable/Mathlab/pull/579), two-pin physical support [#577](https://github.com/definitely-stable/Mathlab/pull/577), actual source C4 Hall lemma [#576](https://github.com/definitely-stable/Mathlab/pull/576), and exact partial matching swap completion #580 are explicitly prior and indispensable.

## Why this slice

AA4-BN gives iff compatibility and minimum transposition distance for PRESELECTED original rooted-Q assignments, but no existence theorem for compatible candidates belonging to two distinct roots. AA4-BO constructs those candidates **for ANY selected pair** among the genuine source roots that satisfy the unchanged full original map's physical BL-LOCAL condition, without assuming two independent globally assigned opposite maps. This is the first nontrivial quantified cross-root compatibility guarantee in this slice chain. Do not infer it is the first such result in all mathematical literature.

## Theorem BO-2ROOT (all true symplectic W3, all dyadic h>=5)

For every `s=2^h`, `h>=5`, the **actual** symplectic generalized quadrangle `W(3,s)` with `V=(s+1)(s^2+1)` original factors per side, original incidence flag IDs `I={(p,l):p incident with l}`, physical pair-edge alphabet `E(K_a)` with minimal `a` satisfying `binom(a,2)>=V`, and **EVERY ALREADY COMPLETELY FIXED**, possibly adversarially correlated, globally injected original POINT and LINE physical pair maps `f,g`, fix ANY TWO DISTINCT genuine original POINT-root cherries

```
r_i = (alpha_i=(p_i,l_i1), beta_i=(p_i,l_i2)), i=1,2,
```

where the two actual original LINE factors `l_i1 != l_i2` have already fixed physical pair images `g(l_i1),g(l_i2)`. Assume for each root, every endpoint of BOTH of its two opposite pinned images has at most `floor((a-4)/8)` absent incident physical edges in the occupied support `E=im(g)`. Shared original pinned LINE factors are allowed across the two roots.

Then there exists **ONE SAME complete globally injected original LINE-factor physical map** `g_prime`, obtained from the *given* global `g` by **at most 8 transpositions of whole ORIGINAL LINE-factor pair images**, satisfying all of the following, simultaneously:

1. `f` unchanged, `im(g_prime)=im(g)`; global original factor injection and fixed physical support hold at **every intermediate permutation**.
2. **ALL actual original LINE-factor pinned images** in the union `P={l_11,l_12,l_21,l_22}` remain unchanged at every intermediate permutation.
3. There are TWO DIFFERENT six-element sets `Q_1,Q_2 subset I`, each consisting of **six DISTINCT genuine original incidence IDs**, containing the EXACT original two rooted flag IDs of its chosen cherry, with first physical B/C4 profile under unchanged f and opposite simple A/C6 profile under the SINGLE g_prime.
4. Hence BOTH distinct original Q are accepted historical positive six-coordinate GF(5) B-left/A-right motifs under this SAME final fixed `f,g_prime`.

Genuine LINE-source cherry / global POINT-map dual holds by symplectic W(3,s) point-line duality. Original source point roots may share source point factors; original line roots may share pinned opposite original factor IDs; no `Sp(4,s)` symmetry of arbitrary physical maps or cross-root probabilistic independence is assumed.

**Quantitative majority consequence:** #577 BL-MAJ establishes for every already fixed `g` a good set of source point cherries of cardinal `G > (3/4)N`, where `N=V binom(s+1,2)`. EVERY unordered pair of distinct good cherries admits the above single-map joint repair. Therefore the fraction of distinct source point cherry root pairs admitting **some** common <=8-swap pinned repair exceeds

\[
\frac{(3N/4)(3N/4-1)}{N(N-1)}
=\frac{9N-12}{16(N-1)}>\frac12,\qquad N>4.
\tag{BO-MAJ-PAIR}
\]

The same dual bound holds for LINE-rooted cherry pairs. This bound counts **pairs of roots with possibly pair-dependent correction maps**, NOT distinct positive root pairs in the original unchanged g and NOT one globally repaired g_prime satisfying all good roots.

## Proof of BO-2ROOT

**Step I: actual original source sixflags with mutually disjoint free opposite factor IDs.** Let `d=s+1>=33` and `P` contain at most four genuine original pinned opposite factors. From parent #576: for *every* original cherry and arbitrary fixed first-side f, there exists a real occupied physical C4 on four different coordinates disjoint from the two physical coordinates of the original source root. Under global injectivity, these four C4 edges correspond to FOUR DIFFERENT genuine original POINT factor IDs distinct from the root. Each such source factor lies on EXACTLY d true original LINE factors. Choose one genuine incidence flag at each of these four points. For `Q_1`, avoid ALL ≤4 pinned opposite source factors and prior selected free opposite source factors (≤3); at most 7 banned choices per step, so `d>=33` suffices. For `Q_2`, additionally avoid the four free original LINE factor IDs used in `Q_1`, for a maximum of 4+4+3=11 banned IDs at any step, still <d. Every chosen Q includes its two fixed true original cherry incidence IDs, has exactly six DISTINCT source incidence flags and **six different actual original opposite LINE factors**. Its true original point-root B physical profile is unchanged. The two four-element sets of *free* original LINE factor IDs are disjoint from each other and from the union P. Therefore `Q_1 != Q_2`, even if the original two rooted cherry pairs share one source LINE factor.

**Step II: physical double-root connected C6 targets with mutually disjoint nonpin images.** Let `E=im(g)`, `m=binom(a,2)-V<=a-2`. The parent #577 physical argument proves a supply of **physically occupied** connected six-edge six-vertex C6 containing ANY BL-regular pair of distinct pinned edges. For two adjacent pins u-v,v-w, the fixed rooted orientation `u-v-w-x-y-z-u` survives with at least

\[
L_{adj}=\frac12(a-3)(a-4)(a-5)
\]

occupied ordered-triple targets (injection into distinct physical undirected C6). For disjoint pins u-v,w-x the fixed orientation `u-v-y-w-x-z-u` survives with at least

\[
L_{dis}=\frac12(a-4)(a-5).
\]

Now forbid at most `t<=6` OTHER fixed physical occupied pair edges `F`, none of which is one of the two root pins. In the first canonical rooted orientation an arbitrary forbidden edge can appear in at most `(a-4)(a-5)` ordered triples: if incident to u or w as an external edge it fixes one new vertex, and if wholly among the three free vertices it eliminates ≤4(a-5) options, which for a>=261 is smaller. In the disjoint orientation, every nonpin edge has one endpoint among the four pinned-coordinate vertices and one among two new vertices, so one forbidden edge excludes at most `a-5` ordered pairs. Hence at least

\[
\begin{aligned}
L_{adj}(t)&\ge (a-4)(a-5)\bigl((a-3)/2-t\bigr)>0,\\
L_{dis}(t)&\ge (a-5)\bigl((a-4)/2-t\bigr)>0
\end{aligned}
\tag{BO-AVOID}
\]

for a>=261 and t<=6. This **does not** require any local regularity beyond the already assumed #577 BL-LOCAL condition on EACH root.

Choose first an occupied physical C6 target `T_1` through the first root's two original right pin images, while **excluding the second root's physical pin images that are not shared** (at most two forbidden edges). Then choose a second occupied physical C6 `T_2` through the second root's two pins while excluding `T_1` minus any physical edge equal to one of those second-root pins (at most six forbidden edges). The choice is possible by BO-AVOID, and it guarantees

```
(T1 minus its own pinned edges) ∩ (T2 minus its own pinned edges) = empty,
(Ti minus its own pinned edges) ∩ physical images of all P = empty.
```

Thus the two **sets of four free target physical pair edges** are disjoint from each other and from all pinned physical images, independent of correlations in the input original g.

**Step III: ONE globally coherent simultaneous assignment and <=8 source-factor image swaps.** Pair four free distinct source LINE IDs of each genuine Q with that root's four free target edges. Step I and II guarantee a globally injective partial request map on at most eight different original LINE factor IDs, with no requested physical edge owned by a protected pinned source factor and no cross-root source/target conflicts. Apply prior exact AA4-BN #580: all these requests admit one complete global injection `g_prime` with identical right occupied support, all P pinned, and exact minimal Cayley transpositions `k-c <= k <=8`. Each intermediate step is a genuine permutation of full ORIGINAL LINE-factor images and retains all pinned images. The historical accepted GF5 B/A test on BOTH unchanged actual original six-incidence-ID Q succeeds in that **one** final global map, because each second projection is the prescribed connected physical C6 and each first projection the unchanged true source B/C4. There was no independent choice of g per Q.

**Step IV: source pair majority.** Apply #577 BL-MAJ's **deterministic** >3/4 bound on genuinely original source cherry pin-regularity for EVERY entire fixed g, then count \(\binom G2\) pairs. Since `N>=V*binom(33,2)>4`, the rational bound above is strictly >1/2. Note that picking two distinct original cherry pairs does not imply their actual source flags have disjoint point/LINE factors; the proof explicitly tolerates shared true opposite pins.

## Reproducible falsifiers and limits

Research implementation: `research/hyp105_issue230_d6aa4bo_simultaneous_cherry_repair.py`. Tests in `research/test_hyp105_issue230_d6aa4bo_simultaneous_cherry_repair.py`; three hosted jobs. They verify (i) all-h h5..80 exact signed integer/Fraction lower bounds for both adjacent and disjoint physical roots after six adversarial additional forbidden edges; (ii) independent physical connected-C6 target enumeration on K7/K8 and explicit pendant-edge negative physical support; (iii) actual symplectic W32 all five original globally injected schemes with genuine incidence-Q IDs and strict guards; (iv) actual symplectic GF4 W34 nononto K14 lex/random and BOTH typed sides with one same repaired full global map accepting two original Q; (v) literal replay of all factor-image transpositions with pin protection at **every** stage; and (vi) explicit rejected fake roots/model assumptions. Finite h1/2 are only negative/positive oracle fixtures, **not** substitutes for original high-order W3 geometry or proofs.

**CRITICAL NONIMPLICATIONS:** The input, **unchanged** fully fixed adversarial `f,g` may have zero accepted B/A (and potentially other classes), and different selected root PAIRS may require mutually incompatible corrected maps. This theorem proves `forall(f,g) forall good distinct root pairs (r1,r2) exists g'_{r1,r2}`; it does **NOT** prove `forall(f,g) exists g' repairing a positive fraction of roots simultaneously`, nor `inf_{f,g} S_s(f,g)=Omega(s^6)`, nor Branch B counterfamily or all-seven full-R3/ASET exponent. It does not meet the root #230 Branch C spectral/rank/cell-probe gate; keep `OPEN_WITH_FORMAL_BLOCKER` and Draft until independent mathematical review and exact-head CI.

**Next actual root-facing step:** find a nontrivial lower bound on a *single* globally corrected map's number of simultaneously accepted original roots, using bounded-degree repair conflicts and actual original W3 intersection combinatorics, or prove an admissible high-h obstruction. Pairwise repairability alone does not imply global Helly, concentration or unchanged-map positivity.
