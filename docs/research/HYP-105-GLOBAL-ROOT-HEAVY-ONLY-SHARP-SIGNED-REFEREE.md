# HYP-105 / issue #230 — AA4-ROOTSHARP: independent end-to-end original-source proof of a heavy-only sharp GF(5) risk floor

**Scientific result, directly reviewed and implemented in this slice.** This
document derives a new quantitative corollary of the fixed-map
ORIGINAL-source Branch A proof chain in #659/#672/#679/#697/#701/#703/#704,
together with independently verified #707 R5 and #708 R6.
It is stacked strictly on frozen Draft #708 HEAD
`604f8b874971785f9a4520f39735a28aa1bedb85` and does not
mutate ancestors or main.

**New result:** the older sharp R6 risk certificate
`min(54162*delta,53838/8)*s^6/51^6` is NOT the strongest consequence of
the already-proved dense-root three-path inequality. A slightly stricter,
constructive dyadic threshold eliminates the dense-branch minimum:

\[
\boxed{R_3(f,g)\ge\frac{54162\,\delta}{51^6}\,s^6.}\tag{ROOT-SHARP}
\]

This holds for every sufficiently large dyadic s and **every complete
separately globally pair-injective arbitrarily correlated FIXED f,g** in
the TRUE original symplectic W(3,s) model, conditional on the explicitly
named graph C6 supersaturation theorem and historical original-source
lemma chain. The all-h algebraic implication is proved here; GitHub
tests audit the constants, provenance and exact arithmetic. It does
not improve the ASET exponent or claim an individual deterministic
GF(5) coefficient assignment is forced to collide.

## 1. Exactly what is fixed, counted and random

For each h>=6 put s=2^h, true W(3,s) source with
`V=(s+1)(s²+1)` original points and original lines and
`N=(s+1)V` distinct original incidence flags.
Let `a=min{j: binom(j,2)>=V}`. Fix **once** complete separately
pair-injective, possibly maximally correlated original typed label maps
`f:P->binom([a],2)`, `g:L->binom([a],2)`.
Every ORIGINAL incidence flag retains its unique immutable ID and
contributes **both** opposite-corner physical diagonals.

`D6` counts original six-distinct-flag matching cycle sixsets, and
`U_prod` counts DISTINCT ORIGINAL B/B-overlap sixsets in the image
of good, unblocked, coordinate-proper three-edge physical paths with
three original CORE owner flags. All three full original
`q--ell--p--r` projection anchors may lie OUTSIDE CORE; that is
essential in the R5/R6 source-to-risk bridge.

The GF(5) risk quantity `R3` is the **SUM of the probabilities of all
ten balanced 3+3 signed events**, with independently uniformly random
51-valued nonzero checksum-4 weight patterns on each original column.
It is NOT a ten-event union probability, and NOT a statement about
every individual deterministic assignment.

## 2. Re-derive heavy-tail and ORIGINAL core once, with exact invariants

For all genuine s>=64, the exact source books obey
`M_f,M_g<=C_s=(s²+1)(s²+a-2)<(6/5)s^4`. In particular the source
conflict graph of L actual ORIGINAL heavy flags has at most `2C_s`
edges, and Caro–Wei followed by two whole-flag binary physical
coordinate cuts gives at least

\[
|I_G|\ge\frac{L^2}{4(4C_s+L)}.
\]

For the FULL physical degree-tail mass `E_T>=epsilon*s^4`, every
original flag owns exactly two distinct edges, so there are
`L>=epsilon*s^4/2` actual heavy ORIGINAL flags. Using the source
book bound gives the exact selected heavy fraction

\[
\epsilon=1787/4096,\qquad
\beta=\frac{5\epsilon^2}{384+40\epsilon}>0.
\]

Every retained original flag retains BOTH diagonals, including its
heavy witness. The genuine balanced physical subgraph construction,
with `T>=2^{19} C_graph^3 / beta^3`, yields an ordinary
simple C6 count from the published balanced graph supersaturation
theorem and the original physical-C6-to-D6 inverse:

\[
E_T\ge\epsilon s^4
\ \Longrightarrow\ 
D_6(f,g)\ge c_{graph}(\beta/32)^6s^6.
\tag{H}
\]

Here `C_graph,c_graph>0` are genuine but NUMERICALLY UNSPECIFIED
existential theorem constants. Never set them to 1 to claim an
unconditional actual numerical dyadic h0.

Define any sufficiently large REAL `T>=max(1,2^19 C_graph³/beta³)`
and

\[
\boxed{\delta=\min\{1/8,c_{graph}(\beta/32)^6\}.}\tag{DELTA}
\]

Then for each fixed f,g either `D6>=delta*s6` (HEAVY branch)
or `E_T<epsilon*s4` by the contrapositive on the SAME maps (DENSE
branch). The independently proved **true ORIGINAL** core budget
\[
\frac Ns^4-\frac12-\frac{C_s}{16s^4}
\ge\frac7{16}-\frac{38245}{33554432}
>\epsilon
\]
ensures deleting the heavy-source flags and original conflict-degree
`>K=64` flags leaves a paired ORIGINAL physical CORE with
`m_0>=s^4`, physical `Delta_0<=Ts`,
original conflict maximum <=64 and unchanged FULL projection anchors.
The Python referee independently reconstructs the true exact
`N,C_s,a` and this budget for all h=6..25 as finite falsifiers.
The all-h budget is the analytic inequality above.

## 3. Re-derive the complete original proper-path loss ledger

The historically proven independent-priority original selector bounds
for any ONE proper r-path, followed by two physical cuts, are

\[
\sigma_2^{-1}=16\cdot65^2,\qquad
\sigma_3^{-1}=64\cdot65^3.
\]

Different physical-path selection events need NOT be independent or
positively correlated; #706 constructs original full-W(3,s)
negative-covariance witnesses. The proof correctly uses linearity of
expectation for each fixed path, followed by Jensen.

In the dense case `D6<delta*s6`, selector C6 source injectivity and the
ordinary bipartite sixth-moment inequality give

\[
L_6=24+288T^2,\qquad
L_4=2\sigma_2^{-2}\sqrt{8L_6}+56T.
\tag{MOMENTS}
\]

The full original-source exceptional endpoint and all FOUR genuine
FULL/CORE blocker estimates (the latter checked directly in #707)
give the independent path-loss constants

\[
E=8\sigma_3^{-1}\sqrt{L_6},\quad
B_0=15\sqrt{65T},\quad
D=4\sqrt{B_0TL_4}.
\tag{LOSSES}
\]

These original-source bounds do NOT require the full source projection
anchors to survive CORE. From the entire original core density and
weighted walk estimates one has the actual directed physical
proper-path lower bound

\[
\boxed{
2U_{prod}\ge\frac{s^6}{2}
              -84Ts^5-Es^{11/2}-Ds^{47/8}.
}\tag{P}
\]

The `2` on the left is EXACTLY the two directed reverse physical
paths per produced DISTINCT ORIGINAL B/B-overlap sixset, not double
counting from two original physical diagonals. #708 independently
establishes that its generated image lies only in the three aligned
ORIGINAL BBo templates, each with EXACT ten-sign GF5 mass 53838.
The six unaligned BBo templates, each with total 53526, are NOT
included in U_prod and cause no loss here.

Divide (P) by 2s^6 and keep ALL three vanishing errors, instead of
prematurely replacing the result with `1/8`:

\[
\boxed{
\frac{U_{prod}}{s^6}\ge\frac14-\Lambda_s,\quad
\Lambda_s=
\frac{42T}{s}
+\frac{E}{2\sqrt{s}}
+\frac{D}{2s^{1/8}}.
}\tag{FINITE-DENSE}
\]

For each fixed actual positive theorem constants and fixed T, all
three right-hand error terms decrease as s increases and tend to 0.

## 4. NEW exact uniform heavy-only threshold, with NO unknown numeric constants

The sharp accepted original sixset GF5 inequality is

\[
51^6R_3(f,g)\ge
54162D_6(f,g)+53838U_{prod}(f,g).
\tag{GF5}
\]

The source sixset classes are DISJOINT because D6 has original
point/line matching factor profiles and BBo repeats an original point
and original line. The right-hand side is a sum over distinct six
original incidence IDs and distinct signed events, NOT a union.

If we are in the HEAVY case, (GF5) immediately yields
`51^6R3>=54162*delta*s6`.

In the DENSE case use (FINITE-DENSE):

\[
51^6R_3\ge53838(1/4-\Lambda_s)s^6.
\]

Crucially `delta<=1/8`. Therefore it is ENOUGH to make

\[
\Lambda_s\le\eta_*:=
\frac14-\frac{54162}{8\cdot53838}
=\boxed{991/7976}.
\tag{ETA}
\]

Then `53838*(1/4-Lambda_s)>=54162/8>=54162*delta`,
so the dense branch gives the **SAME universal lower bound as
the heavy branch**, proving (ROOT-SHARP) for the SAME fixed maps.

**This is genuinely stronger than the previous global min formula.**
At the artificial maximal delta cap `delta=1/8`, the older
`min(54162*delta,53838/8)` was limited by
`53838/8 < 54162/8`. The new proof removes this limitation
at the cost of requiring the slightly smaller error
`eta_*=991/7976<1/8` at a (possibly slightly larger) sufficient h.

For EVERY positive (unknown) real graph constants, T,E,D are finite;
hence such a dyadic threshold exists. A direct **constructive
symbolic sufficient threshold** can be obtained by allocating each
positive term of `Lambda_s` at most `eta_*/3`:

\[
s\ge\max\left\{
64,\frac{126T}{\eta_*},
\left(\frac{3E}{2\eta_*}\right)^2,
\left(\frac{3D}{2\eta_*}\right)^8
\right\}.
\tag{H-STAR}
\]

Round s upward to the next dyadic 2^h. The testing implementation
uses only **exact rational ceilings of radicals** (integers and
Fraction) and verifies each relative loss explicitly for the
supplied HYPOTHETICAL rational C_graph,c_graph. The real
mathematical result remains fully symbolic; trial values 1,1 etc.
are regression inputs, NOT attributed to Simonovits/Jiang–Yepremyan.

## 5. NEW finite-h quantitative tradeoff (not merely asymptotic)

No need to wait until (H-STAR) to have a mathematically valid,
if possibly zero, finite-h inequality. Under the original premises
for every dyadic s>=64 and ANY fixed admissible f,g, use
`[u]_+=max(0,u)`:

\[
\boxed{
R_3(f,g)\ge
\frac{s^6}{51^6}
\min\left\{
54162\delta,\quad
53838\left[\frac14-\Lambda_s\right]_+
\right\}.}\tag{FINITE-RISK}
\]

Proof: in the heavy case use the first term; in the dense case use
the second term together with the nonnegativity of U_prod. The
pointwise minimum is a common lower bound, with no assumed map
distribution and no claim of a positive finite bound if the relative
error is still large.

The code independently verifies this tradeoff at and above the
symbolic threshold and clips a possibly negative dense formula to
zero below threshold. It also returns a current h certificate
without any derivative estimates or numerical floats.

## 6. A stronger asymptotic interpretation and its limits

As s grows dyadically, `Lambda_s ->0`, giving
`liminf U_prod/s^6 >=1/4` WHENEVER the dense case is selected.
Because `53838/4 > 54162/8`, the **uniform** full-root
`liminf 51^6 R3/s^6 >=54162*delta` follows with the stronger
finite-threshold statement already proved in Section 4.

This is a precise nontrivial improvement of the quantitative
original-source risk obstruction, **not** a new ASET exponent.
A lower bound for the signed-event expectation over random GF5
coefficients does not rule out special deterministic coefficient
choices, nor alternative source geometries, alternate extraction
methods, or non-GQ constructions. It does not provide numerical
published graph C6 constants or assert a finite optimal h0.
A theorem of **all** ASET configurations is not implied.

## 7. Independent self-review and acceptance

The referee script
`research/hyp105_global_root_heavy_only_sharp_signed_referee.py`
imports NONE of the historical root/selector calculators or R6 code.
It independently reconstructs all rational heavy/Caro–Wei factors,
CORE budget, sigma inputs, sixth/fourth moment upper coefficients,
exceptional and four-blocker constants, the NEW root target and the
full fixed-map GF5 coefficient. It uses exact integer upper
square/eighth roots to certify h thresholds. Test code ONLY compares
its historical inputs to frozen #704's separate calculator. An
independent exact finite source oracle checks true dyadic
`a,V,N,C_s` and their implications, including non-even h.
The output deliberately identifies every numerical C,c parameter
as HYPOTHETICAL unless genuine published values are supplied.

**Mathematical audit result:** the known Branch A original-source
lemmas and new R6 proof imply (ROOT-SHARP) with no new probabilistic
independence assumptions. This closes the quantitative gap between
the heavy and dense branches in the assembled lower bound, but does
not claim to be a separate foundational re-proof of all 13 earlier
source lemmas, nor does it replace the source's general asymptotic
graph supersaturation theorem. Keep scientific #230 status
`OPEN_WITH_FORMAL_BLOCKER` until the underlying theorem is actually
accepted under repository governance; no merge to main is authorized.

**Next mathematically consequential investigation:** deterministic
GF5 column assignment / conflict-hypergraph extraction on the SAME
original fixed f,g, or a genuinely different geometry. More purely
constant-only Draft slices are not a priority.
