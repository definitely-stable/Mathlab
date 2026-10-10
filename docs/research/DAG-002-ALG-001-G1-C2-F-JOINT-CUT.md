# DAG-002 × ALG-001 — G1-C2-F: joint prefix-information cut, exact restricted matching

**Owner:** [issue #161](https://github.com/definitely-stable/Mathlab/issues/161). Independent branch on main. Existing G1-B (#159), G1-C1 (#264) and open G1-C2-A..E (#267, #268, #271, #274, #275) are untouched. **Classification:** EXACT_CONDITIONAL_CUT / FINITE_MATCHING_PROMISE_FAMILY / CLASSICAL_COUNTING / NO_CLAIM_OF_NOVELTY / NO_UCT_ROOT_TRANSFER.

## 1. Frozen cross-history experiment

Start with m isolated old vertices 0..m−1. Insert old vertex m, with an arbitrary parent subset e among those m vertices. Thus e ranges independently over 2^m histories and is encoded when vertex m arrives by the **charged m-bit parent-incidence command**. Then perform the *same* next command for every history: APPEND_SINK(m+1,{m}). The correct old-to-new Boolean reachability vector includes m and equals 2^m | e. All public IDs, latest parent command, source-cell addresses, initial fresh-record address and fixed decoding program are identical. The experiment varies PREVIOUS histories and is not the fixed-prior-history bound of G1-B.

Require an exact deterministic encoder/updater with:
- H mutable trusted local bits maintained across the previous append; those bits may contain an arbitrary function of e, but are **not free** in an actual multi-step system. Setup/update cost during the preceding append is NOT established here.
- No current parent-incidence row e is supplied to the final append updater: it sees only {m}. It may read at most R **one-bit** old remote source cells adaptively. The probe address at each stage is a deterministic function of public context, retained H bits, and earlier probe answers. Read-address metadata is *not* an unaccounted free answer source.
- A new N-bit remote record initially contains an identical, known all-zero word at a fixed address for every history. At most W of those N bits may be changed in the final physical state, with ordinary writes and no free other mutable remote locations. The finished local state remains H bits.
- Target-only reachability queries can inspect the entire new record and final H local bits without reading prior remote cells, old graph adjacency/labels, mutable address directories, old snapshots, old root epochs, or out-of-band changing code. They receive the queried source ID, not the previous graph history.
- No randomness, wrong answers, probabilistic success, arbitrary history-dependent program T, changing record placement, hidden source read cache, uncharged trusted memory, or cryptographic oracle.

This is deliberately **not** a general dynamic data structure, physical I/O or authenticated-history model.

## 2. G1-C2-F-L1 — simultaneous necessary information cuts

There are K=2^m pairwise distinct required target-coordinate answer vectors.

**Updater transcript cut.** For each fixed previous H-bit trusted state, a deterministic decision tree with at most R adaptive one-bit reads has at most 2^R leaves. Every leaf prescribes the complete future fresh record and H-bit local state. Consequently the number of distinct final observations across all histories cannot exceed 2^(H+R).

**New-record volume cut.** For each possible final H-bit local state, the new initially zero N-bit record with at most W net bit changes has no more than V_2(N,W)=sum_{j=0..min(N,W)} C(N,j) possible final images, so there are at most 2^H V_2(N,W) target observations. Combining,

    2^m <= min( 2^(H+R), 2^H * V_2(N,W) ).

Thus both H+R>=m and 2^(m−H)<=V_2(N,W) are necessary. The result is simply **pigeonhole plus binary decision-tree leaf counting plus a Hamming-ball count**; it is not novel. We have NOT derived an additive R+W bound, a universal Pq bound, an online RAM theorem or a cross-history G1-B transfer.

## 3. G1-C2-F-L2 — exact sufficiency on this narrow promise family

For 0<=H<=m, if R>=m−H and V_2(N,W)>=2^(m−H), these two conditions also suffice **on this family**, not on arbitrary append DAGs. At the preceding append of vertex m, save the low H bits of the m-bit public parent row e as trusted state; publish the other m−H bits at known distinct binary old-source cells (their writes and source storage are not priced in this final-append-only theorem). The final updater reads exactly those m−H cells, constructs the integer residual, and publishes its canonical enumerative code as one of 2^(m−H) distinct N-bit words with <=W ones. Query on the new target inspects its N-bit record and H local bits, reverses that enumeration and answers all m+1 coordinates. Final physical changed-bit budget W and read budget R are met. The fixed codebook is specified algorithmically by lexicographically enumerating combinations by weight; executable/ROM/runtime cost T is **not** charged, so no cross-model algorithmic optimality follows.

The executable certificate additionally enforces the read interface: `retained_state_from_prior_append(e)` computes the H-bit local value at the earlier operation, but the FINAL updater is `update_charged(retained_local, read_old_bit)` and **never receives e**. The verifier keeps the entire old history separately and supplies only a bound one-bit `ChargedOldSource.read_bit` callback with a hard per-operation probe counter and address trace. A read beyond R throws before revealing the bit. The verifier independently recomputes source-to-target reachability by DFS and checks the actual probe trace. This instrumentation prevents an implementation from pretending that direct access to the full old parent mask is just R charged reads.

This is a constructive finite matching argument for a fixed known number of history bits, not a proof that a single code satisfies a future-unbounded online sequence or works under bounded Pq, source page-size constraints, an authenticated root, GC or concurrent readers.

## 4. Independent kill and source audit

The read obstruction and write obstruction are independent:
- m=4,H=1,R=2,N=5,W=2: volume is sufficient, but 2^(H+R)=8<16 histories.
- m=4,H=0,R=4,N=3,W=1: source reads suffice but volume is 1+3=4<16.
- m=3,H=1,R=2,N=3,W=1: both cuts meet equality (2^(1+2)=8 and 2*V_2(3,1)=8), and a matching exact finite certificate exists.

**Escapes:** allow old query reads (lazy adjacency DFS), history-dependent new-record addresses, additional uncharged mutable metadata, larger trusted state, atomic multi-bit cell reads, mutable codebook or nonzero error: the premises break. Therefore the exact restricted result must NOT be advertised as a universal multi-epoch update/query/observer theorem or original asymptotic data-structure lower bound.

Prior art includes [Chandran–Kanukurthi–Ostrovsky, TCC 2014, LULDC](https://www.microsoft.com/en-us/research/publication/locally-updatable-and-locally-decodable-codes/), [Pătraşcu–Tarniţă, TCS 2007, dynamic bit-probe complexity](https://doi.org/10.1016/j.tcs.2007.02.058), [Bulteau et al., SEA 2025, append-only reachability index](https://doi.org/10.4230/LIPIcs.SEA.2025.9) and G1-B finite Hamming-volume result. These sources do not automatically prove a general combined append-DAG cut under this operation model; conversely the joint bound is transparently **classical counting**, so STOP_THEOREM_NOVELTY applies to this specific proposed theorem without pretending a new published primary-source proof.

## 5. Exact reproducibility and acceptance

    python research/dag002_g1c2f_joint_cut.py
    python -m unittest discover -s research -p 'test_dag002_g1c2f_joint_cut.py' -v

Ten independent tests: Hamming-ball independent full-state enumeration; graph-family old-to-new truth values from a separate DFS; both independent resource obstructions; exhaustive matching promise certificates for m<=5,H<=m,N<=5,0<=W<=N; older local-bit setup and no free latest-parent command; certificate tampering; old-source-query escape and invalid dimensions. These are proof falsifiers; full hosted GitHub Actions is required for acceptance.

**Gate:** keep #161 OPEN. Integrate this PR only after exact-head focused AND full Research CI are SUCCESS, and review confirms it is **independent from** queued #267-#275. G1-C2-F is a completed restricted information frontier, not a UCT-005 foundation theorem. To seek a new theorem next, first require a source-level reduction/novelty discriminator with separately charged query P, mutable codebook T, trusted H maintenance and observer PIN/GC; otherwise STOP and archive this line.
