#!/usr/bin/env python3
"""DAG-002 x ALG-001 G1-C1: finite online transition viability, not a novel theorem.

Exact deterministic binary overwrite cells. A decoder is a fixed public table.
An unlimited-read updater may choose successors within the net-write budget;
for R_u<=1 and W_phys<=1 a *single stateless read/overwrite program* must
work uniformly on a closed set, with no public changing epoch side channel.
"""
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class OnlineModel:
    output_bits: int
    remote_bits: int
    net_writes: int
    decoder: tuple[int, ...]
    deltas: tuple[int, ...]

    def __post_init__(self):
        fields = (self.output_bits, self.remote_bits, self.net_writes)
        if any(type(v) is not int for v in fields):
            raise ValueError("model dimensions must be integers, not booleans")
        if not (1 <= self.output_bits <= 4 and 0 <= self.remote_bits <= 4):
            raise ValueError("finite oracle supports n=1..4, N=0..4")
        if not 0 <= self.net_writes <= self.remote_bits:
            raise ValueError("invalid net-write budget")
        if (type(self.decoder) is not tuple or
            len(self.decoder) != (1 << self.remote_bits) or
            any(type(v) is not int or not 0 <= v < (1 << self.output_bits)
                for v in self.decoder)):
            raise ValueError("decoder must be a complete fixed output table")
        if (type(self.deltas) is not tuple or not self.deltas or
            len(set(self.deltas)) != len(self.deltas) or
            any(type(v) is not int or not 0 <= v < (1 << self.output_bits)
                for v in self.deltas)):
            raise ValueError("delta commands must form a nonempty distinct alphabet")

    @property
    def states(self):
        return range(1 << self.remote_bits)

    def target(self, state, delta):
        return self.decoder[state] ^ delta


def successors(model, state, delta, allowed=None):
    """Exact net-Hamming successors, update reads unbounded, no fresh clock."""
    if state not in model.states or delta not in model.deltas:
        raise ValueError("invalid state or delta")
    available = model.states if allowed is None else allowed
    return tuple(other for other in available
                 if (state ^ other).bit_count() <= model.net_writes
                 and model.decoder[other] == model.target(state, delta))


def online_kernel(model):
    """Greatest closed invariant for arbitrary-length adversarial delta sequences.

    A fixed memoryless controller exists from a state iff the state survives.
    Update R_u is UNBOUNDED here (reading all N bits suffices); this cannot
    establish viability under a finite R_u budget.
    """
    live = set(model.states)
    while True:
        doomed = {s for s in live
                  if any(not successors(model, s, delta, live)
                         for delta in model.deltas)}
        if not doomed:
            return frozenset(live)
        live.difference_update(doomed)


def probe_programs(remote_bits, update_reads):
    """All stateless binary overwrite programs for R_u<=1, W_phys<=1.

    Program (read_address or None, action_if_0, action_if_1), where
    action is None (no-op) or (address, constant bit). Addresses/public
    action tables are fixed across epochs; no XOR-write or free epoch.
    """
    if type(remote_bits) is not int or not 0 <= remote_bits <= 3:
        raise ValueError("uniform oracle limited to N<=3")
    if type(update_reads) is not int or update_reads not in (0, 1):
        raise ValueError("uniform oracle supports R_u in {0,1}")
    acts = (None,) + tuple((addr, bit)
                           for addr in range(remote_bits) for bit in (0, 1))
    programs = [(None, a, a) for a in acts]
    if update_reads:
        programs.extend((addr, zero, one)
                        for addr in range(remote_bits)
                        for zero, one in product(acts, repeat=2))
    return tuple(programs)


def apply_probe_program(word, program):
    addr, zero, one = program
    action = zero if addr is None or not ((word >> addr) & 1) else one
    if action is None:
        return word
    position, bit = action
    return (word & ~(1 << position)) | (bit << position)


def uniform_online_witness(model, update_reads, initial):
    """Exhaustively find one *common* stateless program per delta.

    A single program must work on all states of a nonempty closed invariant;
    the invariant contains 'initial'. Only N<=3 and at most one physical
    overwrite are supported, and programs need not charge codebook bits.
    Unlike online_kernel this enforces uniform bounded update reads.
    Returns (invariant states, per-delta programs) or None.
    """
    if model.remote_bits > 3 or model.net_writes != 1:
        raise ValueError("requires N<=3 and W_net=1/W_phys<=1")
    if type(initial) is not int or initial not in model.states:
        raise ValueError("invalid initial state")
    candidates = probe_programs(model.remote_bits, update_reads)
    images = [(p, tuple(apply_probe_program(s, p) for s in model.states))
              for p in candidates]
    # Search ALL physical-state subsets. A witness is a single stateful-free
    # update *program per command*, not a different program per prior state.
    for bits in range(1, 1 << (1 << model.remote_bits)):
        if not (bits & (1 << initial)):
            continue
        live = tuple(s for s in model.states if bits & (1 << s))
        programs = {}
        for delta in model.deltas:
            chosen = next((p for p, image in images
                           if all((bits & (1 << image[s])) and
                                  model.decoder[image[s]] == model.target(s, delta) and
                                  (s ^ image[s]).bit_count() <= model.net_writes
                                  for s in live)), None)
            if chosen is None:
                break
            programs[delta] = chosen
        if len(programs) == len(model.deltas):
            return frozenset(live), programs
    return None


def spoke_counterexample():
    """Four labels in a binary Hamming radius-1 ball, no infinite viability."""
    # 000->00, 001->01, 010->10, 100->11; all other words map to 00.
    return OnlineModel(2, 3, 1, (0, 1, 2, 0, 3, 0, 0, 0), (0, 1, 2, 3))


def syndrome_model():
    """n=2, N=3 fixed Hamming-column parity syndrome from classical coding."""
    return OnlineModel(2, 3, 1,
                       tuple(((s & 1) * 1) ^ (((s >> 1) & 1) * 2) ^
                             (((s >> 2) & 1) * 3) for s in range(8)),
                       (0, 1, 2, 3))


def report():
    bad, good = spoke_counterexample(), syndrome_model()
    witness = uniform_online_witness(good, 1, 0)
    assert witness is not None
    assert set(successors(bad, 0, 0)) | set(successors(bad, 0, 1)) | set(successors(bad, 0, 2)) | set(successors(bad, 0, 3)) == {0, 1, 2, 4}
    assert not online_kernel(bad)
    assert len(online_kernel(good)) == 8
    assert uniform_online_witness(good, 0, 0) is None
    print("DAG_G1C_ONLINE_ONE_SHOT_COUNTEREXAMPLE_PASS")
    print("DAG_G1C_ONLINE_FIXEDPOINT_PASS")
    print("DAG_G1C_R0_OVERWRITE_NO_GO_PASS")
    print("DAG_G1C_R1_SYNDROME_WITNESS_PASS")
    print("NOVELTY_UNPROVED_CLASSICAL_FIXEDPOINT")


if __name__ == "__main__":
    report()
