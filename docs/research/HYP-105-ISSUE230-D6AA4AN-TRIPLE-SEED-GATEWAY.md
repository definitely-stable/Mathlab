# HYP-105 / #230 — D6-AA4-AN: sharp original triple congestion and a complete physical 3→6 seed gate

**Scientific status: RESEARCH DRAFT, a proof-method theorem / non-lift, not Branch A/B/C.** Stack on [AA4-AM genuine-original mixed two-typed triple transport #531](https://github.com/definitely-stable/Mathlab/pull/531) frozen HEAD `6ace4e84f0ab8a1de068f69c3890829d3ebbfe61`. A separate scientific sibling [AA4-AM D-pair seven-GF5 charge #530](https://github.com/definitely-stable/Mathlab/pull/530) already classifies ALL SEVEN selected GF(5) true ORIGINAL six-incidence source classes as having **six physically distinct coordinates of total degree exactly 2 in each typed projection**. We use that precise registered source model classification as a DEPENDENCY, without incorporating #530's branch into ancestry and without declaring prior results novel. Genuine W(3,s), s=2^h>=2, has V=(s+1)(s²+1) original point and V original line source factors and d=s+1 genuine original incidence neighbors for EACH source factor. Every typed global f,g is complete and injective into E(K_a), a=min{n:C(n,2)>=V}, with m=C(a,2)-V<=a-2 missing physical pairs on EACH type. There is no resampling for different flag triples or sixsets.

## AN-1 — exact structural physical 3-edge seed completion lemma (new scoped classification)

Consider a MULTISET of exactly THREE loopless unordered physical edges on K_a, a>=6. Repetitions are permitted because multiple ACTUAL distinct original incidence flag IDs can share one original source factor and therefore the very same globally assigned physical edge. Let `Δ` be the maximum **multiplicity-counting physical vertex degree** of that three-edge multigraph.

**Theorem (single typed projection):** the three given physical edge occurrences can be completed, by adding exactly three more physical edge occurrences, into a loopless two-regular multigraph on EXACTLY six distinct physical coordinates **if and only if `Δ<=2`**.

- Necessity: physical degrees cannot decrease as more actual flag images are appended. A finished two-regular six-coordinate physical pattern has maximum degree 2.
- Sufficiency, exhaustive structural proof: with three original edge occurrences and Δ<=2, each connected nonisolated component is either a path, a closed physical triangle (three distinct pair labels), or a 2-cycle (one repeated pair). A triangle uses all three initial edges, so a new disjoint triangle on three unused coordinates completes it. A 2-cycle uses two edges; the third necessarily forms a DISJOINT one-edge path, so two fresh coordinates close this path into a C4 using three additional edges. In every other case, all components are paths. If there are c=1,2,3 nontrivial paths they use exactly 3+c distinct coordinates. Add 3−c unused isolated coordinates, arrange these c paths and 3−c isolated coordinates into a single cyclic chain, and join consecutive free endpoints by exactly three additional edges. The result is a simple physical C6 on exactly six coordinates. Each case has an explicitly constructive algorithm in `complete_three_physical_edges_to_six_2regular`. QED.

**CRITICAL SCOPE:** this theorem is an equivalence only for **a single physical projection considered in isolation**. A TRUE original six-incidence-Q must use **the SAME THREE additional genuine original point-line flags** to complete **both** typed projections, with their real W(3,s) source incidence, plus the precise seven-positive-GF5 tag constraints. Passing the per-projection physical `Δ<=2` gate is **necessary but NOT sufficient** for a genuine seven-class positive Q. It is not a Branch C reduction: it does not resolve the joint source constraint.

Independent falsification enumerates all exactly **130** distinct physical six-edge two-regular multigraphs on any fixed six-coordinate set, including the 60 simple physical C6, 10 C3+C3, 45 C4+double-edge, and 15 three-double-edge perfect matchings. Their three-edge occurrence submultisets are compared to **every** three-edge K6/K7/K8 multiset, with edge repetitions retained, independently of the constructive algorithm.

## AN-2 — sharp all-global ORIGINAL source triple congestion minimum (new all-h theorem)

For a fixed full globally injected typed point physical map f, define its physical point-coordinate fiber degree
```text
t_x = #{ actual ORIGINAL source point factors p : x belongs to f(p) }.
```
Then `sum_x t_x = 2V`, each `t_x <= a-1`, and `sum_x((a-1)-t_x)=2m` because the one common global image uses exactly V distinct K_a edges.

Let `C3^P(f,g)` count ORDERED triples `(e1,e2,e3)` of **THREE different actual original incidence FLAG IDs**, such that the THREE original source point factors are PAIRWISE DISTINCT and their THREE globally assigned point physical edges all have a common physical point-coordinate. No restriction is placed on the opposite actual line factors (which may repeat), and the same complete globally injected g is arbitrary but fixed. Every three distinct source point edge labels share **at most one** physical coordinate: if they shared two they would coincide as an unordered physical pair, contradicting global f injection. Every genuine source point has exactly d distinct actual opposite neighbors, so each ordered distinct point-factor triple yields exactly d³ distinct ordered original flag-ID triples. Consequently the following is an EXACT count on the ORIGINAL geometry:

```text
C3^P(f,g) = d³ * sum_{x=0}^{a-1} (t_x)_3,
where (n)_3 = n(n-1)(n-2), and C3^P is independent of g.
```

The typed dual `C3^L` replaces source points by source lines and f by g, with the **SAME** theorem. Unlike [#531](https://github.com/definitely-stable/Mathlab/pull/531), this one-sided triple has **three distinct genuine source factor IDs** on its specified side but is NOT required to share a coordinate also on the other side. It is a different theorem and is not another claim of #531's two-type Ω(s6) result.

### EXACT sharp universal minimum and explicit attainment (AN-2a)

Put `q=floor(2V/a)`, `r=2V-aq`, so `0<=r<a`. Then the exact minimum over **ALL** complete globally injected point maps f and independently **ALL** complete globally injected line maps g is

```text
MIN_{all complete global f,g} C3^P(f,g)
  = d³ * [ (a-r)*(q)_3 + r*(q+1)_3 ].
```

**Lower proof.** The integer sequence `F(t)=(t)_3` for nonnegative integers has discrete second difference `F(t+2)-2F(t+1)+F(t)=6t>=0`. Moving one unit of degree from a larger fiber to a smaller fiber without changing `sum t=2V` cannot increase total `sum F(t)`, until all fiber degrees differ by at most one. The balanced degree multiset with a−r values q and r values q+1 therefore gives the global combinatorial minimum (regardless of graph realizability).

**Attainment proof under the ACTUAL global injective pair-label rule.** Missing physical edge graph on a vertices has m<=a−2 edges, and actual occupied K_a image is its complement. When `m<=floor(a/2)`, choose m disjoint missing physical edges (a matching): their vertex degrees are 0 or 1. When `m>floor(a/2)`, partition all a vertices into c=a−m>=2 vertex-disjoint paths, each containing >=2 vertices (possible because c<=floor(a/2)); the disjoint union has exactly `sum(|path|-1)=a-c=m` missing edges and missing-vertex degrees 1 or 2. In BOTH constructions missing-vertex degrees differ by at most one, and therefore occupied image vertex degrees `t_x=a−1−missing_degree(x)` equal q or q+1. Because arbitrary original source factors can be bijected to the occupied physical edges by a complete globally injected map f, this physical extremum is REALIZABLE ON THE GENUINE ORIGINAL source geometry. The other type global g may be ANY complete injection, and the source incidence degree d does not depend on its placement. Hence the displayed minimum is sharp, not just an abstract balanced-density relaxation. QED.

### EXPLICIT uniform polynomial and unextendibility (AN-2b)

As `m<=a-2`, the mean fiber degree `2V/a=a-1-2m/a>=a-3`. By discrete convexity and monotonicity for integers `t>=2`,

```text
C3^P(f,g) >= d³ * a*(a-3)(a-4)(a-5).
```

For every a>=6, `(a-3)/a>=1/2`, `(a-4)/a>=1/3`, `(a-5)/a>=1/6`, giving product >=a³/36. Minimality and `C(a,2)>=V` imply `a²>=2V>=2s³` and d>=s. Therefore:

```text
FOR ALL h>=1, s=2^h, EVERY complete original typed global f,g:
    C3^P(f,g) >= s^9 / 9,
    C3^L(f,g) >= s^9 / 9,
```

counting ORDERED distinct ORIGINAL incidence-flag triples, not merely abstract physical triples. The exact formula is stronger than this deliberately simple constant. Unordered counts divide by 6.

Every one of these C3 source triples has a physical coordinate of degree THREE in its point projection (or line projection in the dual). Adding three more ORIGINAL flags cannot decrease physical degree. Therefore it is **IMPOSSIBLE** to extend such a triple to ANY physically 2-regular six-coordinate six-flag Q in the relevant side. The external all-seven source classification of sibling #530 covers ALL seven selected positive GF(5) tags, so this excludes **ALL SEVEN genuine positive GF(5) classes**, not just the B/A, A/B and D6 subclasses for which #531 explicitly stated its degree-three nonlift. No independent extra original W3s source assumptions are imposed beyond regular degree and actual global injections.

**Important logically:** this is a **sharp, quantified structural NO-LIFT**, not a lower bound on accepted GF5 sixsets and not a counterexample infinite family to the root #230 conjecture. It shows why one cannot route even an enormous guaranteed population of triple physical-coordinate collisions into seven-positive GF5 Q. It says NOTHING about the complementary population of physically un-congested, extendible-on-each-side triples. The key actual missing gate remains **SIMULTANEOUS original-source six-incidence completion in BOTH typed physical projections**, not pre-Hall physical triples alone.

## AN-3 reproducibility and independent model checks

- Standalone universal mathematics: `research/hyp105_issue230_d6aa4an_triple_seed_gateway.py` (`stdlib` only), with explicit balanced missing edge witness, exact finite sharp minimum, constructive all-130-physical-mode seed completion and scope flags.
- Falsifiers: `research/test_hyp105_issue230_d6aa4an_triple_seed_gateway.py`, physically exhaustive all three-edge K6/7/8 multisets and independently enumerated all possible six-vertex two-regular six-edge multigraphs; exact sharp extremal global physical complement for true source s=2,4,8,16,32,64; all-h exact integer bound h=1..72; TRUE original full 45-flag W32 with four globally complete f/g map fixtures, physical 3-distinct-source flag count by direct triple source incidence-ID enumeration; TRUE W34/W38 with missing globally injected physical pairs; exhaustive seven selected original W32 Q physical 2-regular certification on dual-zero/S68, all three-edge submultisets; every missing-subgraph of K6/K7 (m<=a-2) degree convex extremality; malformed point/line physical label controls.
- GitHub-hosted workflow; retain exact final PR HEAD and final checks separately. All finite tests are falsifiers, not a substitute for the algebraic proof. Require independent mathematical referee before accepting science. The sibling #530 classification is a mathematically necessary dependency of the **full-seven** nonlift promotion; sibling #531 two-typed triple theorem is a different previous result. Do not silently splice unrelated sibling commits into this branch.
- Full selected original seven GF5 Q order `S_s(f,g)=Omega(s^6)` for every global f,g is **NOT proved**; a true infinite correlated counterfamily is **NOT provided**; no strict R3/ASET exponent follows.

**Next genuinely relevant lemma (AA4-AO):** For a TRUE actual original **physically uncrowded** three-flag source seed (physical max degree <=2 on EACH type), derive or refute a uniform degree-dependent lower on ACTUAL SOURCE-INCI­DENCE-coupled completions to SIX different original flags landing in at least one of the seven selected positive GF(5) classes. The physical projection lemma makes such a completion possible independently per side but offers NO simultaneous source-Hall guarantee. The next proof must measure the joint source/physical obstruction, or construct a real correlated infinite counterfamily. No hand-edits to generated `registry/*.md`, no claim of Branch C by mere physically necessary/sufficient seed condition.
