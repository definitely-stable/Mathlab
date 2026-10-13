# HYP-105 / issue #230 — D6-AA4-C: original-factor edit transversals and retained GF(5) positivity

**Scope:** an exact ALL-h conditional source-support invariance theorem, plus fully exhaustive finite ORIGINAL W(3,2) typed factor-support and weighted hitting-set diagnostic. **Not** a universal S_s(f,g)≥c s^6 theorem, not Branch B, not total R3 and not an ASET exponent.

**Stack:** Draft strictly on fully GitHub-hosted green D6-AA4-B PR #434, pinned parent head \`f13193e5f1841282a830ff60ceb23e2686a98147\`. No changes or merges into \`main\`, #230/#176/#169 stay OPEN.

## 1. Why the next gate should not duplicate AA4-B four-line fibers

AA4-B fixed the left ORIGINAL f, eleven of fifteen right ORIGINAL lines, and exactly four right factor IDs, and exhaustively evaluated 24 jointly globally injective label permutations, proving exact finite coherent-vs-independent cost gaps 57/68 for S68/S72. Although strong against THAT reduced relaxation, neither result is uniform over the exterior assignments, or over blocks B, or over all h.

A different exact constraint is to record **which ORIGINAL point and line identities** are actually needed by each genuinely accepted sixset. This does not rely on the physical pair **image** remaining fixed, four-factor permutations, local degree moments, or independent Q assignments. It yields a necessary number of ORIGINAL source-factor changes to destroy all previously accepted positive sixsets.

## 2. All-h typed original source-factor survival theorem

Let I_s be the ORIGINAL distinct incidence IDs of genuine W(3,s), s=2^h, h≥1. Let f,g be arbitrary complete independently globally injective typed physical pair maps into the minimal physical K_a alphabet.

Let \(\mathcal P(f,g)\) denote the set of distinct ORIGINAL six-incidence subsets Q whose exact positional classifier \(\Phi\) is in one of the seven accepted necessary GF(5)-positive classes. Define \(S_s(f,g)=|\mathcal P(f,g)|\). Let \(w_Q\) be the previously certified fixed nonnegative class-specific necessary GF(5) floor numerator, and \(Y_s(f,g)=\sum_{Q\in\mathcal P} w_Q\).

For each Q define its TWO-TYPED original source support

\[
T(Q)=\{(\mathrm{point},p): (p,\ell)\in Q\}
\;\cup\;
\{(\mathrm{line},\ell): (p,\ell)\in Q\}.
\]

This retains repeated incidence positions in Q and does not identify original points with original lines even when their physical pairs coincide. Every set T(Q) has at most 12 original factor identities, and each side at most six.

Consider ANY other genuine complete globally injective maps \(f',g'\) on the SAME ORIGINAL W(3,s), such that f'=f on original point factors outside \(B_P\), and g'=g on original line factors outside \(B_L\). The edited original factor block is \(B=B_P\sqcup B_L\), and the reassignments on B may use ANY legal physical pair images, not just permutations of the old image.

For any Q∈\(\mathcal P(f,g)\) with \(T(Q)\cap B=\emptyset\), all six left and six right physical pairs at their SAME six ORIGINAL incidence positions are identical before/after editing. Hence exactly the same one of seven GF(5) classes and the same fixed floor coefficient is retained. Without needing to reason about newly created positive sixsets,

\[
\boxed{\ S_s(f',g') \ge U_B(f,g):=
 \sum_{Q\in\mathcal P(f,g)} \mathbf1[T(Q)\cap B=\emptyset]\ }
\]

and, for the certified selected necessary GF(5) floor numerator (NOT total R3),

\[
\boxed{\ Y_s(f',g') \ge W_B(f,g):=
 \sum_{Q\in\mathcal P(f,g)}w_Q\,\mathbf1[T(Q)\cap B=\emptyset]\ }.
\]

The equalities defining U_B,W_B are exact; only the inequalities are assertions about arbitrary edited global maps, because new positive Q may appear.

### Transversal/robustness corollary

Let \(\mathcal H_{f,g}=\{T(Q):Q\in\mathcal P(f,g)\}\) be the typed ORIGINAL positive-source-support hypergraph. Define its vertex-cover/transversal number

\[
\tau(\mathcal H_{f,g}) = \min\{|B|:\ \forall Q\in\mathcal P(f,g),\
 T(Q)\cap B\neq\emptyset\}.
\]

If \(|B|<\tau\), then \(U_B\ge1\), so **every** allowed complete globally injective re-labelling of those B original factors leaves at least one seven-positive ORIGINAL sixset (even if both typed physical images change). This is exact resilience of a **previously positive fixed witness**, not a proof that ALL maps have S>0 initially or that S remains Ω(s^6).

For every integer b, define the exact **source-edit lower envelope**

\[
E_b(f,g)=\min_{\substack{B\subseteq P\sqcup L\\|B|\le b}} U_B(f,g),
\qquad
F_b(f,g)=\min_{\substack{B\subseteq P\sqcup L\\|B|\le b}} W_B(f,g).
\]

Then every global pair \((f',g')\) at source-factor edit distance ≤b from this fixed \((f,g)\) satisfies \(S(f',g')\ge E_b\), \(Y(f',g')\ge F_b\). Because U_B and W_B are non-increasing as B grows, taking exactly b is sufficient whenever b is within the source factor universe. The minimum over B is a finite original-source hypergraph covering computation, NOT a search through global label maps. **This uniformity is over all edits of bounded size around a FIXED map, not over all globally possible maps.**

### Coarse computable bound without exact transversal search

Let \(d_v=|\{Q\in\mathcal P:v\in T(Q)\}|\). Each Q touched by B is counted in at least one incidence with some v∈B, so pointwise

\[
U_B\ge \max\{0,S-\sum_{v\in B}d_v\}.
\]

The analogous weighted bound uses \(d_v^w=\sum_{Q:v\in T(Q)}w_Q\). These are standard union bounds and not claimed novel. The exact transversal audit is stronger because it tracks all overlaps between affected Q by their genuine original factor IDs.

## 3. Exact original W(3,2) finite audit, no new GF(5) assumptions

Freeze accepted TRUE ORIGINAL schemes S68 and S72 (same symplectic W(3,2), V=15 typed points and V=15 typed lines, K6 physical alphabet, 45 distinct original incidences). Build the positive-source hypergraph using all 62,370 original left A/B/C six-incidence candidates, comparing the historical GF(5) accepted-seven classifier to the independently implemented AA1 positional classifier on every ACCEPTED Q, preserving its immutable six ORIGINAL incidence IDs and seven class tag. Require the original S/Y regression controls:
- S68: S=68, Y=3,112,510.
- S72: S=72, Y=3,283,610.

Encode each original source point factor with bit 0..14 and each original source line factor with bit 15..29. Encode each positive ORIGINAL sixset as a separate bit in a second bitmap, even if its typed factor support equals that of another Q. For each v, compute a bitset of ALL positive original Q touched by v. For an arbitrary source-factor edit B, the OR of these incidence bitsets gives exactly the positive Q whose class might change; its complement gives EXACT U_B and W_B, independently of any chosen future physical assignment.

Exhaust the following ORIGINAL factor-support searches for both schemes:

1. **All 2^15=32,768 subsets** of original point factors; compute exact full one-sided transversal number and every fixed-b robust lower envelope for b=0..15.
2. **All 2^15=32,768 subsets** of original line factors; compute its separately exact transversal number and fixed-b envelope, preserving type distinction.
3. **ALL** mixed subsets of the 30 typed original factors of sizes b=0..5, i.e. Σ_{b=0}^5 C(30,b) = **174,437** source-factor blocks, with exact retained-positive and weighted-GF5 minima and count of zero-survivor blocks. If no mixed transversal occurs by b=5, report only rigorous lower bound τ_mixed≥6; never invent or extrapolate its precise value.

For every b record the number of all tested source supports, worst original factor block, minimum U_B, independent minimum W_B, and number of source-factor hitting sets (blocks with U_B=0). Output exact integral machine report on hosted Linux; no external SAT/SDP solver required.

### Independent falsification

As a second validation, take the **genuine original W32 S68** source, simultaneously swap the physical labels of ORIGINAL point factors 0,1 and ORIGINAL line factors 0,1. These are two independent full globally injective physical pair maps. Recompute the AA1 physical seven classifier on every prior positive original Q that does NOT touch the four changed typed factor identities: require unchanged seven class and unchanged GF(5) weight. Compare exact survivor count/weight against the bitset oracle. Independently brute-force a synthetic size-5 source hypergraph over every one of its 32 source-factor subsets and compare complete weighted and unweighted survivor profiles, as well as transversal number.

For the two AA4-B predeclared original line four-blocks, record the U_B/W_B lower floors as absolute **block edit-invariant** controls. They must not exceed prior complete 24-permutation coherent fiber minima. This is not a claim that U_B equals a fiber minimum.

## 4. Scientific disposition

The all-h theorem is a direct source-support preservation argument. The exact W32 hypergraph transversal/robustness numbers, if nontrivial, are defensible finite discoveries for these frozen correlations. No new universal exponent, positive \(\Omega(s^6)\) bound or infinite correlated counterexample follows: a completely different globally injective f,g may have a different hypergraph, including one with no accepted positive Q, unless Branch A is separately proved.

**Next genuinely global gate:** find a lower bound on \(E_b(f,g)\) that is uniform over ALL globally injective f,g and grows at least c s^6 for appropriately chosen source-block families, or devise a source-support-independent capacity forcing theorem. Local resilience around low-S fixed maps alone cannot substitute for existence of positive motifs across all maps.

Accept implementation only after dedicated AA4-C, INDEX, Proof Audit and full Research GitHub-hosted SUCCESS on the exact final PR SHA, plus independent mathematical review. Never merge the draft stack or close #230/#176/#169 automatically.
