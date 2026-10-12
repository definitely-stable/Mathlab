# HYP-105 K3-G2-A — original-source coincidence theorem for repeated six-cycles

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked child of [PR #373](https://github.com/definitely-stable/Mathlab/pull/373) at pinned head `53df42a07ae0ffbe0e168b68e2711122d5526f97`. PR remains Draft; `main` untouched.

**Scientific status: RESTRICTED_THEOREM_C / ALL-h EXACT SOURCE COINCIDENCE / LOCAL REPEAT o(s^6) / CROSS-ORIGINAL-SOURCE LOSS OPEN.** Neither seven-family S obstruction nor full R3 obstruction is proved.

## 1. Why K3-G1's J=O(s^6) is not enough

K3-G1 established the exact repeated-column incidence count J, the three-repeat C6 pencil-triangle bijection, and `J<=4V(a-2)^2=O(s^6)`. Because total C6 lower bounds can themselves have order s^6, bounding J by the *same* order with an uncontrolled coefficient is insufficient. Independently sharpening global maxima loses the global relation of the original sources.

The next defensible result is to partition J by whether its two aligned 2-paths arise from ONE ORIGINAL source point/line or from TWO DISTINCT original sources. This is a mathematical dichotomy, not a threshold chosen after a finite census.

## 2. Exact factorization through ORIGINAL W(3,s) incidence

Let `I` be the original point-line incidence, and let f and g be one coherent global pair injection. For an original line `l` with physical g(l)={y,y'}, define `t_q(y,y')` as the number of physical t outside {y,y'} for which the two original lines whose physical labels are {y,t}, {y',t} intersect in the **same original point q**. It is zero if either physical label is unused.

GQ partial linearity ensures uniqueness of q for each t. The aligned Kikuchi common-neighbor count is exactly

```
c((x,y),(x,y')) = sum_{q original point} 1[x in f(q)] * t_q(y,y').
```

Now take an original incidence (p,l) with f(p)={x,x'}. Its **horizontal** antipodal repeat contribution is the product `c((x,y),(x,y'))*c((x',y),(x',y'))`. Expanding gives two independently selected original source points q,r. A source coincidence q=r forces f(q)={x,x'}=f(p), and global injectivity forces **q=p**. The point/line-dual argument gives identical structure for the vertical matchings, with source line coincidence forcing the anchor original line l.

For true W(3,s), no two aligned 2-paths in these opposite matchings share an intermediate physical vertex: otherwise two DISTINCT original lines would have two distinct common original points (dual assertion similarly). Thus the "shared intermediate" subtraction of K3-G1 is *identically zero* for every legal labeling. This extra simplification is GQ-specific and checked by the independent oracle.

## 3. Same-source means a physical triangle in an original pencil

For every original point p, its physical line-pencil graph `G_p` has edges `g(l)` for all s+1 lines incident to p. For every original line l, its physical point-pencil graph `F_l` has edges `f(p)` for all s+1 points on l. Define `tau_e(H)` as the number of graph triangles in H using physical edge e.

For p incident l, the number `t_p(y,y')` is exactly `tau_{g(l)}(G_p)`: the two line edges labelled {y,t}, {y',t}, together with {y,y'}, make a physical triangle. The dual statement holds for `F_l`.

Thus the **new exact all-h identity** is

```
J_same =
    sum_{(p,l) in I} [tau_{g(l)}(G_p)^2 + tau_{f(p)}(F_l)^2].
J_cross = J - J_same >= 0.
```

Summing tau once instead of its square counts every physical pencil triangle exactly three times. Therefore `sum_{(p,l)} [tau_g+tau_f]=3*C6_rep3` by K3-G1's pencil bijection, and

```
C6_rep1_local = J_same - 3*C6_rep3
              = sum_{(p,l)} [
                   tau_{g(l)}(G_p)*(tau_{g(l)}(G_p)-1)
                 + tau_{f(p)}(F_l)*(tau_{f(p)}(F_l)-1)].
C6_rep1_cross = J_cross.
C6_rep1 = C6_rep1_local + C6_rep1_cross.
C6_repeated = J_cross + C6_rep1_local + C6_rep3.
```

The source-local single-repeat term has a clear interpretation: two distinct triangles share the SAME physical pencil edge. The cross-source term is the remaining case where the two independently chosen 2-paths originate from different original points or lines, even though their labels are correlated by the same global f,g.

## 4. Uniform o(s^6) local-loss theorem

For ANY simple graph H with m edges, let `d_u` be its degrees. Every edge `e={u,v}` satisfies `tau_e<=min(d_u,d_v)`, hence `tau_e^2<=d_u*d_v`. Since edges are a subset of all unordered vertex pairs,

```
sum_{e in E(H)} tau_e^2
  <= sum_{uv in E(H)} d_u*d_v
  <= sum_{u<v}d_u*d_v
  <= (sum_u d_u)^2/2 = 2*m^2.
```

Each original W(3,s) pencil has precisely m=s+1 distinct physical edges, and there are V source points and V source lines. Hence universally, for every legal globally injective f,g:

```
0 <= J_same <= 4*V*(s+1)^2 = O(s^5) = o(s^6).
0 <= C6_rep1_local <= J_same = o(s^6).
C6_rep3 <= J_same/3 = o(s^6).
C6_repeated = J_cross + O(s^5) (nonnegative remainder).
```

This is the **new asymptotic gain** absent in K3-G1. It identifies where the possible s^6-scale repeated-source loss must live: in genuinely TWO-DISTINCT-ORIGINAL-SOURCE path pairs. A proof that `J_cross=o(s^6)`, or a quantitative coupled C6-vs-cross inequality, would remove K2's repeated-column obstruction for the full-R3 route.

Crucially, the full R3 route is different from original seven-family S in issue #230. Even if this obstruction is removed, the other improper six-distinct-column cycles still require independent classification or charging before Branch A.

## 5. Falsification and acceptance

- A reference oracle counts every triangle and edge-triangle load in point/line source pencils. It certifies the exact formula, `C6_rep1_local`, `J_cross`, and the uniform O(s^5) bound using exact integers.
- An independent oracle enumerates both antipodal 2-path matchings for **every original incidence**, reconstructs each internal path's original point/line from the one global f,g, and directly separates same-source versus cross-source witnesses. It raises on forbidden shared intermediate vertices.
- An independently enumerated physical triple-of-vertices oracle verifies triangle edge loads, sums of tau, sums of tau squared and their universal 2m² cap, including pathological star/book/clique pencils.
- Genuine W(3,2) lex/reverse and W(3,4) lex/random maps; explicit input budgets fail closed. Dedicated GitHub-hosted Contract, inherited full Research and INDEX; no redundant research matrix.
- Until exact-head hosted CI and independent review, PR stays Draft and `main` untouched.

## 6. Next K3-G2-B / alternate original-seven-family branch

Build a **joint original-source pair incidence kernel** for `J_cross` that retains `q != r`, the original point/line GQ incidence constraint and both global injections. Demand either `o(s^6)` uniformly or an exact constant strictly below a simultaneous C6 supersaturation floor (after Theta). Finite extremal stress tests can falsify candidate kernels but cannot certify all h. If these attempts fail, return directly to the proper D6 + other six accepted S-family motif geometry, not to uncontrolled improper cycles.
