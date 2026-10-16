# HYP-105 / issue #230 — AA4-AR: deterministic five-transposition original D6 repair

**Research-only partial theorem.** Strict scientific child of [PR #542](https://github.com/definitely-stable/Mathlab/pull/542). True symplectic W(3,2^h), globally injected typed maps to physical unordered coordinate pairs, six DISTINCT original incidence IDs, and the historical aligned positive GF(5) D6 are mandatory. Branch A/B/C remains OPEN_WITH_FORMAL_BLOCKER. This theorem concerns an EDITED global map g', never asserts positivity at the originally chosen g.

## Formal statement

For EVERY h>=1, s=2^h, V=(s+1)(s²+1), d=s+1 and minimal a with K=binom(a,2)>=V, for EVERY pair of complete globally injective factor maps f:P(W(3,s))->E(K_a) and g:L(W(3,s))->E(K_a), there exist exactly six TRUE distinct original incidences Q={(p_i,l_i):0<=i<6}, all original point factors p_i different and all original line factors l_i different, and a complete global line map g' such that:

1. f is unchanged, and the whole occupied physical right edge-image set of g' equals that of g;
2. g' is obtained from g by at most FIVE transpositions exchanging entire assigned pair labels of TWO actual original LINE factors at each step;
3. one of the six original source line factors, l_0, keeps its previous physical edge g'(l_0)=g(l_0);
4. the SAME true original six incidence IDs Q have precisely matching connected physical coordinate-dual C6 on both typed sides under (f,g'). The historical positive GF(5) seven-family classifier therefore accepts Q as D6; D6(f,g')>=1 and S_7(f,g')>=1.

By true symplectic GQ point/line duality, the reversed typed statement holds with f modified by <=5 actual original point-label swaps, g fixed. There is NO lower bound for D6(f,g) on the original adversarial complete pair, NO Ω(s^6) count at g' or g, NO counterfamily, and NO ASET exponent.

## Lemma 1: almost-complete physical palette has at most one C6-dead occupied edge

Let H=K_a-M, a>=10, m=|M|<=a-2. An occupied physical pair edge e={u,v} is called dead if it belongs to no simple connected physical six-vertex C6 in H. Every such edge can be written at most one way as the sole surviving physical edge incident to a pendant coordinate of H; there is at most ONE dead edge. More precisely: either every occupied edge lies on a physical C6, or m=a-2 and all missing physical edges form a star at u, leaving its sole surviving edge e=(u,v), which is the only C6-dead occupied edge.

**Proof.** For a fixed occupied edge e=(u,v), an undirected physical C6 containing it is determined uniquely by a four-tuple x1,x2,x3,x4 of distinct auxiliary physical coordinates in cyclic order u,v,x1,x2,x3,x4,u. Therefore the number of ambient K_a six-cycles containing e is exactly (a-2)_4.

An absent physical edge h adjacent to e belongs to exactly (a-3)_3 such six-cycles; one disjoint from e belongs to exactly 6(a-4)_2 (three internal path positions, two orientations). For a>=10, (a-3)_3 > 6(a-4)_2. Every absent edge kills at most (a-3)_3 ambient cycles through e. Consequently the number of occupied cycles through e is at least (a-2)_4 - m(a-3)_3, strictly positive for m<a-2. If e is dead, equality requires m=a-2, ALL missing h adjacent to e, and NO six-cycle through e contains two distinct missing edges (otherwise the union bound is strict).

Partition missing edges adjacent to e into those incident to u and those incident to v. If both groups are nonempty and their total size a-2>=8, one can choose missing (u,x) and (v,y) with x≠y. Two other distinct auxiliary coordinates can be chosen to complete an ambient K_a six-cycle containing all of e,(u,x),(v,y). This six-cycle was counted twice by the union bound, contradiction. Thus all a-2 missing edges are incident to ONE endpoint of e: e is a pendant occupied edge. The missing-edge budget cannot isolate two different pendant physical coordinates; the unique remaining pendant edge is the sole C6-dead edge. Conversely, a pendant edge is in no cycle. QED.

For actual GQ minimal physical palettes, s=2 yields a=6,m=0 and full K6 (every edge in C6). For all s>=4, a>=14,m<=a-2, so this physical lemma applies.

## Lemma 2: choose six genuine original flags avoiding the exceptional right line

The complete fixed physical image of f contains a simple six-coordinate C6. Indeed complete K_a has (a)_6/12 unoriented six-cycles, and each missing physical edge destroys at most (a-2)_4 cycles. Thus C6(im f)>=(a)_6/12-m(a-2)_4>0 for the actual minimal a,m (s2: complete K6, s>=4: a>=14).

Invert the six different physical f-edge images of this C6 through ONE fixed injective f to obtain six DIFFERENT actual original point factors p0,...,p5. The right physical lemma leaves at most one unusable physical g-edge; by full right global injection it corresponds to at most one actual original line factor l_bad.

The TRUE source incidence bipartite graph of W(3,s) is connected, d-regular, with V points and V lines. For any proper nonempty subset X of original point factors, |N(X)|>=|X|+1. Indeed d|X| source incidences leave X, each opposite neighbor has source degree d, so |N(X)|>=|X|. Equality would mean all source incidences at the neighboring original line factors return to X, making X union N(X) a connected component, impossible because the real GQ incidence graph is connected and X proper. Removing one possible forbidden actual original line factor reduces |N(X)| by at most one. Hall's inequalities therefore continue to hold after removing l_bad, for every subset of the prescribed six original points (V>=15). Hence choose six distinct ACTUAL original incident line factors l0,...,l5, each pi incident to li, none equal l_bad. Q={(pi,li)} is a genuine six-distinct-original-incidence-ID set with left physical connected C6 and all of its existing right g-images on some occupied physical C6.

## Lemma 3: construct at most FIVE real global line-label swaps

Arrange the actual source Q in the cyclic order of its six physical left source-point edge images. The physical right edge g(l0) is not dead, hence belongs to a connected physical C6 inside im g. Choose a cyclic physical right C6 with first physical pair edge exactly g(l0). Its six cyclic physical pair edges t0,t1,...,t5 are different. Define desired images g'(li)=ti, with t0=g(l0).

For i=1,...,5, if li currently has a different physical label, swap the current g-image of the actual original line factor li with that of the unique true original line factor currently carrying ti. This is one globally legal source-factor transposition. Because all six target labels ti are different, the first anchor and all previously corrected factors remain unchanged. After at most five swaps, the SAME six actual original incidence IDs use the two isomorphic connected positional C6 patterns: their physical coordinate-dual pair multiset on each side equals {{i-1,i}:i in Z/6Z}. The original accepted positive GF(5) D6 classifier applies. The entire right physical occupied edge set is preserved and the same single global g' is shared by every original incidence. QED.

There are two distinct possible cyclic orientations of any right physical C6 through g(l0); these produce two distinct full legal repaired global maps within radius <=5.

## Independent falsifiers and limitations

- Enumerate physical K6–K10 cycle-through-edge counts by an independent simple-cycle definition; check the exact adjacent/disjoint missing-edge incidence identities. Synthetic sharp missing-star physical examples K10/K14/K35 have one dead occupied pendant edge, while restoring just one deleted star edge removes this exception.
- In physical K10, generate independent random missing-edge sets of EVERY budget m=0..8 and brute-test every occupied edge for existence of an actual simple physical C6, without trusting the pendant recognition implementation.
- Use actual original W(3,2) S68 and S72 GLOBAL complete fixed f,g, which historically have D6(f,g)=0, and explicit true original 45-incidence IDs. Generate <=5 swaps, check one unchanged source line factor, validate that the repaired g' is a complete global injection, and independently compare both SIX-position physical coordinate duals with the historical accepted GF(5) seven-class oracle.
- Repeat on true original W(3,4), with minimal physical K14 and six missing globally occupied edge-image pairs, both lex and independent random complete global typed maps. No artificial high-order GQ geometry. Test exact integer palette arithmetic through h64.
- Reject duplicate original incidence IDs, invalid source degrees and invalid full physical pair injections.

**Consequence NOT proved:** This is a bounded-edit positive D6 REPAIR, not a sign-definite transfer from a repaired (f,g') back to the original adversarial (f,g). Such a reverse transfer is precisely the substantive missing mathematical step toward #230 Branch A; prior true original mixed swap experiments [#493](https://github.com/definitely-stable/Mathlab/pull/493) and [#497](https://github.com/definitely-stable/Mathlab/pull/497) have negative as well as positive seven-class discrete derivatives. No monotone cross-family compensation may be assumed.

Classical Hall matching and the elementary physical six-cycle counting formulas are appropriately credited. Existing source original all-h positional D6 and physical-occupancy work includes [#480](https://github.com/definitely-stable/Mathlab/pull/480), [#487](https://github.com/definitely-stable/Mathlab/pull/487), [#539](https://github.com/definitely-stable/Mathlab/pull/539). No claim of independently peer-reviewed novelty. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.
