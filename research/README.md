# Research harness

The research harness keeps the finite LENT-001 baseline executable with Python's standard library only.

It is not a substitute for the mathematical proof and it does not establish novelty.

## Run everything

```bash
python research/run_all.py
python -m unittest discover -s research -p "test_*.py"
```

Expected terminal markers:

```text
EXACT_ARITHMETIC_PASS
EXHAUSTIVE_PASS
FOUNDATION_PASS
```

## Artifacts

- `lent_exact.py` — exact integer definitions of (N_d(V)) and (B_q(m,r)), plus direct Hamming-ball count checks.
- `lent_exhaustive.py` — exhaustive tiny column-family oracle over the frozen prime-field grid.
- `lent-001/protocol.json` — machine-readable G0 contract.
- `test_lent.py` — regression tests, including the binary dependency mapping.
- `lent_hypergraph.py` — G2B signed-side forbidden-hypergraph oracle and exact/bounded branch-and-bound with rigorous unresolved-frontier upper bounds.
- `test_lent_g2b.py` — exhaustive independent hypergraph/ASET oracle checks, GF(7) legal +++ triple, minimality and solver regressions.
- `lent-001/g2b-protocol.json` — frozen G2B-A search/acceptance contract.

G2B-A historical run 37756386646 established exact q=3,m=4,w=2 value 7 and a q=5,m=3,w=2 interval [10,15]. G2B-B1 historically tightened GF5 to **[10,11]** using the classical
weak-Sidon bound. **G2B-B2 proves the exact optimum is 10** via globally
complete symmetry-normalized CNF and independently checked DRAT proof.
See docs/research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md.

- `locality_transition.py` — HYP-001 projective incidence and HYP-002 Steiner exact-column construction witnesses, including characteristic-two counterexamples.
- `test_locality_transition.py` — independent small-grid pair-sum checks and falsification cases.
- `lent-001/hyp001-002-protocol.json` — machine-frozen scope, field domains and evidence acceptance markers.

Run `python research/locality_transition.py` to produce five HYP-001/002
construction markers. CI checks only the finite witnesses, **not** the
asymptotic theorems or novelty claims.

- `hyp002_quadratic.py` — derived finite quadratic bound and necessary C4-free prefix-graph counting certificate.
- `test_hyp002_quadratic.py` — independent ASET-oracle checks, weighted rectangle collisions and C4-not-sufficient regression.

Run `python research/hyp002_quadratic.py` for Phase-B finite markers.
The asymptotic theorem is proved in docs/research/HYP-002-B-QUADRATIC-THEOREM.md;
CI checks instances only and does not establish scientific novelty.

- `affine_two_id.py` — canonical line-ID completion, promised <=2 active-ID decoder, trusted raw/checked transition boundary, dense vs direct memory accounting.
- `test_affine_two_id.py` — exhaustive 2,79,6904 state regressions and explicit 3-distinct versus 2-line alias.
- `bench_affine_two_id.py` — non-gating GitHub-hosted Python timing comparison with a direct two-ID baseline; NOT a Rust benchmark.
- `lent-001/hyp002-c-protocol.json` — frozen correctness/over-capacity/no-go criteria.

Run `python research/affine_two_id.py` and `python research/bench_affine_two_id.py` to reproduce; note that Python immutable raw-update copies O(m) memory even though three coordinate values change.

- `lent_weak_sidon.py` — G2B-B1 odd-group weak-Sidon integer upper, full finite pair-sum/difference-count verification and frozen GF5 witness; no invalid converse ASET mapping.
- `test_lent_weak_sidon.py` — exhaustive tiny-field mapping, GF(3) 3-cycle, sharp GF11 weak-Sidon fixture and fail-closed tests.
- `lent_g2bb_neighborhood.py` — exhausts direct additions (50) and one-delete/two-add choices (12,750) **only around the frozen 10-column witness**, not a global V=11 impossibility certificate.
- `lent-001/g2bb-weak-sidon-protocol.json` — frozen status and upper-certificate acceptance gates.

Run `python research/lent_weak_sidon.py` and `python research/lent_g2bb_neighborhood.py` for distinct rigorous-group-bound and local-only checks.

- `g2bb2_anchor_sat.py` — theorem-backed H-orbit single-anchor GF5 SAT reduction and pure-stdlib exact cardinality CNF.
- `g2bb2_decide.py` — optional bounded GitHub-hosted PySAT discovery with DRUP logs; UNKNOWN is not a negative proof.
- `g2bb2_verify.py` — independently reconstructs the entire 9,990-edge incidence, cross-checks source/CNF hashes and rejects unverified UNSAT.
- `test_g2bb2_anchor_sat.py`, `test_g2bb2_certificate.py` — 384 symmetry actions, small exhaustive truth tables, source independence and false-SAT/UNSAT protections.
- `lent-001/g2bb2-sat-protocol.json` — frozen global exactness decision protocol.

Run `python research/g2bb2_anchor_sat.py` for the no-extra-dependency model contract.
The separate GitHub Actions G2B-B2 workflow generated an UNSAT DRUP proof
for the complete anchored 11-family CNF; the independently built and
pinned drat-trim checker accepted it, yielding exact=10. The workflow
reproduces the full CNF, proof and verification on main; individual
timeouts still report UNKNOWN rather than spuriously overwriting the
previously verified result.

## Evidence semantics

The exhaustive oracle searches unordered families of distinct nonzero columns. For the frozen grid (dge1), this loses no valid exact family: a zero column or duplicate column already violates singleton injectivity.

The oracle uses modular addition for q=2 and q=3 only. Those are prime fields. It does not pretend that integer-mod-q arithmetic implements every prime-power field.

A successful run means the frozen finite machinery is internally consistent on the checked cases. It does not turn an asymptotic claim into a theorem and it does not close the prior-art gate.
