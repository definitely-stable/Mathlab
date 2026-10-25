# HYP-105 / issue #230 — D6-AA4-L: ORIGINAL source-pair GF5 charge-energy frontier and zero-charge positive D6

**Scientific status: NEW all-h s>=16 constructive ORIGINAL GQ isolated-six-flag count, genuine W(3,8) D6 positive ORIGINAL sixset with ZERO eligible source-pair charges on BOTH sides, plus exact finite source-pair × positive-Q Gram energy and degree quantiles.** Root Branch A/B remains OPEN; NO all-h lower for actual total charge I_P+I_L or the seven-GF5 motif S_s; NO full R3/ASET exponent. Counts of individually realizable isolated source sixsets are **NOT** claimed simultaneously positive under ONE global map.

Stack research-only Draft on completely hosted green [D6-AA4-K #460](https://github.com/definitely-stable/Mathlab/pull/460), pinned base commit `dc4314c89aedcf86eba0d3770777cdee018c16e4`. Never merge or modify main; root #230/#176/#169 OPEN.

## 1. Why a further total-charge theorem is a separate problem

D6-AA4-I proves unconditionally that every true original W(3,s), s=2^h>=4, complete two-type globally injected physical labeling has at least s^5/4 original collinear point-pairs and at least s^5/4 concurrent line-pairs whose physical edges are disjoint. D6-AA4-K proves for every actual accepted seven-GF5 original six-incidence Q that the eligible pair charge on each type is at most 9 (with exact A/B/C physical six-coordinate 9/6/3) and joint charge at most 18. Thus

S_s >= ceil((I_P+I_L)/18).

But neither statement lower-bounds I_P+I_L: a positive original source Q may not contain any eligible pair, and an eligible source pair may have zero positive original Q continuations (the pinned true S72 lines 5/10 already prove this for s=2). This slice determines exactly how serious that decoupling can be on TRUE symplectic GQ, while recording the exact second-order charge energy instead of treating a random-GF5 expectation as a deterministic theorem.

## 2. ALL-h new rigorous isolated ORIGINAL six-flag existence/count for s>=16

Let s=2^h>=16, V=(s+1)(s²+1), source point and line collinearity/concurrency graphs each of degree k=s(s+1), and let I be the set of V(s+1) TRUE ORIGINAL incident point-line flags. Call a six-flag original Q "source-separated" if its SIX original source points are pairwise NONCOLLINEAR and its SIX original source lines are pairwise NONCONCURRENT. These flags are necessarily SIX DISTINCT original incidence IDs, six DISTINCT point factors and six DISTINCT line factors.

**THEOREM (elementary closed-neighborhood greedy bound):** after j already chosen source-separated flags, the new point of a flag must avoid the closed source-collinearity neighborhoods of the j previous points, each of size k+1. Similarly the new line must avoid the j previous closed line-concurrency neighborhoods. At most j(k+1)(s+1) true flags are forbidden by the point end, and at most j(k+1)(s+1) by the line end. By the union bound, the number of legal choices for flag j+1 is at least

M_j = (s+1)[V-2j(k+1)], j=0,1,...,5.

For all s=2^h>=16, V>10(k+1), since V-10(k+1)=s³-9s²-9s-9>0 and is increasing for s>=16. Therefore all M_j>0 and, more strongly, the number of ORDERED six-tuples of source-separated original flags is at least product_{j=0}^5 M_j. Since each unordered six-flag Q has exactly 6! orderings, the number of unordered source-separated true ORIGINAL sixsets is at least ceil(product_j M_j / 6!). This is a **nontrivial genuine ORIGINAL GQ all-h combinatorial theorem**, entirely independent of any physical labels, accepted GF5 motif event, or probabilistic argument.

**Crucial distinction:** there is NOT a theorem that all these source-separated Q are simultaneously GF5-positive for any one f,g. However, for any ONE such Q, both type source factors are distinct, so assigning the SAME six physical pair edges forming a C6 to corresponding ORIGINAL point and line factors and extending both maps independently to full global injections makes the historical original positional seven-GF5 classifier accept Q as D6. These completions generally DIFFER from Q to Q. Such an accepted Q has ZERO collinear/concurrent SOURCE pair charge on BOTH sides because the source factors of Q were chosen independent in the genuine ORIGINAL geometry, even though its six physical C6 edges contain 9 physically DISJOINT pairs per type.

Thus for ALL s=2^h>=16 there EXISTS at least one genuine globally injected complete map containing at least one accepted positive original D6 sixset Q with **c_P(Q)=c_L(Q)=0**. This does NOT imply that the **TOTAL** charge I_P+I_L of that same full map is zero: other true original sixsets can be positive and charged. In particular it is NOT an infinite Branch B construction or refutation of any universal total-charge bound.

## 3. Independent constructive true ORIGINAL W(3,8) witness

The proof counting bound only guarantees source-separated six flags for s>=16; the separate finite W38 experiment searches the genuine fixture(3,"lex") 585-original-point, 585-original-line, 5265 ORIGINAL-incidence host using exact original collinearity and line-concurrency adjacency. A deterministic bounded seeded-greedy search selects SIX source-separated true original flags, independently checks every one of the 15 source-point pairs is noncollinear and every one of the 15 source-line pairs is nonconcurrent.

Assign six C6 physical pair labels (0,1),(1,2),(2,3),(3,4),(4,5),(0,5) in the SAME original incidence order on both typed sides; complete all remaining 579 ORIGINAL point factors and all remaining 579 ORIGINAL line factors with distinct unused pair labels (cross-type reuse allowed). Check full global separate injectivity and exact historical ORIGINAL positional `classify_seven_prechecked`. It MUST be the accepted seven class D6 with selected certified GF5 numerator weight 5643. Although the two physical projections have 9 disjoint source-factor pairs each, ZERO are true source-GQ collinear or concurrent: c_P(Q)=c_L(Q)=0. This is a new TRUE-GF5 original-positive sixset **counterexample to any per-Q lower of source charge**, not to the total S or total I global asymptotic question. No whole W38 GF5 census is run.

## 4. Exact first/second moment of ORIGINAL source-pair-to-positive-Q incidence matrix

Fix ANY true globally injected original full map f,g and all actual GF5-positive accepted ORIGINAL six-incidence sets Q (not independent locally constructed Q, and not physical-proper-P3-filtered). For each source type t=P or L let F_t be the TRUE original-collinear/concurrent and physically disjoint pairs, and define the bipartite 0/1 matrix T_t indexed by e∈F_t and Q positive by

T_t(e,Q)=1 if and only if BOTH original source factors of e appear among the six original incidence IDs of Q.

Let d_t(e)=sum_Q T_t(e,Q), U_t(Q)={e∈F_t:T_t(e,Q)=1}. The exact original pair→Q first moment is

I_t = sum_e d_t(e) = sum_Q |U_t(Q)| <= 9 S_s.

The exact second moment/source-pair Gram identity is

E_t = sum_e d_t(e)^2 = sum_{Q,Q'} |U_t(Q) ∩ U_t(Q')|.

This is a direct identity of T_t T_t^T, independent of GF5 class weights; both Q-major and pair-major independent oracles can check it on complete finite W32 maps. Cauchy yields I_t²<=|F_t| E_t. **Important:** that Cauchy inequality is an UPPER bound on I_t given E_t; knowing only the SOURCE pair count |F_t| or an upper on E_t does NOT create a positive lower bound on I_t. In particular the zero incidence matrix T_t satisfies both while |F_t| can be positive. Do not mistake PSD/moment control for proof of positive original GF5 charge.

A correctly weaker deterministic sufficient theorem (robust to zero-degree pairs) is: if at least η|F_t| true eligible original source pairs have ≥b_s positive original GF5 Q, then

I_t >= η|F_t| b_s, and S_s >= ceil(η |F_t| b_s/9).

For s>=4, proving constants η>0 and b_s>=c s uniformly over all REAL f,g would yield S_s>=η c s^6/36. This positive-fraction/multiplicity hypothesis is NOT established; actual W32 degree quantiles (thresholds 1,2,4,8,16,32) are finite evidence only, never a uniform all-h claim.

## 5. Actual ORIGINAL W32 full-positional-GF5 experimental protocol

For S68 and S72 independently, recover genuine W(3,2) 45 source incidence IDs, AA4-D original size-four transversal numbers 53/119, select first all-POINT source-four transversal and freeze all other source maps. Evaluate all 24 complete globally injected K6 point-block permutations; for EACH complete map, independently run accepted historical `seven_census` on all 62,370 ORIGINAL six-incidence candidates preserving seven GF5 class tags and selected certified numerator.

On each actual positive Q and for each typed source P/L, compute its set U_t(Q) of eligible source-collinear/concurrent physically disjoint factor pairs using ACTUAL six original incidence IDs. Check cap ≤9 for EVERY original Q. Independently compute exact pair degrees by iterating every actual source pair against every positive original Q; compare first moment I_t with AA4-K full class-sensitive source charge using an independently coded pair-major oracle, compute E_t from degrees and from ALL ordered Q,Q' original source-pair intersection counts and require equality. Verify exact Cauchy inequality and the degree thresholds. Recompute full S and exact GF5 numerator, never infer an unobserved all-h charge lower.

Important finite W32 S72: original concurrent source lines (5,10) physically disjoint but appear jointly in ZERO positive original GF5 Q; their degree d_L=0 even though F_L nonempty. This is expected and must not be mistakenly rejected. For both pinned schemes exact **one-Q true W38 witness** is a different geometric family of a positive Q with zero original source pair charge on BOTH sides; it must not be confused with a construction whose entire globally injected W38 labelings have zero positive other Q or total I.

## 6. Acceptance and next mathematically meaningful research

Files: `research/hyp105_issue230_d6aa4l_charge_energy_obstruction.py`, independent tests, this formal note, and dedicated GitHub-hosted 3-job workflow. Require independently checked exact finite W38 D6, all-h s>=16 symbolic proof conditions, full W32 S68/S72 sixset historical GF5 matrices with double and Gram oracles, plus full INDEX, Proof Audit, Research workflows on final SHA. Independent math peer review remains OPEN until completed. Strict Draft, no main writes, merges or issue closure.

**Scientific disposition OPEN_WITH_FORMAL_BLOCKER**: no proof or disproof of all-h I_P+I_L=Omega(s^6), no original seven-GF5 S_s=Omega(s^6), no infinite Branch B, no full R3/ASET power. A huge class of true original candidate six-flags can be made individually accepted D6 with no pair charge, reinforcing that pair-charge need not see every positive GF5 Q.

**Next D6-AA4-M:** instead of assuming a spectral pair force must produce positive GF5 Q, seek a genuine mixed ORIGINAL two-type source-flag + physical-coordinate six-motif EXPANSION theorem giving a uniform fraction of charged true seven-GF5 Q, or a uniform charged-degree distribution result. Its proof must invoke more than the classical source pair spectrum and more than the 9-cap. Try to falsify on true globally injected W(3,4) targeted partial class-matching or on the JPKC-012 positional original tensor and EICE-003 source-midpoint covariance; never promote a pseudo family to full W(3,s) injected real maps.
