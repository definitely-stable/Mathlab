# TOM-003 / Phase A — exact no-effect verification and the trusted-old-value boundary

Date: 2026-10-08. Issue: [#49](https://github.com/definitely-stable/Mathlab/issues/49).
Parent scouting program: [TOM-001 #15](https://github.com/definitely-stable/Mathlab/issues/15).

**Decision:** O01 FALSIFICATION-FIRST / NON-NOVEL BASELINE.
**Theorem classification:** CLASSICAL FINITE-STATE/MYHILL–NERODE COROLLARY,
with self-contained proof. **Scientific originality: NOT CLAIMED.**
**Rust/product status:** NO-GO as a standalone exact threshold/no-effect
counter. A genuinely new theorem / Rust primitive has NOT been selected.

## 1. Why this lane was selected, and the candidates rejected

Do not continue a finite ASET maximum as a product-design argument.
G2B-B2's independently checked finite certificate proves
A_5^set(3,2,2)=10, but does not by itself yield a compact, competitive
bounded-active-key Rust object. HYP-001 and HYP-002 already prove
Theta_q(m^(3/2)) and Theta_q(m²) in constrained regimes, but do not
establish *publication novelty*, practical decoding efficiency,
unconditional valid updates, or competitive state size. HYP-002-C
showed a 3-to-2 overload alias and worse payload vs two direct IDs.
Therefore G2 receives the narrower decision **G2_REDUCE_TARGET**:
retain exact proof/coding research, but no G4 originality promotion or
Rust development based merely on existing asymptotic exponents.

Source-aware comparison, ordered by the strongest *model overlap*:

| Candidate | Nearest primary result | Main overlap / falsifier | Decision |
|---|---|---|---|
| O10 sparse ASET & two-ID decoder | Mathlab #25, GF5 checked certificate and known B_h/separable/signature codes | no independently original asymptotic theorem or end-to-end advantage; modulo-3 overload aliases | REDUCE_TARGET; no crate |
| Rateless/new Minisketch alternative | Rateless IBLT SIGCOMM 2024; CertainSync SIGMETRICS 2025; IBLT self-sizing preprint arXiv:2608.26537 | adaptive unknown d, eventual worst-case completion, and in-band sizing already have explicit prior claims under distinct assumptions | STOP-BROAD as a claimed new primitive |
| O05 adversarial CDC/local boundaries | Berger, *Chonkers*, arXiv:2509.11121 (v2, 2025) | provable bounds on size/locality already claimed, periodic exceptions matter | STOP-BROAD |
| O07 dynamic synchronizing positions | Ellert–Kociumaka, STACS 2026, DOI 10.4230/LIPIcs.STACS.2026.36; *Longest Common Extension of a Dynamic String in Parallel Constant Time*, CPM 2026 | 2026 STACS theorem is **static preprocessing/queries**, while the CPM paper explicitly discusses dynamic synchronizing sets; neither justifies "first dynamic" | NO NOVELTY CLAIM, defer |
| O13 reusable authenticated multiproofs | Ethereum SSZ multiproof spec; transparency-dev compact ranges; PICKLE, FutureG/NDSS 2026 | shared sibling map, inter-version hash/path updates, and cached proof reuse already described | STOP-BROAD |
| O04/O06 strong history independence | HI dynamic partitioning 2024/2026, Chonkers/Yarn 2025 | physically observable representation and deterministic serialized tree are distinct; strong published alternatives | STOP-BROAD |
| **O01 exact no-effect** | Ramalingam 1993; self-adjusting computing; differential execution ECOOP 2025; Wang–Yin certificates 2014 | no complete bounded-state/old-validation contract in Mathlab; easy to make false claims with free old bits | **SELECT FOR NEGATIVE GATE**, not novel theorem |

Source URLs:
- https://arxiv.org/abs/2402.02668 (rateless IBLT), https://arxiv.org/abs/2504.08314 (CertainSync), https://arxiv.org/abs/2608.26537 (self-sizing IBLT);
- https://arxiv.org/abs/2509.11121 (Chonkers);
- https://doi.org/10.4230/LIPIcs.STACS.2026.36 (string synchronizing sets), https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.20/LIPIcs.CPM.2026.20.html (dynamic strings);
- https://github.com/ethereum/consensus-specs/blob/master/ssz/merkle-proofs.md and https://github.com/transparency-dev/merkle/blob/main/docs/compact_ranges.md and https://intendproject.eu/resources/conference-papers/66 (PICKLE);
- https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/ (Ramalingam),
  https://doi.org/10.4230/LIPIcs.ECOOP.2025.20 (Kumar–Pacak–Erdweg),
  https://arxiv.org/abs/1404.5743 (Wang–Yin static cell-probe certificates).

Verification tier: publisher/arXiv abstracts and available HTML/source
statements were inspected; this is NOT a theorem-by-theorem proof audit
of every paper. Distinct cost models are explicitly NOT identified.
All date/version/novelty statements remain scoped to the named models.

## 2. Freeze the machine and observation model FIRST

Fix a known Boolean function f:{0,1}^n->{0,1}, n>=1.
It may be a bounded-fanin DAG whose root computes f. The algorithm's
retained state after initialization is M(x), where x is any input vector.
It may preprocess freely ONCE, but all bits that must survive the
initialization are charged (including caches, indices, and "metadata").
The function/circuit itself is public, fixed and not charged as
input-dependent retained state.

**Model U: untrusted overwrite**
- The only operation is write(i,b), where i is a coordinate and b is a
  new Boolean value. The previous value is NOT supplied.
- Every sequence is valid; the transition must be correct for all x.
- After every write the algorithm emits the exact updated f(x)
  (or equivalently a correct change/no-change flag when its prior
  root observation is available).
- Zero random-access probes of *unretained* original input; no hidden
  old-value oracle. Time is not bounded by this theorem.
- Deterministic retained state; error probability zero.

**Model T: *trusted* delta**
- The operation is delta(i,old,new) WITH AN EXTERNAL PROMISE that
  old really equals the current x_i; an invalid promise is outside
  the mathematical guarantee.
- No promise that a compact standalone object can check the old value.
- Cost ledger MUST charge external verification, retained membership
  information, cryptographic witness bytes and hashing work elsewhere.
- The useful hypothetical product operation is
  certify_unchanged(trusted_delta) for a fixed output function.

These are DIFFERENT APIs and their complexity claims must not be mixed.
O01's originally proposed "exact certificate" becomes vacuous if a
trusted old-state oracle is smuggled into Model U for free, or if an
algorithm is allowed to reject every no-effect change.

## 3. Exact classical overwrite-state theorem (no novelty claim)

For Boolean f, coordinate i is **essential** when there is some
assignment to every other coordinate for which flipping i changes f.
Let E(f) be the essential coordinate set, e=|E(f)|.

**THEOREM (finite-state consequence).** An arbitrary-overwrite exact
deterministic machine of Model U needs at least 2^e distinct persistent
input-dependent states, hence e bits in the worst case. Storing the
e essential input bits is sufficient. Therefore the minimal
information-theoretic state size is **exactly e bits**.

**Proof, necessity.** Let x,y agree on all but possibly several
coordinates and differ on any essential i. By essentiality there
exists an assignment z to the OTHER n-1 coordinates such that
f(z,i=0) != f(z,i=1). Feed the same sequence of writes that
sets all j != i to z_j, to two runs initialized by x and y.
Their values at i remain unequal; the exact observed outputs
after this common trace differ. Deterministic machines with
the same initial retained state and the same trace cannot
produce different outputs. Hence M(x) != M(y) whenever x,y
differ on any essential coordinate. There are 2^e possible
projections onto the essential coordinates; each must have
a distinct retained state.

**Sufficiency.** Store x restricted to E(f). Writes to an
inessential coordinate have no effect; writes to essential i
overwrite its stored bit. Since f does not depend on any
inessential coordinate, this information computes the exact
root output under all traces. QED.

This is finite automata **observational equivalence/state
minimization**, an elementary instance of Myhill–Nerode
reasoning, NOT a claimed new combinatorial coding theorem.
The bound counts information only, not update CPU or program
storage. For threshold/AND/OR/XOR involving all n input
coordinates, e=n: exactly n persistent bits are necessary
if *arbitrary overwrites must be answered without old bits
and without probing an external original state*.

## 4. A conditional compression *upper* bound and its hidden cost

For threshold f_k(x)=1[sum_i x_i>=k], with 1<=k<=n,
Model T maintains c=sum_i x_i exactly, initially 0..n.

    c' = c + new - old
    no_effect = (c>=k) == (c'>=k).

It uses ceil(log2(n+1)) bits, exactly n.bit_length() in Python
integer arithmetic, and O(1) count operations per update under
the promise that the externally supplied old bit was correct.

**NOT A STANDALONE SAVING:** if old is obtained from a retained
n-bit exact membership array, the total retained state is at
least n plus the counter; alternatively, old might be part of
a *pre-existing authoritative database* (then the summary is
incremental extra metadata, but the upstream read/check cost
must be charged). A hash commitment without a checked opening
does not give information-theoretic certainty. A cryptographic
opening requires explicit proof bytes/security assumptions.
The theorem in §3 remains valid for Model U.

**Small adversary:** x=(1,1,0), y=(1,0,1), both contain two
ones and have threshold-2 root true. Overwriting coordinate 1
with 0 makes the first root false and the second true. A state
holding only c=2 and receiving write(1,0) cannot distinguish them.
If the second state is fed the false statement old=1 (true old=0),
the purported "trusted delta" update reports a root change
that did not happen, while its count still lies in range.
No count-range guard detects the false promise.

## 5. The executable falsification experiment

Research implementation: research/tom_trust_boundary.py.
Independent test: research/test_tom_trust_boundary.py.

- Enumerate **ALL** Boolean functions for n=1,2,3:
  4, 16 and 256 truth tables. At n=3, histogram of essential
  variable counts e=0,1,2,3 is (2,6,30,218).
- Independently construct Moore-machine states for *every*
  initial bit vector, use all unconditional writes (i,b),
  partition first by observed root, then repeatedly refine by
  labeled successor partition. Count and compare all pairs
  of resulting equivalence classes against the essential-bit
  theorem. No theorem code is imported into the Moore oracle.
- Exhaust all length-three valid trusted-delta traces for all
  n<=4, all thresholds, and all initial inputs; compare changed
  and root against full recomputation.
- Reproduce the same-count/untrusted-write divergence;
  simulate a wrong claimed old bit and show a false no-effect
  guarantee; invalid arguments fail closed.
- Hosted CI checks these *finite* instances only. Its success
  is not a Lean formalization or a novelty certificate.

## 6. Product go/no-go and next target

**O01-D1: STOP standalone** for a generic Boolean no-effect
certificate claiming exactness under free arbitrary overwrites.
The strict impossibility is known in automata theory, and the
trusted-delta workaround already equals textbook maintained
counts with **external** old-value validation.

**O01-D2 (research only, separate authorization required):**
Study a concrete authenticated batch-update workflow where the
consumer already possesses a trusted authoritative lookup or
proof and the question is incremental EXTRA verifier work. Freeze
the full proof size, cache, memory, trust and output guarantee;
compare against direct state lookup, ordinary counters, dynamic
Merkle multiproofs and PICKLE. A genuinely new narrow
information/probe lower bound or an independently measured
end-to-end win is REQUIRED before Rust prototype authorization.

**Mathlab G2:** exact sparse ASET results stay accepted (including
G2B-B2 GF5=10), but G4 theorem selection is deferred and
HYP-001/002 uniqueness remains unestablished. Decision for product
priority: **G2_REDUCE_TARGET**. This does not say the original
finite ASET theorem is false or that all research gaps are closed.

Next permitted research: challenge O01-D2 with a fully charged
reference workflow or search a distinct product operation.
Do NOT promote D1 as a new theorem, publication, patent,
Lean result, or Rust crate.
