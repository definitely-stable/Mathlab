"""Independent AA4-HEAVY-C6-INVERSE original source properness/minimality tests."""
from collections import Counter, defaultdict
from itertools import combinations
import unittest

from hyp105_original_heavy_c6_inverse_minimal import (
    SCHEMA,STATUS,planted_source,_matching,_labels,
    true_owned_edges,source_conflicts,two_cuts,canonical_cycle,
    graph_first_cycles,_adj,_e,inverse_x,inverse_y,
    check_source_finite,certificate
)


def two_3path_halves_count(edges):
    """Cycle census independent of the source-first inverse and DFS C6."""
    adj=_adj(edges)
    total=0
    for u,v in combinations(sorted(adj),2):
        paths=[]
        for a in adj[u]:
            if a==v: continue
            for b in adj[a]:
                if len({u,a,b,v})!=4 or v not in adj[b]:
                    continue
                paths.append((a,b))
        for (a,b),(c,d) in combinations(paths,2):
            if {a,b}.isdisjoint((c,d)):
                total+=1
    if total%3:
        raise AssertionError("pair-of-threepaths source C6 count not divisible by three")
    return total//3


class TestHeavyC6MinimalIndependent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_true_W32_W34_both_full_original_injected_label_maps(self):
        for s in (2,4):
            for mode in ("proper","drop_left_cut","drop_right_cut",
                         "drop_J_independence"):
                c=planted_source(s,mode)
                V=(s+1)*(s*s+1)
                self.assertEqual(c["V"],V)
                self.assertEqual(len(c["flags"]),(s+1)*V)
                self.assertEqual(len(set(c["flags"])),len(c["flags"]))
                self.assertEqual(len(c["f"]),V)
                self.assertEqual(len(c["g"]),V)
                self.assertEqual(len(set(c["f"])),V)
                self.assertEqual(len(set(c["g"])),V)
                self.assertEqual(len(c["ids"]),6)

    def test_02_no_two_original_flags_own_one_physical_edge(self):
        for s in (2,4):
            for mode in ("proper","drop_left_cut","drop_right_cut",
                         "drop_J_independence"):
                c=planted_source(s,mode)
                owner,per=true_owned_edges(c,c["ids"])
                self.assertEqual(len(owner),12)
                self.assertEqual(len(per),6)
                self.assertEqual(Counter(owner.values()),
                                 Counter({i:2 for i in c["ids"]}))
                for diag in per.values():
                    self.assertEqual(len(set(diag[0]+diag[1])),4)
                    self.assertFalse(set(diag[0])&set(diag[1]))

    def test_03_two_source_inverse_independent_point_and_line_directions(self):
        for s in (2,4):
            c=planted_source(s,"proper")
            owner,per=true_owned_edges(c,c["ids"])
            selected,bx,by=two_cuts(c,c["ids"],owner,"proper")
            self.assertEqual(len(selected),12)
            f=canonical_cycle(c["planted"])
            self.assertEqual(graph_first_cycles(selected),(f,))
            self.assertEqual(inverse_x(c["ids"],c,selected),f)
            self.assertEqual(inverse_y(c["ids"],c,selected),f)
            for mutated in (tuple(reversed(c["ids"])),
                            c["ids"][3:]+c["ids"][:3]):
                self.assertEqual(inverse_x(mutated,c,selected),f)
                self.assertEqual(inverse_y(mutated,c,selected),f)

    def test_04_external_graph_first_three_path_pairs_agree_without_factor_twelve(self):
        for s in (2,4):
            for mode in ("proper","drop_left_cut","drop_right_cut",
                         "drop_J_independence"):
                c=planted_source(s,mode)
                owner,_=true_owned_edges(c,c["ids"])
                E,_,_=two_cuts(c,c["ids"],owner,mode)
                physical=graph_first_cycles(E)
                halves=two_3path_halves_count(E)
                self.assertEqual(len(physical),halves)
                self.assertGreaterEqual(halves,1)
                if mode=="proper":
                    self.assertEqual(halves,1)

    def test_05_real_original_J_and_two_cuts_force_six_symbols_each(self):
        for s in (2,4):
            z=check_source_finite(planted_source(s,"proper"))
            self.assertTrue(z["proof_condition_fulfilled"])
            self.assertEqual(z["actual_original_J_conflicts"],0)
            self.assertTrue(z["x_cut_enabled"] and z["y_cut_enabled"])
            self.assertEqual(z["source_proper_C6"],1)
            self.assertEqual(z["physical_improper_C6"],0)
            self.assertTrue(z["for_all_proper_sixsets_dual_source_first_inverse_exact"])

    def test_06_only_right_cut_source_J_independent_is_NOT_enough(self):
        for s in (2,4):
            z=check_source_finite(planted_source(s,"drop_left_cut"))
            self.assertEqual(z["actual_original_J_conflicts"],0)
            self.assertFalse(z["x_cut_enabled"])
            self.assertTrue(z["y_cut_enabled"])
            self.assertGreaterEqual(z["physical_improper_C6"],1)
            self.assertFalse(z["proof_condition_fulfilled"])

    def test_07_only_left_cut_source_J_independent_is_NOT_enough(self):
        for s in (2,4):
            z=check_source_finite(planted_source(s,"drop_right_cut"))
            self.assertEqual(z["actual_original_J_conflicts"],0)
            self.assertTrue(z["x_cut_enabled"])
            self.assertFalse(z["y_cut_enabled"])
            self.assertGreaterEqual(z["physical_improper_C6"],1)
            self.assertFalse(z["proof_condition_fulfilled"])

    def test_08_both_cuts_without_source_J_independence_NOT_enough(self):
        for s in (2,4):
            z=check_source_finite(planted_source(s,"drop_J_independence"))
            self.assertGreater(z["actual_original_J_conflicts"],0)
            self.assertTrue(z["x_cut_enabled"] and z["y_cut_enabled"])
            self.assertGreaterEqual(z["physical_improper_C6"],1)
            self.assertEqual(z["original_source_distinct_points"],5)
            self.assertEqual(z["original_source_distinct_lines"],6)
            self.assertFalse(z["proof_condition_fulfilled"])

    def test_09_true_selected_F_may_DROP_other_diagonal_without_source_cloning(self):
        for s in (2,4):
            c=planted_source(s,"proper")
            owner,_=true_owned_edges(c,c["ids"])
            selected,_,_=two_cuts(c,c["ids"],owner,"proper")
            good={_e(c["planted"][i],c["planted"][(i+1)%6]):c["ids"][i]
                  for i in range(6)}
            self.assertEqual(len(good),6)
            self.assertTrue(all(selected[e]==i for e,i in good.items()))
            cycle=canonical_cycle(c["planted"])
            self.assertEqual(graph_first_cycles(good),(cycle,))
            self.assertEqual(inverse_x(tuple(sorted(c["ids"])),c,good),cycle)
            self.assertEqual(inverse_y(tuple(sorted(c["ids"])),c,good),cycle)

    def test_10_source_inverse_returns_empty_when_a_source_ID_missing(self):
        c=planted_source(2,"proper")
        owner,_=true_owned_edges(c,c["ids"])
        selected,_,_=two_cuts(c,c["ids"],owner,"proper")
        for i in c["ids"]:
            self.assertIsNone(inverse_x(tuple(j for j in c["ids"] if j!=i),
                                        c,selected))
            self.assertIsNone(inverse_y(tuple(j for j in c["ids"] if j!=i),
                                        c,selected))
        self.assertIsNone(inverse_x(tuple(c["ids"][:5])+(c["ids"][0],),c,selected))

    def test_11_6ID_factor_double_graph_must_fail_closed(self):
        c=planted_source(2,"drop_J_independence")
        owner,_=true_owned_edges(c,c["ids"])
        self.assertIsNone(inverse_x(c["ids"],c,owner))
        self.assertIsNone(inverse_y(c["ids"],c,owner))

    def test_12_source_dual_inverse_rejects_missing_actual_diagonal_not_imaginary(self):
        c=planted_source(2,"proper")
        owner,_=true_owned_edges(c,c["ids"])
        selected,_,_=two_cuts(c,c["ids"],owner,"proper")
        for edge in list(selected)[:2]:
            smaller=dict(selected)
            del smaller[edge]
            if edge in {_e(c["planted"][i],c["planted"][(i+1)%6])
                        for i in range(6)}:
                self.assertIsNone(inverse_x(c["ids"],c,smaller))
                self.assertIsNone(inverse_y(c["ids"],c,smaller))

    def test_13_original_duplicate_or_invalid_flag_ID_denied(self):
        c=planted_source(2,"proper")
        with self.assertRaises(ValueError):
            true_owned_edges(c,c["ids"][:5]+(c["ids"][0],))
        with self.assertRaises(ValueError):
            true_owned_edges(c,c["ids"][:5]+(-1,))
        with self.assertRaises(ValueError):
            true_owned_edges(c,c["ids"][:5]+(len(c["flags"]),))

    def test_14_cert_does_not_declare_root_proved_or_ASET_exponent(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["parent_pr"],771)
        self.assertEqual(len(c["full_physical_original_W32_W34_adversarial_rows"]),8)
        self.assertTrue(c["all_h_source_sixID_unoriented_cycle_unique_lift_proved_in_manuscript"])
        self.assertTrue(c["both_cuts_and_original_J_independence_individually_necessary_for_given_proof_sufficient_condition"])
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["global_LOW_acceptance"])
        self.assertFalse(c["general_ASET_exponent_claimed"])


if __name__=="__main__":
    unittest.main()
