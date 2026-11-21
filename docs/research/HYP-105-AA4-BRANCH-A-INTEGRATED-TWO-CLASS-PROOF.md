# HYP-105 / #230 — AA4 Branch A: integrated two-class proof candidate

**Mathematical claim:** For genuine symplectic W(3,s), s=2^h, with the minimum physical pair alphabet and *every* fixed, separately globally injective, arbitrarily correlated f,g, there exist absolute δ>0 and h0 such that for every h≥h0,

    D6(f,g) + U_BB_overlap(f,g) ≥ δ s^6.

In particular the unweighted sum S of the seven HISTORICALLY DEFINED positive six-original-incidence-ID classes in #230 satisfies inf_(f,g) S ≥ δ s^6. Only two of the seven classes are needed.

**Status discipline:** this is a single consolidated all-h **proof candidate**, using one explicitly cited published graph supersaturation theorem. It is not a finite extrapolation or an external peer review. Repository status remains OPEN_WITH_FORMAL_BLOCKER pending independent acceptance of this manuscript, exact-head full Research success and the issue's merge/postmerge-main acceptance protocol. No parent/main merge, no GF5 total-risk upper bound, no general ASET exponent or worldwide priority claim. Strict child of frozen [#786](https://github.com/definitely-stable/Mathlab/pull/786) head 837426b05c2d0f7927cb5ec37b90088ccf5f04ce. Prior #772/#782–#786 establish many constituent lemmas; this manuscript's contribution is their complete common-quantifier composition, independent historical source class audit, direct signed-flow count and a new **expected selected C6 bound D6/1024**.

## 1. Fixed source model and historical positive classes

Let I be the set of N=(s+1)^2(s²+1) distinct actual incident point-line pairs of W(3,s), P and L each of size V=(s+1)(s²+1). Fix a=min{b: binom(b,2)≥V}. Fix arbitrary maps f:P→binom([a],2), g:L→binom([a],2) injective on each side. They are not random and may be correlated arbitrarily.

Every source flag i=(p,l) owns the two opposite real undirected edges in the rectangle f(p)×g(l). On physical vertices [a]×[a], this defines a simple graph H: no loops, no parallel edges, unique source owner of each edge because its two physical coordinate pairs uniquely determine p,l. For any named source set C⊆I, H_C retains both diagonals of each owner. The full graph has 2N edges and degree sum 4N. All deleted-edge subgraphs retain genuine unique owners; no vertex or edge is cloned.

Historical D6 is exactly the definition of merged B3.2 in docs/research/HYP-105-G5-E2-B3-B2-COINCIDENT-CYCLES.md: six originally distinct point factors and six originally distinct line factors, with both projected simple physical C6 having identical dual adjacency on the six column IDs. Its alternating three-versus-three event contributes 5643/51^6 to R3. Historical U_BB_overlap is the class of merged B3.2-E1-A and #224/#227: each typed original multiplicity is [2,1,1,1,1], repeated original point and line share their middle incidence column, and both physical projections have six symbols, each appearing twice (doubled pair plus C4).

These classes are disjoint by the original multiplicity profiles. Other class counts are nonnegative; hence it suffices to prove the two-class inequality. Root no-Z scope is exactly the question in #230, not a claim for arbitrary deleting palettes.

### Positive class coefficients by two-color dual flows

For a support-four source column, its coefficients are the 51 nonzero GF(5)^4 tuples with sum 4. For six columns whose typed physical symbol fibres each have cardinality two, use a dual edge for each physical symbol joining its two columns. At each symbol cancellation requires the two sign-adjusted coefficients to be opposite and nonzero. Orient each edge; assign a nonzero field value to it. The signed contribution to the two endpoints is +z,-z. At original column j the demand is 4 or -4 depending on its sign. Thus admissible assignments are *bijective* with GF5 nonzero dual edge flows with these demands. Balanced three-positive/three-negative signs ensure total demand zero.

For D6 the dual is a doubled six-cycle; take alternating signs. The direct integer tree oracle enumerates 4^7 nonzero choices on the seven edges outside a spanning tree (12 edges, rank 5). A unique flow on the five tree edges completes each choice, determined by sums of residual demands in subtrees modulo 5. Reject any zero tree current. This gives exactly 5643. The historic MITM/Fourier checks used a different method.

For the produced BBo family of Section 6, order columns as (q,l),(p,l),(p,r),i1,i2,i3. On column labels 0,…,5, the x dual has parallel edges 1–2 and C4 0–3–4–5–0; the y dual has parallel edges 0–1 and C4 2–3–4–5–2. This holds for EVERY accepted path, since the two residual factor paths follow the same source order. The direct nonzero tree oracle computes all ten unordered balanced signs with column 0 positive; the sum is 53838 (each ≥5175). This independently reproduces the established aligned BBo signed floor and exceeds historical 51750. Relabeling coordinates or source columns does not change the flow bijection. No independence between different sixsets is needed for the R3 sum: they are distinct events and linearity sums nonnegative contributions.

This proof needs only class membership and positivity, not a new enumeration of all 631 leading or 11,032 subleading types. Those broader issue evidence requirements are not asserted newly implemented by this slice.

## 2. Deterministic source spectral and alphabet bounds

Define the original conflict graph J on I: distinct source flags sharing p conflict when their g-pairs intersect, and distinct flags sharing l conflict when their f-pairs intersect. These two kinds are disjoint since original point-line incidence is simple.

The GQ axiom gives both original point/line collinearity graphs SRG(V,k,lambda,mu) with k=s(s+1), lambda=s-1, mu=s+1. Indeed each original pencil contains s other neighbors; adjacent factors share exactly s-1 common neighbors on their pencil, and nonadjacent factors have one common neighbor per one of s+1 pencils. Thus their adjacency M obeys M²=(s²-1)I-2M+(s+1)11^T, with largest nontrivial eigenvalue s-1. For a physical typed symbol fibre S_x of size d_x, projection onto the all-one vector gives

    2e_col(S_x) ≤ (k-(s-1)) d_x²/V + (s-1)d_x.

Injectivity implies d_x≤a-1, sum d_x=2V, sum d_x²≤2V(a-1). Different labels intersect in at most one symbol; two collinear original factors have a unique common pencil. Therefore independently for f,g,

    e_col(f), e_col(g) ≤ (s²+1)(s²+a-2),
    e(J)=e_col(f)+e_col(g).

Fix H0=32, u0=2^-32, t0=2^-16 and constants

    v=(1+u0)(1+u0²), nu=(1+u0)^2(1+u0²),
    M0=(1+u0²)(1+(23/16)t0),
    A0=2v+(23/4)t0³+4t0^6.

Minimal a gives (a-2)(a-1)<2V, so a-2<sqrt(2V) and a<sqrt(2V)+2. For u=1/s≤u0, t=1/sqrt(s)≤t0, check exactly 2v<(10/7)^2<(23/16)^2. Thus a-2<(10/7)s^1.5, a-1<((10/7)+t³)s^1.5, and

    e(J)<2M0 s^4,   a²<A0 s³,   N≤nu s^4,   4nu<17/4.

The first inequality follows immediately by substituting a-2 into the sharper SRG bound (no loose HR-10 envelope needed). The rational certificate verifies 8(nu+M0)<17 and 24(nu+M0)<49. All constants are label-independent.

## 3. HEAVY: actual ordinary graph supersaturation and exact D6 lift

Use the following published theorem (k=3 case of the even-cycle graph supersaturation result attributed to Simonovits and proved within the graph case of Jiang–Yepremyan 2020, *Combinatorics, Probability and Computing* 29, 698–721, DOI 10.1017/S0963548320000206; https://arxiv.org/abs/1707.03091 and https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/supersaturation-of-even-linear-cycles-in-linear-hypergraphs/240493C1F42618819DA9B16CE7F3E4BD). There are positive absolute constants C_graph,c_graph such that every finite simple graph F with e(F)≥C_graph v(F)^(4/3) has at least c_graph(e(F)/v(F))^6 simple unoriented six-cycles, adjusting a fixed normalization constant if necessary. Numerical constants are unknown here, but their existence is sufficient.

Choose ONCE rational C0≥max(1,C_graph), 0<c0≤min(1,c_graph), BEFORE h,f,g. Let

    R=ceil[256 A0(1+64M0)]=33281,
    T=ceil[(17/2) R³ C0³],  δ=c0/R^6.

Freeze Q_T={v in H:d_H(v)>Ts} and E_T the number of DISTINCT physical edges touching Q_T. If E_T≥s^4/8, their named owner set L0 has |L0|≥s^4/16. The random local-minimum priority argument (or Cauchy on Caro–Wei) selects an independent source set I0 in J[L0] of size at least |L0|²/(|L0|+2e(J[L0])). Since e(J)<2M0s^4, monotonicity in |L0| yields |I0|>s^4/[16(1+64M0)].

Apply one independently uniform fair binary color per actual physical first symbol and one per actual physical second symbol. For each fixed owner the probability both pairs cross is 1/4, so there exists a single coherent pair of cuts retaining a whole J-independent source set S of size |S|≥|I0|/4. Each retained owner still has an original heavy-touching physical edge. Choose for each one such edge and one endpoint q∈Q_T. Pigeonhole q's first-cut color: at least |S|/2 different source owners have witnesses from some fixed bit b. Let U be all actual Q_T vertices of that bit, r=|U|>0. Let Y be all opposite-bit actual neighbors of U in the retained graph and E the actual number of U–Y edges, so E≥|S|/2 and |Y|≤a².

Choose the min(r,|Y|) actual vertices in Y with top U-degrees; the resulting ordinary subgraph F has at most 2r vertices and e(F)≥E r/a² (including the |Y|<r case). Thus e(F)/v(F)≥|S|/(4a²)>s/R. Also v(F)≤2|Q_T|<8N/(Ts)≤(17/2)s³/T. Our frozen T ensures v(F)<(s/(RC0))³ and consequently e(F)≥C0 v(F)^(4/3). The published theorem supplies at least c0(s/R)^6 ordinary simple C6(F).

**Selected ordinary C6 → historical D6 (all orders, no graph-clone loss).** For cycle vertices (x_j,y_j), cyclic distance one excludes repeated first/second coordinates because every physical diagonal changes both. Distance two: if x_j=x_(j+2), two consecutive distinct edges would have the same source point by f injection, and their line labels share y_(j+1). The owners are different since opposite diagonals of a single flag have disjoint vertices; hence they conflict in J. This contradicts S independence. Dual y proof is identical. Distance three excludes equal x by parity of the coherent first cut, and equal y by parity of the second cut. These exhaust all cyclic distances on C6.

Thus each ordinary selected C6 is coordinate-rainbow on both sides, with six distinct original point and line factors. Its two projected simple C6 have identical cyclic **named source owner order**, so it belongs to historical D6. The inverse is unique: the six original f factor edges fix the cyclic owner order up to simultaneous rotation/reversal; each physical corner between consecutive owners has its first AND second symbol forced by the intersection of their corresponding two label pairs. Each intersection has size exactly one. This proves injection even when F deletes single diagonals, and bijection in the full paired graph between rainbow C6 and D6. No factor 6!, 12, or signed multiplicity in the source count.

Hence HEAVY implies D6≥δs^6.

## 4. LOW core, one global selector and expected moments

In LOW E_T<s^4/8, remove from I every original owner touching any frozen Q_T vertex (at most E_T owners). Also remove every original owner of FULL J degree>K=10; their number is at most 2e(J)/(K+1). Retain the paired source CORE C. Its physical Δ=max d_HC≤Ts, induced source J_C degree ≤K, and

    |C|>c s^4,   c=7/8-4M0/(K+1)>0.

The full uncut CORE has physical m=2|C| edges on n=a² corners. For its total ordered 3walks W3, the elementary walk lower bound W3≥(2m)^3/n² follows by choosing a uniformly oriented edge (v,w). Then W3=2m E[d(v)d(w)]. Each endpoint marginal is degree-size-biased, giving E log d(v)≥log(2m/n) by convexity of x log x over all n vertices (0 log 0=0). Jensen for exp now gives the bound. Hence

    W3>w s^6,   w=(4c)^3/A0²>0.

If D6≥δs^6 already, stop. Otherwise assume D6<δs^6≤s^6. Use ONE random global independent priority per named CORE owner and keep local minima in J_C. Independently apply TWO global independent typed-symbol bit cuts and retain only owners crossing both, both diagonals together. Every outcome G is genuine simple bipartite, J_C-independent, subgraph of H_C, physical degree ≤Δ.

For any proper rpath (all r+1 x symbols and r+1 y symbols distinct, r=2,3), its r owners have pairwise different original points and lines, hence nonadjacent in J_C. Condition on their priority values z_i. Each distinct external source neighbor w touching target subset S_w contributes exact conditional probability 1-max_(i∈S_w)z_i≥prod_(i∈S_w)(1-z_i). Integrating independent z_i gives P(all win)≥prod_i(1+d_JC(i))^-1. Each typed cut has exactly two alternating bit assignments on r+1 distinct symbols; joint bit probability 4^-r. Thus proper path survival probability is at least 1/q_r, q_r=4^r(K+1)^r.

Let P_r be the ordered endpoint matrix of proper rpaths in H_C, X_r the surviving proper-path matrix of the SAME random G. Then entrywise EX_r≥P_r/q_r; summing the scalar Jensen inequality and using symmetry and nonnegative adjacency gives

    ||P_r||_F²≤q_r² E tr(A_G^(2r)).

For W_C=sum_(u∈C)1/(1+d_JC(u)), one owner wins with probability 1/(d+1) and passes both cuts with probability 1/4. Hence E m(G)=W_C/2, E tr A_G²=W_C≤N. Distinct owners or paths are not assumed independent.

**NEW expected selected-C6 improvement.** By the all-order lift, every selected C6 is one of the distinct original D6 sets in the paired CORE. Each such sixset has a UNIQUE possible unoriented physical cycle. Its x and y factor cycles each contain six distinct symbols. Exactly two of 2^6 bit patterns alternate on either side; hence simultaneous cuts succeed with probability (2/64)^2=1/1024. A source priority requirement can only reduce this. Summing over all distinct D6 (including those outside C only enlarges the bound) yields

    E C6(G) ≤ D6/1024.

This is a stronger universal expectation than the previous per-outcome upper D6, verified on nonzero true W32/W34 cycles by all 4096 relevant global bit assignments. It does not change the HEAVY density theorem or assume independent cycles.

Any closed sixwalk of a simple bipartite graph that is not a simple cycle has an immediate reversal: a repeated vertex splits it into shorter even closed walks, one of length two. Each unoriented simple C6 has 12 rooted oriented walks; deleting a marked reversal and its backtracking middle vertex gives a length-four closed walk with at most 6Δ insertion possibilities (cyclic position recorded). Hence tr A_G^6≤12C6(G)+6Δ tr A_G^4. For symmetric A, (tr A^4)^2≤tr A² tr A^6=2m tr A^6. Young therefore gives tr A_G^6≤24C6(G)+72m(G)Δ².

Average over the same ω, and use scalar Cauchy over the same outcomes:

    E tr A_G^6 ≤ (3/128) D6 +36Δ² W_C,
    (E tr A_G^4)^2 ≤ W_C E tr A_G^6.

This is an all-h strengthening of #779/#786 with no probabilistic change to H_C. Define

    L6=1+ceil(36 nu T²),   q2=1936, q3=85184.

Then ||P3||²≤q3² L6 s^6, ||P2||²≤q2² sqrt(nu L6) s^5.

## 5. LOW error bounds, same physical core, original FULL anchors

### Coordinate returns and uncut fourth moment

Let Qx,Qy count all ordered physical 2walks in H_C whose first/last x, respectively y, agree, including backtracks. For each named source point p and symbol y put R_C(p,y)=#{(p,l)∈C:y∈g(l)}. In an x-return two-walk the unordered first pair determines p and the middle y determines the pencil. The two choices of orientation of f(p) give Qx=2 sum_(p,y) R_C(p,y)^2. Since sum R_C=2|C| and sum binom(R_C,2) counts exactly the point-side J_C conflicts (distinct injected line labels intersect at most once), Qx=4|C|+4e_point(J_C). The dual gives Qy=4|C|+4e_line(J_C). Thus Qx+Qy=8|C|+4e(J_C)<8(nu+M0)s^4<17s^4.

Write A_C²=P2+B2 on disjoint endpoint supports, B2 the nonproper two-walk matrix. Since every entry ≤Δ and sum B2≤Qx+Qy,

    tr A_C^4 = ||P2||²+||B2||² ≤ L4 s^5,
    L4=q2² ceil_sqrt(ceil(nu L6))+17T.

A nonproper 3walk has a repeated coordinate at gap 2 or 3. Each of the two gap-2 positions costs ≤Δ(Qx+Qy) by extension. For gap three, the positive semidefinite A_C²(Δ I-A_C) gives for each x-fibre indicator z, z^T A_C³ z≤Δ z^T A_C² z, and the dual y. Summing both types and union bounding gives I_improper≤3Δ(Qx+Qy)<49T s^5 using the exact rational strict 24(nu+M0)<49. Here A_C need not be bipartite.

### Endpoint mask

For an ordered off-coordinate endpoint pair (v0,v3), decode their two unordered coordinate pairs as original factors q,r. Missing labels or q incident r are endpoint failures. Otherwise the unique GQ path q–l–p–r gives three FULL original anchor flags. Fail endpoint if f(q) meets f(p) or g(r) meets g(l). Let B=binom(a,2), M=B-V. Missing pairs count exactly 4(2VM+M²); incident pairs 4N (each source pair has four corner orientations). Minimal a implies M<a-1<2s^1.5. Each ordered distinct collinear q,p with shared f symbol yields s choices of r through p other than the unique common line with q; times four endpoint orientations. Thus endpoint bad set Ebad has size at most 4(2VM+M²)+4N+8s(e_col(f)+e_col(g)). Substitute Section 2, and u=1/s,t=1/sqrt(s) to get

    |Ebad|/s^5 < 16(1+u²)(1+2t)+16(1+u)(1+u²)t
                    +16u²+4u(1+u)^2(1+u²) <17.

The last strict inequality uses positivity and exact rational evaluation at u0,t0. Cauchy over ordered endpoints gives the bad-endpoint proper path mass

    I_endpoint ≤ sqrt(|Ebad| ||P3||²) ≤ E s^(11/2),
    E=q3 ceil_sqrt(17 L6).

### Four interior blockers: FULL A=I versus retained C

For eligible nonincident projected endpoints q–l–p–r, the remaining failures are that an inner x symbol belongs to f(p) or inner y to g(l). We bound the first inner x case; reversal gives the second, and true point/line duality the y cases.

For each original point p, set c_x(p)=#{q collinear with p: x∈f(q)} and R_A(p,y)=#{(p,l)∈I:y∈g(l)}; R_C as above. Define K_AC(p,j)=sum_y R_A(p,y)R_C(j,y). The source book Bx is the sum of c_x(p)K_AC(p,j) over retained point j, each orientation (x,k) of f(j), and each p with k∈f(p). The *FULL* original A-side may contain projected anchor flags not in CORE.

For a first-inner-blocked proper directed path with triple of physical corners (v0,v1,v3), write v0=(x,y), v1=(k,z), v3=(x',y'), k∈f(p). The original first edge owner (j,m) is forced, as are q with f(q)={x,x'} collinear p and FULL anchor (p,r) with g(r)={y,y'}. This triple injects into a literal source book term (j,(x,k),p,q,(p,r),(j,m),y): both original flags counted in K_AC share y, and q counted in c_x(p). Conversely such data recover v0 via (x,y), v1 via k and the other symbol in g(m), v3 via other symbols in f(q),g(r). This is a **triple** injection, not an incorrect injection of every full 3walk to a distinct book key. For each triple count middle two-walk completions by (A_C²)(v1,v3); for each fixed (v1,v3) at most Δ choices of v0. Cauchy gives I_x1²≤Bx Δ tr(A_C^4). Similarly I_x2, I_y1, I_y2 bounded with Bx or By. The four events may overlap; use union upper bound.

To control Bx, let F1,F2 denote sums of c_x(p)^2 and K_AC(p,j)^2 over exactly its index triples. Cauchy gives Bx²≤F1 F2. Each fixed (x,p) allows at most two k and hence at most one j per k by pair injection: F1≤2G_f, G_f=sum_(x,p)c_x(p)^2. Actual J_C pencil cliques give R_C(j,y)≤K+1 and sum_y R_A(p,y)≤2(s+1). Hence K_AC≤2(s+1)(K+1) and F2≤2(s+1)(K+1)Theta. Expanding the same literal sums gives Theta=sum_(k,y) d_H(k,y)d_HC(k,y)≤4NΔ. Therefore Bx²≤16(s+1)(K+1)NΔ G_f. Dual By uses its own G_g.

From Section 2's original SRG matrix identity,

    G_f=2V(s²-1)-4e_col(f)+(s+1)sum_x d_x²
       ≤2V(s²-1)+2V(s+1)(a-1).

Using a-1<((10/7)+t³)s^1.5 and v(u)=(1+u)(1+u²), nu(u)=(1+u)^2(1+u²),

    Bx²/[(K+1)T s^(23/2)]
       <32(1+u)nu(u)v(u)[t+(1+u)(10/7+t³)]<46.

The expression is monotone on nonnegative u,t and checked by exact rational evaluation at u0,t0. Independently same for By. With B0=ceil_sqrt(46(K+1)T),

    I_fourblockers ≤4 sqrt(B0 T L4) s^(47/8) ≤ D s^(47/8),
    D=4 ceil_sqrt(B0 T L4).

This rederivation fixes the earlier imprecise wording that every *path* injects into the book: only the three-corner triple injects; the two-walk multiplicity is explicitly charged.

## 6. Accepted paths → actual BBo; final quantifier closure

Every physical proper 3path surviving the endpoint and four inner tests has four distinct symbols per side. Its three path owners have distinct original points and distinct original lines. Closing the typed paths by f(q) and g(r) gives actual simple C4 on each side. The three actual projected original anchor flags (q,l),(p,l),(p,r) exist in FULL I, since q,r are nonincident and p,l are their unique GQ projection; f(p) and g(l) are disjoint from all four path symbols on their respective sides. Hence neither repeated factor overlaps a residual owner or an endpoint label. All six actual named flags are distinct. Exactly one original point p repeats and exactly one original line l repeats; they share the middle anchor (p,l). Both projections are doubled pair plus C4. The historical positive BBo class membership and aligned GF5 flow topology of Section 1 therefore hold.

Conversely an unordered produced sixset determines the repeated point p and line l, hence all three distinguished anchors uniquely; the three residual original owners determine each typed P4 with the endpoint pair fixed. Each P4 permits just two orientations; alignment requires the same middle source owner on both. Thus exactly two actual directed physical paths per produced sixset (simultaneous reversal) or no path for unaligned/nonproduced sixsets. There is no double count of historical BBo sets with absent CORE owners. In particular

    2 U_BB_overlap ≥ W3-I_improper-I_endpoint-I_fourblockers.

Choose ONCE, after C0,c0 but BEFORE any s,f,g, the sufficient integer

    s0=max(2^32,64,
           ceil(49T/(w/64)),
           ceil((E/(w/64))²),
           ceil((D/((15/16)w))^8)).

Exact rational arithmetic gives c>0 and w/64>1/R^6≥δ; all constants are positive independent of every labeling and s. For all dyadic s≥s0 the three error upper bounds sum to at most (1/64+1/64+15/16)w s^6=(31/32)w s^6. Consequently in LOW with D6<δs^6,

    U_BB_overlap ≥ (w/64)s^6 > δs^6.

HEAVY gives D6≥δs^6; LOW either already has this D6 bound or supplies the BBo bound. These exhaustive alternatives concern the SAME s,f,g and the SAME globally fixed C0,c0,T; no exchange of infimum and expectation. Thus the mathematical conclusion is

    inf_(f,g) [D6(f,g)+U_BB_overlap(f,g)] ≥ δs^6
    inf_(f,g) S_s(f,g) ≥ δs^6   for every dyadic s≥s0.

The accepted #230 risk floor, or just the positivity checks of Section 1 for D6 and produced BBo separately, also gives R3≥(5643/51^6)δs^6 for this GQ family. This excludes fixed-label strict O(s^(6-eps)) R3 *for this construction and coefficient distribution*. It does not exclude unrelated weighted ASET constructions, dependent coefficient assignment, other extraction algorithms, or bound the entire R3 from above. Omega is an eventual all-h claim; small h may have both counts zero without contradicting it.

## 7. Evidence and acceptance

The companion independent code reconstructs real physical C6 and source-typed dual lifts independently. On full genuine W(3,2) under three complete f/g maps, it compares a physical-first rainbow C6 DFS to a factor-first full left cycle/actual line assignment census, and compares physical proper 3paths to a source-first exhaustive left B-type sixset enumeration and independent six-owner-order lift. On genuine W(3,4) it obtains a nonzero actual D6 witness without a historical planted ID. It exhaustively colors all 4096 relevant physical symbol-bit assignments of a true D6, exactly four successful. Direct GF5 tree elimination (4^7 chords), both historical positive coefficients, all ten BBo sign partitions and exact 51-pattern palette are independently computed. Fraction ledgers verify all rational margins and the exact dyadic thresholds at three purely FORMAL hypothetical C0,c0 pairs — not published graph constants.

This slice assembles a proof candidate rather than indefinitely leaving each local gate open by name. The remaining acceptance work is independent review of the single manuscript (specifically the historical definitions, shared-source triple book, all-h identities and published theorem), exact-head Research completion and the issue's required formal integration/merge and postmerge main CI. Do not mark PROVED_A on green finite checks alone. If an actual false implication is identified, isolate it here rather than claiming a closed global theorem.
