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
