# HYP-105 / #230 — AA4-K32LIFT: exact conditional line-label expectation for saturated two-flag D6 extensions

**Status: rigorous all-\(h\) conditional expectation identity, with an exact source-incidence W(3,4) positive/zero comparison and an independently exhaustive toy injection oracle.** This is an **annealed/existential** theorem, not a fixed-map pointwise universal \(\Omega(s^6)\) result. The root HYP-105 remains **OPEN_WITH_FORMAL_BLOCKER**. Parent #665 constructs a LEGAL fixed completion with exactly zero local fresh extension mass, so no averaging in this document is permitted to conceal that adversarial choice.

## 1. Exact frontier after #663–665

On a TRUE original symplectic generalized quadrangle \(W(3,s)\), \(s=2^h\), with \(V=(s+1)(s^2+1)\) source points and \(V\) source lines, define \(a=\min\{q:\binom q2\ge V\}\). Both complete source point and line pair-label maps \(f,g\) are separately globally injective. They may be fully correlated.

For one fixed source-ID coherent selected graph \(G\) (source-pencil conflict-free, both original physical diagonals retained and both typed physical-coordinate two-cuts applied), let \(\mathcal K_{\rm sat}(G)\) be its **DISTINCT** saturated physical coordinate-transverse \(K_{3,2}\) original-six-ID parents. Parent #663 proves the exact two-original-flag extension identity for EACH parent \(F\):
\[
|\mathcal E_2(F)|=2\sum_{i<j}|W_{ij}^{H(f,g)}(F)|,
\]
where \(W_{ij}^{H}\) contains *full-H actual* physical common neighbors of two of the three hubs using new symbols on BOTH physical coordinate axes. Parent #664 proves the families \(\mathcal E_2(F)\) are pairwise disjoint for parents saturated in **the same selected G**, hence:
\[
D_6(f,g)\ge 2\sum_{F\in\mathcal K_{\rm sat}(G)}\sum_{i<j}
|W_{ij}^{H(f,g)}(F)|.
\tag{1}
\]

Crucially parent [Draft #665](https://github.com/definitely-stable/Mathlab/pull/665) constructs two complete genuine source \(W(3,4)\) line-label maps sharing the **same entire f** and the same selected source-line labels, which produce identical saturated parent \(G\), but one has **four fresh neighbors / eight accepted original D6 two-flag extensions** and the other has **ZERO**. Therefore (1) cannot be turned into a deterministic all-map positive bound from selected G and f alone. The present slice asks what is nevertheless *exactly true* under an explicitly **randomized completion of the as-yet-unassigned line labels**, and what deterministic **existence** this expectation entails.

## 2. Partially fixed actual source labels and conditional model

Fix a **complete** and globally injective point-pair map \(f:\mathrm{Pts}\to\binom{[a]}2\). Independently choose a source-line subset \(J\subseteq\mathrm{Lines}\), with a **partially fixed** injective \(g_J:J\to\binom{[a]}2\). \(J\) must contain all lines used by the selected original source ID set; thus every edge of its coherent \(G\), including **both** physical diagonals per original ID, is **frozen** and the selected saturation family stays the same under the random completion. The source GQ itself, its \(V(s+1)\) genuine incidence flags and every original source-ID remain fixed and NOT randomized.

Let \(U=\mathrm{Lines}\setminus J\), \(m=|U|=V-|J|\), and let \(\mathcal Q=\binom{[a]}2\setminus g_J(J)\) be the set of still unused *line-label coordinate pairs*, \(Q=|\mathcal Q|=\binom a2-|J|\ge m\). Choose the completion \(g:U\hookrightarrow\mathcal Q\) **uniformly among all injections**. Not all \(Q\) available pair labels need be occupied if \(\binom a2>V\); this distinction matters, for example at \(W(3,4)\), where \(a=14\), \(V=85\), \(Q=79\), \(m=73\).

For each physical saturated parent \(F\) from \(G\), a pair \(i<j\) of its hubs \(h_i=(x_i,y_i)\), \(h_j=(x_j,y_j)\), and a physically **fresh** corner \(w=(x,y)\), define:
\[
P_i=f^{-1}(\{x_i,x\}),\qquad
P_j=f^{-1}(\{x_j,x\}),\qquad
\tau_i=\{y_i,y\},\quad\tau_j=\{y_j,y\}.
\]
If either \(P_i\) or \(P_j\) is undefined, this candidate contributes zero. By different hub physical first coordinates and global point-label injectivity, the two source points \(P_i,P_j\) are different; likewise \(\tau_i\ne\tau_j\). The candidate is a true full-H fresh common neighbor **iff** the actual source lines \(g^{-1}(\tau_i)\), \(g^{-1}(\tau_j)\) are both defined and each of the two genuine original source incidences \((P_i,g^{-1}\tau_i),(P_j,g^{-1}\tau_j)\) exists. This is a true original incidence **rectangle**, not a synthetic edge or random host.

For a source point \(p\), write
\[
d_U(p)=|\{\ell\in U:p\sim\ell\}|,
\]
and for distinct source points \(p\ne q\), write
\[
c_U(p,q)=|\{\ell\in U:p\sim\ell,\ q\sim\ell\}|.
\]
In genuine \(W(3,s)\), two distinct points lie on at most one common line, so \(c_U(p,q)\in\{0,1\}\). In all cases \(d_U(p)\le s+1\). No independence of GQ incidence events is assumed.

## 3. New all-h exact conditional probability theorem

Let \(\tau_i\ne\tau_j\) be the two required line-label slots of an admissible fresh physical corner, and let \(p=P_i,q=P_j\).

**Theorem AA4-K32LIFT.** Conditional on the complete fixed point map \(f\) and partial fixed source-line map \(g_J\), the probability that the corner \(w\) is a **real full-H physical common neighbor** of the two hubs, under a uniformly random injection completion \(g|_U:U\hookrightarrow\mathcal Q\), equals:

\[
\boxed{
\mathbb P(w\in W_{ij}^H(F))=
\begin{cases}
\mathbf1_{p\sim g_J^{-1}(\tau_i)}
\mathbf1_{q\sim g_J^{-1}(\tau_j)},
&\tau_i,\tau_j\in g_J(J),\\[3pt]
\mathbf1_{p\sim g_J^{-1}(\tau_i)}\,d_U(q)/Q,
&\tau_i\in g_J(J),\ \tau_j\notin g_J(J),\\[3pt]
d_U(p)/Q\,\mathbf1_{q\sim g_J^{-1}(\tau_j)},
&\tau_i\notin g_J(J),\ \tau_j\in g_J(J),\\[3pt]
\displaystyle\frac{d_U(p)d_U(q)-c_U(p,q)}{Q(Q-1)},
&\tau_i,\tau_j\notin g_J(J).
\end{cases}
}
\tag{2}
\]

If \(Q<2\) the last case cannot contribute. If a point-pair label inverse is undefined the probability is zero.

*Proof.* In a uniform injection of \(m\) distinct source lines into \(Q\) unoccupied typed coordinate pair labels, a prescribed unused label slot \(\tau\in\mathcal Q\) is occupied by any particular source line \(\ell\in U\) with probability **exactly \(1/Q\)**. Two *distinct* prescribed unused slots are occupied by two **specified distinct** original lines \(\ell\ne\ell'\) with probability **exactly \(1/(Q(Q-1))\)**. Two prescribed slots can never carry the same original line. Therefore:
- if both are fixed, the genuine source incidence conditions are deterministic;
- if exactly one is fixed, sum the uniform \(1/Q\) source-line occupation over the \(d_U\) genuinely incident unassigned lines of the other point;
- if both are unfixed, enumerate \emph{ordered distinct} source line choices. The number of such choices incident to the respective source points is precisely \(d_U(p)d_U(q)-c_U(p,q)\), subtracting the choices in which the same physical source line was counted twice. Divide by \(Q(Q-1)\). Nothing is approximated. \(\square\)

## 4. New all-h exact expected fresh-neighbor mass and existence corollary

Summing the rational probabilities in (2) over **every** parent in the same selected \(G\), all three hub pairs, and all coordinates \(w\) fresh on **both** axes gives the exact conditional expectation:

\[
\boxed{
\mathbb E_{g|U}\,M(G,H(f,g))
=
\sum_{F\in\mathcal K_{\rm sat}(G)}\sum_{i<j}
\sum_{\substack{w=(x,y)\\
x\notin X(F),\ y\notin Y(F)}}
\mathbb P\!\left(w\in W_{ij}^{H(f,g)}(F)\right).
}
\tag{3}
\]

Here \(M=\sum_F\sum_{i<j}|W_{ij}^H(F)|\) is the **same-map saturated extension mass** in #664. All terms are nonnegative and rational; a computational oracle can determine the exact value without enumerating any of the \(Q!/(Q-m)!\) possible legal source-line completions.

Because (1) holds for **every** completion individually and the set of saturated parents does not move when unselected line labels are permuted, linearity of expectation gives:

\[
\boxed{
\mathbb E_{g|U} D_6(f,g)\ \ge\ 2\,\mathbb E_{g|U} M(G,H(f,g)).
}
\tag{4}
\]

**Deterministic existential consequence** (finite averaging principle):

\[
\boxed{
\exists\ \text{an allowed globally injected completion }g\supseteq g_J:
\quad D_6(f,g)\ \ge\ 
\left\lceil 2\mathbb E_{g|U}M(G,H(f,g))\right\rceil.
}
\tag{5}
\]

These statements do **not** hold pointwise for every completion; (4) and (5) do **not** imply root HYP-105. In particular, (5) cannot be used with the original hypothesis' universal \(\forall g\) quantifier. This is an explicitly quantified annealed benchmark and exact diagnostic of how the unselected line labels can suppress local positive compensation.

## 5. Reproducible independent checks and scientific limits

The new source-independent combinatorial algebraic oracle handles any finite genuine incidence list with a complete injected point-pair map, partial injected line-pair labels and fixed physical saturated parent coordinates. Its separate true-source wrapper strictly validates all \(W(3,2^h)\) source flags, separately globally injected complete f and reference g, the selected original incidence IDs, source-pencil conflict freeness, both 2-cuts and **both physical diagonals**, then freezes exactly the actual source-line labels occurring among selected genuine flags.

It checks:
- a **fully exhausted 182-injection** independent finite model with two unfixed source lines and fourteen free line pair labels: the sum of exact physical incidence rectangle indicators over all uniform completions agrees with \(2/(14\cdot13)\);
- explicit both-fixed, one-fixed and both-free formula branches;
- the original-source \(W(3,4)\) positive and ZERO complete line-label maps from PR #665, sharing exactly all 85 point labels and 12 selected line-label assignments and the same two selected saturated blocks: both have the **SAME exact rational conditional expectation** (because conditioning forgets all differences in the unselected line labels), despite their actual full-H fresh-neighbor counts differing **four versus zero** and corresponding historical accepted original two-flag D6-extension counts being **eight versus zero**;
- all actual 425 source GQ incidence flags in both maps, full 85 point/line injected labels, the 79 unoccupied line-label pair slots and 73 unfrozen original source lines, and both paired physical diagonals;
- fail-closed labels, missing genuine source factors and duplicate selected original incidence IDs.

The independent actual-source full-H rectangle oracle of #665 and historical GF5 original sixset classifier of #663/#664 are used as separate finite reference checks. This conditional result is **not** a replacement for their acceptance proofs, nor a guarantee that one given adversarial completion has a positive fresh-neighbor mass.

**Relation to prior art:** uniform injections without replacement, conditional expectation, and the averaging principle are classical. Existing PR #466 addresses a different (global quotient lift) random-regular-fiber model, and does not supply this **exact fixed-source, partially frozen line-label fresh-two-flag** identity. The research contribution here is the correct coupling of an exact finite injection computation to TRUE GQ incidence-rectangle geometry and the already proved unique saturated-parent positive GF5-D6 transfer.

## 6. Next high-priority proof gate

PR #665's ZERO completion shows \(\mathbb E M>0\) cannot become an all-map lower bound on \(M\). To advance the original seven-class universal conjecture, the next task must analyze **all accepted original GF5 motif classes or truly global remaining geometric constraints in the fixed completion**, rather than simply repeating the annealed estimate. A valuable immediate test is a **complete same-map original seven-family census** (or a certified class-specific lower statistic) on the two true W34 completions with the same f and selected G, to learn where accepted mass moves when the local two-flag sector vanishes. A W34 finite comparison is not an asymptotic proof; each accepted candidate must be enumerated or bounded with genuine incidence-ID provenance.

Root \`OPEN_WITH_FORMAL_BLOCKER\`; keep scientific Draft, hosted specialized/INDEX/Research exact HEAD CI and qualified external proof referee. No merge into main.
