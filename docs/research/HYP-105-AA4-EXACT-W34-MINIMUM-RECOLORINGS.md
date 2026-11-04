# HYP-105 / #230 — AA4-OPTIMAL: exact minimum ORIGINAL W(3,4) legal GF(5) source recolorings

Research Draft stacked **strictly** on frozen PR #724, exact SHA `c2354156a23f36e5f3e7b24a104a052c18a6cc55`. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`; this result does not establish the all-h seven original six-motif theorem or an ASET asymptotic exponent.

## The new result is an exact FINITE optimality theorem, not merely a solver attempt

Fix the actual complete symplectic W(3,4) original 425 incidence flags and one of the TWO specific previously frozen separately globally pair-injective real point/line source embeddings `f,g`, either lex or reverse-line. Fix the original checksum4 assignment `c^0` of 51 legal nonzero source palettes per original flag from PR #719, retaining each original physical four-coordinate point/line support and the entire 28-coordinate GF(5) vector representation.

Let

`m(f,g,c^0) = min #{i in 425 ORIGINAL flags : c_i != c_i^0}`

over ALL *legal* resulting coefficient palette assignments `c` on the same globally fixed `f,g` such that all 0-, 1-, 2- and 3-subset sums of its 425 complete original GF(5)^28 source columns are distinct. This definition makes NO monotone-descent, per-step no-new-R3, or order assumptions; simultaneous arbitrary legal recolorings are allowed.

**Exact theorem for these two particular actual source maps:**

- `m(lex,c^0)=25`.
- `m(reverse-line,c^0)=26`.

Both bounds are ATTAINED by new complete physical original GF(5)^28 legal source assignments with EXACTLY those 25/26 changed original flags. No recoloring outside the certified support occurs, so these are strictly stronger than the older #719 concrete upper bounds 27/29. Both new candidate assignments were first discovered at CEGAR iteration 0 without any learned constraints and THEN independently tested by the existing complete external-disk 12-byte source triple-sum referee. The CEGAR search method is NOT used in the proof of optimality.

### Proof of the lower bound: initial signed-event hitting set

At the initial assignment `c^0`, form the hypergraph H whose edges are the ORIGINAL 4-flag supports of every true signed 2v2 equality and ORIGINAL 6-flag supports of every true signed 3v3 equality in the complete physical GF(5)^28 vector space. The C(425,3)=12,704,100 full source-triple exact nonprobabilistic radix census and all C(425,2)=90,100 source pairs establish all initial events, not merely a heuristic witness sample: lex has 1 R2 +54 R3 true signed events (and 475 equal sum triple pairs including overlaps), reverse-line has 0 R2 +61 R3. The initial full physical 28D equalities are included as signed original-ID partitions in immutable #721. New referee independently verifies all these signed equations and source provenance, and reruns the FULL original initial pair/triple census.

For ANY final collision-free assignment, if a signed original event e is disjoint from the set T of changed original ID columns, both physical GF(5) sums remain exactly unchanged, contradicting collision freedom. Hence T is a transversal of H: `|T| >= tau(H)`. This holds for all legal simultaneous, nonmonotone and arbitrarily ordered changes.

Frozen #721 independently certified the EXACT abstract transversal numbers, NOT heuristic lower estimates:
- lex: 55 complete true signed original events, 231 active original source IDs; incidence-dominance reduces to 74 nondominated IDs without changing the minimum transversal. Exhaustively refute cover cardinalities k=23 and k=24, and exhibit a concrete size-25 cover. Thus tau(H)=25, with 1,422 branch nodes in the saved proof run. The new independent referee reruns exact cardinality refutations.
- reverse-line: 61 true signed original events; **26 pairwise vertex-disjoint original physical event edges** give a direct 26-source lower bound, while an explicit 26-source transversal proves the upper bound. Thus tau(H)=26 without trust in an exact-search implementation.

These mathematical lower bounds are universal for **all legal GF(5) recolorings on the same frozen initial source model**, regardless of the search algorithm.

### Proof of the matching upper bound: independently complete actual physical source certificates

The permanent certificate `research/hyp105_w34_minimal_source_recolor_certificates.json` contains BOTH full 425-source legal final palette arrays and the COMPLETE corresponding 425-source initial arrays, the changed original-ID lists, the precise parent lower-bound proof provenance and the exact hosted W34 zero-result source jobs. For each scheme, the new proof checker:

1. Independently rebuilds all 425 actual W(3,4) original incidence flags, the same globally separately pair-injective point/line `f,g`, their exact four physical nonzero positions, and all full 28-coordinate GF(5) columns for the old and new 51-pattern assignments.
2. Checks all 425 legal nonzero GF(5) checksum4 palettes and the unchanged physical coordinate support. Compares old/new full columns at ALL 425 original IDs, proving precisely the 25 or 26 source IDs in the certified minimum cover actually changed and no other original columns changed.
3. Independently reconstructs all initial signed 2v2 and 3v3 ORIGINAL 4/6-ID equalities directly in all 28 physical coordinates and recomputes the exact initial minimum hitting-set lower-bound proof.
4. Audits EVERY one of the C(425,2)=90,100 final original source pair sums in complete GF(5)^28 directly; no two are equal. The 425 singletons are independently unique.
5. Replays the independently implemented established external-disk exact 12-byte GF5 signature original triple referee on **all C(425,3)=12,704,100 triples**, for both old and new assignments. The zero final 3-subset-sum collisions and zero signed R3 conflict count have no probabilistic hashing or sampling assumption; all 425 source IDs and all actual 28 physical coordinates are covered.

Moreover, every source vector has checksum 4 mod5, so the sums of k=0,1,2,3 ORIGINAL flags have distinct checksum values 0,4,3,2 in GF5. This independently eliminates any cross-cardinality equalities. Hence each new assignment is a FULL source 0-to-3 ASET; its changed original source-ID support is exactly the minimum transversal T and thus `m=tau(H)`, proving both exact finite minima.

## Reproducible result and acceptance

| Frozen actual original W34 source | Complete initial original (R2, D3, signed R3) | Old legal full zero-ASET edits (#719) | Exact source hitting-set lower (#721) | New full legal 0-to-3 ASET edits (#724) | Exact finite minimum |
|---|---|---:|---:|---:|---:|
| lex | (1, 475, 54) | 27 | 25 | **25** | **25** |
| reverse-line | (0, 61, 61) | 29 | 26 | **26** | **26** |

The initial complete CEGAR proof host [#41878874102](https://github.com/definitely-stable/Mathlab/actions/runs/41878874102) succeeded on BOTH real maps and independently exact-full-12.7m rehashed the physical zero candidates. This draft introduces an additional strict permanent source certificate AND a new independent **before+after** complete 12.7m referee on the final HEAD, plus negative tampering tests. Only mark this NEW draft accepted when its exact-head specialized, INDEX and Research workflows ALL succeed.

## Fundamental scientific limits

This is a new **exact finite GF(5) source optimization theorem** for TWO specifically fixed source maps at s=4 and their respective specific initial 425-source legal assignments. It does not say the optimal support for ANY global pair-injective f,g is 25 or 26, and certainly does not prove a universal all-h (s=2^h) positive-density lower bound, nor an infinite correlated counterexample to the original seven six-motif event expectation. The original HYP-105 #230 Branch A/B/C criterion is NOT discharged; leave the issue open. A compact publishable finite computational theorem is possible subject to independent mathematical review and complete released certificates, but its scientific scope must never be confused with the root asymptotic problem.

## Next scientifically substantial direction

Now that each of the TWO finite actual W34 supports attains the theoretical minimum abstract transversal, further optimization of recolor count for those maps cannot improve the theorem. The rational next mathematical task is to investigate **uniform s and adversarial correlated f,g**: e.g. can a strictly global source-label-invariant geometric argument force Ω(s^6) signed six-motif count independently of coefficient recoloring, or can an explicit valid infinite correlated construction defeat it? Alternative finite source maps are exploratory tests only, not an asymptotic proof.
