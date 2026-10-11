# HYP-105 C24-B8-H — joint original-sixset cylinder lower and correlated P2+R gate

Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked **Draft** on [B8-G PR #363](https://github.com/definitely-stable/Mathlab/pull/363), exact parent HEAD `4e28b85298fd7ddca1d3e7339e471a00ea60fc19`. No main change, no merge, no self-hosted runners. **RESTRICTED_THEOREM_C_JOINT_PINNED_CYLINDER_SOURCE_FLOORS**, NOT Branch A, B, all-h universal Omega(s^6), GF(5) full R3 or ASET exponent.

## 1. Why a joint bound rather than another pair-only optimization

B8-E proves `S(f,g)=mu_f+P2(f,g)+R(f,g)`; B8-F/G certify pointwise global lower bounds on P2, but finite genuine W32 witnesses prove their separate `min P2 + min R` positive-floor gate cannot close. That does NOT rule out a positive floor on the **correlated sum** P2+R. We therefore work directly from ORIGINAL six-incidence source contributions rather than treat R as an independent random error.

For any fixed original left f, the seven-family score is an exact finite sum over distinct original incidence sixsets J:

```
S(f,g)=sum_{J in ORIGINAL f-eligible sixsets} w_J * A_J(g),
w_J >= 1 integer, A_J(g) in {0,1}.
```

Ordinary A_J checks the genuine right physical 2-factor acceptance. D6 additionally checks the exact matched six-position connected C6 dual signature (not a Boolean cycle-presence relaxation). Each source factor depends only on the original right-line IDs appearing among its SIX original incidence positions; thus |supp J|<=6. w_J denotes exact compressed original multiplicity, preserving distinct sixsets: no motif orbits are equated with original sources, no per-J independent global injection.

## 2. All-h local source-support lower lemma (with explicit pinned qualifier)

Let n be the number of ORIGINAL right lines, m=C(a,2) physical K_a edges, f any admissible complete LEFT injection. Fix **one globally injective partial RIGHT assignment** h on K subset [n] into distinct host edges. Let `F=[n]\K` be unpinned original right lines and `E_free=E(K_a)\im(h)` available host edges. Any legal entire extension g belongs to a constrained **cylinder** `C(h)`.

For each original eligible J put `U_J=supp(J) cap F`. Partition ORIGINAL source records (disjointly by original sixset, retaining w and D6 positional information) into disjoint buckets B_t. Define `U_t=union_{J in B_t} U_J` and exact local bucket function

```
H_t(phi) = sum_{J in B_t} w_J A_J(h union phi),
phi : U_t -> E_free  injective.
```

Every source in B_t reads only h and phi restricted to U_t; no other assigned right line affects its A_J. Consequently, for **EVERY single globally coherent entire extension** g in C(h),

```
S(f,g)=sum_t H_t(g|_{U_t}) >= sum_t min_{injective phi:U_t->E_free} H_t(phi)
       := L_joint(h; B).
```

This is a deterministic, **pointwise lower bound on the genuine seven-score S** in the fixed cylinder. Equivalently (using the fixed f exact B8-E mean and projection),

```
P2(f,g)+R(f,g) >= L_joint(h;B)-mu_f,     ALL g in C(h).
```

It is a JOINT P2+R certificate without separately controlling R. It does not need the B8-E Gram to compute the bound; the Gram independently audits the equality. It requires **nonnegative source coefficients** and correct original source supports. The all-h proof does not assert this lower is positive for any nontrivial unpinned h.

**Monotonic coupling:** merging two distinct source buckets and jointly minimizing the union of their free supports never lowers the bound:

```
min_phi (H_A(phi)+H_B(phi)) >= min_phi H_A(phi)+min_phi H_B(phi).
```

Thus `L_supportwise <= L_coupled <= min_{g in C(h)} S(f,g)`. The first groups exactly by free original support U_J; the second greedily merges whole buckets while the union free support has size <= a user-specified cap. Merge selection is deterministic, but **not claimed optimal**. The final single bucket `B=all sources` gives the EXACT cylinder minimum only when every entire completion is enumerated within an explicit budget. These statements hold for *any* n,m, including all h, with the pinned qualifier. Setting h empty is legal but the supportwise relaxation may yield zero and the exact-global enumeration is intractable: this is NOT a universal GQ lower.

## 3. What the executable certificate actually checks

The reusable core `research/hyp105_g5e2b3e1c24b8h_joint_source_cylinder.py` does NOT pretend to derive a source support from an arbitrary evaluator. Each record is `(canonical original-right support, positive original multiplicity, payload)`. The caller contract is that the evaluator reads ONLY those support IDs; the true W32 adapter independently validates equality between the support and the six original incidence-line positions. For each bucket, all assignments to its union support draw **distinct host edges** from the SAME E_free. What is relaxed is coupling BETWEEN buckets, not physical injectivity within a bucket.

Inputs with noncanonical support, duplicate pinned physical edges, nonpositive weights, non-Boolean oracle output, excessive completion-state count or excessive record-evaluation budget fail closed. Runtime complexity depends on `sum_t (|E_free|)_{|U_t|} * |B_t|`. A bounded exact solver is not an asymptotically efficient all-h six-motif oracle. No 15! global right-bijection loop is used for genuine W32.

## 4. Genuine W(3,2) independent dual-oracle experiment

Fix original f0 and full genuine score-68 right g68 from B8-E/F/G; freeze original right-line indices 0..9 at the physical K6 edge images of g68. There are **five** unassigned original right lines and **five** unused physical K6 edges, giving exactly 5!=120 entire globally coherent right completions. This cylinder is not a local-swap neighborhood and does not contain all 15! right assignments.

- Start with all genuine f0 left-eligible ORIGINAL six-incidence sets, 62,370 candidates and 53,907 seven-family-eligible multiplicity; compile original support, tag, six incidence positions and exact D6 signature. No synthetic score enters the main witness.
- Evaluate the per-original-support local min and the stronger size<=3 coupled bucket min. The final full 5-line bucket computes exact cylinder min with 120 entire maps.
- **Independent second oracle:** for ALL 120 entire globally coherent completions evaluate the established 130-physical-template right pullback, which is algorithmically different from local original-source scanning. Its exact cylinder minimum must coincide with the grouped whole-bucket minimum. Recount the selected minimum and g68 with BOTH original left-first and original RIGHT-FIRST 62,370-original-sixset scorers.
- Independently compile original B8-D 105-line pair influences and B8-E projection. On each of the SAME 120 global assignments compute exact rational P2 and R=S-mu-P2; verify `min(P2+R)=min(S)-mu` and `min P2+min R <= min(P2+R)`. The difference quantifies **true correlated gain** in the cylinder; never substitute any witnessed R as global floor.
- Report separate sourcewise, coupled and exact minima as numerical evidence ONLY after hosted execution. No numerical outcome is hardcoded in the theorem or PR description before independent CI.

## 5. Falsification & acceptance

Independent fast K4 tests use nonlinear functions of actual *shared physical edge adjacency* for multiple original supports, enumerating every 6P4=360 complete global injection and multiple pinned cylinders, exact minima and monotonic group relaxations, multiplicity, budget and invalid-input guards. The true W32 workload is **dedicated GitHub-hosted only**, not default `unittest discover`. Preserve inherited 6-shard Full Research plus fail-closed aggregate and INDEX; no redundant giant orbit search, cache bypass, or self-hosted jobs.

**Acceptance**: Dedicated B8-H Contract, entire inherited Research and INDEX must be SUCCESS on the exact same final B8-H head. Parent B8-G's own 3/3 exact-head checks must be successful independently. Keep PR Draft without merge authorization; root issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

## 6. Next real blocker

A positive (even sharp) cylinder lower only certifies a *subset* of right injections for one fixed f; it does NOT prove the all-f, all-g, all-h Omega(s^6) Branch A or infinite low-S Branch B. To scale beyond the cylinder, one needs a **global covering certificate** (e.g. verified branch-and-bound proof tree over all pinned prefixes) with lower floors on **every leaf** and an all-h analysis of size and positivity, or a symbolic original GQ incidence inequality allowing nontrivial floors with K empty. A finite W32 proof tree would only settle s=2, not asymptotic h. No R3 exponent is inferred.
