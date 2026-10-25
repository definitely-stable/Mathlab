# HYP-105 / #230 AA4-SFC — exact six-original-flag path-collision decomposition

**Scientific status:** a new narrow **all-\(h\) deterministic combinatorial identity** and reproducible \(W(3,2)\)/\(W(3,4)\) finite source-ID certificates; root **OPEN_WITH_FORMAL_BLOCKER**. No unconditional \(\chi^2=O(1)\), \(P=\Theta(s^6)\), GF(5) seven-class lower bound, or ASET-exponent promotion.

## 1. What is counted, precisely

Let \(s=2^h\), \(h\ge1\); true original symplectic \(W(3,s)\), \(V=(s+1)(s^2+1)\), \(a=\min\{m:\binom m2\ge V\}\). Fix arbitrary (possibly correlated) complete injective typed maps \(f:P(W)\to\binom{[a]}2\), \(g:L(W)\to\binom{[a]}2\). Construct the physical undirected corner graph \(H\) from **genuine original incidence flags** \((p,l)\): the original flag contributes two opposite-corner physical edges of rectangle \(f(p)\times g(l)\). Every physical edge has one and only one original source flag ID by typed global injection (AA4-VT, AA4-DEG).

Define the typed source nonincident endpoint universe \(\mathcal E=\{(q,r):q\notin r\}\), \(U=|\mathcal E|=Vs^2(s+1)\).

A **proper directed physical 3-walk** \(w=(v_0,v_1,v_2,v_3)\) has all four first coordinates pairwise distinct, and all four second coordinates pairwise distinct. A walk is **retained** here only if the unordered first-coordinate endpoints belong to one occupied original POINT image \(f(q)\), the unordered second-coordinate endpoints belong to an occupied original LINE image \(g(r)\), **and** \(q\notin r\) in the original GQ. *Internal projection blocking is not applied* (otherwise the prior bad-endpoint mass would vanish by definition). The number of retained proper directed walks projecting to \((q,r)\) is \(N_3(q,r)\). Put

\[
P=\sum_{\mathcal E}N_3(q,r),\qquad
Q=\sum_{\mathcal E}N_3(q,r)^2.
\]

Write \(\mathfrak t(w)\) for the **unordered set of exactly three genuine original incidence IDs** carried by its three physical edges. The IDs are original typed \((p_i,l_i)\), *not* the physical corner edges or just coordinate labels.

## 2. All-h reverse-orbit and forbidden-two-shared-flags lemma

**Theorem 1 (reversal-orbit rigidity, every legal \(s,f,g\)).**

1. The original point IDs \(p_1,p_2,p_3\) of the three physical edges of a proper walk are all distinct; separately its original line IDs \(l_1,l_2,l_3\) are all distinct. Consequently \(|\mathfrak t(w)|=3\).
2. For fixed original typed nonincident endpoints \((q,r)\), any unordered triple \(\mathfrak t\) of original source flags represented by a retained proper physical walk is represented by **exactly two** directed proper physical walks: \(w\) and \(w^{\mathrm{rev}}\).
3. Two different such reversal-orbits with the same original typed nonincident endpoints have **at most one** common original incidence ID. In particular, intersection size \(2\) never occurs.

**Proof.** Each physical edge changes both coordinates. Along a proper physical walk, its first-coordinate edges form a *simple 3-edge path* \(x_0-x_1-x_2-x_3\) in \(K_a\), while its second-coordinate edges form a simple 3-edge path \(y_0-y_1-y_2-y_3\). Distinct simple edges have distinct typed source factor IDs because \(f,g\) are injective. The physical flags at position \(i\) are uniquely the pair of source IDs carried by the coordinate edges at that position. Thus (1).

**Elementary 3-path rigidity.** Two simple 3-edge paths with the **same unordered endpoint pair** that share two undirected edges share all three. Indeed, relative to a path with edges \(e_1=\{x_0,x_1\}\), \(e_2=\{x_1,x_2\}\), \(e_3=\{x_2,x_3\}\): if they share \(e_1,e_2\), the endpoint condition forces \(e_3\); if they share \(e_2,e_3\), it forces \(e_1\); if they share \(e_1,e_3\), each must be an end edge and their remaining free endpoints force \(e_2\). No repeated vertices are allowed. This argument is invariant under path reversal.

If two retained walks project to the same \((q,r)\), both first-coordinate 3-paths have endpoint edge \(f(q)\), and both second-coordinate 3-paths have endpoint edge \(g(r)\). Sharing two **original flags** means sharing two coordinate edges in **both** coordinate paths; 3-path rigidity forces all three point-source IDs and all three line-source IDs. The unique physical edge at each shared source-flag pair then forces the third flag. Further, each coordinate path with a fixed unordered set of three consecutive edges is traversable only in two orientations. To pair source flags at all three positions, the orientation choices on the first- and second-coordinate paths must agree; hence precisely the walk and its full reversal exist. This proves (2)–(3). \(\square\)

The reverse involution has no fixed proper walks. In particular,

\[
\boxed{N_3(q,r)\equiv0\pmod2\quad\text{for every }(q,r)\in\mathcal E.}
\]

## 3. Exact second-moment split by number of original source incidence IDs

For each retained source endpoint pair \((q,r)\), let \(\mathcal O(q,r)\) be the set of reversal-orbits of retained paths. Thus \(|\mathcal O(q,r)|=N_3(q,r)/2\).

For \(j\in\{0,1\}\), define \(C_j\) to be the total number of **unordered pairs of different** reversal-orbits \(O,O'\) in the **same** \(\mathcal O(q,r)\), across all \((q,r)\in\mathcal E\), satisfying \(|\mathfrak t(O)\cap\mathfrak t(O')|=j\).

Class \(C_0\) consists of **two distinct paths using six distinct original incidence IDs**; \(C_1\) consists of two paths using five distinct IDs. Two-shared-ID pairs of different orbits are forbidden by Theorem 1.

In \(Q=\sum N_3^2\), every reversal-orbit pairs its two directed walks with themselves in exactly four ordered ways. Two different orbits yield eight ordered directed-walk pairs, accounting for two orbit orders and the two orientations of each. Therefore:

\[
\boxed{
Q=2P+8C_0+8C_1.
}
\]

This is exact for **every dyadic \(h\ge1\) and all correlated admissible maps**. More finely, let \(Q_j\) count ordered pairs \((w,w')\) in the same source endpoint group with \(|\mathfrak t(w)\cap\mathfrak t(w')|=j\). Then

\[
\boxed{(Q_0,Q_1,Q_2,Q_3)=(8C_0,8C_1,0,2P).}
\]

Important: **\(Q_0\) is a six-distinct-original-incidence-ID *candidate pair-of-physical-paths* count.** Merely having six distinct source IDs does not imply one of the seven historical accepted GF(5) six-incidence motifs. Do not promote \(C_0\) into the root theorem.

### An independent **inverted source-flag** certificate for the five-flag collisions

For any \((q,r)\in\mathcal E\), and any genuine original incidence ID \(\alpha=(p,l)\), let

\[
m_{\alpha}(q,r)
=\bigl|\{O\in\mathcal O(q,r):\alpha\in\mathfrak t(O)\}\bigr|.
\]

Because any pair of different orbits shares **at most one** source ID (Theorem 1), an inverted incidence index counts \(C_1\) *exactly once* per pair:

\[
\boxed{
C_1=\sum_{(q,r)\in\mathcal E}
\sum_{\alpha\in\mathrm{Flags}(W)}
\binom{m_{\alpha}(q,r)}2.
}
\]

There are exactly \(\sum_\alpha m_\alpha(q,r)=3|\mathcal O(q,r)|\) flag appearances at every endpoint. Therefore

\[
\boxed{
C_0=\sum_{(q,r)\in\mathcal E}
\binom{|\mathcal O(q,r)|}{2}-C_1.
}
\]

This is a second **independent indexing method** for the same Q0/Q1 decomposition: rather than compare every pair of orbit triplets, reconstruct an inverted posting list from genuine original flags and count its unordered collisions. It is valuable because \(C_1\) can now be attacked through source flag local occupancies \(m_\alpha(q,r)\) instead of the unstructured second moment \(Q\).

### Consequences for the center-variance barrier

For \(P>0\), the exact AA4-VT divergence becomes

\[
\boxed{\chi^2(N_3)=\frac{U(2P+8C_0+8C_1)}{P^2}-1.}
\]

In particular, under **separately proved** uniform \(P=\Theta(U)=\Theta(s^6)\), bounded \(\chi^2(N_3)\) is equivalent to the new concrete *collision-orbit* requirement \(C_0+C_1=O(U)=O(s^6)\). This exhibits the exact combinatorial objects an all-\(h\) variance proof must control. Without a matching lower bound for \(P\), the equivalence cannot be invoked.

## 4. Independent finite source-ID certificates

Both original GQ instances are constructed from the genuine symplectic GF(2) and GF(4) projective geometry. The oracle computes each physical directed walk from the source incidence flags, recovers **each of its three original incidence IDs** by inverse typed coordinate pairs, and groups by actual original nonincident \((q,r)\). Pair intersections are counted after **reverse-orbit compression**; a separate existing oracle independently recomputes \(P,Q\) by endpoint multiplicities, without using the source-ID collision classes.

| Legal instance | \(P\) | \(Q\) | \(Q_0=8C_0\) | \(Q_1=8C_1\) | \(Q_2\) | \(Q_3=2P\) |
|---|---:|---:|---:|---:|---:|---:|
| \(W(3,2)\), full K6 seed 41 | 986 | 8,612 | 4,608 | 2,032 | **0** | 1,972 |
| \(W(3,2)\), full K6 seed 91 | 860 | 6,312 | 3,224 | 1,368 | **0** | 1,720 |
| \(W(3,4)\), adversarial full K14 | 58,730 | 676,700 | 486,880 | 72,360 | **0** | 117,460 |

Here \(C_0,C_1\) are respectively \((576,254)\), \((403,171)\), \((60,860,9,045)\). Each finite result satisfies \(Q=2P+8(C_0+C_1)\). The zero ID-overlap term is **not negligible** at these widths, but none of these finite samples establishes its asymptotic growth.

All test inputs remain genuine complete injective typed \(f,g\), with both source factor dimensions retained. The oracle rejects malformed/noninjective mappings and tests independent physical-alphabet permutations (not random source-ID substitutions).

## 5. Scientific audit and next gate

This is a source-ID-respecting **bridge** from physical 3-walk variance toward the six-original-incidence hypothesis, not a proof of its seven GF(5) acceptance classes.

The next P0 mathematical question is to bound \(C_0\) and \(C_1\) **separately**, ideally with source geometric constraints and the endpoints fixed to \((q,r)\), rather than with the simple corner graph's global degree norm. A uniform \(C_1=O(s^6)\) or \(C_0=O(s^6)\) would be genuinely useful but is **not proved** by the identities. It may be necessary to build explicit correlated-label adversaries before proposing any general bound. Retain the full original six-flag GF(5) model and independent qualified review gate; root Branch A/B/C remains open.
