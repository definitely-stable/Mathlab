# HYP-105 B3.1-B2-B — completion of the leading six-coordinate repeated-factor-forest GF(5) templates

Date: 2026-10-10. Parent: [#176](https://github.com/definitely-stable/Mathlab/issues/176). Baseline: accepted [#214](https://github.com/definitely-stable/Mathlab/pull/214) (factor matching), [#218](https://github.com/definitely-stable/Mathlab/pull/218) (single cherry), and [six-forest projection polynomial](HYP-105-G5-E2-B3-FOREST-PROJECTION.md).

**SCOPE: complete finite six-coordinate LEADING necessary forest stratum, exact GF(5) full 51-pattern signed flows by integer dual Fourier, independently checked inclusion-exclusion and MITM. NOT complete 11,663-type general forests; NOT a fixed-label upper; NOT a new ASET exponent; NO claim of scientific priority.**

## 1. New structural reduction — only three six-coordinate half-projection types

Select six DISTINCT original incidences of W(3,s), s=2^h. Their factor incidence graph has girth eight, so is a forest. Independently inject original factor vertices on the left and right into unordered pairs of a physical coordinates; each selected column uses two physical coordinates in each color.

A positive GF(5) signed 3-vs-3 trade cannot contain a physical coordinate of incidence-degree one. In a physical block with exactly six distinct touched coordinates and six column occurrences, all coordinates therefore have degree exactly two. In the *dual multigraph* on the six named column IDs, every physical coordinate is an edge. A factor vertex repeated lambda times yields identical coordinate supports on lambda columns.

Hence the only possible partitions of six original factor-edge endpoints with exactly six leafless physical coordinates are:

- A: 1+1+1+1+1+1, dual simple C6 or 2C3; 70 named dual graphs, 1 physical-coordinate ordering divisor.
- B: 2+1+1+1+1, dual two parallel edges joining the repeated pair plus C4 on remaining columns; 3 named graphs per fixed cherry pair, divisor 2.
- C: 2+2+2, dual three disjoint doubled pairs; 1 named graph per fixed partition, divisor 2^3=8.

For fixed named factor endpoints, the count of physical coordinate injections is exactly (a)_6/d for the corresponding divisor d; never divide by the automorphism order of the original factor graph instead. A, B, C are **coordinate projection** types, not GQ subgraphs. Other multiplicity patterns can contribute when fewer than six physical coordinates are touched and are deliberately excluded here.

## 2. Exact enumeration of the remaining leading abstract forest cases

The accepted B3.0 forest-power audit lists 631 possible exponent-six named factor endpoint-partition pairs. Of those, A/A has 1, A/B+B/A has 30, and the NEW part has 600.

| Ordered color classes | Named forest endpoint partitions | Physical signed templates | Reduced fixed-left cases |
|---|---:|---:|---:|
| C/A + A/C | 30 | 21,000 | 70 x 10 |
| C/B + B/C | 360 | 10,800 | 12 x 3 x 10 |
| B/B, intersecting two repeated column-ID pairs | 120 | 10,800 | 8 x 3 x 10 |
| B/B, disjoint repeated pairs | 90 | 8,100 | 6 x 3 x 10 |
| **NEW** | **600** | **50,700** | **1,480** |
| Prior A/A plus A/B/B/A | **31** | **112,000** | accepted |
| **TOTAL leading** | **631** | **162,700** | all included |

Each full named template has 10 UNORDERED balanced sign masks, with global sign complement counted once. In C/B, the B pair MUST connect different C repeated-pair blocks; otherwise the same original incidence (same factor point and line endpoints) would appear twice. In B/B, the repeated factor pair on the right cannot equal that on the left for the same reason. Both intersecting and disjoint unequal pairs are admissible forests. These restrictions are on actual original factor edges, not a heuristic postfilter.

The fixed-left normalization uses 15 C partitions and two color orientations for C/A and C/B; for B/B it uses 15 choices of left repeated pair and 3 choices of left physical C4. The simultaneous column-permutation automorphism group is **48 for C** (C2 wreath S3) and **16 for B** (S2 x D8). It acts simultaneously on the other colored graph and on the balanced sign mask; physical colors never swap inside an orbit. All orbit masses are summed exactly, and the final named mass must equal 50,700.

## 3. Exact GF(5) certificate

For every signed orbit, reconstruct the six distinct support-four columns on twelve physical coordinates. Apply the accepted independent integer 782-dual-state GF(5) full-palette oracle from B3.1-B1b, with each column having 51 allowed nonzero checksum-4 weights, not unit-only GF(5). Sum orbit sizes times exact flow counts. Cross-check representative cases with two mathematically different prior independent methods:

1. Inclusion-exclusion on 2^12 contracted physical edges, including parallel edges.
2. Exact 51^3-per-side signed subset-sum meet-in-middle on actual supports.

The orbit certificate MUST report the complete zero/positive split, minimum/maximum nonnegative flow, total weighted sum, and separate B/B overlap/disjoint coefficients. The previous cherry B/A exact coefficient 3,902,064 for a single fixed physical C4 is a compulsory regression check. Source: [code](../../research/hyp105_g5e2b3b2b_leading_forests.py), [independent tests](../../research/test_hyp105_g5e2b3b2b_leading_forests.py).

### 3.1 Reproduced exact integer certificate (CI acceptance separately required)

The complete signed-orbit quotient was independently reproduced by a separate small Python implementation of the 782-state integer dual sum, including the accepted cherry regression 3,902,064; eight selected new representatives also matched the independent 2^12-edge GF5 inclusion-exclusion oracle.

| Class | Fixed-left signed orbits | Fixed-left named mass | All positive | Flow min..max | Fixed-left exact sum | Total named sum |
|---|---:|---:|---:|---:|---:|---:|
| C/A | 31 | 700 | 700 | 4,332..8,319 | 4,243,968 | 127,319,040 |
| C/B | 12 | 360 | 360 | 4,905..6,786 | 2,084,184 | 62,525,520 |
| B/B intersect | 17 | 240 | 240 | 5,175..5,535 | 1,287,120 | 57,920,400 |
| B/B disjoint | 21 | 180 | 180 | 4,501..8,310 | 1,116,160 | 50,227,200 |
| **Total** | **81** | **1,480** | **1,480** | **4,332..8,319** | — | **297,992,160** |

All **50,700/50,700 named signed templates** have strictly positive exact GF5 51-pattern flow. The displayed overall minimum is 4,332 (C/A); global maximum is 8,319 (C/A). This is an exact finite classification, NOT a claim that every fixed-label GQ family contains any given motif.

The exact signed coefficients per ONE fixed original factor-forest six-set, summed over possible six-coordinate physical graph types and all ten sign partitions, are:

```text
S_CA=4,243,968
S_CB=2,084,184 / 12 = 173,682
S_BB_intersect = 3 * 1,287,120 / 8 = 482,670
S_BB_disjoint = 3 * 1,116,160 / 6 = 558,080
```

The divisors 12, 8, 6 here count possible named original right-cherry pairs per fixed representative; they are NOT physical-coordinate automorphism divisors (those are 8,16,4 in the expectation probabilities). All five numbers including the previous fixed-left cherry regression are frozen as exact integers in source/tests; they must survive PR-head CI.

## 4. The uniform-in-h exact expectation identities once coefficients are certified

Write a=min{t:C(t,2)>=V}, K=C(a,2), V=(s+1)(s^2+1), and (z)_k=z(z-1)...(z-k+1). Let M_CA(s) be the ACTUAL total number of distinct six-incidence original forests of either orientation of C/A; analogously M_CB(s), M_BB_cap(s), M_BB_disj(s). Each forest is counted once with its unique factor-endpoint partitions. These counts are not the number of signed events, and the source does NOT currently give closed exact all-h formulas for them.

Let S_CA be the fixed-C/variable-A signed weighted sum; S_CB the fixed-C/fixed-allowed-B-pair sum over three physical C4 and ten signs; and S_BB_cap/S_BB_disj the sum over all three left and three right physical C4 and ten signs for any fixed corresponding pair-relation. The latter two are independent of the chosen pair through simultaneous named-column relabeling. They are nonnegative exact integers to be read from the signed census.

Then independent uniformly injective physical-pair labels and independently uniform 51-pattern weights satisfy exactly:

```text
E[R3_CA] = M_CA * S_CA * (a)_6^2 / [8 * 51^6 * (K)_3 * (K)_6]
E[R3_CB] = M_CB * S_CB * (a)_6^2 / [16 * 51^6 * (K)_3 * (K)_5]
E[R3_BB] = (M_BB_cap*S_BB_cap + M_BB_disj*S_BB_disj)
           * (a)_6^2 / [4 * 51^6 * (K)_5^2]
```

These are restricted signed-risk contributions, **not** global R3. The multipliers 8, 16 and 4 arise from indistinguishable physical coordinates in the B/C projections, and are independent of the number of abstract factor embeddings. **An additional all-h forest-embedding lower lemma** closes the *random-label* exponent for these classes. For ANY fixed two-colored abstract forest F with at most six distinct selected edges, c connected components and prescribed point/line sides, root each component and embed its vertices successively into the Delta-regular incidence graph (V vertices per side). For every s with V>12, Delta>12, choosing each root avoids at most 12 prior used vertices and choosing each tree child avoids at most 12 prior used vertices. Therefore there are at least (V-12)^c (Delta-12)^6 injective **labeled vertex embeddings**. Each six-incidence edge set can represent at most 12! such labeled embeddings, giving a valid (coarse) lower. The existing upper V^c Delta^6 is immediate. Thus the distinct-factor-forest counts of each nonempty class satisfy

```text
M_CA(s) = Theta(s^15), c=3;
M_CB(s) = Theta(s^12), c=2;
M_BB_intersect(s), M_BB_disjoint(s) = Theta(s^18), c=4.
```

These classes are nonempty for all sufficiently large s by the same greedy construction (without using an unproved Sp(4,s) action on physical labels). Since a=Theta(s^(3/2)) and K=Theta(s^3), the exact coefficient identities above with strictly positive S prove **E_independent_uniform_pair_labels[R3_class]=Theta(s^6) separately for C/A, C/B, B/B-intersect and B/B-disjoint**. This is an expectation-only method barrier, **not** a universal lower for fixed labels nor an improved ASET exponent. The root/child lower is deliberately weak for s<=12 and the asymptotic statement is for s=2^h tending to infinity.

All-h fixed-label corollary: if a certified class has a positive minimum exact F_min over all its possible positive signed events, it gives a restricted risk lower proportional to the ACTUAL fixed-map event multiplicity. It gives no universal lower on multiplicity and never an R3 upper.

### 4.1 New all-h fixed-label *necessary* obstruction (NOT an upper)

For any fixed injective point/line pair-coordinate maps f_s,g_s, let U_CA, U_CB, U_BB_intersect, U_BB_disjoint count the ACTUAL, DISTINCT original six-incidence factor-forest sets of each class whose two physical projections touch exactly six coordinates and have no degree-one coordinate. Because every one of their ten unordered balanced sign events is GF5-positive, the exact finite minima yield the uniform-in-h **necessary lower**:

```text
R3(f_s,g_s) >= [
  43320*U_CA + 49050*U_CB
  + 51750*U_BB_intersect + 45010*U_BB_disjoint
] / 51^6.
```

The four families are disjoint as original six-column sets; risk is a SUM of signed-event probabilities and no union-probability independence is asserted. This may be added to previous accepted disjoint matching six-cycle and one-cherry floors:

```text
R3 >= [5643*D6 + 45600*(U_B_left+U_B_right)
       + 43320*U_CA + 49050*U_CB
       + 51750*U_BB_intersect + 45010*U_BB_disjoint] / 51^6.
```

Here U_B_left/U_B_right specifically refer to accepted #218 single-cherry/6+6, and D6 to accepted matching aligned-C6 events. None of these U/D quantities currently has a proved universal Omega(s^6) lower valid for ALL deterministic f_s,g_s. This is therefore **not** a universal fixed-label obstruction, much less a full ASET upper.

## 5. Limits / remaining proof gate

- The other **11,032** leafless necessary factor-forest shapes (with smaller random-label upper exponents) are OPEN. Their counts may behave differently under exceptional correlated deterministic labels, so cannot be discarded from a fixed-label theorem.
- No all-h R2/R3 simultaneous strict **upper** for a SINGLE injective correlated map has been proved. In particular the accepted random-label expectation Theta(s^6) cannot be promoted to a per-label impossibility.
- The current exponent target remains R2=O(s^(26/5-epsilon2)), R3=O(s^(6-epsilon3)); either needs explicit positive epsilons for the SAME all-h map before any ASET power improvement is claimed.
- No Rust or cross-repository change; #176/#169/#162/#106/#95 remain OPEN.
- CI acceptance: exact PR-head full hosted Research SUCCESS, independent new exact flow/case-count tests, then postmerge main CI. Do not classify a submitted but unverified computation as accepted.
