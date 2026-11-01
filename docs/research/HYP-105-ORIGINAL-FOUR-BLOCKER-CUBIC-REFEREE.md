# HYP-105 / #230 — AA4-R5CUBIC: independent all-four-position FULL/CORE mathematical referee

**Scope:** a self-contained independent AI mathematical audit of R5, with a new exact
source-flag cubic count and genuinely different physical-corner finite falsifier.
Not a claim about the entire Branch A or a new ASET exponent.
Child Draft of frozen PR #706 at `8bd7c1d91b33f200a0d596a91ba01d704486128a`;
`main`, parents and original issue are unchanged.

## 1. What must be audited

Fix the genuine symplectic generalized quadrangle `W(3,s)`,
`s=2^h, h>=1`; the complete ORIGINAL source incidence flags
`\mathcal F={(p,ell):p incident ell}`; and any fixed, separately globally
pair-injective, arbitrarily correlated maps
`f:p->binom([a],2)`, `g:ell->binom([a],2)`.
For an arbitrary retained set `I subseteq mathcal F`, the physical CORE
`H_I` is the simple graph on the actual coordinates `[a]x[a]`,
with **BOTH paired opposite-corner physical diagonals** of each source ID in I.
NO source relabeling, cloning or independent physical edge maps are allowed.

The unique GQ projection of every nonincident original point/line pair
`(q,r)` is `q--ell--p--r`. Those three ORIGINAL source anchors are
`(q,ell),(p,ell),(p,r)`. They are read from the **FULL original geometry**,
regardless of whether any of those flags survived I.

Given a coordinate-proper directed physical three-edge CORE walk
`W=(v0,v1,v2,v3)` with six distinct first/second? More precisely,
**FOUR distinct first coordinates and FOUR distinct second coordinates**,
if endpoint label pairs decode unique ORIGINAL q,r with q nonincident r,
let its four internal-blocker mask be

```
bit 0: v1.left  belongs to f(p)
bit 1: v2.left  belongs to f(p)
bit 2: v1.right belongs to g(ell)
bit 3: v2.right belongs to g(ell).
```

Also retain the independent Boolean `endgood` requiring `f(p)`
to avoid BOTH first endpoint coordinate symbols and `g(ell)` to avoid
BOTH second endpoint symbols. This is the real FULL source endpoint
condition used downstream; it is NOT a requirement that the anchors
are retained in CORE.

## 2. NEW exact ALL-h four-mask ORIGINAL cubic theorem

Let `x_i=1[i in I]`. Consider ALL genuine coordinate-proper oriented
physical length-three paths sourced from three ORIGINAL flags in the
FULL real source, whose physical endpoint pairs decode a nonincident
original q,r. Each path has three **DISTINCT** owner IDs:

- Every physical edge has exactly one ORIGINAL owner by separate global
  pair-injectivity: its two first coordinates recover p, and its two
  right coordinates recover ell.
- If the same original flag ID appeared twice in a coordinate-proper
  length-three walk, its original point label f(p) would contribute the
  same two first coordinate symbols twice. But coordinate-properness
  demands all four first coordinates distinct. Contradiction.

For each unordered ORIGINAL 3-flag support `T`, each `endgood` bit b,
and each four-position blocker mask m in [0,15], let
`c[T,b,m]` be the number of directed **FULL-source-oriented** physical
proper 3-walks with source-flag owner support T, genuine nonincident
original endpoint projection, and class (b,m).

Then for EVERY legal I, EVERY h and EVERY fixed correlated f,g,

```
N_{b,m}(I) = SUM_{T subseteq mathcal F, |T|=3}
                c[T,b,m] PROD_{i in T} x_i.
```

Each c is a **nonnegative INTEGER**. This is a simultaneous EXACT
homogeneous squarefree **degree-three** polynomial for all 32
(`endgood`, four-mask) class populations, not an asymptotic fit.

**Proof:** all oriented physical CORE edges have immutable unique
source owner IDs. A physical 3-walk is present in H_I iff all THREE
distinct owner IDs belong to I. The original endpoint projection,
endgood predicate and mask depend only on the fixed full maps,
full geometry, and the physical walk; deleting OTHER source flags
cannot change them. Thus the count decomposes exactly over supports T
with coefficient c[T,b,m]. This also proves monotonicity for arbitrary
source-flag CORE deletion without a probability assumption.

**Consequences:**

- The exact good/unblocked B/B-eligible path count is `N[True,0](I)`.
- The exact good internally blocked UNION is
  `sum_{m=1}^{15}N[True,m](I)`, with *no double counting* even when
  multiple blocking positions are true on the same path.
- The exact count in blocker position j is
  `sum_{m: m & (1<<j)}N[True,m](I)`.
- Reversal gives a coefficient-preserving involution exchanging
  blocker bits 0<->1 and 2<->3. The two inner-left and two
  inner-right position counts therefore agree separately.
- If ANY of the three full projection anchor IDs is absent in I,
  the monomial still survives **provided the three path owner IDs
  are in I**. Requiring anchors in CORE would be a false theorem.
- The equality is for actual **ORIGINAL flags**, not the entire
  unrelated class of arbitrary three-edges / synthetic physical paths.

## 3. INDEPENDENT re-derivation of the historical mixed source tensor

For first-inner-left blocking, use full original point stars
`S_x={p:x in f(p)}`, FULL source right pencil counts
`R(p,y)=#{r: p incident r and y in g(r)}`, and CORE pencil
`R_I(u,y)=#{lam:(u,lam) in I and y in g(lam)}`.
The exact mixed contraction is

```
K(p,u)=sum_y R(p,y) R_I(u,y)
Phi=sum_{u} sum_{(x,k) in oriented f(u)} sum_{p in S_k}
       |C(p) intersect S_x| K(p,u).
```

Expand Phi by actual source tuples
`(u,lam),(x,k),(y,t),p,q,r`, where
`(u,lam) in I`, `p in S_k`, `q in C(p) intersect S_x`,
`r incident p` and `y in g(r)`.
The incident subpopulation `q incident r` is EXACTLY Psi.

For nonincident q,r, the genuine original GQ axiom forces a
**unique** projection `q--ell--p--r` through the chosen p.
The resulting physical triple
`((x,y),(k,t),(z,w))`, where `f(q)={x,z}` and
`g(r)={y,w}`, determines all original tuple entries uniquely:
its first physical edge recovers the CORE source ID (u,lam),
and its two endpoint label pairs decode q,r; GQ reconstructs p,ell.
Conversely every eligible first-inner-left ORIGINAL physical triple
arises this way. Therefore EXACTLY

```
B_left=Phi-Psi >= 0.
```

This identity does NOT require `(p,r)`, `(p,ell)` or
`(q,ell)` to remain in CORE.

Let `m(v1,v3)` be the number of eligible first edges reaching v1
with fixed last endpoint v3. Then `m<=deg_I(v1)`, so Cauchy yields
the exact all-h finite-graph inequality

```
W_left^2 <= B_left * SUM_{v1,v3}
                m(v1,v3) (A_I^2)[v1,v3]^2
          <= B_left * tr(D_I A_I^4)
          <= B_left * Delta_I * tr(A_I^4).
```

Here W_left counts physical first-inner-left 3-walk completions,
INCLUDING improper completions. Therefore it upper-bounds the good
proper-position count appearing in the new cubic census. Apply path
reversal and physical coordinate transpose to obtain the other THREE
positions; use the ordinary union bound over all four, which holds
regardless of mask overlap.

The existing R5 higher-level envelope
`B<=15 sqrt((K+1)T) s^(23/4)`,
`tr(A_I^4)<=L4 s^5`, `Delta_I<=T s` gives
`I_internal <=4 sqrt(15 sqrt((K+1)T)*T*L4) s^(47/8)`
for fixed K,T. The new exact cubic does NOT assert those old
asymptotic inputs without their own source lemmas.

## 4. Two independent REAL source algorithms and how they differ

**ORIGINAL-first oracle:** enumerate all three-step chains of
ORIENTED edges labelled with immutable actual original flags, not
adjacency from the CORE; derive a support T and class (b,m) using the
FULL original GQ projection. Build ALL nonnegative coefficients c[T,b,m]
before selecting any core.

**PHYSICAL-first oracle:** for each independently chosen CORE I,
reconstruct a physical adjacency list by pairing original flag
diagonals; enumerate actual directed physical three-walks and
classify the nonincident original endpoints. Compute the GQ projection
by a DIFFERENT source procedure: original q's line pencil followed by
line intersections, rather than the first method's line r point-star
traversal.

The two approaches must agree on ALL 32 class counts for all selected
cores. The tests additionally cross-check historical four-position
physical totals, reversal invariants, source-provenance failures,
and nonvacuity. Genuine W32 full maps + all 128 subsets of seven
source IDs and genuine W34 protected 16-flag source configurations
are used. A real positive witness with a FULL anchor outside its
selected 3-flag CORE is required to pass.

**Important limitation:** these are independent computational
enumerations of the same precise finite model. They do not prove
the asymptotic spectral/cauchy input by finite checks; Section 3
gives the mathematical double-count argument. This is an internal
independent AI referee, not a claim of real-world human endorsement.

## 5. Scientific outcome and next action

R5 has a precise proof and a stronger self-contained all-four-mask
ORIGINAL cubic model, with exact nonnegative deletion coefficients.
The previously existing mixed tensor proof is independently
re-derived above. If hosted falsifiers all pass, this provides
substantial new evidence for R5 but does NOT by itself prove R2,
R6, GF5, or the entire original Branch A source chain.

Following successful CI, prioritize R6 original six-ID image
and the same-source GF5 signed acceptance, *not* more
constant polishing. Keep #230 OPEN_WITH_FORMAL_BLOCKER pending
the unresolved mathematical proof obligations (regardless of who
performs the checks); no automatic merge or theorem exaggeration.
