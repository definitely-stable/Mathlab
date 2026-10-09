# HYP-105 G5-E2-B3.2-C — Plücker-indexed nonaligned pair injections (all-h) and exact finite D_s

Date: 2026-10-09. Parent [issue #176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169). Continues accepted [exact fixed-label D_s obstruction](HYP-105-G5-E2-B3-B2-COINCIDENT-CYCLES.md) and [restricted incidence-matched no-go](HYP-105-G5-E2-B3-B3-INCIDENCE-MATCHING-NOGO.md).

**PROVED ALL-h EXPLICIT INJECTION + NON-INCIDENCE-ALIGNMENT / EXACT FINITE GF2-GF4 D_s / NOT A PROVED D_s UPPER / NO SIMULTANEOUS R2/R3 / NO NEW ASET POWER / PLÜCKER INJECTION IS CLASSICAL.**

## 1. Mathematical construction for every h, not a finite-field fit

Let q=2^h, h>=1, and let P and L be points and totally isotropic lines of the **classical** symplectic W(3,q) in PG(3,q), with V=(q+1)(q²+1), N=(q+1)V, degree Δ=q+1. Fix a polynomial-basis encoding for GF(q) by the **lexicographically least monic irreducible degree-h polynomial over GF2**, with elements encoded as h-bit coefficients. This chooses an explicit total order of field elements and hence lexicographic order of normalized projective point representatives.

For a line spanned by two independent GF(q)^4 vectors u,v, define the six **Plücker minors** in lexicographic coordinate-pair order (01,02,03,12,13,23):

```text
P_ij(u,v) = u_i*v_j - u_j*v_i
          = u_i*v_j + u_j*v_i   (characteristic 2).
```

Normalize the first nonzero minor to 1, obtaining the projective exterior-square signature κ(L). Replacing the ordered line basis (u,v) with any other basis multiplies all six minors by the same nonzero determinant, so κ(L) is well-defined. Distinct projective lines give distinct κ(L): the 2D subspace is exactly `{w : w wedge (u wedge v)=0}`. This is the **classical Plücker/Klein embedding**, not a new theorem.

For this repository's symplectic form `<u,v>=u0*v2+u2*v0+u1*v3+u3*v1`, its isotropic lines additionally satisfy `P02=P13`. Independently all projective lines obey the Klein equation

```text
P01*P23 + P02*P13 + P03*P12 = 0.
```

The Python checker asserts these equations for every actual GF2/GF4 line and, independently, equality of κ(L) when using ANY two distinct spanning points of that line.

Define a point rank `r_P:P→{0,...,V−1}` by lexicographic order of normalized four-coordinates, and a line rank `r_L:L→{0,...,V−1}` by lexicographic order of κ(L). As a second control, replace κ(L) by its coordinatewise **Frobenius square** before sorting; since x→x² is a GF2-automorphism of GF(2^h), this remains a permutation of unique signatures. These ranks depend on the chosen field basis; they are NOT asserted to be Sp(4,q)-equivariant.

Let a be the smallest integer with binom(a,2)>=V, and `U_a(t)` the t-th lexicographic unordered pair among binom([a],2), for 0<=t<V. The physical left/right label maps have disjoint coordinate blocks:

```text
f(p) = U_a(r_P(p)),
g_t(L) = U_a((r_L(L)+t) mod V),    t in {0,...,V−1}.
```

Both injections are established by uniqueness of ranks and U_a; each incidence (p,L) gives a **distinct** split-2+2 support of four GF5 coordinates. GF(q) is used only for geometry, while checksum weights/flow equations stay in GF5.

## 2. All-h exact incidence-equality histogram theorem

Define the count of *aligned* incidence edges for any shift:

```text
E_t = #{(p,L) actual GQ incidence : f(p)=g_t(L)}.
```

For any fixed incidence, equality occurs exactly when `t ≡ r_P(p)-r_L(L) (mod V)`, a unique shift among V possible shifts. Summing over all shifts gives the exact identity

```text
Σ_{t=0}^{V−1} E_t = N = V(q+1).
```

Choose the **smallest minimizing** shift `t* = min argmin_t E_t`. The pigeonhole principle gives an all-h bound

```text
E_{t*} <= q+1.
```

This shift is determined by the actual finite-field incidence relation and the Plücker order; no random search or overfitting to D_s is performed. An incidence-matched aligned construction `g(L)=f(π(L))` for an incidence perfect matching π would require **at least V** equal-pair incidence edges `(π(L),L)`. But `V=(q+1)(q²+1)>q+1`. Therefore **the new minshift map cannot belong to the incidence-perfect-matching-aligned family ruled out in B3.3, for any h**, even if point/line labels are evaluated under arbitrary available field encodings.

This is a rigorous **restricted-family escape theorem**, not an upper bound on D_s: the coincidence of two C6 dual column graphs DOES NOT require equality of the left and right pair label of any individual column. Consequently E_t small can coexist with D_s large. No logical implication `E_t=O(q) ⇒ D_s=o(q^6)` is claimed.

## 3. Exact finite experiment and falsifiers

The [reference implementation](../../research/hyp105_g5e2b3c_plucker_shift.py) evaluates h=1 and h=2 by the accepted `symplectic_gq` oracle. **All-h mathematical** construction uses the canonical irreducible polynomial described above; current executable enumeration is intentionally capped at these two fields, since brute W(3,2^h) incidence enumeration is not a scalable runtime algorithm. Only the abstract definition and algebraic injection/nonalignment theorem hold for every h.

Three frozen cases per field:
- `plucker-lex-mincollision`: Plücker-ordered line ranks, smallest shift minimizing E_t.
- `plucker-frobenius-mincollision`: Frobenius-transformed Plücker keys, minimizing shift.
- `plucker-lex-zero`: same Plücker order, zero shift (negative/control arm; not asserted nonaligned).

For each case, the previous B3.2 **exact** C6-incidence join counts D_s without scanning `binom(N,6)`, and reports `5643 D_s/51^6` as a *lower* bound on true GF5 signed risk, not an upper bound. Further exact E_t and the minimization histogram are independently recomputed by direct incidence comparisons, and the previously accepted tiny-subset brute 6-column counter cross-checks the joined D_s. All field-degree/order/canonicalization claims are backed by tests, no 2-point exponent fitting.

**Crucial STOP gate:** even if the minshift maps show a lower D_s at GF2/GF4, this does not imply a uniform-in-h bound; and even an all-h `D_s=O(q^(6−eps))` would NOT imply full R3 control without classifying and counting all other positive six-flow motifs. Also the necessary simultaneous GF5 R2 target `R2=O(q^(26/5−eps_2))` remains unproved for this same map. Do NOT promote ASET exponent.

### 3.1 Exact GF2/GF4 results and a falsified risk proxy

The first hosted complete finite run checks **596 unit tests** and reports the following exact D_s on the three frozen Plücker arms (all N actual factor incidences; no six-subset sampling):

| Labeling | GF(2), s=2: selected shift / E_t / D_s | GF(4), s=4: selected shift / E_t / D_s |
| --- | --- | --- |
| Plücker lex, min-incidence-collision | 1 / 2 / **2** | 29 / 1 / **9,190** |
| Frobenius-Plücker, min-incidence-collision | 1 / 2 / **2** | 15 / 1 / **9,109** |
| Plücker lex, zero shift (control) | 0 / 5 / **6** | 0 / 9 / **9,103** |

The left physical pair graph contains exactly 60 C6 at s=2 and 121,320 C6 at s=4, because point ranks cover V different K_a coordinate pairs in ALL arms.

For scale comparison, the accepted E2-A controls at s=4 have `D_s=8,481` (lex), `8,417` (reverse-line), `10,602` (coordinate-flag). Thus the present Plücker min-incidence-collision candidates **do not improve** the best tested s=4 obstruction control. This comparison is only a finite observation.

**Concrete finite counterexample to a tempting but invalid surrogate:** At GF(4), the Plücker lex zero-shift has `E_0=9 > E_{29}=1` but `D_0=9,103 < D_{29}=9,190`. Hence minimizing point-line physical pair equality does **NOT** monotonically minimize coincident six-cycle obstruction D_s, even for the same original point and line ranks. The all-h nonalignment guarantee E_t≤s+1 remains valid; one cannot promote it to a strict R3 bound. **STOP using E_t as a quantitative proxy for D_s** without independent new structure.

## 4. Source-priority / novelty boundary

The Plücker/Klein line embedding, projective minors, isotropy and finite symplectic generalized quadrangles are classical mathematics:
- Simeon Ball, *An Introduction to Finite Geometry*, section 4.3 (symplectic generalized quadrangle; Plücker/Klein correspondence), <https://web.mat.upc.edu/simeon.michael.ball/IFG.pdf>.
- Standard Grassmannian Plücker embedding: the 2-plane is reconstructed from a decomposable wedge by `w wedge omega=0` (see e.g. *A novel procedure for constructing invariant subspaces of a set of matrices*, Annali di Matematica Pura ed Applicata, 2022, <https://link.springer.com/article/10.1007/s10231-022-01233-7>).
- The shift histogram and min-average lemma is elementary double counting and **not asserted globally novel**.

No proposed Sp(4,q) orbit compression, no uncharged canonical finite-field construction in runtime, and no claim that Plücker ordering is itself an extremal set-system theorem.

## 5. Next research proof gate

**B3.2-D:** choose ONE all-h Plücker/minshift model and develop upper bounds on its positive six-motif multiplicities using explicit geometry and field equations, not an independent-label expectation or two finite observations. Simultaneously establish an all-h per-label R2 bound for that SAME map. If this fails, test correlations stronger than rank permutations (Klein self-duality/spread, carefully handling that self-duality need not match selected physical pair ranks). **B3.1-B** still needs all other exponent-six positive GF5 motifs. Keep [#176](https://github.com/definitely-stable/Mathlab/issues/176) and scientific root issues OPEN; no Rust.
