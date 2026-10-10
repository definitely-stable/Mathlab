# UCT-005 D1-C1 — source-mapped candidate inequality kill gate, exact finite countermodels

2026-10-11. [D1-C #302](https://github.com/definitely-stable/Mathlab/issues/302) · [slice #307](https://github.com/definitely-stable/Mathlab/issues/307) · predecessor [D1-C0 PR #304](https://github.com/definitely-stable/Mathlab/pull/304) · [UCT root #105](https://github.com/definitely-stable/Mathlab/issues/105). **NO NEW NONFACTORIZING JOINT LOWER BOUND. ROOT OPEN_UNPROVED.**

## 1. Frozen candidate protocol

The machine-readable [candidate ledger](UCT-005-G3-B2-D1C1-CANDIDATE-GATE.json) was frozen BEFORE implementing this new falsifier oracle. Every candidate has `model`, `claim`, `quantifiers`, `status`, `falsifier`, `theorem_transfer` and individually unknown F1 axes, which are represented by JSON `null`, **never 0**. The existing [F1-MODEL.json](UCT-005-G3-B2-D1B0-F1-MODEL.json) is authoritative for all 18 cost coordinates; the five parameters n,H,lambda,epsilon,P are distinct. [Executed witness oracle](../../research/uct005_d1c1_hypothesis_kill_gate.py) imports actual accepted reference constructors instead of hard-coding expected paper metrics as observations. [Independent finite tests](../../research/test_uct005_d1c1_hypothesis_kill_gate.py) reject invalid candidate statuses and model upgrades, verify physical staging counters, independent PIN roots, actual F0 Fenwick bit-cell operations and incomplete cost axes.

The claim **`exists an original stronger joint F1 bound` remains `OPEN_UNFORMULATED`**, since the missing candidate inequality, a public family of hard histories/adversarial query distribution, asymptotic security parameter lambda(n), proof and primary theorem reductions cannot be inferred from finite upper-comparator experiments.

## 2. Scientific decision matrix, and what each counterexample does NOT show

| Candidate | Frozen scope | Evidence-based result | Crucial exclusion |
| --- | --- | --- | --- |
| C1: universal W_max Q_max >= n | Honest F0 bit-cells | REJECTED. Explicit counted Fenwick at n=4096: remote=8192 bits, W<=14, Q<=24, WQ<=336<4096 | **NOT** an authenticated F1 protocol |
| C2: k independent n-bit PIN states | Truthful bitmap-only observation projection | REJECTED. n=5, named epochs 0/2/3: 3072 distinct outputs / 12 bits < 15; independently n=4,H=3: 8192 author labeled SET transcripts versus 2000 bitmap histories | Does **NOT** supply F1 online index, proof or physical page upper |
| C3: O(P) trusted PIN scratch forces two old scans | F1 modeled page image **allowing paid speculative stage** | REJECTED by accepted F3-C: for C=17,P=1,M=5, two-pass 55 online bitmap reads vs one-pass 35, but 20 preauth stage writes | No real fsync, no free cleanup or full all-resource Pareto |
| C4: F2 failed update always stages zero | F1 remote server changes an old bitmap between F2 SHA passes | REJECTED: F2 sends five full pages and five cleanup drop requests on abort; no trusted publication | Does not disprove F2 zero-stage property for **pre-existing** SHA-invalid old bitmap |
| C5: every PIN token needs separate immutable snapshot | F1 two offline readers PIN SAME epoch | REJECTED by actual F3-B authenticated offline audit: 2 PIN tokens, exactly 1 distinct historic snapshot image; audit remotely reads charged pages | Separately trusted reader roots and authoritative PIN records remain fully paid |
| C6: F3-C strictly dominates F2 in all axes | F1 before-first-read SHA-invalid old image | REJECTED: F2 stages 0 pages; F3-C stages 5 pages then pays 5 DROP_PAGE (40 address bytes) | Failure-side cost only, no claim of universal F2 dominance |
| C7: F3-D counts are a novel joint theorem | Restricted deterministic coding phase cut | STOP_NOVELTY, since N-1<=lambda+b+8P(W_pre+q_after)+A is basic injection counting; stage 8 pages trades off eight later page reads in finite witness | Neither cryptographic SHA nor historical GC lower bound |
| C8: strictly stronger fully priced authenticated-history lower bound exists | Full computational F1 | **OPEN_UNFORMULATED**: no exact inequality, no hard distribution, no lambda-scaling reduction, no all-cost candidate oracle yet | Inconclusive, NOT disproved and NOT proved |

The narrow negative decisions C1/C2 must **never** be advertised as impossibility of a stronger F1 theorem: they hold in different models. C3-C6 are exact finite *conditional upper* countermodels for the specified F1 reference grammar, not unrestricted cryptographic lower-bound theorems. C7 is classical even if every finite test succeeds.

## 3. Primary literature provenance and transfer gate

We checked the publisher/author abstracts and bibliographic scope, **not a verified full-text theorem-by-theorem reduction**. The machine-checker explicitly requires `REDUCTION_REQUIRED`, rejects `APPLICABLE` and rejects fake `full_text_proof_transfer=true`:

- Fredman–Saks, *The Cell Probe Complexity of Dynamic Data Structures*, STOC 1989, [ACM DOI](https://doi.org/10.1145/73007.73040). Dynamic partial sums and cell probes are not automatically full-page SHA with PIN/GC.
- Pătraşcu–Demaine, *Logarithmic Lower Bounds in the Cell-Probe Model*, SIAM J. Comput. 35(4), 932–963 (2006), [publisher DOI](https://doi.org/10.1137/S0097539705447256). Word size, operation alphabet, amortized randomized distribution and proof semantics need an explicit exact reduction.
- Blum–Evans–Gemmell–Kannan–Naor, *Checking the Correctness of Memories*, Algorithmica (1994), [IBM primary metadata](https://research.ibm.com/publications/checking-the-correctness-of-memories). Trusted verifier memory vs adversarial storage overlaps, but historical authoritative PIN root and external page/write charges do not follow automatically.
- Driscoll–Sarnak–Sleator–Tarjan, *Making Data Structures Persistent*, JCSS 38(1), 86–124 (1989), [publisher DOI](https://doi.org/10.1016/0022-0000(89)90034-2). Persistent linked structures can share versions; they do not directly satisfy SHA adversary, offline two-reader freshness and page-image/GC cost constraints.

Avoid importing duplicate bibliography IDs until separately reconciling with existing Mathlab LIT corpus. Citation metadata and primary abstracts are evidence about **model overlap**, not about establishing new F1 theorems.

## 4. What is necessary to move beyond scoped STOP

D1-C issue #302 requires **one specifically quantified candidate** of form `F(s,S,U_r,U_w,Q_r,B_pi,C_author,C_reader,G,V,A,T,M,GC,F; n,H,P,lambda,epsilon) >= f(n,H,P,lambda,epsilon)`, with all terms dimensionally meaningful and no double-counting, a named hard sequence or adaptive distribution, simultaneous bound in the *same* F1 model, all successful and failed transfer/wire cost axes, proof references mapped under explicit reductions, and an infinite parametric family beating the conjunction of applicable classical bounds.

If no such `F/f` survives paid-replica, fixed-stride snapshots, persistent COW, log-replay, F2 and F3-C and all expected failure costs, record **SCOPED_STOP_NO_NEW_ROOT** rather than rebrand Hamming-ball / pigeonhole / cell-probe lower bounds. The current matrix contains **zero original lower-bound proofs**.

All sample counters are modeled full P-byte API page images, not measurements of NAND traffic or real power-loss behavior. Tests must pass on GitHub-hosted runners with exact-head dedicated+Research+INDEX/D1-A, while predecessor D1-C0 must merge first. **UCT root OPEN_UNPROVED.**
