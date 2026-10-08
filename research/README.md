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

## Evidence semantics

The exhaustive oracle searches unordered families of distinct nonzero columns. For the frozen grid (dge1), this loses no valid exact family: a zero column or duplicate column already violates singleton injectivity.

The oracle uses modular addition for q=2 and q=3 only. Those are prime fields. It does not pretend that integer-mod-q arithmetic implements every prime-power field.

A successful run means the frozen finite machinery is internally consistent on the checked cases. It does not turn an asymptotic claim into a theorem and it does not close the prior-art gate.
