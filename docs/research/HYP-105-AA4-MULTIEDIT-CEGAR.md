# HYP-105 / #230 — AA4-MULTI: sound bounded multiedit source CEGAR

Scientific Draft stacked strictly on frozen PR #723, exact HEAD bd81ccade8dc7f6306174d3fe8104f22927abc15. No main or parent mutations or merge. Root #230 is OPEN_WITH_FORMAL_BLOCKER.

## 1. The genuine next problem

PR #721 gave exact finite ORIGINAL W(3,4) minimum abstract event covers tau=25 (lex) and tau=26 (reverse-line), versus existing genuinely accepted 27/29-source-change complete zero-to-three GF5 ASETs from PR #719. PR #722 computed exact legal 51-palette necessary domains D_i(F), with 463/479 surviving per-source choices in total and all source domains nonempty; PR #723 computed every binary forbidden source tuple from true physical 2v2 and 3v3 events involving precisely 2 edited IDs. All 300/325 pair relations were nonempty and exact arc consistency deleted ZERO source values. Both constructions remain unresolved at their 25/26-ID minimum covers.

This new slice attempts the MISSING three-to-six editable original ID event sectors with an exact original physical GF5 counterexample-guided finite-domain CSP, while separating proven necessity, verified success, exhaustive UNSAT, and bounded inconclusive outcomes.

## 2. All-N source-hyperclause equivalence theorem

For any original source columns c_i in GF(5)^m, fixed finite legal palettes P_i, candidate changed original ID support T and its frozen complement F, consider every disjoint equal-k source signed event (k=2 or3) between subsets A,B of ORIGINAL source IDs, after assigning each edited i in T a palette p_i. If the event holds in full physical GF5^m, let S=(A union B) intersect T, and define the exact finite-domain nogood

   OR over i in S of (X_i != p_i).

All OTHER source IDs in the witness are frozen in F; they cannot change, so every final collision-free assignment on the SAME T must satisfy this clause. The clause cardinality is at most 2k<=6, and after proven frozen-only/one-edited/binary sectors it is at least 3. It is NEVER a heuristic or an independence assumption.

**Theorem (sound counterexample-guided completeness).** For every finite original source and T, an assignment of legal P_i values produces an original 0-to-3 distinct-subset-sum family if and only if it violates NO physically genuine original 2v2 or 3v3 signed-event nogoods. A solver with sound finite-domain legality and only independently checked event nogoods may exclude candidate assignments without excluding ANY correct final ASET. A candidate returned by the solver becomes a CONSTRUCTIVE finite zero ASET only after a COMPLETE physical 1/2/3-sum audit reports zero collisions. An exhaustive proof of NO candidate for the resulting NECESSARY CSP would imply nonexistence on THAT T. Merely reaching iteration, node or time budgets implies NOTHING about nonexistence. Proof: every signed equal-sum event is exactly a witness and yields one nogood. Conversely if no event exists, all size-2 and size-3 subset sums are source-distinct (a shared member in equal triples reduces to a 2v2 equality, and 2 shared members imply duplicate singleton columns; original supports are unique). Each exclusion fixes all editable values contributing to a real equality; such a combination cannot occur in a valid assignment. QED.

No theorem that a fixed minimum T is satisfiable is assumed. Even a verified s=4 solution says nothing about all dyadic s or root Branch A/B/C.

## 3. Complete real-original physical source oracle and reusable cached F

The GH-hosted C++ oracle reads the SAME complete real 425 original symplectic W34 source flags, fixed global point/line pair-injective f,g, four physical nonzero checksum4 positions per original ID, and all 51 allowed coefficient patterns. Parent #722 51-palette domains and #723 exact true original binary relations are regenerated and independently checked on this precise source branch.

The expensive fixed-only physical 28D GF5 distinct source pair/triple signatures are indexed ONCE in an exact lossless 128-bit base-625 representation. Their cardinalities are C(400,2)=79,800 and C(400,3)=10,586,800 (lex), or C(399,2)=79,401 and C(399,3)=10,507,399 (reverse-line). Duplicate F-only sums fail closed because the minimal cover has already been proven to hit EVERY initial signed event.

For each proposed edited source coefficient assignment, the oracle recomputes EVERY remaining source pair/triple sum containing at least one edited original ID, testing signatures both against F-only signatures and between all dynamic source subsets. This covers ALL C(425,2)=90,100 original pairs and ALL C(425,3)=12,704,100 original triples in combination with immutable cached F. It emits FULL signed source-disjoint 2v2/3v3 physical 28D equality witnesses (not class projections); equal triples with one common ORIGINAL ID reduce to true source-distinct 2v2, with two common IDs to singleton equality, ruled out by immutable original four-position supports. Partial scanning reports only its verified witnesses and never a complete zero claim.

A separate Python verifier reconstructs each reported witness directly against ALL 28 original physical GF5 coordinates. Only if every report is a genuine equality is its associated hyperclause added. The pure-Python finite-domain source solver reuses the COMPLETE #723 binary compatibility relations, checks all learned hyperclauses during deterministic bounded backtracking, and does NOT report UNSAT if any node-budget limit is reached.

If the native cached physical oracle exhaustively reports ZERO conflicting signatures for a candidate, a SEPARATE established physical external-radix Python referee must independently rebuild the full actual 425-source GF5 columns and reprocess ALL 12,704,100 original triples and ALL 90,100 pairs with exact original source IDs. Only a second complete zero result may set CONSTRUCTIVE_FULL_ORIGINAL_GF5_ZERO_ASET_VERIFIED.

## 4. Genuine W32 independent falsifier and finite acceptance

The host independently reconstructs a real original W(3,2) physical GF5^12 source subproblem from 45 genuine original symplectic incidence flags. It chooses an independently verified collision-free frozen eight-source subset and four actual editable original source IDs, then enumerates ALL k=2/3 physical signed source equations for the 12 active IDs using a DIFFERENT direct Python implementation. It compares the EXACT signed event sets, not just counts, with the native full pair/triple signature oracle over multiple coefficient assignments, independently checking each 12D physical signed witness. It also verifies a real six-ID W34 original source event becomes a sound learned nogood, finite-domain exhaustive backtracking can prove tiny source UNSAT, bounded search never claims UNSAT, and malformed original source coefficients fail closed.

The experimental hosted run is intentionally bounded to at most 64 GF5 full physical candidate rounds per map and 100,000 pure-source constraint search nodes per candidate. Those computational limits are NOT interpreted as theorems. Any partial attempt must preserve the exact full physical source witness clauses and its outcome as inspectable GitHub Actions artifacts. The report must name the source map, exact frozen 25/26 original IDs, every chosen palette, all independent true source signed event witnesses, learned clauses, node counts and VERIFIED/PARTIAL/BOUNDED status.

## 5. Scientific stop and next gate

No negative search can rule out other 25/26-source minimum abstract covers unless they are ALSO proved impossible. A conditional finite W34 success would only strengthen the constructive minimum-change endpoint for that PARTICULAR correlated fixed f,g. Neither an s=4 result nor a bounded CEGAR failure can prove the all-h original seven-motif lower bound, an infinite counterexample family, or an asymptotic ASET exponent improvement.

Root HYP-105 #230 remains OPEN_WITH_FORMAL_BLOCKER pending a genuine Branch A/B/C result.
