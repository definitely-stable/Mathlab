# HYP-105 B3.2-E1-B: all-label six-motif Ω(s^6) obstruction or infinite correlated counterexample

- Source: https://github.com/definitely-stable/Mathlab/issues/230
- Repository: definitely-stable/Mathlab
- Issue: #230
- State: open
- Author: MrFr3di
- Created (UTC): 2026-10-10T05:18:05Z
- Updated (UTC): 2026-10-14T04:50:36Z
- Captured (UTC): 2026-10-14T05:17:04.342Z
- Comments: 175

---

Parent [HYP-105 #176](https://github.com/definitely-stable/Mathlab/issues/176), upstream [#169](https://github.com/definitely-stable/Mathlab/issues/169). Follows merged [#224](https://github.com/definitely-stable/Mathlab/pull/224), merged [#225](https://github.com/definitely-stable/Mathlab/pull/225), and finite E1-A [PR #227](https://github.com/definitely-stable/Mathlab/pull/227).

## Objective: prove a nontrivial ALL-h statement, not fit finite W32 observations

Let f_s,g_s range over ALL injective maps from the V_s=(s+1)(s^2+1) typed factor vertices of W(3,s), s=2^h, into unordered physical coordinate pairs of K_{a_s}, a_s=min{a:binom(a,2)>=V_s}. Let D6, U_B_left/right and U_CA/U_CB/U_BB_overlap/U_BB_disjoint count ORIGINAL DISTINCT six-incidence factor sets satisfying accepted positive six-coordinate GF5 classes, NOT signed-event counts or physical label automorphism orbits.

Accepted all-h fixed-label necessary R3 floor:

```text
51^6 R3(f_s,g_s) >=
5643 D6 + 45600(U_B_left + U_B_right)
+ 43320 U_CA + 49050 U_CB
+ 51750 U_BB_overlap + 45010 U_BB_disjoint.
```

## Disjunctive proof gate

**Branch A — universal obstruction:** prove `inf_{f_s,g_s} S_s(f_s,g_s) = Omega(s^6)` for S equal the sum of those seven disjoint motif multiplicities. Then no allowed deterministic pair-label family reaches R3=O(s^(6-eps)) via this particular GQ construction / classical alteration. Beware this would NOT rule out all general weighted ASET constructions or other hypergraph-extraction algorithms. Prove all h with positive constant independent of h and no Sp(4,s) assumed symmetry of arbitrary physical labels.

**Branch B — counterexample to A:** exhibit for an infinite s=2^h sequence a concrete correlated f_s,g_s with S_s=o(s^6), plus rigorous all-h bound. Such a witness invalidates A but is NOT by itself an R3 upper because uncounted positive GF5 four/six-coordinate classes may dominate. The actual strict extraction goal needs **same maps** R2=O(s^(26/5-eps2)) and entire R3=O(s^(6-eps3)).

**Branch C — model-equivalent reduction:** If neither A nor B closes, isolate an explicit incidence-tensor/cycle-pair-count inequality (with precise norms, constants, input label alphabet and restrictions) equivalent to one of the assertions. Establish spectral/cell-probe/rank limitations or explicit counterexamples with independent exact finite falsifiers. Do not label mere simulation a theorem.

## Required independent evidence

1. Index all 631 previously positive leading forest partition types and 11,032 subleading necessary shape types by original factor-endpoint partition (keep physical projections distinct). Finite exact counts for W32 E1-A are baseline only: lex U=(13,1,8,14), reverse-line U=(1,1,7,6), with fixed GF5 risk floors 1,656,350/51^6 and 724,680/51^6.
2. Compare D6, Q4, accepted single-cherry U_B and four NEW U counts ON ONE physical labeling. Optimize proxies only as declared *lower-risk surrogates*, never full R3.
3. For any theorem claim demand explicit s=2^h quantifiers, exact GF5 nonzero/checksum4 51-column palette, no assumed independence between correlated maps, no finite-h asymptotic fit.
4. Independent mathematical proof + two methods of oracle falsification, exact PR-head GitHub-hosted Research SUCCESS, postmerge main Research SUCCESS.
5. Status outcomes: PROVED_A, COUNTEREXAMPLE_B, RESTRICTED_THEOREM_C or OPEN_WITH_FORMAL_BLOCKER. No ASET exponent until full strict all-h estimates close.

Do not close #176 or #169 as a consequence of merely accepting E1-A. No Rust or external repo changes.


# All 175 issue comments — original order

## Comment 001 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6094325419
- GitHub comment ID: 6094325419

**HYP-105 B3.2-E1-B0 — exact seven-family same-label reduction submitted as [draft PR #233](https://github.com/definitely-stable/Mathlab/pull/233).** Current PR exact-head Research CI gate is pending; no merge or all-h obstruction claim.

PROVED all-h identity: the coefficient of t^6 and six x/y physical coordinates of degree exactly two in the nonnegative integer polynomial ∏_{original incidence (p,l)}(1+t U_p V_l X_{f(p),1}X_{f(p),2}Y_{g(l),1}Y_{g(l),2}), with factor endpoint tags, counts exactly the selected original six-incidence 6+6 leafless patterns for arbitrary injective f,g. This isolates the coefficient lower needed for the universal-quantifier #230 hypothesis; it does NOT prove this coefficient is Omega(s^6).

GitHub-hosted Research #38027947586 SUCCESS on the seven-class structural oracle (Q4 independently C4/line join; D6 independently C6/line join); #38028014149 SUCCESS on extension that computes all 10 unordered 3v3 signs with full 51 GF5 palette on every qualifying original sixset. **Complete W(3,2) fixed-map finite results, exact selected-family only:**

| | lex | reverse-line |
|--|--:|--:|
| D6 | 15 | 3 |
| B-left/A-right | 98 | 77 |
| A-left/B-right | 110 | 74 |
| C/A | 13 | 1 |
| C/B | 1 | 1 |
| B/B overlap | 8 | 7 |
| B/B disjoint | 14 | 6 |
| S_seven | 259 | 169 |
| Q4 | 50 | 32 |
| Proven simpler R3_min numerator / 51^6 | 11,225,795 | 7,627,209 |
| **Exact R3_seven_selected numerator / 51^6 (all ten GF5 signed events)** | **14,874,594** | **9,330,448** |

The exact restricted R3 includes all 10 signs for D6, versus only one accepted alternating sign in the minimum-based lower. All numbers and individual class sums are frozen in regression tests/docs. **NOT:** total GF5 R3, an all-label Omega(s^6), a strict R3 upper, nor an improved ASET exponent.

New prior-art transfer firewall in proof doc: classical Sidorenko/tree homomorphism bounds count one-target maps, not two synchronized physical degree-2 projections; rainbow-cycle theorems in properly edge-colored graphs cannot be invoked directly because incident factor edges inherit repeated physical pairs. No new LIT IDs claimed.

Next research gate #230 remains B1 all-h universal coefficient lower vs infinite correlated counterexample. #176 remains OPEN.

---

## Comment 002 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6094330142
- GitHub comment ID: 6094330142

**B1 feasibility check — why ordinary expander mixing alone is too weak at the physical coordinate-star scale (prior-art/model audit, not #230 proof).**

Let B be the V×V point–line incidence matrix of W(3,s), V=(s+1)(s²+1), Δ=s+1. For the standard symmetric GQ(s,s) point-collinearity graph, BBᵀ=ΔI+A, where A is s(s+1)-regular and strongly regular with nontrivial eigenvalues s−1 and −(s+1). Consequently B has singular values Δ, √(2s), 0 (multiplicities immaterial here). The vanilla bipartite mixing error for point/line subsets P,L is bounded by √(2s)√(|P||L|).

Physical coordinate fiber F_i={p:i∈f(p)} and G_j={l:j∈g(l)} has mean size t=2V/a, because every injective unordered pair label has two endpoints. For 'typical-size' t=Θ(s^{3/2}) physical coordinate fibers:
  - mixing main term Δ t²/V=Θ(s);
  - spectral error √(2s)*t=Θ(s²);
  - exact squared error-to-main ratio = s*a²/[2(s+1)²]=Θ(s²).
Hence simple one-cut expander mixing can be VACUOUS at the natural coordinate-fiber scale, without showing that some more sophisticated spectral/tensor method must fail. A valid B1 proof needs a true 6th-order coupled contraction inequality or incidence-specific correlation control; invoking ordinary mixing once is not enough.

This model transfer test is separate from E1-B0 PR #233; not implemented as a new spectral theorem or imported as a new LIT entry. The seven-motif all-label Ω(s^6) question remains OPEN.

---

## Comment 003 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096069107
- GitHub comment ID: 6096069107

**B3.2-E1-B1-A progress — [Draft PR #238](https://github.com/definitely-stable/Mathlab/pull/238), hosted exact-HEAD CI pending.**

Two scoped all-h theorems now have explicit proofs and independent finite falsifiers:

(A) Every left injective pair-label map f has L_s(f)=(151/144+O(1/s))s^15 ORIGINAL six-incidence sets with leafless six-coordinate LEFT projection, uniformly in f. Physical K_a A/B/C templates have 70/45/15 configurations per six symbols and 6/5/3 distinct used pair labels. Missing t=K−V<a physical edges destroy at most t*e*F/K templates, by exact edge-transitive double counting; each template lifts to Δ^6, binom(Δ,2)Δ^4 or binom(Δ,2)^3 original incidence sixsets.

(B) For **every fixed f**, a uniformly **independent random right injection g** satisfies E_g U_{B-left/A-right}(f,g)=(140+O(1/s))s^6. GQ W(3,s) has no incidence 4-cycles, so any two left points have at most one common right line (cf. J. Bamberg *Finite Generalized Quadrangles*, https://cage.ugent.be/~bamberg/FGQ.pdf; Encyclopedia of Mathematics generalized quadrangle definition). The left B vertex multiplicity vector (2,1,1,1,1) has 14 cross-factor pairs; independent neighbor sampling shows at least (1−14/Δ²)_+ of original B lifts use SIX DISTINCT right factor vertices. For any six distinct right factors, independent uniform right injection gives exact physical simple six-coordinate 2-factor probability 6!*70*C(a,6)/(K)_6=(560+O(1/s))s^-9. Multiply by (1/4+O(1/s))s^15 left B lifts to get 140. Accepted B/A strictly positive full-GF5 risk implies E_g R3(f,g)>= (45600*140/51^6+o(1))s^6. This proves **for all f, average over g**; trivially for all f EXISTS some bad/high-risk g. It does NOT prove the desired **for all f,g** lower and does not rule out exceptional low-risk correlated g.

More precise #230 transfer target: with T_s(f,g)=S_seven(f,g)/L_s(f), the all-label S_seven=Ω(s^6) assertion is equivalent to an all-label T_s=Ω(s^-9). E1-B1-A proves the denominator uniformly has Θ(s^15) mass; all remaining risk is in the right physical six-motif pass fraction. An asymptotically low S would force right transfer o(s^-9).

**Prior-art firewall for future derandomization:** Exact 6-wise UNIFORM permutations of the K physical **pair-label objects** (not just physical coordinate-symbol permutations) suffice to preserve each six-distinct-original-right-factor completion expectation in theorem (B); see Finucane–Peled–Yaari, *A recursive construction of t-wise uniform permutations*, Random Structures & Algorithms 46 (2015), DOI https://doi.org/10.1002/rsa.20509 . This gives a possible smaller averaging space but NOT the all-fixed-right inequality. Permuting only the a physical coordinate symbols is a gauge symmetry of each S(f,g) and cannot simulate random K-edge assignments. No new canonical LIT ID before source deduplication.

---

## Comment 004 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096274312
- GitHub comment ID: 6096274312

**HYP-105 B3.2-E1-B1-B — exact correlated pair-assignment move implemented in [draft PR #242](https://github.com/definitely-stable/Mathlab/pull/242).** Hosted exact-head Research validation pending. New finite research gate (not a claimed all-h result):

For fixed left f and right injection g, let I_g(E) indicate one of the seven accepted GF5-positive original sixset classes. If g' swaps the physical K_a pair assignments of two ORIGINAL right factor line vertices u!=v, then for any finite original incidence host
```
S_seven(f,g')-S_seven(f,g) =
sum_{original sixsets E touching right factor u or v}
(I_g'(E)-I_g(E)).
```
Identical cancellation holds for the full-GF5 minimum-weight structural floor numerator. Proof: every sixset without either right factor has exactly unchanged physical pair labels. No randomness, independence, or spectral assumption. This improves exact finite search audit complexity by indexing actual touched sixsets instead of re-scanning all C(N,6).

W(3,2), a=6: the program enumerates all 62,370 accepted left original sixsets ONCE and audits EVERY binom(15,2)=105 right-factor K6 pair-label transposition from the pinned reverse-line physical injection. One deterministic minimizer of S_seven over all 105 neighbors (ties min-weight GF5 risk floor, then lex swap) is verified by completely independent full seven-census + real right C6/D6 and C4/Q4 incidence joins; then **all ten** balanced GF5 signed weights per selected sixset are evaluated using accepted full-51 exact Fourier oracle. The independent tests verify 3 additional swaps via full 62,370 original-sixset recounts, swap involution/reconstructed full physical 4-support columns, and separate gauge invariance under coordinate-symbol S6 relabeling.

**Explicit quantifier firewall:** a physical K6 coordinate-symbol permutation is an objective-preserving gauge, whereas assigning a different original right line to a given K6 physical pair label is a genuine non-gauge correlation. This experiment is s=2 ONLY and one 105-neighbor round; neither a global minimum over 15! pair assignments nor a one-swap local optimum after iterations is claimed. Even S=0 at some fixed finite s would NOT refute a large-s Omega(s^6) bound. No all-h obstruction/counterexample or R3 upper asserted. Parent #230/#176 still OPEN.

Next all-h B1-C gate: prove an absolute right-transfer rate S/L >=c s^-9 for EVERY correlated pair f,g, or construct an explicit infinite s=2^h family with S=o(s^6), keeping accepted seven families and full GF5 trade risk distinct.

---

## Comment 005 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096342683
- GitHub comment ID: 6096342683

**B1-C exact hypergraph-intersection reduction for the next infinite-h proof (not yet a theorem of positive lower mass).**

There is a sharper reformulation of the accepted B/A subproblem than the generic two-color sixset tensor. Freeze s=2^h and any left injection f. Define a nonnegative integer-weighted 6-uniform hypergraph H_f on the V ORIGINAL right factor line vertices:

- For any unordered six DISTINCT right line-factor set R, set m_f(R) equal to the number of ORIGINAL six-incidence sets with exactly original right endpoint set R, left original factor multiplicity B=(2,1,1,1,1), and a leafless six-coordinate LEFT physical projection under f.
- No GF5 weights in m_f: count each selected original six-incidence set once. Then Σ_R m_f(R)=H_B(f)=(1/4+O(1/s))s^15 uniformly in f, by accepted B1-A one-sided count and codegree-one collision union bound.
- Let T_a be the ordinary 6-uniform hypergraph on the K=C(a,2) PHYSICAL pair-edge labels: a six-pair set belongs to T_a iff its six physical edges form a SIMPLE 2-factor on exactly six physical vertices (C6 or 2C3). Its exact cardinality is |T_a|=70*C(a,6).

For EVERY right injection g from original factor lines into distinct physical pair-edge labels,

```text
U_{B-left/A-right}(f,g) =
     sum_{R subset L, |R|=6} m_f(R) * 1_{ g(R) in T_a }.
```

Proof: the 6 original right endpoints are all distinct, so under injective g they label six distinct physical edges, and the accepted B/A class criterion is *exactly* that their image is a simple 2-factor; no orientation/sign or 6! factor is introduced because R is UNORDERED. Its ten positive GF5 signed events are handled separately by accepted #218.

Under uniform random injection g, E 1_{g(R) in T_a}=|T_a|/C(K,6)=70*C(a,6)/C(K,6), equivalent to B1-A's 720*70*C(a,6)/(K)_6 and yielding uniform (140+O(1/s))s^6 expectation.

**Important unmet quantifier:** The desired deterministic all-g B/A lower would amount to a *permutation-unavoidable weighted intersection* H_f ∩ g^{-1}T_a of mass Ω(s^6), uniformly for the very structured incidence-derived H_f. A first-moment calculation and large total mass Σm_f do NOT guarantee it: arbitrary 6-uniform hypergraphs of a given total weight can have low-overlap permutations. A counterexample to B/A-only positivity would not necessarily refute the full seven-family S lower (other six classes can contribute). B1-B W32 swaps specifically explore non-gauge changes of this intersection.

**Concrete next B1-C gate:** prove a new incidence-structure-dependent lower on min_g sum_R m_f(R) 1_{g(R) in T_a}, or show a precise upper/countermodel; compare this to full S (seven classes) with same maps. Do not invoke generic rainbow-cycle or Sidorenko results without proving the required transfer. This is a mathematical reduction, not a claim of solved Ω(s^6) or improved ASET exponent.

---

## Comment 006 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096381377
- GitHub comment ID: 6096381377

B1-B VERIFIED on PR #242 (https://github.com/definitely-stable/Mathlab/pull/242). Initial Research CI https://github.com/definitely-stable/Mathlab/actions/runs/38042611336 SUCCESS: complete W(3,2) reverse-line 105-neighbor swap audit (62,370 left original sixsets), independently verified winning right factor line-label swap (4,13). Exact before/after S_seven=169/128, Q4=32/23, minimum GF5 risk numerator=7627209/5803196 over 51^6, and exact selected all-ten-sign full-51 GF5 numerator=9330448/7087162 over 51^6. Class counts before (D6,B-left/A-right,A-left/B-right,C/A,C/B,BB-overlap,BB-disjoint)=(3,77,74,1,1,7,6), after=(2,57,51,3,2,8,5). This is finite selected-family improvement, NOT full R3 or an infinite-h counterexample. NEW PROVED all-h local bounded influence: for s=2^h, Delta=s+1, K=C(a,2), Lplus=C(a,6)[70 Delta^6+45 C(Delta,2)Delta^4+15 C(Delta,2)^3], swapping two original right line-factor pair assignments affects at most B_s=min{Lplus,floor(12 Lplus/K)}=(151/12+o(1))s^12 left-qualified original sixsets. Proof by edge-transitive weighted template multiplicity: fixed original incidence (p,l) appears in at most 6 Lplus/(K Delta) left sixsets, each changed right line incident to Delta original edges; union bound. Hence for ANY correlated legal f,g: |Delta S_seven|<=B_s and |Delta accepted GF5 minimum-floor numerator|<=51750 B_s. This is too weak to imply Omega(s^6) universal obstruction. Full latest extended PR HEAD Research CI still pending; root #230 remains OPEN. Next gate: weighted 6-uniform hypergraph intersection lower for all right assignments or explicit infinite correlated counterexample.

---

## Comment 007 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096398323
- GitHub comment ID: 6096398323

PRIOR-ART GATE for HYP-105 B1-C weighted six-uniform hypergraph intersection, verified 2026-10-10. Canonical Mathlab literature.json currently does NOT contain either DOI: (1) Béla Bollobás & Alex Scott, 'Intersections of hypergraphs', Journal of Combinatorial Theory B 110 (2015), 180–208, DOI https://doi.org/10.1016/j.jctb.2014.08.002, open preprint https://arxiv.org/abs/1408.6348 . This explicitly studies how little or much two WEIGHTED k-uniform hypergraphs can overlap under a vertex bijection, INCLUDING randomly placed overlap and concentration. (2) Bollobás & Scott, 'Intersections of random hypergraphs and tournaments', European Journal of Combinatorics 44A (2015), 125–139, DOI https://doi.org/10.1016/j.ejc.2014.08.023, preprint https://people.maths.ox.ac.uk/scott/Papers/intrand.pdf . Both are directly relevant to the previously identified exact HYP-105 representation U_B/A(f,g)=sum_{|R|=6} m_f(R)*1[g(R) in T_a], where m_f is weighted source-original-sixset multiplicity and T_a is the physical K_a six-edge 2factor 6-uniform target. BEFORE stating worldwide novelty or a new asymptotic weighted overlap theorem, import/deduplicate these papers and compare their exact bounds and assumptions against (i) incidence-generated weighted H_f, not arbitrary/random hypergraph, (ii) highly structured six-edge 2factor target T_a, not random H, (iii) injections V->K with K=V+O(s^1.5), not necessarily equal-size bijections, (iv) requested MIN over EVERY correlated right labeling g, rather than average over g. Their abstracts alone do not prove universal min_g U_B/A>=Omega(s^6) or existence of an avoiding labeling. Next B1-C must derive a precise permitted transfer/counterexample under these four fences. Current B1-A/B1-B results stand separately; root #230 remains OPEN.

---

## Comment 008 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096607945
- GitHub comment ID: 6096607945

HYP-105 B3.2-E1-C0 developed in [PR #249](https://github.com/definitely-stable/Mathlab/pull/249) (full exact-head Research CI pending). Mathematical evidence, not closure of the all-label gate:

(1) For any s=2^h and fixed legal left physical pair injection f, define a NONNEGATIVE INTEGER-weighted 6-uniform source hypergraph m_f(R) on original right factor line sixsets R. Its weight is the number of distinct ORIGINAL six-incidence sets with LEFT factor type B and exactly six LEFT physical coordinates of degree 2, with original RIGHT endpoint set R (six different right line factors). Define target T_a on the K=C(a,2) vertices representing physical unordered K_a pair labels, whose hyperedges are the 70*C(a,6) simple six-edge 2-regular K6 graphs. For ANY arbitrary correlated right injection g, exactly:
U_B-left/A-right(f,g)=SUM_{|R|=6} m_f(R) 1_{g(R) in T_a}.
Uniform independent random g recovers expected overlap E_g U = (sum_R m_f(R)) * 70*C(a,6)/C(K,6), hence (140+O(1/s))s^6 from B1-A. No all-g minimum bound follows.

(2) NEW all-a explicit target two-point structure (proved by S_a orbit counting; independently enumerable K6/K9): |T_a|=70*C(a,6), degree of each physical pair-label vertex =28*C(a-2,4); co-degree of two distinct physical pair labels sharing a coordinate =7*C(a-3,3), and of two disjoint labels =14*C(a-4,2). T_a is an exact 1-design for all a>=6, and a 2-design ONLY at a=9, which does not arise as the minimal physical alphabet for W(3,2^h): a2=6,a4=14. For complete right-label BIJECTIONS V=K, if the weighted source m(R)=c+SUM_{v in R} beta_v has ONLY degree<=1 form, all right permutations give the SAME overlap c*|T_a|+deg(T_a)*SUM beta_v, but the actual incidence source m_f is not shown to have that form. For nonsurjective V<K, this invariance need not hold.

(3) Generic mass-only false transfer: a weighted source with arbitrary large mass M concentrated on one sixset can be mapped to five physical edges incident with coordinate 0 plus physical edge (1,2); this sixset is not in T6. So exact overlap 0 under that bijection despite random mean 2M/143>0. NOT a W(3,s) counterexample, but shows total source mass cannot imply positive deterministic minimum without detailed source distribution.

(4) Prior-art scope: Bollobás–Scott 'Intersections of hypergraphs' JCTB 110 (2015) DOI 10.1016/j.jctb.2014.08.002 directly studies weighted k-hypergraph overlap and single transpositions. Their Theorem 3 controls +/- discrepancy via W-vectors, NOT positive minimum absolute overlap; Theorem 16 exhibits orthogonality patterns. Related 'Intersections of random hypergraphs and tournaments' EJC 44A (2015) DOI 10.1016/j.ejc.2014.08.023 treats random, not deterministic GQ. 2011 graph ancestor DOI 10.1002/jgt.20489 and 2017 random packing DOI 10.1002/rsa.20673 also logged. Proof-note pins titles, authors, DOIs, conditions; no novelty claim for generic overlap. Canonical catalog IDs must be allocated after current IMPORT-013 #250 reservation audit.

(5) GitHub-hosted first B1-C CI found a real test dependency on unmerged B1-B #242; it is FIXED on branch by rebuilding swap(4,13) self-contained from actual original right factor labels and physical supports. New exact-head CI pending. Parent #230/#176 remain OPEN; no universal S_s=Omega(s^6), no infinite correlated counterexample, no full GF5 R3 power. Next gate: GQ-specific weighted second-order source m_f distribution vs the target's two adjacency orbits, and a **minimum**-over-right-injections theorem, not a mere random mean.

---

## Comment 009 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096867991
- GitHub comment ID: 6096867991

HYP-105 B3.2-E1-C0 further PROVED exact model restriction in [PR #249](https://github.com/definitely-stable/Mathlab/pull/249): simple 6-edge 2-regular physical K_a target T_a has five orbits on TRIPLES of distinct physical pair labels. Triangle C3 (r=3) has codegree C(a-3,3); simple length-3 path P4 (r=4) codegree 2 C(a-4,2); 3-star K1,3 (r=4) codegree 0; 2-edge path plus disjoint edge (r=5) codegree 5(a-5); perfect matching of 3 edges (r=6) codegree 8. These counts arise from complete K6 factor-completion numbers (1,2,0,5,8) times C(a-r,6-r), and satisfy sum_triples codegree=20*70*C(a,6). Independently exhaustive K6 and K9 checks cover all 455 and 7140 triple-label 3-edge subsets respectively. In the same PR a direct 8-sixset signed 3-cube trade proves source total mass, ALL individual weighted vertex degrees and ALL pairwise codegrees can agree for TWO abstract nonnegative integer-weighted 6-hypergraphs while fixed overlap with T6 differs (0 vs 1, scalable). Cube: common 3 source vertices (0,1,6) and 3 toggle pairs (2,11),(3,12),(13,14) as lex-ordered K6 edge-label IDs; split 8 corners by parity, only mask7 forms a physical C6. This is NOT a W(3,s)-generated source counterexample. Thus a general second-order-marginal-only deterministic intersection theorem is false, and B1-C1 must explicitly exploit GQ-specific third-order source restrictions or higher-order information to prove all-g min, or construct an infinite counterexample. Older weighted hypergraph overlap/discrepancy research of Bollobás-Scott 2015 has already been recorded; no novelty claim on general hypergraph formalism. Exact-head full Research CI pending; root #230 remains open.

---

## Comment 010 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6096947055
- GitHub comment ID: 6096947055

**NEW B1-C2 prior-art route: permutation/injection Lopsided Lovász Local Lemma PACKING, not a claim of solved all-label #230.** Canonical primary source: Linyuan Lu and László Székely, *Using Lovász Local Lemma in the Space of Random Injections* (Electronic Journal of Combinatorics 14(1), R63, 2007), DOI https://doi.org/10.37236/981, author PDF https://people.math.sc.edu/lu/papers/randinj.pdf. Their Theorem 2 gives a sufficient condition to pack ANY two simple r-uniform hypergraphs H1,H2 into the same n-label universe via injections with disjoint edge images. If |E(H_i)|=m_i and every edge intersects at most d_i other H_i edges, then (d1+1)m2+(d2+1)m1 < C(n,r)/e is sufficient for disjoint packing. A constructive followup is Harris–Srinivasan, *A Constructive Lovász Local Lemma for Permutations* (Theory of Computing 13(17), 2017), DOI https://doi.org/10.4086/toc.2017.v013a017, section 8.4 hypergraph packing; do not equate SODA earlier abstract with publication date. Both are relevant next import after DOI canonical catalog dedup.

Model-correct transfer to B1-C0: for any fixed GQ left labeling f, take H1=SUPPORT of the nonnegative integer source six-hypergraph m_f (ignore multiplicity when detecting whether overlap is zero), H2=physical K_a 6-edge 2factor target T_a, n=K=C(a,2) physical pair-label vertices, r=6. Here |V(H1)|=V<=K, |V(H2)|=K; an injective embedding of H1 into K physical pair-label vertices is exactly a legal right assignment g. Define m_H=|supp(m_f)|, D_H=max_{R∈H} #{R'∈H\{R}:R'∩R ≠ ∅}, and target m_T=70*C(a,6), D_T defined similarly. If (D_H+1)m_T+(D_T+1)m_H < C(K,6)/e, THEN classical Lu-Székely proves existence of g with U_B-left/A-right(f,g)=0. This would refute a B/A-only all-g lower for that f. It does **NOT** establish S_seven=o(s6) because six other strictly positive families persist; also it is a conditional criterion, NOT shown true for any infinite sequence f_s.

Exact target codegrees from E1-C0 imply a simple valid bound D_T+1≤6*deg_T=168*C(a-2,4), since each target hyperedge has six physical pair-label vertices and at most deg_T targets through each. For W32, source m_H=3076 and target m_T=70 whereas C(15,6)=5005, so already the SINGLE term (D_T+1)m_H is large; direct finite certificate needed before asserting failure/success. For all h, B1-C0 proves |supp(m_f)|≥(1/60+o(1))s11 and max weight≤15(s+1)^4 but does NOT bound D_H tightly enough to meet the LLL criterion. B1-C2 gate: compute exact source-support hyperedge intersection degree D_H and target D_T at W32, then seek all-h restricted f_s with sufficiently low values, test whether above strictly certified inequality holds. This is potentially an **avoiding-g / conditional counterexample direction**, not a universal positive-min argument. No ASET power / #230 closure declared.

---

## Comment 011 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097105713
- GitHub comment ID: 6097105713

### HYP-105 B3.2-E1-C1 follow-up — stacked PR #260 (CI pending)

After B1-C0 #249, opened [#260](https://github.com/definitely-stable/Mathlab/pull/260) with a model-specific all-h theorem and independent finite oracle:

- ORIGINAL W(3,s) right-line concurrence graph is SRG (V,s(s+1),s-1,s+1); exact induced three-line 0/1/2/3 concurrence counts. Classical GQ facts, not a novelty claim.
- Exact B-left/A-right source point-wedge decomposition through the **unique** repeated original left point p and disjoint physical C4 on four singleton left factor points.
- Improved structural fiber bound m_f(R) <= c_GQ(R)*(s+1)^4. If the six ORIGINAL right lines in R are pairwise skew, m_f(R)=0. At all h, fraction of original right sixsets eligible for m_f(R)>0 is O(1/s) since E_R[c_GQ(R)]=15*s(s+1)/(V-1). Consistent with #249's Omega(s^11) source-support lower.
- Independent complete W32 wedge-vs-original enumeration (10,935 B candidates, 5,000 distinct-right mass, 3,076 weighted right sixsets, max m=6), plus all 455 original right-line triple source marginals. Dedicated Research CI steps.

**Proof-scope firewall:** four ORIGINAL concurrence classes here are not five target PHYSICAL K_a-edge triple orbits in #249. No inference that arbitrary right pair-label injection preserves GQ adjacency, no claimed min_g overlap Omega(s^6), no full-GF5 R3 power. Both #230 and #176 remain OPEN; outcome OPEN_WITH_FORMAL_BLOCKER. Exact #249 and #260 HEAD hosted Research SUCCESS and post-merge main Research SUCCESS are required before accepting either.

**Next C2:** derive an explicitly model-preserving joint GQ-source/physical-target inequality against arbitrary correlated g, OR construct a certified infinite GQ labeling counterfamily, while respecting all seven positive motif families and original-incidence indexing.

---

## Comment 012 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097188441
- GitHub comment ID: 6097188441

### B1-C2 implementation update — [PR #261](https://github.com/definitely-stable/Mathlab/pull/261), exact CI acceptance PENDING

**Restricted all-h Johnson transfer (classical harmonic algebra, not a universal obstruction):**
For every actual GQ-weighted source m_f and arbitrary correlated right physical injection g (including V<K), zero-padding and a permutation extension give an exact pointwise decomposition
```text
U_B/A(f,g) = M*|T_a|/C(K,6) + U2(f,g) + U3(f,g) + U>=4(f,g).
U2 = (q_adj-q_disj)/C(K-4,4)
   * [sum_{i<j} d_ij(m_f) 1[g(i)∩g(j) ≠ ∅]
     -15*M*K*(a-2)/C(K,2)].
U3 = sum_{i<j<k} d_ijk(m_f) r_T3(g(i),g(j),g(k))/C(K-6,3).
```
The five target physical triple-label S_a orbits from #249 determine r_T3 EXACTLY after subtracting target W0/W1=0/W2. This is a joint ORIGINAL source triple marginal × PHYSICAL orbit contraction for every g. Original GQ concurrency triple types (4) are **not** the physical target triple types (5); replacing one with the other is invalid.

**Exact K6 centered target squared-energy split:**
- W2 = 42/11 (~5.53%);
- W3 = 710/1001 (~1.03%);
- W>=4 = 4966/77, exactly 32279/34545 (~93.44%) of centered target squared energy.

The general nonnegative 3-cube source trade proves low marginals do not determine general overlap; it remains NOT a true W(3,s) source. A rigorous source/target Cauchy sufficient positivity gate has been implemented for W2/W3/W>=4 with exact rational norms, but may be vacuous and is not asserted to prove all-right positivity.

**Implementation and independent falsifiers:** all-a 5-orbit target W3 coefficients and energies; exact source 3-marginal harmonic projection and W>=4 norm; brute all 455 K6 target triples and all 5005 physical sixsets, orthogonality checks; independent full 5005 actual W32 original source reconstruction; all 105 original-right label transpositions for U0+U2+U>=3 and four pinned real permutations for full U0+U2+U3+U>=4; exceptional a=9 non-surjective injection; fail-closed invalid inputs; fast GitHub-hosted `hyp105-c2-contract` plus full Research CI.

Upstream #249 has a repaired JSON `Fraction` serializer; #260 hosted unit-suite failure was traced to a test/report key mismatch and fixed in both parent and stacked C2 branches. Full exact-head CI still required; parent #230 and #176 remain OPEN. Outcome: **RESTRICTED_THEOREM_C** for exact harmonic reduction, **OPEN_WITH_FORMAL_BLOCKER** for the original all-correlated seven-family Omega(s^6) or infinite GQ counterfamily. Next C3 must control the genuine higher-order GQ/physical coupling or exhibit an infinite certified witness.

---

## Comment 013 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097436111
- GitHub comment ID: 6097436111

### HYP-105 C3 added — [PR #266](https://github.com/definitely-stable/Mathlab/pull/266), GitHub-hosted CI pending

**New ALL-h restricted joint GQ/physical theorem:** every ORIGINAL B-left/six-distinct-original-right six-incidence E has a UNIQUE doubled ORIGINAL left point p and hence a distinguished ORIGINAL concurrent right-line pair {u,v}. For fixed {u,v}, B-left source witness multiplicity is <=3*C(a-2,4)*(s+1)^4 (physical singleton C4 plus up to Delta^4 original right-neighbor choices). For ANY injective correlated right physical map g with V occupied edges of physical K_a and t=K−V<a missing edges, occupied physically adjacent pairs satisfy the **sharp** star deletion extremal cap

```text
Amax = K*(a-2) - 2*t*(a-2) + C(t,2),
E_GQ = V*s(s+1)/2.
```

Thus original source mass with physically DISJOINT distinguished pair under g is

```text
M_dis(f,g)>=max(0,H_B^-(s) -
      3*C(a-2,4)*(s+1)^4*min(E_GQ,Amax))
          = (1/4-O(s^(-1/2)))*s^15
```

uniformly over ALL legal f,g as s=2^h→∞. This is a true all-correlated **partial source-target** structural restriction. No independence/random-right transfer was used.

**Important firewall:** physically disjoint ORIGINAL witness pair implies q_dis=14*C(a-4,2) *physical target sextet completions containing the two chosen image labels in the FULL K_a target*, but the FOUR other original right line images need not match a completion. This relaxed two-label functional is **NOT** U_B/A, NOT the seven-family S, and NOT full GF5 R3. #230/#176 remain OPEN_WITH_FORMAL_BLOCKER.

**Evidence in #266:** exact proof, complete original W32 witness-multiplicity census by two different algorithms, all 105 real original-right factor label swaps, exhaustive sharp missing-star K6/K7 checks, exact all-h integer falsifiers; separate `hyp105-c3-contract` hosted workflow plus complete Research checks. Exact HEAD CI not yet accepted. The earlier #261 dedicated C2 contract at HEAD 1fb5fc9693cd is SUCCESS; full Research dependency chain pending.

**Next C4:** establish a model-preserving conditional four-remaining-line source/physical-target completion inequality of sufficient order to imply a positive B/A minimum, OR an all-h certified infinite correlated labeling counterfamily respecting all seven classes. Do not treat physically disjoint partial pairs as completed six-edge 2-factors.

---

## Comment 014 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097635267
- GitHub comment ID: 6097635267

### HYP-105 B1-C4 implemented — [PR #269](https://github.com/definitely-stable/Mathlab/pull/269), CI PENDING

**Exact all-h model-equivalent original-incidence conditional B/A transfer.** A genuine B-left six-incidence motif E has ONE distinguished concurrent original right-line pair P(E) at its unique doubled ORIGINAL left point and four remaining ORIGINAL right lines H(E). The exact nonnegative integer tensor b_f(P,H) retains that original six-incidence multiplicity and separates the **actual physical occupied right image** F=g(L_s) from full K_a. For every correlated injective f,g:
```text
U_B/A(f,g) = Σ_{P,H} b_f(P,H) 1[g(H)∈C_F(g(P))],
C_F(z)={Q⊆F\z:|Q|=4, Q∪z∈T_a}.
```
Hence U_B/A=0 iff each positive source P-slice support avoids that P's occupied four-label completion family. **This exact equivalence is for B/A only**, not the entire seven-family S.

**Two classical but exact conditioned permutation moments, with strict quantifier firewall.** For a SINGLE fixed P, freezing its two physical images and the total occupied F, let π_P be a uniform bijection of other V−2 original right factors to F\g(P); N=C(V−2,4). Set b_H=b_f(P,H), w=Σ b_H, q=|C_F(g(P))|, S_j=Σ_{|H∩H'|=j}b_Hb_H', C_j=#ordered pairs of occupied completions intersecting in j labels, D_j=N*C(4,j)*C(V−6,4−j). Then
```text
E X_P=w*q/N,
E X_P²=Σ_{j:D_j>0}S_j*C_j/D_j,
|U_P(w,g)-w*q/N|² ≤ (Σ_H b_H²-w²/N)*(q-q²/N).
```
The last is unconditional for every FIXED g; a positive Cauchy certificate is sufficient but may be vacuous. Importantly, **each P has a DIFFERENT randomization**; summing separate E X_P does not yield E[U(f,G)] under one common G and cannot establish an adversarial all-g lower.

**New constructive occupied completion lemma:** for physically DISJOINT occupied pair edges ab,cd, with t=K−V missing physical labels, let X={x∉{a,b,c,d}: ax,bx∈F}, Y={y∉{a,b,c,d}:cy,dy∈F}. All x≠y yield distinct real 2factors (abx)∪(cdy). Thus
```text
q_F({ab,cd})>=|X||Y|-|X∩Y|>=L(L-1),
L=max(0,a-4-t).
```
In particular t≤a−6 gives ≥2 occupied physical completions for every disjoint pair. Combined with C3, the SUM OF SEPARATELY CONDITIONED RANDOM BENCHMARKS has a conditional Ω_eta(s6) lower along minimal-alphabet sequences with t≤(1−η)a for fixed η>0. This is **NOT a deterministic fixed-g six-factor count**.

**Explicit occupancy blocker:** in K_7 delete the five physical edges (0,2)..(0,6) but keep (0,1),(2,3). These are disjoint occupied anchor labels with positive full-target codegree 14*C(3,2)=42, but occupied q_F=0 because vertex 0 has physical degree one. Illustrative occupancy-only countermodel, NOT a legitimate actual W(3,s) minimal alphabet at a=7.

**Independent falsifiers:** full W32 conditional source by original six-incidence IDs vs an independently implemented doubled-original-point/physical C4/right-neighbor algorithm (10,935 candidates -> 5,000 original distinct-right units); 105 actual original right-label swaps; independent brute target q for all 105 K6 anchor pairs; complete 6!=720 pair-frozen permutations directly verify E, E² and variance; Cauchy, occupied-missing-star, constructive two-triangle capacity and all-h integer benchmarks; GitHub-hosted C4 contract and complete Research CI. PR head not yet accepted.

**Outcome: RESTRICTED_THEOREM_C for exact B/A conditional reduction; OPEN_WITH_FORMAL_BLOCKER for #230 Branch A/B.** No all-g seven-motif Ω(s6), no infinite correlated counterfamily, no GF5 R3 or ASET exponent. Next C5: prove GQ-specific conditional four-other-line mixing with a uniform o(s6) total error for one shared adversarial g, or construct certified infinite f_s,g_s reducing ALL seven families simultaneously.

---

## Comment 015 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097794007
- GitHub comment ID: 6097794007

### B1-C5 implemented — [PR #273](https://github.com/definitely-stable/Mathlab/pull/273), exact-head CI PENDING

**C4 quantifier correction:** instead of separately conditioning and randomly permuting the four remaining right lines for each distinguished pair P (which gives incompatible probability spaces), fix one genuine W(3,s) original B-left/six-distinct-right weighted 6-hypergraph m_f and one arbitrary physically occupied F=g(L_s)⊆E(K_a), |F|=V. Sample **ONE uniformly random common bijection** Pi:L_s→F and count U(Pi)=Σ_R m_f(R)1[Pi(R)∈T(F)].

**New all-h, arbitrary occupied-image density theorem:** K=C(a,2), t=K−V<a due minimality. Accepted target degree of each physical pair edge is D=28*C(a−2,4), target size 70*C(a,6). By union bound over t absent physical pair labels:
```text
|T(F)| >= [70*C(a,6)−28*t*C(a−2,4)]_+
lost_target_fraction <= 12*t/(a*(a−1)) = O(s^(−3/2)).
E_Pi[U|f,F] = M(f)|T(F)|/C(V,6)
           >= (140−o(1))*s^6 uniformly for ALL f and ALL fixed F.
```
**This is a random-common-right map expectation, NOT a lower for fixed correlated adversarial g.** It improves C0's random-right result by freezing ANY chosen occupied image F, even one chosen adversarially with f.

**Exact one-common-Pi second moment, not separate-P moments:** define ordered original weighted sixset intersection spectra S_j and physical occupied target spectra Q_j for j=0..6. Then
```text
E_Pi[U²] = sum_{j:D_j>0} S_j*Q_j/D_j,
D_j=C(V,6)*C(6,j)*C(V−6,6−j).
```
Seven S_j/Q_j computed without quadratic pair enumeration from 64 k-subset marginals per sixset via A_k=Σ_{|Q|=k}(Σ_{R⊇Q}m_R)²=Σ_{j>=k}C(j,k)S_j and binomial inversion. Gives exact variance, Cauchy/Paley–Zygmund random-positive-fraction lower and Chebyshev zero-fraction upper. No all-g minimum.

**Genuine GQ counterexample to identifying global moments with fixed-g overlap:** for one actual W(3,2) source with 5000 ORIGINAL six-incidence units and the SAME complete physically occupied K6 right image, a reverse-line map yields U_B/A=77; swapping physical right labels of original lines (4,13) yields U_B/A=57, while source/F/global E and Var are UNCHANGED because they are computed over the same common-bijection space. This does not refute a positive ALL-g Omega(s6), but rigorously forbids promoting global moments alone to a deterministic fixed-g equality/lower. Exact global uniform mean is 5000*70/5005=70000/1001.

**Independent implementation/falsifiers:** [reference](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-b32e1c5-common-map-second-moment/research/hyp105_g5e2b3e1c5_common_bijection.py), [tests](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-b32e1c5-common-map-second-moment/research/test_hyp105_g5e2b3e1c5_common_bijection.py), [proof](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-b32e1c5-common-map-second-moment/docs/research/HYP-105-G5-E2-B3-E1C5-COMMON-RIGHT-PERMUTATION.md), dedicated `hyp105-c5-contract` + full Research hosted CI. Brute all 8!=40320 **common** right permutations independently verify E, E², Var and probability bounds; brute all K6/K7 six-edge targets independently verify occupancy; actual W32 source and original-right swaps audited. CI not yet completed on PR #273 exact HEAD.

**Prior art:** Bollobás–Scott, *Intersections of hypergraphs*, JCTB 110 (2015), DOI 10.1016/j.jctb.2014.08.002, specifically studies intersections of weighted uniform hypergraphs and concentration under random placement. General moment/intersection-scheme calculation is classical; only the model-specific fixed-image physical-target density transfer is recorded as restricted Mathlab result, not a claimed novel general overlap theorem.

**Outcome: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Next B1-C6: a genuine model-specific **UNIFORM over fixed g** discrepancy bound of strength <(140−o(1))s6 under one shared right mapping, or an infinite certified f_s,g_s with ALL SEVEN GF5-positive motif families o(s6). No seven-family Omega(s6), no full GF5 R3 upper, no ASET exponent, #230/#176/#169 remain OPEN.

---

## Comment 016 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6097815729
- GitHub comment ID: 6097815729

### Integration update: HYP-105 C0 merged, C1 retargeted, C5 implementation under verification

- [PR #249](https://github.com/definitely-stable/Mathlab/pull/249) **MERGED** into main with commit `7a12fabcfd255620ee65bdd743ecb35523ab1c6d`, after exact-head full Research SUCCESS, focused C0 contract SUCCESS and index CI SUCCESS. New main postmerge Research run [38054412390](https://github.com/definitely-stable/Mathlab/actions/runs/38054412390) QUEUED at last check; postmerge acceptance therefore still pending.
- [PR #260](https://github.com/definitely-stable/Mathlab/pull/260) now **targets main**; exact HEAD `1e79a759c30944e85287143deaef9d1c49cdf2ed` has push Research SUCCESS, C1 contract SUCCESS, index SUCCESS; latest PR-head research run cancelled rather than failed. No merge yet pending new main verification.
- [PR #261](https://github.com/definitely-stable/Mathlab/pull/261) C2 has exact HEAD full Research SUCCESS and contract SUCCESS but is stacked downstream of C1.
- [PR #266](https://github.com/definitely-stable/Mathlab/pull/266) C3 full Research and [#269](https://github.com/definitely-stable/Mathlab/pull/269) C4 full Research/contract are not yet accepted.
- [PR #273](https://github.com/definitely-stable/Mathlab/pull/273) C5 proves uniform occupied-right-image **random common-bijection mean** ≥(140−o(1))s⁶ and exact global second moment via seven sixset-intersection classes. C5 dedicated + full CI are QUEUED. Crucially there is NO worst-case fixed-g Ω(s⁶) claim, no entire seven-family proof, and no GF5 R3 exponent change.

**Next allowed integration action**: verify postmerge main Research on exact `7a12fabc...`, then #260 main-targeting acceptance and merge with expected HEAD SHA; retarget #261 to main and continue #266→#269→#273 one by one only after precise CI and merged-base checks. No self-hosted runners, no branch-wide unverified merges. #230 and #176 remain OPEN_WITH_FORMAL_BLOCKER on the original all-correlated seven-family question.

---

## Comment 017 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098106665
- GitHub comment ID: 6098106665

### HYP-105 B1-C6 implemented — [PR #278](https://github.com/definitely-stable/Mathlab/pull/278), hosted Research acceptance PENDING

**Why C6:** C5's exact SECOND moment for ONE common right bijection can be decomposed fully into six Johnson harmonic degrees. Let A_k(h)=Σ_{|Q|=k}(Σ_{R⊇Q}h(R))² for any weighted original-right six-hypergraph h on V vertices (C5 exact marginal squares). Classical Johnson inclusion-matrix eigenvalues yield
```text
A_k(h) = Σ_{r=0}^k C(6-r,k-r)*C(V-k-r,6-k)*E_r(h);
E_r(h) = ||projection W_r h||² >=0,
dim W_r = C(V,r)-C(V,r-1).
```
Triangular rational inversion of SEVEN A_k recovers all W0..W6 energies, with exact Parseval and no dense C(V,6) representation.

For the actual GQ source m_f on original right lines and an arbitrarily fixed physically occupied target t_F under ONE common uniformly random right bijection Pi:
```text
Var_Pi U = Σ_{r>=1} E_r(m_f)*E_r(t_F)/dim W_r
         = EXACT independent C5 seven-overlap second-moment variance.

(1/2)*E_(Pi,tau)[(U(Pi∘tau)-U(Pi))²]
  = Σ_{r>=1} [r*(V+1-r)/C(V,2)]
                *E_r(m_f)*E_r(t_F)/dim W_r,
```
where tau is ONE uniform transposition of ORIGINAL right-line labels. This is an exact mean Dirichlet energy, **not** a worst-case fixed-g bound. **Important additional scope:** full physical K_a target t has W1=0; arbitrary occupied F may break 1-design symmetry and make W1(t_F)>0. Never substitute C2 full-alphabet W1=0 into C5 arbitrary physical F.

**Exact deterministic, potentially vacuous certificate:** for every fixed correlated physical right map g with the same occupied image F,
```text
|U(g)-mu|² ≤ [Σ_{r>=1}E_r(m_f)]*[Σ_{r>=1}E_r(t_F)].
```
If mu² exceeds RHS, positivity is established for that f,F and all permutations g of F, but no such uniform all-h gate has been established. Smaller random variance Σ_r(E_mr E_tr)/dim_r does NOT imply worst-case deviation bounded by sqrt(Var); a single outlier g is allowed. Actual W32 GQ source and occupied full K6 target have fixed overlaps 77 versus 57 under one real original right-factor swap, yet identical all global E_r/Dirichlet statistics. Thus no generic spectral-only fixed-g numerical equality. Not a counterexample to positive all-g Ω(s6).

**Independent executable checks:** exact C5 vs C6 global variance equality; brute squared k-marginal moments for V=7/8/9/12/15; ALL 8!=40320 common permutations and 28 swaps of each = 1,128,960 checked transitions; true W32 target E2=42/11, E3=710/1001, E>=4=4966/77; nonzero W1 for non-surjective occupied F; malformed-original-source rejection. Dedicated `hyp105-c6-contract` and full Research CI created, both PENDING on exact head `4019c25d5ce179fd79e46dd593fa278d90443ec2`.

**Prior art:** Johnson/S_V multiplicity-free decomposition is classical. Sources examined: Iglesias–Natale, arXiv:1704.06299 and Ducey et al., *Integer diagonal forms for subset intersection relations*, Algebraic Combinatorics 8(1), 2025, DOI 10.5802/alco.406. C6 claims model-specific transfer and reproducibility, not new general representation theory.

**Integration status:** C0 [#249](https://github.com/definitely-stable/Mathlab/pull/249) MERGED as `7a12fabc...` with exact-head Research SUCCESS. Its postmerge main Research currently QUEUED. C1 [#260] full Research SUCCESS and targets main; C2 [#261] full Research SUCCESS but stacked; C3 #266 full Research not accepted; C4 #269 and C5 #273 fast contracts SUCCESS, complete Research pending. #230 / #176 / #169 remain OPEN_WITH_FORMAL_BLOCKER. C7 must provide truly GQ-specific uniform fixed-g control (or infinite seven-family counterexample), not merely typical right-bijection estimates.

---

## Comment 018 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098218392
- GitHub comment ID: 6098218392

HYP-105 C7 continuation (2026-10-10): opened stacked [PR #280](https://github.com/definitely-stable/Mathlab/pull/280) on C6 #278. Exact all-h single-global-bijection pinned-prefix expectation and tower identity; deterministic construction of one right g satisfying U_B/A(f,g) <= floor(M(f)|T(F)|/C(V,6)). Genuine W(3,2) source/target acceptance includes an independently recounted fixed-g B/A <=69 vs reverse-line baseline 77, conditioned on hosted CI success. This is *B/A existence upper*, not a seven-family S lower/upper or strict R3 exponent. Independent 720-completion brute and one-hot integer-zero falsifiers. C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 remain unmerged; exact PR-head and postmerge Research CI mandatory. Outcome remains OPEN_WITH_FORMAL_BLOCKER, issue #230 must not be closed.

---

## Comment 019 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098230543
- GitHub comment ID: 6098230543

### HYP-105 B3.2-E1-C7 implementation — stacked PR #279 (2026-10-10)

**Decision: RESTRICTED_THEOREM_C / FINITE_EXACT_GATE, not PROVED_A and not COUNTEREXAMPLE_B.** Extends C0–C6 (#249–#278), no assumption unfinished upstream merges.

1. Exact all-V rearrangement lower bound for the fixed-f,F B-left/A-right-only minimum: the |T(F)| smallest source sixset weights (including zeros). This is an S_N relaxation of the genuinely induced S_V action, not an all-correlated bound.
2. Exact prefix-forced image-sixset count and admissible branch certificate; finite 6≤V≤9 shared-permutation optimization with ZERO_WITNESS, CERTIFIED_MINIMUM, UNKNOWN_BUDGET. Budget exhaustion never becomes a positive proof.
3. Strict finite separation: at V=8, seven unit-weight source sixsets and the target are complements of the seven edges of a star centered at 0. Every genuine S_8 vertex permutation gives overlap 7 or 1 (minimum 1), while the unrestricted sixset-cell rearrangement lower is 0. Independently checked by all 8! true common maps. This is generic finite K8 geometry, NOT a W(3,s) f/F proof.
4. Genuine W(3,2) f,F control: m_f support 3076, target 70 of 5005, relaxation 0, lex/reverse-line fixed B/A values 98 and 77. No 15! search or all-g claim.
5. Exact PR HEAD GitHub-hosted fast + full Research CI PENDING. Only Branch C reduction/oracle advanced. No positive inf_{f,g} S_seven=Omega(s^6), no GF5 full R3, no strict ASET exponent.

PR: https://github.com/definitely-stable/Mathlab/pull/279

Next gate: integrate upstream C1–C6 only with exact-head CI success, then find an all-h GQ-specific deterministic source/physical-target crossing inequality that survives zero-heavy rearrangement.

---

## Comment 020 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098423246
- GitHub comment ID: 6098423246

### HYP-105 C8 implemented — [PR #284](https://github.com/definitely-stable/Mathlab/pull/284) (2026-10-10)

**Status: RESTRICTED_THEOREM_C, all-V exact conditional rearrangement inequality / exact finite toy, not universal GQ obstruction.**

For each fixed legitimate GQ-left embedding f and physical occupied right image F, choose k original right vertices D and injective pinned physical images p:D→F. Every ONE common full right bijection extending p sends each sixset class X_A={R:R∩D=A} bijectively onto Y_{p(A)}. Its source-to-target overlap in this class is bounded below by the sum of the t_A smallest original weights among X_A, including all implicit zeros, where t_A=#target sixsets in Y_{p(A)}. Summing defines L_D(p); exhaustively minimizing over ALL (V)_k p yields valid deterministic L_D ≤ min_g U_B/A(f,g). The hierarchy is monotone in D and is exact for D=[V] (factorial work).

Combining with the independent C5 mean, for THE SAME f,F:
L_D ≤ min_g U_B/A(f,g) ≤ floor[M_f |T(F)| / C(V,6)].
The upper is **existential**, not an explicit winner and not an all-seven-motif bound. Parallel [PR #280](https://github.com/definitely-stable/Mathlab/pull/280) independently develops a conditional-mean selector; not merged into this stack.

**Strict exact finite countermodel to support-only strength:** V=8 star-edge-complement sixsets, each 7 unit weights: C7 rearrangement=0; pin one source center and exhaust its 8 possible images, C8 lower=1; expected-upper=floor(49/28)=1. Thus the true min is EXACTLY 1 without needing 8! enumeration (independently checked against all 40320 full maps). Generic K8 example, NOT genuine W32 source or physical 2-factor target.

**Genuine W32:** C0/C5 source mass=5000, support=3076, full K6 physical target=70 of 5005. C8 reports 0/1/2-pin exhaustive lower (1,15,210 partial images) for lex/reverse-line source, and existential B/A upper floor(350000/5005)=69. Historical actual fixed mappings 98/77 are independent controls, not minima. Numerical values of low-pin lower estimates await exact CI. No claim S_seven Omega(s6), GF5 R3 or ASET exponent.

New GitHub-hosted hyp105-c8-contract and full Research gates are **PENDING exact PR HEAD**. C8 is stacked on #279, behind #278, #273, #269, #266, #261, #260, with #249 merged. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER.

Next research decision: prove an all-h GQ-/physical-2factor-specific nonzero conditional crossing lower for sufficiently small k, OR rigorously show that bounded k always leaves too many zero-mass completions and develop a stronger orbit/cycle-coupling invariant.

---

## Comment 021 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098572016
- GitHub comment ID: 6098572016

### HYP-105 C9 — all-h zero barrier for <=2 pins, PR #285

Outcome: RESTRICTED_THEOREM_C / ALL-h_METHOD_BARRIER, NOT PROVED_A NOR COUNTEREXAMPLE_B.

For EVERY s=2^h >=16, EVERY legitimate original W(3,s) GQ-left f, EVERY occupied physical right-edge image F with |F|=V, and EVERY pinned set D of up to TWO original right lines with EVERY injective image p, the C8 independent sixset-class rearrangement lower L_D(p)=0.

Exact proof source-cover: any positive original sixset contains a concurrent original GQ right-line pair (C1). Fix two pins, r=0/1/2 source pinned members, n=V-2. With GQ concurrence degree d=s(s+1) and E=V*d/2 edges, positive SOURCE SUPPORT in the frozen class is at most E*C(n-2,4-r)+r*d*C(n-1,5-r)+1_{r=2}*W; W=3*C(a-2,4)*(s+1)^4 is the C3 unique distinguished doubled-point pair weight cap. Any physical occupied target class has at most full T=70*C(a,6) physical 2-factors (C0). For r=0/1/2 exact source_support_upper + T < C(n,6-r). Thus each frozen class has enough zero-weight source cells to fill all relaxed target positions: L_D(p)=0 for ALL pinned images.

All-h proof: exact integer cases s=16,32; for ALL s>=64 analytic rational coefficient inequalities yield ratio <28/s+77/s²+163/s³ <1. Below-threshold s=2/4/8 explicitly NOT claimed. NO assertion for k>=3.

This proves a strict NO-GO for the C8 <=2-pin METHOD, NOT the existence of any legitimate g with U_B/A=0. No all-seven S_s lower, R3, or ASET exponent claim.

PR: https://github.com/definitely-stable/Mathlab/pull/285
Dependencies: #249 merged, C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7 #279 → C8 #284 → C9 #285; separate parallel C7 #280 not merged. Exact-head GitHub-hosted dedicated and Research CI pending.

C10: either prove higher-k barriers with genuine GQ conditioned supports or implement a coupled four-line physical completion invariant; no more standalone two-pin asymptotic optimism.

---

## Comment 022 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098635681
- GitHub comment ID: 6098635681

### HYP-105 C10 implemented: the C8 method also fails with THREE pins (PR #286)

Outcome: RESTRICTED_THEOREM_C / ALL-h_METHOD_BARRIER, not PROVED_A and not COUNTEREXAMPLE_B.

For ALL s=2^h>=16, every genuine original GQ left injection f, every occupied physical right image F, every original right pinned subset D with cardinality <=3, and every injection p:D->F, the C8 independent-per-fiber sixset rearrangement lower L_D(p) is exactly ZERO. No actual full right mapping g with U_B/A=0 is constructed or implied.

Compared with C9, an additional original GQ conditioned witness bound applies to a distinguished ORIGINAL right-line concurrent pair {u,v} and a THIRD fixed ORIGINAL singleton right line w: W3=2*C(a-4,2)*(s+1)^4. Each original singleton q on w contributes at most 2*C(a-4,2) physical C4 cycles containing f(q), and the other three ORIGINAL singleton line choices contribute at most (s+1)^3. In the three-pinned case at most three distinguished pairs can occur. The physical target condition also strengthens: if any physical pinned pair-edge must be in the six-edge 2factor, the target class size is <=28*C(a-2,4), the exact full-K_a one-edge codegree.

For r=0..3 in three-pin class of N_r=C(V-3,6-r), source support plus occupied target is strictly less than N_r. Exact integer cases s16,s32; uniform analytic proof for all s>=64:
(B_r+Q_r)/N_r <29/s+113/s²+163/s³ <1.
Hence all frozen fibers admit zero relaxed assignments, regardless of f,F,D,p. The C9 <=2-pin barrier is strictly strengthened. **No conclusion** for k>=4 or full seven-family GF5/ASET.

PR: https://github.com/definitely-stable/Mathlab/pull/286
Stack: #249 merged, #260→#261→#266→#269→#273→#278→#279→#284→#285→#286. Parallel C7 selector #280 remains independent.
GitHub-hosted dedicated + full Research exact-head acceptance pending. Parent #230 OPEN_WITH_FORMAL_BLOCKER.

C11 must use >=4 pinned lines with more refined GQ marginals or use genuinely coupled physical completion constraints for remaining original right lines.

---

## Comment 023 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6098834417
- GitHub comment ID: 6098834417

### HYP-105 C11: coupled four ORIGINAL right lines and exact conditional second moment — PR #288

**Restricted theorem:** for ONE partial injection p of original right lines into fixed occupied physical right-edge labels, the first and second moments of the weighted B-left/A-right sixset intersection over ONE shared uniform completion g are exact. Ordered pairs of original sixsets are grouped by pinned memberships A,B and overlap j among still-unpinned original lines. Their image orbit size is C(n,r)*C(r,j)*C(n-r,t-j), yielding exact conditional E[U^2|p] via source/physical-target pair-orbit contraction. This corrects any interpretation of different C4 per-anchor conditional randomizations as jointly independent.

**Genuine fixed-prefix lower certificate:** for the M=n! common completions, each actual overlap satisfies (U-mu)^2 <= (M-1) Var(U|p), hence min_g extending p U(g) >= max(0,ceil(mu-sqrt((M-1)Var))). The upper floor(mu) is existential for this same prefix. This is not a lower for all unrestricted g.

**First independent GitHub-hosted exact W32 result (C11 Contract SUCCESS on initial PR head):** freeze reverse-line ORIGINAL GQ left f, and freeze right original indices 0..10 in the historical legitimate physical injection. Enumerate ALL 4!=24 simultaneous maps of original right indices 11..14 into remaining occupied K6 pair-edge labels. Every value is independently identical by original C4 doubled-point + FOUR remaining original line source tensor and C5 weighted 6-set / actual occupied target. Historical U_B/A=77; exact restricted 24-map min=56 and max=77, mean=133/2, variance=28. The conditional moment inequality gives guaranteed lower 42 for EVERY one of the 24 maps, and mean yields existence of a continuation <=66. Concrete minimum map is [14,13,12,11,10,9,8,7,6,5,4,0,1,3,2] in canonical occupied K6-edge indexing. Regression values now frozen; new exact PR HEAD CI still required after doc/test commit.

**Not proved:** unrestricted 15!-map min for a fixed f,F, all-f,F all-g GQ B/A positive floor, full seven-class S_s Omega(s6), full 51-column GF5 R3 or ASET exponent. C10 <=3-pin zero-barrier was about a DIFFERENT classwise independent-sixset relaxation, not this genuinely coupled moment.

PR: https://github.com/definitely-stable/Mathlab/pull/288
Dependency: #249 merged, #260 → #261 → #266 → #269 → #273 → #278 → #279 → #284 → #285 → #286 → #288. Parallel #280 separate. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER.

C12 research gate: produce *uniform across all p* model-preserving coupled source/physical-target orbit bounds using GQ incidence and 2factor geometry, or actual infinite correlated family with all seven motifs checked. Exact-head GitHub-hosted dedicated + full Research SUCCESS before merge.

---

## Comment 024 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6099009450
- GitHub comment ID: 6099009450

### HYP-105 C12 — exact model-preserving physical orbit quotient, [PR #291](https://github.com/definitely-stable/Mathlab/pull/291)

**Status: RESTRICTED_THEOREM_C / ALL-h EXACT GROUP-QUOTIENT.** This is a true reduction of the FULL original-to-physical common right map search space, not an independently randomized relaxation; but NOT a universal positive all-f,g lower for S_seven.

For any s=2^h, genuine fixed original GQ-left mapping f, physically occupied F ⊆ E(K_a) with |F|=V and legal common right bijection g, let H=Aut(K_a,F) permute physical coordinate vertices while stabilizing the ACTUAL occupied right-edge set. The induced group H_edge permutes V physical occupied pair-edge labels. For every h in H, U_B/A(f, h∘g)=U_B/A(f,g) **term-by-term**; every one of the SEVEN original six-incidence motif counts is invariant under the same physical coordinate relabeling. H_edge acts freely on FULL right bijections, hence EXACT quotient V!/|H_edge|. Deduplicate the induced occupied-edge actions to avoid nonfaithful coordinate kernels.

For every FIXED original pinned-right set D, image prefixes p and h∘p have *bijective* sets of genuine common full right-map completions, with IDENTICAL complete overlap distributions, minima, conditional C11 first/second moments and seven-class distributions. Thus exact any-p claims need only one representative of EACH H_edge-prefix orbit. The finite oracle checks orbit stabilizers and exhaustiveness, without falsely merging different original pin identities.

**Genuine W32 K6:** V15, group S6 of order 720. Ordered k=0/1/2/3 pinned physical assignments = 1/15/210/2730, EXACT orbit representatives = 1/1/2/9. Full map quotient is 15!/720 = 1,816,214,400 classes, which are NOT exhaustively enumerated. Incomplete actual K6 images with 2 adjacent/disjoint missing physical edges yield stabilizer group orders 12/16 and surviving target counts 21/28: using whole S6 on an incomplete F would be INVALID.

**Separate exact 1-design fact:** when F is the COMPLETE physical K_a pair-edge alphabet (not general s and not incomplete F), fixing one original line to ANY physical edge gives exactly the same shared-map expected B/A as no pins, for every nonnegative original source. This says nothing about actual all-g overlap or conditional variance.

**Hosted C12 dedicated contract SUCCESS at exact first PR head 6b6bd3064f365830c8e2fc87e5bae19533bbc21c: 7 tests passed**, including all 720 edge actions, incomplete occupied F, exact k<=3 orbit/stabilizer identities, actual GQ W32 C11 common 11-prefix conditional second moments under physical relabeling and full SEVEN class count vector. W32 C11 selected SAME-map B/A minimizer has B/A 56 vs historical 77; S_seven 141 vs 169; accepted GF5 lower numerator 6,400,556 vs 7,627,209. This is a necessary lower-floor numerator, NOT the full R3.

Full Research CI on exact PR head remains IN_PROGRESS, and C1-C11 dependency chain OPEN. Parent #230 stays OPEN_WITH_FORMAL_BLOCKER. C13 must find uniform ORIGINAL GQ source/physical target joint constraints across all orbit reps and all f,F, or a certified legitimate infinite counterfamily; exact orbit quotient alone cannot prove positive Omega(s^6).

---

## Comment 025 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6099064852
- GitHub comment ID: 6099064852

### C12 exact orbit-quotiented full-right-map interval for fixed f,F — PR #291 update

Beyond the previously reported all-h physical Aut(F) free-orbit theorem, the C12 implementation now combines **every exhaustive canonical pinned-physical-image orbit** for a selected subset D of named ORIGINAL right lines, with C11 exact conditional 1st/2nd moments of ONE shared common completion and C8 per-fiber lower.

For each canonical orbit representative p, L(p)=max(C11 finite-population joint-variance LOWER, C8 classwise-rearrangement LOWER) is valid for EVERY genuine full common right bijection extending p. Because applying an h∈Aut(F) maps ANY full g into exactly one representative prefix without changing its U, and because the C11 mean guarantees at least one actual full extension with integer U≤floor(E[U|p]), the following is a rigorous bound for the **GLOBAL minimum over ALL V! right bijections g for THAT SAME fixed f,F**:

  min_repr L(p) ≤ min_all_actual_g U_B/A(f,g) ≤ min_repr floor(E[U_B/A|p]).

It is NOT a valid bound uniform in ALL left f or ALL occupied F until those independent constraints are controlled, and concerns B/A only. The implementation checks exact orbit-size-weighted conditional E U and E U² equals the independent C5 full unconditional moments (both equalities, Fraction arithmetic; fail closed if not). Exact enumeration budgets block partial claims.

**Real original W(3,2) reverse-line f, full K6 F, D=(0,1):** all 210 ordered physical two-pin assignments fall into exactly TWO physical S6 orbits. Verified GitHub-hosted C12 dedicated Contract 8/8 SUCCESS on intermediate PR HEAD d28bce53b450e3b5030227dbf2d0953cce5f024f. Global original-right min certified interval **[0,69]** (NOT positive, NOT exact). Exact orbit-weighted unconditional mean=10000/143; second moment=2142290/429, each independently matching C5. Earlier C11 concrete full map with U=56 is compatible with this honest interval. A single-weighted-source-sixset toy gets exact GLOBAL right minimum zero from matching lower/upper without 15! enumerated maps.

These values were frozen in tests and docs, so exact *latest* C12 PR HEAD dedicated and full Research CI need to pass before merge. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER: symmetry + fixed-f,F global B/A interval are NOT all-f,F,g seven-motif Ω(s6), not full GF5 R3 or an ASET exponent. Next requires source GQ structural inequalities or a legitimate infinite counterfamily across all seven classes.

---

## Comment 026 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6099090395
- GitHub comment ID: 6099090395

### C12 global fixed-f,F right-map certificate sharpened by a REAL C11 full-map witness

The exact Aut(F) prefix-orbit quotient plus C11 conditional mean/variance and C8 frozen-fiber lower yields, for EVERY genuine common right g of the SAME fixed source f and occupied physical image F, a lower min over the canonical prefix representatives; the conditional mean gives an existential upper. The dedicated hosted run on prior code HEAD d28bce53... passed 8 tests, independently recovering C5 unconditional mean=10000/143 and second=2142290/429 via size-weighted prefix orbit towers.

For genuine W32 reverse-line f, full K6 physical F, two fixed named ORIGINAL pins D=(0,1), all 210 physical image prefixes collapse to exactly 2 orbits. The method-only bound is **0 <= min_all_actual_g U_B/A(f,g) <= 69**; the lower is zero and is NOT an obstruction. A full legal right bijection was independently exhibited by the true C11 four-line source and physical completion oracle, with actual U_B/A=56. The C12 reference now permits optional **complete** right-bijection witnesses, validates every mapping and directly recounts actual U against its source and target. Therefore the strongest currently available global B/A interval for this **fixed** f,F is **[0,56]**. No claim its true global minimum equals 56.

This improvement is rigorous even without 15! enumeration: it combines valid lower0, the all-orbit conditional mean upper69, and actual verified U56. The same legitimate map also decreases full seven original motif count S_seven 169→141, as independently confirmed in C11/C12. These finite reductions DO NOT prove or refute all-h Ω(s6) of inf_{f,g} S_seven or full GF5 R3.

Latest PR #291 HEAD 18a5dc3402f7e31dccd1564deada063d37ee469e has the explicit-witness validation and regression freeze; exact-head dedicated and full Research CI are QUEUED. **Do not merge until successful checks and sequential C1-C11 integration.** Parent issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 027 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101495029
- GitHub comment ID: 6101495029

### HYP-105 C13 implemented in [PR #292](https://github.com/definitely-stable/Mathlab/pull/292): simultaneous original GQ and BOTH physical half-group exact quotient

**Scientific status: RESTRICTED_THEOREM_C / ALL-h exact equivalence, NOT PROVED_A and NOT COUNTEREXAMPLE_B.**

For all s=2^h and every genuine original incidence column set I of W(3,s), legal injections f:P→F_L⊆E(K_aL) and g:L→F_R⊆E(K_aR), a SINGLE part-preserving ORIGINAL GQ incidence automorphism sigma=(sigma_P,sigma_L), together with independent physical coordinate automorphisms hL∈Aut(F_L), hR∈Aut(F_R), acts by f'(sigma_P(p))=hL(f(p)), g'(sigma_L(l))=hR(g(l)). This bijects the ACTUAL original six-incidence sets and preserves EACH of all seven original motif counts and the accepted GF5 necessary-floor numerator, rather than independently changing right labels for each motif. No universal all-f,g Ω(s6) or full GF5 R3 is inferred.

The exact JOINT orbit of a full (f,g) pair under G=Aut(GQ)×H_L^edge×H_R^edge (induced physical-edge actions must be deduplicated) has size |G|/stab(f,g), which is not automatically |G|. For fixed sigma the physical hL and hR returning the full physical bijections to themselves are UNIQUELY forced, allowing exact stabilizer computation by looping only over original sigma. A full W32 canonical normal form minimizes both independent physical action images across every SAME original sigma; equal keys iff in the same joint orbit. Hard cap rejects partially enumerated groups.

**Actual W32 independent executable evidence**: original Sp(4,2) action of order 720 independently enumerated by 15×8×3×2 true GF2 symplectic bases and checked against every one of 45 GQ incidences. Original point/line pair orbit types are 45 incident flags and 180 antiflags. Full K6 physical left/right S6 actions each order720; combined |G|=720³=373,248,000. Initial PR-head GitHub-hosted dedicated Contract SUCCESS 7/7; historical reverse-line mapping pair has stabilizer 1 and orbit exactly 373,248,000. Canonical normal form invariant under nonidentity original/left/right triple, seven-class S original/transformed=169 and GF5 necessary-floor numerator=7,627,209.

**NEW exact shared left/right one-pin classification**: 50,625 ORIGINAL point+line + physical left edge + physical right edge choices form just TWO actual joint orbits, size 45·15²=10,125 original incidence flags and 180·15²=40,500 antiflags. Retains ORIGINAL incidence, does NOT conflate with physical edge adjacency. **Computational kill gate**: (15!)² complete W32 mapping pairs, each triple-group orbit has at most 720³ members, so number of genuine JOINT mapping-pair orbits >= **4,581,437,148,288,000**, even with full symmetry quotient. Therefore merely enumerating canonical pairs cannot settle even finite all-f,g W32 with available CI resources. C14 must find stronger coupled positive inequalities, valid branch pruning/proof certificates, or another analytic avenue; symmetry alone is insufficient.

**Fail-closed correction:** arbitrary bijections of 15 physical PAIR-EDGE IDs are legal alternate mappings but NOT necessarily graph automorphisms. C13 transport now explicitly rejects any physical edge action not induced by a genuine physical coordinate permutation; canonicalization rejects missing physical group actions. Negative regression tests added and latest exact HEAD CI is pending.

Stack C0 #249 merged → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7-A #279 → C8 #284 → C9 #285 → C10 #286 → C11 #288 → C12 #291 → C13 #292. Parallel C7-B #280 remains separate. Parent #230 OPEN_WITH_FORMAL_BLOCKER. Do NOT merge before exact latest HEAD dedicated + full Research SUCCESS and ordered prerequisite integration.

---

## Comment 028 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101502790
- GitHub comment ID: 6101502790

### C13 exact latest PR HEAD acceptance progress — hosted dedicated SUCCESS 9/9

PR #292 https://github.com/definitely-stable/Mathlab/pull/292 HEAD 4f63d78203bb064759f6df6a5c4320ae6cb59b00. GitHub-hosted **hyp105-c13-contract** run https://github.com/definitely-stable/Mathlab/actions/runs/38081042422 is **SUCCESS**, nine independent unit tests in ~17s, plus successful true W32 report. Both negative symmetry gate tests passed: arbitrary swaps of 15 PAIR-EDGE IDs not induced by a physical K6 coordinate automorphism are rejected; incomplete physical group enumerations are rejected.

Reported exact true W32 group data: ORIGINAL Sp4(2) automorphisms720, physical left S6=720, physical right S6=720; original original-incidence flags45/nonincidence antiflags180; joint named-pin physical orbit sizes 10,125 and 40,500; combined group order373,248,000, actual historical map pair stabilizer1 and orbit373,248,000; strict universal COUNTING lower for number of genuine full two-sided mapping-pair orbits at least **4,581,437,148,288,000** (no such full orbit enumeration attempted). Exact whole-seven original S169 preserved under a simultaneous nonidentity GQ/left/right transformation and GF5 accepted necessary-floor numerator unchanged.

**NOT YET ACCEPTED/MERGED**: full Research on exact HEAD still queued/in_progress and upstream C1–C12 stack not sequentially integrated. No all-f,g positive seven-family Ω(s^6) or full GF5 R3 bound proved. C14 must seek model-preserving pruning/structural inequalities, not brute-force orbit enumeration.

---

## Comment 029 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101594392
- GitHub comment ID: 6101594392

### C14 implemented: sound partial left/right GQ six-incidence domain minima, [PR #296](https://github.com/definitely-stable/Mathlab/pull/296)

**New restricted result — ALL actual full common completions of ANY finite partial joint node, not a universal all-h obstruction.** For a partial legal original GQ left physical-edge injection f0 and original right physical-edge injection g0, enumerate ORIGINAL six-incidence sets J with ALL touched ORIGINAL left point labels already fixed and whose physical left six-edge projection can be accepted. For each J let D_J be ALL locally injective ways to map its touched yet-unpinned ORIGINAL right line IDs into currently unused physical right-edge labels, and evaluate the ACCEPTED complete seven-class classifier on its exact original 6 incidence IDs. Define a_J=min_(rho∈D_J)1[the sixset belongs to one of seven accepted motifs], and b_J=min_(rho∈D_J)accepted classwise GF5 NECESSARY floor numerator (zero when unselected). Then for EVERY ONE LEGAL COMMON full joint (f,g) extending the partial node, S_seven(f,g)>=sum_J a_J and GF5 accepted necessary-floor numerator>=sum_J b_J. Reason: the actual single shared full g restricts to an option in EACH D_J, so its contribution dominates every local minimum. Individual minimizing rho choices are NOT claimed simultaneously realizable. Other original sixsets contribute nonnegative amounts.

**Monotonicity under legal partial extension:** eligible original left-pinned witness sets remain eligible; their right local domains shrink, so minima cannot decrease; newly eligible sixsets add nonnegative minima. This yields an exact incumbent-based BnB prune: any node lower >= an actual full-map incumbent can be eliminated without missing a strictly better mapping pair. An important implementation correction disallows treating lower>an incumbent from a DIFFERENT subtree as an invariant violation; it is a legitimate prune condition.

**Finite W32 physical K6 implementation:** uses existing exhaustive 62,370 original left 2factor candidate generator, retains ORIGINAL symplectic W32 incidence IDs, and directly evaluates the accepted seven-family classifier and certified GF5 necessary floors for each valid locally injected RIGHT completion. Hard cap of three unpinned original right lines and a cumulative local-classification budget raise on overflow; no truncated 'complete' certificate. Two independent exact completion boxes: 13 left +13 right original pins (2!²=4 legal full mapping pairs), and 12+12 pins (3!²=36 legal full pairs), tested using the existing complete seven_census for EACH actual map and independently via exact branch-and-bound. Zero-unpinned lower must equal actual full S_seven and accepted GF5 numerator. All seven and GF5 minimum scopes explicitly separated.

**No all-f,g conclusion**: C13 proved >=4,581,437,148,288,000 complete W32 joint-orbit classes after the entire three-group symmetry quotient. C14 computes exact bounded-box minima, not the entire global optimization or any all-h Ω(s^6) seven-family theorem. The next productive step C15 is to retain coupling among MULTIPLE original six-incidence witnesses, e.g. clusters of overlapping original right lines and physical 2factor codegrees, rather than separately minimizing each witness. C14 is an admissible baseline to measure whether stronger coupled floors actually prune earlier.

PR #296 stacks on C13 #292 (then C12 #291, C11 #288 etc). Dedicated hyp105-c14-contract and full Research GitHub-hosted checks QUEUED/IN_PROGRESS on original PR HEAD f25e145ce1d36cbc34e3e30620e8775d57944ba2. No merge, no main changes, no inflated acceptance. Parent #230 stays OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 030 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101631325
- GitHub comment ID: 6101631325

### HYP-105 C14 — independently verified exact 36-map W32 joint box, [PR #296](https://github.com/definitely-stable/Mathlab/pull/296)

Dedicated hosted [run 38081738228](https://github.com/definitely-stable/Mathlab/actions/runs/38081738228) on initial PR head f25e145... completed **SUCCESS, 6/6 tests**. Sound lower theorem: for any partial actual original-GQ point and line physical K6 injections, take every ORIGINAL six-incidence candidate with all original LEFT endpoints pinned, and sum the minimum seven-family 0/1 indicator and separately the accepted GF5 necessary-floor numerator over all locally injective still-available original RIGHT endpoint physical labels. Every true COMMON full g restricts to an allowed local choice; thus every actual joint full (f,g) descendant dominates the sum. Per-source choices need not form one joint global map; NO fictitious witness is asserted. Both bounds are MONOTONE as legal physical labels are pinned. Certified node lower>=actual complete-map incumbent legally prunes the whole subtree.

**Actual finite true symplectic W32 reverse-line f,g rooted box:** first12 ORIGINAL left point labels and first12 ORIGINAL right line labels fixed; exactly 3!²=36 genuine full two-sided mapping pairs. INDEPENDENT complete seven_census on ALL36 confirms exact box minimum S_seven=**148**, exact minimum accepted GF5 necessary numerator **6,676,842**. ROOT local sixset lower = only **2** guaranteed seven motifs (2 entirely frozen), GF5 necessary numerator lower **91,200**, exposing large residual relaxation gap. Distinct rigorous branch-and-bound finds the SAME exact S_min148 after visiting **73** nodes, explicitly recounting just **3** complete leaf maps, and soundly pruning **33** subtrees. This is observed for this small rooted box and not an all-f,g branch complexity bound. A valid C11 W32 full map outside this box has S_seven141, so 148 cannot be elevated to a global minimum.

PR #296 is now on head bce72e37a4766558b3d758035a0caa9374c9c414, which adds frozen exact numerical regression gates and an independent GF5 objective full-box solver test. Newest exact-head dedicated CI and full Research checks QUEUED, prior head's dedicated SUCCESS does not establish current head acceptance. No merge until exact head dedicated+full Research SUCCESS and the C1–C13 dependency chain is integrated in order. Parent #230 OPEN_WITH_FORMAL_BLOCKER; no universal Ω(s^6) or full GF5 R3, and no ASET exponent.

C15 decision: leave pure symmetry and weak independent local-sixset envelope behind as primary proof routes. Study coupled clusters of ORIGINAL source six-incidence witnesses, physical 2factor codegrees and GQ concurrence with a provably stronger lower that remains informative at shallower partial embeddings. Benchmark on SAME fixed 36-map independent oracle and on non-prefix / genuine alternative f,g samples to prevent overfit.

---

## Comment 031 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101829127
- GitHub comment ID: 6101829127

### HYP-105 C15 implementation — [PR #300](https://github.com/definitely-stable/Mathlab/pull/300), exact coupled ORIGINAL-right witness clusters

**Theorem (restricted all-finite, exact true W32 executable):** For any legal partial ORIGINAL GQ point→physical-left and line→physical-right pair-edge injections (f0,g0), let W be the distinct actual ORIGINAL six-incidence candidate sets whose every ORIGINAL left endpoint is already pinned. Let P denote ALL complete injective bijections of currently unpinned ORIGINAL right lines to currently unused physical-right labels. For each J∈W and one shared π∈P, evaluate the accepted seven-family class indicator χ_J(π)≥0 and accepted GF5 NECESSARY numerator w_J(π)≥0 on that SAME actual original incidence set. Partition W by its exact touched UNPINNED ORIGINAL right-line signature M_J. Because groups are disjoint, for every actual full common (f,g) descendant:

   Σ_J min_π χ_J(π) ≤ Σ_M min_π Σ_(J:M_J=M) χ_J(π) ≤ min_π Σ_J χ_J(π) ≤ S_seven(f,g).

Identical inequalities hold for GF5 necessary numerator. Leftmost is EXACTLY C14 per-sixset lower (every local right injection extends to a full π), middle couples a common right assignment INSIDE each original-signature witness cluster, last uses ONE SAME full right permutation for ALL already-left-pinned source witnesses. None of the separately attained local/cluster minimizers is spuriously presented as one global witness. Both strengthened bounds are monotone under any legal left/right pin extension; the last is mathematically maximal for the currently eligible source witness subset, NOT necessarily the entire S if unpinned original LEFT points touch omitted source motifs.

**Finite actual W32 tests:** strict original symplectic W32 full K6/K6 mapping boundary, 62,370 original left 2factor candidate source sets; exactly all residual original RIGHT g permutations (<=3! at this phase), no per-motif independent global target assignment. Three bounded same-order BnB proof policies single/cluster/shared; independent actual `seven_census` complete original 3!²=36 joint map oracle from C14 (known S min148, accepted GF5 necessary floor min6,676,842) plus original 2!²=4 box dual seven/GF5 exact objective test. Fail-closed hard bounds on source-right degree, classifications and branch nodes. Whole W32 source if fully pinned must recover the accepted exact seven S and necessary GF5 numerator. The dedicated and full Research GitHub-hosted checks are IN_PROGRESS on PR head f69719edd85c79ff50bb5d53a680085d4681c2ec; no numeric improvement has been claimed yet.

**Scientific kill gate:** if C15's one-right-coupled root estimate remains weak because most original source witnesses touch UNPINNED ORIGINAL LEFT points, stop extending only right clustering. Next C16 must investigate two-sided coupled original-left/right incidence witness families and physical K6 two-factor codegree with rigorous CI falsification. Parent #230 OPEN; no positive universal all-h Ω(s6), no global 15!² W32 optimum and no full GF5 R3 or ASET exponent.

Research stack C0 #249 merged → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7-A #279 → C8 #284 → C9 #285 → C10 #286 → C11 #288 → C12 #291 → C13 #292 → C14 #296 → C15 #300. Parallel #280 not an ancestor. Do not merge until exact-head dedicated+full Research SUCCESS and upstream dependencies reviewed in order.

---

## Comment 032 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101875980
- GitHub comment ID: 6101875980

### C15 EXACT hosted progress — physically correlated RIGHT original lines produce strict, independent W32 improvement

GitHub-hosted [C15 dedicated Contract run 38083573985](https://github.com/definitely-stable/Mathlab/actions/runs/38083573985) on initial PR #300 HEAD f69719edd85c79ff50bb5d53a680085d4681c2ec was **SUCCESS 6/6**, including independent full 36-real-joint-map falsification. Its separate full 3-mode same-map benchmark ran SUCCESS, returning exact actual original W32 reverse-line 12-left-original/12-right-original pinned 3!²=36 box:

- 6,723 original six-incidence witnesses with all LEFT original endpoints pinned; remaining 55,647 source candidates necessarily touch an UNPINNED original left point and are conservatively excluded. Exactly 8 disjoint ORIGINAL touched-missing-right-line signature clusters and 3!=6 full common right label completions.
- Root S_seven deterministic bound improves C14 independent2 → C15 same-right-signature8 → C15 ONE GLOBAL shared right completion12. This follows from the exact proven Σmin ≤ minΣ hierarchy for ORIGINAL six-incidence disjoint witness clusters and a shared right map.
- Accepted GF5 NECESSARY numerator root lower improves 91,200 → 370,950 → 513,393. Not actual full GF5 R3.
- Same independent TRUE full 36-map box optimum S_seven=148, GF5 accepted necessary numerator minimum6,676,842. All three BnB modes independently recover S_min148 with exactly 3 explicit full map leaves recounted, visiting 73/46/34 nodes respectively and pruning 33/19/12 subtree ROOTS. Node visits drop 53.42% for the shared mode. Fewer pruned roots does NOT imply weaker pruning because many subtrees are never visited at all.
- **Scientific limit**: root lower12 is still far below actual minimum148; dominant missing contributions involve UNPINNED ORIGINAL LEFT GQ points, so C16 must use TWO-SIDED left/right coupled witness domains and not more right-only conditional permutations. This is a finite pinned-prefix result; the global inf_{all f,g} S_seven=Ω(s6) issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

All results are now frozen as exact GH source/test/docs regression gates on latest PR #300 HEAD 65baed8bfea058b0d4115dc8cc02342f7f84a303. This updated HEAD needs its own GitHub-hosted dedicated and full Research SUCCESS; the earlier SUCCESS is not inherited. PR #300 STACKED after #296 C14 and dependencies C0–C13; no direct main changes or merge. Full Research on ancestor C14 had cancelled runs even though dedicated passed; do not overstate acceptance.

---

## Comment 033 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101901822
- GitHub comment ID: 6101901822

### C15 latest exact PR HEAD dedicated acceptance — SUCCESS 6/6

[PR #300](https://github.com/definitely-stable/Mathlab/pull/300) exact **HEAD 65baed8bfea058b0d4115dc8cc02342f7f84a303** passed Github-hosted [hyp105-c15-contract run 38084003927](https://github.com/definitely-stable/Mathlab/actions/runs/38084003927) **SUCCESS** (6/6 unit tests, independent complete true-original-W32 three-mode benchmark and frozen numerical comparison). Confirmed directly from exact-head job logs:
- root S lower 2 (C14 individually) → 8 (C15 exact touched-original-right-line signature disjoint witness clusters) → 12 (C15 ONE common residual right map);
- GF5 ACCEPTED NECESSARY numerator root lower 91,200 → 370,950 → 513,393;
- 6,723 original six-incidence witnesses have all-original-left endpoints pinned out of 62,370 candidates, with 8 exact unpinned-original-right-line signature clusters, 6 common right completions;
- BnB visited nodes 73 → 46 → 34; 3 genuine complete leaves recounted in all three modes, soundly pruned subtree roots 33/19/12; 53.42% fewer nodes for shared vs single on identical rooted 36-legal-map box;
- all independent full 36 actual joint (f,g) maps certify true box min S_seven=148, and accepted GF5 NECESSARY numerator min=6,676,842.

**Dedicated exact-head SUCCESS is now confirmed.** Full Research on this same SHA remains IN_PROGRESS and must NOT be called success until it completes. Independent issue #277 proposes splitting the Research CI single 10-minute job into four hosted jobs; prior C14 all-tests Research on exact head was CANCELLED in its broad Unit tests step, not mathematically failed. Keep #300 stacked and do not merge until exact-head full Research SUCCESS and ordered ancestor integration. Parent #230 remains OPEN, with all-f,g universal all-h Ω(s6) and full GF5 R3 still unresolved.

Next scientific C16: two-sided ORIGINAL GQ left/right witness cluster domains because 55,647 of the 62,370 potential left 2factor structural candidates touch currently unpinned ORIGINAL left points, dominating root relaxation gap 12 vs 148.

---

## Comment 034 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6101965548
- GitHub comment ID: 6101965548

### C16 continuation — PR #305 created, exact HEAD acceptance pending

[PR #305](https://github.com/definitely-stable/Mathlab/pull/305) is stacked directly on C15 [#300](https://github.com/definitely-stable/Mathlab/pull/300), not main. No merge, no global mathematical status promotion.

**Found and addressed the actual source obstacle:** unlike C15's 6,723 frozen-left original sixsets, the other 55,647 source candidates are NOT a completion-invariant set; the physical left 2factor sixset enumerator changes with the unpinned ORIGINAL left point→K6 edge bijection. C16 re-enumerates 62,370 distinct ORIGINAL six-incidence candidates for EACH genuine full left tail, pairs it with each genuine full right tail, and counts only the truly selected J (zero when ineligible). There is no canonical-fill or per-motif fake full map assumption.

Proved and implemented the finite conditional hierarchy (separately for accepted seven indicator and nonnegative GF5 NECESSARY floor numerator):

```text
L_C15_shared_eligible
 <= L_C16_named_left_right_signature_clusters
 <= L_C16_named_left_group_minima
 <= L_C16_one_shared_left_groupwise_right
 <= L_C16_exact_full_joint_box
 <= S_seven(actual same full f,g)
```

The same ordered chain applies to accepted necessary GF5 numerator. Six-incidence witnesses are deduplicated by ORIGINAL factor-edge IDs; the signature partition is by the touched unpinned ORIGINAL left and right vertices. Each group is minimized using one common actual left/right injection; discarded signatures do not artificially generate a real joint witness. All lower bounds are monotone under compatible pin extension. The final level is exhaustive in the finite rooted box and is NOT a fast global or all-h result.

**Independent falsification:** actual W(3,2)/K6×K6, 3!²=36 real joint full mapping descendants; all 36 scores independently recounted with accepted `seven_census` and compared per-map, adversarial different-left-filler source memberships, prefix monotonicity, fully pinned equality, GF5 and S, fail-closed 36-map/2,500,000-classification caps. Previously frozen C15 root anchors S=12 / GF5 numerator=513,393; known exact rooted minimum S=148 / GF5 numerator=6,676,842. Do not invent C16 *intermediate* values before exact-head hosted results.

**Acceptance status:** dedicated `hyp105-c16-contract` + full Research exact HEAD GitHub-hosted SUCCESS required; #277 CI sharding still independent/open, C1–C15 integration still pending. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER. No universal Omega(s^6), full GF5 R3, or ASET exponent claimed.

---

## Comment 035 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102127011
- GitHub comment ID: 6102127011

### HYP-105 continuation — C16 hosted PASS, next C17 scientific PR and CI lossless-shard PR

**C16 now has exact-head GitHub-hosted focused SUCCESS**: scientific [PR #305](https://github.com/definitely-stable/Mathlab/pull/305) HEAD 2c6a2d2a0a2908e80a756d8d1abbeadaf19c9239; dedicated [run 38084811013](https://github.com/definitely-stable/Mathlab/actions/runs/38084811013) and independent repeated [run 38084808258](https://github.com/definitely-stable/Mathlab/actions/runs/38084808258) both concluded SUCCESS, as did INDEX. Broad monolithic Research remains incomplete (status cannot be promoted).

**CI unblocking [PR #306](https://github.com/definitely-stable/Mathlab/pull/306)** stacked on C16, not on main: identified that old #277 retained 77 original commands but could delete 30 newer C1–C15 commands if merged as-is. Matched all original 77 (name,run) pairs exactly with 107 current pairs; preserved all 107 and added C16 explicit independent unit/report commands, yielding **109 unique commands** split over six GitHub-hosted jobs (26/23/13/15/20/12), fail-closed aggregate seventh verdict requiring all six SUCCESS. Independent frozen workflow regression enforces full 109 command fingerprint. Exact-head hosted six-job CI is running; no acceptance claim yet. Do not blindly replace research.yml with old #277.

**Scientific [C17 PR #308](https://github.com/definitely-stable/Mathlab/pull/308)** stacked directly on C16 (parallel to #306): proves ORIGINAL sixset factor-support locality for any finite original bipartite incidence host. For each distinct J, seven-class indicator and accepted GF5 necessary numerator depend only on images of original point/line endpoints touched by J. Partition ORIGINAL sixsets by missing-left/missing-right source IDs, and minimize each group over local injective physical pair-label assignments; every local assignment extends globally. Thus L_poly=sum_group min_local cost <= S_seven(f,g) for EVERY one true joint descendant (similarly GF5). Fixed sixset size admits a polynomial (but high-degree) O(|I|^6 V_left^6 V_right^6) direct local enumeration, rather than V_left! V_right! complete assignment enumeration. The W32 executable builds local two-sided support tables, rather than a full joint score matrix, and independently falsifies against C16's full genuine 36/4-map boxes. It also retains optional C15 one-common-right baseline, proving L_poly<=L_C17_shared_right==L_C16_two_sided_signature. **Only pure L_poly has the polynomial-local evaluation claim; the shared-right enhancement may still be factorial**.

C17 dedicated and full hosted CI are pending; new intermediate lower numbers MUST NOT be claimed before exact-head SUCCESS. Scope is RESTRICTED_LOCALITY_THEOREM, not #230 Branch A/B/C proof completion. Global all-s positive Omega(s6) remains OPEN_WITH_FORMAL_BLOCKER. Next C18 must prove a positive all-h lower for L_poly or a formal obstruction to this relaxation, never infer a new ASET exponent from W32.

---

## Comment 036 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102164649
- GitHub comment ID: 6102164649

### HYP-105 C18 — all-h restricted NO-GO discovered and implemented ([PR #310](https://github.com/definitely-stable/Mathlab/pull/310))

While turning C16's two-sided signature relaxation into C17 support-local tables [#308](https://github.com/definitely-stable/Mathlab/pull/308), an exact analytic obstruction emerged: the C17 **pure-local** certificate is **ZERO** for every s=2^h when there are **NO ORIGINAL LEFT POINT PINS**, regardless of any pinned original RIGHT lines and regardless of the occupied physical edge set F of the required size.

**Proof for ALL h (not finite extrapolation):** V=(s+1)(s²+1), a=min{a: C(a,2)>=V}, and V>2a for every s=2^h>=2 (s2: V15/a6; s>=4: a>=7 and V>C(a−1,2)>2a). For every occupied physical F⊆E(K_a) of size V, handshaking gives max physical star degree >=5. Any distinct ORIGINAL six-incidence witness J touches k distinct original LEFT points, 1<=k<=6. Fix its named LEFT-support signature U. For k<=5 injectively assign all U to k physical pair edges from one occupied five-star; the star coordinate then occurs **six** times in the physical projection of EVERY sixset with that same U. For k=6 assign five to star and one to any sixth occupied pair edge; the coordinate occurs at least **five** times. Both violate the necessary physical-left two-factor degree2 constraint. One such LOCAL left map kills all motifs of the entire shared U cluster, independently of g; therefore each independently minimized two-sided (U,V) group has zero accepted seven and GF5 necessary score, giving the exact pure-local L_poly=0 for all h.

**NONTRANSFER:** distinct U clusters may require incompatible physical left star assignments. This is NOT a single allowed global f,g with S=0, NOT a counterexample to universal Omega(s6), NOT #230 Branch B or a full R3 upper. It is a rigorous universal NO-GO for the **particular empty-left-pin independent source-signature relaxation** proposed by C17, analogous in proof-status discipline to the earlier C9/C10 low-pin barriers. Even right-coupling cannot help its empty-left root, because no J has empty original left support.

**Implementation:** separate C18 PR #310 stacked on C17, exact integer star-density oracle, independent k=1..6 multiplicity patterns, adversarial incomplete physical F for s4, real original symplectic W32 left A/B/C source families and independent classifier falsifiers. Dedicated C18 hosted exact-head contract and broad Research queued; no PASS/merge claimed yet.

**Decision gate / C19:** STOP treating pure-local signature minima as a possible all-h Omega(s6) route. Require joint left assignment across DISTINCT original left supports, e.g. shared-left C16 constraints, or a new dual inequality that defeats clusterwise star sabotage. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER; no ASET exponent change. Parallel CI repair [#306](https://github.com/definitely-stable/Mathlab/pull/306) preserves 109 commands and introduces an all-shard aggregate verdict; it is currently running.

---

## Comment 037 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102279239
- GitHub comment ID: 6102279239

### C19 implemented — all-h TWO-ANCHOR shared-left block no-go [PR #312](https://github.com/definitely-stable/Mathlab/pull/312)

Scientific stack: C16 #305 → C17 #308 → C18 #310 → C19 #312. Parallel CI-only #306 has **full GitHub-hosted Research SUCCESS on its exact HEAD** (109 preserved named commands in six research shards + aggregate); it has NOT been merged into the scientific branch. C19 no main modifications or merges.

**C19 ALL-h restricted theorem:** for s=2^h>=2, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}, physical occupied left image F⊆E(K_a) of size V, put t=C(a,2)-V<a−1. Missing physical edge graph has total missing degree 2t<2(a−1), so TWO distinct physical coordinates x,y each have at most ONE missing incident edge. Thus the occupied two-anchor double-star, i.e. occupied edges meeting {x,y}, contains >=2a−5 labels. For s2 full K6 it contains exactly 9. Define B(s)=9 (s=2), 2a−5 otherwise =Theta(s^(3/2)).

Take ANY family W of DISTINCT ORIGINAL six-incidence witnesses with TOTAL union U of named ORIGINAL left points |U|<=B(s); this may include MANY different C17 original-left support signatures with arbitrarily overlapping incidence supports. Choose ONE SAME injective left physical map from ALL U to |U| distinct occupied double-star edges. Every one of the SIX physical left edge occurrences of each J∈W hits x or y. Therefore deg_J(x)+deg_J(y)>=6, whereas an accepted physical-left 2factor forces BOTH degrees<=2 and their sum<=4. Every J in the ENTIRE W block is ineligible together, regardless of the fully shared original-right map. Hence ANY scheme summing independent minima of blockwise nonnegative seven and accepted GF5 necessary contributions has exact ZERO lower at NO ORIGINAL LEFT PINS when EACH block's total named left-point union is <=B(s).

**Stronger than C18:** the NO-GO is not restricted to each motif/signature separately: it defeats one-common-left-and-right-injection optimization WITHIN every small block. It forces >Theta(s^(3/2)) named LEFT support per independently minimized group, OR true cross-block globally consistent LEFT labels, to have any chance at positive universal root floor.

**Critical scope:** these per-block double-star left assignments can be incompatible BETWEEN blocks; C19 constructs NO real globally consistent full f,g with S=0, disproves NEITHER Branch A nor Branch B, establishes no full GF5 R3 and no ASET exponent. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER.

C19 source, independent 7-suite numerical/palette/invalid tests, real original symplectic W32 nine-left-point jointly relabeled 62,370-candidate census baseline-positive→0 falsifier, formal all-h proof, dedicated GitHub-hosted Contract, and research registry are in PR #312. Exact-head CI is NOT YET VERIFIED and must pass. Next C20 should target genuine inter-block left-image consistency at >B(s) source scale.

---

## Comment 038 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102312339
- GitHub comment ID: 6102312339

### C19 exact-head status and six-shard follow-up

First hosted C19 Contract run 38087058039 on ancestor HEAD ea47d893 failed one test-fixture typo: a tuple() call in the synthetic GF4 matching case was supplied six arguments instead of a tuple literal. The other five tests, including independent original W32 62370-candidate nine-left-point source falsification, succeeded. Corrected C19 PR #312 HEAD d50edec7e864d6b5ac3729d505161d249ed88ae3 changes the test fixture only. Dedicated and monolithic Research exact-head checks are QUEUED: no fabricated PASS or inherited acceptance.

CI-only PR #314 is stacked on the corrected C19 head. Its Research workflow losslessly retains 107 original named run checks, plus 2 C16 checks from fully-green PR #306, plus 6 C17/C18/C19 independent tests/reports: 115 unique commands in six separate GitHub-hosted shards, with fail-closed seventh aggregate research-full-suite. New exact pair-fingerprint guard prevents removed/altered commands. Exact-head six-job Research CI is still queued; do not merge to main until hosted checks are SUCCESS and scientific dependencies are integrated in order.

C19 is a restricted all-h NO-GO for independently minimized shared-left witness blocks whose combined named ORIGINAL LEFT support is at most B(s)=Theta(s^1.5). It is neither one global low-S original f,g family nor a positive Omega(s6) theorem. Parent #230 OPEN_WITH_FORMAL_BLOCKER. C20 must couple left assignments across larger original support or establish a global structural inequality.

---

## Comment 039 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102317369
- GitHub comment ID: 6102317369

### C19 exact-head dedicated acceptance confirmed

Scientific PR #312 exact HEAD d50edec7e864d6b5ac3729d505161d249ed88ae3 passed GitHub-hosted [hyp105-c19-contract run 38087146666](https://github.com/definitely-stable/Mathlab/actions/runs/38087146666): SUCCESS, all 6 independent tests plus separately executed genuine W32 report. The earlier ancestor test-fixture TypeError is fixed and does NOT survive on accepted dedicated HEAD.

A useful frozen *observed* genuine W(3,2) fact from the actual runner log: the same nine named ORIGINAL left points (chosen to include one genuine physical K6 six-cycle) support exactly **1,296** original left 2factor six-incidence candidates under historical reverse-line physical labels; assigning ALL nine original points injectively into one occupied physical K6 two-anchor double-star reduces the independent historical 62,370-candidate source count on that same named block to exactly **0**. This is an actual bounded-block witness of the universal method obstruction, NOT an entire 15-original-point globally correlated f,g zero result.

Proof remains ALL h via minimal physical a, t=C(a,2)-V<a−1, two coordinates incident to at most one missing edge each, and occupied two-star capacity B(s)=9 at s2 else >=2a−5=Theta(s^(3/2)); all J in one ORIGINAL named-left block of size<=B mapped together satisfy deg_J(x)+deg_J(y)>=6, impossible for any accepted left 2factor. The independently minimized blocks may choose incompatible left maps. No issue #230 Branch A/B/C closure or new ASET exponent.

Full monolithic Research for C19 is not yet a SUCCESS; downstream CI-only PR #314 has losslessly sharded all 115 checks, but its exact-HEAD hosted Research is QUEUED as of this update. No merge to main pending full-hosted success and ordered ancestor integration.

---

## Comment 040 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102323186
- GitHub comment ID: 6102323186

### Verified exact W32 finite ladder recovered from SUCCESSFUL hosted C16/C17 logs (C19 decision context)

I independently read actual GitHub-hosted exact-head report step output from [C16 Contract 38084811013](https://github.com/definitely-stable/Mathlab/actions/runs/38084811013), and [C17 Contract 38085935292](https://github.com/definitely-stable/Mathlab/actions/runs/38085935292), not intermediate guesses. In the SAME true original W32 reverse-line 12 original-left / 12 original-right pinned 3!²=36 finite completion box, rigorous accepted seven-count floor ladder is:

- C15 one shared RIGHT among already-left-pinned J: **12**;
- C17 pure LOCAL two-sided original named-support min (with pins): **60**, GF5 necessary numerator **2,720,043**;
- C17/C16 right-shared two-sided named-support signature: **64**, GF5 **2,862,486**;
- C16 all RIGHT groups with one original LEFT signature: **107**, GF5 **4,840,636**;
- C16 one shared LEFT map with independently minimized RIGHT groups: **114**, GF5 **5,077,052**;
- C16 exact bounded complete common two-sided minimum: **148**, GF5 **6,676,842**.

C17's exact independent local table evaluated 2,118,438 motif classifications from 374,220 complete-left source instances and 172,206 distinct original incidence-sixsets in the source UNION, with NO full joint score matrix allocated. These are real finite pinned-box comparisons only; do not extrapolate an Omega(s6) to empty pins from them.

C18/C19 all-h ZERO results apply to **NO ORIGINAL LEFT PINS** and independently minimized local witness blocks; they are not contradicted by positive floors after TWELVE original-left pins. The central C20 research problem is to make cross-block left-label compatibility enforce a positive floor at small/zero pin density across all s, not to enhance a rooted W32 finite table again.

C19 [dedicated exact-head hosted run 38087146666](https://github.com/definitely-stable/Mathlab/actions/runs/38087146666) SUCCESS 6/6, genuine W32 selected nine-original-left block pre/post physical double-star: **1,296 -> 0**. Full 115-step six-shard C19 Research CI [#314](https://github.com/definitely-stable/Mathlab/pull/314) remains queued as of this evidence note. Global #230 remains OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 041 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102498170
- GitHub comment ID: 6102498170

### C20 implemented: globally compatible original-left six-cycle floor, all h — [scientific PR #315](https://github.com/definitely-stable/Mathlab/pull/315)

**New ALL-h theorem (strictly LEFT SOURCE only).** For s=2^h>=2, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}, t=C(a,2)-V<a−1, for ANY occupied physical F⊆E(K_a) of size V and ANY one globally compatible bijection f from ALL true ORIGINAL GQ points onto F, the number of DISTINCT ORIGINAL six-incidence sets with physical left projection a simple Hamiltonian C6 satisfies

    N_left,A(f) = C6(F)*(s+1)^6
                >= [60*C(a,6)-24*t*C(a-2,4)]*(s+1)^6
                = Omega(s^15) > 0.

Proof: K_a has exactly 60*C(a,6) undirected six-cycles; every missing physical edge lies in exactly 24*C(a−2,4) cycles, so union-bound physical deleted edges. For s2 the lower is 60 C6; for s>=4 a>=14 and t<a−1 make the bracket strictly positive. A six-cycle corresponds to six DIFFERENT original left factor points under ONE common global f, and choosing one of (s+1) true ORIGINAL incident lines at each produces (s+1)^6 distinct original six-incidence sets per physical C6; distinct cycles cannot generate the same original J. Unlike C18/C19's separately minimized star/double-star block relaxations, this is valid for the ONE global left map.

**CRITICAL NONTRANSFER:** A left-eligible original J need not have accepted RIGHT physical projection under adversarial global g. In particular strict D6 matching constraints must not be ignored. Thus NO conclusion that simultaneously accepted S_seven(f,g)>=Omega(s6) and NO positive GF5 R3 floor / ASET exponent follows. Parent #230 is still OPEN_WITH_FORMAL_BLOCKER.

**Actual hosted tests:** scientific PR #315 exact HEAD e0c75e81a0ec30bc10f32907aac0cbbb52d5478e; focused [C20 Contract 38088695701](https://github.com/definitely-stable/Mathlab/actions/runs/38088695701) **SUCCESS**: five independent tests plus standalone true-original-W32 report. In actual W32, all 4 complete global physical left maps (two historical schemes, with/without ORIGINAL point relabel swap) have 62,370 left sixset candidates, 51,030 A candidates; independently expanded simple Hamiltonian C6 source gives **43,740 DISTINCT ORIGINAL incidences, all contained in the old A source**, plus 7,290 disconnected two-triangle A candidates. GF4 physical K14 V85/t6 deletion gate: at least 108,900 C6 and 1,701,562,500 true-original-left A candidate count mathematically (the executable does NOT enumerate true W(3,4) incidences).

A previous test-only failure was lazy generator not consumed when checking a hard cap; fixed without altering mathematics. The corrected exact-head hosted tests PASS.

**Research CI:** fully green upstream six-shard C19 CI #314 was updated losslessly in [CI PR #316](https://github.com/definitely-stable/Mathlab/pull/316), a separate child stacked upon C20. It preserves all 115 C19 checks and adds two explicit C20 checks, 117 unique named (name,run) steps, six independent GitHub-hosted jobs with seventh all-success aggregate and a frozen exact-workflow fingerprint. #316 exact-HEAD full Research still awaiting result; main untouched and no integration claimed.

**C21 next scientific gate:** enforce ONE global right g and exact ORIGINAL GQ right incidence multiplicity on the C20 forced left-A source. Prove adversarial transfer of a positive fraction to accepted same-J seven classes, OR rigorously exhibit a counterexample to this *transfer* without manufacturing a global low-S all-h family.

---

## Comment 042 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102705024
- GitHub comment ID: 6102705024

### C21-A/B implemented — global original right SDR + exact ONE COMMON randomized D6 mean

[Scientific PR #317](https://github.com/definitely-stable/Mathlab/pull/317) is stacked on fully GREEN C20 117-command CI [PR #316](https://github.com/definitely-stable/Mathlab/pull/316), not main. Scientific C20 [#315](https://github.com/definitely-stable/Mathlab/pull/315) remains unmerged.

**ALL-h restricted results:** For EVERY s=2^h>=2, EVERY global original-GQ point->physical pair injection f, and EVERY occupied right size-V physical alphabet F_R:
1. Each physical left C6 gives at least H(s)=max(1,(s+1)^6-15(s+1)^4) DISTINCT ORIGINAL six-incidence lifts with six DISTINCT ORIGINAL right lines. Pair collision union bound uses at most one shared GQ line per two distinct points; Hall gives the s=2 positive base.
2. Under ONE shared globally uniform right bijection g, each such original sixset is strict D6 with EXACT probability 12*C6(F_R)/(V)_6. The right map is common for every original J and no independence between witnesses is assumed.
3. E_g D6(f,g)=N_original_leftC6_rightDistinct(f)*12*C6(F_R)/(V)_6 >= 12*L(s)^2*H(s)/(V)_6 = (16/3-o(1))*s^6, where L(s)=60*C(a,6)-24t*C(a-2,4).

**NONTRANSFER:** this is a ONE COMMON RANDOM RIGHT MEAN, not a positive minimum for EVERY adversarial g, and it does NOT close all-seven S_s=Omega(s^6), full GF5 R3 or ASET. Right A/A physical cycles without strict D6 column-dual matching are rejected. Issue #230 is OPEN_WITH_FORMAL_BLOCKER.

Independent tests: genuine W(3,2), all four complete original left maps, 43,740 left lifts per map, exact per-physical-cycle right-SDR incidence enumeration vs independent right-neighbor bitmask DP, K6 exactly 720 physical compatible ordered right tuples, actual fixed-g D6 checked against historical accepted seven-class census. Full hosted Research preserves all 117 C20 commands and adds two explicit C21 commands (119 total), plus dedicated C21 Contract.

**Exact PR HEAD** b332a17b6b6acf818a87242f2c3e3fba586e1c08: [C21 Contract #38090279782](https://github.com/definitely-stable/Mathlab/actions/runs/38090279782) SUCCESS; [Full Research #38090279776](https://github.com/definitely-stable/Mathlab/actions/runs/38090279776) and [INDEX #38090279778](https://github.com/definitely-stable/Mathlab/actions/runs/38090279778) were initially QUEUED. No main merge or full acceptance until exact-head hosted success and ancestor integration. Next C21-C/D targets adversarial globally shared right mapping, using C3-C5 and C20 while avoiding C9/C10 and C18/C19 barriers.


---

## Comment 043 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102741587
- GitHub comment ID: 6102741587

### C21-C strengthened on PR #317 — C5 and C21 transfer under the SAME one common global right g

Beyond C21-A/B, the [current scientific PR #317](https://github.com/definitely-stable/Mathlab/pull/317) now contains an exact all-h **joint MEAN** corollary: C5 already proves E_g U_(B-left/A-right) >= M_B(s)=(140-o(1))*s^6 for EVERY fixed global left f and legal occupied F_R. C21 gives E_g D6 >= M_D(s)=(16/3-o(1))*s^6 under the SAME uniform random full right injection g. The ORIGINAL left endpoint profiles differ (B-left has one original point twice, D6 six distinct points), so the counts are disjoint for every g. Thus

    E_g S_seven(f,g) >= M_B(s)+M_D(s)
                     = (436/3-o(1))*s^6.

And by the issue #230 accepted necessary seven-class GF5 inequality,

    E_g R3(f,g) >= [45600*M_B(s)+5643*M_D(s)]/51^6.

Both are **EXPECTATIONS**, never inf_g/minimum claims. Exact rational code and new independent tests also compare true ORIGINAL W(3,2) 45-incidence B-left weighted source/fixed global right overlap against accepted B0 seven_census, alongside C21 strict D6; no double counting or per-class independent right map. No full R3 or ASET exponent.

**Updated exact PR HEAD** b0a7f8145b09d70d35688d3d99c98f233fa94345. Dedicated C21 Contract, full 119-command Research six-shard, and INDEX checks are QUEUED for this updated HEAD. Earlier predecessor HEAD b332a17... C21 Contract SUCCESS 6/6 and INDEX SUCCESS do NOT transfer as acceptance of this current HEAD. Issue #230 remains OPEN_WITH_FORMAL_BLOCKER and main untouched.

---

## Comment 044 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102834289
- GitHub comment ID: 6102834289

### C21-D continued — exact TRUE W32 one-global-right adversary, 40/105 zero-D6 neighbors

[Scientific PR #321](https://github.com/definitely-stable/Mathlab/pull/321) is stacked directly on C21 [#317](https://github.com/definitely-stable/Mathlab/pull/317), which itself depends on C20 [#315](https://github.com/definitely-stable/Mathlab/pull/315) and CI [#316](https://github.com/definitely-stable/Mathlab/pull/316). No main merge.

**RESTRICTED FINITE s=2 exact witness, not all-h counterexample:**
- Genuine original symplectic W(3,2): 15 point factors, 15 line factors, 45 distinct true incidences.
- One globally compatible complete original-left map f(p)=PAIRS[p].
- One globally compatible complete original-right map g(l)=PAIRS[perm[l]], perm=(4,13,2,9,14,3,6,0,8,1,11,5,7,12,10).
- Direct source oracle: 60 physical C6 x 3^6 true original incidence choices = **43,740**; right-distinct ORIGINAL six-line choices **18,716**; strict same-column-dual D6=**0**.
- Independent complete historical seven_census on 62,370 true original incidence sixsets: D6=0, B-left/A-right=60, A-left/B-right=66, C/A=5, C/B=0, B/B-overlap=9, B/B-disjoint=6; actual S_seven=**146**, necessary GF5 numerator **6,698,010**. Weighted-original-right B/A overlap independently returns 60. With SAME frozen f, identity global g has D6=15, S=259.
- Since nonnegative D6 has one attaining COMPLETE g with value 0, exact min over all global right g for this fixed f is ZERO at s=2. But the **same-f** C21 uniform-global-right mean remains 18716/5005 > 0. This formally falsifies a naive positive mean -> positive pointwise D6 transfer on actual W32, NOT the seven-family all-h Omega(s^6) Branch A.
- Exhaustive 105 **legal one-global-right-transposition** neighbors of this fixed W32 witness, reusing all genuine original right distinct C6 sources, have strict D6 histogram (score:count) 0:40, 1:29, 2:24, 3:6, 4:4, 5:1, 9:1. 40 distinct globally coherent right maps also give D6=0. This is finite evidence only, NOT an all-h correlated low-S family.

**Exact PR HEAD** 1ecf1880743e8c85f5c57b8c125ec0dc23e94e70. Added dedicated C21-D Contract, original-GQ direct and complete seven independent tests, six hosted research shards with 121 preserved exact named scripts (119 predecessor + 2), fail-closed seventh aggregate, docs and research index. Research workflow source digest independently rechecked 0x0BAEB6BDD0C8839B over exactly 121 pairs. GitHub-hosted exact-head Contract/Research/INDEX still pending and MUST pass before acceptance, no inherited CI from C21 #317.

**Next mathematical gate:** full seven-class joint original incidence tensor under ONE COMMON global f,g, cross-class tradeoff rather than D6-only. Issue #230 remains OPEN_WITH_FORMAL_BLOCKER. Do NOT claim PROVED_A, COUNTEREXAMPLE_B, total GF5 R3 or ASET exponent.

---

## Comment 045 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102942802
- GitHub comment ID: 6102942802

### C22 implemented in stacked PR #327 — all-h original seven tensor, exact right-swap locality and genuine W32 105-map tradeoffs

[C22 scientific PR #327](https://github.com/definitely-stable/Mathlab/pull/327) is stacked on [C21-D PR #321](https://github.com/definitely-stable/Mathlab/pull/321) -> C21 [#317](https://github.com/definitely-stable/Mathlab/pull/317) -> C20 #316/#315, **NOT main**.

**All-h exact mathematical identities, NOT a positive adversarial theorem:**
1. Six physical two-coordinate masks span exactly six physical coordinates of degree two IFF popcount(OR masks)=6 and XOR masks=0, even when pair edges repeat. Proof total degree 12 + XOR gives each of 6 occupied degrees even and positive => exactly2.
2. Define true ORIGINAL six-incidence set J, globally injective original point->physical pair f and original right line->physical pair g. Its original endpoint multiplicity profiles A/B/C and connected column-position dual matching (D6 only) determine exactly one of 7 accepted tags, or rejection. Both S_seven and accepted necessary GF5 seven-class numerator Q7 are exact all-h sums over the SAME J and SAME f,g; Q7 is NOT full R3.
3. Swapping physical labels of TWO original right GQ lines under ONE globally shared g leaves every J avoiding these original right lines unchanged. The exact S_seven and Q7 delta is a sum ONLY over the common original affected fiber, never independently optimized motif labels. For D6, all-h |delta|<=min(48*C(a-2,4)*(s+1)^6,60*C(a,6)*(s+1)^6)=O(s^12). This is an influence UPPER, not an Omega(s^6) minimum.

**Executable true finite W(3,2):** exactly 62,370 DISTINCT actual original incidence sixsets with valid LEFT physical 2factors, 51,030 original left A / 10,935 B / 405 C, source compiled once to weighted ORIGINAL right line six-tuples. Evaluate ALL 105 complete globally compatible right transpositions of C21-D's full right g with exact sparse updates, output seven-class vectors, S, necessary GF5 numerator, exact conditional minima over ONLY the 105-neighborhood with attaining swaps, right D6/complement covariance numerator. Independently crosscheck full B0 62,370-original-source seven_census at diverse true complete right maps, C0 weighted original B-left source/physical twofactor target, and C21-D known D6 105-histogram. Independent brute checks all K6 unordered six-pair multisets including repeated edges against integer degree direct oracle and 60+10 K6 2factor connectivity decomposition. Verify global right coordinate relabel gauge; fail-closed incomplete right mapping/source budget.

**CI:** Dedicated GitHub-hosted C22 Contract + full Research six shards **123 exact named commands** (all ancestor 121 preserved + 2) + INDEX. Frozen FNV1a64 0xFD5CC5690F2F83B2 source digest, seventh fail-closed aggregate. Exact PR HEAD 4bf882a45303e329fc763565fc47463f28356a7d; all three latest C22 workflows were QUEUED on first check, not yet accepted. main unchanged; prior C21-D full CI also unconfirmed.

**Formal blockers:** no all-h inf_(f,g) S_seven=Omega(s^6), no infinite actual GQ low-S family, no full 15! right minimum, no full GF5 R3 or ASET exponent. This exact 105-swap diagnosis is a rigorous finite falsifier for future C23 cross-class tradeoff hypotheses, not a universal proof. Keep #230 OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 046 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6102977421
- GitHub comment ID: 6102977421

### C22 independent full-original-W32 105-map result frozen in PR #327 (supersedes preliminary no-numeric C22 status)

[Current C22 PR #327](https://github.com/definitely-stable/Mathlab/pull/327) exact source HEAD **8e987a094004af9430e1af391e3842f66464e928**, parent C21-D PR #321. An independent **second** GF(2) W32 projective GQ generator and true-original-incidence 62,370-source seven-family enumerator (not importing the PR Python classifier) confirms:
- actual ORIGINAL sixset source exactly 62,370 (A 51,030, B 10,935, C 405), statically eligible 52,309, compressed ORIGINAL right-line signatures 36,272 with integer multiplicities;
- complete GLOBAL right baseline seven vector (D6, B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap, B/B-disjoint)=(0,60,66,5,0,9,6); S=146; GF5 necessary Q7 numerator=6,698,010;
- all 105 complete globally coherent original-right-line one-swap maps (same original left f) reproduce independent D6 histogram {0:40,1:29,2:24,3:6,4:4,5:1,9:1};
- **min ONLY over those 105 globally valid complete right swaps S_seven=122**, and **min necessary GF5 seven numerator Q7=5,623,340**, BOTH attained by swapping ORIGINAL right factor lines (4,14) in C21-D's single full global right map. Exact joint seven vector at that true complete same f,g is (0,47,57,2,0,11,5), sum 122.

The old baseline and the new (4,14)-swapped full right map BOTH have D6=0, yet the sum of the other six accepted classes falls from 146 to 122. Thus a naive MONOTONE compensation assertion for other classes within D6=0 W32 one-swap maps is **rigorously falsified**. This is NOT a claim of min over all 15! right permutations or over all f, not an infinite small-S family, and not an all-h positive minimum proof. The correct root #230 scientific status is still OPEN_WITH_FORMAL_BLOCKER.

The above finite integers were independently recomputed and then added to C22 regression assertions; this does not replace GitHub-hosted exact HEAD acceptance. Latest [C22 Contract](https://github.com/definitely-stable/Mathlab/actions/runs/38092465488), [full 123-command Research](https://github.com/definitely-stable/Mathlab/actions/runs/38092465549), [INDEX](https://github.com/definitely-stable/Mathlab/actions/runs/38092465498) were all **QUEUED** at last GitHub verification. Do not merge PRs #327/#321/#317/#316/#315 into main based on old green ancestors.

---

## Comment 047 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6103215516
- GitHub comment ID: 6103215516

### C23 implemented — exact ALL-h full-seven mean for ONE common global right g and seven-family transposition sensitivity

[PR #334](https://github.com/definitely-stable/Mathlab/pull/334) stacked on C22 [#327](https://github.com/definitely-stable/Mathlab/pull/327) -> C21-D #321 -> C21 #317 -> C20 #316/#315; main unchanged.

**New all-h quantified exact identities for every GQ(s,s), s=2^h>=2, every fixed globally consistent ORIGINAL left point embedding f, any legal size-V occupied physical right K_a pair alphabet F_R:**

1. Every physical six-coordinate 2-regular six-edge MULTIGRAPH falls into A=70 simple factors, B=45 one doubled physical pair edge + C4, C=15 three doubled disjoint physical pairs: 130 per physical six-coordinate subset. For each fixed physical pair edge e, exactly 40 factors include e ONCE (28 A+12 B) and six include e TWICE (3 B+3 C). Repeats cannot be discarded: accepted original right B/C profiles have repeated physical pair labels.
2. Let H_(tag,rightkind)(f) be the static count of DISTINCT ORIGINAL six-incidence sets with legal left physical twofactor and seven-class original multiplicity conditions; D6 requires the original left physical column-position connected C6. Under ONE uniform complete GLOBAL original right bijection g shared by **all** original sixsets, the exact right admissibility probabilities for original right A/B/C are respectively **6!*T_A(F_R)/(V)_6**, **4!*T_B(F_R)/(V)_5**, **3!*T_C(F_R)/(V)_3**; for strict D6 they are **12*C6(F_R)/(V)_6**. Exact full seven-class expectation E_g S_seven(f,g) is SUM H_(tag,rightkind)*P_(tag,rightkind). Corresponding necessary GF5 seven-class numerator E_g Q7 is same sum weighted by accepted B0 floors. This uses ONE COMMON g and linearity, NOT assumed independence or independent per-motif right g.
3. Global swap of right physical pair labels assigned to any TWO ORIGINAL GQ right line objects can change classes only of original J touching those two lines. For Delta=s+1, each ORIGINAL incidence source appears in at most C(a-2,4)*(40 Delta^5+6(Delta-1)Delta^4) left physical 2factor original sixsets. Therefore for all legal f,g:
   |S_seven(f,g swap)-S_seven(f,g)| <= min(2*C(a-2,4)*(46 Delta^6-6 Delta^5), U_left), where
   U_left=C(a,6)*(70 Delta^6+45 C(Delta,2) Delta^4+15 C(Delta,2)^3).
   Multiply this affected-original-sixset upper by 51750 for the accepted NECESSARY GF5 Q7-numerator sensitivity; NOT total R3. At s2, U_left=62370 exact; asymptotically swap influence upper O(s^12) **not sufficient to infer a positive all-g Omega(s^6) minimum**.

**Implementation and falsifiers:** one C23 Python research oracle with exact fractions for all-seven expected class vector on genuine 45-incidence W32 f and correctly profiled 52,309 static eligible original sixsets; exhaustive independent direct K6 six-edge multiset count including repeated edges (70/45/15 and fixed pair 40+6); all-h s2..128 arithmetic; physical incomplete target tests; all 15P3 physical named triple assignments check P_C=3/91; exact rational necessary GF5 floor and cross-check with earlier accepted C21 partial B/A+D6 mean. Detailed theorem with nontransfer in research doc and index.

**CI:** [C23 exact-HEAD Contract](https://github.com/definitely-stable/Mathlab/actions/runs/38094310780), [full Research six GitHub-hosted shards](https://github.com/definitely-stable/Mathlab/actions/runs/38094310765), [INDEX](https://github.com/definitely-stable/Mathlab/actions/runs/38094310771) were QUEUED at latest check; no success yet. Exact source Research command list: previous 123 steps losslessly preserved + two C23 checks =125, independent FNV1a64 digest **0xE1C77061D31C2B1C**, matched frozen regression guard. Current exact HEAD 5de0758130bbf00898ac47c37a86d36293f4ed5a. Do not promote to CI accepted or merge main without exact-HEAD hosted green and predecessor integration.

**Hard limits:** No all-g positive inf_(f,g) S_seven=Omega(s^6), no infinite correlated small-S source family, no full GF5 R3, no ASET exponent. C23 is an exact shared-global-g EXPECTATION theorem and shared-g worst-transposition INFLUENCE UPPER, not an extremal min. Keep ROOT #230 OPEN_WITH_FORMAL_BLOCKER. Next C24 should investigate higher joint moments/structured globally coherent isoperimetric or group-action inequalities, falsify with C21-D/C22 fixed true-global-map specimens before any all-h theorem claim.

---

## Comment 048 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106513540
- GitHub comment ID: 6106513540

### C24-A1 implemented in stacked PR #340 — all-h deterministic right-C star-collision inequality and genuine W32 zero-C falsifier

[PR #340](https://github.com/definitely-stable/Mathlab/pull/340) is based EXACTLY on scientific C23 [PR #334](https://github.com/definitely-stable/Mathlab/pull/334), no main modifications.

**ALL-h RESTRICTED_THEOREM_C (conditional, not a universal minimum):** for every s=2^h>=2 and every legal original globally coherent pair-label injections f,g, let H_C(f) count DISTINCT original six-incidence left physical 2-factors whose original RIGHT endpoints consist of three original lines appearing twice each. Let W_f(i,j) count these source sixsets involving original right lines i,j, sum_(i<j)W=3H_C. Then

```
S_seven(f,g) >= S_(R=C)(f,g)
 >= H_C(f) - sum_x sum_{i<j in L_x(g)} W_f(i,j).
S_seven(f,g) >= H_C(f)*(1-6(a-2)/(V-1)) - V*||B_f||op,
B_f=W_f-[6H_C/(V(V-1))]*(J-I).
```

The inequalities use physical star capacity |L_x(g)|<=a-1, complete ORIGINAL global g, and a deterministic union bound, not random per-J mappings. A rigorous rational operator-norm upper proxy uses max absolute row sum / ceiling Frobenius norm; it does not establish a sharp all-f norm bound.

**FINITE genuine W(3,2) C-only zero:** independent 15-point/15-line/45-incidence GF(2)^4 symplectic host, two distinct right-first and left-first original sixset enumerators (all 62,370), H_C=92, 83 original right line triples, sum_(i<j)W=276, max W_ij=7. ONE complete globally coherent right permutation (1,13,3,6,10,9,8,0,7,2,11,5,14,12,4), with lex original symplectic lines and K6 pair labels, yields S_(R=C)=0 while E_g S_(R=C)=276/91>0. Does NOT show total S_seven=0 and is NOT an infinite all-h counterexample B.

Independent regression: 105 valid global right-line transpositions; s=2..128 all-h exact geometry arithmetic; malformed injections fail closed.

**CI status at creation:** exact HEAD 1dc78cee1eb6e932246ade34316f44ff535dd97e, C24 dedicated Contract #38120223975, full six GitHub-hosted Research + aggregate #38120223982, INDEX #38120224020 QUEUED. Research preserves 125 predecessor commands plus two explicit C24 checks (127 total), frozen independent fingerprint 0x47EB82D9CD26D8A4. No acceptance/merge until exact-head all three SUCCESS and predecessor reconciliation. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER, no GF5/ASET exponent.

**Next C24-B:** falsify or prove all-f H_C source lower and centered star-discrepancy; avoid claiming all-g positivity from the C-only expectation or concentration.


---

## Comment 049 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106659041
- GitHub comment ID: 6106659041

### C24-B1 implemented — exact ALL-h third-order right-C collision identity, new genuine W32 global-left H45 witness, and pair-tensor information-loss theorem

[Scientific PR #344](https://github.com/definitely-stable/Mathlab/pull/344) is stacked on C24-A1 [PR #340](https://github.com/definitely-stable/Mathlab/pull/340) → C23 #334; NOT main.

**New ALL-h exact identity (every s=2^h>=2; same original f and ONE GLOBAL original-right g):** Let omega_f(i,j,k) be the number of DISTINCT actual original six-incidence sets whose physical LEFT projection is a 2-factor and whose original RIGHT line multiplicity profile is (2,2,2), exactly two incidences on each of three distinct lines. Let H_C=sum omega; W_f(i,j)=sum_(k)omega_f(i,j,k); c_ij(g)=1 iff g(i),g(j) intersect as physical pair edges, and chi_ijk=c_ij+c_ik+c_jk. Then

```
S_(R=C)(f,g) =
   H_C(f) - sum_(i<j) W_f(i,j)*c_ij(g)
          + sum_(i<j<k) omega_f(i,j,k)*max(chi_ijk-1,0).
```

This is exact; the final correction accounts for overcounting 2/3 conflicts. It is **not** a universal positive seven-class minimum.

**Genuine ORIGINAL symplectic W(3,2) 15-by-15, 45 incidences:**
- ONE globally complete left f assigning the 15 original point IDs to lex K6 physical pair edge indices **(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8)** yields H_C(f)=**45**, vs 92 from C24-A1 lex original f.
- Independent right-first THREE ORIGINAL lines × TWO DISTINCT incidences and fully independent physical left first 130 two-factor templates × ORIGINAL incidence selections match ALL 62,370 left sixsets and H_C=45 with 40 named right-line triples. Pair sum 135, maximum pair weight 5.
- ONE globally complete original right g **(12,10,5,2,8,14,1,7,0,6,3,13,9,4,11)** gives S_(R=C)(f,g)=**0** for the SAME f; 105 additional legal complete one-right-line transpositions satisfy exact third-order identity. No per-sixset mapping.
- This is NOT proof of min_f H_C=45, NOT a total seven-family S=0 and NOT an infinite-h Branch B witness.

**Abstract information limitation:** two Pasch three-uniform trades on six named line objects have the exact SAME pair-weight matrix W, but a common complete physical right pair injection yields accepted right-C triples 0 versus 1; first-order star sum is the same. The Pasch abstract structures are NOT asserted to be realizable as a full genuine GQ original sixset source. Thus W alone is insufficient for exact general triple counts; special GQ bounds may still exist.

**CI acceptance:** C24-A1 exact-head [Contract](https://github.com/definitely-stable/Mathlab/actions/runs/38120223975), [Research](https://github.com/definitely-stable/Mathlab/actions/runs/38120223982), [INDEX](https://github.com/definitely-stable/Mathlab/actions/runs/38120224020) all now SUCCESS. C24-B1 #344 exact HEAD d4101fa8e23cf320af1a0423e9e28cb2d5e861b7 workflows initially QUEUED: [Contract](https://github.com/definitely-stable/Mathlab/actions/runs/38121292853), [Research](https://github.com/definitely-stable/Mathlab/actions/runs/38121292839), [INDEX](https://github.com/definitely-stable/Mathlab/actions/runs/38121292852). Research preserves previous 127 exact commands, adds exactly two explicit B1 commands = 129; independent FNV1a64 **0xFBB1D4C90C0FEAC1**. No merge before exact-head all-green and ancestor reconciliation.

**Scientific status:** RESTRICTED exact third-order theorem + genuine W32 conditional C-only zero + abstract pair-only NO-GO; root #230 OPEN_WITH_FORMAL_BLOCKER, no universal all-g positive min / full GF5 R3 / ASET exponent. Next C24-B2: seek or falsify ALL-f lower for H_C plus star-constrained THIRD-order discrepancy; preserve original GQ incidence identities.


---

## Comment 050 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106678477
- GitHub comment ID: 6106678477

### C24-B2 follow-up direction — SAME global W32 f,g full-seven audit (exploratory, NOT CI-frozen)

The genuine C24-B1 complete global ORIGINAL f and g that give H_C(f)=45 and S_(R=C)(f,g)=0 were independently re-enumerated via TWO different ORIGINAL six-incidence orientations: (1) physical-left K6 2factor templates + incident-original-line selections; (2) physical-right K6 2factor templates + incident-original-point selections. Both enumerate 62,370 distinct ORIGINAL selected sixsets and agree on the **entire seven-class vector** under THE SAME complete f,g:

```
D6=1
B-left/A-right=80
A-left/B-right=83
C/A=4
C/B=0
B/B-overlap=2
B/B-disjoint=7
S_seven=177
Q7 accepted necessary GF5 numerator = 8,030,293
```

**Important nontransfer:** C-only complete cancellation under correlated genuine maps DOES NOT imply small full S_seven; 177 here exceeds the C22 fixed-lex-left 105-neighborhood witness 122 (which uses DIFFERENT left map). This is a finite observation, not an all-f or all-h inequality.

This two-direction exploratory full-seven audit was performed outside the PR and **has NOT yet been packaged into independent GitHub-hosted C24-B2 tests**; therefore do not treat it as CI-certified or as final acceptance. The next suitable slice is C24-B2 with a frozen independent two-orientation all-seven classifier and conditional joint optimizer that cannot optimize only right-C. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 051 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106829419
- GitHub comment ID: 6106829419

### HYP-105 C24-B2 implemented — exact genuine original W32 full-seven versus right-C-only finite NO-GO

Scientific stacked [PR #346](https://github.com/definitely-stable/Mathlab/pull/346) based on C24-B1 [PR #344](https://github.com/definitely-stable/Mathlab/pull/344), then C24-A1 #340 and C23 #334. Main not changed.

**Independent exact genuine W(3,2):** complete original 15 point/15 line / 45 incidence GF(2)^4 symplectic host. One fixed globally coherent ORIGINAL LEFT f and one globally coherent ORIGINAL RIGHT g from C24-B1; all 62,370 ORIGINAL six-incidence sets separately enumerated LEFT-FIRST and RIGHT-FIRST. Both independently classify full seven counts (D6, B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap, B/B-disjoint) = **(1,80,83,4,0,2,7)**, total **S_seven=177**, accepted necessary GF5 **Q7=8,030,293**, while accepted ORIGINAL right-C **S_(R=C)=0**. Crucial: symmetric C/A=4 here consists of ORIGINAL LEFT C / ORIGINAL RIGHT A, not right C.

**EXACT full 105 ONE-global-right-line transpositions, SAME f:** 53,907 statically eligible original sixsets compressed into 51,506 weighted original right-label signatures. Swap-localized exact seven counting and accepted necessary GF5. Among ONLY these 105 valid complete right mappings:
- min **full S_seven=129, Q7=5,842,083, right-C=1** at original line swap **(6,14)**, seven-vector (1,64,52,4,0,2,6);
- min S_seven CONDITIONAL on **right-C=0** is **136, Q7=6,172,583** at swap **(10,14)**, seven-vector (1,74,51,2,0,3,5);
- right-C histogram 0:58, 1:35, 2:8, 3:3, 4:1.
- Baseline right-C zero has S_seven=177 but is NOT included in these 105 transpositions.

This is a **genuine finite restricted NO-GO** for the proposition that enforcing C-only zero/minimum is lossless for full seven minimization on this fixed original W32 one-swap neighborhood. Does NOT prove global min over 15! right maps or all left f, an infinite all-h small-S witness, an all-h universal positive S lower, total GF5 R3 or new ASET exponent.

Source: [formal theorem/scope](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-b32e1c24b2-full-seven-joint-audit/docs/research/HYP-105-G5-E2-B3-E1C24B2-JOINT-SEVEN-FINITE-NOGO.md). Dedicated exact PR-head C24-B2 [Contract #38122584840](https://github.com/definitely-stable/Mathlab/actions/runs/38122584840), full [Research #38122584802](https://github.com/definitely-stable/Mathlab/actions/runs/38122584802), [INDEX #38122584868](https://github.com/definitely-stable/Mathlab/actions/runs/38122584868) initially QUEUED, no acceptance yet. Research exactly 131 commands (129 previous preserved +2 C24-B2), FNV1a64 0x2CA51D573F3ADEE7. Require all exact-head SUCCESS, do not merge main.

**Next C24-B3:** a genuinely JOINT full-seven deterministic all-h certificate or falsifier, preserving ONE complete original f,g and original GQ six-incidence identities. Root #230 stays OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 052 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106968408
- GitHub comment ID: 6106968408

### C24-B3 implementation — ALL-h joint-seven swap exchange and exact true-W32 lambda-seven finite frontier

[Stacked research PR #347](https://github.com/definitely-stable/Mathlab/pull/347) built directly on exact-head GREEN C24-B2 [#346](https://github.com/definitely-stable/Mathlab/pull/346) -> #344 -> #340 -> C23 #334. **No main modifications.**

**ALL-h exact exchange proof, every genuine W(3,2^h), arbitrary globally complete f,g:** For the single fixed ORIGINAL-incidence source with static original-endpoint profile and left physical projection, a right global transposition of original right lines i,j changes each accepted seven-family S_tag only on original sixsets touching i or j. No ORIGINAL sixset migrates between different accepted tags under g-only changes; acceptance toggles 0↔its own fixed tag. Thus exact all-h Delta S_seven=sum_tag Delta S_tag, Delta Q7=sum_tag accepted frozen GF5 necessary weight*Delta S_tag. For fixed f,F_R and any real threshold T, min over ALL complete right g S_seven>=T iff EVERY one-swap-stationary complete right g has S_seven>=T, because any global finite-permutation minimizer is stationary. **Equivalence is not a positive all-f all-h lower bound.**

**NEW exact genuine W(3,2) 105-global-right-permutation lower envelope:** For same true ORIGINAL f and complete right baseline g as C24-B2, the accepted minimum full S=129 at one-swap original right (6,14) with ORIGINAL right-C=1 and best full S conditional on C=0 is 136 at (10,14). For EVERY REAL lambda>=0 over exactly these 105 globally coherent complete right maps:

```
min(S_seven+lambda*S_original_right_C)=min(129+lambda,136).
```

Proof uses attainment by complete original GQ maps and lower bounds for C>=1 and C=0. Sharp switch lambda=7. This is finite 105-neighborhood only, not global right 15!, any all-f min or ASET exponent.

**New executable:** per-tag signed exact swap exchange, Q7 and C change, 105 coherent original right swaps, a SECOND 105-swap neighborhood after the 129-score real map, independently recounting any second improving move by full right-first 62,370 original source. Complete toy S3/S4 proof-gate falsifiers. No premature one-swap-local/global-min claim.

**Exact PR HEAD** f0ed7ce155613f4f1eba2f01528e7ee45ce3ac8e. [C24-B3 Contract #38123636076](https://github.com/definitely-stable/Mathlab/actions/runs/38123636076), [full six-shard Research #38123635997](https://github.com/definitely-stable/Mathlab/actions/runs/38123635997), and [INDEX #38123636143](https://github.com/definitely-stable/Mathlab/actions/runs/38123636143) are QUEUED at creation. All previous 131 Research commands preserved +2 =133, independent FNV1a64 0x1719E03AD4892772. No acceptance or merge until exact-head all three SUCCESS.

Root #230 remains OPEN_WITH_FORMAL_BLOCKER. No PROVED_A, no infinite-h COUNTEREXAMPLE_B, no full GF5 R3 or ASET exponent.

---

## Comment 053 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6106995656
- GitHub comment ID: 6106995656

### C24-B3 independently hosted new SAME-map W32 descent: 177 → 129 → 111

Scientific [PR #347](https://github.com/definitely-stable/Mathlab/pull/347) remains stacked on #346, with **NO main modification**. Earlier exact-head [dedicated C24-B3 Contract #38123636076](https://github.com/definitely-stable/Mathlab/actions/runs/38123636076) completed SUCCESS. Logs certify:
- the complete original W32 global f,g baseline has S_seven=177;
- global right-original-line swap (6,14) yields S=129 and original right-C=1, independently full-source checked;
- on all 105 further complete global right swaps from that SAME 129-score map, exactly **17** strictly decrease full S_seven;
- the strongest second original right swap is (12,13), producing **S_seven=111**, independently recounted from 62,370 actual ORIGINAL six-incidence sets via RIGHT-FIRST K6 templates;
- resulting one COMPLETE global original right-line-to-physical-pair index permutation: **(12,10,5,2,8,14,11,7,0,6,3,13,4,9,1)**; same original global LEFT f is retained;
- among 105 original baseline one-swaps, **83** have opposing signed changes among seven accepted classes (not same-source tag migration);
- exact finite regularization min(S+lambda*C)=min(129+lambda,136), threshold lambda=7, is unchanged.

This strictly falsifies any claim that the prior 129-score W32 witness is a one-swap local minimum; it is NOT a global 15! minimum, all-h Omega(s^6) proof or infinite-h low-S counterexample. The THIRD neighborhood of the 111-score global right map remains UNCHECKED.

The PR now includes frozen regression assertions for second swap (12,13), 17 improving neighbors, and S=111 plus new report fields with seven-vector and GF5 necessary Q7. Exact updated HEAD **232dc2e8a753e96bedacdf19ce2fedff1519e9fd** needs new GitHub-hosted C24-B3 Contract, full 133-command Research and INDEX SUCCESS; older checks do not grant final acceptance. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 054 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107151307
- GitHub comment ID: 6107151307

### C24-B4 implemented in stacked draft PR #348 — exact all-h original source swap-flow, signed cut inversion and true W32 third neighborhood

[PR #348](https://github.com/definitely-stable/Mathlab/pull/348), directly based on C24-B3 [#347](https://github.com/definitely-stable/Mathlab/pull/347). No main modification or merge.

**New deterministic all-h RESTRICTED_THEOREM_C** for every s=2^h>=2, fixed legal complete global original LEFT f and one complete globally coherent original RIGHT g, original GQ right lines i,j:
- For each of the seven ORIGINAL distinct six-incidence families t, let G_ij,t count rejected→accepted sources and L_ij,t accepted→rejected sources under exactly one legal global-right transposition. Exact `Delta S_t=G_ij,t-L_ij,t`, `Delta S=sum_t Delta S_t`, `Delta Q7=sum_t w_t Delta S_t`, and an independent original-right-C projection. All counts are ORIGINAL sixsets with multiplicity, not compressed record counts.
- Define `d_ij=Delta S` and signed aggregate cut `C(U)=sum_{i in U,j outside U} d_ij`. **ALL-h exact inversion**: `2d_ij=C({i})+C({j})-C({i,j})`. Thus global-right one-swap stationarity is **equivalent** to every pair-cut inequality `C({i,j})<=C({i})+C({j})`.
- Pure singleton-cut positivity and even all signed cut sums >=0 do **not** enforce per-edge stationarity for an arbitrary signed graph: explicit abstract n=3 counterexample d01=-1, d02=d12=1. This is a *structural information limitation*, NOT a GQ-realizable counterexample B.
- These identities are useful equivalent proof targets, **not** a proof of `S_s(f,g)>=c s^6`, and not an asymptotic compression (the pair-cut matrix remains quadratic).

**Genuine finite original W(3,2) executable:** freeze C24-B3 true H_C=45 complete global LEFT f and the certified full-right two-swap map `(12,10,5,2,8,14,11,7,0,6,3,13,4,9,1)`, baseline `S_seven=111`. Compute **all 105 THIRD neighborhood original-right global swaps**, per-seven-class signed flows, original-right-C, Q7, exact cut inversion and finite signed cut diagnostic. Independent RIGHT-FIRST 62,370 distinct ORIGINAL source enumeration validates the baseline and the best third neighbor; separate source-fiber gain/loss validates its seven-vector delta. Only apply a strict improvement. Third numeric winner is *not pre-asserted* before actual GitHub-hosted completion.

**CI:** six full GitHub-hosted Research shards and seventh fail-closed aggregate preserved; 133 predecessor named steps plus 2 explicit B4 steps = **135**, independent FNV1a64 `0xEFF8E65FF6FECEBE`. Dedicated Contract, full Research and INDEX exact-HEAD runs are QUEUED as of this note; B3 Research #38123832781 is also still queued. Latest B4 head at time of note `696640c29c4e936fbaeea6bf32900bf911e508be` (not acceptance yet). No claim of all-h Omega(s^6), all 15! W32 minimum, entire GF5 R3 bound, or ASET exponent.

**Outcome:** RESTRICTED_THEOREM_C at mathematical-identity level; FINITE_W32_THIRD_NEIGHBORHOOD_IMPLEMENTED_CI_PENDING; #230 remains OPEN_WITH_FORMAL_BLOCKER. **Next allowed:** collect exact latest-head Contract/Research/INDEX verdict and reported third-neighborhood minimum. If an improving edge exists, continue a separately budgeted multi-swap finite descent; if stationary, investigate cut-source correlation or explicit stable low-S witnesses before any all-h claim.

---

## Comment 055 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107212530
- GitHub comment ID: 6107212530

### C24-B4 quantitative genuine W32 follow-up — strict S72 right-transposition local optimum (CI pending)

Updated [draft PR #348](https://github.com/definitely-stable/Mathlab/pull/348) contains a new explicit complete ORIGINAL globally coherent right permutation and exact 105-final-neighbor witness, all using the SAME original complete LEFT f from C24-B1.

Independent local reproduction of the 62,370 genuine symplectic W(3,2) original sixsets with left-first and separate right-first classifiers gives:
- Two-swap baseline S111: eight of 105 strictly improving complete global-original-right transpositions; best third (7,11) -> S102, class vector (1,53,38,3,0,1,6), Q7 necessary 4,607,013, original-right-C 1; 58 original accepted sixsets lost, 49 gained.
- Full globally coherent RIGHT move sequence from S111: (7,11) -> 102, (6,8) -> 93, (5,9) -> 86, (2,8) -> 76, (1,13) -> **72**.
- Final globally complete ORIGINAL right map: `(12,9,11,2,8,6,0,13,5,14,3,7,4,10,1)`; exact seven-vector `(0,36,31,2,0,1,2)`, ORIGINAL right-C 0, GF5 necessary numerator Q7 = 3,283,610, confirmed by separate full RIGHT-FIRST original-sixset census.
- ALL 105 complete original right transpositions from that terminal S72 map have **score >=74**, uniquely deterministic lex-first best (1,14) = 74; **ZERO improving swaps**. This proves a **finite strict one-swap stationary map** for this fixed f, *not* the all-15! right global minimum or all-f/all-h positive S bound.

**All-s threshold consequence:** If the proposed `S_s<cs^6 -> exists negative right swap` is required for every h>=1, then necessarily `c<=72/64=9/8`. This does **not** limit an asymptotic c valid only for sufficiently large h. Mathematical all-h signed source-flow/cut reconstruction identities remain exact but do not close Branch A. No total R3 or ASET claim.

PR head as of this update `9b7a5fed514176a36d8cc9b60f95803dd6836e47`; newly added hosted regression recomputes ALL 105 final right neighbors and two independent 62,370 original source classifiers. **CI acceptance not yet confirmed; main untouched; issue #230 remains OPEN_WITH_FORMAL_BLOCKER.**

---

## Comment 056 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107601011
- GitHub comment ID: 6107601011

### C24-B5 implemented as stacked DRAFT PR #352 — exact original W32 transposition-distance-two sphere

[PR #352](https://github.com/definitely-stable/Mathlab/pull/352) is based **exactly** on C24-B4 #348 (and #347 upstream), **not main**. No merge, no main mutation.

**Exact ALL-n finite-group classification**: composition of two distinct right transpositions has cycle type directed 3-cycle or two disjoint transpositions. For n named ORIGINAL GQ right lines, the number of DISTINCT distance-two maps is `2*C(n,3)+3*C(n,4)`. At original W32 n=15 this gives 910 distinct directed 3-cycles, 4095 disjoint-double states and exactly **5005 distinct endpoints**; each has 3 or 2 ordered decompositions respectively, totaling **10920** two-swap paths. Radius<=2 inclusive contains 5111 states, not all 15! right maps.

**New all-h exact original-right template-pullback identity**: for a globally coherent COMPLETE original-right injection g, every accepted six-incidence source has one uniquely determined physical right multiset six-edge 2-factor T. Count original source right-multiset fibers at the inverse multiset g^(-1)(T), preserving the seven original static family tags and DISTINCT original-sixset multiplicities; D6 additionally checks ordered physical column-dual alignment. In genuine W(3,2), exactly 130 K6 physical 2-factor multiset templates suffice. This is an exact identity, not an all-h complexity upper or S>=Omega(s^6) bound.

**Executable** pins B4's strict true global one-swap S72 original right map `(12,9,11,2,8,6,0,13,5,14,3,7,4,10,1)`, checks all 105 one-swap neighbors and enumerates **all 5005 distinct exact distance-two endpoints**, exact S_seven/seven counts/right-C/GF5 NECESSARY numerator. Cross-validates decisive maps against the full original LEFT ~51,506 compressed signatures and **independent full RIGHT-FIRST 62,370 original six-incidence enumeration**. Reports exact radius-two minimum, count of improved two-swap endpoints, cycle class, best complete right map and the best-path intermediate barrier.

**Mathematical gate**: for disjoint (commuting) swaps A,B, the mixed gradient kappa = S(g^(AB))-S(g^A)-S(g^B)+S(g), supported only on original sixsets touching both swap pairs, must satisfy kappa<-(d_A+d_B) to escape; overlapping swaps are 3-cycles and order-dependent.

**CI**: separate hosted C24-B5 Contract, six full hosted Research shards plus fail-closed aggregate, INDEX. Preserve 135 old Research named commands + 2 new B5 commands = **137**, corrected independently sorted frozen FNV1a64 `0x069403F46467A4EE`. Exact PR HEAD `ac82828113c54965c4e7613a7fc5c61d593234c0`; all three PR-head jobs QUEUED at issue-comment time. Numeric distance-two minimum must come from actual executable report, NOT guessed. Until all three latest-HEAD successes, status is IMPLEMENTED_CI_PENDING. No full 15! / all-f / all-h lower / entire GF5 R3 / ASET conclusions; root #230 stays OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 057 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107618496
- GitHub comment ID: 6107618496

### C24-B5 quantitative research result — first hosted 5005-state exact W32 double-swap S72 -> S68 escape

[Scientific stacked draft PR #352](https://github.com/definitely-stable/Mathlab/pull/352) directly on C24-B4 #348, root #230. **Initial GitHub-hosted dedicated Contract #38128554258 SUCCESS** on its then HEAD `ac82828113c54965c4e7613a7fc5c61d593234c0` (all 6 B5 tests + complete executable original W32 5005-state report + independent full 62,370 original right-first incidence recount). No main modification or merge.

For the genuine original W(3,2) fixed complete global LEFT f (C24-B1 H45) and one complete global RIGHT g72 from C24-B4 (S_seven=72, all 105 single swaps have S>=74), an **EXHAUSTIVE** double-swap orbit test found:
- Exactly `2*C(15,3)=910` distinct directed 3-cycles + `3*C(15,4)=4095` distinct disjoint pairs = **5005** unique exact-two-swap right maps, represented by **10920** ordered distinct two-transposition paths.
- **EXACT minimum S_seven = 68**, exactly **TWO** of 5005 target maps have S<72, both with score 68. The next higher target score is 73. This formally disproves *one-swap stationarity implies two-swap stationarity* even for TRUE original globally coherent W32 f,g.
- Lex-canonical best target globally complete original-right permutation `(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)`, full seven-vector `(0,44,21,0,0,2,1)`, ORIGINAL right-C=0, GF5 necessary numerator Q7=3,112,510. All verified via independent original right-first 62,370 distinct source enumeration, not signed-event overcount.
- Best two-step path: original global right swaps **(4,14) -> intermediate S=82 -> (3,12) -> S=68**. The disjoint swap pair has individual gradients +10 and +17, joint discrete mixed curvature **-31**. Thus `S(gAB)=72+10+17-31=68`; the exact minimal temporary barrier to this best target is +10.
- New all-h exact **original-right physical 2factor template pullback** counts tagged original sixset multiset fibers by inverse image under one global right injection, including D6 ordered dual checks. The W32 finite instantiation requires 130 physical K6 twofactor multigraph templates, 14,693 right multiset fibers, and 53,907 eligible sources. No asymptotic runtime theorem is claimed.
- The numeric result is now frozen fail-closed in code/docs. Full hosted Research six shards+aggregate preserve 135 preceding commands and append two B5 = **137**, frozen independent FNV `0x069403F46467A4EE`.

**Evidence scope:** EXACT FINITE_W32_LOCALITY_SEPARATION (not all-right 15!, all-left-f, all-h S>=Omega(s^6), GF5 total R3 or ASET). The current updated draft PR #352 head `1a4415942f29c4be9207e009e1e9706d2d812758` must obtain **new exact-head Contract/Research/INDEX SUCCESS**; initial older-head Contract SUCCESS alone is not acceptance. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.

**Next allowed mathematical stage** after exact-head CI: analyze complete one-swap neighborhood of new S68 map, then a separate bounded alternating two-swap descent / disjoint-source mixed-curvature inequality, with explicit finite original independent falsifiers.

---

## Comment 058 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107632739
- GitHub comment ID: 6107632739

### C24-B5 additional independent source-level negative curvature oracle (latest stacked draft)

In [PR #352](https://github.com/definitely-stable/Mathlab/pull/352), after initial exact hosted 5005-endpoint Contract SUCCESS, implemented an extra **independent original sixset mixed-difference** for disjoint original line swaps A=(4,14), B=(3,12). The oracle intersects ORIGINAL source fibers touching A and B; for each distinct source J it calculates `X_J(gAB)-X_J(gA)-X_J(gB)+X_J(g)` using four ONE-GLOBAL-right maps, preserves original source multiplicity and seven fixed tags, and reconstructs the signed NECESSARY GF5 numerator. Exact all-h support lemma: only original J touching BOTH disjoint swap pairs may contribute nonzero mixed curvature. Regression pins the genuine original W32 total **kappa=-31** in either swap order and forbids overlapping swaps as an invalid symmetric Hessian. This independently tests the mechanism behind finite S72 -> S68 escape, rather than assuming the curvature from total score subtraction.

Latest draft head at comment time `d626117eb2d6c1eaa6ea40aacf6cc75bfc7ddc15`; exact-head hosted Contract/Research/INDEX are QUEUED. Initial earlier-head Contract #38128554258 SUCCESS must **not** be transferred to this head. No main modification, no merge, no all-h obstruction or full GF5/ASET claims; #230 OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 059 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107694082
- GitHub comment ID: 6107694082

### C24-B6 implemented: all-h disjoint mixed-curvature exposure and exact original W32 S68 radius-two audit

New stacked DRAFT [PR #353](https://github.com/definitely-stable/Mathlab/pull/353) is based **exactly** on C24-B5 [PR #352](https://github.com/definitely-stable/Mathlab/pull/352), atop #348/#347. No `main` changes or merge.

**New deterministic all-h RESTRICTED theorem (every s=2^h>=2, every legal complete original GQ left f and ONE coherent global right g):** For disjoint global original right swaps A,B, and each DISTINCT original original-six-incidence source J with fixed static seven-family tag, mixed contribution `X_J(gAB)-X_J(gA)-X_J(gB)+X_J(g)` vanishes unless J touches BOTH original right pairs, and has magnitude <=2. Therefore `|kappa_AB| <= 2*M_AB` with exact original jointly touched source multiplicity M_AB. For n original right lines and r distinct original right line support per J, exact count of UNORDERED disjoint swap pairs jointly touched is `2K(n,r)=C(n,2)C(n-2,2)-2*C(n-r,2)C(n-2,2)+C(n-r,2)C(n-r-2,2)`. Hence `sum_{unordered disjoint A,B}|kappa_AB|<=2*sum_{original J}K(n,|H(J)|)`, counted with original multiplicities. An independent brute small n=4..6 exact all-r falsifier and true W32 source support histogram test are added. **This is an absolute upper on interaction, not a positive S lower or signed curvature guarantee.**

**Finite genuine original W32 B6:** same globally complete original LEFT f, freeze C24-B5 right map `(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)` with original S=68, seven-vector (0,44,21,0,0,2,1), necessary GF5 numerator 3,112,510. Do NOT assume the new map is right one-swap stationary. Exhaust its entire **105 one-swap and 5005 exact two-swap states** (910 3-cycles + 4095 disjoint doubles, 10920 ordered paths) with the source-backed physical 130-template inverse right classifier, tally separate one/two minima and improvements, and all 4095 exact disjoint mixed curvatures. Compare sum absolute kappa with all-h exact K(n,r) exposure bound. Independently recalculate most-negative and, where disjoint, best-target curvature from jointly-touched ORIGINAL sixsets and verify selected maps via BOTH full original LEFT-first and independent 62,370-original-incidence RIGHT-FIRST classifiers. NO numeric minimum asserted until hosted run.

**CI**: dedicated C24-B6 GitHub-hosted Contract (fast tests + complete W32 report), full six-shard Research with fail-closed seventh aggregate, and INDEX. All **137** predecessor named Research commands retained; B6 adds two, totaling **139**; independent FNV1a64 `0x908406FEEA5AC976`. Initial PR head `a2e8ae292a20b8541570ef5e15b25db01d7eb814` has Contract/Research/INDEX QUEUED at comment time; exact-head all-green required. #230 remains OPEN_WITH_FORMAL_BLOCKER: this finite search is not all-right 15!, all-f/all-h `Omega(s^6)`, entire GF5 R3 or ASET exponent.

---

## Comment 060 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107741776
- GitHub comment ID: 6107741776

### C24-B6 independently reproduced strict ORIGINAL W32 S68 radius-two local optimum — [draft PR #353](https://github.com/definitely-stable/Mathlab/pull/353)

**All-h exact theorem recorded in C24-B6:** for disjoint original RIGHT global swaps A,B every DISTINCT ORIGINAL static seven-family candidate sixset J contributes mixed indicator `X_J(gAB)-X_J(gA)-X_J(gB)+X_J(g)`, which vanishes unless J touches both original swapped line pairs and has absolute value <=2. The exact number of unordered disjoint pair swaps jointly touching a support H with |H|=r among n lines is `2K(n,r)=C(n,2)C(n-2,2)-2C(n-r,2)C(n-2,2)+C(n-r,2)C(n-r-2,2)`. Hence `SUM_{disjoint {A,B}}|kappa_AB| <=2 SUM_J K(n,|H(J)|)` with true original multiplicities. This is an ABSOLUTE upper; it proves no signed descent guarantee or all-h positive lower on seven-score.

**Independent locally executed true original GF(2)^4 W(3,2), ONE fixed global left f and ONE globally coherent original RIGHT g68 from accepted finite C24-B5 witness:**
- Exactly 62,370 DISTINCT ORIGINAL 6-incidence left sources, 53,907 static eligible and 51,506 compressed signatures; separately reconstructed exact 130 physical K6 right-factor pullback scorer.
- ALL 105 complete original RIGHT one-swap states around `g68=(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)`, `S=68`: min neighbor **S=75** at (8,9), ZERO improving.
- ALL 5,005 exact distinct distance-two RIGHT states (910 directed 3-cycles + 4,095 double disjoint swaps): min **S=69** with exactly TWO tied endpoints, ZERO improving. Lex first best global right `(2,9,11,4,10,6,0,13,5,14,3,7,12,1,8)`, seven-vector (0,41,25,0,0,2,1), GF5 necessary Q7 3,158,110 and ORIGINAL right-C=0. Best two-step path `(4,13)` (intermediate S78) then `(0,12)` (S69).
- **FINITE EXACT conclusion (local evidence): S68 is strict right-transposition radius-TWO local minimum for this ONE original global f,g.** This is not global min over all 15! g, not all-f/all-h bound, not full GF5 R3 or ASET.
- Among all 4,095 disjoint swap pairs, 2,731 negative signed mixed curvatures, most negative `kappa=-65` at (0,12),(4,11), but its endpoint is S97 due to positive individual gradients (+35,+59). Thus negative curvature does NOT automatically imply escape.
- Sum exact |kappa| = 40,989. Separately enumerated true original right SUPPORT masks verify every individual `|kappa_AB| <=2 M_AB` for all 4,095 pairs, min slack 33,604. Actual sum M_AB = **77,873,220** equals independent analytic `SUM_J K(15,|H(J)|)`; all-h absolute cap = 155,746,440, considerably too loose to imply obstruction.

**Implementation** in [PR #353](https://github.com/definitely-stable/Mathlab/pull/353): new exact report, independent right-first 62,370-source hosted oracles for both tied minima, explicit all-h arithmetic and genuine W32 tests, new GitHub-hosted dedicated Contract. Full Research retains preceding **137** named commands + 2 new B6 = **139**, frozen FNV1a64 `0x908406FEEA5AC976`. Numerical values are pinned as **fail-closed assertions** and research index.

**Acceptance firewall:** independent LOCAL evidence only at current moment. Latest PR HEAD `ae748103dc6d8bfe6c7f6f653edceaae04b12643`; exact-head Contract #38129664441, Research #38129664425, INDEX #38129664455 **QUEUED**, so B6 remains IMPLEMENTED_CI_PENDING. No main change or merge. Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

**Next mathematical decision:** finite radius-two strict stationarity gives stronger counterevidence to simplistic local descent heuristics, but not to universal positivity. For C24-B7, choose between radius-three finite escape and a GQ-specific SIGNED joint-fiber inequality capable of comparing negative curvature magnitude to the sum of positive first gradients; avoid presenting mere absolute exposure cap as strong asymptotic theorem.

---

## Comment 061 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6108372914
- GitHub comment ID: 6108372914

### C24-B7 implemented — missing LEFT variable from the exact root quantifiers; stacked draft PR #354

[PR #354](https://github.com/definitely-stable/Mathlab/pull/354) is based EXACTLY on [fully hosted-green C24-B6 #353](https://github.com/definitely-stable/Mathlab/pull/353), with predecessor B5 #352/B4 #348/B3 #347 also all exact-head Contract/Research/INDEX SUCCESS. No main changes or merge.

**Critical scientific audit:** B4/B5/B6 held ONE globally complete original LEFT f fixed; although true ORIGINAL W32 map g68 achieved **S=68** and is strict RIGHT radius-two local minimum (105 neighbors min75, 5005 exact-two neighbors min69), root issue #230 quantifies over `inf_{f_s,g_s}` for ALL legal global left/right injections. Thus neither finite stationarity nor universal obstruction has been established.

**All-h exact typed cross-side identity:** for ORIGINAL point transposition A of global f and ORIGINAL line transposition B of global g, `kappa_LR(A,B)=S(f^A,g^B)-S(f^A,g)-S(f,g^B)+S(f,g)`. Individual original **distinct** six-incidence J contributes nothing unless J touches BOTH swapped original point set and original line set; its contribution is at most 2 in absolute value. For W(3,s), `E=(s+1)^2(s^2+1)`, `d=2(s+1)`, `c=#incidences between the two swapped original points and two swapped original lines (0..3)`, the EXACT *unrestricted original sixset* joint-touch support size is `M=C(E,6)-2C(E-d,6)+C(E-2d+c,6)`, so `|kappa_LR|<=2M`. **This upper bound is deliberately labeled too loose for s^6: not a signed descent lemma, Branch A/B or GF5 R3 upper.** Independent small-E,k brute binomial and true W32 all-105x105 point/line overlap tests are implemented.

**New finite true W32 11,236-cell typed global map rectangle:** for baseline C24-B5 f0,g68, inspect all 105 LEFT-only, 105 RIGHT-only, 11,025 simultaneous LEFT/RIGHT-global swaps, plus baseline. **For EACH LEFT swap f^A recompile the 62,370 ORIGINAL physical-left-six-incidence candidate source from scratch under f^A** — old f0 compiled left source must NOT be reused because physical-left sixset eligibility changes! Construct separate exact right inverse 130 physical-K6-two-factor source fibers from each f^A; evaluate all globally complete right swaps on its own source; retain true original sixset tag/multiplicity, accepted original right-C and frozen GF5 necessary Q7. Fully independent original LEFT-first and RIGHT-FIRST 62,370 original sixset census check both exact finite best LEFT-only and best mixed endpoints.

**Hosted workflow:** dedicated C24-B7 Contract for independent small tests and full 11,236-cell report; full six research shards + seventh aggregate and INDEX, preserving 139 prior Research commands plus two B7 = **141** and frozen independent checksum `0x3253D6F764038315`. Initial PR head `5ace8a57a39c0c0ce295133c820b1c9bace097dc`: all three new workflows QUEUED at comment time. No numerical optimum claimed before actual hosted output. The root issue stays OPEN_WITH_FORMAL_BLOCKER. Not all `(15!)^2` f,g maps, not all-h `Omega(s^6)`, no full GF5/ASET theorem.

**After hosted finite census:** preserve exact witness, report signed mixed-side interaction vs single-side gains; then seek a signed all-h incidence-tensor inequality or correlated infinite counterfamily, rather than extending finite brute-force without a proof gate.

---

## Comment 062 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6108393413
- GitHub comment ID: 6108393413

### C24-B7 theoretical audit: unrestricted typed source-touch envelope is *provably far too weak* for the target s^6 exponent

For W(3,s), s=2^h, let E=(s+1)^2(s^2+1)=Theta(s^4) original incidence edges, d=2(s+1)=Theta(s) edges incident to two swapped original points/lines, and c∈{0,1,2,3} actual original cross incidences. The exact joint-touch original sixset universe formula in draft #354 is

`M_c=C(E,6)-2*C(E-d,6)+C(E-2d+c,6)`.

**Asymptotic orders are rigorously much larger than the conjectured scale:**
- If c=0, the second finite difference yields `M_0~d^2*E^4/24~s^18/6` (the O(s^18) leading term comes from one selected incidence in each distinct swap support and four unrestricted others).
- For any fixed c>=1, the **exact positive correction** is `M_c-M_0=SUM_{j=0}^{c-1}C(E-2d+j,5)`, so `M_c~(c/120)*s^20`: a single original incidence touched by BOTH swap pairs allows selection of any other five original incidences.
- The all-h support bound `|kappa_LR|<=2 M_c` is therefore O(s^18) for disjoint incidence supports and O(s^20) for c>=1. Since HYP-105 Branch A seeks a positive lower floor on actual accepted seven-motif count S at order s^6, **this support bound has no discriminating force**. It is correct but cannot close A, B or model-equivalent C by itself.

The actual essential constraint omitted by the unrestricted binomial universe is *simultaneous physical K_{a_s} two-factor eligibility*, accepted original GQ seven-class alignment, and **SIGNED correlated cancellation across distinct original J** under shared complete f,g. An all-h research reduction must capture these or construct a genuine infinite correlated f_s,g_s counterfamily. Do not promote the support inequality to an obstruction theorem.

Dedicated B7 Contract fast independent tests already SUCCESS; its **full 11,236-state mixed f,g census is currently still running**. This comment records a proved analytic limitation, not a guessed finite numerical result.

---

## Comment 063 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6108420321
- GitHub comment ID: 6108420321

### C24-B7 true W32 fully hosted initial Contract result — strict typed left<=1,right<=1 barrier S68

[Scientific stacked DRAFT PR #354](https://github.com/definitely-stable/Mathlab/pull/354), [initial GitHub-hosted Contract #38134355587](https://github.com/definitely-stable/Mathlab/actions/runs/38134355587) **SUCCESS** on its then-exact PR HEAD `5ace8a57a39c0c0ce295133c820b1c9bace097dc`.

After **recompiling each of 105 physical LEFT-eligible original sixset sources independently**, and reclassifying all 105 RIGHT globally complete swaps for each LEFT choice, the hosted 11,236-map ORIGINAL W32 census found:
- Baseline original `f0,g68` has S=68.
- All 105 LEFT-only swaps: minimum **S=70** (swap (3,7)), **ZERO** strict improvements.
- All 105 RIGHT-only swaps: minimum **S=75** (swap (8,9)), **ZERO** improvements.
- All 11,025 joint global left+right swaps: minimum **S=70** with exactly **TWO** tied endpoints, **ZERO** improvements.
- Lex best mixed pair LEFT (3,8), RIGHT (0,14): independent left-only S95, independent right-only S97, mixed S70, exact typed kappa **-54**. Its coherent global maps: f=(13,4,2,10,0,11,1,7,14,6,9,5,12,3,8), g=(8,9,11,4,1,6,0,13,5,14,3,7,2,10,12); seven vector (0,46,18,0,0,2,4), ORIGINAL right-C=0, GF5 **necessary** numerator Q7=3,201,940. Both tied mixed-minima sources are now independently rechecked by full ORIGINAL LEFT and RIGHT-FIRST 62,370 original sixset oracles on updated branch.
- **8,286** mixed signed kappa values negative, most-negative **-70** at typed LEFT (4,14), RIGHT (4,11), yet none improves S68. Original point-line cross-incidence overlap 0:4,185; 1:5,040; 2:1,620; 3:180. The static LEFT eligible original sixset totals **vary 52,856..54,217 across 105 distinct f^A**; reusing the old source would be incorrect.

**New exact finite theorem:** At this ONE true original W(3,2) coherent complete (f0,g68), S68 is strict local minimum for the typed rectangle `LEFT <=1 global transposition, RIGHT <=1 global transposition` including simultaneous moves. Combined with predecessor B6, it's also strictly stationary for <=2 RIGHT-only swaps. This is **not** the all-(15!)² global inf, a universal all-h S>=Omega(s^6) obstruction, an infinite S=o(s^6) correlated counterfamily or a full GF5 R3 upper.

**All-h support limitation rigorously recorded:** common ORIGINAL incidence universe I has E=(s+1)^2(s²+1); d=2(s+1) touched by two original points/lines. Unrestricted joint-touch source count M_c=C(E,6)-2C(E-d,6)+C(E-2d+c,6). If c=0, M0~s^18/6. If c>=1 fixed, M_c~(c/120)s^20 because exact M_c-M0 = Σ_{t=0}^{c-1}C(E-2d+t,5). Hence `|kappa_LR|<=2M_c` is too weak by many powers to resolve the desired s^6 floor. Physical 2-factor co-eligibility, GQ signed correlations and global f,g constraints are still missing.

**Repository work:** dedicated C24-B7 Contract, independent small-universe all-h support tests, all 11,236 typed maps explicit report, all true-original f^A recompiles, both ties full original right-first validation, source and proof documentation, Research command-preserving frozen **141** steps FNV1a64 `0x3253D6F764038315`. Latest PR head at this comment `c35d6e4f9c1f60d8d5ae0b84a8e1995b08fbb75c`. Later freeze commits need **fresh exact-head Contract/Research/INDEX SUCCESS**; old-head Contract green does not count. No main edits or merge. Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 064 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6108934346
- GitHub comment ID: 6108934346

### C24-B8-A implemented — ALL-h exact physical-motif tensor, on separate stacked draft PR #357 (2026-10-11)

[PR #357](https://github.com/definitely-stable/Mathlab/pull/357) is stacked **directly** onto the independently exact-HEAD all-three-green B7 [PR #354](https://github.com/definitely-stable/Mathlab/pull/354), base HEAD `c35d6e4f9c1f60d8d5ae0b84a8e1995b08fbb75c`. New B8-A HEAD at PR creation: `1367ea656693f5ca7b50c352407c851e3740d83f`. **No main mutation and no merge.**

**Proposed all-h restricted theorem (exact combinatorial identity):** Six ordinary positively certified original six-incidence classes have exact Boolean tensor acceptance `X_J(f,g)=L_J(f)*R_J(g)`, where L/R require genuine physical K_a six-coordinate degree-two 2-factors under the ONE complete original f and g. D6 requires an exact equality of connected dual C6 signatures on the six ORIGINAL incidence positions; its acceptance is the dot product of one-hot vectors indexed by 60 six-position Hamiltonian cycles, NOT a product of ordinary physical Booleans. Thus for globally coherent original typed point/line transpositions A,B, the mixed signed gradient decomposes EXACTLY as `kappa=sum_ordinary Delta_A L_J Delta_B R_J + sum_D6 <Delta_A L_J,Delta_B R_J>`. For all h, an explicit physical joint-state change support cap follows (ordinary <=1/J, D6 <=2/J). This replaces B7's unrestricted incidence-touch *upper* envelope but does NOT prove s^6 growth or even any sign.

**Independent implementation and falsifiers:** New [proof note](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-c24b8a-physical-tensor/docs/research/HYP-105-G5-E2-B3-E1C24B8A-PHYSICAL-TENSOR.md), core `research/hyp105_g5e2b3e1c24b8a_physical_tensor.py`, fast seven-tag/D6/small-original-W32 cross-checks against old independent `reference_classifier`, and an **isolated** W32 original 62,370-sixset recompilation for BOTH changed left maps (union of their source domains), verifying authentic four-corner B7 `S=(68,95,97,70), kappa=-54` at (L3,8;R0,14) and separately `kappa=-70` at (L4,14;R4,11). Only these 4-map witnesses are executed, NOT B7's whole 11,236 rectangle.

**CI budget:** Existing 141 named Research commands and six research shards plus aggregate are **unchanged**; new quick unit checks are discovered by the existing foundation shard. A new dedicated GitHub-hosted B8-A Contract runs quick tests then the heavy pair of exact 4-map witness audits; it triggers only on PR/manual (not duplicate branch push), and PR cancellation is enabled. INDEX remains mandatory. Exact latest-head runs: [Contract #38138656686](https://github.com/definitely-stable/Mathlab/actions/runs/38138656686), [Research #38138656669](https://github.com/definitely-stable/Mathlab/actions/runs/38138656669), [INDEX #38138657094](https://github.com/definitely-stable/Mathlab/actions/runs/38138657094). **Pending hosted verdict; keep DRAFT on any failure.**

**Scientific decision:** RESTRICTED_THEOREM_C for exact representation only IF independently verified; root #230 remains OPEN_WITH_FORMAL_BLOCKER. No PROVED_A, no COUNTEREXAMPLE_B infinite family, no whole GF5 R3 bound, no ASET exponent. Next B8-B needs a uniform **SIGNED** correlation bound on the physically admissible six-incidence tensor, or an explicit globally correlated infinite f_s,g_s counterfamily. Do not conflate this exact identity with a nontrivial asymptotic lower.

---

## Comment 065 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6108943828
- GitHub comment ID: 6108943828

### C24-B8-A first exact-head GitHub-hosted Contract SUCCESS — substantial finite physical-curvature bound improvement

[Contract run #38138656686](https://github.com/definitely-stable/Mathlab/actions/runs/38138656686) **SUCCESS** on immutable B8-A PR #357 HEAD `1367ea656693f5ca7b50c352407c851e3740d83f`. All 4 quick independent seven-tag/D6/small-W32 tests **passed in 0.182 s**, followed by explicit independent original W32 4-map tensor oracles.

Both left f0 and swapped f^A were **independently** source-enumerated (62,370 sixsets apiece; union 98,982; **36,612 newly eligible** after the original left swap). No frozen f0-only reuse.

| True original typed W32 | Four scores (S00,S10,S01,S11) | Exact signed kappa | Old unrestricted B7 absolute cap | New physically changing source absolute cap |
|---|---|---:|---:|---:|
| LEFT (3,8), RIGHT (0,14) | (68,95,97,70) | -54 | 5,454,764 | **737** |
| LEFT (4,14), RIGHT (4,11) | (68,107,127,96) | -70 | 6,485,948 | **724** |

The first case additionally passed the separate original RIGHT-FIRST census. The seven-class signed vector for kappa=-54 is D6:-1, B-left/A-right:-22, A-left/B-right:-23, C/A:-2, C/B:-1, B/B-overlap:-5, B/B-disjoint:0. For kappa=-70: D6:0, B-left/A-right:-15, A-left/B-right:-48, C/A:-3, C/B:0, B/B-overlap:0, B/B-disjoint:-4. Both sum exactly and reproduce four left-first scores.

**Careful scientific limit:** 737 and 724 are valid sourcewise absolute bounds for TWO finite W(3,2) rectangles. They are not signed inequalities for all f,g, not Omega(s^6), not full R3, not a novel ASET exponent. The geometric all-h *identity* is proved algebraically, but asymptotic quantitative control of the physical source-change cap is OPEN. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.

Acceptance status remains **PENDING** until full [Research #38138656669](https://github.com/definitely-stable/Mathlab/actions/runs/38138656669) six shards+fail-closed aggregate and [INDEX #38138657094](https://github.com/definitely-stable/Mathlab/actions/runs/38138657094) on the SAME exact head also succeed. Do not modify the branch solely to pin the already archived numerical logs: doing so would invalidate this successful exact-head Contract and create another full Research queue. No main changes, no merge.

---

## Comment 066 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109080388
- GitHub comment ID: 6109080388

### C24-B8-B implemented as separate stacked scientific PR #358 — all-h signed physical transition balance + exact random-global-map first moment (2026-10-11)

[PR #358](https://github.com/definitely-stable/Mathlab/pull/358), head `d79fddff6c046daff1f6eaacec3fbf79779f6355`, is stacked **only on** [B8-A PR #357](https://github.com/definitely-stable/Mathlab/pull/357) head `1367ea656693f5ca7b50c352407c851e3740d83f`, not main. Both PRs remain Draft and no merge is authorized.

1. **ALL-h RESTRICTED signed identity (B8-B1):** using exactly the same ORIGINAL distinct GQ six-incidence population and global complete left/right injections, classify changed ordinary physical 2-factor eligibility as gain/gain, loss/loss (+) vs gain/loss, loss/gain (-); for D6 classify MATCHED one-hot connected C6 cycle signature changes (per-source absolute change <=2). `kappa_LR=sum_t(P_t-N_t)` and `|kappa|<=P+N<=B8A_physical_change_cap<=2*B7_original_joint_touch_universe`. It is not a positive S lower bound and not a sign guarantee.
2. **ALL-h sign-orbit involution (B8-B2):** reversing exactly one typed original global swap orientation negates mixed kappa, so the *complete right-injection orbit* has exact mean kappa=0 for fixed f,A,B; positive and negative nonzero kappa values pair exactly. Strictly negative mixed curvature for ALL unrestricted g is impossible unless the curvature vanishes. A typed joint improvement is iff `N-P > Delta_left_S+Delta_right_S`, which negative kappa alone does not satisfy.
3. **ALL-h exact independent-whole-injection expectation (B8-B3):** probabilities for a physical 2-factor given fixed ORIGINAL endpoint-multiplicity profiles are `p_A=70*C(a,6)*6!/(M)_6`, `p_B=45*C(a,6)*4!/(M)_5`, `p_C=15*C(a,6)*3!/(M)_3`, `M=C(a,2)`. A fixed connected D6 dual-cycle signature has `p_sig=C(a,6)*6!/(M)_6`, so a genuine D6 ORIGINAL source contributes expectation `60*p_sig^2`, ordinary profile u,v contributes `p_u*p_v` under two independent **whole global** injections. Global source-dependency is retained; no false sixset independence. The complete all-h expected S is a weighted sum over still-to-be-counted ORIGINAL GQ typed sixset profile counts. **inf S<=E S, not >=**: no universal obstruction or concentration follows.
4. **Independent executable proof/falsifier:** seven-source signed transition code, exact rational profile counter, fast independent 130-K6-template A70/B45/C15 census and 60*720 D6 signature labellings, 3,003 ORIGINAL W32 small-source B2 independent classifier check, D6 +/-2 non-Boolean witnesses. Separate two-W32-case CI-only original source recompile (f0 and f^A, 62,370 each, union 98,982) examines authentic B7 kappa=-54 and -70, accounts P/N by tag and a precise typed escape threshold, checks left-first and full original right-first. **No 11,236-state B7 rerun**.
5. **Acceptance pending on immutable B8-B head:** [dedicated Contract #38139787028](https://github.com/definitely-stable/Mathlab/actions/runs/38139787028), [full inherited Research #38139786964](https://github.com/definitely-stable/Mathlab/actions/runs/38139786964) (all six shards plus fail-closed aggregate), [INDEX #38139787001](https://github.com/definitely-stable/Mathlab/actions/runs/38139787001). All were QUEUED at this update. Original Research commands unchanged; no new heavyweight default unittest, no proof-result cache, no self-hosted runner.

**Scientific classification:** RESTRICTED_THEOREM_C (exact signed and annealed identities) if exact-head CI green, NEVER PROVED_A or COUNTEREXAMPLE_B. Root #230 OPEN_WITH_FORMAL_BLOCKER. Next B8-C targets a genuine ALL-f,g signed sixset-discrepancy bound or an explicit infinite correlated low-S family; the orbit-zero-mean identity and random-map mean alone provably do not settle the target.

---

## Comment 067 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109107835
- GitHub comment ID: 6109107835

### C24-B8-B exact-head hosted dedicated Contract and INDEX SUCCESS; independently verified signed cancellation (2026-10-11)

PR [#358](https://github.com/definitely-stable/Mathlab/pull/358) HEAD `d79fddff6c046daff1f6eaacec3fbf79779f6355` is unchanged. [Dedicated hosted Contract #38139787028](https://github.com/definitely-stable/Mathlab/actions/runs/38139787028) **SUCCESS**, with all **five** independent light tests in 0.665s and both isolated TRUE original W32 signed 4-corner source witnesses; [INDEX #38139787001](https://github.com/definitely-stable/Mathlab/actions/runs/38139787001) **SUCCESS**.

**New exact finite signed physical counts**, directly from the hosted witness logs (NOT invented or asymptotic):

| Authentic complete original W32 rectangle | Four S values | P matched same-sign | N matched opposite-sign | P+N exact matching absolute cap | B8-A physical cap | B7 original-touch absolute cap | Signed kappa | Strict-descent surplus |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| LEFT (3,8), RIGHT (0,14) | (68,95,97,70) | **27** | **81** | **108** | 737 | 5,454,764 | -54 | **-2** |
| LEFT (4,14), RIGHT (4,11) | (68,107,127,96) | **33** | **103** | **136** | 724 | 6,485,948 | -70 | **-28** |

Source union exactly 98,982 distinct ORIGINAL six-incidence sets after independent original-left physical recompilation for BOTH f0 and f^A; 36,612 new candidates under each swapped-left map. Positive/negative matched counts by each of the seven source tags sum to signed curvature exactly. First-moment theorem, sign-involution, and D6 60 connected-cycle semantics independently tested.

Exact joint improvement iff `N-P > (S10-S00)+(S01-S00)`: case1 54<27+29=56; case2 70<39+59=98, hence no improvement, matching independently computed S11=70 and S11=96. New P+N physical-matched source cap is substantially smaller than B8-A's raw physical joint state-change cap, itself much smaller than B7's unrestricted incidence touch bound. Finite source-specific tightening is NOT an asymptotic s^6 statement.

**Acceptance still PENDING:** [full Research #38139786964](https://github.com/definitely-stable/Mathlab/actions/runs/38139786964) on same HEAD is QUEUED at this check; do not substitute older B8-A or B7 green. No PR branch amend solely to pin measured numbers; preserve exact-HEAD Contract. No main change or merge, #230 remains OPEN_WITH_FORMAL_BLOCKER. B8-C must quantify a signed six-incidence discrepancy uniformly for all complete f,g and s=2^h, not merely optimize these two finite witnesses.

---

## Comment 068 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109300133
- GitHub comment ID: 6109300133

### C24-B8-C implemented — exact fixed-f conditional mean, one-pin information NO-GO, two-edge orbit split and right-C forced-zero (2026-10-11)

[New stacked draft PR #359](https://github.com/definitely-stable/Mathlab/pull/359), immutable initial head `04ccac48399ab405ab40d90ffde0b70313651377`, is based EXACTLY on scientific B8-B [draft PR #358](https://github.com/definitely-stable/Mathlab/pull/358) head `d79fddff6c046daff1f6eaacec3fbf79779f6355`. No main modifications, no merges.

**ALL-h C1 exact conditional-right fixed-left mean**: for every original genuine W(3,s), s=2^h>=2, and any complete global left physical-edge injection f, `mu_s(f)=E_(uniform complete global right injection g) S_s(f,g)` equals the ORIGINAL physically LEFT-eligible six-incidence source count weighted by B8-B's exact p_A/p_B/p_C of each RIGHT original profile, plus left CONNECTED D6 source count weighted by the probability of ONE fixed right dual connected C6 signature p_sig. Sourcewise linearity, no fake independent J or per-J right map. Implemented via B2 original compressed-with-multiplicity fibers and independently checked against original uncompressed 62,370-source W32 enumeration in hosted witness.

**ALL-h C2 independent RIGHT-only physical-coordinate symmetry**: physical Sym(a) acts transitively on one K_a edge while preserving ordinary physical right six-coordinate 2-factors and D6 six-incidence-position dual cycle signature; f remains fixed. Hence `E[S|g(i)=e]=mu_s(f)` for EVERY original right line i and host physical edge e. With one e=(0,1) pinned, the physical-stabilizer has EXACTLY TWO second-edge orbits for any other original right line j: 2(a-2) adjacent edges and C(a-2,2) disjoint edges; their conditional means obey `2(a-2)*mu_adj+C(a-2,2)*mu_dis=(C(a,2)-1)*mu_s(f)`. This is a nontrivial source-orbit reduction but NOT a lower bound on min_g or a concentration inequality. Higher anchors may still have strong correlations.

**ALL-h C3 original RIGHT C=(2,2,2) hard zero:** three distinct right lines repeated twice must map to THREE PAIRWISE DISJOINT physical edges to give a right 2-factor. If two physical pinned edges INTERSECT, the source is rejected for EVERY legal completion. With disjoint pinned lines, conditional right eligibility probability `C(a-4,2)/(C(a,2)-2)`; at true W32 physical a=6, adjacent=0, disjoint=1/13, unpinned p_C=3/91.

**Executable and CI budget:** New exact conditional source probability and guarded injective-completion oracle, five fast standalone unit tests including D6, B/C hard-zero, original W32 3,003-source independent compression comparison, physical Sym(a)-conjugate anchored profiles. Dedicated W32 hosted-only witness independently enumerates full 62,370 left-eligible ORIGINAL sixsets and compares per-tag exact `mu(f0)` with B2's differently constructed original compressed fibers; compares independently RIGHT-FIRST real g68 score 68; tests three RIGHT-only coordinate relabelings preserving entire seven-score; constructs a genuine original W32 right-C two-orbit hard-zero. Explicit C24-B8-C Contract includes fast test and ONE true original source witness. Existing 141 Research steps and six-shard full Research+aggregate, INDEX remain unchanged. NO 11,236-cell B7 orbit or 15! permutation enumeration.

**Exact-head acceptance PENDING:** [Contract #38141486887](https://github.com/definitely-stable/Mathlab/actions/runs/38141486887), [Research #38141486780](https://github.com/definitely-stable/Mathlab/actions/runs/38141486780), [INDEX #38141486804](https://github.com/definitely-stable/Mathlab/actions/runs/38141486804), all at current head; numerically exact W32 mean intentionally NOT guessed before hosted logs. Any test mismatch keeps Draft; do not imply CI SUCCESS from older B8-A/B heads. Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER. No PROVED_A all-f lower, no infinite counterfamily B, no full GF5 R3 or ASET claim.

**NEXT research gate:** worst-case `D_s(f)=mu_s(f)-min_g S_s(f,g)` from signed ORIGINAL incidence 6-motif discrepancy, and independent all-f `mu_s(f)>=c0*s^6`. The zero one-pin information and exact two-pin orbit projection do NOT imply small D_s(f).

---

## Comment 069 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109316505
- GitHub comment ID: 6109316505

### C24-B8-C exact HEAD dedicated hosted Contract + INDEX SUCCESS, first TRUE original W32 conditional mean (2026-10-11)

Scientific [stacked draft PR #359](https://github.com/definitely-stable/Mathlab/pull/359) HEAD `04ccac48399ab405ab40d90ffde0b70313651377`, base B8-B PR #358 HEAD `d79fddff6c046daff1f6eaacec3fbf79779f6355`. [Dedicated B8-C Contract #38141486887](https://github.com/definitely-stable/Mathlab/actions/runs/38141486887) **SUCCESS** at exact head: all **five** fast tests passed in 0.399s, plus the independent real original W32 physical left source/conditional expectation and coordinate-orbit report. [INDEX #38141486804](https://github.com/definitely-stable/Mathlab/actions/runs/38141486804) also **SUCCESS** on same head.

**First independently reproduced exact real W(3,2) fixed-f mean across ALL complete original right injections g** (no 15! enumeration, no per-J independent labeling): freeze the C24-B1 true original complete LEFT f0 and verify via B2 compressed fibers AND independent 62,370 ORIGINAL left-sixset enumeration. Exactly **53,907 statically left seven-family eligible ORIGINAL sixsets**. The exact rational mean is

```
mu_2(f0) = E_g S_2(f0,g) = 870476 / 5005 = 173.92127872127872...
```

For the previously independently certified one complete ORIGINAL right g68, S_2(f0,g68)=68 and confirmed by independent 62,370-source RIGHT-FIRST scorer; hence exact observed conditional signed discrepancy

```
mu_2(f0) - S(f0,g68) = 530136 / 5005 = 105.92127872127872...
```

This certifies **D_2(f0) >= 530136/5005**, NOT equality, because global `min_{15! complete g}` remains unknown. It is a finite falsifier for too-strong uniform small-discrepancy conjectures that include this W32 f0; NO infinite-h negative counterfamily B is obtained.

Genuine left-eligible original source populations and rational mean contributions, in accepted seven order:
- D6: N=21,186, mean 1926/455.
- B-left/A-right: N=6,098, mean 12196/143.
- A-left/B-right: N=21,954, mean 65862/1001.
- C/A: N=342, mean 513/91.
- C/B: N=96, mean 288/1001.
- B/B-overlap: N=1,588, mean 4764/1001.
- B/B-disjoint: N=2,643, mean 7929/1001.

Real original right-C=(2,2,2) six-incidence source of tag **C/A** was independently found, with original repeated right lines (0,1,5), and pinned pair (0,1): adjacent physical right assignments force EXACT conditional acceptance probability **0**; disjoint assignment has exactly **1/13**, global marginal **3/91**. The full original seven-vector remained EXACTLY unchanged for three independent RIGHT-only physical S6 coordinate transpositions with fixed LEFT f0. All match B8-C2/C3 orbit theorems; note a stronger mathematical consequence of coordinate transitive invariance is actually the full conditional LAW of S, not just its mean, is the same after any ONE physical right edge pin. Conditioning on TWO physical edges splits into adjacent vs disjoint orbits; neither implies a worst-case lower on min_g.

**Mandatory last gate**: full six-shard [Research #38141486780](https://github.com/definitely-stable/Mathlab/actions/runs/38141486780) (with fail-closed seventh aggregate) is still running on this exact head. Four science shards have SUCCESS, LENT foundation and HYP coupled exact in progress at last job poll. Older B8-B PR #358 latest-head full Research has now SUCCESS; do NOT conflate old green with new B8-C acceptance. No HEAD change just to pin measured values; retain exact-head Contract. No main modification, no merge; root #230 OPEN_WITH_FORMAL_BLOCKER, Branch A/B unproved.

Next meaningful stage **B8-D**: build the FULL original-line pair conditional influence matrix `I_f(i,j)=mu_adj(f;i,j)-mu_dis(f;i,j)` from left-eligible original sixset fibers and exact physical right completion probabilities; quantify sign and six-motif correlation, not merely the random-map first moment or existing W32 local-swap orbits. DO NOT claim a spectral/variance estimate without proof.

---

## Comment 070 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109534281
- GitHub comment ID: 6109534281

### HYP-105 C24-B8-D — new stacked draft [PR #360](https://github.com/definitely-stable/Mathlab/pull/360)

Parent: [B8-C #359](https://github.com/definitely-stable/Mathlab/pull/359) at `04ccac48399ab405ab40d90ffde0b70313651377`; child exact HEAD `a221b0f817cf06e350974a71f6eee74c30a0f142`. No main changes, no merge, GitHub-hosted runner only.

**Proof scope:** with one complete uniform global RIGHT injection g and arbitrary fixed complete LEFT f, `I_f(i,j)=Cov(S,Z_ij)/(p(1-p))` where `p=4/(a+1)`. Derive exact per-source accepted-motif conditional adjacency via ALL three cases: both pinned original right lines within source, exactly one within, or neither within (nonzero complement edge-depletion!). Preserve ORIGINAL source multiplicities and matched six-POSITION D6 cycle. Aggregate into exact seven-tag 105-pair W32 matrix in linear-time compressed-fiber updates.

**Additional rigorous all-f W32 theorem:** because all 15 K6 edges are occupied, `sum_(j!=i)I_f(i,j)=0` for each row; with physical host slack n<M, correction is `-Cov(S,unoccupied_edges_adjacent_to_g(i))/(p(1-p))`. Full invariant-score MINIMUM cannot generally be recovered from pair-conditional means; this is a limited NO-GO over arbitrary right-coordinate invariant scores, not a NO-GO for this specific seven-score or Branch A.

[Detailed proof](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-c24b8d-two-line-influence/docs/research/HYP-105-G5-E2-B3-E1C24B8D-TWO-LINE-INFLUENCE.md). New exact algebra module, 5 fast independent physical pinned tests and isolated independent ORIGINAL W32 62,370-sixset 3-pair cross-check. Dedicated B8-D Contract, inherited Full Research six shards + fail-closed aggregate and INDEX must ALL succeed on the same final PR #360 HEAD. **No CI acceptance claimed yet.** Root remains `OPEN_WITH_FORMAL_BLOCKER`: neither universal `Omega(s^6)` nor infinite o(s^6) global labeling family proved; do not extrapolate W32 data to all h or full R3/ASET.

---

## Comment 071 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109561826
- GitHub comment ID: 6109561826

### C24-B8-D exact-HEAD hosted W32 result and two-pin limitation (no commit to rerun CI)

GitHub-hosted Dedicated Contract **SUCCESS** on `5e13aa08f4a1322e6255139aa14c68457a895823`: [run 38143434395](https://github.com/definitely-stable/Mathlab/actions/runs/38143434395). All 5 fast falsifiers and independent genuine-original W32 witness succeeded. 62,370 original left candidate sixsets, 53,907 left-eligible originals, 105 exact right-line influences; independent ORIGINAL direct pair checks (0,1), (0,7), (3,10) match compressed fibers. Signs: +47, -58, 0 exactly 0. `min I=-70739/5720`, `max I=17483/1560`, all 15 exact rational row sums zero. Fixed-f exact mean remains `870476/5005`; coherent original S68 g remains valid.

**New strict finite W32 one-pair gate:** because `mu_adj=mu+(3/7)I` and `mu_dis=mu-(4/7)I` for `a=6`, the BEST two-edge orbit conditioning over any ONE chosen original right-line pair and either adjacency class yields precisely

```
min_(i<j, orbit in {adj,dis}) E_g[S(f0,g) | orbit(i,j)]
 = 870476/5005 - 17483/2730   (about 167.517).
```

But the actual complete right g68 has `S(f0,g68)=68`, a mean reduction of `530136/5005` (about 105.921). Thus one chosen pair-orbit conditioning explains at most `17483/2730` (about 6.404) of that reduction. This is an exact restricted finite quantitative certificate of the **single-pair projection's inadequacy**, NOT a proof that the full jointly observed pair graph or higher-order correlated projections are insufficient.

Full Research for the new B8-D final HEAD is still running, with INDEX SUCCESS; no all-three-gates acceptance claimed pending final Research fail-closed aggregator. #230 remains OPEN_WITH_FORMAL_BLOCKER, no merge.

---

## Comment 072 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109700203
- GitHub comment ID: 6109700203

### HYP-105 C24-B8-E — stacked [Draft PR #361](https://github.com/definitely-stable/Mathlab/pull/361)

B8-D parent [PR #360](https://github.com/definitely-stable/Mathlab/pull/360) **all three CI gates SUCCESS** on its final HEAD `5e13aa08f4a1322e6255139aa14c68457a895823`, including all 6 Research jobs and mandatory fail-closed `research-full-suite`. New E branch `research/hyp105-c24b8e-pair-harmonic-residual` initially at `1f6e020f172011d0c4fdd1808a511ea91d8d18f3`, stacked strictly on the B8-D branch. No main changes, no merge, only GitHub-hosted CI.

**ALL-h restricted theorem C:** For the ONE uniform global original-right complete injection to K_a edges (M=C(a,2)), covariance of two centered pair-adjacency indicators equals v on identical index pairs, `-v/(M-2)` on pairs sharing one ORIGINAL right index, and `2v/((M-2)(M-3))` on disjoint index pairs, where `v=4/(a+1)*(1-4/(a+1))`. The exact Johnson Gram has 3 eigenspaces with lambda0/lambda1/lambda2 as documented in the PR. B8-D's exact D6-aware ORIGINAL source matrix supplies `b=Cov(S,Z)=v*I`. The pseudoinverse gives an exact best-L2 pair-linear score component P2 and orthogonal nonlinear residual R; no unbiased independence or concentration assumptions. At true W32, Gram rank 90, nonzero eigenvalue 2/7 and pair coefficient `gamma=6 I/7`.

**Tested only after new exact-head CI:** Independent K6 15P4=32,760 injective images for small-host Gram, singular nullspace gates and independent true ORIGINAL W32 global g68 score / nonlinear residual. If hosted oracle verifies a nonzero true W32 residual, it disproves an affine pair-feature representation of this actual seven-score at this f0, not the existence of an arbitrary nonlinear function of all pair features, or any all-h universal lower.

**Blocker unchanged:** no all-f uniform pointwise residual estimate, no `inf_(f,g) S_s=Omega(s^6)`, no infinite coherent counterfamily `o(s^6)`, and no full GF(5) R3 / ASET claim. CI acceptance for E pending new exact-head Contract, full six-shard Research+aggregator, INDEX.

---

## Comment 073 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109710990
- GitHub comment ID: 6109710990

### C24-B8-E — exact hosted original W32 nonlinear residual: certified numerical and structural results

[Draft PR #361](https://github.com/definitely-stable/Mathlab/pull/361), currently exact HEAD `1f6e020f172011d0c4fdd1808a511ea91d8d18f3`. [B8-E Dedicated Contract run 38144611303](https://github.com/definitely-stable/Mathlab/actions/runs/38144611303) **SUCCESS on that exact HEAD**: 4 independent fast tests (including 32,760 full K6 four-original-line physical injections, complete six-feature joint covariance and artificial nonlinear test), and a separate original W32 full seven-score witness with independent original right-first verification. INDEX [run 38144611334](https://github.com/definitely-stable/Mathlab/actions/runs/38144611334) SUCCESS. B8-E Full Research [run 38144611367](https://github.com/definitely-stable/Mathlab/actions/runs/38144611367) still IN_PROGRESS; no 3/3 acceptance claimed.

**NEW exact real original W32 certificate, not artificial Pasch/motivic example:**

```
mu_2(f0) = 870476/5005 ≈ 173.921279
S_2(f0,g68) = 68                   (independently right-first verified)
P2(f0,g68) = -6875243/60060 ≈ -114.472910
R(f0,g68)  = 73373/8580 ≈ +8.551632
E_g[P2(f0,g)^2] = 329290770373/450900450 ≈ 730.295945
```

Exactly `S=mu+P2+R=68`. The **actual** seven-family `S(f0,·)` is not affine in the 105 pair-adjacency indicators (because this one genuine global g has nonzero L2-orthogonal residual). The sharp finite witness consequence is `||R(f0,·)||_infinity ≥73373/8580`, nothing asymptotic. Critically, at this witness the linear pair projection contributes about -114.473 to the mean-centered score, while the nonlinear residual offsets about +8.552. Hence the earlier single-pair conditional-mean insufficiency should NOT be misread as failure of the entire jointly optimized 105-feature linear projection to explain the S68 witness.

**Next mathematical gate, not another numerical scan:** characterize worst-case negative pair-linear quadratic assignment and obtain independently certified pointwise nonlinear-residual control, uniformly over arbitrary global LEFT f; the exact Gram L2 variance alone cannot bound `min_g S`. Root Branch A/B both open, no full GF(5) R3 or ASET theorem, no merge/main changes.

---

## Comment 074 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109864425
- GitHub comment ID: 6109864425

### HYP-105 C24-B8-F initiated — exact signed-star relaxation (2026-10-11)

Created stacked **Draft [PR #362](https://github.com/definitely-stable/Mathlab/pull/362)** on B8-E [PR #361](https://github.com/definitely-stable/Mathlab/pull/361), pinned to `1f6e020f172011d0c4fdd1808a511ea91d8d18f3`. Current B8-F HEAD at creation: `3489d26affa80bdb73abc131b19317a05ed2b98c`. No main edits/merges.

**Restricted theorem:** For exact full host n=C(a,2), any coherent physical edge-bijection induces a physical star design; true W32 `P_2=(6/7)sum_{u=0}^5 sum_{i<j in T_u(g)} I_f(i,j)`. For any rational star prices `y`, exact `P_2(g)>=((m-3)/(m-1))*(2sum y+a*min_{|U|=a-1}[W(U)-sum_{i in U}y_i])`. W32 needs only 3003 possible star subsets, and the rational dual is independently rechecked. This bounds **pair projection only**, not `S`, and is not the exact QAP global minimum.

**Nonlinear residue formal gate:** An independent all-g bound `R(f,g)>=r_f` is still required for `S(f,g)>=mu_f+L_P(f)+r_f`. B8-E's finite `R(f0,g68)=73373/8580` cannot be substituted as a universal floor. Large h generally have n<m, so the full-host star result is not an all-h W(3,s) bound.

**Evidence:** dedicated hosted contract with 720 exhaustive K4 coherent bijections and true original W32 f0/g68 right-first 62,370-source check, plus inherited full Research and INDEX. Await exact-head CI; keep both stacked PRs Draft pending acceptance. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`; no Branch A/B or complete R3/ASET conclusion.

---

## Comment 075 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109894920
- GitHub comment ID: 6109894920

### B8-F exact hosted certificate: first scientific verdict (PR #362, HEAD `3489d26affa80bdb73abc131b19317a05ed2b98c`)

Dedicated GitHub-hosted Contract completed **SUCCESS**, both exhaustive coherent K4 `6!=720` assignment tests and independent true original W32 sixset source oracle. [Exact job log](https://github.com/definitely-stable/Mathlab/actions/runs/38145858890/job/114488933667). INDEX **SUCCESS**, inherited Full Research still queued at check time.

At fixed genuine W32 `f0,g68`:
- `mu=870476/5005`, `S(g68)=68`, `P_2(g68)=-6875243/60060`, `R(g68)=73373/8580`;
- 3003 individual 5-line star subsets; exact naive all-g `T>=-1053071/4290`;
- after exact rational dual ascent `T>=-279137/1287`, hence **for every global right bijection** `P_2>=-558274/3003`;
- first dual sweep already reaches the reported certificate; additional 3 sweeps are stationary. **No dual/global primal optimality claim.**

**NEW FINITE IMPOSSIBILITY GATE (for THIS separated certificate):** To deduce `S>0` using `mu+L_P+r`, an all-g uniform residual floor would need `r>25706/2145`. But the actual valid g68 has `R(g68)=73373/8580 < 25706/2145`, a strict gap `9817/2860`. Therefore **NO valid all-g residual lower bound can possibly close the positive-floor criterion using this current L_P**. This rules out the *present separated certificate*, **not** Branch A, B or the HYP-105 conjecture. Before pursuing `R` alone, strengthen `L_P` by >`9817/2860` or use a **joint correlated pointwise bound on `P_2+R`**.

Strategic next fork: partial-host all-h n<m extension by deterministic line-graph degree-capacity row bounds or star-occupancy relaxation; W32 full-bijection star formula alone is not uniform in h. Research and INDEX acceptance continue on exact HEAD, no new commits solely to store numeric outputs or duplicate CI.

---

## Comment 076 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6110035856
- GitHub comment ID: 6110035856

### HYP-105 C24-B8-G — all-h physical-host slack theorem implemented, stacked Draft [PR #363](https://github.com/definitely-stable/Mathlab/pull/363)

Pinned parent B8-F [PR #362](https://github.com/definitely-stable/Mathlab/pull/362) HEAD `3489d26affa80bdb73abc131b19317a05ed2b98c`; new B8-G HEAD `4e28b85298fd7ddca1d3e7339e471a00ea60fc19`. No main updates, no merge.

**Sharp ALL-h physical geometry for any one legal global right injection:** `n=(s+1)(s²+1)`, minimal `a`, `m=C(a,2)`, `q=m-n<=a-2`, `d=2(a-2)`. Each assigned host edge has occupied degree `max(0,d-q)<=k_i<=min(d,n-1)`. The induced physical line-graph adjacency count has **attained** extrema `A_min=m(a-2)-dq+max(0,2q-a)` and `A_max=m(a-2)-dq+C(q,2)`. Independent constructive proof: deleted q-host-edge matching/disjoint-paths/star.

**Pointwise all-h B8-E pair-projection certificate** for ANY exact rational gamma: sort each original-line coefficient row; `F_i(k)=sum of smallest k`. For any rational scalar t, `P_2(f,g)>=0.5*sum_i min_{k in [lo,hi]}(F_i(k)-tk)+(t*A_min if t>=0 else t*A_max)-p*sum gamma`. A finite rational breakpoint scan finds the optimum **within this relaxation**, not a real QAP or seven-score minimum. Budgeted fallback remains valid.

**Independent hosted Contract:** exhaustive all 360/720/720 coherent K4 injections, all missing-edge subsets of K4/K5/K6 confirming sharp total-count extrema, true original W32 f0,g68 score-68 and nonlinear residual, plus **explicitly synthetic** s=4 n85/K14/q6/degree18..24 pair feature `Z01-4/15`; synthetic score is NOT original W(3,4) S. Exact-head CI currently queued; inherited research and INDEX unchanged.

**Root remains OPEN_WITH_FORMAL_BLOCKER:** No uniform bound on original seven-score S or nonlinear residual R; no Branch A/B, full R3, or ASET claim. Dedicated, Research and INDEX must all pass at B8-G FINAL HEAD. Do not merge based on this restricted theorem.

---

## Comment 077 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6110051565
- GitHub comment ID: 6110051565

### B8-G final-head Dedicated Contract SUCCESS — scientific numeric audit

Stacked Draft [PR #363](https://github.com/definitely-stable/Mathlab/pull/363) at **exact HEAD `4e28b85298fd7ddca1d3e7339e471a00ea60fc19`**: Dedicated [GitHub-hosted run #38147158778](https://github.com/definitely-stable/Mathlab/actions/runs/38147158778) **SUCCESS**. Six independent named tests PASS, exhaustive K4 global injections and all deleted-edge K4/K5/K6 bounds PASS; true-original W32 + synthetic s4 contract PASS. INDEX on same HEAD **SUCCESS**. Full inherited Research separately pending.

**True original W32 fixed f0, coherent g68:**
- `mu=870476/5005`, `S=68` checked from independent right-first original GQ scorer, `P_2(g68)=-6875243/60060`, `R(g68)=73373/8580`;
- **all-g B8-G row+cardinality projection lower** `L_P=-25084333/120120`, selected t=0;
- older tighter **all-g B8-F full-star dual lower** `-558274/3003`. B8-G's general all-h degree relaxation is **weaker on W32**; report both without implying monotonic improvement.
- B8-G separated positive gate would require a uniform residual lower strictly above `598987/17160`, but observed legal R68 is smaller: this *particular separated certificate* provably cannot close S>0. It is not a lower-bound disproof for S.

**s=4 n<m SYNTHETIC check only:** n=85, a=14, m=91, q=6, occupied row degree 18..24, *attainable physical* total A in 948..963; the exact projected synthetic score `Z01-4/15` attains its independently verified all-g lower `-4/15`. No true original W(3,4) seven-score was computed.

Scientific verdict: `RESTRICTED_THEOREM_C_ALL_h_PAIR_CAPACITY_LINF` is now covered by dedicated GitHub-hosted falsifiers, but **not full PR acceptance** until Full Research SUCCESS. Root #230 `OPEN_WITH_FORMAL_BLOCKER`; next valuable mathematical line is joint signed coupling between original six-incidence contribution and pair-residual rather than further independent marginal tightening. No main change/merge.

---

## Comment 078 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6110566904
- GitHub comment ID: 6110566904

### HYP-105 C24-B8-H — joint original-source cylinder theorem implemented

Created stacked Draft [PR #364](https://github.com/definitely-stable/Mathlab/pull/364) on [PR #363](https://github.com/definitely-stable/Mathlab/pull/363), exact parent B8-G HEAD `4e28b85298fd7ddca1d3e7339e471a00ea60fc19`, new B8-H HEAD `68285a146e6987276e6938261926e4743fe0ffbe`. Both parent B8-F and B8-G now have three exact-HEAD CI checks SUCCESS. No main changes or merges.

**New all-h conditional (PINNED CYLINDER ONLY) deterministic theorem:** The genuine fixed-left seven-score is a sum over nonnegative-weighted ORIGINAL six-incidence records, D6 retaining its exact matched dual six-position signature. Given ONE partial injective original-right physical map h, partition original source records into disjoint buckets B_t with union free-line supports U_t. Then **for EVERY whole globally coherent g extending h**,
`S(f,g)>=sum_t min_{injective phi:U_t->remaining physical edges} sum_{J in B_t} w_J*A_J(h union phi)`.
Equivalently, `P2(f,g)+R(f,g)>=L_joint(h)-mu_f`: a genuinely JOINT source-based residual gate, not the loose sum of independent P2/R minima. Merging source buckets monotonically strengthens the bound. For small residual alphabets a whole-source bucket gives exact cylinder min; budget limits are fail closed.

**Executable true GQ W32:** freeze original right-line indices 0..9 at genuine g68, leave 5 right lines and 5 physical edges (exactly 120 entire global right completions). Evaluate supportwise and <=3-free-line merged source floors, whole-cylinder exact minimum by original sixset scanner, independently verify all 120 with global 130-template right pullback, recount minimizer and g68 via ORIGINAL left-first and RIGHT-FIRST 62,370-sixset oracles, and measure exact min(P2+R) vs min(P2)+min(R) over the SAME cylinder. Synthetic nonlinear K4 independent test included; no 15! or unpinned all-g minimum.

**Precise limitation:** one fixed f0, constrained right cylinder at s=2. No universal Omega(s^6) lower, no infinite coherent low-S family, no full R3 or ASET implication. Need a global covering certificate or symbolic all-h original-source inequality; issue #230 stays OPEN_WITH_FORMAL_BLOCKER. Three CI checks at FINAL B8-H HEAD pending; do not merge by older evidence.

---

## Comment 079 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6110687031
- GitHub comment ID: 6110687031

### HYP-105 C24-B8-H verified science, C24-B8-I auditable proof-tree continuation

**B8-H parent [PR #364](https://github.com/definitely-stable/Mathlab/pull/364), exact head `68285a146e6987276e6938261926e4743fe0ffbe`: Dedicated hosted Contract SUCCESS, INDEX SUCCESS, inherited Research still in progress.** Independent actual original W32 f0, first ten g68 original-right line images pinned, all remaining 5!=120 whole K6-edge completions:
- EXACT cylinder min S=**68**, achieved by known complete g68; original-right-first and left-first seven-score oracles agree.
- Sourcewise exact all-completion floor **16**; source-coupled floor **29** (16 coupled buckets, original multiplicities 53,907 and D6 positional signatures retained). Therefore all coherent g extending these ten pins satisfy genuine **S(f0,g)>=29**.
- Exact joint min(P2+R) = `-530136/5005`; separated min P2 + min R = `-2541377/20020`; exact correlation gain `60119/2860` (>21). This is one PINNED cylinder only, not whole W32 `min_g` or all-h Branch A.
- Hosted [B8-H job evidence](https://github.com/definitely-stable/Mathlab/actions/runs/38151123546) is now SUCCESS; Research required separately.

**Created stacked Draft [PR #365 — C24-B8-I](https://github.com/definitely-stable/Mathlab/pull/365)**, pinned parent B8-H HEAD `68285a146e6987276e6938261926e4743fe0ffbe`, new initial B8-I HEAD `d6b822c4815cb523e7a4c320a2c4b28313d08bfa`. The new exact finite proof-tree checker independently validates complete physical-edge child partitions, valid original global injections, independently rescored original leaf values, source-accepted prune floors, and all budgets. Genuine W32 has (a) an unpruned 120-leaf exact tree with independent original-left scorer replay and original-right-first minimizer audit, and (b) a one-node root prune proving S>=29 using B8-H genuine source bound recomputed in the builder and replayer. Canonical JSON proof bundle + SHA-256 and hosted artifact. K4 all 360/720 assignments and deliberate forged branch/score/prune controls. No naive symmetry quotient or global 15! claims.

**Scope:** finite pinned right cylinder for one f0 at h=1, not universal min over f,g, not an all-h Omega(s^6) proof, no new R3/ASET exponent. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. B8-I exact-head CI queued/pending; no main changes/merges.

---

## Comment 080 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6111259528
- GitHub comment ID: 6111259528

### HYP-105 E1-K1/K2: Kikuchi-graph route to #230, now in draft [PR #366](https://github.com/definitely-stable/Mathlab/pull/366)

[PR #366](https://github.com/definitely-stable/Mathlab/pull/366) is the only PR I have opened for this issue. It is based on `main` (HEAD `0b21fd5`) and does not depend on the unmerged C1…C24-B8-I stack (#260…#365). It is a draft; exact-head CI is running and I have not claimed it passes.

**Status:** RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER. Neither Branch A nor Branch B is decided, and there is no ASET exponent.

#### Why a new route
Every earlier slice hit a proved ceiling of its own method: moments, pins, local search, pair projections. The structural reason is the following.

**D6 is a six-cycle count in an auxiliary graph sitting exactly at the C6 Turán/Moore threshold.** Ĝ has about 0.79·n^{4/3} edges, above every known C6-free bound: Füredi–Naor–Verstraëte (0.6272) and Das et al., arXiv:2609.10003 (0.6144).

**s=2 lies below that threshold, so W32 evidence (including D6=0 maps) cannot separate Branch A from Branch B.**

#### K1: exact all-h identities ([note](https://github.com/definitely-stable/Mathlab/blob/build/sleepy-fermat-sa6c39/docs/research/HYP-105-G5-E2-B3-E1K1-KIKUCHI-C6-SUPERSATURATION.md))
- **Kikuchi graph.** For each incidence (p,l) with f(p)={x,x'} and g(l)={y,y'}, the graph Ĝ on [a]×[a] gets the edges (x,y)–(x',y') and (x,y')–(x',y). Ĝ is simple and has exactly 2N edges.
- **K1.1.** The accepted **D6 equals the number of proper six-cycles of Ĝ**, and **Q4 equals the number of proper four-cycles**.
- **K2.** For every simple graph, `Σ_{u,v} P3(u,v)² = P3 + 12·C6 + Θ`, where Θ is an explicit coincidence mass (four-cycles with a pendant edge, diamonds, bowties) computable from codegrees.
- **K3.** `NB3 ≥ 2m(d̄−1)²` (the k=3 case of Alon–Hoory–Linial, proved directly), together with 2-core peeling. This gives `P3 ≥ 4N(4N/a²−1)² − 6·C3` and μ₀ → 4.
- **Theorem K.** `12·D6 ≥ L(P3) − Θ − 12·C6_imp`, where L(x)=x(x/a⁴−1). The leading term is about 4s⁶.

#### K2: finite all-h classification ([note](https://github.com/definitely-stable/Mathlab/blob/build/sleepy-fermat-sa6c39/docs/research/HYP-105-G5-E2-B3-E1K2-CYCLE-PATTERN-WEIGHTS.md))
- **Six-cycles.** The support pattern of a Kikuchi cycle is independent of s.
  - There are 41 cyclic walk patterns, giving 879 six-cycle patterns with six distinct columns.
  - All 879 have full 51-palette alternating 3v3 GF5 weight **≥ 5643**. Equality holds only for proper cycles (D6).
  - At most 4 cycles share one six-set.
  - 50 further patterns are degenerate (both diagonals of one column, C6_rep).
- **Four-cycles.** All 9 patterns have 2v2 weight **≥ 531**, with equality only for Q4. At most 2 cycles share one four-set, so `51⁴·R2 ≥ (531/2)·C4(Ĝ)`.
- **D2.** Exact identity: pairs of four-cycles sharing exactly one edge correspond one-to-one to six-cycles with an antipodal chord.
- **Theorem K′ (for full R3, not only S).** `51⁶·R3 ≥ (5643/4)·[(L(P3) − Θ)/12 − C6_rep]`. The improper-cycle term disappears. Measured C6_rep/s⁶ is 0.66, 0.02 and 0.002 at s = 2, 4, 8.

#### Exact finite evidence (all values recomputed by independent methods)
- **s=2.** D6=15/3 and Q4=50/32 match `seven_census`, and also agree on 12 further seeded bijections. Kikuchi six-sets alone give R3 numerators of 103,920,064 (lex) and 63,531,068 (reverse-line), versus the accepted seven-family floors of 11,225,795 and 7,627,209.
- **s=4.** D6 and Q4 match the independent left-C6 join (`exact_coincident_c6`) and the C4 join (`exact_coincident_c4`).
- **s=8.** These were local runs and are not pinned in CI. **Theorem K is non-vacuous here for the first time**:

| map | exact D6 | Theorem K floor |
|---|---:|---:|
| lex | 1,412,851 = 5.39·s⁶ | D6 ≥ 0.49·s⁶ |
| random | 1,237,605 = 4.72·s⁶ | D6 ≥ 1.90·s⁶ |

- **Tests.** K1 has 11 tests and K2 has 6, all passing locally. K1 checks against `seven_census`, the left-C6 join and definition-level Θ. K2 uses an independent 3+3 meet-in-the-middle GF5 count and brute-force four-cycles. Full `unittest discover` (1017 tests) passed before K2 was added.

#### Remaining formal blocker and current experiments
**Blocker.** Branch A for R3 needs only `Θ + 12·C6_rep ≤ (48−ε)s⁶`. A K+D2 dichotomy reduces this to regularity of the star-incidence matrix n(x,y): four-cycle mass must not concentrate on hubs or in books K_{2,t}. The candidate structure for Branch B is stars aligned with Baer subquadrangles W(3,√s).

**Exploratory, local, not CI-pinned:**
- **Maximising M2 = Σ n(x,y)²** finds no growth of M2/s⁵: 34.8 → 20.7 → 17.0 at s = 2, 4, 8.
- **Hubs help the bound.** On the M2-maximised map at s=8, Θ grows from 11 to 183·s⁶ but L grows from 73 to 435·s⁶, so the K′ floor *rises* from 5.1 to 21·s⁶. Regularisation, not concentration, is the adversarial direction.
- **Exact-D6 greedy adversaries.** At s=4 they plateau near 0.8·s⁶. At s=8 the run is ongoing (4.79 → 4.28·s⁶ after 275 moves).
- **Still running at s=4:** adversaries that minimise the K′ floor and the total C6. No numbers are claimed for these yet.

**Next:**
1. A rigorous regular-case lemma: C4 ≤ (1−ε)d⁵/16 gives Θ < L.
2. Book control via pencil-star packing.
3. A Baer-subquadrangle test at s=4.

#230, #176 and #169 stay open.

---
_Generated by [Claude Code](https://claude.ai/code)_

---

## Comment 081 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6111583240
- GitHub comment ID: 6111583240

### E1-K follow-up: PR #366 CI green; adversarial runs at s=4 and s=8 finished

**CI.** [PR #366](https://github.com/definitely-stable/Mathlab/pull/366) is green on exact head `0b21fd5`: all 7 checks SUCCESS, including `kikuchi-d6-contract`, every Research shard and the aggregator `research-full-suite`. The PR stays in draft.

**Exploratory local adversaries.** None of these runs are pinned in CI. They are finite evidence, not theorems.

Notation:
- **L** is the Cauchy–Schwarz main term L(P3)=P3(P3/a⁴−1);
- **Θ** is the coincidence mass;
- **floor K** is the lower bound on D6 from Theorem K;
- **floor K′** is (L−Θ)/12, the Theorem K′ lower bound on the number of distinct-column six-cycles.

| run | moves | result | Θ, L | floor |
|---|--:|---|---|---|
| s=4, minimise **floor K′ itself** | 22,407 | floor driven to −22.8·s⁶; actual C6 *rose* to **85.3·s⁶**, D6 to 44.4·s⁶ | Θ=430·s⁶, C4=4.2·s⁵ | negative (vacuous) |
| s=4, minimise **actual total C6** | 2,082 | C6: 7.4 → **4.54·s⁶** | Θ=13.3·s⁶, L=43·s⁶ | floor K′ **2.47·s⁶ > 0** |
| s=8, minimise **exact D6** (incremental) | 555 | D6: 4.79 → **4.05·s⁶** | Θ=9.7·s⁶ | floor K = **1.79·s⁶ > 0** |

At the end of the s=8 run, the reached map has C6=6.92·s⁶ and C4/s⁵=0.04. Its final value was cross-checked by a full recount.

**Reading.**
1. **Making floor K′ vacuous does not lower R3.** It forces C4-rich configurations, and those carry many *more* six-cycles. This is exactly the D2 mechanism: two four-cycles sharing one edge form a chorded six-cycle. So the Θ blocker is an artefact of the proof method, and the right closing argument is the K + D2 dichotomy (Θ-small branch, or C4-rich branch via D2).
2. **The real minimisers regularise the Kikuchi graph and keep Θ ≪ L.** On the maps they reached, the conditional floors stay positive: 54% tight for C6 at s=4, and floor K = 1.79·s⁶ against D6 = 4.05·s⁶ at s=8.
3. **Concentration is not a threat to the floor.** Maximising M2 = Σ n(x,y)² gives no growth of M2/s⁵ (34.8, 20.7, 17.0 at s = 2, 4, 8). On those maps floor K′ *rises*: 5.1 → 21·s⁶ at s=8.

**Next step: a rigorous dichotomy statement.** It needs two pieces:
- a regular-case lemma: Θ < L when C4 ≤ (1−ε)d̄⁵/16;
- book control, via codegree and pencil-star packing in W(3,s).

Together they would give R3 = Ω(s⁶) for all f,g. That would be Branch A for R3, which is stronger than the S-only statement. A Baer-subquadrangle labelling at s=4 remains the explicit Branch-B test case. #230, #176 and #169 stay open.

---
_Generated by [Claude Code](https://claude.ai/code)_

---

## Comment 082 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6112310206
- GitHub comment ID: 6112310206

### HYP-105 E1-K3-A/B — exact local 3-path collision certificate implemented (stacked Draft PR #367)

New [Draft PR #367](https://github.com/definitely-stable/Mathlab/pull/367), based on parent [#366](https://github.com/definitely-stable/Mathlab/pull/366) HEAD `0b21fd51187268e0ffbc3cb19335277103b4e80f`. No main changes or merge.

**RESTRICTED_THEOREM_C** (ALL finite simple graphs): for each ordered distinct endpoint pair (u,v), with path internal loads k_z and b_uv central edges supporting both path orientations,
`Theta_uv=sum_z k_z(k_z-1)-2*b_uv`; for ANY chosen nonempty endpoint set U,
`12*C6>=D_U>=M_U^2/|U|-M_U-Theta_U`.
Independent quadratic path-pair brute force checks the optimized identity; true W(3,2)/W(3,4) global-label tests verify K2 and 12*C6. Original GQ incidence-star degree/codegree contraction is implemented independently from graph adjacency.

**FORMAL NEGATIVE FALSIFIER:** K(2,t) has `P3=4t(t-1)`, `Theta=4t(t-1)(t-2)`, `C6=0`, and all active endpoint pairs have codegree ZERO. Thus filtering only endpoint-low-codegree pairs retains all collisions; that simple all-graph D2* shortcut is false. This does not falsify restricted W(3,s) Branch A.

**Exact hosted results** at PR HEAD `d51f3c575ef8d633c3d62cece0cd91d55009dd7f`: [dedicated K3 Contract SUCCESS](https://github.com/definitely-stable/Mathlab/actions/runs/38164251748), 6 independent test methods passed, deterministic report generated; INDEX SUCCESS. Full Research is still running at the time of this comment. W32 lex C6 integer lower: all pairs 202, active 296 (actual C6=730); s=4 random: all pairs 14,167, active 16,710 (actual C6=28,712). These are bounds on TOTAL C6, **not on D6**, and no all-h claim follows.

**Next formal blocker:** W(3,s)-specific D2* pencil-star/book packing and a finite-to-all-h bound with explicitly controlled repeated-column multiplicities; keep Branch A/B and full R3/ASET OPEN. Do not merge Draft #367 before exact-head full Research and independent review.

---

## Comment 083 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6112521263
- GitHub comment ID: 6112521263

### HYP-105 E1-K3-C — exact C4 book decomposition and original GQ pencil cap

Opened [stacked Draft PR #368](https://github.com/definitely-stable/Mathlab/pull/368) on accepted-tested #367 HEAD `d51f3c575ef8d633c3d62cece0cd91d55009dd7f`, current PR #368 HEAD `3b29892ca1f35d29b25a7a8213753ba9d6b6148b`. No main changes, no merge.

**RESTRICTED_THEOREM_C_ALL_GRAPHS:** For A=sum_e binom(c4(e),2), decompose pairs of four-cycles sharing an edge into H (one common edge, two vertices: antipodally chorded C6), B (two-edge-path book), T (triangle-hook), K (two opposite common edges, same K4). Exact identities: `A=H+2B+T+2K=H+6*sum_{u<v}binom(codeg(u,v),3)+T+6*(#K4)`. Also `H<=3*C6`; on genuine original globally coherent pair-labeled W(3,s), `H_proper<=3*D6`. All-h source-specific result: if two distinct Kikuchi vertices share first OR second physical coordinate, `codeg(u,v)<=a-2` (unique common original point of two lines / unique original common line of two points). No claim for mixed-coordinate pair codegrees.

**Independent exact hosted Contract:** [#38165886344](https://github.com/definitely-stable/Mathlab/actions/runs/38165886344) SUCCESS, 5 independent test methods PASS, including 4-cycle brute-force walk pair census, cubic codegree book formula, K4 and genuine original W(3,2)/W(3,4) factor-incidence contractions; INDEX SUCCESS. Full Research is still running at the time of this comment.

**Exact examples (same global map per row):** W32 lex `C4=69, H=299, B=99, T=29, K=3, H_proper=24, D6>=8, true D6=15`; W32 reverse `C4=49,H=130,B=24,T=16,K=6,H_proper=2,D6>=1,true D6=3`; genuine W(3,4) random `C4=629,H=3391,B=387,T=75,K=3,H_proper=894,D6>=298,true D6=6805`. At s4 3386/3391 H witnesses use distinct original columns but most are not proper, so a full R3 route is quantitatively different from the seven-family D6/S route.

**FORMAL BLOCKER unchanged:** cubic book moment of Kikuchi vertex pairs with BOTH physical coordinates distinct + T + repeated-column/proper losses. A packing theorem for arbitrary globally coherent f,g is required before a universal Omega(s^6) statement. Neither #230 Branch A nor B is decided, and no ASET exponent. Next K3-D: classify mixed-coordinate original incidence arrangements and investigate whether high books force admissible 6-column cycles or can concentrate without such cycles. #230/#176/#169 stay open.

---

## Comment 084 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6112648356
- GitHub comment ID: 6112648356

### HYP-105 E1-K3-D — mixed GQ girth-eight compatibility and Moore book bound implemented

Opened stacked [Draft PR #369](https://github.com/definitely-stable/Mathlab/pull/369) over pinned [#368](https://github.com/definitely-stable/Mathlab/pull/368) HEAD `3b29892ca1f35d29b25a7a8213753ba9d6b6148b`. Final K3-D HEAD `149f4c60e9110c77684ae55708678b5751ebbaba`. Previous #368 full exact-HEAD Research, Contract and INDEX are ALL SUCCESS. No main modifications or merges.

**RESTRICTED all-h theorem** valid for any legal globally coherent f,g on W(3,s), s=2^h: for every mixed Kikuchi vertex pair u=(x,y),v=(x',y') with x!=x',y!=y', let H_uv have left z not x,x', right t not y,y', edge zt iff BOTH ORIGINAL incidences I(F_xz,G_yt)=I(F_x'z,G_y't)=1. Then m_uv=|E(H_uv)|=codeg_Ghat(u,v), and H_uv embeds in ORIGINAL GQ incidence (girth>=8, degree<=s+1). With r=a-2:

- C4-free: `m(m-r)<=r^2(r-1)`; degree constraint `m<=r(s+1)`.
- Girth-eight 3-path injection: `sum_edges(deg(z)-1)(deg(t)-1)<=r^2-m`.
- Stronger all-h **Moore bound** in the m>=3r regime (K1 AHL and 2-core peeling): `m*((m-r)^2+r^2)<=r^4`; in m<3r use `m<=3r-1`. Combined integer capacity uses isqrt and binary search with NO unjustified small-average extension.
- Global exact `M1_mixed+M1_aligned=sum_w binom(original GQ star degree(w),2)`, and certified though generally **very weak** `Bmixed<=M1_mixed*(Cmax-1)*(Cmax-2)/2`.

**Independent exact GitHub-hosted evidence** at FINAL #369 HEAD: dedicated [Contract #38166808457](https://github.com/definitely-stable/Mathlab/actions/runs/38166808457) SUCCESS, 6 independent tests PASS, INDEX SUCCESS; inherited Research still RUNNING at time of writing. Exhaustive W32 mixed pair source reconstruction and C4/C6 freedom; true W(3,4) all 96 book-bearing mixed pairs crosschecked against independent slow original GQ oracle; unit budgets fail closed.

**True-label numeric evidence:** W32 lex Bmixed=90, aligned=9; W32 reverse Bmixed=21, aligned=3; W(3,4) random Bmixed=333, aligned=54. At s4 actual mixed codeg max=4, C4-only cap=46, Moore cap=35, universal book upper=3,500,640 versus actual Bmixed=333. This large gap demonstrates **failure to close global book packing**, NOT a proof of Branch A/B. Existing #230 remains OPEN_WITH_FORMAL_BLOCKER; no all-h S or full R3 exponent, no ASET claim.

**Next K3-E:** exploit SHARED original sources across mixed pairs to control their joint third factorial moment or construct a bounded-multiplicity injection from books to distinct-original-sixset cycles; account separately for T/K4 and improper/repeated columns. Keep #230/#176/#169 open and PRs Draft pending review.

---

## Comment 085 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6112680182
- GitHub comment ID: 6112680182

### HYP-105 E1-K3-D FINAL strengthened certificate — PR #369

Updated stacked [Draft PR #369](https://github.com/definitely-stable/Mathlab/pull/369) on #368. **Current exact HEAD:** `69eb52a445f12a6c40fc278afbbf97d14631cb1e`; only research branch changed, `main` untouched.

**All-h restricted GQ result:** for every legal globally coherent original f,g and mixed vertex pair u,v, the compatibility graph H_uv determined by the product of two ORIGINAL W(3,s) incidence indicators embeds in the original GQ incidence graph, so has girth>=8 and degree<=s+1. Its edge count is exactly Kikuchi codeg(u,v). For r=a-2,m=codeg, C4-free: `m(m-r)<=r^2(r-1)`; for m>=3r the K1 AHL/2-core path bound + unique C6-free three-path endpoints gives `m*((m-r)^2+r^2)<=r^4`; for m<3r use m<=3r-1. A fail-closed exact integer cap Cmax combines these with degree capacity.

**New stronger ALL-h aggregate bridge** from the exact identities `3*binom(c,3)=(c-2)*binom(c,2)`, `M2_all=sum_{u<v}binom(codeg(u,v),2)=2*C4(Kikuchi)`: `Bmixed<=max(Cmax-2,0)*M2mixed<=2*max(Cmax-2,0)*C4`. K3-D independently recounts every C4 as an edge set and separately verifies source-star M1. This is MUCH sharper than the earlier first-moment upper, but not known to be o(s^6) and not a Branch A/B theorem.

**Exact GitHub-hosted final-HEAD evidence:** dedicated [Contract #38167011765](https://github.com/definitely-stable/Mathlab/actions/runs/38167011765) SUCCESS (6 independent tests), INDEX SUCCESS; inherited Research IN PROGRESS at time of this issue update. Source-original, brute original pair-label scan and Kikuchi common-neighbor oracles agree for EVERY W32 mixed pair and ALL 96 true W(3,4) book-bearing mixed pairs; girth C4/C6 absence and unique three-path endpoint checks PASS.

**Observed (genuine full global f,g) Bmixed: W32 lex 90, reverse 21, W(3,4) random 333.** Previous first-moment upper 8,596 / 8,400 / 3,500,640. New second-moment upper **833 / 567 / 35,805**; for s=4 M2mixed=1085, Cmax=35 (C4 cap alone=46), giving bound 33*1085=35,805, still ~108x actual. No finite asymptotic fit or all-h Omega(s^6) proof.

**Next formal blocker K3-E:** a collective original-source coupling/packing inequality reducing mixed M2 or effective c on C4-heavy mixed pairs, or a positive-motif injection from high book mass with bounded multiplicity. Must separately control triangle hooks, K4, improper/repeated six columns and distinguish seven-family S from complete R3. Root #230 stays OPEN_WITH_FORMAL_BLOCKER, #176/#169 open; no ASET exponent, no merges.

---

## Comment 086 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6116319014
- GitHub comment ID: 6116319014

### HYP-105 E1-K3-E — C4-weighted mixed-codegree regularity and physical star-tail certificate implemented

Opened [stacked Draft PR #370](https://github.com/definitely-stable/Mathlab/pull/370) atop [#369](https://github.com/definitely-stable/Mathlab/pull/369) exact parent HEAD `69eb52a445f12a6c40fc278afbbf97d14631cb1e`. New HEAD `841e6fb5b6d59748b8a77ff2232b45169c4fce8f`. Parent #369 final Contract/Research/INDEX ALL SUCCESS. No main modification and no merge.

**All-h exact but conditional source-shape identity.** For mixed unordered GQ Kikuchi vertex pairs, w_uv=binom(codeg(u,v),2), M2mix=sum_mixed w_uv and Bmix=3 sum_mixed binom(codeg,3). Then `Bmix=sum_mixed (codeg-2)*w_uv`. If M2mix>0, C4-weighted kappa=2+Bmix/M2mix; if M2mix=0, kappa is undefined and Bmix=0. For k>=3, Q_k=sum_mixed w_uv*[codeg>=k], **Bmix=sum_{k=3}^{Cmax}Q_k**.

**New rigorous original-star upper:** reconstruct d_u,d_v independently from ORIGINAL W(3,s) source incidence star tensor for ONE whole coherent global pair f,g; let cap_uv=min(Cmax,d_u,d_v), where Cmax is K3-D's all-h C4/C6-free Moore cap. Then `Bmix <= Ustar=sum_mixed max(cap_uv-2,0)*w_uv <= (Cmax-2)*M2mix`. Equivalently each C4-weighted codegree layer is bounded by a source-degree layer. This does NOT prove any uniform o(s^6) bound; Ustar still depends on w_uv of the unknown map.

**Hosted exact HEAD evidence**: [K3-E Contract #38193272885](https://github.com/definitely-stable/Mathlab/actions/runs/38193272885) SUCCESS, **5 independent tests PASS**. INDEX SUCCESS; inherited Full Research in progress at time of this comment. Dedicated tests independently enumerate C4 edge sets via oriented closed walks, reconstruct opposite-vertex C4 weighted diagonal histograms, enumerate triples of common neighbors, check SOURCE degrees, exact layer-cake and star-tail sums on genuine globally labeled W(3,2) and W(3,4). Fail closed on budgets.

**Numerical genuine maps:** W32 lex Bmix 90, K3-D bound 833, new Ustar 435; W32 reverse Bmix 21, old 567, new 243; W(3,4) lex Bmix 891, old 47,652, new 10,162; W(3,4) random seed 20261011 Bmix 333, old 35,805, new 7,548; W(3,4) random seed 230 Bmix 555, old 41,679, new 8,666. Exact kappa for seed 20261011 = 2503/1085 (~2.307). Source-star certificates are stronger but still loose, so no Branch A/B or full R3/ASET exponent is claimed.

**Next proof gate K3-F:** establish SHARED ORIGINAL W(3,s) weighted star-tail packing across ALL global f,g, or show large tails force a bounded-multiplicity accepted proper D6/seven-motif family. Triangle hooks, K4, repeated-column and improper-six-cycle losses must be charged separately; complete GF5 R3 and original seven-motif S remain different conclusions. #230/#176/#169 stay OPEN_WITH_FORMAL_BLOCKER.

---

## Comment 087 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6116574517
- GitHub comment ID: 6116574517

### HYP-105 E1-K3-F1 — all-h shared original-source spectral transport, numeric transfer NO-GO

Opened [stacked Draft PR #371](https://github.com/definitely-stable/Mathlab/pull/371) over [#370](https://github.com/definitely-stable/Mathlab/pull/370) pinned HEAD `841e6fb5b6d59748b8a77ff2232b45169c4fce8f`. New PR head `8d3eae4c1529f37d66b8e8aec8762bdcdd561139`. Parent #370 Contract, INDEX and FULL Research verified SUCCESS. No main changes, no merges.

**New rigorous all-h SHARED-SOURCE result:** let M be the VxV ORIGINAL W(3,s) point-line incidence, and P,L the physical pair endpoint matrices of ONE whole global injective f,g. D=P M L^T is the entire Kikuchi degree matrix; alpha=P1, beta=L1. Exact physical-star transport: `sum_y D_xy=2(s+1)alpha_x`, `sum_x D_xy=2(s+1)beta_y`, `sum D=4(s+1)V`. The W(3,s) original point-collinearity graph is strongly regular with parameters (V,s(s+1),s-1,s+1), so M's nontrivial singular value is sqrt(2s). Thus `sum_xy (V D_xy-(s+1)alpha_x beta_y)^2 <= 8s V^3 min(alpha_max,beta_max)`. Pointwise mixing bounds are also checked with exact integers.

For any threshold k, the number H_k of high-degree physical stars is bounded simultaneously by original row/column marginals, total degree and a spectral Chebyshev bound when k exceeds max(source mean). Consequently the K3-E mixed C4-weighted source-star tail obeys `Qstar_k<=binom(Cmax,2)*binom(Hupper_k,2)` and an all-h joint tail/book upper follows.

**Evidence and CRITICAL NEGATIVE result:** [dedicated exact-head K3-F Contract #38195156076](https://github.com/definitely-stable/Mathlab/actions/runs/38195156076) SUCCESS, 4 independent tests PASS, INDEX SUCCESS. Full Research #38195156089 IN PROGRESS at posting. Tests independently build original source point-collinearity SRG (W32/W34), source incidence degree tensor P*M*L^T, exact physical marginals and C4-weighted mixed hub tails. The joint star-count-to-C4-weight transfer is WEAKER than K3-E on every pinned model: W32 lex actual Bmix=90, old source upper=435, new joint upper=833; reverse actual 21, old 243, new 567; W(3,4) lex actual 891, old 10,162, new 47,652; W(3,4) random seed 20261011 actual 333, old 7,548, new 35,805. The all-h GQ spectral theorem remains valid, but numeric NO-GO for this coarse extraction must be preserved.

**Formal blocker remains:** Source-star concentration alone does not determine which physical high stars are paired in SAME mixed C4 diagonal witnesses. Next K3-F2 must control the *weighted C4 diagonal operator* jointly with original GQ incidence (or prove a bounded-multiplicity injection from book-heavy witnesses to six-distinct-original-column proper D6/seven-family S motifs). No claim of Omega(s^6), full R3 exponent or ASET exponent. Keep issue #230/#176/#169 open, stacked PRs Draft pending independent review.

---

## Comment 088 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6116740754
- GitHub comment ID: 6116740754

### HYP-105 E1-K3-F2 — exact weighted C4 diagonal operator / proper-vs-improper chord ledger

Implemented [stacked Draft PR #372](https://github.com/definitely-stable/Mathlab/pull/372) over validated [PR #371](https://github.com/definitely-stable/Mathlab/pull/371) exact HEAD `8d3eae4c1529f37d66b8e8aec8762bdcdd561139`. PR #372 HEAD `4129b88d7232060b55c8fc3a45050f23976d545e`. No main modifications or merge.

**PROVED exact all-graph mixed diagonal operator:** `W_uv=binom(codeg(u,v),2)` for MIXED coordinate pairs and zero elsewhere; `Q(H)=1/2 h^T W h`, `2 Q(H)+Cut_W(H,H^c)=sum_{u in H}rho_u`. Integer upper bounds from high-vertex row strength, `isqrt(binomial(|H|,2) sum_{u<v}W_uv^2)`, maximum per-pair weight and M2mixed. Independent oriented-C4-walk diagonal oracle and neighbor-pair-wedge row oracle check exactness.

**Exact chorded motif extraction:** every pair of C4s sharing just one edge and exactly two vertices produces a C6 whose opposite chord has multiplicity <=3. In ONE fixed original global point/line labeling, partition `H=Hproper + Himproper_distinct + Hrepeated_original_incidence`. Then `D6>=ceil(Hproper/3)`, and the six-DISTINCT-ORIGINAL-column C6 count is at least `ceil((Hproper+Himproper_distinct)/3)`. These are conditional on the actual Kikuchi graph, not universal asymptotic lower bounds; improper distinct-column H does NOT imply seven-family S membership. An independent quadratic C4 pair oracle checks all three categories against K3-C and accepted K1 D6.

**Verified exact GitHub-hosted evidence:** [K3-F2 Contract #38196383571](https://github.com/definitely-stable/Mathlab/actions/runs/38196383571) SUCCESS (5 independent tests), INDEX SUCCESS, inherited full Research IN PROGRESS at posting.

**Operator bounds (actual Bmixed / K3-F1 coarse / K3-F2 / K3-E exact-star):** W32 lex `90/833/526/435`; W32 reverse `21/567/297/243`; W(3,4) lex `891/47652/12776/10162`; W(3,4) random seed 20261011 `333/35805/8862/7548`. Thus K3-F2 improves the crude F1 spectral transfer but DOES NOT improve exact K3-E. Explicitly preserve this negative result.

**C4-to-chord counts:** W32 lex `H=299; Hproper=24; Himproper_distinct=271; Hrepeated=4; unique chorded proper D6=12`. W(3,4) seeded random `H=3391; Hproper=894; Himproper_distinct=2492; Hrepeated=5; unique chorded proper D6=842; unique chorded improper distinct C6=2438`. Multiplicity-only D6 floors are 8 and 298; these are finite-census results, not all-h floors.

**Root blocker not resolved:** no SHARED-SOURCE all-h bound for the actual weighted C4 diagonal row energies/cuts, no theorem converting arbitrary book B mass into accepted proper D6 or any of other six S families with bounded multiplicity, and T/K4/repeated-column losses are not uniformly controlled. Branch A/B, full R3/ASET exponent remain OPEN. Next K3-G: original GQ-incidence coupling of W row/energy concentration OR original-motif geometric injection. Keep #230/#176/#169 open, PRs Draft until final exact-HEAD Research plus independent review.

---

## Comment 089 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6116956483
- GitHub comment ID: 6116956483

## HYP-105 E1-K3-G1 — all-h antipodal repeated-source-column ledger and aligned codegree packing

Implemented in [stacked Draft PR #373](https://github.com/definitely-stable/Mathlab/pull/373) over accepted CI-green [PR #372](https://github.com/definitely-stable/Mathlab/pull/372) pinned HEAD `4129b88d7232060b55c8fc3a45050f23976d545e`. **Final current PR #373 HEAD** `53df42a07ae0ffbe0e168b68e2711122d5526f97`. No main change or merge; #230/#176/#169 remain OPEN.

**RESTRICTED_THEOREM_C (all h; all globally coherent injective f,g).**

1. A simple Kikuchi C6 using both diagonals of one original incidence rectangle has those edges antipodal. Summing the TWO aligned-corner codegree-product path matchings (with shared-internal-vertex subtractions) over original columns yields an EXACT incidence count `J`. Exhaustive 41x41 canonical coordinate-pattern classification shows only 0, 1 or 3 repeated columns (879/48/2 valid canonical pattern pairs, respectively; zero with 2). Therefore `J=C6_rep1+3*C6_rep3` and `C6_rep=J-2*C6_rep3`.
2. Triple-repeat sixcycles biject with physical-edge triangles in either source point pencil or dual source line pencil: `C6_rep3=sum_p triangle(G_p)+sum_l triangle(F_l)`. Each pencil has exactly s+1 edges, so spectral trace gives `C6_rep3 <= 2V floor(sqrt((2(s+1))^3)/6)=O(s^(9/2))=o(s^6)`, **uniform for ALL legal labelings**.
3. For any aligned pair of distinct physical line coordinates y,y', `sum_x codeg((x,y),(x,y')) <=2(a-2)`; each third physical t corresponds to two DISTINCT source lines, intersecting in at most one source point, whose physical label has exactly two endpoints. The point-line dual also holds. Summing products only over each original GQ pencil then gives the NEW UNIVERSAL `0<=J<=refined_marginal_bound<=4V(a-2)^2=O(s^6)`. This improves the naive O(s^7) from individually bounding aligned codegrees, but does **not** give o(s^6) or a small enough leading constant for the required obstruction.

**Evidence:** [exact-HEAD K3-G1 hosted Contract #38197928932](https://github.com/definitely-stable/Mathlab/actions/runs/38197928932) SUCCESS (5 independent tests: 41x41 patterns, full actual simple-C6 source-column oracle W32/W34, independently reconstituted source-pencil triangles, independent ORIGINAL line-line/point-point incidence reconstruction of aligned marginals, fail-closed budgets); INDEX [#38197928916](https://github.com/definitely-stable/Mathlab/actions/runs/38197928916) SUCCESS. Full Research [#38197928942](https://github.com/definitely-stable/Mathlab/actions/runs/38197928942) is RUNNING at reporting time.

**Exact remaining blocker:** the SINGLE repeat C6 loss `C6_rep1=J-3*C6_rep3` can still be Theta(s^6) under the proved estimate. Next K3-G2 must either prove an all-h incidence-coupled o(s^6) bound for J/rep1, or show the repeat loss is quantitatively offset by a simultaneous C6 lower bound. Neither is by itself a proof of seven-family S: improper distinct-original-column sixcycles contribute only to full GF5 R3 route unless the accepted seven-family membership is independently established.

Status unchanged: **OPEN_WITH_FORMAL_BLOCKER**, no Branch A/B, no full R3/ASET exponent, and no Draft merge without final exact-head CI and independent mathematical review.

---

## Comment 090 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6117078831
- GitHub comment ID: 6117078831

### HYP-105 E1-K3-G2-A — new all-h LOCAL repeated-column saving O(s^5)

[Stacked Draft PR #374](https://github.com/definitely-stable/Mathlab/pull/374) on accepted GitHub-hosted green [#373](https://github.com/definitely-stable/Mathlab/pull/373), pinned parent `53df42a07ae0ffbe0e168b68e2711122d5526f97`. Exact implementation HEAD `bd6d122bcf45bf8cb15cfce786da4d894c10c0d6`. `main` unchanged; no merge.

**New exact all-h source-coincidence theorem:** For one legal globally coherent W(3,s) physical pair labeling, the antipodal repeated-column incidence mass from K3-G1 has a canonical split `J=J_same+J_cross`, based on whether the two length-2 paths originate from the SAME original GQ point/line versus DISTINCT original source points/lines. If the origins coincide, global injectivity forces that origin to be the anchor original point p (or dual line l). The two physical middle vertices can never coincide, by uniqueness of original line/point intersections. Let `tau_e(H)` count triangles containing physical edge e in H, and `G_p/F_l` the s+1-edge physical original point/line pencils. Then exactly:

```
J_same = sum_(p,l incident) [tau_{g(l)}(G_p)^2 + tau_{f(p)}(F_l)^2];
C6_rep1_local = J_same - 3*C6_rep3
              = sum_(p,l incident)[tau_g*(tau_g-1)+tau_f*(tau_f-1)];
C6_rep1_cross = J_cross;
C6_repeated = J_cross + C6_rep1_local + C6_rep3.
```

**NEW UNIVERSAL ALL-h SAVING:** For every simple m-edge graph H, `sum_edges tau_e^2 <= sum_edges d_u*d_v <= (sum d)^2/2 =2m²`. There are 2V original pencils, m=s+1 each, therefore

```
J_same <= 4V(s+1)^2 = O(s^5) = o(s^6);
C6_repeated = J_cross + O(s^5),   J_cross>=0.
```

This isolates the **entire potentially critical Theta(s^6) repeated-source loss** into path-pairs whose ORIGINAL GQ source points/lines are different. It is stronger than K3-G1's sole `J=O(s^6)` and does not assume randomness, automorphism invariance, or finite-h fitting.

**Derived K2 complete-R3 conditional consequence (NOT seven-family S):**
```
51^6 R3 >= (5643/4)*[(L(P3)-Theta)/12 - C6_repeated]
        >= (5643/4)*[(L(P3)-Theta)/12 - J_cross - 4V(s+1)^2].
```
The unresolved sign is now the joint original-source quantity `(L(P3)-Theta)/12-J_cross`, up to an explicit o(s^6) error. Independent bounds on C6 and J_cross do NOT automatically establish the seven accepted six-motif S obstruction.

**Hosted evidence:** [K3-G2-A dedicated Contract #38198859627](https://github.com/definitely-stable/Mathlab/actions/runs/38198859627) SUCCESS (4 independent test methods: brute source provenance of both paths over true W32/W34 global labels, independent exhaustive physical triangles at pencil edges, exact G1 total reconciliation, fail-closed budgets); INDEX [#38198859535](https://github.com/definitely-stable/Mathlab/actions/runs/38198859535) SUCCESS; inherited Full Research [#38198859598](https://github.com/definitely-stable/Mathlab/actions/runs/38198859598) IN PROGRESS at posting.

**Next K3-G2-B** must control J_cross by a joint-original-incidence pair tensor or establish a simultaneous surplus `(L(P3)-Theta)/12 - J_cross >= c s^6` (with explicit constants, all h). This would address *full R3 only*. Separate proof of accepted proper D6 / six other seven-family S contributions is still required for Branch A. #230/#176/#169 remain OPEN; no exponent, no merging Drafts.

---

## Comment 091 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6117275152
- GitHub comment ID: 6117275152

### HYP-105 E1-K3-G2-B — exact original GQ cross-source pair kernel; global physical-wedge packing

Opened stacked [Draft PR #375](https://github.com/definitely-stable/Mathlab/pull/375) over [PR #374](https://github.com/definitely-stable/Mathlab/pull/374) pinned exact parent HEAD `bd6d122bcf45bf8cb15cfce786da4d894c10c0d6`, after parent Contract/INDEX/FULL Research all SUCCESS. Current PR #375 exact HEAD `ee20998932ed4e8cfd07206b97c2899289ac3575`. Only research branch changed. No merge, no `main` modification.

**Restricted exact all-h theorem:** For all s=2^h and ALL legal coherent original global injective f,g, let `T^g[q,l]` count third physical coordinates t whose two globally labelled original lines `{y,t}`, `{y',t}` meet at the original point q, where g(l)={y,y'}. Let `P` be the globally induced endpoint matrix of f and `A_l` the physical edge adjacency of its original line-pencil. Then for different original point origins q,r, `K_l(q,r)=(P^T A_l P)[q,r]` is an integer 0..min(4,s+1). The horizontal **exact** critical repeated-sixcycle mass is

```text
J_cross,h = sum_l sum_{q<r} T^g[q,l]*T^g[r,l]*K_l(q,r).
```

The point-line dual gives `J_cross,v`; `J_cross=J_cross,h+J_cross,v`. The off-diagonal source pair kernel is precisely partitioned into: BOTH on anchor, ONE on anchor, BOTH off anchor and collinear, BOTH off anchor and noncollinear (dually, meeting original lines vs nonmeeting). The exact diagonal contraction recovers K3-G2-A's `J_same`. These are full original-source counts, not independent physical relabelings.

**New global all-h wedge packing (strict, but only first moment):** Physical source wedges of distinct original lines/points have AT MOST ONE ORIGINAL intersection, by GQ partial linearity. Thus with `d_g(t)` the global physical degree from all V g-label edges,

```text
C_g := sum_{q,l} T^g[q,l]
    <= W_g := sum_q sum_t choose(deg_{G_q}(t),2)
    <= sum_t choose(d_g(t),2)
    <= a*choose(a-1,2) = O(s^(9/2)),
```

and dually for f. This improves the naive independent-source-pencil `O(V*s^2)=O(s^5)` cap **on global wedge first-moment only**; the cross-source pair correlation `J_cross` may still be Θ(s^6). A conditional one-map source-pair collision cap is `J_cross<=min(4,s+1)*(sum_l sum_{q<r}T^g[q,l]T^g[r,l]+dual)`. We explicitly do **not** claim Branch A/B or a full R3/seven-family S exponent.

**Exact GitHub-hosted HEAD evidence:** [dedicated K3-G2-B Contract #38200252966](https://github.com/definitely-stable/Mathlab/actions/runs/38200252966) SUCCESS, 4 independent test methods: source-pencil closure enumeration vs reverse physical third-coordinate GQ line intersections, physical-anchor-edge scan vs reference pair kernel on real W32/W34 labels, independent original-source wedge/host-wedge census, and fail-closed budgets. [INDEX #38200253078](https://github.com/definitely-stable/Mathlab/actions/runs/38200253078) SUCCESS. [FULL Research #38200253012](https://github.com/definitely-stable/Mathlab/actions/runs/38200253012) in progress at this report.

**Next proof gate K3-G2-C:** Show uniform power saving or a quantitatively coupled C6-vs-Jcross surplus in one or more geometric pair classes, with explicit all-h constants and exact original GQ source incidence. As a separate scientific route, prove that high improper C6 mass charges accepted seven-family S motifs; full R3 lower bound alone is insufficient to close the original Branch A. Keep #230/#176/#169 OPEN, all stacked PRs Draft pending independent review, no merge.

---

## Comment 092 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6117852161
- GitHub comment ID: 6117852161

### HYP-105 E1-K3-G2-C — exact GQ projection fibers / seven-bin original source cross-kernel

Created [stacked Draft PR #376](https://github.com/definitely-stable/Mathlab/pull/376) on pinned green parent [#375](https://github.com/definitely-stable/Mathlab/pull/375) HEAD `ee20998932ed4e8cfd07206b97c2899289ac3575`. Exact PR #376 HEAD `7adc87e63938abe529d30cb90f802f0e4cb70905`. `main` unchanged; no merge. #230/#176/#169 remain OPEN.

**Restricted exact all-h GQ incidence theorem:** For every original anchor line ell and any original point q not on ell, GQ uniqueness gives one original foot `pi_ell(q)`. For each of s+1 anchor points, its full projection fiber contains exactly `s²+1` original points. Dual original lines/anchor point works. Each unordered pair q<r belongs to exactly one of seven classes with exact counts per anchor:
```
both_on_anchor                      = (s+1)s/2
one_on_projected                    = (s+1)s²
one_on_other                        = (s+1)s³
off_samefoot_collinear              = (s+1)s²(s-1)/2
off_samefoot_noncollinear           = (s+1)s²(s²-s)/2
off_differentfoot_collinear         = (s+1)s⁴/2
off_differentfoot_noncollinear      = (s+1)(s-1)s⁴/2
sum = binom(V,2).
```
Off-differentfoot-collinear pairs correspond precisely to pairs of points on the s³ original lines disjoint from the anchor line (and the dual). All quantifiers hold for every s=2^h regardless of how original source vertices were physically pair-labelled.

**New EXACT seven-bin critical-mass ledger:** `J_cross = sum_C(J_C^h+J_C^v)`, where `J_C^h=sum_ell sum_{q<r in original GQ class C} T^g[q,ell] T^g[r,ell] K^f_ell(q,r)`. Each weighted class is computed for ONE coherent global f,g. The seven categories refine G2-B's four original geometry categories; sum matches G2-A's J_cross and diagonal J_same. For projected fiber totals `A_t=sum_{pi_ell(q)=t}T[q,ell]`, the source-pair unweighted-product accounting satisfies the exact identities `SameFoot=(sum_t A_t²-sum_q T_q²)/2` and `DifferentFoot=((sum_q T_q)²-sum_t A_t²)/2`. No independence assumption.

**Hosted exact-HEAD evidence:** [K3-G2-C dedicated Contract #38204524407](https://github.com/definitely-stable/Mathlab/actions/runs/38204524407) SUCCESS, including independent original-incidence-path projection oracle, ALL original source-pair class counts on genuine W32/W34 (and dual), independent physical-third-coordinate T and anchor physical-edge K, exact double-moment conservation, fail-closed budgets. [INDEX #38204524327](https://github.com/definitely-stable/Mathlab/actions/runs/38204524327) SUCCESS; [full Research #38204524324](https://github.com/definitely-stable/Mathlab/actions/runs/38204524324) IN PROGRESS at writing.

**Finite diagnostic, not a theorem about all labels:** Exact `J_cross / off_differentfoot_noncollinear contribution`: W32 lex `36/18`, W32 reverse `28/6`, W(3,4) lex `128/87`, W(3,4) random seed 20261011 `80/49`. Thus one physically/geomtery permitted class dominates three tested labelings, but no all-h asymptotic inference follows.

**Next K3-G2-D proof gate:** seek source-foot-resolved positive accepted proper-D6/seven-family S charging from heavy off-differentfoot source pairs with bounded multiplicity, OR jointly bound `(L(P3)-Theta)/12-J_cross >= c s^6` for full-R3 (not by itself seven-family S). No `J_cross=o(s^6)`, no Branch A/B, no ASET exponent. Draft pending full Research + independent mathematical review; no merges.

---

## Comment 093 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6117968590
- GitHub comment ID: 6117968590

### HYP-105 E1-K3-G2-D — finite Hall NO-GO to SAME-original-anchor proper-D6 charging

Implemented [stacked Draft PR #377](https://github.com/definitely-stable/Mathlab/pull/377) on validated [#376](https://github.com/definitely-stable/Mathlab/pull/376), pinned parent `7adc87e63938abe529d30cb90f802f0e4cb70905`. **Final revised HEAD** `86dcc5e137230cb9f1843f3526f82ba3dea81d00`. Parent #376 full Contract/INDEX/Research SUCCESS; main unchanged, no merge.

**Concrete mathematical proof-strategy NO-GO:** Every proper D6 is a six-original-column accepted positive motif, whereas each Jcross original-source pair witness is an improper six-cycle with exactly ONE repeated original incidence column. For the exact W(3,2) legal coherent labelings: `lex: Jcross=36, D6=15, heavy off_differentfoot_noncollinear=18`; `reverse-line: Jcross=28, D6=3, heavy=6`. Therefore even completely unrestricted one-to-one assignment to proper D6 is impossible in the s=2 cases, with necessary target multiplicities at least ceil(36/15)=3 and ceil(28/3)=10. Heavy class alone needs multiplicity >=2 in both. This refutes a universal *unit-capacity direct charging proof strategy*, NOT original seven-family S.

**Stronger exact Hall/cut NO-GO at all finite capacities for a SPECIFIC locality rule:** Connect each individual Jcross witness anchored at ORIGINAL (p,l) to exactly those proper D6 that use that same ORIGINAL incidence column. All candidates are enumerated via the one coherent global physical f,g maps, and all proper cycles are verified to use six distinct original columns. Exact capacity-one maximum matching is `lex=13/36` with **9 totally isolated witnesses** and heavy class **5/18 isolated**; `reverse-line=3/28` with **20 isolated** and **all six heavy class witnesses isolated**. A third globally legal random W32 labeling (seed 20261012) gives `Jcross=17, D6=1, 14 isolated; heavy 5, of which 4 isolated`. An isolated witness makes **every** finite-capacity local assignment impossible, not just capacity 1. Integer maxflow=mincut and the finite Hall `|X|<=k|N(X)|` criterion are independently tested against brute exhaustive small bipartite assignments, with residual mincut verified and fail-closed work budgets.

**Hosted exact-head results:** Revised HEAD [Contract #38205425294](https://github.com/definitely-stable/Mathlab/actions/runs/38205425294) SUCCESS, [INDEX #38205425384](https://github.com/definitely-stable/Mathlab/actions/runs/38205425384) SUCCESS, [full Research #38205425408](https://github.com/definitely-stable/Mathlab/actions/runs/38205425408) IN PROGRESS at reporting. Both precise orphan counts for lex/reverse are now pinned by dedicated tests.

**Next proof gate K3-G2-E:** Stop trying to inject repeated-source witnesses into proper D6 while sharing their original repeated anchor column: this relation is FALSIFIED. Either find a locality relation allowing alternative original columns and prove all-h bounded multiplicity to accepted proper D6, or expand targets to the other six actually accepted GF5 six-column motif families, with exact positive palette witnesses and finite Hall gate. No `S_s=Omega(s^6)`, no `Jcross=o(s^6)`, no full R3 exponent or ASET exponent. Issue #230/#176/#169 remain open and all PRs Draft, no merge.

---

## Comment 094 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6118324553
- GitHub comment ID: 6118324553

### HYP-105 E1-K3-G2-E — real seven-family GF5 Hall charging, concrete injective W32 witnesses

Implemented [stacked Draft PR #378](https://github.com/definitely-stable/Mathlab/pull/378) based on fully hosted-green [PR #377](https://github.com/definitely-stable/Mathlab/pull/377), exact parent `86dcc5e137230cb9f1843f3526f82ba3dea81d00`. **Final revised PR #378 HEAD** `ef846731908b219320919b9a486519c442c4eba0`. Main unchanged, no merge. Root #230 OPEN.

**Substantive new finite result:** For complete legal W(3,2)/K6 pair bijections, ALL seven genuinely accepted six ORIGINAL incidence families (D6, B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap, B/B-disjoint), each having a rigorously certified strictly-positive GF5 51-palette risk floor, can provide enough targets to cover ALL individual K3-G2-C original cross-source repeated C6 witnesses under precise local Hall rules. Every Jcross witness's actual six physical edges are independently traced to FIVE distinct ORIGINAL source columns (one repeated twice). Accepted target six-column supports are obtained from the previously verified exhaustive B0 enumerator, not approximated. Direct exact signed GF5 flow oracles verify representatives of EACH of seven true target families.

**Exact bipartite matching with unit target capacity k=1, finite W32 cases:**
```
labeling                    lex    reverse-line   random(seed=20261012)
accepted S_seven targets    259    169            144
Jcross source witnesses      36     28             17
same-anchor matches          36     28             17
>=2 common-source matches    36     28             17
anchor AND >=2 matches       36     25             12
>=3 common-source matches    19      9              4
>=4 common-source matches     0      0              0
```
The full heavy off-differentfoot-noncollinear source class also has capacity-one matches under both `same_anchor` and `overlap_ge_2` in these three W32 maps (18,6,5). Thus K3-G2-D's strong same-anchor NO-GO was specifically for proper-D6-only targets; it CANNOT be generalized to all accepted S targets. Conversely the stricter `anchor AND >=2` rule has 3 isolated witnesses for reverse-line and 5 for random, and overlap>=4 has no candidates in all three examples. **This motivates `|S(w)∩D|>=2` WITHOUT anchor obligation as the candidate all-h proof relation**, not yet an all-h theorem.

**Constructive certificates and checks:** The PR now implements a second, independent augmenting-path algorithm that explicitly constructs injective witness-to-target index assignments and records SHA256 certificates, against the previously independent exact maxflow/mincut Hall algorithm. All individual charge edges, distinct source-column supports, distinct target assignments, accepted GF5 floors, seven original motif classes and prior D6-only regression are validated. [Latest exact HEAD specialized Contract #38207988133](https://github.com/definitely-stable/Mathlab/actions/runs/38207988133) SUCCESS (7 test methods), [INDEX #38207988130](https://github.com/definitely-stable/Mathlab/actions/runs/38207988130) SUCCESS; [full Research #38207988187](https://github.com/definitely-stable/Mathlab/actions/runs/38207988187) QUEUED at this report. Keep Draft until full CI and mathematical review.

**Strict logical frontier:** A successful finite injection gives `Jcross <= S_seven` for THAT specific W32 labeling, not `S_s=Omega(s^6)` for all h. Even if an all-h injection could be proven, one additionally needs an **all-h positive lower bound on Jcross OR a dichotomy/charging argument extracting accepted S positives when Jcross is small**. Neither Branch A nor B of issue #230 is settled, full R3 is a different target, and no ASET exponent is claimed. Next stage E1-K3-G2-F should construct the source-column two-overlap all-h charging candidate or a finite counterexample at W34 by building an efficient all-h accepted S candidate enumerator. No merge, do not modify main.

---

## Comment 095 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6118767763
- GitHub comment ID: 6118767763

### HYP-105 E1-K3-G2-F — TRUE accepted GF5 positive target generation on W(3,4) and constructive partial Hall injections

Implemented [stacked Draft PR #379](https://github.com/definitely-stable/Mathlab/pull/379) over accepted fully CI-green [PR #378](https://github.com/definitely-stable/Mathlab/pull/378), pinned original parent HEAD `ef846731908b219320919b9a486519c442c4eba0`. **Current PR #379 HEAD** `71434182bbce2aae0921b79a8e4f0bdfe74278a8`. Main untouched, no merge.

**New sound all-a structural theorem/certificate:** A six-DISTINCT-ORIGINAL-incidence target using one coherent f,g is in the accepted seven GF5 six-coordinate 2-regular motif classes precisely when both physical halves have exactly six degree-two coordinates, each source factor endpoint multiplicity belongs to A=(1^6), B=(2,1^4), C=(2^3), and D6 (A/A) has matching connected column-dual C6 or B/B has the actual repeated-original-factor positions classified overlap/disjoint. All emitted targets retain previously proven strictly positive class-dependent full 51-palette GF5 floors. The generic classifier was compared **on all 62,370** B0 W32 eligible left-sixsets for both lex and reverse and EXACTLY matches the accepted independent tag oracle. Exhaustive untruncated completion from two fixed original columns around representatives of all seven families exactly matches B0's accepted original sixsets containing that pair.

**Algorithm:** For each actual five-distinct-original-column Jcross witness, choose original column PAIRS, DFS-extend by four new ORIGINAL incidence IDs subject to source original multiplicity<=2, physical coordinate degree<=2, exactly six distinct degree-two symbols in each half, and sound remaining-coordinate feasibility constraints; apply exact seven-family accepted-S classifier. Every target therefore shares at least two ACTUAL ORIGINAL columns with its witness. The closure-first ordering is merely a permutation of candidate columns and retains completeness IF no cutoff. Explicit node and accepted-target caps are FAIL-CLOSED: all targets found remain valid, but a truncated search CANNOT establish absence or an obstruction. Constructive explicit augmenting-path matching (with SHA256 assignment) reconciles exact unit-capacity maxflow/Hall. No full W34 accepted motif enumeration.

**Quantitative new finite W34 result, from [Contract #38210896197](https://github.com/definitely-stable/Mathlab/actions/runs/38210896197) SUCCESS:**
```
True GQ         Jcross all     heavy witnesses SELECTED   distinct genuine positive S targets    exact injective coverage
W(3,2) lex      36             6                         58                                 6/6
W(3,4) lex     128             8                        221                                 8/8
W(3,4) random   75             8                        249                                 8/8
```
W34 random seed is 20261012. Each selected witness examined 10 two-column seeds with 40,000 candidate-node and 12 accepted-target maximum per seed. **All 80 W34 seed-pair searches in EACH model reached a work/target cutoff**, so these are rigorously checked POSITIVE existential certificates for the explicitly sampled eight heavy-class witnesses, NOT completeness, not all-Jcross coverage, and not falsifiers for other witnesses. They establish finite feasibility of source-two-column charging beyond W32.

**Independent exact GF5 on ACTUAL W34 targets:** [Contract #38210952901](https://github.com/definitely-stable/Mathlab/actions/runs/38210952901) SUCCESS (six methods), directly computed all ten signed full GF5 782-orbit Fourier weights on genuine original incidence sets `W34 lex (0,41,68,139,189,206) [B-left/A-right]`, `W34 random (0,140,141,197,209,420) [A-left/B-right]`, `W34 random (2,3,284,334,341,379) [B/B-disjoint]`. All ten sign weights strictly positive per set and total exceeds class accepted GF5 risk numerator floor. Positive S targets are NOT synthetic graph patterns.

**Exact HEAD latest hosted CI:** [specialized Contract #38211074830](https://github.com/definitely-stable/Mathlab/actions/runs/38211074830) SUCCESS, [INDEX #38211074926](https://github.com/definitely-stable/Mathlab/actions/runs/38211074926) SUCCESS, [Research #38211074939](https://github.com/definitely-stable/Mathlab/actions/runs/38211074939) IN PROGRESS at writing.

**Scientific next gate:** Expand actual deterministic all-witness W34 charging with efficient 2-factor closure joins or derivation of symbolic bounded-multiplicity two-original-column charging under arbitrary coherent f,g for ALL s=2^h. Distinguish proof of Jcross<=S from actually desired S>=c*s^6: also need all-h lower Jcross or a positive-S alternative when Jcross is small. No Branch A/B, no full GF5 R3 bound, no new ASET exponent. Keep Draft and #230/#176/#169 OPEN; do not merge to main.

---

## Comment 096 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6119266888
- GitHub comment ID: 6119266888

### HYP-105 E1-K3-G2-G — COMPLETE finite W34 Jcross→accepted-S charging and explicit two quantitative lower certificates

Implemented [stacked Draft PR #380](https://github.com/definitely-stable/Mathlab/pull/380) on parent [#379](https://github.com/definitely-stable/Mathlab/pull/379) pinned accepted exact HEAD `71434182bbce2aae0921b79a8e4f0bdfe74278a8` (all three hosted checks SUCCESS). **Current G2-G HEAD** `8180230dd58a9c0a68b0994136937cfe8c2409db`. Main untouched, no merge, #230 and linked research issues remain OPEN.

**Mathematical aim:** Previous K3-G2-F had a true positive Hall certificate for ONLY 8 heavy-class source witnesses in W34 lex and 8 in W34 random; full Jcross masses are 128 and 75. G2-G now generates EVERY individual original cross-source Jcross improper six-cycle from the full GQ Kikuchi edge→original incidence provenance. Each has exactly five distinct ORIGINAL source columns. The reference builds a globally SHARED, deduplicated index of actual accepted positive six-distinct-ORIGINAL-column S targets from all seven validated GF5 families, each target found via >=2 original column seeded completion. Initial one-seed-per-witness targets serve ALL source witnesses; if exact global capacity-1 Hall leaves an unmatched witness, search its next original seed pair and recompute exact global Hall. Independent integer maxflow/mincut and constructive augmenting-path matching must agree, and every assigned target is independently checked to be a genuine source sixset with positive certified 51-palette class GF5 weight. Incomplete target enumeration can NEVER certify no-go, but discovered positive targets and successful full matchings are rigorous existential results.

**New complete finite theorem for TWO legal globally coherent W(3,4) maps (GitHub-hosted):**
```
Model                    W32 lex control   W34 lex        W34 random(seed 20261012)
Jcross exact              36                128             75
actual accepted S found  150                374            203
capacity-1 matched       36/36              128/128         75/75
additional rounds         0                  1              5
positive S lower         S>=150             S>=374         S>=203
positive weighted R3 floor
   51^6 R3 >=           6,359,976         16,504,153      8,814,887
```
No target reused: each of the 128 lex / 75 random source witnesses is assigned a distinct **positive accepted seven-family** ORIGINAL incidence sixset with at least TWO actual original columns in common. Exactly k=1 target capacity. The full Jcross masses include both point-origin and line-origin contributions, not merely heavy-class sampling. Actual finite inequalities `Jcross(f,g)<=S_4(f,g)` follow for both **specific** maps.

The 374 actual accepted S targets for W34 lex split across 7 families: A-left/B-right 132, B-left/A-right 101, B/B-disjoint 58, B/B-overlap 7, C/A 60, C/B 5, D6 11. The 203 random targets split as 84,36,26,3,42,3,9 respectively. Hence the shown full-R3 lower numerator is a strict bound obtained by summing existing independently-proved GF5 class floors over DISTINCT accepted original source sixsets, NOT an exact evaluation of full R3.

**Evidence:** Initial [Contract #38214269288](https://github.com/definitely-stable/Mathlab/actions/runs/38214269288) SUCCESS gave 127/128 and 70/75 with deliberately small work budget, not a counterexample. Enlarging the pair seed limit to 10 with explicit 30,000-candidate budget per pair yielded full constructive assignments at [Contract #38214367141](https://github.com/definitely-stable/Mathlab/actions/runs/38214367141) SUCCESS. Exact HEAD [Contract #38214542805](https://github.com/definitely-stable/Mathlab/actions/runs/38214542805) SUCCESS now also seals full-map 128/128 & 75/75 positive assignment witness SHA256, exact quantitative S and 51^6 R3 lower integer regressions, exhaustive W32 B0 accepted-target cross-checks, and zero-node negative-proof guards. [INDEX #38214542916](https://github.com/definitely-stable/Mathlab/actions/runs/38214542916) SUCCESS. [Full Research #38214542640](https://github.com/definitely-stable/Mathlab/actions/runs/38214542640) IN PROGRESS at report.

**Strict nonclaims and next proof gate:** Does NOT prove ALL-h `Jcross<=K S_s` or `S_s=Omega(s^6)`; the results hold only for the two specific W34 global injections plus previously pinned W32 cases, with no claim of all-target enumeration. For original Branch A, an all-h uniform K source→S charge and an INDEPENDENT restricted-seven-family quantitative dichotomy `S_s>=alpha*s^6-beta*Jcross` are both necessary to deduce `S_s>=alpha/(1+beta*K)*s^6`. Existing K2/K3 complete Kikuchi C6/full-R3 bounds DO NOT establish the latter S-family inequality. Next K3-G2-H should seek a symbolic all-h source-to-target extension or find a LEGAL adversarial f/g counterexample, and separately establish a genuine accepted S-family surplus/dichotomy rather than importing full R3. Keep all PRs Draft until independent mathematical review, no main change/merge, no ASET exponent.

---

## Comment 097 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6119583175
- GitHub comment ID: 6119583175

### HYP-105 E1-K3-G2-H — complete W32 210-single-swap adversarial Hall gate (Draft implementation)

Created [stacked Draft PR #381](https://github.com/definitely-stable/Mathlab/pull/381) over fully hosted-green [PR #380](https://github.com/definitely-stable/Mathlab/pull/380) pinned HEAD `8180230dd58a9c0a68b0994136937cfe8c2409db`. **Current child HEAD** `1c1e2b55c5df3a93e0a6ae13db183d31095c73c4`. Main untouched; no merge. Root #230/#176/#169 remain OPEN.

**Scientific objective:** G2-G found complete genuine unit Hall positive injections for two W(3,4) maps, but budgeted target enumeration cannot certify negative obstructions. G2-H now uses the W(3,2) **COMPLETE** 62,370-left-candidate B0 seven-family original-sixset enumeration *for every tested map*, with exact original-source five-column Jcross provenance and exactly the `>=2` shared ORIGINAL incidence-column relation. Independently checked maxflow/mincut and constructive augmenting path assignments determine each case. A violated exact Hall cut is a genuinely sound **finite NO-GO for this restricted unit-capacity two-overlap source-to-S charging rule**, NOT a no-go for general `S_s=Omega(s^6)` or full R3.

**Precisely scoped 210-map shell:** 105 transpositions of whole original point pair labels and 105 transpositions of whole original line pair labels around the legal W32 lex `f0,g0`. Recompute ALL authentic accepted S targets and all Jcross witnesses for every resulting globally coherent injection. Emit exact min S, max Jcross, min S-Jcross, min witness target degree, deficiency histogram, positive GF5 floor, and assignment digest. This is not exhaustive over all (15!)² maps and never yields an all-h claim.

**CI at report time:** exact child HEAD [INDEX #38216707576](https://github.com/definitely-stable/Mathlab/actions/runs/38216707576) **SUCCESS**, [full 210-case Contract #38216707775](https://github.com/definitely-stable/Mathlab/actions/runs/38216707775) **IN PROGRESS** (focused tests green; full shell running), [Research #38216707881](https://github.com/definitely-stable/Mathlab/actions/runs/38216707881) **IN PROGRESS**. Do not claim a 210-case theorem or any NO-GO until exact HEAD full-shell output and Research are green. New workflow runs full shell once, not in each inherited Research job.

**Next K3-G2-I:** If the complete-target Hall cut fails for any swap, inspect exact isolated/original-foot classes and the minimum viable capacity/locality relaxation; if all pass, use adversarial *multi-step correlated* f/g permutations with the same complete-target negative-proof discipline. Independently derive the genuine seven-family all-h `S_s>=alpha*s^6-beta*Jcross` surplus theorem; K3 full-C6/R3 does not suffice. Keep all Draft pending independent review.

---

## Comment 098 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6119631901
- GitHub comment ID: 6119631901

### K3-G2-H: exact 210/210 finite one-swap theorem — completed hosted Contract

The **complete** 210-map W(3,2) single-pair-label transposition shell around the fixed legal lex f,g has now passed [Contract #38216707775](https://github.com/definitely-stable/Mathlab/actions/runs/38216707775) **SUCCESS**, including 4 focused unit tests, exhaustive 62,370 B0-eligible original sixsets per map, true seven-GF5 original family classification, all Jcross witnesses and independent integer maxflow / augmenting matchings. **210/210 complete-target unit-two-overlap Hall matchings, 0 finite Hall failures, 0 isolated witnesses.** Exact extrema across different maps: `min S_seven=176` (right swap 2,11); `max Jcross=47` (left swap 3,9); `min(S-Jcross)=139` (left swap 1,14); `min witness accepted-target degree=3` (right swap 1,8). Base lex: Jcross=36, S=259, accepted positive seven-family `51^6 R3>=11,225,795`.

**Finite theorem**: For EACH of the 105 left and 105 right single whole-pair transpositions at W(3,2), EVERY Jcross witness injects into a distinct true positive original accepted seven-family sixset sharing >=2 original incidence columns. This does not quantify over all W32 label permutations or any h>1. The universal all-h charging theorem and independent seven-S surplus `S_s>=alpha*s^6-beta*Jcross` remain OPEN; no Branch A/B or ASET exponent.

Full result/assignment digest: `d841d5e6dfb31666df301297843806deb099b3388be842912c3d7658306fc8b7`. The regression is now pinned in [Draft PR #381](https://github.com/definitely-stable/Mathlab/pull/381) dedicated workflow and research note. Because exact regression/docs were appended after the initial success, final HEAD CI **must be renewed** (Contract/INDEX/full Research) before mathematical acceptance. Main untouched; all parents Draft.

---

## Comment 099 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6120053120
- GitHub comment ID: 6120053120

### HYP-105 E1-K3-G2-I — exact all-host swap locality and coherent correlated W32 Hall adversary

Implemented [stacked Draft PR #382](https://github.com/definitely-stable/Mathlab/pull/382) on fully Contract/INDEX/Research-green [PR #381](https://github.com/definitely-stable/Mathlab/pull/381), pinned parent `4ad9303d065910bdec38ccd6d33e58f5a3bce6db`. No main change or merge; root #230/#176/#169 OPEN.

**Restricted mathematical lemma (arbitrary finite original host):** for any globally coherent original-vertex unordered-physical-pair labelings f,g, swapping complete physical pairs on two original vertices of one side cannot change the accepted exact original six-incidence GF5 seven-class tag of ANY original sixset omitting incidences at both swapped original endpoints. The source/physical profiles and duals for all six columns are unchanged. For W(3,2), implement exact incremental difference: on right swap, restrict rescoring to impacted sixsets of the fixed complete B0 left 62,370 candidate universe; on left swap, include impacted sets in the COMPLETE union of old/new left-eligible 62,370 candidate universes. Every chosen correlated state is independently checked against complete B0 seven-family original-sixset enumeration and complete genuine Jcross-to-S Hall, including independent maxflow/mincut and augmenting path. No hidden incomplete search negative claims.

**Hosted result** [Contract #38219544548](https://github.com/definitely-stable/Mathlab/actions/runs/38219544548) **SUCCESS** on earlier child HEAD `4a9337bcd4b7a4fb52e3e2cb2a963ee6c330d737`: 144 exact delta-scored candidate transpositions, 21 independently full-replayed coherent W32 maps (3 dual-side initial anchors + 18 selected search states), **21/21 accepted positive unit Hall matches, 0 finite local Hall failures**. Greedy seeded correlated searching reduced the smallest OBSERVED `S_seven-Jcross` from the previous complete 210 single-swap shell minimum 139 to **68** on a different, explicitly defined W32 coherent map: `S_seven=94`, `Jcross=26`, minimum accepted target degree 2, and valid `51^6 R3 >= 4,289,420` accepted seven-family contribution (NOT full R3). Other anchor minima: 92,92.

Best source permutation transcript from lex: INITIAL left(0,14), right(0,14); then left(1,4), right(2,4), left(2,13), right(3,13), left(2,3), right(1,14). The six selected-state margins are 139,114,102,84,69,68 respectively. Whole original vertex pair labels are swapped; original GQ incidences unchanged. Transcript digest `25e93b1374d99a6db40a53df913f6e87bfa1cfbcd9909b4b960454d7d54162d9`, final complete labeling digest `d736eae47626ecf935b21d9fec7d09ca1af80a48cda20b50a7e3c7c5bfb3baa0`. These are frozen in subsequent Contract regression and docs. **Final current child HEAD** `165785dacd0005587b16a8242f307dcda9d1233b`; require renewed exact HEAD Contract/INDEX/full Research SUCCESS after regression/doc commits. Keep Draft pending independent mathematical review.

**Research frontier:** The finite optimum is NOT an all-W32 or all-h minimum, the 144 candidates are NOT 144 Hall-certified maps (only 21 selected complete replays), and no all-h `Jcross<=K*S_s`, `S_s>=alpha*s^6-beta*Jcross`, Branch A/B, full R3, or ASET exponent follows. Next K3-G2-J should prioritize symbolic positive-seven-family surplus/dichotomy or a genuine all-h counterexample, not endless finite-search extrapolation.

---

## Comment 100 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6120303972
- GitHub comment ID: 6120303972

### HYP-105 E1-K3-G2-J — exact all-h NECESSARY rational surplus coefficient screen (new stacked Draft PR #383)

Implemented [stacked Draft PR #383](https://github.com/definitely-stable/Mathlab/pull/383) above [PR #382](https://github.com/definitely-stable/Mathlab/pull/382), pinned parent HEAD `165785dacd0005587b16a8242f307dcda9d1233b`, child HEAD `9609eed8de98057b6571fd37e36988b1f0102007`. Main unchanged; #230/#176/#169 OPEN.

**Precise new mathematical theorem (all-h NECESSITY, not sufficiency):** For any all-h proposal `S_s(f,g)>=alpha*s^6-beta*Jcross_s(f,g)`, for every genuine globally coherent legal W(3,2^h) model m one must have `alpha<=(S_m+beta J_m)/s_m^6`. Any finite legal family F gives the exact necessary envelope `A_F(beta)=min_{m in F}(S_m+beta J_m)/s_m^6`. This is piecewise-affine, nondecreasing and concave for beta>=0, with rational slopes/breakpoints. Any alleged alpha STRICTLY above this envelope has a concrete rigorously certified finite GQ counterexample. This screens proposed coefficients; it DOES NOT prove any positive alpha, any finite universal K, S=Omega(s^6), full-R3 result or ASET exponent.

**Implementation:** Exact independent complete B0 62,370 original-sixset accepted GF5 motif enumerations and actual original-source Jcross Kikuchi witnesses on 219 named true W32 labelings (lex, reverse, 210 entire H one-swap shell, 7 coherent best G2-I anchor/path models), all with ONE globally consistent f,g per model; never negative-proof from partial W34 targets. Compute full rational active envelope using integer/Fraction pair-line crossings. Certify each active interval via ALL competing affine inequalities at both endpoints, verify infinity via slopes, PLUS independent exhaustive pair-intersection/midpoint falsifier. Compute necessary `K>=max_{m:S_m>0} J_m/S_m`. Each candidate invalid alpha,beta yields original source map and exact strict counterexample. Original G2-I coherent W32 map S=90 yields explicit falsification of `S_s>=2*s^6` (90<128 at s=2), so for beta=0 universal alpha must satisfy `alpha<=45/32`. This refutes only those candidate constants, not universal Branch A.

**Current acceptance:** [specialized Contract #38221690490](https://github.com/definitely-stable/Mathlab/actions/runs/38221690490) unit/rational tests SUCCESS, full 219-map report IN PROGRESS; [INDEX #38221690444](https://github.com/definitely-stable/Mathlab/actions/runs/38221690444) SUCCESS; [Research #38221690493](https://github.com/definitely-stable/Mathlab/actions/runs/38221690493) IN PROGRESS at report. PR Draft, do not merge before exact child HEAD 3/3 SUCCESS and independent mathematical review. Next K3-G2-K: seek actual all-h positive restricted-S surplus tensor inequality or genuine infinite correlated counterexample, NOT treat finite necessary coefficient cone as proved sufficient bound.

---

## Comment 101 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6120349322
- GitHub comment ID: 6120349322

### K3-G2-J — hosted exact 219-map rational coefficient frontier and true proposed-bound NO-GO

[Stacked Draft PR #383](https://github.com/definitely-stable/Mathlab/pull/383) now has complete hosted [Contract #38221690490](https://github.com/definitely-stable/Mathlab/actions/runs/38221690490) **SUCCESS** at original child HEAD `9609eed8de98057b6571fd37e36988b1f0102007`. All actual finite coherent W32 labels: **219 original legal models**, **198 exact distinct (S_seven,Jcross) pairs**, independent **141 rational intersection/midpoint/ray oracles**, entire 210-map G2-H single-swap regression min S=176/max J=47/min(S-J)=139, and exact G2-I original correlated path replay.

**NEW strictly scoped exact rational finite theorem:** Every proposed UNIVERSAL all-h `S_s>=alpha*s^6-beta*Jcross` (alpha>0,beta>=0) must obey this 219-source NECESSARY coefficient ceiling:
```
0 <= beta <= 11/4: alpha <= (90+21 beta)/64 (real legal correlated map corr:5)
11/4 <= beta <= 8: alpha <= (101+17 beta)/64 (real legal corr:4)
beta >= 8:         alpha <= (117+15 beta)/64 (real legal corr:3)
```
All three supporting lines and both rational switch points were verified by exact Fraction arithmetic with endpoint inequalities against ALL 219 model lines and a second independent complete rational pair-intersection oracle. A strict excess `alpha>A_F(beta)` is a rigorous finite legal GQ counterexample to the PROPOSED universal constants. In particular `(alpha,beta)=(2,0)` is disproved by W32 actual `S=90<2*64=128`. The necessary beta=0 alpha ceiling is **45/32**, NOT a proved positive all-h alpha. A true legal W32 `S=94,Jcross=26` forces **K>=13/47** for any proposed universal `Jcross<=K*S` (again existence of any finite K unproved). Full exact corpus SHA256: `2bed34a0fc5c6181ffc239f60e69cbd7682ee71d1585310c30f66996df89c461`.

**Scientific limitations:** This is a PROVED all-h NECESSITY/separation rule instantiated on finitely many W32 labelings; the explicit finite three-piece envelope is not a universal lower bound for all labels/all h. Partial W34 positive search is not used as falsification. No universal alpha>0, all-h J<=KS, unconditional S=Omega(s^6), Branch A/B, full-R3 or ASET exponent was established.

The PR has since pinned all three rational regimes and digest into the dedicated Contract, research note and index. **Current final HEAD `62fc61376d1190d243968e0e7ca901a120b67570`** requires renewed exact-head Contract/INDEX/full Research SUCCESS before research acceptance. Keep Draft, main untouched, #230/#176/#169 OPEN. Next K3-G2-K must seek a genuine all-h restricted-positive-seven-family tensor lower/defect inequality or an infinite legal correlated counterexample; more finite envelope screening alone will not close the original conjecture.

---

## Comment 102 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6121219328
- GitHub comment ID: 6121219328

### HYP-105 E1-K3-G2-K — constructive all-h fixed-left B/A right-injection via exact conditional expectations

Implemented [stacked Draft PR #384](https://github.com/definitely-stable/Mathlab/pull/384) over fully green [#383](https://github.com/definitely-stable/Mathlab/pull/383), pinned parent exact HEAD `62fc61376d1190d243968e0e7ca901a120b67570`. Main untouched, no merge, #230/#176/#169 remain OPEN.

**New scoped constructive all-h corollary from prior B1-A/C0:** Fix ANY globally injective physical unordered-pair LEFT original factor map f for W(3,s), s=2^h. Let w_f(R) be the number of distinct original six-incidence B-left/6-distinct-right-source supports with original right endpoint sixset R. Let physical T be all 70*C(a,6) six-edge two-factor supports on six physical coordinates of K_a. Under uniform right injection g, `mu_f=(sum_R w_f(R))*70*C(a,6)/C(C(a,2),6)` equals B1-A's existing `(140+o(1))*s^6`, uniformly in f. The exact prefix conditional probability is
```
# {T: T intersect USED_physical_labels == FIXED_images_of_R}
/ C(K-k,6-|FIXED_images_of_R|)
```
The condition excludes used labels assigned outside R (essential). By the **CLASSICAL** conditional-expectation method and exact Fraction tower identity, choosing the maximizer at every original right source vertex creates ONE global injective right g_max with `S_seven(f,g_max)>=U_B/A(f,g_max)>=mu_f`. Similarly choose a minimizer g_min with `U_B/A(f,g_min)<=mu_f`. The abstract six-hypergraph proof holds for all h; generic method is known (e.g., Karayel AFP 2024/2025) and is NOT claimed as an original discovery. This proves SOME right g for each f, NOT a positive bound for every adversarial f,g, nor Branch A/B.

**Independent true-original finite evidence:** [First hosted Contract #38227910260](https://github.com/definitely-stable/Mathlab/actions/runs/38227910260) SUCCESS, with exact physically legal W32 K6 models:
```
fixed f           original weight  random g mean   constructed U_B/A max/min   complete B0 S at max/min
lex               5000             10000/143       131 / 33                   320 / 101
correlated-left   5319             10638/143       120 / 40                   245 / 104
```
All four count records independently checked via true-original C0 weighted B/A physical-six-target overlap and exhaustive 62,370 B0 eligible original sixsets/class-GF5 accepted S census. Strict positive 51^6 R3 seven-family floor for all, no fabricated full R3. Small 7-source/7-physical-label prefixes brute-completed independently and **additional 7-source/8-physical-label non-surjective prefix exhaustive test** added after first CI.

**Current final child HEAD** `5a9044af5b3b67d89b4ac123ccd0a4879376140e`. Host workflow pins exact 4 high/low W32 values, demands independent unit tests and full report. Run final HEAD dedicated Contract, INDEX, Research; keep Draft until all three GREEN plus independent mathematical review. No new ASET exponent. Next G2-L needs actual arbitrary-right signed-trade/stability transport: B1-B single-transposition O(s^12) influence is too weak to telescope to s^6, and C0's 3-cube two-marginal blind trade excludes naive low-order marginal proofs.

---

## Comment 103 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6121992201
- GitHub comment ID: 6121992201

### HYP-105 E1-K3-G2-L — actual 223-map signed seven-S compensation result + all-h XOR swap theorem

Implemented [stacked Draft PR #385](https://github.com/definitely-stable/Mathlab/pull/385) over [PR #384](https://github.com/definitely-stable/Mathlab/pull/384) pinned fully 3/3 GREEN HEAD `5a9044af5b3b67d89b4ac123ccd0a4879376140e`. Main unchanged, no merge; issue #230/#176/#169 OPEN.

**Mathematics, all-h scope:** Signed B/A deficit `D_f(g)=mu_f-U_B/A(f,g)`, remaining six true positive GF5 classes `R(f,g)=S_seven(f,g)-U_B/A(f,g)`, and Jcross obey algebraic IDENTITY `R-D=S_seven-mu_f`. Therefore naive `D<=R+beta Jcross` is EXACTLY equivalent to `S_seven+beta Jcross>=mu_f`. This is NOT already a proved all-h bound. A second genuine all-h support lemma: swapping whole pair labels of two original RIGHT vertices u,v changes the exact weighted source-sixset B/A target overlap ONLY on original right-sixsets R with `|R∩{u,v}|=1`; those containing BOTH or NEITHER have identical unordered physical six-edge images. Signed identity `ΔU=sum_{R:XOR}w_f(R)[1_T(g'(R))-1_T(g(R))]` holds for any globally coherent injective original source labels, all h. It does NOT bound the NEGATIVE gradient needed to close the universal theorem.

**GitHub-hosted exact complete finite result:** [Contract #38232996122](https://github.com/definitely-stable/Mathlab/actions/runs/38232996122) **SUCCESS** on earlier child HEAD `f8a97ebe02716e4128b2e1dbf58332db0663b75a`. Independently exact C0 weighted original-sixset B/A, full 62,370 B0 original-incidence candidate census/SEVEN positive GF5 families, entire both-source-side original Jcross, class GF5 certified lower numerator and rational source f-specific random B/A mean:
- Exactly **223** named coherent W32 legal (f,g): 2 baseline, 210 all one-swap G2-H, 7 correlated G2-I anchor/path, 4 constructed original high/low K3-G2-K maps.
- Exactly **109** distinct original LEFT f sources; **11** maps have genuinely positive signed deficit `mu_f-U_B/A>0`, but **0** have `S_seven<mu_f` and **0** have a J=0, S<mu counterexample. Thus the exact candidate `S>=mu_f` holds at beta=0 ONLY FOR THESE 223 finite maps; cannot promote to all-W32 bijections, all s or Branch A.
- Worst exact SAME-SOURCE `corr:5`: `S=90,Jcross=21,U_B/A=44,remaining-six=46,mu_f=10638/143`, deficit `D=4346/143`, surplus `S-mu_f=2232/143`. Remaining accepted six-family count split `37 A-left/B-right, 6 B/B-disjoint,1 B/B-overlap,2 C/A,0 C/B,0 D6`. `corr:6` S=94,J=26,U=44,rest=50 and residual 2804/143. Distinct named maps, no mixing of extrema.
- Exact full-223-row certificate SHA256 `ebfc121f04056fe0b6215633e1f93ab135a306ced5fb92213925f665e672f1d0`, now sealed in dedicated Contract and research note.

**Final child PR HEAD** `adf466f7093da91d10ea968ed2a45168d6d82739` awaiting renewed exact HEAD Contract/INDEX/full Research before accepting. Remains Draft pending independent mathematical review; main untouched. **Next K3-G2-M:** construct a NEW typed sixth-order signed-source transport inequality for arbitrary right labels with GQ incidence-fiber information (not just the tautology, random mean or 1/2-marginal design), or a legitimate infinite family counterexample. No universal alpha>0, K, or ASET exponent claimed.

---

## Comment 104 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6122353169
- GitHub comment ID: 6122353169

### HYP-105 E1-K3-G2-M — all-h ORIGINAL GQ dual sixsource equality and exact two-family falsifier results

Created [stacked Draft PR #386](https://github.com/definitely-stable/Mathlab/pull/386) on final green [PR #385](https://github.com/definitely-stable/Mathlab/pull/385), pinned parent HEAD `adf466f7093da91d10ea968ed2a45168d6d82739`, Contract/INDEX/Research SUCCESS. No merge, main unchanged; root #230/#176/#169 OPEN.

**New mathematically exact all-h dual incidence reduction:** For a true coherent legal original W(3,s) pair-label (f,g) on original incidence E, transpose EVERY original incidence (p,l)->(l,p) and swap WHOLE source pair assignments (f,g)->(g,f). This maps each original accepted A-left/B-right six-distinct-incidence motif BIJECTIVELY to a dual original accepted B-left/A-right sixset. It follows that `U_A/B(f,g)=sum_{Q:|Q|=6}w_g^dual(Q)*1_T(f(Q))` and `U_B/A(f,g)=sum_{R:|R|=6}w_f(R)*1_T(g(R))`, where weights count DISTINCT actual original six-incidence supports. All seven accepted positive GF5 original-class union S is invariant under dualizing. This holds at all legal s, but cannot itself prove ANY positive universal lower bound.

**Strong proposed universal inequality:** P2 `U_B/A(f,g)+U_A/B(f,g)>=mu_f` would imply P7 `S_seven(f,g)>=mu_f=(140+o(1))*s^6`. Both remain OPEN for all coherent f,g. P2 is strictly stronger: other five positive original GF5 classes can rescue a finite P2 failure. NEVER substitute positive mean over random g or partial W34 counts for a universally valid lower bound.

**First hosted exact evidence** [Contract #38235039675](https://github.com/definitely-stable/Mathlab/actions/runs/38235039675) **SUCCESS** on earlier child HEAD `6d0351dd76d2368cedd96c42c0bac8a15f73ae08`:
- COMPLETE **223** true globally coherent W32 original-label models, 109 different f, 114 different g, independent dual/original 62,370-candidate B0 GF5 seven-family enumerations and independent C0 ORIGINAL/DUAL sixsource target overlaps. **0 finite P2 violations, 0 P7 violations**. Smallest corpus `U_B/A+U_A/B-mu_f=945/143` at `corr:5` (`U_B/A=44,U_A/B=37,S=90,mu=10638/143`).
- A separate **120** precisely delta-scored seeded correlated swap candidate probe (3 initial anchors; 5 selected moves each), with **18** selected/anchor states independently COMPLETE original/dual C0/B0 true-source replay. **0 selected P2/P7 violations**. Harder actual `corr:5` + whole original LEFT vertex-pair-label swap `(13,14)`: `U_B/A=36,U_A/B=39,S=86,Jcross=22,mu_f=9968/143`, other-five=11, exact signed pair margin **757/143>0**, full S-mu margin **2330/143>0**. This is one actual legal coherent global W32 source map, not mixed extrema or an all-W32 minimum.
- Exact 223-row original/dual corpus SHA256 `cdabb909755ea9f1cc5f83874b73c880937cb50039ea5843329e460d87b0f40a`; 15 selected-map path SHA256 `5db98923e6769b8398cf97d400e7f87520275e333bab9538732d031313d22835`; new hardest physical-label hash `e5c3f92068d6221f44cbb77fbae5dc95000144a0c495d216a48cdf3b047bfd4a`. All were pinned to dedicated Contract after initial success and documented in the AI-index.

**Acceptance:** Current final child HEAD `294ce9c1fc688374631d58d91b20ffa8d62ad9c2`; renew exact final-HEAD Contract/INDEX/full Research. Keep Draft pending independent mathematical review. Branch A/B and all-h S=Omega(s^6), charge K and ASET exponent remain UNPROVED. Next scientific step should seek a non-tautological all-h ORIGINAL sixth-order coupled weighted-hypergraph inequality exploiting G2-C GQ projection fibers, or an infinite genuine adversarial f,g family; mere finite sample expansion is not proof.

---

## Comment 105 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6122920408
- GitHub comment ID: 6122920408

### HYP-105 E1-K3-G2-N — Johnson six-harmonic exact target theorem and ORIGINAL GQ-dual spectral certificate

New stacked [Draft PR #387](https://github.com/definitely-stable/Mathlab/pull/387) on accepted-GitHub-hosted [Draft #386](https://github.com/definitely-stable/Mathlab/pull/386) final parent HEAD `294ce9c1fc688374631d58d91b20ffa8d62ad9c2`. Main unchanged; #230/#176/#169 OPEN; do not merge prior to independent mathematical review.

**ALL-a exact Johnson reduction (not an all-h positive GQ lower bound).** For K=C(a,2), p=70*C(a,6)/C(K,6), physical 2-factor indicator on J(K,6) has H1 identically zero. Its H2 pair coefficient is `(c_orbit-p*C(K-2,4))/C(K-4,4)` with `c_adj=7*C(a-3,3)`, `c_dis=14*C(a-4,2)`. Thus H2(S) depends only on pair-edge adjacency A(S). In physical K6: `H2(S)=(60-7*A(S))/330`, and exact target rank energies H0..H6 are **[140/143, 0, 42/11, 710/1001, 86/7, 1182/77, 258/7]**; high ranks 3–6 have energy **9324/143**. Actual K6-2factor exact target is recovered on ALL 5005 physical sixsets, and the entire decomposition is orthogonal, Parseval-valid, and consistent with independent physical two-orbit counts. At a=9, H2=0 (the known 2-design exception); legal W32/W34 a=6/14 are not this exception.

**ALL-host exact source identity.** ORIGINAL B/A weighted sixsource (with explicitly zero-padded unused physical pair labels) satisfies `U_BA=mu_f+C2+C_ge3`; the TRUE ORIGINAL transposed-incidence dual yields independent A/B rank decomposition with its own mean. A rigorous rank>=3 Cauchy–Schwarz certificate checks `C_ge3²<=E_W_ge3*E_T_ge3` from independently computed rank<=2 source marginals. This is a sufficient-criterion framework, NOT a proof of universal P2; abstract C0 3-cube trade shows exact rank<=2 information does not determine higher rank overlap and is NOT a GQ counterexample.

**GitHub-hosted initial Contract [#38239319194](https://github.com/definitely-stable/Mathlab/actions/runs/38239319194) SUCCESS** (5 independent unit tests + full J(15,6) spectrum + true ORIGINAL/DUAL B0/C0 for two W32 maps). For the previously established hard globally coherent map from M: `U_BA=36,U_AB=39,S=86,mu_f=9968/143,P2 margin=757/143`. Spectral contribution on SAME original state: B/A `C2=-1897/55,C_ge3=51/65`; genuine dual A/B `C2=-1207/33,C_ge3=610/429`. The geometric cancellation is much sharper than naive Cauchy–Schwarz: the B/A bound allows |C_ge3| up to ~478.55 while the actual signed correlation is ~0.785. These are two finite original-GQ model certificates, NOT a universal coercivity theorem.

**Correctness hardening:** Source energy requires explicit `a`, because in a non-surjective V<K map the maximum occupied physical coordinate need not equal a-1. Added independent K7 zero-padding regression and pinned entire hosted K6 spectrum and hardest-source correlations in the Contract. Dedicated final-head [Contract #38239673644](https://github.com/definitely-stable/Mathlab/actions/runs/38239673644) **SUCCESS**, [INDEX #38239673565](https://github.com/definitely-stable/Mathlab/actions/runs/38239673565) **SUCCESS** on current N HEAD `6ddf54f6e48914b948c0331a358bc759487d5dce`; full [Research #38239673567](https://github.com/definitely-stable/Mathlab/actions/runs/38239673567) **PENDING** when inspected. No Research acceptance or independent proof review claimed.

**Next K3-G2-O:** derive an ACTUAL all-h GQ-incidence projection-fiber source-specific rank-3..6 cancellation/coercivity inequality jointly coupling W_f and W_g^dual, or construct an infinite coherent legal adversary. P2, P7, S_s=Omega(s^6), uniform charging K, full R3, strict ASET upper and Branch A/B remain **OPEN**. Do not treat spectral decomposition alone as a positive obstruction.

---

## Comment 106 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6123217179
- GitHub comment ID: 6123217179

### HYP-105 E1-K3-G2-O — exact ALL-a H3 physical triple orbits and genuine GQ ORIGINAL 4x5 coupling (new Draft #388)

Created stacked [Draft PR #388](https://github.com/definitely-stable/Mathlab/pull/388) on [Draft #387](https://github.com/definitely-stable/Mathlab/pull/387), pinned parent HEAD `6ddf54f6e48914b948c0331a358bc759487d5dce`. Parent N **3/3 exact-head CI SUCCESS**: [Contract #38239673644](https://github.com/definitely-stable/Mathlab/actions/runs/38239673644), [INDEX #38239673565](https://github.com/definitely-stable/Mathlab/actions/runs/38239673565), [Research #38239673567](https://github.com/definitely-stable/Mathlab/actions/runs/38239673567). Keep all Draft until independent mathematical review, do not modify main.

**ALL-a third-Johnson harmonic physical theorem O1.** For K=C(a,2), physical T_a 70*C(a,6) six-edge twofactors, p=|T|/C(K,6), and all a>=6, third rank h3(A) on 3 physical pair-edge labels is exactly `[c3(A)-p*C(K-3,3)-C(K-5,3)*sum_{B subset A,|B|=2}h2(B)]/C(K-6,3)`. Physical A falls into five orbits triangle,P4,star,P3+edge,3-matching with independently established physical triple codegrees `[C(a-3,3),2*C(a-4,2),0,5*C(a-5,1),8]`. At a=6 the five coefficients are `[57/4004,-25/6006,1/429,5/4004,20/3003]`, E3=`710/1001`, E4+E5+E6=`4966/77`. Entire 5005-case physical K6 H3 projector independently exact; K6 and K9 triple target codegrees independently brute checked.

**ALL-h ORIGINAL-GQ source structural restriction O2.** Original W(3,s) line-intersection SRG parameters are the **classical** `(V=(s+1)(s²+1),k=s(s+1),lambda=s-1,mu=s+1)` with exact original line triple populations r=0,1,2,3. W32 `[80,180,180,15]`, W34 `[43520,40800,13600,850]` fully brute checked on original incidence. More importantly the actual B-left SIX-distinct-ORIGINAL-right-line sixsource weight obeys for ALL legal f/h: `0<=w_f(R)<=(s+1)^4 * e_GQ(R)`, where e_GQ(R) is number of meeting ORIGINAL line pairs among R (unique repeated original left point/cherry). Six pairwise skew original lines necessarily have source weight zero; pointwise improves coarse `15(s+1)^4` C0 cap but cannot give positive target overlap by itself.

**Exact genuine coupled 4x5 tensor O3.** For each original coherent global f,g define integer `M_{r,o}` summing *true* w_f(R) over original sixsets and triples Q with r meeting ORIGINAL right-line pairs and o actual physical shape of g(Q). Exact `sum M=20 sum w_f`, `C3=sum M_{r,o} h3(o)`, independently equal to `C(K-6,3)*sum_{A triple}h3_source(A)h3_target(A)` computed from true zero-padded rank0/1/2/3 source marginals, and separately to N entire seven-rank spectrum. True original/dual source h3 down-kernels pass. Exact remaining ranks 4–6 satisfy CS but the simple bound is NOT sufficient to close P2.

**First hosted O Contract [#38241438573](https://github.com/definitely-stable/Mathlab/actions/runs/38241438573) SUCCESS:** 6 independent tests; full original/dual B0/C0 for 2 true globally coherent W32 maps; 4 exact 4x5 integer tensors. On the same M hardest map: `U_BA=36,U_AB=39,S_seven=86,mu_f=9968/143,P2 margin=757/143`. ORIGINAL B/A: `C3=2192/1001`, `C456=-541/385`, source mass 4984, 4 tensor row sums `[16678,39188,40502,3312]`. TRUE GQ dual A/B: `C3=-1211/858`, `C456=17/6`, source mass 5302, row sums `[18175,41797,42593,3475]`. Plain cherry weight cap is numerically loose (max ratios `2/135` B/A, `4/243` dual). Only ~1.09% of ranks 3–6 **physical target squared energy** is in rank 3; ~98.91% remains at ranks 4–6. This is NOT a proof of arbitrary-label all-h compensation.

**Final O HEAD** `f5d61705bfae3c02e847952e9736a40b29da17f6` after regression seals. Hosted final-head [Contract #38241770114](https://github.com/definitely-stable/Mathlab/actions/runs/38241770114) **SUCCESS** (all unit/complete original+dual checks) and [INDEX #38241770142](https://github.com/definitely-stable/Mathlab/actions/runs/38241770142) **SUCCESS**; full [Research #38241770156](https://github.com/definitely-stable/Mathlab/actions/runs/38241770156) **PENDING** at inspection. Root #230/#176/#169 OPEN. Keep child/parents Draft pending Research exact HEAD and independent mathematical review; no merges/main changes.

**Next K3-G2-P:** derive an actual GQ projection-fiber *FEASIBLE joint tensor* inequality and signed coercive source bounds on ranks 4–6, or a valid infinite global f,g adversary. Do not mistake a spectrum identity, a weak pointwise cherry cap, or observed finite positivity for a universal P2/P7/S=Omega(s^6) proof.

---

## Comment 107 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6123510123
- GitHub comment ID: 6123510123

### HYP-105 E1-K3-G2-P — all-a exact Johnson H4, all-h GQ diamond exclusion, and negative C5+C6 witness

Created [stacked Draft PR #389](https://github.com/definitely-stable/Mathlab/pull/389) over [Draft #388](https://github.com/definitely-stable/Mathlab/pull/388), pinned parent HEAD `f5d61705bfae3c02e847952e9736a40b29da17f6`. Parent #388 **exact-head Contract/INDEX/Research SUCCESS**: [#38241770114](https://github.com/definitely-stable/Mathlab/actions/runs/38241770114), [#38241770142](https://github.com/definitely-stable/Mathlab/actions/runs/38241770142), [#38241770156](https://github.com/definitely-stable/Mathlab/actions/runs/38241770156). All remain Draft pending independent mathematical review; no main merge; #230/#176/#169 OPEN.

**ALL-a exact theorem P1 (physical target Johnson H4).** The 70*C(a,6) genuine physical simple six-edge 2factors admit exactly **11** unlabeled four-edge subgraph orbits, with true orbit populations (a)_v/Aut and real four-target codegrees c4,a(F)=c4,K6(F)*C(a-v,6-v) if v<=6 (zero otherwise). The unique fourth harmonic coefficient is exactly
```
h4(F)=[c4,a(F)-p*C(K-4,2)-C(K-6,2)*sum_{|B|=2,B⊂F}h2(B)-C(K-7,2)*sum_{|A|=3,A⊂F}h3(A)]/C(K-8,2)
```
for K=C(a,2), p=70*C(a,6)/C(K,6). Complete eleven-orbit and automorphism classification checks ALL 20,475 K8 four-edge source templates, orbit population counts, ALL 5005 physical K6 6sets against N's **independent exact Johnson rank-four projector**, and all K6/K9 4-subset physical target codegrees. Exact target energies: a=6 `E4=86/7,E5+E6=4020/77`; a=9 `E4=1436/11,E5+E6=5087680/899`; a=14 `E4=3853077228/2487593,E5+E6=15007591521780/72140197`. This is an exact application of known Johnson harmonic/inclusion theory; no claimed general novelty of the mathematical method.

**ALL-h ORIGINAL GQ restriction P2-GQ (not the P2 conjecture).** In any original generalized quadrangle W(3,s), every three pairwise meeting original lines are concurrent; therefore NO four original lines can induce `K4-e` (diamond) in the original line-intersection graph, for ANY s and ANY whole global f,g injection. Every original clique lies in a pencil of <=s+1 lines; W32 forbids K4, W34 permits concurrent K4 but NEVER a diamond. This is classical GQ geometry, but a genuinely enforced zero row in the new accepted original sixsource coupling tensor.

**New joint TRUE ORIGINAL/physical 11×11 fourth-rank tensor:** `N_{u,v}=sum_{R actual right-6set} w_f(R)*sum_{Q subset R,|Q|=4}1[original induced 4-line intersection type u]1[physical g(Q) graphlet type v]`. Exactly `sum N=15*sum_R w_f(R)`, `N_{diamond,*}=0` for ALL h and `N_{K4,*}=0` if s=2, and rank4 `C4=sum N_{u,v}h4(v)`. Three separate original-source cross-checks: integer coupling tensor; N's entire exact K6 5005-set full Johnson projection; new independent SOURCE 0/1/2/3/4 physical-marginal inversion with explicit full K_a alphabet and correct V<K zero-padding. Source high-rank energy exact; `C56²<=E_W56*E_T56` verified. Both real original B/A and **genuine transposed ORIGINAL GQ dual** A/B independently complete B0/C0-checked on two real global W32 maps (four tensors).

**Hosted regression:** First [#38243351733](https://github.com/definitely-stable/Mathlab/actions/runs/38243351733) failed a **test-only Counter key inclusion check**: four-edge graphlet orbits requiring 7/8 physical coordinates are necessarily absent at a=6 and must have zero populations. Corrected without altering the theorem; [Contract #38243491054](https://github.com/definitely-stable/Mathlab/actions/runs/38243491054) SUCCESS (6 independent tests + two full original/dual model reports). On the SAME previously verified hard original W32 labeling, `U_BA=36,U_AB=39,S=86,mu_f=9968/143,P2 margin=757/143`, but **original B/A C4=129/35,C5+C6=-56/11**; **TRUE original dual A/B C4=143/21,C5+C6=-167/42**. This is a rigorous **finite NO-GO for any candidate claiming rank5+6 signed residue is termwise nonnegative** on all original GQ coherent global f,g; NOT a counterexample to P2, P7, Branch A/B or S=Omega(s^6). Source exact residual E56 original 2285873/1386, dual 37570/21; ordinary CS is far too loose.

**Final child HEAD** `805e1145ff40287ed7759c27dc4126eb7eb6cd20`, after pinned regression and `docs/CURRENT_STATE.md` update. Final-head dedicated [Contract #38243804114](https://github.com/definitely-stable/Mathlab/actions/runs/38243804114) **SUCCESS**, [INDEX #38243804072](https://github.com/definitely-stable/Mathlab/actions/runs/38243804072) **SUCCESS**; full [Research #38243804052](https://github.com/definitely-stable/Mathlab/actions/runs/38243804052) **IN PROGRESS** when inspected. Do NOT accept exact-head 3/3 before Research succeeds; keep stacked Draft pending independent mathematical proof review. Main untouched; root issues OPEN.

**Next K3-G2-Q:** must exploit feasible original-GQ *fifth/sixth-order* incidence/physical couplings or joint ORIGINAL+DUAL signed compensation, rather than incorrectly assume C56>=0. Current verified outcome: `OPEN_WITH_FORMAL_BLOCKER`, no uniform all-h P2/P7, charge K, full GF5 R3 or ASET exponent.

---

## Comment 108 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6123853465
- GitHub comment ID: 6123853465

### HYP-105 E1-K3-G2-Q — ALL-h original GQ girth-eight 4x4 permanent and exact anchored C4 source reconstruction

Implemented [stacked Draft PR #390](https://github.com/definitely-stable/Mathlab/pull/390) on [Draft #389](https://github.com/definitely-stable/Mathlab/pull/389), pinned parent final HEAD `805e1145ff40287ed7759c27dc4126eb7eb6cd20`. Parent **Contract/INDEX/full Research all SUCCESS at exact HEAD** ([#38243804114](https://github.com/definitely-stable/Mathlab/actions/runs/38243804114), [#38243804072](https://github.com/definitely-stable/Mathlab/actions/runs/38243804072), [#38243804052](https://github.com/definitely-stable/Mathlab/actions/runs/38243804052)), independent mathematical proof review still needed. No merges; main unchanged; root #230/#176/#169 OPEN.

**NEW exact ALL-h ORIGINAL sixsource identity.** A true B-left source six-incidence support with SIX DISTINCT original right line endpoints R has one unique twice-used original point p on an intersecting anchor pair of right lines; its other four distinct ORIGINAL left point pair-labels must form a SIMPLE PHYSICAL C4 on four coordinates disjoint from f(p). For every meeting original line-pair B⊂R with unique shared p, and every available original-left square point set Q, the number of ways to assign the other 4 ORIGINAL right lines to Q is exactly the permanent of the 4x4 ORIGINAL GQ incidence matrix A(R\B,Q). Thus for any legal f and ALL h, w_f(R)=sum_{anchor B,Q} perm(A(R\B,Q)), with TRUE distinct original six-incidence supports, no duplicated physical event counts or 6! factor. Holds separately for genuine original GQ dual A/B after transpose and whole physical map exchange.

**NEW sharp girth8 source restriction.** Because the actual original GQ bipartite incidence graph has NO C4 or C6, any 4x4 original sub-incidence matrix has permanent ≤2: two different matchings must differ on one 8-cycle using all vertices; a third would require two odd 4-cycle permutations with an even relative permutation, contradicting the required odd 4-cycle relation. A simple C8 achieves 2, sharp. Independent complete 65536 binary 4x4 matrix census: 16217 valid with no C4/C6, permanent histogram {0:11321,1:4824,2:72}; NONE >2. With ≤3*C(a-2,4) physically available C4 squares per anchor p, ALL h exact true-GQ source bound `w_f(R) <= min((s+1)^4,6*C(a-2,4))*e_GQ(R)`. At W32/K6 this sharpens the previous **81 e_GQ(R) to 6 e_GQ(R)** (13.5x coefficient reduction); for W34/K14 the previous 625 remains better than new coarse 2970, so do NOT infer any all-h exponent gain.

**Full hosted genuine ORIGINAL and DUAL sixsource oracles.** First [Contract #38245954264](https://github.com/definitely-stable/Mathlab/actions/runs/38245954264) **SUCCESS**: six independent tests, then four true original/dual 5005-original-sixline source ledgers for two actual coherent W32 models; EVERY one of 96525 local 4x4 anchor-square matrices/source ledger independently checked against existing full C0 sixth-order original-incidence enumerator, and both independently full B0 original/dual seven GF5 positives. For lex B/A: source 5000, n1=4976,n2=12 (weights 4976+24); lex dual A/B: 5793, n1=5765,n2=14; M-hard B/A: 4984,n1=4958,n2=13; M-hard dual A/B: 5302,n1=5296,n2=3. Strict complete local permanent histograms pinned in Contract, not extrapolated to all maps.

**Exact signed high-order 5/6 coupling to local original matchings:** The same actual legal coherent physical labeling gives
```
lex B/A:               C56_perm1=-145/308, C56_perm2=13/231, sum=-383/924.
lex actual GQ dual A/B: C56_perm1=628/231,  C56_perm2=226/231, sum=122/33.
M-hard B/A:            C56_perm1=-3097/462,C56_perm2=745/462, sum=-56/11.
M-hard actual dual A/B:C56_perm1=-1937/462,C56_perm2=50/231, sum=-167/42.
```
M-hard still has true U_BA=36,U_AB=39,S_seven=86,mu_f=9968/143, P2 margin=757/143>0. This exact source-matching decomposition newly identifies that the negative rank5/6 residual for the hardest map comes primarily from **one-perfect-matching ORIGINAL incidence witnesses**, not rare local double-counting. The theorem `C56_negative_only_due_to_perm2` is therefore INVALID even on W32; P2/P7 are NOT refuted.

**Final child HEAD:** `d26574cd26fc247f874bdeb95cbf79270fe0dff3`, after hosted numeric/seal and docs/CURRENT_STATE updates. [Final-head Contract #38246230558](https://github.com/definitely-stable/Mathlab/actions/runs/38246230558) **SUCCESS**, [INDEX #38246230563](https://github.com/definitely-stable/Mathlab/actions/runs/38246230563) **SUCCESS**; [Research #38246230564](https://github.com/definitely-stable/Mathlab/actions/runs/38246230564) **IN PROGRESS** at last inspection, so 3/3 acceptance cannot be claimed yet. Keep stacked Draft pending exact-head Research and independent mathematics review; no merge/main change.

**Next K3-G2-R:** use the genuine *joint* ORIGINAL and GQ-dual 4x4 Hall/permanent geometry to bound negative signed fifth/sixth-rank **permanent-one** witnesses by positive physical two-factor completions. Search for an all-h source-origin charging or real coherent counterexample; do not simply bound total hypergraph mass or assume C56>=0. Universal P2, P7, S=Omega(s^6), all-h charging K, full R3 and strict ASET exponent remain OPEN.

---

## Comment 109 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6124280868
- GitHub comment ID: 6124280868

### HYP-105 E1-K3-G2-R — complete all-a physical target Johnson ranks 0–6, unique five-edge two-factor completion and true GQ-dual signed rank5/rank6 NO-GO

New stacked [Draft PR #391](https://github.com/definitely-stable/Mathlab/pull/391) on [Draft #390](https://github.com/definitely-stable/Mathlab/pull/390), pinned parent `d26574cd26fc247f874bdeb95cbf79270fe0dff3`. Parent Q exact-head Contract/INDEX/Research **ALL SUCCESS** ([#38246230558](https://github.com/definitely-stable/Mathlab/actions/runs/38246230558), [#38246230563](https://github.com/definitely-stable/Mathlab/actions/runs/38246230563), [#38246230564](https://github.com/definitely-stable/Mathlab/actions/runs/38246230564)). Parent and child stay Draft until independent mathematical proof review, no main merges or changes, root #230/#176/#169 OPEN.

**ALL-a theorem R1 (physical target):** A set of five distinct edges of K_a (a>=6) has exactly ONE completion into a genuine 6-edge simple 2-factor spanning exactly six physical coordinates iff it is the path P6, or disjoint union C3+P3. Every other five-edge graph has ZERO such completions. This follows by deleting one edge from each type of six-edge 2-factor, either 60 six-cycles or 10 unordered pairs of triangles on each choice of six coordinates. Independently enumerated actual complete physical K6 and K9 target 5-edge codegrees; ALL 3003 physical K6 five-edge subsets also compared directly.

**ALL-a theorem R2 (full exact physical Johnson target spectrum):** For K=C(a,2), p=70*C(a,6)/C(K,6), and exact prior physical H2,H3,H4 lifted coefficients evaluated on a physical five-edge set F, its unique fifth Johnson harmonic is
```
h5(F) = [c5(F)-p*(K-5)-(K-7)*H2(F)-(K-8)*H3(F)-(K-9)*H4(F)]/(K-10).
```
Rank-five target E5 is given by evaluating *only two actual physical representative graphs*:
```
E5(a)=C(a,6)*(360*h5(P6)+60*h5(C3+P3)).
E6(a)=70*C(a,6)-E0(a)-E2(a)-E3(a)-E4(a)-E5(a).
```
Hence target ranks **0,1,2,3,4,5,6** admit exact all-a formulas without enumerating J(C(a,2),6). At a=6 exact full squared spectrum [140/143,0,42/11,710/1001,86/7,1182/77,258/7] and coefficients h5(P6)=18/385, h5(C3+P3)=-19/770. At a=9 energies [102900/5797,0,0,35712/493,1436/11,273240/377,1988600/403]. At a=14 energies [7357350/110983,0,2102100/21199,1682278884/3641791,3853077228/2487593,3749500040/368271,260563803500/1316961]. The independent N complete rational 5005-sixset Johnson projection agrees on **EVERY** physical K6 rank5 and rank6 value, not only energies. This is exact physical target design analysis; NOT a source-specific positive lower bound.

**NEW negative TRUE JOINT ORIGINAL+DUAL signed witness on SAME valid W32 f,g:** The two genuine GQ source weights are reconstructed from separate original and transposed Q local anchor 4x4 incidence permanent 1/2 ledgers (all actual 5005 original right-sixsets each). The signed fifth and sixth target contributions were each split into a 2x2 rational matrix: permanent-one versus permanent-two source multiplicities, crossed with target rank5 versus rank6. For hard actual coherent W32 original labels:
```
ORIGINAL B/A: C5=-260/77, C6=-12/7, C56=-56/11
TRUE GQ DUAL A/B: C5=-83/42, C6=-2, C56=-167/42
JOINT SOURCE FIFTH: C5_BA+C5_AB=-2473/462 < 0
JOINT SOURCE SIXTH: C6_BA+C6_AB=-26/7 < 0
JOINT C56=-4189/462 < 0
```
Hard original local 2x2 [rows perm1,perm2; cols rank5,rank6] is [[-8951/2310,-99/35],[1151/2310,39/35]]; true dual is [[-1703/770,-208/105],[272/1155,-2/105]]. Signed negative rank5 mainly comes from genuine ORIGINAL unique-permanent witnesses, not only exceptional perm-two multiplicity. This is an exact finite NO-GO for BOTH attempted all-f,g uniform inequalities joint C5>=0 and joint C6>=0, but NOT a P2 counterexample: U_BA=36,U_AB=39,S_seven=86,mu_f=9968/143, margin=757/143>0.

**Hosted evidence:** The initial dedicated R Contract failed a **test-only** noncanonical physical edge (4,0) negative-example input. It was corrected to canonical (0,4) with no theorem/code change. Corrected [Contract #38248723614](https://github.com/definitely-stable/Mathlab/actions/runs/38248723614) **SUCCESS** (5 unit tests plus two full original/dual source reports). Regression sealed all-a E0..E6 and true original+dual negative C5/C6 exact values in dedicated Contract. Final child HEAD `cc20469da6eddaf576287ca2ad7243bb32b248c2`: exact-head [INDEX #38249084848](https://github.com/definitely-stable/Mathlab/actions/runs/38249084848) **SUCCESS**; [Contract #38249084763](https://github.com/definitely-stable/Mathlab/actions/runs/38249084763) and [full Research #38249084771](https://github.com/definitely-stable/Mathlab/actions/runs/38249084771) were **IN PROGRESS** at last check. Do not claim 3/3 acceptance before green exact final head + independent mathematics review. Keep Draft, main unchanged.

**Next K3-G2-S:** A genuinely ORIGINAL+DUAL nonnegative geometric Hall/charging analysis must explicitly include LOW harmonic or accepted other-five-family positive targets and condition on shared original GQ incidences. Merely hoping H5 or H6 is separately nonnegative fails even under true duality. P2, P7, all-h S=Omega(s^6), charging K, full R3 and strict ASET exponent remain OPEN.

---

## Comment 110 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6124653866
- GitHub comment ID: 6124653866

### HYP-105 E1-K3-G2-S — true original/dual incidence-Hall charging: exact finite NO-GO for one-hop model

Created [stacked Draft PR #392](https://github.com/definitely-stable/Mathlab/pull/392) over Draft #391 final parent HEAD cc20469da6eddaf576287ca2ad7243bb32b248c2 (parent R Contract/INDEX/Research 3/3 exact-head SUCCESS). Child exact HEAD 6b7aafaf6131074fe9d14b998e467ecedefb3f16; main untouched; no merges. [New specialized hosted Contract #38251368999](https://github.com/definitely-stable/Mathlab/actions/runs/38251368999) **SUCCESS**, [INDEX #38251368979](https://github.com/definitely-stable/Mathlab/actions/runs/38251368979) SUCCESS; full [Research #38251368998](https://github.com/definitely-stable/Mathlab/actions/runs/38251368998) initially in progress. Independent mathematical review pending.

**Exact all-h SUFFICIENT charging model, not an established universal bound:** each ORIGINAL B/A permanent support belongs to a unique original repeated point p. Demand at p is rho_a*M_p. Positive original B/A target credits A_p usable only at SAME p; genuine transposed original dual A/B target credits B_l usable only if (p,l) belongs to the ORIGINAL GQ incidence. Each source and dual credit can be spent at most once. Max-flow feasibility iff every original point subset X satisfies rho_a*sum_{p in X}M_p <= sum_{p in X}A_p+sum_{l in N_GQ(X)}B_l. Summing X=P would imply P2, but the converse fails: this model is strictly stronger than P2.

**Actual complete W32 certificate:** independent genuine original/dual 4x4 GQ permanent-1/2 anchor reconstructions, complete 5005 original source sixsets per side, pinned original B0/C0 seven-family totals, and exact Johnson rank0..6 conservation. For both lex and existing hardest-M SAME coherent global f,g, integer max-flow/min-cut agrees with independent exhaustive **ALL 32768 Hall cuts**.

- lex: maxflow=10000=scaled demand, Hall deficit=0; exact scalar P2 margin=19744/143.
- hardest-M: source mass=4984; true BA target=36, true original-dual AB target=39; P2 margin=757/143>0. But subset **X={1,2,3,5,8,13,14}** needs demand=4820, has own BA capacity=1144 and genuine incident dual AB capacity=3146, and therefore fails by **530/143**. Maxflow=9438 < demand=9968. Independent exhaustive Hall maximum deficit also exactly 530 scaled integer units. Genuine same-map joint C5=-2473/462<0 and C6=-26/7<0 retained.

**Decision:** one-hop GQ-local original+dual Hall charging is FALSIFIED on one legal coherent W32 map. This is **NOT** a counterexample to scalar P2, seven-family P7, all-h Branch A/B, strict R3, or ASET. The target spectrum need not be recomputed. Next K3-G2-T: test minimal geometrically justified two-hop point-credit/alternating-path transport with explicit intermediate capacity and compare complete Hall cuts; do NOT create unrestricted 3-hop point-to-line edges without congestion, since the GQ projection axiom makes them complete. Root #230/#176/#169 remain OPEN; all stacked PRs Draft; no main changes.

---

## Comment 111 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6125082847
- GitHub comment ID: 6125082847

### HYP-105 E1-K3-G2-T — exact bounded ORIGINAL GQ point-line-point relay: sharp finite threshold

Created [stacked Draft PR #393](https://github.com/definitely-stable/Mathlab/pull/393) directly on S Draft #392, pinned accepted parent HEAD `6b7aafaf6131074fe9d14b998e467ecedefb3f16` (parent Contract/INDEX/full Research exact-head 3/3 SUCCESS). T final tested HEAD `80e959f79663af1a2540975338e6fb0c940b6f47`. Main unchanged, no merges; #230/#176/#169 remain OPEN and independent mathematical review outstanding.

**New ALL-h conditional exact flow/mincut reduction, not all-h positivity:** B/A demand at true original repeated point p is rho_a*M_p. Consumable original B/A physical target credit A_q can be used on own p or via ORIGINAL collinear route p--l--q, with ONE SHARED bounded-capacity gate kappa_l per intermediate original GQ line. Genuine ORIGINAL-dual A/B physical credit B_l remains directly consumable by points incident to original line l. Neither B/A nor A/B positive capacity may be spent twice. Flow is feasible iff EVERY original point set U and activated relay-line set J subset N_GQ(U) satisfies
```
rho_a*M(U) <= A(U union P(J)) + B(N_GQ(U)) + kappa(N_GQ(U)\J).
```
The model is strictly sufficient for P2; no universal kappa is derived. At zero relay it is exactly S's one-hop Hall gate (rechecked against independently exhausted ALL 32768 W32 ordinary Hall subsets).

**Exact finite ORIGINAL+DUAL W32 on two SAME coherent global f,g:** [hosted first corrected Contract #38253966400](https://github.com/definitely-stable/Mathlab/actions/runs/38253966400) SUCCESS. Independent Dinic and distinct Edmonds–Karp max-flows, all-node integer conservation, actual typed GQ mincut, sharp uniform kappa binary search and independent witness were sealed. Lex original needs kappa=0. The true correlated hardest-M original needs **EXACT MINIMUM integer-scaled per-original-line relay capacity kappa=59**, namely **59/143 physical target-credit units**. A budget one whole target-hit-equivalent per line (kappa=143) suffices for this state; independently certified flow 9968/9968 and deficit 0.

**New independent SHARP lower cut for hardest-M:** original points U={1,2,3,5,8,13,14}; N(U)={0,1,3,4,5,6,7,8,10,11,12,13}; activated outputs J={3,11,13}, leaving exactly 9 capped relay lines. TRUE original/dual sixsource counts give D(U)=4820, own/expanded BA credit A(U union P(J))=1144, neighboring dual AB credit B(N(U))=3146, all scaled by 143. Hence `9*kappa >= 530`, i.e. `kappa >= ceil(530/9)=59`. At kappa=58 there is an exact deficit 8 and maxflow 9960/9968; at kappa=59 the full exact maxflow is 9968/9968. This proves **finite auxiliary-model iff kappa>=59**, not P2.

Final specialized [Contract #38254475697](https://github.com/definitely-stable/Mathlab/actions/runs/38254475697) SUCCESS and [INDEX #38254475396](https://github.com/definitely-stable/Mathlab/actions/runs/38254475396) SUCCESS at final frozen HEAD; full [Research #38254475395](https://github.com/definitely-stable/Mathlab/actions/runs/38254475395) pending final check. Dedicated code, 7 falsifier tests, hosted frozen exact nine-gate regression, standalone math docs and index in PR #393. No merges/main changes.

**Scope:** No universal P2/P7, Branch A/B, s^6 lower bound, strict R3 extraction or ASET exponent. The artificial kappa=1 budget was NOT derived from genuine GQ source witness identities. Next K3-G2-U must derive/falsify a *geometrically justified*, instance-independent bound on original relay-line congestion (preferably actual support-based), test other coherent W32 witnesses, and then attempt a true all-h bounded-capacity Hall theorem. Do not interpret just two W32 examples as an all-h proof.

---

## Comment 112 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6127406457
- GitHub comment ID: 6127406457

### HYP-105 #230: точное опровержение универсальных P2/P7 — отдельный Draft PR #394

Создан [PR #394](https://github.com/definitely-stable/Mathlab/pull/394) от main `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`, без зависимости от unmerged научных стеков. Exact HEAD: `4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e`. Main не изменён, issue #230/#176/#169 остаются OPEN.

**Исправление математического gate:** ранее опубликованный корректный глобальный S68-пример из [C24-B6](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107741776), в сочетании с его источником из [B8-C](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109316505), уже опровергает усиления `P2: U_BA+U_AB>=mu_f` и `P7: S>=mu_f` для всех h>=1. Сам witness не объявляется новым.

На ОДНИХ исходных глобальных f,g:
```
f=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8)
g=(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)
seven=(0,44,21,0,0,2,1), S=68, Q4=9
H_f=6098, true dual H_g=4740, rho_6=2/143
mu_f=12196/143
P2 margin=65-mu_f=-2901/143
P7 margin=68-mu_f=-2472/143
```
Все ORIGINAL unordered six-incidence sets независимо реконструированы тремя способами: физические A/B/C lifts; исходные 4x4 permanents с настоящим dual; прямой C++ перебор ВСЕХ 8,145,060 шестёрок. SAME-map full-51 checksum4 GF5 necessary floor: `3112510/51^6`; Q4 R2 floor: `4779/51^4`. Это не полные R2/R3.

**Следствие для S/T transport:** глобальный cut требует 12196 scaled demand, тогда как BA+AB unit credits всего 9295. Никакие relay capacities, включая неограниченные, не исправят дефицит 2901. Даже все семь единичных credits дают 9724 и дефицит 2472. Это опровержение demand=mu_f/unit-credit протокола, а не всех иных weighted/asymptotic вариантов. Порог 59/143 в PR #393 остаётся верным для другого проверенного экземпляра.

[Подробный русский разбор](https://github.com/definitely-stable/Mathlab/blob/4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e/docs/research/HYP-105-ISSUE230-PROOF-AUDIT.ru.md), [frozen exact calculations](https://github.com/definitely-stable/Mathlab/blob/4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e/research/issue230-proof-audit.json). Локально: полный suite 1018 tests PASS, финальные targeted 13 PASS, независимый mathematical/code review без critical/important замечаний. Exact-head hosted Contract/INDEX/full Research пока отслеживаются; старые CI не считаются новым принятием.

**Scope:** конечное опровержение P2/P7 не является infinite COUNTEREXAMPLE_B и не опровергает исходную асимптотическую S=Omega(s^6) с меньшей константой/large h. Branch A/B остаются OPEN; никаких ASET exponent или merger claims.

---

## Comment 113 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6127418733
- GitHub comment ID: 6127418733

### HYP-105 #230: ALL-h quartic source theorem — sharp Delta² cap and Omega(s¹³) support

Продолжение в отдельном [Draft PR #394](https://github.com/definitely-stable/Mathlab/pull/394), HEAD `4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e`. **RESTRICTED_THEOREM_C**, исходный all-f,g target gate остаётся OPEN.

Для шести DISTINCT ORIGINAL правых прямых R источник w_f(R) разлагается по уникальной исходной concurrent anchor pair B и её точке p. Четыре остальные прямые дают физические adjacency matrices A1..A4 на координатах вне f(p). Точный source count — сумма distinct-vertex quartic traces по трём unoriented cyclic orders. Каждая ORIGINAL шестёрка считается ровно ОДИН раз, без orientation/4! множителей; повторные исходные точки устраняются selector/collision subtraction.

**Теорема для ВСЕХ s=2^h и ВСЕХ допустимых глобальных f:**
```
w_f(R) <= min(Delta^4,12*Delta^2,6*C(a-2,4))*e_GQ(R)
Delta=s+1
|support w_f| >= (1/720+o(1))*s^13, uniformly in f
```
Доказательство нового Delta² cap: каждая A_i содержит <=Delta рёбер, значит Frobenius norm squared <=2Delta. Каждый unrestricted trace <=product of four Frobenius norms <=4Delta². Три cyclic orders дают <=12Delta² на anchor; e_GQ(R) anchors дают указанную оценку. Затем H_f=(1/4+O(1/s))*s^15 и e_GQ(R)<=15 дают uniform source support Omega(s13), улучшая прежний Omega(s11).

**Точная степень и pointwise NO-GO, математически для каждого s>=8:** выбрать anchor pair и четыре прямые, skew ко всем другим выбранным, и продолжить частичную f в глобальную инъекцию минимального K_a. Назначения {u,b_i},{v,b_i},{v,c_j},{u,c_j} дают ровно Delta² source witnesses при e_GQ(R)=1. Другая глобальная f, назначающая все residual points парам, встречающим f(p), даёт w_f(R)=0 при том же e_GQ(R)=1. Поэтому степень2 точна, но положительная pointwise нижняя граница из concurrence alone ложна.

Независимые настоящие W34/W38 глобальные fixtures:
```
s=4: R={0,1,22,27,32,38}, e_GQ=1, sharp w=25, zero w=0
s=8: R={0,1,74,83,92,101}, e_GQ=1, sharp w=81, zero w=0
```
Точный quartic ledger на ВСЕХ 5005 W32 ORIGINAL right sixsets совпадает с независимым original six-incidence generator; genuine source geometry проходит regularity, partial linearity и unique GQ projection axiom. Explicit executable budgets fail closed.

Также записаны полные аналитические доказательства:
- forall fixed f, uniform global random g: E_g U_BA >=[180054835200/13841287201]*s6 >13*s6 для s>=8; не forall g;
- для всех s>=32 обычный unfiltered centered Cauchy даёт отрицательную нижнюю границу; error/mean >=(1-o(1))*s5/sqrt8400, с точными ненормированными l2 norms и zero padding.

[Полное доказательство и точная quartic identity](https://github.com/definitely-stable/Mathlab/blob/4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e/docs/research/HYP-105-ISSUE230-QUARTIC-SOURCE.md), [implementation](https://github.com/definitely-stable/Mathlab/blob/4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e/research/hyp105_issue230_proof_audit.py), [independent falsifiers](https://github.com/definitely-stable/Mathlab/blob/4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e/research/test_hyp105_issue230_proof_audit.py). Mathematical/code review подтвердил multiplicities, constants, sharpness и zero construction. Exact-head hosted acceptance отдельно ожидается.

**Оставшийся substantive blocker:** SOURCE upper/spread и positive random mean не обеспечивают lower intersection с произвольной коррелированной g. Для Branch A требуется настоящее sixth-order joint target acceptance всех семи семейств; для B — infinite coherent family с TOTAL S=o(s6). Ни одно не объявляется доказанным; no strict full R3/ASET exponent.

---

## Comment 114 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6127566725
- GitHub comment ID: 6127566725

### PR #394 — exact-head hosted acceptance SUCCESS

На неизменном HEAD `4263fa8a4f2e3c13703045eb5a3fce7eebe2c78e` подтверждены все три gates:
- [Dedicated proof-audit Contract #38270789280](https://github.com/definitely-stable/Mathlab/actions/runs/38270789280): **SUCCESS**, включая независимые source/permanent проверки, настоящие W34/W38 fixtures и полный C++ перебор 8,145,060 исходных шестёрок.
- [INDEX #38270789155](https://github.com/definitely-stable/Mathlab/actions/runs/38270789155): **SUCCESS**.
- [Полный Research #38270789237](https://github.com/definitely-stable/Mathlab/actions/runs/38270789237): **SUCCESS**, все четыре шарда и fail-closed `research-full-suite` агрегатор; новый квартческий report также SUCCESS.

Локально полный unittest suite дал1018 PASS; финальные13 targeted tests PASS. Mathematical/code review подтвердил multiplicities, реальные глобальные разметки, точные константы и области утверждений.

**Это принятие конечных артефактов и ограниченных аналитических результатов категории C, не доказательство исходной теоремы A.** Остался uniform lower на совместное six-incidence target acceptance для ВСЕХ коррелированных f,g; source cap и random mean его не заменяют. P2/P7 с единичным спросом mu_f опровергнуты. Branch A/B и #230/#176/#169 остаются OPEN. PR остаётся Draft, main не изменён; postmerge main Research здесь не выполнялся. No full-risk upper/ASET exponent/Lean claim.

---

## Comment 115 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6128359394
- GitHub comment ID: 6128359394

Продолжил именно математическое доказательство, без ожидания CI. В отдельный [PR #394](https://github.com/definitely-stable/Mathlab/pull/394), commit `aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d`, добавлены два проверенных универсальных шага.

**1. Для любых коррелированных глобальных f,g существует не меньше (16−o(1))s⁶ ориентированных физических трёхрёберных путей** с четырьмя различными координатами каждой стороны и существующими метками концов. Доказательство: согласованное удаление обеих диагоналей каждой исключаемой инцидентности, контроль координатных блоков и энтропия стационарного блуждания. Выбор случайной разметки не используется. Все o(1) равномерны по f,g.

Спектральная оценка исходного GQ усиливает массу пересекающихся физических пучков:
`M_f,M_g ≤ (s−1)V+(s²+1)(a−1)=O(s⁴)`.
Поэтому можно ограничить блок числом s^(1/10), потеряв o(m) рёбер и сохранив (16−o(1))s⁶ путей.

**2. Точное замыкание использует ORIGINAL геометрию.** Для неинцидентных концов (q,r) существует единственный q—l—p—r; это также тождество BBᵀB=2sB+J. Если f(p),g(l) не пересекают координаты физического пути, получаем учитываемую BB-overlap шестёрку. Кратность ровно **2**, а не4: две ориентации одного синхронизированного пути.

Полный [аналитический вывод и таблица](https://github.com/definitely-stable/Mathlab/blob/aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d/docs/research/HYP-105-ISSUE230-PROJECTION-CLOSURE.md), [точный oracle](https://github.com/definitely-stable/Mathlab/blob/aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d/research/hyp105_issue230_projection.py), [замороженные расчёты](https://github.com/definitely-stable/Mathlab/blob/aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d/research/issue230-projection-closure.json).

Точный контроль S68: 678 proper путей =72 инцидентных +606 блокированных; допустимых неинцидентных замыканий0. Это конечный пример необходимости контролировать потери, не контрпример асимптотической A. Полные случайные глобальные разметки W34/W38 дают соответственно8021/1512478 различных допустимых BB-overlap шестёрок. Проверены сами исходные шестёрки и кратность; эти таблицы не используются как доказательство минимума.

Основная универсальная теорема S=Omega(s⁶) пока **не объявляется доказанной**; ниже отдельно записан закрытый инцидентный случай и остающийся точный барьер.

---

## Comment 116 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6128372528
- GitHub comment ID: 6128372528

Закрыт **инцидентный случай** нового проекционного доказательства — при произвольных согласованных f,g и без предположения max degree=O(s).

Пусть G — полный граф физических диагоналей, H⊆G — сохранённый граф с не больше t соседями в каждом координатном блоке, P_inc — число ориентированных proper H-путей длины3, концы которых соединены ребром ПОЛНОГО G. Через пары общих соседств доказано:

`P_inc ≤24t·M2(G)+√(192m(G)·D6(H))`.

В построенных шестирёберных циклах различны все шесть координат **каждой** стороны; это именно accepted D6, не произвольные Kikuchi циклы. Число свидетелей на один цикл не больше24. Замыкающее ребро не обязано сохраняться в H.

Спектр ORIGINAL GQ даёт равномерно:
`M2(G) ≤8Δ²(a−1)²+16s(a−1)V ≤258s^(11/2)`.
Со спектральным block-pruning t=ceil(s^alpha), 0<alpha<1/2, ошибка есть o(s⁶), а почти все исходные инцидентности сохраняются. Поэтому
`P_inc ≥eta*s⁶ ⇒ D6(H) ≥(eta²/4608)*s⁸`
при достаточно большом s; явно достаточно s^(1/2−alpha)≥24768/eta. Полное [доказательство с кратностями и константами](https://github.com/definitely-stable/Mathlab/blob/aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d/docs/research/HYP-105-ISSUE230-INCIDENT-BOOK.md) прошло отдельную математическую проверку.

**Что осталось для основной A.** В спектрально очищенном графе обозначим через C число НЕинцидентных трёхрёберных путей, чей единственный исходный якорь q—l—p—r имеет f(p) или g(l), встречающую координаты пути. Из доказанных результатов следует:

`(16−o(1))*s⁶ ≤ C+2S+√(192mS),  m=2VΔ`.

Значит равномерная оценка C≤(16−eta)s⁶ с одной фиксированной eta>0 завершила бы A. Более сильная C=o(s⁶) дала бы S≥(8−o(1))s⁶. **Эти верхние оценки C пока не доказаны.** Подсчёт O(s⁵) плохих исходных пар не контролирует кратность путей; пересечение внутренних координат остаётся связанным условием двух разметок.

Таким образом математический прогресс в [PR #394](https://github.com/definitely-stable/Mathlab/pull/394) — универсальный путь (16−o(1))s⁶ и доказанная компенсация инцидентных замыканий. Статус исходной S=Omega(s⁶): **OPEN**, не подтверждается тестами или CI. Все17 локальных проверок проходят; расчёты и исходные шестёрки опубликованы.

---

## Comment 117 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6129048059
- GitHub comment ID: 6129048059

### HYP-105 #230 — D1: exact 16-atom original-GQ blocking and *weighted* endpoint congestion

Created [stacked Draft PR #395](https://github.com/definitely-stable/Mathlab/pull/395) above independent main-based #394, parent HEAD `aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d`, latest child HEAD `976c5e47ac51203370ec2e39105754b58cbadda0`. Main unchanged, no merges; root #230/#176/#169 OPEN. We explicitly STOPPED the previous K3-G2-U universal P2 charging: S68 disproved P2 and P7.

**All-h exact algebraic decomposition (not a universal lower bound):** For every proper endpoint-complete nonincident physical three-path in one coherent ORIGINAL W(3,s) labeling f,g, let (q,r) be its original endpoint pair and q-l-p-r its UNIQUE original GQ projection. Split projected anchor overlap into four bits: f(p) intersects endpoint first coordinates (LE), internal first coordinates (LI), g(l) endpoint second coordinates (RE), internal second coordinates (RI). The 16 disjoint atom counts sum to all nonincident paths. Zero atom gives original accepted synchronized BB-overlap original sixsets, each with multiplicity two by orientation. Blocked C=endpoint-only+internal-only+mixed EXACTLY.

**Exact ORIGINAL bad pair and congestion identity:** The set B_L of original (q,r) with f(p) intersecting f(q) has size `s*sum_{l,x}r_lx(r_lx-1)`, and true ORIGINAL dual B_R similarly has `s*sum_{p,y}t_py(t_py-1)`. Both have O(s^5) original PAIRS, but the physical blocked PATH mass is exactly `E=sum_{(q,r) in B_L union B_R}N_{qr}`. The remaining `J=C_internal_only` counts internal conflicts on otherwise endpoint-good original pairs. Thus **C=E+J**, with no assumption that N_{qr} is small. This is an exact all-h identity but **NOT** a proof of a useful all-h UPPER on C.

**Independent original GQ finite data, all paths complete, no sampling of paths:**

| same coherent f,g | blocked C | endpoint-only | internal-only | mixed | E endpoint path mass |
|--|--:|--:|--:|--:|--:|
| W32 S68 |606|52|62|492|544|
| W34 random|48542|18034|18348|12160|30194|
| W38 random|1888776|851208|869548|168020|1019228|

Also W38 has 70,174 bad ORIGINAL endpoint pairs among 336,960 original nonincident pairs; max 54 oriented physical paths on one bad original pair. ALL 16 masks independently cross-checked by forward physical three-path enumeration and endpair-first middle-edge enumeration for every W32/W34 fixture; W38 complete forward scan and parent baseline cross-check. It is logically incorrect to infer C=O(s^5) from counting O(s^5) bad pairs. W38 internal-only C=869,548 makes endpoint-only compensation insufficient as a standalone mechanism. The finite ledgers use FULL G; PR #394 all-h reservoir is on spectrally pruned H', so no finite all-h extrapolation is asserted.

**GitHub-hosted exact final HEAD checks:** [new D1 Contract #38282464928](https://github.com/definitely-stable/Mathlab/actions/runs/38282464928) SUCCESS, [INDEX #38282464882](https://github.com/definitely-stable/Mathlab/actions/runs/38282464882) SUCCESS, [parent proof-audit #38282464938](https://github.com/definitely-stable/Mathlab/actions/runs/38282464938) SUCCESS. [Full Research #38282464881](https://github.com/definitely-stable/Mathlab/actions/runs/38282464881) remained QUEUED at comment authoring; do not infer green prematurely. Independent mathematical review still outstanding.

**Next D2 substantive gate:** bound/compensate BOTH the endpoint-weighted relation E and internal-only tensor J simultaneously for ALL coherent f,g on spectrally pruned H', ideally `E+J <= (16-eta)s^6 + Lambda*S + o(s^6)` for absolute eta>0 and finite Lambda>=0. This would combine with parent (16-o(1))s^6 path reservoir and incident D6 book compensation to prove Branch A. This proposed bound is NOT established. No original all-h S>=c*s6, no infinite small-S family, no ASET exponent.

---

## Comment 118 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6129611802
- GitHub comment ID: 6129611802

### HYP-105 issue #230 — D2: exact ORIGINAL bad-endpoint mixed-book tensor; unrestricted certificate VACUOUS

Created [stacked Draft PR #396](https://github.com/definitely-stable/Mathlab/pull/396) directly above [D1 Draft #395](https://github.com/definitely-stable/Mathlab/pull/395), parent exact HEAD `976c5e47ac51203370ec2e39105754b58cbadda0` with D1 Contract/INDEX/Proof Audit/full Research 4/4 SUCCESS. New child exact final HEAD `bc4e679d1d1a589d073856e90458e715eaef080c`; main untouched; no merge or closure of #230/#176/#169. Earlier universal P2/P7 **FALSIFIED** by genuine S68 (not resurrected).

**Exact ALL-h mathematical reduction, NOT an all-h positivity result:** For each nonincident TRUE ORIGINAL GQ pair (q,r) with unique projection q-l-p-r and physically endpoint-conflicting original f(q)/f(p) or g(r)/g(l), create precisely TWO unordered physical antipodal grid chords. They are distinct across original pairs and never actual G edges. Let B_bad be the physical chord relation and H any genuine physical subgraph. Exact double-counted source/physical tensor identity:
```
W_H = sum_grid_z deg_Bbad(z)*deg_H(z)
    = sum_(q,r bad) sum_(u in f(q),x in g(r)) D_H(u,x).
D_G = F * Inc_ORIGINAL_GQ * L^T.
T_B(H) = tr(A_H^3*A_Bbad) >= E_H,
```
where E_H is D1's endpoint-bad PROPER oriented physical three-path mass. `T_B-E_H` consists of invalid internal coordinate/vertex coincidences, not extra accepted motifs. Bad original pair SETS regenerated independently by actual original pencils and checked against every unique original projection (stronger than matching their total counts).

From [#394's proven arbitrary-endpoint-relation mixed-book lemma](https://github.com/definitely-stable/Mathlab/pull/394):
```
E_H <= 24*t_H*W_H + sqrt(192*|B_bad|*D6(H)),   |B_bad|=O(s^5).
```
If, for the pruned H of #394 with `t_H=O(s^alpha)`, a NEW uniform bound `W_H=o(s^(6-alpha))` can be independently proved, then on any hypothetical `S=o(s^6)` family, `E_H=o(s^6)`. At alpha=1/10 this requires `W_H=o(s^(59/10))`. **THIS WEIGHTED BOUND IS NOT PROVED**; even proving it would leave the separate D1 internal-only mass I_H OPEN.

**Complete finite actual same-global-f,g records** (`W_H, T_B, E_H`, all integer):
- W32 lex `(2977,1834,786)`; reverse `(2709,1456,676)`; S68 `(3289,1644,544)`; S72 `(3303,1692,600)`.
- W34 lex `(133432,56790,38020)`; random `(115088,44552,30194)`.
- W38 random `(4927736,1195458,1019228[D1])`: unrestricted sparse-trace slack from D1 proper floor exactly `176230`.

Two independent techniques agree on exact T_B for all W32/W34: ORIGINAL endpoint-first middle-neighbor enumeration and separate sparse A_H² then A_H³ contraction. The latter also handles all 140,348 original bad W38 physical chords; the proper W38 E is reused from independently accepted D1, NOT fraudulently claimed as a second new complete enumeration.

**Critical NO-GO of naive application:** On full, unpruned S68, t=3 and 24tW=236,808 while E_H=544. The mixed-book inequality is VACUOUS as a finite D6 detector. Small samples suggesting W/s^(11/2) approx 53–73 DO NOT establish any all-h O(s^(11/2)) theorem. D2 is the correct weighted endpoint obstruction, not its universal solution.

**Exact-head hosted results:** [new dedicated D2 Contract #38286674198](https://github.com/definitely-stable/Mathlab/actions/runs/38286674198) **SUCCESS**, [INDEX #38286674137](https://github.com/definitely-stable/Mathlab/actions/runs/38286674137) **SUCCESS**, [parent proof-audit #38286674270](https://github.com/definitely-stable/Mathlab/actions/runs/38286674270) **SUCCESS**. [Full Research #38286674246](https://github.com/definitely-stable/Mathlab/actions/runs/38286674246) in progress as of comment creation, must check before final acceptance; independent mathematical review pending.

**Next D3**: prove or explicitly falsify an ORIGINAL-incidence-specific uniform weighted energy gain on the spectrally pruned H (not just expected random g, raw pencil size, or full-G Cauchy). In parallel derive a DIFFERENT compensation lemma for the internal-only I_H of D1. The eventual root Branch A needs C=E+I <= (16-eta)s^6 + Lambda*S + o(s^6) for fixed constants. This target is OPEN. Neither PROVED_A nor COUNTEREXAMPLE_B, full risk R3, or ASET exponent was established.

---

## Comment 119 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6130552050
- GitHub comment ID: 6130552050

### HYP-105 issue #230 — D3: exact ORIGINAL GQ double-centered endpoint energy, missing 1/10 exponent isolated

Created [stacked Draft PR #397](https://github.com/definitely-stable/Mathlab/pull/397) on final green [D2 Draft #396](https://github.com/definitely-stable/Mathlab/pull/396) parent HEAD `bc4e679d1d1a589d073856e90458e715eaef080c`. Child final HEAD `108b015b831b90440bbbec7e5e223ea776862059`. Main remains `179d4b93ae9aaea8f837a6aeb9bf4843380d5764` unchanged; no merge, root #230/#176/#169 OPEN. Prior P2/P7 unit-mean proposals remain FALSIFIED by actual coherent S68.

**New strictly scoped exact ALL-h identities (for arbitrary same globally coherent f,g):** Let J be TRUE original GQ VxV point-line incidence, F,L physical a-by-V coordinate incidence matrices for the two global pair-injections (each column exactly TWO ones), and U the ORIGINAL nonincident bad endpoint relation from D1/D2's unique original projection. Exact physical matrices `B=F U L^T`, `D=F J L^T`, `W_G=<B,D>`. With `Delta=s+1`, `k_f=F1,k_g=L1`, define `R=F(J-(Delta/V)11^T)L^T`. Since J is regular, and F^T1=L^T1=2*1, **R has identically ZERO physical row and column sums**, all h and all f,g. Consequently:
```
W_G=Wmean+Wcorr,
Wmean=(Delta/V) sum_(q,r in original bad U) d_f(q)d_g(r),
Wcorr=<B^0,R>,
B^0(u,x)=B(u,x)-row_u/a-col_x/a+total/a²,
||B^0||²=||B||²-(sum row²)/a-(sum col²)/a+total²/a²,
|Wcorr|²<=||B^0||² ||R||²
          <=8s(a-1)V ||B^0||².
```
This is an exact **double-centering/orthogonality** statement and GQ spectral norm certificate, NOT any new positive lower for S. Proven with actual original incidence regularity and original/dual coordinate labels, not an independent f,g random model. The D3 implementation checks all rational identities and squared norms by INTEGER exact equality/inequality, independent original source collinearity enumeration, physical coordinate gauge invariance, and true ORIGINAL FUL/FJL direct products.

**Exact finite signed evidence**, all SAME legal original f,g:
- W32 lex `2977=3060-83`, reverse `2709=2700+9`, S68 `3289=3320-31`, S72 `3303=3340-37`.
- W34 lex `133432=2207655/17+60689/17`, random `115088=1910476/17+46020/17`.
- W38 random `4927736=313987787/65+6315053/65`.
The signed GQ spectral correlation is BOTH positive and negative on actual coherent maps; any `Wcorr<=0` for-all-label shortcut is refuted. Finite trends are NOT all-h guarantees.

**Quantified missing exponent:** TRUE original GQ concurrent-pair physical overlap masses M_f/M_g obey `|U|<=2s(Mf+Mg)`. Existing #394 spectral estimate only `Mf,Mg=O(s^4)`; thus `Wmean<=4Delta(a-1)²|U|/V=O(s^6)`, NOT the `o(s^(59/10))` needed for D2's alpha=1/10 block-pruned mixed-book sufficiency. A strictly SUFFICIENT but UNPROVED split is
```
Mf+Mg=o(s^(39/10)) and ||B^0||_F²=o(s^(63/10)).
```
Then `W_G=o(s^(59/10))` by the double-centered norm and `W_H<=W_G` for H subset G, so only ENDPOINT E_H becomes negligible under S=o(s6). The INTERNAL-ONLY I_H in D1 remains unresolved even if this split holds. NO part of these two stronger little-o hypotheses is proved. Signed cancellations/amortized compensation may offer a better route.

**FINAL child exact-head hosted results at comment authoring:** [dedicated D3 Contract #38293426397](https://github.com/definitely-stable/Mathlab/actions/runs/38293426397) **SUCCESS** (7 focused tests, complete 7-state exact signed rational report), [INDEX #38293426399](https://github.com/definitely-stable/Mathlab/actions/runs/38293426399) **SUCCESS**. [parent Proof Audit #38293426382](https://github.com/definitely-stable/Mathlab/actions/runs/38293426382) and [full Research #38293426394](https://github.com/definitely-stable/Mathlab/actions/runs/38293426394) were IN PROGRESS when checked; verify them before 4/4 acceptance. Independent external proof review still needed. No main merge.

**Next D4 scientific GO/NO-GO:** directly prove/falsify an ALL-f,g sub-`s^4` original pencil overlap mass improvement or a sub-`s^(63/10)` double-centered bad relation norm improvement (for true original GQ and minimal physical pairs); separately analyze internal-only blockers and their positive GF5 family compensation. If either sufficient route fails, record a genuine all-h counterfamily to that ROUTE (not automatically a Branch B counterfamily) and pivot to signed/amortized C<= (16-eta)s6+Lambda*S+o(s6). Branch A/B, full R3 risk, and ASET exponent remain OPEN.

---

## Comment 120 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6130966514
- GitHub comment ID: 6130966514

### HYP-105 issue #230 — D4: ALL-h symplectic-spread COUNTERFAMILY to D3 AUXILIARY little-o gates (not Branch B)

Created [stacked Draft PR #398](https://github.com/definitely-stable/Mathlab/pull/398) on [D3 Draft #397](https://github.com/definitely-stable/Mathlab/pull/397), pinned green parent HEAD `108b015b831b90440bbbec7e5e223ea776862059`. Current child exact HEAD `e757eb71779ca6e0d594e3cc503bef11c80546f1`. Main untouched, #230/#176/#169 OPEN and no merges. The earlier unit-mean P2/P7 strengthening remains FALSIFIED by independent true coherent S68.

**Actual NEW ALL-h constructive mathematical NO-GO:** D3 had proposed but NOT proved the UNCONDITIONAL sufficient hypotheses `Mf+Mg=o(s^(39/10))` and `Wmean=o(s^(59/10))` to obtain its mixed-book spectral transfer. Both are **FALSE** for globally injective original f,g even with the MINIMAL physical alphabet `a=min{k:C(k,2)>=V}`. Construct a true original symplectic spread of W(3,s), s=2^h, via symmetric matrix graphs `M_(b,d)=[[b,d],[d,b+c*d]]`, where `z²+cz+1` is irreducible over GF(s). The s² graph lines plus vertical form a partition into s²+1 disjoint TRUE ORIGINAL isotropic lines, all h.

Let `g0=floor(a/4)`, `n0=a-g0`, `t=floor(n0/(2(s+1)))`, `L=g0*t`. Select L original spread lines and partition into g0 groups of t lines. For group i give all its t(s+1) original points DIFFERENT physical unordered pair labels `{i,g0+j}` using one group anchor i and disjoint nonanchor second coordinates; fill remaining original points with unused physical K_a edges to complete a genuine GLOBAL injective f. Each selected original line then contributes C(s+1,2) distinct original collinear pairs with physical coordinate intersection:
```
Mf>=L*C(s+1,2) = (3/32+o(1))*s^4.
```
The already accepted #394 `Mf=O(s^4)` is therefore **SHARP IN EXPONENT**.

Build a separate TRUE original-line global injection g from all physical K_a edges EXCEPT `K_a-V<a-1` edges of a simple cycle. Each physical right coordinate occurs at least a-3 times, so every original right line label has star sum >=2(a-3). Each ordered distinct original q,p pair on a selected spread line l gives s genuine ORIGINAL nonincident projection pairs q-l-p-r, all endpoint-bad, with d_f(q)>=t(s+1). Therefore the EXACT original D3 Wmean obeys:
```
Wmean >=[(s+1)/V]*[2s*L*C(s+1,2)]*[t(s+1)]*[2(a-3)]
      = (9/32+o(1))*s^6.
```
Thus unconditional Wmean=o(s^(59/10)) also **FALSE**. This does NOT imply W_G=Omega(s6) because `W_G=Wmean+Wcorr` has signed correlation, nor `W_H=Omega(s6)` after #394 spectral pruning, nor anything about `S=o(s6)`. It is **NOT Branch B**. No ASET exponent or full R3 claim. The second D3 proposed centered-norm route `||B0||²=o(s^(63/10))` is not established or falsified by this step.

**Independent COMPLETE ORIGINAL finite witnesses** (each has one SAME globally coherent f,g on all actual points/lines, not sampled sublabels):
- Real W34 GF4: minimal `a=14`, 3 selected disjoint ORIGINAL spread lines, symbolic Mf floor30, **actual original Mf=259**, genuine-dual Mg=257, min right physical star=11; Wmean=2124657/17, Wcorr=50187/17, exact W_G=127932.
- Real W38 GF8: minimal `a=35`, 8 selected disjoint ORIGINAL spread lines, symbolic Mf floor288, **actual original Mf=2556**, genuine-dual Mg=3659, min right physical star=32; Wmean=417494068/65, Wcorr=12447652/65, exact W_G=6614488.
Both finite models independently resolve every graph/vertical spread line against the project ORIGINAL symplectic line catalog, verify projective orthogonality, distinct full spread point partition, whole physical pair-injection, original pencil Mf/Mg and exact signed D3 arithmetic. Exact all-h arithmetic beyond W38 is labeled SYMBOLIC, not falsely claimed to be newly enumerated W316+.

**GitHub-hosted acceptance on current child head:** [new D4 Contract #38296313338](https://github.com/definitely-stable/Mathlab/actions/runs/38296313338) **SUCCESS** after correcting one import detected by the initial RED test; [INDEX #38296313161](https://github.com/definitely-stable/Mathlab/actions/runs/38296313161) **SUCCESS**. [Parent Proof Audit #38296313537](https://github.com/definitely-stable/Mathlab/actions/runs/38296313537) and [full Research #38296313329](https://github.com/definitely-stable/Mathlab/actions/runs/38296313329) were IN PROGRESS when last checked. Verify final exact-head status before full acceptance. Independent external mathematical review pending; remain Draft.

**Next D5:** STOP unconditional sub-s4 original-pencil and sub-s6 mean-energy paths; they are provably false. Test true coherent spread-family FULL signed W_G, independently examine `||B0||²`, and derive an S-conditioned ORIGINAL GQ compensation controlling both D1's endpoint E and internal-only I on the PR394 pruned graph H. Root `S_s(f,g)=Omega(s^6)` remains OPEN.

---

## Comment 121 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6136319790
- GitHub comment ID: 6136319790

### HYP-105 issue #230 D5 — ALL-h **RETENTION-ROBUST** falsifier of the unconditional D2 endpoint-energy gate

Created [stacked Draft PR #399](https://github.com/definitely-stable/Mathlab/pull/399) above [D4 #398](https://github.com/definitely-stable/Mathlab/pull/398), parent exact HEAD `e757eb71779ca6e0d594e3cc503bef11c80546f1` with 4/4 GitHub-hosted exact-head CI SUCCESS. D5 child final HEAD `edf7bf95dc4abcb8cf0e74637f61d0d457805933`. No main modifications, merges, or root #230/#176/#169 closure; P2/P7 are still false as proved by S68.

**New ALL-h analytic statement for a real globally injective ORIGINAL symplectic-spread f_s with MINIMAL alphabet a, for EVERY valid original global line injection g_s, and EVERY physical graph subgraph H_s ⊆ G_s**:

Let `R_s=|E(G_s)\E(H_s)|`, `g0=floor(a/4)`, `t=floor((a-g0)/(2(s+1)))`, `k=t(s+1)`. ORIGINAL D2 nonincident-projection bad-endpoint physical chord relation B_bad is formed from the SAME complete original f,g. Its full nonnegative weighted physical H energy is `W_H=sum_z deg_Bbad(z)*deg_H(z)`. Then

```
W_H >= [s/(g0*a)] * max(0, 2*g0*k*s-R_s)^2,       EXACT all-h;
R_s=o(s^4)  ==>  W_H >= (9/32+o(1))*s^6.
```

**Proof (not probabilistic):** For each of g0 selected ORIGINAL spread-line groups i, k points have distinct global physical labels {i,g0+j} and each such point p has s original lines r excluding its selected spread L_p. Every original incidence (p,r) has TWO distinct TRUE physical G edges, one at grid vertex (i,x) for each x in globally assigned right g(r). Define T_i^G(x) and T_i^H(x) to count full vs retained selected original incidence edges at (i,x). For each original q in L_p\{p}, ORIGINAL GQ uniquely projects nonincident (q,r) to q-L_p-p-r; since f(q),f(p) share anchor i, it is an endpoint-bad ORIGINAL pair in D2 B_bad. Hence **pointwise** `deg_Bbad(i,x)>=s*T_i^G(x)>=s*T_i^H(x)`, and `deg_H(i,x)>=T_i^H(x)`. Therefore `W_H>=s sum_i,x T_i^H(x)^2`. Exactly `2*g0*k*s` witness edges exist in full G; removing ANY R_s physical edges loses <=R_s witness edges. Apply Cauchy **from below** over g0*a anchor grid cells to get the exact theorem. Since `g0~a/4,k~3a/8,a²~2s³`, the all-h constant is 9/32, without assuming a favorable SIGN of D3's correlation, any special right map g, or any specific edge-pruning strategy.

**Strong consequence:** PR #394's coherent spectral pruning retains `1-o(1)` physical G edges, `m(G)=2V(s+1)=Theta(s^4)`; D5 therefore formally falsifies the proposed **UNCONDITIONAL** D2/D3 auxiliary `W_H=o(s^(59/10))` on EVEN THAT class of pruned H. D4 had refuted only the proposed mean/pencil small-o assumptions; D5 now refutes small-o for the **actual nonnegative FULL W_H** robustly under o(s4) edge deletion. No contradiction with the true PR #394 mixed-book upper inequality; it just cannot bound E by taking W universally tiny.

**Independent exact ORIGINAL W34/W38 validation:** Reconstruct full global injective f,g on true project's GF4/GF8 symplectic GQ; use D2 independent real original unique-projection bad endpoint chords and ORIGINAL physical graph adjacency. For EVERY relevant physical grid cell prove in integer arithmetic the two lower inequalities, all TRUE selected 2*g0*k*s witness edges unique, actual deletion count, exact rational Cauchy, independent D3 full no-deletion energy and all four deletion/g permutations (eight cases):
- W34: `W_H=127932` (full balanced), `131936` (full reversed g), `121234` (remove each 19th), `124146` (delete selected witness edges first). Full G m=850, witness selected edges120.
- W38: `W_H=6614488` (full balanced), `6663027` (full reversed g), `6267591` (remove each 19th), `6474532` (adversarial selected-first). Full G m=10530, selected witness edges1152.
Also empty H, synthetic/duplicate-edge falsifiers and symbolic all-h integer arithmetic. Finite values are exact but are **NOT** used to prove the asymptotic exponent.

**Exact final-head CI status as of issue comment:** [D5 dedicated Contract #38333932873](https://github.com/definitely-stable/Mathlab/actions/runs/38333932873) **SUCCESS**, [INDEX #38333932934](https://github.com/definitely-stable/Mathlab/actions/runs/38333932934) **SUCCESS**. [Parent Proof Audit #38333932824](https://github.com/definitely-stable/Mathlab/actions/runs/38333932824) and [full Research #38333932804](https://github.com/definitely-stable/Mathlab/actions/runs/38333932804) pending/in progress when checked. External mathematical review not recorded, PR remains Draft.

**CRITICAL logical boundary:** This is a genuine infinite **counterfamily only to the auxiliary unconditional W_H small-o approach**. It is NOT an infinite family with `S_s(f,g)=o(s^6)` (Branch B), nor proof of `S_s(f,g)=Omega(s^6)` (Branch A); no seven-positive-family R3/ASET claim. The original root proof barrier `C=E+I`, with INTERNAL-only I unresolved, persists. **Next D6** should require an S-CONDITIONAL relation or direct ORIGINAL compensated bound `C<=(16-eta)s^6+Lambda*S+o(s^6)` rather than unconditional spectral/endpoint-energy gains; jointly account for endpoint and internal blocking.

---

## Comment 122 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6136576149
- GitHub comment ID: 6136576149

### HYP-105 #230 — D6-A: exact same-original-map joint energy / 16-atom blocking / GF5 seven-family audit

New strictly stacked [Draft PR #400](https://github.com/definitely-stable/Mathlab/pull/400), base [D5 Draft #399](https://github.com/definitely-stable/Mathlab/pull/399) FINAL parent SHA `edf7bf95dc4abcb8cf0e74637f61d0d457805933`. D5's **own** final-head Contract, INDEX, Proof Audit, full Research are now 4/4 SUCCESS, no merge. D6 current exact head `9e5752c1fc175e1050ad460b76ccc25722839845`. Main unchanged `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`; #230/#176/#169 OPEN.

**Formal gate remains OPEN:** For same complete globally injective original W(3,s) f,g and the genuine PR394-coherently-pruned physical H, either prove an S-conditioned endpoint energy gain plus independent internal-only I control, OR the stronger simultaneous compensation `C(H)=E(H)+I(H)<=(16-eta)*s^6+Lambda*S(f,g)+o(s^6)` for absolute eta>0, Lambda>=0 and uniform map-independent remainder. D5 falsifies ONLY unconditional W small; its spread family has no all-h computed S, thus it does not refute the conditional route and does not settle root Branch A/B.

**New TRUE ORIGINAL complete finite six-map joint certificates, ALL from same pair-injective f,g; W, E, I, C, BB_sync, and full S where available:**
| Coherent original model | W_G | E | I | C | BB_sync | FULL S |
|---|---:|---:|---:|---:|---:|---:|
| W32 lex | 2977 | 786 | 156 | 942 | 2 | 259 |
| W32 reverse | 2709 | 676 | 222 | 898 | 0 | 169 |
| W32 S68 | 3289 | 544 | 62 | 606 | 0 | 68 |
| W32 S72 | 3303 | 600 | 58 | 658 | 0 | 72 |
| W34 actual D5 spread balanced g | 127932 | 35190 | 17570 | 52760 | 7649 | UNMEASURED |
| W34 actual D5 spread reversed g | 131936 | 36014 | 17224 | 53238 | 7479 | UNMEASURED |

**Exact FINITE counterexample to naive monotonicity:** W32 S68 `W=3289>2977=W(lex)` yet `S=68<259=S(lex)` and `C=606<942`. This refutes monotone scalar W-to-S or W-to-C rules, **not** an infinite all-h conditional energy theorem. W34 `S>=BB_sync` is rigorous but NOT the entire seven-class S and MUST NOT be substituted for S in a compensation claim. Independent ORIGINAL endpoint-first/middle-edge oracle agrees with all 16 atoms. Five focused tests on initial exact head SUCCESS; the six exact rows are now pinned for regression on the final HEAD.

**D6 final-head hosted CI:** [dedicated D6 Contract #38335195815](https://github.com/definitely-stable/Mathlab/actions/runs/38335195815) **SUCCESS**, [INDEX #38335195872](https://github.com/definitely-stable/Mathlab/actions/runs/38335195872) **SUCCESS**; [Proof Audit #38335195909](https://github.com/definitely-stable/Mathlab/actions/runs/38335195909) and [full Research #38335195997](https://github.com/definitely-stable/Mathlab/actions/runs/38335195997) not yet successful at posting; check their final exact-head conclusions. External independent math review pending.

**Next D6-B:** implement PR394's *actual* coherent edge-pruning and independently recount original E/I/C/BB on H across the SAME global f,g, with separate adversarial-retention stress; then build a concrete bounded-congestion ORIGINAL 16-atom-to-positive-seven-family charging map or rigorously falsify a named transfer inequality. A scalar finite fit is not a proof. NO PROVED_A/COUNTEREXAMPLE_B, no complete GF5 R3/ASET exponent, do not merge/close anything.

---

## Comment 123 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6136900614
- GitHub comment ID: 6136900614

### HYP-105 / #230 — D6-B literal PR394 coherent pruning: finite exact phase diagnosis

New [Draft PR #401](https://github.com/definitely-stable/Mathlab/pull/401), stacked on fully exact-head green [D6-A Draft #400](https://github.com/definitely-stable/Mathlab/pull/400), pinned parent `9e5752c1fc175e1050ad460b76ccc25722839845` (4/4 hosted SUCCESS). D6-B current final code HEAD `46f8cf23fd5f610abd407979c9432df8f79f0a3b`; main still `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`. No merges, root #230/#176/#169 remain OPEN.

**Scientific control:** PR394's spectral coherent cleaning acts on entire genuine ORIGINAL GQ incidences, always removing/keeping **both actual physical diagonals**, then reclassifies remaining proper 3paths using the **unchanged same global original f,g and unique q-l-p-r projection**. Integer exact tests replace floating exponents: kappa=max k with k^16<=s, original block b removed iff b^10>s, grid vertex peeled iff d^32<s^31. Reversed endpoint-first path enumeration independently agrees with all 16 atoms. Nonnegative W_H independently checked via D2 and D5. Four policies separately named: FULL, LITERAL PR394, NOT-PR394 finite calibration, coherent original-incidence selected-witness-first/every-19th. No finite fit is treated as asymptotic proof.

**NEW TRUE ORIGINAL finite observation: literal PR394 spectral pruning is EMPTY for W32 lex, W32 S68, W34 D5 spread balanced, W34 D5 spread reverse.** Explicit ORIGINAL incidence stage deletions (stage1 bad row/column, stage2 original big blocks, stage3 paired low-degree peeling; followed by retained):
- W32 lex: (0,44,1;0) out of 45.
- W32 S68: (0,45,0;0) out of 45.
- W34 spread balanced: (329,85,11;0) out of 425; 4 bad physical row coordinates and 5 bad column coordinates.
- W34 spread reverse: (319,97,9;0) out of 425; again 4 bad rows and 5 bad columns.

This is **NOT** counterevidence to the all-h PR394 theorem. At s=2,4 (and also s=8) its formal integer neighbor block cap is b<=1; its asymptotic (16-o(1))s6 path survival only starts at sufficiently large h. A zero H yields zero E/I/C by vacuity and cannot support the hoped-for compensation proof.

**Nonvacuous calibration original-GQ examples (NOT literal PR394):**
- W34 spread balanced: retained **482/850** physical edges, `W_H=72810,E=6702,I=3588,C=10290,BB_sync=1376`.
- W34 spread reverse: retained **464/850**, `W_H=72094,E=6170,I=3016,C=9186,BB_sync=1234`.
- Coherent original selected-witness-first retains 818/816 of 850 physical edges with C=46882/47400 and I=15652/15122; endpoint-energy-only route cannot explain those internal-only blockers. FULL W34 baseline C=52760/53238.
- W32 S68 calibrated 48/90 physical edges, W=1759,E=76,I=8,C=84. All these are exact original full-global-f,g finite diagnostics; **not** a universal S compensation inequality.

**Exact-head D6-B hosted CI so far:** [focused Contract #38337114224](https://github.com/definitely-stable/Mathlab/actions/runs/38337114224) **SUCCESS** with 7 pinned tests and 16 full table oracles; [INDEX #38337114263](https://github.com/definitely-stable/Mathlab/actions/runs/38337114263) **SUCCESS**. [Proof Audit #38337114287](https://github.com/definitely-stable/Mathlab/actions/runs/38337114287) and [full Research #38337114222](https://github.com/definitely-stable/Mathlab/actions/runs/38337114222) still pending/in progress at posting; their status must be independently checked. Independently reviewed mathematical compensation theorem is still missing.

**Priority next D6-C:** abandon using literal tiny-s cleaned H as a nonvacuous test. Use genuine finite nonvacuous calibrated/coherent-adversarial H strictly as a *local falsifier*, then develop a bounded-congestion ORIGINAL GQ 16-atom obstruction -> accepted seven GF5 sixset charging rule; prove all-h transfer or produce a precise coherent counterexample to the rule. A second option is a uniform coarse-to-fine mesoscopic cutoff with an analytic error budget, not finite exponents. Neither root Branch A nor B established, full R3 and ASET remain OPEN.

---

## Comment 124 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6137161690
- GitHub comment ID: 6137161690

### HYP-105 / #230 — D6-C complete ORIGINAL local Hall charging: canonical all-h NO-GO + S68 2-incidence falsifier

Created strictly stacked [D6-C Draft PR #402](https://github.com/definitely-stable/Mathlab/pull/402) above [D6-B Draft PR #401](https://github.com/definitely-stable/Mathlab/pull/401), parent exact SHA `46f8cf23fd5f610abd407979c9432df8f79f0a3b` (4/4 CI SUCCESS). D6-C final source/doc SHA `2ebe9d5faebc14d9d55489a89d70a15cf330a7a1`. Main remains `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`; NO merges, #230/#176/#169 OPEN.

**Analytic ALL-h restricted negative lemma:** For ANY globally coherent ORIGINAL W(3,s) pair-injective f,g and any proper nonincident physical H-P3, the unique original GQ projection q-l-p-r supplies the canonical six-incidence candidate of the three original path edges plus (q,l),(p,l),(p,r). If any original incidence repeats, not six distinct. If all six distinct, original path+endpoint pair has degree 2 on each of its four first/right path coordinates, and the extra twice-used f(p),g(l) either introduce exactly two new degree-2 coords or make an existing coordinate degree 4. Therefore any nonzero of D1's four original projection collision mask bits makes this **canonical** candidate non-leafless, excluded from ALL seven accepted positive GF5 sixset classes. Zero-mask canonical closure is known BB-overlap. This is a direct natural-closure NO-GO, not an all-h lower bound on S, and it does NOT rule out noncanonical target repairs.

**Stronger exact finite original repair feasibility via all-seven recipient enumeration and integral maxflow/mincut.** For every blocked oriented physical P3 with three actual distinct ORIGINAL incidence IDs T, an r-preserving repair must choose Q among the FULL accepted positive sixsets with |T∩Q|>=r (r=3,2,1). Solve the exact bipartite integer flow (source triple demand includes BOTH path orientations, sixset capacity K), report unsupported TRUE original path if no Q, otherwise min K and verified Hall cut at K-1. All sixset recipients use the SAME complete original f,g; not BB-sync-only or random independent maps.

| Original W32 complete map | C full-G oriented blocked | Entire seven S | r=3 unsupported | r=2 unsupported / optimal K | r=1 unsupported / optimal K |
| --- | ---: | ---: | ---: | --- | --- |
| lex | 942 | 259 | 760 | 0 / K=4 | 0 / K=4 |
| S68 | 606 | 68 | 596 | **8 / IMPOSSIBLE** | 0 / K=9 |

**Explicit original S68 r=2 NO-GO witness:** genuine physical flattened-grid path `[26,15,7,34]`, original source incidences `[5,16,35]`, ORIGINAL endpoints `q=3, r=13`, unique ORIGINAL projection `p=13,l=8`, blocking mask=13 (LE+RE+RI). The test reconstructs ALL original physical source edges and scans **every one of the 68** accepted original S68 positive six-incidence target sets: intersection with `{5,16,35}` is always at most 1. Thus NO charge preserving >=2 source incidences exists for this legitimate blocked path **at s=2**, independently of recipient congestion. Eight oriented blocked paths (four reversal pairs) have this property. Such a universal all-s rule is FALSE; an asymptotic h>=h0 version is not settled. This same specific witness remains under coherent every-19th source-incidence deletion and under explicitly relaxed finite calibration (NOT the literal PR394 pruning).

**Finite optimal integer Hall cuts:** lex overlap>=2,1 admits K=4, while K=3 fails with exact demand deficit `942-3*259=165`; S68 overlap>=1 admits K=9, while K=8 fails with `606-8*68=62`. Both cuts are the global pigeonhole constraint, and no extra finite congestion penalty appears in these particular feasible cases; finite K does NOT establish any uniform-in-h Lambda.

Literal PR394 W32 H is empty (as D6-B established) and correctly tagged **EMPTY-SOURCE-NO-INFERENCE**. W34/W38 COMPLETE seven-family S is unavailable: NOT fabricated or equated to BB. Neither the target `C_H<=(16-eta)s6+Lambda*S+o(s6)` nor the conditional W-smallness lemma is proved or refuted as an asymptotic statement. Root Branch A/B, full GF5 R3 and ASET exponent OPEN.

**D6-C hosted CI on final source/doc SHA:** [focused Contract #38339013792](https://github.com/definitely-stable/Mathlab/actions/runs/38339013792) SUCCESS, **7 tests** including independent true-source witness vs all 68 sets; [INDEX #38339013760](https://github.com/definitely-stable/Mathlab/actions/runs/38339013760) SUCCESS. [Proof Audit #38339013810](https://github.com/definitely-stable/Mathlab/actions/runs/38339013810) and [Full Research #38339013762](https://github.com/definitely-stable/Mathlab/actions/runs/38339013762) still awaiting final exact-head status at this report; independent mathematical review also outstanding. Keep DRAFT.

**Next D6-D:** develop a genuinely noncanonical ORIGINAL source-to-seven-class repair, allowing at most one preserved original incidence (since r>=2 has a true local s=2 counterexample) OR an analytic large-h expansion/capacity lemma with an explicit exception/error budget. Must handle all 15 nonzero masks E+I on actual PR394 coherently pruned H with uniform h-independent multiplicity; finite S68 optimal K=9 is NOT an all-h bound. Alternate route: prove conditional `S=o(s6)=>W_H=o(s^(59/10))` **plus** bound internal-only I. No issue close/merge or root claims.

---

## Comment 125 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6137703433
- GitHub comment ID: 6137703433

### HYP-105 #230 — D6-D: exact all-h one-incidence Hall factorization and eight genuine finite certificates

Created stacked [Draft PR #403](https://github.com/definitely-stable/Mathlab/pull/403) over final-head 4/4 green D6-C #402 (parent `2ebe9d5faebc14d9d55489a89d70a15cf330a7a1`). The child retains ORIGINAL complete globally injective f,g; main untouched, no merge, root #230/#176/#169 OPEN.

**New restricted all-h theorem (transport equivalence, not existence of universal K):** for original source triples T with oriented blocked-path weights w_T and accepted original positive sixsets Q, one-incidence overlap charging with target maximum multiplicity K is equivalent to integral source→T→original incidence e→Q→sink flow with unbounded middle edges and Q sink-capacity K. Equivalently exact weighted Hall: for all source-triple sets U, sum_U w_T <=K times the number of accepted Q intersecting the union of U's original incidences. Source-closed original-incidence sets F suffice; define M(F)=sum_{T subset F}w_T and B(F)=#{Q intersect F}. The ALL-h actual theorem is **equivalence** to `M(F)<=K B(F)`, NOT such a bound for any fixed K. Network has 3|T|+6|Q| eligibility arcs. Exact minflow/mincut failure at K-1 certifies the optimal integer K; independent D6-C *direct* T→Q flow gives identical K on all four complete W32 cases.

**Complete original seven-family W32, full G**:
| model | E | I | blocked C | full ORIGINAL S | exact min K | ceil(C/S) |
|---|---:|---:|---:|---:|---:|---:|
| lex |786|156|942|259|4|4|
| reverse |676|222|898|169|6|6|
| S68 |544|62|606|68|9|9|
| S72 |600|58|658|72|10|10|

**TRUE original W34 symplectic-spread, only certified synchronized BB-overlap Q subset, full seven S UNKNOWN**:
| W34 model / source graph | E | I | C | accepted BB_sync sixsets | exact min K using BB ONLY |
|---|---:|---:|---:|---:|---:|
| balanced g, FULL G |35190|17570|52760|7649|7|
| reverse g, FULL G |36014|17224|53238|7479|8|
| balanced g, finite RELAXED calibration H (NOT PR394) |6702|3588|10290|7649|2|
| reverse g, finite RELAXED calibration H (NOT PR394) |6170|3016|9186|7479|2|

Each of 52,760 balanced W34 full blocked oriented paths is assigned integrally to a TRUE ORIGINAL accepted BB-positive sixset sharing >=1 TRUE ORIGINAL incidence, at most seven paths per recipient; 26,380 distinct source triples, 7,649 actual BB targets, 125,034 factorized eligibility arcs. Reverse full C=53,238 also assigned using only 7,479 BB recipients at max K=8. This is a **rigorous finite witness**, not ALL-h or all-map proof and not full W34 S computation. Every one of 8 instances reaches the cardinality floor ceil(C/recipients), though smaller Hall cuts can have stronger deficits at K-1 without increasing optimal integer K. One-class-deletion coverage diagnostic on all FOUR W32 full maps reports zero unsupported source paths for each of seven single-class removals; this is coverage ONLY, not a capacity certificate.

[Initial successful D6-D dedicated Contract #38342658597](https://github.com/definitely-stable/Mathlab/actions/runs/38342658597) tests passed after correction of zero-count seven-family ablation names. All eight exact K values now PINNED in tests and published in [D6-D analytic+finite document](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6d-incidence-factored-flow/docs/research/HYP-105-ISSUE230-D6D-FACTORED-INCIDENCE-HALL.md). Final code/doc SHA `550803c3fbf63e597f32ca925768f86e7553b859`, exact-head Contract [#38342845941](https://github.com/definitely-stable/Mathlab/actions/runs/38342845941), INDEX [#38342845979](https://github.com/definitely-stable/Mathlab/actions/runs/38342845979), Proof Audit [#38342845945](https://github.com/definitely-stable/Mathlab/actions/runs/38342845945), Full Research [#38342845946](https://github.com/definitely-stable/Mathlab/actions/runs/38342845946) require final CI verification, and independent mathematical review is still pending.

**Next D6-E analytic research:** establish or refute map-independent original GQ source-support expansion M(F)<=K B(F) for genuine full seven Q on the PR394 coherent H (absolute K independent of h). Need separate E and internal I control, exploit ORIGINAL GQ spectral/geometry without substituting finite W34 BB_sync for S. More focused goal: derive a *bounded-exception* charging with mass at most (16-eta)*s^6+o(s6), plus Lambda*S. Neither universal Branch A nor infinite Branch B proved; ASET/full GF5 risk OPEN.

---

## Comment 126 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6138432553
- GitHub comment ID: 6138432553

### HYP-105 #230 — D6-E: source-closed Hall support-expansion profile

Created stacked Draft PR #404 above D6-D #403, parent `550803c3fbf63e597f32ca925768f86e7553b859`. Main remains untouched; #230/#176/#169 remain OPEN.

**Purpose:** D6-D gave the exact one-incidence Hall equivalence. D6-E turns the next analytic target into an executable support profile rather than another finite-example search.

For an ORIGINAL incidence support `F`, the implemented profile computes

```text
M(F)=M_E(F)+M_I(F)=sum_{T subset F} w(T)
B(F)=#{Q : Q intersects union_{T subset F}T}
required_K(F)=ceil(M(F)/B(F))
```

with zero-denominator detection and exact excess over a candidate `K`. The denominator uses the active source union, so irrelevant incidences cannot artificially improve `B(F)`.

**Implementation:**

- `research/hyp105_issue230_d6e_support_expansion_profile.py`
  - `source_closed_support_profile(...)`
  - `factored_cut_profile(...)`
  - independent endpoint/internal source splitter checked against D6-B `retained_path_census`
  - `finite_w32_support_expansion_report()`
- `research/test_hyp105_issue230_d6e_support_expansion_profile.py`
- `.github/workflows/hyp105-issue230-d6e-support-expansion-profile.yml`
- `docs/research/HYP-105-ISSUE230-D6E-SUPPORT-EXPANSION-PROFILE.md`

**Finite complete-W32 result:**

| W32 map | C | E | I | complete S | K |
|---|---:|---:|---:|---:|---:|
| lex | 942 | 786 | 156 | 259 | 4 |
| reverse | 898 | 676 | 222 | 169 | 6 |
| S68 | 606 | 544 | 62 | 68 | 9 |
| S72 | 658 | 600 | 58 | 72 | 10 |

For these four complete-W32 finite cases, the global source-closed support floor already equals the D6-D exact optimum. Thus no extra local support-expansion penalty is exposed beyond `ceil(C/S)` in those cases. This is a finite diagnostic only.

**Non-claims:** no all-h support-expansion theorem, no controlled exceptional-mass theorem, no Branch A/B resolution, no ASET exponent, no W34 BB-only substitution for unknown complete W34 `S`.

**CI on PR #404 / head `558f2ccb2e724284e80085a1b397c1a1b7b84ce2`:**

- D6-E dedicated Contract #38347922850 — SUCCESS
- INDEX #38347922768 — SUCCESS
- Proof Audit #38347922837 — SUCCESS
- Full Research #38347922832 — running at the time of this comment

**Next analytic target:** prove or refute a genuine all-h bound `M_E(F)+M_I(F)<=K B(F)` for complete seven-family recipients on the actual coherent retained `H`, or replace it by a bounded exceptional-mass decomposition. Finite `K=4,6,9,10` is not a valid universal constant.

---

## Comment 127 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6138853490
- GitHub comment ID: 6138853490

### HYP-105 #230 — D6-G local Hall-excess envelope

Created stacked Draft PR #406 over D6-F #405 final green head `262408745ed4817745973f3455e01be3a5e697eb`. `main` remains untouched; #230/#176/#169 remain OPEN.

D6-G separates exact exception mass from the unavoidable global capacity deficit:

```text
local_excess_K = exception_K - max(0, C-K*S).
```

Interpretation: `max(0,C-K*S)` is pure pigeonhole/global capacity deficit. Positive `local_excess_K` is a genuine local Hall-support obstruction beyond total capacity.

Added:

- `research/hyp105_issue230_d6g_local_excess_envelope.py`
- `research/test_hyp105_issue230_d6g_local_excess_envelope.py`
- `docs/research/HYP-105-ISSUE230-D6G-LOCAL-EXCESS-ENVELOPE.md`
- `.github/workflows/hyp105-issue230-d6g-local-excess-envelope.yml`

Finite complete-W32 all-seven result at first failed capacity `K-1`:

| map | C | complete S | zero-exception K | exception at K-1 | local excess at K-1 |
|---|---:|---:|---:|---:|---:|
| lex | 942 | 259 | 4 | 165 | 0 |
| reverse | 898 | 169 | 6 | 53 | 0 |
| S68 | 606 | 68 | 9 | 62 | 0 |
| S72 | 658 | 72 | 10 | 10 | 0 |

This means these finite W32 instances do not show a local Hall penalty at the first failed capacity; their failure is exactly the global pigeonhole deficit. This is not an all-h theorem.

Explicit non-claims: no all-h uniform `K`, no all-h exception bound, no all-h local-excess bound, no complete W34/W38 seven-family `S`, no Branch A/B resolution, no ASET/R3 exponent.

Current PR #406 CI at posting: D6-G Contract SUCCESS, INDEX SUCCESS; Proof Audit and full Research still running.

---

## Comment 128 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6139217811
- GitHub comment ID: 6139217811

### HYP-105 #230 — D6-E verified; D6-H sufficient original-incidence budget theorem implemented

**Repository audit (2026-10-13):** the previous D6-D #403 and already-created D6-E #404, D6-F #405, D6-G #406 are strictly stacked Draft PRs. Their exact-head hosted dedicated Contracts, INDEX, Proof Audit, and Research are **4/4 SUCCESS each**. Root #230/#176/#169 remain OPEN and main remains \`179d4b93ae9aaea8f837a6aeb9bf4843380d5764\`.

New [Draft PR #407](https://github.com/definitely-stable/Mathlab/pull/407) is stacked **strictly over #406**. It establishes the general *sufficient* incidence allocation theorem: for original source triples with oriented integer demand, accepted original positive sixsets, and any fixed integer K, rational recipient slots a(Q,e) with sum_e a(Q,e)<=K yield a smaller source->T->incidence flow V, implying D_K<=floor(C-V) by embedding and integral maxflow of the D6-D network. Uniform six-slot allocation implies the all-h sufficient endpoint+internal overload bound

    D_K <= floor( sum_e max(0, 2*(L_E(e)+L_I(e))-K*d_A(e)) / 6).

In particular 2(L_E(e)+L_I(e))<=K*d_A(e) at EVERY original source incidence is an all-h sufficient condition for zero-exception one-incidence transport. **The crucial uniform-in-h bound is NOT proved to hold for arbitrary true global f,g or actual high-h PR394 H.** No Branch A/B, full R3, ASET or universal K claim.

The specialized first-head [GitHub-hosted Contract #38353460351](https://github.com/definitely-stable/Mathlab/actions/runs/38353460351) succeeded: 4 exact tests, including independent tiny-instance brute-force and four real W32 complete-seven all-true-original cases. Unexpected useful finite observation: the scaled uniform 1/6 incidence flow matches D6-F exact exception in **all eight** tested capacities: lex (K=3:165, K=4:0); reverse (5:53, 6:0); S68 (8:62, 9:0); S72 (9:10, 10:0). Simpler pointwise equal-third bound is strictly weaker, so no all-h tightness inference. These eight pairs are now pinned in the tests and documentation.

Final pinned child HEAD: \`e4460f9475dfe8ca6270da13348ce6cdb79cf93a\`. Final-head CI runs **must be independently checked** before D6-H technical acceptance. External mathematical review remains pending; keep Draft and main untouched. Next analytic target: prove or falsify quantitative ORIGINAL positive-sixset incidence-degree/selector domination on the SAME f,g for the genuine PR394 retained H, handling E+I jointly and never replacing unknown complete W34/W38 S with BB-only.


---

## Comment 129 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6139817466
- GitHub comment ID: 6139817466

### HYP-105 #230 / D6-I — exact weighted Hall dual for uniform ORIGINAL incidence-port allocation

Created [Draft PR #408](https://github.com/definitely-stable/Mathlab/pull/408) strictly stacked over fully green [D6-H #407](https://github.com/definitely-stable/Mathlab/pull/407), parent `9aa186a421e8890aecdc384fde6c3ae73d106c9a`. Current pinned child HEAD `b3c4a5300d08457018c845b89242498bd5102d5c`. Main unchanged `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`; root #230/#176/#169 OPEN.

**New exact ALL-finite / ALL-h RESTRICTED theorem:** For true ORIGINAL 3-incidence source triples carrying endpoint+internal blocked-path demands w(T), accepted ORIGINAL positive sixsets Q from the SAME global f,g, and integer K, let `d_A(e)=#{Q:e in Q}`, `M(F)=sum_{T subset F} w(T)`, and `D(F)=sum_{e in F} d_A(e)`. The uniform restricted D6-H rational port allocation reserves K/6 capacity from each accepted Q at each of its six original incidences. Its integer network after scaling by 6 has exact shortfall

`Delta6 = 6C-maxflow6 = max_{source-closed F}(6M(F)-K D(F))_+`.

Therefore uniform-port full transport is equivalent to the weighted Hall condition `6M(F)<=K D(F)` for EVERY source-closed F, and by the previous D6-H slot embedding and integrality the **true full original** D6-F exception satisfies `D_K<=floor(Delta6/6)`. This is NOT the full D6-D Hall equivalence, NOT a uniform all-h K, and not root Branch A/B.

**True same-map complete-seven W32 finite results:** lex C/S=942/259, K_full=K_uniform=4, K-1 exception 165; reverse 898/169, K=6, exception53; S68 606/68, K=9, exception62; S72 658/72, K=10, exception10. Each K-1 mincut was exactly all 45 ORIGINAL incidences, with D(F)=6S and Delta6=6(C-(K-1)S). No nontrivial local expansion penalty was found in these FINITE cases; no asymptotic extrapolation.

**Independent falsifiers:** exhaustive all-source-subset enumeration for 72 deterministic small systems × five K (360 checks), independent integer capacity-ratio oracle, exact huge integer 10^80 and strict floor-vs-ceil example, zero/unsupported cases and E+I joint mass check. [First dedicated hosted Contract #38357406426](https://github.com/definitely-stable/Mathlab/actions/runs/38357406426) SUCCESS, tests 5/5. Final pinned-head dedicated D6-I [#38357569243](https://github.com/definitely-stable/Mathlab/actions/runs/38357569243) SUCCESS and INDEX [#38357569311](https://github.com/definitely-stable/Mathlab/actions/runs/38357569311) SUCCESS; Proof Audit and full Research running when recorded. Verify all four exact-head CI before technical acceptance and retain independent mathematical review gate. No merges, PR Draft.

**Next D6-J:** prove or falsify genuine ORIGINAL GQ geometry-based positive-sixset port-boundary lower bounds D(F) vs joint E+I source-closed mass M_H(F) on the ACTUAL PR394 high-h retained H for all correlated global f,g. Partial W34 BB-only recipients must never stand in for complete S.

---

## Comment 130 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6140045223
- GitHub comment ID: 6140045223

### HYP-105 #230 / D6-J — sharp six-factor ALL-h uniform/full model comparison (2026-10-13)

Created [Draft PR #409](https://github.com/definitely-stable/Mathlab/pull/409) strictly stacked above [D6-I #408](https://github.com/definitely-stable/Mathlab/pull/408) HEAD `b3c4a5300d08457018c845b89242498bd5102d5c`. Final pinned D6-J HEAD `773ac86584fc143b41b5196db33def10ee67d2c8`. Main untouched `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`, no merges.

**NEW exact all-finite theorem, no Branch A claim:** for exact ORIGINAL 3-incidence source demand (joint endpoint E + internal I), ORIGINAL complete GF5-positive sixset recipients Q (when available), and capacity K: `V6(K)<=6 Vfull(K)<=V6(6K)`, where V6 is the six-scaled uniform original-port D6-I maxflow and Vfull the exact full original D6-D transport. Define `U(k)=floor((6C-V6(k))/6)`; then `U(6K)<=Dfull(K)<=U(K)`. When all sources have actual positive recipient overlap and C>0, `Kfull<=Kuniform<=6Kfull`. Factor 6 is globally SHARP on finite incidence hypergraphs (one triple and one sixset with exactly one shared original port).

A full integral T→e→Q flow yields a **matching optimum adaptive integral allocation** `a(Q,e)=flow(e→Q)` with `sum_e a(Q,e)<=K`, and its simpler T→e→sink network exactly reproduces full optimum. Thus a fixed map-independent congestion bound and a fixed capacity o(s^6) exception bound are logically equivalent for FULL vs UNIFORM port models after scaling K by <=6. This is NOT a proof that such a fixed K exists on genuine GQ f,g.

**Actual W32 complete-seven numbers:** lex C/S=942/259, Kfull=Kuniform=4, K-1 Dfull=165 and 253 nonzero optimal Q/e slots at K; reverse 898/169, K=6, D=53, slots=167; S68 606/68, K=9, D=62, slots=105; S72 658/72 K=10 D=10 slots=103. All finite only; no full W34/W38 seven-positive recipient substitute. Sharp singleton / 5-recipient synthetic controls, unsupported cases, E/I joint conservation and 192 independently exhaustive finite comparators.

[First dedicated GitHub-hosted D6-J Contract #38358961078](https://github.com/definitely-stable/Mathlab/actions/runs/38358961078) SUCCESS (5/5 tests); at exact final HEAD [D6-J #38359185272](https://github.com/definitely-stable/Mathlab/actions/runs/38359185272) SUCCESS, [INDEX #38359185297](https://github.com/definitely-stable/Mathlab/actions/runs/38359185297) SUCCESS; Proof Audit and Research still running on that HEAD at comment time. Keep acceptance gated on remaining checks and independent mathematical audit. Leave Draft and root #230/#176/#169 OPEN.

**Next genuine geometry step D6-K:** obtain OR falsify quantitative ORIGINAL positive-sixset port expansion against endpoint + internal source mass on ACTUAL PR394 retained H, uniformly over all globally coherent injective f,g. The factor-six theorem shows using uniform ports incurs only universal constant-factor loss in existence questions; it does NOT supply a new positive GF5 sixset lower bound.

---

## Comment 131 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6140685973
- GitHub comment ID: 6140685973

### HYP-105 #230 — D6-K: exact ORIGINAL signed-pressure triple boundary + integer pair calibration (2026-10-13)

[Draft PR #410](https://github.com/definitely-stable/Mathlab/pull/410) strictly stacked on fully-green D6-J [#409](https://github.com/definitely-stable/Mathlab/pull/409) HEAD `773ac86584fc143b41b5196db33def10ee67d2c8`. Final D6-K HEAD `6f360a68ed0aac9c91f8a60455ce0d475d2ffb78`. Main untouched, issue #230/#176/#169 remains OPEN, no mergers.

**All-finite / all-h ORIGINAL weighted triple pressure identity (proved):** For true original blocked proper three-path incidence triples T with shared E+I mass w(T), same-map accepted positive original sixsets Q, and any F of active ORIGINAL incidence IDs, `L(e)=sum_{T contains e}w(T)`, `d_A(e)=#{Q:e in Q}`, `p_K(e)=2L(e)-Kd_A(e)`, and `boundary_w(F)=sum_{crossing T}|T intersect F|w(T)`:

`6 M(F)-K D(F)=sum_{e in F}p_K(e)-2 boundary_w(F)`.

Therefore D6-I's exact scaled Hall deficit is the positive max over F. Source-triple co-occurrence weighted pair projection obeys `pair_cut(F)=2 sum_{crossing T}w(T)<=2 boundary_w(F)`. Writing N=active original incidences, G=sum_I p, v=N sum_I p^2-G^2, the **conditional** Laplacian gate `lambda_2^2(N-1)>=v` implies `Delta6=max(0,G)` (no extra local restricted Hall obstruction). A stronger but conservative integer-only spanning-tree gate `16b^2>=vN^2(N-1)` was implemented; it fails on four genuine W32 finite maps despite global-only Hall cuts.

**NEW exact integral pair flux calibration:** q(e)=N p_K(e)-G. Bidirected ORIGINAL source-pair arcs of capacity N*w_pair carry positive q supplies to negative ones. Maxflow gives an exact *integral primal divergence certificate* iff for every F `|sum_F q|<=N pair_cut(F)`. Feasibility suffices for `Delta6=max(0,G)`. Infeasibility yields a strict exact pair-cut dual F; it does NOT disprove full ORIGINAL or uniform Hall, since ORIGINAL directed 3-port boundary can be stronger. The failing pair witness is independently evaluated in the actual 3-incidence hypergraph.

**Finite original full-seven W32 hosted results (K=K_full−1):** lex C=942 S=259 K=4, full exceptions=165 and PAIR calibration TRUE (131 nonzero pair fluxes); reverse C=898 S=169 K=6 exceptions=53, PAIR TRUE (169 nonzero fluxes). S68 C=606 S=68 K=9 exceptions=62, PAIR FALSE with original 44/45-port dual cut, q(F)=1632, paircut=28, exact N-scaled shortage `1632-45*28=372`. S72 C=658 S=72 K=10 exceptions=10, PAIR FALSE with 42/45 original ports, q(F)=6975, paircut=128, exact shortage `6975-45*128=1215`. Yet all four exact original UNIFORM Hall cuts have ZERO extra local excess and full original mincut support all 45 incidences. These are **finite only**, no high-h projected-label symmetry asserted.

**Circularity gate:** `D(I)=sum_Q |Q intersect I|<=6S`. Any imported lower bound D(I)=Omega(s^6) would ALREADY imply the original S=Omega(s^6) target; D6-K does NOT assert it. Actual high-h PR394 retained H, all correlated complete global maps and full seven-positive sixset geometry remain the missing theorem. W34/W38 BB-only inputs are NOT full S.

**CI:** first D6-K original-contract [#38362708555](https://github.com/definitely-stable/Mathlab/actions/runs/38362708555) SUCCESS with 5 methods and all-subset independent enumeration; subsequent 6-method centered pair-flux [#38363137958](https://github.com/definitely-stable/Mathlab/actions/runs/38363137958) SUCCESS. Exact-final-head dedicated [#38363593955](https://github.com/definitely-stable/Mathlab/actions/runs/38363593955) SUCCESS and INDEX [#38363593957](https://github.com/definitely-stable/Mathlab/actions/runs/38363593957) SUCCESS. Proof Audit and full Research remain pending/in-progress at time of comment; independent math review is NOT substituted by CI. Keep Draft/main unchanged.

**Next mathematical D6-L:** use ORIGINAL directed 3-incidence hypergraph boundary directly (not only pair Laplacian; S68/S72 falsify its necessity), and derive or disprove genuine high-h GF5-positive degree/pressure vs blocked-source expansion for ALL correlated f,g. No Branch A/B or ASET exponent.

---

## Comment 132 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6141043395
- GitHub comment ID: 6141043395

### HYP-105 #230 — D6-L: EXACT directed ORIGINAL three-incidence pressure calibration (2026-10-13)

Created [Draft PR #411](https://github.com/definitely-stable/Mathlab/pull/411), strictly stacked on fully GitHub-hosted-green [D6-K #410](https://github.com/definitely-stable/Mathlab/pull/410) HEAD `6f360a68ed0aac9c91f8a60455ce0d475d2ffb78`. Last child HEAD `511b851048afc16f89d01647026205cda341e829`. Main unchanged `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`, no merges; root #230/#176/#169 remain OPEN.

**New exact ALL-finite / ALL-h conditional ORIGINAL three-port hypergraph result:** Let source triple T consist of 3 ORIGINAL GQ incidences, carry combined endpoint+internal proper oriented blocked P3 weight w(T); accepted genuine GF5-positive Q consist of 6 distinct ORIGINAL incidences from the SAME complete globally injective correlated maps f,g. For K>=0 put active original incidence universe I, N=|I|, p_K(e)=2L(e)-K d_A(e), G=sum_I p, q(e)=N*p(e)-G, and b_dir(F)=sum_{T crossing F}|T∩F|w(T). An integer-flow graph with arcs ORIGINAL e→aux(T) capacity 2Nw(T), aux(T)→e capacity effectively infinite, and positive/negative q demand has exact deficit

`E_dir=max_{F⊆I}[sum_{e∈F}q(e)-2N*b_dir(F)]_+`.

It reconstructs either full integral ORIGINAL three-port flow with exact q divergence, or an ORIGINAL dual support F and positive shortfall. Unlike PAIR cut, this retains 1-vs-2 selected-incidence crossing orientation. Let Delta6 be exact uniform-port scaled Hall deficit and E_pair old centered pair-calibration shortfall:

`0≤E_dir≤E_pair`, `0≤Delta6-max(0,G)≤floor(E_dir/N)` for N>0. Thus E_dir=0 certifies NO local uniform Hall excess. **Balanced special case:** if G=0, `E_dir=N*Delta6` exactly, verified by synthetic disconnected source.

**Major genuine finite W32 improvement:** original complete-seven same-map positive GF5 targets at Kfull−1 yielded:
- lex C=942,S=259,Kfull=4,Dfull=165, pair E=0, **directed E=0** (148 nonzero ORIGINAL triple primal flows);
- reverse C=898,S=169,Kfull=6,Dfull=53, pair E=0, **directed E=0** (179 flows);
- S68 C=606,S=68,Kfull=9,Dfull=62, **pair E=372, directed E=0** (123 flows);
- S72 C=658,S=72,Kfull=10,Dfull=10, **pair E=1215, directed E=0** (180 flows).

This precisely resolves both W32 examples where the centered PAIR model had an obstruction but true original weighted Hall cuts were globally tight. The directed certificates are INTEGER primal reconstructions, not just mincut restatements. The data are **finite only**; no all-h GQ inequality or high-h actual PR394 H proof. A strict SYNTHETIC example T=(0,1,2),w=4,K=1 with 17 accepted sixsets meeting T only at e=2 also has pair E>0 and directed E=0.

Hosted verification: initial D6-L Contract [#38365712256](https://github.com/definitely-stable/Mathlab/actions/runs/38365712256) found a mislabeled synthetic test scenario K=5 (global deficit exceeded local), **not a theorem failure**. Repaired K=30 to isolate true local excess; followup [#38365828118](https://github.com/definitely-stable/Mathlab/actions/runs/38365828118) SUCCESS (5/5 focused tests including 48×4 independent all-incidence-F cut enumerations), plus true W32 fail-closed checks. Final exact-head CI after pinning the four finite triples and G=0 is required. Independent mathematical review remains open; do not merge.

**Mathematical blocker for D6-M:** positive-sixset port boundary D_A(I)≤6S. Any alleged all-h lower bound D_A(I)=Ω(s^6) ALREADY implies the root Branch A S=Ω(s^6), so neither this additional flow theorem nor finite W32 calibration establishes it. Next must derive novel ORIGINAL seven-GF5-class geometry constraints on all correlated f,g for genuine PR394 retained H, or an infinite coherent counterfamily. No full W34/W38 seven-positive S is available; BB-only is not full S.

---

## Comment 133 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6142076553
- GitHub comment ID: 6142076553

### HYP-105 #230 / D6-M — genuine GQ collinearity / positive GF5 right-random C-left/A-right transfer (2026-10-13)

Created [Draft PR #412](https://github.com/definitely-stable/Mathlab/pull/412), strictly stacked on fully CI-green [D6-L #411](https://github.com/definitely-stable/Mathlab/pull/411), parent HEAD `511b851048afc16f89d01647026205cda341e829`. Pinned child HEAD `b95ef33a0c3218b4d07b9577d50bcf1ea01f9ed4`. Main unchanged `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`; no merges; root #230/#176/#169 OPEN.

**New exact ALL-h ORIGINAL W(3,s) collinearity theorem, NOT a Hall restatement:** For ANY fixed globally injective original left point pair map f, a left physical-C template is three ORIGINAL points whose physical f-pairs are pairwise disjoint, each choosing two distinct incident ORIGINAL factor lines. Let d=s+1, B=binom(d,2), A=d−1, Z=binom(d−1,2). The exact numbers of ORIGINAL choices of six DISTINCT right factor lines for these three ORIGINAL points are:
- 0 collinear pairs: B³;
- 1 collinear pair: B³−A²B;
- 2 collinear pairs: B³−2A²B+A²;
- 3 collinear pairs (GQ forces ONE common true line): Z³+3AZ².

**Exactly** for a UNIFORMLY random complete injective right physical map g, conditional on ANY fixed left f,
`E_g U_{C-left/A-right}(f,g) = [720*70*binom(a,6)/(binom(a,2))_6] * sum_{f-pairwise-disjoint triples of ORIGINAL points} Phi_d(triple)`.
This is the **directional subclass C-left/A-right ONLY**. Existing seven-GF5 tag `C/A` aggregates C-left/A-right AND A-left/C-right; no exact equality for the aggregate is claimed. All counted directional sets are known strictly positive original GF5 sixsets. The previously proved all-h left physical C template lower, plus true GQ exact collinear point-pair count `V*s*(s+1)/2`, gives uniform-in-f
`E_g U_{C-left/A-right} >= (35/3-o(1))*s^6`.
Disjoint previously proved `B-left/A-right` expected lower `(140-o(1))*s^6` gives the NEW all-h **right-RANDOM** seven-positive lower
`E_g S_seven(f,g) >= (455/3-o(1))*s^6`.
It is NOT `inf_{f,g} S=Omega(s^6)`; no uniform bound on every adversarial correlated fixed right g; no Branch A/B.

**True ORIGINAL finite evidence:** W32 lex and reverse have IDENTICAL fixed LEFT f, 15 left C point triples, 209 right-distinct C lifts, exact random-right directional expectation **38/13**, but ACTUAL right-map directional counts **4 vs 0**. S68/S72 each have 15 C triples, 297 right-distinct C lifts and expectation **54/13**, but ACTUAL right-map directional counts **0 vs 2**. The W32 full GF5 `C/A` aggregate is separately checked by independent counting both orientations; lex aggregate=13 (4+9), reverse aggregate=1 (0+1). In particular reverse/S68 **falsify** the illegal inference positive random-right directional expectation -> positive for EVERY fixed right g; they do NOT falsify main seven-family S because remaining classes may be positive.

Genuine W34 s=4, with original full 85+85 point/line GQ and all 425 original incidences, has lex: 36,270 left C templates, 32,283,840 right-distinct original sixset lifts, exact random-right directional expectation `1129934400/110983`; random fixed left: 36,624 templates, 32,560,144 lifts, expectation `1139605040/110983`. Absolutely NO invented complete W34 seven-class S: these are **expectations**, not actual fixed right counts. Independent actual GQ four-collinearity-orbit brute right-line selection at s2/s4 and enumeration of 70 simple physical six-edge two-factors among C(15,6)=5005 verified.

**Acceptance:** Initial D6-M hosted contract failed an important **scope mismatch** (one-side C-left/A-right vs two-direction aggregated tag), corrected theorem, independent both-orientation classifier and PR body. [Corrected D6-M CI #38372684216](https://github.com/definitely-stable/Mathlab/actions/runs/38372684216) passed 5/5. [Pinned final D6-M CI #38373287834](https://github.com/definitely-stable/Mathlab/actions/runs/38373287834) SUCCESS with 6 methods, [INDEX #38373287836](https://github.com/definitely-stable/Mathlab/actions/runs/38373287836) SUCCESS; Proof Audit and Research are not yet ACCEPT at comment time. Independent mathematical review OPEN. PR Draft, no merges.

**Next D6-N real proof gate:** a FIXED-right lower on joint accepted GF5 B/A and C/A, or an explicit infinite correlated counterfamily; requires a new ORIGINAL GQ incidence tensor/discrepancy argument beyond the random-right mean. More Hall maxflow duals alone will not resolve this. Keep #230/#176/#169 OPEN, no ASET exponent.

---

## Comment 134 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6142440853
- GitHub comment ID: 6142440853

### HYP-105 #230 / D6-N — exact ORIGINAL C/A correlated six-line overlap and second moment (2026-10-13)

Created strictly stacked [Draft PR #413](https://github.com/definitely-stable/Mathlab/pull/413) above [D6-M #412](https://github.com/definitely-stable/Mathlab/pull/412), base `4454b4fcff63710ed6f82ee63e154ddb7273c46d`. Latest D6-N head `427db12b40cd498efc9e21b2e5fa07c89da42c54`. `main` untouched, root #230/#176/#169 OPEN.

**NEW exact ALL-finite-h ORIGINAL support/physical-mask identity and right-random second moment:** for each fixed globally injective genuine GQ left f, let `w_f(L)` be the number of distinct ORIGINAL C-left sixsets with six DISTINCT ORIGINAL right line identities L, and `A_g(L)` the indicator that the globally injective right g maps L to the accepted physical six-edge A 2-factor. Then `U_Cleft/Aright(f,g)=sum_L w_f(L) A_g(L)` for EVERY fixed g; its actual centered discrepancy is `U-p_A sum_L w_f(L)`. This is an identity, NOT an all-g positive floor.

Define ordered original support-overlap `N_k(f)=sum_{|L∩M|=k}w_f(L)w_f(M)`. The exact globally-without-replacement physical A overlap kernel is derived from seven 70x70 local physical 2-factor tables `T[t,k]`, `P_k(a)=C(a,6)sum_t C(6,t)C(a-6,6-t)T[t,k]`, `q_k(a)=k!(6-k)!²P_k(a)/(C(a,2))_(12-k)`. **Theorem (all h):** `E_g U²=sum_k N_k q_k`, `Var=E_g U²-(p_A sum_L w_f(L))²` for UNIFORMLY random complete right g. No unproved independence even at k=0.

**Genuine W32 fixed-label and exact moments:** lex/reverse have W=209, mean 38/13, variance **4074526/1366365**, observed 4/0; S68/S72 W=297, mean 54/13, variance **2176652/455455**, observed 0/2. ALL four right maps occupy all 15 physical pair edges of K6, so each has **70 physical right A-factors** available: the actual zero in reverse/S68 is weighted ORIGINAL GQ support / right A-mask anti-alignment, not missing physical A targets. Exact Paley–Zygmund conditional lower probabilities of positive U are **5837370/7874633** (~74.13%) for lex/reverse and **1964655/2508818** (~78.31%) for S68/S72; these are random-right guarantees ONLY.

**Independent hosted contract:** [D6-N #38375743633](https://github.com/definitely-stable/Mathlab/actions/runs/38375743633) SUCCESS (6 independent test methods; direct physical K6/K7 six-edge A census, independent GQ point/line sixset selection, set/bitmask overlap checks and fixed-g zero controls). [INDEX #38375743543](https://github.com/definitely-stable/Mathlab/actions/runs/38375743543) SUCCESS, [Proof Audit #38375743542](https://github.com/definitely-stable/Mathlab/actions/runs/38375743542) SUCCESS. Full Research #38375743523 remains pending at this comment. Independent peer mathematics review OPEN. Keep PR Draft; do NOT merge yet.

**Next mathematical obstruction:** quantify the JOINT deterministic correlation across all accepted GF5-positive seven families with genuine original incident-support overlap and physical A/B/C masks, including B/A–C/A cross-covariances, or construct an explicit infinite coherent suppressing family. A second moment and a finite zero of one directed class are neither Branch A nor Branch B. No full W34/W38 seven-S, no ASET exponent. [Proof, exact formulas and nonclaims](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6n-exact-ca-correlated-overlap/docs/research/HYP-105-ISSUE230-D6N-EXACT-CORRELATED-CA-OVERLAP.md).

---

## Comment 135 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6143151482
- GitHub comment ID: 6143151482

### HYP-105 / #230 — D6-O exact ORIGINAL B-left/A-right + C-left/A-right joint correlation (2026-10-13)

Created strictly stacked [Draft PR #414](https://github.com/definitely-stable/Mathlab/pull/414) on fully CI-green D6-N [#413](https://github.com/definitely-stable/Mathlab/pull/413) parent HEAD `427db12b40cd498efc9e21b2e5fa07c89da42c54`. Child pinned HEAD `5ae0578af4f11a8e2eacb8c42afda05a891c9562`. Main untouched; #230/#176/#169 remain OPEN. PR Draft, no merge.

**New exact all-finite-h mixed GF5-positive theorem:** For every fixed globally injective ORIGINAL W(3,s) left pair map f, define original six-right-line support weights `w_B(L), w_C(L)` for distinct ORIGINAL six-incidence subsets with left physical B/C and six DISTINCT ORIGINAL right line factors. The sets of ORIGINAL sixsets are disjoint by physical left type, but can share the same right-line support. For ANY fixed globally injective right g both use exactly the SAME right A indicator `A_g(L)`:

`U_B=sum_L w_B(L)A_g(L)`, `U_C=sum_L w_C(L)A_g(L)`.

For uniform right g and D6-N exact physical joint 2-factor kernel `q_k(a)`, put `N_XY(k)=sum_{|L∩M|=k}w_X(L)w_Y(M)` (ordered). Then exactly `E[U_B U_C]=sum_k N_BC(k)q_k(a)`, `Cov(U_B,U_C)=sum_k N_BC(k)q_k(a)-p_A² W_B W_C`. Exact joint mean/variance follow for selected positive GF5 numerator `Y=45600 U_B+43320 U_C`; dividing expectation by `51^6` remains a right-RANDOM necessary selected-positive risk lower, **NOT** a full R3 upper or fixed-g lower.

**New exact sparse binomial inversion for original mixed spectra** (no O(#supports²) enumeration): `Z_X(T)=sum_{L⊇T}w_X(L)`, `M_r(X,Y)=sum_{|T|=r}Z_X(T)Z_Y(T)=sum_{k≥r}C(k,r)N_XY(k)`, `N_XY(k)=sum_{r≥k}(-1)^(r-k)C(r,k)M_r(X,Y)`. Cost 64 sparse sub-support updates per nonzero six-line L, with exact integral nonnegativity and conservation checks. A second fully independent finite W32 direct O(support²) set-intersection oracle validates all seven ranks, including B/C cross.

**TRUE W32 original finite evidence from dedicated hosted CI #38380663741, SUCCESS, 6/6 test methods:** lex: B distinct-original-right lifts 5000, C 209, ACTUAL fixed right B/A=98, C/A directional=4, cross covariance exactly **8704054/1366365**; reverse: same left f and same covariance, B/A=77, C/A directional=0; S68: B lifts 6098, C 297, actual B/A=44, C/A=0, covariance **6438466/455455**; S72: same left-side moments, observed B/A=36,C/A=2. Full genuine seven-family S separately verified 259/169/68/72; directional classes contained without double count. Independent original point/line generator, accepted seven-GF5 class classifier, direct mixed overlap spectrum, prior D6-N C variance all agree.

**Right-RANDOM finite Paley–Zygmund joint nonzero B/C probability lower**: lex/reverse `19943255535/20391115316` (~97.80%); S68/S72 `60117156750/61572718493` (~97.64%). These are NOT minimum over all g. Positive mixed covariance in these W32 examples is observed exactly and must NOT be extrapolated as universal all-h positivity of covariance.

**CI final HEAD at posting:** [D6-O dedicated Contract #38380663741](https://github.com/definitely-stable/Mathlab/actions/runs/38380663741) SUCCESS; [INDEX #38380663632](https://github.com/definitely-stable/Mathlab/actions/runs/38380663632) SUCCESS; [Proof Audit #38380663734](https://github.com/definitely-stable/Mathlab/actions/runs/38380663734) SUCCESS; full Research [#38380663715](https://github.com/definitely-stable/Mathlab/actions/runs/38380663715) in progress. Independent math peer review OPEN. Keep Draft and all issues OPEN.

**Next D6-P genuine all-g barrier:** joint deterministic support/physical-mask anti-avoidance across all seven accepted ORIGINAL positive classes, including opposite A-left/B-right, A-left/C-right and C/B, B/B, D6, on the SAME globally coherent (f,g). Another random-right moment or generic Hall reduction is insufficient; either uniform all-h Omega(s^6) joint intersection bound or explicit coherent infinite suppressed family is required. W34/W38 complete seven-positive S remains UNKNOWN. [Proof and constraints](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6o-joint-ba-ca-covariance/docs/research/HYP-105-ISSUE230-D6O-JOINT-BA-CA-COVARIANCE.md).

---

## Comment 136 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6143196606
- GitHub comment ID: 6143196606

### D6-O exact-head regression pin update (2026-10-13)

After the initial six-method hosted PASS, the true-W32 original values were pinned explicitly as regression expectations in the **independent test**, so any later changes to B/C-support multiplicities, GF5 accepted class counts, mixed covariance, full seven-S, or exact Paley–Zygmund probability will fail closed.

**Current actual PR #414 HEAD:** `0c8343865b4339da0e54f881801c2c057ea5aeb8` (stacked on D6-N #413 HEAD `427db12b40cd498efc9e21b2e5fa07c89da42c54`; `main` unchanged).

Final-head [D6-O dedicated Contract #38381075156](https://github.com/definitely-stable/Mathlab/actions/runs/38381075156) SUCCESS, [INDEX #38381075067](https://github.com/definitely-stable/Mathlab/actions/runs/38381075067) SUCCESS. [Proof Audit #38381075022](https://github.com/definitely-stable/Mathlab/actions/runs/38381075022) and [full Research #38381074988](https://github.com/definitely-stable/Mathlab/actions/runs/38381074988) were in progress at this check; do not claim all-four-green acceptance yet. Independent mathematical review still OPEN; #230/#176/#169 OPEN; PR remains Draft.

Pinned W32 original values: lex B=5000,C=209,actual B/A=98,C/A=4,S=259; reverse 5000,209,77,0,169; S68 6098,297,44,0,68; S72 6098,297,36,2,72. Exact cross cov lex/reverse 8704054/1366365; S68/S72 6438466/455455. Exact joint right-random positive PZ bounds lex/reverse 19943255535/20391115316; S68/S72 60117156750/61572718493. **All finite controls only**; no Branch A/B claim.

---

## Comment 137 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6143671280
- GitHub comment ID: 6143671280

### HYP-105 #230 / D6-P — deterministic all-seven ORIGINAL right-cylinder/label-swap boundary (2026-10-13)

Created [Draft PR #415](https://github.com/definitely-stable/Mathlab/pull/415) strictly stacked on **all-four-CI-green** D6-O Draft [#414](https://github.com/definitely-stable/Mathlab/pull/414), parent HEAD `0c8343865b4339da0e54f881801c2c057ea5aeb8`. Latest D6-P HEAD `d3ef69ee5213a8ecd3880203d2f24fce565caad8`; main unchanged `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`. #230/#176/#169 remain OPEN; no mergers.

**Exact all-finite-h deterministic original-cylinder identity (model-equivalent, not a nontrivial lower bound):** each ORIGINAL six-incidence set with valid LEFT physical A/B/C projection is grouped by its right ORIGINAL factor IDs **in immutable incidence positions**, preserving repeated original right lines, its left kind, the connected left A column dual (for D6), and repeated left B original-point incidence positions (for B/B). The weight `m_f(tau)` counts truly DISTINCT original incidence sixsets. For every complete correlated globally injective pair f,g, `S_seven(f,g)=sum_tau m_f(tau)1[chi_tau(g) in seven accepted positive GF5 classes]`. The fixed-map previously certified seven-class necessary GF5 R3 lower numerator is the same sum weighted by the frozen class-specific coefficients. Classifier includes BOTH A/B and C/A/C/B orientations, BB overlap/disjoint and aligned D6.

**Why D6-N/O six-original-line support alone cannot be extended unmodified:** A/A D6 requires identical connected column-dual C6 pairings in the six original incidence positions; B/B requires the overlap of repeated ORIGINAL point and line *incidence positions*. A synthetic 6-column physical A/A cycle demonstrates that swapping right physical labels of TWO right lines already present keeps their unordered six right physical pair edges invariant but can toggle D6. This refutes the overly broad 'both-present swap does nothing' rule; that sharpening remains true for the directional B-left/A-right and C-left/A-right subsets only.

**Exact all-h right-transposition delta formula:** for any two original right lines u≠v, only cylinders whose ordered right originals contain u or v can change their accepted tag. Sum weighted before/after indicators over this original-line-inverted boundary for exact `Delta_uv S_seven` and selected GF5 numerator change; retain both-present cylinders for D6. No O(s^6) all-g floor follows.

**Finite original W(3,2) evidence:** compile exactly 62,370 original left-selected sixsets (A=51,030, B=10,935, C=405) for each of lex/reverse/S68/S72. New independent right-column-cylinder classifier and source full seven-GF5 original classifier agree on all seven counts, total S and weighted necessary GF5 floor. Selected global right-line swaps independently agree with complete ORIGINAL sixset re-enumeration for each class, S and GF5 floor. Full set of 105 right-line transpositions per W32 map is evaluated by exact original-cylinder local deltas in the dedicated contract.

**Important new finite falsifier against unjustified swap-descent assumptions:** initial hosted independent test revealed that for at least one true W32 map the least `Delta_uv S` among ALL 105 single right-label swaps is **+7**. Thus an arbitrary right g may be a STRICT one-swap local minimum, and the test's prior assumption `min Delta<=0` was FALSE (not a failure of cylinder identity). Corrected CI records `strict_right_one_swap_local_minimum` and actual minimum-delta pair without assuming existence of a descent move. This is finite only, and local minimum does NOT imply global optimality.

**Acceptance checkpoint:** first hosted D6-P workflow #38383735789 failed **only** the unsound 'every g has nonpositive swap' test assertion; five other original/classifier/swap tests passed, including independent complete recount and synthetic D6 positional counterexample. Following fail-closed correction and reduced duplicate CI work, final exact-head [D6-P Contract #38384349551](https://github.com/definitely-stable/Mathlab/actions/runs/38384349551), [INDEX #38384349442](https://github.com/definitely-stable/Mathlab/actions/runs/38384349442), [Proof Audit #38384349451](https://github.com/definitely-stable/Mathlab/actions/runs/38384349451) and [full Research #38384349518](https://github.com/definitely-stable/Mathlab/actions/runs/38384349518) remain the active required acceptance checks; INDEX green, other status to be verified after completion. Independent mathematical review remains OPEN. Keep PR Draft, no merge, all root issues OPEN.

**Next genuine mathematical gap D6-Q:** an ALL-h deterministic **anti-avoidance** inequality for the sum of all seven accepted original-cylinder indicators over EVERY correlated complete global f,g, or an explicit infinite coherent suppressing family with sub-s^6 S. The cylinder equality and local swap diagnostics alone do not close A/B, do not give full R3 upper or an ASET exponent. [Detailed proof/limitations](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6p-seven-cylinder-swap-audit/docs/research/HYP-105-ISSUE230-D6P-SEVEN-CYLINDER-SWAP-AUDIT.md).

---

## Comment 138 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6143722071
- GitHub comment ID: 6143722071

### D6-P #415 — exact final-head 105-swap ORIGINAL W32 results (2026-10-13)

Final pinned D6-P HEAD `d3ef69ee5213a8ecd3880203d2f24fce565caad8`. [Dedicated hosted Contract #38384349551](https://github.com/definitely-stable/Mathlab/actions/runs/38384349551) **SUCCESS**, six independent unit-test methods passed in 36.3s, followed by ALL 105 right-original-line global pair-label transpositions for each of the four frozen real W(3,2) mappings (report 175.6s). [INDEX #38384349442](https://github.com/definitely-stable/Mathlab/actions/runs/38384349442) SUCCESS and [Proof Audit #38384349451](https://github.com/definitely-stable/Mathlab/actions/runs/38384349451) SUCCESS. [Full Research #38384349518](https://github.com/definitely-stable/Mathlab/actions/runs/38384349518) was still running (HYP105 foundation and exact census finished SUCCESS, remaining LENT foundation unit tests running) at check. Independent mathematical peer review OPEN.

**New independently original-GQ finite result — TWO strict right one-swap local minima:**

| ORIGINAL W32 maps | seven-S | exact right cylinders | decreasing swaps | equal swaps | increasing swaps | min ΔS | max ΔS | best ΔS transposition | min Δ selected GF5 risk numerator |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| lex | 259 | 57,950 | 92 | 0 | 13 | -83 | +47 | (2,11) | -3,280,649 |
| reverse | 169 | 57,950 | 56 | 3 | 46 | -41 | +34 | (4,13) | -1,824,013 |
| S68 | 68 | 53,875 | **0** | **0** | **105** | **+7** | +60 | (8,9) | **+313,640** |
| S72 | 72 | 53,875 | **0** | **0** | **105** | **+2** | +58 | (1,14) | **+98,450** |

All four rows checked against the accepted full seven ORIGINAL GF5 classifier at original right g; selected transpositions additionally checked by independent complete six-incidence set re-enumeration and per-class/weighted GF5 floor reconciliation. The exact all-105 swap deltas use the proven ORIGINAL-cylinder boundary identity.

**Conclusion:** S68 AND S72 are strict local minima against **every single transposition of two ORIGINAL right factor physical pair labels**, with fixed left map and exact ORIGINAL W(3,2), simultaneously for the unweighted seven-S and for the *selected necessary GF5 floor numerator* (all 105 weighted swap deltas positive). This is stronger than the preliminary failed-assumption observation of one +7 strict minimum. It definitively disproves any general lemma asserting that every fixed mapping admits a one-swap nonincrease. It is finite h=1 ONLY and does NOT prove global optimality, all-h correlated suppression or Branch B.

Keep #230/#176/#169 OPEN, PR #415 Draft, main untouched; D6-P is a RESTRICTED_THEOREM_C / model-equivalent exact certificate, not PROVED_A, not COUNTEREXAMPLE_B, and not full R3 upper. Next D6-Q needs a genuinely **global** all-seven anti-avoidance bound for all h and all f,g, or a coherent infinite family; one-swap descent is now conclusively falsified as a universal route.

---

## Comment 139 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6144103469
- GitHub comment ID: 6144103469

### HYP-105 #230 / D6-Q — all-seven fixed-right-IMAGE permutation-orbit transfer (2026-10-13)

Implemented [Draft PR #416](https://github.com/definitely-stable/Mathlab/pull/416), strictly stacked on four-GitHub-hosted-green [D6-P Draft #415](https://github.com/definitely-stable/Mathlab/pull/415), parent pinned HEAD `d3ef69ee5213a8ecd3880203d2f24fce565caad8`. D6-Q pinned HEAD `8fc40298c19459e344d0702560b5deafefe6b94e`; `main` untouched. Root #230/#176/#169 OPEN.

**New all-finite-h theorem Q1 (conditional on fixed f AND fixed physical right IMAGE E):** ORIGINAL GQ W(3,s), s=2^h, V original right line factors; minimal K_a alphabet with K=binom(a,2)>=V and E⊂E(K_a), |E|=V. Uniformly permute the V ORIGINAL right factor identities among the **same fixed set** E of occupied physical pair edges, without randomizing the missing physical edges. This differs from prior D6-M/O uniform injective right completion for h>1. Define physical counts F_A(E) of six-EDGE 2-factors, F_B(E) of a repeated physical pair edge + vertex-disjoint 4-cycle, F_C(E) of a three-edge matching, F_D(E) of 6-cycles. Exact right physical probabilities for original RIGHT multiplicity type A/B/C and aligned A/A D6:

`p_A(E)=6! F_A(E)/(V)_6`, `p_B(E)=4! F_B(E)/(V)_5`, `p_C(E)=3! F_C(E)/(V)_3`, `p_D6(E)=12 F_D(E)/(V)_6` (only when left column dual is a C6; disconnected left dual contributes D6=0). The 12 is the dihedral C6 automorphism count. D6-P incidence-position-aware ORIGINAL sixset cylinders give exact expectations of EACH of the seven accepted positive GF5 classes and their frozen weighted necessary R3 numerator in this fixed-image permutation orbit, including both C/A and C/B directions and B/B original repeated incidence overlap/disjoint. No independence assumptions and no full GF5 R3 upper.

**New deterministic all-h robustness Q2:** complete K_a has `F_A=70 C(a,6)`, `F_B=45 C(a,6)`, `F_C=15 C(a,6)`, `F_D=60 C(a,6)`. If m=K−V physical pairs are missing, for EVERY fixed E each family survives with `F_T(E)>=max(0,F_T(K_a)−m*e_T F_T(K_a)/K)`, with physical distinct pair counts e=(6,5,3,6). Proof: each physical K_a edge participates in exactly e_T F_T(K_a)/K shapes, count shape destructions by union bound. For original s=2^h and **minimal a**: h=1 => (a,V,K,m)=(6,15,15,0); for h>=2, a>=14 and m<=a−2, hence `6m/K<1`. Thus ALL FOUR right physical template types are present in EVERY admissible right physical IMAGE E, even with adversarial missing pairs.

**New all-h quantified image-robust conditional mean Q3:** for every original fixed complete left map f and every admissible right IMAGE E, the conditional orbit A probability is at least `(1−6m/K)*p_A(full K_a injection)`. Combining with the prior accepted D6-M lower `L_BC(s)` for B-left/A-right+C-left/A-right gives
`E_{g': im(g')=E} S_seven(f,g') >= (1−6m/K)*L_BC(s) = (455/3−o(1))*s^6` uniformly over **all f AND all fixed E**. This is a mathematically stricter quantifier than full random right completion but the expectation remains over random **assignment within E**. It does NOT imply `inf_{f,g} S>=c s^6`: special right permutations may be far below their image-orbit average.

**True ORIGINAL W32 independent hosted finite evidence** [dedicated Contract #38387199348](https://github.com/definitely-stable/Mathlab/actions/runs/38387199348) **SUCCESS**, 6/6 independent test methods, including brute K6/K7 physical shape enumeration and single-edge-deletion exactness, 6!/5!/3! separate physical permutation oracles for p_D6 etc, original seven-GF5 fixed-label independent classifier, and real W(3,4) physical right IMAGE shape bounds **WITHOUT** claiming full W34/W38 original S. For four W32 frozen complete maps, fixed-IMAGE right-orbit means for all seven families, versus actual fixed-right counts:
- lex: E[S]=**117558/715** (~164.42); actual S=259, signed discrepancy **+67627/715**; E[selected GF5 lower numerator]=**36957517188/5005**.
- reverse: same left f, same E[S] and GF5 expectation; actual S=169, discrepancy **+3277/715**.
- S68: E[S]=**870476/5005** (~173.92); actual S=68, discrepancy **−530136/5005**; E[selected GF5 lower numerator]=**38910916848/5005**.
- S72: same left f, same E[S] and GF5 expectation; actual S=72, discrepancy **−510116/5005**.
- K6 physical exact right probabilities p_A=2/143, p_B=3/1001, p_C=3/91, p_D6=1/5005.
The previous D6-P S68/S72 strict one-swap local minima are thus quantitatively **negative orbit-mean outliers** in the genuine original W32 finite setting, not evidence of all-h Branch B.

**Additional all-h host symbolic certificate values:** s2 (a6,V15,m0), s4 (a14,V85,m6), s8 (a35,V585,m10) exact positive fixed-IMAGE conditional mean lower certificate generated, without fabricating W34/W38 original seven-S.

**Acceptance at time of posting:** D6-Q HEAD `8fc40298c19459e344d0702560b5deafefe6b94e`: [dedicated Contract #38387199348](https://github.com/definitely-stable/Mathlab/actions/runs/38387199348) SUCCESS, [INDEX #38387199318](https://github.com/definitely-stable/Mathlab/actions/runs/38387199318) SUCCESS, [Proof Audit #38387199477](https://github.com/definitely-stable/Mathlab/actions/runs/38387199477) SUCCESS, [full Research #38387199329](https://github.com/definitely-stable/Mathlab/actions/runs/38387199329) in progress. Independent human mathematical peer review OPEN. Do NOT merge Draft or close #230/#176/#169.

**Next genuine D6-R root barrier:** prove deterministic anti-avoidance for the *worst* right-label assignment within EVERY fixed physical image orbit, uniform in all f,E, or construct an explicit coherent infinite original GQ family with S_s=o(s^6). Positive image-orbit means and finite negative outliers alone settle neither Branch A nor Branch B. Full R3 upper and ASET exponent remain unproved. [Proof and limitations](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6q-seven-class-exact-right-orbit/docs/research/HYP-105-ISSUE230-D6Q-SEVEN-RIGHT-IMAGE-ORBIT.md).

---

## Comment 140 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6144998893
- GitHub comment ID: 6144998893

### HYP-105 / #230 — D6-R exact all-seven disjoint-right-swap mixed Hessian and true W32 targeted two-exchange audit (2026-10-13)

Created [Draft PR #417](https://github.com/definitely-stable/Mathlab/pull/417), strictly stacked on all-four-GitHub-hosted-green D6-Q Draft [#416](https://github.com/definitely-stable/Mathlab/pull/416), parent HEAD `8fc40298c19459e344d0702560b5deafefe6b94e`. Current D6-R HEAD `fa81256cb105b1af8c16fe43297eb65ced15d0c6`. No main changes, #230/#176/#169 remain OPEN.

**ALL-finite-h deterministic exact theorem:** For arbitrary correlated full ORIGINAL W(3,s) left/right pair-label injections f,g and **disjoint** swaps σ=(u,v),τ=(w,z) of FOUR distinct ORIGINAL right-line identities, define the seven-positive count mixed Hessian `Hστ S(g)=S(g^(στ))−S(g^σ)−S(g^τ)+S(g)`. Under D6-P position-aware ORIGINAL six-incidence cylinder weights m_f(c), the four terms cancel for every cylinder NOT touching BOTH swap-support sets `Iσ∩Iτ`. Thus `Hστ S=Σ_{c∈Iσ∩Iτ}m_f(c)[χ_c(g^(στ))−χ_c(g^σ)−χ_c(g^τ)+χ_c(g)]`; exactly CLASSWISE across all seven certified GF5 sectors and for the previously accepted selected necessary GF5 numerator. `Δστ S=Δσ S+Δτ S+Hστ S`. Since every indicator is binary, `|Hστ S|<=2Mστ(f)` where M is the TRUE ORIGINAL cylinder multiplicity in the doubly touched shadow; similarly `|Hστ Y_GF5|<=103500Mστ(f)`. Strict single-swap local minima can only be escaped by this composition when `Hστ S<-(Δσ S+Δτ S)`. **The intersection-only formula is explicitly NOT claimed for overlapping swaps/3-cycles**, whose actions do not commute.

**Real ORIGINAL W32 hosted results:** [initial dedicated CI #38393223553](https://github.com/definitely-stable/Mathlab/actions/runs/38393223553) **SUCCESS** on implementation HEAD `ed37c0e03ba99f6c370f2942f8ab6eafb080d42a`. Six independently tested methods SUCCESS, checking source full seven ORIGINAL-incidence `seven_census` at g,g^σ,g^τ,g^(στ) for selected pairs, every one of seven Hessian class counts, total S, certified GF5 floor numerator, original-cylinder double shadow loads, disjointness and preservation of global right injection. Then performed an explicit deterministic TARGETED search: for each true-original W32 strict one-swap local minimum S68 and S72, rank all 105 singleton right-factor swaps by (ΔS, original IDs), choose **top K=12** minimal-ΔS moves, and test EVERY pair among those 12 whose four ORIGINAL factor IDs are distinct. This is NOT all disjoint two-swap moves or any overlapping 3-cycle.

| Real ORIGINAL map | S | minimum singleton ΔS | targeted disjoint pairs | negative Hessians | minimum Hessian | improved S within targeted pairs | improved selected GF5 floor within targeted pairs | BEST targeted ΔS | BEST targeted GF5 floor Δ numerator | best original pair |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| S68 | 68 | +7 | 49 | 19 | −14 | **0** | **0** | **+7** | +266353 | (1,13)+(10,12) |
| S72 | 72 | +2 | 45 | 19 | −15 | **0** | **0** | **+6** | +287590 | (3,7)+(0,1) |

At those best pairs Hessian is −13 and −15 respectively. Thus genuine ORIGINAL W32 shows substantial NEGATIVE two-swap interaction, but **insufficient to escape the two strict one-swap minima within this carefully bounded candidate subset**. This is a rigorous finite targeted non-escape, NOT all-pairs local optimality and NOT global optimality.

**Exact pinned regressions:** D6-R's hosted workflow and new documentation now fail closed on the above finite values (including exact best pairs and weighted GF5 changes). New final HEAD `fa81256cb105b1af8c16fe43297eb65ced15d0c6` restarted four checks: [D6-R dedicated #38393674322](https://github.com/definitely-stable/Mathlab/actions/runs/38393674322), [INDEX #38393674414](https://github.com/definitely-stable/Mathlab/actions/runs/38393674414), [Proof Audit #38393674491](https://github.com/definitely-stable/Mathlab/actions/runs/38393674491), [full Research #38393674376](https://github.com/definitely-stable/Mathlab/actions/runs/38393674376). Their final-head status must be explicitly rechecked before acceptance; initial CI success at previous SHA cannot be transferred automatically.

**Root barrier:** no all-h deterministic `inf_{f,g}S>=c s^6`, no infinite coherent o(s^6) suppressing family, no total R3 upper, no ASET exponent. Next meaningful stage D6-S: either (i) prove exact global all-label anti-avoidance across ALL seven ORIGINAL cylinder families (not just one-/two-swap moves), or (ii) give a rigorous coherent infinite counterfamily. A separate order-aware 3-cycle curvature formula and finite escape/non-escape tests may help diagnose local traps, but must not be confused with resolving Branch A/B. Human independent mathematics review OPEN. Keep #230/#176/#169 OPEN and PR Draft. [Formal proof](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6r-disjoint-swap-hessian/docs/research/HYP-105-ISSUE230-D6R-DISJOINT-SWAP-HESSIAN.md).

---

## Comment 141 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6145426255
- GitHub comment ID: 6145426255

### HYP-105 #230 / D6-S — exact all-h ordered 3-cycle transfer, true W32 910-cycle barrier and S72 escape (2026-10-13)

Created [Draft PR #418](https://github.com/definitely-stable/Mathlab/pull/418) stacked strictly on **four-CI-green D6-R** [#417](https://github.com/definitely-stable/Mathlab/pull/417), pinned parent HEAD `fa81256cb105b1af8c16fe43297eb65ced15d0c6`. Current D6-S child HEAD after independent regression pins and documentation `bd1e353228f124f21dc1c87f23ccae3610786543`. Main unchanged, root #230/#176/#169 OPEN, PR Draft.

**New all-finite-h deterministic ORIGINAL-cylinder theorem (model-equivalent):** For arbitrary globally injective complete ORIGINAL W(3,s) f,g and ANY right permutation pi moving ORIGINAL right line factor identities T, the exact seven-positive S change (and selected certified GF5 necessary lower numerator) is an ORIGINAL-incidence-position cylinder weighted sum only over cylinders touching T. For OVERLAPPING transpositions σ=(u,v),τ=(v,w), their order produces two different 3-cycles `g_plus` and `g_minus`. The ordered mixed difference `H_{σ then τ}=S(g_plus)−S(gσ)−S(gτ)+S(g)` is supported on Iτ, and decomposes into an intersection contribution over Iσ∩Iτ **PLUS a generally NONZERO transfer tail over Iτ\Iσ**. Reversing order gives Iσ support and the reverse tail. Their exact difference equals the order commutator `S(g_plus)−S(g_minus)`. For `M_T` the TRUE ORIGINAL six-incidence multiplicity of right cylinders meeting T, `|commutator S|<=M_T` and `|commutator selected GF5 necessary numerator|<=51750 M_T`. All seven certified classes, including positional D6 and B/B overlap/disjoint, are retained. Importing D6-R's *intersection-only* mixed Hessian to OVERLAPPING swaps is FALSE: synthetic explicit accepted B-left/A-right right cylinder with Iσ∩Iτ=∅ has forward H_S=+1 and H_GF5=+45600. Independent tests proved this falsifier and compared true ORIGINAL W32 full-seven `seven_census` under both orientation orders, all seven per-class changes, Hessians and GF5 weights.

**New COMPLETE finite h=1 three-factor-support result:** A complete TRUE W(3,2) right map has 15 original right line IDs, so `C(15,3)=455` different triple supports and exactly 2 oriented 3-cycles per triple = **910 legal complete globally injective right 3-cycles per frozen model**. The hosted D6-S initial [run #38395675172](https://github.com/definitely-stable/Mathlab/actions/runs/38395675172) **SUCCESS**: six independent full-original unit tests passed; two independent GitHub-hosted matrix jobs separately exhaustively enumerated all 910 cycles on S68 and S72 (1820 total), each also recomputing the full 105 original right single-swap strict-minimum checks.

| true ORIGINAL W32 scheme | baseline S | ALL 105 singleton swaps >0 | three-cycles ΔS<0 | ΔS=0 | ΔS>0 | GF5 selected numerator improving 3cycles | nonzero orientation order defects (triple supports) | best cycle and ΔS | best selected GF5 floor delta |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| **S68** | 68 | yes, min +7 | **0** | **0** | 910 | **0** | 445/455 | (3,11,12), forward: **+8** | **+317513** |
| **S72** | 72 | yes, min +2 | **1** | **0** | 909 | **1** | 449/455 | **(1,7,9), reverse: −4** | **−179530** |

**Important independent finite S72 three-cycle escape certificate:** for frozen true ORIGINAL W(3,2) S72, cyclically reassign physical right pair labels among original right lines (1,7,9) in REVERSE orientation, preserving f, ORIGINAL geometry, complete globally injective g and its entire physical pair-edge IMAGE. The full ORIGINAL six-incidence classifier independently gives `S:72→68`, selected GF5 necessary floor numerator decreases **179530**, and the exact per-seven-class count delta is `D6=0, B-left/A-right=+7, A-left/B-right=−9, C/A=−1, C/B=0, B/B-overlap=0, B/B-disjoint=−1`. This **falsifies S72 stability against all original right permutations moving ≤3 factors**, despite its strict 105/105 one-swap local minimum. Reaching count 68 does NOT prove identical final g to the frozen S68 map.

**Important positive finite S68 certificate:** the accepted D6-P exhaustive 105 single swaps and this D6-S exhaustive 910 oriented 3-cycles together cover EVERY nonidentity right label permutation with support at most THREE original line factor IDs. ALL 1015 of these moves strictly increase S68. Hence S68 is a strict **≤3-ORIGINAL-right-factor-support LOCAL minimum** with its left ORIGINAL f held fixed. This is NOT a global minimum among all permutations of 15 right factors and NOT an all-h bound for arbitrary f,g. The selected necessary GF5 floor numerator is nondecreasing under all 910 3-cycles (zero improving), and strictly increases under all 105 singleton swaps.

**Fail-closed pinned final-head CI:** D6-S final PR HEAD `bd1e353228f124f21dc1c87f23ccae3610786543` includes two new independent original full-seven GF5 witness recounts and exact regression pins for both 910-cycle counts, all orientation defect counts and concrete best witnesses. Four mandatory GitHub-hosted checks have restarted on FINAL HEAD: [dedicated D6-S #38396591150](https://github.com/definitely-stable/Mathlab/actions/runs/38396591150), [INDEX #38396591188](https://github.com/definitely-stable/Mathlab/actions/runs/38396591188), [Proof Audit #38396591202](https://github.com/definitely-stable/Mathlab/actions/runs/38396591202), [full Research #38396591282](https://github.com/definitely-stable/Mathlab/actions/runs/38396591282). Treat initial CI success at prior SHA as preliminary, not final acceptance. Human independent mathematics review still OPEN.

**Next nonlocal research gate:** D6-T must address permutations with >=4 ORIGINAL right factor support or global all-seven constraint/anti-avoidance certificates, and ultimately arbitrary f,g across ALL h. 3-factor-locality cannot imply global optimum; root Branch A (`inf_{f,g} S_s=Omega(s^6)`) and infinite correlated Branch B (`S_s=o(s^6)`) both remain OPEN, as do full R3 upper and ASET exponent. Keep issues OPEN and Draft unmerged. [Proof, exact quantifiers, finite controls](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6s-oriented-3cycle-commutator/docs/research/HYP-105-ISSUE230-D6S-ORIENTED-THREE-CYCLE-COMMUTATOR.md).

---

## Comment 142 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6146092637
- GitHub comment ID: 6146092637

### HYP-105 #230 / D6-T — globally sound two-sided assignment dual, ALL-h degree-one proof-method NO-GO, finite TRUE-original W32 exact conditional certificates (2026-10-13)

Created [Draft PR #419](https://github.com/definitely-stable/Mathlab/pull/419), STRICTLY stacked on **all-four-GitHub-hosted-green** D6-S [Draft #418](https://github.com/definitely-stable/Mathlab/pull/418), parent head `bd1e353228f124f21dc1c87f23ccae3610786543`. Final D6-T HEAD `126fb06d1c4d775bb241a7b3447df36299a38d34`, `main` unchanged. Root #230/#176/#169 OPEN; no merges or claimed ASET exponent.

**Theorem T1 — sound all-h global two-sided assignment certificate, not a positive bound by itself.** Each TRUE ORIGINAL distinct six-incidence subset Q contributes a nonnegative seven-GF5-positive factor `F_Q(f,g)` depending on <=6 ORIGINAL point labels and <=6 ORIGINAL line labels; two typed complete maps are separately globally injective into K_a physical pair edges, no random averages. For each factor's **complete locally injective truth table** on r<=12 original vertices, define `b_Q=min_phi F_Q(phi)` and `m_(Q,i,e)=min_{phi:phi_i=e}F_Q(phi)`. Then pointwise `F_Q(phi)>=b_Q+(1/r)sum_i[m_(Q,i,phi_i)-b_Q]`. Multiply by `D=lcm(1,...,12)=27720`, sum over **all** ORIGINAL six-incidence factors, and independently solve min-cost injective Hungarian assignments on all ORIGINAL left and all ORIGINAL right vertices. This gives the exact **feasible dual certificate** `S>= [D sum_Q b_Q + MinInjection(A_L) + MinInjection(A_R)]/D`, with the same proof for the certified nonnegative selected GF5 necessary risk numerator. The dual is independently verifiable and fail-closed on incomplete local truth tables; no full original high-h 12-site truth tables were fabricated. The original higher-order primal minimum is NOT equivalent to a minimum-cost linear assignment; the linear assignment is only the dual relaxation.

**Theorem T2 — critical ALL-h mathematical NO-GO for the unconditioned degree-one dual.** For ANY ORIGINAL six-incidence Q, ANY one original site i on either typed side, ANY prescribed physical pair label e, the OPPOSITE typed side can be locally injectively relabeled to make its six physical edges fail 2-regularity: if any original factor repeats >=3 times among six original incidences, physical vertex degree>=3 for every assignment; otherwise at least three opposite original factors are distinct, so map three to pair edges (0,1),(0,2),(0,3), forcing degree>=3 at coordinate 0, and injectively extend to all other original factors since a>=6 and K>=V. The opposite invalid physical projection makes the original GF5-positive contribution ZERO regardless of the prescribed single label. Thus **every** b_Q=0 and m_(Q,i,e)=0; the unrestricted two-sided degree-one certificate is **IDENTICALLY ZERO for ALL powers s=2^h**. This is a rigorous proof-method NO-GO, NOT `S_s(f,g)=0` and NOT a Branch B counterexample. A nontrivial global certificate must preserve stronger joint/cross-side information (pairing or higher local marginals, nonlocal geometric inequalities, etc.).

**True-original finite conditional W32 controls, initial dedicated hosted run #38400711139 SUCCESS for all eight independent unit tests and original report step (before added pins).** Freeze f and all ORIGINAL right factor labels outside T=(3,11,12) for S68 or T=(1,7,9) for S72; permute ONLY those three right factor labels among their exact currently occupied physical K6 edges (3!=6 globally injective maps). Use the exact D6-P incidence-position-aware original sixset cylinders to partition **ALL 62,370 ORIGINAL W32 left candidates** into <=8 original line support-intersection factor groups; independently evaluate complete locally injective truth tables for each group, recover all seven class counts and the certified weighted GF5 numerator for EACH of the six complete right maps, and compare with source original `seven_census` at baseline and the S72 reverse 3-cycle 72→68 witness. Synthetic global capacity witness yields true global min=dual=1 even though independent sitewise minima sum to 0; parity-frustration witness has true global min=1 but degree-one dual=0. Integer Hungarian checked against brute-force all injective assignments, positive/negative costs, fail-closed invalid tables. The ALL-h sitewise NO-GO is constructively verified against TRUE ORIGINAL W32 incidence left A/B/C profiles and a=6/14/35.

**Exact finite six-permutation values and rigorously certified dual gap:**
- True W32 **S68**, T=(3,11,12): exact six right-S counts `[68,83,92,76,108,82]` (permutation order 012,021,102,120,201,210), exact conditional min **68**, new locally verified **Hungarian global-injection dual lower 131/2=65.5**, certified integer S floor 66 (duality gap 5/2). Certified selected necessary GF5 numerator six values `[3112510,3706986,4227460,3430023,4940790,3741890]`, exact conditional minimum **3112510**, dual lower **2994550**, gap 117960.
- True W32 **S72**, T=(1,7,9): six right-S counts `[72,87,84,114,68,88]`, exact conditional min **68** from reverse triple image assignment 201, dual lower **121/2=60.5**, integer floor 61 (gap 15/2). Certified selected GF5 six values `[3283610,3937673,3830810,5203680,3104080,4017080]`, exact conditional minimum **3104080**, dual **2760940**, gap 343140. Source full ORIGINAL GF5 classifier rechecks `S:72→68`, selected GF5 necessary numerator decline 179530.

These are exactly scoped **fixed-f, 12-other-right-labels-frozen** finite suborbits. They are NOT the minimum over all 15! right permutations and NOT an all-f,g/h bound. The user-facing proof scope and numeric witness are [documented](https://github.com/definitely-stable/Mathlab/blob/research/hyp105-issue230-d6t-assignment-dual-certificate/docs/research/HYP-105-ISSUE230-D6T-GLOBAL-ASSIGNMENT-DUAL-NOGO.md).

**CI exact final HEAD `126fb06d1c4d775bb241a7b3447df36299a38d34`**: dedicated [D6-T Contract #38401165209](https://github.com/definitely-stable/Mathlab/actions/runs/38401165209) **SUCCESS** (the earlier pinned regression workflow run #38401015028 failed ONLY a wrong GF5 baseline report dictionary key; source algorithm, 8/8 independent tests and proof results unaffected; key corrected); [INDEX #38401165218](https://github.com/definitely-stable/Mathlab/actions/runs/38401165218) SUCCESS; [Proof Audit #38401165348](https://github.com/definitely-stable/Mathlab/actions/runs/38401165348) and [Full Research #38401165217](https://github.com/definitely-stable/Mathlab/actions/runs/38401165217) required final-head conclusions still to be verified. Independent mathematical review OPEN. PR Draft, no merge. Parent D6-S was all-four green.

**Next genuine Branch A/B gate D6-U:** T2 conclusively rules out the naive unconditional degree-one projected min dual. Must investigate at least genuinely higher-order or cross-side coupled ORIGINAL six-incidence assignment constraints, e.g. a precisely scoped second-level feasibility/dual system with a proven nonzero universal lower or an exact NO-GO, or construct a coherent infinite correlated suppressing family. Retain ORIGINAL column positions, ALL seven GF5-positive classes, global LEFT and RIGHT injections. Do NOT elevate conditional positivity, average-right mass, or W32 local minima to `inf_{f,g}S>=c s^6`. Neither root Branch A nor infinite Branch B is proved.

---

## Comment 143 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6146881737
- GitHub comment ID: 6146881737

### HYP-105 / issue #230 — D6-U all-h proper-scope GF5 conditional-minimum obstruction (2026-10-13)

Created strictly stacked [Draft PR #420](https://github.com/definitely-stable/Mathlab/pull/420) on all-four-CI-green D6-T [#419](https://github.com/definitely-stable/Mathlab/pull/419), exact base HEAD `126fb06d1c4d775bb241a7b3447df36299a38d34`. Latest child HEAD `c6c34e727a4b017880be7437afe4146b564f2e76`. `main` untouched; #230/#176/#169 remain OPEN.

**NEW ALL-h restricted theorem:** In ORIGINAL W(3,2^h), every unordered distinct six-incidence subset Q forms a bipartite six-edge FOREST (GQ girth eight), so Q has at least **seven distinct ORIGINAL typed factor vertices**. For any locally injective physical pair labels pinned on **ANY proper subset** of Q's ORIGINAL factors, including ALL pin subsets of size <=6, one can complete both typed assignments globally injectively so Q's positive seven-GF5 indicator is ZERO (and hence its selected certified nonnegative GF5 numerator is ZERO).

Constructive free-ORIGINAL-site lemma: if final free site appears 3+ times, its physical pair forces degree>=3; if twice, at least one of >=5 physical pair edges incident to an occupied coordinate is unused (only <=4 other incidence positions), so force degree>=3; if once, five fixed physical incidence columns have AT MOST ONE available pair-edge completion to six coordinates each degree two, whereas at least C(a,2)-5>=10 physical pairs remain. One can always choose a non-2-regular completion. Local injections extend to globally injective f,g because C(a,2)>=V.

**Exact scope / STOP criterion:** Every individual-Q proper-scope conditional **MINIMUM** is zero, for unweighted and weighted GF5 positive classes. Therefore no finite-order <=6 local-minimum potential (nor even any proper-scope individual-factor minimum) can furnish a positive universal certificate in the D6-T projected-minimum-only family. This DOES NOT rule out general Sherali–Adams, overlap-consistent pseudomarginals, nonseparable cross-Q dual inequalities, full-scope constraints, or the actual existence of a positive all-h minimum. Branch A/B OPEN, NOT an R3 upper or ASET exponent.

**Implemented:** theorem/proof document, constructive witness Python, independent 203 Bell(6) endpoint-multiplicity cases with adversarial pinned physical labels for a=6/14/35; true-original W(3,2) 45-incidence girth check, actual A/B/C original sixsets and positive seven-GF5 witnesses from S68/S72; fail-closed input validation. PR changed four files. First head had one independent-test spelling NameError; corrected in latest HEAD; all **6/6 dedicated tests pass**, dedicated Contract [run #38406558112](https://github.com/definitely-stable/Mathlab/actions/runs/38406558112) SUCCESS; INDEX [run #38406559012](https://github.com/definitely-stable/Mathlab/actions/runs/38406559012) SUCCESS. Proof Audit [#38406557543](https://github.com/definitely-stable/Mathlab/actions/runs/38406557543) and Full Research [#38406558562](https://github.com/definitely-stable/Mathlab/actions/runs/38406558562) RUNNING at this timestamp; do NOT claim 4/4 acceptance until they complete. Independent mathematical review remains OPEN.

**Next mathematically justified step:** a globally coupled constraint that uses interactions/consistency across multiple original sixsets, not the unconditional conditional MINIMUM tables of individual Q. No merge; no main changes.

---

## Comment 144 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6147420680
- GitHub comment ID: 6147420680

### HYP-105 / #230 — D6-V all-h bounded coupled-cluster STAR obstruction + true W32 exact cluster certificates (2026-10-13)

Created strictly stacked [Draft PR #421](https://github.com/definitely-stable/Mathlab/pull/421) on fully four-GitHub-hosted-green D6-U [#420](https://github.com/definitely-stable/Mathlab/pull/420) parent HEAD `c6c34e727a4b017880be7437afe4146b564f2e76`. Current D6-V exact HEAD `0c1023894ba239ed1c53d5c84356d8e9f839b8a9`. Main untouched; #230/#176/#169 remain OPEN. No merges.

**NEW ALL-h THEOREM V1 (joint rather than single-Q zero):** Let C be ANY collection of ORIGINAL six-incidence sets of W(3,s), s=2^h. If **either** its union of ORIGINAL point factors **or** of ORIGINAL line factors has cardinality <=a-1, with a=min{a:C(a,2)>=(s+1)(s²+1)}, there is ONE **complete globally injective** correlated pair f,g making **EVERY** seven-positive GF5 contribution in C zero, likewise its selected nonnegative necessary GF5 numerator. Proof: injectively map that typed factor union to edges (0,1),...,(0,a-1) of the same K_a star. Every six-incidence physical projection on that side has coordinate zero of degree SIX, incompatible with degree two; extend the typed injection to all V original sites via unused edges and complete other side arbitrarily. No independence, loss of incidence positions or symmetry.

**ALL-h COROLLARY V2 (sharp method-scope necessary threshold):** any cluster C with |C|<=floor((a-1)/6) has both ORIGINAL typed factor unions <=a-1, hence min_{f,g} sum_{Q in C} chi_Q=0. Since a=(sqrt2+o(1))s^(3/2), any independent UNCONDITIONED cluster-minimum block able even possibly to be positive must have at least ceil(a/6)=Omega(s^(3/2)) original sixsets (necessary NOT sufficient). This only rules out *independent block minimum* certificates at uniformly bounded sixset-cluster size, **NOT** general Sherali–Adams, nonlocal cross-block consistency, SOS, or Branch A.

**EXACT coupled finite theorem V3:** Partition exact nonnegative complete original-factor truth tables into disjoint blocks of factor indices, jointly minimize each block over the **union** of ORIGINAL typed sites (injectively on each side), sum their minima. For each block this is a valid exact lower bound on any complete original injection. Bitmask DP over partitions at block sizes <=1/2/3 yields monotone sound lower certificates. Validated against independently enumerated global injective primal controls; fail-closed incomplete tables, illegal rows and objective sign/type checks. Synthetic two complementary parity cost factors each have min zero but coupled min one.

**TRUE ORIGINAL W32 seven-GF5 conditional replay:** Using all 62,370 ORIGINAL left-selected incidence sixsets via D6-T exact incidence-position-aware U=R(Q)∩T right-cylinder factors (<=8 groups), freeze f and other 12 right ORIGINAL physical labels, enumerate all six genuine globally injective permutations of the remaining three lines. Exact cluster lower bounds:

| scheme/objective | singleton clusters | <=2 factors per cluster | <=3 factors per cluster | exact six-permutation min |
|---|---:|---:|---:|---:|
| S68 seven S | 54 | 65 | **68** | 68 |
| S72 seven S | 58 | 59 | **67** | 68 |
| S68 selected GF5 numerator | 2,466,190 | 2,932,293 | **3,112,510** | 3,112,510 |
| S72 selected GF5 numerator | 2,641,340 | 2,689,220 | **3,056,200** | 3,104,080 |

**These are finite CONDITIONED certificates, NOT root all-f,g bounds**. The S68 triple-cluster partition closes both conditional duality gaps, while S72 still has 1 / 47,880 conditional gaps. They demonstrate genuine utility of coupled constraints AFTER enough original labels are frozen, consistent with all-h unconditioned star no-go.

**Hosted acceptance at posting:** exact-head [Dedicated D6-V Contract #38410329413](https://github.com/definitely-stable/Mathlab/actions/runs/38410329413) **SUCCESS (7/7 tests + machine-readable numerical pin)**, [INDEX #38410329754](https://github.com/definitely-stable/Mathlab/actions/runs/38410329754) **SUCCESS**, [Proof Audit #38410330293](https://github.com/definitely-stable/Mathlab/actions/runs/38410330293) **SUCCESS**. [Full Research #38410329620](https://github.com/definitely-stable/Mathlab/actions/runs/38410329620) **IN PROGRESS**. Independent mathematical review OPEN, PR remains Draft. No claim of four-green until full Research completes.

**Next appropriate D6-W:** consider actual cross-cluster overlapping-original-site marginal consistency / nonseparable dual inequalities, not sums of bounded-size independent cluster minima. A positive root proof requires an all-h statement for arbitrary correlated complete f,g.

---

## Comment 145 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6147782937
- GitHub comment ID: 6147782937

### HYP-105 / issue #230 — D6-W exact overlap-consistent typed separator marginal dual (2026-10-13)

Created STRICTLY stacked [Draft PR #422](https://github.com/definitely-stable/Mathlab/pull/422) on [D6-V #421](https://github.com/definitely-stable/Mathlab/pull/421), parent pinned HEAD `0c1023894ba239ed1c53d5c84356d8e9f839b8a9` (now 4/4 GitHub-hosted CI SUCCESS). Latest D6-W head `fcb2556afd6045c95e5959105296d3a025bd2f3b`. No main changes, no merges, #230/#176/#169 OPEN.

**NEW W1 all-finite-h sound theorem — exact signed separator reparameterization.** Given COMPLETE truthful nonnegative ORIGINAL six-incidence GF5-positive local factor tables, choose signed INTEGER functions `theta_(Q,T)(eta_T)` on typed ORIGINAL point/line separator subsets T of size 0,1,2, satisfying `sum_Q theta_(Q,T)(eta_T)=0` for EVERY locally injective typed physical image tuple. Define shifted local costs `G_Q=F_Q+sum_T theta_(Q,T)` (G may be NEGATIVE). Then for ALL correlated globally injective original f,g, `sum_Q F_Q(f,g)=sum_Q G_Q(f,g)>=sum_Q min G_Q`. The implementation enumerates and verifies every complete local truth row, every separator image tuple and pointwise cancellation, including mixed ORIGINAL point-line separators. This is a globally sound *certificate interface* if truthful tables/messages are supplied, NOT an assertion a positive all-h root bound has been found.

**New independent exact one-site pseudomarginal obstruction** (synthetic, NOT original-GQ all-h): on three original sites bijectively assigned three physical pair images, two complementary permutation-parity factors sum identically to 1. Each individually has min 0; their uniform zero-cost distributions have IDENTICAL one-site marginals (each 1/3) but incompatible two-site marginals. Hence one-site local-consistency lower relaxation can be exactly 0 while the true optimum is 1. The signed pair-separator certificate closes this exact gap to 1.

**W2 exact genuine ORIGINAL W32 CONDITIONAL closure:** original f and 12 of 15 right ORIGINAL factors frozen, remaining right triple T=(3,11,12) for S68 or T=(1,7,9) for S72 allowed ALL six bijections onto its three original occupied physical pair images. D6-T original incidence-position-aware grouped factors account for ALL 62,370 original left-selected six-incidence candidates and all seven accepted GF5 classes (D6 physical column alignment; B/B incidence-position overlap/disjoint; both directional classes), independently verified against original seven_census. Add an EXPLICIT zero-cost FULL-three-site ANCHOR region; for a 3-to-3 bijection, the assignments of two originals determine the third. Therefore transfers on separators of size <=2 shift EVERY original conditional factor to zero, leaving the full objective on the anchor. Checked 3! assignments for pointwise original-vs-shifted equality, global original right injection and exact dual/primal equality.

| Real ORIGINAL W32 conditioned objective | D6-V <=3-factor lower | D6-W exact two-site separator dual | exact 6-state primal | gain |
|---|---:|---:|---:|---:|
| S68 seven-S | 68 | 68 | 68 | 0 |
| S72 seven-S | 67 | **68** | 68 | +1 |
| S68 selected nonnegative GF5 numerator | 3,112,510 | 3,112,510 | 3,112,510 | 0 |
| S72 selected nonnegative GF5 numerator | 3,056,200 | **3,104,080** | 3,104,080 | +47,880 |

**Important scope:** the full-three-site anchor plus SATURATED right three-label image and frozen complete left/12 right images are mandatory; this does NOT claim generic rank-two Sherali–Adams exactness, arbitrary ORIGINAL full f/g root lower, Branch A or B, full R3 upper, or an ASET exponent. Mathematical title of a general SA hierarchy not invoked as a proved property.

**Acceptance latest exact head `fcb2556afd6045c95e5959105296d3a025bd2f3b` at posting:** [D6-W dedicated #38412894570](https://github.com/definitely-stable/Mathlab/actions/runs/38412894570) SUCCESS, [INDEX #38412893996](https://github.com/definitely-stable/Mathlab/actions/runs/38412893996) SUCCESS; [Proof Audit #38412895271](https://github.com/definitely-stable/Mathlab/actions/runs/38412895271) IN PROGRESS; [Full Research #38412893347](https://github.com/definitely-stable/Mathlab/actions/runs/38412893347) QUEUED. Initial implementation before final minor dead-branch cleanup also had dedicated 6/6 tests PASS and original numerical pins. Independent mathematical review OPEN. No merge; do not claim 4/4 acceptance until verified.

**Next D6-X:** find nontrivial VERIFIED nonseparable separator messages on arbitrary original f,g without frozen images or a three-site saturated anchor, across all s=2^h. D6-V star obstruction eliminates unconditioned fixed-size independent clusters; mere enlargement of tiny W32 right-permutation orbits cannot resolve Branch A.

---

## Comment 146 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6148562073
- GitHub comment ID: 6148562073

### HYP-105 / #230 — JPKC-001 same-map projection–Kikuchi coupling (2026-10-13)

Created strictly stacked **[Draft PR #423](https://github.com/definitely-stable/Mathlab/pull/423)** on [#394](https://github.com/definitely-stable/Mathlab/pull/394) at parent `aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d`. Latest head `d0d8e6ce428720050de5239e42a635b72ba9c1c7`. **main unchanged; no merge; root A/B remain OPEN.**

**New restricted all-h conditional necessity J1.** For ANY unbounded sequence of complete globally coherent original W(3,2^h) point/line pair injections with `S=o(s^6)`, the SAME maps necessarily obey:
`B_G >= (16-o(1))s^6` (FULL G original nonincident blocked physical P3, distinct from PR #394 retained `C_H=E_H+I_H`) and `Theta(G)+12 C6_improper(G) >= (48-o(1))s^6`. Proof combines #394 universal retained-path and incident-book theorem with exact Kikuchi K2 and AHL path floor, using #394 `M2(G)=O(s^(11/2))` to make triangles negligible.

**Exact variance identity J2, crucial method warning.** For every finite graph,
`12D6 = [L(P3)-Theta-12 C6_improper] + [sum_(u,v) p_uv^2-P3^2/a^4]`.
The last bracket is nonnegative endpoint-path variance: the raw scalar K2 Cauchy–Schwarz branch discards it. Real W32 and W34 examples have negative scalar K margin despite positive D6. Therefore a future proof cannot assume this margin positive without a new variance/weighted-fiber argument. This does NOT disprove root A.

**Implemented:** 5 files: original same-f/g projection and independent Kikuchi exact ledger; independently constructed symplectic-spread D4 TRUE original complete point/line pair maps on GF4/GF8; 8 dedicated tests including W32 lex/reverse/S68/S72, W34 lex/random, W34 spread full joint and W38 spread graph-only energy; focused GitHub-hosted workflow and mathematical report. All original C6 are independently enumerated as a falsifier of K2; proper D6 and synchronized B/B are checked against the ORIGINAL seven-census on W32. Explicit finite/retained/full graph and budget boundaries.

**CI at writing:** Dedicated [run #38418418317](https://github.com/definitely-stable/Mathlab/actions/runs/38418418317) SUCCESS on final exact HEAD, INDEX [#38418418471](https://github.com/definitely-stable/Mathlab/actions/runs/38418418471) SUCCESS. Proof Audit [#38418418421](https://github.com/definitely-stable/Mathlab/actions/runs/38418418421) and Full Research [#38418419689](https://github.com/definitely-stable/Mathlab/actions/runs/38418419689) were RUNNING; do NOT claim 4/4 until verified. Independent mathematical proof review remains OPEN.

**Next allowed research:** original-incidence-preserving cross-witness taxonomy between blocked q-l-p-r closures, K2 weighted endpoint variance, improper cycles and OTHER accepted GF5 classes. Test a noncircular global compensation estimate; D6-W messages only after truthful same-scope factors exist. No branch A/B claim, no improved ASET exponent.

---

## Comment 147 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6148580866
- GitHub comment ID: 6148580866

### HYP-105 / issue #230 — D6-X all-h projective zero-GF5 pseudomarginals, unanchored separator dual NO-GO and exact lifted physical capacity falsifier (2026-10-13)

Created [Draft PR #424](https://github.com/definitely-stable/Mathlab/pull/424) STRICTLY stacked on all-four-CI-green D6-W [#422](https://github.com/definitely-stable/Mathlab/pull/422), parent HEAD `fcb2556afd6045c95e5959105296d3a025bd2f3b`. Current child HEAD **`893f590cc583c7a23a402ad9cf856b780219699f`**. Main untouched; #230/#176/#169 OPEN; no merges.

**X1 — all-h projective star-zero theorem (h>=2).** For ORIGINAL W(3,s), s=2^h, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}>=14, construct on every typed ORIGINAL factor scope U with |U|<=a-1 a mutually projectively CONSISTENT locally injective probability law. Choose a UNIFORM physical center c; assign ORIGINAL point factors injectively and uniformly to different physical star edges (c,j); independently assign ORIGINAL line factors uniformly injectively to all K=C(a,2) physical pair edges. Forgetting factors projects exactly to the corresponding local law on every subset. Every ORIGINAL six-incidence Q has scope <=12<=a-1 and its left physical center c occurs in ALL SIX original incidence positions (including original repeated-point multiplicities). Thus its left physical projection is not six-coordinate 2-regular and **all seven accepted GF5-positive indicators have expected cost ZERO**, as does the certified selected nonnegative GF5 numerator.

The closed-form k-point marginal probability for ordered injective physical edges e_1..e_k is |intersection of their endpoint sets|/[a (a-1)_k]; zero for repeated edges, 1 at k=0. This permits exact Fraction-based verification without floating point or invented W34 full seven-census.

**X3 — NEW all-h NO-GO for an entire unanchored D6-W-style local separator dual family.** Let F_Q be the COMPLETE true ORIGINAL sixset positive GF5 costs, and add any balanced signed typed ORIGINAL separator message functions theta_(Q,T), with |T|<=a-1, and with NO additional lifted global physical column capacity restrictions / full-V anchor. The projective local star family has E[F_Q]=0 on every Q; overlap consistency and pointwise balancing give sum_Q E[theta_(Q,T)]=0 on each T. Hence for the shifted local factors G_Q: `sum_Q min_local G_Q <= sum_Q E_mu G_Q = 0`. Therefore **NO CHOICE of such unanchored separator-only messages can certify positive root S**, even with growing region rank a-1=Theta(s^(3/2)). This is a precise method-class theorem; it does NOT say general Sherali–Adams/SOS fails.

**X2 — exact global occupancy cut proves WHY the projective pseudo is not a genuine global map or standard SA pseudo.** For any two DIFFERENT physical pair edges e=(0,1), e'=(0,2) and an original point p, every valid complete injection x satisfies
`x_(p,e)*(1-sum_(q!=p)x_(q,e'))>=0`.
Under the local star pseudolaw, `E[x_(p,e)]=1/K`, `E[x_(p,e)x_(q,e')]=1/[a(a-1)(a-2)]`, and the conditional expected occupancy of e' by other points is `(V-1)/(2(a-2))>1` for all h, using the exact minimal-K property `V-1>=C(a-1,2)>2(a-2)`. Thus this VALID rank-two lifted physical-column capacity cut has strictly **NEGATIVE** pseudomarginal expectation. It excludes the star pseudo already at a two-site lift, so it is **NOT** a counterexample to standard Sherali–Adams feasibility.

On true W(3,4), `(a,V,K)=(14,85,91)`: unlifted E(column occupancy)=85/91<=1, conditional occupancy=7/2>1, exact lifted slack=**-5/182**, independent direct combinatorial two-site census agrees.

**Independent hosted evidence on final HEAD**: [Dedicated D6-X Contract #38418531396](https://github.com/definitely-stable/Mathlab/actions/runs/38418531396) SUCCESS, **8/8 test methods**, including full ORIGINAL W(3,4) / W(3,8) incidence membership + point multiplicity patterns; exact all-center/spoke enumeration for (a,k)=(7,4) and (14,3) and ALL proper subset projections (2520 and 24024 states); separate rank-two enumeration and minimal physical alphabet s=2..256; fail-closed invalid tuples, scopes and budgets; algebraic X3 proof checksum and false-SA-claim guard. [INDEX #38418531423](https://github.com/definitely-stable/Mathlab/actions/runs/38418531423) SUCCESS, [Proof Audit #38418531676](https://github.com/definitely-stable/Mathlab/actions/runs/38418531676) SUCCESS, [Full Research #38418531473](https://github.com/definitely-stable/Mathlab/actions/runs/38418531473) PENDING at posting. Independent mathematical review OPEN. **3/4 CI GREEN**, not yet final acceptance.

**Strict outcome RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER**: no Branch A Omega(s^6), no Branch B coherent infinite full f/g witnesses, no all-R3 upper, no ASET exponent. D6-Y must include the lifted global assignment occupancy constraints together with original GF5 sixset factors and overlap consistency. The older independent-cluster and unanchored separator-only proof routes now have rigorous all-h STOP criteria; do not increase W32 tiny orbit search.

---

## Comment 148 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6149213668
- GitHub comment ID: 6149213668

### HYP-105 / issue #230 — D6-Y sharp physical IMAGE adjacency capacity specialization + exact selected lifted-column marginal gap (2026-10-13)

Created strictly stacked [Draft PR #425](https://github.com/definitely-stable/Mathlab/pull/425) on [D6-X #424](https://github.com/definitely-stable/Mathlab/pull/424), parent HEAD `893f590cc583c7a23a402ad9cf856b780219699f`, whose 4 GitHub-hosted CI were SUCCESS. Latest D6-Y HEAD **`73ddbae8e12e6444b19069d541082d8a46094a79`**. No `main` changes or merges; #230/#176/#169 remain OPEN.

**MANDATORY NOVELTY ATTRIBUTION:** The extremal graph problem of maximizing adjacent physical edge pairs at fixed graph order/size is CLASSICAL, notably Ahlswede–Katona, *Graphs with maximal number of adjacent pairs of edges* (1978), DOI https://doi.org/10.1007/BF01902206, and Wagner–Wang (2009), DOI https://doi.org/10.1556/SScMath.2009.1107. The D6-Y bound is a self-contained **near-complete K_a specialization** and should NOT be reported as an original graph theory discovery. The explicit Mathlab two-site marginal-gap construction has NOT been shown unpublished relative to earlier combinatorial/LP literature.

**ALL-h sharp physical-IMAGE lemma (every globally injective ORIGINAL f,g):** Let s=2^h, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}, K=C(a,2), m=K−V<=a−2. For ANY complete original point or (independently) original line injection, its occupied physical edge image E satisfies
`A(E)=sum_c C(deg_E(c),2) <= a*C(a−1,2)−2m(a−2)+C(m,2)`.
This is EXACT, SHARP and attained when the m missing physical edges form one physical star: expand occupied degrees via missing graph H; the H contribution is bounded by the number C(m,2) of unordered missing-edge pairs. It does not use assumed Sp(4,s) symmetry, independence of f/g, original factor permutations, or losing incidence positions.

**EXACT restricted global extendibility gap:** Construct physical- and original-factor-exchangeable two-original-point pair marginals on distinct canonical K_a edges with J(adjacent e,e')=1/[K(V−1)], J(disjoint)=[V−1−2(a−2)]/[K(V−1)C(a−2,2)], J(equal)=0. All one-site marginals are 1/K, both original point sites are locally injective, and EVERY explicitly selected global column-capacity lift `E[x_p,e*(1−sum_{q!=p}x_q,e')]>=0` is satisfied. The expected number of physically adjacent ORIGINAL point pairs under this pairwise law is `V(a−2)`, which exceeds the sharp global image bound by exactly `m(a−2)−C(m,2)>0` when m>0. Thus these **selected** lifted physical column inequalities are INSUFFICIENT for global extension of consistent pair marginals. This is NOT a valid general SA/SOS gap claim, and does NOT cover all lifted constraints or all GF5 sixset constraints.

**Concrete true s=4 W(3,4):** V=85, a=14, K=91, m=6; A_max=963, pairwise pseudo expected A=1020, exact gap **57**. Pairwise selected column lift permits adjacency probability 2/7 per random ORIGINAL point pair, but actual complete global map upper is **321/1190**, gap **19/1190**. For s=2, m=0 and gap=0.

**Independent replayable GitHub-hosted evidence:** ALL physical missing-edge sets for (a,m)=(5,3),(6,4),(7,5) (respectively 120, 1,365, **20,349** cases), independent physical O(V²) adjacency oracle versus degree-sum, actual ORIGINAL W32/W34/W38 typed geometry and complete physical maps on both sides, every ordered physical pair at a=6 and a=14 verifying marginal normalization and selected column lifts, exact all-h arithmetic h=1..9, fail-closed inputs and budgets. Dedicated [D6-Y Contract #38423058765](https://github.com/definitely-stable/Mathlab/actions/runs/38423058765) **SUCCESS 8/8 test methods**, [INDEX #38423058915](https://github.com/definitely-stable/Mathlab/actions/runs/38423058915) **SUCCESS**. [Proof Audit #38423058692](https://github.com/definitely-stable/Mathlab/actions/runs/38423058692) and [full Research #38423058734](https://github.com/definitely-stable/Mathlab/actions/runs/38423058734) IN PROGRESS at posting. Independent mathematical review OPEN; PR Draft; no merge.

**OUTCOME RESTRICTED_THEOREM_C:** a SHARP valid all-h capacity constraint and an exact failure witness for a restricted two-site marginal relaxation, NOT Branch A Omega(s^6), NOT Branch B infinite correlated true f/g counterfamily, no positive GF5 seven-S root lower, no all-R3 upper or ASET exponent. Next D6-Z must connect SHARP global physical adjacency/capacity constraints to ORIGINAL incidence-position-aware seven-GF5 sixsets, with a genuine universal proof or explicit further pseudo-falsifier.

---

## Comment 149 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6149297602
- GitHub comment ID: 6149297602

### HYP-105 #230 — JPKC-002 restricted all-h BLOCKED-only collision theorem and ORIGINAL GQ anchor capacity (2026-10-13)

Created strictly stacked [Draft PR #426](https://github.com/definitely-stable/Mathlab/pull/426) on 4/4-success JPKC-001 [#423](https://github.com/definitely-stable/Mathlab/pull/423), parent pinned HEAD `d0d8e6ce428720050de5239e42a635b72ba9c1c7`. Latest JPKC-002 HEAD `c5af5026ce72a96439015e34fdf341b625f8be2c`. No main changes or merges. Root Branch A/B OPEN.

**J3 (ALL-h exact):** for oriented simple physical three-paths with all four row and all four column coordinates distinct, let g_uv be the number at given ORIENTED physical endpoints. Then
`sum g_uv(g_uv-1) = 12 D6 + Theta_GG + I_GG`,
where the two nonnegative defects are (i) shared internal graph vertices and (ii) disjoint interiors creating physical coordinate-IMPROPER simple C6. This is not an unconditional positive S bound.

**J4 (ALL-h conditional, strictly narrower obstruction):** if a hypothetical coherent complete f_s,g_s sequence has `S=o(s^6)`, #394 forces `B_G=sum b_uv >=(16-o(1))s^6` where b_uv counts ONLY true ORIGINAL nonincident, PHYSICALLY BLOCKED, coordinate-proper three-paths on the full G. Thus by CS `sum b_uv(b_uv-1)>=(48-o(1))s^6`. The exact blocked-only identity
`sum b_uv(b_uv-1)=D_BB+Theta_BB+I_BB` with `0<=D_BB<=12D6<=12S=o(s^6)`
gives
`Theta_BB+I_BB >=(48-o(1))s^6`.
Unlike previous #423 all-graph K2 defect, this concentrates necessary mass on collisions of TWO BLOCKED ORIGINAL paths on the SAME complete f,g.

**J5 (ALL-h original-anchor theorem):** all blocked paths with the same oriented grid endpoints have the SAME unique original GQ nonincident q--ell--p--r anchor. Every original nonincident (q,r) has exactly four potential oriented physical endpoint pairs. Since there are V²-N original nonincident anchors, exact finite CS improves to
`sum b_uv(b_uv-1) >= B_G²/[4(V²-N)]-B_G`.
W32 support capacity 720 (vs untyped a^4=1296), W34 27200 (vs 38416). This is not an all-h improvement of leading 48 coefficient, but pins geometry-specific common-original anchor constraints.

**True ORIGINAL complete injection exact data, `(B,collisions,Theta_BB,I_BB,D_BB)`:**
- W32 S68: `(606,512,196,316,0)`; S72: `(658,664,292,372,0)`;
- W34 lex: `(55384,161256,40836,63144,57276)`; W34 random: `(48542,117356,26884,47816,42656)`;
- REAL D4 W34 Desarguesian symplectic-spread f,g: `(52760,149716,38972,57316,53428)`; independently enumerated original `M_f=259>=30` constructive floor.

**Implemented:** original-incidence-ID per edge; seven disjoint ORIGINAL projection statuses; COMPLETE ordered endpoint path-pair taxonomy; independent codegree K2 + original PR #394 projection + W32 true seven GF5 checks; W32 4 maps, W34 lex/random, D4 true spread W34; exact adversarial input/path-pair budgets; GitHub-hosted dedicated CI; machine-readable report with `--spread` switch and pinned tests.

**CI at posting:** [Dedicated #38423791169](https://github.com/definitely-stable/Mathlab/actions/runs/38423791169) SUCCESS exact final HEAD, [INDEX #38423790996](https://github.com/definitely-stable/Mathlab/actions/runs/38423790996) SUCCESS. [Proof Audit #38423791020](https://github.com/definitely-stable/Mathlab/actions/runs/38423791020) and [Research #38423791001](https://github.com/definitely-stable/Mathlab/actions/runs/38423791001) not yet confirmed complete; no 4/4 claim until verified.

**Next mathematical task:** prove/falsify a noncircular all-h compensation involving the COMMON ORIGINAL GQ anchor fibers and physically globally injective K_a occupancy; D6-X #424 proves locally projectively consistent star pseudo-labels can violate lifted global physical-label capacity. Independent mathematical review still OPEN. **No root A/B result, no full GF5 R3/Aset exponent.**

---

## Comment 150 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6149725712
- GitHub comment ID: 6149725712

### HYP-105 / issue #230 — D6-Z exact all-h ORIGINAL six-incidence wedge transport; W32 seven-GF5 image-only/proxy falsifier (2026-10-13)

Created [Draft PR #428](https://github.com/definitely-stable/Mathlab/pull/428) STRICTLY stacked on 4/4-success [D6-Y #425](https://github.com/definitely-stable/Mathlab/pull/425), exact parent HEAD `73ddbae8e12e6444b19069d541082d8a46094a79`. Latest child HEAD **`d3b78794e2bdd9ee47d4bf7419afd59a37cb5b1a`**. No main edits, no merges; issue #230/#176/#169 and Branch A/B OPEN.

**THEOREM Z1 — exact ALL-h incidence-position-aware wedge transport.** For s=2^h, V=(s+1)(s²+1), Delta=s+1, N=V*Delta original incidences, arbitrary complete correlated typed global injections f,g. For each unordered sixset Q of SIX DISTINCT ORIGINAL point-line incidences define `tau_L(Q)=sum_c C(#{i in Q: c in f(original_point(i))},2)` and analogously right. ORIGINAL factor repeats across different incidence positions are COUNTED, not collapsed. Then the all-h exact double-count identity is
`sum_{Q subset ORIGINAL incidences, |Q|=6} tau_L(Q) = C(N−2,4) [2 V C(Delta,2) + Delta² A(f)]`,
where `A(f)=sum_{p<q}1[f(p) physically intersects f(q)]`. Same exact formula for right g. No assumption f,g independent or W32-only. This sums over ALL ORIGINAL sixsets, **NOT** just seven-GF5 accepted ones.

**THEOREM Z2 — exact SHARP all-h global wedge envelope.** Physical image E has K=C(a,2), V occupied, m=K−V<=a−2 missing edges. `A(E)=a C(a−1,2)−2m(a−2)+sum_c C(deg_missing(c),2)`. The final sum lies in EXACT SHARP interval `[max(0,2m−a), C(m,2)]`: min realized by missing disjoint physical-edge matching when 2m<=a, otherwise by disjoint physical paths covering all a vertices; max by a missing physical STAR. Both physical point and line image assignments can independently attain these bounds and thus exact corresponding all-sixset wedge-moment bounds via Z1. This is elementary double counting / classical complementary extremal graph theory, **not novel graph-theory prior art**.

**THEOREM Z3 — genuine ORIGINAL GQ source-collinearity image-conditioned expectation.** Partial linearity gives EXACTLY `V C(Delta,2)` ORIGINAL pairs of points sharing one ORIGINAL line; dual for lines meeting at a point. For any fixed globally injective physical image E and a UNIFORM permutation of its V physical labels onto all ORIGINAL factors, the expected physical overlap among the source-collinear pairs is exactly `V C(Delta,2) A(E)/C(V,2)`. This is an incidence-conditioned image-permutation MEAN, NOT deterministic bound for arbitrary correlated labels and NOT a seven-S lower.

**True ORIGINAL W(3,2) seven-GF5 proxy falsification**: Every W32 f/g complete original factor injection uses all 15 physical K6 edges, so BOTH sharp image-only adjacency statistics `A(f)=A(g)=60` always; nevertheless genuine S68 and S72 have the SAME left f and full right image but different exact accepted original sixset seven-GF5 counts, 68 vs72. Hence seven-S is NOT determined by image-only physical adjacency. Enumerating all 62,370 true left A/B/C original six-incidence candidates for EACH map, the necessary **two-sided physical six-coordinate 2-regular** proxy accepts 331 (S68) / 358 (S72) sets, but only 68 / 72 are in the exact seven GF5-positive classes; thus **263 / 286 false positives** (roughly 79.5% / 79.9% of the proxy). Actual positive and false-positive ORIGINAL six-incidence witnesses are independently reclassified with the exact position-aware original GF5 oracle (D6 matches and B/B overlap preserved). For s>=4, even scalar wedge tau=6 can hold with seven physical coordinates on a six-edge physical tree of degrees (3,2,2,2,1,1,1), not 2-regular.

**True W32 original-collinear physical overlap**: left source-collinear overlap count=35 in both; right count=24 (S68) vs25 (S72); image-conditioned uniform reassignment expectation on either side=180/7. This confirms original incidence placement conveys information absent from both physical IMAGE graphs. Note the collinear statistic DOES distinguish these particular S68/S72 models, so do not overclaim impossibility of all source-aware second-order bounds.

**Independent hosted evidence latest head:** [Dedicated D6-Z #38426777699](https://github.com/definitely-stable/Mathlab/actions/runs/38426777699) SUCCESS **8/8 tests**; independent pair-position census on genuine W32/W34, exact toy C(8,6) sixset enumeration, true W32/W34/W38 paired physical min/max constructions, full W32 62,370 selected incidence candidate scans on S68/S72, independent 4! source collinearity permutation test, strict malformed data/budget rejection and no-Branch-A/B contract. [INDEX #38426777140](https://github.com/definitely-stable/Mathlab/actions/runs/38426777140) SUCCESS. [Proof Audit #38426777074](https://github.com/definitely-stable/Mathlab/actions/runs/38426777074) IN PROGRESS; [Full Research #38426777108](https://github.com/definitely-stable/Mathlab/actions/runs/38426777108) QUEUED at posting. Independent mathematical review OPEN. No 4/4 claim before these complete.

**SCIENTIFIC RESTRICTION:** Z1–Z3 are all-h sound global incidence/moment identities and exact sharp physical envelopes; the **GF5-specific separation** is FINITE W32. None proves `inf_{f,g}S_s>=c s^6`, a coherent infinite counterfamily, full R3 bound, or ASET exponent. D6-AA must retain ORIGINAL incidence positions and higher-order physical cycle matching / B/B overlap relations in any purported positive uniform seven-GF5 dual. An image-only adjacency or scalar-wedge shortcut is insufficient as an exact GF5 classifier.

---

## Comment 151 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6149741807
- GitHub comment ID: 6149741807

### HYP-105 / #230 — JPKC-003 ORIGINAL anchor channel variance + conditional s^7 endpoint-collision storm (2026-10-13)

Created strictly stacked **[Draft PR #427](https://github.com/definitely-stable/Mathlab/pull/427)** on fully green JPKC-002 [#426](https://github.com/definitely-stable/Mathlab/pull/426), parent HEAD `c5af5026ce72a96439015e34fdf341b625f8be2c`. Exact final JPKC-003 HEAD `63991f778bf8b8665f914b056e15a6d7a5c0905f`. NO main change; NO merge. Root A/B OPEN.

**J6 (exact ALL h):** Every ORIGINAL nonincident anchor (q,r) has two physical diagonal channels with blocked physical P3 counts b0,b1, reversed paths preserving counts. Writing B_qr=2(b0+b1), B=sum B_qr, M=V²−N, and K=sum ordered distinct blocked path collisions, the exact nonnegative two-scale variance identity is
`K=B²/(4M)-B + (1/4)sum_(q,r)(B_qr−B/M)² +sum_(q,r)(b0−b1)².`
Both terms are independently checked against the JPKC-002 full physical ordered collision ledger.

**J7 (exact ALL h original source split):** The endpoint blocker predicate on the ORIGINAL q−ell−p−r GQ projection, `f(q)∩f(p)!=∅ OR g(r)∩g(ell)!=∅`, is CONSTANT over both diagonal channels and all physical paths in an anchor. Hence endpoint-sourced blocked population E and internal-only blocked population I=B−E CANNOT cross in an equal-endpoint collision. Exact source counts `A_left=2s M_f`, `A_right=2s M_g`, and `A<=2s(M_f+M_g)<=4s C_s`, where `C_s=(s−1)V+(s²+1)(a−1)=(1+o(1))s^4` is PR #394's proved ORIGINAL GQ spectral cap. Thus `K=K_E+K_I`, `K_E>=E²/(4A)-E`, `K_I>=I²/(4(M−A))-I`, with exact zero-capacity handling.

**J8 (NEW ALL h CONDITIONAL necessary disjunction):** For any hypothetical infinite complete correlated f_s,g_s with `S_s=o(s6)`, PR #394/JPKC-002 forces `B=E+I>=(16−o(1))s6`; therefore either `E>=(8−o(1))s6` forcing `K_E>=(4−o(1))s7`, OR `I>=(8−o(1))s6` forcing `K_I>=(8−o(1))s6`. Subtract at most `12D6<=12S=o(s6)` proper-C6 ordered collisions: the same lower orders MUST occur among wrong internal-overlap/improper-C6 blockers. This does NOT rule either out, NOT Root A/B.

**Exact ORIGINAL complete f,g evidence (B,E,I,K,KE,KI):**
W32 S68 (606,544,62,512,444,68); W32 S72 (658,600,58,664,624,40);
W34 lex (55384,38020,17364,161256,128912,32344);
W34 random (48542,30194,18348,117356,87996,29360);
true D4 W34 Desarguesian symplectic spread (52760,35190,17570,149716,116600,33116).
D6-Y sharp classical Ahlswede–Katona near-complete physical image capacity verified independently on BOTH point/line maps; its global image-pair count is NOT the original collinear M_f.

**Implementation:** proof and exact-scoping doc + fully typed original anchor and two-diagonal Python ledger + 6 dedicated independent tests + GitHub-hosted workflow; fail-closed invalid maps, path budgets, nonstandard image domains, zero-capacity regions. No external D6-X/Y imports or self-hosted runners.

**CI on final exact HEAD at posting:** dedicated [run #38426929679](https://github.com/definitely-stable/Mathlab/actions/runs/38426929679) SUCCESS (6/6), INDEX [#38426929682](https://github.com/definitely-stable/Mathlab/actions/runs/38426929682) SUCCESS; Proof Audit [#38426929625](https://github.com/definitely-stable/Mathlab/actions/runs/38426929625) and full Research [#38426929756](https://github.com/definitely-stable/Mathlab/actions/runs/38426929756) not yet confirmed complete. Independent mathematical review OPEN; do NOT claim 4/4 until verified.

**Next allowed JPKC-004:** target original GQ/palette-global-capacity compensation for the s7 endpoint-only wrong collisions or s6 internal-only wrong collisions, with genuine original incidence witness mapping to the other six accepted GF5 classes. Do not assume source storm cannot exist without proof. Root #230/#176/#169 remain open; no ASET exponent or full R3 upper.

---

## Comment 152 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6150213619
- GitHub comment ID: 6150213619

### HYP-105 / #230 — JPKC-004 source-incidence transport and all-h restricted method NO-GO (2026-10-13)

Created STRICT Draft [PR #429](https://github.com/definitely-stable/Mathlab/pull/429), child of fully 4/4 CI green JPKC-003 [#427](https://github.com/definitely-stable/Mathlab/pull/427), pinned parent HEAD `63991f778bf8b8665f914b056e15a6d7a5c0905f`. New final researched HEAD `05c3360deaa2304106eb5b4f9936821947816451`. Main unchanged, no merge. Root A/B OPEN.

**J9 ALL-h original unique-GQ endpoint closure NO-GO.** For endpoint-bad nonincident ORIGINAL anchor q–ell–p–r, an ORIGINAL 3-incidence physical P3 plus the unique 3 closing ORIGINAL incidence positions is NOT one of the seven positive GF5 sixsets: if f(q) intersects f(p), a physical first coordinate occurs at least 3 times already in original anchor incidence positions (q,ell),(p,ell),(p,r); dual for g(r) and g(ell). Repeated incidence IDs also exclude a genuine sixset. Direct canonical 3+3 completion is a zero-conversion route, NOT Root B.

**J10 ALL-h universal disjoint-pair multiplicity cap.** Each original six-incidence set offers at most 2^6 physical diagonal choices; each simple C6 has 12 ordered antipodal P3-pair witnesses; so at most 768 interior-disjoint ordered collisions per original Q. This is only an upper, NOT a positive witness guarantee.

**NEW J11/J12 ALL-h stronger direct-union structural NO-GO.** For ANY two distinct physical P3s with SAME oriented endpoints:
- If interiors share a physical graph vertex, at most FIVE graph vertices occur in the union, so no 6-coordinate 2-regular left or right ORIGINAL sixset (even with six distinct original IDs).
- Otherwise their union is a simple physical C6. A genuine ORIGINAL sixset of its SIX distinct incidence IDs has both projections precisely 6-coordinate 2-regular **iff** the physical C6 is coordinate-proper (projected row and column step multigraphs are connected 2-regular six-cycles). By Kikuchi K1 the unique accepted motif is exactly ORIGINAL D6.
- With repeated ORIGINAL incidence IDs there is no true original sixset.
**Therefore a direct two-P3 collision union CANNOT generate ANY of the OTHER SIX accepted seven-family GF5 classes for ANY h.** This does NOT exclude those classes from general 6-incidence subsets.

**J13 EXACT all-h endpoint original transfer identity:** Let T_E be ORDERED endpoint-bad blocked same-endpoint P3 pair collisions whose union is SIX distinct original incidence IDs with both physical projections six-coordinate 2-regular. Then `T_E = K_E(proper physical C6) <=12D6<=12S`. Thus if a hypothetical small-S infinite family took JPKC-003 endpoint branch `K_E >=(4-o(1))s7`, its directly convertible sixset fraction is `T_E/K_E=o(1/s)`: almost the whole required s7 collision mass cannot be transported through the same six ORIGINAL incidences. A fundamentally new witness construction would be needed. THIS DOES NOT PROVE Root A/B.

**Exact true original finite results (K_E, T_E, direct nonconvertible):**
W32 lex (1456,64,1392), W32 reverse (1060,24,1036), W32 S68 (444,0,444), W32 S72 (624,0,624); W34 lex (128912,47400,81512), W34 random (87996,33400,54596), true original D4 W34 spread (116600,42940,73660). W32 full seven-GF5 original census independently verifies only D6 selected; W34 source 2regular ↔ proper C6 theorem is analytic and does not claim a full seven-class computational census.

**Implementation:** exact ORIGINAL graph-edge incidence provenance, endpoint-bad closure obstruction, complete typed ordered pair collisions, repeated-ID source failure, left/right 2-regular necessary tests and true W32 GF5 seven-census, disjoint witness cap, J11/J12/J13 all-h structural assertions; independent full original W32 4 maps, W34 lex/random and D4 original symplectic spread; fail-closed path and cache budgets; companion proof doc and dedicated GitHub-hosted runner.

**CI on final HEAD at posting:** dedicated [#38430443222](https://github.com/definitely-stable/Mathlab/actions/runs/38430443222) SUCCESS (6/6); INDEX [#38430443229](https://github.com/definitely-stable/Mathlab/actions/runs/38430443229) SUCCESS; Proof Audit [#38430443219](https://github.com/definitely-stable/Mathlab/actions/runs/38430443219) and Research [#38430443246](https://github.com/definitely-stable/Mathlab/actions/runs/38430443246) pending/in progress at writing, verify before 4/4 claim. Independent mathematical review OPEN. No merges, no main modification, no ASET exponent/full R3 upper.

**Next allowed task JPKC-005:** devise and falsify a NEW ORIGINAL witness involving a second GQ anchor or additional source incidence IDs; test bounded multiplicity and actual seven GF5 selection. Do NOT repeat the disproved direct two-path six-incidence transfer route and do NOT infer selected GF5 positivity from physical image wedge counts (D6-Z #428).

---

## Comment 153 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6150793777
- GitHub comment ID: 6150793777

### HYP-105 D6-AA1–AA3 — stacked Draft implementation

Opened [Draft PR #430](https://github.com/definitely-stable/Mathlab/pull/430) on top of D6-Z #428 (no `main` changes). Exact positional six-column classifier Phi uses B_ij and W3 and enumerates 130 six-position 2-regular multigraphs (60 C6 + 10 C3+C3 + 45 C4+C2 + 15 3C2). Independent oracle agrees with historic seven-class classifier for all 62,370 ORIGINAL W32 left candidates each in S68/S72 (68/72 positives); fixed necessary GF5 weighted numerators 3,112,510 and 3,283,610. All-h one-sided M1..M6 identities and joint original-incidence two-coordinate cell moment identities proved and implemented. Docs and tests are in the PR.

At commit `a2e6e0e6aa3eb78dc82e4f1a6b3c22d69d5b8cc1`: dedicated D6-AA 9 tests SUCCESS, INDEX SUCCESS, Proof Audit SUCCESS; full Research is still pending and must pass before technical acceptance. No all-h positive lower `S_s>=c*s^6` has been obtained; Branch A/B stay OPEN, AA4 global feasibility OPEN. No total R3 upper or ASET conclusion; issue remains OPEN.

---

## Comment 154 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6150795192
- GitHub comment ID: 6150795192

### HYP-105 / #230 — JPKC-005: alternate THREE original incidence completion of one physical P3 seed (13 Oct 2026)

Created STRICT stacked [Draft PR #431](https://github.com/definitely-stable/Mathlab/pull/431) on 4/4 green [JPKC-004 #429](https://github.com/definitely-stable/Mathlab/pull/429), parent pinned SHA `05c3360deaa2304106eb5b4f9936821947816451`. Initial JPKC005 HEAD `bfe03ecc557dd134a64f34499e98ac82b997a03f`. No `main` mutation, no merge. Root A/B remain OPEN.

**New genuine ORIGINAL witness model:** keep ONE coordinate-proper oriented physical P3 with 3 distinct original incidence IDs T, whose original nonincident endpoints (q,r) have endpoint-bad GQ projection. Rather than union two P3s (JPKC004 J11/J12 gives only D6), seek ANY ALTERNATIVE source triple U disjoint T, Q=T ∪ U a TRUE accepted selected GF5 seven-class ORIGINAL sixset. U may form ANOTHER actual GQ projection q'–ell'–p'–r'; the executable checks that structure directly rather than assuming it.

**J14 (ALL-h proved uniform charge):** Each source sixset Q supports <=C(6,3)*2^3*2=320 oriented physical 3-path seeds, because each ORIGINAL incidence has two Kikuchi physical diagonals. Each original 3-incidence seed T has <=16 oriented physical realizations. Hence the incidence-preserving accepted seed→sixset relation has `H_E<=320*S`. If a hypothetical small-S global map family has an endpoint-bad E>=(8-o(1))s^6, then at least E−320S=(8-o(1))s^6 endpoint-bad physical path seeds have ZERO positive alternate three-incidence completions. This is a CONDITIONAL isolation requirement, NOT an unconditional positive S bound.

**J15 (ALL-h proved restricted NO-GO):** A coordinate-proper physical P3 uses four distinct physical coordinate vertices and projects to a length-three path on EACH side. Thus no ORIGINAL sixset extending that seed can have a C-type physical half (3 disjoint doubled original pair edges). In particular, C/A and C/B among the seven positive GF5 classes can NEVER be obtained from this particular P3 extension witness. The other 5 motif classes are possible targets, not automatically guaranteed.

**J16:** For endpoint-bad original GQ anchor, JPKC004 J9 prohibits choosing exactly its 3 canonical original closing incidences as U. Any accepted U differs in at least one original incidence. Do NOT assume two replacements are mandatory: a B physical C4 plus repeated edge C2 can use endpoint chord f(q) or g(r).

**Implemented and tested on GitHub-hosted runner:** complete W32 original seven-family accepted-sixset index over all 62,370 true W32 left six-coordinate candidates; independent general physical-alphabet seven-class classifier checked against prior canonical original checker for BOTH S68 and S72; original seed-to-accepted-Q lookup, true alternative 3-original incidence IDs, actual second GQ 3-walk detection and canonical overlap, per-Q physical multiplicity, exact W32 lex/reverse/S68/S72 complete coverage; W34 lex/random and real D4 W34 spread checked for honest unblocked ORIGINAL B/B-overlap closures, with STRICT NO W34 full seven-census claim. Explicit fail-closed path/accepted Q budgets.

**CI initial HEAD at writing:** [dedicated JPKC005 #38434678482](https://github.com/definitely-stable/Mathlab/actions/runs/38434678482) tests/report steps both SUCCESS, GitHub runner in action post-cleanup; [INDEX #38434678348](https://github.com/definitely-stable/Mathlab/actions/runs/38434678348) SUCCESS; [Proof Audit #38434678418](https://github.com/definitely-stable/Mathlab/actions/runs/38434678418) and [Research #38434678392](https://github.com/definitely-stable/Mathlab/actions/runs/38434678392) were RUNNING. No 4/4 claim until verified. Independent mathematical proof review remains OPEN.

**Next:** examine EXACT W32 true positive alternate completion coverage/second-anchor supports; decide if any all-h extension theorem can withstand S68/S72 low-S and true D4 symplectic spread. If not, record a concrete restricted-method no-go instead of expanding finite tests and pursue a new global occupancy/geometry-coupled invariant.

---

## Comment 155 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6150892543
- GitHub comment ID: 6150892543

### JPKC-005 final mathematical strengthening and exact W32 falsifier — follow-up to #6150795192

Draft [PR #431](https://github.com/definitely-stable/Mathlab/pull/431), strictly stacked on #429. Current exact HEAD `8139eaf2692f26ee860f3b0fd08108e41657e92f`; main unchanged and no merges. Root A/B OPEN.

**New J17 ALL-h theorem (second-true-GQ-anchor route NO-GO).** Let T be any physically coordinate-proper ORIGINAL three-incidence path seed with nonincident original endpoint pair (q,r). Suppose a different 3-ID complement U is a TRUE original GQ length-3 path `q'–ell'–p'–r'`, and Q=T∪U is six-symbol degree-two on BOTH physical coordinate sides. Since the original point p' appears TWICE in U, its physical f(p') edge must use two NEW symbols outside the physical projected P4 of T. The only remaining U physical row edge f(q') must join the original seed P4 endpoints, hence q'=q by global injection. The dual argument forces r'=r. GQ uniqueness then forces U to equal the canonical closure A(q,r). Since endpoint-bad JPKC004 J9 prohibits this canonical closure, **NO endpoint-bad seed has a positive alternate completion U that itself is ANY original GQ 3walk**. Successful alternate U must be a different 3-incidence ORIGINAL factor pattern. This is a restricted ALL-h structural NO-GO, not Root A/B.

**J14 (ALL-h):** `#(oriented physical P3 seeds contained in an ORIGINAL positive sixset Q)<=C(6,3)*2³*2=320`; each original 3-ID source seed has <=16 physical realizations, so if `S=o(s6)` and endpoint branch `E>=(8-o(1))s6`, then `E-320*S=(8-o(1))s6` endpoint-bad seeds must have ZERO alternate accepted 3-ID completion. **J15 (ALL-h):** seed projects to physical P4 on both sides, so cannot extend to C/A or C/B. J16 canonical endpoint-bad closure excluded by J9.

**Exact TRUE ORIGINAL W32 positive alternative completion data**, with columns (E physical endpoint-bad seeds; covered seeds; full accepted (P,Q) hits; genuine SECOND original GQ-walk positives): lex `(786,154,214,0)`; reverse `(676,86,90,0)`; S68 `(544,8,8,0)`; S72 `(600,10,10,0)`. S68 class hits: A-left/B-right=2, B-left/A-right=6, D6=0. S72: 4,6,0. On S68 only 8/544 and S72 only 10/600 eligible endpoint-bad proper P3 seeds have ANY true original positive completion. W32 full selected original seven-family census, and independent GENERAL physical-alphabet original class agreement on ALL 62,370 original left 6coordinate candidates for BOTH S68 and S72, verified. W34 exact unblocked GQ B/B-overlap closure structural pins: lex=15,064; random=16,042; genuine D4 spread=15,298. NO claim of a full positive original W34 sixset census.

**Final-head GitHub-hosted CI as verified:** JPKC005 [#38435598560](https://github.com/definitely-stable/Mathlab/actions/runs/38435598560) SUCCESS, INDEX [#38435598534](https://github.com/definitely-stable/Mathlab/actions/runs/38435598534) SUCCESS; Proof Audit [#38435598411](https://github.com/definitely-stable/Mathlab/actions/runs/38435598411) and Research [#38435598536](https://github.com/definitely-stable/Mathlab/actions/runs/38435598536) were still running at posting. Independent proof review remains OPEN; keep Draft; no merges.

**Next permitted JPKC-006:** investigate **non-GQ-walk ORIGINAL 3-incidence complement factor topologies** and/or a geometry+global physical occupancy-coupled certificate. Do NOT rerun the just closed 'second GQ anchor' method or promote 2-regularity/adjacency proxy as proof.

---

## Comment 156 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6151347871
- GitHub comment ID: 6151347871

### D6-AA4-A source-forest support + conditional six-position transport (Draft PR #433)

Stacked [PR #433](https://github.com/definitely-stable/Mathlab/pull/433) on AA1–AA3 #430 (parent all 4 CI SUCCESS); `main` unchanged.

ALL-h necessary local theorem: any true six-DISTINCT-ORIGINAL-incidence two-sided physical-2-regular Q induces an ORIGINAL bipartite six-edge linear forest (maximum original factor degree 2 and girth 8). The complete abstract 130×130 source support mask is **16,900** named positional graph pairs = **630** source-forbidden (duplicate incidence or short cycle) + **11,430** seven-class admissible + **4,840** non-seven A/A. On genuine W(3,s), all physical two-sided regular false positives are exclusively nonaligned A/A: `S_seven = two_sided_regular_proxy - false_AA`. Abstract-mask admissibility does NOT guarantee embeddability in a particular finite GQ.

AA4-A2 preserves BOTH exact six-position ORIGINAL point/line equality partitions kappa and the two one-sided physical degree-2 marginals L_kappa,R_kappa on all original Q. For each stratum prove sharp two-bit Fréchet bound `J_kappa >= max(0,L_kappa+R_kappa-N_kappa)`; explicit integral pseudocoupling witnesses sharpness *only within this reduced information*, NOT globally valid factor labels. Exact hosted ORIGINAL W32 scan of all C(45,6)=**8,145,060** Q **once**, plus 62,370 left and right factorized candidates per S68/S72, yields:

- S68: actual regular=331, actual seven=68, active source strata=523, Fréchet regular floor=**0**, seven floor=**0**.
- S72: actual regular=358, actual seven=72, active source strata=517, Fréchet regular floor=**0**, seven floor=**0**.
- Every finite false positive was A/A nonalignment (263 and 286), independently corroborating the all-h source support theorem.

Dedicated AA4-A contract GitHub-hosted SUCCESS on SHA `ea49fd31fc7aad26c5fa987caa0494342e627b02` (7/7 tests plus full original finite scan). INDEX and Proof Audit SUCCESS; Research currently in progress and must pass on the same final SHA for complete technical acceptance.

**Interpretation**: even conditional one-sided two-regular marginals retaining both six-position source equality partitions can have a zero minimum; therefore no positive GF5 lower follows from those marginals alone for these finite real controls. This is a **restricted relaxation countermodel**, not an infinite globally correlated f,g (not Branch B). Further research requires cross-Q shared-original-factor and global physical injection/capacity consistency. Branch A/B OPEN; #230/#176/#169 remain OPEN; no new ASET exponent or total R3 claim.

---

## Comment 157 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6151396124
- GitHub comment ID: 6151396124

### HYP-105 / #230 — JPKC-006 exact non-GQ source topology and SHARP 12-seed all-h charge (13 October 2026)

Created STRICT stacked [Draft PR #432](https://github.com/definitely-stable/Mathlab/pull/432) on fully green JPKC005 [#431](https://github.com/definitely-stable/Mathlab/pull/431), pinned parent `8139eaf2692f26ee860f3b0fd08108e41657e92f`. Final new HEAD `22e49e1991992deb437a44a9938e9629b78e3868`; `main` unchanged, no merge, Root A/B OPEN.

**J18 (ALL-h proved, exact and attained):** For any THREE distinct ORIGINAL incidences T, at most TWO oriented coordinate-proper physical P3s of the original two-diagonal Kikuchi graph use exactly those source incidence IDs (one physical path and its reversal). A physical P3 projects to P4 on both physical coordinate halves; the three source incidence edge IDs must appear in IDENTICAL order on both projected paths, so selecting the first half's orientation fixes the second. Earlier loose 16 in JPKC005 can be reduced to sharp 2. Independent exhaustive local source-edge permutation/diagonal oracle verifies every fixture.

**J19 (ALL-h proved, sharp universal 12):** Given any one genuine selected GF5-positive ORIGINAL sixset Q, at most 12 coordinate-proper oriented P3 seeds use three of its six IDs. Exact class bounds: D6≤12 (A-half connected C6 has six consecutive physical three-edge runs ×2 orientations), B-left/A-right≤8, A-left/B-right≤8, B/B-overlap/disjoint≤8 (B half C4+C2, four P4 runs ×2); C/A and C/B=0. W32 lex attains EXACTLY 12 on a genuine positive Q: the 12 coefficient is sharp over original globally injected maps. Thus `H_E=#((endpoint-bad ORIGINAL proper P3), accepted source-sixset Q containing its three incidence IDs)<=12 S`, tightening previous 320 by 26⅔.

**J20 (ALL-h rigorous complete eligible source U taxonomy):** If endpoint-bad P3 T extends to genuine accepted ORIGINAL sixset Q=T∪U, the extra THREE original incidences U have exactly ONE of three bipartite ORIGINAL source-graph topologies:
1. D6 => a matching of 3 disjoint true original point-line incidences (3K2);
2. B-left/A-right => one two-edge wedge at an ORIGINAL POINT p' plus one isolated original incidence at the source endpoint point q;
3. A-left/B-right => dual wedge at an ORIGINAL LINE ell' plus isolated original incidence at source endpoint line r.
No other source U topology survives JPKC005 J15 (C-type impossible for physical P4 seed) + J17 (B/B would form exactly forbidden canonical ORIGINAL GQ three-step q--ell--p--r).
This is a STRICT restricted completion classification, not all possible original 6sets.

**J21 (ALL-h CONDITIONAL only):** In hypothetical small-S endpoint-dominated counterfamily E≥(8-o(1))s⁶ and S=o(s⁶), at least E−12S=(8-o(1))s⁶ endpoint-bad proper physical seeds must admit ZERO TRUE positive original sixset extension. Does NOT prove Root A/B; multiplicity upper never implies positive extension existence.

**Executable:** new standalone source completion generator on genuine globally fixed original f/g, actually enumerates physical A-half length-three C6 complements, source incidences for point/line wedge+B physical half, matched six-column D6 original duals. Never substitutes physical image adjacency for original factor incidence. Independent exhaustive equality on every original endpoint-bad physical seed for W32 lex/reverse/S68/S72 against true selected 62,370-candidate ORIGINAL W32 GF5 oracle; local physical 2-diagonal source triples independently exhaustively validate two-orientation and 12/8/0 class upper.

**TRUE W32 full original data (E full, seeds covered by TRUE selected Q, ordered accepted (P,Q) hits, max per Q):** lex (786,154,214,12); reverse (676,86,90,8); S68 (544,8,8,2); S72 (600,10,10,2). S68 accepted source U: point wedge 6, line wedge 2, matching 0; S72 6,4,0. W32 low-S maps show almost-complete seed isolation, NO universal extension existence proven.

**W34 exact per-seed targeted original data (full E for context, selected genuine endpoint seeds, positive coverage, total accepted (P,Q) hits; A/B,B/A,D6 hits):** lex (38020,96,94,545; 182,222,141), random (30194,96,95,430; 172,162,96), genuine D4 symplectic spread (35190,96,94,537; 212,193,132). Precisely 96 DETERMINISTICALLY DISTRIBUTED actual physical seeds per map receive an EXHAUSTIVE positive source-completion query, but there is NO full W34 seven-S census, no probabilistic sampling guarantee and no extrapolation to s→∞.

**Final HEAD CI status at posting:** [focused JPKC006 #38439362206](https://github.com/definitely-stable/Mathlab/actions/runs/38439362206) SUCCESS (6/6), [INDEX #38439362165](https://github.com/definitely-stable/Mathlab/actions/runs/38439362165) SUCCESS. [Proof Audit #38439362233](https://github.com/definitely-stable/Mathlab/actions/runs/38439362233) in progress and [Research #38439362644](https://github.com/definitely-stable/Mathlab/actions/runs/38439362644) pending at time of writing; do not claim 4/4 without final check. Independent math proof audit remains OPEN.

**Next JPKC-007:** derive/falsify ORIGINAL source-incidence and global physical pair occupancy-coupled *positive EXTENSION EXISTENCE* condition specifically for matching and point/line wedge types, potentially using D6-AA #430 six-position tensor moments; validate on S68/S72 and D4 spread. Do not revisit disproven GQ 3-walk second-anchor route or claim (S=Omega(s^6)).

---

## Comment 158 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6151788832
- GitHub comment ID: 6151788832

### D6-AA4-B — globally coherent original-factor completion fiber implemented

[Draft PR #434](https://github.com/definitely-stable/Mathlab/pull/434) is stacked on AA4-A #433, without any `main` changes. All-h exact *conditional* block completion identity for a frozen ORIGINAL left f and frozen right labels outside B; the remaining global K_a injection has `(m+|B|)_{|B|}` legal completions. The common choice must be used across EVERY ORIGINAL Q touching B. Consequently the exact coherent fiber minimum is >= the sum of independently minimized accepted seven-cylinder costs. A strict gap is a valid cross-Q coherence obstruction to this **limited reduced relaxation**, not a root all-h S lower.

GitHub-hosted dedicated [run #38442101572](https://github.com/definitely-stable/Mathlab/actions/runs/38442101572) passed all 4 independent tests plus both 24-completion actual-original W32 censuses. On S68 fixed 4 right lines, coherent affected S minimum=58, independent cylinder-min sum=1, **gap=57**, GF5 numerator gap=2,604,760; a single affected original cylinder covers all 24 completions. S72: coherent affected S minimum=68, independent cylinder-min sum=0, **gap=68**, GF5 numerator gap=3,104,080; **4 original cylinder signatures cover every one of all 24 globally legal completions**. Actual whole-fiber S minima are 68 for both; their GF5 selected numerator minima are 3,112,510 and 3,104,080 respectively.

Pinned as fail-closed assertions and docs in final HEAD `f13193e5f1841282a830ff60ceb23e2686a98147`; final exact-head dedicated, INDEX, Proof Audit and full Research CI must still all finish SUCCESS to accept implementation. Scope strictly conditional on frozen other factors; **Branch A/B OPEN**, no full GF5 R3 or ASET exponent; #230/#176/#169 remain OPEN.

Next research gate: derive uniform-over-outside-labelings shared-factor/block-family lower, or prove a hard coherent global counterfamily. Do NOT mistake this finite 4-factor coverage for universal `S_s>=c s^6`.

---

## Comment 159 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6151796704
- GitHub comment ID: 6151796704

### HYP-105 / issue #230 — JPKC-007: exact physical-palette vs TRUE ORIGINAL GQ source completion deficit (2026-10-13)

Created STRICT [Draft PR #435](https://github.com/definitely-stable/Mathlab/pull/435) on fully 4/4-green JPKC-006 [#432](https://github.com/definitely-stable/Mathlab/pull/432), pinned parent HEAD `22e49e1991992deb437a44a9938e9629b78e3868`. Final JPKC-007 HEAD `6816514f70f7a6d76e50c4066a284f9eb6ab23bd`. **main unchanged; no merge. Branch A/B #230 OPEN.**

**J22 (ALL-h exact):** For any true ORIGINAL coordinate-proper physical P3 with projected P4 physical endpoints z0,z3, outside-symbol set U=[a]\{z0,z1,z2,z3}, F=available physical z3–z chords, L=available z–z0 chords, and missing interior unordered K_a pairs M, the physical A-half three-edge C6 completion count is exactly `|F||L|−|F∩L|−#{oriented distinct F×L pairs whose interior chord belongs to M}`. Verified independently by first-missing-chord telescoping (first endpoint, second endpoint, internal chord, actually occupied).

**J24 (ALL-h physical-palette only lower):** With m=C(a,2)−V<a−1 globally missing physical pair labels, the physical A-half count is >=`max(0,|F||L|−|F∩L|−2m)`. When both projected P4 endpoints have all outside chords occupied, >=`max(0,(a−4)(a−5)−2m)`. Does NOT prove any original GF5 selected-positive witness.

**J23 (ALL-h exact original source feasibility partitions, not positivity lower):** For L,R genuine occupied physical A-side completions per original proper P3, the 6LR proposed D6 source-factor matchings decompose EXACTLY into missing TRUE ORIGINAL incidence, present but misaligned A/A source-dual, or genuinely selected ORIGINAL D6; each 3L/3R proposed B/A or A/B wedge completion telescopes into missing source endpoint incidence, non-collinear/non-concurrent true original pair, physically conflicting doubled ORIGINAL factor, or genuine selected ORIGINAL B/A/A/B Q. Both true-original f,g remain globally complete and fixed for the WHOLE run, with no invented independence. Every final positive Q checked against independent JPKC006 source constructor; W32 additionally against full exhaustive 62,370-candidate true original seven-GF5 classifier.

**Strong finite PALETTE-ONLY NO-GO:** W(3,2) has V=15,a=6, so both physical images are necessarily COMPLETE K6. Every coordinate-proper P3 has exactly TWO physically occupied A-completions per side. Yet true low-S W32 maps have:
- S68: 544 real endpoint-bad proper P3; L=R=2 each; exactly 13,056 physical A/A matching proposals, 13,002 fail TRUE ORIGINAL incidence, 54 have all three true original source incidences but nonaligned A/A duals; **0 selected D6**. A-left/B-right wedge attempts 3,264 -> (2,594 missing endpoint source incidence, 380 noncollinear source pair, 288 doubled physical interference, **2 positive**); B-left/A-right 3,264 -> (2,682,318,258,**6**).
- S72: 600 real P3; L=R=2 each; 14,400 physical A/A match proposals, 14,316 absent original source incidences, 84 nonaligned true source A/A; **0 selected D6**. A-left/B-right 3,600 -> (2,816,462,318,**4**); B-left/A-right 3,600 -> (2,984,364,246,**6**).
- Despite PERFECT physical K6, only 8/544 (S68) and 10/600 (S72) original endpoint-bad seeds have ANY genuine selected positive ORIGINAL sixset Q. Thus physical-palette availability alone cannot guarantee a pointwise TRUE ORIGINAL GF5 extension; this is a finite method NO-GO, not a claimed infinite Branch B family.

**Honest bounded W34:** exact original source loss telescopes on 32 deterministic spread-out real endpoint-bad seeds each for lex, random, and genuine D4 symplectic-spread globally complete f,g; respective true-positive source seed coverage 31/32, 30/32, 31/32. NOT a random sample, NOT a full W34 positive sixset census, NOT an all-h extension statement.

**CI on final exact HEAD at issue update:** [JPKC007 dedicated #38442401650](https://github.com/definitely-stable/Mathlab/actions/runs/38442401650) **SUCCESS (7/7)**, [INDEX #38442401353](https://github.com/definitely-stable/Mathlab/actions/runs/38442401353) SUCCESS. [Proof Audit #38442401318](https://github.com/definitely-stable/Mathlab/actions/runs/38442401318) and [Research #38442401465](https://github.com/definitely-stable/Mathlab/actions/runs/38442401465) were still active/pending at writing; NO premature 4/4 acceptance. Independent mathematical review OPEN.

**Next justified JPKC-008:** source geometry+global physical injection coupled demand/Hall-deficit witness between shared original point and line factors. D6-AA4 #433 showed source-position two-bit Fréchet relaxation alone has zero positivity on W32 S68/S72. Do NOT return to image-only physical occupancy bounds; do NOT infer universal S=Ω(s^6), ASET exponent, or full R3 upper from J22–J24.

---

## Comment 160 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6153498877
- GitHub comment ID: 6153498877

### D6-AA4-C — exact all-h original-factor edit invariance and true original W32 transversals

[Draft PR #436](https://github.com/definitely-stable/Mathlab/pull/436) stacked on AA4-B #434 (all parent four CI SUCCESS), `main` untouched. New universal **conditional** invariance theorem: for arbitrary globally injective f,g and f',g' agreeing outside a fixed set B of original typed point/line factor identities, each previously seven-positive ORIGINAL six-incidence Q disjoint from B retains its exact class and certified GF5 weight. Hence `S(f',g') >= number of previously positive Q disjoint from B`, even if edited physical image sets change on both types. NO proof that any initial arbitrary f,g has a positive S.

On genuine fixed S68 and S72 W(3,2), enumerate each 62,370 original-left candidate and its seven-positive ORIGINAL source factor support. Independently exhaustive **2^15=32768** point-only and line-only source supports per map and **174,437** mixed 30-factor supports of edit sizes≤5 per map. Exact minimum hitting/transversal number **4** in every mode for BOTH maps. For arbitrary ≤3 typed source factor edits, certified old-Q survival S68≥**4**, GF5 numerator≥**182400**; S72≥**1**, GF5 numerator≥**45600**. At 4 edited factors old-Q survival floor becomes zero for some supports. This is the precise boundary of THIS old-positive support argument, NOT a proof 4 changes can zero the actual S.

AA4-B reconciliation: S68 original right block (0,1,2,3) keeps 10 old positives; S72 right block (1,7,9,12) keeps zero, yet the 24 coherent globally legal fixed-image completion states have S minimum **68** for S72. Thus old-Q survival and cross-Q new motif forcing are distinct exactly witnessed mechanisms.

Initial corrected dedicated run [#38454883036](https://github.com/definitely-stable/Mathlab/actions/runs/38454883036) SUCCESS. Exact finite spectra and independent negative-case candidate checks are now pinned in latest PR HEAD `714e9806463803d6721cd8e7dbe56f27072fae98`; final-head dedicated/INDEX/Proof Audit/Research CI still require verification. Independent math review remains open. Branch A/B OPEN, #230/#176/#169 OPEN; no full GF5 R3 or ASET exponent.

**Next genuine goal**: an all-h/source- and starting-map-independent positivity mechanism, not just finite edit resilience around fixed witnesses.

---

## Comment 161 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6153531952
- GitHub comment ID: 6153531952

### HYP-105 / issue #230 — JPKC-008 exact ORIGINAL Hall matching & global source-key rigidity (14 October 2026)

Created STRICT stacked [Draft PR #437](https://github.com/definitely-stable/Mathlab/pull/437), branch `research/hyp105-issue230-jpkc008-source-hall-coherence`, parent fully 4/4 green JPKC007 [#435](https://github.com/definitely-stable/Mathlab/pull/435) pinned HEAD `6816514f70f7a6d76e50c4066a284f9eb6ab23bd`. New JPKC008 HEAD `759627a707131f7efbbec6e65f1d9dced5abb7fe`. No main change or merge. Root A/B OPEN.

**J25 ALL-h exact (girth-8 ORIGINAL source uniqueness):** Every 3 distinct ORIGINAL GQ points and 3 distinct ORIGINAL lines admit at most ONE perfect point-line incidence matching. Two different perfect matchings would create an alternating 4- or 6-cycle, impossible in a genuine GQ incidence graph. No f/g assumptions.

**J26 ALL-h exact Hall criterion:** `d_H(P,L)=max_{A⊆P} (|A|-|N_L(A)|)`, 7 nonempty subsets. d_H=0 iff the UNIQUE matching of three actual ORIGINAL incidences exists; if >0 an explicit deficient source point subset witnesses impossibility.

**J27 ALL-h exact shared-source source demand telescope:** For every real endpoint-bad original physical P3 seed and each actual pair of physically available A-left/A-right completion triples, count one ORIGINAL Hall key (P,L). Cache the true unique source matching across repeated demands on a fixed complete globally injected f,g. If T_pair=sum L_t*R_t and T_Hall is number of Hall-feasible occurrences, then `6*T_pair-T_Hall` is EXACTLY JPKC007's old six-permutation original incidence mismatch count; `T_Hall=T_nonaligned_AA+T_selected_D6`. Selected D6 requires positional original left/right A/A dual alignment; Hall alone is insufficient.

**J28 ALL-h restricted source-key rigidity / cross-anchor NO-GO:** An A-half source point triple's three true physical f(p) edges form a P4; its two degree-one endpoints uniquely determine q by global injectivity. The right g(ell) A-half determines r. Therefore the combined exact 3×3 source demand key (P,L) determines ONE original nonincident GQ anchor (q,r), and CANNOT be reused across different GQ anchors. Repeated demands CAN occur across different physical P3s WITHIN the same anchor. This closes the naive duplicate-key cross-anchor expansion route; any future global expansion must couple DIFFERENT source keys through shared underlying original factors and/or physical label capacity, not deduplicate the same key.

**J29 ALL-h exact global source 3-matching capacity:** For V=(s+1)(s²+1), d=s+1, N=Vd, the number M3 of three-edge matchings in the ORIGINAL incidence graph is `C(N,3)-N*(d-1)*(N-2)+N*C(2*(d-1),2)-2*V*C(d,3)`; it EQUALS the number of Hall-feasible original (3-point,3-line) factor keys because J25 makes the matching unique. This follows from independent triple counting in the line graph of the regular ORIGINAL GQ incidence graph (N vertices, degree 2(d-1), N(d-1) edges, 2V*C(d,3) triangles). At W32 the exact value is **10,560** Hall-feasible pairs of **207,025** original source 3×3 pairs. This is original capacity, NOT demanded-source lower nor selected GF5 positivity.

**Initial hosted exact ORIGINAL W32 data** on implementation HEAD `11f120177bef435f6b57ceaed622a572240cf7dc`, specialized CI [#38454773389](https://github.com/definitely-stable/Mathlab/actions/runs/38454773389) **SUCCESS (6/6)**:
- W32 lex: 3,144 source key demand occurrences, 1,380 distinct keys, 1,764 repeated occurrences; 288 Hall-feasible, 224 nonaligned, 64 selected D6; 0 keys across distinct original GQ anchors.
- W32 reverse: 2,704 / 1,228 distinct / 1,476 repeats; 152 feasible, 128 nonaligned, 24 selected D6; 0 cross-anchor.
- W32 S68: 2,176 / 1,016 distinct / 1,160 repeats; 54 feasible, all 54 nonaligned, 0 selected D6; 0 cross-anchor.
- W32 S72: 2,400 / 1,092 distinct / 1,308 repeats; 84 feasible, all 84 nonaligned, 0 selected D6; 0 cross-anchor.
- W34 lex/random and true D4 spread: 8 distributed real endpoint-bad P3 per map, 47/43/55 Hall-feasible occurrences, 9/4/9 actually aligned D6. This is STRICTLY targeted, not a W34 full seven-class census.

**Latest final HEAD CI (not yet accepted):** dedicated [#38455335140](https://github.com/definitely-stable/Mathlab/actions/runs/38455335140) verifying J28/J29 additions, INDEX [#38455335318](https://github.com/definitely-stable/Mathlab/actions/runs/38455335318) SUCCESS; Proof Audit [#38455335216](https://github.com/definitely-stable/Mathlab/actions/runs/38455335216) and Research [#38455335145](https://github.com/definitely-stable/Mathlab/actions/runs/38455335145) still running/pending as last verified. No 4/4 claim, independent math review OPEN, root #230/#176/#169 OPEN.

**Next justified JPKC-009:** formulate and test quantitative cross-key incidence overlap/expansion + genuine positional alignment of ORIGINAL matched triples, or integrate with coherent factor injection fibers of D6-AA4-B [#434](https://github.com/definitely-stable/Mathlab/pull/434). Avoid impossible exact-key cross-anchor sharing J28. No root A/B, no full R3/ASET.

---

## Comment 162 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6159452157
- GitHub comment ID: 6159452157

### D6-AA4-D — exhaustive mixed two-type global injection feasibility implementation

New stacked [Draft PR #438](https://github.com/definitely-stable/Mathlab/pull/438), parent fully green #436 at pinned HEAD `714e9806463803d6721cd8e7dbe56f27072fae98`; `main` unchanged, #230/#176/#169 and Branch A/B OPEN.

**All-h exact conditional statement:** freeze actual ORIGINAL W(3,s) f,g outside typed original factor blocks BP and BL. The legal globally injective point/line pair label completions have `(m+|BP|)_{|BP|} (m+|BL|)_{|BL|}` states with m=K−V; every original point/line label is identical across every incidence sixset that shares that factor. For any such complete choice, the previous AA4-C old-Q survival bound is valid, and the coherent exact full GF5 necessary seven count is computed from ORIGINAL six positions. This is not a global Ω(s^6) proof.

**New exhaustive finite ORIGINAL W32 protocol:** For each frozen S68 and S72, inspect ALL C(30,4)=27,405 typed ORIGINAL point/line source factor edit blocks. AA4-C source-transversal numbers verify exactly **53 S68** and **119 S72** potentially zero-old-survivor supports. Every other size-four edit block retains a genuine ORIGINAL positive Q and cannot yield S=0. For EACH of those 172 critical source blocks, exhaust ALL `bP! bL!` globally legal W32 complete point+line physical bijections, classify seven GF5 necessary classes using original-position cylinders, independent historical exact `seven_census` crosschecks on representatives of every split, and report min S, selected GF5 floor, zero-S completions and a universal neighborhood edit-radius-four lower bound relative to each pinned initial map. No independent per-Q physical assignments, no W34 full sixset scan, and no physical edge labels shared within a typed original factor map.

Current implementation SHA `c81901450c736dd4643b205f2e51d37c8c4330b0`: original 27,405-block unit/oracle job SUCCESS; separate complete S68/S72 GitHub-hosted matrix jobs in progress. Initial unit-negative test corrected to exercise lazy generator validation. Full specialized/INDEX/Proof Audit/Research acceptance must be checked against exact final head; no final finite values asserted before hosted results. Documentation `docs/research/HYP-105-ISSUE230-D6AA4D-MIXED-TRANSVERSAL-FIBERS.md`.

---

## Comment 163 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6159489688
- GitHub comment ID: 6159489688

### HYP-105 #230 — JPKC-009 cross-key ORIGINAL source factor overlap & exact 3factor Hall capacity (14 Oct 2026)

Created strictly stacked [Draft PR #439](https://github.com/definitely-stable/Mathlab/pull/439) on 4/4-green JPKC-008 [#437](https://github.com/definitely-stable/Mathlab/pull/437), exact parent HEAD `759627a707131f7efbbec6e65f1d9dced5abb7fe`. Final new JPKC009 HEAD `a3b7d749604896dcbaeae5e594cc2ac6d087e49f`. NO main mutation, NO merge. Root A/B OPEN.

**J30 all-h source one-sided endpoint rigidity:** A genuinely occupied physical A-half triple of 3 distinct ORIGINAL point factors is a 3-edge physical P4; its two degree-one vertices uniquely fix original q via global f injection. Dual true original line triple fixes r via global g. Different source keys sharing ONLY one factor triple can therefore link DIFFERENT original GQ anchors, despite JPKC008 J28 proving identical FULL source pair (P,L) cannot.

**J31 all-h EXACT original fixed-three-point Hall capacity:** For any 3 distinct ORIGINAL GQ points P, d=s+1, c(P)=number of original collinear pairs among P and t(P)=1 iff all 3 points lie on one original line, the number of DISTINCT 3-original-line factor triples L admitting a unique perfect original incidence matching is `Cap(P)=d³-d*c(P)+2*t(P)`. Inclusion-exclusion among three original incident source line choices and girth8 J25 uniqueness. Exact dual for fixed three ORIGINAL lines. Every true demanded Hall-feasible source node degree bounded above by its corresponding Cap. An upper, NOT an existence lower.

**J32 all-h exact independent sum:** Sum all fixed-original-three-point capacities:
`Σ_P Cap(P)=C(V,3)*d³ - d*V*C(d,2)*(V-2) + 2*V*C(d,3)`, identically equal to independently proved JPKC008 J29 line-graph ORIGINAL three-matching count. At W32, full independent direct check of all 455 ORIGINAL point triples × d³ source line choices and all 455 dual ORIGINAL line triples × d³ source point choices yields EXACT **10,560** matched unique source factor pairs. Algebraic two-formula comparison also checked at TRUE W34.

**J33 original bipartite demanded-source graph:** left vertices genuine ORIGINAL point triples P, right genuine ORIGINAL line triples L, edges DISTINCT full demanded source pairs (P,L). Edge count and ALL-h exact cross-anchor overlap decomposition `Cross_left=Σ_P[C(deg P,2)-Σ_r C(deg_r P,2)]`, and dual `Cross_right` over shared source right L, distinguish repeated physical-path copies from DIFFERENT full keys meeting at one source triple and lying on different original (q,r) anchors. Every edge retains one true original Hall matching status, original physical source f/g and actual original D6 selected position.

**J34 ALL h nested support, strict finite method NO-GO:** D=all DISTINCT true demanded source keys, H=Hall-feasible keys, A=keys producing a genuine selected original GF5 D6 Q on at least one actual seed. Then `A⊆H⊆D`, `0<=Cross(A)<=Cross(H)<=Cross(D)` for either left or right ORIGINAL source triple overlaps. Fully checked TRUE ORIGINAL W32 (left raw→Hall→D6; right likewise):
- lex left **4,616→47→5**, right **4,792→59→5**;
- reverse left **3,912→13→0**, right **3,784→10→0**;
- S68 left **2,632→1→0**, right **2,696→4→0**;
- S72 left **2,928→7→0**, right **3,312→3→0**.
Thus even NONZERO genuinely Hall-feasible original cross-GQ-anchor overlap need not produce a positive ORIGINAL D6. This closes naive Hall-overlap→D6 implication at finite W32; it is NOT an all-h Branch B counterexample and does not exclude OTHER true seven-GF5 classes.

**W34 TRUE original finite stress:** 8 distributed proper endpoint-bad P3 each for lex, random and independently genuine D4 symplectic spread, complete original source-demand/Hall star and exact D6 positional checks PER selected seed; genuine D4 right-side 186,543 raw cross-anchor key pairs → 1 Hall-feasible → 0 selected D6. Absolutely NO full W34 seven-family census or probability/infinite inference.

**Implementation:** four new files: exact ORIGINAL all-h theorem/limitations doc, independent source three-factor capacity and cross-key Python implementation, 6 rigorous GitHub-hosted independent acceptance tests, dedicated CI workflow. Original f/g globally fixed throughout. No self-hosted CI. Final-head focused run [#38500736452](https://github.com/definitely-stable/Mathlab/actions/runs/38500736452) SUCCESS (6/6); INDEX [#38500736434](https://github.com/definitely-stable/Mathlab/actions/runs/38500736434) SUCCESS. Full Research [#38500736388](https://github.com/definitely-stable/Mathlab/actions/runs/38500736388) and Proof Audit [#38500736466](https://github.com/definitely-stable/Mathlab/actions/runs/38500736466) not yet confirmed complete at posting; independently review before merge. NO root positive S=Ω(s6), full R3 or ASET exponent.

**Next warranted JPKC-010:** test genuinely NEW global cross-key/cross-source-factor positive-GF5 compensation involving both D6 AND original non-GQ point/line wedge classes under original GQ and globally occupied f,g constraints. D6-AA4-B #434 original coherent fiber positivity is a potential source-consistency lever; merely counting raw/Hall source triple overlap is now explicitly falsified as sufficient. Keep #230/#176/#169 OPEN.

---

## Comment 164 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6159567337
- GitHub comment ID: 6159567337

### D6-AA4-D FULL HOSTED ACCEPTANCE — exact two-typed source-factor zero-feasibility

[Draft PR #438](https://github.com/definitely-stable/Mathlab/pull/438), final head `c81901450c736dd4643b205f2e51d37c8c4330b0`, stacked on fully green #436; **main unchanged**.

ALL FOUR required GitHub-hosted workflows on that exact final SHA are **SUCCESS**: [AA4-D #38500405100](https://github.com/definitely-stable/Mathlab/actions/runs/38500405100) (dedicated source-partition unit oracle + independent exact full S68/S72 matrix), [INDEX #38500405143](https://github.com/definitely-stable/Mathlab/actions/runs/38500405143), [Proof Audit #38500405082](https://github.com/definitely-stable/Mathlab/actions/runs/38500405082), [full Research #38500405096](https://github.com/definitely-stable/Mathlab/actions/runs/38500405096). Independent mathematical peer review remains open.

**Exact all-h conditional theorem:** in genuine W(3,s), freeze complete typed physical pair maps f,g outside arbitrary ORIGINAL point block BP and line block BL. With V source factors of each type, K=C(a,2) physical pair labels, m=K−V free, legal globally injective completed pair maps have exactly `(m+|BP|)_(|BP|) * (m+|BL|)_(|BL|)` possibilities. All shared ORIGINAL factors retain one physical label across all sixsets. The exact coherent seven-positive minimum over these complete maps is >= AA4-C's old-positive ORIGINAL source-factor survivors. This statement does NOT imply `S_s >= cs^6` uniformly over all f,g,h.

**New finite genuine ORIGINAL W32 all-radius-four zero exclusion**: for each pinned S68/S72, inspect ALL **C(30,4)=27,405** possible typed ORIGINAL factor edit supports. Those missing some old positive Q are proven S>=1 for ANY complete globally injective reassignment. Every remaining original-source hitting set is checked by ALL genuine legal complete left+right physical pair map permutations (not independent per-sixset labels):

| Verified property | S68 | S72 |
|---|---:|---:|
| Exact size-four source-transversal blocks | **53** | **119** |
| Complete original typed-point AND typed-line global map completions | **734** | **1,210** |
| Completions with S=0 | **0** | **0** |
| Min seven-S over all true critical completed map fibers | **68** | **68** |
| Min selected necessary GF5 floor numerator | **3,112,510** | **3,104,080** |
| Independent historical full-original seven_census spotchecks across 5 split types | **10** | **10** |

S68 per-original-point split p=0..4: counts **(22,12,8,9,2)**, legal completions **(528,72,32,54,48)**, all min S **68**. S72 splits: counts **(27,29,31,28,4)**, completions **(648,174,124,168,96)**, minima **(68,68,72,72,69)**.

**Strict conclusion:** for EVERY complete physically injective W(3,2) map pair f',g' differing in **AT MOST FOUR ORIGINAL typed point/line factor assignments** from the pinned S68 respectively S72, `S_2(f',g') >= 1`. In the special source-transversal fibers, stronger exact minima above hold. The total 4-edit ball is **NOT** claimed to have S>=68 because nontransversal supports are certified by old-positive survival, potentially only 1.

Neither a universal all-h Branch A lower, an infinite Branch B family, the full GF5 R3, nor an ASET power follows from this fixed-reference finite result. Keep #230/#176/#169 OPEN. Next mathematically justified gate: source/initial-label-INDEPENDENT global capacity and overlapping coherent fiber dual certificates; avoid blindly scaling 4-edit neighborhoods to 15!^2 W32 assignments.

---

## Comment 165 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160145383
- GitHub comment ID: 6160145383

### JPKC-010 implementation opened — exact mixed original D6/B–A/A–B witness transfer

Created stacked research-only [Draft PR #440](https://github.com/definitely-stable/Mathlab/pull/440) above JPKC-009 #439 at pinned parent HEAD `a3b7d749604896dcbaeae5e594cc2ac6d087e49f`. New PR HEAD `a8b01acea77c913bf1934f74931e127ef3f03fee`; **main untouched**; #230 Branch A/B remain OPEN.

- **J35 (all-h exact conditional ledger):** on ONE complete true ORIGINAL globally injective point/line map, per-physical endpoint-bad P3 and ORIGINAL six-incidence Q, independent Hall-matched D6 Q *sets* must equal JPKC-006 source-topology D6 Q sets. Positive wedge classes B-left/A-right and A-left/B-right use true original incidence IDs and exact selected GF5 positional classifier. No Hall-only witness promoted to positive.
- **J36 (existing J19 cap applied jointly):** `S >= ceil(W_D6/12)+ceil(W_BA/8)+ceil(W_AB/8)`. Distinct positive Q are counted once, with an additional cross-anchor positive Q incidence-sharing graph deduplicated by ORIGINAL incidence IDs. This bound may be zero; it does not prove Ω(s^6).
- **J37 (conditional exact coherent finite fiber):** compare all 24 globally injected W32 S68 and all 24 W32 S72 right-factor permutations in the same original blocks as D6-AA4-B; independent full ORIGINAL seven_census on each complete map. Tested via two separate GitHub-hosted matrix jobs, not per-Q free assignments.

Dedicated tests include exact W32 lex/reverse/S68/S72, targeted true W34 lex/random/D4 symplectic spread, independent full W32 accepted-sixset oracle, invalid-map and budget controls. Four GitHub-hosted workflows (dedicated, INDEX, Proof Audit, full Research) presently running on new PR exact HEAD; results pending. No merge or all-h A/B claim. Documentation `docs/research/HYP-105-ISSUE230-JPKC-010-MIXED-POSITIVE-TRANSFER.md`. Independent mathematical peer review remains open.

---

## Comment 166 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160171488
- GitHub comment ID: 6160171488

### D6-AA4-E — all-h global assignment weak dual and exact unary NO-GO (14 Oct 2026)

Created strictly stacked **Draft PR [#441](https://github.com/definitely-stable/Mathlab/pull/441)** on pinned 4/4-green D6-AA4-D [#438](https://github.com/definitely-stable/Mathlab/pull/438) HEAD `c81901450c736dd4643b205f2e51d37c8c4330b0`; new final head `b923eb4a186809908009a82d413c45c36fbe2ad4`. No `main` writes, merges or root issue closure.

**All-h rigorous conditional inequality:** for every genuine ORIGINAL W(3,2^h) six-incidence cost `c_Q`, arbitrary signed rational local unary prices `u_{Q,v,e}` yield

`forall globally independent typed injections f,g: S_s(f,g) >= sum_Q alpha_Q(u) + A_P(U) + A_L(U)`,

where each `alpha_Q` is the minimum of the **true ORIGINAL positional GF5 motif cost minus unary prices over ALL locally typed-injective physical labels**, and `A_P,A_L` are the two independent globally injective min-cost assignments, cross-type edge reuse allowed. The proof is exact local minorant summation; it does NOT supply an all-h positive family of prices.

**Exact analytic NO-GO for general unary approach:** 3 same-type factors with 3 pairwise cyclic-successor constraints have genuine full global minimum 1, while **sup over ALL unary global matching dual prices =0**: each local zero-cost relation has uniform singleton marginals, equal to the marginals of the uniform distribution over all 6 global bijections. No tuning of one-factor prices alone can close this general gap. This is not a genuine-GQ GF5 counterexample. Two contrasting exact toys give local-minimum 0 -> sharp global-dual 1.

**Actual ORIGINAL W32** S68 and S72 images occupy identical full K6 physical edge sets on both types but accepted seven-family scores differ 68 vs 72, GF5 numerators 3,112,510 vs 3,283,610. Image occupancy is not sufficient to reconstruct the actual original-source-incidence count; this does not disprove a possible universal occupancy-based lower.

**GitHub-hosted exact FINAL HEAD results so far:** dedicated [#38505959348](https://github.com/definitely-stable/Mathlab/actions/runs/38505959348) SUCCESS (8/8 independent tests + original W32 report); INDEX [#38505959365](https://github.com/definitely-stable/Mathlab/actions/runs/38505959365) SUCCESS. Proof Audit [#38505959379](https://github.com/definitely-stable/Mathlab/actions/runs/38505959379) and Research [#38505959378](https://github.com/definitely-stable/Mathlab/actions/runs/38505959378) active when checked; **no premature 4/4 claim**. Independent mathematical review OPEN.

**Scientific outcome:** `OPEN_WITH_FORMAL_BLOCKER`; neither Branch A universal `c s^6` nor infinite Branch B, full R3 or new ASET exponent. **Next justified D6-AA4-F:** genuine ORIGINAL GF5 pair/triple separator / cycle-consistency certificate validated against 3-factor analytic counterexample, D6-X/Y pseudo-distributions and AA4 finite witnesses.

---

## Comment 167 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160235619
- GitHub comment ID: 6160235619

### JPKC-010 #440 — hosted finite results and joined JPKC-009 proof evidence

Final implementation HEAD `0500f7846636f1e25f83e43e1f7eeef53cacf6cd` in [Draft PR #440](https://github.com/definitely-stable/Mathlab/pull/440), strictly stacked on #439; `main` unchanged.

**Same real ORIGINAL W32 f,g** full endpoint-bad census and per-source original-sixset exact oracle membership **and completeness**: lex 786 seeds → 68 distinct positive Q, J19 mixed floor 26; reverse 676→31, floor 11; S68 544→**4**, floor **2**; S72 600→**5**, floor **2**. S68 has **8 positive wedge-only seeds and D6=0**; S72 has **10 positive wedge-only seeds and D6=0**. Thus B/A alternatives give actual **finite** positives after Hall→D6 collapse, but witness charge 2 is much smaller than full seven-S 68 or 72. This shows both successful local rescue and a substantial incompleteness of the three-class seed-local approach.

**JPKC-009 cross-anchor raw→Hall→selected D6** *recomputed on same f,g as mixed positives*: lex left 4616→47→5 / right 4792→59→5; reverse 3912→13→0 / 3784→10→0; S68 2632→1→0 / 2696→4→0; S72 2928→7→0 / 3312→3→0. No statistical or causal inference between these counts and wedge positives.

**Full coherent same-source four-original-line injection fibers**, 24 out of 24 legal W32 assignments per S68 and S72, independently audited with true-original seven GF5 census: min full seven-S both **68**; min reached Q **4/3**, min class charge **2/2**. In each fiber some states have D6=0 while others have D6>0. True W34 lex/random/original D4 spread only 4 distributed seeds per map, not full W34 S.

Final-head [specialized #38506412810](https://github.com/definitely-stable/Mathlab/actions/runs/38506412810) SUCCESS (5/5 tests and both full 24-state matrix jobs); [INDEX #38506412895](https://github.com/definitely-stable/Mathlab/actions/runs/38506412895) SUCCESS. Proof Audit #38506412884 and full Research #38506412812 still require exact-head SUCCESS verification. **Root A/B OPEN, no unconditional S=Ω(s^6), no full R3/ASET exponent, independent mathematical review open; no merge.**

---

## Comment 168 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160387925
- GitHub comment ID: 6160387925

### JPKC-011: full seven-class ORIGINAL sixset visibility — Draft PR #442

Implemented [Draft PR #442](https://github.com/definitely-stable/Mathlab/pull/442) stacked strictly on fully 4/4-green [JPKC-010 #440](https://github.com/definitely-stable/Mathlab/pull/440), pinned parent HEAD `0500f7846636f1e25f83e43e1f7eeef53cacf6cd`. Final new research HEAD `5610246a0407a74d4f71c22bc53f01ac424f3740`. Main unchanged; NO merge. Root A/B remain OPEN.

**J38 all-h exact partition:** every accepted ORIGINAL six-incidence Q (all seven GF5 classes, one fixed globally injected f,g) is classified into (1) genuine original endpoint-factor-bad proper P3 detected by JPKC010; (2) broad physical projection blocked but not source endpoint-factor-bad; (3) other physically coordinate-proper P3 only; (4) NO physically coordinate-proper P3. Four strata are disjoint and complete, including frozen 51-column GF5-weight decomposition. Crucial distinction between (1) and (2) was independently found during hosted falsification; a physical internal-row/column projection obstruction is NOT automatically an endpoint-factor collision.

**J39 all-h C-half original sixsets cannot host proper synchronized P3:** underlying physical C-half six-edge projection is 3 doubled disjoint two-cycles, hence a matching rather than a four-coordinate P4. J15/J17 separately prohibit B/B endpoint-factor-bad positive completions, without excluding other valid P3s.

**Independent TRUE ORIGINAL W32 full physical-vs-source local tests:** 62,370 original left-sixcoordinate candidates, all accepted Q exactly once, all 20 original incidence-three subsets per accepted Q, direct 2^3 original diagonal realization and path-status reconstruction crossmatched to independently enumerated full global K2 physical path index; JPKC010 original positive-Q ledgers confirmed for strict factor-endpoint-bad category.

**Exact hosted W32 pins** (full S / strict endpoint-factor bad / projection-only / other proper / completely proper-P3-invisible): lex **259/68/5/17/169**; reverse **169/31/4/4/130**; S68 **68/4/1/0/63**; S72 **72/5/0/1/66**. Thus **63/68=92.65%** and **66/72=91.67%** of low-S globally realizable maps' seven-class positive ORIGINAL Q have NO coordinate-proper P3 AT ALL. S68 invisible Q include **41 B-left/A-right + 19 A-left/B-right + 3 B/B** (no C and no D6), so the invisible phenomenon is not an artifact of C-half topology. S72 invisible 66 split **33 B/A + 28 A/B + 3 B/B + 2 C/A**. This is a finite methodological obstruction to P3-only proof routes, **not** an all-h asymptotic result or Branch B witness.

**Complete frozen coherent four-original-line right-fibers:** all 24 genuine globally injected maps each S68/S72; min complete full S **68/68**, min completely P3-invisible Q **63/61**, min not detected by JPKC010 **64/61**. Different minima need not share a map. No full W34 seven-family count is claimed.

Final-HEAD [dedicated 3-job run #38507600949](https://github.com/definitely-stable/Mathlab/actions/runs/38507600949) SUCCESS and [INDEX #38507600934](https://github.com/definitely-stable/Mathlab/actions/runs/38507600934) SUCCESS; Proof Audit #38507600954 and full Research #38507600963 require final exact-head conclusion check. Independent proof review OPEN. **Next research target:** original incidence six-factor / GF5 positional tensor or polynomial coefficient counting DIRECTLY, not conditioned on existence of a synchronized proper physical P3.

---

## Comment 169 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160517005
- GitHub comment ID: 6160517005

### HYP-105 JPKC-012 — direct ORIGINAL six-factor GF5 incidence tensor (14 October 2026)

Created stacked research-only [Draft PR #443](https://github.com/definitely-stable/Mathlab/pull/443), strict child of now 4/4-CI-green JPKC-011 [#442](https://github.com/definitely-stable/Mathlab/pull/442) at exact parent HEAD `5610246a0407a74d4f71c22bc53f01ac424f3740`. Final implementation HEAD `edf373d93024f5546b4b96cf094032cd51adaeb0`; main untouched, no merges, Root A/B OPEN.

**J41 exact all-h source-factor tensor factorization:** for fixed true original W(3,s) and globally injective f,g, compile the exact nonnegative sparse tensor of left leafless original six-incidence Q indexed by original left source factor type A/B/C, original right line multiset with multiplicities, and B/B original-incidence overlap. For each right factor multiset, right physical 2-regularity is one predicate on ONE shared globally injected g, not independently reassigned labels per Q. Six non-D6 seven-GF5 sectors follow by tensor contraction.

**J42 original-line-NAMED positional dual:** D6 A/A sector is treated separately by the six-original-line-normalized left dual cycle, requiring exact equality to the right global g dual and connectedness. Merely two physical 2-regular sides or Hall-match feasibility are not accepted as D6. No physical P3 requirement in J41/J42.

**New independent W32 exact-cover generator:** 130 degree-two physical multigraphs on K6 (70 simple +45 edge-doubled/C4 +15 three-doubled matching), expanded via genuine original incidence choices into 62,370 distinct original left 6-coordinate candidates. The complete new tensor matches existing independent original seven_census for all seven classes and weighted 51-column necessary GF5 floor on genuine lex/reverse/S68/S72. Right source line profile counts lex/reverse 21,950, S68/S72 17,890; sparse primary rows 29,523 / 25,032; positional D6 dual rows 20,317 / 21,369 respectively. Exact S lex=259, reverse=169, S68=68, S72=72.

**J43 24/24 globally coherent original right four-factor state fibers:** S68 independently optimized source-line-profile positive minima sum **11**, coherent minimum full S **68**, exact coherence gap **57**, **7** individual source-line profiles positive in all 24 states, sufficient greedy cover **1** source profile. S72 independent profile minima sum **0**, coherent min **68**, gap **68**, **0** individually unavoidable source profiles, sufficient greedy cover **4** source profiles. Each legal right global g is shared by all real Q. Greedy cover not asserted optimal, and distinct minima can occur at different states. No all-h Ω(s^6) inference from finite fibers.

[Specialized final HEAD run #38508564133](https://github.com/definitely-stable/Mathlab/actions/runs/38508564133) SUCCESS (5/5 independent/fail-closed tests and both all-24 global fiber jobs); [INDEX #38508564131](https://github.com/definitely-stable/Mathlab/actions/runs/38508564131) SUCCESS. [Proof Audit #38508564135](https://github.com/definitely-stable/Mathlab/actions/runs/38508564135) and [Research #38508564194](https://github.com/definitely-stable/Mathlab/actions/runs/38508564194) require exact-final-head SUCCESS verification. Independent mathematical review OPEN. Universal source-profile positivity transfer inequality across ALL f,g,h is still the explicit blocker; issue #230 / Root A/B remain OPEN. No full W34 seven-S census or ASET exponent claim.

---

## Comment 170 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160546230
- GitHub comment ID: 6160546230

### HYP-105 #230 — D6-AA4-F full ORIGINAL W32 pair→triple coherence separation (14 Oct 2026)

New strict stacked [Draft PR #444](https://github.com/definitely-stable/Mathlab/pull/444) on 4/4-green D6-AA4-E [#441](https://github.com/definitely-stable/Mathlab/pull/441), pinned parent `b923eb4a186809908009a82d413c45c36fbe2ad4`, new final HEAD `1e44610b79ca1edcda872bce38f5524167b61181`. No main changes/merges.

**All-h conditional theorem:** freeze arbitrary true ORIGINAL W(3,2^h) complete two-type global maps outside any three typed ORIGINAL source factor block B. For exact ORIGINAL seven-class GF5 Q-local costs, with correct source dependencies and disjointly grouped Q: `0<=L_independent_Q<=L_pair<=L_triple = min_{ALL globally injected completions of B} S(f',g')`. No assumed Q-wise physical label independence; all 6 original incidence positions maintained. This is not a universal positive lower bound for all starting maps.

**Analytic finite pair consistency NO-GO:** three cyclic successor constraints on three bijective same-type factors have all pairwise zero-cost pseudomarginals singleton-consistent; exact 3-factor global cost must be 1. `(L_ind,L_pair,L_triple)=(0,0,1)`, proved for all actual triple assignments.

**New exact true ORIGINAL W32 hosted result:** [specialized #38508765918](https://github.com/definitely-stable/Mathlab/actions/runs/38508765918) **SUCCESS** across tests and BOTH complete S68/S72 matrices. On **four selected genuine size-3 subblocks of source-four transversals** (point and line separately) the `L_ind / L_pair / L_triple` seven-positive sequences are:
- S68 3 original points **4 / 66 / 68**, GF5 numerator **182400 / 3021310 / 3112510**;
- S68 3 original lines **15 / 59 / 68**, GF5 **684000 / 2702700 / 3112510**;
- S72 3 original points **10 / 67 / 72**, GF5 **455410 / 3055610 / 3283610**;
- S72 3 original lines **10 / 71 / 72**, GF5 **456000 / 3238010 / 3283610**.

Each of 6 full complete global permutations per original triple is independently counted via 62,370 genuine ORIGINAL sixset candidates and same historical seven-GF5 classifier; exact source-dependent per-Q and weighted 51-palette tables recomposed. These are strict **real finite** pair→triple gaps `+2,+9,+5,+1`; no claim across all W32 maps or h>=2.

Final SHA INDEX [#38508765717](https://github.com/definitely-stable/Mathlab/actions/runs/38508765717) SUCCESS; Proof Audit [#38508765783](https://github.com/definitely-stable/Mathlab/actions/runs/38508765783) and Research [#38508765761](https://github.com/definitely-stable/Mathlab/actions/runs/38508765761) not yet confirmed complete as of posting. Independent review OPEN. **OPEN_WITH_FORMAL_BLOCKER**: still no global universal `c*s^6` or infinite Branch B, no full GF5 R3, no ASET exponent. Next D6-AA4-G: test actual ORIGINAL W32 cycle/triple-aware minorant against prior D6-X/Y pseudodistributions and seek an all-h starting-map-independent certificate; avoid physical-P3-only surrogates after JPKC-011 visibility NO-GO.

---

## Comment 171 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160913531
- GitHub comment ID: 6160913531

### JPKC-013 — exact GLOBAL right-injection compatibility (Draft PR #445)

Created [PR #445](https://github.com/definitely-stable/Mathlab/pull/445), stacked strictly on JPKC-012 #443 at parent `edf373d93024f5546b4b96cf094032cd51adaeb0`. Research-only; main unchanged, no merges, issue #230 Root A/B OPEN.

**J44 (all-h exact locality):** for a genuine ORIGINAL right-line multiset profile m (including positional D6), the true positive original-six-incidence count S_m(f,g) depends only on g restricted to the original right lines appearing in m. Verified via identical restriction value classes across all legal frozen W32 24-state fibers, with one complete shared globally injected right g in every state.

**J45 (all-h conditional injection matching-cover inequality):** for a FIXED legal right-factor block-completion family F, if selected true source profiles U have positive-cylinder sets covering every globally injective completion in F, then sum_{m in U} 1[S_m>0] >= 1 and full S>=sum_{m in U}S_m>=1 for every completion in that F. A cover is NOT asserted to exist uniformly over all f,g,s.

**J46 (exact minimal cardinality on full finite fibers):** original source profile masks on all 24 legal right four-line maps (same original labels across all Q); exhaustive finite source-profile mask dominance and memoized search RULES OUT every smaller cover size. S68 has exact minimal cardinality **1** (one original right-line source profile covers all 24), finite min S **68**, per-profile coherence gap 57, cover-source minimum positive Q count **1**, 7 individually positive-all-state source profiles. S72 has exact minimal cardinality **4** (no cover of 1,2,3 profiles exists), finite min S **68**, profile-minima sum 0, coherence gap 68, cover-source minimum **1**, zero universally-positive single source profile. Each of the four selected S72 witness original right-line profiles depends on movable ORIGINAL line 7 alone, and its 24-bit positive mask has exactly 6 states. The four masks are pairwise disjoint and cover all 24 states: a finite one-source-factor 4-value matching certificate, not an all-h obstruction.

True original S72 source-line profiles selected for this precise finite certificate: `(0,2,6,7,8,10)`, `(0,2,3,6,7,8)`, `(0,0,4,7,8,14)`, `(2,3,4,7,10,11)`; respective exact 24-bit state masks: `3194883`, `12583692`, `199728`, `798912` (all popcount 6, union 16777215, pairwise disjoint). Their ORIGINAL positive Q counts are 1 whenever active. This gives a checkable alternative to falsely treating independently zeroable source profiles as jointly zeroable.

[Dedicated final-current HEAD run #38511463301](https://github.com/definitely-stable/Mathlab/actions/runs/38511463301) SUCCESS (5/5 tests plus both complete 24-state independent GF5 matrix jobs); [INDEX #38511463026](https://github.com/definitely-stable/Mathlab/actions/runs/38511463026) SUCCESS; [Proof Audit #38511463027](https://github.com/definitely-stable/Mathlab/actions/runs/38511463027) SUCCESS; [full Research #38511463132](https://github.com/definitely-stable/Mathlab/actions/runs/38511463132) was in progress at last verification. Exact current head `c0d6401ad786b3da05c666b3b50c60fb82c24339`. Independent mathematical proof review remains required before acceptance.

No all-h S=Omega(s^6), infinite correlated low-S counterfamily, full W34 GF5 seven-census, or ASET exponent has been proved. Next research question: lift finite cylinder cover into a genuine all-injection source-capacity inequality with a quantitative s^6 charge; do not infer such a theorem from finite W32 24-state injection masks.

---

## Comment 172 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6160941385
- GitHub comment ID: 6160941385

### D6-AA4-G full ORIGINAL W32 hosted acceptance results — 14 Oct 2026

Strict stacked [Draft PR #446](https://github.com/definitely-stable/Mathlab/pull/446) on all-4-hosted-green [D6-AA4-F #444](https://github.com/definitely-stable/Mathlab/pull/444). Exact new HEAD `f68d6de96af77035ad66dbe5b8cfecd061fd94e4`. No merge or main modification.

**Exact all-h conditional source separator theorem:** for every true ORIGINAL W(3,2^h) globally typed-injective map with all source labels frozen outside arbitrary 4 typed factors, nonnegative seven-GF5 Q costs satisfy `L_ind <= L_two_triads <= L_shared_two_factor_separator <= L_exact_joint_4`. The 12 ordered shared-two-factor triad covers count each ORIGINAL Q exactly once, preserve original factor identities across all Q and full GF5 6-position classification. This remains conditioned on fixed outside assignments and is not universal Branch A.

**Critical new finite experiment:** For both S68/S72 and genuine first ALL-point and ALL-line size-four ORIGINAL source transversals, exhaust EVERY 4!=24 globally injective K6 map completion, classify all 62,370 actual ORIGINAL six-incidence candidates and independently reconstruct per-ORIGINAL-Q class cost and GF5 51-column floor. Dedicated exact [#38511725512](https://github.com/definitely-stable/Mathlab/actions/runs/38511725512) **SUCCESS across 3 jobs** (independent tests and both S68/S72 matrix).

| Genuine ORIGINAL W32 4-factor block | Per-Q independent S min | Independent 3+3 clusters | Shared-original-pair separator | Full coherent 4-factor S min | New separator lift |
|---|---:|---:|---:|---:|---:|
| S68 points | 0 | 65 | **67** | 68 | +2 |
| S68 lines | 0 | 63 | **66** | 68 | +3 |
| S72 points | 0 | 68 | **68** | 72 | +0 |
| S72 lines | 0 | 62 | **63** | 68 | +1 |

| Original scheme/type | 3+3 selected GF5 numerator | Shared-separator GF5 numerator | Joint four-factor exact GF5 numerator |
|---|---:|---:|---:|
| S68 points | 2,975,710 | **3,066,910** | 3,112,510 |
| S68 lines | 2,877,180 | **3,021,310** | 3,112,510 |
| S72 points | 3,101,210 | **3,101,210** | 3,283,610 |
| S72 lines | 2,828,200 | **2,876,080** | 3,104,080 |

Distinct actual ORIGINAL Q positive in at least one of the 24 completions: S68 points **551**, S68 lines **544**, S72 points **559**, S72 lines **555**. **All four independent-Q min=0**, yet common complete global min >=68 in each. The two-triad separator recovers >=62 positives even without forcing both outer factors to a single global assignment. These are SOURCE- and STARTING-MAP-CONDITIONAL numerical theorems on four selected exact critical fibers, NOT an all-W32 or all-h universal result.

**Independent physical pseudomarginal adversarial controls:** D6-X s=4 star-pseudo violates global lifted edge column capacity by **-5/182**; D6-Y selected lifted-pseudo predicts **1020** adjacent occupied original source pairs but sharp globally realizable image has at most **963**, exact gap **57**. These are pre-existing X/Y theorems and DO NOT supply GF5 positivity by themselves.

**Final HEAD CI at note time:** [Dedicated #38511725512](https://github.com/definitely-stable/Mathlab/actions/runs/38511725512) SUCCESS, [INDEX #38511725446](https://github.com/definitely-stable/Mathlab/actions/runs/38511725446) SUCCESS, [Proof Audit #38511725415](https://github.com/definitely-stable/Mathlab/actions/runs/38511725415) SUCCESS; [full Research #38511725480](https://github.com/definitely-stable/Mathlab/actions/runs/38511725480) not yet confirmed complete. Mathematical peer review OPEN.

**Status OPEN_WITH_FORMAL_BLOCKER**: no universal all-h positive GF5 obstruction or infinite Branch B, no full GF5 R3 or ASET exponent. Next D6-AA4-H should combine original complete source-cluster consistency, true image capacity cuts, and JPKC-012 ORIGINAL incidence-profile tensor in a globally sound all-h LP/dual and test its feasibility against X/Y and JPKC-011 non-P3 original Q.

---

## Comment 173 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6161064975
- GitHub comment ID: 6161064975

### HYP-105 / #230 — JPKC-014: source-factor choice and NO double count by ORIGINAL incidence

Implemented [research-only Draft PR #447](https://github.com/definitely-stable/Mathlab/pull/447) strictly stacked on JPKC-013 [#445](https://github.com/definitely-stable/Mathlab/pull/445), pinned parent HEAD `c0d6401ad786b3da05c666b3b50c60fb82c24339`. New HEAD `c5aaf4ca67a5306017d1d29182476d5f306fd895`. `main` unchanged, no merges, Root A/B OPEN.

**J47 — conditional all-h original factor image-star.** In genuine W(3,s), freeze left source f, fixed original right labels outside a moving right-source-line block B, and exhaust all legal injective images for B. If for an original line r in B every possible image e activates a true positive ORIGINAL right-source profile m with `supp(m)∩B={r}`, that profile's exact original-Q count is invariant under other movable source line images by J44 locality. Thus r guarantees the min_e of its image-wise ORIGINAL Q counts on each globally legal map.

**J48 — conditional all-h original-incidence NO double-count charge.** Different r anchors' chosen Q families are disjoint because a fixed ORIGINAL six-incidence Q cannot have `supp_right(Q)∩B={r}` and `={r'}` simultaneously for r!=r'. Consequently `S_s(f,g)>=Σ_{r in stars}q_r`, WITHOUT /6 incidence multiplicity loss. For unrestricted overlapping anchor witnesses, the actual max positive Q anchor multiplicity d<=6 yields `S>=ceil(sum_r |A_r|/d)`. The code validates six unique ORIGINAL incidence IDs, true source support, exact multiplicity and fail-closed negatives.

**J49 — COMPLETE 24/24 global W32 original-Q-set inspection and independent GF5 seven-census:** each state uses ONE globally injected right map for ALL original incidence Q. An independently enumerated full seven-class GF5 ORIGINAL Q six-ID dictionary matches exact JPKC-012 source tensor contributions profile by profile. Complete source-image one-line cylinders, 6 legal permutations per fixed image, are tested for EVERY possible image. Original-Q sets selected for different anchors are checked disjoint by true ORIGINAL line source support.

| Complete pinned four-original-line fiber | Four original star lines | Min distinct true Q by anchor over all images | Guaranteed distinct ORIGINAL Q lower bound for ALL 24 legal maps | Min actual selected distinct ORIGINAL Q | Full seven-S min |
|---|---|---|---:|---:|---:|
| S68 | `0,1,2,3` | `2,2,2,1` | **7** | **8** | 68 |
| S72 | `1,7,9,12` | `2,2,2,1` | **7** | **8** | 68 |

This improves the JPKC-013 one-line 24-state Boolean `S>=1` finite certificate to a non-overcounted **S>=7** certificate from four original lines. The bound is mathematically valid conditional on the original source-star existence hypotheses for any h, but star existence is verified ONLY in these two finite W32 fibers. This is **NOT** an all-h Ω(s^6) bound, an infinite correlated low-S counterfamily, or an ASET exponent.

[Initial specialized GitHub-hosted 3/3 SUCCESS #38512533047](https://github.com/definitely-stable/Mathlab/actions/runs/38512533047); after pinning numerical regression expectations, exact final HEAD [dedicated #38512722772](https://github.com/definitely-stable/Mathlab/actions/runs/38512722772), [INDEX #38512722754](https://github.com/definitely-stable/Mathlab/actions/runs/38512722754), [Proof Audit #38512722817](https://github.com/definitely-stable/Mathlab/actions/runs/38512722817), [Research #38512722778](https://github.com/definitely-stable/Mathlab/actions/runs/38512722778) require final conclusion verification. Separate mathematical proof review OPEN.

**Scaling blocker:** ORIGINAL right lines V=(s+1)(s²+1)=Θ(s³). Uniform O(1) Q per star for Θ(s³) lines only yields Ω(s³), not Ω(s⁶). To close Root A via this strategy requires the aggregate certified star charge `Σ_r q_r=Ω(s⁶)` under ALL globally injective f,g, or a different family of incidence-disjoint high-capacity source configurations.

---

## Comment 174 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6161118753
- GitHub comment ID: 6161118753

### JPKC-014 final mathematical strengthening: J50 true ORIGINAL factor-image injective matching

The initial J47–J49 complete original-sixset source-block stars on S68/S72 pinned 24-state globally injected right-fibers yielded 4 independently positive ORIGINAL source line anchors with rowwise minimum true-Q charges 2+2+2+1=7, with no overcount of any ORIGINAL incidence Q. On every actual coherent assignment the **minimum selected ORIGINAL Q count is 8**, not 7.

**J50 all-h CONDITIONAL source-factor assignment theorem** now identifies the reason. Each original source line anchor r has a *genuinely proven* image-choice integer table `c_(r,e)`, with true positive ORIGINAL Q sets whose right-source support intersects moving block B **only at r**. Distinct anchors' Q sets are disjoint for a fixed true original global right injection g. Global source injection forbids repeating physical images, hence

`S_s(f,g) ≥ Σ_r c_(r,g(r)) ≥ min_(injective σ:R→E) Σ_r c_(r,σ(r)) ≥ Σ_r min_e c_(r,e)`.

The middle optimization is solved exactly by a NEW finite bitmask dynamic-programming bipartite assignment oracle, **independent of the complete original-GF5 seven_census**. For both pinned real W32 four-original-line fibers, the optimum is **8**, rowwise independent minimum **7**, strict injection gain **+1**; all 24 authentic global states previously independently verified had min selected true original Q exactly 8 and full S minimum 68. Independent tiny synthetic brute-force permutation tests independently falsify broken matching solvers. Costs are true original six-ID positive Q, not physical proper P3 / Hall demands / independent per-Q labels.

Code and mathematical note in [Draft PR #447](https://github.com/definitely-stable/Mathlab/pull/447), exact new HEAD `450e0d051216e42bf1af2bdebafdb0fddfedc4b6`, stacked strictly on prior JPKC-013 [#445](https://github.com/definitely-stable/Mathlab/pull/445). [Dedicated CI #38513077598](https://github.com/definitely-stable/Mathlab/actions/runs/38513077598), [INDEX #38513077666](https://github.com/definitely-stable/Mathlab/actions/runs/38513077666), [Proof Audit #38513077617](https://github.com/definitely-stable/Mathlab/actions/runs/38513077617), [Research #38513077544](https://github.com/definitely-stable/Mathlab/actions/runs/38513077544) await all-final-head status. No changes to main, no merges. Root A/B OPEN. The crucial scaling problem is now whether genuine source capacity and injection conflicts enforce `Σ_r c_(r,g(r))=Ω(s^6)` for arbitrary globally injected f,g — not demonstrated by the finite W32 4×4 data.

---

## Comment 175 of 175 — MrFr3di

- Permanent link: https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6161153367
- GitHub comment ID: 6161153367

### D6-AA4-H — exact signed source-capacity dual and ORIGINAL W32 profile partition (2026-10-14)

Created strictly stacked [Draft PR #448](https://github.com/definitely-stable/Mathlab/pull/448) on previous green D6-AA4-G [#446](https://github.com/definitely-stable/Mathlab/pull/446); exact final HEAD `006839457641e7fbb52dbad43ff01e991cab1ce2`; changes ONLY four new research/CI/doc files in branch `research/hyp105-issue230-d6aa4h-capacity-source-dual`. No main writes, no merge or issue closure.

**H1 all-h rigorously valid ordinary Lagrangian weak dual (conditional on full candidate coverage):** If every actual ORIGINAL globally typed injective map is represented in candidate relaxation U with exact original six-incidence GF5 cost C and all valid physical-image/source inequality slacks g_j<=0, then for any nonnegative rational lambda,
`min_{u in U}(C_u+sum lambda_j*g_j(u)) <= min_{true full maps} S_s(f,g)`.
The implemented exact rational one-cut verifier enumerates all affine intersections, includes signed violations, and FAILS CLOSED if no nonpositive feasible candidate cut row. A finite U missing actual maps is NOT a valid global certificate. No new all-h positive lower bound.

**H2 exact pre-existing D6-X/Y capacity pseudo falsifiers, explicitly SYNTHETIC s=4 costs:** physical image Amax=963, false two-site pseudo=1020, valid violation +57 -> optimal exact synthetic dual price **1/57**; D6-X projective-star lifted physical-column slack **-5/182**, synthetic dual price **182/5**. Both upgrade an explicitly artificial cost-0 vs feasible-cost-1 two-row toy to toy lower 1, **NOT** a claimed original GF5 W(3,4) lower bound or full SA/SOS statement.

**H3 rigorous W32 scalar-capacity NO-GO:** for TRUE W(3,2), V=K=15, a=6, m=0 and every globally typed injective image is entire physical K6; `A_P=A_L=Amax=6*C(5,2)=60` ALWAYS. Thus the D6-Y *scalar physical-image adjacency upper* has IDENTICALLY zero slack and cannot repair a strict finite original-source profile coherence gap alone; this does not preclude mixed, source-resolved physical-coordinate cuts.

**H4 NEW true ORIGINAL W32 exact source-profile proof:** For two actual first all-four-LINE critical source transversals (S68 original typed IDs `[15,16,23,28]`, S72 `[15,16,22,24]`), enumerate ALL 24 complete global K6 right-line assignments, independently classify each of the 62,370 accepted candidates on the actual original 45-incidence host, preserve all original source IDs including six ORIGINAL line multiset multiplicities and seven GF5 motifs. Reconstruct per-original-Q cost and exact certified 51-column numerator on EVERY map. Results:

| True ORIGINAL line profile fiber | S68 | S72 |
|---|---:|---:|
| Actual Q positive in any state | 544 | 555 |
| Active named six-line source profiles | 307 | 294 |
| Sum independent per-source-profile S minima | **0** | **0** |
| Exact coherent full globally injected S min | **68** | **68** |
| Sum independent selected GF5 floor numerator minima | **0** | **0** |
| Exact coherent full GF5 numerator minimum | **3,112,510** | **3,104,080** |
| Inclusion-maximal state profile masks | **34** | **34** |
| EXACT MINIMUM number of source profiles covering all 24 true maps | **4** | **4** |

**Exact four-by-six partition witness:** BOTH true scheme covers use pairwise-disjoint masks `63,4032,258048,16515072`, each with exactly SIX occupied state bits, bitwise OR `2^24-1`. All 1-, 2- and 3-profile covers are excluded by complete exhaustive combination search over 34 inclusion-maximal masks, whose dominance reduction preserves unit-cardinality optimum. Independent all-24-state reconstruction and random brute-cover tests pass. Concrete original source profile IDs for the four masks are included in docs and dedicated final-HEAD CI logs. The cover proves S>=1 ONLY in the chosen frozen-outside 24-state fibers; the separately obtained exact min S=68 comes from full true ORIGINAL census, not cover cardinality.

Final-HEAD [dedicated #38513391490](https://github.com/definitely-stable/Mathlab/actions/runs/38513391490) **SUCCESS** (independent rational tests, full ORIGINAL S68 matrix, full ORIGINAL S72 matrix); [INDEX #38513391481](https://github.com/definitely-stable/Mathlab/actions/runs/38513391481) SUCCESS. [Proof Audit #38513391497](https://github.com/definitely-stable/Mathlab/actions/runs/38513391497) and [Research #38513391484](https://github.com/definitely-stable/Mathlab/actions/runs/38513391484) not yet confirmed SUCCESS as of comment. Independent mathematical peer review still OPEN.

**Scientific disposition: OPEN_WITH_FORMAL_BLOCKER.** Still NO `forall h,f,g S_s>=c*s^6`, NO infinite Branch B, full GF5 R3 or ASET exponent. Suggested next D6-AA4-I: develop MIXED original-source/physical-edge occupancy constraints (not only scalar image adjacency), integrate JPKC-011 non-proper-P3 Q and JPKC-012 exact six-incidence line tensor, and falsify candidate global LPs against D6-X/Y before any positive universal claim.

---

