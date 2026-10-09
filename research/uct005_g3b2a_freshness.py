#!/usr/bin/env python3
"""UCT-005 G3-B2-A: two-reader freshness/rollback/fork *symbolic* oracle.

No cryptographic security or byte-I/O benchmark: signature verification is an
ideal predicate for already issued, immutable full-state certificates.
A trusted publication anchor is a separate PAID communication primitive.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class SignedSnapshot:
    epoch: int
    parent_seal: str
    bits: tuple
    seal: str


class SymbolicIssuer:
    """An ideal validity predicate, NOT a server-accessible latest-time oracle."""
    def __init__(self, initial_bits):
        if not initial_bits or any(b not in (0, 1) for b in initial_bits):
            raise ValueError("nonempty binary state required")
        self._issued = {}
        self._serial = 0
        self.genesis = self._sign(0, "origin", tuple(initial_bits))

    def _sign(self, epoch, parent, bits):
        self._serial += 1
        receipt = SignedSnapshot(epoch, parent, tuple(bits),
                                 f"author-seal-{self._serial:05d}")
        self._issued[receipt.seal] = receipt
        return receipt

    def issue(self, parent, index, bit):
        if not self.verify(parent):
            raise ValueError("parent not issued by author")
        if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(parent.bits):
            raise ValueError("invalid update index")
        if bit not in (0, 1) or isinstance(bit, bool):
            raise ValueError("invalid assigned bit")
        bits = list(parent.bits)
        bits[index] = bit
        return self._sign(parent.epoch + 1, parent.seal, bits)

    def verify(self, receipt):
        return (isinstance(receipt, SignedSnapshot)
                and self._issued.get(receipt.seal) == receipt)

    def verify_checkpoint(self, checkpoint):
        issued = self._issued.get(checkpoint.seal)
        return issued is not None and issued.epoch == checkpoint.epoch

    def extends(self, later, earlier):
        """Signature/path membership; DOES NOT disclose the actual latest epoch."""
        if not self.verify(later) or not self.verify_checkpoint(earlier):
            return False
        cursor = later
        seen = set()
        while cursor.epoch > earlier.epoch:
            if cursor.seal in seen:
                return False
            seen.add(cursor.seal)
            parent = self._issued.get(cursor.parent_seal)
            if parent is None or parent.epoch != cursor.epoch - 1:
                return False
            cursor = parent
        return cursor.epoch == earlier.epoch and cursor.seal == earlier.seal

    def adversarial_double_sign(self, parent, index, bit):
        """COMPROMISED AUTHOR only. The server cannot call issue in real model."""
        return self.issue(parent, index, bit)


class TrustedAnchor:
    """Globally monotone ideal root publication; each read is a trusted call."""
    def __init__(self, genesis, issuer):
        if not issuer.verify(genesis) or genesis.epoch != 0:
            raise ValueError("genesis must be authorized")
        # Trust only epoch + seal; never store a hidden full n-bit replica.
        self.current = Checkpoint(genesis.epoch, genesis.seal)
        self.publications = 0

    def publish(self, next_receipt, issuer):
        if (not issuer.verify(next_receipt)
                or next_receipt.epoch != self.current.epoch + 1
                or next_receipt.parent_seal != self.current.seal):
            raise ValueError("nonmonotone/unauthorized anchor publication")
        self.current = Checkpoint(next_receipt.epoch, next_receipt.seal)
        self.publications += 1

    def read(self, available=True):
        return self.current if available else None


class SingleWriter:
    def __init__(self, initial_bits):
        self.issuer = SymbolicIssuer(initial_bits)
        self.anchor = TrustedAnchor(self.issuer.genesis, self.issuer)
        self.history = [self.issuer.genesis]

    def set(self, index, bit):
        receipt = self.issuer.issue(self.history[-1], index, bit)
        self.history.append(receipt)
        self.anchor.publish(receipt, self.issuer)
        return receipt


@dataclass(frozen=True)
class Checkpoint:
    epoch: int
    seal: str


@dataclass
class Reader:
    """Only the tiny durable checkpoint is stored, NEVER the full bit vector."""
    checkpoint: Checkpoint | SignedSnapshot
    n: int = 0

    def __post_init__(self):
        if isinstance(self.checkpoint, SignedSnapshot):
            supplied = self.checkpoint
            self.n = len(supplied.bits)
            self.checkpoint = Checkpoint(supplied.epoch, supplied.seal)
        if not isinstance(self.checkpoint, Checkpoint) or self.n < 1:
            raise ValueError("valid, nonempty client checkpoint required")

    def clone(self):
        return Reader(self.checkpoint, self.n)


@dataclass(frozen=True)
class Accounting:
    """Charged logical traffic; not measured network/physical cryptographic bytes."""
    issuer_full_snapshot_bits: int
    verifier_received_bits: int
    anchor_received_bits: int
    reader_trusted_checkpoint_bits: int
    server_snapshot_cell_reads: int
    anchor_calls: int
    # Byte-accurate encoding and actual hash/signer/prover work NOT implemented.


@dataclass(frozen=True)
class Answer:
    status: str
    value: int | None
    served_epoch: int | None
    costs: Accounting


@dataclass(frozen=True)
class SymbolicCostProfile:
    signature_bits: int = 256
    root_bits: int = 256
    epoch_bits: int = 32

    def __post_init__(self):
        if min(self.signature_bits, self.root_bits, self.epoch_bits) < 1:
            raise ValueError("positive fixed accounting widths required")

    def account(self, n, anchored=False, supplied=True, anchor_returned=True):
        # Full signed snapshot carries n bits, signed root and parent root.
        # The seal is abstract: these widths are ASSUMPTIONS, not key lengths.
        full = n + self.signature_bits + self.root_bits + 2 * self.epoch_bits
        anchor = (self.signature_bits + self.epoch_bits
                  if anchored and anchor_returned else 0)
        return Accounting(
            issuer_full_snapshot_bits=full if supplied else 0,
            verifier_received_bits=full if supplied else 0,
            anchor_received_bits=anchor,
            reader_trusted_checkpoint_bits=self.signature_bits + self.epoch_bits,
            server_snapshot_cell_reads=n if supplied else 0,
            anchor_calls=int(anchored),
        )


def parity(bits, left, right):
    if not (isinstance(left, int) and isinstance(right, int)
            and not isinstance(left, bool) and not isinstance(right, bool)
            and 0 <= left <= right < len(bits)):
        raise ValueError("invalid inclusive range")
    return sum(bits[left:right + 1]) & 1


def read_signed_state(reader, presented, issuer, left, right,
                      profile=SymbolicCostProfile(), anchor=None,
                      anchor_available=True):
    """Full-snapshot baseline, not a Merkle or succinct-proof verifier.

    With anchor=None, this can authenticate historical states but CANNOT
    certify latest-state freshness. With anchor, client first reads a trusted
    current (epoch, seal) pair and fails closed if not reachable.
    """
    if not issuer.verify_checkpoint(reader.checkpoint):
        raise ValueError("reader checkpoint not authentic")
    n = reader.n
    parity(reader.checkpoint.bits, left, right)
    anchored = anchor is not None
    expected = anchor.read(available=anchor_available) if anchored else None
    costs = profile.account(n, anchored=anchored,
                            supplied=(not anchored or expected is not None),
                            anchor_returned=(expected is not None))
    if anchored and expected is None:
        return Answer("NO_TRUSTED_ANCHOR", None, None, costs)
    if not issuer.verify(presented):
        return Answer("INVALID_SIGNATURE_OR_PAYLOAD", None, None, costs)
    if not issuer.extends(presented, reader.checkpoint):
        return Answer("ROLLBACK_OR_FORK_FROM_CHECKPOINT", None, None, costs)
    if anchored and (presented.epoch != expected.epoch or
                     presented.seal != expected.seal):
        return Answer("STALE_OR_EQUIVOCATING_ROOT", None, None, costs)
    reader.checkpoint = Checkpoint(presented.epoch, presented.seal)
    return Answer("ACCEPT", parity(presented.bits, left, right),
                  presented.epoch, costs)


def indistinguishable_without_anchor(no_update_world, hidden_update_world,
                                     presented, left, right):
    """Formal indistinguishability preconditions; independent of reader code.

    Worlds share INITIAL state + public setup, and the server chooses the
    EXACT SAME signed payload and no trusted communication. If latest
    parity differs, no algorithm observing only that identical transcript
    can be both complete on W0 and always latest-correct on W1.
    """
    if no_update_world.history[0].bits != hidden_update_world.history[0].bits:
        raise ValueError("initial states must match")
    if no_update_world.history[-1].bits != no_update_world.history[0].bits:
        raise ValueError("W0 must have no logical update")
    if presented.epoch != 0 or presented.bits != no_update_world.history[0].bits:
        raise ValueError("common old epoch-0 presentation required")
    return (parity(no_update_world.history[-1].bits, left, right) !=
            parity(hidden_update_world.history[-1].bits, left, right))
