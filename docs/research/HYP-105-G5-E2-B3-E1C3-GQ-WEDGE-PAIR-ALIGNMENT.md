# HYP-105 B3.2-E1-C3 — forced physical disjointness of distinguished GQ right-line pairs

2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), #176. Stacked on [#261](https://github.com/definitely-stable/Mathlab/pull/261), following C0 #249 and C1 #260.

**TYPE: restricted all-h universal joint source/physical-label theorem; first honest GQ-wedge-vs-physical-adjacency capacity obstruction. It proves no lower bound for the complete physical 2-factor intersection, seven-family S, or GF5 R3.** Uses classical GQ no-incidence-C4, B1-A original source mass, and an elementary sharp extremal bound on missing-edge adjacency in K_a. Novelty of any general extremal theorem is NOT asserted.

## 1. Fixed model, distinct meaning of two types of adjacency

For each s=2^h, h>=1, consider ALL injective left f:P_s→E(K_a) and right g:L_s→E(K_a) pair-label maps, where V=(s+1)(s²+1), Delta=s+1, K=C(a,2)>=V and a is MINIMAL. Missing physical labels t=K−V<a.

The genuine W(3,s) original B-left weighted hypergraph m_f(R) from B1-C0 has one UNIQUE doubled ORIGINAL left factor point p, four singleton ORIGINAL left points forming a physical C4 (disjoint from f(p)), and six distinct ORIGINAL right line endpoints.

For each one of these ORIGINAL six-incidence sets E define its **distinguished concurrent original right-line pair** w(E)={u,v}: the two distinct right lines chosen at the doubled ORIGINAL point p. The GQ no-incidence-C4 axiom ensures {u,v} uniquely determines p; thus all original six-incidence sets in this source have exactly one distinguished pair.

Under physical right injection g, call this distinguished pair *physically adjacent* if the two physical K_a edges g(u),g(v) share a coordinate, otherwise physically disjoint. These physical adjacency relations are NOT the original line-concurrence edges in Gamma_s and are not automatically preserved by g.

Write M(f)=sum_R m_f(R), M_adj(f,g) and M_dis(f,g) for the sums over ORIGINAL six-incidence E according to their distinguished witness pair. Exactly M_adj+M_dis=M(f).

## 2. New sharp physical occupancy lemma

Let F⊆E(K_a) be any physically occupied graph with V edges, and let its complement M consist of t<a missing edges. For each physical vertex x write r_x=deg_M(x). The line graph L(F) has

```text
A(F) = number of UNORDERED distinct physically adjacent occupied edge pairs
     = sum_x C(a-1-r_x,2)
     = C(a,2)(a-2) - 2t(a-2) + sum_x C(r_x,2).
```

Every pair of different missing edges meets in at most one physical coordinate, so sum_x C(r_x,2) ≤ C(t,2). This is SHARP: deleting t edges incident to a single physical vertex attains equality because t<a. Therefore for every injective g,

```text
A(F_g) ≤ Amax(a,V)
= K(a-2) - 2(K-V)(a-2) + C(K-V,2).
```

This elementary extremal star bound holds independently of any GQ. The independent finite oracle scans ALL missing subsets for K6 (t≤3) and K7 (t≤4), computes occupied physical adjacency by a different direct algorithm, and checks sharpness including an explicit missing star. The bounds do NOT assert that the original GQ line-concurrence graph can realize every physical adjacency of L(F_g).

## 3. New universal GQ distinguished-pair fiber bound

Fix a single concurrent pair {u,v} of ORIGINAL right lines. Its intersection p is UNIQUE by GQ. Every contributing original B-left six-incidence set whose distinguished pair is {u,v} has four other singleton ORIGINAL left points q1,..,q4 whose physical f-images form one simple C4 on four physical coordinates disjoint from the endpoints of f(p). Count possibilities BEFORE imposing the distinct original right endpoints condition:

```text
choose 4 other physical coordinates: C(a-2,4);
choose the undirected C4 on those 4: exactly 3;
choose one ORIGINAL incident right line for each singleton original point:
at most Delta^4.
```

Because f is injective, any chosen physical C4 determines at most one unordered set of four ORIGINAL singleton left points. Thus every ORIGINAL concurrent line pair occurs as the unique doubled-point witness at most

```text
Wmax(s) = 3*C(a-2,4)*(s+1)^4
```

times. No 6!, 4!, physical-coordinate automorphism or GF5 signed multiplicity is inserted.

The original line-concurrence graph has E_GQ=V*s(s+1)/2 edges (C1). The number of those pairs whose **images under g** are physically adjacent is bounded by the smaller of E_GQ and Amax(a,V). Hence, uniformly for all legal correlated f,g,

```text
M_adj(f,g) ≤ Wmax(s)*min(E_GQ,Amax(a,V)).
```

This is genuinely joint: it combines an ORIGINAL GQ source witness capacity and a physical edge-label adjacency capacity. It remains true when V<K and the unused physical pair labels are placed adversarially.

Let H_B^-(s) be C0's independently proved all-h exact integer mass floor on distinct ORIGINAL right endpoint B-left sixsets, derived from B1-A and the original GQ pair-collision bound. Then

```text
M_dis(f,g)
 ≥ max{0,
       H_B^-(s) - 3*C(a-2,4)*(s+1)^4
                     *min(E_GQ,Amax(a,V))}
 = (1/4-O(s^(-1/2)))*s^15
```

**in the asymptotic uniform lower-bound sense**. Indeed a=(sqrt(2)+o(1))s^(3/2), H_B^-(s)=(1/4+O(1/s))s^15 and the excluded adjacent-witness mass is at most (1/sqrt(2)+o(1))s^(29/2). As s grows, the fraction of B-left distinct-right incidence mass whose distinguished concurrent ORIGINAL line pair maps to TWO PHYSICALLY DISJOINT pair labels is at least 1−O(s^(-1/2)). This is compatible with every arbitrary correlation between f and g.

The exact integer formula is valid at EVERY s=2^h, including when the displayed max is zero. It becomes positive for the tested powers-of-two s≥16; no monotonic threshold theorem is claimed merely from finitely many test points. At s=2 the crude uniform lower can be zero while the genuine finite W32 source mass is 5000.

## 4. Positive two-label completions are NOT positive full six-label overlap

In full physical T_a the number of six-edge 2-regular target hyperedges containing a given physically DISJOINT pair of physical K_a edges is exactly

```text
q_dis = 14*C(a-4,2)
```

by accepted B1-C0. Thus if one counts for each ORIGINAL B-left six-incidence E the full-K_a target sixsets containing only the images of its distinguished pair, disregarding images of its OTHER FOUR original right lines, this **relaxed two-label completion** functional is exactly

```text
I_two(f,g) = q_adj*M_adj(f,g) + q_dis*M_dis(f,g)
           ≥ q_dis*max(0,H_B^- - Wmax*min(E_GQ,Amax)).
```

Here q_adj=7*C(a-3,3), and I_two is a weighted count of pairs (E,target completion), not an event count on the actual six images g(R).

**This bound does NOT imply U_B/A(f,g)>0.** In particular:
- a target completion may use physical labels not occupied by g(L);
- even if all six physical labels are occupied, the other four labels need NOT be the images under g of the four specific ORIGINAL right line endpoints of E;
- neither mass of compatible distinguished pairs nor this two-label completion count controls the higher-order Johnson W>=4 contraction from C2;
- one family B/A is strictly less than the full accepted seven-family S and full 51-palette GF5 risk R3.

The positive joint statement therefore supplies a necessary structural mechanism for future C4 source-target inequalities but is not an exponent claim.

## 5. Exact falsifiers and acceptance

[Reference](../../research/hyp105_g5e2b3e1c3_wedge_alignment.py) uses C0's exact integer all-h original mass floor without duplicating its proof; separately constructs a COMPLETE W(3,2) distinguished original-pair witness frequency from each accepted original six-incidence B-left set.

[Tests](../../research/test_hyp105_g5e2b3e1c3_wedge_alignment.py) independently generate the SAME witness counts using a second algorithm (choose repeated ORIGINAL point, four-coordinate physical C4, two original incident right lines, four singleton original neighbors; no production selected_left_six). It checks original line pair concurrence against the actual W32 original incidence graph, all 5000 original source units, 3076 weighted right sixsets, all **105 genuine original right-line pair-label swaps**, complete finite missing-star extremum enumeration, and exact all-h integer bounds at s=2,4,8,...,1024. The oracle does not pretend to enumerate large-s symplectic geometry.

**Acceptance requires:** independent exact unit tests on the exact PR head; complete GitHub-hosted Research SUCCESS, success on dependencies #249/#260/#261, merge via sequential dependency-safe order, and postmerge Research SUCCESS on main. Both #230 and #176 remain OPEN and no ASET exponent changes.

## 6. Next mathematical C4 gate

A valid all-g U_B/A lower needs to certify not merely that a distinguished witness pair has a TARGET two-label completion, but that its four remaining ORIGINAL right line images complete that specific physical six-edge 2-factor. A potentially productive route is a genuine **four-line conditional source-target mixing inequality** with conditioning on the doubled pair, bounded error relative to s^6. Another route is an infinite explicit adversarial f,g that defeats ALL seven classes. Any use of abstract random-right independence for the remaining four under a fixed correlated map g is prohibited.
