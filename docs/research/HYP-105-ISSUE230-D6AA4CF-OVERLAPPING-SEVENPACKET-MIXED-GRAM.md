# HYP-105 / #230 — AA4-CF: overlapping seven-packet original-family exclusion and mixed Gram

**SCIENTIFIC DRAFT**; strict child of [AA4-CE PR #605](https://github.com/definitely-stable/Mathlab/pull/605), frozen parent exact HEAD `f42ef6677b873800574bcc7c67a6c19d6c3030ef`. Root #230 OPEN_WITH_FORMAL_BLOCKER; preserve all 7 historical accepted GF(5) classes and exact 51-column positive weights; no main, accepted registry, or root verdict edits.

## 1. Research selection, prior art and precise frontier

The root demands either original every-fixed-map `S_s(f,g)=Omega(s^6)`, a true ORIGINAL infinite correlated counterfamily `o(s^6)`, or a qualifying equivalent restricted theorem with independent falsifiers. Previous #597–601 proved original full 7class Boolean highpass conditional bounds; #602 original per-Q affine physical GF2 filter; #603 rank-one obstruction; #604 signed one-sided original-map center positive W32 witnesses; #605 shared SAME-SIXPACKET sixcube physical XOR mask and exact within-one-family autocorrelation. None derives quantitative universal original-center S positive.

**NEW gap relative to #605:** a sixflag Q_A can touch packets 0,1,2,3,4,5 while Q_B touches 0,1,2,3,4,6. These two sets do NOT share the same six-packet right mask; their original global correlations cannot be represented by a single 64-bit R_g translation. A first legitimate *overlapping distinct-packet* joint oracle is required before proving any cross-family coercivity.

Research alternatives considered: (a) joint sevenpacket actual physical 2factor compatibility, (b) whole-geometry cherry Hall-defect coercivity, (c) two-sided nilpotent D6/collision mixed moment, (d) infinite counterfamily search. (a) is a deliberately small exact all-h theorem with definitive falsifiers and advances from previous SAME sixpacket coupling. It is not claimed stronger than the global unresolved original-center positivity.

Classical prior: a prescribed graph degree sequence imposes equality of vertex degree vectors; no single distinct simple edge can replace a chosen edge while preserving all graph degrees. Standard degree-preserving graph **2-switches** exchange at least two edges. See Bereg–Ito (2017), *Transforming Graphs with the Same Graphic Sequence*, DOI:10.2197/ipsjjip.25.627 and prior project #599 original sixcube one-edge exclusion. The **five-edge uniqueness lemma itself is elementary/prior**. Scoped new result: use it ACROSS TWO GENUINE ORIGINAL SIX-ID Q FAMILIES on the SAME 128 complete globally injected original g maps, with exact mixed historical necessary physical Gram/weighted incompatibility, not fictitious independently relabeled source Q.

## 2. AA4-CF theorem — all-h original two-family same-five pins cannot coexist

Fix arbitrary h>=1, s=2^h and the authentic symplectic generalized quadrangle W(3,s). Fix ANY two fully globally injected, arbitrarily correlated typed original physical pair maps f (points) and g (LINEs). Fix seven PAIRWISE DISJOINT pairs of TRUE ORIGINAL LINE factor IDs P_i=(u_i,v_i), i=0,..,6, all 14 IDs distinct. Such packets exist since number of LINE source factors V=(s+1)(s²+1)>=15 even at s=2. Toggle WHOLE original g images of each pair independently, producing **ONE GLOBAL** 7cube of 128 complete globally injected original maps g^x with the SAME original occupied image set.

Consider a true original six-DISTINCT-incidence set Q_A using precisely ONE original LINE endpoint in each of packets 0,1,2,3,4,5 (no other original LINE); and Q_B using exactly one from packets 0,1,2,3,4,6. Each is a FIXED original incidence-ID set over all x; it may have any legal original POINT incidence/source class. The two sets cannot be the same because they use different disjoint sixth packets.

Let t_A in F2^6 and t_B in F2^6 denote the ORIGINAL LINE choices in their respective packet families, with first five coordinates correspondingly aligned. Assume first five original factor choices AGREE, t_A[0:5]=t_B[0:5]. At every global x, both sets select exactly the SAME first FIVE actual physical LINE pair images e_i^{x_i XOR (t_A)_i}. Their respective sixth images are e_5^{x_5 XOR (t_A)_5} and e_6^{x_6 XOR (t_B)_5}. These are DISTINCT unordered physical edges since the original g is globally injected across all 14 source LINE IDs.

**Five-fixed-edge uniqueness:** If one six-edge graph consists of five fixed distinct unordered simple edges E5 and a sixth edge e, and is 2-regular on exactly six distinct physical coordinates, then its entire degree vector is determined: every vertex with E5-degree 1 needs precisely one endpoint and there must be exactly two such deficient vertices. Therefore e is the UNIQUE unordered pair connecting those two vertices. If there is no such residual vector, NO edge can complete to a six-coordinate 2factor. In particular, TWO distinct sixth edges e != e' cannot both produce valid 2factors with the same first five actual edges. This does NOT require knowing which six physical vertices are occupied in advance, and is valid even for disconnected 2regular sixgraphs (e.g. two triangles).

Thus, UNIFORMLY over all original h, all complete arbitrary correlated original f,g, all original six-ID Q_A,Q_B of the specified overlapping types and all 128 same complete global g^x,

```text
t_A[0:5] = t_B[0:5]  =>  R_QA(x) * R_QB(x) = 0.
```

Since every one of the accepted HISTORICAL seven GF5 Q classes requires right physical sixcoordinate 2regularity, also

```text
t_A[0:5] = t_B[0:5]  =>  I_QA^GF5(x) * I_QB^GF5(x) = 0.
```

This is a **true original cross-family deterministic anti-coexistence**, not a positive count theorem. The original POINT maps, both GF5 source classes and cross-map correlations are unchanged, and GF5 positivity is only claimed to be a subset of physical support.

## 3. One 128-map physical mixed Gram

For each complete original g and seven real packet-image pairs define two separate 128-bit physical sixgraph predicates:
- R_A(x): actual physical 2regular six-edge graph formed by choosing packets 0..5 under global x, independent of bit 6.
- R_B(x): graph from packets 0..4 and 6, independent of bit 5.

The previous unshifted R_A(x)R_B(x)=0 for all x is the five-edge uniqueness lemma applied with **identical physical choices** in all five shared packets. It does NOT imply absence of overlap after different source orientation shifts. Indeed an exact K6 witness has BOTH masks nonempty and positive mixed overlap for some differing shared orientations; a tool that returned every mixed pair zero would be falsely strong.

For original Q_A orientation t and Q_B orientation u, lift each sixbit source orientation into the appropriate 7bit global packet positions `embed_A(t)` and `embed_B(u)`. Their original right physical necessary indicators on the SAME complete global g^x are

```text
R_QA(x)=R_A(x XOR embed_A(t)),
R_QB(x)=R_B(x XOR embed_B(u)).
```

Define the **mixed 64x64 physical Gram** of actual sevenpacket overlap

```text
J_g(t,u) = sum_{x in F2^7}
     R_A(x XOR embed_A(t))*R_B(x XOR embed_B(u)).
```

It is an exact NONNEGATIVE integer count, 0..128, of common full-g physical right-2factor-admissible states. Its normalized value J/128 is an exact joint probability only if sampling ONE common global swap vector x uniformly. The phrase mixed Gram refers to the inner products of 64 lifted A indicator columns and 64 lifted B columns; the mixed block need not be PSD individually, while the full 128-column joint indicator Gram IS PSD.

The theorem yields `J_g(t,u)=0` whenever t and u have the same first-five orientation bits, for ALL g (and all h). For distinct prefix there is no blanket no-go; test explicit globally injected K6 with A selected physical cycle 01,12,23,34,45,50 and B selected physical cycle 01,12,23,35,54,40 (one flipped shared packet), proving physically NONVACUOUS mixed positive overlap.

## 4. True ORIGINAL f-only historical weighted source mass and exact cross-family upper surrogate

For f and the true original source geometry, and for each family k=A,B, enumerate **all true original SIX-DISTINCT incidence-ID Q** satisfying its six LINE packets and original point-side physical sixcoordinate 2regularity, with an immutable historically possible positive GF5 class c(Q) (the same criterion from #597/#605). Define

```text
H_k(t) = sum_{Q in family k, source orientation t} w_{c(Q)}
N_k(t) = # such TRUE original source Q.
```

The historical necessary weights are the exact seven-class certified positive 51-column constants; the scalar tables depend only on original f and source packets, not on any independently sampled right map.

For each of the same 128 original global right maps define

```text
B_A(x)=sum_t H_A(t) R_A(x XOR embed_A(t))
B_B(x)=sum_u H_B(u) R_B(x XOR embed_B(u)).
```

Then for the REAL accepted historical GF5 sixth-packet family scores `W_A^GF5` and `W_B^GF5` computed on original six incidence IDs,

```text
0 <= W_A^GF5(x) <= B_A(x),
0 <= W_B^GF5(x) <= B_B(x).
```

Their physically necessary mixed upper second moment factorizes EXACTLY:

```text
sum_x B_A(x) B_B(x)
  = sum_(t,u) H_A(t) H_B(u) J_g(t,u).
```

This equality is about PHYSICAL upper surrogates B; it is **NOT an equality** or a positive lower bound for historical GF5 joint motif counts. In particular, if t and u share their first FIVE original source packet LINE factor choices, their weighted contribution vanishes identically in the mixed product for every x.

For the UNWEIGHTED original distinct-Q cross-family candidate population, the exact **structurally forbidden real pair charge** is

```text
F5 = sum_{t,u: t[0:5]=u[0:5]} N_A(t)*N_B(u).
```

The actual physical no-overlap charge is

```text
Fphys = sum_{t,u: J_g(t,u)=0} N_A(t)*N_B(u) >= F5.
```

These are true original-Q-pair counts (not label automorphism orbits), and their exact 51-column weight-product analogues follow by replacing N with H. For ALL legal global g, all F5 pairs can never be simultaneously physical GF5 positive at one fixed original global map; Fphys may exclude more due to specific geometry. A high forbidden fraction does **NOT** imply root A; it may instead evidence anti-alignment of different motif source packets.

## 5. Independent falsifiers and counterexample guard

1. Exhaustively enumerate each 5-edge subset of physical K6 (3,003 subsets), and all 45 pairs of unused candidate sixth edges (135,135 input cases). A separate direct physical degree-counting implementation independently confirms no TWO distinct completions. This is a finite model-independent falsifier of the degree lemma, not a proof for all h.
2. Construct one **FULL 15-edge K6 original LINE injection**, in seven actual source-factor pairs plus one leftover edge, with both A and B masks NONEMPTY. Base A=01,12,23,34,45,50; B=01,12,23,35,45,04 on DIFFERENT shared packet orientation. Check `J(0,0)=0` but `J(0,8)>0` and all 128 exact common-map physical degree profiles. Distinguishes true five-pin exclusion from false global exclusion.
3. On TRUE original symplectic W32/K6 lex and S72 **complete fixed** f,g: enumerate original source Q for BOTH sixpacket families; each true six original incidence IDs remain constant under all 128 complete global right maps, direct independent physical degree and historical seven GF5 check against translated per-family 128-bit masks. Verify the exact mixed Gram identity, F5 and Fphys. Separately substitute the deliberately **BOTH-PHYSICAL-LIVE full actual K6 g injection**, while retaining authentic original f and source incidence system, and repeat.
4. Explicit fail-closed guards on 14 source factor IDs, 12+ source images, overlapping packets, malformed source six-incidence sets and non-injective complete original g. Reverse all original right pair images as an adversarial g-only change, confirming f-only source histograms stay identical.

All computations exact integers; GitHub-hosted runners only, and no fabricated high-h geometry. Dedicated distinct CI jobs and source proof Markdown.

## 5a. Exact true-original W32 cross-family evidence (finite only)

The dedicated ORIGINAL W32 oracle verified all real six-incidence-ID Q from both families over all 128 **complete original** right maps, and independently counted the `Q_A×Q_B` pairs on the genuine original incidence structure.

| True W32 original f/g | Original QA (packets 0..5) | Original QB (packets 0..4,6) | Physically active A / B 7cube states | Total crossfamily Q pairs | Five-same-source-LINE-pin pairs forbidden for EVERY g | Additional physical-specific Fphys | Exact mixed physical envelope sum |
|---|---:|---:|---:|---:|---:|---:|---:|
| lex | 351 | 358 | 0 / 0 | 125,658 | 4,307 | 125,658 | 0 |
| S72 | 301 | 378 | 2 / 2 | 113,778 | 4,064 | 110,205 | 661,709,004,813 |
| S72 same REAL original source f, deliberately globally re-permuted COMPLETE g with both physical family masks nonempty | 301 | 378 | 4 / 4 | 113,778 | 4,064 | 106,487 | 2,940,361,517,916 |

The fifth-common-LINE-pin F5 numbers depend on f and the original true source Q, NOT on the right physical g. They are exact deterministic forbidden pair counts for ALL 128 complete source-image swaps and indeed for ANY complete globally injected right g. Fphys depends on the actual fixed original g and may be much larger; empty physical masks in lex cause Fphys to equal ALL pairs, a trivial stronger obstruction. The S72 cases have BOTH masks nonempty and are therefore nonvacuous (110,205/113,778 and 106,487/113,778 physically incompatible cross-family source Q pairs).

The final both-live adversarial full-K6 g regression independently reconstructs literal 128-bit physical right-2factor masks for EVERY authentic original Q_A and Q_B on all 128 **complete** global original g maps, and counts physical incompatible Q-pairs by ANDing those directly reconstructed masks WITHOUT querying the mixed J matrix. This independently validates 106,487 exact exclusions and 4,064 five-source-pin matches, against the compressed 64x64 mixed Gram approach. A finite numerical fraction is NOT a uniform all-h frequency theorem.

**Strict inference limits:** these are restrictions on physical NECESSARY eligibility, not accepted GF5 positive motifs. In particular neither F5 nor Fphys forces a positive original-center contribution from a different packet family. A disallowed simultaneous pair is not a required individual motif; avoid an unproved supersaturation implication.

## 6. Strict acceptance limitations and what should follow

AA4-CF is an EXACT **conditional structural all-h statement** and a complete finite mixed physical compatibility certificate. It neither proves unchanged global original all-seven positive `S_s(f,g)=Omega(s^6)` for every f,g, nor constructs a genuine infinite correlated `o(s^6)` sequence, nor supplies qualifying Branch C equivalence, full R3/ASET exponent or any implication that source physical candidates are historically GF5 positive. Keep Draft pending exact final-head dedicated/INDEX/Proof Audit/full Research and an INDEPENDENT QUALIFIED mathematical referee, as well as actual accepted ancestor Git stack (not merely a retargeted PR metadata base).

**Next meaningful target:** an intersection/defect inequality connecting overlapping five-pin *physical forbidden pairs* to ALL-SEVEN **positive** original source classes across the FULL set of packets and source-touch counts k<=5. This needs new original geometry; F5 alone is an upper compatibility obstruction and cannot be turned into a universal positive original center by symmetry or positivity claims.
