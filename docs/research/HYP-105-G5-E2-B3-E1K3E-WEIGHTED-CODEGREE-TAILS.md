# HYP-105 B3.2-E1-K3-E — C4-weighted mixed codegree regularity and original-source star-tail certificate

Date: 2026-10-12. Root issue #230. Scientific parent PR #369 at exact HEAD 69eb52a445f12a6c40fc278afbbf97d14631cb1e; descendants of PRs #366–368. No main modifications.

**STATUS: RESTRICTED_THEOREM_C_EXACT_WEIGHTED_LAYERS / SOURCE_STAR_DEGREE_UPPER / OPEN_WITH_FORMAL_BLOCKER_SHARED_GQ_TAIL_PACKING.** No uniform Omega(s^6) for seven-family S or D6, and no full R3/ASET exponent is inferred.

## 1. Why K3-D's universal bound is weak

K3-D proved for any legal globally coherent original f,g on W(3,s), s=2^h, the maximum mixed Kikuchi codegree c(u,v) is bounded by the all-h girth-eight cap

    Cmax = min(C4-free(r), Moore8(r),r*(s+1)), r=a-2.

Also the exact identity M2_all=sum_{u<v} choose(c(u,v),2)=2*C4(Ghat) and the valid inequality

    Bmixed = 3*sum_mixed choose(c(u,v),3)
           <= (Cmax-2)*M2mixed.

This uniformly charges the largest permissible codegree to EACH unit of C4 weight. At W(3,4) random, Cmax=35, while the observed largest codegree is only 4. Tightening the global maximum again is unlikely to solve the joint-concentration problem.

## 2. Exact all-h C4-weighted identity, including empty mass

For every mixed unordered pair {u,v} (different first and second physical coordinates), let c=c(u,v), w(c)=choose(c,2). Define

    M2mixed=sum_mixed w(c);
    Bmixed=sum_mixed (c-2)w(c).

The second is EXACT, since (c-2)*choose(c,2)=3*choose(c,3) for all c>=0 with both sides zero for c<2. If M2mixed>0, define

    kappa_mixed = sum_mixed c*w(c)/M2mixed
                = 2 + Bmixed/M2mixed.

If M2mixed=0, no kappa is defined and Bmixed=0. One must not report a ratio 0/0 as a numerical experimental result.

For every integer k>=3 let

    Q_k = sum_mixed w(c(u,v))*1[c(u,v)>=k].

By finite layer-cake counting,

    Bmixed = sum_{k=3}^{Cmax} Q_k.                  (LAYER)

This exactly locates excess book mass in the high-codegree tails that are ALSO heavy under the four-cycle weighting. Merely knowing a small UNWEIGHTED high-codegree fraction does not control Bmixed.

The histograms in the executable report record: number of physical mixed vertex pairs with each codegree, four-cycle diagonal weight at each codegree, and Q_k by threshold. Each original physical f and g is used globally and coherently.

## 3. NEW original-source star upper and formal proof target

Let n(u)=deg_Ghat(u) be reconstructed from the ORIGINAL GQ star-incidence tensor, independently of Kikuchi adjacency (K3-A/B). For each mixed pair,

    c(u,v) <= min(n(u),n(v),Cmax) =: cap_uv.

Consequently

    Bmixed <= Ustar :=
       sum_mixed max(cap_uv-2,0)*choose(c(u,v),2)
       <= (Cmax-2)*M2mixed.

Unlike the old bound, Ustar charges the high C4 weight according to each endpoint's ORIGINAL star degree rather than the global maximum alone. No probabilistic independence, symmetric host labelling, or unproved physical star regularity is assumed.

Define, for k>=3,

    Q_k^star = sum_mixed w(c(u,v))*1[cap_uv>=k].

Since c<=cap_uv, Q_k<=Q_k^star, and the new all-h exact/upper certificate is

    Bmixed = sum_{k>=3}Q_k
           <= sum_{k>=3}Q_k^star = Ustar.        (STAR-TAIL)

This suggests a mathematically meaningful K3-F gate: establish via ORIGINAL W(3,s) geometry a SHARED-STAR tail packing bound for sum_k Q_k^star or directly Q_k, simultaneously for every legal f,g. Note that Ustar still depends on each actual pair's w(c). Bounding it for all maps is NOT proved here.

For a threshold t with 3<=t<=Cmax, the exact tail formula gives

    Bmixed <= (t-2)*M2mixed + (Cmax-t)*Q_{t+1}.

This follows by charging the first (t-2) possible layers globally and bounding the remaining (Cmax-t) layers by their largest tail Q_{t+1}. It is a deterministic conditional estimate, not a uniform nontrivial bound until Q_{t+1} is controlled.

A negative-result branch must be retained: K_{2,t} books show concentration can avoid all C6 in arbitrary graphs, so a purported all-graph implication from small unweighted tails to Omega(s^6) is false. Any useful hypothesis must retain the original W(3,s) shared-source coupling.

## 4. Independence and evaluation scope

Reference: research/hyp105_g5e2b3e1k3e_weighted_codegrees.py.
Independent tests: research/test_hyp105_g5e2b3e1k3e_weighted_codegrees.py.

The reference derives every c from Ghat common neighborhoods, verifies n(u) against the independent ORIGINAL source star tensor, and checks the book cubic sum using the K3-C analytic formula. It checks M2_all/2 against an independently enumerated C4 edge-set collection. The tests additionally enumerate all C4s by a standalone oriented walk oracle, recover every MIXED opposite-pair weight without using the reference codegree histogram, independently enumerate all triples of common neighbors, and reconstruct per-threshold exact and star tails.

Deterministic models include W(3,2) lex, reverse-line, random and W(3,4) lex plus two pinned globally seeded random pairs. Budgets fail closed for pair counts and explicit C4 census. The dedicated path-limited GitHub-hosted Contract plus inherited Research/INDEX are required. No numpy, local-PC computation, or second full CI matrix.

This is an evidence and mathematics tool: no universal o(s^6) tail mass has yet been proved. The intermediate full R3 via GF5 distinct six-column cycles differs from the original #230 Branch A seven-family S floor.

## 5. Next precise gate

A putative K3-F lemma must give a provably uniform source-dependent envelope for the right-hand side of (STAR-TAIL), or an explicit all-h positive-motif conversion when weighted high-codegree tails are large. It must separately charge K3-C's triangle-hooks T and K4, and original-column repetition/proper vs improper six-cycle loss. Otherwise it does not close D6/S or full R3, even if Bmixed happens to be small on each tested finite labeling.

**Acceptance:** exact PR-HEAD dedicated Contract SUCCESS and inherited Research SUCCESS, independent review before merging. Issue #230, #176, #169 stay OPEN. No Branch A/B/ASET decision.
