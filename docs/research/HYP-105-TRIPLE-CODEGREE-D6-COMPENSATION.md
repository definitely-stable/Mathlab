# HYP-105 / #230 — AA4-TCN: triple-common-neighborhood transversal D6 transfer

**Status:** an all-\(h\) exact **positive subclass identity**, an unconditional same-fixed-map lower bound on genuine accepted ORIGINAL six-incidence GF(5) D6 motifs in terms of physical triple-common-neighbor concentration, plus independently counted finite true-source oracles. **Root remains OPEN_WITH_FORMAL_BLOCKER.** This is not an unconditional \(S_{\rm seven}=\Omega(s^6)\), nor a theorem saying that arbitrary large five-ID noise forces D6. It is a deterministic compensation criterion requiring *three coordinate-separated hubs with a coordinate-spread common neighbor set*.

## 1. Why this slice and what already existed

The stacked PRs #648–656 establish that naive five-flag second moments and even a global average \(O(s^2)\) completion bound for defective physical C6s cannot hold for arbitrary correlated full physical label maps (the latter conditional on the infinite packet existence proof of #651). In the *same* coherent packet family, PR #651 proved many positive ORIGINAL sixflag D6 motifs using physically coherent hub/free K3,3 subgraphs; it was a **restricted construction**, not a universal same-map implication. AA4-RC6 #652 separately established the exact all-\(h\) bijection between physical coordinate-rainbow simple C6 and ORIGINAL GF5 accepted D6 sixsets.

**New result:** eliminate any reliance on the specific #651 packet construction and promote its essential **positive K3,3 mechanism to a deterministic all-map lower-bound certificate**. The model uses the genuine original symplectic \(W(3,s)\), \(s=2^h\), all complete separately globally injected source point/line labels \(f,g\in\binom{[a]}2\), arbitrary correlation, true original incidence flags and the established seven-class GF5 D6 acceptance rule. No source-free K3,3 is ever declared sufficient; every physical adjacency must come from a TRUE original incidence.

## 2. All-h theorem: exactly six positive ORIGINAL D6 per transverse physical K3,3

Let \(H(f,g)\) be the simple physical graph on corners \((u,x)\in[a]^2\), each physical edge backed by exactly one genuine original source incidence flag \((p,l)\), as in AA4-RC6. Call an unordered hub triple

\[
U=\{h_1,h_2,h_3\}\subseteq V(H)
\]

**coordinate-injective** when the three first-coordinates are all distinct and the three second-coordinates are all distinct. Its admissible **common free-neighbor set** is

\[
T(U)=\{z\in N(h_1)\cap N(h_2)\cap N(h_3):
z_0\notin\{(h_i)_0\},\
z_1\notin\{(h_i)_1\}\}.
\]

Note the strong **coordinate exclusion**: a neighbor may be a different physical corner yet share one coordinate with another hub, and would be ineligible. Treat the corners \(T(U)\) as edges of a **simple bipartite coordinate graph** with first-coordinate symbols on one side and second-coordinate symbols on the other. Let

\[
m_3(T)=\bigl|\{\{z_1,z_2,z_3\}\subseteq T:
|\{(z_i)_0\}|=|\{(z_i)_1\}|=3\}\bigr|
\]

be its number of three-edge matchings, i.e. physical free-corner triples transversal on both coordinate sides.

For each \(U\) and one such free triple \(Z\), the nine physical hub/free edges exist, forming a (not necessarily induced) \(K_{3,3}\). Its six Hamilton alternating C6s, with each physical corner coordinate-distinct on BOTH sides, are accepted ORIGINAL D6 under the previous exact bijection. A direct flag-ID derivation also works: the six projected first-coordinate edges are pairwise distinct physical source-point labels, and the second-coordinate edges distinct source-line labels; both named-column duals are the SAME connected C6. Each physical arc is backed by a genuine source incidence and the six ORIGINAL source factors on either side are all distinct.

Define \(B(f,g)\) as the number of distinct **unoriented unorooted** coordinate-transverse (not necessarily induced) physical K3,3 *bipartitions* \(\{U,Z\}\) satisfying the above conditions. Every such K3,3 is counted **exactly twice** in the sum \(\sum_U m_3(T(U))\), once when \(U\) is the chosen hub triple and once when \(Z\) is the chosen hub triple. Different alternating simple physical six-cycles have a **unique alternating bipartition** of their own six physical corners (up to swapping sides), even if their induced physical graph has additional chords. Therefore the six positive source-ID D6 cycles of each K3,3 are disjoint across different bipartitions. Thus:

\[
\boxed{
B(f,g)=\frac12\sum_U m_3(T(U)),\qquad
D_{6,K_{3,3}}(f,g)=6B(f,g)=3\sum_U m_3(T(U))\le D_6(f,g).
}
\]

Here \(D_{6,K_{3,3}}\) is the **exact K3,3-supported subset** of the accepted ORIGINAL D6 sixsets. It is **not** equal to all D6 in general: a genuine coordinate-rainbow C6 may lack physical chords needed to complete its unique alternating \(K_{3,3}\).

The source-to-D6 mapping is injective, not merely an upper bound: two distinct physical C6s can never share the same original sixset because the named-column adjacency order reconstructs the physical corners. Each selected edge is a unique genuine original source flag, and the resulting sixset is accepted by the historical GF(5) seven-family classifier. \(\square\)

## 3. All-h quantitative lower bound: high triple physical codegree forces positive GF5 D6

Write \(m_U=|T(U)|\). Let \(\Delta_U\) be the maximum **coordinate-star degree** among its \(m_U\) physical free corners (max count with the same first-coordinate or same second-coordinate). If \(m_U\ge3\), define \(D_U=2\Delta_U-1\). Selecting three pairwise coordinate-disjoint free corners greedily, after the first choice at most \(\Delta_U+\Delta_U-1=D_U\) possibilities are excluded, and after two at most \(2D_U\). Divide by \(3!=6\) orderings:

\[
\boxed{
6m_3(T(U))\ge
m_U\,[m_U-D_U]_+\,[m_U-2D_U]_+,
\quad [z]_+=\max(z,0).
}
\]

Summing and invoking the exact factor-two normalization above gives the universal **same-fixed-map** inequality

\[
\boxed{
D_6(f,g)\ \ge\
\frac12\sum_{U}
m_U\,[m_U-(2\Delta_U-1)]_+\,
[m_U-2(2\Delta_U-1)]_+.
}
\]

It is valid for **EVERY allowed correlated injection**, all dyadic \(h\), and true source incidence. It makes no statement for a triple common neighbor set concentrated on a single coordinate star (then \(m_3=0\)), so it does **not** assert “large ordinary physical codegree always forces D6.”

Because all three hubs are coordinate-injective and T excludes all six used hub-coordinate symbols, each remaining first-coordinate or second-coordinate symbol has at most \(a-3\) possible partners. Thus \(\Delta_U\le a-3\). The weaker, readily checked threshold

\[
m_U>4(a-3)
\]

automatically forces positive accepted D6, with a cubic polynomial lower bound for each such triple. More generally, a set of \(R\) coordinate-distinct hubs such that every chosen hub triple has \(m_U=\Omega(s^2)\) common free neighbors yields

\[
D_6\ \ge\ \Omega(R^3s^6),
\]

because the minimal physical alphabet is \(a=\Theta(s^{3/2})=o(s^2)\), and \(m_3(T(U))=\Omega(s^6)\) for large \(s\). This is **conditional on the explicit triple-common-neighborhood hypothesis**, not a new root theorem. For the coherent paired-subfield packets of #651, \(R=\Omega(s^{3/2})\), so this recovers a restricted \(\Omega(s^{21/2})\) D6 bound without reusing the packet-specific original base-source matching enumeration; existence of those packets is still imported from #651.

## 4. Independent integer source-ID finite oracles: sharp boundaries

The executable oracle does **not** enumerate all original source sixsets or invent edges. It enumerates candidate physical hub triples via inverted **physical vertex → neighbor triples** postings, evaluates the exact 3-matching count on filtered genuine common free neighbors, deduplicates each bipartition under U↔Z, produces exactly SIX alternating C6 per \(K_{3,3}\), recovers the six true original incidence IDs of each, checks six different genuine source POINT and LINE IDs, and checks each against the historical accepted GF(5) D6 classifier. A separate independent oracle enumerates **all** physical rainbow C6 and verifies the K3,3 sector is a subset.

Frozen original geometry cases:

| Genuine original complete typed map | Accepted original D6 | D6 with full K3,3 physical chords | Other genuine accepted D6 |
|---|---:|---:|---:|
| W(3,2), lex K6 | 15 | 6 | 9 |
| W(3,2), reverse-line K6 | 3 | 0 | 3 |
| W(3,4), adversarial complete K14 | 4,972 | **0** | **4,972** |

The last case is a critical NEGATIVE CONTROL: **triple-codegree K3,3 saturation is not necessary for genuine accepted D6**. Using this sector alone cannot prove the unrestricted original HYP-105 lower bound. Conversely, the genuine original \(W(3,4)\) 16-flag matching into a protected 4×4 hub/free physical grid (the previous PR #651 finite test mechanism) gives at least \(\binom43^2=16\) genuine coordinate-transverse \(K_{3,3}\) bipartitions and at least \(16\times6=96\) distinct accepted original D6 sixsets; full source typed injections are completed and independently validated. Both positive and negative controls are required before drawing an asymptotic inference.

The greedy three-matching lower is checked on arbitrary small physical coordinate grids and correlated-coordinate stars, and the entire source-generated K3,3 sector is invariant under independent bijective physical-coordinate renamings. Genuine original source injection checks and all-h theorem limitations are retained in output.

## 5. What this changes and the next P0 proof gate

This result is a genuinely **same-fixed-map positive transfer** from a precise, testable triple-codegree geometry into accepted ORIGINAL six-ID GF5 D6, and can replace the special packet-only K3,3 argument *once a quantitative triple-codegree lower is established*.

It does **not** show:
- a positive triple-codegree lower for every allowed global injection,
- that high five-ID noise or local physical defect *necessarily* causes well-spread triple common neighbors,
- that D6 alone is always \(\Omega(s^6)\), or
- that one of the **other six accepted original GF(5) classes** compensates whenever the K3,3 sector is absent.

The new complete original \(W(3,4)\) negative control (4,972 D6 but zero K3,3 support) makes the missing bridge concrete. The next best step is a **dichotomy involving both** (i) coordinate-transverse triple-neighbor matching mass and (ii) accepted non-K3,3 original sixflag classes/other physical rainbow C6s, with quantitative constants and true source-ID original incidence quantifiers. A proof that defects alone imply triple-star spread is not available.

Root status stays **OPEN_WITH_FORMAL_BLOCKER**. The all-\(h\) count identities are independent of existence of the infinite packet construction; specialized hosted GF2/GF4 finite oracles are evidence, not substitutes for an independent qualified mathematical referee.


## 6. AA4-PC3 extension — an EXACT ALL-h representation of ALL D6 through pair-codegree triangles

**New stronger theorem:** the fully saturated triple-*common*-neighbor sector in section 2 is only one term in a universal exact **triangle of three PAIR-common-neighbor posting lists**. This extension is essential: the true W(3,4) adversarial case has 4,972 accepted original D6 but ZERO coordinate-transverse K3,3.

For every unordered coordinate-injective physical hub triple \(U=\{h_0<h_1<h_2\}\), let

\[
Q_{ij}(U)=
\{z\in N(h_i)\cap N(h_j):
z_0\notin X(U),\ z_1\notin Y(U)\},
\]

where \(X(U)\), \(Y(U)\) are its three first and three second hub-coordinate symbols. Define the exact transversal witness population for this fixed hub triple

\[
T_3(U)=\sum_{\substack{z_{01}\in Q_{01}(U)\\
z_{12}\in Q_{12}(U)\\
z_{20}\in Q_{20}(U)}}
\mathbf1\!\left[
|\{(z_{01})_0,(z_{12})_0,(z_{20})_0\}|=3,\ 
|\{(z_{01})_1,(z_{12})_1,(z_{20})_1\}|=3
\right].
\]

**Theorem (all-h exact original-six-source-ID D6 pair-codegree triangle identity):**

\[
\boxed{2D_6(f,g)=\sum_{\substack{U\subseteq V(H),\,|U|=3\\
U\text{ coordinate-injective}}}T_3(U).}
\]

*Proof.* Each counted ordered triple of pairwise common neighbors gives the physical simple cycle

\[
h_0-z_{01}-h_1-z_{12}-h_2-z_{20}-h_0.
\]

The enforced coordinate-exclusion and coordinate-injectivity make all six first coordinates and all six second coordinates distinct. Each of its six physical arcs is backed by a UNIQUE TRUE original symplectic source incidence flag; by the preceding AA4-RC6 theorem the resulting six ORIGINAL source flag IDs, original point IDs and original line IDs are distinct and belong to the historic seven-family GF5-accepted **D6** class.

Conversely every such original D6 corresponds uniquely to a simple physical coordinate-rainbow C6. It has exactly two alternating three-corner vertex classes. Either may be chosen as its hub triple \(U\); after sorting that triple \(h_0<h_1<h_2\), each of the three free corners is **uniquely** assigned as the common neighbor between its two consecutive hubs. Thus each accepted ORIGINAL D6 sixset is counted **exactly twice**, and no other sixsets enter the sum. This proves the identity without spectral inequalities, probability, synthetic source graph edges or any f/g independence. \(\square\)

**Relation to AA4-TCN K3,3:** if the three pair witnesses also belong to \(N(h_0)\cap N(h_1)\cap N(h_2)\), they form a complete genuine physical K3,3 and contribute to the saturated term \(\sum_U6m_3(T(U))\) in the *oriented* count. Hence the exact positive decomposition is

\[
\boxed{
D_6(f,g)
=D_{6,K_{3,3}}(f,g)+D_{6,\text{missing chord}}(f,g),
}
\]

where the second nonnegative term counts original accepted D6 cycles whose six physical arcs exist but at least one of the three additional cross chords needed to form the alternating K3,3 does not. This is an exact **same-fixed-map positive split**, not a hypothetical claim that only K3,3 can yield D6.

**Independent genuine-original-source finite checks:** the new implementation builds pair-codegree lists by inverting original physical two-edge wedges, enumerates coordinate-transverse triple witnesses (not physical C6 via DFS), recovers each of six actual original incidence IDs, verifies six distinct point and line factor IDs and the historical GF(5) classifier, and checks each original sixset appears **exactly twice**. Separate previously implemented full-physical-C6 and K3,3 oracles independently certify the totals:

| Genuine complete typed label map | Pair-witness oriented triples | Original accepted D6 | K3,3-supported D6 | Non-K3,3 accepted D6 |
|---|---:|---:|---:|---:|
| W(3,2), lex K6 | 30 | 15 | 6 | 9 |
| W(3,2), reverse-line K6 | 6 | 3 | 0 | 3 |
| W(3,4), adversarial K14 | **9,944** | **4,972** | **0** | **4,972** |

The coherent full-source W(3,4) planted hub/free K4,4 witness supplies at least 96 K3,3-supported accepted source D6 motifs and is crosschecked by the pair-codegree representation. Importantly, the 4,972 source D6 in the adversarial W34 case come **entirely** from the *three PAIR-codegree lists*, without any physical triple-common-neighbor K3,3. This settles the gap in the positive certificate coverage of that example.

**Updated next mathematical P0:** seek a universal lower bound for the **coordinate-transverse triangle mass \( \sum_U T_3(U)\)**, or a **same-fixed-map lower-bound dichotomy across this mass and the other six accepted original GF5 classes**. Unlike the uncorrected physical six-cycle moment, \(T_3\) contains **only correctly accepted six-original-ID GF5 D6 motifs**; high physical defect and five-ID path collision noise are entirely absent from its summands. A lower bound on raw pair-codegrees without the cross-coordinate transversality indicator is NOT sufficient, so the remaining blocker is genuine and quantitative.

The exact identity provides no unconditional asymptotic lower bound itself. Root HYP-105 #230 stays **OPEN_WITH_FORMAL_BLOCKER**, independent scientific proof review required. The finite h=1,2 oracle is a falsifier, not an all-h computational proof.
