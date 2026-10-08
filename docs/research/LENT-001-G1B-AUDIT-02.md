# LENT-001-G1B — primary-source audit 02

Status: **PRIMARY-SOURCE VERIFIED / G1B STILL OPEN**

Date: 2026-10-08

Audit 02 focuses on the two questions left most dangerous after Audit 01:

1. is bounded-active modular subset identification itself already established?
2. if so, is the **bounded per-signature support** frontier already established too?

The answer to the first is yes. The answer to the second is not yet closed.

## 1. Binary ASET without a support constraint is exactly BCC

Primary source:

Keren Censor-Hillel, Bernhard Haeupler, Nancy Lynch, Muriel Médard,
*Bounded-Contention Coding for the Additive Network Model*,
Distributed Computing 28 (2015), 297–308.
Earlier DISC 2012 version:
*Bounded-Contention Coding for Wireless Networks in the High SNR Regime*.

Primary manuscript:
https://arxiv.org/abs/1208.6125

Published-version DOI:
https://doi.org/10.1007/s00446-015-0241-9

The source defines an \([M,m,a]\)-BCC code as a set

\[
C\subseteq\{0,1\}^m,\qquad |C|=M,
\]

such that for any two distinct subsets \(S_1,S_2\subseteq C\) with

\[
|S_1|,|S_2|\le a,
\]

their XORs are different.

This is definitionally the binary ASET exactness condition with

\[
V=M,\qquad d=a,
\]

when the ASET column-support restriction is removed.

The paper also constructs BCC codes using parity-check matrices of binary
linear codes and records length

\[
m=O(a\log M),
\]

which is information-theoretically optimal in order.

### Consequence

The broad object

> exact identification of an unknown subset of at most \(d\) users from a
> binary additive/XOR state

is established prior art.

Therefore Mathlab must not claim novelty for binary ASET itself.

The remaining Mathlab parameter absent from the BCC definition is the
per-codeword/update support constraint

\[
|\operatorname{supp}(a_i)|\le w.
\]

The standard parity-check construction does not freeze a small column
weight.

Novelty effect:

**UNCONSTRAINED BINARY ASET = KNOWN OBJECT; SPARSE-UPDATE EXTREMAL QUESTION
REMAINS.**

## 2. Restricted-access modulo-2 multiple access is older still

Primary source:

Gregory Poltyrev and Jakov Snyders,
*Linear codes for the sum mod-2 multiple-access channel with restricted
access*, IEEE Transactions on Information Theory 41(3), 1995, 794–799.

DOI:
https://doi.org/10.1109/18.382029

The model has a fixed family of \(N\) potential users and at most \(m<N\)
simultaneously active users. The receiver does not know the active subset in
advance. The paper develops modulo-2 separable code collections that recover
the active users/messages over the sum-mod-2 channel.

This is a richer communication model than one-signature-per-user ASET, but it
confirms that **restricted access + modular addition + unknown active set** is
long-established binary multiple-access territory.

Novelty effect:

**additional binary STOP evidence.**

## 3. Finite-field K-out-of-M signature codes directly cover the broad q-ary idea

Primary source:

Jasper Goseling, Cedomir Stefanović, Petar Popovski,
*Sign-Compute-Resolve for Tree Splitting Random Access*,
IEEE Transactions on Information Theory 64(7), 2018.

arXiv:
https://arxiv.org/abs/1602.02612

DOI:
https://doi.org/10.1109/TIT.2018.2839197

The paper explicitly studies signature codes for the

\[
\mathbb F_q
\]

adder channel with up to \(K\) active users out of \(M\).

It imports a Bose–Chowla/Lindström integer construction with integers
\(s_1,\ldots,s_M\) satisfying

\[
\sum_{i\in L_1}s_i\ne\sum_{i\in L_2}s_i
\]

for every distinct

\[
L_1,L_2\subseteq[M],\qquad
|L_1|,|L_2|\le K.
\]

The \(r\)-ary digits of the \(s_i\) are mapped to \(\mathbb F_q\).
By choosing parameters so that adding at most \(K\) digits does not wrap in
\(\mathbb F_q\), the receiver reconstructs the integer sum and therefore the
active set.

The resulting signatures are exactly a finite-field bounded-active-set
identification construction.

### Important restrictions

The construction deliberately takes a **large prime field**; the paper
assumes \(M<q<2M\) and chooses the digit radix so that symbol sums do not
wrap.

It does not impose Mathlab's update-locality condition

\[
|\operatorname{supp}(a_i)|\le w.
\]

Its theorem controls signature length, not per-signature support.

### Consequence

The broad claim

> q-ary exact subset sums through capacity d are a new coding object

is false.

The defensible Mathlab target is narrower:

> what is the sharp state-size / universe-size frontier for **sparse
> finite-field signatures** under a hard per-signature support bound?

Novelty effect:

**UNCONSTRAINED FINITE-FIELD ASET = ESTABLISHED SIGNATURE-CODE TERRITORY;
SPARSE-UPDATE FRONTIER REMAINS UNRESOLVED.**

## 4. Bounded-contention coding also explains the information scale

BCC gives binary exact subset identification using \(O(d\log V)\) state bits
without a small update-support guarantee.

This is consistent with the Sparse-Update Hamming-Ball Bound:

- if communication is kept near the information scale;
- and \(q=2\) is fixed;
- then bounded/constant update support cannot persist in the large-universe
  near-optimal regime.

Thus G1B changes the interpretation of the baseline theorem in a useful way:
it separates the already-known **communication-efficient** construction
problem from the still-interesting **communication-efficient + sparse-update**
problem.

## 5. Constant-weight ordinary-adder codes cover another side of the frontier

Primary source:

P. Z. Fan, M. Darnell, B. Honary,
*Superimposed codes for the multiaccess binary adder channel*,
IEEE Transactions on Information Theory 41(4), 1995, 1178–1182.

DOI:
https://doi.org/10.1109/18.391266

The superposition is ordinary integer addition. The paper proves that
appropriate binary constant-weight codes allow unique recovery of any set of
at most \(m\) simultaneously active users.

This is a direct example of:

- bounded codeword Hamming weight;
- bounded active-set identification;
- exact noiseless decoding;

but under ordinary addition rather than modulo-two addition.

Therefore even

> support-bounded active-user signatures

is not new as a generic concept.

What remains potentially new is the **modular finite-field + hard support
bound + sharp extremal** combination.

## 6. Low-density signature literature is extensive but not an exact substitute

Primary example:

Reza Hoshyar, Ferry P. Wathan, Rahim Tafazolli,
*Novel Low-Density Signature for Synchronous CDMA Systems Over AWGN
Channel*, IEEE Transactions on Signal Processing 56(4), 2008.

DOI:
https://doi.org/10.1109/TSP.2007.909320

This literature deliberately assigns each user a spreading signature with
few nonzero chips.

It is highly relevant terminology/engineering prior art for "sparse
signature".

However its objective is noisy multiuser detection and practical
performance, not deterministic all-input injectivity of every active subset
through capacity \(d\).

It cannot be used as an ASET theorem without a separate reduction.

Novelty effect:

**terminology and engineering neighbor; not a zero-error extremal
replacement.**

## 7. Characteristic-two structural collapse

Let

\[
q=2^s.
\]

Because the field has characteristic two,

\[
-1=1.
\]

For any ASET column family \(a_1,\ldots,a_V\in\mathbb F_q^m\),

\[
\text{ASET exact through }d
\]

is equivalent to

\[
\sum_{i\in U}a_i\ne0
\]

for every nonempty \(U\subseteq[V]\) with

\[
|U|\le2d.
\]

Now fix an \(\mathbb F_2\)-basis of \(\mathbb F_q\). Coordinate expansion is
an additive-group isomorphism

\[
\beta:\mathbb F_q^m\longrightarrow\mathbb F_2^{sm}.
\]

Hence ASET exactness is equivalent to saying that no nonempty set of at most
\(2d\) expanded binary columns has XOR zero.

This is exactly the binary small-dependency condition, with one important
locality change:

- one original q-ary coordinate becomes one binary **block** of \(s\) bits;
- q-ary support at most \(w\) becomes at most \(w\) nonzero binary blocks.

Thus characteristic-two ASET is a **block-sparse binary parity-check/BCC
problem**, not a genuinely arbitrary-coefficient q-ary dependence problem.

A complete proof is recorded separately in
\`LENT-001-G1B-CHAR2-REDUCTION.md\`.

### Consequence for the G1B split

The old provisional split

\[
q=3\quad\text{versus}\quad q>3
\]

is mathematically wrong.

The first structural split must be

\[
\boxed{\operatorname{char}\mathbb F_q=2
\quad\text{versus}\quad
\operatorname{char}\mathbb F_q\ne2.}
\]

Within odd characteristic, q=3 remains special because every nonzero
coefficient is already \(\pm1\); the gap there comes from the separate side
bounds. For odd q>3, both side bounds and restricted coefficient values
matter.

## 8. Finite Field Multiple Access / USPM is additional modern prior art

Primary sources:

Qi-yue Yu, Jiang-xuan Li, Shu Lin,
*Finite Field Multiple Access*, arXiv:2303.14086 (2023).

https://arxiv.org/abs/2303.14086

Qi-yue Yu,
*Finite Field Multiple Access III: from 2-ary to p-ary*,
arXiv:2504.06937 (2025).

https://arxiv.org/abs/2504.06937

These works explicitly use a unique-sum-pattern mapping (USPM) over finite
fields to distinguish multiple users.

Their user/codebook model is not the same as one-signature-per-universe-item
ASET, and their sparse-form system terminology does not by itself impose the
Mathlab column-support extremal condition.

Still, they are mandatory modern prior art for any external statement such
as "finite-field unique-sum multiple access is new".

## 9. Revised novelty statement

After Audits 01–02, the following broad claims are rejected:

- exact bounded-active subset identification is new;
- binary modular bounded-active identification is new;
- finite-field K-out-of-M signature coding is new;
- constant/low-weight active-user signatures are generically new.

The remaining candidate is substantially narrower:

\[
\boxed{
\textbf{sharp support-constrained finite-field signature frontier}
}
\]

namely the extremal behavior of

\[
A_q^{\mathrm{set}}(m,w,d)
\]

when \(w\) is a genuine small update-locality parameter.

The novelty-sensitive question is no longer whether ASET exists. It is:

> Does the hard support constraint create a sharp extremal law that is not
> already covered by sparse parity-check, constant-weight adder,
> signature-code, detecting-matrix, or bounded-contention results?

## 10. Remaining blockers after Audit 02

G1B should not close yet.

The next and possibly final source tranche must target:

1. zero-error **constant-weight / sparse** signature codes specifically over
   modulo-q or finite-field adders;
2. bounded-column-weight quantitative/detecting matrices with exact sparse
   input recovery;
3. block-sparse binary BCC/parity-check results matching the
   characteristic-two reduction;
4. q-ary Hamming-ball / support-constrained \(B_h\) or signed-sum families;
5. exact asymptotics for fixed \(d,w\) under these constraints.

Until those are closed:

**G1B STATUS = OPEN.**
