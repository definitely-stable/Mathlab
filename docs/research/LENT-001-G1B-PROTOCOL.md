# LENT-001-G1B — primary-source novelty-closure protocol

Status: **FROZEN FOR PRIMARY-SOURCE AUDIT v1**

Issue: #6

Baseline:

\[
\texttt{main@e435b72fbf7b94f3f514a3f5fbbae88070876525}
\]

## 1. Objective

Determine whether the sharp extremal problem

\[
A_q^{\mathrm{set}}(m,w,d)
\]

contains a genuinely unclaimed regime after accounting for the closest
coding-theory and additive-combinatorics literature.

G1B is a novelty-classification gate, not a theorem-proving gate.

No asymptotic ASET theorem may be marketed as new before G1B closes.

## 2. Frozen mathematical input

G1B accepts the following G1A results as model facts:

1. ASET exactness is equivalent to absence of a legal signed relation
   \[
   \varepsilon_i\in\{-1,0,1\},
   \quad n_+\le d,\quad n_-\le d.
   \]
2. arbitrary-coefficient independence through \(2d\) columns implies ASET;
3. for \(q=2\), the implication is an equivalence;
4. for \(q=3\) and \(q=5\), strict finite separations exist;
5. the finite separation is not by itself an asymptotic novelty result.

Evidence:
\`LENT-001-G1A-PROOF.md\` and
\`LENT-001-G1A-EVIDENCE.md\`.

## 3. Required primary-source clusters

G1B must audit, in this order:

1. sparse parity-check matrices over finite fields;
2. dissociated / k-dissociated / bounded-order dissociated sets;
3. Sidon / weak Sidon / \(B_h\) / restricted-\(B_h\) families;
4. distinct-summand subset-sum systems;
5. bounded-Hamming-weight / bounded-support additive families;
6. q=3 specializations;
7. only then secondary locality/nested/mixed-alphabet literature where it
   materially affects the ASET novelty boundary.

A search result, survey, encyclopedia page, blog, or AI-generated report may
be used for navigation but cannot close a G1B claim by itself.

## 4. Mandatory per-source schema

Every theorem considered relevant must be recorded with:

- bibliographic identity;
- primary-source URL/DOI/arXiv/proceedings entry;
- exact ambient algebraic object;
- input family;
- distinct versus repeated summands;
- exactly \(h\) versus all cardinalities through \(d\);
- whether cross-cardinality collisions are excluded;
- coefficient set: \(+1\), \(\pm1\), arbitrary field coefficients, or other;
- whether \(n_+\) and \(n_-\) are separately bounded;
- whether only total relation support is bounded;
- bounded support/Hamming-weight assumptions on the generators;
- theorem statement actually proved;
- asymptotic regime;
- parameter map to \((q,m,w,d,V)\);
- direction of implication/reduction;
- consequence for ASET;
- confidence: VERIFIED_PRIMARY or NEEDS_PRIMARY_CHECK.

## 5. Reduction discipline

### Stronger prior-art model

If prior art requires a stronger property than ASET, then its constructions
may give ASET lower bounds.

Its upper bounds do **not** automatically upper-bound ASET.

### Weaker prior-art model

If prior art controls a weaker property, its upper bounds may potentially
constrain ASET only after the implication direction is proved.

Its constructions do **not** automatically satisfy ASET.

### Equivalent model

The word **equivalent** is allowed only after a definition-level reduction
is written in the repository.

Terminology similarity is not evidence of equivalence.

## 6. q=3 rule

G1B must not collapse q=3 into ordinary short linear independence merely
because

\[
\mathbb F_3^\*=\{\pm1\}.
\]

The separate ASET side bounds remain relevant, and G1A already produced a
strict finite separation.

A q=3 prior-art theorem closes the gap only if its relation model matches
the side-bounded ASET condition or a reduction is proved.

## 7. Bounded-support rule

A result for unrestricted subsets of an ambient abelian group/vector space
does not automatically solve the Mathlab extremal problem.

The audit must explicitly record whether the source constrains

\[
|\operatorname{supp}(a_i)|\le w
\]

or provides a reduction preserving the relevant asymptotic scale.

## 8. G1B decision

G1B ends with exactly one repository decision:

- \`CONTINUE_ASET\`
- \`REDUCE_TO_KNOWN_OBJECT\`
- \`SPLIT_Q3_QGT3\`
- \`STOP_NOT_NOVEL\`

The decision must cite the completed source-to-claim matrix and explain why
the other three outcomes were rejected.

## 9. Acceptance

G1B cannot close until:

- every high-priority matrix row has VERIFIED_PRIMARY status or an explicit
  reason it is nonessential;
- theorem statements are copied only as short formulas/parameter summaries,
  not unverifiable paraphrases;
- all claimed implications have a written reduction;
- q=3 is handled explicitly;
- bounded support is handled explicitly;
- PRIOR-ART, CLAIMS, DECISIONS and ROADMAP agree;
- issue #6 contains the final decision.

No preprint promotion is allowed during this gate.
