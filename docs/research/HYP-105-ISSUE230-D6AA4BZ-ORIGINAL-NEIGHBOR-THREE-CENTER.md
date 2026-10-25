# HYP-105 / #230 — AA4-BZ: genuine-original physical three-neighbor sixcube and improved seven-class center kernel

**Scientific Draft**, strict child of [AA4-BY #599](https://github.com/definitely-stable/Mathlab/pull/599), pinned parent SHA f1b6244c832559f062e4c5cbf560ed80fe6bc800. Every claim involves genuine original symplectic W(3,2^h), all h≥1, globally injected typed original physical point f and line g maps that may be arbitrarily correlated, and the same SIX DISTINCT original incidence IDs on both sides. Main and accepted results registry untouched; root #230 remains OPEN_WITH_FORMAL_BLOCKER.

## Source and mathematical prior art

[#597](https://github.com/definitely-stable/Mathlab/pull/597) already proved the conditional unchanged-center all-seven GF(5) selected necessary-risk weighted Fourier certificate for arbitrary fixed f,g using a general Boolean highpass constant η6=51/32. [#599](https://github.com/definitely-stable/Mathlab/pull/599) already established that, if six original sixflag Q meet six disjoint whole-source-LINE image-swap packets, their original right physical 2-regular acceptance indicator is an **independent set** in the 6cube. Its abstract-independent sharp highpass constant is η6=45/32; its negative extremizer consists of every vertex in Hamming layers 1 and 4. [#598](https://github.com/definitely-stable/Mathlab/pull/598) independently investigates a weighted C/A+C/B cubic approximation, not the all-seven bound.

Walsh Fourier analysis, Krawtchouk kernels, and radial layer inequalities are classical; see Ryan O'Donnell, *Analysis of Boolean Functions* (https://arxiv.org/abs/2105.10386). The following new scoped result is a stronger **TRUE physical edge graph** restriction on the original sixpacket Q, not a claimed general new Fourier theorem or a sharp real-world constant.

## BZ-N3 theorem — at most three accepted neighbors at EVERY cube vertex

Fix six PAIRWISE DISJOINT pairs of TRUE original LINE source-factor IDs. Let Q be SIX DIFFERENT genuine original incidence IDs touching all six packets. Because one original incidence has exactly one original LINE source factor, each packet supplies exactly ONE flag of Q; the six true original LINE source factors in Q are distinct. At any vertex x of the 64-state whole-original-LINE-factor-image-swap cube, the six right physical pair edges B={e_1,...,e_6} are ALL DISTINCT (global g^x injection), and the alternatives a_1,...,a_6 for flipping the six packet bits are ALSO mutually DISTINCT and distinct from all six baseline physical edges. No original sixflag ID or source geometry is changed by a swap.

Let R(x) indicate that these six distinct right physical unordered-pair edges form a 2-regular graph on exactly SIX physical coordinates, regardless of connectivity. Any historical GF5 seven-class accepted indicator I_Q(x) obeys 0≤I_Q(x)≤R(x). Then, for ALL dyadic h, every arbitrary correlated complete original f,g and every actual source Q as above,

\[
\boxed{\forall x:\quad
\sum_{i=1}^{6}R(x\oplus e_i)\le3,\qquad
\sum_{i=1}^{6}I_Q(x\oplus e_i)\le3.}
\tag{BZ-N3}
\]

**Proof, without a solver.** Assume at least FOUR distinct one-bit flips i in a set J replace baseline edge e_i by alternative a_i and yield valid 2-regular right physical projections.

First, every physical vertex has baseline B-degree at most TWO: degrees at least FOUR remain at least THREE after a one-edge removal, invalid; for baseline degree THREE, at least one of the four successful flips removes a DIFFERENT baseline edge, so its degree remains at least THREE, invalid.

Suppose two different physical vertices v,w have baseline degree ONE. Each belongs to at most one baseline e_i. Hence at least |J|-2≥2 distinct successful flips j remove edges touching NEITHER v nor w. In each such neighbor, a single newly inserted edge a_j must touch both v and w, raising both degree-one vertices to two. Thus at least TWO different original source LINE image swaps would require the SAME physical alternative pair-edge {v,w}, contradicting the global original g injection on the twelve actual packet LINE factors. Therefore at most ONE vertex has baseline degree ONE. Yet the number of odd-degree vertices in ANY finite graph is even (handshaking lemma), so in fact NO baseline vertex has degree ONE.

Six distinct baseline edges contribute sum of degrees 12 and each nonzero degree is now exactly TWO; thus B itself is 2-regular on exactly SIX vertices. But replacing exactly one physical pair edge by a DIFFERENT edge cannot preserve a simple 2-regular six-edge graph (parent #599's one-edge lemma). This contradicts even one accepted neighbor. Therefore at most THREE neighboring vertices of every x can be 2-regular, and the historical I_Q subset is also at most three. This argument uses the actual original-source complete physical pair-edge INJECTION; merely independent right images redrawn for each Q would not suffice. It does not require f/g independence or any fixed physical six-coordinate support across accepted vertices.

## Exact 7-layer rational highpass dual — eta6≤139/128

By XOR translating an arbitrary reference vertex x to the 6cube origin, the one-edge independent-set property (#599) and new at-most-three-neighbors condition remain valid. Write p_j as the fraction of accepted cube vertices among all binom(6,j) Hamming-weight-j vertices, for j=0,...,6. Thus 0≤p_j≤1. Averaging original edge-exclusion on consecutive layers gives p_j+p_{j+1}≤1. Averaging the N3 bound on layer j gives

\[
j p_{j-1}+(6-j)p_{j+1}\le3,\quad j=0,\ldots,6
\]

with absent boundary terms zero.

The exact cutoff-three 6cube Walsh highpass radial Krawtchouk kernel is K6(j)=(22,-10,2,2,-2,-2,10). Thus the unnormalized highpass output at this origin is

\[
T=22p_0-60p_1+30p_2+40p_3-30p_4-12p_5+10p_6.
\]

**Positive signed dual:** by dropping nonpositive terms and using p0,p6≤1, p2+p3≤1, 2p1+4p3≤3,

\[
T\le22p_0+30(p_2+p_3)+\frac52(2p_1+4p_3)+10p_6
\le22+30+\frac52\cdot3+10=\frac{139}{2}.
\]

**Negative signed dual:** by dropping nonnegative terms and using 6p1≤3, p4+p5≤1, 5p4+p6≤3,

\[
T\ge-60p_1-30p_4-12p_5
\ge-10(6p_1)-12(p_4+p_5)-\frac{18}{5}(5p_4+p_6)
\ge-30-12-\frac{54}{5}=-\frac{264}{5}.
\]

Because 264/5 is smaller than 139/2, dividing by the 64 vertices gives the all-h, all-original-Q pointwise highpass guarantee

\[
\boxed{\eta_6^{BZ}\le\frac{139}{128}
<\eta_6^{BY}=\frac{45}{32},\qquad
\Delta\eta_6=\frac{41}{128}.}
\tag{BZ-ETA}
\]

These are **explicit exact rational inequalities**, not reliance on numerical LP or a heuristic search. Fractional layer averages p=(1,0,1/4,3/4,0,0,1) saturate the displayed positive seven-layer relaxation and p=(0,1/2,0,0,3/5,2/5,0) saturates its negative relaxation. Such fractional layer profiles are **NOT necessarily realizable by a physical sixflag indicator**, and no sharpness claim is made for genuine original W3/GF5. Parent #599's abstract negative extremizer (ALL Hamming layers 1 and 4) has SIX accepted neighbors around 0, strictly violating BZ-N3; its independent-set sharp η6=45/32 is therefore not physically realizable.

## All-seven original fixed-pair center certificate improves without changing any low-order modes

For each fixed original physical f and chosen six source LINE swap packets, parent #599 defines a true original f-only eligible source-sixflag weighted mass

\[
H_6(f)=\sum_{Q\ {\rm genuine\ six\ ID},\ k_Q=6,\ c(Q)\ {\rm accepted}} w_{c(Q)},
\]

and a uniform error envelope E_f^BY covering the weighted seven-class GF5 historical necessary 51-column R3 numerator W(x) on ALL 64 complete globally injected right maps g^x. Only original Q whose original LINE source profile is A can hit all six packets: permitted historical sixth-order classes are D6, B-left/A-right, C/A.

Replacing the valid parent η6 bound with BZ-ETA and leaving all other packet support weights, every accepted class, the entire physical f and original g fixed yields

\[
\boxed{
E_f^{BZ}=E_f^{BY}-\frac{41}{128}H_6(f),\qquad
|W(f,g^x)-P_{\le3}W(x)|\le E_f^{BZ}
}
\]

for EVERY real original symplectic W(3,2^h), every fully fixed arbitrarily correlated complete original f,g and all 64 globally injected right-map vertices simultaneously. In particular for the ORIGINAL UNCHANGED complete physical f,g at x=0,

\[
\boxed{
W(f,g)\ge\max\{0,\ P_{\le3}W(0)-E_f^{BZ}\}.
}
\]

This is a **STRICTLY stronger but CONDITIONAL** original-center seven-class lower certificate than #599 when H6(f)>0. We have NOT proved any universal all-h positive lower margin for P≤3W(0)-E_f^BZ, and the full R3 numerator also includes motifs beyond the seven selected GF5 classes. Accordingly this does NOT close root #230 Branch A, an infinite actual W3 correlated o(s^6) Branch B or a qualifying Branch C model-equivalent reduction.

## Reproducible independent genuine-original falsifiers and exact finite evidence

The additive 3-job dedicated GitHub-hosted workflow covers six test groups:

1. Exact rational radial kernel K6, all original inequalities and fractional dual saturation, with an independent finite 7-dimensional rational checker, and strict η6=139/128 <45/32.
2. Genuine W32 symplectic complete globally injected physical K6 lex/S72 f,g. ALL 351/301 authentic sixth-packet eligible six-ID source Q are independently evaluated on ALL 64 complete original LINE map states; EVERY vertex's six physical 2-regular neighbor count ≤3 and actual accepted GF5 Q is a subset. No random source-Q redraw.
3. A completely independent exhaustive PHYSICAL-K6 check over ALL 5005 possible sets of six distinct physical K6 edges (choose(15,6)), checking all nine unused alternative edges per removed edge and selecting a **MAXIMUM matching** between original packet indices and distinct alternative physical images. Exact histogram of maximum feasible neighbor replacements: 2665 cases with 0, 1260 with 1, 720 with 2, 360 with 3. Physical K6 is an independent finite falsifier, not the all-h source theorem.
4. On real symplectic W32 lex/S72, the parent historical FULL seven-GF5 64-map selected weighted source-census center and parent f-only error improve by exactly Δeta6 times the genuine f-eligible sixth-packet weighted source mass. This error is unchanged after an adversarial complete permutation of right original g.
5. Invalid original packet overlap/count, physical image injection and source-ID guards fail closed.
6. The parent abstract independent-set negative extremizer has SIX accepting neighbors, so cannot represent genuine original physical sixth-packet Q even though it is abstract-independent; a specific no-go to sharp physical realization, NOT a counterfamily for root Branch B.

The complete f-only W32 exact predictions (subject to final-head checks) are:

| True original W32 | eligible k6 source Q | H6(f) | #599 E_f | New BZ E_f | additional saving |
|---|---:|---:|---:|---:|---:|
| lex | 351 | 4690929 | 16297231477/32 | 64996597819/128 | 192328089/128 |
| S72 | 301 | 3731790 | 7794829287/16 | 31102815453/64 | 76501695/64 |

The ACTUAL selected necessary R3 weighted original GF5 score W(0) in these two genuine W32 schemes equals 11225795 and 3283610 respectively (verified in parent). The NEW conditional lower remains zero for both, demonstrating that a tighter source-GQ highpass error alone is insufficient to prove Branch A.

## Credit / mathematical acceptance / next proof frontier

Classical Fourier-Walsh foundations: Ryan O'Donnell, *Analysis of Boolean Functions*, arXiv:2105.10386. Degree-parity counting and LP duals are elementary prior mathematical tools; no published-literature priority or fully sharp original-GF5 extremal constant is claimed for BZ. The correct next step for root #230 is a TRUE original f/g cross-class zero/low-order signed inequality strong enough to force a positive original-center seven-class count, or an actual infinite correlated original W3 o(s^6) counterfamily. A further physical graph refinement may reduce the error but does not remove this logical blocker.

Keep **Draft** until final HEAD dedicated/INDEX/Proof Audit/Full Research CI and independent qualified mathematical referee of the exact all-h degree-one parity proof, all ancestor branches and claim interpretation. Do NOT merge, edit canonical accepted registry, or close issue #230 on green CI alone.
