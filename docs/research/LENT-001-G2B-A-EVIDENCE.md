# LENT-001 / G2B-A — reproducible signed-collision hypergraph evidence

Status: **EXACT NUMERICAL RESULT** (q=3); **CERTIFIED INTERVAL**
(q=5). **NO NOVELTY CLAIM**.

Source protocol: [LENT-001-G2B-A-PROTOCOL.md](LENT-001-G2B-A-PROTOCOL.md)
and machine-readable research/lent-001/g2b-protocol.json.
Parent issue: [#14](https://github.com/definitely-stable/Mathlab/issues/14).

## Hosted evidence

- GitHub Actions run: [37756386646](https://github.com/definitely-stable/Mathlab/actions/runs/37756386646).
- Checked head commit: 0d3329e97d89605bce2df3980d7990fc9fcb9b45.
- Conclusion: SUCCESS.
- Unit tests: 34 passed, including exact graph-versus-ASET small-grid
  exhaustive checks and the GF(7) three-positive-term counterexample.
- All five G2B-A markers emitted:
  G2B_HYPERGRAPH_ORACLE_PASS, G2B_Q3_SPARSE_PASS,
  G2B_Q5_CERTIFICATE_PASS, G2B_WITNESS_PASS, G2B_PHASE_A_PASS.

## Exact/certified results (d=2, w=2)

| q | m | m>w? | candidates | minimal forbidden edges | nodes | optimum/result |
|---:|---:|---|---:|---:|---:|---|
| 3 | 4 | yes | 32 | 1336 | 107407 | **exactly 7** |
| 5 | 3 | yes | 60 | 9990 | 25000 (budget hit) | **10 <= A_5^set(3,2,2) <= 15** |

q=3 search exhausted all relevant branches, with only sound pruning.
The complete-search certificate is a deterministic, source-verifiable
algorithm plus CI result, not an independently checkable proof trace.
Its seven-column witness was independently validated using the G1A ASET oracle:

    (0,0,0,1)
    (0,0,1,0)
    (0,0,2,2)
    (0,1,0,0)
    (1,0,0,1)
    (1,2,0,0)
    (2,0,2,0)

q=5 produced a lower-bound witness with ten columns and a rigorous
global Hamming-ball upper bound 15. Search did NOT exhaust the tree.
Therefore the returned interval is correct, but **the exact optimum is
unknown**. The witness was independently checked by the original ASET
oracle:

    (0,1,1)
    (0,1,2)
    (0,1,3)
    (0,3,1)
    (1,0,2)
    (1,3,0)
    (2,0,4)
    (2,4,0)
    (3,0,0)
    (4,0,0)

## Correctness scope

For any frozen candidate list, the hypergraph lemma gives a mathematical
equivalence between ASET exactness and avoiding its minimal forbidden
edges; the solver's upper bound covers all unresolved branches.
Prime-field arithmetic only. The implementation also checks complete
small cases against an independent subset-sum oracle.

The q=3 exact number is not by itself a new asymptotic theorem.
Neither CI nor finite enumeration certifies scientific novelty.

## Next research gate

G2B-A: **ACCEPTED EXACT/CERTIFIED FOUNDATION** on the recorded run.
G2B as a whole is **OPEN**. Improve the q=5 upper/certificate with
auditable exact pruning or a verified alternative solver, then choose
G2_SELECT_THEOREM / G2_EXPAND_GRID / G2_REDUCE_TARGET / G2_NO_SIGNAL.
Do not start G4 or a Rust crate on the basis of this evidence.
