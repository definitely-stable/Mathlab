# LENT-001 / G2B-B1 — hosted weak-Sidon certificate evidence

**Status:** DERIVED NUMERICAL BOUND + INDEPENDENT FINITE WITNESS.
**Result:** **10 <= A_5^set(3,2,2) <= 11**, exact maximum **UNKNOWN**.
**Date:** 2026-10-08.

## Frozen protocol / theorem

See [G2B-B1 weak-Sidon proof](LENT-001-G2B-B1-WEAK-SIDON-BOUND.md)
and research/lent-001/g2bb-weak-sidon-protocol.json.
Primary source: Roth & Seroussi (1996), Location-correcting
codes, Lemma 5, DOI 10.1109/18.485724. ASET -> weak Sidon
is one-way. No claimed publication novelty.

## GitHub-hosted verification

- Run: https://github.com/definitely-stable/Mathlab/actions/runs/37770881915
- Checked branch SHA: 7208cc94f8a90257628046b705310d01232a03ad
- Conclusion: SUCCESS; **84 unit tests passed**; cross-repo
  catalog validation PASS, 61 indexed records.
- Legacy G0/G1A/G2A/G2B signed hypergraph/HYP/TOM
  checks all passed.
- New assertions:
  G2BB_WEAK_SIDON_MAPPING_PASS,
  G2BB_ODD_GROUP_BOUND_PASS,
  G2BB_GF5_INTERVAL_10_11_PASS,
  G2BB_INDEPENDENT_WITNESS_PASS,
  G2BB_SIDON_PHASE_A_PASS,
  G2BB_FROZEN_WITNESS_LOCAL_MAXIMALITY_PASS,
  G2BB_LOCAL_NEIGHBORHOOD_NON_GLOBAL_PASS.

## GF5 exact arithmetic

- q=5, m=3, w=2, d=2, **m>w**.
- Candidate columns: **60**.
- Minimal forbidden hyperedges: **9,990**.
- Original Hamming-ball upper: **15**.
- Classical weak-Sidon odd group bound: **11**, since
  S={0} union columns has cardinal s=V+1 and
  s(s-3)+1<=5^3=125. The integer step is 12*9+1=109,
  but 13*10+1=131>125.
- Existing independent 10-column ASET witness: VERIFIED.
- Deterministic G2B include/exclude search: 25,000 nodes,
  budget hit; search_exhausted=False, exact=False;
  reports lower=10, upper=11.

Independent ordered-difference audit on the 10-column
witness plus zero:
- |S|=11, N=125;
- 110 ordered differences over 98 represented nonzero
  group differences (excess 12);
- 12 colliding pairs of ordered-difference representations;
- 6 distinct centered arithmetic progressions,
  consistent with two collision pairs per progression;
- total 12 <= 2*11, as required by the lemma.

## Strong, but ONLY local, negative evidence

Every 11-column family reachable from the frozen
10-witness by either:
- one direct addition (50 possibilities); or
- removing ONE existing column and adding TWO
  (10 * C(51,2) = **12,750** possibilities)

was independently checked against the ASET sum oracle.
No valid 11-column family was found in this neighborhood.

**This is not a global impossibility proof.**
A different 11-column family could exist outside that
neighborhood; the certified exact optimum is not known.

## Gate decision

**G2B-B1: ACCEPT**, conditional on the final PR SHA
passing CI after documentation changes.
**G2B-B2: OPEN**. To close:
- demonstrate any independently verified 11-column
  family (then optimum=11), OR
- produce a globally complete, independently auditable
  impossibility proof for all 11-column families
  (then optimum=10).

A node cutoff, optimizer timeout, or failed local
neighborhood search never suffices for the latter.
No G4/new theorem novelty/Lean/Rust release is
authorized by this numerical bound alone.
