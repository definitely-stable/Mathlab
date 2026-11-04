# HYP-105 / #230 — AA4-BINARY: exact two-editable original GF(5) source constraints

Scientific Draft strictly stacked on frozen PR #722, HEAD 10958b04a2bd62f258b95e22f294ea222622a292. No main/ancestor mutations or merge; root #230 remains OPEN_WITH_FORMAL_BLOCKER.

## New all-N pairwise necessity theorem

Fix the N original source columns c_i in GF(5)^m with globally fixed support and legal palettes. Fix the candidate original source-ID edit support T; its complement F is frozen. Let D_i(F) be the exact one-editable-source palette domains from AA4-FROZEN (#722), which exclude ALL signed 2v2/3v3 equalities involving i and only original IDs in F.

For every pair i,j in T, define the exact binary allowed relation R_ij, consisting of ordered legal palettes (p,q) in D_i(F) times D_j(F) that cause NO signed equal-size 2v2 or 3v3 complete-physical-GF5 equality containing EXACTLY the two editable IDs i,j, with all other source IDs drawn from F. Every full 0-to-3 ASET supported on T must satisfy each R_ij.

**Theorem A, all finite N.** Every valid final coefficient assignment supported on T belongs to the finite-domain binary CSP (D_i(F), R_ij). If any R_ij is empty, or if sound arc-consistency propagation empties any source domain, then NO valid final assignment on THIS particular T exists. This applies to arbitrary simultaneous/nonmonotone coefficient changes. No order or palette independence is assumed.

Proof: a forbidden (p,q) has an actual 2k-distinct-original-ID signed physical equality using just i,j and otherwise frozen F sources. Regardless of all other source edits, this equality persists. Thus every possible full assignment must avoid the forbidden pair. Sound arc consistency deletes a value p only when there is no compatible neighbor value in another necessary relation. No full assignment can use such a value; induction over deletions proves the claim. QED.

**Theorem B, complete 0-, 1-, 2-editable-sector exclusion.** If F itself has no original signed 2v2 or 3v3 events, all p_i belong to D_i(F), and all pairwise choices satisfy R_ij, then the final source has NO signed equal-size conflict with at most TWO editable ORIGINAL source IDs. All remaining possible events contain THREE or more IDs from T. The statement does NOT prove the complete source zero-to-three ASET and does NOT imply all-h HYP-105 Branch A/B/C.

Proof: the zero-editable sector is exactly frozen-only; the one-editable sector is excluded by D_i; the two-editable sector is excluded by each R_ij. The original source ID cardinality, not physical point/line coordinate overlap, defines the sectors. QED.

## Four exhaustive binary signed event topologies

For i and j distinct editable original source IDs with actual legal coefficient vectors x=c_i(p) and y=c_j(q), each remaining original flag is frozen in F. Every equal-size signed event involving EXACTLY i,j has one of the following four forms (up to global sign reversal):

1. Genuine 2v2 with both editable on one side: x+y = c_a+c_b, with a,b in F distinct.
2. Genuine 2v2 with editable on opposing sides: x+c_a = y+c_b, with a,b in F distinct.
3. Genuine 3v3 with both editable on one side: x+y+c_a = c_b+c_c+c_d, with a,b,c,d in F all distinct.
4. Genuine 3v3 with editable on opposing sides: x+c_a+c_b = y+c_c+c_d, with a,b,c,d in F all distinct.

The exact C++ implementation indexes ALL source-disjoint frozen 1/2/3-sums in full GF(5)^m using lossless __uint128 base-625/5 packed signatures, not random fingerprints. The distinct full F pair/triple signatures are mandatory and fail closed on a frozen-only internal collision; that property follows from the parent true original hypergraph-cover certificate. The third topology uses exact indexed full F triple sums. For the fourth topology, project every F 2-sum onto the complete coordinates OUTSIDE support(i) UNION support(j); equality of this exact outside projection is NECESSARY for any target difference x-y. Group all F 2-sums by this residue, enumerate ALL ordered source-disjoint pair pairs within each group, and match their exact full-coordinate difference against all legal x-y candidate differences. There are no lost source pairings, no partial triple scans, no graph orbit or sampling. This completes the four classes.

For each forbidden binary tuple, the referee outputs a canonical real source-ID signed event with exact positive and negative sides. The independent Python verifier reconstructs all 425 genuine symplectic W(3,4) 28D GF5 source columns from immutable #719/#721 and #722 complete frozen-core 51-palette witnesses, applies the two replacements, rejects non-source-disjoint events, and verifies every physical GF5 coordinate of every emitted forbidden pair. It also insists every D_i times D_j is partitioned into exactly the explicit allowed tuples and actual signed witness tuples.

## Genuine W34 and independent W32 proof gates

The real experiment separately uses the exact minimum source-ID T of size 25 for lex or 26 for reverse-line, with fixed source F of 400 or 399 original flags. The binary CSP contains C(25,2)=300 or C(26,2)=325 original variable pairs, respectively. Each source pair has at most 51^2 legal pattern combinations; the actual #722 frozen-core domains reduce these products beforehand.

Eight GitHub-hosted W34 shards independently build complete F triple-signature indexes and enumerate every source pair. A distinct genuine W(3,2) physical source test uses a real finite eight-original-flag fixed subset and two editable original flags, all 51x51 candidate pairs, and direct independent Python 12D brute-force enumeration of all four signed topology classes. Invalid original physical GF5 source support fails closed.

An aggregating checker verifies all 300/325 original source pairs and every true forbidden signed GF5^28 witness and then independently computes deterministic AC-3 arc consistency. Every deleted palette is accompanied by an exact no-neighbor-support elimination reason and is revalidated in order. Empty domains give a proven UNSAT of this particular T. Nonempty stabilized domains are only a necessary constraint reduction, **not an assignment**.

## Scientific acceptance and next gate

- Reconstruct all physical original source input arrays exactly from the frozen parent and all four #722 source-fiber files; validate every 51-palette source domain on the complete 28D physical GF5 source.
- Run real W32 independent complete 51x51 source signed-equation test.
- Run genuine full W34 F pair/triple + all 300/325 source pairs and verify all forbidden tuples by direct complete physical coordinates.
- Export full binary constraint graph, arc-consistency proof transcript and source exactness in GitHub-hosted artifacts.
- Avoid any theorem that the frozen-core+binary CSP alone proves a full final ASET. If it is arc-consistent, next step is a complete multi-variable CSP/CEGAR search with explicit >=3-editable signed-event clauses. Any alleged final full zero ASET must be independently rehashed against ALL C(425,3)=12,704,100 original GF5 triple sums and all C(425,2) true original pair sums.
- If this specific T is proven UNSAT, alternative 25/26-ID minimum covers remain possible and must not be ruled out.

No claim of an all-h seven-motif result, improved asymptotic ASET exponent or root Branch A/B/C closure.
