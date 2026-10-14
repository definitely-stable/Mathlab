# HYP-105 / #230 — JPKC-015: exact uniform global-injection D6 ensemble

**14 October 2026.** Strict research-only child of JPKC-014 Draft [PR #447](https://github.com/definitely-stable/Mathlab/pull/447), parent HEAD `450e0d051216e42bf1af2bdebafdb0fddfedc4b6`. Work only in `research/hyp105-issue230-jpkc015-ensemble-d6-capacity`; main untouched. Root A/B OPEN.

## 1. Why this is a meaningful next source-capacity step

JPKC-014 gave an original-incidence-disjoint source factor-choice matching certificate S>=8 for two genuine W32 24-state right assignment fibers (full S minimum 68), but no all-h positive factor-image-star guarantee or Ω(s^6) lower for EVERY globally injected f,g. Merely obtaining one positive source-sixset per original line could only produce Θ(s³), since each original W(3,s) side has V=(s+1)(s²+1)=Θ(s³) source factors.

To test whether the target s^6 exponent is combinatorially natural, compute an **exact all-h ensemble expectation** for the D6 subset under independent **globally injective** original factor maps f,g. This is a strong but strictly different quantifier from Root A. Global point and line labels cannot repeat physical pairs, even across distinct Q: the ensemble samples two entire injections, NOT independent physical edge labels for each incidence.

The physical alphabet uses MINIMAL a=a(s) with N=C(a,2)≥V. If a grows arbitrarily faster, the claimed asymptotic scale is not invariant, so the minimal-alphabet hypothesis is mandatory.

## 2. J51 — exact probability of named ORIGINAL column D6 alignment

Let Q consist of six TRUE ORIGINAL incidence IDs (p_i,l_i) with six distinct original p_i and six distinct original l_i. This is exactly a six-edge MATCHING in the original GQ bipartite incidence graph, not a physical path, not a local P3 event and not a general arbitrary six-original-edge set with repeated factors.

Choose f and g independently and uniformly over all complete injections of the V original points/lines into the N distinct physical K_a pair labels. For each Q, the induced six pair labels on either half form a uniformly random ORDERED six-tuple of distinct physical pairs among (N)_6 ordered possibilities.

D6 is the event that the left and right physical six-coordinate 2-regular projections produce the SAME connected cycle dual on the six NAMED ORIGINAL incidence positions (the historical exact `classify_seven_prechecked` condition, without overcounting signs). There are (6−1)!/2=60 unoriented Hamiltonian cycles D on six named column positions. For a fixed D, each of its six dual edges must receive a distinct physical coordinate, in (a)_6 injective assignments, and these assignments uniquely induce six pair labels on one side. Thus there are exactly 60 (a)_6² favorable ordered left/right physical six-label assignments out of (N)_6² equally likely pairs of tuples:

`p_D6(a)=60*((a)_6/(N)_6)^2`.

This counts each original sixset once, each named dual once; the distinct-left/right source factor hypothesis is essential.

Independent counting control: on a physical K_a graph, independently choose six physical coordinate vertices C(a,6), one undirected Hamiltonian C6 ((6−1)!/2 choices), and a bijection of six named original incidence columns to the six physical C6 edges (6! ways), yielding `C(a,6)*60*6! = 60(a)_6`. This matches the dual-edge assignment count without reusing the dual construction.

## 3. J52 — exact all-h ensemble expectation and sharp asymptotic constant

Let d=s+1, V=(s+1)(s²+1) and M=V*d. The original bipartite incidence graph of W(3,s) has V point vertices, V line vertices, and is d-regular with M ORIGINAL incidence edges. Let M6(s) be the number of six-edge ORIGINAL incidence matchings.

By exact linearity of expectation, irrespective of dependence between D6 events of different Q (which is crucial):

`E_{uniform independent global injections f,g}[D6] = M6(s) * 60*((a)_6/(N)_6)^2.`

**Rigorous greedy source-matching squeeze:** After choosing j<=5 vertex-disjoint ORIGINAL incidences, at most 2jd other ORIGINAL edges are forbidden by their chosen source point or line endpoints. Therefore the number of ordered length-six original source matchings is at least `Π_(j=0)^5(M−2jd)`, and at most `(M)_6` (choose distinct source edges without respecting endpoints). Divide by 6! to obtain

`Π_(j=0)^5(M−2jd)/720 <= M6(s) <= C(M,6)`.

Since V>=15 for s>=2, `M−10d=d(V−10)>=M/3`; all terms positive. The physical minimal a satisfies `a²>=2V` and `N=C(a,2)<2V`, and for a>=6, `(a)_6 >= (a/6)^6`, `(N)_6<=N^6`. Consequently for EVERY s=2^h with h>=1,

```
E[D6] >= (s+1)^6 / (12 * 3^6 * 6^12 * 2^6) > 0.
```

Hence **E[D6]=Ω(s^6)** in the declared independently globally injected minimal-K_a ensemble. This is an all-h proved positive LOWER bound for the AVERAGE, NOT for every f,g. In particular, average positivity cannot contradict fixed legal globally injected W32 S68/S72 maps with D6=0.

A stronger asymptotic follows using the two bounds: for s→∞, `M6(s)~M^6/720`, since d/M=1/V→0; minimal a has `N/V→1`, `a²/V→2`; and falling factorials of length six are asymptotically powers. Thus

```
E[D6] ~ (M^6/720) * 60 * ((a^6/N^6)^2)
      ~ ((V(s+1))^6/720) * 60*2^6/V^6
      = (16/3)*(s+1)^6 ~ (16/3)*s^6.
```

The constant 16/3 is for the D6 **six-original-incidence set count**, not all seven classes, not full GF5 R3, and not a worst-case global f,g minimum. Since each accepted D6 has a previously certified GF5 necessary R3 floor numerator 5643, the ensemble average of that selected positive-class GF5 necessary floor is at least `5643*E[D6]/51^6`, without implying a full risk upper/lower beyond its proper existing context.

## 4. J53 — independent exact ORIGINAL W32 count and physical cycle oracle

A new finite DP computes M6(W(3,2)) from actual ORIGINAL incidence edges independently of physical pair label assignments or historical `seven_census`. Process all 15 original left point factors, skipping each or matching it to one of its three true incident ORIGINAL right line IDs not selected earlier. A bitmask over ORIGINAL right source line IDs records the selected lines, and the terminal six-bit masks sum exact six-edge source matchings. Repeating with the two original bipartitions swapped must yield exactly the same count. The exact expectation then becomes `M6(W32)*p_D6(6)`.

Additionally the physical C6 named-column Hamiltonian count is computed independently on a=6,7,8,12,20 physical coordinate alphabets, and exact rational ensemble expectations are consistent across true original W32 lex, reverse, S68, S72 fixtures, because only true ORIGINAL host structure — not their physical f,g — determines the ensemble mean.

Original W34 *full* seven-GF5 Q census is deliberately not invoked or asserted. For all-h bounds the implementation needs only V,d and factorial products, not any full W34 source enumeration.

## 5. Scientific limitation, acceptance, and next step

A mathematical theorem about **expectation** proves existence of some high-S legal maps, but cannot preclude other very-low-S globally correlated maps. To move toward Root A, the next task is a UNIFORM lower-tail guarantee (or a deterministic all-label source capacity inequality), which cannot follow from the first moment alone. Exact second moments must account for genuine ORIGINAL 6-matching overlaps, shared source points and lines, and both complete globally injective pair label maps. Even a small second moment alone does not show every assignment has S>=c*s^6. Independent minimax/adversarial f,g is the genuine blocker.

Required: 5 fail-closed hosted tests, dedicated independent source-DP and asymptotic bounds CI, INDEX, Proof Audit, Full Research SUCCESS on EXACT final HEAD and separate mathematical proof audit. No main merge, no new ASET exponent, no all-label universal S lower, no infinite correlated counterfamily.

## 6. Independently hosted exact finite validation (W32)

The initial final-current specialized GitHub-hosted workflow completed **5/5 jobs SUCCESS**: five fail-closed structural tests; four true W32 physical-label fixture jobs, each independently counting ORIGINAL six-edge incidence matchings with the left/right bipartitions swapped.

The exact W(3,2) ORIGINAL incidence host has **1,566,360** distinct six-edge bipartite matchings, as independently computed by both orientations of the original incidence DP; this number is invariant under the lex, reverse, S68 and S72 physical-label fixtures because it belongs to the source geometry, not the physical injection.

With a=6 and N=C(6,2)=15, the physical connected D6 left/right dual alignment numerator counts 60*(6)_6=43,200 named six-edge physical C6 labelings per side, independently reproduced by physical graph C6 vertex/edge slot counting. Therefore the **exact ensemble expectation** is

`E[D6]=1,566,360 * 60 * ((6)_6/(15)_6)^2 = 3,759,264 / 1,002,001 ≈ 3.75175673477.`

This finite positive expectation coexists with admissible fixed globally injected S68/S72 maps having **D6=0**, so it CANNOT be cited as a universal worst-case positive D6 claim. The average D6 count is not expected to equal any particular physical labeling's observed D6 count.

At s=2 the analytic greedy-matching interval (before independent exact matching calculation) yields
`6561/4004 <= E[D6] <= 253872/13013`; the exact expectation lies inside. At s=4,8,16 the analytic bounds remain positive, with minimal physical coordinate alphabets a=14,35,94 respectively, and both bound sequences divided by s^6 converge to 16/3 as shown algebraically in J52.

**Acceptable conclusion:** we have a bona fide all-h Ω(s^6) **FIRST-MOMENT** theorem in one specified random globally injected physical-pair ensemble. The critical all-label obstruction to issue #230 Root A, or a genuine infinite low-S correlated Root B counterfamily, remains unsolved; worst-case cannot be inferred from an average.
