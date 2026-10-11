# HYP-105 C24-B8-B — signed physical-change balance and exact annealed baseline

Root [HYP-105 #230](https://github.com/definitely-stable/Mathlab/issues/230), stacked on [C24-B8-A PR #357](https://github.com/definitely-stable/Mathlab/pull/357). B8-A contains the exact six ordinary Boolean plus connected-D6 60-cycle tensor. Scientific B8-B does NOT change the ORIGINAL GQ source semantics, the complete globally injective point/line maps, or the seven GF(5)-necessary family weights.

## 0. Crucial negative gate

No uniformly NEGATIVE mixed curvature bound can hold for EVERY complete right labeling g for one FIXED original right transposition B unless the mixed curvature vanishes identically: the map g -> g^B is a fixed-point-free involution and reverses its sign. Negativity found in 8,286 of 11,025 W32 B7 cells was never an all-h signed descent theorem. The B8-A physical upper cap (737/724 on two particular W32 rectangles) is far smaller than the unrestricted B7 source-touch cap, but an *absolute* cap still cannot prove a positive lower bound on the SCORE S.

## 1. Theorem B8-B1 — ALL-h exact reinforcing/opposing physical transition law

Fix ANY s=2^h>=2, ORIGINAL GQ W(3,s), two complete original global physical point-pair injections f,f^A related by one point transposition A and two complete original global line-pair injections g,g^B related by one line transposition B. For each ORIGINAL **distinct six-incidence** source J and each ordinary original tag t (six of the seven tags), write signed eligibility transitions:

    ell_J = L_J(f^A)-L_J(f) in {-1,0,1},
    r_J   = R_J(g^B)-R_J(g) in {-1,0,1}.

The exact mixed contribution is ell_J*r_J. A contributing ordinary J belongs to exactly one of four categories:

- gain/gain: +1
- loss/loss: +1
- gain/loss: -1
- loss/gain: -1

For D6 let ell_{J,sigma} and r_{J,sigma} be transitions of the **matched connected dual cycle** one-hot indicator, sigma in the exact 60 undirected Hamiltonian C6 signatures on SIX FIXED ORIGINAL incidence positions. Distinct signatures are never merged or optimized independently; their dot product gives the exact mixed D6 contribution. Each nonzero signature product is +1 (same-sign transitions) or -1 (opposite-sign transitions). The net per-source D6 contribution has absolute value <=2; *not* <=1. When both physical side states change but no nonzero cycle signature transition coincides, mixed contribution is zero.

Let P_t count matched same-sign transition products, and N_t count matched opposite-sign transition products, **with each distinct original source and its signature contributions counted exactly once**. Then

    kappa_LR = sum_t (P_t - N_t).

This holds deterministically for EVERY h,f,g. It implies the exact physical-bound hierarchy

    |kappa_LR| <= sum_t(P_t+N_t)
                <= sum_(six ordinary J) 1[ell_J !=0 and r_J !=0]
                    +2 sum_(D6 J) 1[ell_D6 vector !=0 and r_D6 vector !=0]
                <= 2 * M_original_joint_touch(B7).

The first bound is a *matched* absolute count, which may be strictly sharper than the B8-A joint change bound. The gap (P+N)-|kappa| = 2 min(P,N) is EXACT signed cancellation across the original sources/signatures. It proves no power of s and is NOT a lower bound on S.

**Proof:** The B8-A tensor factorization gives each ordinary product and each matched D6 signature product exactly. Split each product by its signs. Finite summation yields P-N. Apply the triangle inequality first to matched products, then bound each ordinary J by 1 and each D6 J by 2; finally use B7's original all-sixsets jointly touched support. No independence or per-source relabeling is assumed.

## 2. Theorem B8-B2 — signed orbit involution (exact zero-mean, not a descent theorem)

For the same FIXED original f, A and B, define kappa(f,g)=S(f^A,g^B)-S(f^A,g)-S(f,g^B)+S(f,g).

    kappa(f^A,g) = -kappa(f,g)
    kappa(f,g^B) = -kappa(f,g)
    kappa(f^A,g^B) = +kappa(f,g).

The first and second equations reverse the orientation of one of the two rectangle axes; reversing both retains its sign. Since g -> g^B permutes the set of ALL legal globally injective right maps,

    sum_(all complete global right injections g) kappa(f,g) = 0.

Furthermore, the nonzero signed curvature multiset has symmetric positive and negative multiplicities on the full right orbit. This is a strict mathematical barrier to trying to deduce an all-g strictly negative mixed curvature from unrestricted transpositions. It says NOTHING about curvature conditional on low S or one-swap stationarity. Fixed orientation sign-invariance only.

For any particular global rectangle let dL=S(f^A,g)-S(f,g), dR=S(f,g^B)-S(f,g). An exact joint typed improvement occurs **iff**

    N-P > dL + dR,

because S(f^A,g^B)-S(f,g) = dL+dR+(P-N). Negative kappa alone is INSUFFICIENT.

## 3. Theorem B8-B3 — exact expectation over two independent complete injections

Let V=(s+1)(s^2+1) be the original point and line count, a=min{a:C(a,2)>=V}, M=C(a,2). Choose f,g uniformly and INDEPENDENTLY from complete injective maps of all original points and lines to distinct physical edges of K_a. Distinct original sixsets are **not independently labeled**; only f and g are independently sampled *whole maps*.

For a fixed original 6-incidence source J, let p_A(a), p_B(a), p_C(a) be the marginal probability that a PHYSICAL side with original multiplicity pattern A/B/C forms a six-coordinate 2-regular multigraph:

    p_A = 70*C(a,6)*6!/(M)_6
    p_B = 45*C(a,6)*4!/(M)_5
    p_C = 15*C(a,6)*3!/(M)_3.

The host-coordinate set is selected with C(a,6), 70/45/15 enumerate the respective physical 2-factor multiset templates on SIX fixed vertices. The factorial counts assign each DISTINCT original factor to one physical edge of its specified multiplicity; critically B has 4!, not 5!, because its repeated original factor MUST occupy the doubled edge. These are exact rational probabilities.

For one FIXED connected D6 dual six-position cycle sigma, the probability on one side is

    p_sigma = C(a,6)*6!/(M)_6,

and there are exactly 60 labeled six-position Hamiltonian cycles. Thus D6 acceptance for one ORIGINAL A/A source has expectation

    E[X_J^D6] = 60 * p_sigma^2,

NOT p_A^2, because both physical sides must have the SAME connected six-cycle signature.

For an ordinary source with original left/right profiles u,v, independence of the TWO global whole injections gives

    E[X_J] = p_u * p_v.

Let N_(t,u,v)(s) count ALL ORIGINAL DISTINCT GQ six-incidence sources with static tag t, and endpoint profiles u/v. Then the EXACT (uncomputed closed source census) complete expected score is

    E[S_s(f,g)] =
        N_D6(s)*60*p_sigma^2
        + sum_(ordinary t,u,v) N_(t,u,v)(s)*p_u*p_v.

This is an all-h algebraic identity **conditional only on a correct original GQ typed source census**, not a concentration bound, not an infimum lower, and not a new ASET exponent. In fact inf_(f,g) S <= E[S]; do not reverse the inequality. Future work must control worst-case signed discrepancy, not only calculate average density.

## 4. Independent oracles and observed finite case

- Implementation `research/hyp105_g5e2b3e1c24b8b_signed_physical_balance.py`: a signed matched-signature source oracle, exact four-map census, rigorous sign-orientation identity, and rational complete-injection mean.
- Fast tests `research/test_hyp105_g5e2b3e1c24b8b_signed_physical_balance.py`: enumerate all 130 physical K6 multiset 2-factors independently (A=70, B=45, C=15); independently check 60 D6 signatures *each* have 720 ordered maps for a=6; exact 3003 ORIGINAL small-W32 source subuniverse against the independent B2 reference classifier; D6 mixed kappa=+2 and reversed -2; exact rational mean and input failures.
- Dedicated Contract `research/hyp105_g5e2b3e1c24b8b_w32_signed_witness.py`: for the two frozen B7 typed rectangles (L3,8/R0,14) and (L4,14/R4,11), independently enumerate f0 and swapped f left sources and their 98,982 distinct original-sixset UNION. Count positive/negative matched signed products separately for all seven original tags. Reconcile all four original score corners with B2 compressed left-first and independent original RIGHT-FIRST census. Record exact escape deficit vs single-side costs. **No full 11,236-state B7 rerun**.

Numerical matched positive/negative counts must be read from the actual latest GitHub-hosted Contract logs and MUST NOT be guessed or asserted before the run.

## 5. Decision / next permitted math

B8-B proves rigorous sign bookkeeping and an exact random-map first moment. It also proves the unrestricted signed transposition mean is ZERO and therefore cannot by itself imply all-f,g positive seven-score obstruction. Status after exact-head green: **RESTRICTED_THEOREM_C_SIGN_BALANCE_AND_ANNEALED_BASELINE**, not PROVED_A or infinite COUNTEREXAMPLE_B.

For B8-C, use the fixed GQ original six-incidence profile-census as the static input to an explicit worst-case **signed discrepancy** problem. A candidate sufficient Branch-A condition would require both a uniform-in-f conditional mean floor E_g S(f,g)>=c0*s^6 and a bound sup_(f,g)(E_g S(f,g)-S(f,g))<=c1*s^6 with c1<c0. Neither bound follows from the first-moment identity, zero-average kappa, ordinary GQ pair spectra, or any two W32 finite witnesses. Test a less-than-target-scale signed correlation certificate on exact original tiny instances before declaring a theorem.

Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains **OPEN_WITH_FORMAL_BLOCKER**; no full GF5 R3 bound, no ASET exponent, no Rust or production artifacts, no main merge. Acceptance demands exact latest-head dedicated B8-B Contract, unchanged full six-shard Research+aggregate, and INDEX SUCCESS on GitHub-hosted runners only.
