# INDEX-001 G2-B2-B — checkpoint lifecycle and fully priced *reference-model* policy oracle

**Scope frozen 2026-10-09.** [Issue #143](https://github.com/definitely-stable/Mathlab/issues/143) · [G2-B parent #126](https://github.com/definitely-stable/Mathlab/issues/126) · [root #117](https://github.com/definitely-stable/Mathlab/issues/117). Based on G2-B0/B1 [durable protocol](INDEX-001-G2-B0-DURABILITY-PROTOCOL.md) and G2-B2-A [application-IO accounting](INDEX-001-G2-B2-A-APPLICATION-IO.md). **Research-only / offline clairvoyance / no new theorem / no NAND or performance claim / no Rust.**

## 1. Frozen operations and timeline

Fixed universe N>=1 of uint32 symbols and successful latest-write-wins `assign(l,r,value)` on half-open ranges. Every update in this slice is nonempty and acknowledged. All filesystem operations succeed except separately tagged failure experiments, and there is *one writer*. Entire snapshot length `S=24+4N` bytes and complete CRC WAL frame length `E=28` bytes. A history contains U updates. A **checkpoint policy** is a set `C⊆{1,..,U}`; checkpoint after update t and before recovery checks associated with t. `r_t∈Z_>=0` denotes a count of independent **clean reopen/read observations** after update t. A clean observation reconstructs state from snapshot and WAL and is **not** a crash or device power failure; observations do not mutate files or erase WAL.

Set `c(t)=max((C∩{1,..,t})∪{0})` and `a_t=t-c(t)` WAL records remaining at the instant immediately after the checkpoint decision. Before an optional checkpoint at t, the old committed snapshot and the just-appended WAL coexist with `g_t=t-c(t-1)` complete records. The filesystem lifecycle at checkpoint is: create temp image S -> fsync -> rename -> fsync directory -> WAL truncate/fsync. A coherent clean checkpoint finishes with one snapshot and zero WAL records.

## 2. Explicit and exactly derivable cost vector (not new)

For this *fixed frame reference*, absent failures/retries/reopen writes:

```
W(C) = S + E*U + S*|C|                             application bytes returned by os.write
R(C) = Σ[t=1..U] r_t * (S + E*a_t)                 bytes returned by clean-restart Path.read_bytes
F(C) = Σ[t=1..U] (S + E*a_t)                       post-decision steady-file bytes × update steps
P(C) = max( S, max_t(S+E*a_t),
            max_{t∈C}(2*S + E*g_t))               maximum temporary+snapshot+WAL visible path bytes
L(C) = max_t a_t                                  maximum steady retained WAL record count
```

Each coordinate is distinct: `F` is byte-steps (a discrete integral of point-in-time footprint), **not** disk bytes written. `P` counts both snapshot and temporary file while compaction is staged. Truncation, fsync, directory metadata activity and physical SSD/NAND pages are **not priced** by W or R; report invocation counts separately. `P` is tested only at instrumentable filesystem stages for selected faults, not a promise about transient inode/page-cache blocks.

Weights `w_W,w_R,w_F ∈ Z_>=0` give scalarized offline policy objective `J=w_W*W+w_R*R+w_F*F`. This deliberately unit-converts byte counts and byte-steps through policy weights; results at different weights cannot be compared as unweighted bytes or throughput. One optional hard constraint `L(C)≤A` restricts **steady** WAL record age only, not the one-update transient WAL present during checkpoint. A second optional budget on `P` is allowed and includes the checkpoint temporary coexistence. Both budgets are exact in this model.

## 3. Finite offline optimizer and independent oracle

An offline dynamic program processes t=1..U and stores the least weighted objective by **steady age** a_t, recording the lexicographically least checkpoint tuple on ties. No-checkpoint increases age by 1; checkpoint resets age to 0 and costs S write bytes. At time t, the per-step variable contribution is `(w_R*E*r_t+w_F*E)*a_t`, plus `w_W*S` for checkpoint. Shared constant
`w_W*(S+E*U)+w_R*S*Σr_t+w_F*S*U`
is added only at the end. The state is sufficient because all future costs depend on history only through current WAL age; peak/steady caps are checked on transitions. A future-time clairvoyant DP solves the **frozen scalar reference objective exactly**, not a competitive online algorithm for unknown workloads.

**Proof by induction:** a state `(t,a_t)` captures all future-dependent information; every valid policy prefix arrives via either prior age `a_t-1` without checkpoint or any prior age with checkpoint. Additive costs and optional per-transition caps preserve optimal substructure. Taking minimum and deterministic tie-break at each state retains an optimal prefix. At t=U the minimum over ages plus the shared constant is globally optimal. An independent exhaustive enumerator checks every subset C for small U, including multiple restarts per t and both caps; it does **not** reuse DP recurrence.

## 4. Adversarial and novelty gates

- Without recovery checks, byte-step penalty, or age cap (`r_t=w_F=0` and `w_W>0`), **any checkpoint strictly increases J**. This is an elementary reference-model observation, not an original theorem or recommendation to never compact in production.
- If r_t has a burst, an offline oracle can checkpoint before that burst, while a fixed periodic threshold may incur excess WAL recovery reads. This is **clairvoyance advantage**, not a new universal online lower bound.
- Comparing policies must report **the full vector (W,R,F,P,L)**, not merely a scalar objective. A policy optimizing one weight setting is not unconditionally optimal for another.
- Logical assigned blocks and canonical run boundaries do not determine durable checkpoint bytes: this baseline writes a full N-cell image regardless of fragment count.
- Version/compaction prior art already indexed: [LIT-098 competitive dynamization](catalog/LITERATURE.md#lit-098), [LIT-175 RASK](catalog/LITERATURE.md#lit-175), [LIT-176 HATS](catalog/LITERATURE.md#lit-176), [LIT-182 Moose/Smoose](catalog/LITERATURE.md#lit-182), [LIT-184 C2LSM](catalog/LITERATURE.md#lit-184), [LIT-185 ArceKV](catalog/LITERATURE.md#lit-185), [LIT-186 RangeReduce](catalog/LITERATURE.md#lit-186). These sources do not imply online optimality for this exact range overwrite API, and an offline DP is not a novel contribution by itself.

## 5. Acceptance and limits

- The independent dense-value oracle verifies exact lookup/scan after every acknowledged operation and after clean reopen; actual returned filesystem bytes, `stat().st_size`, checkpoint count and WAL read bytes must equal the algebraic ledger.
- A separate fault experiment checks sizes of orphan `snapshot.tmp` after interrupted checkpoint and correct recovery from the old snapshot + valid WAL. The stale temporary file is **not** reclaimed automatically by current reference; crash aftermath is outside clean-life formulas W,R,F,P.
- Exhaustive small-U policies (including zero updates, no restarts, multiple restarts at t, hard caps, tied costs) match DP exactly, independent of filesystem implementation.
- Deterministic report, no randomness, no local self-hosted runners. Run `python research/index001_checkpoint_policy.py` and `python -m unittest discover -s research -p "test_index001_checkpoint_policy.py"`, then entire hosted Research workflow on exact PR head.
- No new external bibliography identity was introduced just to rename a known theorem. Any *genuinely missing and primary-verified* future source gets a unique catalog identity and must be merged to `main`; do not duplicate arXiv/publisher versions.

**Decision gate:** `EXACT_REFERENCE_POLICY_DP_OPEN_UNTIL_HOSTED_CI`; `PERSISTENCE_SCOPE_ONE_WRITER_POSIX`; `NOVELTY_NOT_ESTABLISHED`; `PHYSICAL_NAND_UNMEASURED`; `PRODUCTION_RUST_NO_GO`. Follow-on G2-B3: multi-generation crash atomicity, proof of checkpoint commit semantics under weaker device guarantees, multiwriter fencing, and a same-model online adversary.
