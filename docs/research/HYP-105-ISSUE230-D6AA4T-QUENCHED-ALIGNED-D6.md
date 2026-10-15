# HYP-105 / issue #230 — D6-AA4-T: genuine positional D6 tensor and all-h quenched bound

**Scope.** Exact joint original-six-incidence positional tensor, and a uniform ALL-h lower on the expected aligned D6 count for EVERY adversarial fixed global map of one source type when the other type is independently sampled as ONE uniform complete global injection. This is NOT an adversarial f,g lower, NOT a solution to root #230, nor full GF5 R3/ASET. Research-only Draft child of AA4-S #479 at exact parent HEAD 357b3d201e14713668fbd045b450ffd279610081. Main unchanged.

## 1. Exact all-h ORIGINAL 60-fibre positional tensor

Fix any genuine ORIGINAL W(3,s), s=2^h>=2. Its actual source incidence ID universe is E. Let Q_AA consist of six different original-incidence-ID subsets Q whose point and line source factors are both six distinct genuine ORIGINAL factors. Canonically order the six unchanged source incidence IDs so both physical sides share columns 0,...,5. Let C6 denote the 60 labelled simple connected six-cycles on these six ORIGINAL positions.

Let A_f(H,Q)=1 iff the six f(source original point) physical unordered-edge labels at the six original positions of Q create six physical coordinate symbols, each appearing twice, whose coordinate-column incidence dual graph is precisely the labelled cycle H; otherwise zero. Define A_g(H,Q) analogously from the same six ORIGINAL incidence IDs and the complete line-factor map g. Then exactly, for arbitrary admissible complete globally typed-injective f,g:

    D6(f,g) = sum_{H in C6} sum_{Q in Q_AA} A_f(H,Q) A_g(H,Q).

The 60 cycle-position fibres keep both true source factor identities, all six incidence IDs, all physical coordinate pair labels and exact matching (not simply both physical projection marginals). Any accepted D6 contributes once at its unique H; unaligned A/A, disconnected A/A, and every non-AA Q contributes zero. This is a genuine original source/physical inner product, not a product-of-marginals claim.

Define T_f = sum_{H,Q} A_f(H,Q). This counts all left original-AA-connected candidates whose six original line factors are distinct, under one fixed full f.

## 2. Exact conditional theorem for ONE full random global g

Let V=(s+1)(s^2+1) be the number of genuine original points and of genuine original lines, d=s+1 the original source degree, and a minimal with K=binom(a,2)>=V. Fix ANY admissible complete globally point-injective f. Sample ONE complete uniformly random injection g from all V original line IDs to the K physical K_a edges, independently of f; do NOT sample separate g for different Q.

For every Q with A_f(H,Q)=1, its six ORIGINAL line source IDs are distinct. Their complete globally uniform g-images are therefore uniformly distributed over (K)_6 ordered choices of six distinct physical unordered pair labels. Given one connected positional six-cycle H, the right physical coordinate-column dual equals H exactly if the six edges of H receive six distinct physical coordinate symbols. This has precisely (a)_6 assignments; no automorphism quotient is permitted because Q positions are immutable and the assigned six physical symbols can be recovered from the pairs at their incident original columns. Hence

    p_D6(s) = (a)_6 / (K)_6,
    E_g[D6(f,g)] = p_D6(s) * T_f.

This is exact for arbitrary adversarial f and every h>=1. The right Q indicators are correlated under the SAME g but linearity of expectation is enough.

## 3. NEW uniform every-f quantitative lower, ALL h>=1

The complete physical K_a contains exactly (a)_6/12 different six-edge C6 subgraphs. The minimally injected f occupies V out of K physical edges and misses m=K-V<=a-2. Each missing K_a edge belongs to at most (a-2)_4 different physical C6s. Thus every f has

    N_occupied_C6(f) >= (a)_6/12 - m*(a-2)_4.

Every occupied physical C6 determines six DISTINCT original points by global injectivity. The TRUE ORIGINAL point/line incidence bipartite graph is d-regular. For any subset X of its actual points, counting actual source-incidence stubs gives d|X|<=d|N(X)|. Hall's matching theorem therefore gives six DISTINCT original lines, one incident to each of these six source points. For d>=6 the greedy injection of distinct original incident lines gives at least (d)_6 different line assignments. Each yields a unique actual six-original-incidence-ID Q whose left physical dual is a connected labelled C6, and different physical cycles cannot generate the same Q. Thus

    T_f >= [ (a)_6/12 - m*(a-2)_4 ] * max(1,(d)_6),

where for small d<6 the factor 1 is justified by genuine-original Hall matching, rather than a false falling-factorial claim.

For s>=8, a>=35, m<=a-2, d=s+1. Consequently

    N_occupied_C6 >= (a)_6/24 >= a^6/(24*64),
    (d)_6 >= (s/2)^6,
    p_D6 >= 1/a^6,

and therefore

    E_g D6(f,g) >= s^6/98304.

For s=2, a=6,K=15,m=0, occupied C6>=60, Hall matching>=1, p_D6=1/5005; exact rational 60/5005 > 2^6/98304. For s=4, a=14,K=91,m=6, occupied C6>=108900, Hall matching>=1, p_D6=(14)_6/(91)_6 and 108900*p_D6 > 4^6/98304. All calculations use exact integer/rational arithmetic. No finite asymptotic fitting.

**NEW RESTRICTED ALL-h THEOREM:**

    for every original W(3,s), s=2^h>=2, and every full f:
      E_{one uniform complete global g}[D6(f,g)] >= s^6/98304.

By genuine point/line GQ duality the same result holds for every fixed g and an independent single complete globally uniform f.

**Quantifier barrier:** min_f E_g D6 >= c*s^6 and min_g E_f D6 >= c*s^6 do NOT imply min_{f,g} D6 >= c*s^6, nor min_{f,g} S >= c*s^6. Genuine full W32 S68 and S72 have actual D6=0 while lex has D6=15 and reverse has D6=3. Thus the quenched theorem is genuinely about averaging or min-max, not an ASET exponent or Branch A/B solution.

## 4. Independent real ORIGINAL W32 oracle

For each full real W32 typed globally injected K6 labeling: independently list 60 distinct physical K6 C6 edge sets, invert the one original point map and enumerate actual original incidence IDs at each of six different source points with six different original line IDs. Canonically map Q to its connected six-position dual H, with no use of historical original-sixset generation. Independently reconstruct from AA4-Q's 51,030 left-A original Q list and retain source-line-distinct connected H, demanding equality of EVERY original Q -> H.

Join with ONE actual global right g on exactly the same Q and H; compare each D6 original Q to the historical full seven-GF5 Q classifier and AA4-Q independent two-sided join. Test S68,S72,lex,reverse, random complete global two-type permutations, true-original point-line duality, the counterfixture failing real GQ's unique anchor axiom, and exact 720 right-coordinate assignments for a fixed original connected H. Calculate exact rational p=1/5005 for W32, conditional expected D6=T_f/5005; do not confuse actual D6 for a chosen g with this conditional expectation.

Implementation comprises FOUR new research-only files: Python all-h proof/oracle, eight independent unit tests, this proof and limits document, dedicated 3-job GitHub-hosted CI. Require exact final AA4-T SHA dedicated + INDEX + Proof Audit + FULL Research SUCCESS, and separate independent mathematical proof review. Keep stacked Draft, no automatic merging or issue closure. Parent #230, #176, #169 remain OPEN.

### Independently observed exact W32 conditional-vs-deterministic separation

The independently enumerated TRUE ORIGINAL same-Q/H point-first and source-major tensor oracles both found T_f=21,186 for the full globally injected S68 and S72 point maps. Consequently their EXACT conditional expectation for ONE complete globally uniform right original line map is

    E_g D6(f,g) = 21,186 / 5,005 = 1,926 / 455.

Yet the specified complete actual original right g of S68 and of S72 has D6(f,g)=0 (both independently checked against the historical seven-GF5 original source classifier). This is an explicit **true-original finite quantifier obstruction**: positive conditional expectation is compatible with zero actual aligned D6 for a fixed adversarial right map. It does NOT imply S=0 (S68 and S72 have all-seven S=68 and S=72, respectively) and it does not disprove an all-h S lower.

## 5. Next research gate AA4-U

Seek a deterministic joint positive lower surviving ALL adversarial f,g and misaligned A/A. Any candidate must combine actual Q-position-H joint geometry with non-AA positional overlap, JPKC source Hall and EICE internally-blocked anchors. It must be tested against true globally injected original W32 S68/S72 where D6=0. A conditional expectation over random global maps cannot be substituted for a deterministic minimum. If the proposed coupled inequality is falsified, record a genuine complete global f,g counterexample and keep the original obstruction OPEN.
