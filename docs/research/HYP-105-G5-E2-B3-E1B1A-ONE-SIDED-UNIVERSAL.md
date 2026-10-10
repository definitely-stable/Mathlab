# HYP-105 B3.2-E1-B1A — uniform one-sided six-column mass for EVERY pair injection

Date: 2026-10-10. Scope [#230](https://github.com/definitely-stable/Mathlab/issues/230), parent [#176](https://github.com/definitely-stable/Mathlab/issues/176). Independent of pending E1-B0 [#233](https://github.com/definitely-stable/Mathlab/pull/233) implementation.

**PROVED (elementary edge-transitive double counting):** for every h>=1 and every injection of the V=(s+1)(s²+1) left factor vertices into the K=binom(a,2) physical pair labels, with s=2^h, a=min{n:binom(n,2)>=V}, the count of distinct ORIGINAL six-incidence subsets whose LEFT physical projection uses EXACTLY six coordinates of degree two has the uniform asymptotic

```text
L_s(f) = (151/144 + O(1/s)) s^15
```

where the error is uniform in f. More precisely, explicit finite-h integer bounds below apply to every f and to any simple Δ-regular bipartite factor incidence host with Δ=s+1. This is a **one-sided** result. It does NOT prove an all-label lower for the seven TWO-sided families S_s(f,g), strict R3 power, or improved ASET exponent. The proof is a classical double-counting/union-bound argument; the contribution is its correct model specialization and exact finite-h falsifier, not originality over known extremal graph combinatorics.

## 1. Precise frozen combinatorial model

Let H_f be the simple physical graph with vertex set [a] and edge set {f(p): p in P_s}. Because f is injective, H_f has V edges and omits exactly t=K-V edges of the complete K_a; minimality of a gives 0<=t<a. Every left factor vertex has Δ incident ORIGINAL factor-incidence columns (one for each of its Δ distinct GQ line neighbors).

Count UNORDERED subsets E' of exactly SIX distinct ORIGINAL incidences, not balanced sign patterns. Every physical coordinate appearing in the LEFT projection has degree at least 2; we RESTRICT to exactly six touched left coordinates, so all six have degree exactly 2. Classify E' by original LEFT factor multiplicity, as previously accepted:

- A: six distinct original factor points. Their six distinct physical pair edges form a SIMPLE 2-factor of K6: C6 or C3⊔C3. Every realized physical 2-factor yields **Δ^6** distinct original six-incidence subsets.
- B: one original factor point appears twice, four other points once. Its physical pair edge is doubled; four other distinct pair labels form a C4 on the remaining four coordinates. Every realized physical template yields **binom(Δ,2) Δ^4** distinct original six-incidence subsets.
- C: three distinct original factor points each appear twice. Three physical pair edges are disjoint and form a perfect matching of six coordinates. Every realized physical template yields **binom(Δ,2)^3** distinct original six-incidence subsets.

These are the ONLY original factor multiplicity patterns for a six-coordinate degree-two LEFT projection under an injective pair labeling: multiplicity >=3 at a factor would make its two coordinate degrees >=3, impossible; six original columns force A/B/C.

For every six-element physical coordinate subset, the FULL K_a contains precisely 70 A 2-factors (60 simple C6, 10 C3⊔C3), 45 B patterns (15 repeated pairs × three C4 choices), and 15 C perfect matchings. Thus for k∈{A,B,C}, full pattern count F_k(a)=c_k binom(a,6) with c=(70,45,15). Each pattern uses respectively e=(6,5,3) DISTINCT physical edges; B's repeated edge counts ONCE in the missing-label exclusion.

## 2. Main theorem: exact finite-h bounds for every injection

**Theorem E1-B1A (universal one-sided physical template sandwich).** Let G⊆K_a be ANY graph with exactly V edges, K=binom(a,2), t=K-V omitted edges. Write N_k(G) for its physical A/B/C six-coordinate patterns. Then for k=A,B,C,

```text
max{0, F_k(a) - t * e_k * F_k(a)/K} <= N_k(G) <= F_k(a).
```

The ratio e_k F_k/K is ALWAYS integer: each edge of K_a participates in the same number of full templates of type k, because the complete graph's vertex-permutation group acts transitively on physical edges; double-counting (edge,template) incidences counts e_k F_k. Every missing physical edge deletes at most that many templates; the union bound handles overlaps conservatively. No independence, pseudorandomness, GQ automorphism assumption, expander mixing or algebraic properties of f are needed.

Multiplying by the EXACT original-incidence lift multiplicities gives integer bounds

```text
L_k^- = max(0,F_k - t*e_k*F_k/K) * λ_k
           <= L_k(f) <= F_k * λ_k = L_k^+;
λ_A=Δ^6; λ_B=binom(Δ,2)Δ^4; λ_C=binom(Δ,2)^3.

L_s^-=Σ_k L_k^- <= L_s(f) <= Σ_k L_k^+=L_s^+.
```

**Proof that physical templates lift uniquely:** after choosing the distinct left factor vertices defined by physical pair labels, each singleton factor contributes one of its Δ original incidence edges and each doubled factor contributes a two-element subset of its Δ edges. Distinct factor vertices cannot contribute an identical original incidence (the left endpoint would differ); inside one factor the chosen edges are distinct. Conversely, an unordered original incidence six-set uniquely reconstructs the occupied factor pair labels, their multiplicities and its chosen original incidences. Thus no 6! division or physical-coordinate automorphism correction is permitted here.

For G=K6 and Δ=3 (W(3,2)), the formulas give exactly

```text
L_A=70*3^6=51,030;
L_B=45*binom(3,2)*3^4=10,935;
L_C=15*binom(3,2)^3=405;
L_s=62,370.
```

This independently reproduces the accepted exhaustive E1-A original-incidence LEFT candidate census, and the current tests independently scan all 70+45+15 K6 physical patterns at s=2 and both clustered/disjoint six-missing-edge K14 graphs at s=4.

## 3. All-h uniform asymptotic and exact obstruction reduction

For s=2^h→∞, the host GQ parameters imply V=s^3(1+O(1/s)), Δ=s(1+O(1/s)), a=√(2V)(1+O(V^-1/2)), K/V→1, and t/K≤2/a=O(s^-3/2). Consequently the full template bounds and omitted-edge union bounds have the SAME leading terms uniformly in f:

```text
L_A(f)=(7/9+O(1/s))s^15,
L_B(f)=(1/4+O(1/s))s^15,
L_C(f)=(1/48+O(1/s))s^15,
TOTAL L_s(f)=(151/144+O(1/s))s^15.
```

**Corollary E1-B1A-R (precise missing right-side transfer).** Let S_s(f,g) be the previously accepted sum of all seven disjoint positive two-sided six-motif classes (the #230 target); every counted sixset is among the L_s(f) left candidates, so 0≤S_s(f,g)≤L_s(f). Define the exact deterministic *right-pass fraction* T_s(f,g)=S_s(f,g)/L_s(f) (L_s(f)>0 for s=2^h). Then

```text
[∀ admissible f_s,g_s: S_s(f_s,g_s) = Ω(s^6)]
  iff
[∀ admissible f_s,g_s: T_s(f_s,g_s) = Ω(s^-9)]
```

in the usual sense that a uniform absolute positive constant works for all sufficiently large s and **all** injections at that s. This equivalence follows solely from L_s(f)=Θ(s^15) with *uniform* constants; it is NOT a proof of either statement. A counterexample sequence with S_s=o(s^6) is likewise equivalent to T_s=o(s^-9) for that same sequence, but such a sequence has NOT been constructed.

Interpretation: we have now ruled out *left-side sparsity* as a possible all-h explanation for S_s=o(s^6). The unresolved possibility is simultaneous suppression by the RIGHT map g of the accepted seven-family configurations among Θ(s^15) left candidates. On s=2 the previously accepted E1-B0 structural controls give lex T=259/62370 and reverse-line T=169/62370; these are merely finite controls, not asymptotic evidence.

If future work tries to apply Sidorenko, rainbow-cycle, expander mixing or a tensor inequality to force the transfer, it MUST explicitly prove a lower bound on this two-sided T (or the correspondingly weighted signed GF5 quantity) uniformly across arbitrary correlated f,g. The full-GF5 risk still contains other positive four/six-coordinate classes, so S_s=o(s^6) alone never proves R3=o(s^6).

## 4. Code, independent falsifiers and acceptance

[Reference implementation](../../research/hyp105_g5e2b3e1b1a_one_sided.py) uses exact Python integers for GQ parameters, full-template counts, per-missing-edge counts, nonnegative sandwich, original-incidence lift and all-h normalized output. [Independent tests](../../research/test_hyp105_g5e2b3e1b1a_one_sided.py) enumerate every physical A/B/C pattern of K6 and two inequivalent missing-six-edge K14 graphs (not samples), check exact original incidence W32 counts against accepted E1-A, check transitive deletion coefficients across s=2..256, and validate asymptotic normalizations at s=128,256,1024.

This is an elementary/combinatorial **partial theorem**, not a universal two-sided lower, not a new R2 or R3 upper, not a novel GF5 cancellation construction, and does not close #230, #176 or the ASET exponent gap. Only GitHub-hosted runners. Merge gated by exact-head full Research SUCCESS and separate postmerge CI.
