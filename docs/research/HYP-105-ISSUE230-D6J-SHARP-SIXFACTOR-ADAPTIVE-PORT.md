# HYP-105 issue #230 — D6-J: sharp factor-six equivalence and optimal adaptive original-incidence port allocations

**2026-10-13. NEW RESTRICTED_THEOREM_C. Root Branch A/B OPEN; not a positive-sixset asymptotic lower bound.**

Stacked strictly above [D6-I Draft #408](https://github.com/definitely-stable/Mathlab/pull/408) HEAD `b3c4a5300d08457018c845b89242498bd5102d5c`, without merging or changing main. The D6-I parent was certified by the dedicated original-port Hall Contract and INDEX/Proof Audit; final whole-research CI is an independent required check.

## 1. Exact ALL-h six-factor comparison

Fix ANY finite incidence universe and integer weighted ORIGINAL source triples T (blocked oriented proper physical P3, including BOTH endpoint E and internal-only I contributions), genuine accepted ORIGINAL sixsets Q, and nonnegative integer K. A path with source T may be assigned to a positive recipient Q ONLY through one common ORIGINAL incidence e in T ∩ Q. The recipient receives a TOTAL of at most K, shared across all its six ports.

Let V_full(K) be the full exact integer flow from D6-D/D6-F on

    source -> T -> e -> Q -> sink,

with source arc w(T) and Q->sink capacity K. Let V6(k) be the D6-I INTEGER source-to-T-to-e flow with source 6w(T) and original incidence port capacity k*d_A(e), d_A(e)=number of original positive Q containing e. Define C=sum_T w(T) and the (integer) uniform exception certificate U(k)=floor((6C - V6(k))/6).

**Theorem (universal sharp six-factor sandwich):**

    V6(K) <= 6 V_full(K) <= V6(6K).

Equivalently, denoting D_full(K)=C-V_full(K), the **exact original minimum integer exception budget**,

    U(6K) <= D_full(K) <= U(K).

The right inequality is D6-H/D6-I's uniform slot embedding. The left is NEW: take an optimal integer full original flow, decompose each T->e->Q assignment. The total incoming demand at any original incidence e is <=K*d_A(e), since every Q incident to e carries <=K in total. Multiplying all T->e arcs of that flow by six, the uniform network with k=6K has incidence capacity 6K*d_A(e) and source capacity 6w(T), so it can carry at least 6V_full(K). Thus floor(C-V6(6K)/6)<=C-V_full(K). These inequalities include all integer/zero-capacity/unsupported cases and require no geometry-specific equidistribution conjecture.

**Capacity theorem:** if C>0 and every true source T touches at least one accepted original Q (the same support criterion for both full and uniform models), then both minimum *zero-exception* integer capacities exist and

    K_full <= K_uniform <= 6*K_full.

If an original source T has no positive recipient sharing any incidence, **neither** scheme has finite zero-exception K. For an empty source, there is no positive capacity inference.

**Factor 6 is SHARP.** Set one source T={0,1,2}, w(T)=N, and one accepted Q={0,3,4,5,6,7}. The full network uses the single shared original incidence e=0 and has K_full=N. The uniform budget reserves only K/6 at e=0 and must have K_uniform=6N. No c<6 can replace the constant for arbitrary finite incidence data. Such a synthetic construction does NOT establish it occurs in real coherent original W(3,s) labelings at large h.

## 2. Exact adaptive port allocation — no relaxation gap

For any full original maxflow, define

    a(Q,e) = amount of flow on edge e -> Q (an INTEGER).

Then a(Q,e)>=0 is supported only on e in Q, and for each accepted sixset

    sum_{e in Q} a(Q,e) = flow(Q->sink) <= K.

Set c(e)=sum_{Q contains e}a(Q,e). The *restricted* source->T->e->sink network with these (adaptive, generally very nonuniform) capacities can reproduce all the full original T->e flow. Conversely any feasible rational/real slot allocation and restricted flow extends to the full T->e->Q graph. Therefore

    max_{valid adaptive allocations a} V_restricted(a) = V_full(K).

Importantly, the maximizing allocation can be chosen INTEGER, not merely rational. The implementation explicitly extracts the optimal recipient-to-incidence slot table and original source-to-incidence assignment, checks port conservation and K budgets, and independently recomputes the reduced network optimal flow. Thus D6-H's general adaptive sufficient bound is ACTUALLY EXACT when a is optimized, although there is no known map-independent all-h bound on that optimum.

This establishes the sharp logical relationship between restricted D6-I and full D6-D, not a new bound on the true seven-positive S_s.

## 3. ALL-h analytic consequence, conditional on external GQ work

For arbitrary sequences of coherent original f,g and actual PR394 coherently retained H, the following existential notions of *bounded capacity with small exceptions* are equivalent up to a factor six in K:

- There EXISTS an absolute integer K0 with full original D_full(K0)=o(s^6) uniformly over all such maps.
- There EXISTS an absolute integer K1 with restricted uniform U(K1)=o(s^6) uniformly over all such maps.

Indeed the first implies U(6K0)<=D_full(K0)=o(s^6); the second implies D_full(K1)<=U(K1)=o(s^6).

For *zero exceptions*, K_uniform<=6K_full means a map-independent full bounded-congestion theorem would imply a map-independent bounded-uniform-port theorem and vice versa. The factor six may still cost a factor six in the coefficient 16/(K+2) of any subsequent PR394 inequality; thus it is an existence equivalence, NOT coefficient preservation.

No uniform bounded K, no o(s^6) exception bound, no actual GQ positive port-degree lower bound and no Ω(s^6) Branch A proof is obtained in D6-J. The next stage D6-K should probe the **real** ORIGINAL positive boundary vs source demand (or falsify a restricted port assumption) with geometric GQ identities and globally coherent injective labelings; simply reformulating maxflow again is not productive.

## 4. True-original complete-seven W32 finite pinned evidence

The initial GitHub-hosted [D6-J Contract #38358961078](https://github.com/definitely-stable/Mathlab/actions/runs/38358961078) succeeded with 5/5 test methods and 192 independent small-system exhaustive comparisons. The full original flow was independently reconstructed as integer positive-sixset Q-to-original incidence e slots, with exactly conserved endpoint/internal joint source mass.

| Genuine globally coherent W32 mapping | Original C=E+I | Complete accepted S | K_full | K_uniform | Exact FULL exception at K-1 | Nonzero optimal adaptive Q-to-e pairs at K |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| lex | 942 | 259 | 4 | 4 | 165 | 253 |
| reverse | 898 | 169 | 6 | 6 | 53 | 167 |
| S68 | 606 | 68 | 9 | 9 | 62 | 105 |
| S72 | 658 | 72 | 10 | 10 | 10 | 103 |

At K_full, original exception, uniform upper U(K), and uniform lower U(6K) all vanish. At K_full-1, the original exact exception agrees with the UNIFORM upper U(K-1), while U(6(K-1))=0. The new PR assertions pin these *nonzero-exception* cases and verify the adaptive reduced network routes exactly C-D_full(K-1) original paths. No W34 full-seven S or s-growth extrapolation is claimed.

## 5. Engineering and independent falsification

- [Implementation](../../research/hyp105_issue230_d6j_sixfactor_adaptive_port.py): full original integer-flow reconstruction from residual arcs, typed original Q/e/T slot assignments, explicit conservation of Q budgets and shared endpoint/internal demand; adaptive reduced-network recheck, both six-factor inequalities and exact capacity frontier. Fails closed on every inconsistency.
- [Tests](../../research/test_hyp105_issue230_d6j_sixfactor_adaptive_port.py): 48 deterministic non-geometric finite systems and four K each checked against an INDEPENDENT unit-by-unit combinatorial exhaustive assignment (192 tests), sharp 6N/N singleton overlap, large 5-recipient example, unsupported and empty cases, explicit E+I sharing, and four genuine true original W32 globally coherent complete seven-positive GF5 maps.
- [GitHub-hosted contract](../../.github/workflows/hyp105-issue230-d6j-sixfactor-adaptive-port.yml): single dedicated contract on Ubuntu + Python 3.12 with 5 unittest methods and fail-closed true-W32 complete-seven JSON counts. INDEX, Proof Audit and Research are distinct repository-wide checks.

True complete-seven positive ORIGINAL recipient families for W34/W38 are not available; the synchronized BB-overlap subclass is NOT a substitute for the full-seven S. The literal high-h PR394 retained graph H may be empty at tiny s. Root #230, #176, #169 OPEN, PR Draft, main unchanged. External mathematical peer review remains independent of CI.
