# HYP-105 / issue #230 — AA4-AZ: quenched ALL-D opposite-port variance

**Scientific status:** original-source all-h STOCHASTIC PARTIAL THEOREM, draft child of AA4-AY PR #560 at exact HEAD a1098204561548a1521bbdd734333f8de4b7cac7. No original fixed-g minimax, GOOD-only or historical seven GF(5) six-original-ID lower is proved. Root Branch A/B/C stays OPEN_WITH_FORMAL_BLOCKER.

## Precise model, quantified result

For every h>=1, s=2^h, put d=s+1, V=(s+1)(s²+1), a=min{n: binom(n,2)>=V}, t=a-2, m=binom(a,2)-V. Choose ANY complete globally injective original POINT-factor map f from genuine symplectic W(3,s) into pair edges of K_a. Choose ANY fixed right physical support E consisting of V distinct K_a pair edges. Sample ONE coherent uniformly random COMPLETE bijection g from the V original LINE-factor IDs onto E. No incidence-by-incidence independent redraw is permitted.

R=R_ALL(f,g) counts the AA4-AY true original centered THREE-incidence-flag point+line physically opposite wedges: center (p,l), outer (q0,k0),(q1,k1), with all three point factors different and all three LINE factors different. The point physical edges f(q0), f(q1) meet opposite endpoints of f(p); similarly for physical right images g(k0),g(k1) and g(l). These are ALL-D, before physical GOOD filtering and before source 3×3 Hall or seven-GF5 selection.

Let w(l,k0,k1) be the number of genuine point-opposite source triples with those three distinct ordered original line IDs, B=sum w. Define M1=max_j sum_{triple containing j} w and M2=max_{j≠k} sum_{triple containing j and k} w. Define

\[
T(E)=\sum_{\{u,v\}\in E}(\deg_E(u)-1)(\deg_E(v)-1),
\quad p=\frac{2T(E)}{V(V-1)(V-2)},
\quad q=\frac{(V-3)(V-4)(V-5)}{V(V-1)(V-2)},
\]
\[
P_1=\frac{4t^4}{(V-1)(V-2)(V-3)(V-4)}.
\]

**AZ1 (exact mean, bounded relative variance).** For every nonnegative weighted 3-distinct-line-ID source family B>0, arbitrary fixed E and p>0 with V>=6, under ONE complete global right permutation

\[
\mathbb E_g R=Bp,\qquad
0\le\frac{\operatorname{Var}_g R}{(\mathbb E_g R)^2}
\le q^{-1}-1+\frac{3M_1P_1}{Bp^2}+\frac{3M_2}{Bp}.
\tag{AZ1}
\]

**AZ2 (uniform all-h genuine symplectic source).** Put
\[
L=Vt^2-2m(a-1)t,\quad
B_0=d(d-1)(d-2)L,\quad p_0=\frac{2L}{V(V-1)(V-2)}.
\]
For all original fixed f and right E, B>=B0, p>=p0, and the source influence caps are
\[
M_1\le 5d^3t^2,\qquad M_2\le 8d^3t.
\]
Consequently an entirely explicit source-label-independent uniform certificate is

\[
\boxed{\eta_s=q^{-1}-1+
\frac{15d^3t^2P_1}{B_0p_0^2}+
\frac{24d^3t}{B_0p_0}},
\quad
\frac{\operatorname{Var}_g R}{(\mathbb E_g R)^2}\le \eta_s
=O(V^{-1/2})=O(s^{-3/2}).
\tag{AZ2}
\]

AA4-AY already established \(\mathbb E_g R\ge s^6/2\) for all such adversarial supports. Therefore for ALL dyadic h, f and E,

\[
\Pr_g\{R_{\rm ALL}(f,g)<s^6/4\}\le\min(1,4\eta_s).
\tag{AZ3}
\]

The right side tends to zero as h→infinity. This is a high-probability guarantee only for ONE random entire original global g on any fixed E, never for EACH adversarial fixed g.

## Proof AZ1 — 0/1/2+ shared-original-line partition

Draw two ordered source triples independently proportional to their positive weights. With **zero** shared source line IDs, the six right images under the ONE global map are uniform distinct physical pair edges. Compare to two independent samples of ordered, internally distinct physical triples: their images are mutually disjoint with probability q. The unconditional probability both physical opposite indicators hold is p². Conditioning on their disjointness can only raise it to at most p²/q.

With **exactly one** shared original line factor, condition on the physical image edge e of that line. If e is a center, each pair of completing opposite-port edges has at most 2t² ordered choices. If e is one of the outer edges, choose the adjacent center edge (at most 2t choices) and then its complementary-port outer edge (at most t choices): again at most H=2t². Thus at most V H² valid complete image tuples of five distinct physical edges, out of (V)_5 ordered tuples. This is P1.

With **two or three** shared original LINE factors, discard the second event and upper-bound its joint probability by p. For two independent weighted source triples, probability they share at least one line is at most 3M1/B (union bound over the first triple's three IDs); probability they share at least two is at most 3M2/B (union bound over its three unordered ID pairs). As all terms are nonnegative,

\[
\mathbb E[R^2]/B^2\le p^2/q+(3M_1/B)P_1+(3M_2/B)p.
\]

Subtract the squared exact mean B²p² and divide; Chebyshev gives AZ3. Notice the proof explicitly addresses dependencies between events sharing the SAME global permutation.

## Proof AZ2 — actual source influence upper bounds

A genuine symplectic W(3,s) original point or line factor has exactly d incident source flags. A physical f(p) edge has exactly TWO endpoint ports, each containing at most t OTHER original point labels, because the entire original point map f is injective.

For any fixed original line ID j, if it is the center line, choose <=d center points, <=t² outer point pairs and <=d² actual outer incident lines: at most d³t² weighted events. If j is the first or second outer line, choose <=d original points incident to j, <=2t potential center physical neighbors for each such point, <=d genuine center lines, <=t opposite-port point labels, and <=d lines through the latter: at most 2d³t² in each outer position. Sum: M1<=5d³t².

For fixed distinct original line IDs j,k, when one is center and the other outer, choose which is center (2), which outer point-port position (2), then <=d center points, <=d points incident to the given outer line, <=t opposite-port point labels, and <=d choices of its original incident line: total <=4d³t. If both are outer, choose which is in each outer position (2), <=d point choices on each prescribed line, <=2t candidate center physical point labels adjacent to the first outer's physical edge, and <=d actual original center lines: total <=4d³t. Thus M2<=8d³t. These are safe upper counts; no forged synthetic source ID may contribute a valid event.

AA4-AY proves B>=d(d-1)(d-2)T(im f)>=B0 and p>=p0 using two possibly unrelated or correlated global occupied physical supports. Substitute the four deterministic inequalities in AZ1. Asymptotically, V=Theta(s³), t=Theta(s^(3/2)), minimal palette gives t²=O(V), and the prior exact support estimate L>=V²/2 holds for every dyadic order (including s=2). Also p0>=1/V and q^-1-1=O(1/V), while P1/p0²=O(1), M1/B0=O(1/V), M2/(B0p0)=O(V^-1/2). Thus eta_s=O(s^-3/2) without enumerating imaginary high-order source GQs.

## Tests and source provenance

The research implementation constructs a weighted *original* line-triple table directly from actual W32 and W34 incidence flags and a full physical point injection, checks its sum against the independent AA4-AY point-opposite B(f) computation, evaluates exact source one/two-line influence counts, and verifies the sharper measured certificate does not exceed the all-h worst-case envelope. W34 tests genuine K14 with six missing right physical edges. A separate falsifier enumerates ALL 720 globally coherent bijections of six line IDs onto K4 for four independent deliberately overlapping small weighted source families and computes exact rational mean and variance: no false independent-per-event sampler. Exact rational algebra checked for dyadic h=1..35,40,48,64,80; invalid original source IDs and noninjective images are rejected. The pen-and-paper proof above, NOT finite CI, establishes all-h quantifiers.

Examples from the exact bound formula: s=8 gives eta≈0.3592, s=16 eta≈0.0874, s=32 eta≈0.0268 and s=64 eta≈0.0089. These are finite substitutions, not evidence for a deterministic bound on fixed g.

**Prior art:** Covariance by source-ID overlap and concentration of permutation/U-statistics without replacement are established ideas, e.g. J. Ai, O. Kuželka and Y. Wang, *Hoeffding and Bernstein inequalities for U-statistics without replacement*, Statistics & Probability Letters 187 (2022), DOI 10.1016/j.spl.2022.109528. This work does NOT claim a new generic probabilistic technique. Prior project PR #544 already obtains an O(s^-3) relative variance for a DIFFERENT selected D6 six-ID statistic under fixed supports. AA4-AY #560 already proves the ALL-D threeflag quenched mean. AA4-AZ only supplies a concrete source-aware two-overlap variance bound for that narrower original threeflag object.

**Strict nonimplications and review gate:** Original W34 random has 46996 ALL-D physically opposite 3flag events but only 10 GOOD 3flag events, so no ALL-D-to-GOOD transfer can be silently made. No every-(f,g) accepted seven-class original six-incidence GF5 \(S\ge cs^6\), true 3×3 forest-Hall survival, infinite counterfamily, full R3 or ASET exponent has been proved. This scientific Draft requires a final exact-HEAD dedicated+INDEX+Proof Audit+Full Research CI inspection and independent mathematical referee; ancestor #560/#559 and their ancestry must be handled separately. Do not merge this Draft or alter accepted RCP research registry based solely on CI.
