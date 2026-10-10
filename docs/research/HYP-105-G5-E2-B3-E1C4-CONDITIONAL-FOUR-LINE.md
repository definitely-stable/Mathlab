# HYP-105 B3.2-E1-C4 — exact conditional four-original-line completion, paired overlap moments, and blockers

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), #176. Stack: C0 #249 → C1 #260 → C2 #261 → C3 #266 → **C4**.

**TYPE: RESTRICTED_THEOREM_C / exact all-h B/A conditional source–target transfer and pair-frozen conditional permutation first/second moments; W(3,2) independent complete exact oracles. No `inf_{f,g} S_seven=Omega(s^6)` theorem, no infinite counterfamily, no full-51 GF5 R3 upper, no ASET exponent.** The moment identities are classical uniform-without-replacement combinatorics (two-copy intersection schemes), not an original quasi-randomness theorem.

## 1. Model, scope, and precise missing implication from C3

For every h>=1, s=2^h, V=(s+1)(s²+1), a minimal with K=binom(a,2)>=V, consider **all injective correlated** original-left point and original-right line physical pair label maps f,g into E(K_a). Let E range over accepted ORIGINAL six-incidence sets with one repeated ORIGINAL left point p, four singleton left points projecting to physical C4, and **six distinct ORIGINAL right lines**. This is the B-left/A-right source from C0/C1, not the entire seven-family GF5 signed-event count.

There is a unique unordered distinguished original line pair P(E)={u,v} incident at the unique doubled original point. The other four original right line endpoints form H(E)⊆L_s∖P(E), |H|=4. The unique original incidence sixset therefore contributes to exactly one pair/quadruple cell

```text
b_f(P,H) = #{ ORIGINAL B-left six-incidence sets E:
             P(E)=P, H(E)=H, and all six original right endpoints distinct }.
```

The sum over P,H is the C0 original source mass M(f). For each P define w_f(P)=sum_H b_f(P,H), and for its two physical edge labels z=g(P) let F=g(L_s)⊆E(K_a), |F|=V. The EXACT **occupied conditional physical target completion set** is

```text
C_F(z) = {Q⊆F∖z: |Q|=4 and Q∪z in T_a},    q_F(z)=|C_F(z)|.
```

Crucially `q_F(z)` can be **smaller** than full-K_a codegree `q_T(z)`, where q_T(z)=7*binom(a-3,3) for adjacent z and 14*binom(a-4,2) for disjoint z. Missing physical pair labels do not have original right preimages and cannot complete an actual B/A event.

The fundamental exact identity, with NO independence and no averaging over f or g, is:

```text
U_B/A(f,g) = sum_{P original GQ concurrent pair} sum_{H⊆L_s∖P,|H|=4}
                b_f(P,H) * 1[g(H) in C_F(g(P))].
```

This sums each ORIGINAL six-incidence sixset ONCE. Therefore **U=0 iff for every P with w_f(P)>0, the source conditional support g(supp b_f(P,·)) is disjoint from C_F(g(P)).** This is an *equivalent exact conditional obstruction* for the B/A sector, not for S_seven.

## 2. Universal pair occupancy obstruction: full target completions may not be occupied

The C3 physical-disjointness theorem states M_dis(f,g)≥(1/4−O(s^(−1/2)))s^15. It does NOT establish q_F(g(P))>0 for those distinguished pairs, much less that g(H(E)) is a completion.

At general physical alphabet a>=6, let F=E(K_a)∖{(0,j):2≤j<a}; this deletes exactly t=a−2 physical pair labels, leaving physical vertex 0 incident in F **only** with the edge (0,1). For the physically disjoint occupied anchor labels (0,1),(2,3), q_T=14*C(a−4,2)>0 but **q_F=0**, because no 2-regular simple graph can contain an edge at a physical vertex with occupied degree one. This is an elementary sharp illustrative **physical-occupancy countermodel**, not a construction of the minimal-alphabet V_s geometry W(3,s) at an actual s=2^h, and NOT a counterexample to #230.

The identity

```text
q_F(z) = Σ_{J⊆E(K_a)∖F, |J|≤4} (-1)^|J| codeg_{T_a}(z∪J)
```

holds by inclusion–exclusion since each completion adds exactly four other physical pair labels. It is valid for all a>=6 and any occupied F and anchor z⊆F; do not infer codegrees of a 6+-edge set from just C0's two-/three-point data.

## 2A. Additional universal occupied-physical two-triangle subfamily (all a, all missing sets)

C3 provides many distinguished pairs with disjoint PHYSICAL images. Unlike the previous example where missing occupied edges can kill an anchor containing a physically degree-one coordinate, a useful **conditional positive occupancy lemma** holds whenever the missing-edge budget is sufficiently smaller than a.

Fix any physically disjoint occupied anchor edges ab, cd of F⊆E(K_a), |E(K_a)∖F|=t. Let W be all a−4 physical coordinates outside {a,b,c,d} and define

```text
X = {x in W: ax and bx both occupied},
Y = {y in W: cy and dy both occupied}.
```

For every ordered (x,y) in X×Y with x≠y, the physical SIX-edge set consisting of the two disjoint triangles (ab,ax,bx) and (cd,cy,dy) is a genuine occupied 2-factor containing the anchor. These are all DISTINCT since the triangle containing ab uniquely identifies x and the triangle containing cd identifies y. Consequently,

```text
q_F({ab,cd}) >= |X||Y| - |X∩Y|
             >= max{0, L(L−1)},
L = max{0, a−4−t}.
```

The last inequality follows because one missing physical edge can exclude at most one extra coordinate from X and at most one from Y, so both sizes ≥a−4−t. For sizes ≥L, |X||Y|−|X∩Y|≥L(L−1). Thus **if t≤a−6**, EVERY physically disjoint anchor in F admits at least two true occupied physical 2factor completions. The lemma is constructive and uniform over the adversarial occupied physical pair labels, not specific to a random F. It is NOT a guarantee that the four ACTUAL original right line images g(H(E)) coincide with any such completion.

### Exact all-h conditional-random benchmark (not an adversarial lower!)

Combine the new occupied triangle lemma with the genuinely uniform C3 distinguished pair mass lower `M_dis^-(s)`. For each original distinguished pair P, freeze its g(P), F and randomize **that pair's** remaining right labels, as specified in section 3. The sum of these DIFFERENT per-P conditional means obeys the exact finite lower

```text
Σ_{P physically disjoint} E_{π_P}[X_P(π_P)]
  = Σ_{P disjoint} w_f(P)*q_F(g(P))/binom(V−2,4)
 >= M_dis^-(s)*max{0,L(L−1)}/binom(V−2,4).
```

If along a sequence s=2^h the minimal alphabet slack obeys t≤(1−η)a for some FIXED η>0, then L≥ηa−4, the C3 mass is asymptotically ≥(1/4−o(1))s^15, V∼s³, a∼sqrt(2)s^(3/2), and the displayed conditional-benchmark lower is **Omega_η(s^6)**. This is a *restricted theorem about the sum of separately conditioned random means*; it is **NOT** the expectation of the total overlap under a common right random permutation, and does **NOT** imply any positive lower for adversarial fixed g or full seven-family S. Without the η slack assumption the exact bound may be zero.

This exposes the exact missing obstacle: there are MANY legal PHYSICAL completions for almost every source anchor under a non-extreme missing budget, but the actual correlated source conditional four-line images may systematically avoid them. The jointly constrained avoidance is what a future GQ-specific theorem must preclude (or exhibit) on all seven families.

## 3. Pair-frozen conditional random permutation: EXACT all-h moments

For **one fixed** original concurrent pair P, freeze (i) the original GQ source b_f(P,H), (ii) physical images g(P), and (iii) the complete V-element occupied physical pair-edge image F. Let n=V−2 and N=binom(n,4). Randomize a **uniform bijection** of the remaining n original right lines L_s∖P to the n occupied physical labels F∖g(P). This random model is **not** the adversarial fixed g and, as P changes, different pairs give DIFFERENT conditional probability spaces. Do not sum these means and claim a single globally conditional-right-map expectation.

Write b_H=b_f(P,H), C=C_F(g(P)), w=Σ_H b_H, q=|C|. Define random completed source units

```text
X_P(π) = Σ_H b_H * 1[π(H) in C].
```

Uniformity of the image of each original unordered fourset H gives exact first moment:

```text
E X_P = w*q/N.
```

For j=0,..,4 define ordered, weighted pair intersection statistics

```text
S_j = Σ_{H,J: |H∩J|=j} b_H b_J;
C_j = #{(A,B) in C²: |A∩B|=j};
D_j = N * binom(4,j) * binom(n−4,4−j).
```

For any ordered H,J sharing j original lines, (π(H),π(J)) is uniform over D_j ordered physical unordered-fourset pairs sharing j physical labels. Thus **exact second moment**:

```text
E X_P² = Σ_{j=0..4, D_j>0} S_j*C_j/D_j;
Var(X_P) = E X_P² − (w*q/N)² >=0.
```

These are all-h finite rational equalities for EVERY frozen genuine W(3,s) source and arbitrary occupied F. No spectral gap, mixing or random f/g assumption is inserted. The target pair-overlap statistics `C_j` represent physical sixfactor constraints beyond the two-label mass. In particular, just knowing w and q does not determine the conditional variance or fixed-g U.

## 4. Fixed-g deterministic conditional discrepancy: exact quantitative gate

For fixed adversarial g, pull C back via g to a family A of q foursets of L_s∖P. Let b be the vector of b_H on all N original foursets, and t=1_A. Decompose both around their means. The actual completed count for P is

```text
U_P(f,g)=w*q/N + ε_P(f,g),
ε_P = <b−w/N,t−q/N>.
```

The exact, **always valid** conditional Cauchy certificate is

```text
|ε_P|² ≤ [Σ_H b_H² − w²/N] * [q−q²/N].
```

This holds for every f,g and includes possible non-surjective g with V<K, because q counts only occupied completions. If

```text
(w*q/N)² > [Σ_H b_H²−w²/N]*(q−q²/N),
```

then the fixed-g integer `U_P` is strictly positive **for ALL permutations of remaining original right labels with fixed physical anchor z and fixed occupied image F**, even without invoking the pair-frozen randomization.

The Cauchy bound can be *vacuous* when conditional b is sparse, as expected in W(3,s). Its failure does NOT imply the existence of a bad g. The only universally valid all-g global deterministic lower from this certificate is the sum of nonnegative per-P lower bounds, and there is **no verified** positive Omega(s^6) estimate for that sum.

An exact full all-h zero-overlap characterization can also be written as the combinatorial bilinear feasibility system `sum_{P,H}b_f(P,H)1[g(H)∈C_F(g(P))]=0` over physically injective g. This is a model-equivalent Branch C reduction for **B/A only**. The other six GF5-positive classes need separate tensors.

## 5. Independent finite W(3,2) certification and explicit failure modes

The [reference](../../research/hyp105_g5e2b3e1c4_conditional_completion.py) produces b_f(P,H) by the accepted six-incidence original selection with an explicit unique doubled ORIGINAL left factor point and six distinct original right endpoints. It checks per-sixset masses against the independently frozen C0 m_f and retains exact original six-incidence multiplicity.

The [tests](../../research/test_hyp105_g5e2b3e1c4_conditional_completion.py) use **independent** second construction choosing a repeated original point, physical four-cycle, two original incident right lines and one original right line at each singleton point. This produces exactly 10,935 prefilter B-left sixsets and 5,000 qualifying original-right-distinct source units with the SAME complete per-pair/per-fourset tensor.

For all 105 pairs of the full K6 physical label alphabet, the independent oracle enumerates **all binom(15,6)=5005 physical six-edge subsets** and directly verifies exactly q_adj=7, q_dis=14; then filters occupied subsets and checks exact four-label completion set equality.

For the lex and reverse-line genuine W(3,2) labelings, the complete B/A overlap is independently calculated three ways: (i) C4 conditional tensor, (ii) reclassification of the ORIGINAL right six-line physical degree vector, (iii) C0 direct weighted hypergraph overlap. All **105 genuine right-factor transpositions** are checked at the same physical target. The known reverse-line original B/A count 77 and swap (4,13) count 57 are pinned.

The conditional second moment has an **independent exhaustive 6!=720-permutation oracle** for a small V=8 toy physical occupied image F (one true K6 2factor plus two other occupied K6 pair labels). It verifies exact E[X], E[X²], Var[X], all intersection types, and the deterministic Cauchy certificate. The finite toy is NOT a GQ(s) asymptotic theorem; the genuine W32 tests are separate.

The occupied-edge-star countermodel at a=7 with t=a−2 checks q_T>0 while q_F=0, so a full target two-point codegree can never be mistaken for an occupied completion guarantee.

## 6. Prior art and novelty firewall

- Generalized quadrangles: W(3,q) regular point–line incidence graphs have girth eight; GQ no-incidence-C4 ensures unique original double-point witness. Use primary GQ/incidence-graph literature already indexed by C1.
- Johnson association schemes and finite sampling-without-replacement: ordered fourset pair intersection classes j=0..4 and exact second moments are standard hypergeometric combinatorics.
- Hypergraph quasirandomness/counting lemmas generally require higher-order uniformity, not only low-order degree/codegree control. Nagle–Poerschke–Rödl–Schacht, *Hypergraph regularity and quasi-randomness*, SODA 2009, DOI 10.1137/1.9781611973068.26, is context, **not** a transfer theorem for arbitrary correlated right GQ pair embeddings.
- Bollobás–Scott, weighted hypergraph intersection/discrepancy, already cited in C0. Their mean or two-sided discrepancy results do not imply positivity of a minimum over all correlated g.

**Specific deliverable:** a rigorously scoped exact **pair-conditioned B/A obstruction** and pair-frozen moments with two independently executable finite oracles, no claim that the generic conditional second-moment identity is an original theorem.

## 7. Acceptance and C5 direction

Accept **RESTRICTED_THEOREM_C** only after exact PR-head dedicated C4 contract and full GitHub-hosted Research CI SUCCESS, then merge dependencies #249→#260→#261→#266→C4 and postmerge main CI SUCCESS. No self-hosted runners, no synthetic pass reports, no ASET power change. #230/#176/#169 remain OPEN.

C5 decision gate: either a **GQ-specific conditional completion concentration or expander-mixing inequality** with error o(s^6) after summing over P, uniform in ALL legal g; or a certified infinite f_s,g_s adversarial family reducing the FULL seven-motif S to o(s^6). Uniform randomly permuting the remaining labels conditioned on each P separately cannot yield a shared deterministic all-g lower; do not promote the first/second moments to such a theorem.
