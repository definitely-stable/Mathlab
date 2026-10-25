"""HYP-105 Option 1: Multiplicity and Spectral Correlation Investigation on W(3,4).

Standard-library only implementation:
1. Exact mapping from source GQ 3-paths to physical 3-walks in H.
2. Distribution of N_3(u, v) across physical vertex pairs in H.
3. Global N_3 statistics: mean, std, max, sum N_3^2 (Tr A_H^6).
4. Exact census breakdown and blocked ratio.
"""
import collections
import math

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model


def analyze_model_multiplicity(closure, name="model"):
    c = closure
    a = c.a
    n = a * a
    adj = [set(nbr for nbr, _ in c.adj[i]) for i in range(n)]

    # Compute A_H^3
    c3 = [collections.Counter() for _ in range(n)]
    for u in range(n):
        c1 = collections.Counter(adj[u])
        c2 = collections.Counter()
        for w1, k1 in c1.items():
            for w2 in adj[w1]:
                c2[w2] += k1
        for w2, k2 in c2.items():
            for w3 in adj[w2]:
                c3[u][w3] += k2

    census = c.census()

    all_n3 = []
    for u in range(n):
        for v in range(n):
            if u != v:
                all_n3.append(c3[u][v])

    n_pairs = len(all_n3)
    mean_all = sum(all_n3) / n_pairs
    var_all = sum((x - mean_all) ** 2 for x in all_n3) / n_pairs
    std_all = math.sqrt(var_all)
    max_all = max(all_n3)
    sum_sq = sum(x * x for x in all_n3)

    return {
        "name": name,
        "s": c.s,
        "a": a,
        "n_vertices": n,
        "mean_N3": mean_all,
        "std_N3": std_all,
        "max_N3": max_all,
        "sum_N3_sq": sum_sq,
        "census_proper_P3": census["proper_P3"],
        "census_blocked": census["blocked"],
        "census_unblocked": census["unblocked"],
        "census_bbo": census["synchronized_BBo"],
        "blocked_ratio": census["blocked"] / (census["blocked"] + census["unblocked"]),
    }


def run_option1_audit():
    print("=== HYP-105 OPTION 1: MULTIPLICITY & CORRELATION AUDIT ===")
    for s_val, model_name in [(2, "lex"), (2, "random")]:
        m = fixture(s_val, model_name)
        c = ProjectionClosure(m)
        res = analyze_model_multiplicity(c, f"W(3,{c.s}) {model_name}")
        print(f"\nModel: {res['name']}")
        print(f"  Physical vertices: {res['n_vertices']}, Alphabet a: {res['a']}")
        print(f"  Global N_3: mean={res['mean_N3']:.3f}, std={res['std_N3']:.3f}, max={res['max_N3']}")
        print(f"  Sum N_3^2 (Tr A^6): {res['sum_N3_sq']}")
        print(f"  Proper P3: {res['census_proper_P3']}, Blocked: {res['census_blocked']}, Unblocked: {res['census_unblocked']}")
        print(f"  BBo: {res['census_bbo']}, Blocked ratio: {res['blocked_ratio']:.4f}")

    # Also test spread
    m_spread, _, _, _ = true_spread_global_model(2, 'balanced')
    c_spread = ProjectionClosure(m_spread)
    res_spread = analyze_model_multiplicity(c_spread, "W(3,4) spread")
    print(f"\nModel: {res_spread['name']}")
    print(f"  Global N_3: mean={res_spread['mean_N3']:.3f}, std={res_spread['std_N3']:.3f}, max={res_spread['max_N3']}")
    print(f"  Sum N_3^2 (Tr A^6): {res_spread['sum_N3_sq']}")
    print(f"  Proper P3: {res_spread['census_proper_P3']}, Blocked: {res_spread['census_blocked']}, Unblocked: {res_spread['census_unblocked']}")
    print(f"  BBo: {res_spread['census_bbo']}, Blocked ratio: {res_spread['blocked_ratio']:.4f}")


if __name__ == "__main__":
    run_option1_audit()
