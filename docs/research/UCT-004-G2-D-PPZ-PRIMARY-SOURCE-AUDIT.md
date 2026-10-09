# UCT-004 G2-D — primary proof audit: PPZ 1999 resolves witness bits, NOT exact κ

**Date:** 2026-10-09 · [G2-D issue #98](https://github.com/definitely-stable/Mathlab/issues/98) · [all-n proof](UCT-004-G2-D-ALL-N-PPZ-PROOF-BITS.md). **PROVED_DERIVED_CLASSICAL.** Source theorem text personally inspected; original external papers **not claimed fully reproved**. A stand-alone derivation of the *specific isolated-CNF lemma needed here* is given in G2-D.

## A. Two newly pinned primary publications (without duplicate preprint records)

1. **LIT-151** Ramamohan Paturi, Pavel Pudlák, Francis Zane (1999), *Satisfiability Coding Lemma*, Chicago Journal of Theoretical Computer Science 1999 Article 11, DOI [10.4086/cjtcs.1999.011](https://doi.org/10.4086/cjtcs.1999.011), [original author full text](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/PaturiPudlakZane_1999_cjtcs.pdf). **FULLTEXT_THEOREM_SPOTCHECKED**: the journal's early sections define isolated satisfying assignments and prove that a width-p CNF has at most 2^(n−n/p) isolated solutions via satisfiability coding/random variable ordering. **This is prior art, NOT a UCT discovery.** A self-contained PPZ reproduction establishes the narrow lemma Mathlab actually uses; no claim that we independently reconstructed every original article theorem.
2. **LIT-152** Gregory Emdin, Alexander S. Kulikov, Ivan Mihajlin, Nikita Slezkin (2022), *CNF Encodings of Parity*, MFCS 2022, DOI [10.4230/LIPIcs.MFCS.2022.47](https://doi.org/10.4230/LIPIcs.MFCS.2022.47), [official PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol241-mfcs2022/LIPIcs.MFCS.2022.47/LIPIcs.MFCS.2022.47.pdf). **FULLTEXT_THEOREM_SPOTCHECKED**: Section 1 Theorem 1 includes max clause width k≥n/(s+1) with s nondeterministic auxiliary variables, based on the PPZ lemma and depth-3 OR-of-CNF expansion. It uses s *auxiliary variables inside its CNF*; the width includes these variable appearances. It is invalid to identify their k automatically with our local read-budget p. Instead, for a **fixed** witness π, Mathlab forms its own width-p CNF **on only the n input bits**, and applies PPZ to each witness fiber individually.

**Closest modern overlapping certification:** **LIT-149** Kayal–Laplante–Larroque–Prūsis–Vihrovs 2026, *Certification complexity of Boolean functions*, arXiv:2609.26757/ECCC TR26-206; known randomized/quantum certificate complexity characterizations. **LIT-142** Aaronson 2008, **LIT-143** Ambainis et al. 2021 and **LIT-150** proximity proof length are additional prior-art barriers. The G2-D proof **does not** establish an original general proof-of-proximity or online-Merlin–Arthur theorem.

## B. Audited finite-model reduction chain

| Arrow | Logical status | Exact assumption/obligation |
|---|---|---|
| Private-coin soundness δ<1 + perfect completeness → p-separable witness fiber | **PROVED** in G2-C | One fixed π independent coins; soundness over every false input and π; finite X permits intersection of finitely many probability-one events; verifier probes ≤p **data** bits. |
| Fiber H → width-p Boolean CNF F_H, only data variables | **PROVED** independently in G2-D | For each false y choose separating p-coordinate set S_y; clause forbids that projection; F_H is satisfied by all H and by **no opposite-parity input**. |
| All solutions of F_H are isolated | **PROVED** | Flipping ANY one of n bits reverses parity, so cannot remain in F_H's satisfying set. |
| Isolated width-p CNF → |SAT|≤2^(n−n/p) | **PPZ 1999 PRIOR ART + INDEPENDENT NARROW REPRODUCTION** | Critical clause per variable, last-variable probability, Jensen, disjoint PPZ output events. |
| ≤2^b fibers cover 2^(n−1) equal-parity states | **PROVED counting** | Fixed b-bit witness, claimed answer excluded; parity classes size 2^(n−1). |
| b≥ceil(n/p)−1, matching block construction | **PROVED** | Full n,p, but constructed soundness δ=1−1/ceil(n/p) approaches 1, not constant. |
| Exact κ = 2^(ceil(n/p)−1) for nondivisible n/p | **STILL CONJECTURE** | PPZ lower κ≥ceil(2^(n/p−1)) may fall short of the upper. E.g. n=7,p=2 κ∈{6,7,8} but b_min=3 no matter which. |
| G2-D exact b -> practical proof or cryptographic security | **INVALID_TRANSFER / STOP** | Public verifier program size, all witness bits read, proof generation and updates, root authentication, network and CPU **not counted**. |

## C. Why this is not a new general scientific theorem

PPZ 1999 already establishes isolated-CNF cardinality at exactly the needed exponent, and MFCS 2022 treats closely related parity/auxiliary-witness and depth-3 CNF tradeoffs. Our operational cover-to-CNF bridge makes the Mathlab **G2-C exact bit-length parameter** transparent and resolves its *internal* previously open all-n b conjecture; it does not create a new fundamental proof-size theorem by renaming PPZ.

**STOP novelty promotion** for the unpriced parity witness-bit bound. **CONTINUE** exact cover number κ when n/p noninteger and fully charged online authenticated state/query/proof workload as separate tasks. A proof for exact κ must remain honest about the interval in Section V of G2-D and be checked against original circuit and SAT coding literature.

## D. Evidence-gated implementation and downstream scope

- [Proof with independent reconstruction](UCT-004-G2-D-ALL-N-PPZ-PROOF-BITS.md); [exact finite test oracle](../../research/test_uct004_ppz_all_n.py).
- Canonical literature imports LIT-151/152; deterministic forward/inverse bibliography and title-identity pins; dual entry preservation when main advances concurrently.
- KNOWN/STOP entries: all-n exact b = closed classical, general exact κ = open/warning, strong fully priced verification theorem = open.
- Only GitHub-hosted CI; all finite experiments are **falsification companions, not proof of an asymptotic theorem**. No production/Rust changes.
