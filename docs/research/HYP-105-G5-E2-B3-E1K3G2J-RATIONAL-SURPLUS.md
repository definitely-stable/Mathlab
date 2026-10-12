# HYP-105 E1-K3-G2-J — exact rational necessary-constant frontier for seven-S surplus

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of [PR #382](https://github.com/definitely-stable/Mathlab/pull/382), pinned parent HEAD `165785dacd0005587b16a8242f307dcda9d1233b`. Neither main nor parent branches are changed.

## 1. Original research problem and the NOT-PROVED theorem

For each s=2^h, h>=1, and ALL injective physical pair mappings f,g of the original incidence geometry W(3,s), write `S_s(f,g)` for the count of DISTINCT ORIGINAL SIX-INCIDENCE supports accepted by one of the seven positive GF(5) families; write `J_s(f,g)` for the exact Kikuchi repeated-source cross six-cycle witnesses, including both dual source sides. The sought new proof obligation is to find universal constants `alpha>0, beta>=0` satisfying

```
S_s(f,g) >= alpha*s^6 - beta*J_s(f,g), for EVERY h>=1 and EVERY legal coherent f,g.
```

Neither this inequality with any positive alpha nor `J_s<=K*S_s` for any absolute finite K has been proved. Existing C6/R3 total-motif lower bounds cannot be transferred to S without controlling all excluded classes. Finite W32/W34 fits cannot establish universal constants. Incomplete positive W34 S target discovery is NEVER valid to refute an inequality requiring an upper value of S.

## 2. Exact all-h necessary coefficient theorem (PROVED, not sufficient)

For a true legal model m=(s,f,g), the desired inequality is equivalent at this point to

```
alpha <= (S(m) + beta*J(m))/s^6.
```

For any finite collection F of TRUE legal labeled original GQ maps (which may use different h), define the exact finite envelope

```
A_F(beta) := min_{m in F} (S(m)+beta*J(m))/s(m)^6, beta>=0.
```

**Theorem J1 (finite separation and universal necessity).** Every universally valid pair (alpha,beta) with alpha>0, beta>=0 must satisfy `alpha<=A_F(beta)` for ALL finite legal F. If `alpha>A_F(beta)`, some explicitly enumerated legal coherent original W(3,s) labeling in F gives a strict finite COUNTEREXAMPLE to those proposed constants. Consequently

```
A_*(beta) = inf_{h>=1,ALL legal f,g} (S_s+beta*J_s)/s^6 <= A_F(beta).
```

The function A_F is an exact nondecreasing concave piecewise-affine rational-slope function for finite F with rational integer S,J and integer s. For any proposed all-h charging `J_s<=K*S_s`, each true finite map with S>0 requires `K>=J/S`; if a true finite map has S=0 and J>0, NO finite K is possible. These are necessary constraints, NEVER certificates of a positive universal alpha, beta, K or Branch A.

**Proof.** Substitute each legal finite f,g into the quantified universal inequality. Rearrangement yields the individual upper line. Taking finite minima preserves a necessary condition. A strict breach identifies a full original map with certified S,J; it is a true counterexample to the PROPOSED constants. A finite minimum of affine nonnegative-slope lines is piecewise affine, monotone nondecreasing and concave. The charging K condition follows by division when S>0. No distributional or independence assumptions.

## 3. Exact rational support-interval theorem (PROVED)

All W32 candidates have s^6=64. For each map m the line is `l_m(beta)=(S_m+beta*J_m)/64`. Drop dominated same-slope higher-S lines, then:
- At beta=0 choose the smallest S and break ties by the smallest J.
- The next possible switch to a smaller J line occurs at `(S_new-S_old)/(J_old-J_new)`. Choose the EARLIEST rational switch strictly later than the current start.
- At a tie choose the smallest slope J for the interval immediately to the right.
- For each resulting bounded interval `[u,v]`, verify the purported active line <= **EVERY** other candidate line at both endpoints using exact fractions. Since affine differences are affine, endpoint validity implies the inequality for every real beta in that interval. For the final unbounded ray verify the same inequality at its start AND that no candidate has smaller slope.
- Independently construct every nonnegative pairwise rational line intersection, evaluate every intersection and every intermediate rational midpoint, plus points on the final ray. Disagreement invalidates acceptance.

This is a machine-checkable FINITE line-envelope theorem. It can rigorously refute specified candidate alpha,beta values, but cannot make A_F a universal lower bound A_*.

## 4. Exact source corpus and exhaustive/nonexhaustive boundaries

The Contract runs:
- complete baseline W32 lex and reverse-line maps;
- EACH of 105 whole-original-point-pair and 105 whole-original-line-pair single transpositions of lex (entire previously verified G2-H single-swap shell);
- the actual legal dual-side original source-label anchor from G2-I's best correlated path (left(0,14),right(0,14)), and each of its SIX published whole-source-label swaps:
  `left(1,4)`, `right(2,4)`, `left(2,13)`, `right(3,13)`, `left(2,3)`, `right(1,14)`.
  Published exact six `(S,J)` pairs are `(168,29),(132,18),(117,15),(101,17),(90,21),(94,26)`; they must be reproduced from real original incidence sets.

Total **219 distinct named input models** = 2 baselines + 210 one-swap + 7 correlated anchor/path maps. No deduplication of labels is claimed; only duplicate (S,J) support lines are safely coalesced to form the envelope. Every source sixset is counted from the complete independently verified B0 62,370-left-candidate generator, for that SAME globally coherent f,g; every J comes from the exact actual original source Kikuchi cross witness generator. Class-positive GF5 weights are reported but not substituted for S. Every full-shell model is re-evaluated and the G2-H known minima `min S=176`, `max J=47`, `min(S-J)=139` checked exactly.

Concretely at beta=0 a tested correlated map has S=90 at s=2, giving **`alpha<=90/64=45/32`** for ANY proposed UNIVERSAL beta=0 theorem. Thus the proposed all-h bound `S_s>=2*s^6` is rigorously refuted by a legal W32 globally coherent labeling (S=90<128). This is a candidate-constant NO-GO, NOT a refutation of all positive alpha or of Branch A (which is a different unconditional asymptotic assertion).

## 5. Acceptance and next mathematical obligation

GitHub-hosted 25-minute dedicated Contract runs lightweight rational hull tests, then ONCE full 219-map count and rational piece certificate. Report must provide finite model count, distinct S,J pairs, all rational breakpoints, independent intersection probes, finite necessary K lower, exact counterexample to (alpha,beta)=(2,0), source-count digest. INDEX and complete Research must be SUCCESS on exact PR child HEAD; Draft remains pending independent review.

Next K3-G2-K: seek an actual ALL-H positive `S>=alpha*s^6-beta*J` theorem by deriving a source-incidence/physical-label tensor inequality whose failure has explicit finite counterexamples. The rational finite envelope is a NECESSARY-coefficient screen, not a proof of existence. The second independent all-h `J<=K*S` gate also remains open. No ASET exponent and no issue closure.


## 6. Exact 219-map rational frontier, first hosted result (2026-10-12)

[Dedicated GitHub-hosted Contract #38221690490](https://github.com/definitely-stable/Mathlab/actions/runs/38221690490) **SUCCESS** at original child HEAD `9609eed8de98057b6571fd37e36988b1f0102007`. All independently hosted rational-interval tests, exact original W32 B0 accepted GF5 S sixsets, and 210 true G2-H one-swap shell / seven real G2-I coherent-correlated maps agree. Exactly **219** named physical labelings, **198** distinct exact (S,J) pairs, and **141** independent rational pair-intersection/midpoint probes.

**Finite necessary all-h upper envelope:** For EVERY proposed universal all-h `S_s>=alpha*s^6-beta*J_s`, beta>=0, a necessary (NOT sufficient) condition for the 219 checked W32 true-label corpus is:

```
              (90 + 21 beta)/64,     0 <= beta <= 11/4   [corr:5]
alpha <=      (101 + 17 beta)/64,    11/4 <= beta <= 8  [corr:4]
              (117 + 15 beta)/64,   beta >= 8           [corr:3]
```

At exact beta=11/4 and beta=8 adjacent lines agree. All 219 true original points lie ON OR ABOVE the three supporting segments (in S+beta J space), and every active line corresponds to the SAME actual coherent f,g used to count its S and J. The two breakpoints and every line inequality were verified using `fractions.Fraction` and independent all-intersection replays. No W34 partial discovered target count enters a negative coefficient certificate.

The distinct source maps forcing these three lines are among the previously independently reproduced best G2-I path states:
- `corr:5`: `S=90, J=21`, hence if beta=0, `alpha<=45/32`; proposal alpha=2,beta=0 is *FALSE*, with exact legal W32 counterexample `S=90<128`.
- `corr:4`: `S=101, J=17`.
- `corr:3`: `S=117, J=15`.

**Additional universal charge-K necessity:** A genuine legal original W32 map `S=94,J=26` yields `J/S=13/47`. Any universal `J_s<=K*S_s` must have `K>=13/47` (a necessary lower floor on possible K; existence of ANY such finite universal K remains UNPROVED).

Exact SHA256 over the ordered list of 219 complete original (name,S,J,certified GF5 floor numerator) counts:

`2bed34a0fc5c6181ffc239f60e69cbd7682ee71d1585310c30f66996df89c461`.

**Independently verifiable scientific scope:** The rational necessary frontier proof is universal as a logical implication from any legally labeled source map, while the explicit three-piece numerical envelope is ONLY the selected 219 finite W32 models. It is a rigorous elimination oracle for too-large proposed constants. It neither establishes positive universal constants nor gives `S_s=Omega(s^6)`, Branch A/B, entire full-R3 upper or any ASET exponent. After this report, regression invariants have been pinned in the dedicated Contract and must be rechecked at final exact PR child HEAD before acceptance.
