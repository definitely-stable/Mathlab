# HYP-105 #230 — AA4-SELECTOR-MOMENT-JOINT: independent original all-h common-priority and expected fourth/sixth referee

**Status: OPEN_WITH_FORMAL_BLOCKER.** Strict Draft child of frozen [PR #785](https://github.com/definitely-stable/Mathlab/pull/785), exact base HEAD 51f339cd999431d5da265afc4377008a7d44701f. Parents, main, sibling PRs and issue status MUST NOT change. No claim of ASET/GF5 strict exponent, unknown numeric graph C6 constants, or global ROOT PROVED_A. The *local* original all-h selector/moment implication is analyzed here without importing preceding mathematical implementations. Its novelty is an independently proved **direct priority-overlap integral lower bound** with a genuinely source-degree-weighted endpoint energy transfer, not an undocumented claim of discovering the already existing W_C/2 expected edge identity.

## 1. Original source model; one and the same global experiment

For any true original W(3,s), s=2^h, complete separately globally pair-injective ORIGINAL f:P→binom([a],2), g:L→binom([a],2), arbitrary fixed and arbitrarily mutually correlated, let C be a genuine named ORIGINAL flag CORE with two actual distinct physical diagonals per owner, original pencil-conflict J_C with maximum degree K_C and real H_C physical max degree Δ. Each physical edge belongs to exactly one named incidence source flag; no replacement by synthetic graph flags.

Choose ONE independent uniform continuous priority t_u for each u∈C and retain a source flag iff its priority is strictly smaller than ALL priorities of its neighbors in the original J_C. This produces one genuine source J_C-independent set S. Choose ONE global fair independent bit per first-coordinate physical symbol x, and ANOTHER global fair independent bit per second-coordinate symbol y; both symbol-bit families are independent of the priority variables. Retain an entire selected owner u=(p,ell) precisely when (a) u∈S; (b) its f(p) symbols have different x-bits; (c) its g(ell) symbols have different y-bits. Keep **BOTH** opposite physical diagonals of each such owner. The result Gω is a simple undirected physical graph BIPARTITE with respect to the first bit cut. All walks are evaluated in THIS single Gω; none receives separately resampled priorities or physical bits.

## 2. NEW self-contained all-h source survival proof by direct overlap integral

Take any genuine original coordinate-proper directed physical r-walk γ=(v0,...,vr) with r=2 or 3. For each first-coordinate and each second-coordinate sequence, all r+1 physical symbols are distinct. All its r real edge owners U={u1,...,ur} are pairwise different original point factors AND separately different original line factors: repeated point would repeat an unordered adjacent physical x pair; repeated line analogously repeats adjacent physical y pair. Hence owners U are pairwise NONADJACENT in source J_C. This is exact for any correlated f/g at all orders.

Let d_i=deg_J_C(ui). Condition on the priorities z=(t_u1,...,t_ur)∈[0,1]^r of these r target owners. Every external named SOURCE J neighbor w of U has a nonempty index set S_w={i:w∈N_J_C(ui)}. Since w is external (targets are independent), its independent priority must exceed max_(i∈S_w) z_i. Conditionally on z the exact probability ALL targets are source-local minima is

P(E_U|z)=prod_(w∈union_i N(ui)) [1−max_(i∈S_w) z_i]. (SM-1)

For any 0≤z_i≤1, 1−max_(i∈S_w)z_i=min_i(1−z_i)≥prod_(i∈S_w)(1−z_i). Multiplying across actual **distinct** external neighbors (including those shared by two or three owners), the right side becomes prod_i(1−z_i)^d_i. Integrate over the INDEPENDENT target-owner priorities z_i:

**P(E_U)≥prod_(i=1)^r∫_0^1(1−z)^{d_i} dz =prod_i 1/(d_i+1).** (SM-2)

This is a direct product integral proof for **every finite original J_C** and every pairwise J-independent owner set, requiring NO claim that E_ui are independent, and no invoking an unproved positive association condition. Shared external source neighbors can **increase** the probability over this conservative product bound. In particular d_i≤K_C gives P(E_U)≥(K_C+1)^(-r).

Given the entire one-global source priority experiment, the source condition is independent of the global physical bits. Each coordinate-proper r-path has r+1 DISTINCT actual x symbols. Exactly two alternating binary assignments of them survive all r x-edges, a probability 2^(-r); the y symbols yield an INDEPENDENT additional 2^(-r). Other actual source symbol bits are irrelevant to the fixed path but are NOT independently resampled by it. Therefore exactly

**P(γ survives the SAME global experiment) = 4^(-r) P(E_U)
≥4^(-r) prod_(i=1)^r 1/(d_i+1)
≥[4^r(K_C+1)^r]^-1.** (SM-3)

At ROOT K=10, q2=16(11)²=1936 and q3=64(11)³=85184. For arbitrary true original correlated f/g these are source graph bounds, not Monte-Carlo, finite extrapolation, or independent-per-path selection.

## 3. NEW source-degree-weighted proper-path energy transfer: all orders, SAME ω

For each physical ordered endpoint pair (a,b), define P_r(a,b) as the number of actual coordinate-proper directed r-walks of the UNSELECTED paired CORE H_C, r=2 or 3. For each such physical path γ with distinct actual named original owner flags Uγ let

w(γ):=prod_(u∈Uγ) 1/(1+d_J_C(u)).

Define the genuine weighted source original endpoint-path matrix

**W_r(a,b):=sum_(proper original γ:a→b) w(γ).** (SM-4)

The weight refers to the original SOURCE conflict degree, not physical degree, and depends on the path's real named owners; no synthetic source clone. Let X_r,ω(a,b) count those original coordinate-proper paths retained by the SAME global ω. By SM-3 and linearity of expectation, **entrywise**

E X_r,ω(a,b) ≥4^(-r) W_r(a,b)
≥ [4^r(K_C+1)^r]^-1 P_r(a,b). (SM-5)

For each actual endpoint a,b, scalar Jensen gives (EX)^2≤E X². On a finite common physical vertex universe (including isolates), sum all ordered endpoints. Since X_r,ω(a,b)≤(A_Gω^r)(a,b) entrywise and matrices are nonnegative, and A_Gω is real symmetric,

**16^(-r)||W_r||_F² ≤||E X_r,ω||_F²
≤E||X_r,ω||_F²≤E tr(A_Gω^(2r)).** (SM-6)

This is a NEW exact instance-adaptive source J-degree-weighted transfer that can improve individual source labelings beyond global K. The historical uniform assertion follows:

**||P_r||_F²≤[4^r(K_C+1)^r]^2 E tr(A_Gω^(2r)), r∈{2,3}.** (SM-7)

No Jensen step assumes survival indicators of different physical paths are independent. The same one global priority and two global typed cuts are retained throughout both r=2 and r=3 estimates.

## 4. Original expected selected edge law and bipartite sixth trace

For any named original CORE flag u separately, P(u wins priority)=1/(1+d_J_C(u)); the two independent global typed bit cuts retain its two original label pairs with probability exactly 1/4. Since each selected flag contributes TWO actual physical edges, linearity (not inter-owner independence) gives

**W_C:=sum_(u∈C) 1/(1+d_J_C(u));**
**E m(Gω)=W_C/2,  E tr(A_Gω²)=W_C.** (SM-8)

Crucially this is an expectation, NOT a pointwise m(Gω)≤W_C/2 bound. Also W_C≤|C|≤N.

For any fixed global outcome ω, the selected Gω is simple BIPARTITE; the uncut original H_C need NOT be bipartite. Every simple unoriented C6 contributes twelve rooted oriented closed sixwalks. Any other closed sixwalk in a simple bipartite graph contains an immediate length-two reversal: removing a marked reversal yields at most 6Δ tr(A_Gω⁴) possibilities. Thus

tr(A_Gω⁶)≤12 C6(Gω)+6Δ tr(A_Gω⁴). (SM-9)

For symmetric A, trace Cauchy (tr A⁴)²≤(tr A²)(tr A⁶)=2m tr A⁶. Young gives 6Δ tr A⁴≤0.5 tr A⁶+36m Δ², so

**tr(A_Gω⁶)≤24 C6(Gω)+72m(Gω)Δ².** (SM-10)

This is a theorem for ALL finite selected bipartite graphs; it is false to apply its immediate-reversal proof directly to potentially NONBIPARTITE H_C.

An independent original six-ID **C6→D6** source factor inverse is separately established in frozen PR #772; this implication needs a publication acceptance check in the global proof DAG. Under its exact premises (selected owners J_C-independent and BOTH global coordinate cuts), every selected simple C6 maps injectively to a historical D6 unordered original six-incidence-ID set, so **C6(Gω)≤D6_original(f,g)** for EACH fixed outcome. This source inverse is **inherited**, not independently re-proved or accepted here by checking only four flags.

Averaging SM-10 over one unchanged global probability space, and using SM-8:

**E tr(A_Gω⁶)≤24D6_original+36Δ²W_C.** (SM-11)

This is a complete mathematical implication CONDITIONAL on the distinct original C6→D6 acceptance; the independent sixth-walk derivation and global expectation algebra themselves are all-order. The bound is source-degree-weighted and does NOT use independent paths.

## 5. Independent across-outcomes fourth trace and the UNSELECTED physical core

For each fixed realization, spectral Cauchy gives tr(A_Gω⁴)≤sqrt(tr(A_Gω²)tr(A_Gω⁶)). Apply scalar Cauchy across outcomes, NOT equality through E sqrt:

**(E tr A_Gω⁴)²≤(E tr A_Gω²)(E tr A_Gω⁶)
≤ W_C [24D6_original+36Δ²W_C].** (SM-12)

Combine SM-6/SM-7, SM-11 and SM-12:

**||P3||_F²≤q3²[24D6_original+36Δ²W_C].** (SM-13)

**||P2||_F²≤q2² sqrt(W_C[24D6_original+36Δ²W_C]).** (SM-14)

For the ROOT no-deletion LOW branch if D6_original<δs⁶, δ≤1, Δ≤Ts, W_C≤N≤nu_Hs⁴, these yield exactly the separately inherited global constants

L6=24+ceil(36 nu_H T²),
q2=1936,q3=85184,
||P3||²≤q3² L6 s⁶,
||P2||²≤q2² sqrt(nu_H L6)s⁵.

Uncut source paired graph A_C² admits an ENTRYWISE DISJOINT decomposition A_C²=P2+B2, where B2 includes all length-two walks with at least one original coordinate return at endpoints (because physical diagonals always change BOTH typed coordinates). Thus

tr(A_C⁴)=||P2||²+||B2||². (SM-15)

The independently established all-s TRUE original source return formula from frozen #782 is **Qx(C)+Qy(C)=8|C|+4e(J[C])**. Since any entry of B2 is ≤Δ_C and its total mass ≤Qx+Qy, for ROOT H32 if the inherited source SRG J bound gives Qx+Qy<17s⁴,

||B2||²≤Δ_C(Qx+Qy)≤17Ts⁵.

Consequently the desired root uncut CORE trace fourth envelope is

**tr(A_C⁴)≤L4 s⁵,**
**L4=q2² ceil_sqrt(ceil(nu_H L6))+17T.** (SM-16)

The step from selected graph Gω to unselected H_C uses SM-7 and the DISJOINT endpoint decomposition; **it never transfers a bipartite conclusion directly to H_C**.

## 6. Consequence for improved #784/#785 original LOW root, and STOP

The original LOW threshold ledger from frozen #782 and enhancements #784/#785 now has separately established LOCAL proofs for the path partition and positive BBo six-ID inverse, the 17s⁵ FULL-GQ bad endpoint count, the source book 46(K+1)T squared coefficient, and the true coordinate-return 17T/49T. When the inherited original D6 source C6 inverse is accepted with exact hypotheses, SM-11 to SM-16 supply the remaining selected/moment transfer. Then numerical errors would be

W3>w s⁶,
I_coord≤49T s⁵,
I_endpoint≤E_NEW s^(11/2) with E_NEW=q3 ceil_sqrt(17L6),
I_fourblocker≤D_NEW s^(47/8) with
B0_NEW=ceil_sqrt(46(K+1)T), D_NEW=4 ceil_sqrt(B0_NEW T L4).

This composes conditionally into the already documented BBo_produced≥(w/64)s⁶ for sufficiently large s. However the **global** HYP-105 Branch A theorem remains **OPEN_WITH_FORMAL_BLOCKER** until an independent line-by-line publication referee validates the C6→D6 original six-ID injection, all root case/dichotomy quantifiers, original GF5 seven-class sign weights and actual external ordinary Simonovits graph C6 theorem provenance. Numerical C0,c0 remain unknown.

### New independently executable finite falsifier (not proof by extrapolation)

The new research/hyp105_selector_moment_joint_publication.py imports ONLY the independent genuine GF2/GF4 symplectic original GQ FIXTURE from frozen #784, not any prior selector, moment or Jensen computation. It extracts a genuine coordinate-proper 3path from real W(3,2)/W(3,4) lex/reverse/correlated complete globally injected maps, then adds one real ORIGINAL source J-conflicting owner to make a nontrivial 4-source-flag CORE. Independently reconstructs the source J_C and two REAL diagonals per owner.

Enumerates **ALL 4! actual relative source priority orders** and ALL actual relevant **global x/y bit colorings** for this CORE, SEPARATELY. Convolution of the priority-outcome and cut-outcome masks is exact because the two entire global experiments are independent, whereas individual owner events and different path survival events emphatically are NOT. The result is a full exact rational probability distribution on actual retained named owner subsets. Each subset produces one original simple physical graph; independently computes its m, traces 2/4/6, proper endpoint path matrices, the genuine point/line physical 2walk returns, and ordinary unoriented C6 census.

The source referee checks exact SM-8, per-outcome selected bipartite sixth-walk inequalities SM-9/SM-10, same-outcome spectral fourth Cauchy, global expected fourth bound SM-12, both uniform path Jensen bounds and the NEW weighted SM-6 for EVERY finite case, plus exact uncut SM-15 and original source Qx+Qy=8|C|+4e(J[C]). The r=3 source probability is tested by exact full priority orders against SM-2 and actual global two-cut bit masks, not by independently resampling physical paths. In this test there are **only 4 source owners**, so the selected true C6 count is necessarily zero under the full source hypotheses; this is intentionally disclosed as **not an independent positive finite test of source C6→D6** (that gate remains in PR #772).

Hosted GitHub Actions specialist + INDEX + full Research must be SUCCESS on exact final SHA. STOP on the FIRST false original source probability/moment/geometry implication, not on numerical root cosmetic improvements. Passing this 4-owner finite referee is engineering falsification evidence; the all-h mathematical claims rely on the explicit proofs SM-1–SM-16, not on finite testing.
