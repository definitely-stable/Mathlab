# LENT-001 / G2B-A — exact forbidden-hypergraph protocol

Issue: [#14](https://github.com/definitely-stable/Mathlab/issues/14)

Status: **G2B-A IMPLEMENTATION / AWAITING HOSTED EVIDENCE**.

Novelty: **NOT CLAIMED**. This is an exact finite combinatorial
calibration, not a sharp asymptotic theorem or an authorization to create a
Rust library.

## 1. Critical model correction

For d=2 an admissible set has size 0, 1, or 2. ASET-exactness is
injectivity of its modular subset sums. The only forbidden relations arise
from **two distinct admissible subsets** having equal sums.

After cancelling their intersection, any forbidden signed relation must
satisfy both n_plus <= 2 and n_minus <= 2. The number of nonzero entries
is at most four, but **a+b+c=0 with three positive terms is NOT in general
forbidden**.

Counterexample in GF(7): columns (1), (2), (4) sum to zero, yet their
subset sums of size <=2 are 0,1,2,4,3,5,6, all distinct. Any algorithm
that forbids this triple would return a potentially false low optimum.

This file supersedes the informal hyperedge examples in issue #14;
the issue must be corrected to match this frozen rule.

## 2. Formal forbidden-edge equivalence

Let C be the finite list of distinct, nonzero, support-at-most-w vectors
in GF(q)^m. Every index is a vertex. For each admissible index subset
A of size <=2, compute its exact modular sum.

For every pair of different admissible index subsets A,B with equal sums,
add the hyperedge E=A symmetric-difference B (nonempty). Since their
intersection cancels, E has size <=4, and the disjoint positive/negative
partition inherited from A,B has each side <=2.

**Lemma (both directions).** A chosen vertex family T is ASET-exact
through d=2 if and only if T contains no such forbidden edge.

Proof: If there is a collision of two subsets of T, their symmetric
difference is a forbidden edge contained in T. Conversely, any edge
arose from two colliding admissible subsets; after cancellation both
sides consist only of the edge's vertices. Hence if the chosen T contains
the edge, that collision persists. QED.

Deleting a forbidden edge E when a smaller edge F is a subset of E does
not alter independent vertex families; F already prohibits every set
containing E. The implementation computes and keeps only minimal edges.

**Important:** the implementation generates edges from admissible
subset collisions. It does NOT infer them from arbitrary field-linear
dependencies or from unbounded signed relations.

## 3. Exact/certified search

The solver examines each vertex by include/exclude branching.
Every branch is exhaustive. One branch may be discarded only when:

1. selected_count + available_count <= the incumbent (safe cardinality
   upper bound); or
2. inclusion would complete a forbidden edge; or
3. after an inclusion, a last remaining vertex of a nearly complete
   forbidden edge is excluded (forced exclusion).

Each edge containing the newly selected vertex is inspected; edges
containing an already excluded vertex are irrelevant. Excluding vertices
can disable an edge but cannot create a new collision. This justifies
incremental rather than whole-graph propagation.

The node budget is deterministic and is **not** a mathematical pruning
rule. On exhaustion, every pending subtree has upper bound
selected_count+available_count. The global Hamming-ball bound is also
valid. Therefore:

    lower = size of an independently verified witness
    upper = max(lower, maximum over pending subtrees of
                   min(LENT_global_upper, selected+available))

If the search exhausts the tree, or if upper=lower, the optimum is exact.
Otherwise the output is ONLY a certified interval. Runtime is not used
as evidence of optimality.

## 4. Frozen finite targets

| q | m | w | admissible candidates | node budget | required status |
|---:|---:|---:|---:|---:|---|
| 3 | 4 | 2 | 32 | 300,000 | exact optimum 7 |
| 5 | 3 | 2 | 60 | 25,000 | rigorous lower/upper interval |

Both cases have m>w. The q=5 phase-A lower bound must be at least 9;
the elementary LENT upper bound is 15. A stronger q=5 optimum is **not
claimed** until its search closes with certified proof.

Independent checks: compare hypergraph independence to the existing
G1A subset-sum oracle for every small-grid vertex subset; validate all
output witnesses against the independent oracle; verify minimal forbidden
edges; retain the legal GF(7) triple as a regression test.

## 5. Non-goals and next gate

No production code or dependency changes. G0/G1A/G2A protocols are frozen
and untouched. No general-purpose solver performance claim, novelty
claim, Lean formalization or Rust crate is implied.

G2B-A completion means a safe exact model and the first genuinely sparse
q=3 value, plus a certified (possibly broad) q=5 interval.

The remainder of issue #14 requires a *separately reviewed* G2B-B:
improved q=5 pruning/certificates, an exact or substantially tighter
interval, independent proof audit, and an explicit
G2_SELECT_THEOREM / G2_EXPAND_GRID / G2_REDUCE_TARGET / G2_NO_SIGNAL
decision. This file cannot authorize G4 theorem selection.
