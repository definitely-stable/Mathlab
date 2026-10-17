# HYP-105 / #230 — AA4-CA: exact finite Boolean-N3 sixcube highpass bound (15/16)

**SCIENTIFIC DRAFT; strict child of [AA4-BZ #600](https://github.com/definitely-stable/Mathlab/pull/600), parent exact HEAD `4260fe93be8825e1a4b5aa44b7c962d50d24a8c1`.** Not a claim of accepted A/B/C, not merged, and not a physical sharpness theorem. Original issue #230 remains `OPEN_WITH_FORMAL_BLOCKER`. Preserve six distinct ORIGINAL incidence IDs, authentic symplectic `W(3,2^h)` for every `h>=1`, global typed physical-pair injection and arbitrarily correlated complete original maps f,g.

## Why this is a new mathematical slice, rather than repeating BZ

- #597: all-seven selected historical GF(5) weighted fixed-f necessary 51-column risk numerator `W(f,g)`; general Boolean sixth-packet highpass bound `51/32`.
- #599: for a genuine sixth-packet original source Q, physical right 2-regular acceptance indicator is independent in the Boolean sixcube; abstract-independent bound `45/32`.
- #600: for **every** sixcube vertex, at most three of its six neighbors yield genuine-original physical right 2-regularity, hence the historical accepted GF5 Boolean subset obeys the same N3 bound; a seven-dimensional *fractional radial relaxation* yields non-sharp upper `139/128`.
- **AA4-CA new:** impose that the original historical six-Q accepted pattern is a *BOOLEAN 64-vertex set* (not a fractional radial vector). Compute its exact upper and lower degree>3 Fourier highpass norms under independence + N3. This results in a **sharp bound for that constrained abstract Boolean class**, `15/16`, without asserting sharpness for physical edge-support/W3/GF5 realizations.

This is a finite extremal set-system/Boolean-function result; Boolean Walsh/Krawtchouk analysis and classical Turán-type hypergraph counting are prior mathematical foundations, NOT asserted discoveries. See O'Donnell, *Analysis of Boolean Functions* (arXiv:2105.10386) and the classical Turán tetrahedron-free 3-graph problem. No scientific priority claim for this finite computational certificate.

## Quantified theorem AA4-CA-BOOL-N3 (all h, all correlated original f,g)

Let `I:{0,1}^6->{0,1}` be any Boolean function such that

`I(x) I(x xor e_i)=0` for all x,i, and
`sum_i I(x xor e_i) <= 3` for all x.

The two hypotheses are true **for every individual genuine original historical accepted GF5 sixth-packet six-incidence Q** by #599 and #600, on the complete 64-map original whole-source-LINE image-swap cube. They do **not** express independence among distinct Q, and arbitrary f,g correlations are permitted.

For the projection onto Fourier degrees 4,5,6, the exact classical radial kernel around any center is

`K6(j)=(22,-10,2,2,-2,-2,10)` for Hamming distance j.

**Theorem (exact Boolean N3 extremum):**

```text
For every Boolean I satisfying edge independence + N3, every center x,
     -48 <= sum_y I(y) K6(d_H(x,y)) <= 60.
Both endpoints are attained in the ABSTRACT constrained Boolean class.
Therefore max_{I,x} |(I-P_<=3 I)(x)| = 60/64 = 15/16.
```

This sharpness claim is **only** for the class of *all Boolean sixcube subsets* meeting the parent necessary constraints. Additional physical 2-factor edge-compatibility, six original incidence semantics, and GF5 classification may make the realizable exact maximum strictly smaller.

### Exact positive-side reduction to six-element set systems

Translate center to x=0. The maximizing set for the positive signed sum can discard all vertices whose K6 coefficient is negative; independence and N3 are hereditary under taking subsets. The remaining positive layers are 0,2,3,6. Denote selected weight-2 subsets of `[6]` by E and weight-3 subsets by H. The constraints imply:

1. The graph E on six vertices has maximum degree at most **3**: the sixcube N3 inequality at each weight-1 vertex counts its selected layer-2 neighbors (we *drop* any further restriction from layer0).
2. Every physical 2-subset is contained in at most **3** chosen triples H: N3 at a weight-2 vertex (weight-3 neighbors).
3. Every 4-subset contains at most **3** chosen triples H: N3 at a weight-4 vertex (weight-3 neighbors).
4. No pair in E is contained in any triple in H: those two layers would be adjacent.

**Finite lemma:** every (E,H) satisfying these four conditions obeys

```text
|E| + |H| <= 14.
```

A complete exact **proof by finite enumeration** is in `research/hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel.py`. One deterministic certificate enumerates all `2^20=1,048,576` triple subfamilies H, discarding those that violate pair/quad N3 restrictions, leaving **348,644**. For each valid H, the allowed edges are exactly those not contained in any H; a max-plus subset-zeta dynamic program covers **all 2^15=32,768 graphs E** with maximum degree <=3 and finds the largest admissible E. Its verified global optimum is 14. All computations are exact finite integers, not floating point, random sampling, LP tolerance, or geometry fabricated for large h.

**Independent algorithm and separate falsifier:** enumerate **all 32,768 graphs E first**, reduce the degree<=3 graphs under **all 720 vertex permutations** to **62** isomorphism classes, then independently exhaust all subfamilies of triples not containing any selected E edge, checking conditions 2–3 directly. This has *no use* of the other verifier's subset-zeta recurrence. It also gives 14. The 62 representatives and search are mechanically complete by constructing the canonical minimum of each labeled E across all 720 permutations; pair/triple incidences are permutation-invariant. Both algorithms and the assertion that their answers agree are run in GitHub-hosted CI. They constitute an explicit finite proof certificate and two algorithmically independent falsifiers; a hand-only extremal proof or external mathematical peer review is **not** claimed.

Consequently the positive K6 sum is at most

`22 I(0) + 2(|E|+|H|) + 10 I(111111) <= 22+28+10=60`.

**Explicit equality witness (abstract only):** take layer0 and layer6 plus all twenty weight3 subsets **except** the following six (coordinates numbered 1..6):

`125,126,134,234,356,456`.

This gives 14 accepted weight3 vertices, zero weight2 vertices, and passes all 64 N3 and independence constraints, with signed K6 sum `22+28+10=60`.

### Independent analytic negative-side proof and witness

For the minimum, discard positive K6 layers. We retain layers 1,4,5 with counts `n1,n4,n5`. The N3 bound around origin gives `n1<=3`. N3 around each of the six layer-5 vertices permits at most three selected layer-4 neighbors, while any *selected* layer-5 vertex has **zero** selected layer-4 neighbors by independence. Every selected layer-4 vertex lies under exactly two layer-5 vertices, hence

`2 n4 <= 3(6-n5)`, implying `n4+n5 <=9`.

Thus

`sum_y I(y)K6(|y|) >= -10n1-2(n4+n5) >= -30-18=-48`.

Equality is realized abstractly by choosing any three of the six weight1 vertices, plus nine weight4 vertices that are complements of the nine edges of `K3,3` with bipartition `{1,2,3}|{4,5,6}`. An independent direct 64-vertex falsifier verifies this witness, all 64 neighborhoods and its exact signed value -48.

By XOR translation every cube center has the same bound. Since `60>48`, the sharp **abstract constraint-class** highpass norm is `60/64=15/16`.

## Conditional true ORIGINAL all-seven GF5 center consequence

Retain all previous actual-original source-Q classification and GF5 weights from #597–600. Fix a genuine symplectic `W(3,s)`, `s=2^h`, h>=1, a complete globally injected original physical point map f, an arbitrary potentially adversarial correlated complete line map g, and six disjoint genuine original LINE-factor swap packets. Let `H6(f)` be the historical f-only weighted mass of genuine **SIX DISTINCT ORIGINAL incidence-ID sets** that touch all six packets, are point-side eligible and belong to a permitted one of the seven selected positive GF5 classes (same definition as #599–600).

For **each individual** sixpacket Q, parent assumptions ensure the Boolean N3 conditions; triangle inequalities sum over Q without any independence or concentration assumption. Other packet-support terms and P<=3 W are unchanged. Therefore the strict all-h, all-original-center uniform improvement is

```text
eta6_CA = 15/16,
eta6_BZ = 139/128,
Delta_eta = 19/128,

E_f^CA = E_f^BZ - (19/128) H6(f),
|W(f,g^x) - P_<=3 W(x)| <= E_f^CA  for all 64 complete g^x,
W(f,g) >= max(0, P_<=3 W(0) - E_f^CA).
```

Here W is ONLY the historical **selected seven-class 51-column GF5 necessary R3 numerator**, not the full R3 or R2. The inequality does **not** produce an `Omega(s^6)` original-center result absent an independent positive margin on low-order terms. No claim of root Branch A, infinite original correlated counterexample Branch B, or qualifying model-equivalent reduction Branch C.

### Genuine original finite W32 evidence (not an all-h fit)

| Historical authentic original f | H6(f) | Extra BZ->CA saving | AA4-CA E_f | Original unchanged W(0) |
|---|---:|---:|---:|---:|
| W32 lex | 4,690,929 | 89,127,651/128 | 8,113,433,771/16 | 11,225,795 |
| W32 S72 | 3,731,790 | 35,452,005/64 | 3,883,420,431/8 | 3,283,610 |

The expected source mass and exact fractions inherit the **real original historical GF5 full seven-class** W32 census of #600 and must be checked again on this PR head in its own GitHub-hosted test. An adversarial permutation of the COMPLETE g images does not alter f-only E. The computed lower bound remains **ZERO** for both finite examples; neither shows universal positivity. This is not synthetic high-h W geometry.

## Independent evidence and acceptance limits

- All integer enumeration inputs, iteration domains, masks, accepted/forbidden patterns and both exact algorithms are committed in the source; independent 62-orbit implementation checks all pairs first rather than dynamic programming on triples.
- Positive/negative equality patterns, all 64 cube translations, nonbinary/malformed input and forced adjacent/four-neighbor failures have explicit tests.
- Genuine W32 full original GF5 seven-class center and f-only mass/error checks are requested on GitHub-hosted CI, separate from the finite mathematical verifier.
- Parent #600 has a **failed/cancelled general Research workflow state at its observed HEAD** despite dedicated/INDEX/Proof Audit successes; parent acceptance is not inferred.
- This is a conditional partial Fourier bound with a computer-assisted finite lemma. **No external independent mathematical referee** has accepted the source proof, nor are root A/B/C or physical sharpness established. Parent chains remain unmerged Drafts. Do NOT merge this Draft, alter canonical accepted RCP registers, close #230, or assert an ASET exponent based solely on CI.

**Next real frontier:** rather than endlessly tightening a sixth-packet error constant, derive a truly original correlated f/g cross-class zero-/low-order seven-GF5 center *positive-margin* inequality, or a genuine infinite original correlated counterfamily, with the full root #230 acceptance conditions. The local highpass norm reduction does not itself overcome the low-order sign problem.
