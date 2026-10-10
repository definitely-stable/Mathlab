"""Fail-closed typed bridge contract checks; not proof validation by field presence."""
import json
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]
REGISTRY = BASE / "docs/research/UCT-005-G4-TYPED-BRIDGES.json"

CATEGORIES = frozenset({
    "CLASSICAL_DIRECT", "PROOF_INGREDIENT", "COUNTERMODEL",
    "REDUCTION_REQUIRED", "APPLICATION_ONLY",
})
VALID_STATUSES = {
    "CLASSICAL_DIRECT": frozenset({"CLASSICAL_PROVED_RESTRICTED"}),
    "PROOF_INGREDIENT": frozenset({"CLASSICAL_PROVED_RESTRICTED"}),
    "COUNTERMODEL": frozenset({"FALSE_TRANSFER_EXACT", "KNOWN_NONTRANSFER"}),
    "REDUCTION_REQUIRED": frozenset({"OPEN_REDUCTION"}),
    "APPLICATION_ONLY": frozenset({"OPEN_APPLICATION"}),
}
REQUIRED = frozenset({
    "id", "source", "target", "classification", "assumptions",
    "resource_map", "evidence", "non_transfer", "acceptance",
})


def validate_bridge_registry(data):
    if data.get("schema") != "mathlab.uct005.g4.typed_bridges.v1":
        raise ValueError("unknown bridge register schema")
    if data.get("status") != "EVIDENCE_TYPED_ATLAS_NOT_ROOT_THEOREM":
        raise ValueError("root novelty cannot be promoted by registry")
    if data.get("root_issue") != 105 or data.get("owner_issue") != 234:
        raise ValueError("incorrect scientific ownership")
    records = data.get("bridges")
    if not isinstance(records, list) or len(records) < 10:
        raise ValueError("at least 10 explicit typed links required")
    seen = set()
    for record in records:
        if not isinstance(record, dict) or set(record) != REQUIRED:
            raise ValueError("unknown, absent or free bridge record field")
        if not all(isinstance(record[k], str) and record[k].strip()
                   for k in REQUIRED):
            raise ValueError("blank bridge assumptions or explanation")
        if record["id"] in seen:
            raise ValueError("duplicate bridge identity")
        seen.add(record["id"])
        category = record["classification"]
        if category not in CATEGORIES:
            raise ValueError("invalid theorem/reduction type")
        if record["acceptance"] not in VALID_STATUSES[category]:
            raise ValueError("unproved reduction promoted to DIRECT theorem")
    return records


class TypedBridgeRegistryChecks(unittest.TestCase):
    def test_atlas_is_explicit_not_an_original_root(self):
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        records = validate_bridge_registry(data)
        self.assertGreaterEqual(len(records), 16)
        self.assertEqual(len({r["id"] for r in records}), len(records))
        self.assertEqual(len({r["classification"] for r in records}), 5)

    def test_unproved_transfer_promotion_fails_closed(self):
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        record = next(x for x in data["bridges"]
                      if x["classification"] == "REDUCTION_REQUIRED")
        original = record["classification"]
        record["classification"] = "CLASSICAL_DIRECT"
        with self.assertRaises(ValueError):
            validate_bridge_registry(data)
        record["classification"] = original
        record["assumptions"] = ""
        with self.assertRaises(ValueError):
            validate_bridge_registry(data)

    def test_root_and_duplicate_falsifiers(self):
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        data["status"] = "ROOT_ACCEPT"
        with self.assertRaises(ValueError):
            validate_bridge_registry(data)
        data["status"] = "EVIDENCE_TYPED_ATLAS_NOT_ROOT_THEOREM"
        data["bridges"].append(data["bridges"][0].copy())
        with self.assertRaises(ValueError):
            validate_bridge_registry(data)


if __name__ == "__main__":
    unittest.main()
