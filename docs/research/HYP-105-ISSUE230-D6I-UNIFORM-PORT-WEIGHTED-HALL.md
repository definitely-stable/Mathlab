# HYP-105 issue #230 — D6-I: exact weighted Hall dual for uniform original-incidence ports

**2026-10-13. RESTRICTED_THEOREM_C — new exact ALL-finite / ALL-h restriction equivalence. Root A/B OPEN.**

Base: [D6-H Draft #407](https://github.com/definitely-stable/Mathlab/pull/407), pinned fully green parent `9aa186a421e8890aecdc384fde6c3ae73d106c9a`; strictly stacked. This step makes the original accepted sixset-to-incidence *uniform rational K/6 budget* mathematically explicit. It does **not** show that any fixed K suffices for every original correlated global f,g.

## 1. General exact restricted weighted-Hall theorem

Let I be any finite universe of **ORIGINAL** incidence IDs; T distinct 3-subsets with positive integer oriented source multiplicity w(T); A a set of genuinely accepted positive ORIGINAL 6-subsets Q from the **same** complete f,g in applications; K a nonnegative integer. Define:

    C = sum_T w(T),
    d_A(e) = |{Q in A: e in Q}|,
    M(F) = sum_{T subset F} w(T),
    D(F) = sum_{e in F} d_A(e)
         = sum_{Q in A}|Q intersect F|.

The D6-H **uniform** restricted rational transport reserves exactly K/6 recipient slots at EACH of six distinct incidences in every accepted Q. It routes a path using T to exactly ONE of the three incidence ports e in T, consuming that original incidence's aggregate capacity c(e)=K d_A(e)/6. This is a conservative recipient-slot allocation: the full original D6-D model may route additional paths by reallocating a recipient's six slots adaptively.

Multiply all rational capacities by 6 and define a finite integral maxflow network:

    source -[6w(T)]-> T -[6C+1]-> e -[K d_A(e)]-> sink.

Every T-e arc exists iff e in T. Let V6 be maxflow, Delta6=6C-V6.

**THEOREM (exact weighted Hall + source closure for restricted uniform ports).** The following are equivalent:

1. This UNIFORM rational port network routes all original oriented demand C.
2. For every subset U of source triples,

       6 * sum_{T in U}w(T) <= K * sum_{e in union(U)} d_A(e).

3. For every **source-closed** support F=union_{T subset F} T,

       6*M(F) <= K*D(F).

Moreover, for EVERY finite I,T,A,w,K, including all GQ orders and arbitrary complete globally injective original f,g,

    Delta6 = max_{U subset source} (6 sum_{T in U}w(T) - K D(union(U)))_+
           = max_{source-closed F}(6 M(F) - K D(F))_+.

**Proof.** The finite integral bipartite T-e network is precisely the adjacency of source triples to their three ORIGINAL incidence ports; capacities Kd_A(e) are shared port capacities. By maxflow/mincut, after multiplying source demands by six, an s-t cut can be formed from any source set U and all its incidence neighbors union(U); its capacity is 6(C-M(U))+K D(union(U)). Since the middle arcs have finite sentinel capacity 6C+1, which strictly exceeds the trivial 6C cut, no minimum cut crosses one. Conversely every minimum cut has this form. Source-closure U_F={T:T subset F} increases M while preserving the source-incidence union F, so its Hall deficit is >= that of U. In the canonical source-side reachable residual cut, source-closure holds and all equations are exact. The maximum cut deficit equality follows immediately.

**Important:** D(F) counts ORIGINAL positive sixset-to-incidence membership with multiplicity; it is not the accepted positive recipient count B(F)=|{Q:Q meets F}|. Indeed

    B(F) <= D(F) <= 6*B(F).

Thus the restricted uniform condition 6M(F)<=K D(F) is generally STRICTER than full D6-D Hall M(F)<=K B(F). Do not misidentify the two and do not substitute incomplete BB-only recipient pools for full S.

## 2. Exact compensation and minimum restricted K

D6-H's rational slot-extension theorem embeds this restricted flow in full original T-e-Q transport. The full network has integer demands and capacities. Therefore its maximum integral routed mass is at least ceil(V6/6), and the exact full D6-F minimum integer exception satisfies

    D_K <= C-ceil(V6/6) = floor(Delta6/6).

The floor is essential. For one source T={0,1,2} of weight N and one accepted Q touching T only at e=0, with K=6N-1, the uniform port network has Delta6=1, while full D6-D can route ALL N units because K>=N. Thus D_K=0 despite a positive uniform rational deficit.

If EVERY source triple shares at least one ORIGINAL incidence with accepted A, the restricted minimum complete-flow integer capacity is finite and obeys

    K_min_uniform = max_{source-closed F, M(F)>0}
                       ceil(6 M(F)/D(F)) <= 6C,

with exact integer arithmetic and zero-denominator fail-closed validation. If any true source triple has d_A(e)=0 at all its incidences, no finite K works. In all cases

    K_min_full_original <= K_min_uniform.

**NEW ANALYTIC TARGET (still OPEN):** derive a fixed K and eta>0 such that for the actual high-h PR #394 coherent H and same full original global f,g,

    max_F (6 M_H(F)-K D_A(F))_+
       <= 6*(16-eta)*s^6 + o(s^6)

for ALL original source-closed F, uniformly over correlated f,g. Then D_K<=(16-eta)s^6+o(s^6), and the accepted PR394 path reservoir inequality conditionally yields

    S_s >= (eta/(K+2)-o(1))*s^6.

The stronger condition Delta6=o(s^6) would provide coefficient 16/(K+2). D6-I proves the general reduction and exact finite oracle, **not** these all-h geometry inequalities.

## 3. Exact independent audit and intentional falsifiers

- [Algorithm](../../research/hyp105_issue230_d6i_uniform_port_hall.py): independent build of the T-e scaled residual graph; reconstructs the full ORIGINAL source-closed F and independently recomputes M, D, E/I split and Delta6=6M-KD=6C-V6. Integer-only K threshold and exact minimum uniform K with no floating-point ceil.
- [Tests](../../research/test_hyp105_issue230_d6i_uniform_port_hall.py): every one of 2^n source subsets on deterministic random synthetic instances, compared against the mincut oracle and prior D6-H; independent direct ratio for minimum K; irreducible unsupported true source; inert incidence IDs; endpoint+internal partition; arbitrary-precision 10^80; precise floor-vs-ceil counterexample; four genuine W32 same-map COMPLETE seven-positive target families with independent D6-F exact comparison.
- [Hosted contract](../../.github/workflows/hyp105-issue230-d6i-uniform-port-hall.yml): all tests plus JSON fail-closed checks on exact true-original finite counts, no all-h conclusive claims.

The previous finite W32 exact full-original K values are (lex 4, reverse 6, S68 9, S72 10). Previous D6-H found uniform restricted zero-exception at these capacities and matching exact D6-F exceptions at K-1; D6-I explicitly recomputes the restricted mincut and verifies its own minimum K. This is FINITE EVIDENCE, never a uniform K proof.

## 4. Hosted true-original W32 restricted Hall cut result

The first [GitHub-hosted D6-I Contract #38357406426](https://github.com/definitely-stable/Mathlab/actions/runs/38357406426) completed SUCCESS: five dedicated test methods, including 72 deterministic independent enumerations of all source subsets at five K each (360 exact Hall-dual falsifier comparisons), arbitrary 10^80-weight integer tests, and full original W32 true seven-family checks.

| Complete TRUE ORIGINAL W32 f,g | C=E+I | Complete S | Exact D6-D min K | Uniform D6-I min K | D6-F exception at K-1 | Uniform cut F at K-1 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| lex | 942 | 259 | 4 | **4** | 165 | All 45 original incidences |
| reverse | 898 | 169 | 6 | **6** | 53 | All 45 original incidences |
| S68 | 606 | 68 | 9 | **9** | 62 | All 45 original incidences |
| S72 | 658 | 72 | 10 | **10** | 10 | All 45 original incidences |

In these four *finite true ORIGINAL* models, the scaled uniform-port cut at K-1 is exactly 6(C-(K-1)S), with full support F={0,...,44} and D(F)=6S. The restricted uniform capacity K matches the full original minimum K on those instances. This establishes **no** all-h local expansion: the extremal finite witness was global, and the complete seven-positive family for s>=4 is still unknown. The original PR394 high-h coherently pruned H is a different asymptotic object from full-G W32.

## 5. Non-claims and next proof gate

- Not a proof of full original seven-class lower bound S=Omega(s^6), Branch A, or infinite Branch B counterfamily.
- Not a proof of all-h map-independent uniform K or all-h small restricted Hall deficit.
- Not an enumeration of W34/W38 full seven-positive GF5 original sixsets.
- Not an inference from the tiny-s literal PR394 cleaned H, which may be empty.
- Not a proof of full GF5 risk upper, ASET exponent, or any general weighted ASET impossibility.

**Next candidate D6-J:** exploit genuine symplectic GQ incidence identities and positive GF5 sevenset geometry to bound d_A(e) on collectively overloaded incidence supports F, with explicit endpoint-only E and internal-only I contributions; alternatively construct an infinite coherent adversarial f,g showing this sufficient *uniform-port* inequality cannot hold with fixed K. This falsifies only the restricted route, not the original full Hall/Branch A. Maintain Draft PR, independent external math review open, and untouched main.
