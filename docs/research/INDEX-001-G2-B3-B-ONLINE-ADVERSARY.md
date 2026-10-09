# INDEX-001 G2-B3-B — online checkpoint without future restart knowledge

**Frozen model, 2026-10-09.** [Issue #156](https://github.com/definitely-stable/Mathlab/issues/156) · [parent #126](https://github.com/definitely-stable/Mathlab/issues/126) · [offline reference G2-B2-B](INDEX-001-G2-B2-B-CHECKPOINT-POLICY.md) · [generation model G2-B3-A](INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md). **THEOREM ONLY ABOUT THE FROZEN ONE-SLOT FULL-SNAPSHOT / WAL ACCOUNTING MODEL. NOT ORIGINAL AS A GENERAL ONLINE ALGORITHM; SKI-RENTAL/RENT-OR-BUY PRIOR ART OVERLAPS. NO SSD-NAND, HARD POWER LOSS, MULTIWRITER OR RUST API CLAIM.**

## 1. Order of information and admissible instances
- Input: fixed universe N≥1 uint32 blocks, **one-slot** G2-B2-B protocol, S=24+4N application bytes per snapshot, E=28 bytes per nonempty WAL update. U nonempty acknowledged updates. Their intervals and values are revealed to the online policy at step t; they do not change frame sizes in this model.
- At each t, after writing the WAL entry and *before observing the current number r_t of clean recovery/read events*, algorithm chooses whether to checkpoint; after it irrevocably chooses, the adversary reveals any r_t≥0 (or in the finite search r_t∈{0,1,2}). No future restart counts are known. The restart is a read-only observation: it **does not clear or truncate WAL**. This is an **adaptive adversary against deterministic algorithms** when it observes the action and chooses r_t accordingly; exhaustive predetermined r-vectors cover the same deterministic observation/action transcripts.
- Per policy checkpoint tuple C, a_t is WAL age after decision t, snapshot S, entry E. Same exact scalarization as the accepted offline comparator: W=S+EU+S|C|; R=Σ r_t(S+Ea_t); F=Σ(S+Ea_t) byte-steps; J=w_W W+w_R R+w_F F for **nonnegative integer weights** not all zero. Any claim about a competitive ratio in this slice assumes J_off>0, automatically satisfied for nonzero w_W or w_F and U>0; if all weights on recovery but every r_t=0 then both J=0, define ratio 1 by agreement, not 0/0.
- **No max steady WAL-age or peak-path-byte cap in the universal competitive theorem.** Those constraints are modeled and independently tested in G2-B2-B, but imposing them may make the threshold invalid and requires a different theorem. No randomization, predicted restart distribution, varying WAL entry size, cache hit effect, query range-dependent cost, fsync time, device NAND bytes, or multiwriter schedule.

## 2. Reference theorem: simple 2-competitive age threshold (NOT novelty)

Let `T=ceil(S/E)` and checkpoint at update t iff pre-decision WAL age becomes T (i.e. t is a positive multiple of T). Thus `a_t≤T−1` for every t.

For every U≥1, any nonnegative restart sequence, and any nonnegative weights:

1. The online number of checkpoints is `floor(U/T)`, so
   `W_alg = S+EU+S*floor(U/T) ≤ S+2EU ≤ 2*(S+EU) ≤ 2W_opt`, since `S/T ≤E`.
2. `R_alg = Σ r_t(S+Ea_t) ≤ [S+E(T−1)] Σr_t < 2SΣr_t ≤ 2 R_opt`, because `E(T−1)<S`. If no recovery observations, both recovery costs are zero.
3. `F_alg = Σ(S+Ea_t) ≤ [S+E(T−1)]U <2SU ≤2F_opt`.
4. Multiply each coordinate by its nonnegative resource weight and sum: `J_alg ≤2 J_opt`; same weights and horizon for both. No additive constant is needed, but **this bound is only for the full unbounded-cap, fixed-frame reference model**. If U=0, both write the initial snapshot with weights on writing, otherwise zero costs handled explicitly.

The ratio 2 is a **valid coarse upper bound**, NOT asserted optimal for this problem, not a new theorem of online compaction, and no lower bound of 2 is claimed. A finite-horizon enumerator can find strictly smaller ratios for individual N/weights. The proof mainly charges every policy against unavoidable fixed-frame baselines (S+EU, SΣr_t, SU), illustrating a **simple special case of known rent-or-buy / dynamically rebuilt data structure tradeoffs** rather than a source-distinct mathematics breakthrough.

**More general threshold T:** the same component-wise reasoning gives
`J_alg / J_opt ≤ max(1+S/(ET), 1+E(T−1)/S)`, with zero costs interpreted appropriately. The min-over-integer-T certificate may provide a sharper coarse bound, but `T=ceil(S/E)` guarantees at most 2. **No monotonicity of realized ratio with T** is implied.

## 3. Restricted impossibility of perfect deterministic clairvoyance

Fix horizon U=1 with `w_W>0, w_R>0, w_F=0`, and an allowed unbounded r_1 chosen after decision. If online checkpoints, choose r_1=0; offline avoids checkpoint and pays less by w_W*S. If online does not checkpoint, choose any r_1 such that `w_R E r_1 > w_W S`; offline checkpoints and saves more recovery cost than its checkpoint write cost. Therefore every deterministic policy suffers **a strictly positive gap** on at least one input. This **does not prove a 2 lower bound**, nor exclude randomized improvements. It is the standard adversarial rent-or-buy indistinguishability pattern.

## 4. Falsification program, finite search and file-level scope

Implementation `research/index001_online_checkpoint.py`:
- deterministic policies: age threshold `ceil(S/E)`, alternative thresholds 1, 2, T+1, no checkpoint, immediate checkpoint and a previous-restart reactive heuristic (lagging information; NOT predictive);
- at most 3^8 restart vectors r_t∈{0,1,2} for U≤8, explicit exact rational competitive ratios, deterministic tie-breaking and a **separate independent exhaustive offline subset evaluator** on worst witnesses, rather than trusting the DP twice;
- adversary policy `r_t = max_r` when policy did not checkpoint, `r_t=0` when it did, labelled a **greedy witness**, NOT worst-case adversary guarantee;
- varying N∈{1,4,32}, nonnegative weights with at least one positive, zero-restart/hot-restart/bursts, and exact boundary U=T−1/T/T+1; optional filesystem audit using the G2-B2-B returned-byte oracle on selected traces;
- CI reports exact compact JSON or plain-text counts, all source and novelty checks remain enabled.

## 5. Explicit prior-art / novelty decision

This reference upper bound resembles the classical ski-rental deterministic 2-competitive reset decision, and existing general competitive dynamization [LIT-098](catalog/LITERATURE.md#lit-098) already models build/query costs. Our `r_t` are externally observed read counts **after** checkpoint decisions; this differs from a rent/buy price paid before buying and prevents directly importing an optimality/lower-bound proof. The right claim is a narrow self-contained proposition, **not** a universally new `INDEX-001` theorem.

New primary research considered for canonical import (do not duplicate aliases):
- *Prior-Independent and Subgame Optimal Online Algorithms*, ITCS 2026, DOI 10.4230/LIPIcs.ITCS.2026.75: stronger adversarial models and ski rental comparisons, not this index model.
- *Robust and Consistent Ski Rental with Distributional Advice*, ICML 2026 PMLR 306, arXiv 2603.29233: robust prediction techniques, not applicable without a prediction oracle.
- *A new performance metric for the ski rental problem*, Operations Research Letters 2026, DOI 10.1016/j.orl.2025.107382: changes evaluation metric to EoR/RoE, not the deterministic worst-case J_alg/J_opt defined here.
These are **novelty barriers only**. Publisher abstract/venue identity does not mean proofs checked/reproduced.

**Scientific decision:** `RESTRICTED_2_COMPETITIVE_UPPER_BOUND_ELEMENTARY`; `SKI_RENTAL_FAMILY_PRIOR_ART`; `SOURCE_DISTINCT_THEOREM_NOT_ESTABLISHED`; `OFFLINE_DP_BASELINE_ACCEPTED`; `CAP_CONSTRAINED_ONLINE_THEORY_OPEN`; `PHYSICAL_POWER_LOSS_NAND_UNMEASURED`; `RUST_NO_GO`. Further theorem work should target a genuinely range-dependent variable-cost index (where S/E is not fixed and boundary structure/metadata matters), or a formal hard-cap/failed-checkpoint model, instead of claiming novelty for static fixed-frame restarts.
