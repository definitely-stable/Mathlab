# Branch B construction investigation for issue #230

Status: **OPEN_WITH_FORMAL_BLOCKER**, not `COUNTEREXAMPLE_B`. Research-only scoped results; no Branch A/B or full-risk claim.

I did not find an explicit infinite globally injected pair-label family with seven-family `S=o(s^6)`. The following all-h results rigorously exclude two natural geometric construction templates. They do not establish Branch A for arbitrary labels.

## 1. Literal source-geometric duads occupy only a vanishing fraction

Let each physical coordinate be assigned a TRUE point of `W(3,s)`. Call a physical pair geometric if its two assigned distinct points are collinear and its original line label is their unique isotropic join. Repeated physical coordinates assigned to the same source point do not increase the number of distinct original lines represented.

Let `X` be the set of distinct assigned source points, so `x=|X|<=a`. The original source point-collinearity graph has eigenvalues `s(s+1), s-1, -(s+1)`. Its largest nonconstant eigenvalue gives the exact spectral capacity bound

```
2 e_col(X) <= (s-1)x + (s^2+1)*x^2/V
             = (s-1)x + x^2/(s+1),
V=(s+1)(s^2+1).
```

Proof: write its adjacency matrix `A`, indicator `1_X=(x/V)1+z`, and use `z^T A z <= (s-1)||z||^2`; the coefficient of `x^2/V` is `s(s+1)-(s-1)=s^2+1`.

Each distinct represented original line consumes at least one distinct pair of points of `X`, hence the number represented is at most `e_col(X)`. Since minimal `a=(sqrt(2)+o(1))s^(3/2)`, this is `O(s^(5/2))=o(V)`. Thus an `o(V)` exceptional set cannot repair a literal join-of-two-source-points construction. The dual template, source points encoded as intersections of two actual original lines, has the identical bound by the source line-concurrency spectrum.

This proof does not require distinct physical-coordinate source assignments, source automorphism symmetry, or random labels.

## 2. Additive normalized Pluecker duads need a positive fraction of exceptions

Put the isotropic line Klein coordinates in the five-dimensional parabolic quadratic space

```
Q(x0,x1,x2,x3,x4) = x0*x4 + x1^2 + x2*x3
```

over `F_s`. Its nonzero projective singular vectors are exactly the `V` original isotropic line objects. Suppose arbitrary coordinate values `u_1,...,u_a in F_s^5` are given. A used physical pair `{i,j}` is called **additive geometric** if its original line's normalized Klein vector is `[u_i+u_j]` (the sum is nonzero and singular). Because the original line map is an injection, distinct additive geometric pairs have distinct projective directions.

For `s>=8` let `b` be the number of ALL physical pairs that are not additive geometric, including unoccupied pairs. Then

```
b > a^2/100.
```

In particular, if `t` occupied original line labels are exceptions to this additive template, then

```
t > a^2/100 - (binom(a,2)-V) >= a^2/100-a.
```

For `s>=32`, `a>=200`, so `t >= V/100`. Asymptotically `liminf t/V >= 1/50`. Hence even an `o(V)` repair cannot yield legal complete pair labels from this template.

### Proof of the positive-fraction bound

Let `G` be the graph on the `a` physical coordinates whose edges are additive geometric, and `H` its complement. Assume `b=|E(H)|<=a^2/100`. At least `4a/5` coordinates have `H`-degree at most `a/10`, by Markov's inequality. Three such vertices form a `G`-triangle: the third has at least `4a/5-2-2a/10>0` available choices. Since `s>=8` gives `a>=35`, all these inequalities are valid.

Write its coordinate values `u0,u1,u2`, and translate by `u0`. Set `v1=u1+u0`, `v2=u2+u0`. All three triangle differences are singular. Their projective directions are distinct by original-line injectivity, so `v1,v2` are linearly independent. They span a totally singular two-dimensional vector space `W`.

Every common `G`-neighbor `u` of the triangle satisfies `Q(u+u0)=0` and is orthogonal, for the polar form of `Q`, to both `v1,v2`. A nonsingular five-dimensional parabolic quadratic space in even characteristic has `W^perp=W+Rad(B)`, with one-dimensional polar radical having nonzero quadratic value. Thus the singular vectors in `W^perp` are exactly `W`, and `u in u0+W`.

There are at least `a-3-3a/10 >= 3a/5` common neighbors. Differences of two values in this affine plane have at most `s+1` distinct projective directions. Since all additive geometric pairs have distinct directions, among these common neighbors at most `s+1` pairs can be edges of `G`. Consequently

```
b >= binom(ceil(3a/5),2)-(s+1)
   >= 9a^2/50-3a/10-(s+1)
   > a^2/100.
```

The last inequality uses `a>=35`, `a^2>=2V>=2s^3`, and `s+1<=a^2/100` for `s>=8`. This contradicts the assumed bound. No near-complete additive geometric labeling exists.

The proof permits repeated values `u_i`: injectivity is used only on the actually geometric pair labels, so repeated coordinate values cannot evade it. It also permits arbitrary scalar choices of the projective line representative, since the assertion is about `[u_i+u_j]`.

## 3. Why an affine additive attempt is a separate, unresolved route

An affine chart of the genuine source has `s^3` points and lines with point parameters `(u,w,z)` and line parameters `(d,c,b)` and incidences

```
w+c=u*d,       z+b=u^2*d.
```

For example, in the repository's symplectic form take affine point `(1,u,v,w)`, isotropic line spanned by `(1,0,b,c)` and `(0,1,c,d)`, and put `z=v+u*w`. These give exactly the displayed relations; the chart discards only `O(s^2)` factors and `O(s^3)` incidences.

If line parameters themselves were exact sums of two coordinate values in the additive group `F_s^3`, then a six-coordinate Eulerian line projection would force the sum of all six `(d,c,b)` vectors to vanish. For a C/A source profile, writing the differences of each of the three line pairs as `D_i`, the equations imply

```
sum_i D_i = sum_i u_i D_i = sum_i u_i^2 D_i = 0.
```

The three-column Vandermonde matrix is nonsingular when `u_1,u_2,u_3` are distinct. Each `D_i` must then vanish, making the two original lines through a point equal, contrary to distinct original incidences. If exactly two `u_i` coincide, the first two equations force the remaining `D_i` to vanish, again impossible. Thus such a C/A or C/B sixset on the repeated-point side requires **all three `u_i` to be identical**.

There is a dual statement when point parameters are additive pair sums. Three repeated line factors with first parameters `d_i` and the corresponding nonzero point-parameter differences `U_i` satisfy

```
sum_i U_i = sum_i d_i U_i = sum_i d_i U_i^2 = 0.
```

Putting `U_3=U_1+U_2`, the remaining two equations have coefficient determinant `U_1 U_2(U_1+U_2)!=0`. They force `d_1=d_2=d_3`. Thus in either orientation of C/A and C/B the three repeated factors must have identical first parameter. These statements are genuine local algebraic suppression conditions, but not a full seven-family upper: B/A and aligned A/A remain, and no adequate global additive pair labeling has been supplied.

More precisely, for coordinate charges `A=(a_1,...,a_a)` in `F_s^3`, put

```
Sigma_2(A) = {a_i+a_j : i<j}.
```

If `t` original line labels are exceptions to additive affine encoding, at least `V-t` distinct original line parameter triples must occur in `Sigma_2(A)`. Hence necessarily

```
|Sigma_2(A)| >= V-t,
binom(a,2)-|Sigma_2(A)| <= (binom(a,2)-V)+t.
```

For an `o(V)` exceptional set this requires `s^3-o(s^3)` distinct group values from roughly `sqrt(2)s^(3/2)` coordinate charges with `o(s^3)` repeated pair sums. This is an approximate binary Sidon-type capacity problem, not automatically the exact maximum-Sidon-set problem. A standard APN graph supplies only `s^(3/2)` coordinates and half as many physical pairs as necessary (when the required field dimensions are integral). Enlarging its alphabet or using only a bipartite subset violates the minimal-alphabet requirement. No near-full-capacity construction or all-seven S bound is justified here.

Relevant primary sources inspected during the investigation: Babai and Sos, *Sidon sets in groups and induced subgraphs of Cayley graphs* (1985), https://users.renyi.hu/~sos/1985_Sidon_Sets_in_Groups_and_Induced_Subgraphs_of_cayley_Graphs.pdf; Czerwinski and Pott, *Sidon sets, sum-free sets and linear codes*, https://arxiv.org/abs/2304.07906; Thornburgh, *A new upper bound for Sidon sets in F_2^(4k+3)* (23 September 2026), https://arxiv.org/html/2609.27731v1. The latter primary paper explicitly retains a large lower/upper gap for exact Sidon sets; its constant-size improvement does not provide the needed near-full-capacity family. These papers do not settle the approximate capacity problem above, and arbitrary Branch B constructions need not use additive charges.

## 4. Independent local finite falsifiers

Run `python research/hyp105_issue230_geometric_duad_barriers.py`.

The checker verifies the exact sharp spectral inequality on **all 32,768 subsets** of the true W32 source point set. Its direct five-dimensional quadratic-space enumeration finds all 15 maximal singular planes for s=2 and all 85 for s=4 and exhaustively verifies each plane's common-neighbor rigidity. A separate true-source construction uses original symplectic point pencils and exterior minors, finding exactly the same plane sets without reusing the quadratic enumeration. It validates the affine chart pointwise against true W32/W34 source incidences, exhausts both orientations of the nonzero-three-wedge conditions for s=2,4,8 (solution counts 0,24,336 in each orientation), and checks the numerical constant inequalities for h=1 through 12. These finite checks falsify implementation/proof-lemma mistakes; the uniform statements rest on the algebraic proofs above.

No value of S, full R3, or ASET exponent is inferred from these construction obstructions.
