# HYP-105 #230 — D6-K: original signed-pressure boundary and spectral gate

**2026-10-13. RESTRICTED_THEOREM_C. Root Branch A/B OPEN.** Stacked on [Draft D6-J #409](https://github.com/definitely-stable/Mathlab/pull/409), pinned fully green parent 773ac86584fc143b41b5196db33def10ee67d2c8. The full original GF5-positive seven-class W(3,2) census is available; W(3,4) or W(3,8) BB-only lists are NOT complete positive denominators.

## 1. Exact all-finite / all-h pressure identity

Let I be the union of all ORIGINAL three-incidence source triples T carrying positive integral blocked oriented proper three-path multiplicities w(T). Both E endpoint-bad and I internal-only masses enter w(T), sharing the SAME target capacity. A consists of truly accepted ORIGINAL six-incidence sets Q from the SAME globally coherent injective f,g.

Define L(e)=sum over T containing e of w(T), d_A(e)=number of Q containing e, and p_K(e)=2L(e)-K d_A(e). For F subset I, put M(F)=sum over T subset F of w(T), D(F)=sum over e in F of d_A(e) and

    boundary(F) = sum over T with 0<|T intersect F|<3 of |T intersect F|*w(T).

**Exact identity for every F, every K>=0:**

    6M(F)-KD(F) = sum_(e in F) p_K(e) - 2 boundary(F).

Proof: summing L(e) over F counts every fully contained T three times and every crossing T exactly |T intersect F| times; subtract K D(F). D6-I maxflow/mincut therefore gives

    Delta6(K)=max_(F subset I) [sum_(e in F) p_K(e)-2 boundary(F)]_+.

The maximizing source family can be closed without decreasing deficit. This is an exact decomposition of the already established UNIFORM-port Hall dual, not the full recipient Hall equivalence or the root positive GF5 theorem.

The global candidate F=I has no boundary, so with C=sum_T w(T),

    G=6C-KD(I),    Delta6>=max(0,G).

Define exact local uniform Hall excess Hloc6=Delta6-max(0,G). IMPORTANT: D(I) can be STRICTLY less than 6S when a recipient has positive original incidences unused by any blocked source. Do not silently replace G by 6(C-KS).

## 2. Genuine source hypergraph boundary and Laplacian sufficient condition

Replace every ORIGINAL triple T by its three weighted incidence-pairs, each with weight w(T); call the weighted graph P. Every crossing T creates two crossing pairs, independent of whether its intersection with F has size 1 or 2:

    B_pair(F) = 2*sum_(T crossing F) w(T) <= 2*boundary(F).

Never reverse this inequality: the original directed partial boundary is larger for triples with two ports inside F.

Let N=|I|>=2, G=sum_I p_K(e), and the integer pressure variance numerator

    v=N*sum_I p_K(e)^2-G^2 >=0.

For k=|F|, centered Cauchy proves

    sum_(e in F) p_K(e) <= (G*k)/N + sqrt(v*k*(N-k))/N.

If lambda_2 is the weighted Laplacian algebraic connectivity of P, Rayleigh gives

    B_pair(F) >= lambda_2*k*(N-k)/N.

Therefore the *conditional* spectral inequality

    lambda_2^2*(N-1) >= v

implies for EVERY F that its Hall deficit is at most G*k/N, hence

    Delta6(K)=max(0,G).

This proves there is NO restricted local Hall excess under the quantitative source-expansion/pressure-variance hypothesis. It does not prove that ANY real high-h W(3,s) globally correlated f,g satisfies that hypothesis.

### Safe integer-only independent stronger certificate

A maximum-bottleneck spanning tree in P has weakest tree edge b, with b=0 if disconnected. Rayleigh, path Cauchy and the range-variance inequality imply

    lambda_2 >= 4b/[N(N-1)].

Thus the exact-arithmetic sufficient condition is

    16*b^2 >= v*N^2*(N-1).

A zero v certifies global-only regardless of graph connectivity. Failure of this *conservative* tree condition is NOT a mathematical counterexample to source expansion or to the original theorem.

**Nontrivial synthetic witness:** one ORIGINAL triple (0,1,2), w=4, K=1, accepted synthetic sixsets with incidence port degrees (7,9,8). Then p=(1,-1,0), v=6, b=4; the criterion reads 256>=108 and proves Delta6=0, even though a pointwise D6-H condition fails because p(0)>0. This is a finite synthetic test, NOT actual GF5-positive W(3,s).

If Delta6=max(0,G) AND every accepted original recipient port belongs to active source support I, then D(I)=6S, and by full D6-F recipient capacity and D6-H restricted embedding:

    D_full(K)=max(0,C-KS).

Both hypotheses are necessary for claiming this conclusion. Exact source-only G must not be confused with ordinary global pigeonhole loss without full port coverage.

## 2b. Stronger exact integral pair-flow calibration — avoids crude tree eigenvalue lower bound

The spectral tree condition may fail even when the true restricted Hall obstruction is *global only*. There is a strictly stronger, still exact-arithmetic CONSTRUCTIVE sufficient certificate on the same original source-pair graph.

For N>=2, set q(e)=N*p_K(e)-G, so sum_I q(e)=0. Replace each undirected original source-pair edge (u,v) of weight w_uv by two directed transport arcs of capacity N*w_uv in opposite directions. Source supplies are max(q(e),0), sinks absorb max(-q(e),0). Standard integral flow/mincut (with original pair capacities only) proves the following **if and only if** for this centered-pair requirement:

    an integer centered-pair flux exists, with div(g)=q
      iff for every F subset I,
        |sum_(e in F) q(e)| <= N*B_pair(F).

If it exists, sum_F p_K(e) <= (G/N)*|F|+B_pair(F) and B_pair(F)<=2*boundary(F); therefore

    Delta6(K)=max(0,G).

This is an ALL-finite sufficient theorem for uniform ORIGINAL-port Hall, stronger than the conservative tree gate. It is NOT necessary for no local Hall excess, because the ORIGINAL three-incidence boundary can exceed the symmetric pair projection.

Implementation reconstructs each nonzero signed integer pair flux and checks exact centered divergence and capacity. If infeasible, the residual cut F is a **fail-closed independent dual witness** with

    sum_(e in F)q(e) - N*B_pair(F) > 0.

This is an obstruction only to the PAIR calibration, not evidence against D6-I, full D6-D, or the GF5 theorem. No external numerical spectral library is needed; GitHub-hosted Python standard library suffices. Synthetic primal and dual witnesses are independently recomputed by explicit subset arithmetic.

## 3. The circularity obstruction is explicit

For every true positive recipient pool, without any geometric assumptions,

    D(I)=sum_(Q in A) |Q intersect I| <=6*S.

Consequently any claimed independent bound D(I)>=c*s^6 ALREADY implies S>=c*s^6/6 — essentially the very Branch A target. One must derive a new all-h estimate from the GF5 original seven-family and the true correlated pair injections, not assume uniform d_A(e) or extrapolate four W32 examples. A conditional Laplacian certificate alone does not close this logical gap.

## 4. Executable proof witnesses

The [implementation](../../research/hyp105_issue230_d6k_signed_pressure_boundary.py) computes pressure, directed ORIGINAL crossing boundary, weighted pair cut, integer variance, maximum-bottleneck tree, mincut and exact D6-F comparisons; any contradiction is fatal. The [tests](../../research/test_hyp105_issue230_d6k_signed_pressure_boundary.py) enumerate all 2^N ORIGINAL support subsets on small randomly generated systems and independently recompute the cut, including nontrivial spectral pass, strict local obstruction, unsupported and empty cases. A dedicated [GitHub-hosted workflow](../../.github/workflows/hyp105-issue230-d6k-signed-pressure-boundary.yml) evaluates the TRUE SAME-MAP full-seven GF5-positive W32 lex/reverse/S68/S72 instances.

In those four W32 full-G cases, the K_full-1 exact source-closed mincut is ALL 45 ORIGINAL incidences and its directed boundary is zero. Delta6=6*(C-(K_full-1)*S) and exact full D6-F exceptions are respectively 165,53,62,10. At K_full all Delta6=0. These finite facts are NOT a theorem for the actual high-h PR394 coherently retained H, whose tiny-s literal analogue may be empty. Full W34/W38 positive seven-class S remains unknown.

**Next D6-L:** obtain or falsify a TRUE W(3,s) geometry-bound for the pair-projection expansion relative to exact pressure variance for arbitrary globally injective correlated f,g, or use an alternative independent GF5 class identity. No fixed all-h K, nontrivial source exception asymptotics, Branch A/B or ASET exponent follows yet. Leave #230/#176/#169 OPEN, Draft PR, and main unchanged.
