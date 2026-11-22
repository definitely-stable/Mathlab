# GIO-001.3 / G6-C1 — intrinsic Moore-defect matrices, A1/A2/A3 gate without a GQ witness

**Parent:** [#793](https://github.com/definitely-stable/Mathlab/issues/793); **meta:** [#790](https://github.com/definitely-stable/Mathlab/issues/790); **frozen base:** `f42aa108a2f9e15dadebf5c45fa4923cc435742b`. This is a genuinely **intrinsic** structural theorem for **any** biregular source-incidence graph of girth at least eight, not a theorem derived from a hidden GQ template. It closes **restricted A1 and unconditional A2** plus the exact projection part of A3. It does **NOT** prove complete T3, `D6+BBo=Omega(r^6)`, the original generalized ASET exponent, or existence of an infinite non-GQ family meeting all the new hypotheses.

## 1. Precise domain: no GQ assumption

Let `I subset P x L` be a **simple** typed incidence graph (named original source flags). Every point has degree `t+1`, every line contains `s+1` points, with integer `s,t>=2`. The incidence graph has girth `>=8`: no original 4- or 6-cycles. It need not be connected, geometrically classical, fully projected, a generalized polygon, have a field, or be the result of any edit to a GQ.

Set `r=min(s,t)`; fix an integer `b>=1` **before the family** with `max(s,t)<=br`. Let

```
V_P0=(s+1)(s*t+1),   V_L0=(t+1)(s*t+1)
Delta_P=|P|-V_P0,     Delta_L=|L|-V_L0.
```

The Moore path argument forces both excesses nonnegative and
`(t+1)Delta_P=(s+1)Delta_L`. There are exactly
`|P|Delta_L` nonincident point-line pairs without any original 3-flag path,
and each source flag belongs to exactly `3st` of the existing unique projections
(the restricted lemma in draft [#800](https://github.com/definitely-stable/Mathlab/pull/800) is reproved here independently, with no import from that branch).

**Linear-excess A1 hypothesis:** fix **another integer C>=0 before the family** and assume

`0<=Delta_L<=C*r.`

This is deliberately **stronger** than the `Delta_L=O(r^2)` condition adequate merely for an `O(r^5)` missing-endpoint budget. We do not assert that an infinite genuinely non-GQ family with linear excess exists. Finite doubled GQ sources have excess `Theta(r^3)` as r grows and are only out-of-range diagnostics, not evidence for this asymptotic hypothesis.

For arbitrary **complete** independently typed but not probabilistically independent factor maps
`f:P -> binom([aP],2)`, `g:L -> binom([aL],2)`,
the maps are separately globally injective and use the **minimal** alphabets `aP,aL`. They can be adversarial and arbitrarily correlated. No projection/label compatibility beyond these axioms.

## 2. Lemma D: exact defect-corrected collinearity matrix identity

Let `A_P` be the point-collinearity adjacency matrix. Put
`k=s(t+1)`, `lambda=s-1`, `mu=t+1`, `theta=lambda-mu=s-t-2`.
For a nonincident source point q and line ell, say `(q,ell)` is *missing* if NO original 3flag projection `q--J--u--ell` exists.

Define **entrywise nonnegative integer matrix**

`D_P[q,z] = number of lines ell through z for which (q,ell) is missing.`

In particular, a missing (q,ell) contributes one to `D_P[q,z]` for each z incident to ell. Then the **exact** identity holds entrywise:

```
A_P^2 = (k-mu) I + theta A_P + mu * 1*1^T - D_P.   (D-point)
```

**Proof by cases.** The diagonal common-neighbor count equals `k`. Two adjacent distinct points share precisely their other `s-1` line points: an additional common neighbor would produce an original 6-cycle. For distinct nonadjacent q,z, each common neighbor u corresponds to exactly one line ell through z with a 3path from q; a second foot for the same ell would produce a source 4/6-cycle. Thus the number of common neighbors equals `(t+1)-D_P[q,z]`. All matrix entries follow, including diagonal/adjacent zero defect.

The matrix `D_P` is **symmetric** because the other three matrices and `A_P^2` are symmetric. Every row sum is exactly

```
d=(s+1)*Delta_L,
```

since each point is missing exactly `Delta_L` nonincident lines and every such line has `s+1` source points. Consequently `||D_P||_2 <= d`: a symmetric entrywise nonnegative matrix with constant row sum d has all eigenvalues in [-d,d] by the max-absolute-row-sum bound.

**Dual statement**, independently for the line-collinearity adjacency matrix `A_L`, swaps s and t. Its defect matrix `D_L` has the **same** row sum
`(t+1)Delta_P=(s+1)Delta_L=d`. The exact dual identity uses
`k_L=t(s+1)`, `lambda_L=t-1`, `mu_L=s+1`,
`theta_L=t-s-2`.

**Exact negative-eigenvalue falsifier.** For the disjoint union of two W(3,2) copies, `D_P` has 15×15 zero diagonal blocks and off-diagonal blocks `3*11^T`; its row sum is `d=45`. The 30-entry signed vector `(+1)^15,(-1)^15` is an exact eigenvector of eigenvalue **−45**, so `v^T D_P v=-45||v||²<0`. Therefore a purported proof that treats an entrywise-nonnegative projection-defect matrix as **positive semidefinite** is false. This is why Lemma S uses the two-sided bound `|v^T D v|<=d||v||²` on centered vectors, whereas the Gram upper bound in Theorem A1-C only drops `u_z^T D u_z` for actual *nonnegative indicator* vectors.

For a genuine GQ, `Delta_P=Delta_L=0`, so both D matrices vanish and the classical strongly regular identities from #799 reappear **exactly**. In a non-GQ source the correction must not be silently discarded. Nothing here asserts that `D_P` is positive semidefinite; it is entrywise nonnegative and symmetric, which is strictly weaker.

## 3. Lemma S: explicit intrinsic spectral envelope

A_P is k-regular, so its all-ones vector has eigenvalue k, regardless of connectedness. On the orthogonal complement of this vector take any eigenvalue `x`. Apply (D-point) to a unit eigenvector and use `|v^T D_P v|<=d`:

```
x^2 <= |theta|*|x|+(k-mu)+d.
```

It follows without any GQ eigenvalue formula that

```
|x| <= Lambda_P := |s-t-2|+
           ceil(sqrt((s-1)(t+1)+(s+1)*Delta_L)).
```

The dual inequality is

```
|x_dual| <= Lambda_L := |t-s-2|+
           ceil(sqrt((t-1)(s+1)+(t+1)*Delta_P)).
```

Both are exact **integer** safe upper bounds, and under `max(s,t)<=br`, `Delta_L<=Cr`, they satisfy `Lambda_P,Lambda_L=O_{b,C}(r)`, with no hidden field representation or spectral GQ theorem.

The restriction `Delta_L=O(r)` has an important role: if only `Delta_L=O(r^2)` is known, this elementary defect bound yields at best `Lambda=O(r^{3/2})`, too weak *by this method* for the fixed `O(r^4)` conflict budget. This does **not** prove a stronger bound impossible; it identifies an unfilled analytic gap.

## 4. Theorem A1-C: intrinsic conflict and Gram bounds under linear excess

For each factor symbol z define its incidence indicator `u_z` on the corresponding point or line factor vertices. Because f/g are globally pair-injective, no pair of distinct vertices shares more than one factor symbol and each symbol is used at most `a-1` times. Thus

```
sum_z |u_z| = 2V,     sum_z |u_z|^2 <= 2V(a-1).
```

For the point-collinearity graph set `e_col(f)` to the number of its edges whose two factor pairs share one symbol. Decompose `u_z= (|u_z|/V)*1 + v_z` with `v_z orthogonal to 1`. The spectral cap gives

```
e_col(f) = (1/2)sum_z u_z^T A_P u_z
         <= (k/(2V))sum_z |u_z|^2 + (Lambda_P/2)sum_z |u_z|
         <= k(aP-1) + Lambda_P * V_P.
```

Apply the dual inequality to `e_col(g)`. Because the original incidence has no 4-cycles, original owner conflict edges are in **literal bijection** with these point/line collinearity collisions, and the two types do not overlap:

```
e(J) = e_col(f) + e_col(g).
```

For `Delta_L<=Cr` this yields, uniformly over **every admissible f,g**,

`e(J) <= J_{b,C} * r^4`.

For point-symbol indicators, define the exact "pencil square"

`G_P = sum_z ||A_P u_z||_2^2.`

Use the defect identity and the fact that `sum_z u_z^T D_P u_z >=0` (all u_z and D_P entries nonnegative):

```
G_P = 2V_P(k-mu) + 2(s-t-2)e_col(f)
       + (t+1)sum_z |u_z|^2
       - sum_z u_z^T D_P u_z.
```

The dual has the same formula with s,t exchanged. Minimal alphabet size `aP,aL=O_{b,C}(r^{3/2})` and the just-proved `e_col=O_{b,C}(r^4)` yield

```
G_P+G_L = O_{b,C}(r^{11/2}).
```

This is precisely the structural scale needed by the old GQ LOW analysis. **It does not automatically provide all mixed FULL/CORE book moments or the produced BBo source inverse.**

### Fully explicit integer envelopes (not published C6 constants)

For `r>=2`, fixed b,C, define

```
v0=(b+1)*(b*b+1+C)
a0=2*v0+3
k0=b*(b+1)
theta0=b+2
lambda0=theta0+(b+1)*(b+C)
j0=k0*a0+lambda0*v0
J0=2*j0
G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0.
```

They satisfy `V_P,V_L<=v0*r^3`, `aP,aL<=a0*r^(3/2)`, `Lambda_P,Lambda_L<=lambda0*r`, each typed collinearity conflict count `<=j0*r^4`, total `e(J)<=J0*r^4` and **each** Gram `G_P,G_L<=G0*r^(11/2)`. All test certificates check squared last inequalities in exact integer arithmetic, avoiding floating-point threshold errors. These constants are deliberately loose, but **effective from the intrinsic hypotheses only**; they do NOT purport to numerically instantiate the external ordinary graph C6 supersaturation constants used by #799.

## 5. Lemma A2-U: universal proper physical six-cycle inverse, no incidence geometry hypotheses

Suppose only that the original source is simple and both complete physical factor maps are globally pair-injective. Every flag (p,l) owns its two actual opposite physical rectangle diagonals in the bipartite physical coordinate graph. Unique factor pair labels force **unique ownership** for every physical edge.

For any proper physical C6 whose six physical vertices have six distinct point-symbol coordinates **and** six distinct line-symbol coordinates, let `e_0,...,e_5` be its physical edges. The source point factor for `e_i` has pair label `{x_i,x_{i+1}}` and source line factor has `{y_i,y_{i+1}}`. As the physical symbols along the cycle are all distinct, these six unordered pairs are distinct in each factor. Therefore the corresponding source point IDs and line IDs are each distinct, and the six source owner columns have **the same labelled original six-cycle dual topology** in both factors. This is exactly historical `D6`.

Conversely, every historical D6 sixset has the same source dual 6-cycle in both factors; intersections recover a proper physical rainbow six-cycle, unique up to the standard dihedral rotation/reversal canonicalization. This is a **field-, projection-, girth- and GQ-free bijection** of six-ID historical D6 with proper physical rainbow C6 for any simple source with injective factor pair maps.

The finite regression constructs a genuinely non-GQ incidence source containing an actual original C4 by degree-preserving flag switching of W32, and uses two different physical-first and source-first DFS enumerators on that *edited* graph. They must return the identical keyed original six-ID sixsets and canonical physical cycles. It tests the universal inversion claim; it is not used as the all-order proof.

**Consequence for T3 dependency DAG:** A2's basic rainbow physical C6->D6 inverse needs **no new geometric axiom** at all. A1's conflict and pencil-square estimates now have a genuine, independently verifiable non-template source condition. A3's original projection defect and exact load also hold for all biregular girth-eight sources. Remaining difficult work lies in A4/A5 (same priority/LOW, FULL/CORE mixed books) and A6 (aligned produced historical BBo inverse with partial/missing projections and mixed walks).

## 6. Adversarial finite falsifiers and scope

Added code:
- `research/gio_t3c_intrinsic_defect.py`: rebuilds sources from literal incidence lines, requires exact (s,t) bidegrees and no source 4/6 cycles; enumerates **all** nonincident 3paths and source flag loads without reading GQ structure or spectrum; constructs both explicit defect matrices and checks each entry of both A² identities; exact conflict source-owner J vs collinearity counts; exact symbol-first Gram/defect corrections; integer spectral gates and quantified b,C ledger; non-GQ connected two-edge-switch double W32 high-excess source and non-GQ inner-C4 short-cycle source for universal D6 inverse.
- `research/test_gio_t3c_intrinsic_defect.py`: independent all-source-3walk oracle, independent defect reconstruction from A², direct owner conflict check, rational all-excess ledger guards, 1-perp integer Rayleigh vectors, invalid C4/regularity rejection, nonzero doubled-source defect regression, full physical vs source first D6 after actual short-cycle switching.
- `.github/workflows/gio003-g6c-intrinsic-defect.yml`: GitHub-hosted specialist, exact certificate and strict fail-closed checks; standard PR Research/INDEX jobs required on exact HEAD.

Genuine small GQ fixtures: W(3,2), odd W(3,3), true Q^-(5,2) GQ(2,4), dual GQ(4,2). Non-GQ girth-eight examples: two copies of W32, including **connected** degree-preserving cross-switch. Their `Delta_L=15` with `r=2` is well outside a small fixed-C asymptotic family, although a finite conditional ledger with `C=ceil(15/2)=8` is arithmetically valid for that individual witness. A separate within-W32 flag switch creates original C4 and **must fail the girth-eight entry gate** while still satisfying universal A2-U.

## 7. Prior art, independent review gates, STOP

Ordinary GQ strongly regular collinearity spectra are classical (see [Godsil's notes, Distance-Regular Graphs, Section 8](https://www.math.uwaterloo.ca/~cgodsil/pdfs/bigGeom.pdf)). Bipartite Moore-bound/excess methods and the small-excess/cage problem also predate this research ([On biregular bipartite graphs of small excess](https://www.sciencedirect.com/science/article/pii/S0012365X19301232), [Bipartite biregular Moore graphs](https://www.sciencedirect.com/science/article/pii/S0012365X21002958)). The correction-matrix formula is an elementary combination of exact 2-walk counts and existing graph spectral methods; do not assert publication priority or that conditional A1 is globally novel before a dedicated prior-art review.

**Acceptance required:** independent exact finite falsifiers, formula proofs with all quantified assumptions in this manuscript, exact-head specialist + full Research + INDEX SUCCESS, internal critical referee review. This is a **scoped proof**, not external human peer review or Lean certification.

**STOP:** No universal `D6+BBo>=delta r^6` for arbitrary non-template incidence systems; no existence of genuinely non-GQ near-Moore *linear-excess* infinite family; no proof that `Delta_L=O(r^2)` alone forces `e(J)=O(r^4)`; no GQ-independent A4/A5 mixed book moment or A6 produced aligned BBo inverse; no ASET exponent improvement. Do not close #793 or merge unrelated PR stacks. Next G6-C2 should attack A4/A5/A6 using the exact defect/Gram ledger, or derive a sharp impossibility example for the proposed remaining axiom set.
