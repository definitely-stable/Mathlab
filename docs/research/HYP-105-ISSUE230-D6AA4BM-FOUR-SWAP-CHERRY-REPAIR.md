# HYP-105 / #230 — AA4-BM: four-swap original pinned-cherry B/A repair

**Scientific DRAFT; strict child** of [AA4-BL #577](https://github.com/definitely-stable/Mathlab/pull/577), frozen parent SHA `749a9c1cafb0eea32bdd7e1c866c099004bf8ae6`. Not merged; no canonical claim-registry promotion. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**.

## Scope, prior art and why this step

The strongest root target is still the *fully fixed* all-seven-GF5 seven-class lower `inf_(f,g) S_s(f,g)=Omega(s^6)`. The current #576/#577 conditional cherry results hold after globally reallocating other original opposite factor images, **not** for the adversary's original fixed map. #548/#547 previously gave distinct five-swap D6 repair routes; #570/#571 constructed selected D6 under adaptive global injection. This slice does **not** invent the classical greedy transposition mechanism or claim a universal minimax result. It translates the exact TWO-ROOT-PIN B/A transfer of #577 into a deterministic **radius-4** witness for every *pin-regular* original cherry without moving its two pinned opposite source IDs, and counts many distinct repaired complete maps per cherry.

## Exact theorem: every fixed original f,g, every pin-regular rooted cherry

For **every** integer `h>=5`, let `s=2^h`, `d=s+1`, `V=(s+1)(s^2+1)`, and `a` the least integer with `binom(a,2)>=V`. Work in the **genuine original symplectic** `W(3,s)`, with its actual bipartite original incidence IDs, physical pair alphabet `E(K_a)` and **two complete globally injective maps** `f` (original POINT factors) and `g` (original LINE factors). Their physical supports are allowed to be adversarially correlated.

Fix **any** TWO distinct TRUE original flags `alpha=(p,l1)` and `beta=(p,l2)` through the same actual original point `p`. Write `e_i=g(l_i)` and `E=im(g)`. Let `Delta_pin` be the maximum missing physical-pair degree of physical coordinate endpoints in `e1 union e2`. Assume exactly the already-known [#577 BL-LOCAL condition](https://github.com/definitely-stable/Mathlab/pull/577):

```
Delta_pin <= floor((a-4)/8).
```

Then **there exists** a new complete, globally injective original LINE physical map `g_prime` with **the exact same occupied edge support E** such that:

1. `g_prime(l1)=g(l1)` and `g_prime(l2)=g(l2)` (the two actual source-line images are NEVER modified);
2. `g_prime` is obtained from the arbitrary fully fixed input `g` by at most **FOUR transpositions of images of ORIGINAL LINE factor IDs** (not swaps of physical coordinate endpoints);
3. some set `Q` of **exactly SIX distinct genuine ORIGINAL incidence IDs** containing `alpha,beta` has physical point projection of class B/C4 under **unchanged** `f`, physical line projection of class A (connected C6 or two disjoint triangles) under `g_prime`, and the same true original six IDs on both sides. Thus `Q` belongs to the historical accepted positive six-coordinate GF(5) **B-left/A-right** class.

Moreover, writing `T_A(E;e1,e2)` for the **UNORDERED** occupied six-edge physical 2-factors on six distinct right coordinates containing both pinned edges, at least

```
4! * T_A(E;e1,e2) >= 12*(a-4)*(a-5)
```

**distinct** entire complete global maps `g_prime` satisfying (1)–(3) lie in the (unrestricted transposition) Cayley ball of radius four around this **given original g**. There is a dual statement for genuine original LINE-rooted cherries with the physical POINT map modified and two original point images pinned.

### Proof

First, the strict parent [#576](https://github.com/definitely-stable/Mathlab/pull/576) gives, for **each** original cherry, an actual original six-distinct flag source pool `N_BA>=C4_p(f)*(d-2)_4>0`. The actual four non-root point images form an occupied physical C4 outside the two coordinates of `f(p)`; four additional genuine original flags can be chosen with all six actual opposite LINE factors pairwise distinct (including `l1,l2`). Choose **one** such sixflag `Q` once and for all. This first-side source witness is independent of subsequent changes to the other map.

Second, the strict parent [#577](https://github.com/definitely-stable/Mathlab/pull/577), under precisely the local physical hole degree condition stated above, proves `T_A(E;e1,e2) >= (a-4)(a-5)/2 > 0`, for both **adjacent and disjoint** pinned physical edges. In every target `F`, the two pinned physical edges are already attached to the two distinct pinned original line IDs, and there are exactly **four other different occupied physical edges** in `F` to assign to the remaining **four actual original LINE factors** of `Q`. There are `4!=24` assignments per `F`.

Fix one assignment of these four nonpin targets to their genuine original line IDs. Maintain a reverse table for the **entire fixed complete map g**. Process the four requested source IDs in order. For a requested ID `l` and occupied target image `e`, find the original source ID `l_prime` presently carrying `e`. If `l_prime!=l`, swap their images and update the reverse table. Prior requests stay fixed: their assigned images are pairwise distinct, so the current owner of a not-yet-requested target cannot be an earlier fulfilled source ID. Neither anchored `l1` nor `l2` can ever be touched because their two images are distinct from all four target images. At most four transpositions produce the entire **still bijective** `g_prime`, with the original support, both original pin images, and all six true original factor IDs. The resulting same `Q` has both required physical projections. This is a **deterministic** proof, requiring no independent re-randomization per Q and no source label automorphism.

Finally, keep that single genuine original `Q` fixed. Each physical six-edge set `F` and one of its `24` assignments specifies a **different ordered four-image tuple** on the same four actual source LINE factors, hence a **different whole globally injected g_prime**. Therefore there are `24*T_A` pairwise distinct, reachable accepted maps; apply the #577 `T_A` bound to get `>=12(a-4)(a-5)`. These are maps that may vary with the selected actual cherry. No positive count on the *input* g follows.

### Deterministic majority corollary for an arbitrary fixed entire pair f,g

[#577 BL-MAJ](https://github.com/definitely-stable/Mathlab/pull/577) proves that, for **every** already fully fixed original `g`, **strictly more than 3/4** of all actual original point-source cherry roots have `Delta_pin<=floor((a-4)/8)`. Therefore **each** of these more than 3/4 actual original cherry roots admits `>=12(a-4)(a-5)` distinct complete right maps reachable by at most four image transpositions, preserving that root's exact two original opposite pins, and having one genuinely accepted six-incidence-ID B/A motif through the root. The same dual holds for each fixed original `f`.

**Quantifier warning:** `forall (f,g), forall good root, exists a root-dependent g_prime`; it is **NOT** `forall (f,g), exists one g_prime handling all roots`, and much less `forall (f,g), S_s(f,g)>=c*s^6`. If different roots require incompatible repairs, this theorem does not resolve their competition. In particular, the original `g` can still have zero rooted B/A count.

## Independent oracle and falsifiers

`research/hyp105_issue230_d6aa4bm_four_swap_cherry_repair.py` implements source-ID-preserving swaps and an **independent physical A-target enumerator**. `research/test_hyp105_issue230_d6aa4bm_four_swap_cherry_repair.py` tests: (i) all dyadic h5..80 rational/integer exact inherited two-pin and majority inequalities (no fabricated high-order source GQ); (ii) independent K6 adjacency/disjoint physical `T_A=7/14` versus parent #577, testing **all 24T** distinct repaired full global maps for one fixed source ID set; (iii) actual original symplectic W32 on five independent complete typed f,g schemes and true original source sixflag Q; (iv) genuine GF4 W34 nononto K14 on both typed sides; (v) abstract pendant-edge physical obstruction and invalid/disallowed pin choices. Tests verify the **unchanged true original six incidence IDs**, six **different opposite original factor IDs**, globally injected original support, actual unchanged pinned factor images and postrepair two-regular physical opposite coordinates. A source pool having no Q is reported as no witness, not silently synthesized.

Passing these checks does NOT independently prove the inherited all-h #576/#577 lemmas and does not constitute scientific acceptance. The root #230 Branch A/B/C stays OPEN_WITH_FORMAL_BLOCKER. Before merging the Draft, require exact final-HEAD CI on GitHub-hosted runners, parent ancestry and independent proof audit, including review of #576/#577.

## Relation to literature

The transposition construction is a standard permutation argument. The original geometry and source-factor distinctness come from the preceding repository slices. Adjacent prior art includes the root's earlier [five-swap six-source-ID repair #548](https://github.com/definitely-stable/Mathlab/pull/548) and general work on constrained permutations. The scoped claim is a new **combination and quantified application inside this research chain**, not a priority claim against wider graph-repair or permutation literature.

**Next root-facing missing lemma:** control joint interference/repair concentration across **all** actual source cherry roots while keeping the SAME originally adversarial g fixed; convert many individually repairable radius-4 witnesses into an unavoidable positive original seven-GF5 S **or** a rigorous fully correlated infinite counterfamily. No R3/ASET exponent is claimed.
