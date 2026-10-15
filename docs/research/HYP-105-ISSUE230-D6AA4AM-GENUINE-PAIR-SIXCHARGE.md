# HYP-105 / issue #230 — AA4-AM: exact genuine-original two-flag → seven-GF5 sixset extension incidence and charging obstruction

**Research-only Draft child of [AA4-AL PR #529](https://github.com/definitely-stable/Mathlab/pull/529).** Frozen parent SHA \`8e5763dea0f95ad9959a3050be47f8aa078c2334\`. All combinatorial statements refer to the ACTUAL W(3,s), s=2^h>=2, all complete globally injective typed physical source factor edge maps f,g into the minimal unordered-pair K_a palette, and six DISTINCT true original point-line incidence IDs. Physical maps remain identical across every flag, pair and sextuple. Classical combinatorial double counting is not claimed original; this study applies it to the seven selected positive GF(5) true ORIGINAL incidence-motif classes and identifies their structural zero-charge subspace.

## 1. From AA4-AL global pair energy to exact original six-ID extensions

AA4-AL proved that for every global genuine original f,g there exist at least

    D_ord(f,g)>=16V²(s+1)²/a² -4V(s+1)² >=2s^5

ORDERED compatible ORIGINAL flag pairs (p,l),(q,m) with:
- genuinely distinct original points p!=q and lines l!=m;
- f(p)∩f(q)≠∅ in the *same* physical original point map;
- g(l)∩g(m)≠∅ in the *same* physical original line map.

Every such physical intersection contains **exactly one** coordinate because complete physical unordered-pair maps are globally injective. Let \`D=D_ord/2\` be their distinct UNORDERED source two-flag pairs. The new AA4-AM uses EXACTLY that actual-source D population; it does NOT replace it by arbitrary pairs of abstract physical edges or a resampled source incidence graph.

For any positively selected original six-DISTINCT-flag Q from the genuine seven-GF5 classes, define

    k(Q) := #{ {e_i,e_j} ⊂ Q : {e_i,e_j}∈D }.

This is its true-original pair-anchor multiplicity. Define the genuine seven selected six-ID incidence-family \`𝒮(f,g)\` and the exact ORIGINAL extension hypergraph \`H\` with left vertices \`D\`, right vertices \`𝒮\`, and one incidence (e,Q) precisely when e⊂Q.

    S := |𝒮|,
    E := |E(H)| = ∑_{Q∈𝒮} k(Q) = ∑_{e∈D} deg_H(e),
    U := #{Q∈𝒮 : k(Q)=0},
    C := #{e∈D : deg_H(e)>0}.

Each term is an ACTUAL distinct original-incidence-ID integer with the same globally fixed maps. The expression is an exact **two-way** count, not an expected or averaged physical label event.

## 2. NEW all-h physical source projection structural theorem

Every selected positive GF5 ORIGINAL six-Q has six distinct *physical coordinates each used twice* on both typed sides. For one original source-type projection, only the three source-factor multiplicity partitions are admissible:

| True original source-type six-flag partition | Physical pair image | # physical coordinate links joining DIFFERENT original source factors |
|---|---|---:|
| A: \`1+1+1+1+1+1\` | six different actual original source factors, forming a simple physical six-edge 2-factor | exactly 6 |
| B: \`2+1+1+1+1\` | one repeated actual source factor, other four physically forming complementary C4 | exactly 4 |
| C: \`2+2+2\` | three actual source factors each repeated twice, opposite physical images a matching on six coordinates | **exactly 0** |

Proof: Every physical coordinate belongs to exactly TWO of the six physical flag-edge labels. Because physical source-factor edge images are globally injective, if two flags at that coordinate have the SAME original source factor then those two flags share both physical coordinates of that one image and are excluded from the AA4-AL D predicate (which requires distinct original point and line source factors). A has no repeated original source factor: all six physical coordinate multiplicity pairs join distinct original factors. B has precisely two physical coordinates inside its repeated source factor, and four physical coordinates pairing its four different source factors along a C4. C has six coordinates all internal to the three repeated original source factors, so EVERY physical coordinate pair fails the distinct-original-factor requirement.

A D-anchor of a selected true original six-Q must be a physical coordinate pair simultaneously on both sides. Therefore, for ALL globally injected original f,g, all h and genuine accepted Q:

| Seven selected positive GF5 original six-ID class | True point/line source projection types | Proven \`k(Q)\` |
|---|---|---|
| D6 | A/A, the two physical column duals are an **aligned** six-cycle on the SIX original flag positions | **exactly 6** |
| B-left/A-right | B/A | \`0≤k(Q)≤4\` |
| A-left/B-right | A/B | \`0≤k(Q)≤4\` |
| C/A | C/A or A/C | **exactly 0** |
| C/B | C/B or B/C | **exactly 0** |
| B/B-overlap | B/B | \`0≤k(Q)≤4\` |
| B/B-disjoint | B/B | \`0≤k(Q)≤4\` |

**New structural obstruction:** The selected C/A and C/B sixclasses are perfectly legitimate genuine original six-GF5 positive objects but have ZERO eligible AA4-AL D anchors **for every global source physical map**, as a matter of physical source multiplicity. The user must NOT reason that covering or charging D captures *every* member of the original seven selected family. In D6, aligned original 6cycle dual physical coordinate pair graphs coincide, and all six shared coordinate links use distinct genuine source point and line factors, so \`k=6\` exactly.

The table is an all-h genuine-original theorem; the finite W32 witness calculations below are only independent tests, not the source of these symbolic bounds.

## 3. NEW exact all-map seven-family charging identity and asymptotic equivalence

Since every Q with positive k contributes between 1 and 6 original D anchors, while every Q in U contributes none,

    S = U + #{Q:k(Q)>0},
    #{Q:k(Q)>0} ≤ E ≤ 6 #{Q:k(Q)>0}.

Thus for EVERY genuine W(3,2^h), complete global f,g, exactly

    **U+E/6 ≤ S ≤ U+E**

and, equivalently, since \`S≤U+E≤6S\`,

    **S=Omega(s^6) for a sequence of global maps iff U+E=Omega(s^6)**,

with constants changing by at most SIX. The same pointwise comparison transfers correctly through the ALL-f,g infimum. This is a valid **Branch-C-style MODEL REFORMULATION** of the target into one anchored extension energy E plus a zero-anchor motif mass U. It is emphatically NOT a proof of Branch A, Branch B, or an independent estimate on U or E; an equivalence that retains a difficult original unanchored mass is not itself a solution of #230. It reveals precisely what extra theorem is required for the hoped-for pair-to-six lifting.

In particular, AA4-AL's guarantee \`D>=s^5\` does **not** bound E from below: E counts accepted genuine six-Q extensions, and some D vertices can have extension degree zero. Also the weak sufficient route \`E>=c*s^6\` would yield \`S>=c*s^6/6\` even without controlling U; a different sufficient route is \`U>=c*s^6\`. Neither route is proved.

For finite true-original W32, a complete source-first D-pair-major independently exhaustive oracle agrees with the six-Q-major edge incidence total and computes:
- \`D\`, \`C\`, uncovered \`D-C\`, coverage ratio \`C/D\`;
- full tag-specific selected genuine original six-Q counts, tag-specific extension charges E and genuine zero-anchor U;
- histogram of k(Q) for selected original six-ID Q and positive extension degrees deg_H(e);
- exact weighted selected GF5-51 R3 floor preserved in the separate historical oracle; NO claim that E, U compute all signed GF5 R3.

## 4. Nonextension and asymptotic-order obstacles to naive arguments

Even if EVERY AA4-AL D pair could be extended to at least ONE positive original six-Q, one would only obtain \`E>=D>=Omega(s^5)\` and hence \`S>=E/6>=Omega(s^5)\`. This is **one power short** of the sought \`Omega(s^6)\`. To obtain a universal all-map Omega(s^6) via this E charging channel when U is not already large, one needs **order s extensions on average per guaranteed D pair**, or an independent proof that the universe of positive D pairs itself is Omega(s^6), not currently known. A theorem saying merely \`every D pair is covered\` is insufficient for the target asymptotic exponent using the existing AA4-AL lower.

The frozen genuine W32 dual-zero complete global maps are a caution: D/2=277 true compatible original two-flag pairs coexist with BOTH split-two-triangle true B/A and dual A/B six-Q subtype masses EXACTLY ZERO. The complete original B/A and A/B remain 46, 61, with seven-class S=123, so this is a falsifier of **restricted-class-only** extension, not an all-seven-map zero and not a Branch B counterfamily.

The selected C/A and C/B classes, where k(Q)=0 for all h, show that any attempted disjoint-charging proof that ignores U is fundamentally incomplete as a representation of the full selected seven-positive family.

## 5. Four independently executable tests and exact-source controls

- Independent historical \`seven_census(model, witness_sets=True)\` supplies **every selected actual original six-incidence-ID Q** in finite W(3,2), with exactly 62,370 per original point half six-coordinate candidate witness scan. Five globally fixed typed full physical injection maps are tested separately: dual-zero, lex, reverse, S68, S72. The selected six-Q set is never re-sampled and no six-Q orbits are collapsed.
- Independent source/physical construction \`exact_two_sided_original_seven_join(model, independent_history=True,collect=True)\` on dual-zero and S68 must return exactly the same ORIGINAL six-ID Q→tag sets as the original 62,370-half historical oracle.
- A genuinely different **D-FIRST** finite source-major referee scans ACTUAL original 45 incidence flag pairs satisfying AA4-AL, then for each original selected six-Q checks incidence \`e⊂Q\` directly. It MUST match the Q-first \(E\), \(C\), uncovered D, and the positive extension-degree histogram. This second algorithm does not compute E by summing the same tag-channel k(Q) data.
- Actual ORIGINAL symplectic source transvection and independent physical point/line coordinate relabelings preserve \`D,S,E,U,C\` and all tag k(Q) histograms under that actual same global f,g pair.
- Actual finite genuine W(3,4) lex/random globally injected but nonsurjective K14 with exactly six physical image holes is tested on independently reconstructed real B/A and dual A/B anchored source roots, physical occupied C4 and original opposite complete twofactor H×24 source permutations; every genuine ORIGINAL selected local six-ID Q respects \`k<=4\` and its D anchors belong to the independent full-source D-pair index. **No full-W34 seven-GF5 census is claimed**.
- Negative tests reject fake repeated-original-six-ID Q, made-up source factors, incomplete/non-injective source global physical maps, and use of the W32 full-seven machinery on W34.

**Acceptance and routing:** strict child Draft atop AA4-AL #529; exact final HEAD GitHub-hosted dedicated, INDEX, Proof Audit, Full Research, separate mathematical referee, no RCP accepted theorem or generated five-registry update until approval, no main merges. Full issue #230 remains OPEN.

**Next mathematical step AA4-AN:** Establish an actual nontrivial all-global lower either on \`E\` (globally extendible genuine D pairs with controlled average number of actual selected six-ID positive extensions) or on \`U\` (unanchored true original positive GF5 classes). Develop a sharp original-source/physical-coordinate fiber tensor discriminating D pairs that are ineligible for all seven versus those with Ω(s) extensions. Falsify any too-strong pointwise source-pair extension bound against the frozen W32/w34 ORIGINAL six-ID evidence before suggesting it as a universal lemma. This model-equivalent charging decomposition is a useful research protocol but, alone, not a solution to Branch A/B/C.
