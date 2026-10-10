#!/usr/bin/env python3
"""UCT-005 D1-B: deterministic text-level source/hardness dependency firewall.

This checks documentation/source metadata inventory, NOT the semantic truth
or absence of unstated proof reductions. New matching mentions fail closed.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/research/UCT-005-D1B-CONDITIONAL-DEPENDENCY-REGISTER.json"
CATALOG = ROOT / "docs/research/catalog/literature.json"
SENSITIVE = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:3SUM|APSP|SETH|OVH|OMv|"
    r"Exact[\s-]+Triangle|Zero[\s-]+Weight[\s-]+[kK][\s-]+Clique)"
    r"(?![A-Za-z0-9])"
)
PUBLICATION_FIELDS = ("title", "summary_ru", "limits_ru")
KINDS = {
    "ALGORITHM_TITLE_NO_HARDNESS", "APSP_ALGORITHM_NOT_HARDNESS",
    "SCOPED_SOURCE_AUDIT", "BIBLIOGRAPHY_NAVIGATION",
    "SETH_INDEPENDENT_CONDITIONAL_PRIOR_ART",
    "REFUTATION_SOURCE_NO_NEW_MATHLAB_THEOREM",
}


def doc_mentions(root, excluded):
    """Return sorted (repo-relative path, line number, matched source line)."""
    seen = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".json"}:
            continue
        rel = path.relative_to(root).as_posix()
        if rel in excluded or any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if SENSITIVE.search(line):
                seen.append((rel, number, line.strip()))
    return seen


def audit_docs(manifest, root):
    expected = manifest["documented_occurrences"]
    errors = []
    used = set()
    for path, line_no, line in doc_mentions(root, set(manifest["excluded_paths"])):
        matching = [index for index, item in enumerate(expected)
                    if item["path"] == path and item["anchor"] in line]
        if len(matching) != 1:
            errors.append(f"{path}:{line_no}: UNREVIEWED_HARDNESS_MENTION ({len(matching)} anchors)")
        elif matching[0] in used:
            errors.append(f"{path}:{line_no}: DUPLICATED_ANCHOR {expected[matching[0]]['anchor']}")
        else:
            index = matching[0]
            used.add(index)
            if line != expected[index].get("expected_line"):
                errors.append(f"{path}:{line_no}: CHANGED_REVIEWED_MENTION {expected[index]['anchor']}")
    for index, item in enumerate(expected):
        if item["kind"] not in KINDS:
            errors.append(f"{item['path']}: unknown classification {item['kind']}")
        if index not in used:
            errors.append(f"{item['path']}: MISSING_EXPECTED_ANCHOR {item['anchor']}")
    return errors


def audit_catalog(manifest, entries):
    expected = {item["lit_id"]: item for item in manifest["catalog_occurrences"]}
    errors = []
    used = set()
    for entry in entries:
        matched = sorted(key for key in PUBLICATION_FIELDS
                         if SENSITIVE.search(entry.get(key, "")))
        if not matched:
            continue
        lid = entry["id"]
        item = expected.get(lid)
        if item is None:
            errors.append(f"{lid}: UNREVIEWED_CANONICAL_HARDNESS_MENTION {matched}")
        elif (entry.get("identity") != item["identity"]
              or matched != sorted(item["fields"])
              or any(entry.get(field) != item.get("expected_values", {}).get(field)
                     for field in matched)):
            errors.append(f"{lid}: SOURCE_IDENTITY_OR_FIELDS_MISMATCH {matched}")
        elif item["kind"] not in KINDS:
            errors.append(f"{lid}: invalid classification {item['kind']}")
        else:
            used.add(lid)
    for lid in expected.keys() - used:
        errors.append(f"{lid}: MISSING_EXPECTED_CATALOG_MENTION")
    return errors


def audit(root=ROOT, manifest_path=MANIFEST, catalog_path=CATALOG):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    errors = []
    if manifest.get("schema") != "mathlab.fine_grained_dependency_audit.v1":
        errors.append("UNKNOWN_AUDIT_SCHEMA")
    if manifest.get("source", {}).get("id") != "LIT-357":
        errors.append("CHANGED_2026_BREAKTHROUGH_ANCHOR")
    errors.extend(audit_docs(manifest, root))
    errors.extend(audit_catalog(manifest, catalog["entries"]))
    return errors


def main():
    errors = audit()
    if errors:
        for error in errors:
            print("UCT005_D1B_AUDIT_ERROR:", error)
        raise SystemExit(1)
    print("UCT005_D1B_CONDITIONAL_HARDNESS_INVENTORY_PASS")
    print("UCT005_D1B_NO_DIRECT_TEXTUAL_3SUM_APSP_DEPENDENCY_FOUND")
    print("UCT005_D1B_IMPLICIT_PROOF_DEPENDENCIES_NOT_EXCLUDED")
    print("UCT005_ROOT_OPEN")


if __name__ == "__main__":
    main()
