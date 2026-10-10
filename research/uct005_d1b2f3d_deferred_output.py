#!/usr/bin/env python3
"""UCT-005 D1-B2-F3-D: exact deterministic deferred-output counting cut.

This is an elementary injection/pigeonhole restriction, not a UCT-005 root
bound, SHA preimage assumption, crash proof or general streaming lower bound.
Preverification staging is explicitly charged; side channels and copies must
be zero or counted separately.
"""
from __future__ import annotations

from dataclasses import dataclass
import json


@dataclass(frozen=True)
class PhaseCut:
    """One bit is fixed in input and overwritten in the full output.

    All sources of data-dependent information at the phase boundary:
    - digest_bits: trusted λ-bit digest (any deterministic map, not SHA decode);
    - scratch_bits: extra trusted data-dependent state, INCLUDING control;
    - preauth_stage_pages: complete P-byte remote pages written before SHA gate;
    - postauth_read_pages: complete old-source P-byte pages read after gate;
    - other_leak_bits: charged data-dependent addresses/side channels.

    No free external copy, state-dependent program/advice, external writes
    beyond those charged, stochastic failures or verification shortcuts.
    """
    source_bits: int
    page_bytes: int
    digest_bits: int
    scratch_bits: int
    preauth_stage_pages: int
    postauth_read_pages: int
    other_leak_bits: int = 0

    def __post_init__(self):
        for k in ("source_bits", "page_bytes", "digest_bits", "scratch_bits",
                  "preauth_stage_pages", "postauth_read_pages", "other_leak_bits"):
            x = getattr(self, k)
            if type(x) is not int or x < 0:
                raise ValueError(f"{k} must be a nonnegative integer")
        if self.source_bits < 1 or self.page_bytes == 0:
            raise ValueError("positive source word size and physical page")
        if self.source_bits > 1 << 20:
            raise ValueError("finite source-bit census safety bound")

    @property
    def public_target_fixed_inputs_log2(self) -> int:
        """Number of independent variable input bits in fixed-target domain."""
        return self.source_bits - 1

    @property
    def paid_phase_information_capacity(self) -> int:
        return (self.digest_bits + self.scratch_bits +
                8*self.page_bytes*(self.preauth_stage_pages +
                                   self.postauth_read_pages) +
                self.other_leak_bits)

    @property
    def exact_reconstruction_not_ruled_out_by_counting(self) -> bool:
        # Necessary, not sufficient; definitely not an existence theorem.
        return self.paid_phase_information_capacity >= self.source_bits - 1

    @property
    def provably_insufficient_bits(self) -> int:
        return max(0, self.source_bits - 1 -
                   self.paid_phase_information_capacity)

    @property
    def required_postauth_pages_if_stage_frozen(self) -> int:
        """Exact ceiling of the *necessary* counting-based page budget."""
        deficit = (self.source_bits - 1 - self.digest_bits -
                   self.scratch_bits - 8*self.page_bytes*self.preauth_stage_pages -
                   self.other_leak_bits)
        return max(0, (deficit + 8*self.page_bytes - 1)//(8*self.page_bytes))

    def report(self) -> dict:
        return {
            "status": "RESTRICTED_CLASSICAL_COUNTING_LEMMA_ONLY",
            "root_novelty": "OPEN_UNPROVED",
            "N": self.source_bits, "P": self.page_bytes,
            "lambda": self.digest_bits, "b": self.scratch_bits,
            "W_pre": self.preauth_stage_pages,
            "Q_after": self.postauth_read_pages, "A": self.other_leak_bits,
            "independent_outputs_log2": self.public_target_fixed_inputs_log2,
            "paid_information_capacity_bits": self.paid_phase_information_capacity,
            "impossibility_gap_bits": self.provably_insufficient_bits,
            "necessary_Q_after_with_fixed_stage":
                self.required_postauth_pages_if_stage_frozen,
            "necessary_not_sufficient": True,
            "cryptographic_SHA_or_physical_powerloss_claim": False,
            "full_Pareto_or_new_UCT_lower_bound": False,
        }


def abstract_deferred_output_upper(N: int, P: int, digest_budget: int,
                                   scratch_budget: int, Q: int) -> dict:
    """Construct a finite *abstract* equality witness using a freely chosen
    λ-bit digest encoding, NOT actual SHA-256 or authenticated server scheme.

    Source domain x_0=0, and output y_0=1. The first N-WQ bits include
    target and the first known non-target bits, allocated across digest+RAM.
    The last Q complete physical pages of old source are read after the gate.
    No pre-auth stage writes. This only illustrates tightness of information
    accounting up to page granularity and is NOT a secure implementation.
    """
    cut = PhaseCut(N,P,digest_budget,scratch_budget,0,Q)
    page_bits = 8*P
    if N % page_bits != 0 or Q > N // page_bits:
        raise ValueError("witness requires complete fixed-size physical pages")
    # Q may cover the entire source, including the overwritten target bit;
    # in that case the target is reset after decoding the page response.
    prefix_count = max(0, N - Q*page_bits - 1)
    if prefix_count > digest_budget + scratch_budget:
        raise ValueError("insufficient abstract digest+memory for prefix")
    if N > 16:
        raise ValueError("full independent exhaustive enumeration N<=16 only")
    used_digest = min(digest_budget,prefix_count)
    used_scratch = prefix_count - used_digest
    if used_scratch > scratch_budget:
        raise AssertionError("prefix memory allocation mistake")
    observed_words = 0
    distinct_transcripts = set()
    for other_bits in range(1 << (N-1)):
        x = other_bits << 1  # target bit 0 fixed to zero
        prefix = (x >> 1) & ((1 << prefix_count)-1)
        token = prefix & ((1 << used_digest)-1)
        state = prefix >> used_digest
        page_suffix = x >> (N-Q*page_bits) if Q else 0
        # Fixed public schedule: read exactly the last Q complete pages;
        # the observed P-byte images carry the corresponding bit suffix.
        transcript = (token,state,page_suffix)
        if transcript in distinct_transcripts:
            raise AssertionError("abstract encoding collided")
        distinct_transcripts.add(transcript)
        recovered_prefix = ((state << used_digest)|token)
        reconstructed = (1 | (recovered_prefix << 1))
        if Q:
            reconstructed |= page_suffix << (N-Q*page_bits)
        expected = x | 1
        if reconstructed != expected:
            raise AssertionError("wrong whole-image reconstruction")
        observed_words += 1
    return {
        "classification": "ABSTRACT_CODING_WITNESS_NOT_SHA",
        "N": N, "P": P, "lambda": digest_budget, "b": scratch_budget,
        "Q": Q, "W_pre": 0, "used_digest_bits": used_digest,
        "used_scratch_bits": used_scratch,
        "independently_enumerated_fixed_target_inputs": observed_words,
        "unique_transcripts": len(distinct_transcripts),
        "all_output_words_match_exactly": True,
        "not_an_authenticated_protocol": True,
        "root_novelty": "OPEN_UNPROVED",
    }


def report() -> dict:
    examples = [
        PhaseCut(8,1,0,6,0,0),
        PhaseCut(8,1,0,6,0,1),
        PhaseCut(1024,64,256,128,0,0),
        PhaseCut(1024,64,256,128,0,2),
        PhaseCut(1024,64,256,128,2,0),
    ]
    return {
        "root_novelty": "OPEN_UNPROVED",
        "canonical_deterministic_phase_cut": (
            "N-1 <= lambda + b + 8*P*(W_pre+Q_after) + A"),
        "necessary_not_sufficient": True,
        "cases": [x.report() for x in examples],
        "abstract_witnesses": [
            abstract_deferred_output_upper(8,1,0,7,0),
            abstract_deferred_output_upper(16,1,2,5,1),
            abstract_deferred_output_upper(16,2,0,15,0),
        ],
    }


if __name__ == "__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
