# HYP-105 / issue #230 — D6-AA4-W2-CYC: all-h **uniform-in-f relative variance O(s^-3)**

**Scientific status:** research-only **new scoped conditional theorem**, pending independent mathematical referee. Direct parent [#492 / W-CYC](https://github.com/definitely-stable/Mathlab/pull/492) proves all-h E_g[D6²] <= 30 billion s^12 and only a positive CONSTANT conditional success probability. Earlier [#489](https://github.com/definitely-stable/Mathlab/pull/489) already computed the full true-original W32 21,186² covariance matrix; [#487](https://github.com/definitely-stable/Mathlab/pull/487) already gave the exact all-overlap pair gluing polynomial. The elementary second-moment method is classical. Here the **new point** is the six-original-LINE codegree cap O(d³), enabling an *asymptotically vanishing relative variance* instead of only a constant lower probability. No main changes, no source theorem promotion, no user-per-Q randomness.

## The model and exact quantifiers

For **every** integer h>=3, s=2^h, let W(3,s) be the ACTUAL symplectic generalized quadrangle, V=(s+1)(s²+1) source POINTS and V source LINES, d=s+1 source incidence degree and exactly Vd distinct genuine original incidences. Let a be the MINIMAL integer with K=binom(a,2)>=V and m=K-V<=a-2 missing physical pair images. Fix **ANY** globally injected complete mapping f from true original POINT factors to unordered physical edges of K_a. Sample **ONE** uniform complete globally injected mapping g from the true original LINE factors to the same K_a physical edge alphabet (the image has V elements). This same g is used for EVERY actual source incidence and sixset.

Let Q_f be all sets of six DISTINCT original incidence IDs whose original point factors are six DISTINCT point IDs, whose original line factors are six DISTINCT line IDs, and whose six fixed-f point-physical edges form a simple connected physical six-coordinate C6. For each Q, let X_Q(g) be 1 iff g on the six original line factor IDs makes the physical coordinate column-dual connected C6 IDENTICAL to the fixed-f column-dual on the SAME six original incidence positions. Such a Q is precisely the accepted positive seven-GF(5) **D6** original class; unaligned A/A is NOT counted. Set D=D6(f,g)=sum_(Q in Q_f) X_Q(g), N=|Q_f|, p=(a)_6/(K)_6 and mu=E_g D=Np. The identity and lower bound mu>=s^6/8 were already proved in [#480](https://github.com/definitely-stable/Mathlab/pull/480) (rechecked arithmetically here). No supposed independence between Q events.

### Main theorem

For EVERY h>=3 and EVERY f as above, there is an **explicit computable nonnegative rational epsilon_s, independent of f**, such that

1. **Var_g D / mu² <= epsilon_s <= 1,867,824/a² + 1,399,680/d³ <= 2,333,592/s³.**
2. By Cauchy–Schwarz, **Pr_g(D>0) >= 1/(1+epsilon_s)**.
3. By Chebyshev, **Pr_g(D>=s^6/16) >= max(0,1-4 epsilon_s)**.
4. Consequently D/mu converges in probability to 1, **uniformly in every adversarial fixed complete original point mapping f**, and the failure probability for the nonzero/half-mean event is O(s^-3) as s=2^h grows. The same applies with original point/line roles exchanged by W(3,s) duality.

These results concern **one random global opposite-side map**; they do NOT assert D>0 or S_s(f,g)>=cs^6 for EVERY fixed adversarial pair f,g. Real W32 S68/S72 with D6=0 still exist. No Branch A/B/C of root #230 is accepted.

## Full proof

**1. Uniform number of genuine ORIGINAL left source sixsets.** Every physical undirected C6 in K_a uses exactly six distinct physical pair edges, hence their inverse images under f are six distinct actual original point factors. These six source points each have exactly d *real* original source line neighbors. Greedy choice of six DIFFERENT real original line factors succeeds in at least (d)_6 assignments (the j-th step excludes at most j earlier line factors). An occupied physical C6 determines a unique unordered set of the six original points, so these sets of resulting genuine six original incidence IDs do not overlap between physical C6s. A fixed physical missing edge lies in exactly (a-2)_4 undirected K_a physical C6. Thus, **for EVERY f**,

N >= N_low = [(a)_6/12 - m(a-2)_4] * (d)_6 >0.

For s>=8, a>=35, m<=a-2 implies the bracket is >=(a)_6/24. Monotonicity of (d)_6/d^6 for d>=9 and exact (9)_6/9^6>1/9, combined with (a)_6/a^6 >= 1-15/a >=1/2, gives the convenient **N>=a^6 d^6 /432**. The exact program uses the sharper integer N_low.

**2. Source-LINE codegrees for 1<=r<=5.** Fix a set T of r DISTINCT TRUE original source line factors. In any genuine Q in Q_f containing T, each named source line factor chooses one of its d actual neighboring source point factors. Thus at most d^r choices of r point physical edge images under f; distinctness restrictions only remove choices. The r point physical edges must all lie on some simple physical C6. Such prescribed edges (if admissible) form c>=1 vertex-disjoint paths, c<=min(r,6-r). A classical direct path completion count from predecessor #485 equals

M_(r,c) = 2^(c-1) (5-r)! binom(a-r-c,6-r-c).

If prescribed physical edges branch, form a shorter closed cycle, or reuse endpoints illegally, no such C6 can contain them. For a>=35, simple exact comparison of c cases r=1,...,5 shows M_r=max_c M_(r,c) = (a-r-1)_(5-r) <= a^(5-r). For each resulting physical C6, assign genuine source line neighbors to the remaining 6-r physical point factors in at most d^(6-r) ways. Therefore the number of actual original six-ID Q containing T is **Delta_r <= d^6 M_r**. This is a bound on *sets of REAL ORIGINAL source incidences*, not fake independently redrawable edge labels.

**3. Crucial new r=6 source-LINE codegree improvement.** Fix SIX distinct genuine original source LINE factors l1,...,l6. The union of all their ORIGINAL point neighbor sets has at most 6d distinct original point factors. Since f is globally injective, their images form a simple physical graph H with E(H)<=6d distinct physical pair edges. Every Q containing ALL six lines uses exactly six physical source-point edges from H that form a simple connected physical C6. A simple unoriented C6 has 12 oriented traversals. For each oriented traversal the alternating THREE oriented edges uniquely determine the entire six-cycle: u1-v1-u2-v2-u3-v3-u1. There are at most (2E(H))³ ordered oriented triples. Hence the number of simple physical C6 in H is <= (2E(H))³/12. For each physical C6, the six prescribed named original source line factors can be bijectively assigned to its six actual source point factors in at most 6!=720 ways; each choice determines actual original six-incidence IDs if its genuine source incidences exist, and cannot invent extra incidences. Consequently

**Delta_6 <= 6! * (2*(6d))³/12 = 103,680 d³**.

The elementary fallback Delta_6<=d^6 also holds, so use min(d^6,103680d³). This **improves the predecessor #492 d^6 codegree for sufficiently large d** and is the decisive step needed for vanishing normalized variance. No independence, source GQ automorphism, or global factor label resampling is assumed.

**4. Conditional gluing under ONE full g.** Fix a genuine left-eligible Q and condition on X_Q=1. Its six true original source line factor physical pair images already constitute a physical six-cycle; its remaining original source line factors are uniformly injectively assigned from the K-6 unused physical edges. For a second true Q' sharing exactly r of Q's source original line factors, its shared r right physical edge images are prescribed. For r=1,...,5, at most M_r right physical C6s contain the prescribed edges, and each C6 admits at most 12 bijective cyclic position isomorphisms for the named source line factors. Hence

q_r := Pr(X_Q'=1 | X_Q=1) <= min(1, 12 M_r / (K-6)_(6-r)).

For r=6 use q_6<=1: same-six-line incompatible positional cycles are impossible, and identical ones have X_Q'=X_Q. For r=0 use q_0<=(a)_6/(K-6)_6; this is an upper bound, NOT a claim that two distinct original events are independent. The inequalities hold regardless of shared original POINT factors and agree with the exact cyclic positional kernel from #487.

**5. All ordered true Q×Q pairs.** For fixed first Q and each r>=1, choose r of its six original lines in binom(6,r) ways. The count of second original Q' containing that source-line subset is <=Delta_r. Thus the number of original ordered Q,Q' with EXACT r shared original line IDs is <=binom(6,r)*N*Delta_r; any pairs with larger overlap may be overcounted when bounding these sectors, which is harmless. All zero-overlap ordered pairs are <=N². Expand the square of D from the actual original indicators. With mu=Np,

E[D²]/mu² <= (q0/p) + sum_(r=1)^6 [binom(6,r)*Delta_r/N]*(q_r/p).

Define **epsilon_s** as the preceding RHS minus one, substituting the exact universal N_low, the exact q0 and the source-codegree upper values. Every quantity is an exact nonnegative Fraction, and the computation does NOT enumerate fake high-h symplectic points/lines.

**6. Explicit all-h O(s^-3) certificate.** For s>=8, a>=35, K>=595, K-11>=K/2, a²>=2V>=2s³, K<=a²/2 and d>=s:

- Zero-overlap correction q0/p-1 = (K)_6/(K-6)_6 -1 <=288/a², by (1+12/K)^6 <=1+96/K and K>=a²/3.
- For each r=1,...,5, N>=a^6d^6/432, Delta_r<=d^6a^(5-r), p>=(a^6/2)/K^6, and q_r<=12a^(5-r)/(K/2)^(6-r) yield **binom(6,r)*(Delta_r/N)*(q_r/p) <= 10368 binom(6,r) 2^(6-2r)/a²**. The five explicit integer numerators for r=1..5 are 995,328; 622,080; 207,360; 38,880; 3,888, totaling 1,867,536.
- For r=6, use Delta_6<=103680d³, q_6<=1 and 1/p <=a^6/32, giving **Delta_6/(Np)<=1,399,680/d³**.

Adding the r0 correction yields

**epsilon_s <= (1,867,536+288)/a²+1,399,680/d³ = 1,867,824/a² + 1,399,680/d³ <= 2,333,592/s³.**

This is a symbolic inequality for **every power-of-two h>=3**, not a numerical fitted asymptotic. The exact sharper epsilon_s from the displayed pair-sector formulas is evaluated via big integers/Fractions. It is permissible for coarse bounds to exceed one at small s: probability lower bounds are capped at zero where necessary. By #480, mu>=s^6/8, so D>=mu/2 implies D>=s^6/16. Cauchy–Schwarz and Chebyshev give all stated probabilistic conclusions. Point-line duality gives the opposite fixed-map quantifier order.

## Exact finite certificates and independent falsification

The versioned Python implementation includes physical connected-C6 path-component capacities and the six-source-LINE neighborhood cap, with exact all-h arithmetic. Its independent tests:
- enumerate all real physical C6 in K6/K7/K8 by permutations and compare each subset-of-edges extension count to the formula, including disconnected prescribed paths;
- brute count C6 in several arbitrary physical graphs and verify the oriented-alternating-triple cap;
- enumerate 21,186 true distinct-six-original-incidence candidate Q under each globally fixed S68/S72 point map of ORIGINAL W(3,2) and directly measure source line codegrees for selected 1..6-line subsets; this is a **structural falsifier**, not an s=2 theorem claim;
- compare selected exact two-D6 original source line overlap gluing probabilities from #487 to all sector conditional upper bounds for s=2,4,8,16;
- certify exact rational inequalities for powers h=3..22, including genuine worst-case epsilon_s, the all-h analytic constant and explicit root-proposition false flags.

Reproduce on Python 3.12:

    PYTHONPATH=research python -m unittest discover -s research -p 'test_hyp105_issue230_d6aa4w2cyc_relative_variance.py' -v
    PYTHONPATH=research python research/hyp105_issue230_d6aa4w2cyc_relative_variance.py --h 8

**Finite implication examples from exact arithmetic:** At s=64, epsilon_s<0.1. At s=128, epsilon_s<1/80, so Pr(D>=s^6/16)>=0.95. At s=256, epsilon_s<1/700, giving Pr(D>=s^6/16)>=0.994. These use the sharper exact all-sector certificate, NOT only the coarse 2,333,592/s³ analytic bound; finite numbers do not substitute for the all-h proof.

## Prior art, novelty boundary and acceptance

The second-moment/Cauchy and Chebyshev tools are classical. The graph-theoretic oriented-alternating-edge proof is an elementary extremal cycle upper bound, not independently claimed as a novel abstract graph theorem. Existing probabilistic inequalities such as Janson-type dependency-graph bounds assume particular independence/dependency structures and cannot be applied blindly to a uniform **injective** global permutation map; see [Janson and Warnke 2016](https://doi.org/10.1002/rsa.20590) and [Janson–Kurauskas 2023](https://doi.org/10.37236/11618). The research-specific result lies in counting **genuine original W(3,s) incidence-sixset source-LINE codegrees** with correlated physical permutations and showing a uniform relative variance that vanishes. No independent prior-art novelty review or mathematical peer approval has occurred.

**Crucial logical non-implication:** The original #230 demands inf_(f,g) S_s(f,g)>=c s^6 for EVERY **deterministic correlated** f,g, or a rigorous infinite o(s^6) counterfamily, or a fully scoped C reduction. A probability tending one over random g for each f permits a small exceptional set of adversarial global g, so it does NOT close any of those gates. W32 fixed S68/S72 D6=0 provides a concrete model-scope warning. Do not merge research Draft before exact HEAD dedicated/Research/Proof Audit and independent proof review; do not promote scientific claim registry or close #230.
