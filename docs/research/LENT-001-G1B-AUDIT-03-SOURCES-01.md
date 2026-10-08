# LENT-001-G1B — Audit 03 source pass 01

Status: **PRIMARY-SOURCE / PUBLISHER-METADATA VERIFIED, PARTIAL**

## 1. Ericson–Levenshtein: modulo-2 superimposed codes

Primary paper:

Thomas Ericson, Vladimir I. Levenshtein,
*Superimposed Codes in the Hamming Space*,
IEEE Transactions on Information Theory 40(6), 1994, 1882–1893.

DOI:
https://doi.org/10.1109/18.340463

The model assumes a population of users with at most a bounded number active.
The channel output is the modulo-2 sum of the active users' binary
codewords, and the code family is designed so that the active users and
their messages are identifiable.

This is older direct evidence that modular binary bounded-active
identification is established coding theory.

It reinforces the q=2 STOP decision but does not close the hard per-signature
support frontier for odd characteristic.

## 2. Bshouty–Mazzawi: (0,1) parity-check matrices over Z_p

Primary source:

Nader H. Bshouty, Hanna Mazzawi,
*On Parity Check (0,1)-Matrix over Z_p*,
SIAM Journal on Discrete Mathematics 29(1), 2015, 631–657.

DOI:
https://doi.org/10.1137/120881129

The paper proves existence of a binary-entry matrix with asymptotically tight
row count such that every prescribed-size set of columns is linearly
independent over \(\mathbb Z_p\).

This is directly relevant to signature coding and coin weighing, but it
controls arbitrary-coefficient linear independence and **does not impose a
hard small Hamming weight on each column**.

Relation to ASET:

- the property is stronger than ASET where the same short-column map applies;
- it gives communication-length baselines and constructions;
- it does not by itself solve the support-constrained extremal problem.

## 3. Mathys 1990: T-active-out-of-N multiple-access coding

Primary metadata:

Peter Mathys,
*A Class of Codes for a T Active Users out of N Multiple-Access
Communication System*,
IEEE Transactions on Information Theory 36(6), 1990, 1206–1219.

DOI:
https://doi.org/10.1109/18.59923

The channel is a noiseless real adder with binary or real inputs. The work
constructs user codes for bounded active-user multiple access and includes
identification of an unknown active-user set in the stated regime.

This is further evidence that bounded-active identity recovery itself is old.
Its arithmetic is ordinary addition and it is not a hard finite-field support
extremal theorem.

## 4. Constant-column-weight group testing is not a direct closure

Aldridge–Johnson–Scarlett and follow-up work study constant/near-constant
tests-per-item designs.

This matches Mathlab's **location of the sparsity constraint**: column
weight corresponds to how many tests/coordinates an item touches.

However the standard model in those papers is Boolean OR group testing with
probabilistic/asymptotic recovery, not zero-error additive/modular subset
identification.

Therefore this literature is a structural comparator, not an ASET theorem.

## 5. Constant-weight ordinary adder remains the strongest direct sparse
neighbor found so far

Fan–Darnell–Honary (1995) prove unique bounded-active decoding from ordinary
integer sums using suitable binary constant-weight codes.

Fan–Gu–Hachimori–Miao (2021) develop constant-weight signature-code
extremal quantities and bounds in a weighted binary adder model.

These sources demonstrate that a hard signature-weight extremal problem is
well established under ordinary-addition variants.

The unresolved distinction remains:

\[
\text{hard support}
+
\text{finite-field/mod-q addition}
+
\text{zero-error all subsets through }d.
\]

## 6. Block-weight coding terminology is not enough

Coding papers using "block weight" or "sum-rank/block metric" usually bound
the support of **codewords/errors in blocks**.

Mathlab characteristic-two reduction instead needs a hard bound on the number
of nonzero blocks in **each parity-check/signature column**.

These are different orientations of the constraint.

No block-metric theorem is imported without an explicit transpose/reduction.

## 7. Audit-03 status after pass 01

No primary-verified source in this pass gives the full sharp hard-support
finite-field signature frontier.

That statement is only a status of this audit pass, not evidence of novelty.

Still required:

1. dedicated search for constant-weight/mod-q signature code extremal theory;
2. bounded-column-weight additive detecting matrices under zero error;
3. block-sparse parity-check column extremal theory;
4. q-ary support-constrained distinct-sum/additive-combinatorics results;
5. theorem-level fixed-(d,w) exponent comparison.

G1B remains OPEN.
