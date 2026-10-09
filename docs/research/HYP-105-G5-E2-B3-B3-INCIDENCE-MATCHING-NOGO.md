# HYP-105 G5-E2-B3.3 — A restricted all-h no-go for incidence-matched correlated pair labels

Date: 2026-10-09. Parent [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162). Follows [B3.2 exact D_s](HYP-105-G5-E2-B3-B2-COINCIDENT-CYCLES.md) and [B3.1 GF5 5643-flow certificate](HYP-105-G5-E2-B3-B1-CRITICAL-FLOWS.md).

**PROVED_RESTRICTED_ALL-h_STRONG_METHOD_NO-GO / HALL_PERFECT_MATCHING / EXTREMAL_DENSE_Ka_C6_COUNT / NO_UNIVERSAL_ASET_NO-GO / NO_GENERAL_CORRELATED_INJECTION_NO-GO / ORIGINALITY_UNVERIFIED.**

## 1. Freeze the restricted correlation class

Let s=2^h for every h>=1. The classical symplectic generalized quadrangle W(3,s) has V=(s+1)(s²+1) points and V lines, each point/line of degree Delta=s+1; N=V(s+1) incidence edges. Let a=min{r:binom(r,2)>=V}, K=binom(a,2). Fix ANY injection f from the V point vertices into the K physical edges of K_a (unordered distinct coordinate pairs), not necessarily lex or algebraic.

An **incidence-matched aligned pair labeling** means choosing a bijection pi from LINES to POINTS such that pi(l) is ON the line l, then setting the other half's physical pair injection by

```text
g(l) := f(pi(l)),
```

in the disjoint right block. This g is injective since f and pi are, but it is maximally synchronized with f on V selected matching columns. Nothing in the theorem asserts Sp(4,s)-equivariance: a lexicographic algorithm choosing pi depends on finite-field/basis ordering.

**Existence for ALL h:** The bipartite incidence graph has degree Delta on both sides. For every subset X of line vertices, the number of edges from X is exactly Delta|X|, all ending in N(X), each receiving at most Delta edges. Thus |N(X)|>=|X|. Hall's marriage theorem guarantees a perfect incidence matching pi. A deterministic lexicographic augmenting-path algorithm is given in [reference code](../../research/hyp105_g5e2b3b3_incidence_nogo.py); the all-h existence proof is the elementary regular-bipartite Hall theorem, not a numerical observation.

## 2. Dense coordinate palette forces many six-cycles

Because a is the **smallest** integer with K=binom(a,2)>=V, the image f(P) occupies all but r=K−V pair-edges of complete K_a, with 0<=r<a−1. The K_a graph contains exactly (a)_6/12 unoriented, unlabeled simple C6. Each **fixed physical pair edge** belongs to exactly (a−2)_4 such cycles: count the six-cycle edge incidences ((a)_6/12)*6, divide by K=binom(a,2), or directly place the remaining four distinct coordinates.

Deleting r edges removes at most r*(a−2)_4 cycles by the union bound (a cycle may be overcounted as removed but never undercounted). Therefore, for EVERY injection f:

```text
C6(f(P)) >= (a)_6/12 - (K-V)*(a-2)_4.
```

This lower bound may be clamped at 0 for small finite parameters, but for W(3,2^h), a=Theta(s^(3/2)), r=O(a), so the leading term is Theta(a^6) and the possible deletions only O(a^5). In particular C6(f(P))=Omega(a^6)=Omega(s^9), uniformly for all sufficiently large h, independent of which f is used.

## 3. Injection into real forbidden six-column events

Take any simple coordinate cycle C6 in the physical left graph f(P). Its six edges correspond, by injectivity, to six DISTINCT point factor vertices p_1,...,p_6 in cyclic order. Let l_i=pi^-1(p_i), the unique matched line containing p_i. Since pi is bijective, all six lines l_i are distinct, and every (p_i,l_i) is an actual symplectic incidence column. These six columns are a six-edge FACTOR MATCHING.

Under the aligned labeling g(l_i)=f(pi(l_i))=f(p_i), the right physical pairs are the **same** six coordinate pairs as on the left (in a separate block). Both dual column adjacency graphs are the same C6, with unique unordered alternating 3+3 sign partition. Every physical C6 gives a different six-column set; thus the exact D_s from B3.2 satisfies

```text
D_s(f, f◦pi) >= C6(f(P)).
```

The B3.2 all-h exact GF5 flow coefficient proves R3(B_s)>=5643*D_s/51^6. Combining yields our **restricted no-go theorem**:

```text
R3(B_s(f, f◦pi))
 >= (5643/51^6) * max(0, (a)_6/12-(K-V)*(a-2)_4)
 = Omega(s^9).
```

This holds for **EVERY** all-h sequence of injective f and incidence-perfect-matchings pi in the stated class, even if they vary adversarially with h. It contradicts the necessary target R3=O(s^(6-epsilon)) for every epsilon>0 and therefore **rules out exactly this natural incidence-matched-alignment class as a route to the existing risk-alteration proof of an improved ASET power**. It does NOT rule out other correlated coordinate embeddings, all possible GF5 weight choices, stronger independent-set extraction, or the original ASET conjecture.

## 4. Finite reproducibility; no exponent fitted from small s

The reference constructs a lexicographically deterministic perfect incidence matching in the accepted GF(2)/GF(4) symplectic incidence graph. It creates the physically two-block correlated map g(l)=f(pi(l)) and evaluates exact D_s via B3.2's non-C(N,6) cycle-incidence join.

Elementary all-injection lower floors:
- s=2: V=15, a=6, r=0; C6(K6)=60; necessarily D_s>=60. The exact incidence-matched verifier found **D_2=69**.
- s=4: V=85, a=14, r=6; C6(K14)=180,180, each omitted physical edge participates in 11,880 cycles, so D_s>=180,180−6*11,880=**108,900**. The actual left pair palette in accepted E2-A controls has 121,320 cycles, so the stronger finite D_s>=121,320 holds for this particular f. The exact incidence-matched verifier found **D_4=157,251**. Neither value is an extrapolated asymptotic power.

Independent hosted regression checks: Hall matching incident and bijective for real GF2/GF4 geometry; all-h integer lower algebra for s=2,4,8,16,32; complete GF2 / GF4 exact D_s and physical six-cycle lower; direct all-one GF5 signed cancellation for selected witness; direct brute on a small true factor-incidence subset. No claim that the finite enumeration itself proves the infinite lower — the proof is the Hall + missing-edge cycle union bound above.

## 5. Decision and next allowed direction

**STOP only the correlated class g=f◦pi.** A better candidate must *avoid forced physical pair identity on a perfect factor incidence matching*, while retaining global point/line injection. The next B3.2-C algebraic candidate can study finite-field traces, spread/flag structures, or genuine `GF(2^h)` symplectic invariants; prove all-h injectivity and absence of this alignment defect **before** computing risk. All other positive six-flow motifs and simultaneous R2/R3 all-h risk bounds remain OPEN. Do not assert a new ASET exponent, a universal pair-map lower bound, or scientific novelty without publication audit. No Rust or production code.
