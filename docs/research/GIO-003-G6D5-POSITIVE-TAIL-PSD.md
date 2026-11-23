# GIO-001.3 / G6-D5 — weighted positive spectral tail and exact PSD certificates

**Research context:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), meta [#790](https://github.com/definitely-stable/Mathlab/issues/790). Frozen [G6-D4 #809](https://github.com/definitely-stable/Mathlab/pull/809) HEAD `2fc2761fd5cb25db16150b08f60922e937fb05ff`, including corrected G6-D1-FIX and G6-C1/C2/C3 parent stack. **Scope:** source-level *conditional* new A1/Gram certificate for actual original source flags, not an unrestricted abstract T3 theorem, not new ASET extraction, not an externally referee-approved theorem. Do not merge the stacked drafts or change main automatically.

## 1. Bottleneck left by G6-D4

The earlier G6-D4 all-order result imposes at most `m<=nu*r^(7/6)` centered positive original-source collinearity eigenvalues ABOVE `ell*r`, certified exactly by `m^6<=nu^6*r^7`. It protects the total exceptional contribution by multiplying *number* of outliers by an independent worst-case cubic estimate `lambda<=O(r^(4/3))`. This is wasteful if a large fraction of eigenvalues sit only slightly above the cutoff.

**New source-intrinsic gate:** fix integers `b>=1, C>=0, ell>=0, nu>=0` before choosing any source or label maps. Let an ACTUAL simple thick (s,t)-biregular girth-at-least-eight original incidence `I⊆P×L` obey `r=min(s,t)`, `max(s,t)<=b*r`, `Delta_L=|L|-(t+1)(st+1)<=C*r²`. For the two ORIGINAL collinearity adjacency matrices `A_P`, `A_L`, separately define

```
  tau_ell(A) := sum_{lambda in Spec(A restricted to 1^perp)}
                       max(lambda-ell*r,0).

  tau_ell(A_P) <= nu*r^(5/2),
  tau_ell(A_L) <= nu*r^(5/2).              (D5-TAIL)
```

The sum includes algebraic multiplicity and omits **exactly one** all-ones principal mode. A disconnected original source can have additional principal-sized eigenvalues in `1^perp`, which are INCLUDED and charged. The gate controls the *weighted total excess* above the cutoff, **not the number of positive outliers**, **not the sum of their unshifted eigenvalues**, and **not** `||F0||²`.

## 2. Exact source factor-trace proof, all fixed admissible f/g

Let `H[p,x]=1` exactly when one of the two symbols of f(p) is x. Because f is complete, unordered-pair injective and uses the minimal typed alphabet a, every row has sum 2 and every symbol fiber has size `d_x<=a-1`. Consequently

```
 ||H||²_2<=||H||_1*||H||_infty<=2(a-1),
 ||H||²_F=2V,
 sum_x d_x²<=2V(a-1).
```

If A is the ORIGINAL source point collinearity adjacency, each source-collinear pair shares at most one label symbol, hence

```
  2 e_col(f) = Tr(H^T A H).
```

Let `P=I-J/V` be the orthogonal projector to `1^perp`; A is regular of valency k. We have the exact matrix Loewner inequality on the full vertex space

```
  A <= (k/V)J + ell*r*P + D_+,
  D=P(A-ell*r I)P,  D_+=max(D,0).
```

Because the trivial mode is orthogonal, D_+ is PSD, centered and has trace `tau_ell(A)`. Taking the H-trace and using `Tr(H^T D_+ H)<=||H||²_2 Tr D_+` gives

```
 e_col(f) <= k(a-1) + ell*r*V + (a-1)*tau_ell(A).        (D5-C)
```

This is valid for **every** adversarial fixed f on this original source, with no eigenvector-delocalization and no assumed source spectrum shape beyond the weighted tail gate. Repeating independently on the original line dual gives the same bound for every g (including arbitrarily correlated f/g). The source size/degree minimal-alphabet envelopes `V<=v0*r³`, `k<=k0*r²`, `a-1<=a0*r^(3/2)` yield

```
  e_col(f), e_col(g)
       <= [k0*a0+ell*v0+nu*a0] * r⁴
       = j0*r⁴;
  J_original(f,g) <= 2 j0*r⁴.
```

Use the accepted **G6-C1 ORIGINAL** exact pencil Gram identity with **nonnegative source symbol indicators** and the favorable negative entrywise defect correction `-sum u_x^T D_source u_x <=0` (D_source NOT PSD for arbitrary signed vectors). This gives `Gram_P²,Gram_L²<=G0²r^11`, where

```
 v0=(b+1)(b²+1+C), n0=(b+1)v0, a0=2v0+3,
 k0=b(b+1), theta0=b+2,
 j0=k0*a0+ell*v0+nu*a0, J0=2j0,
 G0=2v0*k0+2theta0*j0+2(b+1)v0*a0.
```

Nothing here proves the original HEAVY/LOW or original source book inverses anew. The all-order ledger **imports** accepted G6-C2/C3 proper FULL/CORE inverse and same global owner/bit selector, while retaining original 3st projection loads and `4V_P Delta_L<=4v0 C r^5` at the correct **critical O(r⁵)** scale. Given those prerequisites and the external ordinary-graph C6 theorem, the same conditional T3 conclusion is available:

```
 D6_original(I\Z;f,g) + BBo_original_produced(I\Z;f,g)
   >= delta*r^6    for all |Z|<=rho*r^4 and sufficiently large r.
```

The constants `rho,delta>0` and threshold `r0` depend only on the fixed source gate plus existential ordinary C6 constants. The exact ledger chooses them last and uses **FORMAL_ONLY** numeric graph constants `C0=c0=1` as illustrative placeholders, not a claim about optimal published numerical values.

## 3. All-rational PSD spectral-tail witness (no numerical eigensolver)

For any ACTUAL regular source adjacency A, define `D=P(A-ell*r I)P`. The exact source eigenvalue positive excess `tau=Tr D_+` has a standard convex PSD upper certificate: exhibit **ANY real/rational symmetric matrix W** such that

```
       W >= 0 (PSD),
       W-D >= 0 (PSD),
       (Tr W)^2 <= nu²*r⁵,   Tr W>=0.            (D5-PSD)
```

Indeed, the orthogonal spectral projector E_+ onto positive eigenvectors of D satisfies `Tr W >= Tr(E_+ W) >= Tr(E_+ D)=Tr D_+=tau`. Thus `tau²<=nu²*r⁵`, equivalently to (D5-TAIL) since all quantities are nonnegative. This is a **sufficient computational witness**, not a claim that every source passing D5-TAIL has an easily found small rational W. The exact implementation performs rational Sylvester congruence to check both PSD requirements and the squared trace inequality with no approximate eigensolvers or rounded fractional powers.

The method generalizes beyond G6-D4: by the corrected G6-D1 cubic a D4 source with `m<=nu_D4*r^(7/6)` has positive eigenvalues `<=B0*r^(4/3)` (fixed B0), hence `tau<=B0 nu_D4*r^(5/2)`. Thus every G6-D4 source obeys D5 with `nu_D5=B0 nu_D4` and the same b,C,ell, though not necessarily the *same numerical nu*. This is an implication of source conditions; it does NOT create a new independently realized infinite graph family.

## 4. Exact strict separation on ACTUAL connected non-GQ original source: Wenger W₂(5)

The published classical Wenger two-step spectrum (Cioabă–Lazebnik–Li, 2014) has for q>=3 the ORIGINAL point/line collinearity A eigenvalues `k=q(q−1)` (one principal), `−q,0,+q` (centered), with multiplicity of `+q` equal to `m2=q(q−1)²/2`. For q=5:

```
  |P|=|L|=125; |I_original|=625; r=4,
  Delta_P=Delta_L=2q(q−1)=40 <=3r²=48,
  cutoff ell*r=4,  ell=1, nu=2.
  +q=5 has multiplicity m2=40.
```

The **G6-D4 rank gate** at the same ell=1,nu=2 fails: `40^6>2^6*4^7`. By contrast the exact **G6-D5 weighted tail** is

```
  tau_ell(A)=m2*(q−4)=40,
  tau²=1600 <=nu²*r⁵=4*1024=4096.
```

This is a **literal connected real quadratic-excess, non-GQ source** with original incidence geometry, not a synthetic missing mask. The line-dual source passes exactly the same check. It strictly separates the two sufficient source gates **at this finite source and identical b=1,C=3,ell=1,nu=2**. It does **not** imply an actual G6-D5-only **infinite** source family: for the whole Wenger series at ell=1, `tau~r³/2`, which exceeds a fixed `nu r^(5/2)` asymptotically; ell=2 yields tail zero and also satisfies the previous D2 gate.

The finite W₂(3) (r=2) provides a second exact connected non-GQ separation: its tail equals 6 on both types while the positive outlier multiplicity also equals 6 and fails the corresponding fixed rank gate.

**Symbolic no-go for this very same fixed infinite Wenger parameter gate.** For every published prime-power q>=3, put r=q−1 and ell=1,nu=2. The positive-outlier multiplicity is `m2=q r²/2`; each contributes exactly `q−r=1` beyond the cutoff, so `tau=q r²/2`. Therefore the weighted tail inequality becomes **precisely**

```
   tau² <= 4 r^5    <=>    (r+1)² <= 16r.
```

It fails for **every integer r>=14**, since `r²−14r+1>0` already at r=14 and increases thereafter. In particular published prime-field `q=13` passes the fixed gate arithmetically (`tau=936`), whereas the actual available prime-power `q=17` fails (`tau=2176` exceeds `2*16^(5/2)=2048`). The symbolic regression checks prime q=3,5,7,11,13,17,19 via **published spectra**, without pretending to build original `q³`-vertex incidence graphs at large q. This is a formal **non-extension** result for the fixed `ell=1,nu=2` Wenger route, not a universal no-go for D5 on other sources or different cutoff parameters.

### Exact polynomial projector as PSD witness

For these **actual source Wenger instances** (not arbitrary sources), let `n=q³`, `k=q(q−1)` and A be its literal original point or line adjacency. The centered projector onto its `+q` eigenspace is **exactly**

```
  Q_plus = [A(A+qI)]/(2q²) - k(k+q)/(2q² n) * J.
```

This polynomial is zero at centered eigenvalues `-q` and 0, one at `+q`, and zero at the principal mode k. Set `W=max(q−ell*r,0)*Q_plus`. The new implementation constructs W only using **literal original adjacency and common-neighbor integer counts**, checks rational row sums, symmetric form, exact trace `m2 max(q−ell*r,0)`, **both full PSD inequalities by independent rational inertia** and signed original labels. Its exact source-first tests additionally verify `A W=qW` by an independently computed adjacency-vector multiply, preventing a mere symbolic assertion or fabricated projection.

For genuine **disconnected doubled GQ** sources, a centered block-sign vector carries one extra eigenvalue k; a separate rank-one rational W certificates it. These sources are accepted only as **finite controls** (their general variable-order Moore excess grows like r³, so they cannot establish a quadratic-excess infinite family).

## 5. Research significance, prior art and next frontier

The spectral positive-part trace/Ky Fan/SDP dual inequality is **standard matrix analysis**, not claimed as a newly discovered mathematical theorem. Wenger graph spectra are also prior art: [Cioabă, Lazebnik, Li, *On the Spectrum of Wenger Graphs* (2014)](https://arxiv.org/abs/1402.3341), JCTB. The genuinely **project-specific** contribution is the new source transfer certificate that uses a weighted spectral tail instead of G6-D2's worst centered-F norm or G6-D4's count of exceptional modes, for the historical ORIGINAL six-source-flag obstruction with arbitrary correlated minimal factor maps, subject to previously accepted G6-C2/C3 inverses.

The **next research step** is source realizability: construct a true infinite near-Moore quadratic-excess girth-eight family with `tau_ell<=nu*r^(5/2)` for fixed ell,nu but violating every fixed D4 exceptional multiplicity gate; or prove structural constraints on actual source spectra that rule this out. A synthetic regular 0/1 F or a single finite Wenger instance does not establish a new all-order separation. Also compare weighted-tail versus incidence fiber-*adapted* spectral projector energies, where even total spectral tail could be large yet each admissible factor H has bounded coupling; that would require genuinely new source+factor analysis.

**CI acceptance:** exact HEAD specialist tests/certificate, entire Research, INDEX, mathematical critical review of the PSD projection and all-original FULL/CORE inheritance. Keep #793 OPEN, this and parent PRs Draft, no auto-merge, no external human peer review or Lean claim.
