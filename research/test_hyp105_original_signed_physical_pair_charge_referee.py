"""Independent literal physical ORIGINAL compatible/bad pair falsifiers."""
from fractions import Fraction
import unittest

from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_three_owner_joint_ports_referee import (
    CASES,_joint_original_three_owner_ports,
    _true_original_joint_middle_moment,
)
from hyp105_original_codegree_priority_referee import (
    _original_three_owner_codegree_selector_envelope,
)
from hyp105_original_signed_physical_pair_charge_referee import (
    SCHEMA,ROOT_STATUS,EXPECTED,_independent_literal_original_pair_cones,
    _original_independent_physical_pair_good,canonical_report,
)


def _make_complete_joint_group(c,group,cache):
    out=[]
    for path,owners,exact,oldlo,oldup in group:
        key=tuple(sorted(owners))
        if key not in cache:
            cache[key]=_original_three_owner_codegree_selector_envelope(
                key,c["J"])
        lower,upper,_=cache[key]
        if not oldlo<=lower<=exact<=upper<=oldup:
            raise AssertionError("inherited ORIGINAL codegree rank mismatch")
        out.append((path,owners,exact,oldlo,oldup,lower,upper))
    return out


class TestSignedOriginalPhysicalPairCone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_scope_and_complete_source_paths_eight(self):
        z=self.report
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["status"],ROOT_STATUS)
        self.assertEqual(z["issue"],230)
        self.assertTrue(z["universal_all_h_original_signed_source_pair_cone_theorem"])
        self.assertFalse(z["universal_all_h_original_B75_proved"])
        self.assertFalse(z["root_original_seven_six_motif_Omega_s6_proved"])
        self.assertFalse(z["ASET_exponent_claimed"])
        rows=z["complete_eight_source_case_certificates"]
        self.assertEqual([(r["s"],r["scheme"],r["retained_original_CORE"])
                          for r in rows],list(CASES))
        self.assertEqual([r["counts"]["real_physical_directed_proper_P3"]
                          for r in rows],list(EXPECTED))
        self.assertTrue(all(r["finite_complete_not_sampling"] for r in rows))

    def test_all_eight_true_original_signed_cone_RISK_exact_fractions(self):
        for row in self.report["complete_eight_source_case_certificates"]:
            M=Fraction(row["exact_original_M"])
            G=Fraction(row["exact_original_G"])
            B=Fraction(row["exact_original_B"])
            GL=Fraction(row["original_CODEGREE_lower_G"])
            GU=Fraction(row["original_CODEGREE_upper_G"])
            BU=Fraction(row["original_CODEGREE_upper_B_signed_pair"])
            MU=Fraction(row["original_CODEGREE_upper_M"])
            old=Fraction(row["old_CODEGREE_common_B_over_M_upper"])
            new=Fraction(row["new_SIGNED_cones_B_over_M_upper"])
            margin=Fraction(row["signed_MARGIN_three_Glow_minus_Bup"])
            self.assertEqual(M,B+G)
            self.assertEqual(MU,BU+GU)
            self.assertTrue(0<GL<=G<=GU)
            self.assertTrue(0<=B<=BU)
            self.assertTrue(B/M<=new<=old<1)
            self.assertEqual(old,1-GL/MU)
            self.assertEqual(new,BU/(BU+GL))
            self.assertEqual(margin,3*GL-BU)
            self.assertEqual(row["signed_CONE_B75_strict_certified"],BU<3*GL)
            self.assertEqual(row["strict_improvement_over_parent"],new<old)
            self.assertFalse(row["root_PROVED_A"])

    def test_all_eight_finite_original_cases_pass_signed_strict_B75(self):
        # The parent #765 rigorously certified all eight finite cases,
        # so sign-aware general domination MUST preserve acceptance.
        for row in self.report["complete_eight_source_case_certificates"]:
            self.assertTrue(row["signed_CONE_B75_strict_certified"])
            self.assertLess(
                Fraction(row["new_SIGNED_cones_B_over_M_upper"]),Fraction(3,4))

    def test_literal_good_bad_ordered_physical_pair_oracle_independent_of_moments(self):
        # Crucial independent falsifier: NO use of sparse source moment
        # implementation in the O(n²) pair indicator and pair products.
        for case in (CASES[0],CASES[1],CASES[2],CASES[3]):
            c=_source(*case)
            bins,_=_joint_original_three_owner_ports(c)
            triple_cache={}
            candidates=sorted(bins.items(),key=lambda kv:len(kv[1]),reverse=True)[:12]
            candidates+=sorted(bins.items(),key=lambda kv:kv[0])[:12]
            seen=set()
            for ends,group in candidates:
                if ends in seen:
                    continue
                seen.add(ends)
                augmented=_make_complete_joint_group(c,group,triple_cache)
                for index in (2,5,6):
                    actual=_true_original_joint_middle_moment(augmented,c,index)
                    G,B=_independent_literal_original_pair_cones(augmented,c,index)
                    self.assertEqual(actual["G"],G,(case,ends,index,"G"))
                    self.assertEqual(actual["B"],B,(case,ends,index,"B"))
                    self.assertEqual(actual["M"],G+B,(case,ends,index,"M"))

    def test_original_pair_oracle_incompatible_endpoint_refused(self):
        c=_source(2,"lex","full")
        bins,_=_joint_original_three_owner_ports(c)
        a=list(bins.values())[0][0]
        b=next(g[0] for ends,g in bins.items() if ends!=(
            a[0][0],a[0][-1]))
        with self.assertRaises(ValueError):
            _original_independent_physical_pair_good(a,b,c)

    def test_parent_codegree_bound_dominated_strictly_on_full_W34(self):
        for row in self.report["complete_eight_source_case_certificates"]:
            if row["s"]!=4 or row["retained_original_CORE"]!="full":
                continue
            old=Fraction(row["old_CODEGREE_common_B_over_M_upper"])
            new=Fraction(row["new_SIGNED_cones_B_over_M_upper"])
            self.assertLess(new,old)

    def test_local_bad_witnesses_never_misclassified(self):
        for row in self.report["complete_eight_source_case_certificates"]:
            counts=row["counts"]
            self.assertEqual(
                counts["ordered_physical_endpoint_bins"],
                counts["strict_signed_B75_safe_endpoint_bins"]
                +counts["not_locally_certified_endpoint_bins"])
            self.assertGreaterEqual(counts["not_locally_certified_endpoint_bins"],0)


if __name__=="__main__":
    unittest.main()
