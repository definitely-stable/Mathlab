# Minimal-alphabet quotient-H pair charts, restored 2026-10-26

**Status: LEGAL_ALL_ODD_H_FAMILY; S_UNPROVED.** This restores the locally checked 2026-10-15 construction after the prior cloud filesystem was lost. The independent oracle has been reconstructed and rerun. Nothing here proves Branch B of issue 230, a universal Branch A lower, or a full GF5 risk upper.

## Exact source and alphabet

Let h>=3 be odd, s=2^h, D=(3h+1)/2, Q=2^D, N=s^3=Q^2/2, B=s^2+s+1, V=N+B. Let a be the smallest integer with binom(a,2)>=V and m=binom(a,2)-V, so 0<=m<=a-2 and Q<a. Use exactly a physical coordinates on each side.

For the symplectic form <x,y>=x0*y2+x2*y0+x1*y3+x3*y1, the affine source points and lines are

    P(u,w,z)=[1,u,z+u*w,w],
    L(d,c,b)=span((1,0,b,c),(0,1,c,d)).

Their exact incidence equations are w+c=u*d and z+b=u^2*d. There are N objects of each affine type and B remaining objects of each type. Order boundary points by first-nonzero-coordinate-one representatives, boundary lines by reduced row-echelon matrices, and all finite field elements by polynomial-basis integers.

## Charges and a deterministic bijection

Choose the first monic irreducible binary polynomial in coefficient-integer order to define each field. Fix 0<=r<=h and H=2^r. Let H_r in F_s span the first r basis vectors and U_j in F_Q span the first j+1 basis vectors, for j=r,h.

The Q core coordinates x in F_Q have fine charges eta_x=(x,x^3 mod U_r). Identify F_Q x (F_Q/U_r) with F_s^2 x (F_s/H_r) by the following explicit binary-linear map J_r. Concatenate the D bits of the first component delta and bits h+1,...,D-1 of the second component t. The first h and second h bits give the first two F_s coordinates. Bits r+1,...,h of t give bits r,...,h-1 of the third coordinate; its low r bits are zero. Dropping the third coordinate gives J_coarse(delta,t mod U_h). In particular the low h bits of delta are the first raw F_s coordinate.

For delta!=0 there are Q/2 unordered core pairs {x,x+delta}. Their cubic sums have affine-hyperplane image with linear part

    T_delta={t:Tr(t/delta^3)=0},

because x^3+(x+delta)^3=delta^3*((x/delta)^2+x/delta+1). Say delta is j-bad when U_j is contained in T_delta, and put b_j equal to their number.

For each delta slice, assign physical pairs to raw parameter triples as follows, always using lexicographic order within the stated sets.

1. If delta is not r-bad, each fine charge has H pairs. Bijection them to the H raw triples in that H_r fiber.
2. If delta is r-bad, half of its fine charges occur, each with 2H pairs. Assign the first H pairs to all H raw triples in the occurring fiber. Q/4 pairs and Q/4 raw triples remain.
3. If delta is r-bad but not h-bad, biject the leftovers separately within each coarse first-two-coordinate charge. Each coarse charge has half its fine fibers occurring, so leftover counts agree.
4. If delta is h-bad, biject the remaining Q/4 pairs and Q/4 raw triples over the entire slice. The first half already assigned in step 2 remains exact.

The absent delta=0 raw slice has Q/2 triples. There are exactly B+Q/2+m physical pairs involving at least one of the a-Q non-core coordinates. Assign their first Q/2+B pairs to that zero slice and then to the boundary objects; leave m pairs unused.

Apply the same algorithm separately to raw point triples (u,w,z) and raw line triples (d,c,b). This gives full deterministic injections f and g on the original symplectic GQ using its minimal alphabet. Numerical labels of equal raw triples may coincide between sides, whose physical coordinate blocks remain distinct.

## Exact declared error sets

For either map let E_rough comprise the boundary, zero slice and remapped Q/4 objects in every h-bad slice. Let E_fine additionally include the remapped Q/4 objects in other r-bad slices. Exactly

    |E_rough|=B+Q/2+b_h*Q/4,
    |E_fine| =B+Q/2+b_r*Q/4.                      (1)

Outside E_rough the first TWO raw fields equal sums of endpoint charges. Outside E_fine the full triple equals the endpoint sum modulo (0,0,H_r). Remapped objects can accidentally satisfy these identities; (1) counts declared exceptional sets, not a test of actual inequality.

Trace nondegeneracy gives

    b_j=#{delta!=0:delta^(-3) in U_j^perp}
        <=3*(Q/2^(j+1)-1).

If D is odd, cubing is a permutation, so b_j=Q/2^(j+1)-1. In this progression h=3 mod4,

    |E_rough|=(5/4)*s^2+s+1+Q/4,
    |E_fine| =s^3/2^(r+2)+s^2+s+1+Q/4.

Uniformly over all odd h>=3 the bounds are O(s^2) and O(s^3/H+s^2). Thus r=floor(epsilon*h), 0<epsilon<=1, gives a polynomially vanishing exceptional fraction. These exact all-h statements are about legal labelings and charge errors only.

## Why no seven-family upper follows

A physical degree-two sixset avoiding the relevant exceptions has sum u=sum w=sum d=sum c=0, and, if fine-exact, sum z,sum b in H_r. Incidence then gives sum u*d=0 and sum u^2*d in H_r.

For three repeated affine points, pair their two distinct affine lines and put D_i equal to the two d differences. Then D_i!=0, sum D_i=sum u_i*D_i=0 and sum u_i^2*D_i in H_r. Exactly two coincident u_i are impossible. Equal u_i give a rank drop; three distinct u_i give H-1 nonzero choices for the Vandermonde residual. That generic stratum compensates the proposed 1/H saving from repeated-point lift equalities.

The companion `HYP-105-ISSUE230-QUOTIENT-LIFT-EXPECTATION.md` proves an actual C/A expectation lower for independent regular-fiber lift permutations, with all source incidences and physical coordinate conditions retained. It does not exclude carefully correlated deterministic permutations. An arbitrary endpoint-additive completion of these quotient charges is also **not** covered by the older quarter-capacity theorem for linear projections of a Gold graph: nonlinear completion of the missing endpoint bits can leave that class.

The reconstruction oracle checks h=3,r=1,2 on the full minimal alphabet, all affine endpoint identities, every declared error set, the actual RREF source geometry, quotient triangle counts and a genuine generic-u C/A witness. The oracle does not count the full S of the lexicographic family.
