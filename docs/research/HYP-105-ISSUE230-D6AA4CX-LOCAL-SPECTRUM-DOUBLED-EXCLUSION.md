# HYP-105 #230 — AA4-CX: original local spectral cap upgrades ALL-CUT raw spoke leakage to Ω(s^5); exact doubled-exclusion loss

**SCIENTIFIC DRAFT.** Strict mathematical child [AA4-CW #623](https://github.com/definitely-stable/Mathlab/pull/623), frozen parent `af573b78ec211ddea3e9084f9795859bad126e97`; upstream original physical C4→true-original matching identity [AA4-CR #618](https://github.com/definitely-stable/Mathlab/pull/618), physical C4 dense reservoirs [AA4-CT #620](https://github.com/definitely-stable/Mathlab/pull/620), zero-local C4/3matching construction [AA4-CV #622](https://github.com/definitely-stable/Mathlab/pull/622). No modification to main or original accepted GF(5) seven-class registry.

## 1. The decisive OPEN gap, and selected scoped mathematical advance

Parent AA4-CW showed every arbitrary fully complete global original point-factor f and line-factor g (with any correlations) has Ω(s^(9/2)) TRUE genuine nonincident point–line source P3 anchors with a positive ORIGINAL incidence across their **raw** physical source-spoke neighborhoods in EVERY two halfcoordinate cuts. This is not an actual `B/B-overlap` GF(5)-accepted original sixflag, as doubled-factor exclusions and the actual source 3×3 perfect matching remain open.

Its count used the crude per-anchor bound `C_XY(p,l)<=2(k-2)(s+1)=O(s^(5/2))`. But the TRUE original GQ bipartite incidence matrix has nontrivial singular value sqrt(2s), and the same expander-mixing inequality applies ALSO to each individual source spoke-neighborhood pair, reducing the maximum to **O(s²)** for *every* original endpoint pair.

We give (A) an improved **all-h universally quantified Ω(s^5) RAW original-spoke-positive source 3path theorem** and (B) an exact **one-global-map doubled-factor deletion certificate** with quantitative upper bounds and explicit proof-method limitations. We DO NOT assert an unconditional positive SAFE-spoke, original 3×3 perfect matching, sevenGF5 positive motif, root A/B/C or ASET exponent.

## 2. Exactly quantified all-h theorem AA4-CX.1

Let every h>=24, s=2^h, V=(s+1)(s²+1), d=s+1. Let a be the MINIMAL physical coordinate count with binom(a,2)>=V; both maps f,g are fully globally injected ORIGINAL typed factor images into the same unordered K_a pair alphabet, correlated arbitrarily, with H=binom(a,2)-V<=a-2 holes per side. Let X,Y be ANY cuts of k=floor(a/2) physical symbols and define ORIGINAL source factor cut sets P_X,L_Y and raw ORIGINAL spoke source neighborhoods

```text
A_p={i∈P_X\{p}: f(i)∩f(p)≠∅},
B_l={j∈L_Y\{l}: g(j)∩g(l)≠∅}.
C(p,l)= #{(i,j) actual immutable ORIGINAL W(3,s) incidence IDs:
             i∈A_p, j∈B_l}.
```

Every ORIGINAL nonincident p,l has exactly one true ORIGINAL three-incidence-ID path p--l0--q--l. A_p,B_l are **raw** physical spokes only, without double-factor or physical C4-center exclusions.

**Theorem AA4-CX.1 (uniform all h>=24, all original full global correlated f,g, all halfcuts X,Y):**

```text
For EVERY original endpoint pair p∈P_X,l∈L_Y:
  0<=C(p,l) < 4s².                                               (CX.1)

#{(p,l)∈P_X×L_Y, p NOT original incident l, C(p,l)>0}
   >= V*d * ( k²/(2048 s²) - 1 )
   >= s⁵ / 16384.                                                (CX.2)
```

Here (CX.2) is **NOT** counting physical valid doubled-disjoint paths or GF5-positive motifs; it counts true original NONINCIDENT source path anchors with a positive genuine original source flag in their raw spoke×spoke product. Its improvement over AA4-CW is a genuine factor Ω(s^(1/2)).

### Proof (i): original source GQ singular-value bound at EACH anchor

For true original W(3,s), the original incidence M (V×V POINT vs LINE factors) has largest singular value d=s+1 and second singular value sqrt(2s). Thus for ANY ORIGINAL source factor subsets A,B

```text
E_M(A,B) <= d|A||B|/V + sqrt(2s)*sqrt(|A||B|).
```

The physical source pair alphabet is a simple graph on k cut symbols. Each real image f(p) is one physical edge and can share an endpoint with at most 2(k−2) OTHER in-cut physical edges, regardless of hole configuration. Therefore `|A_p|,|B_l|<=2(k−2)`, and

```text
C(p,l) <= 4d(k−2)²/V + 2(k−2)sqrt(2s).                           (CX.3)
```

The standard minimal K_a relation already proved in AA4-CS gives `a−2<1.5*s^(3/2)` for every dyadic s>=16. With k=floor(a/2), this implies k−2<.75*s^(3/2). Consequently for s>=16

```text
4d(k−2)²/V < (9/4)(s+1) <= s²,
2(k−2)sqrt(2s) < (3sqrt(2)/2)s² < 3s².
```

So `C(p,l)<4s²` for EVERY original pair regardless of f/g correlation, genuine original geometry only. This is a direct classical expander-mixing estimate; NOT a newly discovered general spectral result.

### Proof (ii): same global, exactly COUNTED original raw spoke mass

AA4-CW proved from physical holes, heavy-coordinate charging and true original source GQ spectral mixing that, for EVERY global f,g and cuts X,Y,

```text
T=Σ_(p∈P_X,l∈L_Y) C(p,l)
  =Σ_((i,j) TRUE ORIGINAL incidence, i∈P_X,j∈L_Y)
     |A_i| |B_j|
  >= k²*d*V/512                                                    (CX.4)
```

with **no independent random embeddings**. By CX.1, at least `T/(4s²) >= k²*dV/(2048s²)` cut endpoint pairs have positive C. There are at most Vd originally INCIDENT p,l pairs (in the entire genuine W3). Discard all, obtaining the first line in CX.2.

### Proof (iii): explicit all-h `s^5/16384` numerical constant (not an extrapolation)

Minimality of a yields `a(a−1)>=2V>2s³`, and for all dyadic s>=2^24, `k²>=s³/4`. Also Vd>=s⁴ and s>=16384. Thus

```text
k²*dV/(2048s²) - Vd
 = dV*(k²/(2048s²)−1)
 >= s⁴*(s/8192−1)
 >= s⁵/16384.
```

The last step is exact at s=16384 and stronger thereafter. The all-h lower bound is proven analytically, and h=1..30 integer checks are only independent *falsifiers*.

## 3. Actual TRUE original threepath doubled-factor filter

For each true ORIGINAL nonincident (p,l) choose its unique REAL source 3flag path p--l0--q--l. Call the anchor **DOUBLE-DISJOINT** exactly when `f(p)∩f(q)=∅` and `g(l)∩g(l0)=∅`. AA4-CR requires both conditions to contribute an accepted historical original B/B-overlap GF(5) sixflag.

For a DOUBLE-DISJOINT anchor, define **SAFE SPOKES** by removing from A_p every genuine original source point factor i whose f(i) intersects doubled original source image f(q), and from B_l every source line factor j whose g(j) intersects doubled image g(l0). Let C_safe(p,l) count actual original source incidence IDs between these filtered two source factor sets. Every true source factor image is an ORIGINAL global image, unchanged across all anchors.

**Lemma AA4-CX.2 (ALL h>=1, EVERY genuine nonincident DOUBLE-DISJOINT source anchor, EVERY complete typed f,g and cuts):**

```text
|A_p\A_safe| <= 4,    |B_l\B_safe| <= 4;
0<= C_safe(p,l) <= C(p,l);
0<= C(p,l)-C_safe(p,l) <= 8d,    d=s+1.                           (CX.5)
```

Proof: f(p)={u,v} is disjoint from f(q)={x,y}; any image sharing both is one of FOUR possible physical edges `{u,x},{u,y},{v,x},{v,y}`. One typed injective original source factor per physical edge. Similarly four on the other side. Delete all true original W3 incident flags meeting these at most eight source factors; each source factor has exactly d immutable true incidence IDs. This statement is **loss upper bound**, not positivity when C_raw<=8d.

**Lemma AA4-CX.3 (ALL h>=1, source geometry W(3,s), every fixed original f,g, any cuts):** For each original point p, at most `2(a−2)s` genuinely nonincident original lines l can generate `f(p)∩f(q)!=∅` along the unique true-original P3. Reason: at most `2(a−2)` original POINT factor images f(q) share a physical coordinate with f(p), and each genuine original source point q collinear with p is the P3 middle point for exactly s different lines l passing through q but NOT p. By true source projective GQ uniqueness, no double counting of q,l is needed for the bound. The dual proof gives the same bound per original source line l for `g(l)∩g(l0)!=∅`. Therefore the union of BAD original nonincident cut anchors (violating either physical double-disjointness condition) is bounded by

```text
N_bad(X,Y;f,g) <= 2(a−2)s*(|P_X|+|L_Y|)
              <= 4(a−2)s V = O(s^(11/2)).                       (CX.6)
```

The O(s^(11/2)) holds since a=Θ(s^(3/2)). The raw positive floor CX.2 is only Ω(s⁵), so subtracting CX.6 **CANNOT** certify that any of the guaranteed Ω(s⁵) raw-positive source P3 anchors is double-disjoint. Even on double-disjoint anchors CX.5 permits all raw cross-flags to disappear when `C(p,l)<=8d`; the global raw moment lower is too weak to avoid that loss. AA4-CX therefore explicitly documents two still-open transfer obstructions, not an accepted sixflag floor.

## 4. What precise scope DOES and DOES NOT follow

- **Follows:** a rigorously stronger EVERY-global-map, EVERY-halfcut all-h Ω(s⁵) lower count of distinct TRUE original nonincident source P3 anchors with at least one actual original incidence between raw physical source-spoke neighbor sets. Entire original source point-line factor IDs, complete typed f,g, arbitrary correlations and immutable original flag IDs preserved.
- **Follows:** any admissible DOUBLE-DISJOINT anchor loses at most four spoke source factors per side (at most 8d real original cross-flags); globally the original source anchors that fail double-disjointness are at most O(s^(11/2)). These are exact deterministic upper bounds, not probabilistic expectations.
- **Does NOT follow:** at least one safe-spoke cross-flag universally; source occupied C4 center edges; existence of two other distinct actual GQ original incidence flags completing one true source 3×3 matching; historical accepted positive GF(5) six-ID Q; a universal `U_BBo=Ω(s^6)`, all-seven `S=Ω(s^6)`, infinite root Branch B small-S correlated family, root-equivalent C, full R3 or ASET exponent. A source cross-spoke flag is not the same thing as a SOURCE 3-matching!
- **Beyond h>=24:** CX.5 and CX.6 hold for ALL dyadic h>=1, not only large s. CX.1–CX.2 are explicitly asserted all h>=24 with a simple non-optimal constant; do not promote finite smaller-h observations.

## 5. Independent exact falsifiers and previous proof provenance

- `research/hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion.py`: exact h-arithmetic; real original source AA4-CW raw/source-first identity; full original P3 path q,l0; physical doubled-factor label intersection tests; explicit safe original source spoke incidence flag counting; exact loss decomposition and bad-anchor bound.
- `research/test_hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion.py`: REAL original W32 lex/S72, three physical halfcuts for each: every true original nonincident source p,l and independent original-incidence-ID-first oracle for raw and safe; W34 lex/random two halfcuts each and W38 lex/random halfcut each with independent original-source flag-first anchored falsifiers; h1..30 arbitrary-precision integer all-h and physical exclusion gates; original local source spectral cap independently checked with exact squared comparisons (no float); invalid source maps/cuts/h fail closed.
- `.github/workflows/hyp105-issue230-aa4cx-local-spectrum-doubled-exclusion.yml`: isolated GitHub-hosted unit test lanes, exact PR head, no local unverified machine success claims.

**Prior art:** original GQ strongly regular point graph and incidence singular spectrum are classical ([Brouwer–Haemers, *Spectra of Graphs*](https://link.springer.com/book/10.1007/978-1-4614-1939-6)); expander mixing is classical. New scope is the project-specific EXACT original map-independent raw-spoke Ω(s⁵) improvement and complete doubled-source image fail-loss quantification under two fully arbitrary correlated ORIGINAL source factor-to-minimal-K_a physical pair injections. No broad standalone new spectral theorem claim.

**Next meaningful mathematical milestone AA4-CY:** Derive an ORIGINAL cross-incidence moment estimate (likely a second-moment or robust source-fiber/dual incidence bound) surviving AA4-CX's `O(s^(11/2))` bad-anchor deletion AND `8d` loss per good anchor, or a truly sixflag/all-seven GF(5) compensation inequality. Without both barriers controlled, no path from raw-spoke positive counts to Branch A. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER** and stack stays scientific Draft pending exact-head full Research, independent qualified mathematical review, and parent PR integration acceptance.
