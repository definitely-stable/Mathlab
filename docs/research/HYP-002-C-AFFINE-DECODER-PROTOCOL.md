# HYP-002-C — affine two-ID decoder: theorem and product gate

Date: 2026-10-08. Status: RESEARCH FOUNDATION / NO PRODUCT GO.
Issue #34. No novel theorem or Rust crate is claimed.

## Exact restricted model

Let rank r>=1, m=3^r and coordinates be the points of affine
space F_3^r indexed as base-3 integers 0..m-1.

For two distinct points x,y, the point z=-x-y componentwise
modulo 3 completes a unique affine line L={x,y,z}.
The canonical ID of this line is the two smallest point indices
(x_min,x_second). Third-point completion requires O(r) integer
operations and **no V=m(m-1)/6-entry ID lookup table**.

A *promised state* represents a set S of at most TWO DISTINCT
active lines using dense trits:

    state[p] = |{L in S : p belongs to L}| mod 3.

The promise is part of the theorem, NOT something the trit vector
can authenticate.

## Decoding theorem (DERIVED, novelty unverified)

For any state produced by a valid promised S, a deterministic
decoder reconstructs S after one dense scan and no more than
C(6,3)=20 candidate checks:

- Empty: every trit is 0.
- One active line: exactly three 1-positions. The triple
  must satisfy x+y+z=0 componentwise modulo 3.
- Two overlapping lines: exactly four 1-positions and one
  2-position c (their unique intersection). Pair a 1-position
  u with its unique mate v=-c-u. Test the remaining two 1s
  as the second line through c; at most four candidates.
- Two disjoint lines: exactly six 1-positions. Enumerate up
  to 20 triples; retain any affine line whose complement is
  also a line. Canonicalize and independently re-encode.

Every candidate is verified by exact re-encoding. The
Steiner linearity lemma and HYP-002 ASET injectivity guarantee
a UNIQUE candidate for all promised states. Candidate
enumeration remains constant-size, but full state scanning
and Python immutable-array copying cost O(m). Algebraic
third-point completion costs O(r)=O(log m). Thus full
decoding is O(m+20r)=O(m), NOT O(1).

## Fundamental over-capacity impossibility

Three DISTINCT lines in F_3^2:

    (0,1,2), (0,3,6), (0,4,8)

and two OTHER distinct lines:

    (1,3,8), (2,4,6)

have IDENTICAL incidence sums modulo 3.

Therefore a decoder given only the nine trits cannot
always distinguish >2 active lines from <=2. This is
an information-theoretic ambiguity, not an implementation bug.

Even inserting the SAME line three times returns its
trit state to zero. No unguarded modulo-3 update API
can guarantee unique-membership semantics.

Laboratory APIs explicitly separate:
- trusted_raw_update: three arithmetic coordinate changes,
  NO membership/capacity check. This Python implementation
  copies the full length-m tuple, so its ACTUAL runtime and
  allocation costs are O(m), not O(3).
- checked_transition: decodes/scans before acting and
  rejects duplicate insertion, missing deletion and capacity
  violations WHEN the preexisting state obeys the promise.
  It costs O(m) per update and cannot reveal an already
  aliased invalid update history.

Extra trusted membership metadata would change both
the performance and storage budget; it cannot be free.

## Storage lower bounds and direct comparator

With V=m(m-1)/6 possible lines and at most two active,
the exact number of promised states is

    N=1+V+C(V,2).

Any lossless representation needs at least ceil(log2 N) bits.
The dense sketch ideally requires ceil(m log2 3) bits, or 2m
bits with basic 2-bit packing, or 8m bits as a byte array.

Without any V-size lookup table, the direct comparator
stores the first TWO point coordinates of each of at most
two canonical line IDs, using at most

    4*ceil(log2 m) + 2 occupancy bits.

This comparison is payload-only; real schemas and metadata
overheads would need to be compared on equal footing.

| r | m | V | Minimum bits | Ideal trit bits | 2-bit trit payload | Direct two-ID payload |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 9 | 12 | 7 | 15 | 18 | 18 |
| 3 | 27 | 117 | 13 | 43 | 54 | 22 |
| 4 | 81 | 1080 | 20 | 129 | 162 | 30 |
| 5 | 243 | 9801 | 26 | 386 | 486 | 34 |

Thus dense trits require Theta(m) bits, whereas
canonical storage for two IDs requires O(log m) bits.
Even ideal trit packing does not make dense state
storage-competitive for sufficiently large m.

The memory comparison is arithmetic, not a CPU benchmark.
No claims about real Rust runtime throughput are made.

## Frozen reproducibility acceptance

Primary source: research/affine_two_id.py
Independent tests: research/test_affine_two_id.py

- Exhaustively enumerate EVERY valid <=2-ID state for
  r=1,2,3: exactly 2, 79 and 6904 states.
- Check rank<=3 canonical pair and third-point geometry.
- Compare r=2 encoder states with an independent
  coordinate-count implementation and G1A exact oracle.
- Reject malformed shape, non-trits, noncanonical IDs,
  duplicate insertions, missing deletions, capacity overflow.
- Reproduce the explicit three-distinct-lines-to-two
  alias and triple identical-line wraparound.
- Produce bounded memory numbers for r=1..5.
- Retain G0/G1A/G2A/G2B/TOM/HYP-001/HYP-002 gates.

A passing finite CI proves neither generalized fail-safe
behaviour beyond the cardinality promise nor originality.

## Product decision and next direction

RECOMMENDATION: STOP_STANDALONE_DENSE_TWO_ID.

For the sole task of maintaining at most two IDs, there
is no practical reason shown to pay Theta(m) sketch
storage and Theta(m) validated updates when canonical
two-ID storage needs O(log m) bits and needs no V-table.

This is not a universal claim that sparse-update
additive sketches lack value. A different application
may require **composable state merge/subtraction** or
distributed updates with enforceable cardinality
guarantees. That workload must be specified, benchmarked
with full index/membership metadata, and tested against
direct exact baselines before opening a Rust crate.

Historical citations: Cheng et al.,
https://arxiv.org/abs/1507.00954 (separable codes);
Blackburn https://arxiv.org/abs/1505.02597.
These sources establish proximity of known coding
models, not originality of this restricted decoder.
