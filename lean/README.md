# Lean formalization

Status: **NOT STARTED**.

Mathlab does not mark a theorem “formalized” merely because a Lean plan exists.

## LENT-001 target kernel

The first formalization should prove only the finite baseline:

1. support of a finite sum is contained in the union of supports;
2. support cardinality of a sum of at most d support-w vectors is at most dw;
3. injectivity of (Phi) on sets of size at most d gives at least (N_d(V)) distinct states;
4. the number of q-ary length-m states of support at most r is (B_q(m,r));
5. conclude (N_d(V)le B_q(m,dw)).

Entropy bounds, asymptotics, novelty claims, and decoder models are separate later layers.

When the first checked file lands, add a machine-readable formalization catalogue rather than pre-declaring one.
