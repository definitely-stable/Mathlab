# HYP-105 G5-C2 — Exact signed-trade density frontier and finite alteration evidence

Date: 2026-10-09. Active issue [#106](https://github.com/definitely-stable/Mathlab/issues/106), parent [#95](https://github.com/definitely-stable/Mathlab/issues/95), predecessors [G5-C0](HYP-105-G5-C0-SIGNED-ORACLE-FOUNDATION.md) and [G5-C1](HYP-105-G5-C1-TRADES.md).

**Status: CONDITIONAL_CLASSICAL_ALTERATION_THEOREM / EXACT_FINITE_CONFLICT_SPECTRUM / NO_NEW_EXPONENT / NO_RATIO_THEOREM / NO_RUST.** This slice turns G5-C1's signed trades into *quantified forbidden-support counts* and makes explicit what must be proved about an infinite family before a genuine exponent result is possible. Do not confuse an empirical sample on 12 coordinates with an asymptotic count for arbitrary m. No other repositories are changed.

## 1. Freeze three mathematically distinct objects

(1) **Unrestricted ASET**: distinct nonzero vectors in GF(5)^m, support at most four, arbitrary nonzero coefficients, with *all* subset sums of cardinalities 0..3 unique. Allowed collision types include unequal sizes such as 1-vs-2 and 3-vs-2 (G5-C1).

(2) **Restricted candidate universe** B_m: unit all-one columns of *exact support four*, with exactly two coordinates in a fixed left block and two in a disjoint right block. For q=5 the total-coordinate-sum functional equals 4 per column. It follows that every trade with at most three columns on each side has the SAME number of columns on both sides. Distinctness rules out 1-vs-1. Thus every failure of exact three-sum injectivity in B_m reduces to an unordered disjoint 2-vs-2 or 3-vs-3 equality; if a 3-vs-3 equality shares a column then cancellation reduces to 2-vs-2. This characterization is **NOT** valid for unrestricted weighted ASET.

(3) **Forbidden-support hypergraph** H_m on column IDs of B_m. For each actual signed collision add its participating column-ID union as a forbidden hyperedge. Keep only inclusion-minimal supports. In the restricted unit GF5 case minimal edges have sizes 4 and 6; let T_4(m), T_6(m) count these distinct supports (not relation multiplicities). If a 6-edge collision contains an independent 4-edge collision support, the 6-edge is redundant and dropped. A subset is actual ASET through d=3 iff it contains **no** hyperedge of H_m.

Tests and the counting script work for any **finite** allowed B, using W(3,2) as an explicit fixed graph-only construction. The factor graph's girth eight does not imply ASET: the G5-B four-column collision is intentionally present.

## 2. C2-A — alteration lemma and constructive finite certificate (classical)

**Proposition (any finite forbidden hypergraph, not ASET-specific).** Let H be an arbitrary hypergraph on N items, with T_t inclusion-minimal forbidden supports of size t>=2. For each rational or real p in [0,1], there exists an H-independent vertex set of size at least

    p*N - sum_{t>=2} T_t * p^t.

In particular the maximum H-independent set is at least the maximum of this expression and zero. The bound is numerical, not a claimed tight optimum.

**Proof.** Include each item independently with probability p, obtaining S. The expected number of selected items is pN. Each forbidden hyperedge of size t is fully contained in S with probability p^t, so the expected score |S|-#{H subseteq S} is exactly the displayed expression. Some realization has score at least its expectation. From this realization, remove one currently selected item from each forbidden edge still fully present. Removing an item never creates an edge and removes at most as many items as the original number of fully present edges. The final independent set has cardinality at least the original score, proving the bound. QED.

**Explicit conditional-expectation derandomization (same bound).** Process IDs i=0..N-1. Conditional on earlier inclusion/exclusion decisions, the difference between the conditional score expectations if i is included and if it is excluded is exactly:

    Delta_i = 1 - sum_{H containing i, H avoids earlier excluded IDs}
                      p^{number of elements of H with ID>i}.

Keep i when Delta_i>=0, otherwise exclude it. By construction each step does not decrease the conditional expected score. When all IDs are fixed, the resulting integer score is at least pN-sum T_t p^t. Greedy cleanup then produces a real independent set. The implementation calculates these rational quantities with Python Fraction, not machine floating-point. A float is used *only* for choosing among candidate rational grid points; the certificate itself is re-evaluated exactly. **No optimality** of the chosen grid probability or extracted family is asserted.

The lemma is standard first-moment probabilistic alteration and conditional expectations: **DERIVED_CLASSICAL**, not a new math discovery. Its value here is a falsifiable, precisely priced link from signed-trade counts to an ASET lower construction.

## 3. C2-B — precise asymptotic GO/STOP thresholds for the W(3,2)-style base

**Conditional asymptotic theorem (same classical alteration argument).** Suppose for arbitrarily large m one has a **specified true family** B_m on m coordinates, N_m >= c*m^a distinct columns, and T_t(m) <= C_t*m^{b_t} distinct inclusion-minimal signed-trade supports of size t, with c>0, fixed finite set of t>=2 and constants C_t independent of m. Set

    delta_* = max(0, max_t [(b_t-a)/(t-1)]).

Provided delta_*<a, the alteration lemma yields an actual ASET subfamily of size Omega(m^(a-delta_*)). If some equality b_t-a=(t-1)delta_* holds, choose a sufficiently small *constant* prefactor p=lambda*m^(-delta_*) to make the expected total forbidden penalty at most half of N_m p. This is a uniform-in-m argument only when the assumed **upper counts for ALL m** and the lower base size are actually proved.

**Proof.** Use p=lambda*m^(-delta_*), with fixed 0<lambda<=1. For each t, T_t p^t <= C_t lambda^t m^{b_t-t delta_*} <= C_t lambda^t m^{a-delta_*}, since delta_* >= (b_t-a)/(t-1). Meanwhile N_m p>=c lambda m^{a-delta_*}. For finitely many t>=2, choose lambda so that sum_t C_t lambda^{t-1} <= c/2. The expected score is at least (c lambda/2)m^{a-delta_*}. The previous finite lemma extracts an actual independent ASET family. QED.

**Target numeric gate, global-split UNIT support4 ONLY.** The classical generalized-quadrangle base graph in G5-B has N_m=Omega(m^(8/3)). Here t=4 and t=6 suffice, so

    delta_* = max(0, (b_4-8/3)/3, (b_6-8/3)/5).

To strictly beat the published lower **power** 12/5 using this alteration route (and hence ultimately beat its logarithmic factor asymptotically), sufficient strict exponent conditions are:

    b_4 < 52/15   (=3.4666...)
    b_6 < 4.

This follows from a=8/3 and the target delta_*<8/3-12/5=4/15. These are **CONDITIONAL SUFFICIENCY TESTS**, not measured asymptotic T_4 or T_6 bounds, not necessary conditions for *all possible* improvements, and not a proof of a better lower bound. For unrestricted weighted ASET, t=2,3,5 collisions also exist and their counts must be charged separately; never use this even-t simplification without uniform unit assumptions.

**Strong gate for G5-C3:** provide explicit deterministic or probabilistic infinite coordinate-pair labelings B_m with rigorous upper bounds on BOTH T_4(m),T_6(m) satisfying the displayed inequalities, including constants, along an unbounded sequence of m with bounded gaps (or justify extension to all sufficiently large m). Alternatively find a different counting argument giving an unconditional stronger upper ASET bound. Finite W32 measurements cannot certify those exponents.

## 4. C2-C — exact finite graph-only countermodel spectrum

Executable sources: [hyp105_g5c2_density.py](../../research/hyp105_g5c2_density.py) and [test_hyp105_g5c2_density.py](../../research/test_hyp105_g5c2_density.py). The reference starts from the 45-edge incidence graph W(3,2), already proved to have girth eight in G5-B. Each of its 15 vertices on each side is injected into the 15 coordinate-pairs of a six-coordinate half, producing 45 *unit support4 GF5* columns on 12 coordinates. The original bijection and three fixed-seed permutations (0,1,2) are evaluated, without changing abstract factor-graph girth.

1. Independently group all C(45,2) pair sums and C(45,3) triple sums by **complete integer coordinate signatures** (integer sums equal field sums here because no coordinate count exceeds three and p=5).
2. Convert equal distinct subset sums to disjoint 4- or 6-column forbidden supports, cancel shared triple IDs and remove 6-supports already containing a smaller 4-support collision. Deduplicate by column-ID bitmask.
3. Use a deterministic rational p-grid to choose a *finite* first-moment bound, then conditional expectations and deletion to build an explicit exact ASET subfamily.
4. Independently validate its actual GF5 all-subset sums (including cardinality 0) with the older direct oracle. Cross-check randomized small subfamilies against exhaustive GF5 signed-pattern enumeration. Exhaustively enumerate the entire Bernoulli distribution on small toy hypergraphs to validate the rational expected-score equality.

A real ASET witness extracted from a dense **invalid** graph-only family is a useful correctness check; its finite size does not establish any improved order of growth. Count distinct minimal supports, not the number of relation witnesses or hash bucket collisions. The script prints a deterministic JSON report to stdout when run directly:

    python research/hyp105_g5c2_density.py
    python -m unittest discover -s research -p "test_hyp105_g5c2_density.py"

The existing research CI unittest discovery picks up the new test automatically. For publication or a new exponent, demand **exact-head GitHub-hosted SUCCESS**, inspect failures and evidence, and expand from W32 to a mathematically proved all-m family.

### 4.1 Exact GitHub-hosted W(3,2) data (m=12 only)

[Research workflow #972 on PR #116](https://github.com/definitely-stable/Mathlab/actions/runs/37893366030) completed **SUCCESS**, including full test discovery and the dedicated deterministic density report. Exact code head for that run: 8673ded4aebef6618121a693a345753c0bb1fb55. These are numbers of **distinct inclusion-minimal forbidden column-ID supports**, not signed-relation multiplicities. Base W32 has 45 columns for each row.

| L/R coordinate-pair labeling | T4 | T6 | Extracted exact GF5 ASET columns |
| --- | ---: | ---: | ---: |
| Original fixed labels | 69 | 1940 | 19 |
| Permuted, seed 0 | 53 | 1874 | 20 |
| Permuted, seed 1 | 46 | 1722 | 20 |
| Permuted, seed 2 | 50 | 1750 | 19 |

These graphs are isomorphic as **pair-signature** bipartite factor graphs (girth 8), but have different coordinate-level signed-trade counts under legal injective pair labelings. Thus graph isomorphism and girth **do not determine signed-trade density** even in this 45-edge example. The extracted subfamilies independently pass actual complete GF5 subset-sum checks through cardinality three; **not** claimed maximal at m=12.

**Finite-only boundary:** fitting a growth exponent from these four samples, which all have the same ambient m=12, would be invalid. No proved upper b4/b6, improved ASET asymptotic bound or growing ratio follows. This section pins numerical CI evidence; future implementation changes must reverify counts.

## 5. Prior art, novelty limitations and stopping rule

- [Naor–Verstraëte, Combinatorica 2008, author-hosted full paper](https://web.math.princeton.edu/~naor/homepage%20files/PARITY.pdf), Theorem 2.2: already proves a collision of equal three-element signed subsets at density above O_q(m^(8/3)). Its theorem is **not** the six-wise arbitrary-coefficient independence converse.
- Lefmann (2005), [publisher DOI](https://doi.org/10.1017/S0963548304006625), LIT-043: already gives A_lin and hence ASET lower Omega_q(m^(12/5) (log m)^(1/5)) when k=6,r=4 and gcd(5,4)=1.
- Classical probabilistic alteration / conditional-expectation arguments are **not** new. Existing catalog LIT-043, LIT-152, LIT-136, LIT-148 reused without duplicates. Full 2025–2026 theorem-level novelty census is not claimed complete.

**C2 scope/decision:** mathematical density *criterion* and finite deterministic executable evidence, NO_EXPONENT_IMPROVEMENT, NO_GROWING_RATIO_PROOF, NO_RUST. Keep #106 and parent #95 OPEN. If G5-C3 fails to prove true infinite-family conflict-count bounds, record STOP_NO_NEW_EXPONENT for this alteration strategy rather than promoting finite numeric samples or claiming a new theorem.
