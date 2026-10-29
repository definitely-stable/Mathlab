# Internal audit record for the universal sextic manuscript

Date: 2026-10-29. This is an internal mathematical and implementation
audit, not an external qualified referee report or a CI result.

## Latest-change analysis

The reviewed baseline is PR #671 at
`afe8d0ba78261397df2a68c12f927054ad368441`. The sequence #660--664 develops
coherent cycle/codegree identities and local original-D6 extensions.
The genuine fixed-map witness in #665 shows that the local fresh-extension
mass can vanish despite the same selected source graph and complete f.
#666 supplies a good completion by conditional expectation. #667--668
show that local extension mass, total D6, and total seven-class S have
different orderings on those finite completions. None gives a universal
fixed-map lower bound. #669--671 give uniform conditional means and exact
second moments under a randomly completed g; their stated probabilistic
scope does not settle the deterministic quantifier.

The present manuscript instead fixes both full maps, uses #659 to keep a
dense physical core, and introduces a random selector of original flags
only to transfer moment inequalities back to this fixed core. The output
is the deterministic asymptotic estimate for D6 plus B/B-overlap.

## Critical checks

1. **Conflict truncation:** full source books bound the NUMBER of deleted
   original IDs. Deleting a whole ID always deletes both diagonals.
   Neither step requires a bound on the number of original projection
   anchors lost: the later mixed estimate explicitly uses full anchors.
2. **Simultaneous path survival:** a proper short path has pairwise
   nonconflicting original flags. The event that all of them precede
   their combined closed neighborhoods is a sufficient event, even when
   those neighborhoods overlap. Subsequent coordinate cuts have the
   stated pathwise probability. No mutual independence of paths is used.
3. **Sixth moments:** the nonsimple-walk term is first bounded by
   `6 Delta tr(A^4)` and absorbed by spectral Cauchy. It is not discarded
   or directly estimated by `O(m Delta^2)`. Bipartiteness is used only for
   the coherent selected graph, where it is actually available.
4. **Core moment:** Jensen transfers the moment of PROPER two-paths;
   improper two-walks are separately controlled by the pencil books and
   maximum degree. This distinction is needed because the core itself
   need not be coherent.
5. **Odd coordinate returns:** these are included. The row identity
   `sum_x 1_x^T A0^3 1_x <= Delta sum_x ||A0 1_x||^2` controls them
   without assuming coordinate cuts on the dense core.
6. **Mixed internal blocking:** the kernel uses full `R(p,y)` and core
   `R0(u,y)`. The degree-product identity has one FULL and one CORE
   factor, so `Delta_core sum D_full` applies. Substituting two core
   factors would leave out genuine projection anchors and invalidate the
   argument. Internal independent checks confirmed the exponents
   `11/2`, `6`, `23/4`, and `47/8` in this order.
7. **Original GF(5) bridge:** the three appended projection flags and the
   three path flags are six distinct original IDs. Their two repeated
   factors meet at one flag, and each half is doubled pair plus disjoint
   C4. The unchanged historical classifier accepts them as B/B-overlap.
   At most two directed paths yield each sixset; equality holds on every
   produced finite sixset. This yields a SUBCOUNT of the historical class.
8. **Quantifiers:** T,K and all proof constants are fixed independently
   of h and the labels. The final result is uniform for all sufficiently
   large dyadic s, which is the stated Omega(s^6) Branch A assertion.
   A stronger positive minimum at every small h is not inferred.

## Reproducible finite evidence

The frozen fixture is generated from genuine source incidences, not
synthetic graph flags. For each row the paired core is built anew; every
produced original sixset is checked against the historical classifier.

| Full labels / retained core | Proper directed 3-paths | Unblocked paths | Distinct original B/B-overlap subcount | Unblocked paths using an anchor outside core |
|---|---:|---:|---:|---:|
| W32 lex / all 45 IDs | 1346 | 4 | 2 | 0 |
| W32 reverse-line / all 45 IDs | 1154 | 0 | 0 | 0 |
| W34 adversarial / all 425 IDs | 70476 | 10522 | 5261 | 0 |
| Same W34 labels / 283 IDs | 21214 | 3196 | 1598 | 2348 |

The full W34 path partition agrees with the earlier independently coded
weighted-endpoint oracle: missing 8306, incident 3440, original-end-bad
35616, good-endpoint internally blocked 12592, and unblocked 10522.
The sparse row specifically exercises full-source anchors outside the
retained core. Original-ID multiplicity is exactly two in every positive
row. Coordinate permutations preserve the complete new certificate.

Additional exhaustive falsifiers cover every 3-by-3 bipartite graph for
the sixth-moment absorption, and every four-vertex conflict graph with
every priority order and every prescribed independent 2/3-set for the
selector. These finite checks support the identities, not an all-h fit.

Run:

```sh
python -m unittest discover -s research -p 'test_hyp105_universal_sextic_obstruction.py' -v
python -m unittest discover -s research -p 'test_hyp105_full_physical_degree_tail.py' -v
python research/hyp105_universal_sextic_obstruction.py /tmp/hyp105-universal-sextic-obstruction.json
cmp research/fixtures/hyp105_universal_sextic_obstruction.json /tmp/hyp105-universal-sextic-obstruction.json
```

The complete manuscript and explicit constants remain subject to external
qualified mathematical review. No exact-head hosted CI result is asserted
here; publication does not change the issue's acceptance state.
