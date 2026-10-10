# HYP-105 B3.2-E1-C7 — exact single-permutation conditional prefix selector

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), [#176](https://github.com/definitely-stable/Mathlab/issues/176). **Dependency stack:** merged C0 [#249](https://github.com/definitely-stable/Mathlab/pull/249) → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → **C7 (this branch)**.

**TYPE: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** This is classical method of conditional expectations, now calculated for the actual weighted original-right GQ source and exactly occupied physical six-edge two-factor target. Not a new abstract concentration theorem. No universal seven-family lower or new ASET exponent.

## Exact all-h prefix-fiber identity

For every s=2^h, h≥1, put V=(s+1)(s²+1), let L be V original GQ right line vertices, F any **fixed** occupied right physical edge image with |F|=V, and let m_f(R)≥0 be C0's genuine weighted B-left source on original six-line sets. Fix a partial injection p:D⊆L→F, with image I=p(D). Select **ONE** uniformly random full bijection Π:L→F conditioned on Π|_D=p.

For A⊆D of size at most six, define

```
b_p(A)=sum_{R: |R|=6, R intersect D=A} m_f(R).
q_p(p(A))=# { T in T(F) : T intersect I = p(A) }.
n=V-|D|.
```

Then the exact rational identity is

```
E[U_B/A(Π) | Π|_D=p]
 = sum_{A⊆D, |A|≤6} b_p(A)*q_p(p(A))/C(n,6-|A|).
```

Only A with b_p(A)>0 occur; every corresponding denominator is nonzero. Proof: for each original sixset R, the remaining 6−|R∩D| image labels are uniformly distributed over the C(n,6−|R∩D|) residual image subsets. Each eligible occupied target sixset T must contain precisely the pinned images p(R∩D) among I. Sum the indicator expectations by original weighted R. No assumption of pairwise independence or physical GQ automorphism is used.

**Tower:** for x∈L\D, averaging the |F\I| children over possible images y yields the parent mean exactly. This holds for arbitrary genuine f,F,p and arbitrary correlation in the already pinned part.

## Exact constructive result and integer zero gate

Pick the smallest unpinned original line x and among all available images y choose the one with minimum exact conditional expectation, tie-break by physical edge index. Because child expectations average to the parent, the chosen path never increases. At depth V, the conditional expectation is the actual nonnegative integer U_B/A for **one deterministic legal g**. Therefore, for every genuine f and occupied F,

```
exists legal g:L→F with U_B/A(f,g)
    <= floor(M(f)*|T(F)|/C(V,6)).
```

This is an upper (existence) guarantee, **not** the desired lower bound `inf_(f,g) S_seven=Omega(s^6)`. An additional exact zero-witness rule follows: whenever a pinned fiber's conditional mean is strictly below 1, some completion has U_B/A=0, and the greedy selector constructs one (integrality). This rule concerns B/A only; it is not an all-seven-family counterexample to #230 and cannot imply R3 upper.

The method is generally exponentially expensive in the number of factor vertices because scanning all available next images and exact weighted source/target aggregates need not be bounded by a useful polynomial in the full GQ input size. The present finite implementation is an oracle, not a runtime/performance theorem.

## Acceptance and independent falsifiers

- Enumerate all 6!=720 completions of a 2-pinned, eight-factor single-permutation model; compare rational mean to brute fixed-map U.
- Check parent/child conditional tower without calling the production formula for the direct permutation enumeration.
- Match empty-prefix expectation to independent C5 global first moment and full-prefix value to independent C5 fixed-map recount.
- Verify integer zero-witness rule on a one-hot **abstract** model; never call it GQ evidence.
- On the **actual original** W(3,2) source, reverse-line baseline U_B/A=77, M=5000, |T_6|=70 and C(15,6)=5005. Greedy must certify a legal fixed map with U_B/A≤floor(350000/5005)=69. Independently recount weighted original source overlap for the emitted map.
- Reject duplicate target 6sets, invalid original source endpoints, repeated/invalid physical target labels in a partial injection, and any change of source/target indexing.
- Hosted dedicated `hyp105-c7-contract` and full `research` must both SUCCESS on the exact PR HEAD; post-merge main Research SUCCESS remains mandatory. Do not merge before C1–C6 and CI clear.

## Scientific decision

C6's Johnson variance computes random-average fluctuations exactly, while C7 conditions the **same random permutation** and constructs one adversarially favorable deterministic completion. It **does not** solve the deterministic *minimum* of the full seven-class S over all true f,g. Useful next model-preserving step: identify all seven distinct original-incidence motif tensors with compatible conditional-prefix descriptions on the **same f,g** and prove an all-h joint bound, or find a genuine infinite counterfamily. Reusing only the B/A overlap optimizer to claim a seven-family result is prohibited.

[Implementation](../../research/hyp105_g5e2b3e1c7_conditional_prefix.py) · [independent finite falsifiers](../../research/test_hyp105_g5e2b3e1c7_conditional_prefix.py).
