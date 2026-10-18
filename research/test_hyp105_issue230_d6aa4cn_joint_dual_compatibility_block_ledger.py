"""AA4-CN exact all-h original twofiber D6 compatibility K2,2 and Q-pair signed compensation."""
import unittest
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4cn_joint_dual_compatibility_block_ledger import (
    CASES,exact_original_dual_96_compatibility,
    original_twofiber_pairwise_D6_compensation_ledger,
    original_AA4CM_negative_named_and_full_ledger,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    ORBIT,FAMILIES,GRAPH_CASES,complete_overlapping_global_f,
    genuine_original_two_fiber_fixture,_cov,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import W_D


def independent_original_direct_D6_supports(model,pts,records):
    """Raw real original historical classifier on ALL 96 COMPLETE f maps."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    supports={}
    for Q,dual in records:
        states=set()
        for ix,state in enumerate(ORBIT):
            ff=complete_overlapping_global_f(f,pts,state)
            if classify_seven_all_a_original_Q(Q,ff,g,inc)=="D6":
                states.add(ix)
        supports[Q]=frozenset(states)
    if len(supports)!=len(records):
        raise AssertionError("duplicate ORIGINAL six distinct flag sets within one POINT source fiber")
    return supports


def independent_original_pair_vs_block_ledger(model,pts,ledger):
    """Independent 96-state historical sevenclass D6 pair support oracle.

    Never use the compatibility matrix to determine direct original
    Q coacceptance. Deduplicated ORIGINAL six-incidence-ID keys.
    """
    cert=ledger["physical_compatibility_certificate"]
    DA=independent_original_direct_D6_supports(
        model,pts,ledger["original_Q_active_records_A"])
    DB=independent_original_direct_D6_supports(
        model,pts,ledger["original_Q_active_records_B"])
    pre=cert["preimages_per_dual_in_96"]
    expected_joint=cert["joint_states_per_compatible_dual_pair"]
    joint=0;comp=0;M=0;M_k=Counter();K_k=Counter()
    for QA,statesA in DA.items():
        if len(statesA)!=pre:
            raise AssertionError("actual original Q positive at wrong count of global complete f maps")
        for QB,statesB in DB.items():
            if len(statesB)!=pre:
                raise AssertionError("actual original Q B positive at wrong count of global complete f maps")
            overlap=len(set(QA)&set(QB))
            M_k[overlap]+=1;M+=1
            coaccept=len(statesA & statesB)
            if coaccept not in (0,expected_joint):
                raise AssertionError("actual original Q-pair coacceptance not K2,2 block quantized")
            if coaccept:
                K_k[overlap]+=1;comp+=1;joint+=coaccept
    if M!=ledger["M_all_original_D6_Q_pairs"] or comp!=ledger["K_compatible_original_D6_Q_pairs"]:
        raise AssertionError("independent direct genuine-original classifier Q-pairs disagree with dual graph ledger")
    if dict(M_k)!=ledger["M_by_number_shared_TRUE_original_incidence_IDs"] or dict(K_k)!=ledger["K_by_number_shared_TRUE_original_incidence_IDs"]:
        raise AssertionError("independent actual ORIGINAL six-ID overlaps differ from source-dual-Q certificate")
    pA=Fraction(pre,len(ORBIT))
    pB=pA
    from_direct=Fraction(W_D*W_D)*(
        Fraction(joint,len(ORBIT))-Fraction(M)*pA*pB)
    if from_direct!=ledger["exact_original_twofiber_GF5_covariance"]:
        raise AssertionError("independent direct source GF5 pairwise covariance differs from all-h block algebra")
    return {"M":M,"K":comp,"original_full_global_Q_pair_coaccepted_state_count":joint,
            "direct_covariance":from_direct,"A_records":len(DA),"B_records":len(DB)}


class AA4CNExactOriginalBlockAndCompensation(unittest.TestCase):
    def test_01_both_four_shared_physical_completion_types_exact_96_state_K22(self):
        for case,(q,pre,mult,nb) in CASES.items():
            z=exact_original_dual_96_compatibility(case)
            self.assertEqual(z["dual_types_each"],q)
            self.assertEqual(z["preimages_per_dual_in_96"],pre)
            self.assertEqual(z["compatible_dual_pairs"],2*q)
            self.assertEqual(z["incompatible_dual_pairs"],q*q-2*q)
            self.assertEqual(z["joint_states_per_compatible_dual_pair"],mult)
            self.assertEqual(z["number_of_K2_2_blocks"],nb)
            self.assertEqual(z["binary_compatibility_matrix_rank"],nb)
            self.assertEqual(len(z["entire_96_state_joint_counter"]),2*q)
            self.assertEqual(sum(z["entire_96_state_joint_counter"].values()),96)
            self.assertEqual(z["covariance_exact_scale"],Fraction(W_D*W_D,q*q))
            self.assertEqual(z["covariance_compatible_coefficient"],Fraction(q,2))
            self.assertEqual(sum(len(A)*len(B) for A,B in z["blocks"]),2*q)
            print("AA4CN_CERT_96_K22",case,"q",q,"blocks",nb,
                  "compatible",2*q,"joint_support_preimage",mult,flush=True)
        with self.assertRaises(ValueError):
            exact_original_dual_96_compatibility("not_original_GQ")

    def test_02_genuine_original_W32_fourcycle_source_Q_pair_block_ledger(self):
        model,pts,w=genuine_original_two_fiber_fixture(1,"four_cycle_switch")
        z=original_twofiber_pairwise_D6_compensation_ledger(model,pts)
        self.assertEqual((z["s"],z["V"],z["a"]),(2,15,6))
        self.assertEqual(z["completion_case"],"four_cycle_switch")
        self.assertEqual(z["original_sixflag_Q_fiber_size_each"],3**6)
        direct=independent_original_pair_vs_block_ledger(model,pts,z)
        self.assertEqual(direct["direct_covariance"],z["reported_original_twofiber_covariance"])
        self.assertEqual(
            sum(z["signed_coefficient_by_TRUE_original_Q_incidence_overlap"].values()),
            6*z["K_compatible_original_D6_Q_pairs"]-z["M_all_original_D6_Q_pairs"])
        print("AA4CN_TRUE_ORIGINAL_W32",direct,"overlap",
              z["signed_coefficient_by_TRUE_original_Q_incidence_overlap"],flush=True)

    def test_03_genuine_original_W34_negative_FULL_original_A_fiber_exact_signed_Q_pair_conservation(self):
        r=original_AA4CM_negative_named_and_full_ledger(2)
        z=r["pairwise"];f=r["source_original"]
        self.assertEqual((z["s"],z["V"]),(4,85))
        self.assertEqual(z["completion_case"],"vertex_replacement")
        self.assertEqual(z["exact_original_twofiber_GF5_covariance"],Fraction(-10614483,32))
        self.assertEqual(12*z["K_compatible_original_D6_Q_pairs"]-z["M_all_original_D6_Q_pairs"],-6)
        direct=independent_original_pair_vs_block_ledger(
            f["actual_original_model"],f["eight_REAL_original_POINT_source_ids"],z)
        self.assertEqual(direct["direct_covariance"],Fraction(-10614483,32))
        print("AA4CN_TRUE_ORIGINAL_W34_NEGATIVE",direct,
              "by_true_incidence_overlap",z["signed_coefficient_by_TRUE_original_Q_incidence_overlap"],
              "B_C_baselines",(z["exact_invariant_historical_BC_baseline_A"],
                               z["exact_invariant_historical_BC_baseline_B"]),flush=True)

    def test_04_genuine_original_W38_exact_D6_Q_pair_cancellation_explains_ZERO_family_covariance(self):
        r=original_AA4CM_negative_named_and_full_ledger(3)
        z=r["pairwise"];f=r["source_original"]
        self.assertEqual((z["s"],z["V"]),(8,585))
        self.assertEqual(z["completion_case"],"vertex_replacement")
        self.assertEqual(z["exact_original_twofiber_GF5_covariance"],0)
        self.assertEqual(z["M_all_original_D6_Q_pairs"],
                         12*z["K_compatible_original_D6_Q_pairs"])
        direct=independent_original_pair_vs_block_ledger(
            f["actual_original_model"],f["eight_REAL_original_POINT_source_ids"],z)
        self.assertEqual(direct["direct_covariance"],0)
        self.assertGreater(z["K_compatible_original_D6_Q_pairs"],0)
        self.assertGreater(z["M_minus_K_incompatible_original_D6_Q_pairs"],0)
        print("AA4CN_TRUE_ORIGINAL_W38_ZERO_EXACT",direct,
              "by_true_incidence_overlap",z["signed_coefficient_by_TRUE_original_Q_incidence_overlap"],
              "B_C_baselines",(z["exact_invariant_historical_BC_baseline_A"],
                               z["exact_invariant_historical_BC_baseline_B"]),flush=True)

    def test_05_independent_injection_source_flag_overlap_and_baseline_cannot_change_covariance(self):
        for h in (2,3):
            r=original_AA4CM_negative_named_and_full_ledger(h)
            z=r["pairwise"]
            self.assertEqual(sum(z["M_by_number_shared_TRUE_original_incidence_IDs"].values()),
                             z["M_all_original_D6_Q_pairs"])
            self.assertEqual(sum(z["K_by_number_shared_TRUE_original_incidence_IDs"].values()),
                             z["K_compatible_original_D6_Q_pairs"])
            self.assertEqual(sum(z["signed_coefficient_by_TRUE_original_Q_incidence_overlap"].values()),
                             12*z["K_compatible_original_D6_Q_pairs"]-z["M_all_original_D6_Q_pairs"])
            self.assertTrue(z["only_original_rightA_D6_incidence_pairs_create_covariance"])
            self.assertTrue(z["same_complete_global_original_f_and_unchanged_g"])
            self.assertTrue(z["full_original_GQ_S_s_NOT_COMPUTED"])


if __name__=="__main__":
    unittest.main()
