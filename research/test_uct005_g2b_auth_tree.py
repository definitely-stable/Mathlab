"""UCT-005 G2-B finite authenticated quadtree oracle (research ONLY).

This checks structural binding under SHA-256 for finite examples; NO cryptographic
security proof, physical timing claim, production byte protocol or durability claim.
"""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import unittest

DIGEST_BYTES = 32


def children_bounds(bounds):
    r, c, side = bounds
    h = side // 2
    return ((r, c, h), (r, c + h, h),
            (r + h, c, h), (r + h, c + h, h))


def box_bytes(bounds):
    return b"".join(int(x).to_bytes(4, "big") for x in bounds)


def leaf_digest(bounds, bit):
    assert bit in (0, 1)
    return sha256(b"UCT005-G2B-LEAF-v1" + box_bytes(bounds) +
                  bytes([bit])).hexdigest()


def parent_digest(bounds, aggregate, digests):
    assert aggregate in (0, 1) and len(digests) == 4
    assert all(isinstance(h, str) and len(h) == 2 * DIGEST_BYTES
               for h in digests)
    return sha256(
        b"UCT005-G2B-INNER-v1" + box_bytes(bounds) +
        bytes([aggregate]) +
        b"".join(bytes.fromhex(h) for h in digests)
    ).hexdigest()


def make_tree(bits, bounds):
    r, c, n = bounds
    if n == 1:
        v = bits[r][c]
        return {"bounds": bounds, "value": v, "digest": leaf_digest(bounds, v),
                "children": None}
    nodes = [make_tree(bits, b) for b in children_bounds(bounds)]
    v = 0
    for child in nodes:
        v ^= child["value"]
    return {"bounds": bounds, "value": v,
            "digest": parent_digest(bounds, v, [c["digest"] for c in nodes]),
            "children": nodes}


def intersects(bounds, rect):
    r, c, n = bounds
    a, b, x, y = rect
    return r < x and a < r + n and c < y and b < c + n


def covered(bounds, rect):
    r, c, n = bounds
    a, b, x, y = rect
    return a <= r and b <= c and r + n <= x and c + n <= y


def make_query_proof(node, rect):
    b = node["bounds"]
    if not intersects(b, rect):
        return ("O", node["digest"])
    if covered(b, rect):
        if node["children"] is None:
            return ("F", node["value"], None)
        return ("F", node["value"],
                tuple(x["digest"] for x in node["children"]))
    if node["children"] is None:
        raise AssertionError("leaf must be either outside or covered")
    return ("P", node["value"],
            tuple(make_query_proof(child, rect) for child in node["children"]))


def _verify_query_node(bounds, rect, proof):
    if not isinstance(proof, tuple) or not proof:
        raise ValueError("malformed proof")
    tag = proof[0]
    r, c, side = bounds
    if not intersects(bounds, rect):
        if tag != "O" or len(proof) != 2:
            raise ValueError("outside proof required")
        h = proof[1]
        if not isinstance(h, str) or len(h) != 2 * DIGEST_BYTES:
            raise ValueError("malformed outside digest")
        return h, 0
    if covered(bounds, rect):
        if tag != "F" or len(proof) != 3 or proof[1] not in (0, 1):
            raise ValueError("full-node aggregate proof required")
        aggregate, hashes = proof[1:]
        if side == 1:
            if hashes is not None:
                raise ValueError("leaf cannot have child digests")
            return leaf_digest(bounds, aggregate), aggregate
        if not isinstance(hashes, tuple) or len(hashes) != 4:
            raise ValueError("four child digests required")
        try:
            return parent_digest(bounds, aggregate, hashes), aggregate
        except (AssertionError, ValueError) as ex:
            raise ValueError("invalid child digest") from ex
    if tag != "P" or len(proof) != 3 or proof[1] not in (0, 1):
        raise ValueError("partial-node proof required")
    if side == 1 or not isinstance(proof[2], tuple) or len(proof[2]) != 4:
        raise ValueError("invalid partial structure")
    h, answer = [], 0
    for child_bounds, child_proof in zip(children_bounds(bounds), proof[2]):
        digest, contribution = _verify_query_node(child_bounds, rect, child_proof)
        h.append(digest)
        answer ^= contribution
    return parent_digest(bounds, proof[1], h), answer


def verify_query(trusted_root, epoch, supplied_epoch, side, rect, proof):
    if supplied_epoch != epoch:
        raise ValueError("stale epoch")
    if not (0 <= rect[0] < rect[2] <= side and
            0 <= rect[1] < rect[3] <= side):
        raise ValueError("invalid rectangle")
    digest, answer = _verify_query_node((0, 0, side), rect, proof)
    if digest != trusted_root:
        raise ValueError("root mismatch")
    return answer


def _index(bounds, row, col):
    r, c, side = bounds
    if not (r <= row < r + side and c <= col < c + side):
        raise ValueError("point outside subtree")
    h = side // 2
    return (2 if row >= r + h else 0) + (1 if col >= c + h else 0)


def make_update_proof(node, row, col):
    path = []
    cur = node
    while cur["children"] is not None:
        at = _index(cur["bounds"], row, col)
        siblings = tuple(ch["digest"] for i, ch in
                         enumerate(cur["children"]) if i != at)
        path.append((cur["value"], siblings))
        cur = cur["children"][at]
    return cur["value"], tuple(path)


def _compute_update_roots(side, row, col, proof):
    if not isinstance(proof, tuple) or len(proof) != 2:
        raise ValueError("bad update proof")
    old, path = proof
    if old not in (0, 1):
        raise ValueError("invalid leaf bit")
    bounds = (0, 0, side)
    ancestors = []
    for frame in path:
        if (not isinstance(frame, tuple) or len(frame) != 2 or
                frame[0] not in (0, 1) or not isinstance(frame[1], tuple) or
                len(frame[1]) != 3):
            raise ValueError("invalid ancestor frame")
        at = _index(bounds, row, col)
        ancestors.append((bounds, at, frame))
        bounds = children_bounds(bounds)[at]
    if bounds != (row, col, 1):
        raise ValueError("incomplete or overlong path")
    previous = leaf_digest(bounds, old)
    next_digest = leaf_digest(bounds, old ^ 1)
    for parent, at, (aggregate, sib) in reversed(ancestors):
        before = list(sib)
        before.insert(at, previous)
        after = list(sib)
        after.insert(at, next_digest)
        try:
            previous = parent_digest(parent, aggregate, before)
            next_digest = parent_digest(parent, aggregate ^ 1, after)
        except (AssertionError, ValueError) as e:
            raise ValueError("invalid update digests") from e
    return previous, next_digest


def accept_flip(trusted_root, epoch, supplied_epoch, side, row, col, proof):
    if supplied_epoch != epoch:
        raise ValueError("stale update request")
    if not (0 <= row < side and 0 <= col < side):
        raise ValueError("invalid coordinate")
    old_digest, new_digest = _compute_update_roots(side, row, col, proof)
    if old_digest != trusted_root:
        raise ValueError("invalid old state")
    return new_digest, epoch + 1


def server_flip(node, row, col):
    """In-place O(log N) path-only update; never rebuild unrelated subtrees."""
    if node["children"] is None:
        node["value"] ^= 1
        node["digest"] = leaf_digest(node["bounds"], node["value"])
        return 1
    idx = _index(node["bounds"], row, col)
    touched = server_flip(node["children"][idx], row, col)
    node["value"] ^= 1
    node["digest"] = parent_digest(node["bounds"], node["value"],
                                    [x["digest"] for x in node["children"]])
    return touched + 1


def proof_counts(proof):
    """Abstract digest/aggregate occurrences; NOT serialized network bytes."""
    if proof[0] == "O":
        return (1, 0)
    if proof[0] == "F":
        return (0 if proof[2] is None else 4, 1)
    if proof[0] == "P":
        hashes, aggregates = 0, 1
        for child in proof[2]:
            h, a = proof_counts(child)
            hashes += h
            aggregates += a
        return hashes, aggregates
    raise ValueError("unknown tag")


def truth(bits, rect):
    a, b, r, c = rect
    ans = 0
    for x in range(a, r):
        for y in range(b, c):
            ans ^= bits[x][y]
    return ans


class G2BFrozenAuthenticatedOracleTests(unittest.TestCase):
    def test_exhaustive_2x2_states_rectangles_and_updates(self):
        n = 2
        rectangles = [(a, b, c, d)
                      for a in range(n) for c in range(a + 1, n + 1)
                      for b in range(n) for d in range(b + 1, n + 1)]
        for state in product((0, 1), repeat=4):
            values = [list(state[0:2]), list(state[2:4])]
            root = make_tree(values, (0, 0, n))
            original = root["digest"]
            for rect in rectangles:
                proof = make_query_proof(root, rect)
                self.assertEqual(verify_query(original, 0, 0, n, rect, proof),
                                 truth(values, rect))
            for row, col in product(range(n), repeat=2):
                server = deepcopy(root)
                proof = make_update_proof(server, row, col)
                next_digest, next_epoch = accept_flip(
                    original, 0, 0, n, row, col, proof)
                self.assertEqual(server_flip(server, row, col), 2)
                self.assertEqual(next_digest, server["digest"])
                post = [list(r) for r in values]
                post[row][col] ^= 1
                for rect in rectangles:
                    q = make_query_proof(server, rect)
                    self.assertEqual(
                        verify_query(next_digest, next_epoch, next_epoch,
                                     n, rect, q), truth(post, rect))
                self.assertRaises(ValueError, verify_query, next_digest, 1, 1,
                                  n, (row, col, row + 1, col + 1),
                                  make_query_proof(root,
                                                   (row, col, row + 1, col + 1)))

    def test_adaptive_four_by_four_and_genuine_root_progression(self):
        n = 4
        a = [[0 for _ in range(n)] for _ in range(n)]
        root = make_tree(a, (0, 0, n))
        digest = root["digest"]
        epoch = 0
        for step in range(32):
            row, col = (3 * step + step // 4) % n, (step + step // 3) % n
            update = make_update_proof(root, row, col)
            digest, epoch = accept_flip(digest, epoch, epoch, n, row, col, update)
            self.assertEqual(server_flip(root, row, col), 3)
            self.assertEqual(root["digest"], digest)
            a[row][col] ^= 1
            for r0 in range(n):
                for c0 in range(n):
                    rect = (r0, c0, n - (step % (n-r0)), n - ((step // 2) % (n-c0)))
                    if not (rect[0] < rect[2] and rect[1] < rect[3]):
                        continue
                    prf = make_query_proof(root, rect)
                    self.assertEqual(
                        verify_query(digest, epoch, epoch, n, rect, prf),
                        truth(a, rect))

    def test_malicious_tamper_delete_replay_wrong_branch_and_epoch(self):
        n = 4
        a = [[(r + c) % 2 for c in range(n)] for r in range(n)]
        node = make_tree(a, (0, 0, n))
        digest = node["digest"]
        entire = (0, 0, n, n)
        q = make_query_proof(node, entire)
        self.assertEqual(proof_counts(q), (4, 1))  # 4 digests, not Omega(N) digests.
        evil = ("F", q[1] ^ 1, q[2])
        with self.assertRaises(ValueError):
            verify_query(digest, 0, 0, n, entire, evil)
        with self.assertRaises(ValueError):
            verify_query(digest, 0, -1, n, entire, q)
        with self.assertRaises(ValueError):
            verify_query(digest, 0, 0, n, entire, ("F", q[1], q[2][:-1]))
        rect = (1, 1, 4, 4)
        partial = make_query_proof(node, rect)
        self.assertEqual(partial[0], "P")
        with self.assertRaises(ValueError):
            verify_query(digest, 0, 0, n, rect, ("P", partial[1],
                                                partial[2][:-1]))
        # Reuse the correct full-grid digest while reporting a different
        # aggregate cannot be authenticated against the trusted root.
        upd = make_update_proof(node, 1, 1)
        next_digest, epoch = accept_flip(digest, 0, 0, n, 1, 1, upd)
        server_flip(node, 1, 1)
        with self.assertRaises(ValueError):
            verify_query(next_digest, epoch, epoch, n, entire, q)
        with self.assertRaises(ValueError):
            accept_flip(next_digest, epoch, 0, n, 1, 1, upd)
        forged_update = (upd[0] ^ 1, upd[1])
        with self.assertRaises(ValueError):
            accept_flip(digest, 0, 0, n, 1, 1, forged_update)

    def test_one_by_one_edge_and_epoch_binding_even_when_state_repeats(self):
        a = [[0]]
        node = make_tree(a, (0, 0, 1))
        digest = node["digest"]
        proof = make_query_proof(node, (0, 0, 1, 1))
        self.assertEqual(proof_counts(proof), (0, 1))
        for epoch in range(2):
            upd = make_update_proof(node, 0, 0)
            digest, next_epoch = accept_flip(digest, epoch, epoch, 1, 0, 0, upd)
            self.assertEqual(server_flip(node, 0, 0), 1)
            self.assertEqual(node["digest"], digest)
            self.assertEqual(next_epoch, epoch + 1)
        self.assertEqual(digest, leaf_digest((0, 0, 1), 0))
        with self.assertRaises(ValueError):
            verify_query(digest, 2, 0, 1, (0, 0, 1, 1), proof)
        self.assertEqual(verify_query(digest, 2, 2, 1, (0, 0, 1, 1), proof), 0)

    def test_point_embedding_of_read_and_conditional_flip_write(self):
        for n in (1, 2, 4):
            bits = [[(r * n + c) % 2 for c in range(n)] for r in range(n)]
            tree = make_tree(bits, (0, 0, n))
            digest = tree["digest"]
            epoch = 0
            for t in range(n * n):
                i, j = divmod(t, n)
                point = (i, j, i+1, j+1)
                prf = make_query_proof(tree, point)
                old = verify_query(digest, epoch, epoch, n, point, prf)
                self.assertEqual(old, bits[i][j])
                wanted = old ^ 1
                u = make_update_proof(tree, i, j)
                digest, epoch = accept_flip(digest, epoch, epoch, n, i, j, u)
                server_flip(tree, i, j)
                bits[i][j] = wanted
                self.assertEqual(verify_query(
                    digest, epoch, epoch, n, point,
                    make_query_proof(tree, point)), wanted)


if __name__ == "__main__":
    unittest.main()
