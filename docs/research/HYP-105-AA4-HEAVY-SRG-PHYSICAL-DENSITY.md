# HYP-105 / #230 — AA4-HEAVY-SRG-PHYSICAL-DENSITY: all-order audit of real HEAVY F and stronger constant

**Status:** scoped independently derived deterministic HEAVY theorem, not accepted root Branch A. Strict scientific child of frozen [Draft #775](https://github.com/definitely-stable/Mathlab/pull/775) HEAD 1d84380b8450e62ec3d72ed2209cfaf55eecb8a1. No ancestor/main changes or merges. Root #230 remains OPEN_WITH_FORMAL_BLOCKER, no GF5/ASET exponent. Prior #744/#750 already derived the owner-to-F construction, #772 already accepted the C6→original-D6 source lift, and #775 already strengthened original source J. **New:** independently audited combination of the true physical construction with sharper original J and a NEW minimal-pair-alphabet bound a²<A_H s³, producing R=66562 instead of 93312 at fixed H=32.

## A. Original source and quantified inputs

Fix EVEN integer H≥8 ONCE before all subsequent choices. For any s=2^h≥2^H, original true symplectic W(3,s) has V=(s+1)(s²+1) points and lines, N=(s+1)V distinct named ORIGINAL incidence flags. Let a=min{b:binom(b,2)≥V}, f:P↪binom([a],2), g:L↪binom([a],2), fixed separately globally pair-injective, arbitrarily correlated. Every flag owns two vertex-disjoint ACTUAL physical diagonal edges of f(p)×g(ell), with unique named source ownership. Work with **Z=empty**, which is sufficient for the root seven-original-motif Branch A obstruction. Define the true original physical simple graph Hfull with 2N actual edges, Q_T={v:degree_Hfull(v)>Ts}, and the count E_T of actual edges touching frozen Q_T. HEAVY is E_T≥s⁴/8.

## B. Genuine source J and sharpened alphabet

The already independently reviewed original GQ/SRG theorem #775 gives, with full ORIGINAL point/line pencil source conflict J,

e(J) < 2 M_H s⁴,   M_H=(1+2^(-2H))(1+23/(16·2^(H/2))).    (B1)

Its criterion is SAME original point with intersecting g-label pairs OR SAME original line with intersecting f-label pairs. No random embeddings, Sp symmetry, f/g independence or cloned flags.

Minimality of a implies (a−2)(a−1)<2V and hence a<sqrt(2V)+2. Since V/s³=(1+1/s)(1+1/s²), for s≥2^H we have V/s³≤(1+2^(-H))(1+2^(-2H)). The GQ envelope for H≥8 gives sqrt(2V)<(23/16)s^(3/2), because V≤(33/32)s³ and sqrt(33/16)<23/16. Square a<sqrt(2V)+2, divide by s³ and use these exact inequalities:

a² < A_H s³, where

A_H = 2(1+2^(-H))(1+2^(-2H))
      +23/(4·2^(3H/2)) +4·2^(-3H).                     (B2)

A_H is an explicit positive RATIONAL for even H. Crucially A_H→2 rather than historical universal 9/4, with NO assumption a(a−1)/2=V. This is a valid bound for every legal f/g.

## C. Source heavy owners, Caro–Wei and whole-flag two cuts

Each actual edge touches at most one distinct original flag owner and each flag owns exactly two edges. Thus the E_T≥s⁴/8 HEAVY edges represent L≥E_T/2≥λs⁴ distinct genuine original flag IDs, λ=1/16. The induced source conflict J on these L named flags has at most the full e(J)<2M_Hs⁴ edges. Caro–Wei and Cauchy (not graph symmetry) yield an independent set I with

|I| ≥ L²/(L+2e(J[L]))
    > λ²/(λ+4M_H) s⁴.                                (C1)

Give physical symbols of f independently uniform bits, choose one coloring retaining ≥|I|/2 WHOLE owner flags whose f pair crosses; then give g symbols independent bits and fix a coloring retaining ≥half of those WHOLE owners. Let S denote retained ORIGINAL IDs, still source J-independent. ALL their two real diagonals survive together, with consistent bichromatic cuts in BOTH typed physical alphabets. Therefore

|S| ≥ |I|/4 > λ²/(4(λ+4M_H)) s⁴.                     (C2)

Only linearity of expectation and the method of conditional expectations are needed; no independence of different flag survival events is assumed.

## D. Physical F without cloning or synthetic edge changes

Each i∈S had an ORIGINAL heavy edge touching frozen Q_T; choose ONE real surviving heavy edge and ONE real Q_T endpoint as witness. Different i have different witness edges due original source ownership. Majority of these witnesses have the same first-coordinate bit b; at least |S|/2 original-owned REAL edges witness that bit. Let R_Q be ALL actual Q_T physical vertices of bit b, r=|R_Q|≥1. Each retained f-pair crosses the first cut, so the other actual endpoint of every witnessed edge has the opposite bit; their physical endpoint set Y⊆[a]² satisfies |Y|≤a².

Partition Y into at most ceil(|Y|/r)≤2a²/r blocks, size at most r (since r≤a² and |Y|≥1). Pick the block with the most ACTUAL selected-owner physical edges touching R_Q. Define simple graph F on real physical vertices R_Q and that chosen block, with ALL existing selected physical edges between the two; no extra vertices or edges are created. Then

m_F ≥ |S|r/(4a²),  v_F≤2r,  m_F/v_F≥|S|/(8a²).      (D1)

F is a subgraph of the paired selected source graph; it may retain only one of a flag's original two diagonals, as required for an ordinary graph C6 theorem. Full Hfull has total degree 4N; each heavy vertex has original degree >Ts, so |Q_T|<4N/(Ts). Since N≤17s⁴/16 for s≥64,

v_F≤2|Q_T|<8N/(Ts)≤(17/2)s³/T.                   (D2)

Combine B2,C2,D1: m_F/v_F > λ² s/[32 A_H(λ+4M_H)]. For

R_H=ceil(32 A_H(λ+4M_H)/λ²), λ=1/16,

we conclude the improved TRUE-physical all-h HEAVY inequality

m_F/v_F > s/R_H.                                 (D3)

Both estimates D2/D3 use exact source/physical objects, not theoretical copy graphs.

## E. External C6 and genuine ORIGINAL D6

Fix once, BEFORE s and f/g, rational existential ordinary C6 graph theorem bounds C0≥max(1,C_graph), 0<c0≤min(1,c_graph), with the external Jiang–Yepremyan 2020 r=2,k=3 specialization previously checked in #749. Their actual numeric values are NOT established here. Choose T=ceil((17/2)R_H³ C0³). Then D2 and D3 give (m_F/v_F)^3≥C0³ v_F, so the published theorem applies to this ACTUAL simple graph F. The independently audited #772 six-flag source inverse applies because selected S is TRUE original J-independent and has BOTH coherent typed physical cuts. Every unoriented simple C6 of F maps injectively to one original six-incidence-ID D6, no 12 or 6! factor. Therefore in HEAVY,

D6_ORIGINAL(f,g) ≥ (c0/R_H^6)s^6.                (E1)

This is a properly quantified deterministic all-h HEAVY implication from GQ and the published ordinary graph theorem, NOT the full LOW/HEAVY root result.

## F. Numerical constants: exact rational, NOT a numerical published graph theorem

At fixed H=32, R_H=**66562**, previously R_old=93312. The coefficient improves by the exact ratio (93312/66562)^6 ≈ **7.59044**, with the SAME s^6 exponent and same existential c0. The LOW inherited K=10, H=32 source core bound, Blakley–Roy, Harris q2=1936/q3=85184, and asymmetric allocation α=(1/64,1/64,15/16) are unchanged, while T,L6,L4,B0,E,D,s0,δ must ALL use the NEW R.

Independent exact Fraction root probes, using deliberately FORMAL C0/c0 placeholders only:

| FORMAL C0,c0 | Previous #775 h0 | New conditional h0 |
| --- | ---: | ---: |
| (1,1) | 667 | **653** |
| (2,1/5) | 697 | **683** |
| (7/3,1/17) | 704 | **689** |

All three numbers are formal algebraic examples; they are NOT actual published theorem thresholds or finite-s verified results. The LOW branch and exact P3→BBo original sixset inverse remain separate acceptance conditions. If those are independently proved and accepted, unchanged HEAVY/LOW logic conditionally gives S_s(f,g)≥(c0/R_H^6)s^6 for the unweighted seven original six-ID classes. Do NOT promote #230 to PROVED_A merely on finite tests or green CI.

## G. Independent falsifiers, scientific limits, next proof gate

Standalone source code in research/hyp105_heavy_srg_physical_density.py only imports the existing first-principles true symplectic W32/W34 incidence constructor from #748 for finite source fixtures, not prior HEAVY/J/selector/LOW/ROOT/GF5 computations. It independently implements original two-diagonal ownership; frozen heavy edge census; named pencil J; diagnostic greedy original independent owner subset; two deterministic full-symbol conditional-expectation cuts; witness majority; real opposite symbol blocks and ordinary F. Genuine W32/W34 lex/reverse/shift tests verify all concrete inequalities nonvacuously, using diagnostic **T=1 (NOT the all-h T)**.

Further exact independent tests check H=8,16,24,32,40,64 rational envelopes, minimal original a via integer square roots, H32 R, 7x improvement, formal h0 and all STOP conditions. Historical #775 root calculator is used ONLY in tests to compare predecessor thresholds, never in the standalone computation.

**Next scientific acceptance gate:** independently audit the genuine ORIGINAL selected LOW 4th/6th-moment transfer and the mixed FULL A/CORE C blocker global exponents. The known P3→produced BBo two-direction injection is to be included in that global proof dependency review. Root #230 remains OPEN_WITH_FORMAL_BLOCKER; no source paper publication or ASET exponent claim follows from this slice alone.
