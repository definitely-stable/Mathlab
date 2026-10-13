# HYP-105 / #230 — JPKC-003: ORIGINAL anchored two-channel variance and endpoint/internal collision concentration

**2026-10-13. RESTRICTED_THEOREM_C / conditional all-h J8, exact all-finite-h J6/J7. Neither Root A nor B solved.**

Strict child of all-4-CI-success [JPKC-002 Draft #426](https://github.com/definitely-stable/Mathlab/pull/426) exact parent HEAD `c5af5026ce72a96439015e34fdf341b625f8be2c`. Parent [JPKC-001 #423](https://github.com/definitely-stable/Mathlab/pull/423) also 4/4 green. Do not merge/change `main`.

## 1. Scope; the original anchor makes endpoint blocking CONSTANT per whole fiber

Let s=2^h, h>=1; V=(s+1)(s²+1); N=V(s+1); a=min{t:binom(t,2)>=V}. Fix **ONE** globally complete injective ORIGINAL point map f and line map g, possibly adversarially correlated, with minimal physical K_a palette on each typed side. Form the true two-diagonal G on [a]×[a].

For every ORIGINAL nonincident point-line pair (q,r), its UNIQUE original GQ projection is q--ell--p--r. There are precisely four potential ORIENTED physical endpoints, falling into two reversal-related diagonal channels:

- channel 0: (x,y)->(x',y') and its reversal;
- channel 1: (x,y')->(x',y) and its reversal,

where f(q)={x,x'}, g(r)={y,y'}. Let `b0(q,r)`, `b1(q,r)` be the counts of coordinate-proper, nonincident, ORIGINAL-anchor physically BLOCKED oriented simple physical length-3 paths on the two forward channels. Reversal preserves both the entire original path property and blocker status, so these are the reverse counts too.

Write `B_qr=2(b0+b1)` and `K_qr=2[b0(b0-1)+b1(b1-1)]`. K_qr is precisely the number of ORDERED distinct blocked path pairs at the same oriented endpoint within this original anchor. Put `M=V²-N`, `B=sum B_qr`, `K=sum K_qr`.

Define the ORIGINAL **endpoint-bad** predicate

```
e(q,r)= [ f(q) intersects f(p) ] OR [ g(r) intersects g(ell) ].
```

This predicate depends ONLY on the ORIGINAL anchor (q,r), not on the chosen internal physical three-path or diagonal channel. If it holds, **EVERY** endpoint-complete coordinate-proper physical path in any of this anchor's channels is automatically blocked; if not, every blocked path in this anchor is **internal-only**, blocked exclusively because f(p) or g(ell) intersects an *internal* path coordinate, not the endpoint pair itself.

Thus the endpoint-blocked path population E and internal-only population I=B-E are completely separated BY ORIGINAL ANCHOR. In particular, collision pairs with the SAME physical endpoints cannot mix endpoint-bad and internal-only categories. This is a stronger and precisely scoped statement than treating PR #394's E_H and I_H as independent pointwise energies: here we measure the FULL G only. `C_H<=B_G` remains the only proved retained/full comparison.

## 2. THEOREM J6: exact original-anchor and physical-diagonal TWO-SCALE variance

For each original anchor the binomial identity yields

```
K_qr = B_qr²/4 - B_qr + [b0(q,r)-b1(q,r)]².
```

Summing, and writing `Bbar=B/M`, gives the **exact all-finite-h equality**

```
K = B²/(4M) - B
      + (1/4) sum_(q,r nonincident) [B_qr-Bbar]²
      + sum_(q,r nonincident) [b0(q,r)-b1(q,r)]².      (J6)
```

Both variance terms are nonnegative, with NO statistical independence, generic graph approximation, or signed term. The first is ORIGINAL GQ anchor-load variance, and the second is within-anchor two-diagonal imbalance. JPKC-002/J5 retained only the first scalar Cauchy term. J6 precisely identifies BOTH missing energies and improves any finite certificate that can independently lower-bound either variance.

This is an exact reindexing/strengthening of the original JPKC-002 collision identity, NOT an unconditional new GF5 positive motif count or improved ASET exponent.

## 3. THEOREM J7: exact endpoint/internal split and source-support Cauchy cuts

Let M_f be the number of UNORDERED collinear DISTINCT original point pairs whose physical f-label edges intersect; M_g the dual number of ORIGINAL concurrent line pairs with intersecting g-labels. PR #394 proves uniformly for all legal complete injections

```
M_f,M_g <= C_s := (s-1)V+(s²+1)(a-1) = (1+o(1))s⁴.
```

Count endpoint-bad ORIGINAL nonincident anchors:

```
A_L = #{(q,r): f(q) intersects f(p)} = 2s M_f,
A_R = #{(q,r): g(r) intersects g(ell)} = 2s M_g,
A   = A_L + A_R - A_both <=2s(M_f+M_g) <=4s C_s.
```

The factors 2s are EXACT: each unordered collinear source point pair yields two orientations q,p, and for each orientation exactly s original nonincident right lines r through p outside its unique original line ell; the point-line dual is identical. Inclusion-exclusion gives the exact union size A; no assumption of independent left/right labels.

The number of endpoint-bad ORIENTED grid endpoint fibers is at most 4A, and for remaining original anchors at most 4(M-A). Thus by Cauchy-Schwarz and the J6 diagonal/reversal identity, the **exact finite bounds**

```
K_E >= E²/(4A) - E,              if A>0; if A=0 then E=K_E=0
K_I >= I²/[4(M-A)] - I,          if M>A; if M=A then I=K_I=0
K = K_E+K_I.
```

Here K_E (respectively K_I) counts ordered pairs of TWO endpoint-bad (respectively TWO internal-only) blocked paths with the same physical endpoints. There are **no mixed E/I terms at all**, not merely a nonnegative leftover. Total J7 lower is the sum of two separate bounds, generally stronger than J5 `B²/(4M)-B`. All displayed lower expressions can be negative at small finite s and remain mathematically valid; implementation never clips a negative proven lower to zero without labeling it.

The independently implemented D6-Y sharp near-complete Ahlswede–Katona (1978) occupied-edge image bound is also checked on BOTH f/g:
```
A_image(E)<=a*C(a-1,2)-2m(a-2)+C(m,2), m=C(a,2)-V.
```
It controls PHYSICAL image pair intersections over all ORIGINAL pairs, not the ORIGINAL-collinear-only M_f and M_g; it CANNOT substitute for PR #394's stronger O(s⁴) GQ source theorem. No novelty claim for the Ahlswede–Katona extremal inequality.

## 4. THEOREM J8: sharper ALL-h necessary concentration dichotomy for ANY hypothetical Root-B family

Assume a sequence s=2^h->infinity of arbitrary complete globally correlated original pair maps f_s,g_s has `S_s=o(s⁶)`. PR #394 plus JPKC-001/JPKC-002 already proves

```
B=E+I >= (16-o(1))s⁶,
D6 <=S=o(s⁶).
```

Therefore, by pigeonhole, **at least one** of the following holds along EACH sufficiently large s (which branch is taken may vary with s):

**Endpoint branch: E >= (8-o(1))s⁶.** Since A<=4s C_s=(4+o(1))s⁵, J7 implies

```
K_E >= E²/(4A)-E >= (4-o(1))s⁷.
```

At most 12 D6=o(s⁶) of ALL ordered blocked-endpoint collision pairs can form proper physical C6, hence the combined **endpoint-bad shared-interior and coordinate-improper C6** defect mass is >=(4-o(1))s⁷.

**Internal branch: I >= (8-o(1))s⁶.** As M=(1+o(1))s⁶ and M-A<=M, J7 gives

```
K_I >= I²/[4(M-A)]-I >= (8-o(1))s⁶.
```

Subtracting <=12D6=o(s⁶) correct C6 pairs forces the **internal-only** shared-interior + coordinate-improper defect mass >=(8-o(1))s⁶.

J8 is a genuine sharpening of the NECESSARY structural conditions for a hypothetical counterfamily: either an s⁷-scale endpoint-sourced collision storm is present, or an s⁶-scale internal-only collision defect must be present. This does **NOT** prove either branch impossible. Huge collision counts may be fully absorbed by improper structures. A separate all-h anti-concentration/compensation theorem is still mandatory to deduce Root A.

## 5. Implemented original-finite falsifiers

`research/hyp105_issue230_jpkc003_anchor_channel_concentration.py` independently:
1. validates the complete TRUE ORIGINAL GQ f,g and all original nonincident unique projections;
2. computes ALL physical oriented simple path fibers from JPKC-002 and exactly two original physical diagonal channels per anchor, checking reversal and anchor-constant endpoint badness;
3. directly counts M_f from collinear ORIGINAL point pairs and M_g from ORIGINAL concurrent line pairs; checks `A_L=2s M_f, A_R=2s M_g`;
4. checks both EXACT J6 nonnegative variance terms, endpoint/internal J7 Cauchy bounds and `K=K_E+K_I`, independently against the full ordered collision tensor from JPKC-002;
5. computes sharp near-complete physical-image occupancy cut on both original typed maps, with separately tested O(V²) physical adjacency definition;
6. runs W32 lex/reverse/S68/S72, W34 lex/random, and independently constructed REAL D4 Desarguesian symplectic-spread W34 maps.

All fixtures use ONE coherent f,g; nothing is resampled per (q,r) anchor or denominator. W38 full path enumeration is not represented as a complete tested census. Dedicated hosted tests use explicit fail-closed path budgets and reject illegal global injections. No W34 full seven-family census is claimed.

## 6. Next permitted research gate (JPKC-004)

- Prove/falsify a **GEOMETRY + globally occupied-image capacity** restriction on the *bad* J8 collision terms, not on their sum with correct D6.
- Specifically: does the s⁷ endpoint storm force additional ORIGINAL seven-family GF5 motifs, or can a single coherent infinite spread-style family absorb it in coordinate-improper cycles?
- Conversely, if almost all blockers are internal-only, establish a quantitative transversal/expansion property across distinct original anchors that transfers its s⁶ collision mass to at least one of the remaining six accepted positive classes.
- Track actual original incidence IDs and source overlap types before using D6-W marginal messages; D6-X/Y demonstrate that seemingly consistent local pseudolabelings can violate global image cuts.

**Acceptance rule:** exact final HEAD GitHub-hosted Contract/INDEX/Proof Audit/full Research all SUCCESS plus independent mathematical review before any merge. Root #230/#176/#169 remain OPEN. `main` untouched. Never label this as `PROVED_A`, `COUNTEREXAMPLE_B`, an R3 upper bound or ASET exponent.
