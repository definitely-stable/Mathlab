# HYP-105 / issue #230 — AA4-AK: full true-ORIGINAL adjacent-pinned connected-C6 Hall transfer

**Research-only, strictly scoped ALL-h deterministic equality and conditional Hall dilution.** Strict child of [AA4-AJ connected-C6 PR #521](https://github.com/definitely-stable/Mathlab/pull/521), pinned parent HEAD \`195f80eb7d8770d6f0ddce0d59087f13c9f9e0e4\`. Work is distinct from parallel [#522](https://github.com/definitely-stable/Mathlab/pull/522) (DISJOINT-pin 2+2 bridges only), [#523](https://github.com/definitely-stable/Mathlab/pull/523) (DISJOINT-pin original source-Hall site cap) and original source-genuine [#519](https://github.com/definitely-stable/Mathlab/pull/519) (the three A physical sectors without source-sparse adjacent transfer). No main changes; root issue #230 Branch A/B/C remains OPEN.

## 1. Why the missing adjacent-pin genuine original Hall sector is real

Parent AJ #521 exactly partitions physically disjoint pinned opposite physical edges e0,e1 in connected C6 into two crossed-spoke patterns (2(a−4)(a−5)) and four internal-linked patterns (4(a−4)(a−5)), and gives an all-h original source/Hall formula. But genuine original W(3,s) may have **physically adjacent** images of TWO different actual pinned original source flags. On actual W(3,2) globally injected finite dual zero-split witness, connected-C6 true accepted source Q with adjacent opposite physical pins contribute **23 B-left/A-right** and **17 A-left/B-right**, not merely a rare theoretical possibility. Parent #521 disjoint connected C6 accounts for only 17/41 Q versus full 40/58 true original Q. That remaining actual source sector is not covered by the parent and must not be silently set to zero.

Fix any true ORIGINAL W(3,s), s=2^h≥2, with point and line sets of size V=(s+1)(s²+1), original incidence degree d=s+1. Fix TWO complete and GLOBALLY injected typed physical pair maps f,g, each mapping every original typed factor to a distinct unordered pair in K_a (a minimal C(a,2)≥V), and FIXED across every distinct original six-incidence ID Q. All genuine original source 6-Q factors are precisely actual symplectic incidence edges, not independently faked regular incidence pairs. Fix an original B-side repeated source factor p with two **different actual source incidence flags** through p, whose opposite source factors have physically distinct but ADJACENT globally assigned labels. Fix four different other original B-side factors q0,q1,q2,q3 whose global B images form one occupied C4 on four physical coordinates outside f(p).

## 2. NEW AK-1: unique oriented adjacent physical C6 path (all h)

The two globally assigned pinned opposite physical pairs share EXACTLY one physical coordinate. Write them uniquely as e0={u,v}, e1={u,w} where u is common, v is other endpoint of first pin, w is other endpoint of second pin. Every six-vertex connected simple 2-regular physical graph H containing these pins is a single cycle, and because both pins share u, their remaining vertices form exactly one oriented path from w to v of length FOUR through three other distinct physical vertices a,b,c:

\[
\boxed{H=\{uv,uw,wa,ab,bc,cv\},\qquad
a,b,c\notin\{u,v,w\},\ a,b,c\text{ pairwise different}.}
\]

The ordering and orientation are UNIQUE for the fixed ordered opposite original source flag pins, so distinct triples (a,b,c) yield distinct physical H. Exact complete-physical raw pattern count is thus

\[
\boxed{|\mathcal H_{\rm connected,adjacent}(u,v,w)|=(a_{\rm alphabet}-3)_3
=6\binom{a_{\rm alphabet}-3}{3}.}
\]

Here a_alphabet is the number of physical coordinates, not the first auxiliary path vertex named a. This reproduces the known physical connected-C6 capacity for adjacent pins from #519 but adds an exact source-sparse transfer, not a new graph-cycle enumeration theorem. All K6/K7/K8 pinned adjacent edge pairs are independently exhaustively checked against a full 70-shape physical two-factor enumerator.

## 3. NEW AK-2: exact all-h TRUE original six-Q source-Hall transfer with just TWO anchored internal edges

The globally occupied opposite physical edges wa,ab,bc,cv correspond to four UNIQUE actual original opposite source factors under g⁻¹. Since the actual six source Q has four distinct original B-side singleton factors qi, choose the original source row index k assigned the internal physical edge ab, and a DIFFERENT row index ℓ assigned the internal physical edge bc. There are exactly 4·3=12 ordered choices. The ACTUAL opposite source factors α=g⁻¹(ab), β=g⁻¹(bc) must belong to the TRUE original GQ incidence neighborhoods α∈N(qk), β∈N(qℓ).

**Sparse original-neighbor exact algorithm:** for each ordered original row pair k≠ℓ, iterate all (α,β)∈N(qk)×N(qℓ), at most d² TRUE original factor pairs. Skip α=β; their SINGLE globally fixed physical edges must share exactly ONE physical vertex b and have other endpoints a,c outside the pinned physical triple {u,v,w}. Those endpoints must be distinct. Test that the **two outer physical edges** {w,a} and {c,v} are globally occupied under the SAME global opposite injection g; if so they identify UNIQUE real opposite original source factors γ,δ. The remaining two original rows i,j must receive γ,δ in one of precisely TWO bijections that are checked directly against their TRUE original GQ neighborhoods.

The accepted genuine original GF5 Q count for this fixed root/two source flags/physically occupied source B-C4 is EXACT:

\[
\boxed{
T_{\rm adjacent\ C6}
=\sum_{\substack{k,\ell\in[4]\\k\ne\ell}}
\sum_{\alpha\in N(q_k)}
\sum_{\beta\in N(q_\ell)}
\mathbf1_{\rm actual\ physical\ path\ }\
\Big[
\mathbf1_{\gamma\in N(q_i),\delta\in N(q_j)}
+\mathbf1_{\delta\in N(q_i),\gamma\in N(q_j)}
\Big].
}
\]

The bracket is zero when the path physical edge conditions do not hold. The source-six flag IDs are all distinct: the two pinned original flags have B-source repeated root p, the other four flags have distinct q_i and different opposite globally injected factor images; all physical path edges are distinct and not pinned. The same Q is NOT counted twice in this algorithm because each accepted true Q uniquely determines its physical C6 H, its two internal edge rows k,ℓ, and the remaining 2-rook bijection. An original induced true C8 may produce TWO distinct matching assignments for one physical H, correctly included by the two source bijections, consistent with AA4-AE.

The formula is deterministic for **every h and arbitrary complete global f,g**, uses O(12d²) genuine original source neighbor-pair probes per fixed original B-C4 cohort rather than O((a_alphabet−3)_3) physical path enumeration, and preserves the original genuine W(3,s) source incidence requirement. Symmetric point/line dual also holds.

### NEW unconditional original-source upper

The 12 ordered internal source row choices, at most d² genuine opposite source-neighbor pairs each, and at most TWO assignments of remaining original source rows imply

\[
\boxed{0\le T_{\rm adjacent\ C6}(p,\text{two flags},\mathbf q;f,g)\le24(s+1)^2.}
\]

This is an **upper on accepted true original GF5 Q**, not a source-only forest lower or a positive all-map Hall lower.

## 4. NEW AK-3: all-global conditional physical occupancy and even stronger Hall dilution O(s^{-5/2})

Define m=C(a_alphabet,2)−V≤a_alphabet−2 missing physical opposite edge images in the single complete global g. For any physical coordinate t, let D(t) be its missing physical edge degree. Suppose ONLY the two **nonshared pinned physical endpoints** v,w satisfy D(v)<a_alphabet/16 and D(w)<a_alphabet/16. **The shared pinned physical coordinate u needs no bound at all**: the four unpinned path edges wa,ab,bc,cv do not touch u.

Among exactly (a_alphabet−3)(a_alphabet−4)(a_alphabet−5) complete raw physical oriented path triples, an absent outer edge wa or cv removes at most (D(w)+D(v))(a_alphabet−4)(a_alphabet−5) patterns. Each missing internal physical edge ab or bc removes at most 2m(a_alphabet−5) patterns, so both remove at most 4m(a_alphabet−5). Union bound, no independence or per-Q physical resampling:

\[
\begin{aligned}
H_{\rm occupied}^{\rm adjacent,C6}
&\ge (a-3)(a-4)(a-5)\\
&\quad-(D(v)+D(w))(a-4)(a-5)-4m(a-5)\\
&>(a-5)\left(\frac78a^2-\frac{21}2a+20\right).
\end{aligned}
\]

For every s=2^h≥16, a≥94 and m≤a−2; elementary inequalities on the displayed polynomial yield the explicit simpler bound

\[
\boxed{H_{\rm occupied}^{\rm adjacent,C6}\ge a^3/2.}
\]

Because every Hall-positive physical H contributes at least one accepted true Q, and T≤24(s+1)², we obtain for each such low-hole adjacent pinned original source cohort, for ALL globally injected f,g,

\[
\boxed{\frac{H_{\rm Hall+}}{H_{\rm occupied}}
\le \frac{48(s+1)^2}{a^3}
=O(s^{-5/2}).}
\]

Compared with the O(1/s) Hall success upper in disjoint pinned physical sectors (#523/#521), adjacent pinned connected-C6 physically valid candidates are forced to be **even more strongly diluted by genuine original source Hall incidence** when the two nonshared physical endpoint hole degrees are small. This does NOT assert the existence of many low-hole **adjacent original pinned source rootpairs** in every f,g. It is a quantified CONDITIONAL theorem for every actual such pair, not an unconditional global mass lower; physical adjacency itself may be scarce or absent depending on adversarial opposite injection. No lower on Hall-positive Q follows.

## 5. Genuine-original exhaustive independent falsifiers

1. Exhaust all adjacent edge pairs in K6, K7, K8 and all complete physical original six-coordinate C6 patterns. Verify the exact one-to-one triple path characterization, raw capacity 6*C(a−3,3), unicity and no accidental double counting.
2. On the TRUE original W(3,2) symplectic source graph, all original 45 incidence IDs, all 15 real source roots, all three actual two-flag selections per root and all three original B physical complement C4 patterns per root, on BOTH typed sides of five full globally injected W32 models (historical S68/S72/lex/reverse and independent zero-split). For every adjacent pinned actual root/C4 cohort, compare the NEW sparse two-internal-edge source Hall count to an independent full physical C6 enumeration with genuine original 4×4 permanent 0,1,2 and original C8 extra-matching identity. Zero-split expected genuine adjacent accepted 23 B/A and 17 A/B; physically occupied connected adjacent C6 558 and 432, respectively.
3. On the TRUE ORIGINAL W(3,4), lex and random full typed globally injected but NONONTO K14 images, two orientations, selected actual original adjacent root/two flag pairs and physical B-C4s: compare NEW count to independent complete source Hall four-rook plus existing AA4-AI full connected C6 sector physical census. Missing opposite physical pairs must remain missing and may not be treated as source factors.
4. On genuine W(3,8), lex/random physical K35 maps with 10 unoccupied physical edge images, both typed sides and selected actual original root/C4s, independently enumerate every physical adjacent C6 (up to 29,760 raw paths) and confirm the same original six-Q accepted count, source C8 extras and degree bound.
5. An actual common symplectic source automorphism of W(3,2), plus independently arbitrary point/line physical alphabet permutations, must preserve counts when following the SAME actual original pinned source flags and original four-C4-factor IDs, NOT comparing arbitrary first chosen C4 after reindexing.
6. All exact powers s=2^h through h=43: physical missing-edge union-bound integer/Fraction thresholds, source-degree cap, conditional upper 48d²/a³ and no invalid assertion of all-map Hall success. Invalid source incidences and noninjective source physical map IDs fail closed.


### Exact finite TRUE W(3,2) adjacent physical pins sector ledger

On the true indexed original symplectic W(3,2), each tested typed pair map is a separately complete K6 pair-edge bijection and source incidence has exactly 45 actual original flags. For each of five fixed global pair-map models and EACH of the point-B/line-A and line-B/point-A orientations, the dedicated independent oracle evaluates ALL 15 original roots ×3 ACTUAL pinned original flag-pairs ×3 globally occupied point/line physical source C4s = 135 cohorts per typed orientation. The numbers below are **only ADJACENT opposite pinned physical** connected C6 contributions, not all GF5 or disjoint pinned counts. The two independent algorithms are (i) sparse 12 ordered internal original source row pairs + their actual GQ neighbor edges and (ii) all physical genuine A twofactors + true original 4×4 source girth-eight permanent.

| Fixed complete true W32 typed pair map | Accepted original six-ID B/A adjacent C6 | Accepted original six-ID A/B adjacent C6 | Occupied physical opposite adjacent C6 H, B/A | Occupied physical opposite adjacent C6 H, A/B |
|---|---:|---:|---:|---:|
| zero-split original-global pair | 23 | 17 | 558 | 432 |
| lex | 56 | 50 | 576 | 468 |
| reverse | 18 | 19 | 378 | 468 |
| S68 | 7 | 6 | 432 | 630 |
| S72 | 11 | 11 | 450 | 630 |

The zero-split W32 pair has **17/41 accepted** disjoint pinned connected C6 source Q in earlier AJ #521, plus **23/17 adjacent** from this AK theorem, exactly **40/58** full genuine ORIGINAL connected C6 accepted Q reported by earlier AA4-AI #519. The same physical occupied sectors add **504+558=1062** (point-B) and **756+432=1188** (line-B). Consequently every nonzero finite adjacent class is REAL genuine W32 accepted incidence, not an assumed missing pattern, and each is checked against the unmodified historical globally injected source model.

This table does not establish a positive all-global-map accepted count at arbitrarily large s. It is finite strict original geometry regression evidence for the all-h transfer identity and an explicit confirmation that disconnected-pins-only formulas were incomplete for connected-C6 GF5.

## 6. Acceptance, nonimplications and actual next proof gate

**Proved restricted all-h:** the genuine original adjacent physical pins imply a unique physical C6 oriented path; the sparse two-anchored-source-edge original 12×2 channel formula is an EXACT true-original six-ID GF5 count under every complete global f/g; its per-source-root upper 24d²; conditional on only two nonshared pinned physical missing degrees <a/16, physically occupied C6 count ≥a³/2 (s≥16) and actual Hall-positive physical fraction O(s^-5/2). Dual point/line roles hold.

**Not proved:** every source root has adjacent physical pins; a positive global count of adjacent-pin accepted GF5 Q; an all-map Ω(s6) bound on the true original seven-selected GF5 sum S_s(f,g); infinite globally injected S=o(s6) source counterfamily; any full R3/ASET exponent.

**Next meaningful gate:** combine BOTH previously exact DISJOINT original connected-C6 transfer (two crossed-spoke + four internal link) and this ADJACENT exact original connected-C6 transfer with the three physical A sector counts (split 2C3, same 2C3, connected C6) on identical globally injected true GQ source six-Q. Prove a genuinely nonzero GLOBAL original Hall mass lower across these channels (possibly with five other selected GF5 classes including positional D6), or an actual infinite correlated original full-global counterfamily. More physical occupancy alone is insufficient.

**Integration:** research-only Draft strict stacked child of #521, exact parent SHA recorded; standalone executable proof, independent tests, structured Markdown and GitHub-hosted workflow. Full dedicated/INDEX/Proof Audit/Full Research exact-final-head CI and **independent mathematical proof referee** required before scientific acceptance, authoritatively SHA-pinned canonical RCP JSON registration, regeneration of five structured Markdown research registries, or merging this Draft. Root #230 remains OPEN.
