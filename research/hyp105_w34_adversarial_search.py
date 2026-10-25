"""HYP-105 Issue #230: Adversarial Minimization and Branch B Counterexample Search on W(3,4).

Tests whether an adversarial search on W(3,4) (s=4, s^6=4096, V=85, a=14) can drive
the synchronized BB-overlap count BBo(f, g) or total S(f, g) down towards 0 (e.g. < 0.1 s^6 or = 0),
or whether it hits a strict universal positive floor BBo >= c_0 s^6 across all tested configurations.
"""
from collections import Counter
from itertools import combinations
import json
import math
import random
import time

from hyp105_issue230_proof_audit import parameters, _geometry, _model
from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model


class FastW34Evaluator:
    """High-performance finite GQ(4,4) path-projection evaluator on alphabet a=14, V=85."""

    def __init__(self):
        _, points, lines, incidences = _geometry(2)
        p = parameters(4)
        self.s, self.a, self.v, self.delta = p['s'], p['a'], p['V'], p['Delta']
        self.s6 = self.s ** 6
        self.edges = tuple(tuple(e) for e in incidences)
        self.lines = [set() for _ in range(self.v)]
        self.point_lines = [set() for _ in range(self.v)]
        for q, l in self.edges:
            self.lines[l].add(q)
            self.point_lines[q].add(l)

        self.edge_matrix = [False] * (self.v * self.v)
        for q, l in self.edges:
            self.edge_matrix[q * self.v + l] = True

        self.proj_p = [-1] * (self.v * self.v)
        self.proj_l = [-1] * (self.v * self.v)
        for q, nbrs in enumerate(self.point_lines):
            for l in nbrs:
                for pt in self.lines[l] - {q}:
                    for r in self.point_lines[pt] - {l}:
                        self.proj_p[q * self.v + r] = pt
                        self.proj_l[q * self.v + r] = l

        a = self.a
        self.v_x = [u // a for u in range(a * a)]
        self.v_y = [u % a for u in range(a * a)]
        self.v_mx = [1 << (u // a) for u in range(a * a)]
        self.v_my = [1 << (u % a) for u in range(a * a)]
        self.all_pairs = tuple(combinations(range(a), 2))

    def evaluate_bbo(self, f, g):
        """Fast calculation of synchronized BBo = unblocked // 2."""
        a = self.a
        v = self.v
        fi_table = [-1] * (a * a)
        for q, (u, w) in enumerate(f):
            fi_table[u * a + w] = q
            fi_table[w * a + u] = q
        gi_table = [-1] * (a * a)
        for r, (x, y) in enumerate(g):
            gi_table[x * a + y] = r
            gi_table[y * a + x] = r

        f_masks = [(1 << u) | (1 << w) for u, w in f]
        g_masks = [(1 << x) | (1 << y) for x, y in g]

        adj = [[] for _ in range(a * a)]
        for p, l in self.edges:
            u, w = f[p]
            x, y = g[l]
            b1, c1 = u * a + x, w * a + y
            b2, c2 = u * a + y, w * a + x
            adj[b1].append(c1)
            adj[c1].append(b1)
            adj[b2].append(c2)
            adj[c2].append(b2)

        v_mx, v_my = self.v_mx, self.v_my
        v_x, v_y = self.v_x, self.v_y
        edge_matrix = self.edge_matrix
        proj_p, proj_l = self.proj_p, self.proj_l

        unblocked = 0
        for u0 in range(a * a):
            m0_x, m0_y = v_mx[u0], v_my[u0]
            u0_base = v_x[u0] * a
            y0_base = v_y[u0] * a
            for u1 in adj[u0]:
                m1_x = m0_x | v_mx[u1]
                m1_y = m0_y | v_my[u1]
                for u2 in adj[u1]:
                    if (m1_x & v_mx[u2]) or (m1_y & v_my[u2]):
                        continue
                    m2_x = m1_x | v_mx[u2]
                    m2_y = m1_y | v_my[u2]
                    for u3 in adj[u2]:
                        if (m2_x & v_mx[u3]) or (m2_y & v_my[u3]):
                            continue
                        q = fi_table[u0_base + v_x[u3]]
                        r = gi_table[y0_base + v_y[u3]]
                        if q < 0 or r < 0:
                            continue
                        qr = q * v + r
                        if edge_matrix[qr]:
                            continue
                        p = proj_p[qr]
                        l = proj_l[qr]
                        if (f_masks[p] & (m2_x | v_mx[u3])) or (g_masks[l] & (m2_y | v_my[u3])):
                            continue
                        unblocked += 1
        return unblocked // 2

    def full_census(self, f, g):
        """Full exact census matching ProjectionClosure.census()."""
        a = self.a
        v = self.v
        fi_table = [-1] * (a * a)
        for q, (u, w) in enumerate(f):
            fi_table[u * a + w] = q
            fi_table[w * a + u] = q
        gi_table = [-1] * (a * a)
        for r, (x, y) in enumerate(g):
            gi_table[x * a + y] = r
            gi_table[y * a + x] = r

        f_masks = [(1 << u) | (1 << w) for u, w in f]
        g_masks = [(1 << x) | (1 << y) for x, y in g]

        adj = [[] for _ in range(a * a)]
        for p, l in self.edges:
            u, w = f[p]
            x, y = g[l]
            b1, c1 = u * a + x, w * a + y
            b2, c2 = u * a + y, w * a + x
            adj[b1].append(c1)
            adj[c1].append(b1)
            adj[b2].append(c2)
            adj[c2].append(b2)

        v_mx, v_my = self.v_mx, self.v_my
        v_x, v_y = self.v_x, self.v_y
        edge_matrix = self.edge_matrix
        proj_p, proj_l = self.proj_p, self.proj_l

        proper_P3 = 0
        missing = 0
        incident = 0
        blocked = 0
        blocked_left = 0
        blocked_right = 0
        blocked_both = 0
        unblocked = 0

        for u0 in range(a * a):
            m0_x, m0_y = v_mx[u0], v_my[u0]
            u0_base = v_x[u0] * a
            y0_base = v_y[u0] * a
            for u1 in adj[u0]:
                m1_x = m0_x | v_mx[u1]
                m1_y = m0_y | v_my[u1]
                for u2 in adj[u1]:
                    if (m1_x & v_mx[u2]) or (m1_y & v_my[u2]):
                        continue
                    m2_x = m1_x | v_mx[u2]
                    m2_y = m1_y | v_my[u2]
                    for u3 in adj[u2]:
                        if (m2_x & v_mx[u3]) or (m2_y & v_my[u3]):
                            continue
                        proper_P3 += 1
                        q = fi_table[u0_base + v_x[u3]]
                        r = gi_table[y0_base + v_y[u3]]
                        if q < 0 or r < 0:
                            missing += 1
                            continue
                        qr = q * v + r
                        if edge_matrix[qr]:
                            incident += 1
                            continue
                        p = proj_p[qr]
                        l = proj_l[qr]
                        left = bool(f_masks[p] & (m2_x | v_mx[u3]))
                        right = bool(g_masks[l] & (m2_y | v_my[u3]))
                        if left or right:
                            blocked += 1
                            blocked_left += left
                            blocked_right += right
                            blocked_both += (left and right)
                            continue
                        unblocked += 1

        bbo = unblocked // 2
        return {
            'proper_P3': proper_P3,
            'missing': missing,
            'incident': incident,
            'blocked': blocked,
            'blocked_left': blocked_left,
            'blocked_right': blocked_right,
            'blocked_both': blocked_both,
            'unblocked': unblocked,
            'synchronized_BBo': bbo,
            's': self.s,
            'a': self.a,
            's6': self.s6,
            'bbo_ratio_s6': bbo / self.s6,
            'blocked_ratio': blocked / (blocked + unblocked) if (blocked + unblocked) > 0 else 0.0,
        }


def run_greedy_swap_descent(evaluator, f_init, g_init, *, max_steps=500, patience=200, rng_seed=42):
    """Greedy local descent on (f, g) permutations.

    At each step, picks a random transposition in f or g. If it strictly decreases BBo,
    accepts it. Stops after max_steps or when patience consecutive attempts yield no improvement.
    """
    rng = random.Random(rng_seed)
    f = list(f_init)
    g = list(g_init)
    curr_bbo = evaluator.evaluate_bbo(f, g)
    history = [(0, curr_bbo, curr_bbo / evaluator.s6)]

    t0 = time.time()
    steps_without_improvement = 0
    accepted_swaps = 0

    for step in range(1, max_steps + 1):
        side = rng.choice(['f', 'g'])
        u, v = rng.sample(range(85), 2)
        if side == 'f':
            f[u], f[v] = f[v], f[u]
            new_bbo = evaluator.evaluate_bbo(f, g)
            if new_bbo < curr_bbo:
                curr_bbo = new_bbo
                history.append((step, curr_bbo, curr_bbo / evaluator.s6))
                accepted_swaps += 1
                steps_without_improvement = 0
            else:
                f[u], f[v] = f[v], f[u]
                steps_without_improvement += 1
        else:
            g[u], g[v] = g[v], g[u]
            new_bbo = evaluator.evaluate_bbo(f, g)
            if new_bbo < curr_bbo:
                curr_bbo = new_bbo
                history.append((step, curr_bbo, curr_bbo / evaluator.s6))
                accepted_swaps += 1
                steps_without_improvement = 0
            else:
                g[u], g[v] = g[v], g[u]
                steps_without_improvement += 1

        if steps_without_improvement >= patience:
            break

    elapsed = time.time() - t0
    final_census = evaluator.full_census(f, g)
    return {
        'method': 'greedy_descent',
        'steps_run': step,
        'accepted_swaps': accepted_swaps,
        'elapsed_seconds': elapsed,
        'initial_bbo': history[0][1],
        'initial_bbo_ratio': history[0][2],
        'final_bbo': curr_bbo,
        'final_bbo_ratio': curr_bbo / evaluator.s6,
        'history': history,
        'final_census': final_census,
        'f': tuple(f),
        'g': tuple(g),
    }


def run_simulated_annealing(evaluator, f_init, g_init, *, n_steps=1000, t_start=80.0,
                            cooling_rate=0.996, quench_steps=300, rng_seed=42):
    """Simulated annealing with Metropolis-Hastings acceptance, followed by greedy quench."""
    rng = random.Random(rng_seed)
    f = list(f_init)
    g = list(g_init)
    curr_bbo = evaluator.evaluate_bbo(f, g)
    best_f = list(f)
    best_g = list(g)
    best_bbo = curr_bbo

    t = t_start
    history = [(0, curr_bbo, curr_bbo / evaluator.s6, best_bbo)]
    accepted_steps = 0
    t0 = time.time()

    for step in range(1, n_steps + 1):
        side = rng.choice(['f', 'g'])
        u, v = rng.sample(range(85), 2)
        if side == 'f':
            f[u], f[v] = f[v], f[u]
            cand_bbo = evaluator.evaluate_bbo(f, g)
            delta = cand_bbo - curr_bbo
            if delta <= 0 or (t > 0.01 and rng.random() < math.exp(-delta / t)):
                curr_bbo = cand_bbo
                accepted_steps += 1
                if curr_bbo < best_bbo:
                    best_bbo = curr_bbo
                    best_f = list(f)
                    best_g = list(g)
            else:
                f[u], f[v] = f[v], f[u]
        else:
            g[u], g[v] = g[v], g[u]
            cand_bbo = evaluator.evaluate_bbo(f, g)
            delta = cand_bbo - curr_bbo
            if delta <= 0 or (t > 0.01 and rng.random() < math.exp(-delta / t)):
                curr_bbo = cand_bbo
                accepted_steps += 1
                if curr_bbo < best_bbo:
                    best_bbo = curr_bbo
                    best_f = list(f)
                    best_g = list(g)
            else:
                g[u], g[v] = g[v], g[u]

        t = max(0.01, t * cooling_rate)
        if step % 25 == 0 or step == n_steps:
            history.append((step, curr_bbo, curr_bbo / evaluator.s6, best_bbo))

    # Quench phase: greedy descent from the best configuration
    quench_res = run_greedy_swap_descent(evaluator, best_f, best_g,
                                         max_steps=quench_steps, patience=150, rng_seed=rng_seed+100)

    elapsed = time.time() - t0
    final_census = quench_res['final_census']
    return {
        'method': 'simulated_annealing_with_quench',
        'sa_steps': n_steps,
        'sa_accepted': accepted_steps,
        'sa_best_bbo': best_bbo,
        'quench_steps_run': quench_res['steps_run'],
        'quench_accepted': quench_res['accepted_swaps'],
        'elapsed_seconds': elapsed,
        'initial_bbo': history[0][1],
        'initial_bbo_ratio': history[0][2],
        'final_bbo': quench_res['final_bbo'],
        'final_bbo_ratio': quench_res['final_bbo_ratio'],
        'sa_history': history,
        'final_census': final_census,
        'f': quench_res['f'],
        'g': quench_res['g'],
    }


def run_comprehensive_w34_adversarial_suite(*, max_steps=500, sa_steps=800):
    """Executes the full adversarial minimization suite across lex, spread, and random seeds."""
    evaluator = FastW34Evaluator()
    results = {}

    # 1. Lex baseline
    m_lex = fixture(2, 'lex')
    f_lex, g_lex = m_lex['left_labels'], m_lex['right_labels']
    print(f"--- Running Greedy Descent from 'lex' (start BBo: {evaluator.evaluate_bbo(f_lex, g_lex)}) ---")
    res_lex_greedy = run_greedy_swap_descent(evaluator, f_lex, g_lex, max_steps=max_steps, rng_seed=101)
    print(f"  Greedy Lex: final BBo = {res_lex_greedy['final_bbo']} ({res_lex_greedy['final_bbo_ratio']:.3f} s^6) in {res_lex_greedy['elapsed_seconds']:.1f}s")

    print(f"--- Running Simulated Annealing from 'lex' ---")
    res_lex_sa = run_simulated_annealing(evaluator, f_lex, g_lex, n_steps=sa_steps, rng_seed=102)
    print(f"  SA Lex: final BBo = {res_lex_sa['final_bbo']} ({res_lex_sa['final_bbo_ratio']:.3f} s^6) in {res_lex_sa['elapsed_seconds']:.1f}s")
    results['lex_greedy'] = res_lex_greedy
    results['lex_sa'] = res_lex_sa

    # 2. Spread baseline (D5 balanced spread)
    m_spread, _, _, _ = true_spread_global_model(2, 'balanced')
    f_spread, g_spread = m_spread['left_labels'], m_spread['right_labels']
    print(f"\n--- Running Greedy Descent from 'spread' (start BBo: {evaluator.evaluate_bbo(f_spread, g_spread)}) ---")
    res_spread_greedy = run_greedy_swap_descent(evaluator, f_spread, g_spread, max_steps=max_steps, rng_seed=201)
    print(f"  Greedy Spread: final BBo = {res_spread_greedy['final_bbo']} ({res_spread_greedy['final_bbo_ratio']:.3f} s^6) in {res_spread_greedy['elapsed_seconds']:.1f}s")

    print(f"--- Running Simulated Annealing from 'spread' ---")
    res_spread_sa = run_simulated_annealing(evaluator, f_spread, g_spread, n_steps=sa_steps, rng_seed=202)
    print(f"  SA Spread: final BBo = {res_spread_sa['final_bbo']} ({res_spread_sa['final_bbo_ratio']:.3f} s^6) in {res_spread_sa['elapsed_seconds']:.1f}s")
    results['spread_greedy'] = res_spread_greedy
    results['spread_sa'] = res_spread_sa

    # 3. Random seeds
    for idx, rseed in enumerate([301, 302, 303], start=1):
        rng = random.Random(rseed)
        f_rand = list(evaluator.all_pairs[:85])
        g_rand = list(evaluator.all_pairs[:85])
        rng.shuffle(f_rand)
        rng.shuffle(g_rand)
        start_bbo = evaluator.evaluate_bbo(f_rand, g_rand)
        print(f"\n--- Running Greedy Descent from 'random_{idx}' (start BBo: {start_bbo}) ---")
        res_rand_greedy = run_greedy_swap_descent(evaluator, f_rand, g_rand, max_steps=max_steps, rng_seed=rseed+10)
        print(f"  Greedy Rand {idx}: final BBo = {res_rand_greedy['final_bbo']} ({res_rand_greedy['final_bbo_ratio']:.3f} s^6) in {res_rand_greedy['elapsed_seconds']:.1f}s")

        print(f"--- Running Simulated Annealing from 'random_{idx}' ---")
        res_rand_sa = run_simulated_annealing(evaluator, f_rand, g_rand, n_steps=sa_steps, rng_seed=rseed+20)
        print(f"  SA Rand {idx}: final BBo = {res_rand_sa['final_bbo']} ({res_rand_sa['final_bbo_ratio']:.3f} s^6) in {res_rand_sa['elapsed_seconds']:.1f}s")
        results[f'random_{idx}_greedy'] = res_rand_greedy
        results[f'random_{idx}_sa'] = res_rand_sa

    return results


if __name__ == '__main__':
    res = run_comprehensive_w34_adversarial_suite(max_steps=500, sa_steps=800)
    # Save a summary json
    summary = {}
    for name, data in res.items():
        summary[name] = {
            'initial_bbo': data['initial_bbo'],
            'initial_ratio': data['initial_bbo_ratio'],
            'final_bbo': data['final_bbo'],
            'final_ratio': data['final_bbo_ratio'],
            'elapsed_seconds': data['elapsed_seconds'],
            'census': data['final_census'],
        }
    with open('research/hyp105_w34_adversarial_results.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("\nSaved comprehensive results to research/hyp105_w34_adversarial_results.json")
