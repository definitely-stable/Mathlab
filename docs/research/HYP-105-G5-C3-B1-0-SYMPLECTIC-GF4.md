# HYP-105 G5-C3-B1.0 — Symplectic GF(2^h) geometry, proof and independent exact oracle

Date: 2026-10-09. Parent [#136](https://github.com/definitely-stable/Mathlab/issues/136), [#119](https://github.com/definitely-stable/Mathlab/issues/119), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95).

**CLASSICAL_INFINITE_GEOMETRY_REPROVED / INDEPENDENT_GF4_ORACLE / NO_NEW_ASET_EXPONENT / NO_PAIR_LABEL_BOUND_YET.** This is a genuine all-s **foundation**, not the new ASET lower construction. The distinction is indispensable.

## 1. Fully quantified theorem (all s=2^h)

Let F=GF(s), s=2^h, h>=1, and let V=F^4 with the nondegenerate alternating form

    B(u,v) = u_0 v_2 + u_2 v_0 + u_1 v_3 + u_3 v_1.

A point is a one-dimensional F-subspace of V. A line is a two-dimensional **totally isotropic** F-subspace (B(u,v)=0 for any u,v in the line). Incidence means containment.

**Theorem B1.0 (classical symplectic generalized quadrangle).** For every s=2^h, the geometry W(3,s) has exactly (s+1)(s²+1) point objects and as many line objects; every line has s+1 points and every point belongs to s+1 lines. For any point P not on line L, exactly one point of L is B-orthogonal to P and hence collinear with P. Therefore the bipartite point-line incidence graph has degree s+1, exactly (s+1)²(s²+1) edges and no cycles of length four or six (girth eight).

**Proof.** There are (s^4-1)/(s-1)=(s+1)(s²+1) projective one-dimensional subspaces of V. Fix P=[u]. The symplectic perpendicular subspace u^\perp has dimension three and contains <u> (alternation). The isotropic lines through P are exactly projectivizations of 2-dimensional subspaces <u,v> contained in u^\perp. Such lines correspond bijectively to one-dimensional subspaces of the 2-dimensional quotient u^\perp/<u>, of which there are s+1. Each projective line has (s²-1)/(s-1)=s+1 points. Double-count incidences to obtain equal numbers of point and line objects and E=(s+1)²(s²+1).

For P not on a totally isotropic line L, the restriction of B(u,·) to the two-dimensional vector subspace L is a **nonzero** linear functional: if it vanished identically, u would lie in L^\perp=L (a maximal isotropic/Lagrangian plane in nondegenerate symplectic dimension 4), contradicting P outside L. The kernel is one-dimensional and determines exactly one projective point Q on L with B(u,Q)=0. The span of u and Q is totally isotropic, hence they are collinear, proving uniqueness.

Two distinct projective points determine at most one projective line, so there is no 4-cycle of incidence. A 6-cycle would exhibit three pairwise distinct points and three pairwise distinct isotropic lines such that the points are pairwise collinear. Take any of the three points P and the opposite line L not containing P; the other two points on L would both be collinear with P, contradicting the proved uniqueness. A cycle of length eight exists for s>=2 (e.g. local quadrangles), and is independently witnessed by the finite GF2/GF4 oracles; therefore girth is exactly eight. QED.

**Priority:** This is long-established classical finite geometry, NOT an original Mathlab discovery. Official published related 2025 primary: [Abdukhalikov–Ball–Ho–Popatia, *Ovoids in the cyclic presentation of PG(3,q)*, Designs, Codes and Cryptography (2025)](https://doi.org/10.1007/s10623-025-01695-9), Section 2, explicitly states symplectic W(q) with parameters (q,q). The source works in a cyclic alternative model; we do NOT claim its novel ovoid results are ours. Older W(3,s) references already under Mathlab's LIT-136.

## 2. Machine-checkable GF(4) construction that is NOT Z/4Z

Use polynomial-basis GF(4)=GF(2)[x]/(x²+x+1). Elements 0,1,x,x+1 are integers 0,1,2,3 in the **polynomial coefficient** encoding, but arithmetic is not arithmetic modulo 4: x*x=x+1, and x*(x+1)=1. Addition is bitwise XOR. Multiplication shifts and reduces via the irreducible binary polynomial 0b111. Nonzero inverses use Fermat a^(s-2). Projective vectors use first-nonzero-coordinate normalization, quotienting by scalar action; any two distinct orthogonal normalized vectors define the projective line consisting of normalized representatives [u+t v] for t in F plus [v].

[GF(2^h) reference constructor](../../research/hyp105_b1_symplectic.py) exposes exact field arithmetic, 4D projective normalization, symplectic perpendicular, line spans, and a completely deduplicated projective incidence structure. Hosted finite certificates:

| Field | Projective points | Isotropic lines | Incidence edges | Regular degree |
| --- | ---: | ---: | ---: | ---: |
| GF(2) | 15 | 15 | 45 | 3 |
| GF(4) | 85 | 85 | 425 | 5 |

Both incidence graphs must have girth eight. The GF2 line sets are independently identified with the frozen W(3,2) fixture by translating projective point coordinates into 4-bit index words. GF4 is checked using all 85*(85-5)=6800 point-not-on-line instances: **exactly one** B-orthogonal point per nonincident isotropic line. This is a property oracle logically independent of simply counting line edges. Tests reject nonorthogonal generators, zero projective points, malformed scalar encodings and GF4 mistakes.

No 3^N full signed-oracle enumeration. GF4 GQ is a graph geometry over characteristic two, **NOT** a finite-field GF5 linear/ASET code. Mixing these fields would invalidate the mathematics.

Run in research GitHub CI:

    python -m unittest discover -s research -p "test_hyp105_b1_symplectic.py"
    python research/hyp105_b1_symplectic.py

## 3. The genuinely open proof step: pair-coordinate transport

For **each** s=2^h, a(s) is the least integer with binom(a(s),2)>=(s+1)(s²+1). Then a(s)=Theta(s^(3/2)). Need explicit **injective** assignments on both bipartite parts,

    f_s, g_s : {W(3,s) point/line labels} --> binom([a(s)],2),

forming N_s=(s+1)²(s²+1)=Theta(m^(8/3)) unit four-support GF5 columns with m=2 a(s). The mere existence of injections by pigeonhole (or a lexicographic rank mapping) does NOT prove useful signed-trade density; this is where originality is needed.

Define T4(s), T6(s) to count **distinct minimal actual** GF5 signed-trade supports of the resulting columns. In this unit restricted model only balanced 2-versus-2 and 3-versus-3 trades arise; an all-s upper on both (not simply a graph-girth claim) is needed. The classical alteration sufficiency gate for a strict power gain over the known A_lin lower 12/5 is

    T4(s) = O(m^b4), b4 < 52/15,
    T6(s) = O(m^b6), b6 < 4.

Neither uniform estimate is proved by the present source. In G5-C2, independent uniform random labelings actually give E[T6]>=Omega(m^4); expectation is NOT a universal lower. Exceptional duad/syntheme labels for s=2 cannot transfer by the full-K_a-duad correspondence to s>=3.

**Next alternatives beyond labeling:** Choose GF5 weights from an affine checksum hyperplane so subset cardinalities remain distinguishable, but trades can be destroyed by coefficients; or retain a graph candidate and derive hypergraph independent-set bounds using maximum degrees/codegrees rather than only T4/T6 totals. These need distinct proofs, independent finite falsification and complete prior-art checks. Do not claim GF4 incidence alone is a new lower bound.

## 4. Stopping conditions

B1.0 may be ACCEPTED if the algebraic all-s statement is proved, GF4 arithmetic validated independently and hosted exact-head CI is SUCCESS. This completes an **infinite classical foundation**, not the original ASET problem.

B1.1 or G5-D can claim a new ASET exponent only with a uniform infinite set of actually GF5 valid distinct subset sums and mathematically explicit constants/quantifiers. An improved maximum at m=12 cannot be extrapolated to all m. Parent #136/#119/#106/#95 remain OPEN.
