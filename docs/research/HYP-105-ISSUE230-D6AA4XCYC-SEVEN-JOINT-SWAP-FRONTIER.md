# HYP-105 / issue #230 — D6-AA4-X-CYC: deterministic joint seven-GF5 one-swap frontier

**Classification: exact all-h locality identity + finite genuine-original W(3,2) exhaustive local computation. NOT a universal seven-class obstruction, NOT an infinite counterfamily, and NOT a full R3 bound.**

**Parent:** research-only D6-AA4-W-CYC Draft PR #492, HEAD 3446985535e02293c112ba886c2e6e0752c085a0, whose four hosted workflows were SUCCESS when the child branch was created. The base branch is research/hyp105-issue230-d6aa4wcyc-uniform-second-moment. No changes to main. Issue #230 and its upstream issues remain open.

## 1. Objective and gap after W-CYC

The root disjunction asks whether EVERY pair of complete globally injected ORIGINAL point/line physical-pair labels has S_s(f,g) = Omega(s^6), or whether an explicit infinite sequence has S_s=o(s^6), or whether a model-equivalent restricted reduction can be proved.

The exact all-h AA4-Q identity is

\[
S_s(f,g)=N_{\neg AA}(f,g)+D_6(f,g).
\]

Here N_nonAA is the ORIGINAL six-incidence multiplicity of all accepted classes outside AA; D6 requires exactly equal CONNECTED six-column coordinate duals on both physical sides. Both must be evaluated under the SAME global f and SAME global g and the SAME six distinct actual original incidence IDs. The AA4-W-CYC dimension-free positive probability under uniformly random g does not imply adversarial positivity for every g. Actual W32 S68 and S72 have D6=0 and positive other classes.

X-CYC tests the local deterministic tension: does globally swapping exactly two source-line physical labels preserve D6=0 while reducing other classes, and how do the seven historical GF5 contributions trade off? A complete finite one-swap neighborhood is more informative and reproducible than sampling swaps or optimizing D6 alone. It must NOT be described as a proof for arbitrary s or arbitrary pairs.

## 2. Exact all-h original-line support lemma (deterministic)

Let I be the finite set of ACTUAL ORIGINAL point-line incidence IDs of any genuine W(3,s), s=2^h>=2. Let f and g be arbitrary complete globally injected typed maps into the physical unordered-pair alphabet K_a. For two DIFFERENT ACTUAL source line factors u,v, define g' to be g after exchanging precisely the physical images g(u) and g(v), with every other original source label unchanged. This preserves global injectivity, the same alphabet and every genuine source incidence.

For any unordered six-ID subset Q of I, its physical right half depends only on the physical images of the source lines appearing in Q. Consequently if Q contains no ORIGINAL incidence touching u or v, its right half is identical under g and g'. Its left half is identical because f is fixed. The original seven-class indicator I_t(Q;f,g), for EACH of the seven GF5 accepted tags t, therefore satisfies

\[
I_t(Q;f,g')-I_t(Q;f,g)=0 \quad
\text{if }L(Q)\cap\{u,v\}=\varnothing.
\]

Writing A_{u,v}:={Q subset I, |Q|=6, L(Q) intersects {u,v}}, there is an EXACT finite derivative for EACH accepted class, without sign or stochastic assumptions:

\[
C_t(f,g')-C_t(f,g)
=\sum_{Q\in A_{u,v}}[I_t(Q;f,g')-I_t(Q;f,g)].
\]

Summing over the seven tags gives the EXACT S derivative. Restricting to D6 gives its EXACT derivative; weighting every accepted tag with the already certified positive 51-palette GF5 floor w_t gives the EXACT derivative of the seven-class selected risk numerator. This is a statement for EVERY genuine W(3,2^h), all complete global f,g, and every allowed u,v, but does NOT supply a positive sign, quantitative lower bound, or all-h optimization conclusion.

A computational strengthening uses a fixed f and precomputes the set H_P(f) of all six-ID sets with left physical 2-regular profile A,B,C. Since every historical selected positive seven-class set belongs to this fixed H_P, the sums can be safely restricted to A_{u,v} intersect H_P without omitting accepted motifs.

## 3. Independent implementation: original W(3,2) one-swap census

True original model: exactly 15 point factor IDs, 15 line factor IDs, 45 distinct actual source point-line incidences, each factor of incidence degree 3. Minimal a=6, K_a=15 physical unordered pairs. Every complete global map of one side is a permutation of these 15 edges; exactly C(15,2)=105 unordered source-line transpositions are available.

For fixed f (separately S68 and S72), obtain H_P(f) from the independent AA4-Q physical two-factor enumerator: exactly 62,370 distinct genuine ORIGINAL six-ID sets, not synthetic physical paths. For each fixed Q, compute immutable original line-source multiplicity and original B/B-overlap flag; if the source profile cannot be A/B/C on the line side, its selected right-side acceptance is impossible for EVERY g. For AA source with left physical 2-factor, cache the connected six-column dual on the SAME six original positions (or mark disconnected as never D6).

For a candidate globally injected g, use six physical unordered-pair labels at the ACTUAL original Q line endpoints. Count each of six physical coordinate appearances in a separate four-bit lane. Since only six pair labels occur, every lane is <=6, so no carry between lanes is possible. The right physical half is 2-regular if and only if the packed lane value equals the integer with six degree-two nibbles (0x222222). For physically 2-regular A/A, count D6 only if the right six-position dual equals the connected cached left dual; all other allowed source shapes map to their exact accepted positive tag. This mechanism counts ORIGINAL Q multiplicities, not merely source orbit representatives.

Compute the baseline seven counts under ONE full g. For each of the 105 swaps, adjust only those cached original Q records containing u or v as actual ORIGINAL line endpoints; unchanged source Q records provably retain their acceptance. Recount ALL seven historical GF5 positive classes, the exact unweighted S, D6, N_nonAA and the previously certified weighted numerator. Compare the best total S against the best subject to D6=0; build the nondominated (D6,N_nonAA) Pareto set. The unchanged baseline is included as the 106th local candidate.

The only global condition guaranteed for each candidate is complete physical edge-label bijectivity of the line side; f remains exactly frozen. There is no claim that 105 swaps exhaust all 15! line permutations, different f, or all h.

## 4. Two independent falsification paths and acceptance

1. Sparse-original-support derivative versus a completely new scan of ALL 62,370 H_P sixsets for multiple prescribed source swaps. Compare exact seven-tag vector, S, N_nonAA, D6 and the weighted numerator, without reusing the sparse update.
2. Against the separately implemented AA4-Q full left-right 62,370/62,370 ORIGINAL incidence-ID hash join and the historical original GF5 seven-class oracle. Verify S68, S72 baselines and representative changed g, including the final local optimum. Recheck that original GQ C/C is impossible and that every candidate remains a complete global line-image bijection.
3. Exhaust precisely 105 different transpositions for each frozen f. Record counts of D6-zero neighbors, exact best total S and exact D6-zero constrained best, and the nondominated frontier. Confirm all outcome flags for universal root A/B/C are OPEN, not PROVED.

Reproducible local commands from repository root:

    python -m unittest discover -s research -p "test_hyp105_issue230_d6aa4xcyc_seven_joint_swap_frontier.py" -v
    python research/hyp105_issue230_d6aa4xcyc_seven_joint_swap_frontier.py --scheme S68
    python research/hyp105_issue230_d6aa4xcyc_seven_joint_swap_frontier.py --scheme S72

Hosted CI executes these on GitHub-hosted ubuntu-latest. No self-hosted runner; no external package installation.

## 5. Scientific decision rule and next slices

The finite algorithm gives a *complete radius-one right-source-line-label transposition certificate* around each anchor, not a global minimum even at W32. A locally nondominated D6=0 configuration with positive N_nonAA does NOT prove a lower bound for all W32 f,g. Likewise a lower observed S does NOT establish S=o(s^6).

After numerical results are independently checked, the mathematically consequential next problem is a quantified all-h deterministic inequality tying the true-original positional C6 alignment deficit to at least one non-AA forest-cell excess under the same global map pair. Existing AA4-V positional two-factor identity and AA4-U actual source forest transport provide necessary formal building blocks, but neither supplies that inequality. Formalize any candidate, search adversarial finite counterexamples first, then require an actual all-h proof before marking issue #230 Branch A/B/C accepted.

**Publication/provenance:** all mathematical claims above are limited to the all-h support identity and exact finite exhaustive transposition procedure. Reported outcome numbers must come from successful exact-head hosted workflow or independent run; do not extrapolate the 105-local results to global deterministic quantifiers.


## 6. Completed point-line dual extension: all 210 single-side swaps

**A stronger finite X-CYC certificate, NOT a new all-h quantitative lower.** The actual source incidence structure of W(3,s) has point-line duality. To score a true-original POINT-label transposition without changing the original six-incidence universe, exchange actual point and line source endpoints and the two complete typed maps, then apply the independent right-swap oracle. Convert A-left/B-right and B-left/A-right tags back to the ORIGINAL typing. Their certified GF5 positive weights are equal (45,600), and all other accepted tags and their weights are symmetric. The full historical GF5 classifier is applied once again in the ORIGINAL typing to independently check each selected optimum.

Thus per frozen original complete W32 f,g, the **closed radius-one two-sided neighborhood** consists exactly of identity, 105 swaps of original line labels with f fixed, and 105 swaps of original point labels with g fixed: 211 distinct full global mapping pairs. A simultaneous alteration of both sides is NOT included.

### Exact results verified on GitHub-hosted dedicated CI

Dedicated parent-of-results run: https://github.com/definitely-stable/Mathlab/actions/runs/38701781145 . All three jobs SUCCESS, including independent tests and separate S68/S72 exact 105+105 matrices; the printed numerical certificates correspond to code HEAD 640a78fe73eb01f60e079e50029518cc7c317272. Unit tests independently passed 9/9. The following table contains **literal finite results**, not probabilistic or asymptotic estimates.

| Genuine original quantity | S68 | S72 |
| --- | ---: | ---: |
| Baseline S = N_nonAA + D6 | 68 | 72 |
| Baseline D6 | 0 | 0 |
| Right-original-line transpositions checked | 105 | 105 |
| Both typed side transpositions checked | 210 | 210 |
| Full global pairs incl. unchanged original | 211 | 211 |
| D6-zero complete mapping pairs among the 211 | 164 | 124 |
| Minimum S among all 211 | 68 | 72 |
| Minimum N_nonAA with D6=0 among all 211 | 68 | 72 |
| Minimum weighted GF5 numerator among all 211 | 3,112,510 | 3,283,610 |
| Distinct nondominated (D6,N_nonAA) pairs | 1 | 1 |

In BOTH 211-neighborhoods the unchanged baseline itself attains the minimum unweighted full S, the minimum subject to D6=0, AND the minimum historical selected 51-palette risk numerator. The only nondominated objective pair is (0,68) for S68 and (0,72) for S72. This establishes **exact weak local optimality under every single within-one-typed-side source-label transposition**, simultaneously for the full seven-class S and for the selected certified GF5 risk contribution. Equality with another neighbor is not excluded; there is no strict local minimum claim.

### Original seven-class vectors at local minima

| Accepted original GF5 class | S68 | S72 |
| --- | ---: | ---: |
| D6 | 0 | 0 |
| B-left/A-right | 44 | 36 |
| A-left/B-right | 21 | 31 |
| C/A | 0 | 2 |
| C/B | 0 | 0 |
| B/B-overlap | 2 | 1 |
| B/B-disjoint | 1 | 2 |
| TOTAL selected S | 68 | 72 |
| Certified selected weighted numerator | 3,112,510 | 3,283,610 |

The independent canonical ORIGINAL-orientation AA4-Q exact full two-sided join and historical seven-GF5 oracles checked each retained minimum. The proven analytical content is still the exact all-h support derivative lemma, not the assertion that these locally optimal W32 examples lower-bound all maps at W32 or all larger powers of two.

### Research decision

These results reject the naive strategy of obtaining a smaller seven-class count from S68/S72 via **one** global source-factor label transposition on either typed side; they do not rule out higher-radius cycles, correlated simultaneous point-line moves, or other anchors. A follow-up should explicitly test genuine multi-swap or simultaneous moves and search for counterexamples to a PRECISE all-h deterministic charge-transfer inequality tying suppressed D6 to additional non-AA source forest-cell mass.

**Acceptance category for issue #230:** OPEN_WITH_FORMAL_BLOCKER (not PROVED_A, COUNTEREXAMPLE_B or RESTRICTED_THEOREM_C), until the all-h deterministic statement is independently proved. Current finite X-CYC is a reproducible local optimization certificate only.
