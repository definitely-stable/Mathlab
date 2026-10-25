# HYP-105 / issue #230 — AA4-BE: adversarial partial original LINE-map pins lift to accepted original sixflag GF(5) D6

**Status:** mathematical research DRAFT. This is an original SIX-DISTINCT-INCIDENCE flag / historically accepted D6 theorem, rather than the threeflag GOOD statistic of #561–#565. Strict child of [AA4-BD #565](https://github.com/definitely-stable/Mathlab/pull/565), pinned ancestor 5a80e74800820ea0d1b6f7a464dd2adc80ae983f. Scientific siblings [#541](https://github.com/definitely-stable/Mathlab/pull/541), [#544](https://github.com/definitely-stable/Mathlab/pull/544) and [#548](https://github.com/definitely-stable/Mathlab/pull/548) remain on another stack: their exact ORIGINAL D6 candidate and physical sixcycle formulae are explicitly credited, NOT rediscovered here.

## The original root #230 hurdle and quantifiers

Fix every genuine original symplectic W(3,s), where s=2^h with h>=5; let d=s+1, V=(s+1)(s²+1), let a=min{n:binom(n,2)>=V}, K=binom(a,2), m=K−V. Each source point p and line l are ACTUAL distinct factor IDs with ACTUAL symplectic point-line incidence flag (p,l). Fix ANY COMPLETE globally injected point source pair-edge labeling f and ANY fixed occupied physical right LINE-image set E of V distinct unordered pair edges of K_a (E may be adversarially chosen and has m physical holes).

Pick ANY k distinct ORIGINAL LINE factor IDs, J subset of the real original line factor set, with 0<=k<=floor(V/16). Give them ANY injective physical pair-edge images phi:J→E. This partial map can correlate arbitrarily with f, source GQ incidence and E. Sample ONE uniform COMPLETE global original LINE bijection g from the other V−k actual source LINE factor IDs to the remaining V−k distinct physical right pair edges. All given pinned source-image assignments stay untouched.

Let D6_free(f,g;J) count accepted ORIGINAL D6 motifs containing exactly SIX distinct original incidence flag IDs, on six DIFFERENT original point factors and SIX DIFFERENT original LINE factors, NONE of whose actual original LINE IDs is pinned. Both f and g physical six-edge projections of the SAME actual six original flag IDs must form a simple connected physical C6 with IDENTICAL incidence position adjacency. This is precisely historical accepted positive original GF(5) D6 A/A (the source family of previous #541/#544). Thus D6_free is a nonnegative subset of the ROOT seven-class S_s(f,g), for each single actual full g. No signed surrogate, no fake source factor graph, no per-sixset independent redraw.

**AA4-BE1 — uniform all-h adversarial partial-global-line-map D6 extension.**
For EVERY such s,f,E,J,phi,

\[
\boxed{
\mathbb E_{g\supset\phi} D6_{\rm free}(f,g;J)
\ge\frac{27}{25}(s+1)^6\ge s^6,
\qquad
\exists\ {\rm one\ complete\ legal}\ g\supset\phi:
S_s(f,g)\ge D6(f,g)\ge s^6.
}
\]

This covers up to 6.25% of all ORIGINAL LINE factor images preassigned by an adversary, preserving the entire fixed source point map and right physical edge support. Its conclusion is now an **accepted original sixflag positive GF(5) D6** component, not merely a physically compatible threeflag wedge.

**AA4-BE2 — constructive nonzero density, without independent sixflag events.**
For the same uniform single full completion distribution,

\[
\boxed{
\Pr_{g\supset\phi}\bigl[D6(f,g)\ge s^6/2\bigr]
\ge \frac{s^6/2}{C_{\rm tot}\,d^6},
\quad C_{\rm tot}=(a)_6/12.
}
\]

This probability lower is generally very small, O(s^-9), and is NOT asserted to be asymptotically 1; it follows from the exact mean and a pointwise upper for all global maps. Existing #544 gives stronger high-probability bounds for the k=0 case, but not this arbitrary partial sixflag pinning theorem. We deliberately do NOT transplant #544 second moments without auditing pinned conditional codegrees.

## 1. Actual original physical point C6 and six-source-ID pool

Let C6(F) be the number of UNORIENTED simple physical 6-cycles in the occupied pair-edge graph F. There are exactly

\[
C_{\rm tot}=(a)_6/12
\]

undirected physical C6 in a complete K_a. Each physical pair edge belongs to exactly (a−2)_4 such cycles, since 6 C_tot/[binom(a,2)] = (a−2)_4. Fix t_4=(a−2)_4.

Each of the m missing physical support edges destroys at most t_4 cycles. Thus for EVERY permitted complete occupied physical support F (including both image(f) and E),

\[
\boxed{C6(F)\ge L_6:=C_{\rm tot}-m t_4.}
\tag{BE-C}
\]

This is the previously established exact original physical hole bound of #541/#548. The next step uses the real GQ source girth: for each physical point cycle consisting of SIX different source point IDs p1,...,p6, each chooses one of its d genuine original incident LINE IDs. Among d^6 choices, at most 15d^4 have a collision of two line-factor IDs because two distinct original GQ points have at most ONE original source LINE common to their neighborhoods. All remaining choices give six distinct true source LINE IDs and six ACTUAL distinct original flag IDs. Therefore

\[
A_6(f)\ge C6(\operatorname{im}f)\,q_s,\qquad
q_s=d^6-15d^4=d^4(d^2-15)>0.
\tag{BE-S}
\]

This six-original-factor source lower was proved by parent-side siblings #541/#548 and holds for ANY globally injected point map f. It does not assume any shared source flags are independent.

## 2. NEW true-original single pinned LINE-ID sixflag influence

For ANY one specified ACTUAL original LINE source factor j, at most d ORIGINAL point factors p are incident to j. Because f is globally injective, the physical edge f(p) is fixed and belongs to at most t_4 undirected point physical C6. Once one original line j is selected at its unique flagged original point position, the other FIVE real original incidence line IDs admit at most d^5 choices. Consequently the number of eligible actual original sixflag point-C6 candidates containing the given true LINE ID j is at most

\[
\boxed{\Delta_1^{(6)}\le d\cdot t_4\cdot d^5=d^6\,t_4.}
\tag{BE-I}
\]

No additional factor six is needed: every distinct original line assignment has j in EXACTLY ONE of six actual original point positions, and the sum over the at most d genuine original points of j counts that position once. Cycles are undirected unrooted original physical C6 sets; no distinct original sixflag source Q is counted repeatedly by vertex root or orientation.

Fix ANY pinned set J of k original LINE source IDs. Delete every candidate source sixflag containing ANY one of those pinned original line factor IDs. A union bound over genuinely distinct original source IDs, without resampling any original Q, gives

\[
\boxed{
A_6^{\rm free}(f;J)\ge L_6\,q_s-kd^6t_4.
}
\tag{BE-SF}
\]

This new pinned source influence is the crucial quantitative step from the earlier THREE-original-ID GOOD pinned lemma to the root SIX-original-ID historical D6 component.

## 3. NEW physical pinned occupied right-edge cycle deletion

Each pinned original LINE ID j∈J is assigned a distinct already occupied physical right pair edge phi(j)∈E, but other source line IDs remain globally unassigned. To count only right physical C6 using no pinned occupied pair edge image, delete the entire pinned physical edge set phi(J) from E. A second union bound on physically distinct sixcycles yields

\[
\boxed{ C_6^{\rm free}(E;\phi(J))\ge L_6-k\,t_4.}
\tag{BE-RF}
\]

This never changes the ORIGINAL right occupied support E, its missing edges or globally injected image: it just restricts the subset of SIX target physical pairs eligible for the unpinned-source-only count. The k assigned right physical edge labels are still part of the complete global original right map.

## 4. Exact conditional mean for ONE coherent complete original LINE permutation

Conditional on arbitrary f,E,J,phi, there are N=V−k remaining distinct original LINE factor IDs, mapped by ONE uniform complete bijection onto the N remaining distinct physical occupied right pair edges. For each eligible source Q using SIX different ACTUAL unpinned original LINE IDs, the images of those six real original source line IDs are a uniform ordered SIX-tuple of distinct remaining physical pair edges, with denominator (N)_6. Each physical right C6 admits exactly TWELVE position-preserving aligned placements relative to the already fixed point C6, not six factorial independently accepted different source Q.

Hence the **exact** conditional one-global-map identity is

\[
\boxed{
\mathbb E_{g\supset\phi} D6_{\rm free}
=
A_6^{\rm free}(f;J)\frac{12\,C_6^{\rm free}(E;\phi(J))}{(V-k)_6}.
}
\tag{BE-M}
\]

All original incidence flags and physical source point images are fixed; globally overlapping actual source Q share the SAME one map g. Event independence is never assumed. This is the true-original pinned extension of the known k=0 formula in #541, not another annealed two-side-redraw mean.

## 5. Explicit elementary all-dyadic lower and numerical-free 1/16 gate

Minimality of a gives m<=a−2 and a>=261 for h>=5. Therefore

\[
\frac{m t_4}{C_{\rm tot}}=\frac{12m}{a(a-1)}
\le\frac{12}{a-1}\le\frac{12}{260}<\frac1{20},
\]
so L6≥19 C_tot/20. Furthermore k<=V/16 and V<=a(a-1)/2 imply

\[
\frac{k t_4}{C_{\rm tot}}=\frac{12k}{a(a-1)}
\le \frac38.
\]

Since d=s+1>=33 and 15/d²<=15/1089, the two independent surviving masses satisfy

\[
\boxed{
A_6^{\rm free}\ge C_{\rm tot}\,d^6
\left(\frac{19}{20}\left(1-\frac{15}{d^2}\right)-\frac38\right)
\ge\frac12 C_{\rm tot}\,d^6,
}
\]
\[
\boxed{
C_6^{\rm free}\ge\left(\frac{19}{20}-\frac38\right)C_{\rm tot}
=\frac{23}{40}C_{\rm tot}\ge\frac12 C_{\rm tot}.
}
\]

Inserting in BE-M and using (V−k)_6<=V^6, we obtain

\[
\mathbb E D6_{\rm free}
\ge 3\frac{C_{\rm tot}^2 d^6}{V^6}.
\]

The elementary union bound on the six complete K_a falling factors gives (a)_6>=a^6(1−15/a)>=9 a^6/10 for a>=261, and V<=a²/2. Hence

\[
\boxed{
\mathbb E D6_{\rm free}
\ge3\left(\frac{9a^6}{120}\right)^2\frac{64d^6}{a^{12}}
=\frac{27}{25}d^6
\ge s^6.
}
\tag{BE-L}
\]

A legal complete original global line bijection achieving at least the finite average BE-L exists. It retains every original source line image pinned by the adversary, and the SOURCE Q is a genuine positive historical six-source-incidence D6. This proves AA4-BE1 with ALL appropriate all-h and arbitrary cross-map correlation quantifiers.

## 6. Density of high-D6 completions and limits

For every legal complete original f,g the number D6_free cannot exceed the number of original point-C6 sixflag candidates A6(f), itself at most C_tot*d^6. Let M=C_tot*d^6. Denote τ=s^6/2. For a uniform legal completion, E[D6_free]>=s^6. If p=Pr(D6_free>=τ), then E[D6_free] <=p*M+(1−p)*τ. Thus

\[
\boxed{p\ge\frac{s^6/2}{M-\tau}\ge\frac{s^6/2}{M}.}
\]

The full accepted D6(f,g)>=D6_free, so the same probability floor holds for all allowed pinned global completions. This is a deliberately WEAK but genuine finite-count lower requiring no fake independent sixflag indicator events. Previous #544 obtains much stronger concentration when k=0 but with a distinct, separately audited all-h variance proof.

## 7. Reproducible falsifiers, parallel work and original scope

The new code implements the exact original all-h rational BE-C, BE-I, BE-SF, BE-RF, BE-M and BE-L inequalities for s=2^h, h>=5, with arbitrary k=0,1,floor(V/16), checking the exact simple 27/25*d^6 mean lower, arithmetic for h up to 80, and explicit domain rejection.

An **independent full REAL ORIGINAL W32** oracle enumerates all physical point C6 on f's actual globally injected K6 support, all d^6 real original source incident line choices at those six ACTUAL original point IDs, then discards choices with repeated original LINE IDs or pins. It separately enumerates all physical C6 in the free right physical support, compares exactly to the BE-M conditional expected mean, and checks the historical source pool 18,716 original six-Q for lex/reverse and 21,186 for S68/S72, as recorded by #548. Finite W32 is NOT the h>=5 theorem. Independent physical K6 six-edge target-map 6! bijection enumeration returns 12 positional C6 alignments out of 720; independent K6 full C6 count 60 and actual one-edge deletion count bound (a−2)_4=24. W32's actual original GQ line-factor neighborhoods also pass the independent no-multiple-common-line condition. Invalid injection, repeated locked physical images, out-of-range source IDs and unproved h reject fail closed.

**Scientific prior-art boundary:** #541 already proved unpinned k=0 ORIGINAL D6 quenched mean, #544 variance and high-probability on fixed complete physical supports, and #548 source six-Q pool and five-swap repair. The new scoped step is uniform **adversarial arbitrary PARTIAL ORIGINAL LINE-ID pinning** directly for the HISTORICAL accepted SIX ORIGINAL distinct flag GF(5) D6 family, using a new one-original-LINE-factor candidate influence deletion plus a separate fixed physical right sixcycle deletion. No claim of newly discovering GQ source Hall, physical C6 counts, sampling without replacement or probabilistic method. Parallel #566/#567 concern partial GOOD 3flag source statistics; this is NOT duplicating those.

**NOT PROVED:** a lower bound for every individually given COMPLETELY FIXED original f,g; acceptance for the other six selected historical GF(5) classes individually; original seven-class universal S>=c*s6; root #230 A/B/C or the R3/ASET strict exponent. Pinning all V original LINE IDs leaves zero permutations and is specifically outside this theorem. Keep Draft pending exact final-HEAD specialized, INDEX, Proof Audit, Research and independent mathematical referee; passing CI is not a substitute for independent proof review.

**Next root-facing task:** exploit actual global original source incidence and both physical maps to handle MORE locked labels while preserving accepted SIX-ID motifs, or isolate an exact deterministic anti-alignment certificate for all prescribed original factor labels. Do not keep improving purely stochastic threeflag bounds when true original sixflag tests are available.
