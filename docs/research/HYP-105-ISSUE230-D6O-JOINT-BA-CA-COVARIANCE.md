# HYP-105 issue #230 — D6-O: exact joint ORIGINAL B/A + C/A overlap and covariance

**2026-10-13. RESTRICTED_THEOREM_C / Branch A/B OPEN.** New Draft PR stacked strictly on D6-N #413 at pinned parent HEAD 427db12b40cd498efc9e21b2e5fa07c89da42c54. The `main` branch is not modified. D6-N passed all four GitHub-hosted CI on that exact HEAD. D6-M and D6-N are not merged. Independent mathematical peer review of D6-O remains required. This is a theorem about genuine original GQ right-line supports, not a generic Hall-flow rephrasing.

## 1. New two-class exact deterministic observable

Let s=2^h, h>=1, let the ORIGINAL W(3,s) have V=(s+1)(s^2+1) points and equally many lines, and let f,g be complete globally injective maps of ORIGINAL point and line factor vertices to unordered edges of physical K_a, where a is minimal with binom(a,2)>=V. Consider unordered sets of six DISTINCT ORIGINAL incidences satisfying left physical type B or type C and SIX distinct ORIGINAL right line factor identities. Every such sixset is counted once (not its signed GF5 events or physical-coordinate automorphism orbit).

For X in {B,C}, define w_X^f(L) as the number of those original sixsets with left physical X and with right ORIGINAL six-line identity set exactly L, |L|=6. The two sets of original sixsets are disjoint since their left physical types differ, even if they induce the same right ORIGINAL line set L. Let A_g(L) be 1 precisely when the six physical right pair labels g(L) form a simple 2-regular six-edge graph on six physical coordinates. For **every fixed possibly adversarial/correlated right g**, there are exact identities

    U_B(f,g)=sum_L w_B^f(L) A_g(L)
    U_C(f,g)=sum_L w_C^f(L) A_g(L)
    U_B+U_C=sum_L (w_B^f(L)+w_C^f(L)) A_g(L).

The two directional classes are disjoint subsets of the previously accepted *strictly GF5-positive* seven families: B-left/A-right and C-left/A-right (the latter belongs to the aggregate C/A tag). There is no double counting of ORIGINAL incidence sixsets, even when the same six right lines have both nonzero original left B and C multiplicities.

Crucial: both directional classes test **the SAME** right A-mask for a given g. Treating them as independent right events would therefore be false.

## 2. ALL-h exact mixed second-moment theorem

Fix f. For X,Y in {B,C}, define W_X=sum_L w_X(L) and the ordered **ORIGINAL** mixed overlap spectrum

    N_XY(k)=sum_{L,M: |L intersect M|=k} w_X(L)w_Y(M), k=0,...,6.

Write p_A for the exact D6-M right-uniform A probability, q_k(a) for the exact D6-N two-A joint kernel. These are rational values respecting globally injective WITHOUT-REPLACEMENT right g. Then for **uniform random complete right g**, conditioning on this fixed left f,

    E_g U_X=p_A W_X,
    E_g[U_X U_Y]=sum_{k=0}^6 N_XY(k) q_k(a),
    Cov_g(U_B,U_C)=sum_k N_BC(k) q_k(a) - p_A^2 W_B W_C,
    Var_g(U_B+U_C)=Var_g(U_B)+Var_g(U_C)+2 Cov_g(U_B,U_C).

Proof: expand each product of the finite sums over ORIGINAL right six-line supports and group ordered pairs by their true-original intersection cardinality. The exact conditional probability of two accepted physical right A events is q_k(a), regardless of the identities of their original lines, since g is globally uniformly sampled. No independence or mean-field assumption enters. Note that N_BC(6) can be positive because the **same right original support** may carry distinct left B and left C original sixsets. These are disjoint original sixsets but their right-mask indicators are perfectly aligned for such a common support.

For the selected nonnegative GF5 necessary R3 lower numerator, use the accepted repository weights a_B=45600, a_C=43320 (the existing C/A coefficient applies to its directional C/A subset). Let Y=a_B U_B+a_C U_C. The **exact selected-two-class** random-right moment satisfies

    E_g Y=a_B p_A W_B + a_C p_A W_C,
    Var_g Y=a_B² Var_g(U_B)+a_C² Var_g(U_C)
            +2a_Ba_C Cov_g(U_B,U_C).

Dividing E Y by 51^6 is a lower bound for the expected selected-positive necessary GF5 risk, not an upper bound for total R3 and not an assertion about every fixed g. Conditional Paley–Zygmund gives Pr_g(U_B+U_C>0)>= (E(U_B+U_C))²/E(U_B+U_C)² and similarly for Y; this is a probability guarantee only.

## 3. NEW exact sparse binomial-inverse algorithm

The original-line mixed spectrum can be computed *without* a quadratic pairwise comparison of all six-line supports. For any set T of original right lines, with r=|T|<=6, define the extension sum

    Z_X(T)=sum_{L ⊇ T} w_X(L).

The exact binomial moments for two classes are

    M_r(X,Y)=sum_{T:|T|=r} Z_X(T)Z_Y(T)
            =sum_{k=r}^6 binom(k,r) N_XY(k).

The reason is elementary but essential: a pair of six-line original supports with k shared lines contains exactly binom(k,r) common r-subsets T. By **integer binomial inversion**,

    N_XY(k)=sum_{r=k}^6 (-1)^(r-k) binom(r,k) M_r(X,Y).

This is valid for ALL finite h (any number V of original right factors) and for any nonnegative integer ORIGINAL six-line weights. The executable implementation accumulates all 2^6=64 subsets of every nonzero ORIGINAL right six-line support with Counter dictionaries. It never scans all support pairs; the direct O(|supp B|*|supp C|) oracle is reserved for **independent finite W32 falsification**. Complexity of building the sparse extension profiles is O(64(|supp B|+|supp C|)) integer updates, plus dictionary lookups; no V-dimensional dense 2^V table is needed.

The inversion also proves the exact checks

    sum_k N_XY(k)=W_X W_Y,
    N_XY(6)=sum_L w_X(L)w_Y(L),
    N_XY(k)>=0.

A failure of any of these hard-fails the model instead of silently projecting a negative count onto zero.

## 4. Actual original W(3,2) acceptance methodology

For frozen complete W(3,2) physical mappings lex/reverse/S68/S72:

- Main enumeration: existing exact left-candidate generator E1-A `selected_left_six`; keep left B/C, require six distinct **true ORIGINAL** right lines, aggregate into w_B(L) and w_C(L).
- **Fully independent** enumeration: build original GQ point→incident lines directly from incidences. For B enumerate one doubled left physical edge, an independently generated four-coordinate C4 on the remaining physical coordinates, choose two distinct original lines at the doubled original point and one at each of four original singleton points. For C enumerate triples of physical-disjoint original point pair labels and two true original incident lines at each point. Require six distinct ORIGINAL right line IDs in both.
- Independent overlap oracle: direct set intersections of ordered ORIGINAL line supports, compared to the sparse binomial-inverse formula including all 7 overlap ranks.
- Compare directional fixed-right B counts against the full accepted seven-GF5 `B-left/A-right` class; C counts against the aggregate C/A by independently counting its reverse A-left/C-right direction. Verify selected exact fixed-right weighted numerator does not exceed the previously certified full-seven GF5 necessary floor.
- The separate old D6-N C-only O(n^2) variance oracle must agree **exactly** with the new joint model's C mean/variance. Independently recompute cross covariance from direct spectrum and the D6-N physical right-A overlap kernel.
- Check numerical moments using exact Fraction arithmetic only. A positive conditional mean or Paley–Zygmund probability MUST NOT be interpreted as universal fixed-g positivity. The complete original seven-positive S for W(3,4)/W(3,8) remains unknown and is NEVER fabricated.

The logical advance is that a single exact mixed spectrum now handles simultaneous left B/C support and their globally coupled right A mask. This is strictly more informative than either D6-M's marginal first moments or D6-N's one-class second moment.

## 5. Fundamental unresolved all-g gate and what D6-P must attack

Root #230 Branch A requires inf over BOTH globally correlated complete maps f and g of the sum S_seven of **seven** distinct accepted positive original sixset classes to be Omega(s^6), not merely E_g S_seven. Neither the new exact covariance theorem nor any second-moment or finite-W32 frequency establishes this.

A possible next genuine geometric gate is an exact joint physical-mask/cylinder formulation incorporating B-left/A-right, C-left/A-right, the opposite directions A-left/B-right and A-left/C-right, and the remaining accepted C/B and B/B overlap/disjoint classes plus D6. This must track both ORIGINAL point and ORIGINAL line support, and physical left/right patterns under the **same** f and g. Then prove a deterministic nonconcentration/anti-avoidance bound for all g, or build an explicit coherent infinite correlated family with S=o(s^6). Optimizing conditional random-right moments alone is not Branch A. Do not start another transport/Hall surrogate as substitute.

## 6. Scope and acceptance

- Theorem: exact mixed covariance for any fixed left f and uniform right g, ALL finite s=2^h, plus exact deterministic support-mask decomposition for any fixed f,g.
- Code: `research/hyp105_issue230_d6o_joint_ba_ca_covariance.py`.
- Independent falsifiers: `research/test_hyp105_issue230_d6o_joint_ba_ca_covariance.py`.
- GitHub-hosted dedicated contract: `.github/workflows/hyp105-issue230-d6o-joint-ba-ca-covariance.yml`.
- Require final identical PR HEAD with dedicated Contract, INDEX, Proof Audit, full Research all SUCCESS; independent mathematics review remains OPEN. PR Draft, no merge or main mutation.
- No PROVED_A, no infinite COUNTEREXAMPLE_B, no ASET exponent; status RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.
