# HYP-103 G0 — exact batch certificate reduction and primary-source stop gate

Date: 2026-10-08. Parent: [issue #70](https://github.com/definitely-stable/Mathlab/issues/70) / [TOM-007 #68](https://github.com/definitely-stable/Mathlab/issues/68).
Base: main at \`20db37795c2d3da9a567e342983a971ab9ebb7a6\`.
Status: **PROVED_CLASSICAL_REDUCTION / STOP_BROAD_CLAIM / NO_RUST**.
The mathematical statement below is a self-contained proof of an **elementary characterization of standard certificate complexity**, NOT a newly discovered mathematical theorem. No source is claimed to prove our exact old-root/update-specific lemma verbatim.

## Freeze the information model BEFORE an optimization

- Let \`f:{0,1}^n -> {0,1}\` be a public, fixed, total Boolean function (it may be implemented as a DAG; its representation is NOT charged by the first model).
- The verifier knows the authenticated old root/output \`r=f(x)\`, the full description of \`f\`, and a public batched overwrite \`u\`. It does **not** have the old input contents for free; it can probe an old input coordinate of the true \`x\` for unit cost.
- A batch \`u=(D,z)\` simultaneously overwrites positions \`D\` by constants \`z_i\`. Unchanged coordinates are retained. Updates, old root, and positions are public; old input bits not read remain unknown.
- The verifier may receive an untrusted **hint of probe addresses** but never an unverified truth value. Probed old input values are authenticated. The first objective is **minimum number of nonadaptive old input probes needed to determine the new output exactly**, assuming the actual input \`x\`.
- Persistent extra metadata beyond the old root is **not included**; if added, its construction/storage/authentication costs must be charged separately. Cryptographic digests, full old-input access, dynamic node caches, and proofer work are not free.
- Strict soundness means an output bit can be returned only when *every* old input consistent with all trusted observations yields that same output. Strict completeness here means that for each actual input \`x\` at least one finite certificate exists, possibly the full set of coordinate probes.
- This is *NOT* a real network/wire-size result, succinct proof, dynamic algorithm time lower bound, optimal nonadaptive probe-order algorithm, or a theorem for cryptographic Merkle proofs.

Define \`X_r = {y in {0,1}^n : f(y)=r}\`.
Define \`h_u(y) = f(y with D overwritten by z)\`.
For an actual \`x in X_r\`, define the opposite-output consistency set
\`O(x,u,r)={y in X_r:h_u(y)!=h_u(x)}\`
and the difference set \`diff(x,y)={i:x_i!=y_i}\`.

## Theorem: exact minimum verified old-bit certificate (classical)

The smallest number of old-input-coordinate probes allowing a correct claimed output \`h_u(x)\` is

    c(x,u,r) =
        min_{J subset [n]} |J|
        subject to forall y in O(x,u,r), J intersect diff(x,y) != empty.

Equivalently, \`c\` is **minimum certificate complexity of h_u over the promise domain X_r at x**, i.e. the minimum coordinate set J making h_u constant on the compatible subcube \`{y in X_r:y_J=x_J}\`.

**Proof (if and only if).** If J omits all differing coordinates for some opposite-output y, then both old inputs x and y yield exactly the same known root, batch overwrite and observed probe values, yet require distinct correct outputs. Therefore no exact deterministic verifier observing only J can certify the true answer. Conversely, if J intersects every opposite y's difference set, every compatible old input y has the same h_u value as x, so the verifier can enumerate the finite promise domain and safely return that value. A hint can identify J but cannot authenticate false claimed old values without probing them. The characterization follows. QED.

This is **not a novel complexity class**. The optimal set J is a minimum hitting set of the difference sets; the brute-force verifier and the computation of J may themselves be exponentially expensive. Only *probe count* is optimized here: do not infer a fast certificate-generation algorithm. A treewidth-t DAG has additional structure, but no bound on this minimum or fast minimizer follows from the lemma without a new, fully costed theorem.

**Cost-model sensitivity.**
1. If the verifier receives the entire old input x as trusted input at zero read cost, then c=0 by definition and the "certificate" is vacuous.
2. If the verifier can trust a fully precomputed per-update answer table for all u, c=0 (but the table has exponential construction/storage cost); the old root is not a stand-in for that table.
3. If a prover may supply unverified old values at no cost and the verifier accepts them, soundness fails on indistinguishable inputs.
4. If setup/preparation, proof bytes, verification time and memory count, a zero-probe answer obtained by exhaustive enumeration may be catastrophically inefficient. This lemma is not an end-to-end complexity bound.

## Exact special-case witness (why batching benefit alone is not original)

Let \`f(a,b)=a AND b\`, old input x=(0,0), authenticated old output r=0. For the singleton overwrite \`u_a=(a<-1)\`, old x_b must be read to certify the output remains zero: c=1. Symmetrically \`u_b=(b<-1)\` has c=1. Yet the joint overwrite \`u_ab=(a<-1,b<-1)\` makes h constantly 1 on X_r, so c=0: the new output is known without reading either old input. Thus \`c_batch < c_singleton_a+c_singleton_b\`, and the two individually no-effect updates jointly **change** the old output. Both facts are elementary and compatible with standard certificate complexity.

## Independent falsification protocol

\`research/test_hyp103_certificates.py\` must implement:
- Method A: exhaustive consistency-subcube enumeration over every candidate probe set J.
- Method B: independent hitting-set verification against all opposite-output witnesses.
- Enumerate **all Boolean functions on n=0..3 inputs** (1, 4, 16, 256 functions respectively), actual input x, and every update pattern with each coordinate unchanged, overwritten zero, or overwritten one. Check A==B and soundness of accepted J.
- Edge cases: constant functions, no-op batches, full overwrites, AND/OR/XOR, and a witness that only old root cannot identify a new output.
- The fixed public function is represented by truth-table bits for the proof oracle, **not** by a full implementation of a bounded-treewidth DAG.

## Mandatory prior art, independently matched at least at abstract/model level

| Existing/new reference | Relevant result and overlap | Exact limitation of transfer |
| --- | --- | --- |
| [Wang–Yin, *Certificates in Data Structures* (2014)](https://arxiv.org/abs/1404.5743), existing LIT-041 | Certificate = nondeterministic cell probes; lower bounds | Static cell-probe data structures, not our charged DAG update protocol. |
| [Grossman–Komargodski–Naor, ITCS 2020](https://doi.org/10.4230/LIPIcs.ITCS.2020.56), **LIT-105** | Instance optimality compared against certificate-aided algorithms | Not our specific root-promise lemma; directly rules out renaming generic certificates as new. |
| [Buhrman–de Wolf, TCS 2002](https://doi.org/10.1016/S0304-3975(01)00144-X), **LIT-108** | Certificate complexity vs deterministic/randomized/quantum decision trees | Standard definition, not a new dynamic verifier implementation. |
| [Datta et al., MFCS 2024](https://doi.org/10.4230/LIPIcs.MFCS.2024.46), **LIT-103** | Batch dynamic query maintenance with bounded-depth updates | DynFO / small-depth circuit updates, not optimal witness size of a Boolean DAG with state probes. |
| [Acar et al., ESA 2020](https://doi.org/10.4230/LIPIcs.ESA.2020.2), **LIT-104** | Work-efficient batched dynamic trees via change propagation and computation distance | Tree problems, expected update work, not old-root promise certificate probing. |
| [Kumar et al., ECOOP 2025](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20), existing LIT-010 | Differential execution and formal consistency of incremental programs | Does not establish our exact restricted certificate formula, but eliminates a broad "first batch incremental computation" claim. |
| [Aldema Tshuva–Oshman, ITCS 2026](https://doi.org/10.4230/LIPIcs.ITCS.2026.6), existing LIT-068 | Incrementally verifiable computation with updatable batch arguments | Computational cryptographic succinctness; unlike the information-theoretic read-probe model here. |
| [Nalli–Polisetty–Sarma, 2026 v2](https://arxiv.org/abs/2602.01042), **LIT-107** | Incondensability of certificate complexity via restrictions | Different condensation operation; v2 explicitly retracts a proof compared to v1; never import unverified claims. |
| [Kayal et al., ECCC TR26-206, 2026-09-22](https://eccc.weizmann.ac.il/report/2026/206/), **LIT-106** | Operational certification complexity, query-model characterizations and separations | Focus includes zero-error/exact quantum queries; not an asserted lower bound on our DAG batch operation. |

**Source validation ceiling:** official publisher/arXiv/ECCC abstracts and metadata checked; no full theorem-by-theorem PDF proof replication, Lean formalization or scholarly novelty certification. Source overlap means no broad novelty, but does **not** prove every narrowed resource model has already been solved.

## Verdict and next mathematical target

**HYP-103-BROAD = STOP_CLASSICAL_CERTIFICATE_REDUCTION.** A minimum-probe shared verifier given only an old root does not become a genuinely new theorem merely by naming the batch \`Delta\`, restricting f to a DAG, or introducing a "certifier" Rust crate.

The *only* conditional reopening is a materially different priced regime: bounded persistent metadata, authenticated *partial* old state, AND simultaneously optimized generator/verification work/size under a specific restricted function family, compared against ordinary shared change propagation and classic certificate complexity. Otherwise stop work and move to HYP-101 oracle time–space lower bound or HYP-105 fixed-support asymptotic separation with source-level novelty audit.

No new Rust, performance claim, production API, LENT/G2 changes, or cross-project work.
