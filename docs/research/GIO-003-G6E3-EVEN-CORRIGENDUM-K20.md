# GIO-003 / G6-E3 — corrected EVEN characteristic 2021 source and improved κ=20 bound

**Tracking:** issue [#793](https://github.com/definitely-stable/Mathlab/issues/793), meta #790. Parent: [G6-E2 Draft #814](https://github.com/definitely-stable/Mathlab/pull/814) frozen exact HEAD ddac1e2eeb52556e7abda95f57ee6f5fd9c4a4ec (22/22 specialist, INDEX and full Research SUCCESS). New G6-E3 stays a separate stacked Draft. No merge or main change.

**Prior art, not a new graph discovery:** Abreu, Araujo-Pardo, Balbuena and Labbate, *A Construction of Small (q−1)-Regular Graphs of Girth 8*, EJC 22(2), #P2.10 (2015), **Corrigendum added May 18, 2021**, [publisher corrected PDF pp. 10–11, Theorem 6](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p10/pdf/). The incorrect 2015 all-order perfect-dominating source of order 2q(q−1)² is withdrawn. The corrected even-prime-power graph construction of order 2q(q²−q−4), quasi-perfect dominating set and matching are published PRIOR ART. G6-E3's contribution is a project-specific exact ORIGINAL-source realization and spectral transfer with improved even-field constant κ=20; neither the graph family nor singular-value interlacing itself is new.

## 1. Why EVEN characteristic is a separate theorem

G6-E2 built corrected ODD prime-power sources using two slopes +1 and −1. Reusing the odd formula at q=2^e is **invalid** because +1=−1 and 2b=0: its supposed 2q-element line set collapses to just q lines. The true Theorem 6 has DIFFERENT slopes m, m^{-1}, different original closed neighborhoods and an independently defined matching.

Fix any q=2^e≥8, with a finite-field representation F_q, and select exact field elements x,m such that x∉{0,1}, m∉{0,1,x}, and (for a deliberately fail-closed SUBFAMILY) **x≠m^{-1}**. The latter is a stronger source-independent requirement than the published theorem's minimum assumptions: it makes the five forbidden matching slope names distinct and ensures an exact q(q−5)-edge matching. It is always possible at all q≥8 and does not claim all allowed theorem-6 parameter choices satisfy this additional gate.

The relevant new Moore parameter is r=q−2; the corrected original bipartite source has degree q−1=r+1, and exactly

~~~
|P|=|L|=q(q²−q−4)
|I_original|=q(q−1)(q²−q−4)
Delta_P=Delta_L=|P|−(r+1)(r²+1)
               =4r²+3r−5 <=5r².
~~~

For the first ACTUAL finite field GF(8) (quotient by irreducible polynomial z³+z+1, encoded 0b1011), select x=2, m=3 and m^{-1}=6, all five forbidden elements distinct. Field addition is XOR, multiplication and inverses are exact polynomial arithmetic, and symbolic infinity q is NEVER included in field operations.

## 2. Literal source from original GQ coordinates

Reconstruct the TRUE generalized quadrangle Γ_q=GQ(q,q) from G6-E1's original point-by-line coordinate equations, then its original q-regular PDS-induced G_q^x (not the completed parent GQ). Let N_G[U] denote CLOSED original one-neighborhoods in this actual G_q^x.

Set α=m+m^{-1} in the **finite field**, with 2=0 in characteristic two. The corrected Theorem 6 defines original line set

~~~
R = {(m,b,αb)_LINE, (m^{-1},b,αb)_LINE : b∈F_q}.
~~~

The literal corrected QUASI-perfect dominating set is

~~~
A = union_{c∈F_q} N_G[(infty,1,c)_POINT],
S = A union N_G[R],

|R|=2q, |A|=q(q+1), |N_G[R]|=q²+3q,
A and N_G[R] disjoint, |S|=2q²+4q,
|S ∩ P|=|S ∩ L|=q²+2q.
~~~

After deleting S, survivor degrees are q−1 or q. S is **NOT** a perfect dominating set. The remaining degree-q vertices are precisely endpoints of the original source edge MATCHING

~~~
M = { ((infty,a,β_a b)_POINT,(a,b,β_a b)_LINE) :
      a∈F_q\{0,1,x,m,m^{-1}}, b∈F_q },
β_a=a+a^{-1}.
~~~

In characteristic two, β_a=0 would force a²=1, hence a=1, which is excluded. Therefore at fixed a, b↦β_ab is injective; for different a the original point second coordinate differs. The q(q−5) original matching edges have 2q(q−5) distinct endpoints. An independent graph-level check confirms **all** are actual undeleted original incidence flags, and exactly these endpoints are all surviving degree-q vertices. Remove M and re-run Mathlab's geometry-free source_graph on the final actual point-line flags. Girth≥8 is preserved and independently checked; source projection feet, missing threepaths, point/line Moore excess and every ORIGINAL flag load of 3r² are reconstructed on the FINAL corrected source, never synthesized.

For GF(8):

| Stage | Vertices per side | Degree | Actual original flags |
|---|---:|---:|---:|
| Full parent Γ_8 | 585 | 9 | 5,265 |
| Old original G_8^x | 496 | 8 | 3,968 |
| After S, before M | 416 | 7 or 8 | 2,936 |
| Final after S and 24 matching edges | 416 | 7 | 2,912 |

The 832 survivors before M consist of **48 original vertices of degree 8** and 784 of degree 7; deleting 24 disjoint original M flags repairs each degree-8 endpoint. Final original defect Δ_P=Δ_L=157. The final 416×416 source splits disjointly into 2,912 true ORIGINAL incidence flags, 104,832 true nonincident but projected threepaths, and 65,312 true absent-threepath pairs; their sum is precisely 416². In the source every original flag has exactly 3r²=108 projected-source anchors.

For the later q=16 (an EXISTING published family member), |P|=|L|=3,776, |I_original|=56,640, Δ=821. The code independently validates literal GF(16) parameter arithmetic and exact all-order formulas, but does **not** pretend to have instantiated q16's huge original source or matrix.

## 3. Automatic even-source spectral theorem with κ=20

Let B be the actual Γ_q point–line incidence matrix. The classical parent GQ(q,q) spectrum supplies

~~~
σ_1(B)=q+1,   σ_2(B)=sqrt(2q).
~~~

After the original vertex deletions B and S, let K be the original B row/column submatrix restricted to remaining TRUE original points and lines. The final source incidence C is **not** a pure row/column submatrix because matching flags were also removed. It is

~~~
C=K−E_M,
~~~

where the 0/1 matching incidence E_M is a partial permutation matrix satisfying ||E_M||_2=1 (for q≥8 the matching is nonempty). Standard singular-value compression and Weyl perturbation then yield

~~~
σ_2(C)≤σ_2(K)+||E_M||_2≤sqrt(2q)+1.
~~~

Final C is square and (q−1)-regular, hence its first singular value is q−1. For r=q−2≥6, r²>2q, so q−1>sqrt(2q)+1: the original source is connected, and the singular gap is not an artefact of ignoring additional disconnected principal modes.

The essential even-specific improvement is the **larger minimum r=6**:

~~~
2q=2r+4 ≤(8/3)r,
sqrt(2q) ≤(4/sqrt(6))*sqrt(r),
1 ≤sqrt(r/6).

Thus σ_2(C) ≤ 5 sqrt(r/6), and
nonprincipal x∈Spec(CCᵀ) or Spec(CᵀC)
satisfies 0≤x≤25r/6.
~~~

Apply the **CORRECTED G6-D1 cubic identity** to the actual original missing threeflag-incidence matrix F, with reduced source s=t=r and h=2r:

~~~
T(T−2rI)² = F Fᵀ + (|L|−2Delta_L) J,
U(U−2rI)² = FᵀF + (|P|−2Delta_P) J,
T=CCᵀ, U=CᵀC.
~~~

On the centered 1-perpendicular subspace the rank-one J vanishes. The squared spectral levels of centered original F0 are therefore p(x)=x(x−2r)². On [0,25r/6] this cubic has an internal critical maximum at x=2r/3 of 32r³/27, and a possibly larger endpoint:

~~~
p(25r/6)=(25r/6)*(13r/6)²=(4225/216)r³.

max_{0≤x≤25r/6} p(x)
  =max{32/27,4225/216} r³
  =(4225/216)r³ <20r³.
~~~

Thus **EVERY corrected even prime-power q≥8 source with the explicit five-distinct matching parameters** satisfies on BOTH original typed sides

~~~
b=1,   C=5,   κ=20  (FIXED before q, source and f/g),
Delta_L,Delta_P≤5r²,
||F0||_2²<20r³.
~~~

This is a complete geometric **source-gate proof**, not a guess from a finite numerical spectrum. The generic inequality and GQ spectrum are prior art; the resulting exact even-source gate and κ20 improve on the conservative odd-source κ48 in the Mathlab project. It is not asserted that 20 is sharp.

## 4. Historical conditional T3 transfer and finite BBo

The accepted G6-D2 **DIRECT** source theorem with fixed (b,C,κ)=(1,5,20) controls true original source J(f,g)=O(r⁴) and both pencil Grams O(r^(11/2)) for **any** complete minimal unordered-pair-injective fixed typed f/g, even maximally correlated. It imports the G6-C2 proper FULL/CORE original six-source-ID inverse and G6-C3 HEAVY/LOW single global owner/selector, real original 3st source projection loads, and exact unprojected original missing-endpoint term 4|P|Δ_L=O(r⁵). Together with the external ordinary graph C6 counting theorem, this yields only the previously established **CONDITIONAL** original T3 lower bound, for all sufficiently large even q and up to ρr⁴ adversarially removed ORIGINAL flags:

~~~
D6_original(I\Z;f,g)+BBo_produced_original(I\Z;f,g)
   ≥ δr⁶    (δ,ρ>0 fixed before source and labels).
~~~

Formal ledger values C0=c0=1 are **FORMAL ONLY placeholders**, NOT independently sourced numerical graph C6 constants. Neither unrestricted abstract T3, a new dependent GF5 ASET exponent, independent external referee nor Lean theorem is claimed.

The finite GF8 source is also passed to a genuine **physical threewalk search**, with three independent historical original BBo inverse reconstructions, and the negative control removing one ORIGINAL FULL projection anchor; positive literal BBo is saved as six actual source flag IDs and their coordinates. This is finite integration evidence, not the asymptotic δr⁶ estimate at q8.

## 5. Exact acceptance, limitations, next research

Implementation: research/gio_t3e3_even_corrigendum.py, 23 independent tests in research/test_gio_t3e3_even_corrigendum.py, specialized .github/workflows/gio003-g6e3-even-corrigendum-matching-k20.yml. The REAL GF8 source uses actual polynomial quotient arithmetic, original Γ8/PDS flags, original corrected Theorem6 closed neighborhoods, original 24 matching edges, independent true source geometry, point/line two-walk identities, typed original J/Gram and exact six-flag inverse. The odd-characteristic S formula is a negative control: its R collapses from 16 to 8 original lines in characteristic 2.

**STOP:** require exact final PR HEAD GitHub-hosted specialist unit tests + serialized source JSON, full Research and INDEX SUCCESS, internal critical mathematical review, Draft-only stacking. Do not merge ancestor PRs or close #793. Do not interpret q8 finite examples as a complete asymptotic lower bound.

**Next substantive work:** exploit original matching geometry for stronger odd/even κ, or find genuine connected infinite quadratic-excess original source families beyond the *optimized* G6-D2–D7 union rather than just another spectral sufficient condition. The corrected even/odd 2021 families themselves were already known to graph theorists.
