# TOM-005: seven cross-domain theorem candidates — all seven proof targets

Date: 2026-10-08. Issue [#59](https://github.com/definitely-stable/Mathlab/issues/59).
Status: SELF-CONTAINED SEVEN-CLAIM PROOF DRAFT / HOSTED CI PENDING.
Originality: **NOT ESTABLISHED**. Formal Lean proof: **NOT ATTEMPTED**.
Read the [33 already-known/STOP records](KNOWN-AND-STOPPED-RESEARCH.md) first.

## Contract: stages 1, 2, 3 performed for ALL seven candidates

1. Search across independent problem families, not seven IBLT sketches.
2. Freeze operation, strongest known comparable model, counted resource,
   important exclusions, and exact claim before looking at toy results.
3. Supply a mathematical derivation AND separately enumerated finite oracle
   for ALL seven candidates. A finite oracle is regression evidence,
   not a replacement for the universally quantified proof.

Statuses: DERIVED_CLASSICAL = proved locally but based on standard old mathematics.
MODEL_COUNTEREXAMPLE = attractive stronger statement false under changed assumptions.
OPEN_NOVELTY = sharper product/model-specific theorem NOT proved here.
A source URL is a primary-anchor entry point, not proof of exhaustive coverage.

## Source-to-model and product screening

| ID | Product operation | Source and strongest model overlap | Distinct computational resource | Decision |
| --- | --- | --- | --- | --- |
| A | Certified cheapest codec/base trial | Standard branch-bound; [Finesse FAST19](https://www.usenix.org/conference/fast19/presentation/zhang) is retrieval comparator, not the certificate theorem | Paid encoder trials and independent per-candidate lower bounds | CLASSICAL; novel useful codec bound OPEN |
| B | Pareto-prune whole patch choices | Classical multiobjective dominance; [Palantir ASPLOS24](https://doi.org/10.1145/3620665.3640353) is a nearby codec filtering comparator | Exact vector of full patch bytes, CPU and memory | CLASSICAL |
| C | Multi-segment base switching optimization | [Bellman 1958 routing theorem](https://doi.org/10.1090/qam/102435) | Full optimal route under local cost + switching | CLASSICAL |
| D | Expected-optimal fail-fast test order | [Garey 1973](https://doi.org/10.1016/0012-365X(73)90113-1), [independent-test theorem 2013](https://doi.org/10.1016/j.dam.2013.07.014) | Expected verifier CPU under independent rejects | CLASSICAL |
| E | Durable immutable generation root publication | Classical CoW/shadow paging; [Stanford crash-consistency project](https://www.scs.stanford.edu/21sp-cs111/proj/proj_log.html) | Flush/durable atomic commit, crash-prefix | CLASSICAL |
| F | Collision-free exact fixed-bit range identity | Elementary injective counting; [Aljoscha Meyer range reconciliation](https://github.com/AljoschaMeyer/set-reconciliation) is probabilistic-hash application | Independent bits stored for N exact distinct states | CLASSICAL |
| G | Eager exact DAG output change cost | [Ramalingam 1993](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/), [ECOOP 2025](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20) | Materialized cell writes for downstream outputs | CLASSICAL |

These are *distinct workloads*. Do not infer the source cited proves our exact statement
under identical assumptions; each proof below is given explicitly. No novel theorem,
Rust crate, global theory completeness or comparative speedup is claimed.

## A. Necessary and sufficient stop certificate

Frozen model: n independent candidate true integer costs x_i in inclusive intervals
[L_i,U_i]. Nonempty subset E has been evaluated exactly; return an E-member with
cost b=min(x_i for i in E). All unknown in-range assignments are independently
possible. No extra cross-candidate constraints are assumed.

**THEOREM A:** The returned evaluated candidate is guaranteed globally minimum for
every completion of unknown costs if and only if L_j >= b for every untested j.

**Proof.** For sufficiency, x_j >= L_j >= b for every unknown, and all known
costs are >=b. For necessity, if one L_j < b, choose x_j=L_j and any allowed
values for other unknowns. Then this competitor strictly beats every evaluated
candidate. Ties are valid. Both directions use independent feasible intervals. QED.

**Kill condition:** when unmeasured costs have hard dependencies, setting x_j=L_j
may contradict observed costs; necessity no longer follows. An actual DELSK use
needs a useful cheaply computable admissible lower bound on encoded bytes.
Classical optimality certificate, not a research discovery.

## B. Dominance preserves independent complete-choice minima

Frozen model: vectors v_1,...,v_n with k nonnegative cost coordinates.
The objective F is coordinatewise nondecreasing and depends only on the
single complete candidate. Candidate a is dominated if some retained
candidate b has v_b<=v_a in every coordinate, or is an equal-cost representative.

**THEOREM B:** Removing dominated candidates does not alter min_i F(v_i).

**Proof.** Monotonicity implies F(v_b)<=F(v_a). Replace any deleted minimizer
by its dominating representative; finite chains terminate at an undominated
vector (ties resolved by index). The minimum value is unchanged. QED.

**Kill condition:** nonmonotone F(v)=-sum(v) prefers (2,2) to (1,1), yet the
naive pruning removes (2,2). Segment-level pruning is also invalid if cost
includes transitions to adjacent segments or setup sharing. Pareto 101, NOT novel.

## C. Global segment routing with a switching charge

Frozen model: T>=1 segments, K>=1 fixed candidate bases, local cost c[t,j]>=0,
constant penalty lambda>=0 for changing the base between adjacent segments.
The total is sum_t c[t,j_t] + lambda*sum_{t>=1} I[j_t != j_(t-1)].

**THEOREM C:** Define D[0,j]=c[0,j] and
D[t,j]=c[t,j] + min_i (D[t-1,i]+lambda*I[i!=j]).
Then min_j D[T-1,j] is the global route optimum.
Cost O(T*K*K) time, O(K) auxiliary space for value only.

**Proof.** Every path ending in j has unique last predecessor i and cost
equal to its prefix cost plus last transition and local segment contribution.
Induct on t and take the minimum over i. Appending j to an optimal predecessor
attains the recurrence, and min over terminal j attains the global optimum. QED.

**Counterexample to greedy:** c=((0,1),(1,0)), lambda=3: local greedy
changes 0 to 1 and pays 3, while staying at 0 costs 1. Global shared
dictionaries break the Markov state assumption and require a different model.
Classical Bellman/Viterbi result, NOT novel.

## D. Optimal ordering of independent fail-fast tests

Frozen model: tests i have deterministic cost c_i>=0 and independent terminal
reject event of probability p_i in [0,1]. After first reject no more tests run.
All tests are otherwise required; reject semantics cannot be wrong.
Expected cost in order pi is sum_t c[pi_t]*product_{s<t}(1-p[pi_s]).

**THEOREM D:** The minimum expected cost ordering is nonincreasing p_i/c_i
for c_i>0; zero-cost tests may be placed first; ratio ties arbitrary.

**Proof.** Holding a common preceding survival Q and identical later suffix,
expected costs of a then b and b then a differ by
Q * (c_a*p_b - c_b*p_a). Thus a precedes b precisely when
p_a/c_a >= p_b/c_b for positive costs. Repeated adjacent inversion swaps
reach a sorted optimal ordering. Zero-cost tests can move earlier without
increasing expectation. QED.

**Kill condition:** conditional/correlated rejection rates, shared work and
false rejects do not satisfy the model. Garey 1973 and the 2013 independent
testing result are direct prior-art; no claimed new ordering theorem.

## E. Commit safety of a durable immutable root switch

Frozen abstract machine: old immutable generation/root already durable;
new bytes prepared separately; a successful flush makes all referenced new
bytes durable; durable atomic root publication updates the only recovery
root; a crash occurs at an action boundary and discards non-durable bytes.
The old committed bytes remain untouched.

**THEOREM E:** prepare -> durable_flush -> atomic_publish yields old or complete
new generation after EVERY crash-prefix in this abstract machine.

**Proof.** Before the atomic publish step the durable root still references
the immutable complete old generation. After publish it references a fully
persisted new generation, because flush preceded the root switch. An atomic
pointer switch has no intermediate/root-torn state. Every prefix satisfies the
invariant. QED.

**Counterexample:** prepare -> publish -> flush, crash just after publish:
root can reference unflushed/unavailable data. This toy theorem does NOT prove
real filesystem fsync, cache flush, NVMe write-order, multiwriter or GC safety.
This is classical CoW/shadow paging, not a new crash protocol.

## F. Pigeonhole limit of a deterministic exact fingerprint

Frozen model: N>=1 distinguishable input states, exactly b>=0 retained bits,
no side information, input probes, interaction or external membership structure,
and absolute (not probabilistic/cryptographic) exactness.

**THEOREM F:** A deterministic perfectly distinguishing mapping exists
iff 2^b>=N, equivalently b>=ceil(log2 N).

**Proof.** Perfect distinction requires an injection from N input states into
2^b possible bit strings; pigeonhole proves the necessity. If the inequality
holds, enumerate the N inputs and use their unique b-bit ordinal encoding,
proving existence (not efficient construction). QED.

**Kill condition:** cryptographic hash binding, allowed collisions with
probability delta, auxiliary persistent data and source probes change the model.
Do not claim short practical SHA fingerprints are mathematically injective,
or that this theorem provides a feasible collision attack. Classical counting.

## G. Eager materialized output fanout lower bound

Frozen model: one Boolean input x and n independently materialized output
cells y_j = x AND 1, required correct after every input update. A cell write
can modify only one independently stored output location and its cost is 1.
Update x from 0 to 1.

**THEOREM G:** Exactly n output-cell writes are necessary and sufficient
for this update.

**Proof.** Each distinct materialized output cell must change from 0 to 1;
at least one write to each of n locations is necessary. Writing each once
suffices. QED.

**Kill condition:** if outputs are lazy or share a single reference to x, one
source modification is sufficient until outputs are queried. Hence no general
Omega(n) update-time bound is proved for lazy incremental computation.
The lower bound concerns explicit output materialization only.

## Independent executable falsification plan for ALL seven

- A: enumerate independent interval completions and verify iff outcome.
- B: enumerate vector sets and positive monotone objectives; adversarial
  nonmonotone counterexample.
- C: brute-force all K-ary routes and switch penalties; greedy counterexample.
- D: enumerate all test permutations with exact rational probabilities.
- E: enumerate all 6 action orders and 4 crash cuts; publish-before-flush fails.
- F: enumerate *all* small maps of N states to 2^b codewords.
- G: enumerate all concrete eager output vectors, compare changed cell count.

[Pure model kernels](../../research/tom005_models.py) and
[independent enumeration tests](../../research/test_tom005_models.py)
run on GitHub-hosted CI. Exhaustive finite cases TEST the mathematical model,
not the universal proof by themselves.

## Research verdict / next genuinely hard question

All seven narrow statements have complete human-readable deductive proofs in
this file and are classified **DERIVED_CLASSICAL**, not original discoveries.
Their independently tested small cases require a passing merged-head CI gate.
No Lean kernel formalization or new Rust product is authorized.

The single best *conditional product + research extension* is A:
a genuinely cheap, codec-aware, ADMISSIBLE and usefully tight base-specific
lower bound for encoded patch size under a precisely frozen encoder and fixed
resource budget. This bound is **NOT constructed or proved** here. If impossible
or already known after paper-level search, reject without a new crate.
A second conditional extension is C with global shared dictionary state, where
the simple Bellman recurrence ceases to model full costs. Both require first
demonstrating a *source-level* gap beyond published optimization work.

**Scientific status:** 7 of 7 baseline theorems self-contained PROVED;
0 of 7 novel theorem claims certified; no fabricated original theorem.
