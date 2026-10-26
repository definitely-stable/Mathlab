"""Exact independent original-GQ and historical-class audits of quotient lifts."""
from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import tempfile
import unittest

import hyp105_issue230_quotient_charge as q


class QuotientChargeTests(unittest.TestCase):
    def test_full_minimal_maps_and_declared_errors(self):
        for r, expected in ((1,145),(2,113)):
            row=q.construct(3,r)
            self.assertEqual((row['V'],row['a'],row['holes']),(585,35,10))
            self.assertEqual(row['fine_exceptions_full'],expected)
            self.assertEqual(row['rough_exceptions_full'],97)

    def test_independent_projective_and_RREF_affine_source(self):
        row=q.source_audit(3)
        self.assertEqual(row['points'],585)
        self.assertEqual(row['lines'],585)
        self.assertEqual(row['affine_incidences'],4096)

    def test_exact_generic_and_rank_drop_triangle_counts(self):
        for r, generic, same in ((1,86016,86016),(2,129024,43008)):
            row=q.triangle_audit(3,r)
            self.assertEqual(row['generic_u_triangles'],generic)
            self.assertEqual(row['same_u_triangles'],same)

    def test_actual_six_original_incidence_witness_has_historical_CA_class(self):
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        row=q.witness_audit()
        self.assertEqual((row['lift_assignments'],row['lift_successes']),(4096,64))
        left=row['point_pairs']
        cycle=row['cycle']
        right=[tuple(sorted((cycle[i],cycle[(i+1)%6]))) for i in range(6)]
        def normalize(labels):
            symbols=sorted({x for pair in labels for x in pair})
            self.assertEqual(len(symbols),6)
            index={x:i for i,x in enumerate(symbols)}
            return tuple(tuple(index[x] for x in pair) for pair in labels)
        flags=tuple((i,j) for i in range(3) for j in (i,i+3))
        self.assertEqual(classify_seven_prechecked(tuple(range(6)),normalize(left),
                                                  normalize(right),flags),'C/A')
        self.assertEqual(sorted(Counter(p for p,l in flags).values()),[2,2,2])
        self.assertEqual(len({l for p,l in flags}),6)

    def test_frozen_certificate_is_reproduced_without_writing_source_tree(self):
        fixture=Path(__file__).parent/'fixtures/hyp105_issue230_local_transfer/quotient_charge_evidence.json'
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(StringIO()):
            q.main(Path(tmp))
            self.assertEqual(json.loads((Path(tmp)/'quotient_charge_evidence.json').read_text()),
                             json.loads(fixture.read_text()))


if __name__=='__main__':
    unittest.main()
