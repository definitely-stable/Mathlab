"""HYP-105 AA4-REFGATE — machine-checkable scientific proof-obligation index.

This is NOT a proof assistant, not peer review, and not certification of
every theorem. It checks preservation of the exact source/CORE/physical/
GF5 witness boundaries and source artifact availability, computes a
dependency graph, and rejects unsupported theorem-promotion moves.

The reviewer document remains the source of mathematical argument.
Status is intentionally OPEN_WITH_FORMAL_BLOCKER until actual external
qualified peer review, even if every GitHub Actions test passes.
"""
from dataclasses import dataclass, replace
from pathlib import Path
from collections import defaultdict
import json


@dataclass(frozen=True)
class Claim:
    id: str
    source: str
    document: str
    must_contain: tuple[str, ...]
    needs: tuple[str, ...]
    evidence_type: str = "INTERNAL_PROOF_AND_TESTS"


# Historical provenance is attributable. Each witness file exists in
# FROZEN ancestry; no new claims that old known lemmas were invented.
CLAIMS = (
    Claim("GQ", "ORIGINAL_FULL",
          "docs/research/HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md",
          ("W(3,s)", "source", "original"), ()),
    Claim("BOOK", "ORIGINAL_FULL",
          "docs/research/HYP-105-EXACT-ORIGINAL-BOOK-CORE-BUDGET.md",
          ("book", "original", "budget"), ("GQ",)),
    Claim("SS6", "EXTERNAL_GRAPH",
          "docs/research/HYP-105-BRANCH-A-ROOT-REFEREE.md",
          ("jiang", "yepremyan", "supersaturation"), (),
          "EXTERNAL_PUBLISHED_EXISTENTIAL_CONSTANTS"),
    Claim("TAIL", "ORIGINAL_FULL_TO_PHYSICAL",
          "docs/research/HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md",
          ("tail", "original", "physical"), ("GQ","BOOK","SS6")),
    Claim("CORE", "ORIGINAL_CORE",
          "docs/research/HYP-105-EXACT-ORIGINAL-BOOK-CORE-BUDGET.md",
          ("epsilon", "core", "source"), ("GQ","BOOK","TAIL")),
    Claim("D6", "PHYSICAL_TO_ORIGINAL_SIXSET",
          "docs/research/HYP-105-D6-CANONICAL-SOURCE-SIX-ID-INVERSE-REFEREE.md",
          ("rainbow", "original", "inverse"), ("GQ",)),
    Claim("SELECTOR", "ORIGINAL_CORE_TO_SELECTED",
          "docs/research/HYP-105-SELECTOR-PATH-PAIR-COVARIANCE-REFEREE.md",
          ("covariance", "jensen", "priority"), ("CORE","D6")),
    Claim("WALK6", "BIPARTITE_PHYSICAL",
          "docs/research/HYP-105-BIPARTITE-SIXWALK-MOBIUS-MOMENT-REFEREE.md",
          ("möbius", "bipartite", "six"), ("SELECTOR","D6")),
    Claim("ENDPOINT", "ORIGINAL_FULL_CORE_MIXED",
          "docs/research/HYP-105-UNIVERSAL-SEXTIC-OBSTRUCTION.md",
          ("exceptional endpoints", "projection", "proper"), ("CORE","GQ")),
    Claim("BLOCKER", "ORIGINAL_FULL_CORE_MIXED",
          "docs/research/HYP-105-MIXED-SOURCE-COLLINEARITY-ENERGY-REFEREE.md",
          ("collinearity", "full/core", "original"), ("ENDPOINT","CORE","WALK6")),
    Claim("BBO", "CORE_PATH_TO_ORIGINAL_SIXSET",
          "docs/research/HYP-105-BBO-ORIGINAL-CORE-CUBIC-POLYNOMIAL-REFEREE.md",
          ("cubic", "nonanchor", "anchor"), ("ENDPOINT","BLOCKER","GQ")),
    Claim("ROOT", "ALL_DYADIC_FIXED_MAPS",
          "docs/research/HYP-105-ORIGINAL-SELECTOR-SIXWALK-JOINT-ROOT-GATE.md",
          ("dyadic", "jensen", "graph"), ("TAIL","CORE","D6","SELECTOR",
                                      "WALK6","ENDPOINT","BLOCKER","BBO","SS6")),
    Claim("GF5", "ORIGINAL_SIXSET_TO_SIGNED_GF5",
          "docs/research/HYP-105-SHARP-TEN-SIGN-R3-FLOOR.md",
          ("51", "sign", "original"), ("D6","BBO","ROOT")),
)

TRANSFERS = (
    # source object --bridge--> target object, with exact extra witness.
    ("GQ","CORE","true_original_full_flag_deletion_keeps_unique_ids"),
    ("CORE","SELECTOR","whole_original_flag_keeps_both_real_diagonals"),
    ("SELECTOR","D6","two_typed_cuts_cherryfree_coordinate_rainbow"),
    ("CORE","ENDPOINT","full_original_projection_anchors_not_core"),
    ("ENDPOINT","BBO","three_nonanchor_core_ids_full_original_three_anchors"),
    ("BBO","GF5","six_distinct_original_ids_not_physical_multiplicity"),
    ("SELECTOR","WALK6","jensen_not_pair_path_independence"),
    ("SS6","TAIL","external_ordinary_simple_C6_constants_unknown"),
)
BRIDGE_IDS = tuple(t[2] for t in TRANSFERS)

FORBIDDEN_PROMOTIONS = (
    "full_anchor_required_in_core",
    "independent_distinct_path_events",
    "numeric_published_C_graph_equals_one",
    "numeric_published_c_graph_equals_one",
    "finite_W32_W34_implies_all_h",
    "six_physical_edges_equals_six_original_flags_without_owner_injectivity",
    "s6_derived_from_external_C6_without_balance_density_gate",
    "github_ci_equals_qualified_mathematical_referee",
    "unrestricted_aset_exponent_conclusion",
)

def validate_manifest(claims=CLAIMS,transfers=TRANSFERS):
    """Fail closed on absent proof inputs, false promotion or cycles."""
    claims=tuple(claims)
    transfers=tuple(transfers)
    names={c.id for c in claims}
    if len(names)!=len(claims) or not names:
        raise ValueError("duplicate/empty scientific claim nodes")
    if not {"GQ","BOOK","SS6","TAIL","CORE","SELECTOR","WALK6",
            "D6","ENDPOINT","BLOCKER","BBO","ROOT","GF5"}<=names:
        raise ValueError("one or more mandatory all-h original theorem inputs missing")
    graph={}
    for c in claims:
        if (c.source not in {
            "ORIGINAL_FULL","EXTERNAL_GRAPH","ORIGINAL_FULL_TO_PHYSICAL",
            "ORIGINAL_CORE","PHYSICAL_TO_ORIGINAL_SIXSET",
            "ORIGINAL_CORE_TO_SELECTED","BIPARTITE_PHYSICAL",
            "ORIGINAL_FULL_CORE_MIXED","CORE_PATH_TO_ORIGINAL_SIXSET",
            "ALL_DYADIC_FIXED_MAPS","ORIGINAL_SIXSET_TO_SIGNED_GF5"
        } or any(n not in names for n in c.needs)
            or c.id in c.needs or not c.must_contain
            or not c.document.startswith("docs/research/")
            or ".." in c.document):
            raise ValueError("invalid source scope/dependency or proof document")
        graph[c.id]=set(c.needs)
    if next(c for c in claims if c.id=="SS6").evidence_type != "EXTERNAL_PUBLISHED_EXISTENTIAL_CONSTANTS":
        raise ValueError("published C6 supersaturation not tagged as EXTERNAL")
    if next(c for c in claims if c.id=="ROOT").source != "ALL_DYADIC_FIXED_MAPS":
        raise ValueError("root cannot be promoted beyond scoped fixed original f,g")
    marks=set()
    for origin,destination,bridge in transfers:
        if (origin not in names or destination not in names or
            bridge in marks or bridge not in BRIDGE_IDS):
            raise ValueError("missing or forged typed theorem source transfer")
        marks.add(bridge)
    if marks != set(BRIDGE_IDS):
        raise ValueError("ALL original-full/core/physical/source/GF5 witness gates required")
    if (not graph["ROOT"]>={"SS6","TAIL","CORE","SELECTOR","WALK6",
                            "D6","ENDPOINT","BLOCKER","BBO"} or
        not graph["GF5"]>={"ROOT","D6","BBO"}):
        raise ValueError("root/GF5 quantitative dependency dropped")
    visited={}
    order=[]
    def visit(n):
        if visited.get(n)==1:
            raise ValueError("circular scientific source dependency")
        if visited.get(n)==2:return
        visited[n]=1
        for p in sorted(graph[n]):visit(p)
        visited[n]=2
        order.append(n)
    for n in sorted(graph):visit(n)
    return tuple(order)


def validate_scope_transfers(assumptions=None):
    """Explicit original source proof-provenance guard.

    NO positive machine attestation of mathematical correctness; this
    function checks that a claimed ROOT argument does not cross an
    object/probability/quantifier boundary without its named lemma.
    """
    assumptions=set(BRIDGE_IDS) if assumptions is None else set(assumptions)
    if assumptions & set(FORBIDDEN_PROMOTIONS):
        raise ValueError("a known scientifically invalid promotion was asserted")
    missing=set(BRIDGE_IDS)-assumptions
    if missing:
        raise ValueError("unproved original source transition(s): "+",".join(sorted(missing)))
    return {
        "mandatory_source_transfers":len(BRIDGE_IDS),
        "all_named_transfers_accounted_for":True,
        "source_full_core_anchors_distinguished":True,
        "selector_path_pair_independence_forbidden":True,
        "external_graph_constants_not_numeric":True,
        "finite_s_checks_not_all_h_proofs":True,
        "not_a_formal_or_external_proof":True,
    }


def audit_repository(root):
    root=Path(root).resolve()
    order=validate_manifest()
    scope=validate_scope_transfers()
    files=[]
    for c in CLAIMS:
        proof=(root/c.document).resolve()
        if root not in proof.parents or not proof.is_file():
            raise ValueError("missing genuine proof source: "+c.document)
        source=proof.read_text(encoding="utf-8").casefold()
        lacking=[frag for frag in c.must_contain
                if frag.casefold() not in source]
        if lacking:
            raise ValueError(f"proof source {c.id}: missing anchors {lacking}")
        files.append({"claim":c.id,"original_object_scope":c.source,
                      "evidence":c.document,"evidence_type":c.evidence_type,
                      "dependency_claims":c.needs,
                      "source_markers_verified":len(c.must_contain)})
    return {
        "milestone":"HYP-105/230",
        "scientific_acceptance":"OPEN_WITH_FORMAL_BLOCKER",
        "external_qualified_review_completed":False,
        "human_referee_needed":True,
        "real_published_graph_constants_numeric_available":False,
        "formal_proof_assistant_verification":False,
        "source_objects_scoped":len(files),
        "topological_dependency_order":order,
        "boundary_scope_guard":scope,
        "claim_documents":files,
        "warnings":[
            "Content markers, unit tests and GitHub CI do NOT independently prove mathematical lemmas.",
            "External ordinary graph C6 supersaturation constants remain existential.",
            "Actual signed HYP-105 is conditional on scoped original Branch A and GF5 inputs.",
            "No merge or root issue closure before qualified independent mathematics peer review."
        ]
    }


def json_report(root):
    return json.dumps(audit_repository(root),indent=2,ensure_ascii=False)


if __name__=="__main__":
    print(json_report(Path(__file__).resolve().parents[1]))
