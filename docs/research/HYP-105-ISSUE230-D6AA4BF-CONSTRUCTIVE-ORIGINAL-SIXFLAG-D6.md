# HYP-105 / #230 — AA4-BF: deterministic original sixflag D6 completion via exact conditional expectations

**Scientific DRAFT; strict child of [AA4-BE PR #568](https://github.com/definitely-stable/Mathlab/pull/568), frozen parent HEAD 937fa5be1a6648ee404732b8868f10be85e9c45c.** No main changes, no accepted mathematical claim promotion, no declaration of Branch A/B/C. This is a CONSTRUCTIVE upgrade of the previous ORIGINAL SIX-incidence historical positive GF(5) D6 quantitative partial-line-map mean theorem, not another GOOD threeflag concentration theorem. Earlier [#566](https://github.com/definitely-stable/Mathlab/pull/566) proves constructive GOOD threeflag source completions (different statistic); parallel [#569](https://github.com/definitely-stable/Mathlab/pull/569) constructs at least ONE accepted original D6 and separately many GOOD threeflag wedges in one map (not s^6 accepted D6 sixflag lower). The method of conditional expectations is classical; novelty is confined to this exact source/physical model and quantitative result.

## Exact mathematical quantifiers

Let s=2^h, h>=5, and let W(3,s) be the actual symplectic generalized quadrangle with genuine original incidence flag IDs (p,l), d=s+1 original line neighbors per original point and V=(s+1)(s²+1) original point and line factors of each type. Put a=min{n:binom(n,2)>=V} and E(K_a) the original physical unordered pair-edge alphabet for EACH typed side.

Fix ANY globally injected COMPLETE original POINT physical pair-edge map f, ANY adversarial V-element occupied physical RIGHT line edge support E in K_a, and ANY k<=floor(V/16) distinct ACTUAL ORIGINAL LINE source factor IDs J with ANY injective physical pair edge assignment phi:J→E. The pins may be arbitrarily correlated with the original incidence structure, f and E. An adversary may adaptively choose the NEXT as-yet-unassigned actual original LINE factor ID after seeing all prior chosen physical images, but the constructor, not the adversary, chooses the edge image of that factor.

**AA4-BF:** There is an explicit finite EXACT RATIONAL GREEDY ALGORITHM that produces ONE complete original LINE factor globally injected bijective map g* onto E, preserving all initial actual original line-factor physical pair assignments phi, f, E and EVERY original incidence ID, satisfying

\[
\boxed{S_{D6}(f,g_*)\ge\lceil\Phi(\phi)\rceil\ge s^6.}
\]

The positive S_D6 is the HISTORICAL selected original GF(5) accepted D6 A/A class on SIX DISTINCT ACTUAL original incidence flag IDs, SIX different genuine original point factor IDs and SIX different genuine original LINE factor IDs, with the same fixed six actual flag IDs under BOTH physical projections f and g. It is a nonnegative subcount of the seven-class root objective S_s(f,g). It is NOT the earlier physically GOOD threeflag source statistic. This theorem constructs ONE favorable full map extending arbitrary PARTIAL assignments; it does not claim a positive count for ALL already fully fixed adversarial f,g (where all V line images are prescribed).

## True original source six-incidence weighted ledger

Enumerate each undirected simple physical six-coordinate C6 in the complete fixed POINT occupied support im(f), using ONE canonical six-coordinate root and orientation for each undirected cycle (e.g. least coordinate first and second coordinate smaller than last). Let the six consecutive physical point pair edges be e0..e5 and pi=f^{-1}(ei) the SIX different original point IDs. Select li from the ACTUAL source neighborhood of pi, independently as a combinatorial enumeration (not randomizing a global map), with SIX DISTINCT ORIGINAL LINE factor IDs and six real original source incidence flags (pi,li). Discard source Q if any li belongs to the *initial* fixed LINE set J. The remaining genuine original sixflag candidates Q have ordered sixline factor tuple q=(l0,...,l5), with weight w(q)>=1 counting all different eligible original point sixcycles that have that same ordered source LINE six-tuple. No six rotations or reversed duplicate source point cycles are counted as different undirected Q.

The total original source weight B=sum_q w(q) equals the previously independently established genuine original original-point-C6 sixflag source candidate count A6_free(f;J) from PR #568. Source incidence flags NEVER change as a function of a proposed or chosen right mapping. In the finite executable W32 original symplectic fixture generator this ledger is materialized by literal original source incidence lists and canonical original point physical sixcycles. High-order W(3,s) geometries are not faked or fabricated by the all-h parameter-only bound verifier.

## Accepted right physical positional targets

Enumerate each undirected simple six-coordinate C6 entirely within the fixed right occupied physical edge set E. For every such physical cycle, form exactly 12 ordered six-pair-edge target rows: six rotations and both directions. Call their set C(E). It has exactly 12 C6(E) elements. Given one true original source point sixcycle in canonical original point position order, the historical accepted ORIGINAL D6 condition is exactly that the corresponding SIX original right-line factor images form one of those 12 ordered right target rows. This is the positional sixflag equivalence of #541 and #539; the root class is not redefined here. Physical sixflag count for a fixed full original map g is thus EXACTLY

\[
D6_{\mathrm{free}}(f,g;J)
=\sum_q w(q)\,
1[(g(l_0),\ldots,g(l_5))\in C(E)].
\]

## AA4-BF1: exact ONE-global-map conditional potential

For any intermediate globally legal partially assigned original LINE map psi:J'→E extending phi, write n=V−|J'| and U=im(psi) for its used physical edges. For a fixed genuine-original q=(l0,...,l5), let I(q,psi)={i:li in dom(psi)}, c=|I|. Define H(q,psi) to count those accepted right physical positional target rows (r0,...,r5) in C(E) satisfying BOTH:

- For every already assigned source-line position i in I, the right target edge ri is EXACTLY the globally fixed psi(li).
- For every unassigned source-line position i not in I, the right target edge ri belongs to the still-free set E minus U.

Then the exact rational potential is

\[
\boxed{
\Phi(\psi)
=\sum_q w(q)\frac{H(q,\psi)}{(n)_{6-c}},
}
\tag{BF-P}
\]

with (n)_r=n(n−1)...(n−r+1), (n)_0=1 and terms with r>n interpreted as zero (not an impossible partial completion). There is a single G sampled uniformly from ALL (V−|J'|)! complete whole original LINE-factor bijections extending psi, not a separately sampled right map for every Q. Since the SIX original line IDs in each q are distinct and global injection is preserved, their remaining 6−c images are uniformly distributed over the (n)_{6−c} ordered distinct right edges. Exactly H choices achieve accepted original D6. Therefore

\[
\boxed{\Phi(\psi)=\mathbb E_{G\supset\psi}
[D6_{\mathrm{free}}(f,G;J)].}
\tag{BF-M}
\]

Summing over overlapping genuine source Q is valid by linearity of expectation: **NO independence of any different source Q events is assumed.**

At the initially pinned state psi=phi, every q is from an ORIGINAL Q not containing any initially pinned source LINE IDs, so c=0, and the right target rows avoiding all initially pinned physical right edges are precisely the 12 orientations of the remaining right physical sixcycles. Consequently

\[
\Phi(\phi)
=A6_{\mathrm{free}}(f;J)\frac{12 C6(E\setminus\phi(J))}{(V-k)_6}
\ge\frac{27}{25}(s+1)^6>s^6.
\]

This is EXACTLY the uniform conditional mean (not a new independent theorem) of parent #568, proven for ALL dyadic h>=5 and ANY correlated legal f,E,J,phi.

## AA4-BF2: exact tower and adversarial adaptive source order

For any unassigned ACTUAL original LINE factor j, under one global uniformly random completion conditioned on psi, the single new physical edge image G(j) is uniformly distributed over all n free physical pair edges e. Therefore the classical conditional expectation tower is EXACTLY

\[
\boxed{
\Phi(\psi)=\frac1n
\sum_{e\in E\setminus U}
\Phi(\psi\cup\{j\mapsto e\}).
}
\tag{BF-T}
\]

The next actual source LINE ID j can be selected **ADAPTIVELY by an adversary**, including from the previous assigned physical images. The deterministic algorithm evaluates every free e, using Python exact Fraction for the full genuine source sixflag positional potential, then selects a maximizing value; ties break canonically by the sorted physical edge. The selected image is appended to the SAME globally injected original LINE map psi, so Phi never decreases. After V−k iterations, all source LINE factors are assigned and there remains exactly ONE complete map g*. Its potential is the literal finite accepted original D6 count on this same map:

\[
S_{D6}(f,g_*)\ge
D6_{\mathrm{free}}(f,g_*;J)
=\Phi(g_*)\ge\Phi(\phi)\ge s^6.
\]

This proves AA4-BF for ANY adaptively selected order of original LINE factor IDs, provided the constructor chooses the next image edge. If the adversary also chooses images until k=V, the positivity theorem does NOT apply. The algorithm is finite and exact but may be prohibitively expensive at large h; no benchmark or production efficiency is claimed. Mathematically all-h constructive does NOT mean computationally efficient at real high orders.

## Independent oracles and falsifiers

- Generic small whole-permutation K6 toy: six actual LINE-label positions and SIX physical right pair images forming a cycle; independently enumerate ALL 6!=720 global maps. Exactly 12 satisfy the original D6 physical positional alignment, so the exact conditional initial potential is 1/60. In adversarial source order (5,3,1,4,0,2), at all 6 rounds verify the n-way rational tower exactly, terminal global map assigns each label to a distinct physical right edge and has exactly ONE accepted physical sixcycle. This toy tests *only* global permutation algebra and does not purport to be a fictional genuine W(3,s) source.
- Literal true original symplectic W32 source fixture lex/reverse/S68/S72: enumerate 18,716 / 21,186 original six-source-flag point cycle candidates with original true incidence neighborhoods and verify them against the separate #568 source Q census. Independently verify the exact initial one whole-global D6 conditional mean against #568, and the full fixed complete given original physical f,g D6 count with an unrelated literal six right physical edge rainbow adjacency oracle.
- Literal true original W32 source maps lex and S68 with a NONIDENTITY arbitrary pinned original LINE image, original source Q touching the initial pinned source LINE IDs removed; the initial one-global conditional source D6 mean exactly agrees with an independently enumerated original source/physical sixcycle oracle from parent #568. One and two greedy steps selected in reverse original source-factor ID order explicitly satisfy the exact tower and preserve the adversarially pinned physical image.
- One complete actual original W32 lex full 15-original-LINE-ID greedy global image map in reverse source order: the FINAL integer potential equals the literal same-original-sixflag D6 on the final chosen true globally injected map, and is at least the original all-completions mean. No small-h positivity lower is attributed to the large-h theorem.
- Exact all-h parameter-only s=2^h h=5..35 plus h40,48,64,80 for pinned source counts 0,1,floor(V/16): inherit the parent verified all-h conditional mean >=27/25(s+1)^6 and apply the exact BF-T identity symbolically; NEVER invent a huge symplectic W3 source fixture.
- All original source/physical global injection violations, repeated source line IDs in a sixflag, source ID outside V, terminal event claimed with incomplete global map, and false h<5 domain fail closed.

## Prior-art and scientific nonimplications

Conditional expectations are classical, not new. Prior #541 already proved conditional mean for no initial pins, #544 original D6 fixed-support concentration, #548 every genuine source sixflag Q repair within five swaps of a given map, #568 arbitrary <=V/16 pins strong SIX-ID D6 expected mean; #566 is an earlier constructive routine for DIFFERENT three-original-incidence GOOD source weights, #569 already guarantees one selected original sixflag D6 in a same-global map with GOOD threeflag Ω(s^6). This AA4-BF quantitatively constructs Ω(s^6) genuinely accepted original SIX-ID D6 using the arbitrary pinned extension conditions, not any fixed-g minimax theorem.

**NOT PROVED:** a positive original seven-class S_s(f,g) for EVERY previously fully fixed arbitrary pair f,g; a legitimate infinite correlated counterfamily o(s^6); equivalent Branch C; residual original 3×3 Hall general transfer for arbitrary fixed g; R3/ASET strict exponent. Keep root issue #230 OPEN_WITH_FORMAL_BLOCKER and the scientific PR DRAFT until final exact SHA dedicated CI, INDEX, Proof Audit, Full Research and independent mathematics referee/ancestor gate. No automatic merge or acceptance based only on numeric tests.
