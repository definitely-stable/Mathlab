"""AA4-BY: independent minimax, REAL ORIGINAL sixflag edge-exclusion falsifiers."""
import unittest
from collections import Counter,deque
from fractions import Fraction
from itertools import product
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import apply_disjoint_factor_swaps
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,exact_boolean_high_pass_operator_norm,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    CUBE6_INDEPENDENT_HIGH_PASS,CUBE6_IMPROVEMENT,
    independent_sixcube_highpass_certificate,
    original_six_packet_source_line_A,
    physical_right_is_six_vertex_two_regular,
    assert_one_edge_swap_exclusion,
    original_six_Q_exact_poincare_identity,
    refined_original_W32_f_only_all_seven_kernel,
    refined_original_W32_all64_center_certificate,
)
PACKETS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))

def independent_weighted_bipartite_cube_MWIS(K,sign):
    """Entirely independent exact 64-vertex max-flow dual oracle.

    Max weight independent vertex set of 6cube = positive clipped vertex
    total minus minimum weighted vertex cover via bipartite mincut.
    Edmonds-Karp with integer capacities, no external installed graph lib.
    """
    n=len(K);k=n.bit_length()-1
    if n!=1<<k:raise ValueError("power of two K needed")
    source=n;sink=n+1
    weights=[max(0,sign*v) for v in K]
    cap=[{} for _ in range(n+2)]
    def add(u,v,w):
        cap[u][v]=cap[u].get(v,0)+w
        cap[v].setdefault(u,0)
    INF=sum(weights)+1
    for x,w in enumerate(weights):
        if x.bit_count()%2==0:
            add(source,x,w)
            for j in range(k):add(x,x^(1<<j),INF)
        else:add(x,sink,w)
    flow=0
    while True:
        pred={source:None}
        queue=deque([source])
        while queue and sink not in pred:
            u=queue.popleft()
            for v,w in cap[u].items():
                if w>0 and v not in pred:
                    pred[v]=u;queue.append(v)
                    if v==sink:break
        if sink not in pred:break
        push=INF;v=sink
        while pred[v] is not None:
            u=pred[v];push=min(push,cap[u][v]);v=u
        v=sink
        while pred[v] is not None:
            u=pred[v];cap[u][v]-=push;cap[v][u]+=push;v=u
        flow+=push
    return sum(weights)-flow

class Original2FactorSixPacketKernel(unittest.TestCase):
    def test_01_exact_k6_SHARP_independent_cube_walsh_maxflow(self):
        z=independent_sixcube_highpass_certificate()
        K=high_degree_boolean_kernel(6)
        self.assertEqual(independent_weighted_bipartite_cube_MWIS(K,1),72)
        self.assertEqual(independent_weighted_bipartite_cube_MWIS(K,-1),90)
        self.assertEqual(CUBE6_INDEPENDENT_HIGH_PASS,Fraction(45,32))
        self.assertEqual(CUBE6_IMPROVEMENT,Fraction(3,16))
        self.assertEqual(exact_boolean_high_pass_operator_norm(6),Fraction(51,32))
        self.assertLess(z["abstract_sharp_sixcube_independent_norm"],
                        z["general_boolean_sixcube_norm"])
        for k in (4,5):
            Kk=high_degree_boolean_kernel(k)
            scored=max(independent_weighted_bipartite_cube_MWIS(Kk,s)
                       for s in (1,-1))
            self.assertEqual(Fraction(scored,1<<k),
                             exact_boolean_high_pass_operator_norm(k))

    def test_02_original_W32_all_6_touched_REAL_Q_independent_and_Walsh_energy(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(m)
            rows=[Q for Q,_ in selected_left_six(m) if
                  original_six_packet_source_line_A(Q,inc,PACKETS,V)]
            self.assertGreater(len(rows),0)
            self.assertEqual(len(rows),351 if scheme=="lex" else 301)
            n_with_accept=0
            for Q in rows:
                accepted=assert_one_edge_swap_exclusion(Q,inc,g,PACKETS,V)
                z=original_six_Q_exact_poincare_identity(accepted)
                if z["mean_acceptance"]:n_with_accept+=1
                for mask,x in enumerate(accepted):
                    global_g=apply_disjoint_factor_swaps(
                       g,PACKETS,tuple(j for j in range(6) if mask>>j&1))
                    historical=classify_seven_prechecked(Q,f,global_g,inc)
                    self.assertEqual(int(historical is not None),x)
                    if historical is not None:
                        self.assertIn(historical,("D6","B-left/A-right","C/A"))
                self.assertLessEqual(sum(accepted),32)
            print("AA4BY_TRUE_W32_SIXPACKET_REAL_Q",scheme,
                  "source_candidates",len(rows),
                  "nonzero_true_historical_acceptance",n_with_accept,flush=True)

    def test_03_f_QUE_NCHED_all_seven_original_error_strict_and_right_g_independence(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            a=refined_original_W32_f_only_all_seven_kernel(model,PACKETS)
            old=a["prior_general_boolean_f_quenched_E"]
            new=a["sharpened_true_original_2factor_independent_f_quenched_E"]
            self.assertEqual(old-new,CUBE6_IMPROVEMENT*
               a["exact_source_line_A_six_packet_weighted_GF5_support"])
            self.assertGreater(old-new,0)
            self.assertLess(new,old)
            self.assertTrue(
                set(a["f_only_true_original_six_touch_source_Q_by_class"])
                <= {"D6","B-left/A-right","C/A"})
            swapped=dict(model,right_labels=tuple(reversed(model["right_labels"])))
            b=refined_original_W32_f_only_all_seven_kernel(swapped,PACKETS)
            self.assertEqual(a["sharpened_true_original_2factor_independent_f_quenched_E"],
                             b["sharpened_true_original_2factor_independent_f_quenched_E"])
            self.assertEqual(a["f_only_true_original_six_touch_source_Q_by_class"],
                             b["f_only_true_original_six_touch_source_Q_by_class"])
            print("AA4BY_REAL_ORIGINAL_W32_ERROR_IMPROVEMENT",scheme,
                  "prior",old,"refined",new,"reduction",old-new,flush=True)

    def test_04_TRUE_W32_full_original_ALL_SEVEN_global_64_center(self):
        for scheme in ("lex","S72"):
            data=refined_original_W32_all64_center_certificate(fixture(1,scheme),PACKETS)
            self.assertEqual(data["all_global_right_map_vertices_verified"],64)
            self.assertLess(data["new_sharpened_f_only_E"],
                            Fraction(16325377051,32) if scheme=="lex"
                            else Fraction(7806024657,16))
            self.assertLessEqual(data["new_original_center_certified_lower"],
                                 data["original_center_true_weighted_GF5"])
            self.assertGreaterEqual(data["new_original_center_certified_lower"],0)

    def test_05_real_original_source_AND_bad_Q_guards(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,_,_=_original_source(model)
        for Q,_ in selected_left_six(model):
            if original_six_packet_source_line_A(Q,inc,PACKETS,V):
                break
        for bad in ((Q[0],)*6,(Q[0],Q[1],Q[2],Q[3],Q[4],999)):
            with self.assertRaises(ValueError):
                original_six_packet_source_line_A(bad,inc,PACKETS,V)
        with self.assertRaises(ValueError):
            original_six_packet_source_line_A(Q,inc,PACKETS[:5],V)
        with self.assertRaises(ValueError):
            original_six_packet_source_line_A(Q,inc,
              ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10)),V)
        with self.assertRaises(ValueError):
            original_six_Q_exact_poincare_identity((1,)*64)
        with self.assertRaises(ValueError):
            original_six_Q_exact_poincare_identity((1,0))
        with self.assertRaises(ValueError):
            refined_original_W32_f_only_all_seven_kernel(fixture(2,"lex"),PACKETS)

    def test_06_independent_one_edge_degree_vector_2regular_combinatorics(self):
        # Exhaust all 2-regular 6-edge simple K6 graphs, independently try
        # ALL 15 original occupied edges and alternate physical pair edges.
        from itertools import combinations
        edges=tuple(combinations(range(6),2))
        motifs=0
        for Q in combinations(edges,6):
            deg=Counter(e for edge in Q for e in edge)
            if len(deg)!=6 or any(v!=2 for v in deg.values()):continue
            motifs+=1
            for dropped in Q:
                for added in edges:
                    if added==dropped:continue
                    candidate=tuple(e for e in Q if e!=dropped)+(added,)
                    deg2=Counter(x for e in candidate for x in e)
                    self.assertFalse(len(deg2)==6 and all(v==2 for v in deg2.values()))
        self.assertEqual(motifs,70)

if __name__=="__main__":
    unittest.main()
