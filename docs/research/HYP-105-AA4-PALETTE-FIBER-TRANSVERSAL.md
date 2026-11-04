# HYP-105 / #230 — AA4-FIBER: exact 51-palette forbidden fibers and order-independent erasure transversal

Scientific DRAFT, stacked on immutable PR #719 SHA bb9378cac271cbfb8f6f446d932fd009178f8d79. The certified s=4 two-scheme finite zero-to-three ASETs remain unchanged. Root #230 remains OPEN_WITH_FORMAL_BLOCKER; this document proves no all-h availability of clean recolorings and no asymptotic exponent.

## Exact model and quantifiers

Fix any N distinct original source IDs and vectors c_j in GF(5)^m. For each original incidence i, its immutable four physical support positions J_i are the two point and two line coordinates of the separately pair-injective globally fixed maps f,g. A legal replacement c_i(t) vanishes off J_i and has four nonzero coordinates with total GF(5) checksum 4. Its palette P_i has exactly 51 distinct vectors, independently of s, N, f and g. No source IDs are duplicated, no 4-support is modified, and c_i(t) is globally reused in every event.

For k=2 or k=3, let E_k(c) be the set of unordered pairs {A,B} of disjoint ORIGINAL k-subsets with equal complete GF(5)^m sums. This is the genuine distinct-source signed k-vs-k event set, not the all-triple D3 proxy or an expectation over random palettes. For fixed i define

H_{i,k}(t) = # { (A,B): A subset [N]\{i}, |A|=k-1; B subset [N]\{i}, |B|=k; A cap B = empty; c_i(t)+sum(A)=sum(B) }.

Every event containing i has exactly one global orientation placing i on the positive side. Therefore H_{i,k}(t) is exactly the number of events containing i, with no 2-to-1 ambiguity.

## Theorem 1 — exact forbidden palette fiber criterion

Let W_{i,k} be the multiset of full physical residues sum(B)-sum(A) over all qualifying disjoint original other-ID A,B. For each palette t, H_{i,k}(t) is the multiplicity of the COMPLETE vector c_i(t) in W_{i,k}. In particular, a residue can forbid t only when it vanishes at EVERY physical coordinate outside J_i and equals the legal four-coordinate pattern ON J_i. A single qualifying pair/triple forces at most one of the 51 t, but different pairs/triples may force the same t.

Define B3(i)={t:H_{i,3}(t)>0}, B2(i)={t:H_{i,2}(t)>H_{i,2}(old)}. For every fixed legal original source assignment:

CleanSafe(i) = P_i \ (B3(i) union B2(i))

is EXACTLY the set of replacements which (a) create zero true signed six-distinct-original R3 events containing i, and (b) do not increase total genuine R2. All events avoiding i are unchanged. Hence a clean R2-safe recoloring exists if and only if |B3 union B2| < 51. Its count is 51-|B3 union B2| and the computable conservative lower bound is

|CleanSafe(i)| >= max(0, 51-|B3|-|B2|).

This is a sufficient coverage inequality, NOT a general bound on the sizes of B3 and B2. Even if the AVERAGE H3 over 51 patterns is small, the R2 admissibility filter must be intersected explicitly; an unqualified inference that some simultaneously safe t exists is invalid.

Proof: the complete residue equality is exactly the defining signed equation, and each source event with i has a unique i-positive orientation. Every altered k-event contains i, so E_k(new) outside i is unchanged. Thus the new incident k-event count equals H_{i,k}(new), and the total R2 difference is H_{i,2}(new)-H_{i,2}(old). Intersect the conditions H3(new)=0 and H2(new)<=H2(old); take the complement within 51. The lower bound follows by the union bound on two finite sets. QED.

A weaker but sometimes cheaper sufficient criterion is: number of distinct source-residual values on the legal 51-pattern support plus number of R2-worsening patterns is at most 50. Bounding the number of original 2+3 witnesses instead of distinct residues also works, but is strictly more conservative when collisions share a palette.

## Theorem 2 — exact composition and transversal necessity

Consider ANY sequence of legally supported single-original-ID changes, each satisfying H_{i,3}(new)=0. The edited ID may be revisited; let T be the SET of all edited original IDs, and let E3^0 be the ORIGINAL signed event set before the sequence. After every prefix,

E3^prefix = {e in E3^0 : e cap T_prefix = empty}.

In particular the final event hypergraph depends ONLY on the set of edited IDs, not on their order or the chosen palettes, CONDITIONAL on every intermediate edit actually being clean. This does NOT say that any arbitrary order or palette can realize the same T: feasibility can be strongly order-dependent.

Proof by induction: the PR #719 exact no-new-event single-edit theorem deletes precisely current events containing the edited ID and leaves all others untouched. Filtering by avoidance of i after filtering by avoidance of T is the same as filtering by avoidance of T union {i}. QED.

Therefore a complete zero-R3 clean erasure sequence must select a vertex cover of the INITIAL six-uniform signed event hypergraph. If it also ends R2=0 (even if its intermediate R2 events change), every INITIAL four-ID R2 event must contain at least one edited ID, because an event with all four unchanged columns persists. Consequently

number of distinct edited original flags >= tau(E2_initial union E3_initial)
                                      >= nu(E2_initial union E3_initial),

where tau is minimum vertex-cover/transversal cardinality and nu is maximum number of pairwise vertex-disjoint original event edges. These are genuine source-ID set-system bounds, not bounds on an arbitrary abstract graph without original IDs. For an R3-only target use E3_initial.

If every accepted edit also satisfies true R2 nonincrease and strictly decreases R2+R3, there are at most R2_initial+R3_initial accepted edits; this is a TERMINATION bound, not a guaranteed convergence theorem.

## Application to permanent two W34 finite source certificates

Frozen #719 independently recorded two actual true-original W(3,4) 425-source maps. Lex begins (R2,R3)=(1,54), ends (0,0) after 27 distinct genuine source recolorings. Reverse-line begins (0,61), ends (0,0) after 29 distinct recolorings. The saved trace has exactly zero newly created six-ID events per step, so these traces induce partitions of the INITIAL 54 and 61 six-ID events according to their first edited source ID. The sum of recorded deletion counts must equal 54/61, respectively. The new independent lightweight tests verify this trace-level partition arithmetic, plus separate full-GF5 miniature exhaustive falsifiers for the two theorems. The full 12,704,100 genuine original-triple physical W34 rehash remains the INDEPENDENT #719 verifier; trace arithmetic alone is NOT a substitute.

To quantify tau or nu numerically for the real W34 initial six-ID hypergraphs, export the ACTUAL canonical six-ID witness sets from the independent external complete GF5 referee. The committed #719 short certificate has per-edit deletion counts but not an independently complete initial witness hypergraph, so numeric optimality of 27/29 moves is NOT claimed here. The new theorem explains exactly what a future minimum transversal / packing oracle must certify.

## Formal all-h research gate

For each dyadic s=2^h and EACH fixed pair of allowed globally injected physical f,g, a universal greedy convergence theorem would require a proof that EVERY reachable positive-risk source state has some original ID with a legal t in CleanSafe(i) which strictly reduces R2+R3. Existence on W(3,4), or even a source-independent upper bound on average H3, does not imply this statement. No such h-uniform non-saturation theorem is proven in this slice.

More importantly, root #230 Branch A concerns an all-f,g lower bound on seven ORIGINAL six-motif counts S_s(f,g), not the existential deterministic source coefficient assignment. A finite zero R3 coefficient assignment and this conditional palette criterion do NOT refute Branch A and do not settle Branch B or C. The prior conditional root machinery and externally sourced ordinary C6 supersaturation hypotheses are preserved without promotion.

## Independent falsification and governance

The dedicated Python oracle uses the COMPLETE GF5^m residues, disjoint original IDs, exactly 51 legal checksum4 patterns, and an algorithmically different direct pair/triple sum enumeration to cross-check H2/H3. It tests EVERY legal 51-replacement option for a fixed six-original-vector witness, including palettes creating NEW conflicts, full event SET subtraction, R2 nonincrease, a second consecutive safe edit and exact transversal bounds. Tests fail when incident-event orientation or distinct-original-ID conditions are corrupted.

The UCT-005 D1-B incidental algorithm-term inventory remains fail-closed. The inherited #719 FULL Research failure is from three unregistered textual 3SUM mentions (one prose and two identical JSON keys), not a GF5 mathematical failure. This child registers them by EXACT reviewed source lines and exact expected counts, extending the audit without excluding paths, suppressing tests or weakening the upstream dependency-hardness firewall.

Next actual mathematical frontier: derive a nontrivial h-uniform upper bound on forbidden legal palette fibers (or an all-h obstruction to such a bound) from true W(3,s) incidence and arbitrary correlated pair labels. The present iff criterion, two finite certificates and event transversals are inputs, not that missing theorem.
