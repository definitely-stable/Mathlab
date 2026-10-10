# HYP-105 B3.2-E1-C12 — exact physical orbit quotient of ONE common right-factor bijection

Date: 2026-10-10. Parent issue #230; C12 stacked directly after C11 PR #288, with earlier C1–C10 dependency sequence still OPEN. Independent C7 conditional selector PR #280 is a companion, not an ancestor.

**TYPE: ALL-h EXACT RESTRICTED GROUP-QUOTIENT THEOREM / FINITE K6 PHYSICAL AUTOMORPHISM ORACLE / REAL W32 SAME-MAP SEVEN-CLASS VERIFICATION.** No positive uniform all-f,g lower, GF5 R3 upper, or ASET exponent.

## 1. A rigorous model-preserving symmetry, with ALL quantifiers

Fix any s=2^h (h>=1), its V original GQ right factor lines, any legal injective original GQ-left map f to physical K_a pair labels, and any physically occupied set F⊆E(K_a) of exactly V edges, a minimal or larger physical alphabet. Let T(F) be the set of six distinct physically occupied edges that form a simple two-regular graph on exactly six physical coordinate vertices. Its indicator t_F is expressed on the V right occupied physical-edge labels.

Let H=Aut(K_a,F) be the subgroup of permutations of the a PHYSICAL coordinate vertices sending F exactly to F. Each h∈H induces a permutation alpha_h of the V occupied edge-label indices. Let H_edge be the image group of these induced label actions; its size may be smaller than |H| when F has isolated physical coordinates, hence use the DISTINCT induced maps and never divide by a nonfaithful coordinate action count.

The genuine B-left/A-right source m_f(R) is a nonnegative weight on sixsets R of ORIGINAL GQ right line IDs; no original right-line incidence relation is changed by h. For every one legal FULL original-to-occupied-right bijection g, define

    U_f,F(g) = SUM_R m_f(R) t_F(g(R)).

Then, for EVERY h∈H, not merely on average,

    U_f,F(alpha_h ∘ g) = U_f,F(g).

Proof: h sends every physical occupied simple six-edge 2-factor onto another such 2-factor, with no edge reused, so t_F(alpha_h(Q))=t_F(Q) for EVERY physical occupied Q. Apply this equality to Q=g(R) term-by-term, preserving all original sixset multiplicities.

The same argument, applied to each original six-incidence set and the physical right-degree-profile/cycle graph classifier, preserves ALL SEVEN original-six-incidence motif counts simultaneously, for the SAME legal left f and right g. A full GF5 matrix under an induced physical coordinate row permutation has the same rank-dependent risk, but the executable C12 proof gate checks only the exact seven-count vector and its already accepted classwise GF5 necessary-floor numerator, NOT the exact full 51-column GF5 risk. No independent reoptimization by motif is permitted.

## 2. Exact quotient — full maps AND pinned prefixes

Because each g is surjective from all V original right factors onto all V physically occupied edge labels, H_edge acts FREELY on the full original-to-physical map set by left composition: if alpha∘g=g then alpha fixes every occupied edge, hence is the identity element of H_edge. Thus every full-map orbit has exactly |H_edge| maps, and

    #full-right-map orbits = V! / |H_edge|,
    min_(ALL actual full g) U_f,F(g) =
        min_(ONE representative per H_edge-orbit) U_f,F(g).

The same holds for any seven-family same-map count or other physically coordinate-invariant statistic. This is EXACT: no relaxation and no discarded non-equivalent original GQ right map.

Fix a subset D of k named ORIGINAL right lines, whose ordering is recorded, and let p:D→F be any injective physical images of those same original pins. Coordinate actions map p to alpha∘p without touching D or f. The entire collection of (V-k)! common full completions of p corresponds BIJECTIVELY to that of alpha∘p under g→alpha∘g. Thus their COMPLETE distribution of U, all exact conditional moments of every order (including C11 mean/variance), minima, and the entire seven-motif vector distribution are identical. This is a stronger correspondence than equality of first and second moments alone.

The ordered (V)_k injective physical pin-image assignments are partitioned into H_edge-orbits, of individual size |H_edge|/|Stab(p)|. Exhaustively checking ONE canonical representative of every physical prefix orbit is sufficient to establish any uniform-in-p statement about these same-map statistics. A bound true for one arbitrary prefix is NOT a bound for all prefixes unless it holds for every representative.

The finite reference enumerates Aut(F) by coordinate permutations for a<=9 only when a! fits an explicit hard budget, deduplicates its induced occupied-label action, partitions exactly ALL (V)_k assignments only when they fit max_prefixes, and verifies every orbit/stabilizer cardinality plus the complete orbit cardinality sum. Work budgets raise ValueError (never certify a partial orbit list).

## 3. Sharp full K6 finite example and honest complexity

When the real W(3,2) right image F is the COMPLETE K6 physical edge set, V=15 and H_edge≅S6 has order exactly 720; its action on all 15 pair-edge labels is faithful. For ANY fixed ordered original right pins D, the exact orbit partition has:

| Original pinned lines k | Physical injections (15)_k | Canonical physical orbits |
| ---: | ---: | ---: |
| 0 | 1 | 1 |
| 1 | 15 | 1 |
| 2 | 210 | 2 |
| 3 | 2730 | 9 |

The two-pin classes correspond exactly to physical adjacency vs disjointness of the two assigned pair edges. Three-pin ordered classes split into nine true edge-ordered physical graph-pattern orbits; using only the five *UNORDERED* three-edge graph types from C0 would incorrectly merge distinct named original pin assignments, hence is NOT allowed. Their orbit sizes and stabilizers are checked exactly.

The entire full-map space would quotient from 15! = 1,307,674,368,000 to 15!/720 = 1,816,214,400 equivalence classes. This is a ~720× exact search reduction BUT STILL computationally too large for the current CI budget; C12 does NOT claim enumeration of all these classes or the unrestricted full B/A minimum.

For incomplete images, the group is Aut(F), NOT unconditional S_a. The independent finite K6 tests delete two physically adjacent missing pair edges and two physically disjoint missing pair edges: the exact induced group sizes are 12 and 16 respectively; surviving target 2factor counts are 21 and 28. Every listed automorphism is checked to preserve the ACTUAL occupied target. Applying full S6 to an incomplete F is explicitly forbidden.

## 4. A distinct all-a one-pin no-information theorem for full F only

For the COMPLETE physical edge alphabet F=E(K_a) with V=C(a,2), the physical 2factor hypergraph T_a is edge-transitive, hence a true 1-design. Put T=|T_a|=70*C(a,6), and d=6T/V. Fix any ORIGINAL source right line u and any physical pair-edge e, leaving all other original right lines uniformly permuted. The conditional source sixsets containing u hit a physical target with probability

    d/C(V-1,5) = T/C(V,6),

whereas source sixsets omitting u hit with probability

    (T-d)/C(V-1,6) = T/C(V,6).

Therefore for EVERY nonnegative weighted ORIGINAL source (not only GQ f), any original u and any assigned physical e,

    E[U | g(u)=e] = (SUM_R m_f(R))*T/C(V,6) = E[U].

This is a sharp **FIRST MOMENT BLINDNESS** for one pinned original line when F is the full physical pair alphabet. It does NOT imply zero overlap, constant actual U, equality of second moments, or the same result for incomplete F. Most higher-order W(3,s) physical alphabets have missing edges and are NOT covered by the full-F corollary.

## 5. Real original W32 falsifiers and whole seven-family guard

C12 reconstructs the exact real original W(3,2) B/A source and full K6 target, physical S6 edge action, and C11's original reverse-line map. It verifies:
- Exact physical prefix orbit counts 1/1/2/9 for k=0/1/2/3 and all720 coordinate actions preserving the entire target.
- C11 original 11-pin conditional common-right FIRST/SECOND moments and variance are identical under an explicit nonidentity physical coordinate automorphism applied to EVERY pinned right image.
- The same original left f with physically transformed full right map has identical full seven-class original six-incidence motif count VECTOR and GF5 classwise necessary-floor numerator.
- C11 all-24 coupled-four-original-line result remains exact: historical B/A=77, 24-map restricted min=56, common conditional mean=133/2 and variance=28, no independent anchor maps.
- The same-map seven-family comparison from accepted exact-head C11 dedicated CI: historical S_seven=169 and B/A minimizer S_seven=141, change=-28. The accepted GF5 necessary-floor numerators are 7,627,209 and 6,400,556, respectively; those are LOWER certificates, NOT full R3 values.

Each of these finite statements is regression-checked on GitHub-hosted runners. A valid reduction of S_seven from 169→141 does not prove that its all-h lower floor fails, nor that the full GF5 R3 has improved by the same fraction.

## 6. Acceptance and next scientific decision

Dedicated hyp105-c12-contract and FULL Research CI must both report SUCCESS on the exact PR HEAD; predecessor C1–C11 should be reviewed and merged in dependency order, and post-merge main Research CI verified. No PR should be merged based on queued or previously successful checks of a different SHA.

**Research decision for C13:** use exact group quotient to reduce the family of candidate ORIGINAL-to-PHYSICAL right maps and construct a *globally valid* lower for all non-equivalent f,F,g — not merely all p for fixed f,F — via source GQ-conditioned pair/quadruple capacity, physical 2factor stabilizers and jointly consistent four-remaining-line completions. The group theorem is mathematically exact but symmetry alone cannot supply positivity. If the worst-case conditional invariant stays zero on a single representative orbit, that valid obstruction must be reported without promoting it to a real zero-overlap map. Parent #230 remains OPEN_WITH_FORMAL_BLOCKER.
