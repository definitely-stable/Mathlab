# HYP-105 #230 — EICE-002: whole-incidence paired-diagonal G* theorem

Status: **RESTRICTED_THEOREM_C**. True *all-h* structural theorem for s=2^h>=64, arbitrary globally injected ORIGINAL f,g. **NO Branch A S=Omega(s^6)**; no spectral endpoint/interior ENERGY UPPER. Research-only; strictly stacked on EICE-001 PR #449 (HEAD 414b14b0023db6f30a03c27973b980eb826c0b20), whose base is PR #394.

## Theorem G1 — coherent regularizer with explicit uniform constants

For s=2^h>=64, V=(s+1)(s^2+1), a=min{b:binom(b,2)>=V}, N=V(s+1), any globally injective ORIGINAL f:P->pairs([a]) and g:L->pairs([a]) on W(3,s), there exists a subset I* of complete ORIGINAL incidence IDs, whose entire two physical Kikuchi diagonals are retained, and G* with:

    |E(G*)| >= s^4 / 40000,
    min{deg(v):deg(v)>0} >= s/1000000,
    all nonbacktracking 3-paths coordinate-proper,
    every ordinary simple C6 coordinate-proper and hence equal to ORIGINAL D6,
    G* bipartite and every coordinate block of physical neighbors degree <=1.

No restrictions on correlation between f,g. No assumption S=o(s^6), random g, independent source scopes, or finite cut-off extrapolation.

### Proof with constants

Write r_{p,y}=#{l incident p:y in g(l)}, and symmetrically r_{l,x}=#{p incident l:x in f(p)}. Define ORIGINAL pair-collision books

    M_g=sum_(p,y) binom(r_{p,y},2),   M_f=sum_(l,x) binom(r_{l,x},2).

Use the previously proved PR394 GQ spectral book bound:

    M_f,M_g <= C_s=(s-1)V+(s^2+1)(a-1).

For s>=64, a <= floor(2*s^(3/2)): put b=floor(2*s^(3/2)), note binom(b,2)>=(2*s^(3/2)-1)*(2*s^(3/2)-2)/2 >= (s+1)(s^2+1); hence a^2<=4s^3. Also

    C_s/N=(s-1)/(s+1)+(a-1)/(s+1)^2
          < 1 + 2/sqrt(s) <=5/4 <3/2.

We use the deliberately looser C_s<=3N/2.

STEP 1: In every ORIGINAL point pencil p consider the graph of g(l) labels for l through p. Delete edges incident to any physical vertex with local degree >D=8. The number deleted is at most 2M_g/D, because for degree k>D the number of deleted incidences touching that vertex is <= k <= 2*binom(k,2)/D. The remaining local physical graph has maximum degree <=D. Greedy edge matching keeps >=remaining/(2D-1) incidences. Summing over p:

    |I1| >= [N-2M_g/8]/15 >= (1-3/8)N/15 = N/24.

STEP 2: In every ORIGINAL line pencil l apply the dual operation to f(p) for currently retained p in l, with D'=160. Restricting incidences cannot increase M_f. Greedy local matchings yield

    |I2| >= [|I1|-2M_f/160]/319
          >= [N/24 - 3N/160]/319 = 11N/153120.

The two per-pencil disjointness properties survive further incidence deletions.

STEP 3: For selected I2 color all left physical coordinates cL:[a]->{0,1} such that >=half the incidence-weighted physical f(p) edges are bichromatic. This follows by uniformly random coloring, or by deterministic conditional expectations. Keep only those I_L. Repeat on the right physical coordinates cR, weighted by I_L, keeping I3. Then

    |I3| >= |I2|/4 >= 11N/612480.

Each incidence still contributes BOTH physical diagonals. Before peeling there are 2|I3| >= 11N/306240 physical edges.

STEP 4: **Paired incidence peeling**, not ordinary arbitrary physical edge peeling. While a physical vertex has 0<deg(v)<delta*s (delta=10^-6), remove EVERY whole original incidence whose one physical diagonal meets v; this simultaneously removes the other diagonal elsewhere. Processing v removes at most deg(v)<delta*s source IDs and <=2deg(v) physical edges. Each nonzero-degree physical vertex can be processed at most once as degrees only decrease. The graph has a^2 physical vertices, hence total physical edge deletions <2delta*s*a^2 <=8e-6*s^4. Thus the final number of physical edges is

    >= (11/306240 - 8/1000000)*s^4
    = (2429/87000000)*s^4 > s^4/40000.

Every remaining nonisolated vertex has degree >=delta*s. A vertex may become isolated during peeling without harm. No diagonal is retained alone.

STEP 5: For each surviving physical edge from original (p,l), f(p)={x,x'} is cL-bichromatic and g(l)={y,y'} is cR-bichromatic. Every physical edge flips cL, so G* is bipartite. At a fixed physical vertex (x,y), two distinct neighbors with the same x-coordinate would represent two ORIGINAL incidences on the same original p and two g(l) labels meeting at y; forbidden by STEP 1. Dually, neighbors with the same y-coordinate would require two ORIGINAL points on the same original l with f(p) labels meeting at x; forbidden by STEP 2. Thus no physical nonbacktracking step can repeat a coordinate two positions later. Bipartiteness forbids repetition at odd distances. In length 3 any coordinate repetition has distance 2 or 3, hence every NB P3 is coordinate-proper. For a simple physical C6, any coordinate repetition has cyclic distance 2,3 or 4; distance 4 is equivalent to distance 2 around the cycle. Thus all C6 coordinate-proper, and by previously proved K1/J11 original provenance gives C6 = D6. This completes G1.

### Caveats

- For s=64 the bound delta*s is substantially below 1, and is not a useful finite minimum-degree statement. Reversible stationary nonbacktracking walks without terminal loss require delta*s>=2, e.g. s>=2,000,000. This is sufficient for an asymptotic all-h theorem; NO W32/W34 experiment verifies the numeric density constant.
- A **bipartite, pair-coherent G*** is guaranteed, but there is no theorem saying its specific collision energy N(E_f+E_g) is below the EICE-001 threshold. An adversarial map can have a G* with theta_I close to 1. Branch A remains OPEN.
- A finite original GQ or full graph with arbitrary pair labels is NOT a proof of the constants; the proof above is analytic.
- Exact physical C6-to-D6 identity relies on complete original incidence provenance, not ordinary graph C6 alone.
- This does not certify all-R3 or any ASET exponent.

## Implementation

- \`research/hyp105_issue230_paired_gstar.py\`: fixed D/D' original-source cherry pruning; deterministic two-side conditional weighted bicoloring; paired incidence peeling; independent provenance/degree/coordinate-proper physical graph checker; exact rational analytic constant evaluator.
- \`research/test_hyp105_issue230_paired_gstar.py\`: genuine complete ORIGINAL W32 four maps and W34 two maps, source-pair provenance, independent min-degree/doubled-diagonal checks, negative artificial cherry and invalid input/path budget tests, and 64..2048 exact-rational symbolic arithmetic sanity checks.
- \`.github/workflows/hyp105-issue230-eice002.yml\`: independent GitHub-hosted ubuntu-latest test and report.

## Next EICE-003 gate

Use the certified construction as a valid base class for the exact EICE-001 original endpoint/interior energy. Investigate *selection* among valid G* by alternative matching/maxcut ties, not merely the deterministic canonical graph; prove or falsify an absolute eta>0 such that one valid G* has 16N(E_f+E_g)<=(1-eta)^2 for all complete f,g, at sufficiently large h. If false, preserve typed original IDs and classify the high-energy collision tensor and alternate C/B original sixsets. NO premature A claim.
