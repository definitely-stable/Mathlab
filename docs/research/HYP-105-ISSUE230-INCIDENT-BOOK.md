**STATUS: RESTRICTED_THEOREM_C.** This proves the incident-endpoint branch of the [universal projection reduction](HYP-105-ISSUE230-PROJECTION-CLOSURE.md). The nonincident doubled-anchor blocking branch remains open; no universal seven-family lower is asserted.

# Proper incident 3-paths force proper six-cycles

This is a universal graph inequality. It uses no unproved regularization or source-geometric assertion.

Let G be a simple graph on a subset of [a] x [a], with every edge changing both coordinates. Let H be any subgraph of G. Assume that for every vertex u and every coordinate value c, at most t neighbors of u in H have first coordinate c, and at most t have second coordinate c. Let m=e(G), M2=sum_v d_G(v)^2, and z be the number of six-cycles in H whose first coordinates are all distinct and whose second coordinates are all distinct. Let P be the number of oriented proper three-edge H paths whose endpoints are adjacent in G. Then

    P <= 24 t M2 + sqrt(192 m z).

Consequently

    z >= (P-24 t M2)_+^2 / (192 m).

## Mixed books and membership weights

For every unordered pair B={u,v} with distinct first and distinct second coordinates, put W_B=N_H(u) intersect N_H(v) and k_B=|W_B|. Call B large if k_B >= 20 t. A membership of B at a full G edge e={u,w}, with distinguished center u, means w is in N_H(v) intersect N_G(u). Its weight is k_B. The same definition applies with v as distinguished center.

For each proper unoriented H path u-b-c-w whose endpoints are adjacent in G, there are exactly two membership/leaf witnesses: book {u,c} with membership at e={u,w}, distinguished center u and leaf b; and book {b,w}, distinguished center w and leaf c. Thus the number P of oriented paths is at most the sum of all membership weights. Extra witnesses may be improper; using an upper count is harmless.

There are at most sum_w d_G(w)d_H(w) <= M2 memberships in total: choose mixed leaf w, its G neighbor u, and its H neighbor v. Therefore the total weight of memberships with k_B < 20t is at most 20t M2.

## Compatible large memberships

Fix a full edge e={x,y}. Each large membership has a center equal to x or y and an other center z. When the distinguished center is x, z is an H neighbor of y; when it is y, z is an H neighbor of x. Its weight is at most d_H(x) or d_H(y), respectively.

Two memberships are compatible when their other centers z1,z2 have distinct first and distinct second coordinates. All four fixed vertices x,y,z1,z2 then have distinct first and distinct second coordinates. For a fixed membership, incompatible memberships of the first type have total weight at most 2t d_H(x), and incompatible memberships of the second type have total weight at most 2t d_H(y). This includes the membership itself. Indeed all incompatible other centers lie in at most two prescribed coordinate blocks in the relevant H neighborhood.

Every ordered compatible membership pair B,C gives at least

    (k_B-8t)(k_C-10t) >= k_B k_C/4

proper six-cycle witnesses. Select a leaf of B avoiding the coordinates of the four fixed vertices (at most 8t excluded choices), then a leaf of C also avoiding the first selected leaf (at most 10t excluded choices). If both memberships have center x, the cycle is

    x - b_B - z_B - y - z_C - b_C - x.

If their distinguished centers are x and y, it is

    x - b_B - z_B - y - b_C - z_C - x.

The symmetric case with both distinguished centers y is identical. Every displayed edge belongs to H. The full G edge xy is an antipodal chord.

A proper six-cycle has at most three antipodal G chords. For a fixed cycle and chord there are at most four unordered membership pairs (two with a common distinguished center and two with different distinguished centers), hence at most eight ordered pairs, with their leaves determined by the cycle. Thus the number of ordered compatible pair/leaf witnesses is at most 24z. Summing the weights of compatible ordered pairs over full edges gives at most 96z.

## Bounding large-book mass

Let A_e be the sum of weights of large memberships at e={x,y}. By the incompatible-weight bound, the compatible ordered weight at e is at least

    A_e^2 - 2t(d_H(x)+d_H(y)) A_e.

Call e overloaded if A_e > 4t(d_H(x)+d_H(y)). Its compatible ordered weight is at least A_e^2/2. Therefore

    sum_overloaded A_e^2 <= 192 z,
    sum_overloaded A_e <= sqrt(192 m z).

For the remaining edges,

    sum_not_overloaded A_e
      <= 4t sum_{xy in E(G)}(d_H(x)+d_H(y))
      = 4t sum_v d_G(v)d_H(v)
      <= 4t M2.

Combining the small- and large-membership masses proves the displayed theorem.

## Application to the Kikuchi graph

If the full Kikuchi graph has M2=O(s^(11/2)), m=O(s^4), and block pruning gives t=s^alpha with 0<alpha<1/2, then t M2=o(s^6). Hence an incident-endpoint proper-path mass P>=eta s^6 forces z>=c_eta s^8, and in particular supplies the desired Omega(s^6) proper-D6 floor. This resolves only the incident-endpoint branch; the original-source nonincident completion and its blocking defects are separate.

## Complete uniform M2 bound for original W(3,s)

Write V=(s+1)(s^2+1), Delta=s+1, and let I be the V by V original point-line incidence matrix. The point collinearity graph C has strongly regular parameters

    degree s(s+1), lambda=s-1, mu=s+1.

Indeed a pair of collinear points has the other s-1 points on its line as common neighbors, while a noncollinear pair has one common neighbor on each of the s+1 lines through the first point. Thus

    I I^T = Delta Id + C,
    C^2 = (s^2-1) Id - 2 C + (s+1) J.

On the orthogonal complement of the all-ones vector the eigenvalues of C are s-1 and -s-1. Therefore the singular values of I are Delta on constants and sqrt(2s) or zero on their orthogonal complements. In particular, with E=I-(Delta/V)J,

    ||E||_op^2 <= 2s.

Let F and L be the a by V zero-one physical pair-incidence matrices for f and g. Each column has two ones; every row sum is at most a-1. The full Kikuchi degree matrix D is exactly F I L^T: an original incidence contributes one neighbor at every one of the four pairs of its physical endpoints, and injectivity prevents duplicate neighbors.

The matrix F F^T is nonnegative and its row sums are twice the physical star sizes, hence at most 2(a-1). Consequently ||F||_op^2 <= 2(a-1). Also ||L^T||_F^2=2V. If k_f=F1 and k_g=L1, then

    D = (Delta/V) k_f k_g^T + F E L^T,
    ||k_f||^2, ||k_g||^2 <= 2V(a-1),
    ||F E L^T||_F^2 <= 8s(a-1)V.

Using ||X+Y||_F^2 <= 2||X||_F^2+2||Y||_F^2 gives the explicit all-label bound

    M2(G)=||D||_F^2
      <= 8 Delta^2(a-1)^2 + 16s(a-1)V.

Since minimal a satisfies a-1 <= sqrt(2V)+1, for s>=2 one may use V<=2s^3, Delta<=3s/2, and a-1<=3s^(3/2). In particular

    M2(G) <= 162s^5 + 96s^(11/2) <= 258s^(11/2).

No average-label assumption or maximum Kikuchi degree O(s) has been used.

The [GQ spectral block refinement](HYP-105-ISSUE230-PROJECTION-CLOSURE.md)
proves that pruning at t=ceil(s^alpha), any fixed alpha>0, can retain
(1-o(1))*m edges and the (16-o(1))*s^6 proper path reservoir. In particular
alpha=1/10 is available, so the application above has no conditional
regularization assumption.

For explicit constants, let 0<alpha<1/2 and P>=eta*s^6. Since m<=6s^4
and t<=2s^alpha, the condition s^(1/2-alpha)>=24768/eta ensures
24tM2<=eta*s^6/2 and therefore

    D6(H) >= (eta^2/4608)*s^8.

This compensates incident closures only. The nonincident doubled-anchor
collision count remains unbounded in the required direction.

## More general endpoint relation

The same proof works for any undirected simple endpoint relation B whose pairs change both coordinates, even when B is not a graph supergraph of H. It only names potential antipodal chords; none of its pairs is used as an edge of a generated six-cycle. If P_B counts oriented proper H three-paths with endpoint pair in B, then

    P_B <= 24t sum_v d_B(v)d_H(v) + sqrt(192 |B| z).

For an anchor-blocking endpoint mask of size O(s^5), a negligible weighted small-book mass would force z=Omega(s^7). Merely knowing |B|=O(s^5) does not bound sum_v d_B(v)d_H(v) sufficiently.

## Source-count bound for endpoint anchor blocking

For a nonincident original endpoint pair (q,r), write its unique original length-three completion as q-l-p-r. If f(p) and f(q) share a physical coordinate, then p and q are distinct collinear points and physically adjacent pair labels. Conversely, every ordered such p,q on original line l, and each of the s original lines r through p other than l, gives a nonincident endpoint pair q,r with that same unique completion. Thus the exact number of these endpoint pairs is

    s sum_{l,x} r_{l,x}(r_{l,x}-1),

where r_{l,x}=|I(l) intersect P_x|. Injective physical pair labels share at most one coordinate, so there is no extra multiplicity in the sum. The GQ spectral bound gives

    sum_{l,x} r_{l,x}^2
      <= 4sV + 2(s^2+1)(a-1),
    sum_{l,x} r_{l,x}(r_{l,x}-1)
      <= (2s-2)V + 2(s^2+1)(a-1) = O(s^4).

The endpoint-pair count is therefore O(s^5). The point-line dual assertion applies to g(l) intersect g(r). A source endpoint pair determines only four oriented physical grid endpoint pairs.

This counts endpoint pairs, not H path multiplicity on them; it therefore does not yet prove negligible blocked-path mass. Internal physical coordinates in the completion anchor are an additional unresolved case.
