# LENT-001-G1B — primary-source novelty-closure protocol

Status: **FROZEN FOR PRIMARY-SOURCE AUDIT v2**

Issue: #6

Baseline for v2:

\[
\texttt{main@5f168b26020de61f1b229585d143ab5d05dc4538}
\]

## 1. Objective

Determine whether the **support-constrained** extremal problem

\[
A_q^{\mathrm{set}}(m,w,d)
\]

contains a genuinely unclaimed regime.

Audit 02 establishes that bounded-active exact subset identification itself
is already established under BCC/signature-code terminology. G1B therefore
no longer asks whether ASET-like coding exists. It asks whether the sharp
hard-support frontier is already known.

No publication novelty claim is permitted before G1B closes.

## 2. Accepted model facts

G1B accepts:

1. ASET-SIGNED from G1A;
2. q=2 small-dependency equivalence;
3. q=3/q=5 finite separation from arbitrary-coefficient independence;
4. binary BCC as definitionally equivalent to unconstrained binary ASET;
5. finite-field K-out-of-M signature codes as direct prior art for
   unconstrained q-ary bounded-active identification;
6. the characteristic-two block reduction from
   \`LENT-001-G1B-CHAR2-REDUCTION.md\`.

## 3. Primary novelty parameter

The distinguishing Mathlab condition is

\[
|\operatorname{supp}(a_i)|\le w.
\]

Every candidate novelty theorem must use this parameter essentially.

A theorem that remains unchanged after deleting \(w\) is not a new
Mathlab-specific target.

## 4. Field-regime split

The source audit must distinguish:

### Characteristic two

For

\[
q=2^s,
\]

ASET is a block-sparse binary short-dependency problem after basis
expansion.

The remaining question is whether the corresponding block-sparse extremal
problem is already known sharply.

### q=3

All nonzero coefficients are \(\pm1\), but ASET's separate positive and
negative side bounds remain weaker than ordinary short linear independence.

### Odd q>3

Both the coefficient restriction to \(\pm1\) and the separate side bounds
matter.

No single "q>2" conclusion is allowed unless it covers all three cases.

## 5. Mandatory source clusters

Before G1B may close, audit:

1. sparse/block-sparse binary BCC and parity-check matrices;
2. zero-error sparse/constant-weight signatures over finite-field or
   modulo-q adders;
3. constant-weight ordinary-adder signature/superimposed codes;
4. bounded-column-weight additive/quantitative detecting matrices;
5. support-constrained q-ary \(B_h\), Sidon, free or signed-sum families;
6. q=3 distinct-summand/two-sided relation systems.

Low-density-signature AWGN/NOMA literature is a terminology/engineering
neighbor only unless an exact all-input reduction is proved.

## 6. Transfer discipline

All v1 reduction rules remain active.

In addition:

- BCC proves that **unconstrained** binary ASET is known.
- Finite-field K-out-of-M signature constructions prove that bounded-active
  finite-field identification is known in general.
- Constant-weight ordinary-adder constructions prove that sparse signatures
  are generically known, but do not automatically solve modular ASET.
- Therefore novelty can only reside in the intersection of hard support,
  modular arithmetic, and sharp extremal behavior.

## 7. Allowed G1B exits

Version 1's provisional \`SPLIT_Q3_QGT3\` exit is deprecated.

G1B v2 ends with exactly one:

- \`CONTINUE_SPARSE_ASET\`
- \`REDUCE_TO_KNOWN_SPARSE_SIGNATURE\`
- \`SPLIT_BY_CHARACTERISTIC\`
- \`STOP_NOT_NOVEL\`

If \`SPLIT_BY_CHARACTERISTIC\` is chosen, the decision must separately
classify:

- characteristic two;
- q=3;
- odd q>3.

## 8. Acceptance

G1B cannot close until:

- every direct sparse-signature source class is primary-verified or marked
  nonessential with justification;
- the characteristic-two block-sparse lane is explicitly classified;
- q=3 is explicitly classified;
- odd q>3 is explicitly classified;
- all claimed upper/lower-bound transfers have written reductions;
- CLAIMS, PRIOR-ART, SOURCE-MATRIX, DECISIONS and ROADMAP agree;
- issue #6 records the final v2 exit.

No preprint promotion is allowed during G1B.
