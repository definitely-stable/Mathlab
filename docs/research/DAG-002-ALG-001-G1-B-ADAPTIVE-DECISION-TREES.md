# DAG-002 × ALG-001 G1-B — adaptive cell-probe frontier and maintained-state syndrome counterexample

**Status 2026-10-09:** RESTRICTED_DETERMINISTIC_PROOF / ONLINE_EXACT_FINITE_MODEL / CLASSICAL_CODING_PRIOR_ART / UNIVERSAL_UCT_ROOT_OPEN / NO_RUST. Parent [G1 #140](https://github.com/definitely-stable/Mathlab/issues/140), [G1-B #157](https://github.com/definitely-stable/Mathlab/issues/157), G1-A [#145](https://github.com/definitely-stable/Mathlab/pull/145).

G1-A's `2^(B+G) V_c(N,W)>=2^n` ignores read probes. Here a *conditional, fixed-previous-state* argument includes `P`; a full online construction reveals how the bounds interact. Both are elementary uses of decision-tree influence and classical Hamming parity-check syndrome coding; **no claim of a genuinely new cell-probe lower bound**. Compared with unrelated UCT-005 [G2-B2](UCT-005-G2-B2-EXACT-BROADCAST-QUOTIENT-AND-STOP.md), which proves a separate zero-error *broadcast-communication* quotient theorem; our physical read/write model is not a corollary of that broadcaster result.

## 1. Unified finite-operation model and hidden-state exclusions

Fix an arbitrary **complete prior history**, including remote physical memory `R_old∈([2^c])^N`, the full public code, immutable vertex identities and labels, and all earlier local/trusted bits. After that fixed same history, the adversary chooses one of `K` legal new update inputs, leading to `K` **pairwise distinct n-bit query-output vectors**. For an antichain append replacing the parent list, `K=2^n`; single-coordinate updates or a restricted parent alphabet may have `K≪2^n`. Note that `K=2^n` is *not* a claim for single-entry matrix-rank updates.

The deterministic update changes at most `W` **distinct final remote cells** relative to that fixed prior snapshot and leaves behind `H=B+G` input-dependent local bits accessible to the queries. All mutable auxiliary caches, persistent query history or source parent arrays consulted by queries must either be included in these charged bits/cells or the model does not apply. Each coordinate query independently may make `≤P` **adaptive** probes to c-bit remote cells, with next probe address depending on all prior returned cell contents, fixed public query identity and final local bits. Arbitrary free computation between probes allowed; public code size and preprocessing may be huge but fixed independent of the new update input (must be charged in performance interpretation). One exact output bit per query, zero error; no cryptographic verification, parallel query side channels or free update payload to decoder. Query `i` has a fixed program after conditioning on new local state `l`.

Distinguish **three update metrics**: net changed cells `W_net`; actual remote write operations `W_phys_ops`; update **read** probes `R_u`. Always `W_net≤W_phys_ops` for binary overwrite, but bytes/page amplification and crash handling are unmeasured. Never count the address, data or update type of an instruction as an uncharged query-time side channel; update command is accessible only to updater.

## 2. G1-B-L1 — per-history adaptive decision-tree support bound (ELEMENTARY)

For nonnegative integer P and cell bit width c≥1, the maximum possible number of **distinct potentially probed addresses** in a single query decision tree of depth P is

```
T_c(P) = Σ_{d=0}^{P-1} (2^c)^d
       = 0                    if P=0
       = (2^(cP)-1)/(2^c-1)  if P>=1.
M = min{N, n*T_c(P)}.
V_c(M,W) = Σ_{j=0}^{min(W,M)} binom(M,j)*(2^c-1)^j.
```

**Theorem G1-B-L1 (conditional necessary bound).** Under §1, whenever `K` different legal successor updates from the **same fixed prior history** must give `K` different exact vectors of n coordinate-query answers, any deterministic scheme satisfies:

```
K ≤ 2^H * V_c(M, W_net),     H=B+G, M=min(N,n*T_c(P)).
```

**Proof.** Fix one of the at most `2^H` final local values `l`. All n decoders are now fixed deterministic c-ary decision trees of probe depth at most P. There are at most `T_c(P)` probe nodes/addresses in each tree, so their **union** `A_l` contains at most `M` distinct remote addresses. Across legal successors whose local value equals l, output bits can depend only on the remote projection `R_new|A_l`; data outside `A_l` cannot affect any output. The old fixed remote word restricts that projection to differ in at most W cells, hence at most `V_c(|A_l|,W)≤V_c(M,W)` different projections. Deterministic exactness implies no two distinct target answer vectors can share `(l,R_new|A_l)`. Sum over ≤`2^H` l and conclude the inequality. QED.

For W=0, remote contents remain fixed: `K≤2^H`. For P=0, M=0 and identical bound holds. For unrestricted P and N small, this specializes to G1-A. This is a **joint finite resource inequality**, not a verified mathematically novel lower bound: it composes elementary decision-tree node count and Hamming-ball injection, and it does not track preprocessing, cell address computation, randomized error or cryptographic soundness.

**Strict numerical separation:** choose `n=2,c=1,N=3,W=1,K=4,H=0`. G1-A admits `V_1(3,1)=4` and therefore cannot reject it; G1-B for P=1 uses M=min(3,2)=2, yielding `V_1(2,1)=3<4`, so **P=1 is impossible**. For P=2, M=3 and `V_1(3,1)=4`, leaving room for a construction. Even `N≫n` cannot defeat the P=1 bound, because each of the n fixed one-probe decoders examines at most one address per local state.

**Critical kill:** `H=0,P=0,W=n` still cannot serve nontrivial outputs; `H=n,P=0` can. Arbitrary shared remote cells may toggle *many* logical answers with one write; G1-A's coordinate XOR-delta Hamming *output-distance* argument cannot be reused. Data-dependent adaptive addressing is **already** included by the full decision tree, not approximated as one fixed probe address. A fixed prior history is indispensable; summing L1 over unrelated histories does not yield amortized multiclock lower bounds.

## 3. G1-B-C1 — exact maintained-state linear syndrome scheme

This is a **classical binary parity-check/Hamming-code construction**. For n logical bits, store N=`2^n−1` remote binary cells, indexed by all distinct nonzero columns `a∈GF(2)^n`; call the current remote bit `x_a`. Logical output is `y=⊕_{a≠0} (x_a a)`. Decoder query i computes the XOR of all cells whose column has i-th bit 1, reading exactly `P=2^{n−1}` remote bits. No mutable local label or global manifest (`H=0`).

**Operation DELTA(d):** the updater is given a publicly typed **n-bit delta** `d` (the request payload, not supplied to queries). For `d≠0`, it reads the current physical bit at column address d, toggles it and writes the new value. **Exact cost:** one remote update read `R_u=1`, one remote update write `W_phys_ops=1`, net changed cells `W_net=1`; for `d=0`, all zero. Then `y' = y⊕d` for **every previous remote state**, by GF(2) linearity. Arbitrary sequences of deltas therefore preserve correctness indefinitely, with no per-history reset or no-op side channels. This is a logical bit-cell model; physical page, journal, durability/rollback, public codebook ROM and real I/O timings are **not** measured. Encoding an arbitrary request TARGET(t) instead of DELTA(d) requires knowing current y; either the updater reads sufficient remote cells or maintains a separate priced n-bit trusted copy, so target updates are not being offered for free.

At n=2, `N=3` columns 01,10,11; `P=2`, `W=1`, `H=0`. The three possible nonzero delta commands each toggle one physical bit. This achieves the strict P=2 threshold from G1-B-L1 for **arbitrary online update sequences**. It is *not* a theorem that every dynamic DAG achieves this with constant cell writes or efficient queries as n grows; P and N both increase exponentially.

### G1-B-L2 — exact linear-subclass counting, NOT a general structure lower bound

Restrict further to fixed binary linear observables `y=Ax` with binary `n×N` matrix A, no mutable local state, **every** nonzero delta command required, and each update permitted to toggle **at most one physical binary cell**. Then the set of nonzero columns of A must contain **every nonzero n-bit vector**, whence `N≥2^n−1`. For each coordinate i, there are `2^{n−1}` required nonzero columns with bit i=1. Thus each output row of A has at least `2^{n−1}` nonzero entries and the *specified exact parity reader* accesses at least that many cells. With n=2, it needs ≥3 cells and ≥2 parity-probe reads per coordinate.

**Proof:** toggling one cell j changes y by precisely column `A_j`. From every current state and each prescribed nonzero delta, a one-toggle update exists only if `A_j=d` for some j. Distinct nonzero deltas require distinct respective columns. Exactly half of the `2^n` possible n-bit vectors have i-th coordinate 1, all nonzero. Under parity-reader semantics each such remote bit is individually influential over the full remote domain. QED. This is elementary linear algebra/code theory, **not** an unconditional lower bound on P for nonlinear or adaptive non-parity observers, nor a rank-only dynamic-matrix theorem. Code description and address widths matter in product design.

**Boundary example:** the tempting **fixed center + sparse XOR** codec from G1-A needs center changes across replacements. The syndrome scheme instead updates a persistent linear state via the delta alphabet and remains valid across every sequence. It does not contradict G1-A: different assumptions about codebook and query computation.

## 4. Exact finite regression and falsification ledger

- Exhaust ALL binary deterministic one-probe coordinate decoder pairs (constant, read, negated read) with `N=0..4` and every `W=0..N` remote snapshot. Count distinct output vectors independently of `V_1(M,W)`; no coordinate-addressing assumption.
- Explicit adaptive depth-two binary query tree has three potential addresses (root and two branches), but exactly two actual probes per execution; independent enumeration across all binary words.
- Exhaust all 4^4 (n=2) and 8^3 (n=3) online target histories **converted by the test client** into explicit `DELTA` updates, with reference parity-syndrome reduction different from the production-style per-coordinate query implementation; count the update's one read and one write. Also n=4 finite checks, plus n=2 all eight possible previous remote states and every desired delta.
- Exhaust all 0–3-column fixed binary 2-output matrices to verify one-toggle universality cannot occur with N<3, independent of A's rank.
- Show `P=1` impossible with `N=3,W=1,H=0,n=2`, while P=2 exact dynamic construction succeeds. Do **not** extrapolate to same construction for arbitrary DAG topology or authenticated snapshots.
- `R_u` (update read), `W_phys_ops`, `W_net`, `P_q` remain distinct; a bit write within a word or page must not be represented as a one-byte durable write.

## 5. Scientific novelty and next-step decision

Prior art already includes [Fredman–Saks 1989](https://doi.org/10.1145/73007.73040), [Pătraşcu–Demaine 2006](https://doi.org/10.1137/S0097539705447256), [Young Kun Ko, ECCC 2025 TR25-156](https://eccc.weizmann.ac.il/report/2025/156/) (one-way communication translation), [Ko ECCC 2026 TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) (Boolean Multiphase, 2.5-round verification), and classical coding/linear syndromes. The 2026 lower bound is specifically a **Multiphase** result, not a black-box lower bound on DAG append labels. G1-B-L1 is a classical-style finite composition; L2 matches the parity-check structure of Hamming codes. No new scientific novelty established; do not start a Rust library from these observations.

**G1-B accepted only when tests and exact PR-head CI pass; G1-C stays OPEN under issue #140.** Next: either (a) compare maintained-state adaptive `P/R_u/W` against known dynamic bit-probe and locally-updatable/decodable codes with fully priced *codebook/preprocessing* and authenticated or adversarial context, looking for a real nonfactorizing result, or (b) **STOP_NOVELTY** if it reduces to classical coding/information bounds. Source canonical import [#147](https://github.com/definitely-stable/Mathlab/issues/147) waits for HYP-105 LIT-205 reservation and is tracked separately.
