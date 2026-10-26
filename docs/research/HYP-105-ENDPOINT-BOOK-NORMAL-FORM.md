# Recalled exact bad-endpoint population and the remaining weighted condition

**Prior accepted input, not a new theorem.** Root's source audit located
the exact identities in PR #427 / issue comment 6149741807 and PR #626 /
issue comment 6357916912. The purpose here is to restore their stronger
O(s^5) population estimate in the present normal form and independently
recheck the implementation. Do not publish this as a novel endpoint bound.

References: [PR #427](https://github.com/definitely-stable/Mathlab/pull/427),
[prior issue comment](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6149741807),
[PR #626](https://github.com/definitely-stable/Mathlab/pull/626),
[later issue comment](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6357916912).

For the same fixed source and labels as `HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md`, let
Omega={(q,r):q an original point, r an original line, q not incident r}.
Its cardinality is U=V(V-d)=s^2N. Every pair has the unique original
projection q--ell--p--r.

Let B_L be pairs for which f(q) intersects f(p), and B_R pairs for which
g(r) intersects g(ell). These are the original end-bad events, as opposed
to internally blocked physical paths. Then for EVERY h>=1 and EVERY
allowed correlated complete f,g,

    |B_L|=2s M_f,   |B_R|=2s M_g.                (E1)

Indeed each unordered collinear pair {q,p} with intersecting f-labels has
one original joining line ell and two orientations. Once p is the anchor,
choose r among the s lines through p other than ell. Original C4-freeness
makes q nonincident with r. This is a bijection to B_L. The dual argument
is identical. Thus

    |B_L union B_R| <=2s(M_f+M_g)<=4s C_s=O(s^5),
    rho:=|B_L union B_R|/U <=4C_s/(sN)=(4+o(1))/s.   (E2)

No disjointness of B_L,B_R is claimed. Their overlap can be substantial.
For s>=64 the convenient bound rho<=6/s follows from C_s<=1.5s^4 and
N>=s^4.

For ANY probability law nu on the SAME nonincident original endpoint
population Omega, let mu be its uniform law and

    chi2(nu||mu)=sum_(omega in Omega) (nu(omega)-mu(omega))^2/mu(omega).

The exact centered Cauchy bound is

    nu(B_L union B_R)
       <=rho+sqrt[rho(1-rho) chi2(nu||mu)].         (E3)

Therefore chi2=o(s) is sufficient for vanishing path-weighted end-bad
mass, if nu is the decoded endpoint law of the actual physical paths
being counted. An O(1) chi-square bound is stronger than necessary for
this endpoint event. Neither bound on chi-square is proved here.

The exact unweighted population count DOES NOT by itself bound the
weighted physical path mass. Individual endpoint pairs may support many
paths, and all maps in (E1)--(E3) are the same fixed f,g. Internal blocking
remains a separate issue even when (E3) is useful. Thus this corollary
does not close the root seven-family lower.

`exact_bad_endpoint_population` in `hyp105_full_physical_degree_tail.py` checks (E1)
in two independent ways on complete true W32/W34 labels: original-source
pair/book enumeration versus decoding EVERY nonincident original point--
line projection. Its results record the overlap and union separately.
