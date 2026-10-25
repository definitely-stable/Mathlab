# HYP-105 #230 — AA4-CZ: an ORIGINAL collinearity-spectrum bound beats the doubled-factor bad-path mass

**Scientific DRAFT.** Strict child of [AA4-CY #625](https://github.com/definitely-stable/Mathlab/pull/625) at exact frozen parent `f3ff921eeca572234450cda68e45e97090018c06`. Prerequisites [AA4-CW #623](https://github.com/definitely-stable/Mathlab/pull/623) original raw-spoke first moment, [AA4-CX #624](https://github.com/definitely-stable/Mathlab/pull/624) per-anchor source spectral cap and doubled physical factors, [AA4-CY #625](https://github.com/definitely-stable/Mathlab/pull/625) original raw-spoke Frobenius second moment. No accepted historical seven-GF(5) registry or main changes; true ORIGINAL immutable incidence IDs and one complete correlated global f/g retained.

## 1. Mathematical decision: exploit ORIGINAL source collinearity to beat the s^(11/2) bad-path barrier

AA4-CY proved for every dyadic h>=24 and arbitrary globally injected original factor maps that, in every pair of physical halfcuts X,Y, the first and second moments of REAL ORIGINAL **raw spoke-crossing** source-incidence matrix C are

```
V=(s+1)(s²+1), d=s+1, a=min{b:binom(b,2)>=V}, k=floor(a/2);
T=∑_(p,l) C[p,l] >= d V k²/512;
Q=∑_(p,l) C[p,l]² <=64 s V k³.             [CY]
```

For a genuinely original nonincident source point p/line l let p--l0--q--l be the UNIQUE three-original-incidence-ID P3. Such an anchor is physically DOUBLE-DISJOINT when the ORIGINAL factor pair labels satisfy f(p)∩f(q)=∅ and g(l)∩g(l0)=∅. AA4-CX's elementary geometric upper on bad anchors was O(s^(11/2)); combined with CY's Q, that left T_bad=O(s⁷), exactly the exponent of total lower T=Ω(s⁷).

**AA4-CZ introduces a new project-specific use of the KNOWN TRUE ORIGINAL point/dual collinearity graph singular spectrum:** all bad original nonincident anchors together are only **O(s⁵)**, not O(s^(11/2)), for every complete correlated f,g. Thus the very same global second moment now beats lost bad-anchor mass, and **provably guarantees a uniform positive RAW true-original source-incidence mass on physically double-disjoint nonincident anchors** for ALL dyadic h>=60. THIS DOES NOT FORCE a SAFE-spoke SOURCE flag, occupied C4 or full original 3×3 perfect matching.

## 2. Theorem AA4-CZ.1 — all-h bad-source-path bound via original collinearity stars

Let s=2^h, h>=1, W(3,s) genuine ORIGINAL symplectic GQ, V original POINT factors and V LINE factors, original incidence degree d=s+1. Let f be ANY complete injective assignment of actual original point-factor IDs to pair-images in physical K_a, and g the same on actual original LINE factors, arbitrary correlation. Each image uses TWO physical coordinates; each physical coordinate u belongs to at most a−1 image pairs because each typed mapping is injective.

Define the original POINT collinearity graph A_P (p≠q, p/q incident with some same **true original** LINE), and the ORIGINAL LINE intersection graph A_L (dual). Both are strongly regular for GQ(s,s), with

```
source vertices V=(s+1)(s²+1),
source degree t=s(s+1)=s d,
source nontrivial eigenvalues s−1 and −s−1.
||A_P−(t/V)J||op=||A_L−(t/V)J||op=s+1=d.     (CZ.1)
```

This is a CLASSICAL original GQ spectrum, not newly established. For every physical coordinate u define the ACTUAL ORIGINAL factor star S_u^f={p genuine original POINT: u∈f(p)}, and similarly S_u^g on the dual ORIGINAL LINE factors. Because one full global injective map f is used everywhere,

```
|S_u^f| <= a−1,
∑_u |S_u^f| = 2V,
∑_u |S_u^f|² <= 2V(a−1),                 (CZ.2)
```

and identically on g. By (CZ.1), the number of ORIENTED true original collinear pairs inside any physical coordinate star satisfies, with x=1_{S_u},

```
xᵀ A_P x <= (t/V)|S_u|²+d|S_u|.
```

Every distinct original source point pair (p,q) with p,q TRUE ORIGINAL collinear **and** physical images overlapping f(p)∩f(q)≠∅ belongs to EXACTLY ONE physical coordinate star, because two DISTINCT occupied physical pairs in K_a cannot share two endpoints. Summing over u in the FIXED map yields

```
B_POINT(f)
 :=#{(p,q) oriented TRUE ORIGINAL collinear p≠q :
      f(p)∩f(q)≠∅}
 <= (t/V)*2V(a−1)+2dV
 =2d[s(a−1)+V].                         (CZ.3)
```

The exact same upper holds for B_LINE(g) on the TRUE ORIGINAL DUAL GQ line-intersection graph.

**Genuine GQ projection conversion (EXACT source geometry):** For each true original collinear ordered point pair (p,q), there exists a unique true original line l0 through p,q. There are exactly **s** other TRUE original lines l through q (excluding l0); p not incident with each, and its unique source 3flag path p--l0--q--l projects to q. Conversely, every genuine nonincident original (p,l) with f(p)∩f(q(p,l))≠∅ arises uniquely this way. Thus

```
#FULL true ORIGINAL nonincident LEFT-bad source anchors
  =s B_POINT(f);
#FULL true ORIGINAL nonincident RIGHT-bad source anchors
  =s B_LINE(g).                         (CZ.4)
```

The dual identity in second line uses oriented TRUE ORIGINAL intersecting lines (l,l0) and exactly s genuine original source points p on l0 outside l. Any physical halfcut has at most this many bad anchors. Without an assumption of independence, union bound gives

```
N_bad(X,Y;f,g)
 <=s [ B_POINT(f)+B_LINE(g) ]
 <=4s d [V+s(a−1)].                     (CZ.5)
```

Because for all dyadic s>=16 the minimal physical alphabet satisfies a−2<1.5s^(3/2) (proved in AA4-CS), s(a−1)<=V. Hence

```
N_bad(X,Y;f,g) <=8s d V=O(s⁵).         (CZ.6)
```

All original point IDs, line IDs and path-incidence IDs are immutable. The physical coordinate stars merely SELECT real original factors; they are not synthetic original SOURCE geometry.

## 3. New all-h DOUBLE-DISJOINT original RAW source mass theorem (h>=60)

**Theorem AA4-CZ.2.** For every h>=60, s=2^h, genuine W(3,s), every globally complete pair f,g of typed injective original factor maps into minimal K_a with ANY correlation, and every two physical halfcoordinate cuts X,Y with |X|=|Y|=k=floor(a/2), let G_XY be the TRUE ORIGINAL nonincident cut anchors (p,l) whose unique original P3 p--l0--q--l has both physical disjointness gates f(p)∩f(q)=∅ and g(l)∩g(l0)=∅. Then

```
∑_((p,l)∈G_XY) C[p,l] >= (d V k²)/2048.                    (CZ.7)

#{(p,l)∈G_XY : C[p,l]>0}
 >= (d² V k)/(2^28 s)
 > s^(11/2)/2^29.                                           (CZ.8)
```

Here C[p,l] is the exact AA4-CW/CY RAW count of TRUE ORIGINAL incidence flags between REAL ORIGINAL factor IDs with images touching f(p) and g(l) **inside the two physical cuts**; it does NOT include the critical AA4-CR removal of source spoke factors with image intersecting f(q)/g(l0), nor occupied C4 centers or three distinct extra SOURCE matching flags.

**Proof: bad mass by the same original second moment, now a strictly smaller support.** The 0/1 bad mask B=1 on source nonincident physical bad anchors, 0 elsewhere, has support size <=8sdV by CZ.6. Using Cauchy–Schwarz on finite ORIGINAL source anchor entries (nonnegative integer values),

```
T_bad:=∑_(bad original nonincident cut paths) C[p,l]
 <= sqrt(N_bad * Q)
 <= sqrt((8sdV)(64sVk³)).
```

Parent CY's exact first-moment bound T>=dVk²/512. Therefore

```
(T_bad/T)²
 <= (8sdV)(64sVk³) / (dVk²/512)²
 = 2^27 s²/(d k).                                         (CZ.9)
```

For h>=60, the minimal K_a satisfies k>0.5s^(3/2), d>=s, so d k >0.5s^(5/2)>=2^29 s². Thus CZ.9 gives T_bad<=T/2. **This is the new formerly blocked transfer gate** for the actual source double-disjoint condition.

**Remove source INCIDENT endpoint pairs separately.** AA4-CX independently proves for all h>=24 that every original cut C[p,l]<4s² (again from true ORIGINAL bipartite GQ singular spectrum). At most Vd endpoint pairs (p,l) are TRUE ORIGINAL INCIDENT (cannot be 3flag simple path), hence their total first-moment contribution

```
T_incident <=4s² Vd <=T/4                           (CZ.10)
```

once k²>=8192s². This holds analytically for all h>=60 because k>0.5s^(3/2) and s>=2^60.

The three disjoint categories of original cut endpoints are original incident, genuine original nonincident physically bad, and genuine original nonincident physically DOUBLE-DISJOINT. So by CZ.9/CZ.10

```
T_good :=∑_(G_XY) C[p,l]
   =T−T_bad−T_incident
   >=T/4>=d V k²/2048.
```

Finally Cauchy–Schwarz on good support and parent global Q bound gives

```
#{G_XY with positive RAW genuine original incidence}
 >=T_good²/Q
 >= (d² V k)/(2^28 s).
```

Since V>s³, k>0.5s^(3/2) and d>=s, this is STRICTLY >s^(11/2)/2^29. Every quantified map/cut is fixed globally; NO random independence of ORIGINAL f,g.

**Large-h threshold:** h>=60 is deliberately nonoptimal but ANALYTIC. At s>=2^60, k>0.5s^(3/2) gives d k>2^29 s² and k²>8192 s²; both inequalities monotonically persist for larger dyadic h. Exact h1..75 integer checks are merely falsifiers. Neither theorem rests on a finite high-h genuine GQ enumeration, which would be infeasible.

## 4. Independent true ORIGINAL finite oracles and falsification plan

**Source module** `research/hyp105_issue230_d6aa4cz_collinearity_badpath_mass.py` provides exact h arithmetic and, on genuine W32/W34/W38 original fixtures, independently enumerates original source collinear pairs by true source flags, their physical pair-coordinate overlaps, every cut TRUE ORIGINAL nonincident unique source 3flag P3 and physical doubled-overlap bad flags, plus actual true-original raw C[p,l] mass partition (incident/bad/good) via a separately oriented original source-flag-first pushforward.

**Independent test module** `research/test_hyp105_issue230_d6aa4cz_collinearity_badpath_mass.py` reconstructs original collinearity another way: for EVERY physical coordinate star S_u, directly checks true ORIGINAL point/dual-line collinearity and exact spectral star edge bound, summing the star original source counts. On full genuine W32/W34, it also enumerates EVERY ORIGINAL nonincident (p,l) source P3 independent of source pair physical star counting and verifies exact identities `#LEFT_BAD=s*B_POINT`, `#RIGHT_BAD=s*B_LINE`; genuine W32 lex/S72 and W34/W38 lex/random complete original global maps are independently checked in separate physical halfcuts. For W32, another oracle loops ORIGINAL immutable source flag IDs for EACH original nonincident endpoint and checks bad/raw/good mass partition exactly. The tests use exact integer h1..75 all-h parameter gates with explicit h59/h60 boundary and malformed maps/cuts fail-closed.

**Prior art boundaries:** the GQ point/dual collinearity strongly regular spectrum is classical ([Brouwer–Haemers, *Spectra of Graphs*, Theorem 9.6.2](https://aeb.win.tue.nl/2WF02/spectra.pdf)); also discussed in [Spiro et al., *Incidence-free sets and edge domination in incidence graphs*, Journal of Combinatorial Designs, 2024](https://doi.org/10.1002/jcd.21925). It is not a new universal collinearity spectral theorem. The **new scoped research contribution** is its use together with the actual physically injected original factor coordinate stars and exact original GQ projection to improve adversarial double-physical-bad-anchor upper exponent from 11/2 to 5 and obtain an all-h, every-map, every-cut positive true-original **RAW** source-incidence guarantee on genuinely DOUBLE-DISJOINT original P3s. That is a genuine positive transfer beyond AA4-CY's all-raw stage, but it does NOT solve the project GF5 question.

## 5. Absolutely mandatory non-implications and next true original matching gate

CZ.7 and CZ.8 survive BOTH **anchor-level** conditions f(p)∩f(q)=∅ and g(l)∩g(l0)=∅ of AA4-CR. They do **not** guarantee that a RAW source spoke-crossing original incidence flag (i,j) survives deletion of source factors whose physical images intersect f(q),g(l0). The at-most-4-spokes-per-side deletion can remove up to 8d actual ORIGINAL flags on any source anchor (AA4-CX). Worst-case summing 8d over ≍V² original good cut endpoint pairs is O(s⁷), the SAME order as lower CZ.7, and may erase the guaranteed mass. Even a SAFE crossing original original flag between occupied spokes does not ensure that both distinct additional physical C4 central edges are occupied, much less two more immutable original incidence flags completing an original 3×3 perfect matching. AA4-CV's infinite actual-original local zero-matchings remain compatible with the many-anchor RAW surviving theorem.

In particular **nothing here proves** an original accepted positive historical B/B-overlap sixflag, universal U_BBo or whole sevenclass S_s(f,g)=Ω(s⁶), root Branch A/B/C, strict R3 or ASET exponent. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`; #626 scientific Draft must await exact PR HEAD GitHub-hosted checks, independent qualified mathematical review and ancestor acceptance. Next **AA4-DA**: use genuine ORIGINAL source geometry to control the correlated raw→SAFE spoke-mass loss and actual physical C4 centers across many anchors, or rigorously prove original all-seven GF5 compensation with one fixed f,g. Do not repeatedly reapply generic norm bounds without a new transfer invariant.
