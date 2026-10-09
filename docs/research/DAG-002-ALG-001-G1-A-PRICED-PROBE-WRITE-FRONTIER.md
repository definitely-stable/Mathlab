# DAG-002 × ALG-001 G1-A — priced local state, remote probes and sparse writes

**Status 2026-10-09:** G1-A MODEL + elementary one-shot counting theorem + restricted covering-code equivalence + explicit external-memory falsifiers. [G1 issue #140](https://github.com/definitely-stable/Mathlab/issues/140). Previous G0 [#138](https://github.com/definitely-stable/Mathlab/pull/138); parallel UCT-005 [#105](https://github.com/definitely-stable/Mathlab/issues/105). **NOT a novel universal theorem / no bounded-error theorem / no Rust.**

## 1. Typed task and resource model — no free data

Let a fixed independent antichain prefix contain `n` vertices, already committed with immutable labels. `append(v,S)` creates one sink with arbitrary incoming parent set `S⊆[n]`; the observable vector of its exact reachability/coordinate queries is `1_S∈{0,1}^n`. The prefix is identical for every `S`; old labels contain **no future knowledge**. This is a **single append from a public, input-independent physical snapshot**, *not* arbitrary maintained-state updates.

New variable local label: `B` bits; mutable global input-dependent manifest: `G` bits; both available to query. Remote mutable storage: `N` publicly addressable cells, each `c>=1` bits. Before append its exact contents `R_0∈([2^c])^N` are independent of `S`. Write budget `W`: **at most W distinct final cells differ from the baseline**, not number of instructions or rewrites. Repeated writes that restore a cell count towards actual physical I/O but not this Hamming-distance budget; G1-A records both quantities separately, and never infers physical byte savings. Each query may adaptively probe at most `P` remote cells and compute arbitrarily; remote source parents or immutable source graph must be included in `N`, not provided for free. Private query randomness, verification, auth bits, crash recovery and adversarial multi-update sequences are **excluded** from the theorems below; reserve independent explicit `V`, trusted-state and soundness dimensions.

The codebook/algorithm is fixed, input-independent and may be arbitrarily large; its own description/preprocessing size `T` must be charged in broader models (we fix it when comparing the `2^n` possible `S` in G1-A). Inputs that limit `S` to a subfamily `𝒮` substitute `|𝒮|` for `2^n`.

## 2. Exact universal single-append write-state counting — ELEMENTARY

Define the number of remote words of `N` cells with at most `W` changed cells relative to one fixed baseline:

```
V_c(N,W) = Σ_{j=0}^{min(W,N)} binom(N,j) (2^c-1)^j.
```

**G1-A-L1, finite injection (elementary/published-style counting):** every deterministic **exact** observer, irrespective of `P`, must satisfy

```
2^(B+G) * V_c(N,W) >= 2^n
B+G >= max(0, ceil(log2 ceil(2^n/V_c(N,W)))).
```

**Proof:** fixed old labels and fixed baseline have no dependence on S. After append, the complete input-dependent accessible state consists of a `(B+G)`-bit local pair and at most `V_c(N,W)` possible remote final states (choose `j` addresses and `j` nonbaseline values). Two distinct S cannot share an identical final local+remote state because their `n` exact coordinate query output vectors differ. Count states. QED.

**Crucial limits:** `P` does not appear; this is a *necessary* injection bound, NOT a joint read/write lower bound, and it is usually far from sufficient when `P` is small. Storing the entire `n`-bit parent row in `N=n,c=1,W=n,B=G=0,P=1` answers exact membership, falsifying unrestricted `B+G>=n`. Conversely, `N=0` or `W=0` reduces to G0. For general codebooks, changed remote addresses can encode information, so `W*c` is **not** an upper bound on the written information; the combinatorial choice of addresses is charged by `binom(N,j)`. This simple Hamming-ball injection is classical and **not a new dynamic cell-probe theorem**.

### One-shot vs maintained-state distinction

The above W is **net changed cells compared to a fixed public snapshot**, not update writes between two dependent states `S_t,S_{t+1}`. If both target encodings are at most `W` from baseline, their mutual Hamming distance can reach `2W` (and a real implementation can make even more intermediate writes). Switching cached centers may change all local label bits too. Thus no amortized, persistent or crash-safe write guarantee follows. In particular, a direct-source bit array has one-probe reads but may require n changes on one arbitrary append; subsequent one-bit flips cost one changed remote bit.

## 3. Restricted, sharp **covering-code equivalence** (NOT universal)

We now freeze a much narrower **public coordinate-addressed XOR-delta** family: `N=n`, `c=1`, `P=1`; each logical coordinate i always reads remote cell i exactly once. Its final value is `D_i` where at most W bits of `D` differ from the all-zero baseline. The local label selects one of `K` public bit-vector *centers* `C_l∈{0,1}^n`, and decoder returns `C_l[i] XOR D_i`; all cells are in the priced remote store. **No address-dependent query routing, shared remote broadcast, or arbitrary decoder.**

**G1-A-L2 (known covering-code equivalence):** all `2^n` masks can be represented with at most `W` net remote writes iff the codebook of centers has Hamming covering radius `≤W`. Hence the minimum **number of local codebook choices** is `K(n,W)`, the classical binary covering-code number; fixed-width local bits `B>=ceil(log2 K(n,W))`. The classical volume bound `K(n,W)>=ceil(2^n / Σ_{j≤W}binom(n,j))` is necessary, and not always sufficient for the exact number of centers.

**Proof:** for given S, `S=C_l XOR D`. `wt(D)=d_H(S,C_l)≤W` iff S is covered by center `C_l`. Taking all S is exactly a covering code. QED. This equivalence is **an algebraic rewriting of known covering-code definitions**. See Cohen–Lobstein–Sloane, *Further Results on the Covering Radius of Codes* (IEEE Trans. IT 1986), [DOI 10.1109/TIT.1986.1057227](https://doi.org/10.1109/TIT.1986.1057227), author abstract [Lobstein](https://www.lri.fr/~lobstein/resumeFurther.html). The source's `K(n,R)` terminology predates this Mathlab construction.

**Countermodel against universal K(n,W) inference:** if many coordinate queries may read the **same** remote cell, one changed cell can flip all n query outputs at once, e.g. `Q_i=R[0]` for every i. That violates per-coordinate Hamming radius W while respecting one remote probe per query. General deterministic one-probe schemes may adapt addresses to local labels and have different state geometry; **covering code optimality is not established for them**.

## 4. ALG-001 source and model boundaries

The nonzero binary row `A_S=[1_S]` has rank exactly one for every `S≠∅`, but coordinate queries still distinguish `2^n−1` cases. G1-A-L1 on this promised family replaces RHS `2^n` with `2^n−1`; `S=∅` is omitted. Rank-only output is identically one and needs no variable state under the promise. A row-family replacement is not a *single-entry* update and does not conflict with [LIT-195 dynamic rank ICALP 2026](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) `Õ(r^1.405)` arithmetic per-entry update bound. No graph reachability theorem is imported by rank analogy.

## 5. Mathematical prior art and novelty closure

| Work | Authentic target | What **cannot** transfer |
| --- | --- | --- |
| [LIT-187 SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9) | Immutable append-only chain-top DAG reachability indexes | First-fit chain heuristic ⇒ optimal width or authenticated storage |
| [LIT-195 ICALP 2026](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) | Dynamic matrix rank/basis/matching update arithmetic | Constant rank ⇒ constant coordinate-observation state |
| [Fredman–Saks STOC 1989](https://doi.org/10.1145/73007.73040), [Pătraşcu–Demaine SICOMP 2006](https://doi.org/10.1137/S0097539705447256) | Dynamic cell-probe lower bounds for *specific* update/query languages | Lower bound on an unrestricted single append with 1-bit one-probe index |
| [E. Viola, *Bit-Probe Lower Bounds for Succinct Data Structures* SICOMP 2012](https://doi.org/10.1137/090766619) | Redundancy/probe tradeoffs for nonbinary arrays, fixed-cardinality membership | Binary full-cube membership direct array with n bits has P=1 and no redundancy; do not infer extra Ω(n) |
| [Cohen–Lobstein–Sloane IEEE IT 1986](https://doi.org/10.1109/TIT.1986.1057227) | Covering-code minimal K(n,R) and sphere bounds | New theorem claim for fixed center + sparse XOR delta |
| [Young Kun Ko, ECCC TR26-047 (2026)](https://eccc.weizmann.ac.il/report/2026/047/) ([arXiv:2603.25914](https://arxiv.org/abs/2603.25914)) | Unconditional Ω((log n/loglog n)^2) dynamic Boolean **Multiphase** cell-probe lower bound by 2.5-round communication with verification | Arbitrary reachability/coordinate membership, DAG append-only updates or universally charged cryptographic verification. 2026 author report/FOCS accepted listing, **not** full independent proof replay |

**Primary-source diligence:** Existing LIT identity IDs cited where cataloged; the two source identities for Cohen 1986 and Ko 2026 are included here with canonical DOI/arXiv identifiers but **not assigned a free LIT slot pending collision-safe global catalog import** (parallel HYP-105 PR #132 plans LIT-205). No copied paper text and no claims of independent verification of proofs.

## 6. Independent finite falsifiers (stdlib only)

- Exhaustive `(N,c,W)` remote snapshot enumerator (binary and 2-bit cells) verifies exact `V_c(N,W)` for `N≤4`, incl. `W=0`, `N=0`, input-invalid rejection.
- Full exact brute-force covering center set search for `n≤4` versus an **independent** over-all-subsets oracle; known illustrative `K(3,1)=2, K(4,1)=4` checked without trusting cached paper numbers.
- End-to-end all-mask encoder/decoder for `n≤4`, one remote bit-probe/query, center-label bits and at most W net writes, verified against a separate coordinate bit oracle.
- Counterexample source-array `P=1,B=G=0,W=n`, broadcast one-cell flipping all query outcomes with W=1, exact `d=1` fixed-subset model `ceil(log₂n)` local bits; shared-cell broadcast falsifies untyped Hamming-ball transfer.
- Model boundary: for consecutive masks `01→10` with same center `00` and W=1 relative to baseline, physical transition requires **two** changed cells; W is not per-update recourse.
- All tests mathematical/finite, **not benchmarked I/O or independently checked Ko proof**.

## 7. G1-B novelty gate and next valid action

`G1-A ACCEPT_MODEL` iff GitHub-hosted exact HEAD CI passes and the independent snapshot and decoding oracles agree. **Nonfactorizing theorem: NOT PROVED; COVERING-CODE TRANSFER: KNOWN.** G1-B must (a) specify truly adaptive `P`, multi-round maintained writes and a fully charged accessible remote state, (b) compare to modern dynamic Boolean Multiphase/communication lower bounds, and (c) find a strict theorem that cannot be reduced to Hamming covering or classical counting. If this is merely `K(n,W)` rebranding, record **STOP_NOVELTY** and prefer a narrower, verifiable algorithmic result. No Rust/prod.

