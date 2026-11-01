# HYP-105 / #230 — AA4-SIGN10: sharp ten-sign ORIGINAL (D_6) and (B/B)-overlap GF(5) risk floor

**Status:** an exact finite-algebra **ALL-h fixed-map** corollary, backed by full independent two-oracle signed checks and actual ORIGINAL (W(3,2))/(W(3,4)) source realizations. Scientific **Draft** stacked strictly on [#687](https://github.com/definitely-stable/Mathlab/pull/687), pinned parent `dfb84d0c2076f822e178371c3b7e48229c32a996`. It does not purport to be an independent qualified external referee of the geometric Branch A proof, does not change the sextic exponent or produce an upper bound for R2/R3, does not merge ancestor PRs and does not close issue #230.

## 1. Why the previously accepted lower bound is not sharp

The accepted source-sixset necessary lower bound (from merged #214, #218, #224 and fixed-family census) is

\[
51^6 R_3(f,g)\ge 5643D_6+45600(U_{B,L}+U_{B,R})
  +43320 U_{CA}+49050U_{CB}+51750U_{BB,\mathrm{overlap}}
  +45010U_{BB,\mathrm{disjoint}}.\tag{1}
\]

Every `D6` and `U` counts an **unordered set of SIX DISTINCT ORIGINAL incidence flag IDs**, not physical embeddings, sign partitions or flow assignments. Point and line factor maps are complete and separately globally injected, arbitrarily correlated and fixed. The original source is true symplectic `W(3,s)` for `s=2^h`, every integer `h>=1`.

The historical coefficient `5643` for matching aligned physical C6/C6 counted **only the unique alternating signed partition**. But in the original signed-event definition of `R3`, all ten unordered 3-versus-3 partitions of six named columns contribute **separate nonnegative expectations**. In contrast, `51750=10*5175` is an intentionally conservative floor for B/B-overlap, obtained by using the smallest **individual signed** flow count in each of ten partitions, even though a single physical sixset cannot simultaneously attain the minima for all ten partitions.

The present slice makes this distinction exact. It **does not** estimate the probability of the UNION of ten dependent events. The object `R3` is the **sum of the probabilities** over unordered signed 3-versus-3 partitions; linearity of expectation, not independence, justifies their addition. If the quantity were a union probability instead, this theorem would not follow.

## 2. Full 51-pattern GF5 coefficient model and two independent finite proofs

For each of six ORIGINAL flags, its four nonzero GF(5) entries `(a0,a1,b0,b1)` lie in `GF(5)*` and sum to `4 mod5`; there are exactly 51 choices. For each sign mask with exactly three '+' and three '-' columns, identify the physical coordinate in each color with a graph edge joining the TWO named columns that contain that coordinate. The resulting 12-edge two-color multigraph `H` lives on the **six original column IDs**. If `sigma_i` denotes the sign, the four checksum and all physical-coordinate cancellation equations are in exact bijection with nowhere-zero signed edge currents satisfying

\[
B_H x=b,\qquad b_i=4\sigma_i\pmod5,\qquad x_e\in\{1,2,3,4\}.\tag{2}
\]

The ten unordered balanced signs are represented by the ten plus triples that contain named original ID 0 (global sign complement identified ONCE).

The two independent `#687` solvers are fully exercised on every case here, not just held-out samples:

* **Edge-deletion IE oracle:** an exact sum over `2^12` colored edge subsets, respecting parallel edges and the component-balancing condition, with `5^{|A|-6+c(A)}` for each allowed subset.
* **Direct tree-current oracle:** independently enumerate all `4^7` assignments to nonzero chord currents in a deterministic spanning tree and uniquely solve the remaining five tree currents by leaf elimination, checking that no solved current is zero.

Neither method calls the historical original-flow tables, restricted Fourier oracle, or a precomputed coefficient lookup. They agree for the complete 100-case test universe described below, including independently planted true-original source flags.

## 3. New exact D6 coefficient: 54,162, not 5,643

A `D6` sixset has six **different ORIGINAL point factors** and six **different ORIGINAL line factors**. Both left and right physical column-adjacency graphs are the SAME simple six-cycle on those six named original flags. The two color copies remain different edges in the 12-edge multigraph, even if they join the same named columns. Every `D6` instance is simultaneously equivalent by a COMMON original-column permutation to this graph; no physical color exchange or source relabeling between sides is needed.

The ten unordered signed GF5 counts are exactly

\[
(5265,5454,5454,5265,5454,5643,5454,5454,5454,5265).
\]

Equivalently there are three masks with 5265 coefficient assignments, six with 5454, and one alternating mask with 5643, all positive. Therefore the **entire accepted signed R3 subfamily contribution** of each ORIGINAL D6 sixset is

\[
\boxed{
F_{D6}^{\rm all-signs}=3(5265)+6(5454)+5643=54162.
}\tag{3}
\]

This is an exact finite integer identity independent of `s,f,g`, rather than a finite-h statistical fit. The old 5643 term remains valid but discards the other nine positive signed events.

## 4. New sharp B/B-overlap coefficient: 53,526, not 51,750

A true ORIGINAL `B/B-overlap` sixset has a unique twice-repeated ORIGINAL point factor and a unique twice-repeated ORIGINAL line factor. Their repeated two-ID pairs intersect in **exactly one ORIGINAL incidence ID**. After a COMMON renaming of the six ORIGINAL columns, choose repeated point pair `{0,1}` and repeated line pair `{0,2}`. Each physical half has two parallel coordinate edges on its repeated pair plus one of exactly THREE physical four-cycles on the four remaining ORIGINAL columns. Hence there are exactly `3*3=9` colored C4/C4 templates, each with ten canonical sign events, a total of 90 exact finite cases.

For all nine templates, sum the **actual ten signed counts**, rather than ten times their common single-event minimum. The complete exact distribution is

\[
\begin{array}{c|c|c}
\text{number of physical templates}&\text{sum of all ten signs}&\text{source sixset class}\\\hline
6&53526&B/B\ \mathrm{overlap}\\
3&53838&B/B\ \mathrm{overlap}
\end{array}
\]

Every one of the ninety signed flow counts is strictly positive, with the individual range `5175..5535`. The sum over all ninety cases is `6*53526+3*53838=482670`, reproducing the previously accepted historical finite aggregate. Therefore EVERY fixed legal ORIGINAL B/B-overlap sixset has

\[
\boxed{
F_{BBo}^{\rm all-signs}\in\{53526,53838\},\qquad
F_{BBo}^{\rm all-signs}\ge53526.
}\tag{4}
\]

In contrast, the previous inequality applied `10*5175=51750` even though no fixed physical sixset attains ten simultaneous single-sign minima. Equation (4) is the exact **sharp uniform signed-event floor**, not a claim that every sixset has exactly 53526.

## 5. Sharpness is realized on actual original W(3,2), W(3,4)

For **each** genuine `h=1,2`, the independent test constructs a real ORIGINAL nonincident `q,r` pair and its unique original projection `q--ell--p--r`, then appends THREE genuine original source flags with pairwise distinct point/line factors outside `{q,p,ell,r}`. The six original flags now have exactly five original point factors, five original line factors and one common repeated-factor incidence `(p,ell)`.

Holding the SAME six original flag IDs fixed, independently vary only the complete, separately globally injected physical pair maps f,g to realize all `3*3=9` possible left/right C4 physical incidence structures. This is done by **constructing actual source-factor label maps and re-reading all twelve physical coordinate incidences from their six ORIGINAL flag IDs**, never by merely declaring nine abstract profiles. In both genuine finite sources the resulting ten-signed aggregate distribution is exactly six occurrences of 53526 and three of 53838. Thus the uniform minimum 53526 is **attainable for a legal complete source mapping**; it cannot be raised for arbitrary maps without using an extra global restriction.

Likewise a true six-flag ORIGINAL point/line matching is placed on coincident physical left/right C6s in both `W(3,2)` and `W(3,4)`, with both typed maps extended globally and injectively. All ten signed full-palette counts independently give the total 54162. The finite genuine witnesses establish realizability and exclude a fake-profile loophole; the **all-h algebraic inequalities** follow from (2)–(4), not extrapolation from the two small field orders.

## 6. NEW all-map GF5 floor and root implication

Because D6 original sixsets have SIX distinct point and SIX distinct line factors, whereas BBo sixsets have FIVE each and one repeated-original-source flag overlap, these source-sixset populations are **disjoint by factor partition**, even under arbitrary correlated physical pair maps. In the original signed-event risk metric, signs over each original sixset are also distinct events. Therefore the following **UNCONDITIONAL exact finite-algebra lower bound** holds for all genuine W(3,s), all dyadic h and all fixed complete legal correlated maps:

\[
\boxed{
51^6R_3(f,g)\ \ge\ 54162D_6(f,g)
 +53526U_{BB,\mathrm{overlap}}(f,g).
}\tag{5}
\]

The other five accepted disjoint families may be added back without loss:

\[
\begin{aligned}
51^6R_3(f,g)\ge {}&
54162D_6+45600(U_{B,L}+U_{B,R})\\
&+43320 U_{CA}+49050 U_{CB}\\
&+53526U_{BB,\mathrm{overlap}}+45010U_{BB,\mathrm{disjoint}}.
\end{aligned}\tag{6}
\]

Now **ONLY IF** the separately proved and externally accepted geometric Branch A input [#659/#672–686] holds with some `delta>0` and for all sufficiently large dyadic s,

\[
D_6(f,g)+U_{BB,\rm overlap}(f,g)\ge\delta s^6,
\tag{7}
\]

we obtain the strengthened model-specific asymptotic obstruction

\[
\boxed{
R_3(f,g)\ge
\frac{53526\,\delta}{51^6}s^6.
}\tag{8}
\]

This is an improvement by the **exact factor** `53526/5643` (approximately `9.49`) over the earlier uniform numerical floor `5643*delta/51^6`. Crucially, the exponent 6 and the separately unknown positive graph SS6 constants C,c (hence delta and h0) are **unchanged**. This is a stronger lower-risk coefficient, **not** a new global ASET exponent, a strict R2/R3 upper bound, a claim of R3=the displayed lower sum, or an obstruction beyond the specified GQ/classical-alteration model.

## 7. Independent CI, limits and next gate

The slice contains:

* `research/hyp105_sharp_signed_r3_floor_referee.py`: all ten signs of the original D6; exact full-ten totals for all nine BBo templates; verified sharp root coefficients; full source-ID physical C4 inverse construction for *all nine actual W32/W34 planted original-sixset lifts* and the full original D6 lift.
* `research/test_hyp105_sharp_signed_r3_floor_referee.py`: **7 independently scoped test groups**, all 100 colored signed cases checked by BOTH inclusion/exclusion and primal tree-current solutions, source-ID-preserving nine-lifts on both real finite symplectic GQs, all ten actual D6 signs, signed-column permutation invariance, exact fixed-risk inequalities and invalid-input rejection.
* `.github/workflows/hyp105-sharp-signed-r3-floor-referee.yml`: Github-hosted Ubuntu 24.04 / Python 3.12 exact-head specialist tests. Verify `Research` and `INDEX` workflows independently on the final source SHA before reporting PASS.

**Scientific STOP:** no qualified external scientific referee of the global geometric universal D6+BBo lower, no automatic mathematical acceptance or merge, no changes to parent PRs, no issue closure. The exact finite GF5 signed-weight coefficients are now sharper but the root #230 acceptance remains `OPEN_WITH_FORMAL_BLOCKER`. Next prioritize actual qualified scrutiny of #659/#672's global geometric argument and independent provenance of all six original IDs; avoid presenting internal CI as independent external peer review.
