# HYP-105 E2-B3.1-B1-A — independent GF(5) Fourier verification of accepted 5×6 matching flows

Date: 2026-10-10. Parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162).

**IMPORTANT PRE-EXISTING RESULT / NO DUPLICATION CLAIM.** [HYP-105 E2-B3.1-B1, merged PR #214](HYP-105-G5-E2-B3-B-FULL-MATCHING-FLOWS.md) **ALREADY COMPLETED** the exhaustive GF(5) classification of **all simple six-factor-matching 4–6 coordinate physical profiles** on both sides: 610 projected profiles, 5,486 signed color-preserving orbits, 3,721,000 named signed cases, 100 zero cases confined to 6×6, and the exact matching weighted coefficient \(C_{5,6}=4,578,391,800\). The present slice is **NOT** the first complete 5×6 classification. It supplies an algorithmically independent **782-state integer Fourier exact-flow oracle**, reproduces the accepted **5×6 coefficient and event mass**, and isolates a sharper fixed-label 5×6/6×5 necessary-risk constant.

**ACCEPTANCE SCOPE:** INDEPENDENT_CROSS_CERTIFICATE_OF_PR214 / EXACT_2100_5×6_SIGNED_REPRESENTATIVES / ALL_POSITIVE / MIN_GF5_WEIGHT=10950 / NEW_RESTRICTED_FIXED_LABEL_R3_COROLLARY / NONMATCHING_FACTOR_FORESTS_OPEN / NO_FIXED_LABEL_R3_UPPER / NO_NEW_ASET_EXPONENT / NO_CLAIM_OF_GENERAL_CHARACTER_SUM_NOVELTY.

## 1. Precisely bounded mathematical model

Let \(s=2^h\), \(h\ge1\), and \(G_s=W(3,s)\) be the classical point-line symplectic GQ incidence graph with \(V=(s+1)(s^2+1)\) vertices **per factor side**, \(N=(s+1)V\) incidences and degree \(\Delta=s+1\). Fix injective maps of point vertices and line vertices into distinct unordered physical pairs of \(K_a\), where \(a\) is minimal with \(K=\binom a2\ge V\). The coordinate halves are physically disjoint.

Take an unordered set of **six factor incidences forming a matching**: six different point endpoints and six different line endpoints. Their physical coordinate-pair labels are then **six distinct simple edges per half**. Restrict to templates where the left physical pair graph has exactly **five touched coordinates** with minimum degree two, and the right has exactly **six touched coordinates** with minimum degree two. Let \(U_{5,6}(f,g)\) count these actual original factor six-matchings. Define \(U_{6,5}\) symmetrically and \(U_{56}=U_{5,6}+U_{6,5}\). The two cases are disjoint **as six-column set types**.

For each of the ten unordered balanced sign partitions (3 versus 3), count the exact number of assignments of all 24 weights \(w_{ic}\in\mathbb F_5^*\) satisfying:

\[
  \sum_{c\in S_i}w_{ic}=4\pmod5,\qquad
  \sum_{i:c\in S_i}\varepsilon_i w_{ic}=0\pmod5,
  \quad\varepsilon_i\in\{+1,-1\},\quad\sum_i\varepsilon_i=0.
\]

Each column has 51 admissible nonzero checksum-4 weight tuples. The risk \(R_3\) is the **sum of probabilities of distinct unsigned 3v3 signed events**. It is **not** their union probability; different sign events may share actual weight assignments.

## 2. Independent 782-state integer GF(5) formula

The accepted PR #214 calculates half-block GF(5) sum histograms and convolves the two halves, so a verification based on that same routine would not be independent. This slice instead uses the **classical orthogonality of additive characters** on all 24 coefficient incidences and six checksum constraints.

For each column dual variable \(\lambda_i\in\mathbb F_5\), coordinate dual \(\mu_c\in\mathbb F_5\), and primitive fifth root of unity \(\zeta\), the nonzero-incidence character factor is \(\psi(z)=4\) when \(z=0\), and \(-1\) otherwise. Thus

\[
 F=5^{-(6+C)}
  \sum_{\lambda\in\mathbb F_5^6}
  \sum_{\mu\in\mathbb F_5^C}
   \zeta^{-4\sum_i\lambda_i}
   \prod_{(i,c)}\psi(\lambda_i+\varepsilon_i\mu_c).
\]

For each physical coordinate \(c\) let \(d_c=\#\{i:c\in S_i\}\), and \(n_t(c)=\#\{i:c\in S_i,\ -\varepsilon_i\lambda_i=t\}\). Eliminating \(\mu_c\) analytically yields the exact integer

\[
 \Phi_c(\lambda)=\sum_{t=0}^4 4^{n_t(c)}(-1)^{d_c-n_t(c)}.
\]

Because signs balance, the gauge change \(\lambda_i\mapsto\lambda_i+\varepsilon_i u\), \(\mu_c\mapsto\mu_c-u\) fixes the integrand and leaves \(\sum_i\lambda_i\) unchanged; choose the unique representative with \(\lambda_0=0\). Under nonzero common multiplication \(\lambda\mapsto\alpha\lambda\), all \(\Phi_c\) are unchanged and the four fifth roots sum to \(4\) if \(\sum_i\lambda_i=0\), otherwise \(-1\). The zero vector contributes \(1\). Therefore the complex character sums cancel **exactly**, yielding the **integer-only** identity

\[
 \boxed{\displaystyle
 F=\frac{1}{5^{5+C}}\!
   \sum_{\substack{\lambda_0=0\\
                    \lambda\ /\ \mathbb F_5^*}}
   \omega(\lambda)\prod_c\Phi_c(\lambda),\quad
 \omega(0)=1,\quad
 \omega(\lambda\ne0)=
 \begin{cases}
  4,&\sum_i\lambda_i=0,\\
  -1,&\sum_i\lambda_i\ne0.
 \end{cases}}
\]

Exactly \(1+(5^5-1)/4=\mathbf{782}\) representatives are evaluated per full six-column GF5 event. The program uses no floating point and fails unless the numerator is divisible by \(5^{5+C}\) and \(0\le F\le51^6\). This is an exact specialized finite-field identity, not a new universal theorem or an all-h \(R_3\) bound.

Independent oracles: the **previously accepted 51³-side meet-in-middle GF5 histogram** checks real 5×6 witnesses; **B3.1-A 2¹²-edge flow inclusion/exclusion** checks C6/C6; physical coordinate permutation, column permutation and sign reversal preserve counts; a new singleton coordinate forces exactly zero.

## 3. Complete 5×6 re-enumeration and equality to the accepted coefficient

Enumerating six simple \(K_5\) edges touching all five physical coordinates with minimum degree two gives **85** labeled physical graph sets. Quotienting by \(S_5\) yields **three** unlabeled graph types, with respective labeled physical-graph multiplicities \(g=(15,60,10)\). The other six-coordinate projection is a 2-factor on the six named columns (60 C6 types and 10 disjoint \(C_3\sqcup C_3\) types). There are ten unordered balanced sign masks. Fix each representative left graph and take its six lex-ordered edges as column IDs. Exactly **3 × 70 × 10 = 2,100 covering representative** templates are evaluated. These 2,100 are **not claimed to be 2,100 distinct signed graph-isomorphism orbits**.

All 2,100 exact GF5 events are positive, with the following values:

| Five-coordinate graph class | \(S_5\) edge-set multiplicity | Cases | Minimum \(F\) | Maximum \(F\) |
| --- | ---: | ---: | ---: | ---: |
| Degree profile (4,2,2,2,2) | 15 | 700 | **14,400** | **17,955** |
| First (3,3,2,2,2) type | 60 | 700 | **10,950** | **12,357** |
| Second (3,3,2,2,2) type | 10 | 700 | **11,685** | **12,405** |

The accepted PR #214 already established every 5×6 matching flow is positive. The **independent reproduction** here is independently tested against its *complete weighted signed coefficient*. Let \(S_j\) be the sum of the 700 full-GF5 weights for fixed left type \(j\). Each \(K_5\) graph shape contributes \(g_j 6!/5!=6g_j\) distinct column-named canonical five-coordinate profiles. Summing over the full right-factor/sign space is invariant under a simultaneous column relabeling. Consequently, the completely independent Fourier calculation must satisfy

\[
 \boxed{C_{5,6}=6\sum_{j=1}^{3}g_j S_j
         =4,578,391,800},
 \qquad
 \boxed{\#\text{ labeled signed 5×6 templates}
       =6\sum_{j=1}^{3}g_j(70)(10)=357,000}.
\]

Both equalities are **hard runtime assertions** against PR #214, which obtained the same results using a different algorithm and 5,486 color/sign orbit classification. This is the principal new validation value of PR #216.

## 4. Restricted all-h quantitative corollary, not a new full matching classification

Because every tested 5×6 signed representative has **at least \(10,950\)** GF5 weight solutions, every real six-factor-matching in \(U_{56}(f,g)\), for **every h** and **every fixed injective labeling**, contributes at least ten distinct balanced signed-event probabilities of \(10,950/51^6\) each. Therefore:

\[
  \boxed{\displaystyle
     R_3(B_s(f,g))\ge
      \frac{109,500}{51^6}U_{56}(f,g)
     \qquad(s=2^h,\ h\ge1).}
\]

This corollary is **restricted**: no nonzero universal per-label lower bound on \(U_{56}\) is known. It is an explicit improvement over the broad 4,806 coefficient lower **only for this subfamily**; the accepted complete matching result remains authoritative.

Under independent uniform pair injections, for one original six-factor matching the exact projection probabilities are

\[
   p_5=\frac{510(a)_5}{(K)_6},\qquad
   p_6=\frac{70(a)_6}{(K)_6}.
\]

The 510 and 70 independently equal coefficients of the previously accepted [B3.0 projection polynomial](HYP-105-G5-E2-B3-FOREST-PROJECTION.md) for profile \((1,1,1,1,1,1)\). Let \(M_6(G_s)\) be the **actual number** of original six-edge factor matchings. Then \(\mathbb E[U_{56}]=2M_6(G_s)p_5p_6\), and the greedy bound \(M_6\ge\prod_{j=0}^5(N-2j\Delta)/6!\) yields a matching-class lower contribution \(\mathbb E[R_3]=\Omega(s^{9/2})\) **under independent random labels only**. This is **subleading** to the already known \(\Theta(s^6)\) complete matching-class random expectation of PR #214, not a competing or improved exponent.

## 5. Remaining problems and strict novelty boundary

**Already closed by accepted PR #214:** all factor-disjoint original six-edge *matching* cases, including physical 4×4, 4×5, 4×6, 5×5, 5×6 and 6×6. They must NOT be reopened or presented as a new discovery.

**OPEN B3.1-B2:** six-edge **original factor forests with repeated point or line endpoints**, which lead to repeated physical pair labels even under injective endpoint maps. Those are outside simple six-edge matching projections. The 11,663 abstract B3.0 factor-forest shape cases are not fully classified by exact GF5 flow.

**OPEN B3.2-E:** joint all-h *upper* bounds on \(R_2\) and \(R_3\) on the SAME fixed geometry-aware injection, including positive motifs with repeated factor endpoints. The new Fourier certificate supplies a lower-bound diagnostic and independent finite verification, **not** an upper bound, new ASET exponent, or novel general additive character identity. Keep #176/#169/#162 roots OPEN. No Rust or unrelated repository changes.

[Implementation](../../research/hyp105_g5e2b3b1b_five_six_flows.py) · [independent tests](../../research/test_hyp105_g5e2b3b1b_five_six_flows.py) · [accepted full-matching classification](HYP-105-G5-E2-B3-B-FULL-MATCHING-FLOWS.md).
