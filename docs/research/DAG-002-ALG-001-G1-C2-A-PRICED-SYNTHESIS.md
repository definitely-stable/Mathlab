# DAG-002 × ALG-001 — G1-C2-A: fully typed finite online updater synthesis

**Parent:** [issue #161](https://github.com/definitely-stable/Mathlab/issues/161).
**Predecessor:** [G1-C1 PR #264](https://github.com/definitely-stable/Mathlab/pull/264), must merge or be verified before this dependent branch.
**Scientific decision:** EXACT_FINITE_SYNTHESIS / CLASSICAL_SAFETY_AND_CIRCUIT_ENUMERATION / SOURCE_LEVEL_NOVELTY_OPEN / NO_ROOT_TRANSFER.

## 1. Why G1-C1 is insufficient

The G1-C1 fixed-point criterion assumes that the updater can inspect an entire N-cell physical state (up to N remote reads). Its existential successor may vary for each old physical word. A real bounded-read updater must instead use one immutable program for each public DELTA command and retained local state, and that program must distinguish states using only charged read transcripts. An arbitrary controller selectable *after* seeing the full word is an unpriced side channel.

This stage freezes a binary model with logical n<=2, N<=3 remote cells and H<=1 locally trusted bits, N+H<=3, fixed decoder, explicit alphabet D of GF(2) delta commands, deterministic zero-error operation, and a declared initial physical+local state. Queries see their local value and read at most P remote bits; updating sees delta and local value, reads at most R remote bits, performs <=1 constant-bit remote overwrite and <=L trusted local-bit flips. Charge W_phys operations independently from W_net changed final cells. No hardware XOR write, free latest-epoch clock, cached target bit, unpriced prior-state access or changing codebook.

A correct protocol has one closed invariant I of physical+local states. The same query decision tree must work on every state in I sharing the given local value, and the same update decision tree must work for every state in I sharing local value and delta. Each leaf contains an ordinary constant overwrite/no-op plus an explicit new local value. Reads may adapt to previously returned remote bits (depth <=2). For each original state and each delta, the resulting physical state must remain in I and the decoder output must change by XOR delta. Unreachable words may be excluded, but a separate required_states argument pins states that MUST be supported.

## 2. Exhaustiveness criterion (classical finite decision-tree fact)

For a fixed invariant I, recursively test whether one leaf action has the required postcondition on every state in a currently indistinguishable class. If no leaf works and a probe remains, split that class by an addressed remote bit and recurse on the two outcomes. All addresses 0..N-1 and every legal action are enumerated. Each solution is one common read tree, not a distinct program per physical word. Finally enumerate all finite subsets I containing the initial and all required states.

This returns YES iff a protocol with these exact restrictions exists. A NO result is **only** for the frozen table grammar and search dimensions. The method is a standard finite safety/circuit synthesis reduction; scientific novelty is NOT established.

To price the public program explicitly, encode each tree by a preorder prefix grammar: internal node = 1 tag bit + ceil(log2 N) address bits (for N=1 the only address uses 0 bits) + the two children; leaf = 0 tag bit + ceil(log2 A) bits selecting one of A possible actions. Query leaf A=2; update leaf A=(1+2N)*2^H. Store one query tree for each pair (coordinate,local value), and one update tree for each (delta,local value), even if a local value is unreachable. Their complete length T is compared with a user-supplied T budget. Model dimensions, header, lookup interpreter, update-command delivery, trust/authorization and source preprocessing are EXCLUDED: T is an exact wire payload **within this one declared grammar**, not an entropy lower bound or optimal executable representation.

## 3. Exact mandatory falsifiers

**C2-A1, one-bit direct store:** n=1,N=1,H=0,D={0,1}, decoder f(z)=z. The full-read safety game is winning forever, but no updater with R=0 and fixed-address constant overwrites can realize repeated DELTA(1) correctly. R=1,W_phys=W_net=1,P=1 can, by reading then writing the complement. The enumerator produces a fixed certificate with T=15 payload bits under the chosen grammar, not a claim of 15 necessary bits across all encodings.

**C2-A2, retained local information:** n=1,N=0,H=1,D={0,1}, decoder f(local)=local. P=R=W_phys=W_net=0 is feasible if the local-bit flip budget is L=1; L=0 is impossible. A fixed grammar certificate has T=12 bits. This is a countermodel to any assertion that remote update reads are universally required when local state is left unpriced.

**C2-A3, admissible-codeword quantifier:** n=1,N=2,H=0, f(z)=z0 XOR z1. P=1 works on a closed 2-codeword subset, but is impossible if all four words are required; P=2 succeeds on the full domain. Thus no general P>=2 theorem follows from the truth table alone without stating the invariant support.

**C2-A4, fixed program metadata:** exact tree payload T must be charged before comparing against a claimed T budget; fixed grammar is a chosen reference encoding, not a lower bound valid for all compressed program representations.

## 4. Independent reproducibility

Run the deterministic report and six unit tests (including independent literal enumeration of every n=1,N<=2 decoder under R in {0,1}, direct policy replay for every invariant state and command, invalid input/codebook manipulation):

~~~bash
python research/dag002_g1c2_synthesis.py
python -m unittest discover -s research -p 'test_dag002_g1c2_synthesis.py' -v
~~~

Both a dedicated GitHub-hosted CI job and the repository's existing automatic Research unit-test discovery run them. Do not mark this accepted until exact-head focused and full Research CI are SUCCESS.

## 5. Prior-art separation and next acceptance gate

- [Chandran–Kanukurthi–Ostrovsky, TCC 2014, locally updatable/decodable codes](https://doi.org/10.1007/978-3-642-54242-8_21) has a distinct Prefix Hamming corruption model, cryptographic variants and dynamic proofs-of-retrievability; no parameter transfer follows from the title or abstract.
- [Pătraşcu–Tarniţă, On dynamic bit-probe complexity](https://collaborate.princeton.edu/en/publications/on-dynamic-bit-probe-complexity/) studies dynamic bit-probe lower bounds, including partial sums. A future asymptotic claim must distinguish their operation and adversary models.
- [Ko, ECCC 2025 TR25-156](https://eccc.weizmann.ac.il/report/2025/156/) and [Ko, ECCC 2026 TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) concern scoped cell-probe/communication hardness, not automatic theorems about arbitrary local-memory XOR codecs.
- [G1-B #159](https://github.com/definitely-stable/Mathlab/pull/159) already contains the classical linear Hamming-syndrome construction.
- [UCT-005 root #105](https://github.com/definitely-stable/Mathlab/issues/105) and F1 #223 include authenticated freshness and physical costs, which this slice DOES NOT model.

This is source/model comparison, **not** an independent full-paper theorem-by-theorem audit. Do not import bibliography identities here (owned by #147).

**Next G1-C2-B:** extend beyond a fixed decoder to a quantified family of online append-DAG membership outputs and independently charged physical pages/trusted root; test a precise resource-preserving reduction to published bit-probe/lower-bound work. A new root theorem requires a new proof beyond finite code enumeration, exact source-level closure, and independent falsification. Otherwise record STOP_THEOREM_NOVELTY. No Rust or other repositories touched.
