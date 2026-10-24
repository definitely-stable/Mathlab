"""HYP-105: Exhaustive 1-swap neighborhood audit & adversarial search on genuine W(3,2).

Searches for adversarial permutations g in S_15 minimizing the core sum D6 + BA + AB
and total historical count S_seven to test whether simultaneous annihilation
D6 = 0 and BA = 0 and AB = 0 is possible on W(3,2), or whether the certified floor
remains strictly positive across all tested orbits.
"""
from collections import Counter
from itertools import combinations
import random
import time

from hyp105_issue230_proof_audit import frozen_model, F0, G68, G72
from hyp105_g5e2b3e1b0_seven_signature import (
    physical_column_dual, is_connected_column_cycle
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six, PAIRS

# ---------------------------------------------------------------------------
# Precomputed physical bitmask tables on K_6
# ---------------------------------------------------------------------------
two_factors_mask = [False] * 32768
for subset in combinations(range(15), 6):
    deg = [0] * 6
    for e in subset:
        u, v = PAIRS[e]
        deg[u] += 1
        deg[v] += 1
    if all(d == 2 for d in deg):
        two_factors_mask[sum(1 << e for e in subset)] = True

B_factors_mask = [False] * (15 << 15)
for e_rep in range(15):
    u_rep, v_rep = PAIRS[e_rep]
    rem_verts = [v for v in range(6) if v != u_rep and v != v_rep]
    for c4_edges in combinations(range(15), 4):
        if e_rep in c4_edges:
            continue
        deg = {v: 0 for v in rem_verts}
        valid = True
        for e in c4_edges:
            u, v = PAIRS[e]
            if u not in deg or v not in deg:
                valid = False
                break
            deg[u] += 1
            deg[v] += 1
        if valid and all(d == 2 for d in deg.values()):
            c4_m = sum(1 << e for e in c4_edges)
            B_factors_mask[(e_rep << 15) | c4_m] = True

C_factors_mask = [False] * 32768
for subset in combinations(range(15), 3):
    deg = [0] * 6
    for e in subset:
        u, v = PAIRS[e]
        deg[u] += 1
        deg[v] += 1
    if all(d == 1 for d in deg):
        C_factors_mask[sum(1 << e for e in subset)] = True


class W32BitmaskEvaluator:
    def __init__(self, f_perm):
        f_labels = tuple(PAIRS[i] for i in f_perm)
        m = frozen_model('lex')
        self.edges = m['incidences']
        m['left_labels'] = f_labels

        self.cand_BA = []
        self.cand_AB = []
        self.cand_AA = []
        self.cand_CA_right_A = []
        self.cand_CA_right_C = []
        self.cand_CB_right_B = []
        self.cand_CB_right_C = []
        self.cand_BB_overlap = []
        self.cand_BB_disjoint = []

        for ids, expected_left in selected_left_six(m):
            p = tuple(self.edges[i][0] for i in ids)
            l = tuple(self.edges[i][1] for i in ids)
            lkind = expected_left

            freq = Counter(l)
            prof = tuple(sorted(freq.values(), reverse=True))
            if prof == (1, 1, 1, 1, 1, 1):
                rkind = "A"
            elif prof == (2, 1, 1, 1, 1):
                rkind = "B"
            elif prof == (2, 2, 2):
                rkind = "C"
            else:
                continue

            if lkind == "B" and rkind == "A":
                self.cand_BA.append(l)
            elif lkind == "A" and rkind == "B":
                l_rep = next(k for k, v in freq.items() if v == 2)
                l_singles = tuple(k for k, v in freq.items() if v == 1)
                self.cand_AB.append((l_rep, l_singles))
            elif lkind == "A" and rkind == "A":
                ld = physical_column_dual(self.edges, f_labels, p)
                if ld and is_connected_column_cycle(ld):
                    self.cand_AA.append((ld, l))
            elif lkind == "C" and rkind == "A":
                self.cand_CA_right_A.append(l)
            elif lkind == "A" and rkind == "C":
                pairs = tuple(k for k, v in freq.items() if v == 2)
                self.cand_CA_right_C.append(pairs)
            elif lkind == "C" and rkind == "B":
                l_rep = next(k for k, v in freq.items() if v == 2)
                l_singles = tuple(k for k, v in freq.items() if v == 1)
                self.cand_CB_right_B.append((l_rep, l_singles))
            elif lkind == "B" and rkind == "C":
                pairs = tuple(k for k, v in freq.items() if v == 2)
                self.cand_CB_right_C.append(pairs)
            elif lkind == "B" and rkind == "B":
                l_rep = next(k for k, v in freq.items() if v == 2)
                l_singles = tuple(k for k, v in freq.items() if v == 1)
                lp = next(x for x, n in Counter(p).items() if n == 2)
                L = {j for j, x in enumerate(p) if x == lp}
                R = {j for j, x in enumerate(l) if x == l_rep}
                if len(L & R) == 1:
                    self.cand_BB_overlap.append((l_rep, l_singles))
                else:
                    self.cand_BB_disjoint.append((l_rep, l_singles))

    def evaluate_all(self, g_perm):
        g_bits = [1 << g_perm[i] for i in range(15)]
        g_labels = tuple(PAIRS[i] for i in g_perm)

        # 1. BA
        BA = 0
        for l0, l1, l2, l3, l4, l5 in self.cand_BA:
            m = g_bits[l0] | g_bits[l1] | g_bits[l2] | g_bits[l3] | g_bits[l4] | g_bits[l5]
            if two_factors_mask[m]:
                BA += 1

        # 2. AB
        AB = 0
        for l_rep, (s0, s1, s2, s3) in self.cand_AB:
            c4_m = g_bits[s0] | g_bits[s1] | g_bits[s2] | g_bits[s3]
            if B_factors_mask[(g_perm[l_rep] << 15) | c4_m]:
                AB += 1

        # 3. D6
        D6 = 0
        for ld, (l0, l1, l2, l3, l4, l5) in self.cand_AA:
            m = g_bits[l0] | g_bits[l1] | g_bits[l2] | g_bits[l3] | g_bits[l4] | g_bits[l5]
            if two_factors_mask[m]:
                rd = physical_column_dual(self.edges, g_labels, (l0, l1, l2, l3, l4, l5))
                if ld == rd:
                    D6 += 1

        # 4. CA
        CA = 0
        for l0, l1, l2, l3, l4, l5 in self.cand_CA_right_A:
            m = g_bits[l0] | g_bits[l1] | g_bits[l2] | g_bits[l3] | g_bits[l4] | g_bits[l5]
            if two_factors_mask[m]:
                CA += 1
        for p0, p1, p2 in self.cand_CA_right_C:
            m = g_bits[p0] | g_bits[p1] | g_bits[p2]
            if C_factors_mask[m]:
                CA += 1

        # 5. CB
        CB = 0
        for l_rep, (s0, s1, s2, s3) in self.cand_CB_right_B:
            c4_m = g_bits[s0] | g_bits[s1] | g_bits[s2] | g_bits[s3]
            if B_factors_mask[(g_perm[l_rep] << 15) | c4_m]:
                CB += 1
        for p0, p1, p2 in self.cand_CB_right_C:
            m = g_bits[p0] | g_bits[p1] | g_bits[p2]
            if C_factors_mask[m]:
                CB += 1

        # 6. BB
        BB_overlap = 0
        for l_rep, (s0, s1, s2, s3) in self.cand_BB_overlap:
            c4_m = g_bits[s0] | g_bits[s1] | g_bits[s2] | g_bits[s3]
            if B_factors_mask[(g_perm[l_rep] << 15) | c4_m]:
                BB_overlap += 1

        BB_disjoint = 0
        for l_rep, (s0, s1, s2, s3) in self.cand_BB_disjoint:
            c4_m = g_bits[s0] | g_bits[s1] | g_bits[s2] | g_bits[s3]
            if B_factors_mask[(g_perm[l_rep] << 15) | c4_m]:
                BB_disjoint += 1

        core = D6 + BA + AB
        total_S = core + CA + CB + BB_overlap + BB_disjoint
        return {
            "D6": D6,
            "BA": BA,
            "AB": AB,
            "core": core,
            "CA": CA,
            "CB": CB,
            "BB_overlap": BB_overlap,
            "BB_disjoint": BB_disjoint,
            "total_S": total_S,
        }


def run_full_1swap_neighborhood_audit(evaluator, base_perm, name="S68"):
    """Exhaustively scan all 105 1-transposition swaps around base_perm."""
    base_res = evaluator.evaluate_all(base_perm)
    print(f"\n--- 1-Swap Neighborhood Audit around {name} ---")
    print(f"Base permutation {name}: core={base_res['core']}, S={base_res['total_S']} ({base_res})")

    min_neighbor_core = 999999
    min_neighbor_S = 999999
    strictly_better_neighbors = []

    all_pairs = list(combinations(range(15), 2))
    assert len(all_pairs) == 105

    for i, j in all_pairs:
        # Swap lines i and j
        swapped = list(base_perm)
        swapped[i], swapped[j] = swapped[j], swapped[i]
        swapped_perm = tuple(swapped)

        res = evaluator.evaluate_all(swapped_perm)
        c = res["core"]
        s = res["total_S"]

        if c < min_neighbor_core:
            min_neighbor_core = c
        if s < min_neighbor_S:
            min_neighbor_S = s

        if c < base_res["core"] or s < base_res["total_S"]:
            strictly_better_neighbors.append((i, j, c, s))

    is_strict_local_min_core = (min_neighbor_core > base_res["core"])
    is_strict_local_min_S = (min_neighbor_S > base_res["total_S"])

    print(f"Total 1-swap neighbors scanned: {len(all_pairs)}")
    print(f"Minimum neighbor core: {min_neighbor_core} (base={base_res['core']}, strict local min? {is_strict_local_min_core})")
    print(f"Minimum neighbor total_S: {min_neighbor_S} (base={base_res['total_S']}, strict local min? {is_strict_local_min_S})")
    print(f"Strictly better neighbors count: {len(strictly_better_neighbors)}")

    return {
        "base_name": name,
        "base_core": base_res["core"],
        "base_S": base_res["total_S"],
        "min_neighbor_core": min_neighbor_core,
        "min_neighbor_S": min_neighbor_S,
        "is_strict_local_min_core": is_strict_local_min_core,
        "is_strict_local_min_S": is_strict_local_min_S,
        "strictly_better_neighbors": strictly_better_neighbors,
    }


def run_randomized_adversarial_search(evaluator, num_starts=20, steps_per_start=50, seed=42):
    """Run randomized local search to find the lowest possible D6 + BA + AB and total S."""
    rng = random.Random(seed)
    global_min_core = 999999
    global_min_S = 999999
    best_perm_core = None
    best_perm_S = None
    all_pairs = list(combinations(range(15), 2))

    print(f"\n--- Randomized Adversarial Search ({num_starts} starts x {steps_per_start} steps) ---")
    t0 = time.time()

    for start_idx in range(num_starts):
        # Start from random permutation or from known seeds
        if start_idx == 0:
            curr_perm = G68
        elif start_idx == 1:
            curr_perm = G72
        elif start_idx == 2:
            curr_perm = tuple(range(15))
        elif start_idx == 3:
            curr_perm = tuple(reversed(range(15)))
        else:
            p = list(range(15))
            rng.shuffle(p)
            curr_perm = tuple(p)

        curr_res = evaluator.evaluate_all(curr_perm)
        curr_score = curr_res["core"]

        if curr_res["core"] < global_min_core:
            global_min_core = curr_res["core"]
            best_perm_core = curr_perm
        if curr_res["total_S"] < global_min_S:
            global_min_S = curr_res["total_S"]
            best_perm_S = curr_perm

        # Greedy local descent
        for step in range(steps_per_start):
            improved = False
            # Sample random subset of swaps
            sample_swaps = rng.sample(all_pairs, min(30, len(all_pairs)))
            for i, j in sample_swaps:
                cand = list(curr_perm)
                cand[i], cand[j] = cand[j], cand[i]
                cand_perm = tuple(cand)
                cand_res = evaluator.evaluate_all(cand_perm)
                if cand_res["core"] < curr_score:
                    curr_perm = cand_perm
                    curr_score = cand_res["core"]
                    curr_res = cand_res
                    improved = True
                    if curr_res["core"] < global_min_core:
                        global_min_core = curr_res["core"]
                        best_perm_core = curr_perm
                    if curr_res["total_S"] < global_min_S:
                        global_min_S = curr_res["total_S"]
                        best_perm_S = curr_perm
                    break
            if not improved:
                break

    elapsed = time.time() - t0
    print(f"Adversarial search completed in {elapsed:.2f}s.")
    print(f"Global minimum core sum found: {global_min_core} (achieved by best_perm_core)")
    print(f"Global minimum total S found: {global_min_S} (achieved by best_perm_S)")
    res_best = evaluator.evaluate_all(best_perm_core)
    print(f"Best core details: {res_best}")

    return {
        "global_min_core": global_min_core,
        "global_min_S": global_min_S,
        "best_core_details": res_best,
        "simultaneous_zero_found": global_min_core == 0,
    }


if __name__ == "__main__":
    eval_f0 = W32BitmaskEvaluator(F0)
    audit_s68 = run_full_1swap_neighborhood_audit(eval_f0, G68, "S68")
    audit_s72 = run_full_1swap_neighborhood_audit(eval_f0, G72, "S72")
    search_res = run_randomized_adversarial_search(eval_f0, num_starts=30, steps_per_start=40)
