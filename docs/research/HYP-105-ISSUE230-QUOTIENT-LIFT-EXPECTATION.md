# Generic C/A expectation survives independent quotient-H lifts

Restored and audited locally 2026-10-26 from the 2026-10-15 argument. **Scope: independent random regular-fiber permutations only; no all-deterministic-lift lower.**

Use the parameters, maps and explicit J_r of `HYP-105-ISSUE230-QUOTIENT-CHARGE-FAMILY.md`. Write H=2^r, b=b_r, A=b+1. Fix all exceptional assignments. In every regular fine fiber choose a uniform bijection of its H physical pair objects onto its H raw lifts, independently across fibers and across f,g.

Let C_generic count C/A motifs with three repeated affine points of pairwise distinct first parameters u, six distinct affine lines, all outside the declared fine exception sets. Then

    E C_generic >= (2/3)*T*(1-L),
    T=(s^3/H)*s*(s-1)*(s-2)*(H-1),
    L=3A/s+3A/Q+3A/H+18/H.                       (1)

Since A<=3Q/(2H), if h tends through odd integers and H/s^(3/4) tends to infinity, then E S >=(2/3-o(1))*s^6. Thus independent large-H randomization does not prove Branch B; a large expectation alone does not exclude exceptional deterministic permutations.

## Ordered quotient triangles

In K=F_s^3/(0,0,H_r), of size M=s^3/H, set v(D,u)=(D,uD,u^2D+H_r) for D!=0. Count ordered triples Y_0,Y_1,Y_2 with successive differences v(D_0,u_0),v(D_1,u_1),v(D_2,u_2), all D_i nonzero and all u_i distinct.

Choose D_0!=0,D_1 notin {0,D_0}, D_2=D_0+D_1. The first two coordinates force u_2=(u_0D_0+u_1D_1)/D_2. The last-coordinate condition is

    (D_0D_1/D_2)*(u_0+u_1)^2 in H_r.

Each nonzero residual t in H_r gives one u_1 per u_0, and all three u_i are distinct. Translation of Y_0 is free. The exact count is T. Residual t=0 instead gives M*s*(s-1)*(s-2) equal-u triangles. The H-1 generic choices must not be omitted.

## Physical coordinates and source distinctness

A regular Y has H unordered representations eta_x+eta_y, a matching because eta_x contains x. Its 2H oriented representations have first endpoint uniform on an affine binary subspace of size 2H; the other endpoint is x+delta(Y).

Discard triangles with any nonregular Y_i (proportion at most 3A/Q), or any u_i in P={low h bits of a nonregular delta}, |P|<=A (proportion at most 3A/s). Translation makes each delta(Y_i) uniform. For fixed D_0,D_1,t, varying the common u_0 translates all u_i uniformly. The latter exclusion ensures every possible decoded point is in a regular fine fiber: its first field u is precisely the low h bits of its auxiliary delta.

Independently choose oriented representations Y_j=eta_(a_j)+eta_(a_j+delta_j). Form the physical right six-cycle

    (x0,x1,x2,x3,x4,x5)
       =(a0,a1,a2,a0+delta0,a1+delta1,a2+delta2)

with edges e_i={x_i,x_(i+1 mod6)}. Opposite edge charge differences are respectively Y_0+Y_1,Y_1+Y_2,Y_2+Y_0.

Discard representations with repeated physical coordinates, a nonregular physical cycle-edge direction, or two equal physical edge directions. Their total proportion is at most 12/H+3A/H:

* Twelve cross-opposite-pair coordinate equalities each have probability at most 1/(2H), giving 6/H.
* The six cycle-edge directions each have maximum point probability 1/(2H), giving 3A/H for nonregular directions.
* Opposite cycle-edge directions already differ: their difference has low h bits D_i!=0. Each of the other twelve direction equalities has probability at most 1/(2H), giving 6/H.

The maximum-atom estimates hold because sums of independent uniform affine-subspace samples of size 2H are uniform on an affine sum-subspace of at least that size. Six distinct auxiliary directions imply six distinct regular fine fibers.

## Exact b-lift equations and original C/A sixsets

Write the actual decoded lines l_i=(d_i,c_i,b_i). The quotient triangles give, for i=0,1,2,

    d_i+d_(i+3)=D_i!=0,
    c_i+c_(i+3)=u_iD_i,
    b_i+b_(i+3)=u_i^2D_i mod H_r.

The opposite lines meet the same affine point exactly when the three congruences in b are exact equalities. Their six independent uniform H_r lifts satisfy these three equations on disjoint variable pairs with probability exactly H^(-3). In particular this is not the false inference that two lines with identical (d,c) and different b meet.

On success define the actual source points

    p_i=(u_i,c_i+u_i*d_i,b_i+u_i^2*d_i).

Both l_i and l_(i+3) are incident to p_i by the exact two source equations. The three p_i are distinct because their u_i differ. The six l_i are distinct because their physical pair labels differ and g is injective.

Each of the three regular point fibers is a matching of H physical pair objects. Independent f permutations make their labels disjoint with probability at least 1-6/H: each fixed edge intersects at most two edges of another matching. Thus the six distinct original incidences {(p_i,l_i),(p_i,l_(i+3)):i=0,1,2} have precisely C/A original profiles, a right physical C6, and six degree-two physical coordinates on each side. They are actual accepted motifs avoiding every fine exception.

Every resulting physical right C6 with its opposite-edge repeated-point pairing has exactly twelve coordinate representations (six starts and two directions). Hence

    E C_generic >= ((2H)^3/12)*T
      *(1-3A/s-3A/Q-12/H-3A/H)*H^(-3)*(1-6/H),

which proves (1) when its right side is useful; otherwise (1) is trivial. The finite oracle checks the exact quotient-triple counts, a definition-level C/A witness and all H^6=4096 line-lift assignments in its H=4 example, of which exactly H^3=64 succeed.

The unproved deterministic direction is sparse stability: does o(s^6) actual C/A mass force approximate C4 cancellation of the physical edge lift function? Universal C4 cancellation would force endpoint-additive lifts, but this hypothesis is substantially stronger than the source-realized seven-motif condition. No removal theorem or capacity obstruction for arbitrary nonlinear endpoint completion is asserted.
