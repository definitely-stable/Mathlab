"""AA4-CQ independent original-source, path-walk and arithmetic falsifiers."""
from math import comb, isqrt
from itertools import combinations
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import (
    _validated_original, explicit_three_walks, macro_path_cut)


def _cuts(a):
    k = a // 2
    yield tuple(range(k)), tuple(range(a - k, a))
    yield tuple(range(a - k, a)), tuple(range(k))
    yield tuple(range(1, k + 1)), tuple(range(max(0, a - k - 1), a - 1))
    yield tuple(range(0, k)), tuple(range(1, k + 1))


class AA4CQOriginalPathCutCertificate(unittest.TestCase):
    def test_01_real_original_incidence_cubic_identity_independent_3walks(self):
        for h in (1, 2, 3):
            for scheme in (("lex", "S72") if h == 1 else ("lex", "random")):
                model = fixture(h, scheme)
                s, V, a, f, g, point_lines, line_points = _validated_original(model)
                # Full 15x15 and 85x85 two-sided walk verification; selected
                # genuine 585x585 cases for W38 (no fake full-root count).
                if h <= 2:
                    pairs = [(p, l) for p in range(V) for l in range(V)]
                else:
                    pp = sorted(set(list(range(35)) + list(range(V - 35, V))))
                    ll = sorted(set(list(range(35)) + list(range(V - 35, V))))
                    pairs = [(p, l) for p in pp for l in ll]
                for p, l in pairs:
                    walks = explicit_three_walks(p, l, point_lines, line_points)
                    self.assertEqual(walks, 2 * s + 1 if l in point_lines[p] else 1)
                self.assertEqual(len(point_lines), V)
                self.assertEqual(len(line_points), V)
                print("AA4CQ_TRUE_GQ_CUBIC", s, scheme, "pairs", len(pairs), flush=True)

    def test_02_complete_original_global_cut_arbitrary_correlated_maps(self):
        for h in (1, 2, 3):
            for scheme in (("lex", "S72") if h == 1 else ("lex", "random")):
                s, V, a, f, g, pl, lp = _validated_original(fixture(h, scheme))
                for X, Y in _cuts(a):
                    z = macro_path_cut(fixture(h, scheme), X, Y)
                    P = z["P_original_point_factor_ids"]
                    L = z["L_original_line_factor_ids"]
                    direct = sum(l not in pl[p] for p in P for l in L)
                    self.assertEqual(direct, z["unique_original_simple_3path_count"])
                    self.assertEqual(direct, z["direct_nonincidence_pair_count"])
                    self.assertEqual(z["original_flag_edges_between_cuts"],
                                     len(P) * len(L) - direct)
                    self.assertGreaterEqual(direct, len(P) * len(L) -
                                            (s + 1) * min(len(P), len(L)))
                    m = z["m_min_cut_factor_images"]
                    if m >= s + 1:
                        self.assertGreaterEqual(direct, m * (m - s - 1))
                    if s >= 8:
                        self.assertGreaterEqual(128 * direct, V * V)
                        self.assertTrue(z["macro_s6_gate"])
                    self.assertFalse(z["count_is_positive_GF5_sixflag"])
                    self.assertEqual(z["root_status"], "OPEN_WITH_FORMAL_BLOCKER")
                    # Alternative true ORIGINAL incidence path enumeration.
                    for p in P[:12]:
                        for l in L[:12]:
                            if l not in pl[p]:
                                self.assertEqual(explicit_three_walks(p,l,pl,lp),1)
                print("AA4CQ_TRUE_ORIGINAL_CUTS",s,scheme,"checked",4,flush=True)

    def test_03_injection_original_flag_and_coordinate_fail_closed(self):
        model = fixture(2, "lex")
        with self.assertRaises(ValueError):
            macro_path_cut(model, point_coordinates=(0, 1))
        with self.assertRaises(ValueError):
            macro_path_cut(model, line_coordinates=tuple([-1] + list(range(1, 7))))
        bad = dict(model)
        lab = list(model["left_labels"])
        lab[1] = lab[0]
        bad["left_labels"] = tuple(lab)
        with self.assertRaises((ValueError, AssertionError)):
            macro_path_cut(bad)
        bad2 = dict(model)
        bad2["incidences"] = tuple(model["incidences"][:-1])
        with self.assertRaises((ValueError, AssertionError)):
            macro_path_cut(bad2)

    def test_04_all_micro_six_coordinate_spectral_floors_cannot_force_flag(self):
        for h in (2, 3, 4, 5):
            s = 1 << h
            V = (s + 1) * (s*s + 1)
            # The exact expander-mixing FLOOR is nonpositive for every
            # nonempty x,y <= C(6,2)=15 (zero is a possible floor).
            for x in range(1, 16):
                for y in range(1, 16):
                    lhs = 2*s*(V - x)*(V - y)
                    rhs = (s+1)**2*x*y
                    self.assertGreaterEqual(lhs, rhs)
            self.assertGreaterEqual(2*s*(V-15)**2, 225*(s+1)**2)

    def test_05_independent_all_h_symbolic_cut_arithmetic_regression(self):
        for h in range(3, 13):
            s = 1 << h
            V = (s + 1) * (s*s + 1)
            a = (1 + isqrt(1 + 8*V)) // 2
            while comb(a, 2) < V:
                a += 1
            while a > 2 and comb(a-1, 2) >= V:
                a -= 1
            k = a // 2
            H = comb(a, 2) - V
            m = comb(k, 2) - H
            self.assertGreaterEqual(a, 22)
            self.assertGreaterEqual(8*m, V)
            self.assertGreaterEqual(V, 16*(s+1))
            self.assertGreaterEqual(128*m*(m-s-1), V*V)
            self.assertLess(H, a-1)
            print("AA4CQ_ARITH_ALL_H",h,"a",a,"m",m,flush=True)

    def test_06_true_original_W32_exact_sixflag_BBo_matching_extension(self):
        """Independent 3! matching enumeration, NOT a physical GF5 acceptance."""
        from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
        from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
            classify_seven_all_a_original_Q)
        for scheme in ("lex", "S72"):
            original = fixture(1, scheme)
            _, _, _, actual_inc, actual_f, actual_g, _, _ = _original_source(original)
            original_flag_id = {pair: i for i, pair in enumerate(actual_inc)}
            s, V, a, f, g, pl, lp = _validated_original(original)
            d = s + 1
            flags = tuple((p, l) for p in range(V) for l in pl[p])
            self.assertEqual(len(flags), V*d)
            cut = macro_path_cut(original)
            cut_endpoints = {(p, l)
                             for p in cut["P_original_point_factor_ids"]
                             for l in cut["L_original_line_factor_ids"]
                             if l not in pl[p]}
            visited_source_Q_for_cut = set()
            physically_accepted_cut_BBo = 0
            total_original_source_BBo = 0
            total_cut_BBo = 0
            for p in range(V):
                for l in range(V):
                    if l in pl[p]:
                        continue
                    path = [(l0, q) for l0 in pl[p]
                            for q in lp[l0] if l in pl[q]]
                    self.assertEqual(len(path), 1)
                    l0, q = path[0]
                    self.assertNotEqual(p, q)
                    self.assertNotEqual(l, l0)
                    path_flags = ((p,l0),(q,l0),(q,l))
                    excluded_points = {p,q}
                    excluded_lines = {l0,l}
                    eligible = [flag for flag in flags
                                if flag[0] not in excluded_points
                                and flag[1] not in excluded_lines]
                    cnt = 0
                    for triple in combinations(eligible, 3):
                        if (len({u for u,v in triple}) != 3 or
                                len({v for u,v in triple}) != 3):
                            continue
                        cnt += 1
                        if (p, l) in cut_endpoints:
                            q6 = frozenset(path_flags + triple)
                            self.assertEqual(len(q6), 6)
                            # Exactly source path(3) + 3 original singleton flags.
                            pc = [sum(u == pid for u,v in q6) for pid in range(V)]
                            lc = [sum(v == lid for u,v in q6) for lid in range(V)]
                            self.assertEqual(sorted(v for v in pc if v),[1,1,1,1,2])
                            self.assertEqual(sorted(v for v in lc if v),[1,1,1,1,2])
                            self.assertNotIn(q6,visited_source_Q_for_cut)
                            visited_source_Q_for_cut.add(q6)
                            actual_ids = tuple(sorted(original_flag_id[e] for e in q6))
                            tag = classify_seven_all_a_original_Q(
                                actual_ids, actual_f, actual_g, actual_inc)
                            if tag is not None:
                                self.assertEqual(tag, "B/B-overlap")
                                physically_accepted_cut_BBo += 1
                    # The genuine original W32 GQ has a uniform nonincident
                    # original 3-path orbit; source-only total from AA4-U.
                    self.assertEqual(cnt, 5056)
                    self.assertGreaterEqual(6*cnt,
                                            (V*d-4*d)*(V*d-6*d)*(V*d-8*d))
                    total_original_source_BBo += cnt
                    if (p, l) in cut_endpoints:
                        total_cut_BBo += cnt
            self.assertEqual(total_original_source_BBo, 910080)
            self.assertEqual(total_cut_BBo, 5056*cut["unique_original_simple_3path_count"])
            self.assertEqual(len(visited_source_Q_for_cut), total_cut_BBo)
            self.assertGreaterEqual(
                6*total_cut_BBo,
                cut["source_BBo_six_distinct_original_flags_matched_anchor_floor_numerator"])
            print("AA4CQ_GENUINE_SOURCE_W32_MATCHING",scheme,
                  "total_original_BBo",total_original_source_BBo,
                  "cut_original_BBo",total_cut_BBo,
                  "path_cut_count",cut["unique_original_simple_3path_count"],
                  "physical_BBo_GF5_accepted_in_cut",physically_accepted_cut_BBo,
                  "historical_physical_GF5_ACCEPTANCE_NOT_IMPLIED",flush=True)


if __name__ == "__main__":
    unittest.main()
