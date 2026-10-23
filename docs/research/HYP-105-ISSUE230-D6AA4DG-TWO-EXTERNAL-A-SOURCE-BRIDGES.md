# HYP-105 #230 — AA4-DG: two-external-factor threshold and eight exact physical A-bridges for nonlocal historical GF(5) compensation

**Scientifically scoped theorem and source oracle — SCiENTIFIC DRAFT, NOT root A/B/C.**
Strict child of [AA4-DF #632](https://github.com/definitely-stable/Mathlab/pull/632), frozen base SHA `13cab8f0993c4c12d83c3bec13234caeaf9dcb88`. No main mutation, no historical seven-class definition change, no invented source inc ID, no independent f/g assumption.

## 1. What changed beyond AA4-DF

AA4-DF proves any actual ORIGINAL local source reservoir on EACH typed POINT/LINE side produced by genuine W(3,s) source P3 and an actually occupied physical C4 completion consists of **five different original SOURCE factor IDs**, whose physical images are a FOUR-CYCLE plus one DISJOINT doubled factor physical edge. It classifies which historical source endpoint profiles A/B/C can occur with **no outside ORIGINAL factors**, and supplies genuine W32 local Hall-failing examples with no positive historical GF5 sixflag inside the same 5+5 reservoir.

This raises a precise nonlocal scientific question: for any of the four historical accepted seven-GF5 positive classes with an A side — D6, B-left/A-right, A-left/B-right, and C/A — HOW MANY extra actual original typed source factor IDs must necessarily leave that reservoir? Can we classify all minimum-width physical ways to leave it, then check the TRUE original incidence source edge IDs without pretending physical occupancy produces original incidences? AA4-DG answers the first two questions completely for **exactly two** outside factor IDs, and implements the third for frozen actual source maps on explicit source-anchor subsets.

## 2. THEOREM DG.1 (every dyadic h>=1, every original W(3,s), all complete correlated typed maps, every actual occupied C4 and doubled original source image)

Fix one typed original source point/line full injected map, with image edges for five genuinely distinct source factors

```
original base source factor e0          = {u,v}
actual original physical C4 source triad:
   e1={u,z}, e2={z,w}, e3={w,v}
original doubled source factor d       = {x,y}
{x,y} ∩ {u,v,z,w}=∅.
```

Take ANY physically valid HISTORICAL source endpoint-profile A candidate: SIX DISTINCT ORIGINAL typed factor IDs, each SOURCE factor used ONCE in six ORIGINAL incidence flags, and the six **physical pair-images** form a 2-regular graph on exactly SIX coordinate vertices (a physical six-edge 2factor). Suppose the six factor IDs include at least FOUR of the five local source factors.

Then:

1. **Five local source factors + one outside ORIGINAL source factor is impossible.** The four-cycle already has degree 2 at its four physical coordinates. The only two unsaturated physical vertices are x,y of doubled edge; the sixth edge would have to be exactly {x,y}, ALREADY OCCUPIED by one ORIGINAL factor. Global injection forbids another source factor with the same physical image.
2. **Therefore EXACTLY four local + EXACTLY two outside ORIGINAL factor IDs are required.** Further, the four local IDs cannot be all four edges of the physical C4: with only two outside edges, a disjoint physical 2-cycle on {x,y} would be necessary but impossible in the simple K_a physical graph. Consequently they are the doubled factor {x,y} plus exactly THREE of the four C4 cycle edges.
3. Deleting the omitted C4 edge turns the three kept C4 edges into a three-edge path with exactly TWO physical degree-1 terminal vertices (say t0,t1). The doubled physical edge x-y also has exactly TWO degree-1 terminals. The two external physical pair-images MUST be one of the TWO cross perfect matchings

```
{t0,x},{t1,y}       or       {t0,y},{t1,x},
```

and each chosen physical pair edge MUST actually be occupied by a DIFFERENT ORIGINAL source factor under the SAME globally fixed typed map.
4. There are exactly FOUR choices of omitted actual original C4 edge × TWO cross matchings = **EIGHT candidate minimal nonlocal A physical completion templates**. No other physical A configuration with precisely two outside source factors exists. Because the original typed map is globally injected, each occupied physical cross-edge has exactly one genuine ORIGINAL source factor ID; the catalogue contains at most eight distinct 6-source-factor sets, with zero or more missing when a required physical pair edge is unoccupied.

All these statements are purely rigorous graph degree/exact physical-label claims, for any h and any complete original W3 typed map; NOT claims that the corresponding source six INCIDENCE flags exist between those six original factors and any chosen opposite typed source factors. True ORIGINAL source incidence is controlled by the underlying W3 graph of degree d=s+1, which is independent of *arbitrary* globally correlated physical source labels.

**Corollary DG.2 — necessary nonlocal source-factor radius for the four historical A classes:** If a 6-ID accepted historical GF5 source motif is represented using actual original source factors from such a paired original P5×L5 reservoir with at most **one external factor ID on each side**, then the original motif cannot be D6, either A/B orientation or C/A. Any original motif of these four types must use at least TWO original factors outside the local source reservoir on each typed side that carries the A profile. In particular, D6 requires >=2 outside on BOTH original POINT and LINE typed maps. An A/B or C/A source motif with EXACTLY TWO outside source factors on the A side can only use one of the eight specified original physically occupied cross-bridge templates.

**Important limitation:** An historical positive sixflag need NOT use >=4 of this specific local C4 source factors. The eight-template classification is exhaustive ONLY at the minimum two-external-factor width, not a global catalogue of every historical A positive Q in W3. A historical motif with three or more outside factors may evade the templates, and the established corollary does not prohibit it.

## 3. Proof completeness and independent source checks

The proof can be checked without source GQ specific combinatorial spectra: calculate physical coordinate degree deficit `2−deg(v)` for the chosen local five source factor physical edges. They have degree0 deficit at four C4 coordinates, and degree1 deficit at the two doubled coordinates. Adding one new physical edge cannot repair both deficits because it must coincide with the occupied doubled edge; adding two edges while retaining four local edges forces the three-edge path/doubled matching structure as above. Graph source factor injection is essential; without it a duplicated doubled physical edge could give an invalid six-factor A.

The new module `research/hyp105_issue230_d6aa4dg_two_external_A_bridge.py` validates TRUE occupied ORIGINAL physical C4 source factors, constructs each of the eight possible real physical cross-bridge templates, looks up their ORIGINAL typed source factor IDs ONLY when both physical cross edges actually belong to the full global source factor image map, and verifies that every returned 6-source-factor A candidate has EXACTLY four original local and two ORIGINAL external IDs, with a physical two-regular simple graph on six coordinates. The code never invents ORIGINAL incidence edge (i,j).

For actual original paired C4s of frozen actual original W3 source anchors, it then independently obtains immutable TRUE ORIGINAL incidence IDs `(i,j)` for each possible POINT A candidate and LINE local B/C candidate, vice versa, or BOTH source sides with A; enumerates all six distinct ORIGINAL source incidence-ID Q subsets and calls the existing authoritative full seven historical GF5 original classifier `classify_seven_all_a_original_Q`. The only accepted labels in these scenarios are D6, B-left/A-right, A-left/B-right, C/A, and all results are reported with C4-reservoir multiplicity AND distinct immutable original Q count separately. A configured cap marks the audit **PARTIAL**.

A completely independent test `research/test_hyp105_issue230_d6aa4dg_two_external_A_bridge.py` brute-forces ALL six-source-factor subsets formed from four of five occupied local edges plus any two outside ORIGINAL source factors and applies direct physical 2factor degree counting; on full K6 it independently finds EXACTLY eight templates, and no one-external A candidate. Real globally complete W32 lex/S72 and W34 lex/random source embeddings are checked against that independent brute for genuine physically occupied original C4s; W32 capped sample gets a separately ordered independent 6-SOURCE-ID original incidence historical classifier census, W34 capped first C4 pairs same, W38 lex/random only two C4 pairs and explicitly PARTIAL. Malformed C4s, injected typed map duplicates, caps and source-anchor IDs rejected.

Finite examples validate the code, not the universality of the theorem; the graph-degree argument is the ALL-h proof. The requested global AA4-DG **compensation theorem** is still OPEN: possible physical cross-edge completion does not guarantee actual source incidences needed for SIX immutable flags on BOTH typed maps, and this theorem provides no lower bound on the historical original all-seven count.

## 4. Why this is scientifically useful, without overstating it

The previous AA4-DF locally negative witness showed a single Hall-defective marked source incidence need NOT yield ANY positive original GF5 sixflag using only its 5+5 original source factor IDs. AA4-DG rules out a broad attempted repair: merely incorporating one outside source factor per typed side still cannot reach FOUR of the SEVEN classes (those containing A). A mathematically viable compensation argument for those classes MUST genuinely LEAVE the local reservoir by >=2 SOURCE original factor IDs on the A side. The exact eight physical bridge possibilities provides a bounded branching interface into a richer original source-incidence search. That is materially more discriminating than unrestricted "search all source factor 6-sets".

**Next AA4-DH:** For the same frozen f,g, count the ACTUAL original sixflag incidences on these nonlocal bridge candidate templates with multiplicity control, then either (i) prove lower bound of accepted A-side original Q from large source Hall deficits, or (ii) exhibit genuine original maps where the two-external physically occupied bridge mechanism is present but original incidences block every accepted A-side sixflag in those template sets. If compensation must extend to >=3 outside factor IDs, derive an ORIGINAL source factor expansion hierarchy with a bounded source motif reuse injection. Keep root A/B/C status open.

**Prior art boundary:** degree-deficit matching, K4 cycle path and 2factor completion are elementary graph facts. Genuine source GQ incidence properties (degree s+1, bipartite girth8) are classical; see Godsil–Royle, *Algebraic Graph Theory*, Chapter 5. What is project-specific here is the original W3 source pair-label injection, five-source-factor C4 reservoir and its exact nonlocal minimal external source budget for the seven historic GF5-positive six-incidence-ID classes. Independent qualified scientific review remains necessary before publication.

Root #230: `OPEN_WITH_FORMAL_BLOCKER`. No universal S>=cs^6, no correlated all-h low-S f/g family, no root-equivalent C reduction, no strict R3/ASET exponent. Scientific Draft, no main merge, ancestor proofs and exact-head Research/qualified referee pending.
