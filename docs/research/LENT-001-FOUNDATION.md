# LENT-001 — sparse-update state-space mathematical foundation

## 1. Sparse-Update Hamming-Ball Bound

**THEOREM (baseline; novelty not claimed).**

Under the frozen protocol,

[
N_d(V)=sum_{i=0}^d{Vchoose i}
le
B_q(m,dw)
=
sum_{j=0}^{min(dw,m)}{mchoose j}(q-1)^j.
]

### Proof

Every admissible set (S) has at most (d) elements. Hence (Phi(S)) is a sum of at most (d) columns. Support is subadditive, so

[
|operatorname{supp}Phi(S)|le dw.
]

Exactness makes the (N_d(V)) states (Phi(S)) pairwise distinct. Every such state lies in the q-ary Hamming ball of radius (min(dw,m)) around zero. That ball has exactly

[
B_q(m,dw)
]

states. Therefore (N_d(V)le B_q(m,dw)). ∎

This proof is finite and combinatorial. CI checks finite instances but is not the proof.

Naming status: this theorem is the **Sparse-Update Hamming-Ball Bound for Exact Additive Set Sketches**. The historical phrase "Locality–Entropy Trilemma" is not used as a theorem name because the proved statement is a quantitative tradeoff, not a generic assertion that exactly two of three goals can always be optimized.

## 2. Binary entropy corollary

For (q=2), define

[
ho=rac{dw}{m}.
]

For (0lehole 1/2),

[
sum_{jle ho m}{mchoose j}
le 2^{mH_2(ho)}.
]

Therefore, whenever (dw/mle 1/2),

[
mH_2(dw/m)ge log_2 N_d(V).
]

**DERIVED RESULT.**

If in addition

[
mle(1+arepsilon)log_2N_d(V),
]

then

[
H_2(dw/m)gerac1{1+arepsilon}
]

and hence

[
wge
rac md,
H_2^{-1}!left(rac1{1+arepsilon}ight).
]

As (arepsilon	o0), the inverse tends to (1/2), giving the near-optimal heuristic scale

[
wgtrsim rac{m}{2d}.
]

For (d=o(V)) in standard regimes where
(log {Vchoose d}=Theta(dlog(V/d))), this yields

[
w=Omega(log(V/d))
]

for a fixed binary alphabet and near-entropy state size.

The asymptotic conversion must not be presented as the finite theorem.

## 3. q-ary entropy corollary

Define normalized q-ary entropy on
(0lehole1-1/q):

[
H_q(ho)=
holog_q(q-1)
-holog_qho
-(1-ho)log_q(1-ho).
]

Let

[
alpha_q(arepsilon)
=
H_q^{-1}!left(rac1{1+arepsilon}ight).
]

**DERIVED RESULT.**

If

[
mlog_2qle(1+arepsilon)log_2N_d(V),
]

then the finite bound plus the standard q-ary Hamming-ball entropy estimate imply

[
rac{dw}{m}ge alpha_q(arepsilon),
]

with the case (dw/m>1-1/q) already satisfying the inequality trivially.

Thus

[
wgerac md,alpha_q(arepsilon).
]

Combined with the information bound
(mgelog_qN_d(V)),

[
wge
rac{alpha_q(arepsilon)}{d}log_qN_d(V).
]

Equivalently,

[
log_2 q
ge
rac{alpha_q(arepsilon)}{dw}log_2N_d(V).
]

This is an exact implicit alphabet/locality tradeoff once the entropy inequality is accepted.

A uniform simplification
(log q=Omega(log(V/d)/w))
is **not yet promoted**: the required uniform handling of
(alpha_q(arepsilon)) will be proved/audited separately.

## 4. Constant-locality finite consequence

For binary sketches and integer (r=dw) with (1le rle m),

[
B_2(m,r)
=
sum_{j=0}^r{mchoose j}
le
left(rac{em}{r}ight)^r.
]

Hence

[
m
ge
rac{dw}{e},
N_d(V)^{1/(dw)}.
]

**ASYMPTOTIC RESULT.**

For fixed (d,wge1) and (V	oinfty),

[
N_d(V)=Theta(V^d),
]

so the elementary count gives

[
m=Omega(V^{1/w}).
]

This is a strong separation from the unconstrained information scale
(Theta(dlog V)), but it is not state of the art in the binary sparse-matrix regime.

## 5. Why the binary extremal target is not cleanly new

Let (A) be the (m	imes V) binary matrix with columns (a_x).

Exactness for all sets of size at most (d) holds iff there is no nonempty subset of at most (2d) columns whose GF(2) sum is zero. Equivalently, every at-most-(2d) column set is linearly independent.

Thus the proposed binary extremal quantity

[
A_2(m,w,d)
]

is the classical sparse parity-check extremal problem under the parameter map

[
	ext{rows}=m,qquad
	ext{independence}=2d,qquad
	ext{column weight}=w,qquad
	ext{columns}=V.
]

The G1 audit must use the coding-theory literature before proposing a sharp binary asymptotic.

## 6. Nested/prefix corollary

**DERIVED RESULT, model-dependent; novelty not claimed.**

Suppose one common q-ary coordinate sequence defines prefixes of lengths (m_d), and the prefix at (d) is exact for all sets of size at most (d). Let (w_d) be the maximum column support inside that prefix.

Then every prefix separately satisfies

[
N_d(V)le B_q(m_d,dw_d).
]

If every prefix is near-entropy in the sense

[
m_dlog_2q
le
(1+arepsilon)log_2N_d(V),
]

then

[
w_d
ge
rac{m_d}{d}alpha_q(arepsilon).
]

Therefore a fixed alphabet plus uniformly (O(1)) prefix support cannot coexist with near-entropy prefixes over regimes where (log_q N_d(V)/d) diverges.

This is the precise safe form of the “universal prefix-optimal + fixed alphabet + constant locality” obstruction.

## 7. Minisketch / PinSketch boundary

Minisketch implements a BCH/PinSketch-style set sketch. Its own documentation states that a sketch of b-bit elements with capacity c occupies (bc) bits and that sketches combine linearly.

This is consistent with LENT, not a counterexample. Minisketch update work scales with capacity; it does not provide a fixed-(w), constant-support update map while c grows. Its large field is relevant, but so is its nonconstant per-element syndrome work.

## 8. Stuffed IBLT boundary

Stuffed IBLTs (Klausen–Pagh–Walzer, 2026) obtain near-information-optimal space, constant-time updates and linear-time decoding with high probability in a randomized multiset-sketch model.

That does not contradict the G0 theorem:

- G0 requires worst-case injectivity of the fixed map for every admissible set;
- Stuffed IBLT gives high-probability recovery;
- its cell state is richer than a single binary bit.

The exact model comparison belongs in G1.

## 9. Research target after corrections

The strongest plausible new directions are not the elementary count and not the already-classical binary extremal problem.

Priority order:

1. q-ary exact set sketches where collisions use restricted coefficients in ({-1,0,1}), not arbitrary linear dependence;
2. tight nested-prefix lower bounds beyond applying the finite theorem independently to each prefix;
3. nonuniform coordinate alphabets / cell payloads;
4. a joint lower bound including decoder or incremental-computation cost, only after the computation model is frozen;
5. matching constructions in a regime not already covered by sparse parity-check theory.
