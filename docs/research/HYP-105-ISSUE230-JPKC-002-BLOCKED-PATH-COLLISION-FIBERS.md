# HYP-105 / #230 — JPKC-002: proper- and blocked-path endpoint-collision theorem

**2026-10-13; STATUS: RESTRICTED_THEOREM_C + TRUE ORIGINAL FINITE ORACLES. Root PROVED_A / COUNTEREXAMPLE_B both OPEN.** Strict child of JPKC-001 [#423] at exact parent HEAD `d0d8e6ce428720050de5239e42a635b72ba9c1c7`. No main modification/merge. This note does not import or assume merged the separate Kikuchi [#366] or D6-X [#424] stacks.

## 1. Frozen model and count conventions

Use the TRUE original generalized quadrangle W(3,s), s=2^h, V=(s+1)(s^2+1), Delta=s+1, a=min{b:binom(b,2)>=V}, two COMPLETE separate globally injective, potentially correlated original pair maps f,g, and the TWO-DIAGONAL Kikuchi graph G on [a]x[a], n=a^2, m=2V Delta.

For an ORIENTED SIMPLE three-edge graph path
`P=(u,b,c,v)`, all four graph vertices distinct, define its **coordinate-proper** condition: all four first coordinates, and separately all four second coordinates, are distinct. These are the same proper physical path conditions (before endpoint-pair completion) as in PR #394. Count paths by their ORIENTED endpoint tuple (u,v), retaining each physical graph edge's UNIQUE original incidence ID.

Partition all oriented simple paths into the seven EXACT disjoint statuses:

1. coordinate repeat (not coordinate-proper);
2. coordinate-proper, missing at least one of original endpoint pair labels q=f^-1(first endpoint pair), r=g^-1(second endpoint pair);
3. endpoint labels present, q incident with r;
4. q nonincident r, unique GQ projection q--ell--p--r, physically blocked ONLY at original left anchor f(p);
5. same, blocked ONLY at original right anchor g(ell);
6. same, blocked on BOTH original physical sides;
7. accepted unblocked unique nonincident projection.

The accepted last case produces exactly one synchronized B/B-overlap original sixset per reversal pair, and is a strict SUBCLASS of all seven S motifs, not the total seven-census at s>2. Define `GOOD` as statuses 2..7 (coordinate-proper), and `BLOCKED` as statuses 4..6. The full-G block count B_G is **not** the retained H' quantity C_H in PR #394, although C_H<=B_G.

For each ordered graph endpoint pair (u,v), let `g_uv` be the number of GOOD paths, and `b_uv` the number of BLOCKED paths. Both are nonnegative integers.

## 2. ALL-h exact collision identity J3 (good paths)

**THEOREM J3.** For EVERY finite valid model and hence for every h>=1,

```
sum_(u,v) g_uv(g_uv-1)
   = 12 D6(G) + Theta_GG + I_GG.
```

`Theta_GG` counts ORDERED DISTINCT pairs of coordinate-proper oriented simple P3 paths with exactly the same oriented endpoints and AT LEAST one shared internal vertex. `I_GG` counts ORDERED DISTINCT pairs with the same oriented endpoints, mutually disjoint internal vertices, but whose resulting simple undirected 6-cycle repeats a first or second physical coordinate. Both masses are nonnegative and have no hidden 6-cycle multiplicity. `D6` is exactly the true accepted ORIGINAL A/A aligned connected sixset class, equal to proper six-cycles of G.

**Proof.** The left counts ordered pairs (P,Q) of DISTINCT GOOD oriented 3-paths with identical ordered endpoints. Their two 2-element sets of internal graph vertices either intersect (Theta_GG) or are disjoint. In the latter case the union is a SIMPLE graph C6; it either uses six distinct first AND six distinct second coordinates (accepted proper D6), or not (I_GG). Every proper C6 contributes exactly 12 such ordered oriented-endpoint path pairs: three antipodal vertex pairs times two orientations times two path orders, all GOOD. QED.

**Corollary:** `12S >= sum g_uv(g_uv-1)-Theta_GG-I_GG`. Its RHS equals `12D6`, so this is a useful exact DECOMPOSITION, not a new stronger numeric bound absent estimates on its two nonnegative defect terms.

## 3. ALL-h exact blocked-only identity J4

Let `D_BB` denote the number of ORDERED pairs of blocked paths with common ordered endpoints and disjoint internal graph vertices whose union is a proper physical six-cycle (so 0<=D_BB<=12D6). Let `Theta_BB` and `I_BB` denote the corresponding **blocked-blocked** subsets of Theta_GG and I_GG. Then

```
sum_(u,v) b_uv(b_uv-1) = D_BB + Theta_BB + I_BB
                         <=12 D6 + Theta_BB + I_BB.
```

All quantities are exact nonnegative integers. This is a source-specific decomposition: EVERY path in it has real ORIGINAL endpoint q,r and a uniquely defined original GQ projection q--ell--p--r. It does not simply reclassify coordinate-repeat graph paths.

**THEOREM J4 (NEW CONDITIONAL ALL-h NECESSARY BARRIER).** Assume an unbounded sequence of globally complete legal f_s,g_s satisfies `S_s=o(s^6)`. Then on the SAME complete maps,

```
B_G = sum b_uv >= (16-o(1)) s^6,
sum b_uv(b_uv-1) >= (48-o(1)) s^6,
Theta_BB + I_BB >= (48-o(1)) s^6.
```

**Proof.** From JPKC-001/PR #394, on that sequence the coherent retained H' has >=(16-o(1))s^6 endpoint-complete coordinate-proper paths; accepted unblocked paths are <=2S=o(s^6), and the incident-path mixed-book bound gives incident mass <=o(s^6) (because proper D6<=S and m=Theta(s^4), t*M2=o(s^6)). Thus retained blocked C_H >=(16-o(1))s^6, and B_G>=C_H. Let n=a^2, so the number of all ordered endpoint pairs is n²=a^4=(4+o(1))s^6. Cauchy-Schwarz gives

```
sum b_uv(b_uv-1) >= B_G²/a^4 - B_G.
```

The RHS is increasing for B_G>=a^4/2, satisfied for sufficiently large s under B_G>=(16-o(1))s^6. Its value is >=(48-o(1))s^6. Finally `D_BB<=12D6<=12S=o(s^6)`. Therefore Theta_BB+I_BB>=(48-o(1))s^6. QED.

**Strict enhancement of JPKC-001:** the previous K2 counterfamily condition merely forced total `Theta+12 C6_imp >=(48-o(1))s^6`. J4 forces the entire leading-order mass *inside collisions of two physically BLOCKED coordinate-proper true-GQ paths*, a subset of the original total coincidence and improper-cycle mass. No claim that one of Theta_BB or I_BB must individually attain a nonzero fixed share beyond the obvious pigeonhole (at least half of the combined asymptotic floor).

## 4. ALL-h anchor-fiber theorem J5 and sharper finite capacity

For any blocked path with oriented grid endpoints u=(x,y), v=(x',y'), its endpoint physical unordered labels determine

```
q=f^-1({x,x'}),  r=g^-1({y,y'}),   q not incident with r.
```

The GQ projection axiom determines exactly ONE ORIGINAL anchor q--ell--p--r for that pair (q,r). Therefore **every blocked path in the same oriented (u,v) fiber has the same ORIGINAL projection anchor**, even if their internal original incidences differ.

Conversely for a fixed ORIGINAL nonincident pair (q,r), there are exactly **four possible oriented physical endpoint pairs**: the two diagonals across f(q)×g(r), each in two orientations. Global pair injection ensures distinct original (q,r) yield disjoint endpoint-pair fibers.

The number of ORIGINAL nonincident (q,r) is exactly `V²-N`, `N=V Delta`. Thus b_uv has support on AT MOST `4(V²-N)` oriented endpoint fibers, so the stronger finite estimate is

```
sum b_uv(b_uv-1) >= B_G² / [4(V²-N)] - B_G.
```

Unlike replacing a^4 by the number of nonzero fibers, this bound is an **all-h algebraically known capacity**, independent of the unknown f,g or of B. The exact finite capacity is 720 for W32 (vs a^4=1296), and 27,200 for W34 (vs a^4=38,416). Both have the same asymptotic leading 4s^6, so J4's constant 48 is unchanged.

These original anchor fibers are the most promising transfer object for geometry-specific constraints on Theta_BB and I_BB: both paths at a collision have the SAME original q,r,p,ell, which was obscured by untyped Kikuchi K2 totals.

## 5. Direct finite SOURCE-ID taxonomy (without synthetic surrogates)

The new executable `research/hyp105_issue230_jpkc002_path_collision_taxonomy.py` reconstructs each physical edge's original incidence ID from the COMPLETE f,g and ORIGINAL GQ incidences. It enumerates all oriented simple P3 and partitions them into exact seven statuses by ORIGINAL projection, then iterates every ordered pair of paths sharing endpoints.

It independently checks:
- global total P3 against JPKC-001's separate graph moment implementation;
- complete ORIGINAL projection status counts against PR #394's independent `ProjectionClosure.census`;
- all collision pairs = diagonal P3 + Theta + 12 C6, using independent codegree-based K2;
- all proper six-cycle pairs, and all improper-cycle pairs, with the exact factor 12;
- each proper physical six-cycle contains SIX DISTINCT ORIGINAL incidence IDs and is exactly ORIGINAL D6 in the true W32 seven-family classifier;
- no coordinate-improper physical six-cycle with six distinct original incidences can be misclassified as one of the seven selected GF5-positive classes;
- J3/J4 exact falling-factorial identities and positive CS slack on same-map data;
- each blocked fiber maps to a single real ORIGINAL nonincident GQ anchor q,r and the four-fiber capacity J5;
- ORIGINAL W32 true seven S and selected GF5 numerator, not the full GF5 R3;
- independent true symplectic-spread W34 complete f,g from JPKC-001.

Finite fixtures: original W32 lex/reverse/S68/S72; true original W34 lex/random; TRUE D4 W34 spread stress. No general s=4 seven-census is claimed. W38 direct path-pair enumeration is deliberately NOT claimed; combinatorial path budget fails closed rather than silently sampling.

**No computational result establishes a uniform all-h LOWER on S.** The only uniform asymptotic statements are J4's *necessary consequences of hypothetical small S*, derived analytically from already proved PR #394 statements.

## 5a. Exact jointly pinned full ORIGINAL blocked-collision ledger

All entries are counts of ORIENTED blocked 3-paths, or ORDERED
distinct pairs of such paths with the SAME oriented endpoints.
They are computed on ONE genuine complete pair (f,g) in each
row; no sampling per anchor and no unverified root extrapolation.

| True original map | B_G | sum b_uv(b_uv-1) | Shared internal Theta_BB | Improper C6 I_BB | Proper C6 D_BB |
|---|---:|---:|---:|---:|---:|
| W32 lex | 942 | 1,872 | 880 | 912 | 80 |
| W32 reverse | 898 | 1,432 | 740 | 664 | 28 |
| W32 S68 | 606 | 512 | 196 | 316 | 0 |
| W32 S72 | 658 | 664 | 292 | 372 | 0 |
| W34 lex | 55,384 | 161,256 | 40,836 | 63,144 | 57,276 |
| W34 random(230+2) | 48,542 | 117,356 | 26,884 | 47,816 | 42,656 |

The entries in each row satisfy `sum b(b-1)=Theta_BB+I_BB+D_BB`
exactly, not just asymptotically. W32 S68 and S72 demonstrate that
**blocked-path collisions alone need not produce ANY proper D6** at
the smallest scale: both `D_BB=0` while `S=68` or `72`.
At W34 the proper term can be substantial, but the bad classes are
also of the same order. Finite observations do NOT establish their
asymptotic proportions.

The dedicated report additionally emits the independent complete
D4 Desarguesian symplectic-spread W34 witness using the `--spread`
switch, recording its true original Mf and the same exact collision
taxonomy. A positive finite CS bound does not imply a positive
universal all-h S floor.

## 6. Next mathematically justified step

The new key target is a **geometry-aware common-anchor anti-concentration/compensation** estimate, for all legal f,g:

```
Theta_BB + I_BB <= (48-eta)s^6 + Lambda*S + o(s^6),
```

for eta>0 and finite Lambda; together with J4 it would force Root A. However it may be FALSE when many other GF5 classes are positive, so first use real symplectic-spread/adversarial finite maps to seek falsifiers. An alternative is to prove that excess shared-anchor collision mass must produce some OTHER selected GF5 family; this is more plausible than unconditional little-o of each defect.

Do NOT assume `B_G=C_H`, or `Theta_BB=Theta`, or that improper cycles correspond to accepted seven GF5 sixsets. Do NOT import D6-W's three-variable conditioned dual exactness as generic fixed-rank global proof.

**Acceptance:** dedicated exact original tests on GitHub-hosted runner, INDEX, Proof Audit, Research success on final PR head, plus independent mathematical review before any merge. Issues #230/#176/#169 remain OPEN; no `main` mutation.
