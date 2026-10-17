# HYP-105 / issue #230 — AA4-CB: genuine-original physical incidence-parity code and uniform 27/32 seven-GF5 sixcube bound

**SCIENTIFIC DRAFT.** Strict child of [AA4-CA #601](https://github.com/definitely-stable/Mathlab/pull/601) frozen parent HEAD `efb95dd2f1fb876f4b93ff2c0109ce6fb337c687`. No accepted registry or main changes. All results preserve the TRUE original symplectic generalized quadrangle `W(3,2^h)` for ALL h>=1; two arbitrary complete, globally injective, potentially mutually correlated typed original physical-pair maps f and g; SAME six distinct original incidence-ID Q, historical 51-column GF5 and seven-class semantics. Root A/B/C stays **OPEN_WITH_FORMAL_BLOCKER**.

## Scientific selection — new directions and trade-offs

The scientific bottleneck is **pointwise positivity at the unchanged adversarial original (f,g)**, not lack of positive annealed mass. Competing research ideas:

1. **Joint GF5 cross-class low-degree margin:** seek a signed, truly-original cross-map inequality forcing `P_<=3 W(0) > E` or directly `M1+D6>=cs^6`. Highest ultimate relevance to Branch A; existing #574–575 cherry moment and Hall-defect results, #590 signed Gram, and #598 sign-flip witnesses show the first naive positivity routes fail. Requires a new genuinely geometric coercivity mechanism.
2. **Source-cherry Hall-defect stability:** prove that a near-total loss in the enormous one-sided `U` reservoir #575 necessarily creates D6 or other positive seven-class motifs somewhere on the SAME fixed map. The needed global two-side transport inequality is open; a large one-sided count cannot alone force an original-center match.
3. **Physical parity-code sieve (SELECTED):** use a necessary constraint absent from #597–601 — **physical coordinate degrees must all be even**. This creates a GLOBAL sixpacket binary syndrome matrix common to all original Q, forces the support of each accepted Q into a single affine code coset, and yields a compact, rigorously checkable exact Walsh bound and new `g`-adaptive certificate. More structural than refining an abstract Boolean extremum, yet tractable without inventing high-h GQ data.
4. **Two-sided squarefree trace / SDP:** couple #572 nilpotent D6 trace to #574 collision moments through an exact low-rank Gram tensor. Risk: sign-indefinite cross terms and known #555/#558 Hessian no-go; positive semidefinite surrogate by itself is not physical-GF5 coercivity.
5. **Infinite correlated counterfamily:** search highly structured physical image permutations indexed by `s=2^h`, and prove `S_s=o(s^6)` for the SAME actual maps. Finite W32 optimized maps cannot support this conclusion; no such infinite family has been established.

Selection criterion: mathematically new *input invariant*, explicit all-h consequence, falsifiability, limited overlap, and realistic completion. Idea 3 is chosen as an independently scoped theorem; ideas 1–2 remain priority for genuinely closing the root after this slice.

## AA4-CB-PARITY — an exact all-h affine cycle-code constraint

Fix six PAIRWISE DISJOINT original LINE source-factor image-swap packets `(u_i,v_i)`, i=1..6. Fix one actual ORIGINAL six-DISTINCT-incidence-ID set Q hitting all six packets exactly once (the prior original source-support lemma, #590/#599). Let `e_i^0` be its selected original LINE source factor's current g image, and `e_i^1` be the other original LINE source factor's g image. All 12 unordered physical pair edges are **globally distinct** by injection. The sixcube state x chooses physical right edges `e_i^{x_i}`. All 64 x correspond to 64 **complete** original globally injected maps, not independent per-Q redraws.

Let `∂{a,b}=1_a+1_b` be the unsigned degree-incidence column in `GF(2)^a`. Put

```text
b = xor_i ∂e_i^0,
d_i = ∂e_i^0 xor ∂e_i^1,
D = [d_1 ... d_6] over GF(2).
```

For each sixcube state, its entire physical vertex-degree parity vector is

```text
q(x) = b xor D*x.
```

Historical GF(5) seven-class positive acceptance requires the right physical SIX-edge graph to be 2-regular on exactly SIX physical coordinates; therefore `q(x)=0`. For its Boolean indicator `I_Q`,

```text
supp(I_Q) subset {x : D*x=b}.
```

**Crucial affine distinction:** b need not be zero. Even when ORIGINAL x=0 is rejected, a different full global g^x may be accepted and solve the **inhomogeneous** syndrome. A homogeneous-only check is mathematically invalid. The module and adversarial test explicitly preserve b.

This is a *necessary* filter, not an assertion that parity implies degree<=2 or historical GF5 positivity. All Q on the same six globally fixed original source swap packets have identical D (up to swapping individual bit orientations), and no independence among Q is used.

## AA4-CB-RANK — no rank-one packet can produce a physical six-edge 2-factor

All `d_i` are nonzero because the twelve actual source factor images are different unordered physical pairs. Suppose rank(D)=1 and a cube vertex x is physically 2-regular on SIX vertices. Since GF(2) has only one nonzero vector in a one-dimensional space, all six `d_i=d≠0`. A symmetric difference of two distinct edge-boundary vectors has support cardinality exactly **2 or 4**.

- If `|d|=2` with support {u,v}, both edges of each image pair share their OTHER endpoint w and switch the endpoint u to v or v to u. Hence all six selected baseline physical edges are incident to u or v. In a 2-regular graph the total degree at u,v is at most 4, so there can be at most four distinct selected edges incident to them — contradiction to six.
- If `|d|=4`, both distinct physical edge images must lie entirely in the SAME four physical coordinates (each is one complementary matching edge on that four-set). The six selected edges therefore use **at most four** physical coordinates, contradicting the required exactly six.

Thus rank 1 forces every original-sixpacket right 2-factor indicator identically zero; if it is nonzero, `rank(D)>=2` and the allowed affine coset has at most `2^(6-2)=16` of 64 states.

This is a true ORIGINAL physical theorem for every h, every complete arbitrary correlated f,g, every genuine Q. It is a global-injection claim: if different Q or states independently redrew edge images the twelve-edge hypothesis would be invalid.

## AA4-CB-KERNEL — exact rank-two affine code Walsh bound

The degree>3 Walsh projection on Q6 about any center t has radial integer kernel

```text
K6(j) = (22,-10,2,2,-2,-2,10), j=0..6.
```

If the rank is at least two, the original positive Boolean indicator is supported in one affine coset of the kernel of D. For a signed K6 sum, the largest possible *positive* choice of that indicator on the coset is the sum of positive K6 entries in it; similarly, the negative extremum is the negative of the sum of negative entries. Taking every possible coset also covers an arbitrary translated center t. This is a safe bound, because it RELAXES physical degree, N3, source incidence and GF5 requirements.

**Finite rank-two lemma:** for EVERY affine coset of EVERY rank-two linear map `GF(2)^6->GF(2)^2`, its sum of positive K6 entries and magnitude of negative K6 entries are **both <=54**.

**Finite mathematical proof A — 16 complete column profiles.** Choose a basis of the two dual linear forms; each of the six coordinate columns has one of four GF2^2 colors 0,1,2,3. The group `GL(2,2)` permutes the three nonzero colors. Thus every rank-two matrix can be reduced, without changing signed Walsh sums or syndrome maxima, to ONE of exactly 16 integer color-frequency profiles `(n0,n1,n2,n3)`, with `n1>=n2>=n3>=0`, `n2>=1`, sum 6. Multiply the exact four-colored generating polynomial in the group ring

```text
F(z,U)=(1+z)^n0 (1+z U_1)^n1 (1+z U_2)^n2 (1+z U_3)^n3,
U_a U_b = U_(a xor b).
```

The coefficient of `z^j U_t` is EXACTLY the number of Hamming-weight-j vertices in syndrome t. Weight coefficients by positive and negative parts of K6. The **maximum over four syndromes** for each of the 16 cases, with zero columns allowed, is:

```text
(n0,n1,n2,n3): max positive/negative unsigned numerator
(0,2,2,2):54   (0,3,2,1):44   (0,3,3,0):36
(0,4,1,1):52  (0,4,2,0):48   (0,5,1,0):52
(1,2,2,1):38  (1,3,1,1):50   (1,3,2,0):40
(1,4,1,0):48  (2,2,1,1):34   (2,2,2,0):46
(2,3,1,0):42  (3,1,1,1):42   (3,2,1,0):38
(4,1,1,0):42
```

This small finite certificate is **universal**, independent of s, and entirely integer/rational. Every rank-r>2 kernel sits inside a rank-two super-kernel (select two independent row checks), so the same positive/negative-part bound applies by set inclusion.

**Independent proof/falsifier B:** enumerate all independent ordered pairs of two sixbit dual masks, canonicalize their three nonzero row-space members, and directly group all 64 cube vertices into four cosets. There are exactly `[6 choose 2]_2=651` distinct rank-two dual row spaces; exhaustively compute signed positive/negative K6 mass on all 2,604 affine cosets, independently of the group-ring profile calculation. The exact maximum is also 54. No LP, floating point or external solver.

**Consequence (every genuine original sixpacket GF5 acceptance indicator):**

```text
max_x |(I_Q-P_<=3 I_Q)(x)| <= 54/64 = 27/32 < 15/16.
```

This `27/32` is SHARP over a relaxed abstract rank-two affine-support model (dual masks 15 and 51, zero-syndrome coset, retain positive K6 entries). It is NOT claimed SHARP over genuine original globally injected physical edge pairs or historical seven-GF5 Q. That relaxed witness also obeys abstract N3/independence, so the parity condition adds a genuinely new restriction beyond the constraint class optimized in #601.

### An even stronger ORIGINAL rank-adaptive certificate

For the FIXED actual complete original g and fixed six source LINE packets, compute the entire six-column D and the exact affine-coset maximum

```text
eta(D) = (1/64) max_{syndrome cell C}
  { sum_{x in C} max(K6(|x|),0),
    sum_{x in C} max(-K6(|x|),0) }.
```

This is evaluated over at most 64 integers; `eta(D)<=27/32` for rank>=2. For rank1 physical acceptance is empty and `eta(D)=0`. Thus an actual g-dependent bound may be **strictly stronger** than uniform `27/32`; the global f-only bound remains valid if g is unknown. The cosets are independent of Q orientation (reversing individual packet bits only translates the syndrome partition).

## Exact original all-seven 51-column GF5 fixed-center consequence

Retain the same H6(f;packets) original f-only weighted eligible SIX-DISTINCT-incidence source-Q mass and the unchanged low degree score P<=3 W from #597–601. Each eligible sixth-sensitive Q now obeys `eta6<=27/32`, with other support terms unchanged; summing per-Q nonnegative weights uses ordinary triangle inequality, **not cross-Q independence**. All dyadic h>=1, all original complete correlated f,g, all 64 fully injected right-map cube vertices:

```text
E_f^CB = E_f^CA - (3/32)*H6(f;packets),
|W(f,g^x)-P_<=3 W(x)| <= E_f^CB.
W(f,g) >= max(0, P_<=3 W(0) - E_f^CB).
```

For a known original g, `E_(f,g)^CB=E_f^CA-(15/16-eta(D))*H6(f)` is a stronger all-64-state, same-map certificate.

**Genuine original W32 exact predictions to independently check on GitHub-hosted CI:**

| W32 physical f scheme | Actual H6(f) | Additional universal saving over CA | New uniform E_f^CB | True historical W(0) |
|---|---:|---:|---:|---:|
| lex | 4690929 | 14072787/32 | 16212794755/32 | 11225795 |
| S72 | 3731790 | 5597685/16 | 7761243177/16 | 3283610 |

Both values are derived from authentic original W32 historical seven-GF5 prior source counts; no finite extrapolation to large W3. The rank-adaptive values depend on actual g and are separately printed and validated in the tests. No positivity is inferred if low-order margin stays nonpositive.

## Scope, prior art and non-implication

Cycle-space parity over GF(2), binary incidence matrices, rank-nullity, affine codes and Walsh/Krawtchouk projections are **classical** (e.g., Diestel, *Graph Theory*, §cycle/bond spaces; Kavitha–Mehlhorn–Michail–Paluch, *A minimum cycle basis algorithm*, 2008, https://link.springer.com/article/10.1007/s00453-007-9064-z; O'Donnell, *Analysis of Boolean Functions*, https://arxiv.org/abs/2105.10386). Novelty claim is narrow: combine those classical facts with actual ORIGINAL globally injected six-LINE-swap, same-six-ID GF5 necessary risk to obtain rank-one physical exclusion and a rigorously certified rank-two bound. No external literature-priority audit or peer referee acceptance.

This is **PARTIAL all-h progress**, NOT `PROVED_A`, `COUNTEREXAMPLE_B` or `RESTRICTED_THEOREM_C`: it does not prove unchanged original `S_s(f,g)=Omega(s^6)`, construct an authentic infinite correlated `o(s^6)` sequence, or give a model-equivalent root reduction. The selected positive GF5 W is a NECESSARY subset of the full R3 numerator, not entire R3 or an ASET exponent. The local parity code bounds the fluctuating high-order part; absent a positive original-center low-order seven-class inequality, root #230 remains open. CI verifies computation, not a human proof acceptance. Keep Draft and do not alter accepted claims/main/issue state until qualified referee, exact final-head CI and ancestor gates.

## Reproducibility

1. Exact 16-profile finite certificate, independent complete 651-dual-space enumeration (no SciPy).
2. A physical K8 injection with rank one and NO six-edge 2factor across all64 maps.
3. A physical K6 original-center **nonzero affine syndrome** counterexample to a wrong homogeneous-only projection.
4. Original W32 lex and S72: every genuine sixth-packet original Q, all 64 global right maps, direct physical 2factor and historic seven-GF5 tag as independent checks, universal and actual-g-adaptive W32 envelope.
5. Invalid source packets and physical image injection rejected; three GitHub-hosted jobs on the new Draft.

**Next priority:** original two-sided low-degree seven-class positive-margin/defect coupling (ideas 1 and 2), not endless local kernel improvement. A promising now-falsifiable question is whether **averaging rank-adaptive parity coset restrictions across MANY coupled sixpackets** forces a nontrivial global seven-class positive count for every unchanged (f,g), rather than merely a single packet error saving. That cross-packet coercivity statement remains unproved.
