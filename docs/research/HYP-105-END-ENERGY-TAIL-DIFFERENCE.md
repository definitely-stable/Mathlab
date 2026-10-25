# HYP-105 / #230: exact tail-difference energy and a supersextic five-flag counterfamily

Date: 2026-10-26. Source checkout observed at `e012581a4b5db90daa17ed62513d6ad3a292b86d`. **Scoped deterministic infinite-family counterexample to a proposed moment-route premise. Root OPEN_WITH_FORMAL_BLOCKER.** The construction concerns the five-original-incidence-ID term \(C_{1,\mathrm{end}}\), not the seven accepted GF(5) six-incidence classes.

## 1. Exact formula and normalization

Use the true original \(W(3,s)\), complete separately injective correlated maps \(f,g\), and their simple physical corner graph \(H\). Its vertices are physical corners. For an ordered pair of corners \((u,v)\), call a corner \(x\) eligible when:

1. \(x\in\Gamma_H(u)\setminus\Gamma_H(v)\).
2. The first coordinates of \(x,u,v\) are pairwise distinct, and their second coordinates are pairwise distinct.
3. The endpoint pairs \(\{x_0,v_0\}\) and \(\{x_1,v_1\}\) are occupied source labels \(f(q),g(r)\), with original \(q\notin r\).

The first edge \(xu\) has a unique original source flag \(\alpha\). For eligible \(x\), let

\[
 k_{uv}(x)=\bigl|\{z\in\Gamma_H(u)\cap\Gamma_H(v):
 |\{x_0,u_0,z_0,v_0\}|=|\{x_1,u_1,z_1,v_1\}|=4\}\bigr|.
\]

Every such \(z\) gives the proper path \(x-u-z-v\), oriented so the shared end flag comes first. Its endpoint source pair is \((q,r)\). Conversely an SFC end posting determines \(x\) as the two shared coordinates of the flag/endpoint rectangles, \(u\) as the opposite flag corner and \(v\) as the opposite endpoint corner. This is a bijection between end postings \((\alpha,q,r)\) and eligible ordered triples \((u,v,x)\). Each reversal-orbit is represented once by this orientation. Two distinct paths at one posting have only their shared flag in common by SFC rigidity. Therefore no extra factor two or four occurs:

\[
 \boxed{C_{1,\mathrm{end}}=
 \sum_{u,v\text{ ordered}}\ \sum_{x\text{ eligible}}\binom{k_{uv}(x)}2.}
\]

The source nonincidence condition is essential. For occupied endpoint pairs it is equivalent to absence of the physical edge \(xv\), because that edge would be uniquely the source flag \((q,r)\). In particular, a pair of twin high-codegree hubs has no eligible tails in the common neighborhood.

Writing \(c_{uv}=|\Gamma_H(u)\cap\Gamma_H(v)|\) gives the valid generic envelope

\[
 C_{1,\mathrm{end}}\le
 \sum_{u,v\text{ ordered}}(d_H(u)-c_{uv})\binom{c_{uv}}2.
\]

It drops coordinate properness and occupied-endpoint restrictions, but keeps the necessary tail difference. The following construction shows that keeping this difference does not rescue a universal \(O(s^6)\) bound for \(C_{1,\mathrm{end}}\).

## 2. Quantified obstruction

For every \(t=2^k\), \(k\ge3\), set

\[
 s=t^2,\quad n=(t+1)(t^2+1),\quad d=t+1,\quad e=nd,
 \quad V=(s+1)(s^2+1),\quad R=\lfloor n/256\rfloor.
\]

There exist complete separately injective typed pair maps on genuine \(W(3,s)\), with minimal physical alphabet \(a\), for which

\[
 \boxed{C_{1,\mathrm{end}}\ge\frac{3R e^3}{1600}
 \ge\frac{3}{819200}s^{15/2}.}
\]

All finite choices below can be taken lexicographically first among admissible choices. No efficient construction-time claim is made. This is an infinite dyadic subsequence, sufficient to contradict an asserted uniform all-h \(C_{1,\mathrm{end}}=O(s^6)\).

## 3. Pack many paired genuine source subgeometries

Let \(P_0,L_0\) be the \(n+n\) source vertex sets of the canonical subfield \(W(3,t)\) inside \(W(3,t^2)\). The [paired-subfield note](HYP-105-END-POSTING-SUBFIELD-INVESTIGATION.md) proves this embedding preserves incidence, that \(G=\mathrm{Sp}_4(\mathbb F_s)\) is transitive on each ambient typed side, and that \(n^2/V<2\) for \(t\ge4\).

Suppose \(j<R\) packets have already been chosen, with used source point and line sets \(S_P,S_L\), each of size at most \(2jn\). Choose independent uniform \(A,B\in G\) temporarily for an averaging argument. Define bad base point indices

\[
 D_P=\{p\in P_0:Ap\in S_P\ \text{or}\ Bp\in S_P\ \text{or}\ Ap\in BP_0\},
\]

and define \(D_L\) on source lines analogously. A union bound and transitivity give

\[
 \mathbb E(|D_P|+|D_L|)
 \le\frac{2(|S_P|+|S_L|)n+2n^2}{V}
 \le(8j+2)\frac{n^2}{V}<16j+4\le n/8.
\]

The last inequality follows from \(j\le R-1\), \(16j+4<16R\le n/16\); here \(R\ge1\) because \(t\ge8\). Hence some ordered pair \((A_j,B_j)\) has total deletion at most \(n/8\). Choose the first such pair. Put \(P_j=P_0\setminus D_P\), \(L_j=L_0\setminus D_L\).

Both image supports avoid all previously used source vertices. Also \(A_jP_j\cap B_jP_j=\varnothing\): an equality \(A_jp=B_jp'\) would make \(p\in D_P\). The line supports are disjoint for the same reason. Thus every paired packet has four source supports disjoint in their respective typed universes, both internally and from all other packets.

Deleting a base point or line removes at most \(d\) subfield incidences. Define the retained induced base incidence set exactly by \(F_j=\{(p,l)\in P_j\times L_j:p\in l\}\); scalar extension introduces no extra incidence. Consequently it has size

\[
 |F_j|\ge e-(n/8)d=7e/8.
\]

Each retained flag has genuine images in both source copies. This completes the induction for all \(R\) packets. The random pair is only an existence proof for a fixed source choice; the final physical maps are deterministic and correlated.

## 4. Separate common neighbors from genuine nonincident tails

For one packet, weight each retained source line \(l\in L_j\) by its incidence degree in \(F_j\), at most \(d\). Split the lines into \(J_j,K_j\) with each incidence mass at least \(e/4\). Such a split exists: assign lines successively to the lighter side, keeping final weight discrepancy at most \(d\). Both masses are at least \((7e/8-d)/2\ge e/4\). Choose the first admissible partition.

Let \(F_K\) denote the incidence mass on \(K_j\), and \(d_K(p)\) the degree of a retained point into that line set. Then \(|K_j|\ge F_K/d\ge n/4\). For uniform permutations \(\sigma\) of \(K_j\), the number of preserved tail incidences has expectation

\[
 \mathbb E_\sigma\#\{(p,l)\in F_j:l\in K_j,\ (p,\sigma(l))\in F_j\}
 =\frac{\sum_{p\in P_j}d_K(p)^2}{|K_j|}
 \le\frac{d F_K}{|K_j|}
 \le\frac{4}{t^2+1}F_K<F_K/4.
\]

Choose the first permutation attaining at most this expectation, and extend it by the identity on \(J_j\). There are therefore at least \(3F_K/4\ge3e/16\) tail flags \((p,l)\) with \(l\in K_j\) such that \(p\notin\sigma(l)\). The source-pair incidence comparison is genuine: extending scalars from the subfield creates no extra incidence among the retained subfield vertices.

## 5. All prescribed labels fit and extend

Reserve two distinct center symbols \(b_j,c_j\) for each packet, using \(2R\) symbols total, and a shared pool of \(n\) free symbols disjoint from all centers. Use the same integer center symbols on both physical coordinate sides, whose roles remain typed. There is enough alphabet:

\[
 n+2R\le\frac{129}{128}n
 \le\frac{129\cdot87}{128\cdot64}t^3<\sqrt2\,t^3,
\]

using the preceding note's \(n+2\le(87/64)t^3\). Thus \(\binom{n+2R}{2}<t^6<V\), so minimality gives \(a\ge n+2R+1\). No extra outside-flag symbols are needed here.

Choose one global free-symbol injection \(p\mapsto z_p\) on all \(P_0\), and independently one global injection \(l\mapsto Z_l\) on all \(L_0\). Use their restrictions in every packet. This coherent choice is allowed by the shared pool of \(n\) free symbols; all negative-energy bounds above and below hold with it. Prescribe

\[
\begin{aligned}
 f(A_jp)&=\{c_j,z_p\},& f(B_jp)&=\{b_j,z_p\},\\
 g(A_jl)&=\{c_j,Z_l\},& g(B_j\sigma(l))&=\{b_j,Z_l\}.
\end{aligned}
\]

Source supports are globally disjoint by the induction. Physical pair images are globally distinct on each typed side: a prescribed pair has exactly one center and one free symbol; centers are unique across packet/sides of the pair, and the within-packet free assignments are injective. Reusing the free pool between different packets causes no collision. Complete all unassigned source factors using unused physical pairs in lexicographic order, possible because \(\binom a2\ge V\). Extra resulting physical edges cannot remove any paths used for this lower bound.

## 6. Count exact five-source-ID end collisions

Fix a packet's ordered hubs \(u=(c_j,c_j)\), \(v=(b_j,b_j)\). Every retained base flag \((p',l')\in F_j\) with \(l'\in J_j\) supplies a common neighbor \(z=(z_{p'},Z_{l'})\): its two original source flags are \((A_jp',A_jl')\) and \((B_jp',B_jl')\). There are at least \(e/4\) such common neighbors.

For any of the at least \(3e/16\) tail flags from section 4, put \(x=(z_p,Z_l)\). The edge \(xu\) is the source flag \(\alpha=(A_jp,A_jl)\). The endpoint source labels recovered from \(x,v\) are \(q=B_jp\), \(r=B_j\sigma(l)\), which are genuinely nonincident. Thus \(x\in\Gamma(u)\setminus\Gamma(v)\), exactly as required, rather than merely belonging to a high-degree hub neighborhood.

The line coordinate of this tail lies in \(K_j\), whereas common neighbors use \(J_j\), so their second coordinates never coincide. The only possible extra first-coordinate collision is \(p'=p\), which removes at most \(d\) common-neighbor flags. Every tail therefore has

\[
 k_{uv}(x)\ge e/4-d\ge e/5,
 \qquad \binom{k_{uv}(x)}2\ge e^2/100.
\]

Here \(n\ge20\) gives the first inequality, and \(k\ge2\) allows \(\binom k2\ge k^2/4\). The two different common-neighbor choices give two paths sharing exactly \(\alpha\): their remaining first-copy flags are distinct, their remaining second-copy flags are distinct, and the two copies have disjoint typed supports. Thus each counted pair has exactly five original incidence IDs, belongs to \(C_{1,\mathrm{end}}\), and is counted once at its unique shared posting. Different packets have different source \(\alpha\)'s, so their contributions are disjoint.

Summing gives \(C_{1,\mathrm{end}}\ge3Re^3/1600\). Since \(R\ge n/512\), \(n\ge t^3\), and \(e\ge t^4\), the claimed \((3/819200)t^{15}=(3/819200)s^{15/2}\) bound follows.

## 7. What this changes, and what remains open

The proposed uniform \(C_{1,\mathrm{end}}=O(s^6)\), and hence uniform \(C_0+C_1=O(s^6)\), are false in the stated unrestricted correlated-map model. The original source girth and physical degree bound remain valid; the counterfamily respects both. It uses large codegrees together with many *nonneighbor* tails, so the tail-difference restriction does not eliminate the obstruction.

From \(Q=2P+8(C_0+C_1)\) and \(U=\Theta(s^6)\), if one separately had \(P=O(s^6)\) on this family, then \(\chi^2=UQ/P^2-1=\Omega(s^{3/2})\). Accordingly the earlier pair of uniform sufficient premises \(P=O(s^6)\) and \(\chi^2=o(s^{1/2})\) cannot both hold. This is conditional on that \(P\) bound; no unconditional lower bound on \(\chi^2\) is asserted without controlling \(P\).

The construction amplifies **five-ID noise**. It does not upper-bound the seven accepted GF(5) six-ID motif count, produce \(S_{\mathrm{seven}}=o(s^6)\), or settle Branch A/B. A root proof should bypass this uncontrolled five-ID term, for example by controlling an appropriately defined six-distinct-ID quantity directly. The next restricted result shows that the coherently indexed family actually has a large accepted six-ID class; no general noise-to-risk dichotomy is proved.

## 8. Positive restricted theorem: coherent packets have many genuine D6 motifs

Retain the global coherent free-symbol indexing fixed in section 5. For \(t=2^k\ge16\), hence \(R\ge3\), the very same completed maps satisfy

\[
 \boxed{D_6\ge 2^{-35}s^{21/2}.}
\]

This is a lower bound for the historical accepted original six-incidence-ID \(D_6\) class, whose left and right named-column duals are the same connected C6. It holds for every completion of the protected partial labels and every tail-line permutation allowed above. It is a property of this coherent construction, not an arbitrary-map theorem.

For any three distinct packets, each \(F_j\) omits at most \(e/8\) of the same base subfield flag universe \(F_0\). Their common flag set therefore has size \(E\ge5e/8\). Coherent indexing makes each common flag \((p,l)\) the *same physical free corner* \((z_p,Z_l)\) in all three packets. Each of the three first-copy hubs \((c_j,c_j)\) is adjacent to that corner through the true original source flag \((A_jp,A_jl)\). These first-copy adjacencies use the identity g-label assignment even when \(l\in K_j\); the tail permutation affects only the second copy.

The common base incidence graph has maximum degree at most \(d\) on either side. It contains at least

\[
 \frac{E(E-2d)(E-4d)}6
\]

unordered three-edge matchings: choose an ordered first edge, remove edges incident with its two endpoints (at most \(2d\)), choose a second edge, and remove edges incident with both chosen edges (at most \(4d\)). Divide by the six orderings of each matching. The conservative deletions already include previously chosen edges. Distinct matching points and lines give three free corners with distinct first coordinates and distinct second coordinates.

The three hubs and three chosen free corners span a physical K3,3 and have six undirected Hamilton six-cycles. Each cycle uses three distinct center symbols and three distinct free symbols in each coordinate, so both coordinate projections are simple C6's with exactly the same named edge-adjacency order. Its six original source point IDs are all distinct: at one hub the matching supplies two distinct base points, while different hubs use disjoint \(A_jP_j\) supports. The source line IDs are likewise distinct. Thus its selected six original flags form a genuine factor matching, and the accepted seven-class classifier identifies their aligned left/right named-column dual as \(D_6\). No inference from the five-ID path-pair term is used.

There is no source-sixset overcount in this construction. For a selected first-copy source flag \((A_jp,A_jl)\), its labels distinguish the unique diagonal edge joining the hub \((c_j,c_j)\) to free corner \((z_p,Z_l)\). The other physical edge of that original flag lies between off-diagonal corners and is not among these counted cycles. Therefore an original sixset uniquely reconstructs its hub/free physical edge set, the three packet IDs, the three base flags, and its Hamilton cycle. Different hub triples, base matchings, or Hamilton edge sets give different original sixsets.

For \(n\ge32\), \(E-2d\ge e/2\) and \(E-4d\ge e/2\). Multiplying the matching lower bound by six Hamilton cycles gives at least \(5e^3/32\) distinct D6 sets per unordered hub triple. For \(R\ge3\), \(\binom R3\ge R^3/27\), hence

\[
 D_6\ge\frac{5}{864}R^3e^3
 \ge\frac{5}{864\cdot512^3}n^3e^3
 \ge2^{-35}t^{21}=2^{-35}s^{21/2}.
\]

The last safe constant uses \(5\cdot256\ge864\), \(n\ge t^3\), \(e\ge t^4\). Consequently \(S_{\mathrm{seven}}\ge D_6\) grows much faster than \(s^6\) on this particular coherent counterfamily to the moment premise. This explicitly prevents interpreting its large five-ID noise as a root Branch B counterexample. A general theorem saying that large five-ID noise always forces accepted six-ID compensation remains open.

**STOP condition for this route:** do not reopen a uniform \(C_{1,\mathrm{end}}=O(s^6)\) claim under the same unrestricted map assumptions. A revised question needs a changed statistic that removes the five-ID concentrations, or an explicit additional map restriction excluding this family. Such a restriction alone would not answer root #230, which permits all correlated injections.

## Executed finite evidence

An independent corner/tail loop on the persisted genuine W(3,4) paired-subfield witness gave `C1_end_exact_corner_tail_formula=20468`, agreeing with the SFC source-posting oracle. There were 203512 eligible ordered tail triples and 57892 with a nonzero proper join. The generic difference envelope was 40407. The loop built \(H\) directly from true source flags, recovered original endpoint IDs through \(f^{-1},g^{-1}\), checked nonincidence against the original flag set, and computed each proper common-neighbor intersection independently of SFC postings. No aggregate large-field family was enumerated.

A further actual W(3,4) check split that witness's retained eleven-line support by greedy incidence-weight balancing. It produced `J=[0,5,6,10,22,26]` with incidence mass 15 and `K=[1,2,9,21,25]` with mass 13. Exhausting permutations of those five K-lines found the lexicographically first minimum `K -> [9,21,1,25,2]`, preserving only one K-incidence. Reassigning only the second source copy's K-line images accordingly gave twelve genuinely nonincident tails, each with at least thirteen proper common-J neighbors. Summing their actual \(\binom{k}{2}\) values gave a selected-posting lower count of 1110; the full source SFC oracle on the resulting complete injections returned `C1_end=20255`. The check asserted every constructed endpoint's genuine original nonincidence. This exercises the tail-permutation mechanism on a real source, but the infinite packed-family statement is proved analytically above.

An exact-integer stdin check for `k=3..10`, with `t=1<<k`, `s=t*t`, `n=(t+1)*(t*t+1)`, `e=n*(t+1)`, `V=(s+1)*(s*s+1)`, and `R=n//256`, asserted:

```python
assert n*n < 2*V and R >= 1
assert 8*(16*(R-1)+4) <= n
assert (n+2*R)*(n+2*R-1) < 2*V
assert 7*e-8*(t+1) >= 4*e
assert 16*(t+1) < n
assert e >= 20*(t+1)
assert 512*R >= n
```

Actual output: `AGGREGATE_EXACT_INTEGER_PARAMETERS_PASS k=3..10`. These sanity checks are distinct from the quantified analytic proof above.

For the restricted positive theorem, a further stdin check verified the constant inequalities for `k=4..12`, producing `COHERENT_D6_CONSTANTS_PASS k=4..12`. An independent enumeration of all six-edge subsets of the nine edges of K3,3 found exactly six Hamilton edge sets and passed each, with six distinct original source factor IDs, to the repository's `classify_seven_prechecked` filter. All six were classified `D6`; actual output: `K33_SIX_ORIGINAL_MATCHING_D6_CLASSIFICATIONS_PASS cycles=6`. This finite template check validates the accepted-class transfer and multiplicity six, not a large-field exhaustive count.

The persisted [corner/tail oracle](../../research/hyp105_end_energy_tail_difference.py) uses the formula directly without calling the SFC orbit index. Its [tests](../../research/test_hyp105_end_energy_tail_difference.py) reproduce the two original W32 witnesses, the W34 adversarial certificate, and the paired-subfield W34 witness; they also check injection rejection, physical coordinate permutations and exact parameter inequalities through k=1024. The tail-line twist is persisted as a real W34 regression with source nonincidence and both independent aggregate oracles. A separate genuine W34 nine-source-flag matching, extended to full typed injections, realizes the K3,3 template and gives six different accepted D6 sixsets under the unchanged classifier. The [run record](../../research/hyp105_end_energy_tail_difference_run_20261026.json) pins commands, model-identifier availability, sources and actual outputs. The specialized GitHub workflow includes these tests.

Observed raw Windows source SHA-256 hashes:

| Source | SHA-256 |
|---|---|
| `research/hyp105_end_posting_subfield.py` | `86b1f522dba177d148d84512cf5953aab0a2f5671cc46c6d54a2e61f5977d237` |
| `research/hyp105_sixflag_pair_collision.py` | `ce8f9c633f1e23331a6b69b5720df0cd5b31d3148b550b93af5ff1def6c89ddc` |
| `docs/research/HYP-105-END-POSTING-SUBFIELD-INVESTIGATION.md` | `a3ae543652fb2de76b0d4f561a168a26e633d6c91643a79e2e3ae12ee5a663bd` |

Local follow-up verification: **51 related tests passed**, along with catalog, known/STOP registry, literature and whitespace validators. Independent read-only agent reviews checked the packed negative construction, coherent positive accepted-class transfer, original-sixset normalization and exact constants; no actionable defects were found. Passing finite checks is not the proof of the quantified claims above, and these reviews are not a qualified human referee.

The inherited runtime was described as GPT-6; its exact variant was unavailable. Mathlab MCP reporting, scientific acceptance-field changes, published snapshot updates, hosted full CI for this new local diff and a qualified external mathematical referee were not supplied by this investigation.
