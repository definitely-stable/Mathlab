"""TOM-003-D2: independent Merkle structural oracle and adversarial changes."""
from itertools import combinations, product
import unittest

from tom_authenticated_overwrite import (
    authenticated_overwrite, check_bits, compare_costs, complete_tree,
    enumerate_costs, helper_indices, prove, reconstruct, selection,
)


def independent_ssz_frontier(n, indices):
    # Independent formulation: the helper frontier comprises siblings
    # of the union of EVERY selected leaf-to-root path, excluding any
    # node already on a selected path. No call to helper_indices().
    paths=set()
    for i in indices:
        v=n+i
        while v>1:
            paths.add(v)
            v//=2
    return tuple(sorted({v^1 for v in paths if (v^1) not in paths}))


def untrusted_reference_root(bits):
    # Independent bottom-up recursive oracle using SHA256's directly
    # defined domain-separated composition, without complete_tree().
    from hashlib import sha256
    def build(left, right):
        if right-left==1:
            return sha256(
                bytes([0])+left.to_bytes(4,"big")+bytes([bits[left]])
            ).digest()
        mid=(left+right)//2
        return sha256(bytes([1])+build(left,mid)+build(mid,right)).digest()
    return build(0,len(bits))


class AuthenticatedOverwriteD2Tests(unittest.TestCase):
    def test_independent_frontier_all_nonempty_sets(self):
        for n in (2,4,8):
            for size in range(1,n+1):
                for subset in combinations(range(n),size):
                    self.assertEqual(
                        helper_indices(n,subset),
                        independent_ssz_frontier(n,subset),
                        (n,subset)
                    )
            report=enumerate_costs(n)
            self.assertEqual(report["exhaustive_nonempty_batches"],2**n-1)
            self.assertGreater(report["batches_with_savings"],0 if n>2 else -1)

    def test_complete_small_merkle_roots_against_independent_oracle(self):
        for n in (2,4,8):
            for mask in range(1<<n):
                bits=tuple((mask>>i)&1 for i in range(n))
                self.assertEqual(complete_tree(bits)[1],untrusted_reference_root(bits))

    def test_all_batched_proofs_reconstruct_exact_same_root(self):
        for n in (2,4,8):
            inputs=[
                tuple((mask>>i)&1 for i in range(n))
                for mask in (0,1,(1<<n)-1,(1<<n)//3)
            ]
            for bits in inputs:
                tree=complete_tree(bits)
                for size in range(1,n+1):
                    for subset in combinations(range(n),size):
                        proof=prove(tree,subset)
                        root,hashes=reconstruct(n,subset,[bits[i] for i in subset],proof)
                        self.assertEqual(root,tree[1])
                        self.assertGreaterEqual(hashes,len(subset))
                        self.assertEqual(set(proof),set(helper_indices(n,subset)))

    def test_valid_overwrite_count_root_and_predicate_sequences(self):
        for n in (2,4,8):
            for mask in (0, 1, (1<<n)-1, (1<<n)//3):
                bits=[(mask>>i)&1 for i in range(n)]
                for threshold in (1,(n+1)//2,n):
                    state=bits.copy()
                    root=complete_tree(state)[1]
                    count=sum(state)
                    # Pinned diverse deterministic batches, with no duplicate.
                    batches=[(0,), (n-1,), (0,n-1)] if n>2 else [(0,),(1,),(0,1)]
                    for number,group in enumerate(batches):
                        edits=tuple((i,state[i],(state[i]+1+number%2)%2) for i in group)
                        old_f=count>=threshold
                        p=prove(complete_tree(state),group)
                        result=authenticated_overwrite(n,root,count,threshold,edits,p)
                        for i,old,new in edits:
                            self.assertEqual(state[i],old)
                            state[i]=new
                        count=sum(state)
                        root=complete_tree(state)[1]
                        self.assertEqual(result.root,root)
                        self.assertEqual(result.count,count)
                        self.assertEqual(result.no_effect,old_f==(count>=threshold))

    def test_tampering_old_new_hashes_and_stale_root_fail_closed(self):
        bits=[0,1,0,1,0,0,1,1]
        tree=complete_tree(bits)
        idx=(0,1)
        proof=prove(tree,idx)
        good=((0,0,1),(1,1,0))
        accepted=authenticated_overwrite(8,tree[1],sum(bits),4,good,proof)
        self.assertEqual(accepted.count,4)
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,tree[1],sum(bits),4,((0,1,1),(1,1,0)),proof)
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,tree[1],sum(bits),4,good,
                                    {k:bytes([b[0]^1])+b[1:] if k==min(proof) else b
                                     for k,b in proof.items()})
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,tree[1],sum(bits),4,good,{})
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,tree[1],sum(bits),4,good,{**proof,1:b"0"*32})
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,accepted.root,accepted.count,4,good,proof)
        # Other subtree changes -> one previously authenticated sibling
        # becomes stale, even when the affected ID is not in this update.
        other=list(bits);other[7]^=1
        with self.assertRaises(ValueError):
            authenticated_overwrite(8,complete_tree(other)[1],sum(other),4,good,proof)

    def test_duplicate_indices_domain_root_and_count_checks(self):
        bits=[1,0,0,1]
        root=complete_tree(bits)[1]
        proof=prove(complete_tree(bits),(0,))
        bad_edits=[
            ((0,1,0),(0,0,1)), ((0,1,0),(0,1,0)),
        ]
        for e in bad_edits:
            with self.assertRaises(ValueError):
                authenticated_overwrite(4,root,2,2,e,proof)
        for bogus_n in (0,3,8):
            with self.assertRaises(ValueError):
                authenticated_overwrite(bogus_n,root,2,2,((0,1,0),),proof)
        for bogus_count in (-1,5):
            with self.assertRaises(ValueError):
                authenticated_overwrite(4,root,bogus_count,2,((0,1,0),),proof)
        for i in (-1,4):
            with self.assertRaises(ValueError):
                authenticated_overwrite(4,root,2,2,((i,0,1),),proof)
        with self.assertRaises(ValueError):
            authenticated_overwrite(4,b"\x00"*32,2,2,((0,1,0),),proof)
        with self.assertRaises(ValueError):
            authenticated_overwrite(4,root,2,2,((0,1,2),),proof)

    def test_untrusted_count_is_not_authenticated_by_root(self):
        # Protocol explicitly requires an authenticated initial count.
        # Root authenticates actual bytes, not an arbitrary count value.
        bits=(0,)*8
        root=complete_tree(bits)[1]
        proof=prove(complete_tree(bits),(0,))
        edit=((0,0,1),)
        trusted=authenticated_overwrite(8,root,0,1,edit,proof)
        claimed=authenticated_overwrite(8,root,7,1,edit,proof)
        self.assertFalse(trusted.no_effect)  # 0 -> 1 crosses threshold
        self.assertTrue(claimed.no_effect)    # fraudulent 7 -> 8 does not
        self.assertEqual(trusted.root,claimed.root)
        self.assertNotEqual(trusted.count,claimed.count)

    def test_structural_cost_exact_not_runtime(self):
        adjacent=compare_costs(8,(0,1))
        apart=compare_costs(8,(0,7))
        self.assertEqual(adjacent["batched_proof_digest_nodes"],2)
        self.assertEqual(apart["batched_proof_digest_nodes"],4)
        self.assertEqual(adjacent["independent_proof_digest_nodes"],6)
        self.assertEqual(adjacent["independent_digest_bytes"],6*32)
        self.assertEqual(adjacent["batched_digest_bytes"],2*32)
        self.assertEqual(adjacent["direct_retained_bits"],8)
        self.assertEqual(adjacent["trusted_merkle_root_bits"],256)
        self.assertEqual(adjacent["prover_full_tree_sha256_setup"],15)
        self.assertEqual(adjacent["prover_full_tree_stored_digest_bytes"],15*32)
        self.assertGreater(adjacent["verifier_batch_sha256_calls_old_and_new"],0)


if __name__=="__main__":
    unittest.main()
