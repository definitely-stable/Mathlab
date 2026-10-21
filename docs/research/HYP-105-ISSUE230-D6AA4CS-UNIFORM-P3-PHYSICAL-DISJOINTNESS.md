# HYP-105 / issue #230 — AA4-CS: uniform all-h true-original PHYSICAL disjointness of macro GQ threepaths

**Scientific Draft**, strict child of [AA4-CR #618](https://github.com/definitely-stable/Mathlab/pull/618) at exact parent `299d940b24960f6e54f1318562035afdf5f8a67f`. Research-only additive theorem, independent true-original source GQ oracle, tests and GitHub-hosted workflow. No changes to main, accepted historical seven GF5 classes, R3 weights or root disposition.

## 1. Real scientific gap and precise goal

AA4-CQ/#617 gives `T(X,Y) >= V²/128 > s^6/128` genuine ORIGINAL source 3paths per two arbitrary half-physical-coordinate cuts X,Y for all s=2^h >=8 under EVERY correlated complete globally injected original typed factor map f,g. AA4-CR/#618 shows that to create an accepted true original B/B-overlap six-incidence motif from a unique source 3path `p--l0--q--l`, we need first
`f(p)∩f(q)=∅` and `g(l)∩g(l0)=∅`, followed by TWO occupied physical C4 completions and ONE true original GQ 3×3 incidence perfect matching.

**NEW AA4-CS theorem proves BOTH preliminary physical disjointness conditions hold for Omega(s^6) REAL ORIGINAL 3paths in EVERY halfcoordinate cut at all sufficiently large h**, with a fully explicit threshold `h>=14` and constant `1/128`; no independence assumption between f,g or between original source paths. Hence *physical pair intersection*, the first of three gates in #618, cannot erase the macroscopic original threepath reservoir asymptotically. Crucially this does NOT prove even one true original sixflag satisfies either remaining occupied-C4/permanent test, and gives NO root A/B/C closure.

## 2. Exact theorem (all complete correlated original f,g)

Let s=2^h, V=(s+1)(s²+1), a=min integer with C(a,2)>=V, k=floor(a/2), physical holes H=C(a,2)-V, and
`m=C(k,2)-H`. For ANY typed global complete injections f from ALL genuine original POINT factors into unordered physical K_a pairs and g from ALL genuine original LINE factors into the SAME physical alphabet, with arbitrary correlations; for ANY X,Y subsets [a] with |X|=|Y|=k, define

```
P_X={p: f(p) entirely contained in X},  L_Y={l: g(l) entirely in Y},
x=|P_X|, y=|L_Y|,
T = number of TRUE original NONINCIDENT pairs (p,l)∈P_X×L_Y.
```

By the GQ axiom, every such (p,l) gives a UNIQUE original path `p--l0--q--l`, with three different original incidence-ID flags. Define the genuinely physical-double-disjoint path count

```
A(X,Y;f,g) = # {(p,l) NONINCIDENT in P_X×L_Y:
                  f(p)∩f(q)=∅  and  g(l)∩g(l0)=∅}.
```

For **EVERY h>=1** (even when the below numerical lower is vacuous), with d=s+1 and c=2(a-2)s, we have the exact one-sided original-point/line bad-path bounds:

```
  bad_f <= c*x,  bad_g <= c*y,
  T=xy-e_G(P_X,L_Y),   e_G(P_X,L_Y)<=d min(x,y),
  A=T-bad_f-bad_g+bad_both,
  A>=xy-d min(x,y)-c(x+y).
```

**PROOF of the important bound, no probabilistic argument:**

Fix original POINT source factor p. Other original POINT factors q whose globally unique physical pair image f(q) meets f(p) correspond to other physical K_a edges incident to at least one endpoint of the 2-edge f(p). There are EXACTLY `2(a-2)` such **other** K_a pair-edges (a-2 at each physical endpoint), regardless of the physical holes, so global injectivity allows at most that many bad q. For each q≠p collinear with p, GQ partial linearity allows at most one common true source LINE factor l0. There are exactly s other true original LINE factors l through q besides l0 (if no common line, there are none). For all these l, p and l are nonincident: otherwise a second common line of p,q would violate GQ partial linearity. Each pair (p,l) has the UNIQUE middle q by the GQ nonincident axiom. Thus, at most `2(a-2)*s` TRUE original nonincident p-to-l source 3paths can violate `f(p)∩f(q)=∅` per fixed p, independent of which l lie in L_Y. Sum over p∈P_X: `bad_f <=2(a-2)s*x`.

The SOURCE DUAL argument fixes original LINE l, counts other original LINE factors l0 whose globally unique g(l0) physical pair image meets g(l), at most 2(a-2). If l,l0 meet in one genuine original SOURCE POINT q, each original l0 has exactly s other real source POINT factors p besides q. Again these are nonincident with l by GQ partial linearity. Hence `bad_g<=2(a-2)s*y`. Both estimates remain valid even for fully adversarially correlated f and g. Finally union inclusion–exclusion of literal TRUE original source endpoints gives the exact A identity and lower.

### Explicit uniform large-h bound, constant and proof

From #617's already proved minimal-alphabet hole bound, for s>=8, `x,y>=m>=V/8`. We now show for every dyadic `s>=2^14=16384` that

```
  m >= 2(s+1) + 8(a-2)s = 2d +4c.
```

This is a fully symbolic inequality, NOT interpolation of finite W32/W34/W38 counts:

1. For s>=16, `V=s³+s²+s+1 <=(9/8)s³`. Minimality of a gives `C(a-1,2)<V`, hence `(a-1)(a-2)<2V<=(9/4)s³`. Since `(a-2)^2<(a-1)(a-2)`, we have `a-2 < (3/2)s^(3/2)`.
2. For s>=2^14, `sqrt(s)>=128`. Therefore `m>=V/8>=s³/8>=16s^(5/2)`, whereas `2d+4c=2(s+1)+8(a-2)s <2(s+1)+12s^(5/2) <=16s^(5/2)`, with the final inequality from `2(s+1)<=4s^(5/2)` (all s>=1). Thus `m>=2d+4c`.
3. With x,y>=m, divide total upper failure estimate by xy:
```
 (d*min(x,y)+c*(x+y))/(xy)
     =d/max(x,y)+c/x+c/y
     <=(d+2c)/m <= 1/2.
```
So `A>=xy/2 >=m²/2>=V²/128>s^6/128`.

**ALL-h physical-disjoint original threepath theorem**:

```
  FOR ALL dyadic s=2^h with h>=14,
  FOR ALL genuine original W(3,s),
  FOR ALL complete globally injected arbitrary correlated typed f,g,
  FOR ALL physical halfcoordinate X,Y:
      A(X,Y;f,g) >= |P_X|*|L_Y|/2
                 >= V²/128
                 >  s^6/128.
```

In fact `A/(xy)>=1-(d+2c)/m=1-O(s^(-1/2))`. Thus almost all SOURCE nonincident cut endpoint pairs eventually pass BOTH physical disjointness preconditions (the original incidence pairs themselves form only fraction O(s^-2)), independently of adversarial f,g correlation. Again, these are ORIGINAL THREE-flag paths, NOT accepted sixflag GF5 class contributions.

The explicit h>=14 is conservative: finite exact integer checks show the simple sufficient condition m>=2d+4c starts already at h=11, but that finite observation is NOT extended to all higher h by fiat. The mathematically proved universal range used for conclusions is h>=14 only.

## 3. Direct root-level separation from B/B historical GF5 positivity

For each physically disjoint original path, AA4-CR defines `Phi_f,g(p,l)` as the exact number of pairs of occupied real physical C4 source completions yielding a TRUE ORIGINAL 3×3 point-line perfect matching. The full historic accepted `U_BB_overlap(f,g)` is the sum of these nonnegative integers over all original nonincident (p,l), while all source paths with an intersecting required physical edge necessarily have Phi=0.

AA4-CS guarantees macroscopic **NONVACUOUS ANCHORS**, not positive `Phi`. The remaining exact all-h root gap is:

```
 for all large dyadic s and all correlated full original f,g:
   is sum_(p,l physically disjoint in P_X×L_Y) Phi_f,g(p,l)
      bounded below by eta * A(X,Y;f,g) for some eta>0 ?
```

If so (a SUFFICIENT, not necessary root condition), `S_s(f,g)>=U_BB_overlap(X,Y;f,g)>=eta*A>eta*s^6/128` would close Branch A. No such eta is shown. Alternatively the OTHER SIX historical seven-GF5 accepted original classes could compensate failing per(B)=0, but there is no demonstrated crossclass fixed-map positive inequality. **The unconditional conclusion of this PR ends at THREE ORIGINAL incidence flags**: no root A/B/C, no full R3, no ASET exponent.

## 3a. Frozen authentic original model cut falsifiers, no asymptotic extrapolation

On each row below, complete globally injected arbitrary correlated typed original f,g are fixed for the entire test. The true source Q object is the UNIQUE THREE-incidence path `p--l0--q--l`, not a synthetic path and not an accepted GF5 sixflag. The first physical halfcut uses X={0,...,k-1}, Y={a-k,...,a-1}, with k=floor(a/2). All results were checked by two INDEPENDENT GQ source traversals: POINT-first `p--l0--q--l` and LINE-first `l--q--l0--p`, and match previous #617 genuine source `macro_path_cut` path counts EXACTLY.

| True original symplectic host & full typed maps | Original nonincident source P3 T | Original P3 passing BOTH physical disjointness A | Failed f(p)/f(q) condition | Failed g(l)/g(l0) condition | Failed BOTH, counted twice |
| --- | ---: | ---: | ---: | ---: | ---: |
| W(3,2) lex | 8 | 1 | 4 | 6 | 3 |
| W(3,2) S72 | 7 | **0** | 6 | 4 | 3 |
| W(3,4) lex | 299 | 123 | 96 | 106 | 26 |
| W(3,4) random | 379 | 209 | 84 | 106 | 20 |
| W(3,8) lex | 16,893 | **12,358** | 2,318 | 2,461 | 244 |
| W(3,8) random | 17,415 | **13,832** | 1,904 | 1,895 | 216 |

Every row obeys exactly `A=T-bad_f-bad_g+bad_both`, including the finite **zero** for W32 S72. This is consistent with (and does not challenge) the asymptotic threshold h>=14. For W38 lex first cut, e.g. `16893-2318-2461+244=12358`: this is the real source GQ count of P3 paths with both physical disjoint edges and **not** a count of historical sixflag GF5-positive B/B-overlap Q.

For the *finite integer arithmetic regression* `h=14, s=16,384`, exact minimal physical parameters are `a=2,965,912`, `m=1,099,577,957,519`, and `2(s+1)+8(a-2)s=388,747,788,290`; thus `m` exceeds the sufficient threshold. These numbers are a unit-test sample of the preceding **symbolic proof**, not its foundation. The proof itself applies to every dyadic h>=14 with no upper bound.

## 4. Exact ORIGINAL source finite independent validation

The exact Python source-model oracle reads real source W(3,2), W(3,4), W(3,8) (15/85/585 true original typed factor IDs, full 45/425/5265 true source flags), verifies the two global complete physical pair injections, and for FOUR full globally fixed half-coordinate cut pairs on each of two independently built source maps (W32 lex/S72; W34 lex/random; W38 lex/random) independently counts every genuine nonincident true original p,l and resolves its UNIQUE middle (q,l0). It records exact left-only/right-only/both physical intersection failures and both physically disjoint actual original P3 survivors. Its exact path count is compared to the PREEXISTING #617 macro-path-cut source certificate and the independent GQ original LINE-first (l→q→l0→p) source traversal, not just arithmetic bounds. For every cut it checks `A=T-bad_f-bad_g+bad_both`, both one-sided bad caps, original type injection, and the min-alphabet source occupancy certificate. h1/h2/h3 finite GQ runs do NOT pretend to meet the h>=14 universal threshold.

A separate pure-integer arithmetic checker validates m,V,a,H and inequality from h=1 to h=26 including h>=14; this is a regression only: the symbolic proof is above. Malformed original global typed maps or incidence flags, repeated/out-of-range coordinate cuts, and h<1 fail closed. GitHub-hosted CI tests W32/W34/W38 separately, plus arithmetic and invalid-input gates.

Classical sources: the original GQ nonincident-point-to-line unique length-three path, regular incidence degree and C4-freeness are standard finite geometry; compare the GQ axioms in https://www.sciencedirect.com/topics/mathematics/strongly-regular-graph and the GQ incidence graph girth-eight characterization in https://en.wikipedia.org/wiki/Generalized_quadrangle. New scoped content here is the explicit `2(a-2)s` per-endpoint **correlated-global-physical-label bad-path bound**, its simultaneous typed union and uniform dyadic h>=14 macro-scale physical disjointness consequence for HYP-105. No novel general GQ axiom is claimed.

**Scientific acceptance gate:** research Draft only. Must pass exact HEAD dedicated source tests, INDEX, Proof Audit, full Research workflow and qualified independent mathematical referee plus stacked ancestor acceptance. Previous parent #618 generic Research was CANCELLED despite dedicated/INDEX/Proof Audit success. No main merge and root #230 disposition unchanged.

**Next AA4-CT:** Quantify occupied physical C4 source completion totals AND actual original GQ triple permanent after restricting to guaranteed physically disjoint source P3; disprove a universal eta if necessary, or derive a fixed-map all-seven compensation inequality. A physical-disjoint 3path by itself is NEVER a historic positive sixflag class.
