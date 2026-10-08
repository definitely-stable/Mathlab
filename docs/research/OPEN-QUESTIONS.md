# Open research questions

> **TOM-005 UPDATE:** Seven broad cross-domain operations have already been audited mathematically under frozen basic models (all seven narrowly scoped theorems have human-readable proofs and adversarial finite test harnesses). See [TOM-005 seven-way theorem and source audit](TOM-005-SEVEN-THEOREM-AUDIT.md) and records KR-034 through KR-040 in the [40-entry no-repeat registry](KNOWN-AND-STOPPED-RESEARCH.md). **These are classical baselines, not seven novel open problems.** Their genuine sharper product extensions require fresh source-gap proof and cannot be marked proved by toy checks.


> **STATUS OVERRIDE (2026-10-08):** This file is a historical question bank, **not an active authorization list**. Before investigating ANY item, consult the [33-record scoped known/closed/STOP registry](KNOWN-AND-STOPPED-RESEARCH.md) and [G2/TOM decision audit](THEOREM-GAP-004-FOUR-STAGE-AUDIT.md). In particular, the G2B q5=10 finite instance is certified CLOSED; HYP-001/002 broad exponents have Lefmann 2005 construction overlap; the HYP-002 quadratic conjecture was DISCHARGED; TOM-003 D1/D2 standalone product lanes are STOP. Nestedness-only tax is DEFER, not an original theorem. Reopen a question only under its stated new model/benefit gate.


## Priority 1 — ASET extremal problem

1. **Sharp ASET growth.** What is the asymptotic growth of
   \[
   A_q^{\mathrm{set}}(m,w,d)
   \]
   for fixed \(q,d,w\) as \(m\to\infty\)?

2. **Restricted-vs-linear gap.** For \(q>2\), when is
   \[
   A_q^{\mathrm{set}}(m,w,d)
   \]
   asymptotically larger than the corresponding arbitrary-coefficient sparse small-column-independence extremal function?

3. **q=3 boundary.** Does the fact that \(\mathbb F_3^\*=\{\pm1\}\) collapse ASET to a known short-dependence problem after accounting for separate positive/negative side bounds, or is there still a genuine gap?

4. **Matching exponents.** Can one obtain a matching upper/lower exponent for any nontrivial fixed parameter regime?

5. **Constructions.** Can random constant-weight q-ary columns, algebraic constructions, or lifted Sidon/dissociated constructions match the best ASET upper bound?

## Priority 2 — exact definition maps

6. **Dissociated sets.** Which k-dissociated / bounded-order dissociated definitions are exactly equivalent to ASET after fixing the ambient field and support bound?

7. **Sidon / B_h.** Under which convention, if any, does ASET for \(d=2\) or general \(d\) reduce to weak Sidon / restricted \(B_h\) uniqueness?

8. **Repeated summands.** Which prior results permit repeated elements, and can they be transferred to distinct-element subset sums without losing the claimed exponent?

9. **Cross-cardinality uniqueness.** Which prior objects control collisions between sums of different cardinalities, not only equal-size sums?

## Priority 3 — nested + locality

10. **Simultaneous near-optimality.** For a common nested family, can all capacities in a set \(D\) simultaneously satisfy
    \[
    m_d\log_2 q \le (1+\varepsilon)\log_2 N_d(V)
    \]
    while every universe element has bounded update support?

11. **Additional tax.** Does bounded update locality force a positive lower bound on the simultaneous competitive ratio
    \[
    \rho(D)=
    \max_{d\in D}
    \frac{m_d\log_2 q}{\log_2N_d(V)}
    \]
    beyond pointwise LENT?

12. **Construction side.** Can check splitting, spatial coupling, or another prefix construction match pointwise ASET/LENT bounds at multiple capacities?

## Priority 4 — mixed alphabets

13. **Optimal heterogeneous cells.** Given a bit budget
    \[
    \sum_j\log_2 q_j,
    \]
    what distribution of \(q_j\) maximizes the reachable state count under a support budget?

14. **Does heterogeneity help?** Can nonuniform alphabets strictly beat every uniform alphabet construction at the same total bit budget and update locality?

15. **Prior-art closure.** Which mixed-alphabet code bounds already imply the relevant counting or extremal inequalities?

## Deferred — computation

16. **Independent cost model.** Which computational resource should be used so that it is not merely a restatement of update locality?

Candidates:

- decoding time;
- incremental decoding work;
- cell probes;
- memory probes;
- preprocessing.

17. **Joint bound.** Only after the model is frozen: can communication, update locality and the chosen computational resource be lower-bounded jointly?

## Immediate G1A prior-art questions

- What are the sharp Lefmann/Naor–Verstraete-style bounds over finite fields for bounded column support and small-column independence?
- What results exist for k-dissociated subsets of finite abelian groups or vector spaces with an additional Hamming-weight/support restriction?
- What is known for weak Sidon / restricted \(B_h\) families inside Hamming balls?
- Which update-efficient code bounds concern write/change complexity rather than query/repair locality?
- Which rate-compatible code results show vanishing or non-vanishing overhead from nestedness alone?
- Which mixed-alphabet bounds are definitionally compatible with the LENT counting model?

## Formalization questions

- What Mathlib representation gives the cleanest finite-support cardinality proof?
- Should the first Lean theorem use Fin m -> ZMod p for prime \(q\), then generalize to finite fields?
- Can the Hamming-ball count be isolated from field structure and proved over any finite pointed alphabet?
- What is the cleanest Lean representation of the signed relation with separate \(n_+\) and \(n_-\) bounds?
