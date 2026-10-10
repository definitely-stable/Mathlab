# HYP-105 B3.2-E1-C20 — unavoidable globally compatible LEFT six-cycle source

2026-10-11. Parent theorem issue [#230](https://github.com/definitely-stable/Mathlab/issues/230). Scientific lineage C16 #305 → C17 #308 → C18 #310 → C19 #312 → C20. Parallel fully hosted C16 CI #306 and C19 CI #314 remain separate, not silently merged or taken as exact-head evidence of C20.

**RESULT: POSITIVE ALL-h LOWER FOR ORIGINAL LEFT-PROJECTION A-SOURCE ONLY. NOT AN ALL-h LOWER FOR SAME-(f,g) SEVEN S OR GF5.** This is the first scalar lower after C18/C19's no-go that genuinely quantifies a ONE GLOBAL LEFT injection over all original factor points without treating independently sabotaged local blocks as compatible.

## 1. The fully quantified all-h theorem

For EVERY h>=1, s=2^h, let W(3,s) be the true original GQ incidence graph. It has V=(s+1)(s²+1) original factor points, exactly s+1 original lines through each point, and V original lines. Set

    a = min { n : C(n,2) >= V },
    t = C(a,2)-V.

Let F⊆E(K_a) be ANY arbitrary occupied physical pair-edge set of exactly V edges (not necessarily the whole K_a). Let f: original points → F be ANY bijection, i.e. ONE globally compatible physical-left assignment for EVERY original point. The admissible right alphabet, right injection g and any original right correlations play NO role in this left-only theorem.

Let N_left,A(f) count DISTINCT ORIGINAL six-incidence sets J whose physical LEFT projection is a **single simple physical six-cycle C6** on six distinct physical coordinates and six distinct original points (the type-A original support), with one original incidence selected at each of those six original points.

**C20 theorem:**

    N_left,A(f) >= [60 C(a,6) - 24 t C(a-2,4)] (s+1)^6 > 0

for EVERY such globally compatible f,F and EVERY h>=1. In fact the right side is Omega(s^15). The stronger, exactly defined identity is N_left,A(f)= C6(F)*(s+1)^6, since each original point has exactly s+1 original incidence choices.

Proof:
1. A complete K_a has exactly 60*C(a,6) unoriented simple six-cycles: for each 6-subset, the number of Hamiltonian undirected cycles is (6−1)!/2=60.
2. ONE fixed physical pair-edge e belongs to exactly 24*C(a−2,4) such six-cycles: choose the other four coordinates and note exactly 24 of 60 6-cycles on those vertices contain e.
3. Removing t arbitrary physical edges destroys AT MOST the sum of individual incident cycle counts; cycles containing multiple missing edges are overcounted in this subtraction, which is conservative. Therefore C6(F)>=60*C(a,6)−24t*C(a−2,4).
4. Each surviving physical six-cycle contains six DISTINCT physical pair-edge labels. The bijection f maps these to six distinct ORIGINAL W(3,s) factor points. Independently choose one among the s+1 distinct ORIGINAL incident lines through each point. Every six-tuple generates exactly one distinct ORIGINAL six-incidence set, so yields (s+1)^6 sets. Different physical cycles use different sets of six physical edges, so cannot generate the same ORIGINAL J.
5. Minimality of a gives 0<=t<a−1. For s=2, (V,a,t)=(15,6,0), and C6 lower is exactly 60. For s>=4, a>=14 and

    60 C(a,6)-24t C(a−2,4)
      = [2 a(a−1)−24t] C(a−2,4)
      >= [2a(a−1)−24(a−2)] C(a−2,4) > 0.

The positivity is an **all-h integer algebraic theorem**, not extrapolation from W32. Since a=Theta(s^(3/2)), t=O(a), the number of C6(F) is Omega(a^6)=Omega(s^9); multiply by (s+1)^6 to obtain Omega(s^15).

## 2. Why this defeats the misleading local sabotage transfer

C18 and C19 allow separately minimizing witness blocks, each with its own locally chosen left injection into an occupied physical star or double-star. Such independently chosen assignments need NOT fit into a COMMON global f. C20 instead accounts for ONE SINGLE occupied F and bijection f of all original points, and counts the unavoidable complete global C6 population. Each right g can independently affect acceptance, but it cannot make these ORIGINAL left-projected C6 candidate sets disappear from the source.

This is a true globally compatible positive LEFT obstruction to annihilating all left projected witnesses, not yet a bound on simultaneously accepted left/right seven-class witnesses. A left A-source candidate may be REJECTED by the right projection, or (for A/A) by the strict matching-dependent D6 classifier. Therefore it would be INVALID to assert S_seven(f,g)>=the stated left count. Nor does it give a positive GF5 R3 lower or strict upper or new ASET exponent.

## 3. Exact bounded finite oracles, genuine ORIGINAL GQ incidence

Executable: research/hyp105_g5e2b3e1c20_global_left_c6.py
Independent tests: research/test_hyp105_g5e2b3e1c20_global_left_c6.py
GitHub-hosted Contract: .github/workflows/hyp105-c20-contract.yml

- Exact integer a,V,t and analytic C6/A-source lower for s=2,4,8,16,32,64,128; input rejects non-powers of two and fake physical models. At s=2 lower 60*3^6=43,740 original A source sets.
- At s=4, V=85, a=14, t=6. The deletion bound is 108,900 SIX-CYCLES and 108900*5^6=1,701,562,500 distinct ORIGINAL A-left candidate sets, without claiming that GF4 original incidence has been enumerated in code.
- An independent exact small-host enumerator constructs each undirected simple physical six-cycle only once by canonical smallest-start/reversal ordering, and directly validates the cycle-deletion multiplicity for K6, K7 and K8.
- Four distinct incomplete occupied GF4 physical K14 edge sets (six missing edges: lex, reverse lex, star and matching) test actual C6 counts >=108,900, independently of the formal union bound.
- Genuine W(3,2) original 45-incidence oracle: the accepted historical selected_left_six enumerator has exactly 62,370 distinct original left-projected sixsets, of which 51,030 are original-left A. The NEW independent Hamilton C6×3^6 expansion produces exactly 43,740 original sixsets; every one must occur in the old A source. The other 7,290 original A candidates arise from two disconnected physical 3-cycles (two triangles). This is checked for both 'lex' and 'reverse-line' physical models, each before and after a nontrivial swap of two ORIGINAL source-point physical pair-edge images.
- Any truncated or mis-shapen physical K_a set, duplicated pair edge, reversed edge or too-large exact cycle graph fails closed. Dedicated exact-head GitHub-hosted contract and full Research required; no self-hosted runners, no main changes.

## 4. Next all-h research gate — accepted right-seven transfer

C20 gives an explicit large pool of globally unavoidable true original LEFT A motifs. The unresolved main #230 question is whether ANY adversarial global original-right injection g can reject ALL BUT o(s^6) of them while simultaneously choosing the other accepted source classes. This must be studied with genuine ORIGINAL GQ right multiplicities, one globally compatible g, and the exact D6 coupling rule. Naive random-right expectation alone does NOT lower-bound an adversarial minimum; independent local right minimization may again have a zero floor. The next C21 must quantify a right-transfer/failure certificate or a rigorous counterexample to such a transfer, retaining the C18/C19 star adversaries and the same ORIGINAL six-incidence identity discipline.

Issue #230 remains **OPEN_WITH_FORMAL_BLOCKER**. No branch A all-h S positive result, branch B globally correlated low-S family, or equivalent-model C proof is claimed by C20.
