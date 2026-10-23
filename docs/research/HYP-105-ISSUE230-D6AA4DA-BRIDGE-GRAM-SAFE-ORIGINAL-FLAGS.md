# HYP-105 #230 — AA4-DA: original bridge-Gram theorem preserves SAFE source spoke incidence after both physical exclusions

**Scientific Draft. Mathematical PARTIAL progress, NOT root Branch A/B/C.** Strict child [AA4-CZ #626](https://github.com/definitely-stable/Mathlab/pull/626), pinned parent HEAD `5179c44615ab621140f3f9a42d969730c562aecc`. Ancestors [AA4-CW #623](https://github.com/definitely-stable/Mathlab/pull/623), [AA4-CX #624](https://github.com/definitely-stable/Mathlab/pull/624), [AA4-CY #625](https://github.com/definitely-stable/Mathlab/pull/625) and [AA4-CR #618](https://github.com/definitely-stable/Mathlab/pull/618). Keep genuine ORIGINAL W(3,s), all six incidence IDs immutable, physically injected globally complete typed original f,g with arbitrary correlation and historical GF5 class registry unchanged.

## 1. NEW exact mathematical result / scope and quantifiers

Let **every** dyadic s=2^h, h>=96; let V=(s+1)(s²+1) be original POINT factor and original LINE factor count in genuine symplectic W(3,s), d=s+1 original source degree, a the MINIMAL physical K_a coordinate count with binom(a,2)>=V and k=floor(a/2). Let f be any full injective original POINT factor→physical pair image map and g any full injective original LINE factor→physical pair image map, with NO independent/randomness assumption and the SAME common physical alphabet. Let X,Y be ANY two k-coordinate physical subsets (may overlap). Use the genuine original incidence matrix M[p,l]=1 iff p is genuinely incident to l. Let physical overlapping ORIGINAL point-factor raw spoke set

```
A_p = {i ORIGINAL POINT: f(i) ⊂ X, i != p, f(i) ∩ f(p) != ∅}
```

and B_l dually from g and Y.

For any genuine ORIGINAL source NONINCIDENT pair p,l with unique genuine original source 3-incidence-ID path `p--l0--q--l`, require both anchor physical exclusion gates

```
f(p) ∩ f(q) = empty;       g(l) ∩ g(l0) = empty.       (DA.0)
```

Define **SAFE** source neighbor sets by deleting from A_p all original source point factors i with f(i) meeting doubled original point-factor image f(q), and from B_l all original line factors j with g(j) meeting doubled original line-factor g(l0):

```
A_safe(p,l)={i∈A_p: f(i)∩f(q)=∅};
B_safe(p,l)={j∈B_l: g(j)∩g(l0)=∅};
C_safe(p,l) = #{(i,j) genuine immutable ORIGINAL incidence IDs:
                 i∈A_safe, j∈B_safe, M[i,j]=1}.
```

Let G_XY denote only the genuine original nonincident p,l in physical cuts satisfying DA.0 (same one globally fixed f,g, no re-embedding at any anchor).

**Theorem AA4-DA.1 (ALL h>=96, EVERY genuine original W(3,2^h), EVERY full arbitrarily correlated original f,g, EVERY physical halfcuts X,Y):**

```
L_raw→safe = sum_(p,l in G_XY) (C_raw(p,l)-C_safe(p,l))
             <= 384*s^(27/4).                               (DA.1)

sum_(p,l in G_XY) C_safe(p,l)
             >= s^7/16384.                                  (DA.2)

#{(p,l)∈G_XY: C_safe(p,l)>=1}
             >= s^(11/2)/2^35.                               (DA.3)
```

(Careful: real-valued upper/lower exponents are exact analytic mathematical inequalities; exact dyadic integer falsifiers avoid floating point. At h>=96, s is a perfect fourth power.) Thus many genuine original nonincident three-ID source P3s persist after **both anchor double-disjointness conditions AND both ORIGINAL raw source spoke-image deletions**. This is a new project-specific positive SAFE source-flag transfer. Importantly, a SAFE genuine source crossing incidence (i,j) is **NOT** an occupied physical C4 center edge or a true source 3×3 perfect matching. No accepted historical six-original-incidence-ID GF5 B/B-overlap lower, no all-seven S_s floor, root Branch A/B/C or R3 exponent follows.

## 2. Critical source geometry: physical bridge edges versus true ORIGINAL pencils

Fix one admissible actual original nonincident anchor p--l0--q--l satisfying physical DA.0. An original point spoke i is RAW but NOT SAFE iff its ACTUAL physical pair edge f(i) meets both disjoint edges f(p) and f(q). Therefore f(i) is **one of four possible bridge physical pair edges** (as in AA4-CX). For the LEFT-deleted source crossing original flags, we may drop the Y-cut/anchor condition, ignore l≠l0, and overcount every real ORIGINAL line l incident with the real ORIGINAL projection point q and every real ORIGINAL line j incident with this bridge POINT source factor i such that g(l),g(j) are physically adjacent edges in the Y-cut.

Let A_g be the V×V symmetric line-graph adjacency matrix **on TRUE ORIGINAL LINE factor IDs** selected by the fixed g-cut: A_g[l,j]=1 iff l!=j, g(l),g(j)⊂Y and g(l)∩g(j)≠∅. Let

```
K_g(q,i) = (M A_g M^T)[q,i]
          = Σ_{l original incident q} Σ_{j original incident i} A_g[l,j].
                                                                  (DA.4)
```

Only genuine ORIGINAL incidence relation appears in M; physical A_g is merely source-indexed. Let

```
r_f(q,i) = #{p genuine ORIGINAL POINT:
              p≠q, p and q TRUE source collinear,
              f(p)∩f(q)=∅,
              f(i)∩f(p)≠∅, f(i)∩f(q)≠∅}.
```

Then the exact true-original LEFT bridge-Gram *overcount* satisfies

```
L_LEFT <= Σ_{q,i} r_f(q,i) K_g(q,i).                    (DA.5)
```

The dual RIGHT loss is bounded identically by Σ_{l0,j} r_g(l0,j) K_f(l0,j), with `K_f = M^T A_f M` and A_f physical-overlap adjacency indexed by genuine ORIGINAL POINT factor IDs, and r_g counts genuine ORIGINAL source intersecting LINE pairs in the DUAL W(3,s).

**Uniform combinatorial bridge multiplicities, every complete injective pair embedding:**

1. For each ordered TRUE ORIGINAL source-collinear p,q, f(p) and f(q) disjoint have **at most four** physical edges intersecting both. Any is the image of at most ONE original POINT factor i because f globally injective. GQ collinearity source degree is s(s+1)=sd. Hence `Σ_{q,i} r_f(q,i) <=4Vsd` (and same for r_g).
2. Fix real original source (q,i) with r_f(q,i)>0. Then the physical f(i) intersects f(q) in EXACTLY one coordinate (f(i)≠f(q)). Its OTHER coordinate y is outside f(q). Every original p counted in r_f(q,i) has f(p) disjoint from f(q) and meets f(i), hence f(p) must contain y. The **single shared physical coordinate star** contains at most a−1 pair edges, excluding f(i), yielding `r_f(q,i)<=a−2`. Identical on dual.
3. Therefore `Σ_{q,i} r_f(q,i)^2 <=4Vsd(a−2)`. This crucially counts SOURCE-collinear true original ordered p,q and physically UNIQUE bridge i; it is NOT an arbitrary source factor gadget.

## 3. Frobenius bound for GQ source pencil–physical overlap–GQ source pencil

The ORIGINAL W(3,s) incidence M is d-regular, nontrivial singular value sqrt(2s); write `M=(d/V)J+E`, ||E||op=sqrt(2s). The physical line-graph A_g on TRUE ORIGINAL LINE factor IDs satisfies ||A_g||op<=2k, ||A_g||F²<=2kV, ||A_g 1||<=2k sqrt(V), 1ᵀ A_g 1<=2kV. Thus

```
K_g = M A_g M^T

||K_g||F
 <= ||(d²/V²)J A_g J||F
   + ||(d/V) J A_g E^T||F
   + ||(d/V) E A_g J||F
   + ||E A_g E^T||F

 <= 2kd² + 4dk sqrt(2s) +2s sqrt(2kV).            (DA.6)
```

The same holds for the true-original DUAL matrix K_f=M^T A_f M. From the elementary exact dyadic upper V<=2s³,d<=2s,k<=s^(3/2),a−2<=2s^(3/2) (s>=16), DA.6 implies

```
||K_g||F, ||K_f||F <=32s^(7/2).                  (DA.7)
```

By Cauchy–Schwarz on the **real original q,i index set**, physical bridge uniqueness, DA.5, and the source GQ collinearity bound:

```
L_LEFT
 <= sqrt(Σ r_f(q,i)²) ||K_g||F
 <= sqrt(4Vsd(a−2)) * 32s^(7/2)
 <= sqrt(32)*32 s^(27/4)
 < 192 s^(27/4).                                  (DA.8)
```

Dual same. The union deletion of source flags is at most the sum of the two directions, so DA.1 follows. The key exponent 27/4=6.75 is LESS than the guaranteed AA4-CZ original double-disjoint raw mass exponent 7.

## 4. Compare genuine original SAFE losses with AA4-CZ's positive source raw mass

AA4-CZ gives for every h>=60, every fixed complete correlated f,g and cuts:

```
T_GOOD_RAW=Σ_(genuine nonincident double-disjoint paths) C_raw
 >= dVk²/2048.                                            (DA.9)
```

For dyadic h>=96, minimal physical K_a gives k²>=s³/4, d>=s, V>s³. Therefore `T_GOOD_RAW>=s^7/8192`. Since s>=2^96 ensures `s^(1/4)>=2^24>384*16384=6,291,456`,

```
L_raw→safe <=384s^(27/4) <=s^7/16384.
T_GOOD_SAFE>=s^7/8192−s^7/16384=s^7/16384.
```

Lastly, for all source anchor pairs the ORIGINAL RAW C[p,l] is nonnegative and safe C_safe[p,l]<=C[p,l], hence

```
Σ_{good} C_safe[p,l]^2 <= Q_RAW <=64sVk³<=128s^(17/2).
```

True-original Cauchy gives `#{good C_safe>0}>=T_GOOD_SAFE²/Q_RAW>=s^(11/2)/2^35`. Every SOURCE anchor remains a real unique ORIGINAL three-incidence-ID path; the C_safe value counts true original *source* flag IDs i,j only, not artificial physical incidences.

## 5. Genuine ORIGINAL independent falsifiers (finite h only, no proof extrapolation)

File `research/hyp105_issue230_d6aa4da_bridge_gram_safe_source_flags.py` has:
- Big integer gate h1..110 with h95/h96 exact conservative analytic transition.
- TRUE original source first/second moment from AA4-CZ and exact RAW→SAFE source flag census from AA4-CX, using fixed one global original map.
- Two new **separately source-/dual-source indexed** bridge-Gram overcounts by enumeration of every ordered true ORIGINAL collinear p,q and their at most four occupied bridge original POINT factor IDs i (plus dual LINE factors). Each computes `K_g(q,i)` by actual immutable original source incidence pencils and actual physical g-cut overlap, with a cache only for performance; asserts bridge multiplicity<=a−2 and true original GQ collinearity degree.

Independent test `research/test_hyp105_issue230_d6aa4da_bridge_gram_safe_source_flags.py` **does not reuse** that source bridge enumeration: for genuine original W32 and W34 it loops EVERY original typed source factor ID i instead of looking up the four coordinate bridge pairs, and directly builds K_g and K_f from all genuine source pencil pairs and physical edge intersections. A separate W32 test enumerates EVERY immutable TRUE ORIGINAL source incidence ID for EACH genuine nonincident double-disjoint source P3 and checks RAW, SAFE and exact deletion vs the bridge-Gram overcount. Genuine W34/W38 lex/random globally frozen typed complete images and multiple coordinate cuts compare original SAFE losses, positive source counts and formal nonimplications.

Five hosted isolated CI lanes are additive; exact-HEAD CI must be inspected before asserting validation. No physical K_a-derived surrogate ORIGINAL source incidence is allowed. No local workstation tests or generated synthetic replacement W3 geometry.

## 6. Limits / why this is NOT yet the original GF(5) theorem

**SAFE original crossed source flag ≠ historical six-incidence-ID matching.** Even if the ORIGINAL point factors i∈A_safe and line factors j∈B_safe are truly incident, the physical C4 template on the point side would need two additional original source factor images (center {z,w} and another bridge source factor) all occupied; similarly line side. Finally three disjoint **additional true ORIGINAL incidence IDs** must connect the two completed three-factor triples in a perfect 3×3 matching. Original GQ girth8 ensures matching uniqueness if present, but does not force existence. Existing [AA4-CV #622](https://github.com/definitely-stable/Mathlab/pull/622) constructs maximally physically occupied C4 completions for one source path with zero original 3×3 matching; it is not contradicted by AA4-DA.

The proof excludes physical double overlaps and bridge-spoke flags correctly, but a source SAFE crossing (i,j) might not lie in ANY admissible physically occupied C4 completion family (physical center edge absent or other spokes not completed), and might not participate in a 3×3 perfect matching. Thus no universal B/B-overlap positive Q lower, no universal whole-seven `S_s(f,g)>=cs^6`, no small-S all-h counterfamily, no root-equivalent reduction C, no R3/ASET exponent. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`.

**Next AA4-DB high-value gate**: transfer robust SAFE original source flag mass through both occupied physical C4 centers and two further DISTINCT immutable ORIGINAL matching flags, or a genuine fixed-map seven-GF5 class compensation bound. Need avoid applying only generic spectral mixing without original matching source correlation structure. Keep AA4-DA Scientific Draft, independent qualified mathematics review and full exact-head GitHub-hosted CI required before integration.

**Prior art boundary:** singular spectra of original generalized quadrangles and expander-mixing are classical (A. E. Brouwer & W. H. Haemers, *Spectra of Graphs*, Springer, 2012). Project-specific bridge-multiplicity/Gram composition and combined physical/source all-global-map transfer may be publishable *conditional on independent review*, but no general new universal spectral theorem is claimed.
