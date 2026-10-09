# UCT-002 — operational observation-capacity master theorem (classical baseline)

**Date:** 2026-10-09. **Issue:** [#77](https://github.com/definitely-stable/Mathlab/issues/77), parent [#76](https://github.com/definitely-stable/Mathlab/issues/76). **Status: PROVED_DERIVED_CLASSICAL; original unified scientific theory NOT established.** This document is deliberately larger than a sketch or patching theorem. It is a rigorously typed combination of Hamming-ball geometry, adaptive decision-tree leaf counting and the classical Fano converse. Proof is self-contained; implementation is checked separately by finite oracles.

## I. Common mathematical object

Fix finite state space X, directed graph E of **allowed updates**, distinguished reference x0, integer radius d>=0. Define R_d(x0) as vertices accessible by at most d transitions. The maintained memory is a deterministic code phi:X->A^m where |A|=q>=2; on each allowed edge (x,y), at most w code coordinates change. There is no implicit charging of *computation* or address/word probes by this Hamming condition. If the update algorithm receives only an operation label rather than old state, it must separately implement a transition congruence (UCT-001 and TOM-003).

Let Q=(Q1,...,Qt), t>=1, be a **fixed finite suite of public, stateless observable queries** with Q_i:X->Y_i. Joint signature O_Q(y)=(Q1(y),...,Qt(y)). Choose representatives F subset R_d(x0) with pairwise different signatures; K=|F|>=2. Public x0, graph, query definitions and suite are the SAME for all representatives; otherwise state-dependent differences must be charged.

The verifier gets:
1. final mutable code phi(y) (q^m space, but only local ball around phi(x0) is reachable);
2. **ONE** state-dependent b-bit annotation h(y), padded to exactly b bits, common to **all** queries; it could be a trusted side message or an honestly supplied proof in a sound protocol;
3. a state-dependent **external read-only oracle** a_y:[N]->Sigma whose alphabet size s=|Sigma|>=2. During answering the fixed query suite the verifier performs a total of **at most P** symbol probes, with addresses adaptively selected as deterministic functions of known data and prior answers. Its transcript includes the returned symbols only; probe addresses are functions of previous observations and are not free independent messages. Public coins R independent of y may be used by a randomized verifier. Any state-dependent external metadata (root, length, reference, signature, index, proof, key) is counted in phi, h or the oracle probes.
4. exact joint answers, or a specified average joint error e for a uniformly sampled representative y in F (randomness over verifier's independent coins and the sampled representative).

This model deliberately distinguishes **trusted/bound side information** from **untrusted prover annotations**. Counting the b bits of an honest witness gives a necessary budget; it DOES NOT prove soundness against dishonest witnesses, authentication, generation cost or update cost of that witness. If each query has a distinct witness, their **total** length replaces b. If query suite is adaptive or chosen after learning secret randomness, this theorem needs its own new conditional transcript model; do not transfer its error statement wholesale.

Define the q-ary ball volume:

    V_q(m,r) = sum_{j=0}^{min(r,m)} binom(m,j)*(q-1)^j
    r = min(d*w, m)

## II. Master theorem — exact operational resource capacity

**THEOREM UCT-002/A (exact):** Under the frozen model, any deterministic, exact, universally correct joint-query verifier satisfies

    K <= V_q(m,r) * 2^b * s^P.                                      (A)

**Proof.** Along each length<=d transition path from x0, triangle inequality gives d_H(phi(x0),phi(y))<=d*w. Hence phi(F) lies in a ball of V_q(m,r) possible words. For any fixed pair (phi(y),h(y)), a deterministic adaptive probe algorithm of depth at most P is a decision tree with s-ary branches. It has at most s^P terminal paths (by the prefix-free leaf bound; early termination does not increase the maximum). Addresses and query choices cannot create further branches because they are determined by the protocol and previously seen symbols. For an exact joint verifier, two representatives with different joint signatures cannot share a complete observation tuple (code, annotation, read-response leaf); if they did, the verifier would follow the same branches and return the same answers. Therefore F injects into at most V_q(m,r)*2^b*s^P observable transcripts, proving (A). QED.

**THEOREM UCT-002/B (randomized average-error converse):** Let Y be uniform on F and R independent public verifier coins. Let e be the average probability of producing at least one wrong answer in the **full joint suite** (one common experiment), and assume **0<=e<=1-1/K**. Then

    log2 K <= log2 V_q(m,r) + b + P*log2 s
              + h2(e) + e*log2(K-1).                             (B)

**Proof.** Condition on R=r0. Code and h take at most V_q(m,r)*2^b joint values, irrespective of y. Given them and r0, all external access outcomes form an adaptive s-ary decision tree with <=s^P possible leaves. Thus the complete decoder observation Z=(phi(Y),h(Y),oracle transcript,R) obeys I(Y;Z|R)<=log2 V+b+P log2 s and I(Y;R)=0. Denote by Yhat the inferred representative from the jointly decoded signature if the signature matches one representative (arbitrarily map other signatures). Its error probability is at most e, or choose an optimal representative decoder with error e'<=e. Apply Fano to Y, Z with actual e' to obtain log2 K <= I(Y;Z)+h2(e')+e'log2(K-1). The Fano penalty is nondecreasing on [0,1-1/K], and an optimal decoder has e'<=1-1/K; if the claimed e>1-1/K the statement with e instead of e' need not be monotone, so **interpret (B) using actual optimal decoding error e'** or assume e<=1-1/K. Under that explicit assumption, replace e' by e, proving (B). QED.

For a uniform guarantee Pr[joint incorrect]<=epsilon with 0<=epsilon<=1-1/K, the rightmost terms may be replaced by h2(epsilon)+epsilon*log2(K-1). For Q individual fixed queries with joint uniform conditional error guarantees epsilon_i, a union bound gives <=sum epsilon_i (clamped to 1) for the joint event **under the same fixed experiment**. Adaptive choice depending on revealed hidden coins is NOT covered by that substitution.

**Alternative coarse converse** for arbitrary e (no monotonicity issue): log2 K <= log2 V+b+P log2 s+1+e*log2 K when e is an upper bound on the joint error.

## III. Master theorem is not a new law of nature

The product formula is a straightforward combination of old counting arguments. It is NOT a proof of optimal physical data structures, an original streaming theorem, unconditional cryptography, or a new rate-distortion result. Strong published overlaps include Fredman–Saks (1989), Pătraşcu–Demaine (2006), locally updatable/decodable codes (2014), annotated stream proof/space tradeoffs (2014), online Merlin–Arthur verification (2024), and Fano's inequality. See [cross-domain primary source audit](UCT-002-PRIMARY-SOURCE-AND-BRICKS.md).

The exact inequality is **necessary, not sufficient**. A star realizes it when b-bit helper and source oracle are freely state-dependent, but graph-embedding obstructions, witness-generation time, transition congruence, security and streaming order can prevent achieving it in natural workloads.

## IV. Sharp finite example (tight when all resources really are independent)

Let q=2, m=2, w=d=1, b=P=1, s=2. The radius-one ball around 00 is {00,01,10}: V_2(2,1)=3. Form exactly K=12 distinct states parameterized by triples (code∈{00,01,10}, helper∈{0,1}, oracle_bit∈{0,1}). Choose center (00,0,0) and directed edges from center to each of the other eleven states. The edge locality bound holds because only the code is constrained; a zero-change edge is admissible. Let joint observable be complete state identity. The verifier reads code, helper and one oracle bit, so recovers all 12 exactly. The bound is saturated: 12=3*2*2. Updating external helper/oracle contents is NOT free in a realistic system unless these resources are separately charged.

## V. Why the query-suite qualification is indispensable

Take X={0,1}^n, no maintained bits m=0, no helper b=0, source oracle a_x(i)=x_i; Q_i(x)=x_i for i in [n]. Each query individually uses p_i=1. Taken together the n answers distinguish 2^n states. Incorrect shortcut "there are only 2^p outcomes, so the whole service distinguishes <=2" is FALSE. The correct total budget P=sum_i p_i=n gives 2^n<=s^n, tight. Per-query resources cannot be substituted as total-service resources without specifying the family of queries, reusability and total accesses.

Similarly, fixing an old-root r or old snapshot while selecting distinct states within its **one fibre** is essential. If the verifier receives an arbitrary state-dependent perfect oracle for the new output for free, the theorem is inapplicable, not contradicted.

## VI. Exact specialization and NON-specializations of previous bricks

| Source result | Formal relationship with master theorem | What absolutely does NOT follow |
|---|---|---|
| **LENT-001 / KR-001** | **SPECIAL_CASE:** X=subsets of at most d IDs, Q=identity, x0=empty, b=P=0, phi=sum of w-sparse columns, graph singleton additions -> original Hamming-ball inequality. | Does not establish optimal ASET constructions / support-sensitive asymptotic sharpness. |
| **UCT-001 graph bound** | **SPECIAL_CASE:** t=1, b=P=0. | Volume alone does not guarantee graph embedding; triangle and K(2,3) fail. |
| **TOM-003 (Myhill–Nerode state)** | **REDUCTION_WITH_ADDITIONAL_HYPOTHESES:** replace current observable by **future-trace equivalence** to correctly identify memory states under unknown old bits. | An arbitrary-overwrite update machine is NOT automatically implemented by any code meeting current-state O and the ball bound. |
| **HYP-103 exact probe certificate** | **ANALOGY/COMPONENT:** authenticated old-bit reads instantiate charged oracle queries; a hitting-set minimum is stronger, pointwise and depends on actual Boolean function. | Does not follow as equality from (A): capacity is only a coarse necessary condition. |
| **TOM-005 minimum/route/fanout** | **INDEPENDENT_COST_LEMMAS:** applicable only after constructing an exact same-workload reduction of additional time/physical-output cost. | Cannot add their bounds to (A) without proving shared semantics. |
| **TOM-006 / UCT-003 absent-q-gram** | **SEPARATE_STRUCTURAL_CONSTRAINT** on transformations; shows weak data summaries may not predict actual minimum patch cost. | Not a corollary of (A), nor a proof of universal VCDIFF limits. |
| **DeltaMeter Energy / Parity** | **ERROR_CONTRACT_COMPARATOR:** finite-sample ideal randomness vs asymptotic parity and keyed/adaptive model; Fano is a converse for uniformly distinguishable messages, not the estimator's guarantee. | Fano does NOT establish or refute DeltaMeter's estimator profiles. |
| **Annotated streams / MA** | **PRIOR_ART AND ADVERSARY_BARRIER:** untrusted annotation requires an independent soundness definition; message/verification space tradeoffs can be nonlinear. | Treating h(y) as trusted bits ignores the MA/OMA proof obligation. |

## VII. Genuine NEW theorem target (OPEN, not proved)

**CONJECTURE UCT-002/C (nonfactorizing dynamic observation frontier).** Find a named natural family T_n of *fully specified* dynamic exact query tasks and a range of m,w,b,P where EVERY sound online protocol with charged annotation update/generation, local mutable updates and adaptive external reads satisfies a lower bound **strictly stronger by an unbounded factor** than both (A) and the best separately available cell-probe/annotated-stream/code lower bounds under an assumption-preserving map. Desired shape:

    K(T_n) <= V_q(m,dw)*2^b*s^P / D_n,  with D_n -> infinity,

or an equivalent nonlinear inequality involving all resources under a directly exhibited hard distribution. Here K(T_n) is the number of admissible distinct joint signatures within radius d. There is NO claim such a D_n exists for all tasks; the sharp star shows the universal version with D_n>1 is false.

**Minimum proof obligations:** (a) exact hard task and dynamics; (b) online/untrusted witness semantics and cost ledger; (c) source-theorem-by-source-theorem model map; (d) nontrivial separation from the conjunction of known bounds; (e) finite falsification oracle before asymptotic proof; (f) matching construction or quantification of unavoidable slack. This remains a RESEARCH TARGET. A negative outcome is a correct STOP decision.

## VIII. Verification
`research/test_uct002_joint_capacity.py` independently enumerates small balls / address-decision trees, the sharp 12-state star, and countermodels where 1 query cannot represent the whole suite. CI checks finite instances, not universal scientific novelty or theorem proofs. All new claims maintain Mathlab's strict evidence labels.

## IX. Operational query-probe extension (UCT-003, proved classical, 2026-10-09)

The exact capacity master theorem observes the **whole** maintained code. It does not limit how many codeword cells each user query probes. [UCT-003's adaptive read/write influence theorem](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md) adds actual charged query read paths: every update changing a query answer must change a probed cell, and support must hit all affected paths. One-bit-probe Boolean services have the sharp representation/write sensitivity characterization. For n-bit dynamic prefix XOR this forces **w>=n** if all prefix queries are answered with p<=1 bit probe; conversely an injective complete bit-toggle representation with w<=1 must be a coordinate embedding, forcing p>=n for the full prefix query, even though the capacity inequality alone allows m=n,w=1 if the whole representation may be freely observed. This is a **DERIVED_CLASSICAL** task-specific strengthening and does not make UCT-002 a novel unified asymptotic lower-bound theorem. Review current [G1 source audit](UCT-003-G1-SOURCE-AND-GAP-AUDIT.md); strong p>=2 + sound annotation novelty remains OPEN.

## X. Soundness, fractional update packing, and linear witness-length tradeoffs (UCT-004, 2026-10-09)

The [UCT-004 G2-A classical theorem](UCT-004-G2-A-SOUND-WITNESS-PACKING.md) charges **actual reads of maintained code** and requires **untrusted-witness soundness** for all false-claim proofs. Under independent private verifier coins, randomized influence/hitting coupling gives a fractional support packing bound; the w=1 parity endpoint is sharp using an explicit full-string sampling proof. A second **restricted linear local-test** rank argument gives b>=ceil(n/p)-1 with a matching block-parity witness. This is stronger in this exact model than merely counting honest side-message bits as in UCT-002, but does **NOT** establish new publication novelty, complete authentication cost, or bounds for general nonlinear adaptive protocols. [G2-A primary source audit](UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md) compares classical fractional adversary methods and 2026 randomized-vs-certificate research; G2 original frontier remains OPEN.
