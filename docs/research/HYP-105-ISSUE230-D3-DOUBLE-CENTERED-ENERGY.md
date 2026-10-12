# HYP-105 #230 D3 — exact double-centered GQ energy and the missing 1/10 exponent

**12 October 2026. RESTRICTED_THEOREM_C; BOTH ROOT BRANCHES OPEN.** Strictly stacked above [D2 Draft #396](https://github.com/definitely-stable/Mathlab/pull/396) accepted HEAD `bc4e679d1d1a589d073856e90458e715eaef080c`. No change to main and no acceptance of the already-disproved unit-mean P2/P7. The only root theorem in [#230](https://github.com/definitely-stable/Mathlab/issues/230) is `S_s(f,g)=Omega(s^6)` for **ALL** coherent original global pair injections f,g; this remains UNPROVED.

## 1. Correct analytic decision before implementation

Parent D1 split nonincident blocking `C=E+I` into endpoint-bad path mass E and internal-only mass I. D2 constructed the EXACT physical bad antipodal-chord relation B and mixed-book bound for the pruned graph H:

    E_H <= 24 t_H W_H + sqrt(192 |B| D6(H)),  |B|=O(s^5).

On the actual coherent spectral pruning of [#394](HYP-105-ISSUE230-PROJECTION-CLOSURE.md), `t_H=O(s^(1/10))`. Thus `W_H=o(s^(59/10))` would imply `E_H=o(s^6)` along a hypothetical `S=o(s^6)` sequence. It would NOT bound I. The D2 observed finite full-G mixed-book bounds were vacuous, so an extra **genuinely universal** inequality is essential.

D3 does not assert that `W_H=o(s^(59/10))`; it extracts the two specific necessary sufficient proof subproblems out of the full ORIGINAL GQ spectrum.

## 2. All-h EXACT physical ORIGINAL factor-matrix identity

For `s=2^h`, `V=(s+1)(s^2+1)`, `Delta=s+1`, `a=min{k:C(k,2)>=V}`, let `J` be the V-by-V actual original GQ point-line incidence matrix (not the all-ones matrix). Let `F` and `L` be a-by-V physical coordinate incidence matrices for ONE pair of globally injective original point/line pair maps `f,g`. Every original factor vertex receives exactly ONE unordered physical pair. Every column of F,L therefore has exactly two ones, and every row has <=a-1 ones.

Define `U_{q,r}=1` iff the TRUE original (q,r) is nonincident, and its unique GQ projection `q-l-p-r` has `f(q) intersects f(p)` OR `g(r) intersects g(l)`. This is the D1/D2 endpoint-bad original relation. Define

    B = F U L^T,  D = F J L^T,  W_G = <B,D>_F.

D is the physical grid graph degree matrix. B is the physical bad relation degree matrix: each original bad (q,r) contributes exactly four physical grid *endpoint vertices*, corresponding to exactly two undirected physical antipodal chords. All objects and matrix rows are globally coherent; U is NOT independently randomized, and `U_{q,r}` is defined by the original projection, not by a physical adjacency shortcut.

Let `k_f=F 1`, `k_g=L 1` be physical-coordinate original label star degrees, and `R=F (J-(Delta/V)11^T)L^T`. Then

    D=(Delta/V) k_f k_g^T + R,                                  (D3.1)
    W_G=W_mean+W_corr,                                         (D3.2)
    W_mean=(Delta/V) sum_((q,r): U=1) d_f(q)d_g(r),             (D3.3)
    d_f(q)=sum_(u in f(q))k_f(u), d_g(r)=sum_(x in g(r))k_g(x),
    W_corr=<B,R>.

These are exact rational identities, all s and all coherent f,g. The independent D3 implementation calculates both RHS representations of mean: from original bad (q,r) and the physical grid degree vectors. It checks that both sums match the actual D2 W.

## 3. Stronger ALL-h DOUBLE CENTERING, proven analytically

The ORIGINAL GQ incidence is regular of row/column sum Delta. Let `E=J-(Delta/V)11^T`. Therefore `E1=0` and `1^T E=0`. Since every F and L column has exactly TWO ones,

    L^T 1_a=2*1_V,    F^T 1_a=2*1_V.

Consequently the physical residual is zero-row AND zero-column:

    R 1_a=0,     1_a^T R=0.                                   (D3.4)

Let `r_u=sum_x B(u,x)`, `c_x=sum_u B(u,x)`, `b=sum B=4|U|`. Define the exact physical double-centered bad relation

    B^0(u,x)=B(u,x)-r_u/a-c_x/a+b/a^2.                         (D3.5)

It has zero row and column sums, and because of (D3.4) we obtain

    W_corr=<B,R>=<B^0,R>.                                    (D3.6)

Its norm is given by the exact two-way ANOVA identity

    ||B^0||_F^2 = ||B||_F^2
                  -(1/a)sum_u r_u^2-(1/a)sum_x c_x^2+b^2/a^2. (D3.7)

Thus all one-coordinate additive masses of the physical bad relation are **provably irrelevant to the spectral correction**, even for maximally correlated original maps. This improves the *form of the certificate* over the previous Cauchy bound using the uncentered B, but is NOT itself a positive bound on S.

## 4. ALL-h GQ spectral theorem and exact certificate

In W(3,s), the ORIGINAL point-line incidence J has singular values Delta, sqrt(2s), or 0. Hence

    ||E||_op <= sqrt(2s).

The physical coordinate incidence matrix F obeys `||F||_op^2<=2(a-1)` because its nonnegative FF^T has row sum <=2(a-1). Also `||L^T||_F^2=2V`. Therefore

    ||R||_F^2
    =||F E L^T||_F^2
    <= ||F||_op^2 ||E||_op^2 ||L^T||_F^2
    <= 8s(a-1)V = O(s^(11/2)).                              (D3.8)

Combining Cauchy with exact double-centering:

    |W_corr|^2 <= ||B^0||_F^2 ||R||_F^2
              <= 8s(a-1)V ||B^0||_F^2.                        (D3.9)

All finite checks are INTEGER EXACT. Let `Rtilde=V*D-Delta*k_f*k_g^T` and `Btilde=a^2*B-a*r_u-a*c_x+b`; the code checks integer equality of both original and physical contractions, zero row/col sums, exact separate norm identity, and

    (<Btilde,Rtilde>)^2
       <= (sum Btilde^2)(sum Rtilde^2),

with no float approximations. It also checks (D3.8).

## 5. Critical mean barrier: why today's known GQ spectrum does NOT close D2

Since `d_f(q),d_g(r)<=2(a-1)`, the main term has the exact pointwise bound

    W_mean <= [4 Delta (a-1)^2/V] * |U| = O(s)*|U|.            (D3.10)

By TRUE original GQ pencils, if `M_f` counts unordered collinear original POINT pairs whose physical f-labels intersect, and `M_g` is the genuine original LINE dual, then

    |B_L|=2s M_f, |B_R|=2s M_g, |U|<=2s(M_f+M_g).            (D3.11)

The accepted GQ spectral pencil result from #394 is only

    M_f,M_g <= (s-1)V+(s^2+1)(a-1) = O(s^4).                 (D3.12)

Therefore the EXISTING bounds yield only `W_mean=O(s^6)`. D2's alpha=1/10 requires `W_H=o(s^(59/10))`; we CANNOT infer this from `O(s^6)`, and no finite sample supports promoting an asymptotic power saving.

One **sufficient but not established** uniform route is

    M_f+M_g = o(s^(39/10))   (implies |U|=o(s^(49/10))),
    ||B^0||_F^2 = o(s^(63/10)).

Then (D3.10)-(D3.12) and (D3.9) imply `W_G=o(s^(59/10))`, and `W_H<=W_G` for any retained H subset G with fixed B; PR #394's mixed-book inequality gives `E_H=o(s^6)` along a hypothetical small-S sequence. The CENTERED norm exponent is checked:

    2*(59/10) - 11/2 = 63/10.

This is a **conditional reduction**. D3 neither proves either uniform hypothesis nor proves the separate internal-only bound I. It also leaves open the possibility that a more subtle signed cancellation in `W_corr` or amortization by S is a better method; the sufficient split is not necessary.

## 6. Finite independent proof/counterexample oracle

[Reference implementation](../../research/hyp105_issue230_d3_double_centered_energy.py) and [focused tests](../../research/test_hyp105_issue230_d3_double_centered_energy.py) execute seven actual complete coherent ORIGINAL states: W32 lex/reverse/S68/S72, W34 lex/random, W38 random. All independently derive:
- both typed ORIGINAL point-/line-pencil unordered collinearity masses M_f,M_g and union exact pair sets;
- physical F*U*L^T tensor from original bad pairs, matched to D2's independent antipodal physical chords;
- physical F*J*L^T degree matrix by direct ORIGINAL incidence, matched to true physical degrees;
- exact original and physical rational mean, signed spectral correction and total W;
- R scaled by V and B^0 scaled by a^2, exact zero row/column sums, exact ANOVA identity and integer Cauchy;
- rigorous spectral ||R||^2 cap and globally injective physical star cap;
- independent ORIGINAL collinear-pair enumeration for W34 and independent separate physical coordinate relabeling invariance on S68;
- fail-closed assumptions and status flags: no all-h S or endpoint blocking bound.

The full finite seven-state report is **NOT** a proof of any o(s^power) theorem. The source and target use the SAME original GQ f,g; no independent stochastic resampling is permitted within one state.

## 7. Next D4 options and stop rules

(1) Strongest candidate: bound the double-centered `B^0` norm through the ORIGINAL GQ projection tensor and physical coordinate occupancy, not just |U|. Can one prove `||B^0||^2=o(s^(63/10))` uniformly, or prove an explicit coherent all-h family falsifying it?

(2) Independently audit the true pencil mass `M_f+M_g`: the available O(s^4) is only 1/10 power away from the sufficiency condition o(s^(39/10)). A sharper physical line-graph vs W(3,s) intersection theorem would be new mathematical input; do not assume typical random f achieves the worst-case adversarial upper.

(3) If either target fails, study a **COMPENSATED** inequality of `W_H<=o(s^(59/10))+K*S/s^alpha` or directly `C=E+I <=(16-eta)s^6+Lambda*S+o(s^6)`; do not attempt to resuscitate falsified global P2/P7.

No merge to main, no #230/#176/#169 closure, no strict full R3 bound, no new ASET exponent. Independent mathematical proof review remains required even if Contract/INDEX/full Research are all green.
