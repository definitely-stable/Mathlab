# UCT-004 G2-A — source statement audit, novelty barrier and fully priced boundaries

**Date:** 2026-10-09. **Issue #87**; mathematical proof [sound-witness packing](UCT-004-G2-A-SOUND-WITNESS-PACKING.md). **Evidence level:** original publisher/institution/author abstract + Mathlab self-contained restricted lemmas. NO full original-source proof independently reproduced. No universal originality claim.

## 1. Critical primary works and why a broad "new" claim would be misleading

| Canonical or proposed source | Original result, as claimed in publisher/author material | Impact on UCT-004 |
|---|---|---|
| **LIT-114** Pătraşcu & Tarniţă, *On Dynamic Bit-Probe Complexity*, TCS 380 (2007), DOI [10.1016/j.tcs.2007.02.058](https://doi.org/10.1016/j.tcs.2007.02.058) | Publisher/Princeton abstract explicitly reports lower bound `Ω(log n / log log log n)` for maintaining partial sums over Z/2Z, among bit-probe and chronogram results. | Severe same-problem prior-art barrier; source bit-probe *accesses* vs our physically *changed* stored bits, worst-case vs amortization, read-only vs write-and-query cost must be normalized before theorem comparison. |
| **LIT-111/112** Fredman–Saks (1989); Pătraşcu–Demaine (2006), DOI 10.1145/73007.73040 / 10.1137/S0097539705447256 | Established joint update/query dynamic cell-probe lower bounds and chronogram/information-transfer methods. | Source of strong already-known dynamic interactions; G2 must add an independently priced trust/proof dimension without conflating word probes and changed bits. |
| **LIT-129/131** Chakrabarti et al. *Annotations in Data Streams* (2014); Ghosh–Shah *New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification* (2024) | Untrusted online annotation and verifier-space/proof communication tradeoffs, including nontrivial online Merlin–Arthur barriers. | These are the real theorem competitors for proof bytes, transcript timing, and dishonest prover soundness, not static trusted side-message capacity. |
| **LIT-127** Chandran et al. *Locally Updatable and Locally Decodable Codes*, TCC 2014 | Simultaneous local reads/writes in coded data under a defined attack/corruption setting. | Existing code-locality coupling; claims of novel dynamic read/write proof capability need distinguish this channel/adversary model. |
| **LIT-142** Scott Aaronson, *Quantum Certificate Complexity*, JCSS 74(3) (2008), DOI [10.1016/j.jcss.2007.06.020](https://doi.org/10.1016/j.jcss.2007.06.020) | Introduces randomized certificate complexity and quantum certificate complexity, characterizes their relationship, gives query-complexity separations. | **Direct prior-art obstruction:** randomized local verification of an assertion is not a new UCT concept. Our argument is a restricted coupling of such a certificate bound to *dynamic update supports*. |
| **LIT-143** Ambainis–Kokainis–Prūsis–Vihrovs–Zajakins, *All Classical Adversary Methods Are Equivalent for Total Functions*, ACM TOCT 13(1), DOI [10.1145/3442357](https://doi.org/10.1145/3442357), 2021 | Original university/publisher abstract: classical adversary lower-bound methods are equivalent for total Boolean functions and equal fractional block sensitivity `fbs(f)`. It distinguishes partial functions. | **Strong STOP for naive novelty of fractional packing**: ordinary `ν*` lower bounds are established as fractional block-sensitivity/dual certificate linear programs for Boolean query problems; dynamic stored-support coupling is a useful model-specific *reduction*, not established new global asymptotics. |
| **LIT-144** Ben-David & Kothari, *Randomized Query Complexity Can Beat Certificate Complexity*, author preprint [arXiv:2609.15063](https://arxiv.org/abs/2609.15063), 2026-09-14 | Authors construct a total Boolean function for which randomized query complexity is `O-tilde(sqrt(C(f)))`, nearly optimal up to logs, separating randomized query complexity and deterministic certificates. | **Fresh 2026 falsification warning:** do NOT transfer an exact deterministic certificate lower bound directly into a bounded-error randomized algorithm. G2-1 is instead a narrowly defined **untrusted proof soundness** game with a single fixed witness; it does not imply arbitrary randomized query lower bounds via C(f). |

Additional near source: [ECCC TR17-150](https://eccc.weizmann.ac.il/report/2017/150/) (precursor of LIT-143) and [arXiv:1810.02393](https://arxiv.org/abs/1810.02393) on fractional block sensitivity. No duplicate records for a journal DOI and its preprint under separate LIT IDs. [Ko ECCC TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) is already **LIT-119** and source statement scoped in UCT-001.

**Paper accuracy warning:** The 2026 Ben-David/Kothari preprint is an **author assertion from an abstract** here; no independent line-by-line proof audit, publication/peer-review status or applicability to a dynamic data structure is asserted.

## 2. Valid new *combination* versus genuinely NEW theorem

`G2-1` (randomized paired-run coupling) + `G2-2` (weighted hitting/packing) + `G2-3` (w=1 hypercube rigidity) + a matching zero-error-completeness bit-sampling protocol form a **coherent, rigorous, explicitly scoped cross-domain theorem package**. Its result is stronger than a totally uncosted honest-advice capacity inequality on exactly the **fixed** model, because even arbitrarily long untrusted messages cannot eliminate reads at δ=0 if physical update supports are disjoint. However **the ingredients are classical**: indistinguishability, randomized certificate/adversary LP, hypercube embedding, and sampling. That it combines them is NOT enough to claim a new theorem worthy of publication.

The closest novelty question requires a theorem that remains **nonredundant AFTER** translation of its message space, persistent trusted state, online proof publication timing, update/access costs, and adversarial randomness to both (i) dynamic partial sums lower bounds and (ii) streaming annotated MA lower bounds. There is no proof of such a separation here. **STOP_BROAD_NOVELTY / CONTINUE_G2_NARROW.**

## 3. Resource accounting reconciliation

| Charge/guarantee | G2-A lower bound | G2-A matching protocol | Missing to claim end-to-end theory |
|---|---|---|---|
| Persistent state | binary M(x), length m | m=n raw input bits | compressed/authenticated persistent storage, versioning, roots and corruption model |
| Update changed cells | w=1 in sharp parity corollary | one bit flips per toggle | number of read and written cells, update CPU/prover state management |
| Data verifier probes | worst-case ≤p | uniformly sampled p distinct bit reads | authenticated external range reads, addresses, network I/O |
| Prover witness bits | finite π, arbitrary b lower bound | b=n | maintenance/transmission charge b and proof generation work |
| Verifier CPU | unbounded in converse | Θ(n+p) in example | actual algorithmic CPU and crypto cost |
| Completeness | fixed honest π independent coins, ≥1−α | α=0 | proof availability and latency on concurrent updates |
| Soundness | for every dishonest π and false claim ≤δ | δ=1−p/n | public-coin prover, adaptive history, reused seed, PRF reduction and adversarial corruptions |
| Cryptographic binding | no crypto root | none needed | a Merkle root requires trusted authentic storage; cannot be taken as a free oracle |
| Query scope | one full parity query under the *full prefix service* storing raw x | all prefix queries remain answerable by up to n raw-bit reads | lower bound for a **joint** bounded-p query service, not only one selected query |

## 4. G2-C next experiment (evidence-gated)

Freeze **fully priced online sound bit-query protocol** before simulation: if witness length n can be replaced by substantially smaller b while keeping p=Θ(n) or p=o(n) and δ<1/2, that is an *actual certificate-length tradeoff*; direct and Fenwick data structures plus standard annotated proofs are explicit baselines. For n≤3, enumerate b≤2, p≤2 with *soundness quantified over every false witness and every state*, fixed coin sets and update-congruence. Avoid claiming that an exact exhaustive n=3 result proves asymptotic optimality. A larger original bound only after original theorem source review.

**Gates:** G2-A source/finite proof ACCEPT after exact PR CI; G2-B original multi-resource theorem UNPROVED; no Rust, no production claims.
