#!/usr/bin/env python3
"""D1-C1: independent, fail-closed UCT-005 F1 hypothesis falsification gate.

The only accepted outcome is scoped REJECTED / CLASSICAL_STOP / OPEN.
No same-model UCT root lower-bound theorem, crypto reduction or page durability
is derived. Incompletely charged axes are never assigned zero.
"""
from __future__ import annotations

import json
from math import ceil
from pathlib import Path

from uct005_d1b0_f1_reference import validate_contract
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1
from uct005_d1b2f3b_three_model_pareto import authenticated_streamed_PIN_audit
from uct005_d1b2f3c_onepass_speculative_pin import same_history_onepass
from uct005_d1b2f3d_deferred_output import PhaseCut
from uct005_d1b2f3e_failure_amp import (
    between_pass_F2_mutation, compare_preverification_fault,
)
from uct005_d1c0_observation_entropy import (
    distinguishable_tuples, exact_minimum_fixed_bits,
    independent_labeled_receipt_oracle,
)

PATH = (Path(__file__).resolve().parents[1] /
        "docs/research/UCT-005-G3-B2-D1C1-CANDIDATE-GATE.json")
ALLOWED = frozenset({
    "REJECTED_SCOPED_F0", "REJECTED_SCOPED_OBSERVATION",
    "REJECTED_SCOPED_F1_UPPER", "STOP_NOVELTY_CLASSICAL",
    "OPEN_UNFORMULATED",
})
EXPECTED = (
    ("C1-F0-BIT-PRODUCT", "honest_fenwick_upper_k12"),
    ("C2-OBS-INDEPENDENT-PIN", "c0_exact_reachable_entropy"),
    ("C3-TWO-PASS-NECESSITY", "f3c_one_pass_billed"),
    ("C4-F2-ZERO-ABORT-WRITES", "f3e_second_pass_toctou"),
    ("C5-PIN-TOKEN-IMAGE-MULTIPLICITY", "f3b_same_epoch_deduplicated_retention"),
    ("C6-F3C-ALL-AXIS-DOMINATES-F2", "f3e_invalid_preauth_stage"),
    ("C7-F3D-ORIGINAL-UCT-ROOT", "f3d_elementary_counting_only"),
    ("C8-EXISTENCE-STRONGER-JOINT-F1", "NONE_YET"),
)


def validate_matrix(matrix: dict) -> dict:
    if type(matrix) is not dict or matrix.get("schema") != (
            "mathlab.uct005.d1c1.falsification.v1"):
        raise ValueError("unfrozen hypothesis schema")
    if matrix.get("root_status") != "OPEN_UNPROVED":
        raise ValueError("root theorem must remain unproved")
    spec = validate_contract()
    axis_set = set(matrix.get("full_f1_axes", ()))
    required_axes = set(spec["coordinates"]) - {
        "n", "H", "lambda", "epsilon", "P",
    }
    if axis_set != required_axes:
        raise ValueError("incomplete or false F1 physical resource vocabulary")
    sources = matrix.get("primary_source_transfer")
    if not isinstance(sources, list) or len(sources) != 4:
        raise ValueError("missing primary source/mapping gates")
    for source in sources:
        if (not source.get("url", "").startswith("https://")
                or source.get("status") != "REDUCTION_REQUIRED"
                or source.get("full_text_proof_transfer") is not False
                or not source.get("model")):
            raise ValueError("metadata-only source cannot count as proof transfer")
    items = matrix.get("candidates")
    if not isinstance(items, list) or len(items) != len(EXPECTED):
        raise ValueError("missing fixed candidate or altered finite gate")
    for expected, item in zip(EXPECTED, items):
        if item.get("id") != expected[0] or item.get("falsifier") != expected[1]:
            raise ValueError("candidate witness IDs must be pinned")
        if (item.get("status") not in ALLOWED
                or not isinstance(item.get("model"), str)
                or not item.get("claim") or not item.get("quantifiers")
                or not item.get("theorem_transfer")):
            raise ValueError("incomplete candidate or false theorem promotion")
        unknown = item.get("unpriced_f1_axes")
        if (not isinstance(unknown, list) or not unknown
                or any(axis not in axis_set for axis in unknown)):
            raise ValueError("every incomplete F1 comparator retains unknown axes")
        is_open = item["status"] == "OPEN_UNFORMULATED"
        if is_open != (item.get("novel_joint_f1_lower") is None):
            raise ValueError("OPEN must stay null and scoped rejects must be false")
        if item.get("novel_joint_f1_lower") is True:
            raise ValueError("no original UCT lower bound has been proved")
        if (item["id"] in ("C1-F0-BIT-PRODUCT", "C2-OBS-INDEPENDENT-PIN")
                and item["status"] == "REJECTED_SCOPED_F1_UPPER"):
            raise ValueError("F0 or bitmap-answer projection cannot disprove full F1")
    return matrix


def load_matrix() -> dict:
    return validate_matrix(json.loads(PATH.read_text(encoding="utf-8")))


class HonestFenwick:
    """Distinct F0 honest bit-cell comparator; NEVER presented as F1 security."""
    def __init__(self, n: int):
        if type(n) is not int or n < 2 or n & (n-1):
            raise ValueError("power-of-two n>=2 for frozen upper")
        self.n = n
        self.raw = [0]*n
        self.tree = [0]*(n+1)

    def set(self, index: int, bit: int) -> tuple[int,int]:
        if type(index) is not int or not 0 <= index < self.n or bit not in (0,1):
            raise ValueError("invalid SET")
        reads = 1  # old raw bit fetch is explicitly paid
        if self.raw[index] == bit:
            return reads, 0
        self.raw[index] = bit
        writes = 1  # changed raw cell
        pos = index+1
        while pos <= self.n:
            self.tree[pos] ^= 1
            writes += 1
            pos += pos & -pos
        return reads,writes

    def _prefix(self, end: int) -> tuple[int,int]:
        p=0
        reads=0
        while end:
            p ^= self.tree[end]
            reads += 1
            end -= end & -end
        return p,reads

    def parity(self, lo: int, hi: int) -> tuple[int,int]:
        if type(lo) is not int or type(hi) is not int or not 0<=lo<hi<=self.n:
            raise ValueError("invalid half-open interval")
        a,ra=self._prefix(lo)
        b,rb=self._prefix(hi)
        return a^b,ra+rb


def fenwick_witness() -> dict:
    n=1<<12
    k=12
    a=HonestFenwick(n)
    worst_w=worst_q=0
    # Distinct actual updates from zero so all bit-cell write ledgers are paid.
    for i in range(n):
        reads,writes=a.set(i,1)
        if reads != 1 or writes > k+2:
            raise AssertionError("honest F0 SET upper was violated")
        worst_w=max(worst_w,writes)
    for i in range(n):
        value,reads=a.parity(i,i+1)
        if value!=1 or reads>2*k:
            raise AssertionError("Fenwick exact bit/query budget violated")
        worst_q=max(worst_q,reads)
    if (k+2)*(2*k)>=n or worst_q*worst_w>=n:
        raise AssertionError("claimed Fenwick falsifier is not asymptotically witnessed")
    return {"model":"F0_HONEST_BIT_CELL","n":n,
            "remote_raw_plus_tree_bit_cells":2*n,
            "max_actual_remote_changed_bits_per_set":worst_w,
            "max_observed_remote_query_reads":worst_q,
            "worst_case_analytic_write_upper":k+2,
            "worst_case_analytic_query_upper":2*k,
            "analytic_product_upper":(k+2)*(2*k),
            "f1_authenticated_protocol":False}


def observation_witness() -> dict:
    times=(0,2,3)
    n=5
    count=distinguishable_tuples(n,times)
    bits=exact_minimum_fixed_bits(count)
    receipts=independent_labeled_receipt_oracle(4,3)
    if (count,bits)!=(3072,12) or receipts[
            "distinct_initial_plus_labeled_SET_transcripts"]!=8192:
        raise AssertionError("online reachable bitmap and author receipts conflated")
    if receipts["distinct_bitmap_answer_paths_only"]!=2000:
        raise AssertionError("labeled author histories were incorrectly identified")
    return {"model":"OBSERVATION_ONLY_NAMED_EPOCHS",
            "n":n,"times":list(times),
            "distinct_answer_tuples":count,
            "exact_minimum_fixed_bits":bits,
            "naive_independent_bits":n*len(times),
            "distinct_labeled_SET_trajectories_n4_H3":8192,
            "distinct_bitmap_paths_n4_H3":2000,
            "signed_author_receipts_and_physical_pages":None}


def one_pass_witness() -> dict:
    z=same_history_onepass((0,1,0),1,17)
    M=ceil(ceil(2*17/8)/1)
    if (z["online_bitmap_page_reads"]["two_pass_stream"]!=11*M or
            z["online_bitmap_page_reads"]["speculative_one_pass"]!=7*M or
            z["onepass_speculative_full_page_writes_before_authentication"]!=4*M):
        raise AssertionError("F3-C one-pass counterexample missing paid staging")
    return {"model":"F1_IDEAL_PAGE_IMAGE_SPECULATIVE_STAGE",
            "P":1,"C":17,"M":M,
            "F2_online_read_pages":11*M,
            "F3C_online_read_pages":7*M,
            "F3C_preauth_full_page_writes":4*M,
            "complete_crash_durability_or_SHA_reduction":False}


def changed_between_scans_witness() -> dict:
    r=between_pass_F2_mutation(17,1)
    z=r["F2_after_pass1_failure_cost"]
    if (z["stage_page_writes"]!=r["M"]
            or z["abort_stage_drop_calls"]!=r["M"]
            or z["trusted_root_publications"]!=0):
        raise AssertionError("F2 failed mutation wrongly called zero-write")
    return {"model":"F1_IDEAL_PAGE_IMAGE_ADVERSARIAL_SECOND_PASS",
            "F2_aborted_stage_page_writes":z["stage_page_writes"],
            "F2_cleanup_drop_calls":z["abort_stage_drop_calls"],
            "trusted_publications":z["trusted_root_publications"]}


def duplicate_pin_witness() -> dict:
    m=StreamedPinBitmapF1((0,1,0),1,8)
    m.pin_current(0)
    m.pin_current(1)
    m.set(1,1)
    audit=authenticated_streamed_PIN_audit(m)
    S=m._pages_per_snapshot()
    if (audit["PIN_entries"]!=2 or audit["PIN_epochs"]!=(0,)
            or audit["extra_PIN_page_images"]!=S):
        raise AssertionError("same epoch must not duplicate physical snapshot")
    return {"model":"F1_IDEAL_PAGE_IMAGE_INDEPENDENT_READERS",
            "PIN_entries":2,"distinct_retained_PIN_epochs":1,
            "retained_remote_snapshot_pages":S,
            "offline_authenticated_audit_reads":audit["offline_PIN_scan_pages"],
            "ideal_authority_and_local_PIN_roots_are_paid":True}


def failed_stage_witness() -> dict:
    z=compare_preverification_fault(C=17,P=1,kind="preexisting_wrong_SHA")
    two,one=z["two_pass"],z["one_pass"]
    if (two["stage_page_writes"]!=0
            or one["stage_page_writes"]!=z["M"]
            or one["abort_stage_drop_calls"]!=z["M"]):
        raise AssertionError("F2/F3-C all-axis comparison omitted failure writes")
    return {"model":"F1_IDEAL_PAGE_IMAGE_PREEXISTING_INVALID_SHA",
            "M":z["M"],"F2_stage_page_writes":0,
            "F3C_stage_page_writes":one["stage_page_writes"],
            "F3C_cleanup_drop_address_bytes":
                one["abort_stage_drop_address_bytes"],
            "F2_and_F3C_full_system_Pareto":None}


def counting_witness() -> dict:
    cut=PhaseCut(80,1,8,8,0,0)
    if cut.required_postauth_pages_if_stage_frozen!=8:
        raise AssertionError("elementary deferred output count changed")
    paid=PhaseCut(80,1,8,8,8,0)
    if paid.required_postauth_pages_if_stage_frozen!=0:
        raise AssertionError("pre-auth stage bits were not charged")
    return {"model":"RESTRICTED_DETERMINISTIC_DEFERRED_OUTPUT",
            "N":80,"lambda":8,"b":8,"P":1,
            "minimal_post_auth_read_pages_without_stage":8,
            "minimal_post_auth_reads_with_eight_staged_pages":0,
            "only_classical_pigeonhole_injection":True,
            "novel_UCT_root":False}


def report() -> dict:
    matrix=load_matrix()
    evidence=(
        fenwick_witness(), observation_witness(), one_pass_witness(),
        changed_between_scans_witness(),duplicate_pin_witness(),
        failed_stage_witness(),counting_witness(),
        {"model":"F1_FULL_COMPUTATIONAL_ADVERSARIAL",
         "result":"OPEN_UNFORMULATED","quantified_joint_formula":None},
    )
    if len(evidence)!=len(matrix["candidates"]):
        raise AssertionError("candidate/counterexample mismatch")
    rows=[]
    for item,witness in zip(matrix["candidates"],evidence):
        # The final OPEN candidate cannot be elevated because there is no
        # fully priced lower-bound theorem or complete theorem transfer.
        if item["status"]=="OPEN_UNFORMULATED" and (
                witness["quantified_joint_formula"] is not None):
            raise AssertionError("candidate unexpectedly promoted to theorem")
        rows.append({
            "candidate":item["id"],"scope":item["model"],
            "decision":item["status"],"theorem_transfer":item["theorem_transfer"],
            "unpriced_f1_axes":{axis:None for axis in item["unpriced_f1_axes"]},
            "actual_finite_witness":witness,
            "root_novelty":"OPEN_UNPROVED",
        })
    return {
        "classification":"D1_C_SCOPED_FALSIFICATION_AND_PRIOR_TRANSFER_STOP",
        "root_novelty":"OPEN_UNPROVED",
        "strict_novel_joint_lower_bound_proved":False,
        "primary_theorem_full_text_transfer":False,
        "candidates":rows,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
