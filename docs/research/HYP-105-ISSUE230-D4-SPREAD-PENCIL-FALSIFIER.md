# HYP-105 issue #230 D4 — genuine infinite symplectic-spread falsifier of the D3 proof route

**12 October 2026 · ALL-h COUNTERFAMILY TO THE PROPOSED D3 AUXILIARY ESTIMATES; ROOT A/B BOTH OPEN.**

This stage is stacked only on [D3 Draft PR #397](https://github.com/definitely-stable/Mathlab/pull/397), parent exact HEAD `108b015b831b90440bbbec7e5e223ea776862059` (hosted Contract/INDEX/Proof Audit/full Research 4/4 SUCCESS). Main is unchanged. The issue #230 root universal `S_s(f,g)=Omega(s^6)` is **NOT disproved or proved**. The actual new all-h result is a concrete **NO-GO for the unconditional auxiliary hypothesis** `M_f+M_g=o(s^(39/10))` and its implied `W_mean=o(s^(59/10))` route in D3.

## 1. Statement (ALL powers s=2^h, asymptotically h→infinity)

Write `V=(s+1)(s²+1)` and choose the MINIMAL physical alphabet `a` satisfying `binom(a,2)>=V`. There is an **explicit deterministic** pair of globally injective original point- and original line-label maps

    f: original W(3,s) points -> binom([a],2)
    g: original W(3,s) lines  -> binom([a],2)

such that the TRUE ORIGINAL number `M_f` of unordered collinear original point pairs whose two physical f-labels share a coordinate satisfies

    M_f >= (3/32+o(1)) s^4.                                  (D4.1)

Consequently the D3 **unconditional** proposed sufficient condition `M_f+M_g=o(s^(39/10))` is FALSE for admissible minimal-alphabet globally coherent f,g. The accepted `M_f=O(s^4)` spectral estimate from PR #394 has an **optimal exponent four** (possibly improvable constant).

Furthermore the D3 ORIGINAL GQ mean endpoint energy on the SAME complete coherent f,g from D3,

    W_mean=(s+1)/V * sum_{original bad (q,r)} d_f(q)d_g(r),

obeys

    W_mean >= (9/32+o(1)) s^6.                              (D4.2)

Thus also `W_mean=o(s^(59/10))` fails on an infinite genuine family. **This does not prove that the FULL nonnegative endpoint energy** `W_G=W_mean+W_corr` is Omega(s^6): `W_corr` can have either sign and may cancel. It says nothing by itself about the spectrally retained `W_H` of #394, the internal-only blockers `I_H`, or the total seven-family `S`. In particular no `S=o(s^6)` infinite family is constructed.

## 2. Original symplectic Desarguesian spread — explicit algebra and proof

The W(3,s) built in Mathlab's `hyp105_b1_symplectic.py` uses projective vectors `(x_0,x_1,y_0,y_1)∈GF(s)^4` with alternating bilinear form

    <(x,y),(x',y')> = x·y' + x'·y            (characteristic 2).

Choose `c∈GF(s)^*` such that `z²+c z+1` has NO root in GF(s). Such a `c` exists for every power of two: pick a quadratic irreducible over GF(s), rescale its nonzero constant term to 1 using the unique square root in characteristic two (alternatively use trace-one construction). For every `(b,d)∈GF(s)^2`, take the symmetric matrix

    A_(b,d) = [[b,d],[d,b+c*d]]

and the ORIGINAL projective line

    L_(b,d) = { [ (x,A_(b,d)x) ] : x∈GF(s)^2 \ {0} }.

Also take the vertical line `L_infty={[(0,y)] : y!=0}`. Each graph line is totally isotropic because A is symmetric and the standard alternating form vanishes on two graph vectors. For nonzero difference `(b,d)`,

    det A_(b,d) = b²+c*b*d+d² !=0

by the irreducibility of `z²+c z+1`. Therefore two distinct graph lines have no common projective point. Every graph line is disjoint from the vertical. There are `s²+1` lines of `s+1` ORIGINAL points each, and their total `(s²+1)(s+1)=V`; hence they form a spread, partitioning ALL original points. This is the classical Desarguesian symplectic-spread mechanism, not a new finite-geometry existence result. See [Thas, *Symplectic spreads in PG(3,q), inversive planes and projective planes* (1997)](https://doi.org/10.1016/S0012-365X(96)00345-7) and [Lavrauw et al., *50 Years of translation structures* (2022)](https://link.springer.com/article/10.1007/s00022-022-00643-5).

The code implements this algebra using the project's **real GF(2^h)** multiplication (not integer mod-4), resolves EVERY graph/vertical projective line against the TRUE original `W(3,s)` line IDs, validates orthogonality pairwise, and exhaustively checks the disjoint partition on true W34/W38.

## 3. Entire global f-injection — all unused original points completed

Let

    g0 = floor(a/4)                               number of anchor physical coords
    n0 = a-g0                                    distinct available nonanchor coords
    t  = floor(n0/(2(s+1)))                      spread lines per anchor
    L  = g0*t                                    selected original spread lines.

For all sufficiently large s (and in particular the true finite checks s=4,8), `g0>0,t>=1`, `L<=s²+1`, and `t(s+1)<=n0/2`. Partition any L distinct lines from the ORIGINAL symplectic spread into g0 blocks of t lines each. Because the spread lines are mutually vertex-disjoint, each block has exactly `k=t(s+1)` distinct ORIGINAL points.

For block i∈{0,...,g0-1}, map its k original points INJECTIVELY to pairs

    { i, g0+j },  j=0,...,k-1.

This is a canonical unordered physical pair, and different blocks have different anchor coordinate i; the second coordinate belongs to the disjoint nonanchor set. Therefore none of the selected original points share the SAME physical unordered pair. Complete f on **EVERY remaining ORIGINAL point** with distinct unused edges of K_a; possible because `binom(a,2)>=V` and exactly L(s+1) distinct pairs were already allocated. This is a complete valid original map f for the MINIMAL alphabet — not a partial or independently resampled labeling.

Every selected spread line has all its `s+1` original points with one common physical anchor coordinate. Every unordered point pair on it contributes once to `M_f`, and no such pair appears on two distinct selected spread lines (spread partition). Thus the exact all-h deterministic floor is

    M_f >= L * binom(s+1,2).                                (D4.3)

The TRUE ORIGINAL left-endpoint-bad `(q,r)` relation has exact identity `|B_L|=2s M_f`, hence

    |B_L| >= 2s L binom(s+1,2).                            (D4.4)

Only a SUBSET of these bad pairs is used to prove the mean-energy floor below.

## 4. Entire global ORIGINAL line-label g-injection, with balanced stars

The minimal palette surplus satisfies

    0 <= K-V < a-1,   K=binom(a,2).

Take `K-V` consecutive distinct edges of the simple cycle on the physical alphabet `[a]`, and remove them from K_a. There remain EXACTLY V distinct unordered pairs. Assign them in deterministic order bijectively to ALL original W(3,s) LINES. Each physical coordinate loses at most TWO incident pairs (since deleted pairs lie in a simple cycle), so every physical coordinate appears on at least `a-3` distinct original right line labels, and for EVERY original line r,

    d_g(r)=sum_{x in g(r)} deg_{physical star of g}(x) >= 2(a-3).

This is a single FULL globally coherent g, not a per-(q,r) choice or random completion. The construction does not assume or use any unproved all-h GQ positivity.

## 5. Rigorous ALL-h asymptotic constants, including mean energy

Minimal K_a gives `a=(sqrt(2)+o(1)) s^(3/2)`. Therefore

    g0=(1/4+o(1))a,
    n0=(3/4+o(1))a,
    t=(3/8+o(1))a/(s+1),
    L=(3/32+o(1))a²/(s+1)=(3/16+o(1))s².

By (D4.3),

    M_f >= (3/16+o(1))s² * (1/2+o(1))s²
        = (3/32+o(1)) s^4.

For each ordered pair of distinct original points q,p on one selected original spread line l, the GQ axiom provides EXACTLY s ORIGINAL lines r through p other than l; the unique original nonincident projection of (q,r) is q-l-p-r. All such pairs are distinct by the GQ unique projection, and are endpoint-bad because their physical f-pairs share the selected anchor. Number of such generated ORIGINAL bad pairs is exactly

    2s L binom(s+1,2) = (3/16+o(1)) s^5.

For every such q, its physical anchor-coordinate original label star degree is at least `k=t(s+1)=(3/8+o(1))a`. For EVERY r, the globally balanced right g has `d_g(r)>=2(a-3)`. The original D3 mean formula yields the constructive exact floor

    W_mean >= [ (s+1)/V ]
              [ 2s L binom(s+1,2) ]
              [ t(s+1) ]
              [ 2(a-3) ].                                     (D4.5)

Since `(s+1)/V=1/(s²+1)`, `a²=(2+o(1))s³`, this lower bound is

    (1+o(1))/s² * (3/16+o(1))s^5
    * (3/8+o(1))a * (2+o(1))a
    = (9/32+o(1))s^6.

**Critical limit of inference:** (D4.5) is a lower bound on W_mean, not on signed `W_corr` or their SUM. It falsifies the unconditional D3 pair of SUFFICIENT little-o hypotheses. It is not a counterexample to all-label S=Omega(s6); even the seven-family S for this infinite construction remains uncomputed.

## 6. Independent true-original proof and finite witness oracles

[Source](../../research/hyp105_issue230_d4_spread_pencil_falsifier.py) and [tests](../../research/test_hyp105_issue230_d4_spread_pencil_falsifier.py) verify:
- rootless degree-two polynomial over actual GF4/GF8 and GF16;
- canonical symmetric graph plus vertical ORIGINAL lines, complete spread and all original symplectic orthogonality;
- independently materialized complete globally injective minimal-alphabet f AND g on W(3,4) and W(3,8);
- exact original pencil M_f/M_g (not physical surrogate), full D3 rational mean energy on the SAME globally fixed f,g, and its (D4.5) exact rational lower;
- cycle-omission right coordinate degrees >=a-3 (independent line labels);
- exact symbolic arithmetic for all s=2^h through large h (these are NOT labeled as new finite GQ geometry runs);
- FALSE flags for `M_f+M_g=o(s^(39/10))`, `Wmean=o(s^(59/10))`, and explicitly OPEN all seven-family/root A/B.

## 7. D5 scientifically valid follow-up

**STOP unconditional D3 branch** that assumed `M_f+M_g=o(s^(39/10))` for all coherent maps. We now have a constructive infinite counterfamily. A route assuming `Wmean=o(s^(59/10))` universally is also FALSE. This does **not** eliminate compensated, small-S-conditional, or sign-cancellation routes:

1. Investigate the **FULL physical** W_G for this infinite spread family and whether actual GQ incidence forces cancellation or, under spectral pruning, changes the `W_H` exponent. Prove before asserting.
2. Independently prove/falsify the DOUBLE-CENTERED `||B^0||²=o(s^(63/10))` candidate; the spread lower on M_f does not automatically disprove it.
3. Return to the actual target `C=E+I <=(16-eta)s^6+Lambda S+o(s^6)`, conditional on genuinely correlated seven-positive-family S (not the already false P2/P7 mean demand). The internal-only I obstruction remains independent.

**No ASET exponent, no full R3, no Branch B. No main merge. Require dedicated hosted Contract/INDEX/full Research final SHA and separate mathematical proof audit.**
