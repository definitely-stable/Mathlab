# HYP-105 issue #230 — JPKC-007: original-source completion deficit and physical palette feasibility

**2026-10-13. RESTRICTED_THEOREM_C / exactly reproducible ORIGINAL deficit certificates. Branch A/B OPEN.**
Strict Draft child of fully 4/4-success [JPKC-006 #432](https://github.com/definitely-stable/Mathlab/pull/432), parent pinned HEAD `22e49e1991992deb437a44a9938e9629b78e3868`; `main` unchanged, no merge. D6-AA4 #433 source-stratum Fréchet relaxation has ZERO certified positivity on W32 S68/S72, so no independent left/right pseudocoupling is used here.

## 1. The correct obstruction gate after JPKC-006

For any actual complete ORIGINAL W(3,s), s=2^h, with two globally injective physical pair maps f,g to E(K_a), take an endpoint-bad physically coordinate-proper simple oriented Kikuchi P3, with its exact three ORIGINAL incidence IDs T. As proved in JPKC-006, the ONLY true selected seven-positive sixsets Q containing T can be completed by the non-GQ ORIGINAL types:

1. A/A matched D6: three new ORIGINAL incidences form an independent point-line matching;
2. A-left/B-right: line-wedge plus single ORIGINAL incident edge;
3. B-left/A-right: point-wedge plus single ORIGINAL incident edge.

JPKC-006 showed at most 12 source P3 seeds per selected sixset but did NOT guarantee even one such selected Q exists. Therefore JPKC-007 separates the demand into three distinct feasibility layers: actual occupied physical K_a pair edges, actual ORIGINAL GQ endpoint/collinearity/concurrency, and actual signed-positionally aligned selected GF5 motif topology.

The distinctions are ALL on the SAME globally complete f,g, not on fictitious independent source marginals. The original three-incidence-ID source structure is retained until the final classifier.

## 2. THEOREM J22 — exact all-h physical A-half palette-hole decomposition

Let z0,z1,z2,z3 be four distinct physical row symbols of a projected P4, let U=[a]\{z0,z1,z2,z3}, t=a−4. Any physically C6-completing *A-side* three-edge continuation must be

`(z3,z4), (z4,z5), (z5,z0)`, for ordered DISTINCT z4,z5∈U.

Let `F={z∈U : {z3,z}∈image(f)}`, `L={z∈U : {z,z0}∈image(f)}`, and `M_int` be missing physical unordered pairs contained in U (use image(g) for right side). Put `m=binom(a,2)-V`, the EXACT total number of missing physical pair labels on that side.

**THEOREM J22 (every h; EXACT algebraic identity):**

```
A_half(z0,z3) =
    |F| |L| - |F∩L|
  - # {(z4,z5)∈F×L : z4 != z5, {z4,z5}∈M_int}.
```

Equivalently, the `t(t−1)` ordered choices partition disjointly by the FIRST missing physical chord: missing z3–z4; missing z5–z0 after the first was occupied; missing middle z4–z5 after both endpoints were occupied; and fully occupied A-half paths. The implementation checks BOTH independent counts on every true source P3.

**THEOREM J24 (all h; valid PALETTE lower, NOT an original GF5 certificate):**

```
A_half >= max(0, |F||L| - |F∩L| - 2m).
```

Each missing physical unordered pair inside U removes at most two oriented choices (z4,z5). If both projected P4 endpoints have ALL their chords to U occupied, then F=L=U and
`A_half >= max(0,(a−4)(a−5)-2m)`. Here m<a−1 for the minimal physical alphabet. Whenever a is sufficiently large this palette-only bound is quadratic in a for such regular endpoints; HOWEVER it does not guarantee any accepted ORIGINAL sixset, because source incidence matching and GF5 positional alignment remain unrestricted.

These two results are exact universally quantified finite/all-h statements, do NOT assume random physical labels and do NOT use an unproved `S=Omega(s6)`.

## 3. THEOREM J23 — exact original source-deficit accounting; no hidden pseudocoupling

Fix a proper physical P3 seed T. Let A_L(P), A_R(P) be the exact A-half continuation source-factor triples obtained by J22 on left and right. Put L=|A_L|, R=|A_R|.

### D6 matching transfer

For each ordered pair (left completion triple, right completion triple), choose a bijection of their three TRUE source point factors to three TRUE source line factors (six permutations). There are exactly `6LR` source matching attempts. Partition:

- At least one proposed ORIGINAL point-line incidence does NOT belong to true W(3,s);
- All three actual ORIGINAL incidences exist, but their A/A projected physical six-column duals are NOT the SAME accepted D6 positional cycle;
- A genuine selected ORIGINAL D6 six-incidence set Q=T∪U.

Their nonnegative counts sum **EXACTLY to 6LR**. Counting is by these exact ordered source-factor matching proposals. No imputed GF5 positivity from merely two-sided 2-regularity (the D6-AA4 nonaligned A/A obstruction is preserved).

### B/A and A/B wedge transfers

For each actual A-side continuation triple, mark one of its three original factors as the UNIQUE original endpoint chord, giving exactly `3L` (or `3R`) labeled wedge proposals. Partition disjointly into:

- The endpoint-chord source factor fails original incidence with the fixed ORIGINAL endpoint q/r;
- The other two source factors lack a shared original GQ point/line (nonconcurrency/noncollinearity);
- They have a unique common original GQ factor, but its physical pair-label edge intersects the seed's four symbols on the doubled-factor B-side;
- All true ORIGINAL source incidences and physical conditions pass, producing a selected seven-positive B/A (respectively A/B) sixset.

The exact original GQ axiom and global f/g injection make each surviving wedge completion unique and ensure the four cells telescope to `3L` or `3R`. This telescope is not a novel unconditional lower on its FINAL positive cell.

The actual three class-positive survivor sets are independently compared per seed with the constructive JPKC-006 original alternate-completion oracle; at W32 also with the complete ORIGINAL exact seven-GF5 sixset census.

## 4. W32 S68/S72 gives a rigorous finite obstruction to PALETTE-ONLY extension

For s=2, V=(s+1)(s²+1)=15 and minimal a=6. Thus image(f)=image(g)=ALL edges of physical K6 for **every** legal global injection. For any coordinate-proper projected P4, U contains exactly TWO new physical vertices. Both choices (z4,z5) and (z5,z4) are fully present; there are EXACTLY TWO physical A-side completions on EACH side and ZERO physical palette missing-chord losses.

In particular, all physically endpoint-bad ORIGINAL P3 seeds in W32 S68/S72 have `L=R=2`, and each has exactly `6LR=24` physically valid candidate A/A source-factor matchings, plus 6 original B/A wedge proposals and 6 original A/B wedge proposals, before checking actual ORIGINAL GQ incidence and physical doubled-factor compatibility.

Yet the exhaustive ORIGINAL GF5 oracle finds only:
- S68: 544 endpoint-bad oriented physical P3s, just **8** with ANY selected Q, and 8 positive (P,Q) completion pairs;
- S72: 600 endpoint-bad P3s, just **10** with ANY selected Q, and 10 positive pairs.

Thus the naive implication “rich or even PERFECT physical Ka palette completion implies a positive ORIGINAL seven-GF5 extension for each endpoint-bad P3” is **FALSE**. This refutes that simple local proof strategy at s=2. It does not refute a properly quantified sufficiently-large-s extension theorem; finite low-S data alone never prove an infinite counterfamily.

The exact J23 partition identifies whether the missing transfer is (a) genuine ORIGINAL GQ incidence, (b) physical doubled-factor interference, or (c) nonaligned genuine source A/A cycles. The next stage may exploit these source-specific deficits, but cannot discard them as lower-order errors without a proof.

## 4a. Exact 2026-10-13 GitHub-hosted ORIGINAL loss certificates

On the TRUE original W32 S68 and S72 global f,g, the physical
image on EACH side is EXACTLY K6. Consequently the physical
A-half deficit from missing palette edges is ZERO for all
endpoint-bad seeds (two occupied completions per physical half).

The exact ORIGINAL source matching (D6) loss telescope counts
ATTEMPTED MATCHINGS of three source point factors against three
source line factors; these are NOT 6sets until all three ORIGINAL
point-line incidences actually exist:

| True ORIGINAL W32 map | Eligible endpoint-bad P3 | 6LR source-matching attempts | Absent ORIGINAL incidence | All ORIGINAL incidences exist, but nonaligned A/A | Accepted D6 |
|---|---:|---:|---:|---:|---:|
| S68 | 544 | 13,056 | **13,002** | 54 | **0** |
| S72 | 600 | 14,400 | **14,316** | 84 | **0** |

The two separately enumerated wedge transfer loss telescopes count
LABELED choices of one distinguished original endpoint-chord factor
among the three additional physical A-side factors:

| W32 | A-side | Physical 3L or 3R proposals | Source endpoint incidence missing | Source pair not collinear / not concurrent | GQ partner physical label conflicts | Real positive selected Q |
|---|---|---:|---:|---:|---:|---:|
| S68 | A-left / B-right | 3,264 | 2,594 | 380 | 288 | **2** |
| S68 | B-left / A-right | 3,264 | 2,682 | 318 | 258 | **6** |
| S72 | A-left / B-right | 3,600 | 2,816 | 462 | 318 | **4** |
| S72 | B-left / A-right | 3,600 | 2,984 | 364 | 246 | **6** |

These numbers were checked by a dedicated exact GitHub-hosted
source oracle against JPKC-006's independent construction and the
entire 62,370-left-candidate true ORIGINAL W32 seven-family census.

**Precise limitation:** these are counts of SOURCE-FACTOR PROPOSALS
and their reasons for failure, not counts of sixsets of independent
randomly sampled incidence patterns. The large absence of
ORIGINAL point-line matches is perfectly compatible with
genuine W(3,2) incidence sparsity. The observation shows why an
attempt to bound the final selected GF5 cell solely by physical
Ka occupancy cannot work pointwise. It is NOT an infinite
globally realizable Branch-B construction and does not exclude
a sophisticated global source-geometry compensation theorem.

The W34 checks use only **32 deterministic spread-out real
endpoint-bad physical source seeds** for lex, random, and true
D4 symplectic-spread maps, with complete PER-SELECTED-SEED
matching and wedge constructions. Their positive counts were,
respectively, 31/32, 30/32 and 31/32 covered; they are NOT
a full W34 seven-family census or a statistical/asymptotic
estimate, and are not directly comparable as probability
estimates to the exhaustive low-S W32 rows.

## 5. Implemented original finite truth gates

`research/hyp105_issue230_jpkc007_completion_deficit_ledger.py` and its six dedicated GitHub-hosted tests:
- use one globally valid ORIGINAL f,g with full symplectic GQ projection;
- enumerate all genuine endpoint-bad oriented proper physical P3s for W32 lex/reverse/S68/S72;
- check two independent algebraic ways of counting A-side physical completions and the exact 3-stage palette-hole decomposition;
- construct every true ORIGINAL D6 matching and B/A or A/B wedge source extension independently from the prior JPKC-006 generator;
- explicitly retain and quantify genuine source incidence deficits, true GQ collinearity/concurrency, physical B-side interference, and nonaligned A/A positional cycles;
- require exact per-source equality with constructive JPKC-006 outputs and complete W32 accepted-sixset reference classifier;
- for W34 lex/random and true D4 symplectic-spread physically complete f,g, evaluate exactly **32 deterministic source-distributed seeds per map** (complete per seed, not a random sample/full W34 seven-GF5 census);
- reject illegal global injections, incorrect exact W32 scope, path budget overflow or bad sampling budget.

No W38 or full W34 seven-family census; no extrapolation from finite ratios. GitHub-hosted runners ONLY.

## 6. What a future proof must actually establish

A simple lower on the physical palette A-half `A_half=Omega(a²)` cannot imply any lower on source-positive Q unless it is paired with a **uniform ORIGINAL incidence-compatible matching or wedge survival** bound and a **nonaligned A/A penalty**. The correct necessary target is a noncircular positive inequality on the FINAL cells of J23 across ALL original anchors under actual global f/g occupancy, or a truly stronger geometrical invariant. D6-AA #430 and D6-AA4 #433 provide position-aware moments and identify the relaxation obstruction, but their marginal Fréchet coupling is not a realizable global witness.

Next permissible **JPKC-008**: search for a globally coupled ORIGINAL demand-matching/Hall deficiency certificate across shared source point/line factors and their globally occupied physical edges; quantify whether endpoint-shortage incidence patterns must force positive witnesses of OTHER classes, or construct a lawful infinite adversarial family. Keep root #230/#176/#169 OPEN and do not merge unreviewed work.
