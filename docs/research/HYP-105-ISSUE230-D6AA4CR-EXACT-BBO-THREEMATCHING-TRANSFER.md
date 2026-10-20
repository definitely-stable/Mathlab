# HYP-105 / #230 — AA4-CR: exact original 3-path-to-historical-B/B-overlap physical transfer by two C4 completions and one 3×3 permanent

**Scientific Draft**, strict child of [AA4-CQ PR #617](https://github.com/definitely-stable/Mathlab/pull/617), parent pinned `eccf7948b10e57c579fb47608f21c59e3c17a0bf`. No changes to main, accepted historical seven-class GF5 registry, root #230 acceptance, or ancestor branches.

## 1. Decisive missing mechanism after AA4-CQ

#617 proved an all-h (h>=3) lower of >s^18/6144 on SOURCE-ONLY six-distinct-incidence-ID B/B-overlap forests anchored in arbitrary complete physical halfcoordinate cuts. The historical seven-GF5 B/B-overlap class, however, additionally requires physical degree TWO on exactly SIX physical coordinates on BOTH sides for the SAME six actual ORIGINAL source incidence flags. #617 found true original W32 half-cuts with tens of thousands of source forests and ZERO physical positive B/B-overlap. No unconditional positive transfer was proved.

Rather than introduce an unjustified random acceptance probability, AA4-CR resolves the source-to-physical transfer **exactly** for ONE of the seven positive classes in terms of a finite, fully original and physically constrained matching functional. This formula has arbitrary correlated complete typed maps f,g and all dyadic h as genuine mathematical quantifiers. It is an exact oracle/reduction for the historical B/B-overlap *summand*, NOT an equivalent C reduction for the WHOLE root #230 count S and NOT a positive lower.

## 2. All-h exact physical characterization of the historical B/B-overlap class

Fix s=2^h, h>=1, the authentic symplectic GQ W(3,s), its V=(s+1)(s²+1) ORIGINAL POINT and LINE factor IDs, and ONE pair of arbitrary complete globally injected original pair-label maps f(p), g(l) into the SAME minimal physical alphabet K_a. Maps may be arbitrarily correlated.

A TRUE original SIX-DISTINCT-incidence-ID set Q is of source type B/B-overlap iff it has exactly one doubled ORIGINAL POINT factor q, one doubled ORIGINAL LINE factor l0, their repeated-factor intersection is a true ORIGINAL incidence flag (q,l0), and the other two flags touching q and l0 are respectively (q,l) and (p,l0), with THREE remaining source-isolated singleton actual flags (p_i,l_i), i=1,2,3. The connected original incidence path component is

```text
(p,l0) — (q,l0) — (q,l)
    original incidence graph: p -- l0 -- q -- l
```

Here p,l are NONINCIDENT genuine original endpoint factor IDs: if (p,l) were also a true flag, the original GQ would contain a forbidden source C4. Every such Q has a UNIQUE path component, and the unique original GQ axiom gives EXACTLY one such 3path for every nonincident original (p,l). Thus accepted B/B-overlap Q are partitioned **without multiplicity** by original p-to-l nonincidence endpoint pairs.

Given this fixed genuine original threeflag path p--l0--q--l, define e=f(p), d=f(q), r=g(l), t=g(l0), each a physical simple pair edge. The physical LEFT source pattern B contains f(q) twice and f(p) once; the physical RIGHT source pattern B contains g(l0) twice and g(l) once.

**Necessary and sufficient physical conditions:**

1. e and d share NO physical coordinate, and r and t share NO coordinate. A doubly used physical pair edge contributes physical coordinate degree2 at its two endpoints, so any other selected edge touching one of them would violate degree2.
2. The other THREE distinct singleton POINT factor images, together with physical edge e=f(p), must be exactly a simple physical C4 on four coordinates disjoint from d=f(q). The analogous other THREE singleton LINE images, together with r=g(l), must be exactly a C4 on four coordinates disjoint from t=g(l0).
3. The chosen three actual source POINT factor IDs P=(p1,p2,p3) and three actual source LINE factor IDs L=(l1,l2,l3) must admit a perfect matching through TRUE ORIGINAL GQ incidence flags (p_i,l_{pi(i)}). Those are the three remaining immutable ORIGINAL source flags. No independent f/g redraw or synthetic edge.
4. Every such choice of two physical C4 completions and a matching produces a six-distinct-original-incidence set whose historic accepted sevenGF5 class tag is precisely B/B-overlap. Conversely every historic B/B-overlap Q yields EXACTLY one anchor, LEFT C4, RIGHT C4 and true source matching.

The physical C4 list is elementary. When e={u,v}, d={x,y} are disjoint, choose any two distinct fresh coordinates {z,w} outside e∪d, then the THREE additional C4 edges are either {(u,z),(z,w),(w,v)} or {(u,w),(w,z),(z,v)}. Retain the C4 only if EVERY required edge is occupied in the ONE existing f map (and decode each via its exact inverse source factor). Thus there are at most `2*binom(a-4,2)` left C4 source triples at this anchor, and independently at most that many right C4 source triples for the fixed g. Missing physical pair labels are handled EXACTLY, never filled by invented original source vertices.

## 3. NEW exact 3×3 permanent/uniqueness lemma

For source triples P,L obtained from these two physically compatible completions, define the TRUE original GQ incidence submatrix

```text
B_ij = 1_{(p_i,l_j) is a REAL ORIGINAL incidence flag}, i,j=1,2,3.
```

Then `per(B)=sum_(pi in S3) prod_i B_i,pi(i)` is always either 0 or 1.

**Proof:** Two distinct source perfect matchings on exactly 3 POINT source factors and 3 LINE source factors have a nonempty symmetric difference whose components are alternating cycles of length 4 or 6. The incidence graph of an actual generalized quadrangle has girth EIGHT, so neither cycle can occur. Hence at most ONE perfect matching exists. This is the classical alternating-cycle matching argument combined with the classical genuine-GQ girth8 property, not a new general perfect-matching theorem.

**Exact all-h historical count identity:**

Let A range over every TRUE original nonincident original (p,l) pair; reconstruct its unique actual original 3path and define `C_f(A)` / `C_g(A)` as the occupied physical LEFT/RIGHT C4 completion source triples above. For each C4-pair (P,L), let B(P,L) be the literal TRUE source 3×3 incidence matrix. Then

```text
  U_BB-overlap(f,g)
    = Σ_(p,l) true nonincident original
        1_{f(p)∩f(q)=∅} 1_{g(l)∩g(l0)=∅}
        Σ_(P∈C_f(p,q)) Σ_(L∈C_g(l,l0)) per(B(P,L)),
  with per(B(P,L))∈{0,1} exactly.
```

The sum is over the SAME immutable complete globally injected typed original f,g throughout. Every summand is an ACTUAL original six-ID Q, counted ONCE via its unique SOURCE path. No source-only physical surrogate enters the result; exact historical accepted GF5 necessary numerator for this class alone is `51750 * U_BB-overlap`.

A simple consequent all-h **upper** (NOT lower) bound:

```text
  U_BB-overlap(f,g)
      <= (# actual original nonincident p,l)
         * 4*binom(a-4,2)^2
      <= V(V-(s+1)) * 4*binom(a-4,2)^2.
```

For a halfcoordinate cut X,Y, replace the anchor sum by TRUE original nonincident pairs with f(p)⊆X and g(l)⊆Y; this EXACTLY counts that cut's historically accepted B/B-overlap Q whose UNIQUE original source 3path endpoint pair lies in the cut. It may be ZERO, including when #617 guarantees many source-only original six-ID forests. **The core root barrier now lies in forcing positive 3×3 permanents across these coupled physical completions, not in merely counting original forests.**

## 4. Implementation, scientific evidence and independent oracles

File `research/hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer.py`: validates the TRUE complete original W3 incidence host and entire typed f,g, gets the ACTUAL unique original threepath per chosen genuine nonincident (p,l), enumerates occupied C4 completions on both complete physical factor maps, calculates exact at-most-one source 3×3 permanent, creates actual six original flag ID sets, and checks the unchanged HISTORICAL accepted sevenGF5 classifier returns B/B-overlap. Duplicate Q or >1 matching causes a hard failure. Supports ALL nonincident anchors for W32, selected endpoints/cuts for W34/W38; no claim of cheap full all-h runtime.

Independent exact W32 referee: enumerate **EVERY** true original nonincident anchor on two independently globally complete original W32 f,g schemes (`lex` and `S72`), compare not just totals but the ACTUAL SET of accepted original six incidence ID Q against prior complete LEFT-first `seven_census(..., witness_sets=True)`. Also transpose the FULL ORIGINAL GQ POINT/LINE incidence sides, exchange complete original f,g while keeping six true incidence ID positions fixed, and independently check exact Q set invariance. This is strictly stronger than comparing class totals.

Half-cut countercontrol: for actual true original W32 complete fixed maps, cuts X={0,1,2}, Y={3,4,5} yield 8 genuine nonincident anchors in lex, 7 in S72, i.e. 40,448 and 35,392 true original source BBo sixflag forests, but the physical matching transfer count is 0 for BOTH, agreeing with independently established #617 finite original physical GF5 tags. This clearly disproves an unjustified universal all-h>=1 transfer fraction, not a proposed large-h statement.

Independent higher-h finite scoped tests: true W34 lex/random with 72 genuine original nonincident anchors each (all other true ORIGINAL incidence IDs/map factors held fixed), real W38 lex with one true original anchor, compare accepted Q ID sets across COMPLETE source POINT↔LINE transpose for the same anchor endpoints reversed, independently retag accepted real Q under original historical GF5 classifier; prohibit converting a limited-anchor sample into a full global W34 or W38 U count. All-h mathematical equivalence is proven algebraically from GQ axioms and physical C4 uniqueness, not by extrapolating these finite samples.

## 4a. Frozen exact-head original symplectic GQ acceptance evidence

This entire table refers to **REAL immutable original six-incidence-ID Q**, global typed full f,g fixed per row. For W32, the new exact physical two-C4/3×3 permanent oracle was compared to the entire accepted B/B-overlap **SET** of original Q from the independent LEFT-first historical seven-GF5 classifier. For both W34 rows, the algorithm exhausts ALL 6,800 TRUE original nonincident point-line pairs, all occupied physical two-C4 choices, and every real original 3×3 permanent; each entire class count agrees exactly with the independent prior AA4-CP full original W34 seven-GF5 right-first C++ join.

| Real ORIGINAL symplectic GQ / complete full maps | True source nonincident 3paths | Anchors physically disjoint BOTH sides | C4 completion pairs tested | Permanent=0 | Permanent=1 and historical accepted sixflag B/B-overlap | Historical accepted GF5 necessary numerator for THIS class only |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| W(3,2) lex | 180 | 27 | 108 | 100 | **8** | **414,000** |
| W(3,2) S72 | 180 | 13 | 52 | 51 | **1** | **51,750** |
| W(3,4) lex, **entire original class** | **6,800** | 3,152 | **17,609,778** | **17,587,667** | **22,111** | **1,144,244,250** |
| W(3,4) random, **entire original class** | **6,800** | 3,597 | **19,223,325** | **19,199,157** | **24,168** | **1,250,694,000** |
| W(3,8) lex, **ONE explicitly selected nontrivial original P3 only** | 1 | 1 | **828,100** | 828,077 | **23** | **1,190,250** |

The W38 test specifically selects genuine original nonincident endpoint factors (p,l)=(0,74) with **BOTH** typed physical doubled-vs-single edge disjointness conditions satisfied. It exercises all 910 actual occupied C4 source triples on each side and 828,100 coupled original 3×3 incidence matrices; 23 real perfect matchings survive. A vacuous physically blocked anchor would not provide this check. This W38 datum MUST NOT be presented as the entire W38 original U_BBo class census.

**Independent scientific falsifiers:** entire original W32 accepted Q ID-sets equal the legacy historical seven_census B/B-overlap witness sets exactly for lex and S72; original source POINT↔LINE dual transpose produces identical true sixflag Q-ID sets on both W32 models and both 72-anchor real W34 lex/random models; W38's nontrivial selected path also preserves its accepted immutable Q IDs under full typed source dualization. No full original GF5 class-count from a physical-only surrogate is ever accepted.

### Direct quantitative next proof gate (sufficient only, NOT root equivalence)

For h>=3, AA4-CQ proved that **EVERY** global correlated complete typed f,g and EVERY two halfalphabet physical coordinate cuts X,Y contain at least T(X,Y)>s^6/128 genuine original nonincident endpoint anchors. AA4-CR now assigns each such source anchor a fixed nonnegative integer `Phi_f,g(p,l)`: the number of pairs of occupied physical C4 completions with permanent1 in the genuine original 3×3 incidence matrix. The new exact identity gives

```text
  U_BBo(X,Y;f,g)
     = sum_(p in P_X, l in L_Y, p nonincident l) Phi_f,g(p,l).
```

Therefore the **uniform conditional acceptance criterion**

```text
  for some η>0 and all sufficiently large dyadic s,
  for every legal correlated globally complete original f,g and
  for every physical halfalphabet cut X,Y:

    [sum_(p,l) Phi_f,g(p,l)] / T(X,Y) >= η
```

would IMPLY `S_s(f,g) >= U_BBo(X,Y;f,g) > (η/128)*s^6` for root Branch A. This is a much more explicit point-line-incidence-permanent question than #617's artificial-looking `c/s^12` percentage of enormous source-only matchings. **It is only SUFFICIENT, not necessary for the full sevenclass root**, since the other six accepted historical GF5 classes may force S even where a given B/B-overlap cut has zero transfer. The W32 original finite halfcut X=012/Y=345 with 8 and7 nonincident anchors but ZERO accepted B/B-overlap directly falsifies this criterion if incorrectly demanded for h=1, but does NOT refute a still-unproved h>=3 statement. NO positive η is asserted by this work.

A different valid research route is a fixed-map **all-seven compensation** bound: whenever this particular permanent sum is small, the other six historically accepted true-original source sixflag classes must dominate. That remains open as well.

## 5. Scientific limitations and next gate

Classical prior art: girth8 generalized-quadrangle incidence geometry (see [GQ incidence graph definition](https://en.wikipedia.org/wiki/Generalized_quadrangle)), and symmetric difference of perfect matchings/alternating cycles (e.g. [matching graph literature](https://www.sciencedirect.com/science/article/pii/S0304397502004966)). The new scoped HYP-105 contribution is the EXACT acceptance equivalence and the fully correlated original physical completion-to-3×3-permanent identity for one historical GF5-positive original sixflag class. This is not a novel general matching theorem or proof of root C.

**NO root A/B/C**: This work does NOT show the 3×3 permanent is positive for even one of the macro-cut anchors for every arbitrary correlated f,g. It does not establish any positive fraction c/s^12, a uniform global `S_s>=cs^6`, an infinite original `S=o(s^6)` counterfamily, or a root-equivalent exact reduction covering **ALL seven** historical GF5 classes. It also does not compute all signed GF5 events or full R3/ASET. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`.

**Best subsequent AA4-CS:** characterize under actual GQ girth8 and globally complete physical pair maps which structural configurations guarantee a 1-permanent for a coupled C4 pair, and whether the total over ALL source paths + the OTHER SIX accepted classes admits a fixed-map coercive lower. Prove a quantitative all-h lower or real infinite adversarial small-S sequence; otherwise no root-closure claim. Do NOT manufacture random independent f,g or treat source-only s^18 growth as physical GF5-positive.

Keep this independent additive scientific PR in DRAFT pending exact-head GitHub-hosted dedicated checks, INDEX/Proof Audit/Research, ancestry acceptance and a qualified independent mathematical referee. main not modified.
