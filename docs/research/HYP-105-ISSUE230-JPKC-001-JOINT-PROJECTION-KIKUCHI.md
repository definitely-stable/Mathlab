# HYP-105 / #230 — JPKC-001: joint ORIGINAL projection/Kikuchi defect audit

**2026-10-13. STATUS: RESTRICTED_THEOREM_C (all-h necessary obstruction pair) + FINITE_EXACT falsifier. ROOT A/B OPEN.**

This is a strictly stacked Draft **on PR #394**, commit `aa9dfb87595ba0ce0d7aa2ae6294b550bccdf09d`. It does NOT import PR #366 or the D6-V/W stacks, does NOT modify `main`, and does NOT merge. The new Kikuchi computation is independent of the PR #366 implementation and is tested against its separately pinned exact numerical controls.

## 1. Objects and quantifiers: one coherent f,g

Let s=2^h (h>=1), V=(s+1)(s^2+1), a=min{b:C(b,2)>=V}, and let f and g be arbitrary separate COMPLETE injections from ORIGINAL W(3,s) points and lines to E(K_a). They may be adversarially correlated. Every computation below uses the very same pair f,g; there is no resampling across the two ledgers.

Let G on [a]x[a] have the two diagonals of each ORIGINAL incidence (p,l). Put n=a^2, m=2V(s+1). For each graph-simple oriented three-path with six distinct used original physical row/column coordinates (four rows and four columns across its four vertices), consider the ORIGINAL end-point labels q,r. If either label is absent, the path is MISSING; if q is incident with r, INCIDENT; otherwise unique GQ projection q--ell--p--r exists, and the path is BLOCKED if the physical label of p or ell intersects its four coordinates on that side, otherwise UNBLOCKED. These categories are exactly disjoint.

In the **full G**, define B_G=number of BLOCKED paths (not E_H+I_H). A complete unblocked path gives one of the synchronized B/B-overlap accepted original sixsets, counted with exactly two orientations. Hence `unblocked_G/2 <= S` for every legal global map, with no assumption on the choice of H.

For the cycle ledger, P3(G)=number of simple oriented length-three paths, p_uv their ordered endpoint multiplicities, C6(G) ALL undirected simple six-cycles, D6(G) the proper cycles with six distinct first and six distinct second coordinates, C6_imp=C6-D6, and Theta the precise K2 coincident-internal-vertex sum.

IMPORTANT: the PR #394 analytic proof uses a **retained coherent H subset G**. Its bound on the nonincident blocked paths C_H=E_H+I_H must not be substituted as equality with B_G. What is valid is C_H<=B_G.

## 2. Proved all-h double-defect necessity

**THEOREM J1 (conditional, ALL powers s=2^h).** If a sequence of valid complete globally injective (f_s,g_s), along unbounded h, satisfies S_s=o(s^6), then the SAME assignments satisfy

```
B_G(f_s,g_s) >= (16-o(1)) s^6,
Theta(G(f_s,g_s)) + 12 C6_imp(G(f_s,g_s)) >= (48-o(1)) s^6.
```

The o(1) terms may depend on the chosen assignment sequence but the universal lower bounds used in their derivation are uniform over f,g. This is a *necessary condition on a hypothetical Branch-B counterfamily*, not proof that such a sequence exists, and not a sufficient counterexample criterion.

**Proof of the first inequality.** PR #394 establishes a coherent retained graph H with P_good(H)>=(16-o(1))s^6 and the mixed-book closure inequality

```
(16-o(1)) s^6 <= C_H + 2 S + sqrt(192 m S).
```

Since m=Theta(s^4), if S=o(s^6), then S=o(s^6) and sqrt(m S)=o(s^5), hence o(s^6). Thus C_H>=(16-o(1))s^6. Every retained blocked oriented path remains a blocked path in the full graph with the same labels, so B_G>=C_H. QED.

**Proof of the second inequality.** The exact simple-graph identity (K2) for the FULL Kikuchi graph is

```
sum_(u,v) p_uv^2 = P3 + 12 C6 + Theta.
```

Cauchy-Schwarz over at most a^4 ordered pairs implies, writing L(x)=x(x/a^4-1),

```
12 D6 >= L(P3) - Theta - 12 C6_imp,
```

therefore

```
Theta+12 C6_imp >= L(P3)-12 D6.
```

Since D6<=S, the last term is o(s^6). The Alon–Hoory–Linial non-backtracking lower bound and the K1 peeling argument give

```
P3 >= 4N(4N/a^2-1)^2 - 6 C3,       N=V(s+1).
```

Here `4N/a^2=(2+o(1))s`. The uniformly proved moment bound in PR #394 is `M2(G)=sum_v deg(v)^2=O(s^(11/2))`. For a simple graph, `3C3 <= sum_v binom(deg(v),2) <= M2/2`. Thus `C3=O(s^(11/2))=o(s^6)`. It follows that `P3>=(16-o(1))s^6`. The function L is increasing for x>=a^4/2; here P3/a^4>=4-o(1), so `L(P3)>=(48-o(1))s^6`. QED.

**Do not generalize J1 to all f,g as pointwise numeric inequalities with the asymptotic constants 16/48 at s=2,4,8.** This is a conditional sequence statement with asymptotic errors, not a finite threshold. In particular neither `B_G >= 16 s^6` nor `Theta+12C6_imp >= 48s^6` is asserted for finite W32.

## 3. Exact finite JPKC gate and independent checks

The executable `research/hyp105_issue230_jpkc_joint_defect_gate.py`:
1. Receives the **validated complete true ORIGINAL** f,g via PR #394 `ProjectionClosure` and computes its definition-level full-G projection classification.
2. Independently constructs the Kikuchi adjacency directly from both physical diagonals of EVERY original incidence.
3. Counts all oriented simple 3-paths; separately calculates Theta from original graph codegrees, triangles, pendant C4, diamond and bowtie terms. Infers all C6 via the EXACT K2 identity.
4. Independently enumerates EVERY undirected graph six-cycle once (minimum vertex / reflection canonical rule), partitions proper/improper, and checks agreement with K2.
5. Verifies the K3 rational lower bound and exact Cauchy-Schwarz/proper D6 inequalities.
6. At W32, independently computes the complete original seven-class S via the existing B0 census and checks D6-proper plus synchronized B/B-overlap against it.
7. Fails closed on path/cycle budgets, invalid full pair injections, missing original GQ incidence structure and contradictory identities.

Cross-checks against separately published Kikuchi K1 values at s=2:
```
                       P3    Theta    ALL C6   D6
lex                  3846     5476       730   15
reverse-line         3300     3316       485    3
```
At s=4 lex, the separately published pin is `P3=132644; Theta=127684; C6=37320; D6=8481`. PR #394's independent geometrical census pins true-original closure classifications for lex/random at s=2,4.

The executable is *not* a full seven-family oracle for s=4/8. It refuses the W32-only seven-family cross-check outside s=2. A missing exact cycle census is never presented as zero cycles. No bound obtained on the full G is silently substituted for the retained H gate.

## 4. Falsifiable research conjecture (NOT proved)

One particularly small sufficient JPKC gate is the following same-map alternative. For some uniform constants eta,eps>0 and Lambda<infinity, and all sufficiently large s, EVERY globally coherent f,g has at least one:

(A) `C_H <= (16-eta)s^6 + Lambda*S + o(s^6)`, with H a PR #394 valid retained graph for that same f,g; or

(B) `L(P3(G))-Theta(G)-12C6_imp(G) >= eps*s^6`.

Either alternative implies `S=Omega(s^6)` by the already proved projection and proper-D6 inequalities. This is a SUFFICIENT RESEARCH CONJECTURE, **not** a theorem in this PR.

It may be false even when Root A is true, because other seven-positive GF5 motif families can dominate while BOTH these restricted mechanisms have small margin. Its failure is a method NO-GO, not an infinite Branch-B construction.

## 5. Connections to D6-V/W and Kikuchi K2; priority decisions

D6-U proves each individual-Q proper-scope conditional minimum zero. D6-V goes further: any independent unconditioned cluster with <=floor((a-1)/6) original sixsets has zero joint minimum. Thus merely partitioning JPKC witnesses into constant-size independent minima cannot prove the theorem.

D6-W implements signed separator-reparameterization, sound for exact truthful factor tables and mutually cancelling messages, and closes saturated THREE-site W32 conditional orbits. Its finite result **does not** imply two-site messages can prove an all-h original bound without fixing most factor images.

Recommended next step after this exact truth gate is a **new source-witness overlap taxonomy** between PR #394 blocked closure events, K2 coincidence types and the OTHER six selected GF5 motifs. Do not equate the retained E_H+I_H with K2's Theta or K3's cross-original J; first exhibit original incidence-preserving correspondence with multiplicities. Only if such a taxonomy yields an independently verifiable nonnegative compensation inequality should D6-W messages be proposed as a certificate for that inequality.

Potential falsifier: on the actual symplectic-spread complete injections of D4, compute the finite JPKC defect pair and search for simultaneous near-saturation. A failure of the small alternative (A)/(B) only refutes that method, NOT Root A.

## 6. Acceptance contract and prohibited inferences

- Dedicated GitHub-hosted JPKC tests must succeed at the FINAL PR HEAD; no local workstation required.
- Independently verify exact K2 values against explicit cycle DFS (no identity used as its own test), and exact D6 against ORIGINAL seven-census.
- Pin W32 S68/S72 and W34 lex/random closure controls.
- Keep `main` unchanged. Do NOT merge without independent mathematical review.
- Issue #230, #176 and #169 remain OPEN.
- No `PROVED_A`, `COUNTEREXAMPLE_B`, new full R3 upper, or ASET exponent is authorized.

**Next allowed action:** investigate genuine original-factor cross-witness overlap and conditional compensations, not additional standalone W32 right-swap or independent small-cluster minimizations.
