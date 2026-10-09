# INDEX-001 G2-B4-A — canonical variable-size binary range checkpoints

**Protocol frozen 2026-10-09; issue [#173](https://github.com/definitely-stable/Mathlab/issues/173), parent [#126](https://github.com/definitely-stable/Mathlab/issues/126).** Follows [G0](INDEX-001-G0-RANGE-MAP-FOUNDATION.md) and the [constant-snapshot 2-bound](INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md). The earlier guarantee must **not** be transferred without proving its assumptions. This is a mathematical byte-accounting model and Python oracle, not a durable implementation, SSD measurement, physical page lower bound, or production API.

## G0. Canonical exact storage model

- Universe N>=1; binary latest-write-wins state f_t of length N, initial f_0=0^N. A nonempty update u_t=(l_t,r_t,v_t) assigns a half-open range, 0<=l<r<=N and v in {0,1}. The number k_t of maximal homogeneous runs varies. Every operation is acknowledged; clean restarts only *read* state.
- Exact **snapshot on disk**: four ASCII bytes IXR1, canonical unsigned base-128 varint for N, canonical varint for k, each run encoded as unsigned positive length varint followed by a single byte 0/1; CRC32 little-endian four bytes. The first run starts at zero, all runs alternate symbols, lengths sum to N, no unused suffix. This is not a succinct-entropy-optimal format and has no lookup index.
- The exact application byte length is S_t = 8 + len(uvar(N)) + len(uvar(k_t)) + sum_{j=1..k_t}[len(uvar(L_{t,j}))+1]. The eight bytes are magic and CRC. For N<=8, S_t=10+2k_t.
- Exact **WAL frame**: two ASCII bytes RW, canonical unsigned varint for l, canonical varint for r, one binary value byte, CRC32 little-endian four bytes: E_t = 7 + len(uvar(l_t)) + len(uvar(r_t)). For endpoints <=127, E_t=9. CRC validation, canonical encoding, and interval validation have independent tests; this stage does not implement POSIX atomic commit.
- Bytes in memory (expanded dense state), serialized file bytes, bytes handed to a hypothetical write, retained dead versions, and pages/NAND programmed are different resources. Encoding time, indirections, fsync, metadata journals, partial torn frames and garbage collection **are not** priced in this initial slice.

For checkpoints C subset of {1,..,U}, let c(t)=max({0} union (C intersect [1,t])) and A_t=sum_{i=c(t)+1..t} E_i. The initial snapshot is S_0; every update always appends its frame, including when a checkpoint follows it.

- **W(C)** = S_0 + sum_{t=1..U} E_t + sum_{t in C} S_t (serialized bytes written, not NAND).
- **R(C)** = sum_{t=1..U} r_t [S_{c(t)} + A_t] (clean-restart bytes read).
- **F(C)** = sum_{t=1..U} [S_{c(t)} + A_t] (steady on-disk byte-steps, not RAM).
- **P(C)** = maximum over initial S_0, each post-decision steady footprint, and for every t in C the transient **old** snapshot S_{c(t-1)} + all WAL bytes since that checkpoint including E_t + **new** S_t. This is a staged-path byte bound, not allocator or NAND occupancy.
- J(C)=w_W W(C)+w_R R(C)+w_F F(C) for nonnegative integer weights not all zero. No peak/age caps, no failed checkpoints or concurrent writers in this result. Checkpoint choice is made after receiving update t but **before** observing r_t. Offline knows the entire sequence of updates and restarts and may checkpoint at any t.

Online policy tested here: checkpoint immediately after update t if accumulated WAL bytes since the last checkpoint (including E_t) are at least the **current** compressed snapshot size S_t. This is a natural but naive variable-size extension of G2-B3-B. There is no assertion that this policy is best possible.

## G1. Exact falsification of the unchanged competitive ratio 2

N=6, f_0=000000; updates in order:

| t | assign(l,r,v) | state | k_t | S_t | E_t | checkpoint by naive online |
|---|---|---|---:|---:|---:|---|
| 0 | — | 000000 | 1 | 12 | — | initial |
| 1 | (1,2,1) | 010000 | 3 | 16 | 9 | no (9 < 16) |
| 2 | (3,4,1) | 010100 | 5 | 20 | 9 | no (18 < 20) |
| 3 | (5,6,1) | 010101 | 6 | 22 | 9 | yes (27 >= 22) |
| 4 | (0,6,0) | 000000 | 1 | 12 | 9 | no (9 < 12) |

Set r_1=r_2=r_3=0, r_4=1, weights (w_W,w_R,w_F)=(0,1,0). Immediately after t=4, the online policy **still holds snapshot S_3=22 plus E_4=9**, so R_online=31. The offline optimizer checkpoints at t=4 and reads S_4=12, so R_offline=12. Thus **J_online/J_offline=31/12 > 2**, a concrete four-update counterexample. Both independent subset enumeration and a DP indexed by the last checkpoint confirm the optimum. No hardware or asymptotic impossibility is inferred.

The gap can also persist with strictly positive write and read weights if r_4 is large enough. This falsifies *only* the proposed naive S_t threshold policy under this exact serialized-variable model; it does not prove that **every** online algorithm exceeds factor 2.

## Restricted theorem: a valid coarse parameter-dependent upper bound

Let S_min=min_{0<=t<=U} S_t>0, S_max=max_{0<=t<=U} S_t, kappa=S_max/S_min>=1. For this online policy, without caps, and **any** update sequence, nonnegative r_t and resource weights,

**J_online <= 2 kappa J_offline**,

with zero-zero objective interpreted as equal cost (ratio 1). Proof:

1. At each online checkpoint at t, the actual checkpoint bytes S_t are <= the pending WAL bytes since its previous checkpoint. Checkpoint intervals are disjoint, hence sum_{t in C_online} S_t <= sum_{t=1..U} E_t. Therefore W_online <= S_0 + 2 sum E_t <= 2 W_offline.
2. At a step with **no** online checkpoint, the saved snapshot is at most S_max, while the pending WAL bytes are **strictly less than** the current S_t <= S_max. Thus the steady footprint is <2 S_max. When it does checkpoint, the steady footprint is S_t <= S_max. Any offline schedule has steady footprint >= S_min. Summing after multiplying each step by r_t>=0 gives R_online <= 2 kappa R_offline, and summing unweighted steps gives F_online <= 2 kappa F_offline.
3. Multiply the three coordinate inequalities by their corresponding nonnegative weights. Since kappa>=1, the stated inequality follows.

This proof supplies only an instance-specific **coarse upper bound**, not a tight competitive ratio or novel fundamental theorem. A factor expressed using kappa may degrade with N and the encoding. The result cannot be generalized to hard peak caps, unconstrained cache/query costs, physical relocation, compact auxiliary metadata or arbitrary external data structures. The independent finite oracle is a falsifier, not an all-N proof.

## Verification scope and the next gate

Implemented: exhaustive serialization of every binary map for N<=8, independently checked count 2*C(N-1,k-1); CRC/truncation/canonical-varint checks; WAL varint boundaries; independent dense/run oracles; offline DP versus all checkpoint subsets for **the full assignment alphabet N<=3, U<=3 and restart counts {0,2}**, two resource-weight tuples; seeded additional traces N<=6, U=5; exact four-update witness. All tests run in GitHub-hosted Research workflow. The full N<=6, U<=5 cross-product of **all** assignments and r_t in {0,1,2} is **not** claimed exhausted; it is significantly larger and should be reduced by proved state-equivalence classes or split into checkpointable CI shards before calling it complete.

**G2 remains open:** define physical contiguous packed-file recourse, page size, metadata/RAM bounds, allowed reallocation/slack, update and scan page probes, and crash recovery. Without those quantifiers, a statement that succinctness *forces* nonlocal rewrites is false for alternative indirection/buffering implementations. A narrowly restricted contiguous layout could be studied separately, clearly not as a universal bound. Compare formally to already pinned dynamic succinct dictionaries, bitvectors, online dynamization and RASK/LSM rather than claiming a source-distinct theorem now.

### Two newly checked 2026 primary sources — novelty barriers

1. **arXiv:2603.23119** — Gabriel Marques Domingues, *Compressing Dynamic Fully Indexable Dictionaries in Word-RAM* (2026; author record states to appear STOC 2026), https://arxiv.org/abs/2603.23119 . Dynamic rank/select and single-bit modification using space close to combinatorial entropy; **not** a durable range-assignment checkpoint theorem. Verification: primary arXiv abstract/metadata checked 2026-10-09; paper's proof not independently checked.
2. **arXiv:2604.24080** — Takaaki Nishimoto and Yasuo Tabei, *Dynamic Grammar-Compressed Self-Index in δ-Optimal Space* (arXiv v3, 2026), https://arxiv.org/abs/2604.24080 . Dynamic compressed self-index with insert/delete and locate, **not** overwrite-range WAL or physical compaction. Verification: primary arXiv abstract/metadata checked 2026-10-09; proof/benchmarks not independently reproduced.

Dedup check against main repository search performed by arXiv identifiers: neither was found before this slice. Both are **imported as canonical LIT-212/LIT-213** in the generated [LITERATURE.md](catalog/LITERATURE.md) and [LITERATURE-BY-RESEARCH.md](catalog/LITERATURE-BY-RESEARCH.md), pinned to this document's reachable authoring commit, with title and identity checks. Bibliographic verification is not proof verification. Existing relevant canonical anchors: LIT-175 RASK, LIT-098 competitive dynamization, LIT-177/179/180/181 dynamic succinct structures, LIT-182/185/186 LSM and range storage. Their model assumptions remain distinct.

**Scientific decision:** EXACT_VARIABLE_RLE_MODEL_FROZEN; NAIVE_2_TRANSFER_FALSIFIED_BY_WITNESS; COARSE_2_KAPPA_BOUND_PROVED_IN_FROZEN_MODEL; GENERAL_LOCALITY_COMPRESSION_RECOURSE_THEOREM_NOT_PROVED; PHYSICAL_STORAGE_NONCLAIM; RUST_NO_GO.
