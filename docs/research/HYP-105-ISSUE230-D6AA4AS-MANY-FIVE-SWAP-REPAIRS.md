# HYP-105 / issue #230 — AA4-AS: polynomially many deterministic GLOBAL D6 repairs

**Status:** research-only partial theorem; independent mathematical referee has NOT reviewed it. Strict scientific child of [AA4-AR PR #545](https://github.com/definitely-stable/Mathlab/pull/545). All source geometry is the ACTUAL original symplectic W(3,2^h); f and g are arbitrary full globally injected original point/line factor physical unordered-pair maps; all six source incidence IDs and their original point and line factors are different. Root issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Main theorem — ALL h>=1, EVERY adversarial f,g

Let s=2^h, V=(s+1)(s²+1), d=s+1, and a the smallest integer with K=binom(a,2)>=V, m=K−V<=a−2. Denote by B5(g) the finite set of complete original-line physical pair assignments obtained from the **original given g** by at most FIVE transpositions exchanging images of TWO distinct actual original LINE factors at each step. Every such right global map has exactly the same occupied physical pair-image support as g.

**Theorem.** For EVERY genuine symplectic W(3,s) and EVERY complete global f,g, there exist a SINGLE six-DISTINCT-ORIGINAL-incidence Q and ONE selected original line factor l0 in Q such that at least

\[
\boxed{(a-2)_4\ge \frac14s^6}
\]

**pairwise DIFFERENT full global right maps** g' belong to B5(g), preserve g'(l0)=g(l0), and accept **this SAME fixed actual original Q** in the historical positive seven-GF(5) D6 class under (f,g'). The same statement for repairing the original point map f, holding g fixed, follows from genuine W(3,s) point/line duality.

These maps are full injections and one and the same map g' is shared across all original Q; there are no artificial independently assigned physical pairs and no duplicate six-Q certificate counting. **This is NOT** D6(f,g)>0 at the original adversarial g, not inf S_seven(f,g)>=c s^6, not Branch A/B/C and not an ASET exponent. The radius-five transposition ball is much larger than s^6; no constant fraction of that ball is claimed.

## 2. Robust physical edge-cycle lemma

For every occupied physical right edge e in the simple graph H=(a coordinate vertices, im g), let c(e) be the number of undirected connected simple physical C6 containing e. An edge e in the AMBIENT complete K_a lies on exactly

A=(a−2)_4

six-coordinate C6s: orient its fixed endpoints u→v and choose the ordered remaining four coordinates. Call an occupied e **robust** when c(e)>=A/2.

Every one of the m missing pair edges h destroys exactly A ambient physical C6s. Each destroyed ambient C6 contains at most SIX occupied edges, so double counting its anchored-edge losses yields

\[
\sum_{e\in\operatorname{im}g}(A-c(e))\le6mA.
\]

Every nonrobust e loses strictly more than A/2; hence the number b of nonrobust occupied physical pair labels satisfies b<12m (we use the weaker b<=12m in estimates). Because original g is ONE injective source-line map, these labels have precisely b distinct preimage actual original LINE factor IDs. Let B be that genuine original line set.

## 3. True original GQ incidence regularity transfers bad lines to bad points

Let P_bad be actual original POINT factors p whose *entire d-line neighborhood of genuine original source incidences* is contained in B. Each actual original line has exactly d incident original points; the bad lines jointly support exactly d|B| genuine original incidence IDs. Every p in P_bad consumes its own d different incidences. Therefore

\[
|P_{\rm bad}|\le |B|\le12m.
\]

This is a deterministic consequence of actual W(3,s) regularity; it never relabels the source independently for different six-Q.

## 4. An occupied physical left C6 with at least one robust right-line anchor

All ambient physical K_a simple undirected C6s number (a)_6/12=KA/6. Each physical edge lies on A such cycles. The global f image has m missing physical edges. Additionally remove the at most 12m occupied left physical edge images f(p) for genuine original p in P_bad. After these deletions the lower number of cycles is

\[
C_{\rm clean}\ge(a)_6/12-(m+|P_{\rm bad}|)A
\ge A(K/6-13m).
\]

For true symplectic powers h=1,2,3,4 the minimal physical alphabet pairs (a,m) are exactly (6,0), (14,6), (35,10), (94,2). Every one satisfies m<=(a−2)/2, so **every** occupied right edge is already robust by the anchored-edge missing-edge union bound: at most m(a−3)_3 physical C6s through e are deleted, versus A=(a−2)(a−3)_3 available in the full K_a. For a=6 the image is full K6. Thus P_bad is empty and f has at least one occupied physical C6.

For every h>=5, s>=32 gives a>=261 by exact integer V>binom(260,2). For all a>=261 the elementary polynomial inequality K=a(a−1)/2>78(a−2)>=78m holds, so K/6>13m and C_clean>0. These two branches cover **ALL original h>=1**, not a finite-sample asymptotic fit.

Choose ONE surviving actual physical C6 on six distinct point physical pair edges of im f. Its inverse images through the ONE injective f give six genuinely different original point factors p0,...,p5, none belonging to P_bad. Hence at least one of the actual original source lines through p0 has a robust right physical g-image; call that original line l0.

## 5. Actual original source Hall matching and many global repairs

The real symplectic original incidence bipartite graph is connected, d-regular, with V factors on both sides. For every nonempty proper original point subset X, the strict Hall inequality |N(X)|>=|X|+1 follows from regularity and connectedness: equality would force X union N(X) to be a full connected component. Delete only the already chosen original line l0 from the neighbor sets of p1,...,p5. Every subset retains Hall, so choose five different actual original incident line factors l1,...,l5 distinct from l0. Thus Q={(p_i,l_i):i=0,...,5} consists of six genuine different original incidence IDs, six different point IDs, six different line IDs, and the physical fixed-f left six-column dual is a connected C6 in this same incidence-column order.

The physical right edge e0=g(l0) is robust, so it belongs to >=A/2 different undirected physical C6s entirely inside the **fixed physical support of g**. Each such cycle admits TWO different cyclic orientations with its first unoriented physical pair edge equal e0: (e0,t1,t2,t3,t4,t5) and (e0,t5,t4,t3,t2,t1). They give DIFFERENT ordered physical pair targets on the six **original LINE factor IDs** l0,...,l5, and two different cycles also give different targets.

For each ordered right physical cycle, leave g(l0)=e0 untouched; sequentially swap the current images of actual original lines l1,...,l5 with the unique original line factor currently carrying the next target pair edge. Distinct six target physical edges guarantee no previously corrected source-line assignment is disturbed. This realizes the desired six physical right cyclic edge positions in at most five entire-global-line-image transpositions and preserves im g unchanged. The same six real original incidence positions have identical connected column duals on both physical sides. Hence the historical positive GF5 D6 accepts Q for that global g'.

Different ordered physical right cycles give different right pair-image values on the same six original line IDs and hence different complete full global maps. The count is at least 2*(A/2)=A=(a−2)_4. QED.

## 6. Explicit uniform bound in powers of s

For s=2, a=6 and A=24>=s^6/4=16. For s>=4, a>=14 and a²>=2V>=2s³. Then

\[
(a-2)_4\ge(a-5)^4\ge a^4/8\ge s^6/2\ge s^6/4.
\]

The second inequality is 8(1−5/a)^4>=1, monotone for a>=14, valid at a=14 because 8*9^4>14^4. All computations are exact integers, with no floating-point or fake high-h symplectic geometry.

## 7. Exact reproducible falsifiers

The versioned program in the research directory computes each exact all-h formula using true dyadic s. Independent tests:

- literal physical C6 enumeration in K6–K10 confirms exact anchored cycles A, sixfold global physical edge-C6 incidences, and double-count identity; randomized/adversarial missing-edge K10 checks global loss-mass bound and number of nonrobust edges via independent physical graph DFS;
- true W32 S68/S72 global point/line map pairs independently have D6(f,g)=0 on ALL 21,186 original source left-C6 six-ID Q; each has exactly 48 distinct globally legal five-swap-or-fewer positive D6 repaired right maps for one and the same original six-ID Q, checked via historic W32 GF(5) seven-tag oracle and independent positional physical-dual graph;
- true W34 original symplectic lex/random K14 source maps have six missing global physical edge images, and the exact anchored physical C6 through the fixed right anchor is counted independently via literal physical adjacency DFS. Every different repaired complete global g' is independently checked against the actual original six-incidence positional dual definition (the historic W32 half-classifier is K6-only, and deliberately NOT reused for K14);
- independent random genuine original W32/W34 six-point to distinct-line matching with one excluded original line confirms the strict Hall step; malformed original dyadic s, invalid global maps and overclaim flags are rejected.

Dedicated CI uses only GitHub-hosted jobs. No scientific Draft may be merged merely because CI is green: exact HEAD dedicated, INDEX, Proof Audit, Full Research, and independent mathematical review are separate scientific acceptance requirements. Do not hand-edit generated research registries.

## 8. Prior-art and unsolved quantifier

Hall's theorem, dense graph physical six-cycle counts, and transposition sorting are classical; known pancyclicity literature (including Bondy's theorem) is contextual prior art rather than claimed originality. The specialized combined every-original-f,g neighborhood **cardinality** is new only relative to inspected Mathlab Draft results; no independent publication novelty has been verified. The parallel [AA4-AR fixed-two-support concentration PR #544](https://github.com/definitely-stable/Mathlab/pull/544) is not duplicated: it averages over all source-line bijections on prescribed supports, whereas this theorem counts good maps within FIVE original line factor transpositions of EACH adversarially fixed original g.

Remaining true root challenge: establish a **deterministic quantitative reverse-transfer** from good repaired g' to the given adversarial g across the entire ORIGINAL seven GF5 classes, without asserting falsely that seven-tag changes under global swaps have a fixed sign. The actual W32 [#493](https://github.com/definitely-stable/Mathlab/pull/493) and [#497](https://github.com/definitely-stable/Mathlab/pull/497) mixed-swap counterchecks forbid such an assumption. Root #230 stays OPEN_WITH_FORMAL_BLOCKER.
