# HYP-105 / issue #230 — AA4-AF: every-original-root-pair robust B/A source gate and local quenched transfer

**All-h restricted mathematical claim, research-only Draft.** Stacked child of [AA4-AE PR #512](https://github.com/definitely-stable/Mathlab/pull/512), exact pinned parent SHA \`3b101175bb266eced914294fc17185c8aa04d184\`. Preserve TRUE original W(3,2^h) source geometry, exactly six distinct actual original incidence IDs Q, one globally complete physically injective typed point map f, and one independently drawn uniformly COMPLETE but globally shared typed line map g. This is a *local root-flag pair* guarantee, not the all-map adversarial #230 Branch A. No production code, no main changes.

## 1. Critical nonduplication and scientific scope

The earlier \`hyp105_g5e2b3e1b1a_one_sided.py\` already rigorously proved the **GLOBAL** one-sided theorem \(\forall f:\mathbb E_{\mathrm{full\ uniform}\ g} C_{B/A}(f,g)=(140+o(1))s^6\), using a physical B template count and a source-column collision floor. AA4-W later supplied exact one-side/global seven GF5 conditional transfer kernels. **Do not misattribute a universal quenched global expectation to this slice; it is prior art within this very repository.**

The new issue230-AF theorem strengthens the **distribution across original roots**: for every complete GLOBAL f and for **EVERY separately prescribed actual original point p and EVERY prescribed pair of its ACTUAL distinct incident source lines** \(\{\ell_0,\ell_1\}\), the source B/A first gate is positive with a uniform all-h quantitative lower. No averaging over roots, no permutation of original incidence graph and no other source positions are required. Under one uniform COMPLETE GLOBAL g, each rooted original pair has a positive expected GF5-accepted opposite physical A transfer, with an independent explicit constant. This is not contained in the older global statement, since positivity of a global sum alone need not entail positivity in each pinned source cohort.

## 2. All-h exact minimal physical alphabet and occupied complement C4 lemma (AF-1)

Let s=2^h, h>=1; d=s+1, V=(s+1)(s²+1), a=min{t:C(t,2)>=V}, K=C(a,2), m=K−V. Minimality forces \(0\le m\le a-2\). Let f be ANY complete globally injective original point-label map \(P\hookrightarrow E(K_a)\), so its image is the full set of physical unordered edges except exactly m missing edges.

Fix an ARBITRARY actual original source point p, with its globally assigned physical edge e=f(p). The complementary physical coordinate alphabet comprises n=a−2 other vertices. Any simple physical 4-cycle C4 on four of these n vertices has four physical edges, and all four represent four distinct actual original point factors \(q_1,\ldots,q_4\) exactly when those edges lie in im(f). One complete K_n supports exactly \(3\binom n4\) unoriented C4. One missing physical edge lying *inside* the complement participates in exactly \((n-2)(n-3)\) different C4 (pick two other vertices and either of two C4s containing that prescribed edge). A missing edge touching either excluded root coordinate affects ZERO such complement C4s. Therefore the simple missing-edge union bound yields **for EACH p and EACH globally injected f simultaneously**:

\[
\boxed{
C_4^\mathrm{occ}(p;f)\ge
\mathcal C_s:=
\max\left(0,\;
3\binom{a-2}{4} -m(a-4)(a-5)
\right).
}
\]

This is a real occupancy certificate for **each** original p, not an ensemble mean, and correctly permits K>V (unoccupied physical pairs) in genuine W(3,4), W(3,8), etc. It does not depend on the chosen second map g, on the actual original root p geometry or on an artificial source relabeling.

## 3. All-h TRUE-ORIGINAL GQ rooted flag-pair local four-rook lower (AF-2)

Fix **TWO different actual original source flags** \((p,\ell_0)\), \((p,\ell_1)\) through the same actual original point p. Select ANY ONE occupied complementary physical C4 from AF-1, whose four edges globally correspond to four other **distinct actual original points** q1..q4 under the ONE map f.

Let \(A_i=N_{\mathrm{GQ}}(q_i)\setminus\{\ell_0,\ell_1\}\) be their genuine source-line neighbors with the two root lines excluded. Original GQ girth8 implies:

- \(|A_i|\ge d-1=s\). Because a distinct original point qi cannot be incident to BOTH source lines through p without an original 4cycle.
- \(|A_i\cap A_j|\le1\) for i≠j (the two distinct original points share at most one actual original line).
- The true source Q of two pinned flags plus four distinct actual flags \((q_i,t_i)\), \(t_i\in A_i\), \(t_i\) pairwise distinct, is a legitimate six-DISTINCT-original-incidence-ID source B/A forest Q with the pinned unique repeated point p and original source line A profile.

Among at least s⁴ ordered candidate source assignments, the six row-pair line collisions remove at most \(6d^2\) (fix one common line choice ≤1, two remaining arbitrary neighbor choices ≤d²). In addition, a greedy distinct-source assignment gives \((s)_4=s(s-1)(s-2)(s-3)\) for s≥4. Hence **each physically realized original rooted B C4** supports at least

\[
\mathcal R_s=
\max\left\{0,\;
s^4-6(s+1)^2,\;
s(s-1)(s-2)(s-3)
\right\}
\]

different genuine source B/A Q with these two pinned original flags.

Every different occupied physical C4 corresponds to a different quartet of actual globally labeled point factors and so produces DISJOINT original six-Q families at fixed root and flag pair. Every original B/A Q has a UNIQUE repeated original point and its unique two selected flags, so the Q families also partition disjointly over all \(V\binom d2\) such root pairs. Thus **for all h≥2 (s≥4), every f, every actual p and every prescribed root line pair**,

\[
\boxed{
F^{\mathrm{src-BA}}_{p,\{\ell_0,\ell_1\}}(f)
\ \ge\ \mathcal C_s\mathcal R_s\ >0.
}
\]

For s=2 the bound may vanish; no all-root s=2 positivity is asserted. This is *source-only* genuine GQ A profile plus physical B on f, NOT an assertion that an adversarial g accepts opposite physical A.

## 4. Exact one-GLOBAL-uniform-opposite-map transfer and new LOCAL guarantee (AF-3)

Let g be chosen independently of fixed f, uniformly among all COMPLETE globally injective maps of the entire original line factor set L into E(K_a). For any FIXED source B/A six-Q with six DIFFERENT true original line factors, their six physical unordered edges are uniformly distributed across six ordered distinct physical K_a edges without replacement. The probability of physical six-vertex, six-edge 2-factor type A equals exactly the **previously certified historical one-global-map kernel**

\[
\alpha_s=\frac{70(a)_6}{(K)_6},
\]

where \((x)_6=x(x-1)\cdots(x-5)\). This transfer uses ONE random complete global injection shared by ALL source Q. Different Q event correlations are unrestricted; only linearity of expectation is used.

Therefore for **each separately fixed actual root and its two flagged lines** and **every adversarial fixed complete f**:

\[
\boxed{
\mathbb E_{\text{ONE complete global }g}
C^{B/A}_{p,\{\ell_0,\ell_1\}}(f,g)
=\alpha_s F^{\mathrm{src-BA}}_{p,\{\ell_0,\ell_1\}}(f)
\ge \alpha_s\mathcal C_s\mathcal R_s.
}
\]

The exact equality is a one-global-map conditional linearity identity; the quantitative **local lower** is new. This does not imply the event holds for **every** g, even though g is globally consistent in every six-Q. Symmetric theorem with point and line types swapped holds for every fixed complete original g and one uniform complete f.

### Explicit order-independent positive constants, all s=2^h≥8

For s≥8, a≥35, n=a−2≥33 and m≤n. Therefore

\[
\mathcal C_s
\ge 3\binom n4-n(n-2)(n-3)
=\frac{n(n-2)(n-3)(n-9)}8
\ge\frac{n^4}{64}\ge\frac{a^4}{1024}.
\]

Also \(\mathcal R_s\ge s^4-6(s+1)^2\ge s^4/2\). By the minimal physical alphabet \(a\le2s^{3/2}\) (proof: \(b=\lfloor2s^{3/2}\rfloor\) satisfies \(\binom b2\ge(s+1)(s²+1)\) for all s≥8) and \(a\ge10\),

\[
\alpha_s
=\frac{70(a)_6}{(K)_6}
\ge\frac{70(a/2)^6}{(a²/2)^6}
=\frac{70}{a^6}.
\]

Hence with all constants explicit for EVERY original root flag-pair:

\[
\boxed{
\mathbb E_g C_{p,\{\ell_0,\ell_1\}}^{B/A}(f,g)
\ge\frac{35s^4}{1024a^2}
\ge\frac{35s}{4096}
\ge\frac{s}{128},
\quad s\ge8.
}
\]

Summing the **disjoint actual original source root-flag-pair families**, \(V\binom{s+1}2\ge s^5/2\), yields the independent (weaker than the prior 140-leading constant, but **root-locally certified**) total:

\[
\boxed{
\forall f:\quad
\mathbb E_{\text{ONE GLOBAL }g}C_{BA}(f,g)
\ge\frac{s^6}{256},\quad s=2^h\ge8.
}
\]

This final sum is a corollary, not the main new result. The prior \((140+o(1))s^6\) uniform global conditional expectation theorem is asymptotically vastly stronger numerically, and is acknowledged above. The new value is that every original root-pair separately has expected \(\Omega(s)\) distinct accepted GF5 source-Q witnesses.

## 5. Independent real-original finite falsifiers and protocol

- All-h symbolic integer oracle computes minimal K_a, unused m, exact complete-C4 count and missing-edge influence, true source four-rook union+greedy floors, exact rational historical uniform global physical A kernel, per-root guarantee, and aggregate sum; check s=2^1..2^18 with no floating point precision.
- Independently construct TRUE original W(3,2) all four historical global source K6 injection models S68/S72/lex/reverse. K=V=15 and each physical root e has exactly 3 occupied complementary physical C4. Exhaust **all 15 original point roots and all 15 original line roots** for each model and verify against a second adjacency-based *oriented physical C4 walk trace* divided by eight, not the same omitted-matching enum.
- TRUE original W(3,4), a=14,K=91,V=85,m=6. The physical-C4 universal per-original-root floor is \(3\binom{12}4 -6\cdot10\cdot9=\mathbf{945}\). For genuine complete global lex and random physical injection maps on both typed sides, test several true original roots and different actual pinned root-flag pairs. Independently count occupied C4 via adjacency walks and 4-C4 inverse-label enumeration; exact literal genuine source four-neighbor incidence assignments (≤5⁴) for several actual occupied physical C4 patterns, verify each ≥ \(\mathcal R_4=\mathbf{106}\). Full true original global f/g maps retained; no pretending missing K_a edges are present.
- Strict negative controls fail malformed injections, source incidence truncations, invalid original source root/pinned pair index; preserve original six source flag distinctness. Real-source transvection and independent physical coordinate permutations keep each rooted population invariant when transporting p and its pinned incident flag pair together.
- No finite W(3,8) exhaustive full six-Q run needed; symbolic all-h theorem covers every order, while TRUE W32/W34 exact finite tests validate physical/source definitions.


### Hosted original W(3,4) independent root certificate (first exact scientific data)

TRUE W(3,4), minimal physical K14, V=85 actual original points/lines of degree d=5, K=91 physical coordinate pairs and exactly 6 unoccupied physical pair images. On **one actual root=0** on each original typed side, for global lex and globally shuffled random typed injection fixtures, independently counting all occupied physical complement C4 by (i) direct 4-vertex/three-matchings inverse-source-label construction and (ii) entirely independent simple oriented 4-step adjacency-walk/8 gives:

| Global complete original labels | Original rooted type | Actually occupied physical complement C4 | Every-f physical universal floor | Every-C4 actual original source 4-rook guaranteed floor | Per root+actual two flags source-Q floor |
|---|---|---:|---:|---:|---:|
| lex | point (B-left/A-source) | **1,050** | 945 | 106 | 100,170 |
| lex | line (B-right/A-source) | **1,050** | 945 | 106 | 100,170 |
| random | point (B-left/A-source) | **1,083** | 945 | 106 | 100,170 |
| random | line (B-right/A-source) | **1,081** | 945 | 106 | 100,170 |

These **are true W34 occupied physical-image counts for root=0**, not all-root extrema or s→∞ averages. Independent explicit actual original-neighbor line/point four-rook choices for the first 12 occupied C4s per true root and pinned flag pair each satisfy the per-C4 bound 106 (directly tested with all at most 5⁴ choices; no fake independent redrawing of the global point/line edge injections). Additional standalone unittests exercise root=17, multiple root-flag pairs and true Sp(4,4) source transvection plus independent physical relabels. The universal source support floor 945×106=**100,170 actual distinct original Q per prescribed root-flag pair** holds analytically at s=4 for *every* physically injected original map, including ones not included in the finite test fixtures. No all-adversarial-g positive GF5 second-gate assertion follows.

**Exact all-h CI cost discipline:** the preexisting older random-global probability helper uses a *linear-in-physical-alphabet-size* search for minimal a; high orders s=2^18 would make repeated use impractical. The new theorem obtains a by \`math.isqrt\` in O(1) large-integer steps and validates the exact six-term Fraction probability independently for h=1..18; the legacy baseline is cross-checked only for bounded h≤7, without relaxing any theorem or f/g global-injection requirements. GitHub-hosted runners only.

## 6. Scientific decision, next blocker, research acceptance

**PROVED (all-h, restricted):** every physically complete globally injected original f has per-each-actual-root-and-two-original-flags a uniformly large occupied complementary physical C4 population; GQ 4-cycle-free source-neighbor structure then forces at least \(\mathcal C_s\mathcal R_s\) distinct true source B/A forests for *each* pinned pair; one globally uniformly random full opposite injection has exact **local** mean ≥\(\alpha_s\mathcal C_s\mathcal R_s\), and ≥s/128 for s≥8. Dual result holds.

**ALREADY KNOWN, not claimed new:** existence of a global fixed-f average \((140+o(1))s^6\), the source-only per-realized 4-rook matching floor (parallel Y5), 70 physical A six-edge patterns and global one-sided transfer kernel. The novel quantifier strengthening is **uniform across EACH prescribed original root-flag-pair** with a nonvanishing physical occupancy bound even when K>V, plus an explicit all-order constant and independent live-GQ finite falsifiers.

**NOT PROVED:** forall f forall g a positive Hall-positive physical-A acceptance count, HYP-105 issue230 Branch A/B/C, a full R3/ASET exponent or a universal finite minimax. One global random g can yield positive mean while special correlated physical g suppresses many rooted accepted motifs; the previous S68/S72 and source GQ eight-cycle evidence warn against all-g extrapolation.

**True next science gate:** apply globally shared g Hall/JPKC/EICE constraints to control the mismatch between many **nonzero source first-gate cohorts** and simultaneously physical-A-accepted cohorts across all four canonical adversarial physical sectors; or construct an explicit globally injected counterexample to this intermediate all-g claim, tracking all seven historical GF5 classes including D6. More source first-gate counting or new random-global mean asymptotics alone is low priority.

**Integration:** research-only stacked Draft child of PR #512, no main merge/edit. Require exact-final-HEAD specialized CI, INDEX, Proof Audit, Full Research SUCCESS and independent mathematical reviewer before acceptance. Preserve versioned mathematical Markdown, code, source-normalized exact tables and negative witnesses; register SHA-pinned accepted claims and their source dependencies in authoritative RCP JSON and regenerate five derived Markdown registers **after independent review**. Do not hand-edit generated registry docs. Root #230 OPEN.
