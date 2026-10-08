# LENT-001 — frozen sparse-update foundation protocol

Status: **FROZEN FOR G0 FOUNDATION v1**

Terminology note: `LENT-001` is the stable historical ID. The former expansion "Locality–Entropy Trilemma" is deprecated for new public-facing material. This protocol's mathematical content is unchanged.

Issue: #1.

Baseline repository head before this slice:
`a04999ec607d2cc4b7779d18d887c120dd56939b`.

## 1. Model

Let the universe be ([V]). Let (q) be a prime power and let the sketch state be in (mathbb F_q^m).

Each universe element (x) has an update column

[
a_x in mathbb F_q^m.
]

For a set (Ssubseteq[V]),

[
Phi(S)=sum_{xin S}a_x.
]

The G0 model is deterministic once the columns are fixed.

### Exactness

For all distinct (S,Tsubseteq[V]) with (|S|,|T|le d),

[
Phi(S)
ePhi(T).
]

This is worst-case injectivity, not high-probability recovery.

### Update locality

Each column satisfies

[
|operatorname{supp}(a_x)|le w.
]

Locality counts changed sketch coordinates, not arithmetic operations inside a coordinate and not source-set maintenance.

### Communication

A state has (m) coordinates over alphabet size (q), i.e. nominal state information (mlog_2 q) bits before representation overhead.

## 2. Finite baseline

Define

[
N_d(V)=sum_{i=0}^d {Vchoose i}
]

with the convention ({Vchoose i}=0) for (i>V), and

[
B_q(m,r)=sum_{j=0}^{min(r,m)}{mchoose j}(q-1)^j.
]

The frozen finite statement is

[
N_d(V)le B_q(m,dw).
]

This statement is a correctness target, not a novelty claim.

## 3. Permitted G0 proof

The proof may use only:

1. there are (N_d(V)) admissible source sets;
2. exactness makes their sketch states distinct;
3. a sum of at most (d) columns of support at most (w) has support at most (dw);
4. the number of q-ary length-m vectors of support at most (dw) is (B_q(m,dw)).

No asymptotics are required for G0 acceptance.

## 4. Binary mapping

For (q=2), a collision between two sets of size at most (d) is equivalent to a nonempty GF(2) dependency among at most (2d) columns.

Therefore the binary extremal problem is directly connected to sparse parity-check matrices whose columns have weight at most (w) and whose small column subsets are independent.

This mapping is frozen as a prior-art warning.

## 5. Randomized sketches

A randomized sketch that succeeds with high probability is outside the G0 exact model unless the random seed is fixed and the resulting map is injective for every admissible input.

Do not cite a high-probability construction as a counterexample to the deterministic theorem.

## 6. Prefix model

Nested/prefix claims are not part of the G0 theorem.

For later use, a prefix family must define one common coordinate sequence and, for each (d), a prefix length (m_d). Prefix locality (w_d) is the maximum support of a column restricted to the first (m_d) coordinates.

Any LENT theorem applied to a prefix must use ((m_d,w_d,d)), not an unstated global locality.

## 7. Change control

Before G0 closes, changes are allowed only to repair ambiguity or mathematical error.

After G0:

- weakening/strengthening exactness;
- changing the locality metric;
- allowing failure probability;
- changing alphabet semantics;
- changing subset-size domain;

requires a new protocol version before affected evidence is collected.

## 8. G0 acceptance

G0 returns `FOUNDATION_PASS` only when:

- protocol and claim registry agree;
- exact arithmetic checker passes;
- exhaustive-small oracle passes its frozen grid;
- CI is green on the PR head;
- no document claims publication novelty.

Anything else is `FOUNDATION_INCOMPLETE`.
