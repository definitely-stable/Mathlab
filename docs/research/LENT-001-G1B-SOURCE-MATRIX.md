# LENT-001-G1B — primary-source matrix

Status: **OPEN / AUDIT 02 RECORDED**

Issue: #6

Rows marked VERIFIED_PRIMARY have been checked against a primary paper,
author manuscript, proceedings record, or publisher metadata. A verified
neighboring model is not automatically an ASET theorem: every transfer still
needs the implication direction recorded below.

## A. Direct modular active-set identification

| Source | Exact model | Relation to ASET | Support/locality status | Confidence |
|---|---|---|---|---|
| Censor-Hillel–Haeupler–Lynch–Médard, *Bounded-Contention Coding for the Additive Network Model* / arXiv:1208.6125 | binary codewords; XORs of every two distinct subsets of size ≤a must differ | **definitionally binary ASET when the support bound is removed** | no hard small column-weight parameter in the BCC definition | VERIFIED_PRIMARY |
| Poltyrev–Snyders (1995), *Linear codes for the sum mod-2 multiple-access channel with restricted access* | unknown active subset among N potential users over sum-mod-2 MAC; active-user/message separation | richer binary modular multiple-access model | not a hard per-signature support extremal theorem | VERIFIED_PRIMARY |
| Goseling–Stefanović–Popovski, arXiv:1602.02612 / TIT 2018 | up to K active users; signatures summed in \(\mathbb F_q\); identities recoverable from the sum | direct finite-field bounded-active signature-code prior art | construction optimizes signature length; no hard support≤w frontier | VERIFIED_PRIMARY |
| Yu–Li–Lin, arXiv:2303.14086 and later FFMA/USPM work | finite-field unique sum-pattern multiple access | modern finite-field unique-sum neighbor; different codebook/user model | sparse-form terminology is not by itself ASET column-support extremality | VERIFIED_PRIMARY at model level |

### Consequence

The broad object "exact bounded-active subset identification under modular /
finite-field addition" is not a new Mathlab object.

The G1B novelty question is now specifically the **hard support-constrained
extremal frontier**.

## B. Sparse parity-check / short-dependency baselines

| Source/object | Model | ASET relation | Confidence |
|---|---|---|---|
| Lefmann–Pudlák–Savický (1996) | binary bounded-column-weight parity-check matrices | direct q=2 sparse baseline | VERIFIED at model level |
| Lefmann (2005), *Sparse Parity-Check Matrices over GF(q)* | support≤r; every k columns independent for arbitrary nonzero field coefficients | stronger than odd-characteristic ASET; constructions transfer, q>2 upper bounds do not automatically transfer | VERIFIED_PRIMARY |
| Naor–Verstraete (2005) | improved sparse parity-check bounds | binary/finite-field neighboring baseline | NEEDS_THEOREM_MAP |
| characteristic-two block reduction | \(q=2^s\) ASET expanded through an \(\mathbb F_2\) basis | exact block-sparse binary short-dependency problem | PROVED_IN_REPO |
| block-sparse BCC/parity-check extremal literature | hard bound on number of nonzero s-bit coordinate blocks per column | potentially direct char-2 closure | NEEDS_PRIMARY_CHECK |

## C. Dissociated / free / signed-relation families

| Source/object | Exact definition | Relation to ASET | Confidence |
|---|---|---|---|
| Shkredov, arXiv:2205.07296 | k-dissociated bounds coefficient magnitude \(|\varepsilon_\lambda|\le k\) | full dissociation is stronger than finite-d ASET; terminology is not bounded order | VERIFIED_PRIMARY |
| Nešetřil–Rödl–Sales (2024), free | all finite subset sums distinct | stronger than every finite-d ASET | VERIFIED_PRIMARY |
| Nešetřil–Rödl–Sales (2024), h-free | one collision side ≤h, the other unrestricted | stronger than ASET_h | VERIFIED_PRIMARY |
| two-sided h-free / both-side-bounded signed systems | both \(n_+,n_-\le d\) | potentially definitionally closest odd-characteristic object | NEEDS_PRIMARY_CHECK |
| bounded-support finite-field dissociated families | additionally support≤w per generator | could directly constrain sparse ASET | NEEDS_PRIMARY_CHECK |

## D. Sidon / \(B_h\) / fixed-cardinality additive uniqueness

| Source/object | Exact model | Relation to ASET | Confidence |
|---|---|---|---|
| Nešetřil–Rödl–Sales \(B_h^*\) | sums of h distinct elements unique | ASET_d implies \(B_h^*\) for h≤d; converse absent | VERIFIED_PRIMARY |
| Kiss–Sándor, arXiv:2006.02783 | separates distinct-term and repetition-allowed h-sum representation functions | confirms convention split | VERIFIED_PRIMARY |
| Huang–Tait–Won, arXiv:1809.05117 | Sidon/2-cap in \(\mathbb F_3^n\), including repeated-summand equations | not ASET d=2; standard Sidon maximum cannot be imported automatically | VERIFIED_PRIMARY |
| Sima–Li–Shomorony–Milenkovic, arXiv:2303.12990 | constant-weight binary vectors; real-valued sums of distinct pairs unique | support-constrained ordinary-addition equal-cardinality neighbor | VERIFIED_PRIMARY |
| q-ary Hamming-ball / support≤w \(B_h\) families | finite-field or modular distinct-sum uniqueness with hard generator support | potentially direct sparse-ASET bound | NEEDS_PRIMARY_CHECK |

## E. Sparse / constant-weight signature and adder codes

| Source | Exact model | Relation to ASET | Confidence |
|---|---|---|---|
| Fan–Darnell–Honary (1995), DOI 10.1109/18.391266 | constant-weight binary user codewords; ordinary adder; any ≤m active users uniquely decodable under correlation condition | proves sparse exact active-user signatures are old in ordinary-addition model | VERIFIED_PRIMARY |
| Fan–Gu–Hachimori–Miao, arXiv:1905.10180 / TIT 2021 | t-signature + constant-weight t-signature for weighted binary adder | strong support-constrained ordinary-adder neighbor | VERIFIED_PRIMARY |
| Erdoğan–Maringer–Polyanskii, arXiv:2206.10735 | q-ary signatures with integer sums | all-subset integer-addition neighbor | VERIFIED_PRIMARY |
| Hoshyar–Wathan–Tafazolli (2008), low-density signatures | sparse signatures for noisy CDMA detection | terminology/engineering neighbor only; not zero-error all-input injectivity | VERIFIED_PRIMARY |
| zero-error constant-weight/sparse signatures over finite-field/mod-q adder | hard support≤w plus bounded active set under modular addition | could directly absorb Mathlab target | NEEDS_PRIMARY_CHECK |

## F. Additive / quantitative group testing

| Source/object | Model | Relation to ASET | Confidence |
|---|---|---|---|
| Chang–Chen–Guo–Huang, arXiv:1303.6020 | additive \((D,d)\)-separability for d-sparse vectors under standard arithmetic | for D={0,1}, ordinary-arithmetic bounded-d analogue; modular ASET implies ordinary separability | VERIFIED_PRIMARY |
| bounded-column-weight quantitative/detecting matrices | exact sparse-input recovery + hard measurement-column weight | may provide necessary ASET upper bounds if arithmetic transfer applies | NEEDS_PRIMARY_CHECK |
| modulo-q quantitative/detecting matrices | exact d-sparse recovery modulo q | potentially direct ASET object | NEEDS_PRIMARY_CHECK |

## G. Characteristic split

### Characteristic two: \(q=2^s\)

Repository theorem:

\[
\text{ASET}_d
\Longleftrightarrow
\text{no nonempty GF(2) dependency among }\le2d
\]

after expanding every \(\mathbb F_q\) coordinate to an s-bit block.

The support constraint becomes:

\[
\text{at most }w\text{ nonzero binary blocks per column}.
\]

Status: **block-sparse binary BCC/parity-check lane**.

### q=3

Every nonzero scalar is \(\pm1\), but the separate positive/negative side
bounds distinguish ASET from ordinary short linear dependence.

Status: **side-bound gap remains**.

### Odd q>3

Both restrictions matter:

- allowed ASET coefficients are only \(\pm1\);
- positive and negative sides are separately bounded by d.

Status: **coefficient + side-bound gap remains**.

## H. Arithmetic transfer rule

For the same integer-represented columns and bounded-d binary source domain:

\[
\text{mod-}q\text{ ASET}
\Longrightarrow
\text{ordinary-integer additive separability}.
\]

Therefore a compatible upper bound for the ordinary-addition super-class can
be necessary for ASET.

The reverse direction does not hold in general because distinct integer sums
may coincide modulo q.

## I. Current decision table

| Regime | What is already known | Remaining support-sensitive question | G1B status |
|---|---|---|---|
| q=2 | BCC = unconstrained binary ASET; sparse parity-check theory | sharp effect of hard small column weight is already heavily overlapped by sparse parity-check literature | STOP as main novelty lane |
| char 2, q=2^s, s>1 | exact block-binary reduction | sharp block-sparse BCC/parity-check extremal law | OPEN |
| q=3 | finite-field signature coding exists; standard Sidon and arbitrary-linear models are non-equivalent | sharp support≤w law with two-sided side bounds | OPEN |
| odd q>3 | finite-field bounded-active signatures exist; Lefmann gives stronger sparse constructions | sharp support≤w law under restricted ±1 coefficients + side bounds | OPEN |

## J. What remains before G1B can close

Audit 03 must specifically target:

1. block-sparse BCC/parity-check results for characteristic two;
2. zero-error hard-sparse finite-field/mod-q signature codes;
3. bounded-column-weight quantitative/detecting matrices;
4. support-constrained q-ary \(B_h\)/signed-sum families;
5. fixed-\((d,w)\) asymptotics in any of these equivalent/stronger models.

Until then:

**G1B STATUS = OPEN.**
