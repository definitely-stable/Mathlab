"""Independent genuine ORIGINAL path-P3 literal physical compatibility checks."""
from fractions import Fraction
import unittest

from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_three_owner_joint_ports_referee import (
    CASES,_joint_original_three_owner_ports,_true_original_joint_middle_moment,
)
from hyp105_original_codegree_priority_referee import (
    _original_three_owner_codegree_selector_envelope,
)
from hyp105_original_signed_physical_pair_charge_referee import (
    _original_independent_physical_pair_good,
)
from hyp105_original_pathwise_corner_charge_referee import (
    SCHEMA,STATUS,EXPECTED,B75,_physical_original_pathwise_charges,
    canonical_report,
)


class TestOriginalTruePhysicalPathwiseCorner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_root_scope_and_complete_finite_census(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["issue"],230)
        self.assertEqual(r["status"],STATUS)
        self.assertTrue(r["universal_all_h_original_pathwise_correction_identity_proved"])
        self.assertTrue(r["universal_all_h_strict_B75_requires_one_real_heavy_path_proved"])
        self.assertFalse(r["universal_all_h_B75_for_all_fixed_correlated_f_g_proved"])
        self.assertFalse(r["root_original_all_label_seven_motif_Omega_s6_proved"])
        self.assertFalse(r["ASET_exponent_claimed"])
        rows=r["complete_genuine_original_source_cases"]
        self.assertEqual(
            [(z["s"],z["scheme"],z["retained_original_CORE"]) for z in rows],
            list(CASES))
        self.assertEqual([z["counts"]["true_original_physical_proper_P3"]
                          for z in rows],list(EXPECTED))

    def test_all_eight_signed_lower_valid_and_never_deteriorates(self):
        for z in self.report["complete_genuine_original_source_cases"]:
            M=Fraction(z["exact_original_M"])
            B=Fraction(z["exact_original_B"])
            G=Fraction(z["exact_original_G"])
            GL=Fraction(z["parent_SIGNCHARGE_G_lower"])
            BU=Fraction(z["parent_SIGNCHARGE_B_upper"])
            parent=Fraction(z["parent_SIGNCHARGE_B_over_M_bound"])
            L=Fraction(z["new_original_pathwise_signed_deficit_global_lower"])
            rowcap=Fraction(z["new_pathwise_signed_risk_upper_if_positive_else_one"])
            chosen=Fraction(z["best_certified_risk_upper_parent_or_pathwise"])
            self.assertEqual(M,B+G)
            self.assertTrue(0<=B<=BU and 0<GL<=G)
            self.assertEqual(parent,BU/(BU+GL))
            self.assertTrue(L<=3*G-B)
            self.assertTrue(3*GL-BU<=3*G-B)
            self.assertTrue(B/M<=chosen<=parent<1)
            self.assertEqual(chosen,min(parent,rowcap))
            self.assertEqual(z["new_pathwise_signed_strict_B75_criterion"],L>0)
            if L>0:
                self.assertLess(chosen,B75)
            self.assertFalse(z["root_PROVED_A"])

    def test_exact_sparse_pathwise_matches_INDEPENDENT_literal_physical_pair_rows(self):
        # A completely separate O(n²) oracle, NOT imported from the new
        # pathwise formula or any middle-overlap source moment routine.
        for case in (CASES[0],CASES[1],CASES[2],CASES[3]):
            c=_source(*case)
            bins,_=_joint_original_three_owner_ports(c)
            choices=sorted(bins.items(),key=lambda kv:len(kv[1]),reverse=True)[:12]
            choices+=sorted(bins.items(),key=lambda kv:kv[0])[:12]
            seen=set()
            cache={}
            for ends,group in choices:
                if ends in seen:continue
                seen.add(ends)
                enriched=[]
                for path,owners,w,oldlo,oldup in group:
                    key=tuple(sorted(owners))
                    if key not in cache:
                        cache[key]=_original_three_owner_codegree_selector_envelope(
                            key,c["J"])
                    lo,up,_=cache[key]
                    enriched.append((path,owners,w,oldlo,oldup,lo,up))
                for idx in (2,5,6):
                    charge=_physical_original_pathwise_charges(enriched,c,idx)
                    self.assertEqual(charge["M"],charge["W"]**2)
                    self.assertEqual(len(charge["rows"]),len(enriched))
                    for n,row in enumerate(enriched):
                        literal_good=literal_bad=Fraction(0)
                        for other in enriched:
                            if _original_independent_physical_pair_good(row,other,c):
                                literal_good+=other[idx]
                            else:
                                literal_bad+=other[idx]
                        g,b,N,tail,head=charge["rows"][n]
                        self.assertEqual(g,literal_good,(case,ends,n,idx,"good"))
                        self.assertEqual(b,literal_bad,(case,ends,n,idx,"bad"))
                        self.assertEqual(g+b,charge["W"])
                        self.assertTrue(0<=b<=N)
                        self.assertTrue(0<=tail and 0<=head)
                    existing=_true_original_joint_middle_moment(enriched,c,idx)
                    self.assertEqual(charge["G"],existing["G"])
                    self.assertEqual(charge["B"],existing["B"])

    def test_real_original_heavy_path_necessity_checked_in_all_bins(self):
        # Even if no finite bin is B75-bad, independently check exact
        # necessary condition and self/corner correction for EACH
        # eligible genuine source endpoint in W32 reverse.
        c=_source(2,"reverse","full")
        bins,_=_joint_original_three_owner_ports(c)
        count=0
        for ends,group in bins.items():
            charge=_physical_original_pathwise_charges(group,c,2)
            for row,term in zip(group,charge["rows"]):
                w=row[2];good,bad,N,tail,head=term
                self.assertEqual(bad,N-w-tail-head)
                self.assertEqual(good,charge["W"]-bad)
                if bad*4>3*charge["W"]:
                    self.assertGreater(N,3*charge["W"]/4+w+tail+head)
                count+=1
        self.assertEqual(count,1154)

    def test_geometry_is_NOT_misinterpreted_as_shared_rank_event_probability(self):
        # The quadratic forms are products of marginal selector weights,
        # NOT joint path-selection event probabilities. A single shared
        # source outsider yields exact rank pi=1/4, not (1/2)^3.
        from hyp105_original_full_w34_weighted_risk_referee import _rank_probability3
        J=[{3},{3},{3},{0,1,2}]
        self.assertEqual(_rank_probability3((0,1,2),J),Fraction(1,4))
        self.assertNotEqual(_rank_probability3((0,1,2),J),Fraction(1,8))

    def test_abstract_five_conflicting_paths_witness_is_algebraic_only(self):
        # Standalone positive-cone adversarial falsifier (NOT a claimed
        # realizable original W32/W34 source). Five equal-weight fully
        # conflicting paths: B/M=4/5 and each path sees bad-neighbor=4/5.
        z=[Fraction(1,5)]*5
        W=sum(z)
        G=sum(w*w for w in z)
        B=W*W-G
        self.assertEqual(B/(B+G),Fraction(4,5))
        for w in z:
            self.assertGreater((W-w)/W,B75)
        # This ensures theorem is conditional; no claim "every abstract
        # compatibility matrix automatically satisfies B75".

    def test_invalid_physical_endpoints_refused(self):
        c=_source(2,"lex","full")
        bins,_=_joint_original_three_owner_ports(c)
        items=list(bins.items())
        a=items[0][1][0]
        b=next(g[0] for k,g in items if k!=items[0][0])
        with self.assertRaises(AssertionError):
            _physical_original_pathwise_charges((a,b),c,2)
        with self.assertRaises(ValueError):
            _physical_original_pathwise_charges((),c,2)

    def test_complete_local_population_partition(self):
        for z in self.report["complete_genuine_original_source_cases"]:
            count=z["counts"]
            self.assertLessEqual(
                count["strict_pathwise_row_B75_certified_endpoint_bins"],
                count["ordered_true_original_physical_endpoint_bins"])
            self.assertEqual(
                count["true_local_B75_fail_or_equality_endpoint_bins"],0)


if __name__=="__main__":
    unittest.main()
