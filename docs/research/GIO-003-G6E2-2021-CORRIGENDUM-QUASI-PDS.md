# GIO-003 / G6-E2 — corrected 2021 quasi-perfect domination, true matching deletion and uniform GQ compression

**Scope and exact base:** [issue #793](https://github.com/definitely-stable/Mathlab/issues/793), frozen parent [G6-E1 Draft #813](https://github.com/definitely-stable/Mathlab/pull/813) at `d82b8d784710e47e37ca30d912ee097f9dfbea57`. New research branch separate; no main writes, no automatic merge.

**Critical prior-art rule:** Abreu, Araujo-Pardo, Balbuena, Labbate, *A construction of small (q−1)-regular graphs of girth 8*, *Electronic Journal of Combinatorics* 22(2) (2015), #P2.10; **corrigendum added May 18, 2021 to THE SAME PDF**, pp. 9–11: [EJC corrected publisher PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p10/pdf/). The original 2015 Theorem 5 claiming an infinite family of order `2q(q−1)^2` is **RETRACTED in the publisher PDF**. The purported perfect dominating set works only at q=5 and not at q≥7. **Never use that theorem for all orders.** The new construction is the *published* corrected family of order `2q(q²−q−4)`; its graph construction is prior art, not new worldwide mathematics.

## 1. Objective, exact correction, and comparison to G6-E1

G6-E1 constructs a true q-regular near-Moore source by deleting a published *perfect* dominating set B from GQ(q,q), with q(q²−2) vertices on each partite side, true original flags q²(q²−2), defect `2q(q−2)<2(q−1)²` and a *geometrically proved* centered-F0 operator bound `2(q−1)³`.

G6-E2 investigates a **different degree**, namely *q−1* with new `r=q−2` (not q−1). It uses the CORRECTED 2021 construction, which deletes a **quasi-perfect** dominating S from the G6-E1 intermediate source G_q^x, then removes all edges of a **matching M** joining the remaining degree-q vertices. This last step is essential: the resulting incidence is NOT merely a row/column submatrix of the GQ parent. The naive G6-E1 compression inequality without the matching perturbation is logically invalid here.

Correct theorem / exact source parameters for odd prime-power q≥7:

```
  |P|=|L| = q(q²−q−4)
  degree of each ORIGINAL vertex = q−1 = r+1, r=q−2
  original flags = (q−1)q(q²−q−4)
  original Moore excess:
    Δ_P=Δ_L = q(q²−q−4)−(r+1)(r²+1)
            = 4r²+3r−5 <=5r²   (r>=5).
```

For all q>=7 this order differs from the retracted 2015 expression q(q−1)². At the exceptional q=5 the two order formulas coincide numerically (both equal 80 vertices per type), consistent with the corrigendum's statement that the old proposed perfect dominating set worked only at q=5; this isolated equality must never be promoted to the false all-order construction. For q=7, the q−1 construction has 266 original points +266 lines, 1,596 original flags, true Δ=110. For q=5 it yields a finite exceptional example of 80 points+80 lines, 320 original flags, Δ=40, but q5 is **never used as evidence for the incorrect 2015 all-order statement**.

## 2. Corrected source construction from ACTUAL original incidences

Let F_q be the finite field and `∞` the symbolic infinity name in the G6-E1 Γ_q coordinates. Choose x,y∈F_q according to corrected **Theorem 5** of the 2021 corrigendum:

- q odd, q≥5; x and y are distinct from each other and from 0,1,−1.
- If q≡1 (mod 4) and q>5, require x²+1=0 and y=x^{−1}. For q≡3 (mod 4), no such extra equation.
- For the implemented **literal prime-field** controls q=5 choose x=2,y=3; q=7 choose x=2,y=3. The symbolic all-order theorem uses the published existence and finite-field equations for all appropriate odd prime powers, not a fake GF(q) implementation for arbitrary composite q.

Build the literal q-regular G6-E1 original source `G_q^x=Γ_q\B` with x as the already published perfect-domination parameter. Its actual named vertices are point triples `(a,b,c)_0`, line triples `(a,b,c)_1` including ∞, and the ORIGINAL incidence adjacency (no factor f/g).

Set the following ACTUAL line vertices

```
   R = {(1,b,−2b)_LINE, (−1,b,2b)_LINE : b∈F_q}.
```

With `N_G[U]=U ∪N_G(U)` denoting the **closed** original one-neighborhood, set

```
   S = ( ⋃_{j∈F_q} N_{G_q^x}[(∞,y,j)_POINT] )
         ∪ N_{G_q^x}[R].
```

The corrected Theorem 5 proves S is **quasi-perfect**, NOT perfect. Its total cardinality is `2q²+4q` with exactly `q²+2q` removed from each typed side. The remaining true original point/line graph has degrees **q−1 or q**. The surviving degree-q vertices are exactly the endpoints of a MATCHING

```
  M = {
    ((a,b,t)_LINE, (∞,a,t)_POINT) :
    a∈F_q\\{0,1,−1,x,y}, b∈F_q,
    t=−b(a+a^{-1})
  }.
```

Here every edge is independently validated as a **literal source incidence**, all matching endpoints are distinct, and the set of all degree-q vertices after S is EXACTLY the set of endpoints of M, never just a numerical degree prediction. The matching has `q(q−5)` original edges (14 at q=7; no edges at exceptional q5). Delete those edges and then reconstruct **the entire final graph from ORIGINAL remaining point-by-line flags**. The geometry-free G6-C1 `source_graph` independently enforces uniform q−1 degree, true girth≥8, exact original missing point→line threeflag projections and original flag loads `3r²`; it never synthesizes a missing F or fills projected GQ anchors.

**Source-first q=7 falsifier:** S alone leaves 28 vertices of degree 7 and 504 vertices of degree 6 on the two sides together, so declaring S perfect or skipping M is immediately falsified. Removing all 14 matching edges makes every survivor degree 6. This is why the 2021 corrigendum is an absolute stop condition for replication of the 2015 paper.

## 3. New Mathlab-specific GQ-source spectral transfer with edge-perturbation

The original parent Γ_q is a true GQ(q,q) from G6-E1. Let its ORIGINAL 0/1 point-by-line incidence be B, with singular values

```
   σ1(B)=q+1,
   σ2(B)²=2q,
   all remaining singular values <=sqrt(2q).
```

After the two vertex deletions B and S, let K denote the corresponding **square original induced submatrix** of B on the final survivor vertices, BEFORE the matching edge removal. The **actual final original incidence matrix** is

```
   C=K−E_M,
```

where E_M is a 0/1 **partial permutation matrix** of the published matching. For q≥7, M is nonempty, and `||E_M||_2=1` exactly (this is not true for an arbitrary collection of removed flags). By singular-value interlacing under row/column compression and Weyl's singular-value perturbation inequality,

```
   σ2(K) <=σ2(B)=sqrt(2q),
   σ2(C) <=σ2(K)+||E_M|| <=sqrt(2q)+1.
```

The corrected published source C is square and (q−1)-regular, so its top singular value equals `q−1`. For q≥7, `q−1>sqrt(2q)+1` because `(q−2)²>2q`; therefore the source is automatically **connected** and every nonprincipal eigenvalue x of its ORIGINAL `T=CCᵀ` and `U=CᵀC` lies in

```
  0<=x<=(sqrt(2q)+1)².
```

Set `r=q−2>=5`; note `2q=2r+4<=49r/16` and `1<=sqrt(r)/2`. Thus

```
   sqrt(2q)+1
      <=(7/4+1/2)*sqrt(r)=(9/4)*sqrt(r);
   x<=81r/16.
```

Apply the **corrected original G6-D1 cubic missing-projection identity** for the actual FINAL source with `h=s+t=2r`:

```
 T(T−2r I)²=FFᵀ+(|L|−2Δ_L)J,
 centered F0F0ᵀ = T(T−2r I)² on 1^perp.
```

Here F is the matrix of **genuine ORIGINAL absent threepath projections AFTER BOTH S and M**. The function `p(x)=x(x−2r)²` on `[0,81r/16]` has a stationary local maximum at `x=2r/3` and an endpoint maximum at `x=81r/16`; exact arithmetic gives

```
 max p(x) <=max{ 32r³/27,
                 (81r/16)*(49r/16)² }
           = (194481/4096)r³ <48r³.
```

This holds on **BOTH original source types** (same nonzero incidence singular values), with no independent global F0 spectral assumption, no sixth-moment condition and no numerical eigenvalue rounding.

Hence the CORRECTED 2021 source family for every odd prime power q≥7 satisfies the fixed G6-D2 DIRECT gate:

```
     b=1, C=5, κ=48,
     Δ_L=Δ_P=4r²+3r−5<=5r²,
     ||F0||²<=48r³.
```

The large constant κ=48 is a SAFE simple universal bound derived from the parent + matching; it is **not claimed to be sharp**. A future improvement can exploit the matching geometry or full source spectrum to reduce it.

## 4. Conditional historical original-six-flag T3 transfer

Use exactly the accepted existing G6-D2 direct-operator all-order ledger
`integrated_quadratic_direct_ledger(b=1,C=5,kappa=48)`, together with source-original G6-C1 J/Gram, proper FULL/CORE G6-C2, original HEAVY/LOW single global owner G6-C3 and the external ordinary graph C6 theorem. Missing projections are never completed; original projection flag loads are `3r²` and the critical unprojected endpoint count remains `O(r⁵)`.

The imported chain gives only the **CONDITIONAL** all-order statement: there exist fixed positive δ,ρ and threshold r0, depending on the source gate and existential external graph constants, so that for every allowed arbitrarily correlated complete minimal pair-injective original f/g, every set of at most `ρr⁴` deleted ORIGINAL flags, and every corrected odd prime-power q≥7 with r=q−2≥r0,

```
  D6_original(I\\Z;f,g)+BBo_produced_original(I\\Z;f,g)
       >=δr⁶.
```

The numerical external graph constants C0=c0=1 in the inherited ledger are **FORMAL_ONLY placeholders**, NOT independently sourced optimal constants. This is NOT an unrestricted source theorem, new dependent GF(5)/ASET exponent, or an external referee certification.

## 5. Exact finite tests and publication guardrails

`research/gio_t3e2_corrigendum_quasi_pds.py` implements only literal finite fields supported by G6-D3 (q=5,7 are true prime fields) and the original G6-E1 parent; it never pretends to build prime-power q=9,25,49 from integer modular arithmetic.

`research/test_gio_t3e2_corrigendum_quasi_pds.py` independently verifies:

- q=5 exceptional finite original graph, the matching empty; q=7 *required* nonempty 14-edge actual matching, 126 original vertex deletions, exact 532 surviving original vertices, girth≥8 and 1,596 original flags.
- Both original point and line true incidence second-walk defect identities, full 3r² original projection loads, independently reconstructed final remaining flags vs exact S+M operation.
- q=7 lexicographic and correlated independently fixed minimal factor maps, original source conflicts J and source pencil Gram; no factor independence or source GQ completion.
- True original missing centered F0F0ᵀ rational PSD check at q=5 (finite exceptional source), plus the all-order Weyl/critical-polynomial source proof for q>=7.
- Corrigendum parameter falsifiers: forbidden x/y, odd vs even, extra x²+1=0 and y=x^{-1} for q≡1 mod4, q5 exception, and literal failed q7 regularity when M is incorrectly omitted.
- The original **false 2015 all-order order claim is explicitly rejected**; only the corrected 2021 `2q(q²−q−4)` family is asserted at all orders.

CI acceptance: exact PR HEAD specialist tests + machine-readable source JSON gate, INDEX and full Research GitHub-hosted SUCCESS. Independently audit the corrigendum provenance, the matching adjacency, the field operations, the singular-compression perturbation and both source types. Keep Draft; do NOT merge staged ancestors or close #793 automatically.

### 5.1 Genuine corrected q=7 historical six-original-flag BBo witness

Besides proving the source spectral gate, the corrected q=7, x=2, y=3 actual `G_q^x - S - M` source is passed directly through the **historical six-ID BBo owner inverse**. The targeted original FULL/CORE procedure finds a nontrivial BBo after examining only **44** actual physical threewalks; it extracts six pairwise DISTINCT original point-by-line flag IDs:

- Three ORIGINAL full projection anchors from a real nonincident source point/line pair with a valid threeflag path in the corrected source; and
- Three ORIGINAL physical edge owners from the residual threewalk.

The production certificate serializes all six original flag IDs, original point/line coordinates and the physical path itself. The three independent inherited implementations (manual physical, published physical and source-first original-owner inverse) agree exactly and report at least one produced BBo for the frozen **six original** owner flags. Deleting one ORIGINAL FULL projection anchor destroys that witness, a nontrivial negative control. The test also verifies that the corrected source **already had its 14 matching edges removed**, so no positive witness is accidentally counted on the wrong, quasi-regular pre-matching graph.

This is a **finite** witness for historical original six-ID machinery at the first literal corrected q>=7 source (q=7, 266 vertices each part, 1596 original flags). It is **not** a proof of the asymptotic `delta*r^6` conclusion at q=7, and it does not establish all-order T3 without the imported G6-C2/C3 analytic machinery.

## 6. Further research

The most valuable next source advance is **the EVEN prime-power q>=8 corrected Theorem 6**, which uses a different quasi-dominating S and matching M. Implement independently rather than reusing odd-coordinate formulas (the characteristics differ). Separately, improve κ=48 by exploiting the exact sign/symmetry of the matching perturbation instead of the blunt operator norm 1, or import the 2018 `q³−q sqrt(q)−q` smaller q-regular W(3,q) family for square q with its published source geometry.

**Bottom line:** this work repairs a potentially serious historical-paper reproducibility trap, verifies an additional ACTUAL corrected q−1-regular original family of different degree, and provides an unconditional SOURCE geometric norm gate for every odd prime power q>=7, within the existing conditional original six-flag framework.
