# HYP-105 / #230 — AA4-ORIGINAL-COVER

Scientific Draft based on PR #720, exact parent HEAD 8bdef0393e197d02b09c56addd55dacff16254d8. This is a finite research step. Root status: OPEN_WITH_FORMAL_BLOCKER.

## Theorem: necessary edit-support transversal without monotonicity

Fix N ORIGINAL physical GF(5) columns. Let E2 and E3 be all unordered equal-sum signed events of two disjoint original 2-subsets and two disjoint original 3-subsets, respectively. Define H as the 4/6-uniform source-ID hypergraph whose edges are unions of IDs in the original signed events.

For **any** final collision-free assignment c' obtained by editing original source IDs T, without requiring any restrictions on the intermediate states:

    |T| >= tau(H) >= nu(H).

Here tau is minimum source-ID cover cardinality and nu is maximum pairwise vertex-disjoint original event packing cardinality.

Proof: if an original event contains no edited source ID, all its columns remain unchanged and its equality survives in the final assignment. Thus every initial event must be hit. Vertex-disjoint edges require distinct chosen source IDs. This is an all-N necessary condition, not a palette construction theorem. It strengthens PR #720's clean-step deletion argument because it does not require no-new-event monotonicity.

## Actual W(3,4) research procedure

The parent PR #719 establishes genuine finite W34 source erasure traces (lex: 27 changes, initial R2=1 and R3=54; reverse-line: 29 changes, initial R2=0 and R3=61). Those counts are achieved edit counts, not minimality proofs.

Our new independent hosted referee reconstructs the actual 425 ORIGINAL symplectic source columns in GF(5)^28 and enumerates ALL 12,704,100 original triple signatures using the exact external radix oracle from PR #713, recovering EVERY true 3-vs-3 signed event. Separately it enumerates the exact original two-subset signatures and every 2-vs-2 event. Each original event equation is verified on all physical GF5 coordinates. Only true distinct ORIGINAL flag IDs are admitted.

The source-ID solver exports an explicit disjoint-event packing (certified lower bound), a concrete source cover (certified upper bound), and attempts an exact minimum cover. Every uncovered event branches on every one of its original source IDs; disjoint-event packings and max degrees provide safe lower pruning. If the node limit is reached, the result is BOUNDED with an honest interval, not an invented exact optimum.

A separate small original-event oracle checks the solver against exhaustive enumeration of all source-ID subsets over mixed 4/6-edge fixtures. The full actual W34 results are produced only by the GitHub-hosted two-scheme matrix and saved in artifacts.

## Limitations

An abstract minimum cover does not guarantee that any legal 51-pattern GF5 clean-source recoloring schedule exists. A finite s=4 cover cannot prove the h-uniform issue #230 Branch A/B/C, a new asymptotic ASET exponent, or a universal palette availability theorem.

Next step after numerical certificates: investigate feasibility of 51-palette schedules against the actual initial conflict hypergraphs and search for non-saturation bounds valid for all dyadic h and correlated original f,g.


## 3. Stronger all-N exact dominance theorem for abstract covers

For any original event hypergraph H, let I(v) be the set of current original signed-event hyperedges containing a source ID v. If I(v) is contained in I(u), then every cover using v may replace v with u without increasing its size. If the incidence sets are equal, retain the least source ID as canonical representative. By applying this containment reduction simultaneously and following the strict-inclusion order, one obtains an equivalent minimum-COVER problem on undominated source IDs. For every removed ID the implementation independently retains a superset-incidence witness.

Proof: replacing v by u hits every edge previously hit by v, because I(v) subset I(u). It may hit additional edges. Repeated replacement cannot increase cover size; in a finite containment partially ordered set every chain ends in a maximal representative. Equal-incidence ties are settled deterministically. The optimum transversal tau is unchanged. QED.

**Scope restriction:** this is exact for the ABSTRACT initial original source-ID COVER. A dominating u need not have any admissible GF5 recoloring, and this lemma does not preserve the existence of a particular 51-palette clean schedule or an asymptotic construction.

## 4. GitHub-hosted FULL original W34 result and exact combinatorial proof bounds

The first hosted exhaustive complete physical source census #41856319439 reconstructed all genuine source events from 12,704,100 original GF5^28 triple sums per fixed map, plus the complete original pair audit. After new all-N source-incidence domination, an independent second complete physical census and exact source-cover replay #41858006050 produced the following FINAL mathematically verified abstract results (subsequent permanent saved-certificate exact-HEAD CI still required):

| Genuine ORIGINAL W(3,4) source map | E2 original | E3 original | Active original source IDs | After safe source dominance | Certified vertex-disjoint packing | Exact tau(H) | Previously ACTUAL clean GF5 edits |
|---|---:|---:|---:|---:|---:|---:|---:|
| lex | 1 | 54 | 231 | 74 | 23 | **25** | 27 |
| reverse-line | 0 | 61 | 255 | 80 | 26 | **26** | 29 |

For reverse-line, the minimum tau=26 has an immediate checkable primal-dual certificate: one concrete 26-source hitting set and one family of 26 pairwise source-ID-disjoint original six-flag signed events. Since each packing edge requires its own source and the cover hits ALL 61 original events, the bounds meet exactly, WITHOUT relying on the branch-and-bound solver's claim of optimum.

For lex, the source-ID packing gives tau>=23, the exact incidence-dominated exhaustive source-cover search completely refuted k=23 and k=24, and it produced and independently verified an explicit 25-source cover. Thus tau=25 exactly. The hosted deterministic exhaustive proof visited 1,422 nodes and retained 74 undominated candidate IDs out of the 231 original IDs participating in the true current E2/E3 events. Its result is also checked by a separate permanent source-certificate test with the same exhaustive algorithm and adversarial tiny brute-force controls. This is an exhaustive finite proof, not a polynomial-time all-N bound.

The ACTUAL previously verified lex 27-change and reverse-line 29-change GF5 clean recoloring traces are unchanged. Accordingly, for the minimum number m of ORIGINAL source IDs that need to be recolored to reach a collision-free assignment **with the same fixed W34 f,g maps and same 51 legal checksum4 palette**, the certified bounds are

  25 <= m_lex <= 27, and 26 <= m_reverse-line <= 29.

The upper bounds are CONSTRUCTIVE genuine previously fully rehashed GF5 source assignments. The lower bounds hold for **all** possible (including nonmonotone) source coefficient changes because any final collision-free assignment must cover the initial conflicts. **Neither actual coefficient-edit minimum is proven to equal tau**: a minimum abstract cover need not admit a legal complete GF5 source assignment on precisely those IDs. No claim that a 25/26-change construction exists is made.

The permanent committed full 55/61 signed-event partition evidence and all source cover/packing witnesses are in research/hyp105_w34_original_event_cover_certificates.json. The original external 12-byte full-triple GF5 referee must reproduce those complete event sets on the FINAL PR HEAD and compare to the stored certificate. An independent static full physical 28D signed-equation and 90,100 pair-sum verifier plus a replay of lex k=23/k=24 nonexistence and independent packing checks also run on the final HEAD.

## 5. Scientific frontier after exact tau

For lex the remaining coefficient-realization gap is at most two additional source IDs; for reverse-line at most three. A relevant next step is to test *exact legal 51-palette feasibility* for size-tau original covers rather than treating the abstract cover as a source assignment. For arbitrary dyadic s, the truly unresolved statement is an h-uniform source-local forbidden-palette non-saturation inequality that survives adversarial correlated physical labels and sequential recolorings. These finite tau values do not imply an all-h existence/obstruction or close root Branch A/B/C.
