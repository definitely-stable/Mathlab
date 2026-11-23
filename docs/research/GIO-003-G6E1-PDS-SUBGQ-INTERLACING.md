# GIO-003 / G6-E1 — actual smaller near-Moore sources via perfect domination and GQ interlacing

**Issue:** [#793](https://github.com/definitely-stable/Mathlab/issues/793); stacked on [G6-D7 #812](https://github.com/definitely-stable/Mathlab/pull/812), frozen source HEAD `4d7cd8f80a407da85e8e9c2ff6aa5edfc57ec261`. All parent G6-D7 specialized (20/20), full Research and INDEX CI were SUCCESS on that HEAD. Research-only **Draft**: no automatic merge or change to main.

**Prior art explicitly credited:** M. Abreu, G. Araujo-Pardo, C. Balbuena, D. Labbate, [*An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8* (2011), arXiv:1111.3279](https://arxiv.org/abs/1111.3279), Definitions 1.1 and Theorems 1.1, 1.2(ii), 1.3. The graph family and the dominating-set deletion are **NOT newly discovered by Mathlab**. Standard singular-value submatrix compression/interlacing is likewise classical.

**What Mathlab adds:** a literally built, independently audited **smaller and genuinely different** source-realizable quadratic-Moore-excess family, together with a uniform original-source **G6-D2 DIRECT centered missing-projection spectral bound derived from parent GQ interlacing**, with no independent operator hypothesis. This is a new *project-specific* source transfer/certificate to the inherited six-original-ID obstruction scheme, NOT a new unrestricted GIO T3 or dependent GF(5) ASET exponent.

## 1. Why the earlier H_q proposal would duplicate existing Mathlab work

Definition 2.1 in Abreu et al. gives a q-regular H_q incidence:
```
  (a,b,c)_line ~ (x, ax+b, a²x+c)_point.
```

Although H_q is not isomorphic to D(3,q) for q>=3 (published statement), an **exact dual relabeling** identifies it with the parabola `h(u)=u²` special case of the EXISTING G6-D3 affine-arc source:
```
 H_q point (x,y,z)  ->  G6-D3 original line (-x,-y,-z);
 H_q line  (a,b,c)  ->  G6-D3 original point (a,b,c).

 On the G6-D3 line (-x,-y,-z), the u=a original point is
 (a, -x*a +y, -x*a²+z)=(a,b,c).
```

The exact finite-field identity holds in every characteristic, including 2, and is separately regression-tested. Thus merely importing H_q would artificially double-count the existing G6-D3 source theorem. **G6-E1 deliberately instead uses the smaller `q(q²−2)`-per-side PDS-deletion construction** of Abreu et al., Theorems 1.2(ii), 1.3, which has cardinality different from q³ for every q>=3.

## 2. LITERAL published parent generalized quadrangle Γ_q

Fix any prime power q>=3 and finite field F_q. The published original parent Γ_q has on EACH partite side coordinate names
```
 V = {(a,b,c):a,b,c∈F_q}
     ∪ {(q,b,c):b,c∈F_q}
     ∪ {(q,q,d):d∈F_q∪{q}},
 |V| = q³+q²+q+1 = (q+1)(q²+1),
```
where symbol `q` is a **formal infinity marker**, not a field element. Original line-to-point adjacency:

```
  line (a,b,c), a∈F_q:
       points (x, ax+b, a²x+2ab+c) for x∈F_q,
       plus point (q,a,c);

  line (q,b,c), b,c∈F_q:
       points (c,b,x) for x∈F_q,
       plus point (q,q,c);

  line (q,q,d), d∈F_q∪{q}:
       points (q,d,x) for x∈F_q,
       plus point (q,q,q).
```

All arithmetic on true field coordinates uses F_q operations. **Critical characteristic-two gate:** `2ab` is the FIELD SUM `(ab)+(ab)=0` in GF(2^e), not `field.mul(numerical_code_2,ab)`, which would generate a different and invalid parent in GF(4), GF(8). The exact source-first verifier requires the (q+1)-regular parent to have **no missing projection pairs** and independently checks point and line generalized-quadrangle two-walk defect identities. Thus no incorrect parent can pass by only matching a vertex count.

## 3. EXACT published perfect dominating set B (Theorem 1.2(ii))

For original Γ_q adjacency write N[u] for the **closed** one-neighborhood and N²[u] for the **closed** two-neighborhood. Fix **nonzero** ξ∈F_q. Let `u_c=(q,0,c)_line`, `v=(q,q,0)_line`, `w=(q,q,ξ)_line`. Delete exactly the original vertices

```
 B = (union_{c∈F_q} N[u_c])
     ∪ N[v]
     ∪ ((union_{c∈F_q} N²[u_c]) ∩ N²[v])
     ∪ N²[w].
```

The published theorem gives **perfect domination**:
```
 |B| = 2(q²+3q+1),
 |B∩Points|=|B∩Lines|=q²+3q+1,
 each original vertex not in B has EXACTLY ONE original neighbor in B.
```

The new code constructs and independently counts every literal Γ_q adjacency, every closed original one/two-ball, both side cardinalities, and every outside-vertex neighbor in B. It then takes the **induced original source subgraph** `Γ_q[V\\B]`; because the parent degree is q+1, every remaining vertex has exactly q original flags. Girth≥8 persists under taking an induced subgraph, and Mathlab's geometry-free `source_graph` is called AGAIN on the reduced original flags, independently catching all accidental 4-/6-cycles, broken degree counts, projection foot multiplicities and source original threeflag loads.

For the reduced source, put **r=q−1**, hence new (s,t)=(r,r). Exact:
```
  V_P=V_L=(q+1)(q²+1)-(q²+3q+1)
          = q(q²−2) = q³−2q,

  |I_original| = q²(q²−2),

  Moore_P=Moore_L=(r+1)(r²+1)
                   =q(q²−2q+2),

  Delta_P=Delta_L=2q(q−2)
                 =2((q−1)²−1) < 2r².
```

Thus the source is **genuine non-GQ** with a **uniform C=2 quadratic-excess envelope**, strictly better than the Wenger q³ family with `Delta=2q(q−1)<=3r²` and strictly fewer point/line source vertices. It also has **exactly 3r² original nonincident threeflag-projection loads per original flag**, and every missing source point-to-line projection is an actual missing pair, not an invented completed incidence.

Selected finite dimensions (all independent original-source assertions, not an infinite proof by extrapolation):

| q | parent vertices/side | removed B/side | original remaining vertices/side | original flags | Delta/side |
|---:|---:|---:|---:|---:|---:|
| 3 | 40 | 19 | 21 | 63 | 6 |
| 4 = 2² | 85 | 29 | 56 | 224 | 16 |
| 5 | 156 | 41 | 115 | 575 | 30 |

## 4. NEW uniform parent-submatrix spectral interlacing theorem

The following source theorem holds for **ANY** q-regular BALANCED **induced** original point-line sub-incidence of a true generalized quadrangle GQ(q,q), not just this particular published perfect dominating set, provided q>=3.

Let B_Γ be the parent's point-by-line 0/1 incidence matrix (square) with row/column degree q+1. The parent's original point collinearity adjacency has GQ strongly-regular parameters
```
 k=q(q+1), lambda=q−1, mu=q+1,
 A²=(k-mu)I + (lambda-mu)A +mu*J.
```
On the one-orthogonal subspace its two collinearity eigenvalues solve
```
 eta²+2eta−(q²−1)=0
    => eta=q−1 or eta=−(q+1).
```
Hence parent B_Γ B_Γᵀ has singular-squared levels
```
  (q+1)²           once (principal),
  2q               (nonprincipal),
  0                (nonprincipal).
```

Take ANY square q-regular original induced submatrix `B'` by retaining equal-sized subsets of genuine parent points and lines, and **no other invented flags**. The standard singular-value compression inequality yields for each index j
```
 sigma_j(B') <= sigma_j(B_Γ).
```
Because B' is q-regular, `sigma_1(B')=q`. For q>2,
```
 sigma_2(B')² <=2q<q².
```
If the reduced source were disconnected, the q-regular bipartite components would produce *at least two* singular values equal to q, a contradiction. Therefore the source is **automatically connected**. Moreover on **both original types** the nonprincipal squared singular-value spectrum `x` of `B'B'ᵀ` or `B'ᵀB'` lies in the exact interval `0<=x<=2q`.

Now use the **corrected G6-D1** actual source cubic missing-projection identity, with reduced (s,t)=(r,r), `h=s+t=2r`:
```
  T(T-2rI)²=F Fᵀ+(|L|-2Delta_L)J,
  T=B'B'ᵀ,
  centered F0F0ᵀ = T(T-2rI)² on 1_perp.
```

The cubic function `p(x)=x(x-2r)²` on `0<=x<=2q` has nonnegative values and exact maximum
```
  max_{0<=x<=2q} p(x)
    =max{ 4(2r)³/27, 8q }
    =max{ 32r³/27, 8q }.
```

For ALL q>=4, `8q<=2r³`, and `32r³/27<2r³`, giving

```
  ||F0||²_2 <=2r³   on BOTH original point and line types,
  q>=4, without any independent F0 operator or sixth-moment assumption.
```

At q=3 the same proof yields `||F0||²<=3r³`, and the finite certificate uses κ=3, not a false κ=2 claim. **These estimates are UNIFORM in q**, as the parent GQ existence and PDS formula are already published for every prime power; integer/field-realization tests at q=3,4,5 are finite source falsifiers, not the basis of the all-order bound.

The proof uses the standard singular-value compression bound and parent GQ spectrum, NOT a new worldwide spectral graph theorem. Its application to the historical G6-D1 missing operator and G6-D2 source transfer is new *within this Mathlab research program*.

## 5. Conditional source transfer to original six-ID T3

For every prime power q>=4, this concrete genuine original source satisfies the FIXED G6-D2 source assumptions:
```
 b=1,   C=2,   kappa=2,
 r=q−1,   Delta_L=2(r²−1)<2r²,
 ||F0||²<=2r³ on point AND line original types.
```

Therefore import exactly the PREVIOUSLY ACCEPTED
`integrated_quadratic_direct_ledger(b=1,C=2,kappa=2)`: the same original source conflict bound `J(f,g)=O(r⁴)`, source pencil Gram²<=G0²*r^11, G6-C2 proper original six-source-ID FULL/CORE BBo inverse, G6-C3 HEAVY/LOW with a **single global original owner/bit selector**, original 3st source projection loads and the true `4V_P Delta_L=O(r⁵)` original missing-endpoint term. Given the existing external ordinary graph C6 counting theorem and its existential constants, fixed positive `rho,delta,r0` follow **conditionally** so that for every arbitrary complete minimal pair-injective f/g (even adversarially correlated) and all original flag deletions |Z|<=rho*r⁴,

```
  D6_original(I\\Z;f,g)+BBo_produced_original(I\\Z;f,g)
       >=delta*r⁶  for prime-power q>=4 with q−1>=r0.
```

**Logical limitation:** the full G6-C2/C3 and external C6 proofs are **imported**, NOT re-proven here. `C0=c0=1` inside a small formal numerical ledger are **FORMAL_ONLY**, not certified published C6 numerical constants. An explicit finite q=5 graph generally has r far below the astronomically conservative sufficient r0: a finite PSD pass must NOT be misrepresented as applying the asymptotic lower-bound theorem at q=5.

## 6. Exact engineering certificate and independent falsifiers

Implementation: `research/gio_t3e1_subgq_pds.py`, tested by `research/test_gio_t3e1_subgq_pds.py`.

Verification is TRUE original-source first:

- Independent explicit Γ_q coordinate/field equation and original GQ source with zero missing projections, both point and line two-walk identities.
- Published closed-neighborhood B exact membership, each remaining vertex exactly one deleted neighbor, B side-balance, retained q-degree, exact original-induced flags, reduced girth≥8 and original 3st owner load.
- Independent two-sided source f/g arbitrary minimal labels, ORIGINAL source J conflicts and source Gram exact identity.
- Exact rational Sylvester proof that the finite original F0 centered Gram is ≤κr³ I on BOTH typed sides, and separately that reduced centered B'B'ᵀ and B'ᵀB' ≤2qI on 1_perp, using original source incidence only. No approximate eigensolvers.
- Field-characteristic-2 falsifier for the common incorrect `2ab` interpretation, and false PDS/false GQ-shortcycle construction rejects.
- Explicit negative novelty check: published H_q is exactly a DUAL of the existing G6-D3 parabola arc source; it is NOT counted as a separate new family. Smaller reduced cardinality q³−2q differs from all q³ affine-arc/Wenger sources.
- Prime-power symbolic all-order q=3,4,5,7,8,9,11,13,16,17,19,32,64,101 with **exact inequalities**; only implementation-supported literal F_q (prime and selected binary powers) is instantiated for finite graphs.

### 6.1 Nontrivial genuine original FULL/CORE six-ID BBo, not merely spectra

Beyond mathematical feasibility, the new source now runs through the **existing, fully original named-flag G6-C2 inverse**, with a deterministic adversarial mixed FULL/CORE subset. Three separately implemented algorithms (manual physical 3-walk, published physical BBo classifier and source-first owner-join) return exactly the **same six-original-flag sets**:

| TRUE original PDS source | Factor labels | Original flags | Mixed FULL/CORE produced original six-ID BBo motifs |
|---|---|---:|---:|
| q=3, 21 original points + 21 lines | Lexicographic minimal | 63 | **4** |
| q=4 (GF(4)), 56 original points + 56 lines | Correlated minimal fixed | 224 | **258** |

The certificate stores a concrete tuple of **six distinct ORIGINAL flag IDs and six original point-line owner names** for each case, the independently verified point and line FULL/CORE book counts, and explicit `nontrivial=TRUE` gates. The counting is over actual FULL projection anchors and CORE physical owners; it never supplies a projection where the reduced source has a missing threeflag path. The paper's original perfect dominating deletion is reconstructed independently of the inverse algorithm.

These are strict FINITE nontrivial witness and source-program integration checks. The all-order `D6+BBo>=delta*r^6` conclusion still requires the imported G6-C2/C3 HEAVY/LOW analytic machinery, published graph C6 theorem and r>=r0. The values **4** and **258** are not estimates of delta or of the asymptotic leading coefficient.

## 7. Publication/priority and next mathematical step

World prior art includes the **2011 Abreu et al. original graph construction**, earlier generalized-quadrangle PDS/geometric configurations and classical matrix interlacing. Do not call those constructions or interlacing themselves a new theorem of worldwide graph theory. An independent thorough novelty/prior-art referee would still be needed before claiming the specific transfer result as publishable.

The program-level gain is substantive: we now have a smaller **actually source-realizable** infinite near-Moore family, with tighter original excess coefficient C=2, separate field characteristic 2 examples and **automatically certified** fixed centered operator κ=2. This moves the research from an uninterrupted sequence of additional spectral assumptions to *verifying a genuinely different, already existing family of source configurations.*

The next genuinely OPEN frontier is a real connected infinite quadratic-excess original source **outside the optimized G6-D2–D7 union**, or a proof that certain near-Moore source constructions automatically satisfy a weak G6-D7 local spectral certificate. An arbitrary synthetic regular missing F or one finite source cannot establish this.

**STOP:** the new PR must be Draft and target the frozen #812 branch; exact-head specialist, INDEX, full Research and independent scoped mathematical review required; no auto-merge, no issue #793 closure, no unrestricted T3 or new GF5 exponent claim.
