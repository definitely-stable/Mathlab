# GIO-001.3 / G6-D3 — affine-arc structural transfer: many real quadratic-excess sources with original six-ID obstruction

**Issue:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), meta [#790](https://github.com/definitely-stable/Mathlab/issues/790).

**Stack:** this manuscript is based on [G6-D2 #806](https://github.com/definitely-stable/Mathlab/pull/806) at exact original head `6605187776e0d5d15aa70c2df123a39d55ac85f6`, and inherits the explicitly bounded source-flag HEAVY/LOW from G6-C3/C2/C1. It introduces **a source-geometric sufficient condition** for the previously required centered spectral bound, not a new source GQ axiom. No synthetic new flags are inserted into missing original projections.

## 1. Prior art and precise novelty boundary

**Not new:** projective arcs, affine point–line graphs built from arcs, the fact that an arc construction is C4/C6-free, the generalized Wenger graph and character-sum/Cayley spectrum methods, classical finite fields, Wenger W₂(q), and their known relation to ambient generalized quadrangles. Sources:

- Cioabă, Lazebnik, Li, [*On the Spectrum of Wenger Graphs* (2014)](https://arxiv.org/abs/1402.3341), especially the monomial model `W'_2(q)`, the Cayley direction character method, and Theorem 2.1 for its spectrum.
- Mellinger, Mubayi and related finite-geometric constructions, summarized in [*A construction for infinite families of semisymmetric graphs revealing their full automorphism group*, Theorem 5.3](https://doi.org/10.1007/s10801-013-0475-4), and the [finite-arcs exposition](https://anuragbishnoi.wordpress.com/2018/04/28/wenger-graphs/). These already show arc-induced incidence graphs have girth eight.
- [Recent 2025 algebraic graph constructions survey](https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/3/7714/files/2025/05/withYeWang2025.pdf), §4.5.1, on generalized Wenger graphs and their additive-character spectra; also [*On the characterization of some algebraically defined bipartite graphs of girth eight*](https://www.sciencedirect.com/science/article/pii/S0166218X21003759).

**New *within Mathlab's program* (subject to independent external mathematical review):** an explicit all-order transfer from **every** affine q-point projective arc to the **historical original six-source-ID D6 + actually-produced aligned BBo obstruction** for **all** arbitrary complete MINIMAL injective factor labels f/g, even correlated and adversarial, with deletions of original named flags. The obstruction uses the actual original source, original missing endpoint geometry and G6-C2 FULL/CORE inverse; it does NOT use a GQ supertemplate even when a graph admits one. No claim that affine-arc graphs or their eigenvalues have just been discovered.

## 2. Source construction from an arbitrary projective q-arc (the structural input)

Let `q>=3` be **any prime power**, and let `h:F_q→F_q` be an arbitrary function with

```
  K_h = { [1:u:h(u)] : u in F_q }
```

a **projective q-arc**, meaning no THREE distinct `[1:u:h(u)]` are collinear. The coordinates u must range over all of Fq; this is an **affine-graph q-arc** rather than an unjustified claim that EVERY projective arc admits the chosen chart.

Define the **actual** original point and line sets separately as `P=L=F_q³`. Point `p=(u,v,w)` is incident with original line `ell=[a,b,c]` iff

```
  b+v = a*u,            c+w = a*h(u).             (ARC-I)
```

For every point, choose a arbitrarily and the two remaining line coordinates are uniquely determined, so it has exactly q original lines. Dually, for every line and every u, the point v,w is uniquely determined. Thus the original source is a **simple q-regular bipartite graph** on exactly `2q³` vertices with `q⁴` distinct ORIGINAL source flags, and `s=t=q-1=r`. No geometric or algebraic source completion is performed.

### Girth >=8 (self-contained original-source proof)

Two distinct original lines `ell,ell'` sharing a point `(u,v,w)` satisfy

```
  ell-ell' = (a-a')*(1,u,h(u)).
```

The coefficient `lambda=a-a'` is nonzero for distinct lines, because equal a would force their other coordinates to agree. For any two different lines, this equation has at most ONE solution u (read the first two coordinates), so the source has no C4.

Suppose an original simple C6 existed, with three distinct lines `ell0,ell1,ell2` and three distinct pairwise intermediate points. Their three nonzero difference vectors add to zero:

```
  lambda_1*(1,u1,h(u1))
 +lambda_2*(1,u2,h(u2))
 +lambda_3*(1,u3,h(u3)) = 0.
```

If u1,u2,u3 were all distinct, this is a nontrivial linear dependence among three projectively collinear arc vectors, contrary to the arc hypothesis. If EXACTLY two u values coincide, the remaining direction must lie in the span of that same direction, hence its first/second coordinates force it to coincide too. If all THREE coincide, every line lies on the same affine direction line, and the uniquely determined common original point is repeated; this is not a simple C6. Thus C6 is impossible. By q-regularity for q>=3, girth is exactly 8 (the original graph has fewer than the bipartite girth-10 Moore bound). Its connectedness is also forced by component size: each component would require at least `q((q-1)^2+1)` points while `q³<2q((q-1)^2+1)` for q>=3.

The original Moore excess is **exactly**

```
   Delta_L=Delta_P=q³-q((q-1)²+1)
                    =2q(q-1)=2r(r+1)>0,
```

so these ACTUAL sources are **NOT GQ**; they have genuinely quadratic excess, uniformly `Delta_L<=3r²`, without being a GQ supergraph / GQ source assumption. The original nonincident point-line projection table is partial: it has exactly `q³ Delta_L` missing entries and each actual original named flag occurs in exactly `3r²` genuine 3flag projections. These facts are rechecked by the original incidence-first source checker, not filled from an ambient Q(4,q).

## 3. Fourier/Cayley source spectra from the q-arc (NO spectral gap assumption)

Original line–line two-step adjacency `A_L=BᵀB-qI` is the Cayley graph of the **additive group `F_q³`** with connection set

```
   S={ lambda*(1,u,h(u)):
            lambda in F_q^*, u in F_q }.
```

These are `q(q-1)` distinct nonzero original differences; each pair of distinct original lines has at most one original common point, so there are no multiplicities. For a nontrivial additive character `psi:F_q→C^*`, every additive character of `F_q³` is indexed by `w=(w0,w1,w2)`. If

`z(w)=|{u∈F_q : w0+w1*u+w2*h(u)=0}|`,

the exact Fourier eigenvalue of `A_L` is

```
  lambda(w) = sum_(u∈Fq,lambda≠0)
     psi(lambda*(w0+w1*u+w2*h(u)))
            =q*z(w)-q
```

by the **exact additive character orthogonality identity**, not a floating eigensolver. Thus `U=BᵀB` has eigenvalue `q*z(w)`.

For w=0, z(w)=q and this is the unique principal eigenvalue q². For EVERY nonzero w, the equation cuts K_h with a projective line, hence the **q-arc** hypothesis forces `z(w)∈{0,1,2}`. The complete original point and line two-step eigenvalues on the centered subspace therefore belong to

```
       {0,q,2q}.                                     (ARC-SPEC)
```

These three values actually occur. Counting projective lines by their intersection size with q arc points, there are `binom(q,2)` secants (2 roots), `2q` 1-intersection lines, and the remainder 0-intersection lines. Each projective line equation corresponds to q−1 nonzero scalar forms. Therefore the exact centered multiplicities are

```
   m_(2q)=(q-1)*binom(q,2)=q(q-1)²/2,
   m_q=(q-1)*2q=2q(q-1),
   m_0=q³-1-m_q-m_(2q).
```

Every affine-graph q-arc source is accordingly **cospectral with the published Wenger W₂(q) at the point/line incidence two-step level**. This does NOT assert graph isomorphism between different arcs or the absence/presence of a GQ embedding; those questions are separate.

## 4. Intrinsic missing-projection norm and optimal fixed asymptotic constants

G6-D1 proved for ANY actual girth>=8 original source, without GQ axioms,

```
  T(T-2rI)^2
    = FFᵀ+(|L|-2Delta_L)J,  T=BBᵀ,
```

where F is the **rectangular original missing 3flag projection matrix**. On centered vectors, its nontrivial squared singular levels are precisely `x(x-2r)^2` for x the centered eigenvalues (ARC-SPEC). Thus the centered missing projection `F0=F-(Delta_L/|L|)J` obeys **exactly**
The corrected rank-one coefficient is `Delta_L` (the row sum of original missing-projection `F`), not `Delta_P` for unequal source orders. In the present q-arc family `s=t=q-1` and `Delta_L=Delta_P`, so the correction does not change any q-arc statement or Fourier eigenvalue. In the general source theorem the centered restriction remains valid; see [G6-D1 asymmetric correction](GIO-003-G6D1-RECTANGULAR-CUBIC-CORRECTION.md).


```
   ||F0||₂² = max{ q(q-2)², 8q }.
```

The positive levels actually occur because q-point arcs have secants and tangent lines. For q>=5, r=q−1>=4,

```
   r³-q(q-2)² = r²+r-1>0,
   r³-8q = r³-8(r+1) >= 0.
```

So ALL such source arcs, for ALL prime powers q>=5, satisfy **the same uniform structural G6-D2 theorem gate with FIXED**

```
          b=1,    C=3,    kappa=1.
```

The exact minimal integer kappa values are 3 for q=3, 2 for q=4 and 1 for q>=5 (these are only small-q exceptions, not family-dependent asymptotic parameters). The optional G6-D2 sixth-moment assumption `S6(F)<=M*r^9` is **not** added: the class is Wenger-cospectral and in fact its S6 is Θ(q¹¹), exceeding this overly strong sufficient test.

## 5. Consequent original historical six-ID obstruction for EVERY affine q-arc

**Theorem ARC-T3 (project-specific six-motif transfer, conditional on accepted G6-C3/G6-C2 combinatorics and the published ordinary graph C6 theorem):** Choose the projectively noncollinear q-arc K_h as above for ANY prime power q>=5; build the **ACTUAL** source `I_h` from (ARC-I), NOT a GQ. For each r=q−1 and **any** two complete MINIMAL separately globally pair-injective typed physical label maps `f:P→binom([aP],2)`, `g:L→binom([aL],2)`, independently of their relative correlation, and any adversarial ORIGINAL source flag deletion `Z⊆I_h` satisfying `|Z|<=rho*r⁴`, there exist constants rho,delta>0 and r0 fixed **universally over ALL q and ALL such arc functions h**, such that whenever r>=r0,

```
    D6_(I_h\Z)(f,g) + BBo_produced,(I_h\Z)(f,g)
                  >= delta*r⁶.
```

This is a direct application of the already calculated exact G6-D2 quadratic centered-spectral theorem ledger `integrated_quadratic_direct_ledger(b=1,C=3,kappa=1)`. Original six-ID D6 is inverse from genuine physical rainbow C6; produced aligned historical BBo counts only ACTUAL FULL surviving original projection anchors, with original CORE physical triples as in G6-C2. Nothing uses an enlarged ambient GQ to complete a missing projection. The HEAVY/LOW proof is uniform under arbitrary f/g and source-flag deletions.

**Existential external constants:** the all-order rho,delta,r0 depend on the externally established ordinary-graph C6 supersaturation theorem; program instances using `C0=1,c0=1` are explicitly **FORMAL_ONLY sample parameter ledgers**, not certified published constants or practically small thresholds. This is not an unrestricted all-quadratic-excess T3 or an ASET exponent theorem. The original #793 remains OPEN.

## 6. A concrete second infinite arc model: characteristic-two fourth powers

For `q=2^e` and `e>=3` ODD, take

```
               h(u)=u^4.
```

This is a well-defined projective q-arc function for the whole infinite series `e=3,5,7,9,...`. Indeed in characteristic two, fixing u and taking v≠u, the projective slope is

```
  (v^4-u^4)/(v-u) = (v+u)^3.
```

For fixed u, all these slopes are distinct precisely when the cube power map on `F_q^*` is injective. Since `F_q^*` is cyclic of order `2^e−1`, this occurs if and only if

```
             gcd(3,2^e-1)=1,
```

which holds if and only if **e is ODD**. Hence no three projective arc points are collinear for every odd e≥3. Each actual source `I_{u^4}` has q³ original points and lines, q⁴ original source flags, girth8, exact excess 2q(q−1), and the same centered spectral kappa=1 bound for q≥8. **This is a known finite-geometry monomial/translation-arc construction, not a new oval or a demonstrated nonisomorphic graph family.** It does establish a second explicit function construction under the uniform ARC-T3 theorem.

**Negative control:** for even e the cube map has a nontrivial kernel. `q=4` and `q=16` with h=u⁴ are NOT arcs: the q4 literal incidence graph contains a genuine forbidden original C6 and must be rejected by the original incidence-first validation. q16 is rejected by a separate exhaustive slope+determinant oracle without constructing a prohibitive dense `4096×4096` matrix. Never silently extrapolate h=u⁴ to all binary field degrees.

## 7. Independent finite tests, CI, and exact boundaries

Four new files in stacked Draft PR G6-D3:
- `research/gio_t3d3_affine_arc.py`: exact finite prime/GF(2^e) field arithmetic (literal q=4,8,16,32), line-first original source builder from any affine arc, **independent** projective determinant and slope collision oracles; original G6-C1 source_check frozen original named flags and genuine missing/projection census; complete exact additive-character root count for each of the q³ characters, roots at 0/1/2/q, projective secant/tangent multiplicities, centered missing F0 cubic certificate and fixed b,C,kappa all-order ledger. Separate exact all-e odd-power q=2^e h=u⁴ proof.
- `research/test_gio_t3d3_affine_arc.py`: independent line-first incidence oracle versus production point-first source; finite field multiplication/inverse/distributivity; true **q=3,5 Wenger-parabola** cases and **q=8 h=u² vs h=u⁴** distinct polynomials and identical spectral multiplicities, original source no C4/C6, 3st projection load, missing original endpoints. Explicit negative q=4/16 h=u⁴, **20** independent falsifiers. Original q8 binary arc source conflict and dual pencil Gram are also recomputed for lex and correlated minimal physical f/g without dense numerical eigensolvers.
- **Historical six-ID original source inverse on ACTUAL q=8 h=u⁴**, not inherited from the parabola: construct ALL original q⁴=4096 named flags and their true uncompleted 3flag projected-anchor table, then search **at most 3,000,000 actual proper physical threewalk candidates** for a valid true historical six-ID BBo motif (early stopping). Freeze precisely that **six-original-ID FULL survivor set** and its **three residual original physical CORE source IDs**, and run G6-C2's **three independently coded physical-first, historical published classifier and source-middle-owner-first BBo inverse algorithms on the bounded 6/3 set**. They must yield exactly ONE identical original sixset. Critically, deleting one of its three **genuine FULL original projection anchor IDs**, with the three CORE owners unchanged, must force ALL independent algorithms to return ZERO; no external GQ completion is permitted. This targeted finite falsifier is intentionally bounded instead of exhaustively enumerating every 4096-original-owner path; it is NOT the all-q asymptotic proof.
- `.github/workflows/gio003-g6d3-affine-arc.yml`: GitHub-hosted Python3.12 specialist, exact JSON artifact, 19 tests and consistency gates. Inherit original full Research and INDEX on the exact stacked HEAD.

**STOP:** The result is **not** the full unrestricted T3 for all abstract biregular sources or even all girth8 quadratic-excess sources. Arc/Fourier geometry is an **additional structural hypothesis** which implies the G6-D2 centered source norm; its existence and classical graph properties are prior art. Neither an ambient GQ nonembeddability proof nor a new graph-isomorphism classification is claimed. No external peer referee, Lean certification, fixed numeric ordinary C6 constants, dependent GF5 theorem or unqualified ASET exponent. Keep PR Draft and #793 OPEN until exact HEAD specialist + Research + INDEX all succeed, then only a narrowly scoped governed integration. Do not merge the ancestor Draft PR chain automatically.

**Next frontier (G6-D4):** can original source **incidence codegrees, localized fiber interactions, or a bounded number of exceptional F0 singular modes** replace the projective-arc assumption and imply the same historical six-ID obstruction for ALL quadratic-excess sources? Construct a *genuine* girth8 biregular near-Moore source violating the centered spectral gap if one exists; artificial regular 0/1 missing matrices are insufficient counterexamples.
