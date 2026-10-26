"""HYP-105 #230 AA4-K32X2 genuine source exhaustive exchange and 6-fold audit."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import (
    physical,genuine_source,planted_original_k44
)
from hyp105_saturated_k32_original_sixset_radius2 import (
    genuine_W34_protected_k32_radius_two
)
from hyp105_k32_radius2_exact_extension_count import (
    one_k32_original_two_exchange,
    independent_original_source_factor_exchange_census,
    certified_family_k32_extension_mass,
)


class TestK32ExactTwoSourceFlagExtension(unittest.TestCase):
    def test_real_W34_full_original_425_flags_brute_equal_physical(self):
        report,f,g,flags,lc,rc=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        hubs=tuple((j,j+6) for j in range(3))
        frees=tuple((j,j+6) for j in (3,4))
        full,provenance=physical(range(len(flags)),flags,f,g)
        direct=one_k32_original_two_exchange(
            hubs,frees,flags,f,g,
            full_adjacency=full,full_provenance=provenance)
        brute=independent_original_source_factor_exchange_census(
            hubs,frees,flags,f,g)
        self.assertEqual(
            set(direct["source_accepted_sixsets"]),
            brute["brute_original_source_accepted_two_swaps"])
        self.assertGreaterEqual(
            direct["two_exchange_accepted_original_D6"],2)
        self.assertEqual(
            direct["two_exchange_accepted_original_D6"],
            2*direct["true_new_common_vertices_total"])
        self.assertGreater(
            brute["independent_same_hub_repeated_point_pairs_checked"],0)
        self.assertEqual(
            set(direct["old_original_six_flags"]),
            set(report["true_original_protected_ids"]))
        self.assertTrue(direct[
            "all_h_exact_radius_two_extension_formula_proved"])

    def test_original_selected_W34_eight_flags_sharp_exact_two(self):
        report,f,g,flags,_,_=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        old=report["true_original_protected_ids"]
        extra=report["true_original_two_additional_ids"]
        restricted,provenance=physical(old+extra,flags,f,g)
        hubs=tuple((j,j+6) for j in range(3))
        frees=((3,9),(4,10))
        p=one_k32_original_two_exchange(
            hubs,frees,flags,f,g,
            full_adjacency=restricted,full_provenance=provenance)
        self.assertEqual(p["two_exchange_accepted_original_D6"],2)
        self.assertEqual(p["true_new_common_vertices_total"],1)
        self.assertEqual(
            set(p["source_accepted_sixsets"]),
            set(report["sharp_accepted_original_D6_two_replacements"]))
        fam=certified_family_k32_extension_mass(
            ((hubs,frees),),flags,f,g,
            adjacency=restricted,provenance=provenance)
        self.assertEqual(
            fam["two_exchange_D6_parent_witness_mass"],2)
        self.assertEqual(fam[
            "distinct_accepted_original_GF5_D6_sixsets"],2)
        self.assertEqual(fam["max_actual_parent_multiplicity"],1)

    def test_original_W34_misaligned_two_flags_rejected(self):
        report,f,g,flags,_,_=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        old=report["true_original_protected_ids"]
        extra=report["true_original_two_additional_ids"]
        f=list(f)
        g=list(g)
        ell_a=flags[extra[0]][1]
        ell_b=flags[extra[1]][1]
        g[ell_a],g[ell_b]=g[ell_b],g[ell_a]
        restricted,prov=physical(old+extra,flags,f,g)
        hubs=tuple((j,j+6) for j in range(3))
        frees=((3,9),(4,10))
        res=one_k32_original_two_exchange(
            hubs,frees,flags,f,g,
            full_adjacency=restricted,full_provenance=prov)
        independent=independent_original_source_factor_exchange_census(
            hubs,frees,flags,f,g)
        self.assertEqual(
            res["two_exchange_accepted_original_D6"],0)
        self.assertEqual(
            independent["brute_original_source_accepted_two_swaps"],set())

    def test_real_original_W34_grid_attains_exact_sixfold_limit(self):
        f,g,ids=planted_original_k44()
        _,_,flags=genuine_source(2)
        indexed={(hub,free):idx for (hub,free),idx in zip(
            ((hub,free) for hub in range(4) for free in range(4,8)),ids)}
        selected=tuple(indexed[h,z] for h in range(3) for z in (4,5,6))
        adjacency,provenance=physical(selected,flags,f,g)
        hubs=tuple((j,j) for j in range(3))
        frees=tuple((j,j) for j in (4,5,6))
        parents=[]
        for pair in combinations(frees,2):
            parents.append((hubs,pair))
        for pair in combinations(hubs,2):
            parents.append((frees,pair))
        cert=certified_family_k32_extension_mass(
            parents,flags,f,g,
            adjacency=adjacency,provenance=provenance)
        self.assertEqual(cert[
            "distinct_original_K32_source_sixsets"],6)
        self.assertEqual(cert[
            "two_exchange_D6_parent_witness_mass"],36)
        self.assertEqual(cert[
            "distinct_accepted_original_GF5_D6_sixsets"],6)
        self.assertEqual(cert["max_actual_parent_multiplicity"],6)
        self.assertEqual(
            cert["certified_D6_lower_numerator"],
            6*cert["certified_D6_lower_denominator"])
        self.assertTrue(cert[
            "all_h_global_sixfold_multiplicity_bound_proved"])

    def test_source_coordinate_properness_and_uniqueness_gate(self):
        report,f,g,flags,_,_=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        hubs=tuple((j,j+6) for j in range(3))
        frees=((3,9),(4,10))
        full,prov=physical(range(len(flags)),flags,f,g)
        with self.assertRaises(ValueError):
            one_k32_original_two_exchange(
                (hubs[0],hubs[0],hubs[2]),frees,flags,f,g,
                full_adjacency=full,full_provenance=prov)
        with self.assertRaises(ValueError):
            one_k32_original_two_exchange(
                hubs,((3,9),(3,10)),flags,f,g,
                full_adjacency=full,full_provenance=prov)
        with self.assertRaises(ValueError):
            certified_family_k32_extension_mass(
                ((hubs,frees),(hubs,frees)),flags,f,g,
                adjacency=full,provenance=prov)


if __name__=="__main__":
    unittest.main()
