# Independent acceptance audit: full physical-degree tail compensation

Date: 2026-10-26. Reviewed `HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md` in full, independently
of its finite selector implementation. The current source model is the
genuine W(3,s), `s=2^h>=64`, complete minimal-alphabet separately globally
injective typed f,g, with arbitrary correlation.

**Internal independent audit; qualified external review remains pending.**

**Verdict: checked as a scoped all-h global theorem.** No blocking
mathematical flaw was found. The argument proves a genuine same-fixed-map
D6 compensation estimate for the full physical-degree tail. It does not
prove the root seven-family lower bound.

## Constants and source accounting

The source book bound is valid: with source incidence matrix B and a
line-star indicator of size k, the nontrivial singular bound gives

```
||B 1_L||^2 <= 2s*k+(s^2+1)*k^2/V.
```

Summing coordinate stars and subtracting their first moments yields
`M_f,M_g<=C_s=(s-1)V+(s^2+1)(a-1)`. Global pair injectivity is used
exactly where required: every coordinate star has size at most a-1,
and two different physical pairs intersect in at most one coordinate.

For any selected original-ID set I, the conflict graph has exactly
`M_f(I)+M_g(I)` edges. A conflict at a shared source point cannot also
be a conflict at a shared source line for two different incidence IDs.
Thus there is no hidden factor two or source-pair overcount. An
independent set enforces both original-pencil matching properties.

Caro–Wei, followed by Cauchy–Schwarz, gives the source-ID independent-set
bound `L^2/(4C_s+L)`. The priority-order proof is valid on fixed maps and
does not randomize f or g. The stated minimum-current-degree greedy proof
is also valid: deleting its closed neighborhood removes reciprocal-degree
weight at most one, and all remaining reciprocal degrees increase.

For s>=64, `a^2<=4s^3`, `N<=2s^4`, `C_s<1.5s^4` are safe. In particular

```
L>=epsilon*s^4/2,
4C_s+L<=8s^4
```

give at least `epsilon^2*s^4/32` independent source IDs. Two coordinate
cuts retain at least a quarter, so beta=`epsilon^2/128` is valid.
These bounds do not use epsilon<=1; the theorem may indeed be applied
with the actual normalized tail `epsilon=E_T/s^4`.

Every chosen source ID retains both diagonals, including its preassigned
edge at the original full-H heavy set Q_T. Different IDs have different
physical witness edges. The heavy set is not recomputed after thinning.

## Balanced graph step

After the cuts, at least half of the witness edges have an assigned
heavy endpoint in one bipartition class R. With `r=|R|<=16s^3/T`,
partitioning the other class into chunks of size at most r uses at most
`2a^2/r` chunks. One actual graph F therefore has

```
v(F)<=2r,
e(F)>=beta*r*s/16,
e(F)/v(F)>=beta*s/32.
```

The condition `T>=2^20*C_graph^3*beta^(-3)` is exactly sufficient for
`e(F)>=C_graph*v(F)^(4/3)`. The proved balanced C6 theorem gives
`#C6(F)>=c_graph*(beta/32)^6*s^6`. No cloning is used, so there are no
cycles projecting to repeated original vertices. The graph F may split
diagonal pairs solely for counting: its edges still belong to the already
paired coherent graph G. Every simple C6 in G is coordinate proper by
the cuts and no-cherry conditions and maps injectively to a genuine
accepted original D6 sixset.

Consequently substitution of beta gives exactly

```
T>=2^41*C_graph^3*epsilon^(-6)
  and E_T>=epsilon*s^4
imply D6>=c_graph*epsilon^12*s^6/2^72.
```

For E_T>0 put epsilon=E_T/s^4. Either the threshold holds and the D6
bound can be inverted, or it fails and its threshold can be inverted.
This validates the maximum form of the pointwise estimate:

```
E_T/s^4 <= max{
  (2^41*C_graph^3/T)^(1/6),
  (2^72*D6/(c_graph*s^6))^(1/12)
}.
```

The zero-tail case is immediate. No clipping constant is needed.

## Provenance and remaining gap

The external graph input is a proved balanced supersaturation theorem,
not the general unbalanced conjecture. A primary self-contained proof
including the graph case is [Jiang and Yepremyan, *Supersaturation of even
linear cycles in linear hypergraphs*](https://arxiv.org/abs/1707.03091).
It is restated as Theorem 2 in [Vassilevska Williams and Westover,
*Listing 6-Cycles in Sparse Graphs*](https://arxiv.org/html/2411.07499v2#S1.SS1).
The source-to-D6 passage is the independently checked rainbow-C6
bijection of PR #652. No paired-subfield packet existence is imported.

Under `S_seven=o(s^6)`, this theorem gives uniform integrability of full-H
degrees at scale s. Whole-source deletion of the heavy tail loses at
most `2E_T` physical edges and leaves maximum degree at most Ts. Thus
one can keep an arbitrarily large fraction of the original full graph
at a fixed degree cap depending on that fraction.

This retained graph still may have coordinate cherries and no global
coordinate cuts. Enforcing those conditions can cost a fixed fraction.
Nor does bounded degree alone control the remaining coordinate-return
cycle mass or force another historical accepted class. A separate
global transversality/compensation statement is required to prove
Branch A. The root status must therefore remain open.

The finite selector tests are useful falsifiers of exact source-ID and
physical provenance, but are not used here as a proof of supersaturation
constants or of an all-h scientific conclusion. No remote action was
taken during this independent review.
