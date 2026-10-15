# HYP-105 / issue #230 — EICE-003-L: probabilistic NO-GO for the proposed four-END-CLEAN GQ anchor capacity bound

**Research status:** \`THEOREM_L_CLEAN_CAPACITY_NO_GO\`, branch A/B and ASET still OPEN. Strict research-only Draft child of [EICE-003-K PR #469](https://github.com/definitely-stable/Mathlab/pull/469) at exact parent HEAD \`73cfebed8042f0f9b6592bd318295fb0bdf69a5b\`. Do not merge or edit main. This result **REFUTES** the proposed sufficient auxiliary estimates \`max_e C_e=o(s⁴)\` and \`sum_e C_e=o(s⁸)\` uniformly over all globally injective original f,g. It does **NOT** refute the root HYP-105 Branch A lower bound, nor the analogous \`H_e\` estimate for four INTERNALLY BLOCKED anchors.

## L1 — exact all-h random-injection lower expectation

Fix any s=2^h>=64 and genuine ORIGINAL symplectic GQ W(3,s), with

    V=(s+1)(s²+1), d=s+1, N=Vd,
    a=min{b: binom(b,2)>=V}, T=binom(a,2), U=T-V.

The ORIGINAL source contains N distinct point–line incidence IDs. Independently choose f: original V points -> T distinct K_a coordinate pairs and g: original V lines -> T distinct K_a coordinate pairs as UNIFORMLY RANDOM INJECTIONS. These are actual legally globally injected original source labels, NOT independently sampled pair labels per physical edge.

Fix ONE arbitrarily chosen TRUE ORIGINAL middle incidence e=(p2,ell2). Condition on its genuine point pair f(p2)={x0,x1} and line pair g(ell2)={y0,y1}, ordering both pairs canonically.

Select ORDERED four other ORIGINAL source incidences e1=(p1,l1), e2=(p2',l2'), e3=(p3,l3), e4=(p4,l4) such that all FIVE original source point IDs and all FIVE original source line IDs, including those in e, are pairwise distinct. (The aliases p2' and l2' are unrelated to the middle p2,ell2.) At the jth choice, j=1,2,3,4, exclude all incidences through the already chosen j original points and all j original lines. This excludes at most 2jd original incidences. Thus the number of genuine ordered original four-arm source matchings is at least

    M_s = product_{j=1..4}(N-2jd)
        = d^4 product_{j=1..4}(V-2j).                         (L1-M)

Force sources e1,e2 into the ORIGINAL physical middle corner Q00 and e3,e4 into opposite Q11, and require all four external point coordinates ξ_i pairwise distinct and all four external line coordinates υ_i pairwise distinct. For fixed f(p2), the probability of this POINT assignment (without replacement among the remaining T-1 point labels) is exactly

    R_s = (a-2)_4 / (T-1)_4,                                  (L1-R)

where (n)_4=n(n-1)(n-2)(n-3). The LINE assignment independently has the SAME probability R_s. Hence the exact physical 2×2 opposite-corner assignment probability is R_s², with no Bernoulli independence substituted for sampling without replacement. Every qualifying physical source assignment yields the real I1 five-source paired-diagonal coordinate-proper K_{2,2} template. It is counted 2!2!=4 times by ordering the two Q00 and two Q11 true source incidences.

The four induced ORIGINAL endpoint point labels f(q_ij) are pairs {ξ_i,ξ_{j+2}} (i=1,2;j=1,2) and the original line labels g(r_ij) are corresponding {υ_i,υ_{j+2}}. Because all external ξ_i and υ_i are distinct, these are FOUR pairwise DISTINCT desired original point-pair labels and FOUR distinct desired original line-pair labels. None equals any of the already exposed FIVE original point or line source labels, because each source label contains a CENTRAL x or y coordinate while all desired endpoint pairs are external-external.

### L2 — all eight true original endpoint labels + four NONINCIDENT END-CLEAN anchor paths

Condition on the physical quadrant assignment. The remaining true original f and g images are independently uniformly chosen injective subsets of the remaining T-5 pair labels. By conditional-uniform-exposure, at most U=T-V of those T-5 labels are unassigned on each side. A union bound across the eight distinct original q/r endpoint labels gives

    P(any of 8 desired ORIGINAL endpoint labels missing)
         <= 8U/(T-5).                                        (L2-A)

Whenever present, the four ORIGINAL q_ij are distinct genuine source points, uniformly allocated among V-5 unexposed point IDs; the four ORIGINAL r_ij are distinct genuine source lines, uniformly allocated among V-5 unexposed line IDs. The two assignments are independent (f/g originally independent), but the four corners within each side are sampled WITHOUT replacement. No independence of the resulting q/r anchors is claimed.

Exclude any of the following exceptional original incidence events:

- any of the 16 cross incidences \`q_ij incident r_kl\` (this includes the four required endpoint nonincidences and prevents an intermediate original anchor point from being another exposed q, or an intermediate anchor line from being another exposed r);
- any of 4 decoded original r labels incident with any of the FIVE originally exposed arm/middle source points p (at most 20 incidences);
- any of 4 decoded original q labels incident with any of the FIVE originally exposed arm/middle source lines ell (at most 20 incidences).

For a fixed point, an independently uniformly sampled available ORIGINAL line is incident with it with probability at most d/(V-5), and dually for a fixed line and uniformly available point. Thus, using a union bound (including dependent events),

    P(any true original source geometry exception)
        <= (16+20+20)d/(V-5) = 56d/(V-5).                    (L2-B)

If none happens, each of the four pairs (q_ij,r_ij) is nonincident, hence has a UNIQUE TRUE ORIGINAL GQ anchor q_ij--ell_ij--p_ij--r_ij. Moreover its intermediate TRUE original point p_ij is neither one of the initially exposed FIVE original source points nor any of the FOUR decoded q labels, and its intermediate TRUE original line ell_ij is neither one of the FIVE original source lines nor any of the FOUR decoded r labels. This precisely justifies deferred exposure of the ANCHOR intermediates.

Conditional on those ORIGINAL source incidences/identities, each still-unexposed f(p_ij) is a uniformly random physical pair among the T-9 unused point labels, and each unexposed g(ell_ij) is similarly uniform among the unused line labels. For each exposed f(q_ij) or g(r_ij), at most 2(a-2) other K_a physical pairs intersect it. The union bound over four left and four right ORIGINAL anchor end-dirty collisions gives

    P(any of 8 true anchor-end label overlaps)
        <= 8 * 2(a-2)/(T-9) = 16(a-2)/(T-9).                 (L2-C)

Different anchor intermediates may coincide with one another; this bound does NOT assume they are independent. Sequentially revealing their random labels only DECREASES or preserves the per-source available-unseen denominator at earlier stages. More carefully, for a later intermediate that was previously revealed as another anchor, the event of its potential overlap with the newly exposed endpoint is controlled by the original uniform permutation conditional on the set of all nine initially exposed source/endpoint labels: its marginal remains uniform among T-9. Thus ordinary union bounding on eight one-factor marginal events is valid.

Combining L2-A/B/C yields the fully explicit conditional success lower bound

    beta_s = 8U/(T-5) + 56d/(V-5) + 16(a-2)/(T-9);
    P(all FOUR ORIGINAL q/r pairs present, nonincident,
      and their four ORIGINAL unique GQ anchors end-clean
      | prescribed true source physical quadrant assignment)
        >= max(0,1-beta_s).                                 (L2)

Hence for EVERY fixed genuine ORIGINAL middle incidence e,

    E_{random genuine global f,g}[ C_e ]
      >= B_s := [d^4 product_{j=1..4}(V-2j)/4]
                * ((a-2)_4/(T-1)_4)^2
                * max(0,1-beta_s).                          (L-EXACT)

Here C_e is EXACTLY EICE-003-J's true original five-incidence physical template count with all FOUR decoded, NONINCIDENT, end-clean unique ORIGINAL GQ anchors, not the internally allblocked H_e. This proof counts only ONE of the two physical middle diagonals (Q00/Q11), so it is a valid lower bound regardless of the other.

## L3 — explicit uniform c*s⁴ NO-GO and global sum

For all s>=64, the minimal K_a physical coordinate pair universe obeys:

    V>=s³, a<=3*s^(3/2), a>=10, T>=V, U<a;
    beta_s <= 72*s^(3/2)/(s³-9)
             + 56*(s+1)/(s³-5) < 1/4;
    M_s >= s⁴*(V/2)^4;
    (a-2)_4/(T-1)_4 >= ((a-5)/T)^4 >= a^(-4).

The latter follows from a>=10, (a-5)>=a/2 and T<=a²/2. Therefore, by L-EXACT,

    E C_e >= (3/4) * [s⁴*(V/2)^4/4] * a^(-8)
          >= (3/4) * s⁴/(64*3^8)
           = s⁴/559872 > s⁴/1,000,000.                    (L-NOGO)

All inequalities are elementary symbolic inequalities valid for every s=2^h>=64, not numerical fits. The executable Fraction checker separately verifies exact B_s and the coarse inequalities for s=64,...,65536 and fails closed if they disagree. The all-h theorem is the symbolic proof above.

**Existence and decisive falsification:** Since C_e≥0, by ordinary averaging there exists at least one GLOBALLY INJECTIVE genuine original f,g for which \`C_e >= s⁴/1,000,000\` for any prescribed true middle source e. This falsifies the proposed UNIFORM statement

    max_e C_e=o(s⁴) over all globally injected original f,g. [FALSE]

Moreover the lower expectation applies to EVERY e under the SAME distribution of globally injected f,g. By LINEARITY OF EXPECTATION (no independence among different central sources required),

    E[sum_e C_e] = sum_e E[C_e] >= N*s⁴/1,000,000,

so one single genuine globally injected f,g simultaneously has

    sum_e C_e >= N*s⁴/1,000,000 = Ω(s⁸).           (L-TOTAL)

This refutes the other sufficient proposal \`sum_e C_e=o(s⁸)\` UNIFORMLY across all global injections.

**CRITICAL SCOPE:** This probabilistic construction says that FOUR original GQ anchor END-CLEAN events can be simultaneously abundant in source-coherent physical five-incidence templates. It says NOTHING about the completely different requirement that all four anchors be **INTERNALLY BLOCKED by the same original middle source**. It does not produce any positive original GF(5) six-incidence motif, refute original Branch A, prove H_e large, or settle the ASET exponent. The root Branch A may still hold through sparse internal blocking or an independently certified accepted-seven GF5 compensation. The K-stage clean-anchor scarcity strategy must be ABANDONED as a universal proof, and effort should go to true H_e or the positive original sixset mapping.

## L4 — independent executable proof falsifiers

- \`research/hyp105_issue230_random_clean_capacity_nogo.py\`: exact integer/Fraction source GQ ordered-four-edge matching lower M_s, without-replacement quadrant probability R_s², each three-part explicit exception term beta_s, rational B_s, simultaneous aggregate existence; no simulated Bernoulli replacement.
- \`research/test_hyp105_issue230_random_clean_capacity_nogo.py\`: explicitly exhaust all four-edge physical pair injections after one central K6 pair and verify the exact \`(a-2)_4/(T-1)_4\` probability, symbolic input inequalities, all-h rational s=64..65536 (and s=2^20 for large integer input), actual original W32 GQ incidence matching combinatorial count at multiple specified true middle sources, actual W34 J stage C totals as finite supporting controls, malformed-input and false-GF5 negative controls.
- \`docs/research/HYP-105-ISSUE230-EICE003L-RANDOM-CLEAN-NOGO.md\`: this formal proof, source scope and research NO-GO.
- \`.github/workflows/hyp105-issue230-eice003l.yml\`: GitHub-hosted exact rational proofs and inherited K regressions; no self-hosted runner.

**Next EICE-003-M:** return to the INTERNAL-blocked true original four-anchor capacity H_e, not to a now-disproved clean-anchor C_e upper. Analyze the additional label intersections f(anchor point)∩f(middle source point), g(anchor line)∩g(middle source line) and their original source geometry, or construct an all-h accepted-seven GF5 positive sixset transfer with rigorously bounded real original preimages. In random globally injective source families, the end-clean four-anchor templates are abundant but simultaneous internal blockers may be rare; test this distinction with independent true original source oracles rather than inferring it. Draft only; main and root issue untouched.
