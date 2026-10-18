"""Independent AA4-CL real original W32/W34/W38 jointly coupled 96-map twofiber tests."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    S4,SWAPS,ORBIT,A_S4,GRAPH_CASES,FAMILIES,
    exact_shared_S4_spectral_certificate,s4_swap,complete_overlapping_global_f,
    original_two_fiber_same_global_96_orbit,genuine_original_two_fiber_fixture,
    _cov,_mean,_shared_gradient,shared_internal_dual_adjacencies,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import _full_pair_injection
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,classify_four_common_completion,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import _six_position_dual_cycle
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


class AA4CLExactTwoFiberScientificReferee(unittest.TestCase):
    def test_01_exact_S4_integer_spectrum_and_period2_parity_falsifier(self):
        c=exact_shared_S4_spectral_certificate()
        self.assertEqual(c["integer_traces"],(24,0,144,0,2880))
        self.assertEqual(c["eigenvalues"],(6,2,0,-2,-6))
        self.assertEqual(c["multiplicities"],(1,9,4,9,1))
        self.assertEqual(c["laplacian_eigenvalues"],(0,4,6,8,12))
        self.assertEqual(c["mixed_covariance_squared_coefficient"],Fraction(9,16))
        # S4 full 1-step random transposition is bipartite:
        # sign(permutation) has eigenvalue -6, not contracted in L2.
        def inversion_parity(sigma):
            return -1 if sum(sigma[i]>sigma[j]
                             for i in range(4) for j in range(i+1,4))%2 else 1
        vec=tuple(inversion_parity(sigma) for sigma in S4)
        self.assertEqual(sum(vec),0)
        self.assertEqual(tuple(sum(A_S4[i][j]*vec[j] for j in range(24))
                               for i in range(24)),
                         tuple(-6*v for v in vec))
        self.assertEqual(_cov(vec,vec),1)
        self.assertEqual(_cov(tuple(-x for x in vec),
                              tuple(-x for x in vec)),1)
        # Exact nonconstant smallest L=4 eigenspace extremizer
        # independently via product of (A - other_eigenvalue I)
        roots=(6,2,0,-2,-6)
        vector=[int(i==0) for i in range(24)]
        for root in roots:
            if root==2:continue
            vector=[sum(A_S4[i][j]*vector[j] for j in range(24))
                    -root*vector[i] for i in range(24)]
        self.assertTrue(any(vector))
        self.assertEqual(sum(vector),0)
        self.assertEqual(tuple(sum(A_S4[i][j]*vector[j] for j in range(24))
                               for i in range(24)),
                         tuple(2*v for v in vector))
        values={s:v for s,v in zip(S4,vector)}
        d,_other,_mixed=_shared_gradient(values,values)
        var=_cov(vector,vector)
        self.assertEqual(d/var,Fraction(4,3))
        self.assertEqual(var*var,Fraction(9,16)*d*d)
        for bad in [(0,0,0),(tuple(range(4)),2,0),
                    (tuple(range(4)),0,2)]:
            with self.assertRaises(ValueError):
                # test on valid 8-source map fixture below instead
                if bad[0]==0:s4_swap(tuple(range(4)),0,0)
                else:s4_swap(tuple(range(4)),9,10)
        print("AA4CL_SHARED_S4_INTEGER_SPECTRUM",c,
              "bipartite_period_two",True,flush=True)

    def _direct_true_original_96_referee(self,power,case):
        model,pts,w=genuine_original_two_fiber_fixture(power,case)
        s,V,a,inc,f,g,_,_=_original_source(model)
        self.assertEqual(len(set(pts)),8)
        self.assertEqual(len(set(w["QA"])&set(w["QB"])),4)
        self.assertEqual(classify_seven_all_a_original_Q(w["QA"],f,g,inc),"D6")
        self.assertEqual(classify_seven_all_a_original_Q(w["QB"],f,g,inc),"D6")
        z=original_two_fiber_same_global_96_orbit(model,pts)
        self.assertEqual(z["96_legal_COMPLETE_global_original_POINT_maps"],96)
        self.assertEqual(z["genuine_four_shared_edge_type"],case)
        fib=z["original_histograms"]
        original_Q_by_family={key:tuple(q for q,typ,cyc in fib[key]["eligible_actual_original_Q"])
                              for key in ("A","B")}
        direct={"A":{},"B":{}}
        # Independently reconstruct the TWO complete original sixflag
        # historical class sums at EACH of 96 real globally completed f.
        for state in ORBIT:
            changed=complete_overlapping_global_f(f,pts,state)
            self.assertEqual(set(changed),set(f))
            self.assertEqual(len(set(changed)),V)
            for fam,indices in FAMILIES.items():
                val=sum(R3_CERTIFIED_FLOORS.get(
                    classify_seven_all_a_original_Q(Q,changed,g,inc),0)
                    for Q in original_Q_by_family[fam])
                direct[fam][state]=val
                self.assertEqual(val,z["global_state_scores"][fam][state])
        rawA=tuple(direct["A"][state] for state in ORBIT)
        rawB=tuple(direct["B"][state] for state in ORBIT)
        self.assertEqual(_cov(rawA,rawB),z["historical_score_covariance_A_B"])
        self.assertEqual(_mean(rawA),z["historical_score_mean_A"])
        self.assertEqual(_mean(rawB),z["historical_score_mean_B"])
        ua=z["24_shared_conditional_mean_A"]
        ub=z["24_shared_conditional_mean_B"]
        self.assertEqual(_cov(tuple(ua[s] for s in S4),tuple(ub[s] for s in S4)),
                         _cov(rawA,rawB))
        self.assertLessEqual(
            z["historical_score_covariance_A_B"]**2,
            Fraction(9,16)*z["shared_squared_gradient_A"]*
                z["shared_squared_gradient_B"])
        # When only one exclusive pair swaps, the OTHER source-fiber
        # scores must be IDENTICAL; original g untouched.
        for sig in S4:
            for alpha in range(2):
                for beta in range(2):
                    self.assertEqual(
                        direct["A"][(sig,alpha,beta)],
                        direct["A"][(sig,alpha,1-beta)])
                    self.assertEqual(
                        direct["B"][(sig,alpha,beta)],
                        direct["B"][(sig,1-alpha,beta)])
        self.assertGreater(len(original_Q_by_family["A"]),0)
        self.assertGreater(len(original_Q_by_family["B"]),0)
        print("AA4CL_TRUE_ORIGINAL_TWO_FIBER",{"s":s,"case":case,
            "Q_A":len(original_Q_by_family["A"]),
            "Q_B":len(original_Q_by_family["B"]),
            "mean_A":str(z["historical_score_mean_A"]),
            "mean_B":str(z["historical_score_mean_B"]),
            "cov":str(z["historical_score_covariance_A_B"]),
            "var_A":str(z["historical_score_variance_A"]),
            "var_B":str(z["historical_score_variance_B"]),
            "grad_A":str(z["shared_squared_gradient_A"]),
            "grad_B":str(z["shared_squared_gradient_B"]),
            "mixed":str(z["shared_mixed_gradient_A_B"])},flush=True)
        return z

    def test_02_TRUE_W32_two_overlapping_fibers_C4_switched(self):
        z=self._direct_true_original_96_referee(1,"four_cycle_switch")
        self.assertEqual(z["s"],2)
        self.assertEqual(z["V"],15)
        self.assertEqual(z["a"],6)
        self.assertEqual(z["original_Q_fiber_size_each"],3**6)
        self.assertEqual(z["historical_score_covariance_A_B"],Fraction(10614483,16))
        self.assertEqual((len(z["original_histograms"]["A"]["eligible_actual_original_Q"]),
                          len(z["original_histograms"]["B"]["eligible_actual_original_Q"])),(4,5))

    def test_03_TRUE_W34_two_overlapping_fibers_vertex_replacement(self):
        z=self._direct_true_original_96_referee(2,"vertex_replacement")
        self.assertEqual(z["s"],4)
        self.assertEqual(z["V"],85)
        self.assertEqual(z["a"],14)
        self.assertEqual(z["original_Q_fiber_size_each"],5**6)
        self.assertEqual(z["historical_score_covariance_A_B"],Fraction(10614483,32))
        self.assertEqual((len(z["original_histograms"]["A"]["eligible_actual_original_Q"]),
                          len(z["original_histograms"]["B"]["eligible_actual_original_Q"])),(8,7))

    def test_04_TRUE_W38_two_overlapping_fibers_vertex_replacement(self):
        z=self._direct_true_original_96_referee(3,"vertex_replacement")
        self.assertEqual(z["s"],8)
        self.assertEqual(z["V"],585)
        self.assertEqual(z["original_Q_fiber_size_each"],9**6)
        self.assertEqual(z["historical_score_covariance_A_B"],Fraction(10614483,32))
        self.assertEqual((len(z["original_histograms"]["A"]["eligible_actual_original_Q"]),
                          len(z["original_histograms"]["B"]["eligible_actual_original_Q"])),(7,1))

    def test_05_different_original_RIGHT_vs_LEFT_completion_type_no_assumed_covariance_sign(self):
        # SAME complete original f left-cherry-C6 two-fiber geometry, but
        # change ONE COMPLETE original g (still globally injected) so
        # its eight selected real original LINE factor images form the
        # *opposite* physical C4 two-switch completion type.
        # The two true original Q_A/Q_B are still physically right C6,
        # yet their SIX original incidence-position alignment need not
        # agree at this global f. Test the nontrivial possible anti-
        # correlation rather than assuming nonnegative source covariance.
        model,pts,w=genuine_original_two_fiber_fixture(2,"vertex_replacement")
        s,V,a,inc,f,g,_,_=_original_source(model)
        line_by_point={}
        for Q in (w["QA"],w["QB"]):
            for j in Q:
                point,line=inc[j]
                if point in line_by_point and line_by_point[point]!=line:
                    raise AssertionError("genuine original shared Q line mismatch")
                line_by_point[point]=line
        self.assertEqual(set(line_by_point),set(pts))
        line_ids=tuple(line_by_point[p] for p in pts)
        self.assertEqual(len(set(line_ids)),8)
        right_edges=sum(GRAPH_CASES["four_cycle_switch"],())
        swapped_g=_full_pair_injection(V,a,dict(zip(line_ids,right_edges)))
        self.assertEqual(len(set(swapped_g)),V)
        different=dict(model,right_labels=swapped_g)
        # Source A/A pinned Q have DIFFERENT completion STRUCTURAL
        # orbit invariants: left cherry =3 adjacencies among its four
        # common original incidence-column positions, right 2switch =2.
        # Therefore neither historical D6 may be positive in ANY
        # jointly legal complete original f map of the shared 96 orbit.
        for fam in ("A","B"):
            Q=w["Q"+fam]
            positions=FAMILIES[fam]
            right=tuple(swapped_g[inc[next(
                j for j in Q if inc[j][0]==pts[i])][1]] for i in positions)
            rc=_six_position_dual_cycle(right)
            self.assertEqual(shared_internal_dual_adjacencies(rc),2)
            for state in ORBIT:
                ff=complete_overlapping_global_f(f,pts,state)
                left=_six_position_dual_cycle(tuple(ff[pts[i]] for i in positions))
                self.assertEqual(shared_internal_dual_adjacencies(left),3)
                self.assertIsNone(classify_seven_all_a_original_Q(Q,ff,swapped_g,inc))
        original=original_two_fiber_same_global_96_orbit(model,pts)
        alternate=original_two_fiber_same_global_96_orbit(different,pts)
        cov1=original["historical_score_covariance_A_B"]
        cov2=alternate["historical_score_covariance_A_B"]
        self.assertGreaterEqual(Fraction(9,16)*
                alternate["shared_squared_gradient_A"]*
                alternate["shared_squared_gradient_B"],cov2**2)
        self.assertGreater(alternate["historical_score_variance_A"],0)
        # A countercontrol, NOT a failure of the covariance theorem:
        # right physical twofactor support is valid, but its labeled
        # position-dual never aligns with B's left cherry completion
        # on ANY of the 96 legal same-global-f states. Source-B/C
        # baseline can persist, but B has zero D6 variation.
        self.assertEqual(alternate["historical_score_variance_B"],0)
        self.assertEqual(cov2,0)
        self.assertEqual(alternate["historical_score_mean_A"],Fraction(9405,8))
        self.assertEqual(alternate["historical_score_mean_B"],0)
        self.assertGreater(cov1,0)
        print("AA4CL_TRUE_W34_RIGHT_C4_VS_LEFT_CHERRY",
              "same_original_f_full",True,
              "fully_remapped_g_injected",True,
              "cov_original_cherry",str(cov1),
              "cov_alt_right_C4",str(cov2),
              "meanA",str(alternate["historical_score_mean_A"]),
              "meanB",str(alternate["historical_score_mean_B"]),
              "mixed",str(alternate["shared_mixed_gradient_A_B"]),flush=True)

    def test_06_failclosed_incompatible_original_8factor_and_invalid_maps(self):
        m,pts,w=genuine_original_two_fiber_fixture(2,"vertex_replacement")
        s,V,a,inc,f,g,_,_=_original_source(m)
        with self.assertRaises(ValueError):
            original_two_fiber_same_global_96_orbit(m,pts[:7])
        with self.assertRaises(ValueError):
            original_two_fiber_same_global_96_orbit(m,pts[:7]+pts[:1])
        with self.assertRaises(ValueError):
            complete_overlapping_global_f(f,pts,(tuple(range(4)),0,2))
        with self.assertRaises(ValueError):
            complete_overlapping_global_f(f,pts,(tuple(range(4)),0,False))
        with self.assertRaises(ValueError):
            complete_overlapping_global_f(f,pts,(tuple(range(4)),0))
        with self.assertRaises(ValueError):
            complete_overlapping_global_f(list(f[:-1])+[f[0]],pts,ORBIT[0])
        with self.assertRaises(ValueError):
            original_two_fiber_same_global_96_orbit(dict(m,left_labels=tuple(
                list(f[:pts[7]])+[f[pts[0]]]+list(f[pts[7]+1:]))),pts)
        with self.assertRaises(ValueError):
            genuine_original_two_fiber_fixture(1,"vertex_replacement")
        with self.assertRaises(ValueError):
            genuine_original_two_fiber_fixture(4,"vertex_replacement")


if __name__=="__main__":
    unittest.main()
