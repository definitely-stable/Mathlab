# HYP-105 #230 — AA4-SEVEN34: exact true-source W34 all-seven GF(5) census

**Scope:** finite, **EXHAUSTIVE** original-six-incidence-ID seven-family census of the two independently protected legal \(W(3,4)\) label completions from #665, with identical complete point-label map \(f\), identical frozen 12 source-line labels \(g_J\), identical source 85+85 factors, and identical 425 original symplectic GQ incidence flags. **Root remains OPEN_WITH_FORMAL_BLOCKER.** No all-\(h\) lower bound, all-\(h\) counterfamily, exact *total* \(R_3\), or new ASET exponent is claimed.

## 1. Problem and exact combinatorial reduction

Root #230 counts once per six DISTINCT ORIGINAL source incidence IDs, not signed GF(5) event counts, physical automorphism orbits, or individual physical edges. An accepted sixset must have a physical degree-two six-symbol projection on both typed axes. On either axis, the original endpoint-multiplicity partition must be **A**, **B**, or **C**:

- **A:** six different original source factor IDs, one original incidence flag per factor. Physical graph on the corresponding six distinct pair labels must be simple 2-regular on SIX coordinate symbols (C6 or two disjoint triangles).
- **B:** exactly five different original source factor IDs, one used in TWO distinct original flags, four used once each. The repeated factor contributes the same physical pair edge TWICE. For degree two on six symbols, the other four distinct original factors must be the FOUR physical edges of a simple C4 on four coordinate symbols disjoint from the repeated physical pair edge. Hence the physical degree-two projection has structure doubled-edge + C4.
- **C:** exactly three different original source factor IDs, each used in exactly TWO original flags. Their three DISTINCT physical pair edges must form a 3-matching of six coordinate symbols; each edge occurs twice. Hence the projected structure is three doubled disjoint edges.

These are NECESSARY and SUFFICIENT source-partition/physical projection descriptions, by counting total six incidences, source endpoint multiplicities and the prescribed coordinate degrees.

The accepted historical seven-family partition is:
1. A/A: only the aligned original \(D6\) source-sixsets (the historical column-dual connected C6 match), independently and EXACTLY counted by #667's source-flag physical rainbow-C6 oracle.
2. B-left/A-right: counted by enumerating left B once and testing right A + right physical degree-two.
3. A-left/B-right: symmetrically enumerate right B once, require left A.
4. C/A: enumerate either left C with right A OR right C with left A; these are disjoint sixset families.
5. C/B: enumerate left C with right B OR right C with left B; again disjoint.
6. B/B-overlap: enumerate LEFT B once, require right B with the two repeated original source endpoint pairs sharing ONE selected original incidence ID.
7. B/B-disjoint: enumerate LEFT B once, require right B with no shared selected incidence ID.

These seven cases are pairwise disjoint and cover every historically accepted original positive GF(5) sixset by the original seven-class classifier. The C/C and A/A nonaligned physical motifs are NOT counted as accepted; B/B is deliberately not double-enumerated by both directions. Any candidate whose physical projection is not degree-two on six physical symbols on EITHER axis is rejected.

## 2. Unique canonical finite enumeration, no choose(425,6) scan

**B-side:** Fix the unique duplicated original source factor \(p\) and its TWO selected source flag IDs (unordered). Fix the unique four-vertex coordinate subset disjoint from the two physical coordinates in its pair label, and the distinct 4-cycle on those vertices (exactly THREE possible C4 edge sets). Since the full typed label map is globally injective, each of the four C4 physical edges has at most one original source factor owner. If any is unoccupied, reject. Choose ONE genuine original source incidence ID incident to EACH such source factor. The six selected original flags are all different. Every structurally valid B-side sixset has **one and only one** such description (the repeated source factor and disjoint four-cycle are uniquely recoverable).

**C-side:** Fix the unique unordered triple of duplicated original source factors \(p<q<r\), require their physical pair labels to be pairwise coordinate-disjoint, and choose TWO unordered original source incidence IDs from each factor's genuine source pencil. Each structural C-side sixset has **exactly one** description.

A pure **C++20** finite inner loop enumerates only these B/C configurations, with no sampling, deduplication by physical label automorphisms, approximated asymptotics or synthetic source flags. For the opposite physical projection, a 4-bit nibble per coordinate stores the exact sixset coordinate degree (0..6, no carry); a physical projection qualifies **iff** every nibble is either 0 or 2. Since exactly twelve coordinate occurrences exist, the accepted projection automatically has exactly six degree-two symbols. Original opposite factor IDs then determine A versus B and (for B/B) true ORIGINAL ID overlap. The native program outputs exact integer counts, candidate traversal sizes and at least ONE ORIGINAL six-incidence-ID witness in every nonempty class.

Independent Python invokes the HISTORICAL original GF(5) seven-family classifier for each witness to reject any misidentified new class. For \(W(3,2)\), *ALL SEVEN numeric counts*, the total seven-family \(S\), and the necessary GF(5) weighted numerator must match the historical full 62,370-candidate independent Python enumeration for BOTH lex and reverse-line maps. That is a complete independent finite crosscheck of the new canonical B/C enumeration and GF(5) class semantics. For \(W(3,4)\), the independently verified #667 \(D6\) source-ID physical DFS supplies the A/A accepted contribution and retains the exact POS=7567, ZERO=8110 protected regression.

## 3. Source model and output

The source is the actual finite-field symplectic \(W(3,4)\), with 85 original points, 85 original lines and 425 genuine incidence flags. Each original factor receives a globally injected pair label from \(K_{14}\), whose 91 possible pairs leave six unused factor slots on each axis. The two compared complete maps have the SAME entire \(f\) and SAME twelve frozen \(g_J\) assignments; the other 73 original line labels differ through the exact immutable #665 permutation of 79 available pair slots. All ORIGINAL incidence flags are preserved.

The report prints the **seven exact integer multiplicities**, \(S=\sum_{\rm seven}\) and the accepted strict necessary GF(5) third-risk floor
\[
  51^6 R_3(f,g)\;\ge\;
  5643D6+45600(U_{B{\rm left}}+U_{B{\rm right}})
  +43320U_{CA}+49050U_{CB}
  +51750U_{BB{\rm overlap}}+45010U_{BB{\rm disjoint}}.
\]
This is **a lower bound**, not the exact total \(R_3\), not a signed-event census, and not an upper bound. The exact positivity of per-class GF(5) coefficients and seven labels comes from historical accepted source work. This slice adds an exhaustive finite genuine-source high-order census and does not rederive Fourier GF(5) coefficients.

Exact reproducibility on hosted Linux (Python 3.12, g++ C++20):
\`HYP105_FULL_W34_SEVEN=1 python -m unittest discover -s research -p 'test_hyp105_w34_seven_class_census.py' -v\`.
The dedicated hosted workflow is \`.github/workflows/hyp105-w34-all-seven-original-gf5.yml\`; expected machine-readable log tag: \`HYP105_AA4_SEVEN34_CERTIFICATE=\`. The full Research suite can run the W32 independent controls without repeating the large W34 census; W34 is checked in the dedicated hosted gate only.

## 4. Scientific non-implications and next proof gate

At one finite \(s=4\), a complete seven-class POS/ZERO comparison resolves whether suppressing two local K3,2 source expansions decreases or increases either global \(S_{\rm seven}\) or its **accepted necessary GF(5) floor**. The ordering may vary between raw \(S\) and weighted GF(5) risk; both are separately reported. This has no universal all-\(h\) extrapolation: a single finite comparison cannot establish an asymptotic \(\inf_{f,g}S_s=\Omega(s^6)\), nor a dyadic infinite family with \(S=o(s^6)\).

Even when a local \(D6\) proxy fails monotonicity (#667), the full seven-class source census is only a finite falsifier or finite positive example. Next mathematical step after inspecting its certified counts: derive an **all-map, same-fixed-\(f,g\)** deterministic compensation inequality between the *global* seven accepted original source classes, anchored in the full source incidence tensor or codegree identities, with explicit asymptotic constants or an admissible counterfamily. A finite optimizer, annealed expectation, or heuristic local penalty cannot replace that universal quantified step.

**References:** [root issue #230](https://github.com/definitely-stable/Mathlab/issues/230); [#665 local ZERO](https://github.com/definitely-stable/Mathlab/pull/665); [#666 conditional expectation](https://github.com/definitely-stable/Mathlab/pull/666); [#667 exact global D6 displacement](https://github.com/definitely-stable/Mathlab/pull/667). The present work is a scientific Draft stacked directly on #667; parent/main are not mutated.


## 5. Exact hosted certificate — W34 POS versus ZERO (28 October 2026)

The specialized GitHub-hosted [run #40632519617](https://github.com/definitely-stable/Mathlab/actions/runs/40632519617) finished **SUCCESS** on initial PR head \`4725aeca1eebf7c3a669c54ed65bfda1b5d09ed6\` with the exact machine-readable certificate \`HYP105_AA4_SEVEN34_CERTIFICATE\`. All W32 independent historical seven-class checks and both full genuine W34 model computations passed. The following *numerical assertions are now pinned as exact regressions in subsequent PR head* and require the new exact-head hosted checks before final integration.

| Historical original sixflag accepted GF(5) class | POS complete map | ZERO complete map | ZERO − POS |
|---|---:|---:|---:|
| D6 (independent original source #667) | 7,567 | 8,110 | +543 |
| B-left/A-right | 177,564 | 170,578 | −6,986 |
| A-left/B-right | 173,412 | 168,080 | −5,332 |
| C/A | 22,122 | 21,349 | −773 |
| C/B | 4,070 | 4,336 | +266 |
| B/B-overlap | 22,802 | 23,262 | +460 |
| B/B-disjoint | 21,921 | 19,827 | −2,094 |
| **Complete original sixset sum S_seven** | **429,458** | **415,542** | **−13,916** |

The ZERO completion, while having **more** global accepted original D6 (\(+543\), from parent #667), actually has **fewer** accepted original sixsets over ALL SEVEN historical classes (−13,916 = −3.24036% of POS). The largest structural difference is in the two one-sided B/A classes (joint count change −12,318). This is a certified **FINITE, same-f/same-frozen-g_J inverse-order counterexample** to treating **global D6** as a monotonically aligned proxy for the *full seven-class* \(S_{\rm seven}\). The selected saturated-parent M also decreases (4 to 0) and therefore is NOT falsified as a monotone S proxy by THIS pair; its universal validity remains unproved.

The strictly necessary full-palette GF(5) third-order **lower floor** also changes in the same direction as S, with exact numerators:

\[
  51^6R_3(f,g_{\rm POS})\ge
  \underbrace{19{,}371{,}832{,}431}_{\text{seven-family necessary numerator}},
\]
\[
  51^6R_3(f,g_{\rm ZERO})\ge
  \underbrace{18{,}722{,}310{,}780}_{\text{seven-family necessary numerator}},
\]
so the ZERO minus POS difference between these **certified necessary lower-floor numerators** is precisely \(-649{,}521{,}651\). In rational \(R_3\) units these are \(19{,}371{,}832{,}431/17{,}596{,}287{,}801\approx1.1009045\) and \(18{,}722{,}310{,}780/17{,}596{,}287{,}801\approx1.0639921\). **This is a comparison of lower floors, NOT proof that the actual total R3 decreases.** Additional positive GF(5) events outside the seven selected families, and additional signs within them, can differ.

The exhaustive B/C-only native enumeration examined the exact canonical source candidates:
- POS: **1,211,625,000** B candidates (both typed directions), **72,540,000** C candidates.
- ZERO: **1,201,268,750** B candidates, **72,893,000** C candidates.

All six source-ID witnesses for the non-D6 classes passed the separate historical GF(5) accepted-class classifier; the complete W32 reference census on lex/reverse mappings also exactly matched historical accepted seven-class counts and numerical weighted floor. D6 values came from separate source-ID physical rainbow-cycle enumeration. The canonical B/C enumeration algorithm counts an arbitrary accepted sixset with its repeated factor and square/matching **once**, not one copy per coordinate automorphism. The input is all 425 actual original symplectic flags, not an abstract synthetic physical graph.

### Refined formal STOP and next allowed mathematical question

The last two original W34 maps **disprove monotonic ranking by global D6**, not by every local proxy:
\[
D6_{\rm ZERO}>D6_{\rm POS},
\qquad
S_{\rm ZERO}<S_{\rm POS},
\]
under fixed complete f and fixed selected source physical structure. They do **not** prove an all-h universal negative correlation, nor refute any universally valid inequality \(S\ge D6\). In these two particular maps the local saturated-parent mass M decreases from 4 to 0 **together with S**, so this pair does NOT falsify monotonicity of M versus S; it only shows that M and global D6 can order maps oppositely (#667), while global D6 and S can likewise order maps oppositely (this slice). The rigorous all-h root \(S_s(f,g)=\Omega(s^6)\) remains **OPEN_WITH_FORMAL_BLOCKER**. Future work must prove an all-map same-completion lower bound on the **full** positive original motif functional, or formulate a precise model-equivalent all-h reduction; simply increasing global D6 or decreasing one local saturated-parent statistic cannot safely rank seven-class \(S\) for arbitrary correlated completions.
