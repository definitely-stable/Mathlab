# HYP-105 issue #230 — D5: retention-robust bad-endpoint energy falsifies the unconditional D2 route

**2026-10-13. Mathematical scope: EXACT ALL-h NO-GO FOR AN AUXILIARY UNIFORM ENERGY UPPER; #230 ROOT A/B OPEN.**

Strictly stacked above [D4 Draft PR #398](https://github.com/definitely-stable/Mathlab/pull/398) accepted head `e757eb71779ca6e0d594e3cc503bef11c80546f1`, all four hosted CI checks SUCCESS. No modification or merge to main. D4 used an explicit genuine W(3,s) symplectic spread to disprove unconditional `M_f+M_g=o(s^(39/10))` and `W_mean=o(s^(59/10))`. This D5 theorem is genuinely stronger: it disproves **smallness of the FULL nonnegative W_H even after deletion of o(s⁴) arbitrary physical edges**, with no assumption on the sign of the centered correlation, and **ANY valid global original line labeling g**.

## 1. The new all-h theorem (for all sufficiently large s=2^h)

Let G be the TRUE original physical rectangle-diagonal graph from globally injective f,g, with `m=2V(s+1)=(2+o(1))s^4` distinct undirected physical edges. Let B_bad be D2's original-projection bad-endpoint physical anti-diagonal-chord relation and H ANY physical undirected retained subgraph `H⊆G`. Define

    W_H = sum_{z in [a]x[a]} d_Bbad(z) d_H(z),
    R_s = |E(G) \ E(H)|.

There is an EXPLICIT legal minimal-palette original point-label map f_s (D4's genuine symplectic spread construction) such that for **EVERY** globally injective original line-label map g_s, and **EVERY** H⊆G,

    W_H >= [s/(g0*a)] * (2*g0*k*s - R_s)_+²,                (D5.1)

where

    a  = min{n: binom(n,2) >= (s+1)(s²+1)},
    g0 = floor(a/4),
    t  = floor((a-g0)/(2(s+1))),
    k  = t(s+1),
    x_+=max(0,x).

If H_s retains `m-o(s^4)` physical edges, then

    W_H >= (9/32+o(1)) s^6.                                (D5.2)

Because PR #394 constructs H_s with `|E(G) \ E(H_s)|=o(m)=o(s^4)`, this NO-GO also applies to its coherently spectrally pruned H_s. Therefore the **unconditional** universal D2/D3 proposed sufficient lemma

    W_H=o(s^(59/10)) for all globally injective original f,g      (FALSE)

is now refuted on the very class of retained graphs D2 intended to use. **This is NOT a counterexample to the ORIGINAL goal `S_s(f,g)=Omega(s^6)`, and no small-S coherent family is exhibited.** A compensation hypothesis *conditional on S=o(s^6)*, or an inequality with positive (S)-charge, may remain true.

## 2. Proof of the physical bad-relation certificate

Use D4's classical explicit Desarguesian symplectic spread of TRUE original W(3,s) into s²+1 mutually disjoint totally isotropic ORIGINAL lines. Partition `g0*t` selected lines into `g0` groups, t selected lines per group. Each original point p in group i gets f(p)={i,g0+j}, where `0<=j<k` is injective within the group. All other original points get distinct unused physical unordered pairs; the full f is globally injective, on the MINIMAL a.

Fix ANY globally injective original line-pair map g. For group i, write P_i for its k TRUE original points. Every p in P_i lies on a unique selected spread line L_p. Let `r != L_p` run through its s other TRUE ORIGINAL lines.

For any such incidence (p,r) and each original point q in `L_p\{p}` (there are exactly s choices), the unique GQ nonincident projection of (q,r) is `q-L_p-p-r`. Since **both** f(q) and f(p) contain physical anchor i, the original (q,r) is in D2's B_L⊆B_bad. This uses ONLY the original GQ axiom and ONE fixed globally injective f,g.

Each original incidence (p,r) has f(p)={i,j}, g(r)={x,y}, and contributes the TWO distinct actual physical graph G edges

    ((i,x),(j,y)) and ((i,y),(j,x)),

one incident at grid vertex (i,x) and one at (i,y). Because f and g are globally injective original pair maps, these edges never collide for distinct original incidences. In particular each of these physical graph edges has precisely ONE endpoint with first-coordinate anchor i, because j>=g0 and i<g0.

For each physical coordinate x let `T_i^G(x)` count those actual physical edges from selected nonspread original incidences (p,r) incident at physical grid vertex (i,x), and `T_i^H(x)` the same count when **the edge is retained in H**. They are nonnegative integers with `T_i^G(x)>=T_i^H(x)`. These counts are a TRUE typed subset of the actual physical graph degrees, so

    d_H(i,x) >= T_i^H(x).                                   (D5.3)

Each chosen ORIGINAL (p,r) contributes exactly s distinct bad ORIGINAL pairs (q,r), each of whose anti-diagonal physical chord endpoint set contains (i,x) when x∈g(r). D2's exact definition `B_bad=F U L^T` gives

    d_Bbad(i,x) >= s*T_i^G(x) >= s*T_i^H(x).                (D5.4)

Combining (D5.3)–(D5.4),

    W_H
      =sum_{z} d_Bbad(z)d_H(z)
      >=s*sum_{i<g0,x<a} [T_i^H(x)]².                      (D5.5)

This is a **positive lower energy certificate**, not a signed spectral estimate. No cancellation of D3's Wmean by Wcorr can eliminate it.

## 3. Edge deletion and the exact all-h robust inequality

There are precisely k original points per group and s nonspread TRUE original lines through each, each selected point-line incidence making TWO true physical edges. Thus

    sum_{i,x} T_i^G(x)=2*g0*k*s.                             (D5.6)

Every deleted physical graph edge removes AT MOST ONE of these selected witness edges (disjointness proved above), hence

    sum_{i,x} T_i^H(x) >= (2*g0*k*s-R_s)_+.                 (D5.7)

Apply integer Cauchy to exactly `g0*a` physical grid anchor cells:

    sum_{i,x} [T_i^H(x)]²
      >= [sum_{i,x} T_i^H(x)]²/(g0*a).                      (D5.8)

(D5.5)–(D5.8) prove D5.1 for **every** subgraph H of G, and any globally injective right g. We did not assume H is constructed by an entropy algorithm or that deleted edges have bounded concentration.

For the asymptotic, minimal a gives `a=(sqrt2+o(1))s^(3/2)`, while `g0=(1/4+o(1))a`, `k=(3/8+o(1))a`. Therefore

    2*g0*k*s = (3/8+o(1))s^4,
    (s/(g0*a))*(2*g0*k*s)^2=(9/32+o(1))s^6.

If `R_s=o(s^4)`, the R_s contribution changes the relative retained selected-edge count by o(1), establishing (D5.2). The coefficient 9/32 is a lower guarantee for this PARTICULAR construction; it is not an extremal all-label constant.

## 4. Exact finite true-original implementation and independent audits

[Executable all-h definition / finite witness oracle](../../research/hyp105_issue230_d5_retained_energy.py) and [independent tests](../../research/test_hyp105_issue230_d5_retained_energy.py) build exactly the same TRUE original projective symplectic spread as D4 and reconstruct a complete legal minimal-palette original f (but D5 uses its OWN implementation, rather than trusting D4's finished model). Two separately globally injective g are tested: D4's balanced simple-cycle-deletion map and its full reversed original line-assignment.

For real W(3,4) and W(3,8), checks reconstruct:
- the complete original GQ incidence and unique original projection through `ProjectionClosure`, with full f,g validating globally injective canonical physical pairs;
- independently all `2V(s+1)` physical original graph edges and the exact `2*g0*k*s` selected nonspread incidence physical edges;
- no collision of physical edges across true original selected incidences; physical anchor endpoint i unique per selected edge;
- actual degree-by-grid `d_Bbad` via D2's **independent original projection plus two-chord construction**, and `d_H` via complete retained actual adjacency; every original selected witness verifies (D5.3), (D5.4) cell by cell;
- D5's positive quadratic `s*sum(T_i^H)^2`, exact rational refined and deletion-budget lower, and the full D2 original energy W_H;
- full no-deletion energy W_G **independently** against D3's true original mean+signed spectral decomposition;
- for each original W34/W38 two distinct GLOBAL right g maps and two physically deleted-edge regimes: every 19th original physical edge and a more adversarial policy deleting selected witness edges FIRST; also zero retained edges and rejection of synthetic/non-original deletions;
- symbolic all-h parameter and exact rational coefficient arithmetic, which is not misreported as a new physically enumerated W(3,16) geometry.

## 5. Scientific decision

The proposed D2/D3 unconditioned implication `W_H=o(s^(59/10))` **for every f,g and the H of #394** is FALSE. This is stronger than D4's counterexample to the individual mean-term/spectral pencil sufficient estimates, because here `W_H` is itself a sum of **nonnegative actual physical degrees**, and the theorem survives deletion of **o(s^4)** arbitrary physical edges.

The path inequality from PR #394

    E_H<=24*t_H*W_H+sqrt(192*|B_bad|*D6(H))

remains formally true; it has simply become **vacuous as an unconditional small-E argument** on this legal family. Big W_H does NOT prove big E_H or prove small/large S. To prove root Branch A, D6 should explore either:
- an S-CONDITIONAL dichotomy `S=o(s^6) => W_H=o(s^(59/10))` (not contradicted by D5, as S remains unmeasured for this infinite family);
- direct weighted ENDPOINT + INTERNAL cancellation/compensation `C=E+I <=(16-eta)s^6+Lambda S+o(s^6)`;
- a new replacement for the crude small-book `24tW` term using original-geometry conditioned six-cycle certificates, not merely arbitrary chord sets.

The centered ||B^0|| upper from D3 remains independently open. D5 alone does not invalidate that auxiliary hypothesis, though together with the mean and full-energy lower it makes any naïve two-term Cauchy proof of small W more implausible.

**NO CLAIMS:** no original `S=Omega(s6)` universal theorem, no `S=o(s6)` infinite Branch B, no ASET exponent, no general GF5 R3. Retain Draft; no main merge; separate mathematical proof audit and exact-head GitHub-hosted Contract, INDEX and full Research required.
