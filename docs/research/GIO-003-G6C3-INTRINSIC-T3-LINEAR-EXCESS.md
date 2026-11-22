# GIO-001.3 / G6-C3 — intrinsic all-order HEAVY/LOW with linear Moore excess

**Issue:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), meta [#790](https://github.com/definitely-stable/Mathlab/issues/790); **stacked dependencies:** [G6-C1 #802](https://github.com/definitely-stable/Mathlab/pull/802) and [G6-C2 #803](https://github.com/definitely-stable/Mathlab/pull/803) with exact tested prerequisite HEADs `8932e4c76c2d04c3e1c15f7f56f15a50a7d8f918`, `bc82adeef2574c1985cca49b786d3b3447f1758d`. This manuscript extends **accepted original HEAVY/LOW combinatorics of #230/#799** by explicit substitution of G6-C1/C2 **intrinsic non-GQ** lemmas. It does not assume the new incidence graph is a generalized quadrangle or arose by a GQ edit. It does rely on the published **ordinary** C6 supersaturation theorem and on the already accepted shared-priority/coherent-cut LOW moment lemma, which is identified rather than concealed.

## 1. Theorem T3-L (conditional on fixed linear Moore excess, no GQ)

Fix **two integers b≥1 and C≥0**, both BEFORE choosing an arbitrary source, factor maps or an asymptotic family. Let `I⊆P×L` be an *actual* finite simple incidence graph of girth at least eight. Every original point belongs to exactly t+1 lines and every original line contains exactly s+1 points, with integers s,t≥2; let

`r=min(s,t)`, `max(s,t)≤br`,
`Delta_L=|L|−(t+1)(st+1)`, `0≤Delta_L≤Cr`.

The dual excess `Delta_P=|P|−(s+1)(st+1)` automatically satisfies `(t+1)Delta_P=(s+1)Delta_L`. **No** connectivity, source projection-completeness, distance-regularity, field, classical/nonclassical GQ representation, hidden GQ supertemplate, or actual existence assumption beyond the displayed source itself is made.

Fix **arbitrary** complete globally separately injective point- and line-factor unordered-pair maps `f:P→binom([aP],2)`, `g:L→binom([aL],2)` using **their minimal separate alphabets**. The maps may be adversarial, correlated with each other and source, and need not be random. Each original source flag receives its distinct named ID; its physical graph consists of two opposite diagonals in the rectangle `f(p)×g(ell)`. For any set of adversarial source-flag deletions `Z⊆I`, let A=I\Z.

**Theorem T3-L.** There are **positive** constants `rho_(b,C)>0`, `delta_(b,C)>0` and integer `r0_(b,C)` (also depending on the fixed existential ordinary-graph C6 theorem constants), determined only by these *fixed parameters*, such that for every actual I, f,g satisfying the conditions and every `|Z|≤rho_(b,C)*r⁴`, `r≥r0_(b,C)`,

```
D6_A(f,g) + BBo_produced,A(f,g) ≥ delta_(b,C) r^6.
```

Here D6 is the **historical original six distinct named flag** D6 source class. `BBo_produced,A` means only sixsets **actually produced** by proper physical CORE threewalks with ALL three **genuine original surviving** projection anchors in FULL A, including the strict original repeated-point/repeated-line + shared middle anchor condition, never a fabricated full GQ projection. It is a subset of historical BBo. The proof gives either sufficiently many original D6 in HEAVY or sufficiently many actually produced aligned BBo in LOW. **This is a conditional structural theorem with the strict extra hypothesis `Delta_L≤Cr`**, NOT the unrestricted T3 for arbitrary non-GQ graphs, NOT an ASET exponent upper bound.

**Nonvacuity vs scientific novelty:** The class includes *all sufficiently large existing GQ* with `Delta_L=0`. The result does **not** prove there is an infinite sequence of genuinely non-GQ sources with `0<Delta_L≤Cr`. A finite doubled GQ has `Delta_L=Theta(r³)` along large GQ families and does not supply such an example. A mathematical referee must separately examine small-excess feasibility before claiming new infinite non-GQ applications. In particular `C=0` forces complete original projection (a GQ), and the G6-C3 theorem then specializes to existing #799. This reduction is a feature, not proof of an unconstrained new class.

## 2. Intrinsic input ledger, with no silent SRG/GQ inheritance

Put

```
V_P0=(s+1)(st+1),  V_L0=(t+1)(st+1),
V_P=V_P0+Delta_P,   V_L=V_L0+Delta_L,
N=|I|=V_P(t+1)=V_L(s+1).
```

Girth≥8 implies every nonincident pair (q,ell) has **at most one** original length-three projection. Exactly `V_P Delta_L` pairs have **none**. Each named original source flag appears in exactly `3st` existing original three-flag projections. These are G6-C1 counts, not an invented full-GQ projection.

From G6-C1 let A_P,A_L be genuine point/line collinearity graphs. Their exact defect-corrected identities are

```
A_P^2=(kP-muP)I+(s-t-2)A_P+muP J-D_P,
A_L^2=(kL-muL)I+(t-s-2)A_L+muL J-D_L,
muP=t+1, muL=s+1.
```

D_P,D_L are **symmetric entrywise nonnegative** and each has constant row sum `d=(s+1)Delta_L=(t+1)Delta_P`. They are NOT automatically PSD (two W32 copies give exact eigenvalue -45). The centered operator norm `||D||≤d` supplies conditional spectral cap O_(b,C)(r). Exact symbol-fibre counting supplies the independently proved original owner conflict graph `e(J)≤J0 r⁴` and point/line original Gram energies `G_f,G_g≤G0 r^(11/2)`. No source GQ spectrum was inserted.

### Fully explicit conservative integer envelopes

Set

```
v0=(b+1)(b²+1+C),     n0=(b+1)v0,
a0=2v0+3,             A0=a0²,
k0=b(b+1),             theta0=b+2,
Lambda0=theta0+(b+1)(b+C),
j0=k0 a0 + Lambda0 v0,
J0=2 j0,
G0=2 v0 k0 +2 theta0 j0 +2(b+1)v0 a0.
```

For all r≥2 in the domain, the exact G6-C1 estimates give

`V_P,V_L≤v0*r³`, `r⁴≤N≤n0*r⁴`,
`aP,aL≤a0*r^(3/2)`, `aP*aL≤A0*r³`,
`e_col,P,e_col,L≤j0*r⁴`, `e(J)≤J0*r⁴`,
`G_f,G_g≤G0*r^(11/2)`.

All inequalities are **uniform in the arbitrarily chosen complete minimal f,g**. Nothing requires `s=t`. Note that the physical vertex count is `aP*aL`, not `aP²` unless equal by actual data.

## 3. Freeze external graph constants and one selector

Use the *published ordinary graph* C6 supersaturation theorem (quoted in accepted #799; Jiang–Yepremyan, *Combinatorics, Probability and Computing* 29 (2020), 698–721, DOI https://doi.org/10.1017/S0963548320000206). Its existential constants are denoted `C_graph,c_graph>0`; choose exact rational `C0≥max(1,C_graph)` and `0<c0≤min(1,c_graph)` once. The statement needed is that every ordinary simple graph F with `e(F)≥C_graph*v(F)^(4/3)` has ≥`c_graph*(e(F)/v(F))^6` unoriented simple C6, with harmless normalization absorbed in the choice of c_graph.

**No published numeric values of C_graph/c_graph are supplied in this project.** The exact rational `C0=1,c0=1` and other values in tests are **hypothetical formal inputs only**, not certified admissible graph theorem constants. Nevertheless existential positivity yields genuine positive derived constants for any actually admissible input.

Define once, *before the source and any random selection*:

```
rho_cap=1/32, K=16J0+1, c=1/2,
R=512 A0(1+64J0),
T=ceil(8 n0 R³ C0³),
w=(4c)³/A0²=8/A0²,
q2=16(K+1)², q3=64(K+1)³.
```

Check `7/8−rho_cap−2J0/(K+1)>c`. The original source owner conflict graph J is based on **named original source flags**, not physical edges, and has degree threshold K. These constants are fixed independently of original projections/geometry.

The **shared selector lemma** is exactly the accepted all-source combinatorial step of #230/#799: independently give each surviving CORE original owner a single continuous random priority and keep J_C-local minima; give each typed coordinate symbol its **one global independent fair bit** (first factor and second factor). A retained original owner contributes its two physical diagonals only when BOTH of its typed factor symbol pairs cross the global bit cuts. The resulting physical graph G is one simple bipartite graph: every selected physical edge flips the first bit and the second bit. Do not draw a fresh cut/priority for each queried path or C6.

For any physical proper original CORE iwalk (i=2,3), whose i+1 x symbols and i+1 y symbols are separately distinct, its i distinct original owners are J_C-independent; all priority winners survive simultaneously with probability ≥`(K+1)^(-i)` and the correct global cut succeeds with probability exactly `4^(-i)`. Therefore for ordered proper iwalk endpoint matrix P_i of unselected H_C and the **same selected** graph G,

```
||P_i||_F² ≤ q_i² E tr(A_G^(2i)).
```

Each selected simple physical C6 is proper (J_C independent removes gap-two typed repeats, global cuts remove gap-three repeats) and has a unique **historical original D6** six-ID source inverse by the **geometry-unconditional** G6-C1 A2 lemma. A fixed proper physical D6 cycle survives both global cuts with probability exactly `1/1024`; priorities can only delete it. Thus `E C6(G)≤D6_A/1024` (not a separate independent draw for each possible cycle). The selected simple bipartite graph's closed-six-walk reversal bound gives

```
E tr(A_G^6) ≤ (3/128) D6_A +36(Tr)² W_C,
 W_C=Σ_(i∈C) 1/(1+degree_JC(i)) ≤ N.
```

The finite specialist independently enumerates **every** global bit-cut for a genuine proper 2edge/3edge path (exact probabilities 1/16 and 1/64) and for an actual proper original D6 (4/4096=1/1024), and samples one common global priority+two cuts on true and non-GQ source cores. These are falsifiers, **not** proof of the all-order selector inequalities, which are inherited and analyzed explicitly above.

## 4. HEAVY — ordinary physical supersaturation remains geometric-free

Freeze the FULL original physical degree threshold `Tr` before deleting Z and let `E_T` be the original **distinct** physical edges touching `{v:d_H(v)>Tr}`. In HEAVY suppose `E_T≥r⁴/8`. Removing `|Z|≤rho_cap*r⁴` original owners removes at most `2|Z|` real physical edges; at least `r⁴/32` source owners each with a surviving heavy-touching edge remain. Caro–Wei on original flag conflict J yields at least

`r⁴/[32(1+64J0)]`

pairwise J-independent genuine original source owners. Two coherent typed global cuts preserve both real diagonals of at least one quarter of these owners; a frozen heavy endpoint/orientation yields an actual simple bipartite physical graph F with `U⊆Q_T`, `U∩Y=∅`, distinct actual source edges, satisfying

```
e(F)/v(F) ≥ r/R,
v(F) ≤8N/(Tr)≤8n0*r³/T≤(r/(R C0))³.
```

Hence `e(F)≥C0*v(F)^(4/3)`, and the cited ordinary graph theorem supplies at least `c0*r^6/R^6` actual simple physical C6. The J-independent owners and global cuts make each C6 proper with **six distinct named original source owners**; the G6-C1 universal physical C6→D6 inverse is sufficient. Thus

`D6_A ≥ c0*r⁶/R⁶.`

No GQ projection axiom, regular source spectrum or nonexistent projected endpoint is used in this branch.

## 5. LOW — freeze one genuine original CORE C and sixth/fourth moments

In LOW `E_T<r⁴/8`. Remove from original FULL I **all** Z, all owners touching frozen FULL heavy edges, and all FULL J owners with degree>K. The remaining actual original source subset C obeys

```
|C| > [1−1/8−rho_cap−2J0/(K+1)] r⁴
    > c*r⁴=r⁴/2.
```

Physical H_C has genuine maximum degree `≤Tr` because all owners touching FULL heavy vertices were removed. `maxdeg(J_C)≤K`, source flags remain named, and `C⊆A=I\Z`.

For actual physical H_C, each original owner contributes exactly two real edges. Its oriented 3walk count obeys the degree-biased Jensen/Cauchy bound (valid without physical bipartiteness)

```
W3(H_C)≥(4|C|)³/(aP*aL)²>w*r^6.
```

If `D6_A≥delta*r⁶` already, we stop in the D6 class. Else `D6_A<delta*r⁶≤r⁶`. Use exactly the ONE selected G from §3. The sixth-moment bound yields

```
L6=1+ceil(36n0 T²),
||P3||_F²≤q3² L6 r⁶.
```

The original source owner coordinate-return identity `Qx+Qy=8|C|+4e(J_C)` depends only on pair injectivity and original ownership, **not** source geometry. Thus

```
Q0=8n0+4J0,
Qx+Qy≤Q0*r⁴,
||P2||_F²≤q2² sqrt(n0 L6)*r⁵,
tr(A_C^4)≤L4*r⁵,
L4=q2² ceil(sqrt(n0 L6))+Q0*T.
```

There are two gap-two repeated-coordinate types and the gap-three return type. The identity `A_C²(Tr I−A_C)≥0` means **positive semidefinite as a POLYNOMIAL IN A_C** when its spectrum lies in [-Tr,Tr], since `λ²(Tr−λ)≥0`; no assertion is made that A_C itself is bipartite or PSD. As in the accepted proof, the combined improper 3walk error obeys

`I_improper≤3 T Q0*r⁵.`

This portion is geometric-free; finite new tests compare literal physical two-/three-walk counts and Qx+Qy to the original named owner J relation for connected/ disconnected non-GQ and unequal GQ fixtures. They do not mistake a 3walk for a proper one.

## 6. LOW original endpoint defects: the ONLY NEW leading source term

For each ordered off-coordinate physical endpoint pair `(v0,v3)`, decode unordered first-factor pair and second-factor pair to original q,r only if they exist. The complete partition from G6-C2 yields

```
E_bad ≤4(M_P V_L+M_L V_P+M_P M_L)
     +4N +4V_P Delta_L
     +8t e_col,P(f)+8s e_col,L(g)
     +12st|Z|.
```

In particular the **new term** `4V_P Delta_L` is *exactly* the missing-original-threepath endpoint count, with four ordered orientations per missing pair. It does not get reclassified as a GQ-compatible endpoint, and deletion Z never creates a new *original frozen* projection. The final `12st|Z|` is original-anchor damage: every original flag belongs to exactly 3st projected nonincident endpoint pairs; FOUR physical orientations per damaged original pair. Neither deleted source nor added synthetic incidences can supply a new anchor.

For r≥2, using the intrinsic envelopes from §2 and `|Z|≤rho*r⁴` gives

```
E_bad ≤ E0*r⁵ +12 b² rho*r⁶,
E0=4(2a0 v0+a0²)+4n0+4v0 C+8bJ0.
```

The **Moore term** is `4v0 C*r⁴≤4v0 C*r⁵`, conservatively absorbed into E0; it vanishes for GQ (C=0). Thus, by the SAME global P3 selected-moment estimate,

```
I_endpoint≤q3 sqrt(L6*(E0/r+12b²rho))*r⁶
          ≤E*r^(11/2)+q3 sqrt(12b²rho L6)*r⁶,
E=q3 ceil(sqrt(E0*L6)).
```

The *deleted-anchor term* is order r⁶ and therefore cannot be dropped at large r; rho must be chosen after q3 and L6.

## 7. LOW FOUR interior blockers: exact FULL-A/CORE-C original book transfer

The only eligible physical proper source 3walks surviving §6's original endpoint mask have a frozen **existing** original three-flag projection `q--ell--p--r` whose anchors live in FULL A. Their three actual physical path owners are in the CORE C. The remaining possible disqualifiers are first/second physical x symbols hitting f(p) or first/second physical y symbols hitting g(ell).

G6-C2 independently proved the full-original/retained-core book inequalities, with actual original source J_C owner conflict degree ≤K and physical max CORE degree ≤Tr,

```
B_x²≤16(t+1)(K+1)|A|(Tr)G_f,
B_y²≤16(s+1)(K+1)|A|(Tr)G_g.
```

Insert §2's **defect-corrected** energies, `t+1,s+1≤(b+1)r`, `|A|≤n0 r⁴`. Then both

```
B_x²,B_y²≤16(b+1)n0 G0(K+1)T*r^(23/2).
```

With `BK=ceil(sqrt(16(b+1)n0 G0(K+1)T))`, this means `B_x,B_y≤BK*r^(23/4)`. The **local physical triple-to-source-book injection** is for each **distinct three-corner triple (v0,v1,v3)**, *not for all full paths*. For each fixed (v1,v3), its possible v0 choices are at most Δ_C≤Tr, while middle completions are `(A_C²)[v1,v3]`. The exact local G6-C2 theorem therefore bounds each of four blockers by `sqrt(B_(x/y)*Tr*tr(A_C^4))`. Summing them gives

```
I_fourblockers≤4 sqrt(BK*T*L4)*r^(47/8)
              ≤D*r^(47/8),
D=4ceil(sqrt(BK*T*L4)).
```

No GQ unique projection on *all* point-line pairs is used; we only handle real existing original projection anchors that survived the preceding masks. The prepared partial-projection inverse verifies the produced original BBo class and the **two** directed reversal orientations for every sixset.

## 8. Close all errors and prove the quantifiers

Freeze constants in the following exact order: (b,C); intrinsic v0,n0,a0,J0,G0; existential actual ordinary-graph C0,c0; selector K,R,T,q2,q3; moments Q0,L6,L4; endpoint E0,E; mixed book BK,D; and **only THEN** the deletion radius rho and source threshold r0.

Let `eps=w/8` and choose

```
rho=min(1/32, eps²/[12 b² q3² L6]) > 0,
delta=min(c0/R^6,w/4) > 0,
r0=max(2^32, ceil(3TQ0/eps), ceil((E/eps)²),
       ceil((D/eps)^8)).
```

These are **exact rational/integer expressions**. They are not numerically executable deletion thresholds until an actually admissible ordinary graph C0,c0 is supplied; program sample `C0=1,c0=1` is only a symbolic arithmetic demonstration.

For every integral r≥r0 in the stated domain and every deletion |Z|≤rho*r⁴, the exact ledger verifies **four independent LOW loss budgets**:

```
I_improper ≤ 3TQ0*r⁵ ≤ eps*r⁶;
I_endpoint(clean) ≤E*r^(11/2) ≤eps*r⁶;
I_endpoint(deleted anchors) ≤q3 sqrt(12b²rho L6)*r⁶≤eps*r⁶;
I_fourblockers ≤D*r^(47/8)≤eps*r⁶.
```

Their sum is at most `4eps*r⁶=(w/2)r⁶`. LOW began with `W3>w*r⁶`, so more than `(w/2)r⁶` proper eligible physical paths remain. Each accepted path produces a genuine original aligned BBo with its three original CORE source flags and its three **surviving FULL original** anchor flags, all six distinct. Conversely any produced original BBo can account for **exactly two** reverse oriented proper 3walks (G6-C2 original inverse). Consequently

`BBo_produced,A>(w/4)r⁶≥delta*r⁶`.

In HEAVY, `D6_A≥c0 r⁶/R⁶≥delta*r⁶`. These two cases exhaust the FULL original physical degree split on the *same* source, f/g and deleted named IDs. No expectation is interchanged with a universal minimum over f/g; randomness enters only the common selector inside the deterministic LOW proof and the independent **post-theorem** GF5 coefficient application.

Thus Theorem T3-L follows, as a transparently conditioned extension of the previously accepted #230/#799 HEAVY/LOW proof.

### Source-disjoint packing and independent GF5 coefficients

The theorem is robust against EVERY original source deletion |Z|≤rho*r⁴ on the same original I/f/g. A maximal matching of distinct named original D6 or actually produced aligned BBo six-ID hyperedges has ≥floor(rho*r⁴/6)+1 pairwise disjoint original flag sixsets. Fixing one signed GF5 checksum-four trade event per sixset gives independent success indicators for the **specific** iid 51-pattern source coefficient model of accepted #230/#793, each with probability at least `5175/51^6`. Hence selected-event Chernoff tail `Pr[X<p*m/2]≤exp(−p*m/8)` for `p=5175/51^6`; this does not prove an unrestricted adversarial deterministic-coefficient ASET exponent, dependent-coefficient result or full-risk upper bound.

## 9. Falsifiers and strict scientific STOP

Files in this stacked PR:
- `research/gio_t3c3_integrated_low.py`: exact all-order FORMAL_ONLY rational proof ledger with the new Moore endpoint coefficient; physical FULL heavy/LOW CORE freeze with explicit source original J and actual physical H; literal x/y coordinate-return and 2/3/4/6-walk checks; one common global J-min priority and two coherent typed symbol cuts; exhaustive genuine local 2/3 path cut probability and one real original D6 1/1024 global cut check.
- `research/test_gio_t3c3_integrated_low.py`: independent iterative all-physical-walk census versus recursive implementation; true and connected/disconnected non-GQ fixtures; literal original source J-vs-coordinate-return identity; source flag removal + high-degree cap; invalid b,C/external rational thresholds; four-error exact inequalities at formal giant r0 without constructing imaginary enormous sources.
- `.github/workflows/gio003-g6c3-integrated-low.yml`: GitHub-hosted Python 3.12 specialist with JSON certificate, exact-head standard Research and INDEX inherited from parent. No local physical PC required.

**Prior art check:** bipartite biregular Moore excess/girth/cages (e.g. [On biregular bipartite graphs of small excess](https://www.sciencedirect.com/science/article/pii/S0012365X19301232)), generalized quadrangle Moore cages (see [survey](https://www.combinatorics.org/files/Surveys/ds16/ds16v3-2013.pdf)) and the published ordinary graph even-cycle supersaturation theorem precede this research. The mathematical novelty, if externally verified, would be the **specific source-motif obstruction under intrinsic small-excess assumptions**, not the Moore bound, spectral identity or general C6 graph theorem by themselves.

**STOP and acceptance:** theorem T3-L is **conditional on fixed b, fixed C, girth≥8, regularity, complete minimal injective factor labels and the accepted published ordinary graph C6 theorem**. The *fully unrestricted* abstract incidence T3 (#793) remains open. The positive-excess condition may have an unknown/excluded infinite non-GQ realization; it is NOT presented as an existing new geometry family. This is an internal combined mathematical proof candidate based on accepted upstream lemmas, not external peer review or Lean. Require all exact-head specialist + Research + INDEX checks and a separate critical internal review, then only a narrowly governed stacked merge. Do not auto-merge old #800–#803 or close #793.
