# HYP-105 issue230: corrected proof gate and sharp-order quartic source tensor

2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230), parents #176/#169. Independent main-based change, pinned base `179d4b93ae9aaea8f837a6aeb9bf4843380d5764`; no dependency on the unmerged C24 or K3 stacks.

**Status: RESTRICTED_THEOREM_C.** Exact finite counterexamples refute the proposed all-h P2/P7 unit-mean inequalities. Analytic proofs establish a sharper ALL-h source cap, its sharp exponent, global source-support mass, a half-random lower with explicit constant, and an unfiltered Cauchy method barrier. **Neither PROVED_A nor COUNTEREXAMPLE_B.** No total GF5 R3 upper, new ASET exponent, or Lean formalization. GitHub-hosted acceptance is tracked separately from mathematical review; no merge authorized by this document.

## 1. Frozen model, source, and target

Let s=2^h, h>=1, V=(s+1)(s^2+1), Delta=s+1, a=min{b:C(b,2)>=V}, K=C(a,2). P,L,E are the ORIGINAL point/line/incidence objects of W(3,s). Physical f:P->E(K_a) and g:L->E(K_a) are arbitrary global injections, possibly correlated. Physical pair labels are objects distinct from original points/lines.

For an unordered sixset R of DISTINCT original right lines, w_f(R) counts DISTINCT unordered original six-incidence sets with right endpoint set R, original left profile (2,1,1,1,1), and six LEFT physical coordinates each of degree two. Let H_f=sum_R w_f(R). Accepted B1-A gives H_f=(1/4+O(1/s))*s^15, uniformly f. Define T_a as the 70*C(a,6) simple six-edge 2-factors on six physical coordinates. Then exactly, for every fixed correlated f,g,

    U_BA(f,g) = sum_R w_f(R) 1[g(R) in T_a].
    rho_a = 70*C(a,6)/C(K,6);  mu_f = rho_a*H_f.

The equality is an original-incidence bijection, not a randomization assumption. Under one uniform global g, mu_f is the expected U_BA. All-h source mass and random mean are accepted in [B1-A](HYP-105-G5-E2-B3-E1B1A-ONE-SIDED-UNIVERSAL.md); the exact overlap is [C0](HYP-105-G5-E2-B3-E1C0-WEIGHTED-OVERLAP-TRANSFER.md). They do not provide a minimum over g.

## 2. ALL-h exact original-anchor quartic identity

Fix R. A source witness has a unique doubled original point p, and a unique pair B={l,l'} of its original right lines meeting at p. GQ partial linearity determines p from B. Denote the remaining four DISTINCT original lines by r1,r2,r3,r4. Let X=[a]\f(p). For each i define the symmetric zero-diagonal 0/1 matrix A_i on X:

    A_i[x,y]=1 iff the original point q on r_i has f(q)={x,y}.

An edge image has a unique point origin because f is injective. An original point shared by different residual lines yields the same physical edge in several matrices; this overlap is retained, not assumed absent.

Define the precise quartic tensor contraction

    C(A1,A2,A3,A4) =
      sum over sigma in {(1,2,3,4),(1,2,4,3),(1,3,2,4)}
      sum over DISTINCT x0,x1,x2,x3 in X
        A_sigma1[x0,x1] A_sigma2[x1,x2]
        A_sigma3[x2,x3] A_sigma4[x3,x0].

Then, for every h and every f,

    w_f(R) = sum_{B subset R, B concurrent} C(A1,A2,A3,A4).       (Q1)

**Proof of multiplicity.** A physical simple C4 with one edge for each named residual original line determines four distinct original point origins. None is p, since both coordinates of f(p) are excluded. Together with (p,l),(p,l'), these give exactly one B-left source witness. Conversely a witness reconstructs the physical square, its four named line colors, and the unique doubled point/anchor pair. There are three unoriented cyclic orders of four named colors. Fixing a representative order and starting with color 1 fixes the starting edge and its orientation. Therefore one colored square contributes ONE, without a factor 2,4,8 or 4!. Distinct assignments of original lines to a square produce different original-incidence sets and must remain distinct. Anchors cannot double-count a witness, even when three or more lines of R meet at one point: the selected pair at the doubled point is uniquely reconstructible. This proves (Q1).

## 3. ALL-h source cap improves Delta^4 to Delta^2

Use the unnormalized Frobenius norm ||A||_F^2=sum_{x,y}A[x,y]^2. Each A_i has at most Delta distinct edges, so ||A_i||_F^2<=2Delta. For one cyclic order,

    0 <= distinct-vertex trace <= tr(A1 A2 A3 A4)
       <= ||A1||_F ||A2||_F ||A3||_F ||A4||_F
       <= 4 Delta^2.

The middle inequality follows from Frobenius Cauchy-Schwarz on A1A2 versus (A3A4)^T, followed by Frobenius submultiplicativity. Dropping the distinct-coordinate selector increases the nonnegative integer sum. Thus every anchor contributes at most 12Delta^2. If e_GQ(R) counts concurrent ORIGINAL line pairs among R, then for all s=2^h and all f,

    0 <= w_f(R) <= 12(s+1)^2 e_GQ(R).                         (Q2)

Two further independently proved bounds may be combined with it:

    w_f(R) <= min(Delta^4,12Delta^2,6*C(a-2,4))*e_GQ(R).       (Q3)

The Delta^4 term counts at most Delta choices on each residual original line. For the final term there are at most3*C(a-2,4) physical squares outside f(p). A 4x4 original incidence submatrix has permanent at most2: two different matchings must differ along one alternating C8; a third matching would make an even relative permutation between two odd four-cycles, contradicting girth eight. Each square therefore contributes at most2 original assignments per anchor. This proof is self-contained and agrees with the independently developed [Q draft](https://github.com/definitely-stable/Mathlab/pull/390); its code is not imported here.

Since e_GQ(R)<=15, max_R w_f(R)<=180Delta^2. Combining (Q2) with the UNIFORM H_f asymptotic proves

    |support w_f| >= H_f/(180Delta^2)
                  >= (1/720+o(1))*s^13, uniformly in f.       (Q4)

This strengthens main's previous Omega(s^11) source-support lower by two powers. It does not imply a target intersection lower for arbitrary g.

## 4. The Delta^2 exponent is sharp: explicit ALL-h extension

For every s=2^h>=8 choose two original lines l,l' meeting at p. Greedily choose four further lines r1..r4, mutually skew and skew to both anchor lines. The original line-intersection graph has degree d=s(s+1). At the last choice at most5(d+1) lines are excluded, while

    V-5(d+1)=s^3-4s^2-4s-4>0  for s>=8.

Thus the six-line R has exactly one concurrent pair. Its four residual line point sets have 4Delta DISTINCT points, all different from p. There are enough physical symbols for u,v,b1..bDelta,c1..cDelta,z,z', because

    V-C(2s+5,2)=s^3-s^2-8s-9>0 for s>=8,

so the minimal a>=2s+6=2Delta+4. Assign f(p)={z,z'}, and assign the points of the four residual lines bijectively to

    r1: {u,bi},   r2: {v,bi},
    r3: {v,cj},   r4: {u,cj},       i,j=1..Delta.

All4Delta+1 assigned physical pair objects are different. Extend to every remaining original point by unused pairs, possible since K>=V. The only physical colored squares are u-bi-v-cj-u. There is exactly one witness for each ordered pair (i,j), hence

    e_GQ(R)=1,  w_f(R)=Delta^2.                              (Q5)

This is an ALL-h sharp-order source construction, not a construction with small total S. No right map suppression is established.

There is also an ALL-h zero-source construction for s>=8 on the same R. Let f(p)={0,1}; assign the4Delta residual points to different pair objects meeting{0,1}, excluding{0,1}. There are2a-4 such pairs. For s>=4,

    V-C(2s+3,2)=s^3-s^2-4s-2>0,

so a>=2s+4 and2a-4>=4Delta. After extension to a global injection, all four matrices restricted to X=[a]\{0,1} vanish. Therefore

    e_GQ(R)=1,  w_f(R)=0.                                   (Q6)

This rules out every strictly positive pointwise lower from e_GQ(R)>0. It leaves the global support lower (Q4) intact. The independent finite W34 certificate handles s=4 as well; the general existence proof is stated for s>=8.

## 5. Exact trace correction and independent finite falsifiers

Full traces are upper bounds, not equal to source counts. For one order write d_ij(x)=sum_y A_i[x,y]A_j[x,y]. Exact inclusion-exclusion gives

    T_simple = tr(A1 A2 A3 A4)
             -sum_x d12(x)d34(x)-sum_x d23(x)d41(x)
             +sum_{x,y} prod_i A_i[x,y].                    (Q7)

Adjacent vertices cannot coincide because all matrices are loopless. The only non-simple four-walks have x0=x2 or x1=x3; their intersection is the last term. For binary matrices that term equals twice the number of physical edges shared by all four colors. Repeated original points are thereby excluded without assuming independence or disjoint pencils.

The new implementation computes (Q7) using sparse two-path matrices. Tests compare it to direct edge assignments on independent finite colored graphs and to the existing ORIGINAL six-incidence source generator on every one of the5005 W32 original right sixsets, for lex and the correlated S68 f. True W34/W38 fixtures independently check source point products:

| s | actual original R | e_GQ(R) | sharp weight | zero weight |
| --- | --- | ---: | ---: | ---: |
| 4 | {0,1,22,27,32,38} | 1 | 25 | 0 |
| 8 | {0,1,74,83,92,101} | 1 | 81 | 0 |

Every map assigns ALL V original points injectively in the MINIMAL physical alphabet; these are not per-sixset labels. The executable geometry oracle validates regularity, partial linearity and the unique GQ projection axiom, with an explicit V<=600 cap. Oversized full-source ledgers fail closed instead of returning partial counts.

## 6. Correction of P2/P7 and resource-transfer direction

The previously published global S68 maps, with physical K6 pairs in lex order, are

    f=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8)
    g=(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8).

Three independent original-incidence reconstructions give

    seven vector=(0,44,21,0,0,2,1), S=68, Q4=9;
    H_f=6098, true dual H_g=4740, rho_6=2/143;
    mu_f=12196/143;
    U_BA+U_AB-mu_f=-2901/143;
    S-mu_f=-2472/143.

The accepted GF5 minimum floor on the SAME maps is3112510/51^6, and Q4 yields R2>=4779/51^4. The palette has all51 nonzero checksum4 patterns; these are accepted necessary floors, not complete R2/R3 risks. D6=0 does not make full R3 zero.

Therefore the all-h P2/P7 exact unit-mean proposals in [M](https://github.com/definitely-stable/Mathlab/pull/386) are FALSE. The example and source mass were separately known in [B6](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6107741776) and [B8-C](https://github.com/definitely-stable/Mathlab/issues/230#issuecomment-6109316505); the correction combines those facts, without claiming the witness was newly discovered.

Any single-use unit-credit transport demanding mu_f fails at the global cut, regardless of relay capacities:143*65=9295<12196. Even all seven motif unit credits give143*68=9724<12196. [T's59/143 threshold](https://github.com/definitely-stable/Mathlab/pull/393) remains correct for its other finite instance and cannot establish universal P2. Weighted credits, additional positive GF5 classes, reduced demand, and sufficiently-large-h formulations are different possible statements.

## 7. Two additional analytic results retained in this PR

For every s>=8 and fixed f, the exact random-right mean satisfies

    E_g U_BA >= [180054835200/13841287201]*s^6 >13s^6>12s^6.

The proof uses45*C(a,6) B templates, at most5t/K template deletion, exact C(Delta,2)Delta^4 lifts, right collision probability<=14/Delta^2, and rho_a. It is forall f exists g, not forall f,g. Full derivation is in the [Russian audit](HYP-105-ISSUE230-PROOF-AUDIT.ru.md).

For every s>=32 and every f, ordinary centered unfiltered Cauchy on C([K],6) is vacuous. Pad unused source objects with zero, set N=C(K,6), p=rho_a. Under unnormalized norms, the error E_CS=||w-H/N||_2*sqrt(Np(1-p)) obeys

    E_CS/(Hp) >= sqrt[(eta_s^-1-1)(1-p)/p]>1,
    eta_s=15(s+1)/(s^2+s+1)<1/2, p<1/2.

This follows because every positive source sixset contains an original concurrent pair, so its support has size<=N*eta_s. Asymptotically the error/mean ratio is at least(1-o(1))*s^5/sqrt(8400). This is a limitation of the specified norm bound, not of every spectral method.

## 8. What would actually close issue230

The original Branch A requires one positive c independent of h with S>=c*s^6 for ALL sufficiently large h and ALL coherent f,g. The finite P7 counterexample and local zero-source construction do not refute it. Branch B requires an infinite correlated global family with total seven S=o(s^6), which is not supplied here.

The missing step is an original-incidence-specific sixth-order lower on the coupled target acceptance of (Q1) and the other six motif families. Improving SOURCE upper/spread bounds is not that step. Neither a mean, a generic norm estimate, nor a verified auxiliary max-flow identity may be promoted to it. The631 leading forest types and11032 subleading necessary shapes remain the existing full-risk context; this scoped PR does not reclassify them or assert a strict full-risk upper.

## 9. Executable evidence and acceptance

- [Exact source and analytic reference](../../research/hyp105_issue230_proof_audit.py).
- [Independent original-incidence and 4x4 permanent oracle](../../research/hyp105_issue230_independent.py), no imports from the new reference or prior repository classifiers.
- [Definition-level C++ exhaustive8145060-sixset oracle](../../research/hyp105_issue230_bruteforce.cpp), no template or permanent algorithm.
- [Independent tests](../../research/test_hyp105_issue230_proof_audit.py).
- [Frozen exact calculations](../../research/issue230-proof-audit.json), including same-map Q4, GF5 necessary floors, sharp/zero original-source fixtures, and rational analytic bounds.

Run `python -m unittest discover -s research -p 'test_hyp105_issue230_proof_audit.py'` and `python research/hyp105_issue230_proof_audit.py`. Compile/run the C++ oracle with the dedicated hosted Contract. Full Research retains every original named step, adds the new reference report, and tests discover the new regressions. Mathematical review verified multiplicities, constants, sharpness and zero construction separately. No automatic scientific novelty claim follows from CI. Remain Draft until exact-head hosted Contract, INDEX and complete Research succeed; postmerge main Research is a separate gate if later merged by the user.
