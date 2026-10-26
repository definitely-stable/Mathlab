# Full physical-degree tail compensation by ORIGINAL D6

Date: 2026-10-26. Frozen source: genuine W(3,s), s=2^h, arbitrary complete
separately injective physical pair maps f,g with the minimal alphabet.
The result below is a new global D6 compensation theorem. It does **not**
prove the root seven-family lower bound. It is stronger in scope than the
earlier degree trimming restricted to an already coherent G*.

## 1. Statement with quantitative exponents

Write V=(s+1)(s^2+1), d=s+1, N=Vd, and
a=min{b:binom(b,2)>=V}. Let H be the FULL physical graph on [a]^2. Each
original incidence (p,ell), with f(p)={x,x'} and g(ell)={y,y'}, contributes
BOTH physical diagonals (x,y)--(x',y') and (x,y')--(x',y).

Let C_graph,c_graph>0 be absolute constants in the standard balanced
six-cycle supersaturation theorem:

    e(F)>=C_graph v(F)^(4/3)
       implies #C6(F)>=c_graph (e(F)/v(F))^6.       (SS6)

Here cycles are simple, unoriented and unrooted. Increasing C_graph and
decreasing c_graph accommodates any fixed conventional normalization.
This is a proved BALANCED graph theorem; no conjectural unbalanced
supersaturation statement is used.

For T>0 define

    Q_T={v:deg_H(v)>T*s},
    E_T=#{uv in E(H):u in Q_T or v in Q_T}.

For every s=2^h>=64, every allowed correlated f,g, and EVERY epsilon>0,

    E_T>=epsilon*s^4,
    T>=2^41 C_graph^3 epsilon^(-6)

imply the same-fixed-map ORIGINAL motif bound

    D6(f,g)>=c_graph epsilon^12 s^6 / 2^72.        (1)

There is no epsilon<=1 restriction: if the premise is possible then
automatically epsilon<=2N/s^4<=4. Equivalently the unconditional tail
estimate, valid for every T>0, is

    E_T/s^4 <= (2^41 C_graph^3/T)^(1/6)
                +(2^72 D6(f,g)/(c_graph s^6))^(1/12).   (2)

In fact the maximum of the two displayed terms suffices. Thus if along
any allowed map sequence S_seven=o(s^6), and hence D6=o(s^6), then

    limsup_(h->infinity) E_T/s^4
       <= (2^41 C_graph^3/T)^(1/6).                (3)

Consequently the degrees of the FULL H are uniformly integrable at the
s scale under the small-S hypothesis. This conclusion concerns almost
all full physical edges; it does not begin with a low-density G*.

## 2. Source book bound and exact original-ID conflicts

For an original point p and right coordinate y put

    r_(p,y)=#{ell:p incident ell and y in g(ell)}.

The original point-pencil collision book is

    M_g=sum_(p,y) binom(r_(p,y),2).

Its dual M_f is defined on original line pencils and left coordinates.
Since g is globally injective, two distinct source lines have different
simple physical pair labels and share at most one coordinate. Thus M_g
counts each unordered pair of conflicting original incidence IDs at a
common point exactly once. The dual statement holds for M_f.

The source incidence singular values are d,sqrt(2s),0. For each right
coordinate y, its original line-star set L_y has size k_y<=a-1 and
sum_y k_y=2V. Spectral decomposition gives

    ||B 1_(L_y)||_2^2
       <=2s*k_y+(s^2+1)*k_y^2/V.

Using sum_y k_y^2<=2V(a-1), and subtracting the total first moment
sum_(p,y) r_(p,y)=2Vd, yields

    M_g,M_f <= C_s
      :=(s-1)V+(s^2+1)(a-1)
       =(s^2+1)(s^2+a-2).                         (4)

For any subset I of COMPLETE original incidence IDs, both restricted
books can only decrease.

Define its conflict graph K_I on the ORIGINAL IDs in I. Two different
IDs are adjacent if either:

* they have the same original point and their g-line labels intersect;
* they have the same original line and their f-point labels intersect.

A distinct pair cannot meet both conditions because the original source
is simple. Consequently the exact conflict-edge identity is

    |E(K_I)|=M_g(I)+M_f(I)<=2C_s.                  (5)

An independent set J in this graph has BOTH desired original-pencil
matching properties simultaneously. In particular, all retained opposite
labels in any retained original pencil are pairwise disjoint.

## 3. A coherent subset of every dense original-ID subset

Let L=|I|. The Caro--Wei bound and Cauchy give

    alpha(K_I)>=sum_(i in I) 1/(deg(i)+1)
       >=L^2/(2|E(K_I)|+L)
       >=L^2/(4C_s+L).                           (6)

For completeness, assign independent continuous ranks to the fixed
original IDs and keep each ID whose rank is smallest in its closed
neighborhood. Adjacent IDs cannot both be kept, and the expected number
kept is exactly the first sum in (6). This randomization selects a subset
of the fixed maps; it assumes no randomness or independence of f,g.

A deterministic minimum-current-degree greedy algorithm also achieves
the Caro--Wei bound. At a minimum-degree vertex v, the sum of
1/(deg(u)+1) over u in its closed neighborhood is at most one. Removing
that neighborhood decreases other degrees, so induction preserves the
claimed reciprocal-degree lower bound.

Choose an independent J satisfying (6). Independently two-color the left
physical coordinates and retain the whole incidence ID whenever its f
pair is bichromatic. At least |J|/2 IDs can be retained. Do the same on
the right; at least |J|/4 IDs survive. BOTH diagonals of each retained ID
remain. Call the resulting physical graph G.

G has no row/column cherries: two neighbors of one corner with the same
first coordinate would arise at one original point pencil with intersecting
g labels; the dual case is analogous. Every edge flips both physical
coordinate colors. Therefore every ordinary simple C6 in G is coordinate-
proper: a repeated coordinate at cyclic distance two violates no-cherries,
at distance three violates the coordinate cut, and distance four is the
reverse distance-two case. The established exact physical-to-original
bijection makes every such C6 a distinct accepted ORIGINAL D6 sixset.

Explicitly, six distinct first coordinates make its six source point
pair labels distinct; the same holds for its source line labels. Adjacent
cycle edges share precisely the same named-column neighbor on both
halves, so the two column duals are the same connected C6. Conversely
those duals reconstruct each intervening physical corner uniquely.
Different physical C6s therefore cannot represent the same original
six-incidence set. This recalls the scoped bijection in Draft PR #652;
it does not assume any unproved packet construction.

This proves the general selection lemma

    |I_G| >= L^2 / [4(4C_s+L)],                   (7)

with original-ID pairing, no cherries and BOTH coordinate cuts. Any
preassigned physical witness edge of an ID in I_G survives automatically.
No minimum-degree property is asserted or needed.

## 4. Applying the selector to the full-H degree tail

For s>=64 the elementary minimal-alphabet estimates give

    a<=2s^(3/2), a^2<=4s^3, N<=2s^4,
    C_s<= (1+s^(-2))(1+2/sqrt(s))*s^4 <(3/2)s^4.   (8)

For example, b=floor(2s^(3/2)) satisfies
binom(b,2)>=2s^3-3s^(3/2)+1>=V in this range. For the second inequality,
3s^(3/2)<=3s^2/8 and s<=s^2/64 leave a positive difference
s^2*(s-89/64). This proves the alphabet bound without rounding error.
The other two bounds follow by substitution: N/s^4=(1+1/s)^2(1+1/s^2)<2
and (1+1/s^2)(1+2/sqrt(s))<3/2 for every s>=64.

Every physical edge has a unique true original incidence ID. Let I be
all IDs with at least one physical diagonal touching Q_T, and preassign
one such heavy witness edge to each. Since one ID has exactly two
diagonals,

    L=|I|>=E_T/2>=epsilon*s^4/2, L<=N<=2s^4.

Equations (6),(8) give |J|>=L^2/(8s^4)>=epsilon^2*s^4/32.
After the two coordinate cuts,

    |I_G|>=epsilon^2*s^4/128 = beta*s^4,
    beta:=epsilon^2/2^7.                          (9)

Each retained ID keeps its heavy witness edge touching the ORIGINAL full-
graph set Q_T. This is not a new high-degree set computed after pruning.
Moreover

    |Q_T| <=4N/(Ts)<=8s^3/T<=16s^3/T.             (10)

Thus G has at least beta*s^4 distinct heavy witness edges incident with
a set Q_T of size at most 16s^3/T. These edges remain pair-coherent and
the whole graph G has the coordinate-proper-cycle property.

## 5. Balanced chunks, not unbalanced supersaturation

Use the bipartition X,Y of G given by the left coordinate cut. Assign
each heavy witness to one of its endpoints lying in Q_T. At least half
the witnesses have assigned endpoint on one side, say X. Let

    R=Q_T intersect X, r=|R|<=16s^3/T.

The actual physical bipartite graph between R and Y therefore has at
least beta*s^4/2 edges. Put n=a^2<=4s^3. Partition Y into at most
ceil(|Y|/r)<=2n/r chunks of size at most r. Some chunk F, together with
R, has

    e(F)>=beta*r*s/16,
    v(F)<=2r,
    e(F)/v(F)>=beta*s/32.                         (11)

Since v(F)<=32s^3/T, condition

    T>=2^20 C_graph^3 beta^(-3)                   (12)

ensures e(F)/v(F)>=C_graph*v(F)^(1/3). Apply the proved BALANCED
theorem (SS6) to this ONE ordinary physical subgraph F:

    #C6(F)>=c_graph*(beta/32)^6*s^6.              (13)

No vertices are cloned; no degenerate closed walks are counted. F need
not retain paired diagonals, because it is used only to count cycles
inside the already paired coherent graph G. Every such C6 is still
coordinate-proper and backed by its six distinct genuine source IDs,
so #C6(F)<=D6(f,g).

Substituting beta=epsilon^2/2^7 into (12),(13) gives precisely

    T>=2^41 C_graph^3 epsilon^(-6),
    D6>=c_graph epsilon^12 s^6/2^72.

This completes the proof of (1). For (2), put epsilon=E_T/s^4. If the
threshold on T holds, invert the D6 conclusion. If it fails, invert the
threshold itself. The two alternatives prove the stated maximum/sum bound.

## 6. What this permits, and what remains open

Deleting every whole original ID with any diagonal touching Q_T removes
at most E_T original IDs and at most 2E_T physical edges. The remaining
paired graph has maximum degree <=T*s. Under S=o(s^6), taking T large
therefore retains an arbitrarily large fraction of the FULL H edge set.
It is a degree truncation, not a claim that this near-full graph already
has no cherries or coordinate cuts; enforcing those can still cost a
fixed positive fraction of its incidences.

In particular this theorem does not put the near-full graph above a
generic proper-C6 extremal threshold after the cuts. It proves neither
sum_U L_*(U)=Omega(s^6) in PR #658 nor a universal positive bound for
the other six accepted families. The root global transversality/compensation
inequality remains unproved.

## 7. Graph theorem provenance

The balanced even-cycle supersaturation theorem (SS6) is classical.
Jiang--Yepremyan, "Supersaturation of even linear cycles in linear hypergraphs",
arXiv:1707.03091, includes the graph case r=2 and attributes it to
Simonovits. Williams--Westover, arXiv:2411.07499v2, explicitly restate the
balanced graph result as Theorem 2. Their general unbalanced extension
is conjectural; the chunk argument above deliberately does not import it.
The source-to-D6 bijection is the scoped theorem in Draft PR #652, and the entire
new selection/tail argument is independent of #656's packet existence.

Finite source-ID selector and provenance checks accompany this proof in
`hyp105_full_physical_degree_tail.py` and `research/fixtures/hyp105_full_physical_degree_tail_results.json`. Those
finite checks verify the selection identities, not asymptotic graph
constants or the root seven-family claim.
