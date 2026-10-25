# HYP-105 / #230 — AA4-CT: dense physical K_a forces occupied C4 reservoirs along genuine original GQ paths

**Scientific DRAFT; partial all-h theorem, NOT Branch A/B/C acceptance.**
Strict child of [AA4-CS PR #619](https://github.com/definitely-stable/Mathlab/pull/619), parent immutable SHA `88f1dec8d89ccc30f30e720eaa341eaf7ecc91fb`; upstream physical-transfer identity [AA4-CR PR #618](https://github.com/definitely-stable/Mathlab/pull/618). Keep main, all seven accepted historical GF(5) necessary weights, R3, and issue #230 unmodified.

## 1. Precise unresolved implication

For every h>=14 and every globally complete typed injected **possibly arbitrarily correlated** original point/line maps f,g on genuine W(3,s), s=2^h, AA4-CS proved that **every pair of half-coordinate physical cuts** X,Y contains at least xy/2 genuine original nonincident threeflag source paths p--l0--q--l, with f(p) disjoint f(q) and g(l) disjoint g(l0). The historical B/B-overlap GF(5) sixflag transfer of AA4-CR still requires (i) an occupied physical C4 completing f(p), away from f(q); (ii) another occupied C4 completing g(l), away from g(l0); and (iii) ONE true ORIGINAL GQ perfect matching of the two resulting triple sets, i.e. permanent of an original 3x3 incidence matrix equal to 1.

Here we prove that **both occupied physical C4 reservoirs have quadratic size in a** along at least Omega(s^6) genuine original source paths under every permitted correlated f,g. This removes only the physical-occupancy obstruction for **many** paths. The 3x3 original permanent can still vanish for every physical C4 pair.

## 2. Physical anchored-C4 lemma (exact all a>=16)

Let a>=16, and let E be ANY occupied graph on the physical coordinate alphabet [a], obtained by deleting at most H<=a-2 distinct physical edges of K_a. For an occupied single physical edge e={u,v} and an occupied doubled edge d={x,y} disjoint from e, put F=[a]\(e∪d), n=a-4.

A candidate C4 containing e and avoiding d is uniquely an ordered pair (z,w) of **different** F vertices and its three added edges {(u,z),(z,w),(w,v)}. Consequently full K_a has N=n(n-1)=(a-4)(a-5) anchored candidates. Define hole-degree h(v)=#missing physical pairs incident to v. A missing (u,z) or (v,w) kills at most n-1 candidates, and a missing internal {z,w} kills at most 2. Hence **for every e,d**, with exact actual occupied count C_E(e|d),

```text
C_E(e|d) >= N - (h(u)+h(v))(n-1) - 2H.               (CT.1)
```

This charging may count a failed C4 more than once, which is harmless for a lower bound. In fact if A={z in F: (u,z) in E}, B={w in F: (v,w) in E}, then the independent exact holes formula is

```text
C_E(e|d) = |A| |B| - |A ∩ B|
           - Σ_{missing {z,w}⊂F} (1_{z∈A,w∈B}+1_{w∈A,z∈B}).  (CT.2)
```

Call a physical vertex **heavy** if 16h(v)>=a. Since Σ_v h(v)=2H<=2(a-2)<2a, there are strictly fewer than 32 heavy vertices, i.e. **at most 31**. If neither endpoint of e is heavy, then h(u)+h(v)<a/8<=n/4 for a>=16. Also, for a>=16,

```text
2H <=2(a-2) <= (a-4)(a-5)/4=N/4,
```

the final inequality being equivalent to a²-17a+36>=0 (at a=16: 20>0; increases thereafter). From CT.1,

```text
C_E(e|d) >= N/2 = (a-4)(a-5)/2                     (CT.3)
```

for EVERY occupied d disjoint from e. There is no dependence on the location of d or on any source incidence.

**Why all-e positivity is FALSE:** place a-2 missing edges at a single star center u, leaving e={u,v} occupied; then e has **zero** occupied C4 completions, even though only a-2 physical edges are absent. Heavy-endpoint exclusion is essential. The committed adversarial test checks this obstruction explicitly.

## 3. Original W(3,2^h) uniform theorem (all h>=14, arbitrary complete correlated f,g)

Let s=2^h, h>=14. Let V=(s+1)(s²+1), a the **minimal** integer with binom(a,2)>=V, k=floor(a/2), H=binom(a,2)-V<=a-2. Fix arbitrary complete globally injected original point and line factor-to-physical pair maps f,g, not assumed independent. Each map omits exactly H physical pairs, and may have its own unrelated holes.

Fix **arbitrary** X,Y subsets of the same physical [a], |X|=|Y|=k. Let P_X be the genuine original point factors p with f(p)⊂X and L_Y the genuine original line factors l with g(l)⊂Y, x=|P_X|, y=|L_Y|.

As in AA4-CS (which only uses global injections and the original GQ incidence axioms), x,y>=m where m=binom(k,2)-H>=V/8 for s>=8. Define B=32(a-1). At most 31 heavy physical vertices exist separately for each map; hence at most **B** original source point endpoints p have f(p) meeting a heavy vertex, and at most B original source line endpoints l have g(l) meeting a heavy vertex. This is a conservative universal bound because each physical coordinate has only a-1 distinct occupied pair edges, and source pair-label maps are globally injected.

AA4-CS guarantees >=xy/2 true ORIGINAL nonincident source threepaths p--l0--q--l satisfying BOTH f(p)∩f(q)=empty and g(l)∩g(l0)=empty, without any independent random selection. Remove every such path whose original p has a heavy f(p) endpoint or original l has a heavy g(l) endpoint. This deletes **at most B*y+B*x** genuine original paths. Thus the number A_CT(X,Y;f,g) of surviving genuine source P3 with BOTH physical disjointness and nonheavy original ENDPOINT physical images satisfies

```text
A_CT >= xy/2 - B(x+y).                               (CT.4)
```

At every retained path, BOTH original f and g physical maps separately satisfy CT.3, so the number of **occupied physical pair of C4 completions** is at least N²/4. These source factor triples are decoded from the ONE fixed globally injected f and g, not independently redrawn, and may or may not be joined by genuine original incidence flags.

**Explicit all-h numerical threshold:** AA4-CS establishes a-2< (3/2)s^(3/2) for s>=16. Therefore a-1<2s^(3/2), and

```text
8B=256(a-1)<512s^(3/2).
m >= V/8 > s^3/8 >=512s^(3/2)       (s>=2^14, already s>=256).
```

The last comparison is equivalent to s^(3/2)>=4096. So m>=8B, and

```text
B(x+y)/(xy) <= 2B/m <=1/4.
A_CT >= xy/4 >= m²/4 >= V²/256 > s^6/256.            (CT.5)
```

**Theorem AA4-CT (all dyadic h>=14):** for EVERY complete original W(3,s), EVERY arbitrary pair of globally injected and mutually correlated original typed maps f,g, and EVERY two physical halfalphabet cuts X,Y, at least **s^6/256** genuine original simple nonincident threeflag P3 anchors have BOTH physical source-factor disjointness and at least (a-4)(a-5)/2 individually occupied physical C4 completions **on EACH side**. There are consequently at least A_CT*N²/4 coupled occupied physical C4 completion pairs, **none of which is counted as an accepted sixflag unless its true original 3x3 incidence permanent equals one**.

The inequalities are deterministic. They do not average over label maps, original paths, geometry symmetries, or random seeds. Source P3 is uniquely determined by original nonincidence p not incident l. There is no claim of independent completion-side sampling. All six original incidence IDs and historic GF(5) acceptance still require an actual matching.

## 4. Independent falsifiers and execution contract

Implementation: `research/hyp105_issue230_d6aa4ct_dense_physical_c4_reservoir.py`.

- **Oracle 1**, mathematical CT.2: occupied K_a minus exact physical hole complement, count |A||B|, subtract diagonal and individually charged missing internal unordered edges; enforce independent CT.1 charging and nonheavy CT.3.
- **Oracle 2**, the independent existing AA4-CR physical source-C4 triple enumerator AND a third elementary ordered physical path-cycle walker; compare ACTUAL occupied C4 counts for genuine true original W(3,2), W(3,4), W(3,8) complete f,g labels, including adversarial holes concentrated at a star.
- **Original source oracle:** enumerate real point/line nonincidence, unique original source 3flag path, both true typed f/g doubled-vs-single physical disjoint tests, then remove only **entire genuine source endpoints** incident to heavy physical coordinates. Compare original P3/disjoint counts against AA4-CS independent certificate on two complete actual f,g schemes per W32/W34/W38; do not claim high-h GQ explicit enumeration.
- **All-h arithmetic falsifier:** integer exact minimal a,m,H,B,N for dyadic h=1..26; the finite regression merely probes the independent infinite analytic derivation for h>=14.
- **Fail closed:** invalid coordinate pair, duplicate physical labels, malformed cuts, noninjective original model, and noninteger h are rejected.

All tests run on GitHub-hosted runners in a separate Draft PR with its own paths-scoped workflow. The source modules use the existing true-original GQ host and already validated globally complete maps; no modification of historic accepted GF(5) classifiers or seven-class ledgers.

## 5. Non-implications, prior work and the actual next lemma

The pigeonhole/hole-degree charging is elementary extremal graph counting; it is **not** claimed as a new general C4 supersaturation theorem. For broader context, He–Ma–Yang, *Some exact results on 4-cycles: stability and supersaturation*, JCTB 149 (2021), DOI 10.1016/j.jctb.2021.01.007, concerns sparse extremal C4 thresholds, while this specific problem is a near-complete K_a with H=O(a) missing edges. The classical GQ axioms, girth eight, and uniqueness of original nonincident 3paths were already used in AA4-CQ/CR. The contribution claimed here is solely the deterministic **project-specific coupling** of near-complete physical C4 occupancy with genuine original GQ nonincident P3 counts and typed correlated global injections.

A tempting false inference would be that, because CT.5 supplies Ω(s^6) genuine source paths each with Ω(a^4) occupied C4-pairs, some positive fraction of those pairs has a true ORIGINAL 3x3 incidence matching. **NO SUCH CONCLUSION HAS BEEN PROVED**. In a sparse GQ incidence graph, the physical matching may be 0 for all tested completions. A positive permanent lower bound uniform in f,g, or alternatively a fixed-map compensating lower from the other six historically accepted original GF(5) classes, is the next substantive mathematical obstruction.

This is a scoped ALL-h **partial theorem**, NOT the root Branch A seven-class S>=c s^6, NOT an infinite Branch B counterfamily, and NOT a model-equivalent root Branch C reduction. It establishes no whole R3 / ASET exponent. The root issue status remains **OPEN_WITH_FORMAL_BLOCKER**, and this proof is DRAFT pending exact-head CI and independent qualified mathematical review. Do not merge ahead of parent #619's own acceptance and ancestry gates.
