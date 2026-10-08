"""G2B-B2 independent CNF source verifier and safe verdict tests."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from hashlib import sha256

from g2bb2_anchor_sat import build_atleast_cnf, formula_source_hash
from g2bb2_verify import (
    independently_enumerated_graph, independently_validate_witness,
    verify_artifacts, verify_model_source,
)
from lent_hypergraph import build_forbidden_hypergraph


class G2BB2CertificateTests(unittest.TestCase):
    def test_independent_full_source_reconstruction(self):
        columns,edges=independently_enumerated_graph()
        graph=build_forbidden_hypergraph(5,3,2)
        self.assertEqual(columns,graph.columns)
        self.assertEqual(edges,graph.edges)
        self.assertEqual((len(columns),len(edges)),(60,9990))
        source_hash,dimacs=verify_model_source()
        self.assertEqual(source_hash,formula_source_hash(graph))
        self.assertEqual(dimacs,build_atleast_cnf(graph,11,True).dimacs())

    def test_unknown_status_not_mislabelled_exact(self):
        h,cnf=verify_model_source()
        with TemporaryDirectory() as tmp:
            p=Path(tmp)
            (p/"problem.cnf").write_text(cnf)
            (p/"decision.json").write_text(json.dumps({
                "status":"UNKNOWN_CONFLICT_BUDGET",
                "source_sha256":h,
                "cnf_sha256":sha256(cnf.encode()).hexdigest(),
                "exact_value":None,
            }))
            self.assertEqual(verify_artifacts(p),"UNKNOWN")
            (p/"proof.drat").write_text("0\n")
            with self.assertRaises(AssertionError):
                verify_artifacts(p)

    def test_reject_fake_sat_witness_and_fake_unsat_proof(self):
        h,cnf=verify_model_source()
        with TemporaryDirectory() as tmp:
            p=Path(tmp)
            (p/"problem.cnf").write_text(cnf)
            info={"source_sha256":h,
                  "cnf_sha256":sha256(cnf.encode()).hexdigest()}
            (p/"decision.json").write_text(json.dumps({
                **info,"status":"SAT_INDEPENDENT_WITNESS_EXACT_11",
                "exact_value":11}))
            (p/"witness.json").write_text(json.dumps({
                "q":5,"m":3,"w":2,"d":2,"V":11,
                "columns":[[0,0,i%5] for i in range(11)]}))
            with self.assertRaises(AssertionError):
                verify_artifacts(p)
            (p/"decision.json").write_text(json.dumps({
                **info,"status":"UNSAT_UNVERIFIED_CERTIFICATE_REQUIRED",
                "exact_value":None,
            }))
            (p/"proof.drat").write_text("0\n")
            with self.assertRaises((RuntimeError,AssertionError)):
                verify_artifacts(p,drat_trim="/bin/false")

    def test_witness_domain_rejection(self):
        with self.assertRaises(AssertionError):
            independently_validate_witness({
                "q":5,"m":3,"w":2,"d":2,"V":11,
                "columns":[[0,0,1]]*11
            })
        with self.assertRaises(AssertionError):
            independently_validate_witness({
                "q":5,"m":3,"w":3,"d":2,"V":11,
                "columns":[[0,0,1]]*11
            })


if __name__=="__main__":
    unittest.main()
