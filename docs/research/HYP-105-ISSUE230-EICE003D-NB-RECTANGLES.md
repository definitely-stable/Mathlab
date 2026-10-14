# HYP-105 / #230 — EICE-003-D: true NB3 rectangles and four-matching original transport

**Status: RESTRICTED_THEOREM_C; Branch A/B remain OPEN.** Strict research-only child of EICE-003-C [Draft PR #453](https://github.com/definitely-stable/Mathlab/pull/453), frozen parent HEAD \`5590a5dfaf6d1fc37c18a8e006186799361df6e7\`. Changes are ONLY in a new child branch. No main merge, no ASET exponent, no all-h spectral compensation claim.

## Mathematical input and scope

Fix true original GQ W(3,s), s=2^h, and arbitrary globally injective original point/line physical pair labels \`f,g\`. Let a physical graph H be the union of BOTH physical diagonals for some subset I* of true original incidence IDs. Assume the EICE-002 coherent structural conditions:

1. a common physical two-colouring cL on left coordinates and cR on right coordinates; every physical edge crosses both cuts;
2. at each physical vertex (x,y), its neighbours have pairwise distinct left and pairwise distinct right coordinates;
3. every NB3 path is coordinate-proper (follows from 1–2, or can be audited independently).

These hypotheses are CHECKED, not inferred from a full unconstrained graph. Let M=|I*|>0, m=2M physical edges, and \`d_*=\min_{v:deg(v)>0}deg(v)\`. The stationary edge-rooted NB3 probability law is defined only if d_*>=2. When d_*=1, one may normalize the surviving NB3 paths, but source-middle uniformity and D3/D4 conclusions for the stationary law must NOT be applied.

## D1 — exact product of two genuine outer-neighbour transitions

Fix an ORIENTED physical middle edge u→v. Write \`A=N_H(u)\setminus{v}\` and \`B=N_H(v)\setminus{u}\`. Conditional on this oriented edge under the stationary NB3 law, the outer path vertices w∈A and z∈B are INDEPENDENT and uniform:

    Pr[w,z | middle=(u,v)] = 1/(|A|*|B|).

Consequently the eligible true ORIGINAL GQ endpoint/middle incidence transport is EXACTLY

    T[(q,r),e] = (1/(2m))*sum_(oriented (u,v) with original source e)
                  [sum_(w∈A,z∈B) 1[eligible ORIGINAL endpoints (q,r)]
                   / ((deg(u)-1)*(deg(v)-1))].                     (D1)

Here q=f^{-1}({x(w),x(z)}), r=g^{-1}({y(w),y(z)}) when these pairs are present among actual global original labels, and eligibility includes coordinate-properness, true nonincidence q∉r, unique GQ projection q--ell--p--r, and end-clean f(p)∩f(q)=g(ell)∩g(r)=empty. Each physical middle edge has EXACT original source incidence ID e and the two physical diagonal edges per e remain coupled.

D1 does NOT imply q and r are independent conditional on the middle edge: both depend on the SAME pair (w,z).

## D2 — four partial endpoint matchings per TRUE original middle incidence

The two physical cuts imply x(w),x(z) always have OPPOSITE left colours and y(w),y(z) OPPOSITE right colours. The local coordinate-neighbour uniqueness property implies the maps w→x(w), z→x(z) are separately injective, and likewise for y. Therefore, within one fixed directed middle edge u→v, the unordered left endpoint pair {x(w),x(z)} determines w AND z uniquely (colours determine the orientation), and the same holds for the right endpoint pair. Since f,g are globally injective, both maps

    (w,z) -> q=f^{-1}({x(w),x(z)})
    (w,z) -> r=g^{-1}({y(w),y(z)})

are INJECTIVE on their domains of definition.

Hence the set of actually decoded original endpoint pairs (q,r) for a fixed directed middle edge is a PARTIAL MATCHING between true original points and true original lines. Eligibility filtering only removes edges from this matching. A genuine original middle source incidence e produces two physical diagonals and four orientations total. Thus the support of the transport column \`T[.,e]\` is a union of at most FOUR partial original endpoint matchings. In particular, for every fixed (e,q), there are at most four possible r, and for every fixed (e,r) at most four possible q. All statements are exact all-h and fail if the EICE-002 local cherry/cut conditions are removed.

This is a genuinely new restriction on source transport that was absent from the arbitrary coupling in EICE-003-C C5. It still does not force a blocked-path gap: the prior RELAXED C5 transport already puts only one endpoint pair per e and hence ALSO obeys the degree-one matching constraint, but fails actual physical rectangle/path and end-clean realizability.

## D3 — exact stationary source–endpoint atom ceiling

For d_*>=2, the stationary original middle incidence E is uniform on the M retained genuine source IDs (EICE-003-C C3). Each source ID gives exactly four oriented middle edges; each conditioned rectangle cell has weight

    1/[4*(deg(u)-1)*(deg(v)-1)]   conditional on E=e.

By D2, for a fixed true ORIGINAL endpoint point q and line r each of the four orientations contributes AT MOST ONE outer pair to \`Pr[X=(q,r)|E=e]\`. The same statement holds with only q or only r prescribed. Therefore

    Pr[X=(q,r)|E=e] <= 1/(d_*-1)^2,
    Pr[X_point=q|E=e] <= 1/(d_*-1)^2,
    Pr[X_line=r|E=e] <= 1/(d_*-1)^2,                (D3)

where the X=(q,r) event means actual eligible end-clean original endpoints and missing/invalid ones are assigned ⊥. Equivalently the true joint transport atom satisfies

    T[(q,r),e] <= 1/[M*(d_*-1)^2].

This is a nontrivial finite-time anti-concentration consequence of physical paths; it does NOT bound the probability that the anchor is internally blocked because there can be many distinct blocking endpoint pairs for the same e. A missing endpoint symbol ⊥ can have arbitrarily high conditional mass, and is NOT covered by D3.

## D4 — a genuine Shannon UPPER, insufficient to close C6

Let X=(q,r) for a path with true original eligible end-clean endpoints and X=⊥ for any other path, P=Pr[X≠⊥], and C_clean be the number of real original nonincident end-clean endpoint pairs (q,r). Under the stationary law H(E)=log M and the atom ceiling D3 implies

    H(X|E=e) >= 2*Pr[X≠⊥|E=e]*log(d_*-1),

since each non-⊥ conditional atom has probability <=(d_*-1)^(-2); the ⊥ entropy term is nonnegative. Averaging over e gives

    H(X|E) >= 2P*log(d_*-1).

Also H(X) <= h_2(P)+P*log(C_clean). Thus

    I(X;E) <= h_2(P)+P*log(C_clean)-2P*log(d_*-1). (D4)

If P=0 then I(X;E)=0, and the formula is interpreted continuously. This is an ALL-h mathematical bound conditioned only on the genuine EICE-002 structural G* + active d_*>=2, no stochastic independence of f,g and no asymptotic fitting. It requires BOTH left/right coordinate cut+cherry properties. The diagnostic implementation uses float logs, but D4 is proved analytically.

For the explicit EICE-002 all-h constants d_*>=(10^(-6))s and C_clean<=V²=O(s^6), the D4 upper is at best (4+o(1))*log(s)+O(1) when P=1, while EICE-003-C C6 forces only (3/2-o(1))*log s-O(1) if theta_I=1-o(1). **The entropy gap is too large to prove Branch A.** Thus it is INVALID to claim that merely finding an information upper bound settles HYP-105: this particular bound demonstrably does not.

## D5 — limits of the local matching improvement

The EICE-003-C relaxed transport with one original endpoint pair for each middle source e, uniformly, has a degree-one endpoint matching column and can still have 100% abstract blocked mass. Therefore **D2 matching columns + C3 uniform middle marginal + C2 sparse original overlap rows** are NOT, by themselves, a valid proof of a gap. The additional simultaneous physical rectangle-product origin and end-clean conditions in D1 remain essential.

Next productive targets are **non-tautological**:

1. Exact low-rank/singular-value constraints on the TRUE rectangle decoder K_{u,v} and original anchor-blocking mask *composed together*, rather than applying the abstract GQ spectral gap to arbitrary T.
2. A sharp pairwise pseudorandomness or forbidden-subrectangle lemma for true original labels in all admissible G*.
3. A complete original GF(5) oracle compensating structured pathological high-blocking rectangles via accepted C/B, B/C and other six-incidence classes, without equating a physical C6 with a positive original motif.

None of these three is solved here.

## Implementation and acceptance

- \`research/hyp105_issue230_nb_rectangles.py\`: deterministic validation of two actual coordinate cuts, source-pair provenance, exact independent-neighbour rectangle product weights and original endpoint decoders, D2 injective per-oriented-edge q/r matching, D3 strict stationary atom ceiling, optional true D4 information diagnostic.
- \`research/test_hyp105_issue230_nb_rectangles.py\`: four real original W(3,2) global injection fixtures, genuine W(3,4) lex/random, independent full NB3 path enumeration that must match original rectangle transport exactly in Fraction arithmetic, strict negative tests for full-G cherries / incorrect coordinate cuts / bad global injections, and small abstract D4 scaling checks.
- \`docs/research/HYP-105-ISSUE230-EICE003D-NB-RECTANGLES.md\`: mathematical proofs and limitations.
- \`.github/workflows/hyp105-issue230-eice003d.yml\`: GitHub-hosted focused CI and unchanged-parent regressions.

All s=2,4 runs are *finite structural falsifiers*, not an all-h quantitative proof by extrapolation; D1–D4 have independent all-h arguments. Root Branch A/B remain OPEN; EICE-003-D is research-only / DRAFT, no merging or issue closure.
