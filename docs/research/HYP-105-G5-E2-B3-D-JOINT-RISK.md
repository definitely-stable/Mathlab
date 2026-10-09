# HYP-105 G5-E2-B3.2-D — Four-cycle Q4 obstruction, complete unit T4, paired finite GF(5) R2/R3

Date: 2026-10-09. Parents [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162). Follows [Plücker nonalignment](HYP-105-G5-E2-B3-C-PLUCKER-NONALIGNED.md), [coincident C6 obstruction](HYP-105-G5-E2-B3-B2-COINCIDENT-CYCLES.md), [full weighted GF5 disjoint pair energy](HYP-105-G5-E2-B1-EXACT-DISJOINT-ENERGY.md), [independent-label R2 upper](HYP-105-G5-E2-B2-RANDOM-R2-BOUND.md).

**ALL-h FIXED LABEL LOWER R2/ALL-h EXACT RANDOM Q4 EXPECTATION AND MATCHING LOWER / FULL FINITE UNIT-COEFFICIENT T4 / EXACT GF5 R2/R3 ON ONE 7-COLUMN WITNESS-ENRICHED SUBFAMILY / NO FULL GF4 WEIGHTED R2/R3 / NO UNIFORM STRICT R2/R3 UPPER / NO NEW ASET EXPONENT / SCIENTIFIC PRIORITY UNVERIFIED.**

## 1. New necessary R2 motif: matched C4/C4

For s=2^h let G_s=W(3,s) be the known bipartite point-line incidence graph with V=(s+1)(s²+1) vertices on each side, N=(s+1)V factor incidences and regular degree Δ=s+1, and fix ANY injections f:P→binom([a],2), g:L→binom([a],2), where a is minimal such that binom(a,2)≥V. All columns are physically distinct support-four split 2+2 vectors.

Define `Q4(f,g)` to be the number of unordered sets S of **four** factor incidence edges with eight distinct factor endpoints (a size-four factor matching), such that the four physical left pair-label edges and four right pair-label edges each form a simple 4-cycle C4 on four physical coordinates, and their **dual column-adjacency graphs** on the four named column IDs are the SAME C4. There is precisely one unordered alternating balanced 2+2 sign partition around the shared C4. This event has a positive fixed exact GF(5) four-column weight:

```text
F4 = number of 4*4 all-nonzero GF5 checksum-4 coefficient assignments
     solving the alternating signed C4/C4 trade.
```

**Exact coefficient and independent closed-form proof: F4=531.** Regard the two physical coordinate edges (one in each color) corresponding to each edge of the shared abstract 4-column C4 as an **ordered pair** of nonzero GF5 weights, with sum `t_i in GF5`. The alternating 2vs2 sign makes opposite-side weights equal for every physical coordinate. The required checksum of each column is `t_(i-1)+t_i=4 mod5`, so around the even cycle `t_0=t_2=t` and `t_1=t_3=4-t`. A given GF5 sum has `c(0)=4` nonzero ordered representations and `c(u)=3` when `u!=0`. Therefore

```text
F4 = sum_{t in GF5} c(t)^2 * c(4-t)^2
   = 2*(4^2)*(3^2) + 3*(3^4) = 531.
```

This closed form counts *exactly* all admissible weight assignments and is independently verified by E2-B1's full **51²-side GF5 additive-sum histogram** and E0's **2^16-edge prescribed-boundary nowhere-zero flow inclusion/exclusion**. The three derivations agree. It is a four-column template coefficient, not a new general flow theorem.

**Theorem D1 — all-h fixed-label necessary obstruction**:

```text
R2(B_s(f,g)) >= 531 * Q4(f,g) / 51^4.
```

Proof: each Q4 matching gives exactly one unordered alternating 2-vs-2 signed trade; its support incidence is isomorphic to the C4/C4 template and therefore admits exactly F4 of the 51^4 independent allowed full-nonzero checksum4 coefficient assignments. Distinct four-factor-matchings define distinct signed collision events, and R2 sums all their nonnegative probabilities. No other GF5 events are subtracted. This proof does NOT imply any lower bound on Q4 for arbitrary f,g, or any full R2 upper.

## 2. Exact all-h independent-random expectation and matching-class exponent

Let M4(G_s) denote the EXACT (not estimated) number of unordered matchings of four actual GQ factor incidence edges. Under independent uniform injections of each factor part's V vertices into all K=binom(a,2) physical coordinate pairs, a given four-factor matching projects to any one designated 4-cycle dual column-adjacency graph in a chosen half with probability EXACTLY

```text
P4(a) = (a)_4/(K)_4.
```

The four named columns admit precisely 4!/8=3 possible C4 column-adjacency graphs. The three coincident two-color events are disjoint, so linearity yields the **exact** identity

```text
E_independent_labels[Q4] = 3*M4(G_s)*P4(a)^2.
```

Greedy factor-matching choice gives the rigorous explicit lower count

```text
M4(G_s) >= (1/24) * product_{j=0}^{3} (N-2j Δ).
```

Indeed each already selected factor matching edge forbids at most two vertex stars of ≤Δ edges. Here N=Θ(s^4), a=Θ(s^(3/2)), K=Θ(s^3); hence the factor lower is Θ(s^16) and P4(a)^2=Θ(s^-12). Consequently

```text
E_uniform_labels[R2] >= 531*3*M4*P4^2 /51^4
                    = Omega(s^4).
```

With the **accepted** E2-B2 independent-label upper E[R2]=O(s^4), we get E[R2]=Θ(s^4), strictly in this RANDOM model. This is a **model-specific elementary matching-class lower**, not a universal per-label lower and not a new extremal ASET exponent. It means random-label R2 exponent is sharp, even before considering the difficult R3 side. Compare the analogous D_s matching-C6 risk: E[R3]=Theta(s^6) in the accepted independent uniform label model.

## 3. Full GF2/GF4 exact Q4 and unit four-trade multiplicity, no binom(N,4)

The reference [exact finite four/six audit](../../research/hyp105_g5e2b3d_joint_risk.py) computes for both the prior reverse-line control and **the same Plücker lex-min-collision map** as E2-B3.2-C at each h=1/2:

- Full Q4 by enumerating canonical **physical** simple C4 on the left point-pair graph (least coordinate first, smaller neighboring coordinate second) and joining only ACTUAL factor-incidence right line choices. Right physical pair labels must form the matching simple C4 on the SAME four named column IDs, with all endpoints distinct. Each four-factor matching contributes once. Fail-closed cycle budget; no binom(N,4).
- Full **unit** two-vs-two signed trade event count T4_UNIT for ALL N=45 or 425 columns by hash grouping of exactly binom(N,2) integer base-five two-column sums. Each unit support has four 1 coefficients with checksum4 in GF5; since two unit vectors sum to digits 0,1,2, radix-5 encodings have NO carrying. Equal pairs with shared original column IDs are impossible for distinct supports, so every bucket collision corresponds to one real four-column unit GF5 equality. Counts both oriented-event multiplicity (unordered 2vs2) and distinct four-column sets admitting ≥1 unit conflict, which must **not be conflated**. This is **not** full 51^4-weighted R2.
- Record Q4, T4_UNIT and the E2-B3.2-B **full exact D_s** six-cycle count on **the same labeling**. This provides simultaneously grounded necessary R2/R3 risk contributions, not upper bounds.
- Independent oracle for Q4 enumerates all four-column incidence subsets on a deliberately small capped factor subgraph and recomputes both physical dual column-adjacency graphs. Independent oracle for unit T4 directly enumerates every four-column subset and all three 2vs2 choices on a small sampled column set, with equality checked coordinate by coordinate; direct full GF5 E0 flow verifies F4.

### 3.1 Exact hosted full finite model counts and model-method falsifier

GitHub-hosted Research completed a full earlier HEAD run with **628 passing unit tests** and an exact, exhaustive-with-respect-to-defined-count finite report. The following counts are NOT asymptotic and NOT estimated from sampled six-sets:

| Field / full N | Same-label map | Exact Q4 (matching C4) | All unit signed 2v2 events T4 | Distinct unit four-column sets | Exact D6 (matching C6) |
| --- | --- | ---: | ---: | ---: | ---: |
| GF(2), N=45 | Plücker lex-mincollision | **25** | **57** | 57 | **2** |
| GF(2), N=45 | Prior reverse-line control | **32** | **66** | 66 | **3** |
| GF(4), N=425 | Plücker lex-mincollision | **608** | **1,388** | 1,388 | **9,190** |
| GF(4), N=425 | Prior reverse-line control | **573** | **1,380** | 1,380 | **8,417** |

All four T4 signed event counts happen to equal the distinct T4 support-set counts in THESE data; the implementation keeps the quantities separate and does **not** claim equality as a general theorem.

**Concrete method limitation:** Q4 is strictly weaker than full unit T4: at GF4 Plücker, `Q4=608` while `T4_unit=1388`. Even the full exact count of UNIT conflicts is only a lower-risk diagnostic, because each event can admit many of the full 51-pattern GF5 assignments and nonunit events may also be positive. Therefore a bound on the coincident-C4 family **does not** establish upper control of total R2. The Plücker GF4 map is also worse than old reverse-line on BOTH Q4 (608>573), unit T4 (1388>1380), and D6 (9190>8417). No experimental Plücker improvement should be claimed.

## 4. Exact full-palette GF5 R2/R3 — only one explicit seven-column subfamily per model

The report **intentionally** chooses a 7-column subset of the SAME full GQ labeling: the six ordered columns of the FIRST canonical positive exact D_s coincident C6 matching witness, plus the **smallest unused real factor incidence column ID**. This is deliberately **witness-enriched**, not uniform sampling and not representative of whole GQ risk. It is guaranteed to include a genuine GF5 3-vs-3 positive trade and therefore prevents a vacuous zero-R3 sample.

On exactly those seven columns, compute **exact** full checksum4, all-nonzero 51-pattern GF5 weighted R2 by E2-B1 disjoint 2-sum Möbius energy (21*51² local pair assignments). Enumerate all 7*10=70 possible unordered 3-vs-3 signed events; remove only proven-zero events via E1 necessary topology gates and apply **exact** 51³-side GF5 meet-in-middle to EVERY surviving event, including potentially zero-flow gated survivors. Sum flow counts/51^6 to obtain exact sample R3. Enforce explicit ≤12 GF5 candidate budget; exceed it ⇒ FAIL, never silently return incomplete data. The first witness contributes at least 5643 weighted assignments.

Sample R2 and R3 are **exact finite** values for those seven named columns, not upper bounds for the full N=45/425 factor family. Even a direct favorable Q4 or sample R2 does not certify `R2(B_s)=O(s^(26/5-eps_2))` or `R3(B_s)=O(s^(6-eps_3))` uniformly in h. Positive six-motif families outside selected seven remain entirely open.

## 5. Falsifiers, evidence gates and next step

- **Proof scope:** D1 and exact E[Q4] identity hold for ALL h (algebraic counting). Full Q4, unit T4 and exact selected 7-column GF5 R2/R3 are only GF2/GF4 (frozen control). No external geometric symmetry is used.
- **Independent checks:** analytic 531 coefficient vs E0 16-edge inclusion/exclusion vs 51²-side MITM for F4; direct subset brute oracle for Q4; direct coordinate-by-coordinate unit T4; direct balanced 2vs2 single-event summation vs energy on four selected supports; true GF5 3v3 event numerator >=5643.
- **Prior art:** classical alternating/signed graph flow and counting matchings in regular bipartite graphs, published Fu–Ren–Wang (2025) as previously indexed. Do not assert a new general flow theorem or original combinatorial lower exponent without external priority audit.
- **NO-GO gate:** no all-h Plücker or reverse-line **upper** proved, no new ASET exponent. No finite estimate may be fit to uniform asymptotics. B3.1-B (other positive six-flow motif multiplicities), B3.2-E (all-h bounded R2/R3 for same geometry-aware map) remain OPEN.
