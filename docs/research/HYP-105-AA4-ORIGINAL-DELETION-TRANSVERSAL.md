# HYP-105 / #230 — AA4-DELTRANS: exact adversarial ORIGINAL-ID deletion certificates and binomial GF(5) palette distance

**Scientific status:** finite full original W(3,2) adversarial-deletion problem with a complete exhaustive certificate; plus rigorous **all-finite-N**, independently signed original-flag-packing stochastic-domination theorem. Its **all-h** inference is expressly *conditional* on the previously documented but scientifically unaccepted [Draft #674](https://github.com/definitely-stable/Mathlab/pull/674) true-original arbitrary-deletion result, which itself uses [Draft #672](https://github.com/definitely-stable/Mathlab/pull/672) and the real Simonovits/Jiang–Yepremyan balanced C6 supersaturation input. This slice does NOT independently prove that all-h geometric statement, resolve root Branch A/B/C, or establish any ASET exponent. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains **OPEN_WITH_FORMAL_BLOCKER**. It is stacked on immutable AA4-PALDIST [Draft #726](https://github.com/definitely-stable/Mathlab/pull/726) exact parent \`5230510b48884f4fbafa3b35ab0fd82720897a0d\`, whose source six-ID disjoint 10-sign union probability is a verified prerequisite.

## 1. Research step: attack the *universal deletion* interface, not only random-coefficient expectation

The previous AA4-PALDIST source construction used a deterministic greedily **maximal** three-element accepted sixset packing on each of the two complete original W(3,2) mappings. Such a packing is not necessarily **maximum**; neither its cardinality nor the original-source hitting set gives the exact worst-case number of ORIGINAL incidence ID deletions needed to kill every D6/BBo motif. The geometric [#674] theorem claims resilience of accepted ORIGINAL D6/BBo sixsets against ANY adversarial original flag deletion Z of size O(s⁴), for all sufficiently large dyadic s and ALL fixed complete arbitrarily correlated globally injected factor-pair maps. A finite check on selected Z cannot justify that universal quantifier, but an EXACT complete finite source hypergraph and a fully enumerated adversarial-deletion frontier can falsify hidden conflation of source-ID deletion, projected coordinate deletion, maximal-versus-maximum packing, or loss of projection anchor provenance.

Define the finite original accepted six-uniform source hypergraph

\[
  \mathcal H_{f,g}
    =\{Q\subseteq I(W(3,s)):\ |Q|=6,\;
      Q\text{ is a true accepted }D_6\text{ or } B/B\text{-overlap original sixset}\}.
\]

Each Q is literally a set of six distinct original (point,line) incidence IDs, **same six IDs** in both globally fixed left and right physical embeddings. Define the minimum adversarial original-incidence deletion number

\[
 \tau(\mathcal H)=\min\{|Z|:\forall Q\in\mathcal H,\;Q\cap Z\ne\varnothing\}
\]

and the **maximum** size of a pairwise-ORIGINAL-ID-disjoint family

\[
 \nu(\mathcal H)=\max\bigl\{|\mathcal M|:\mathcal M\subseteq\mathcal H,\;
     \forall Q\ne Q'\in\mathcal M,\ Q\cap Q'=\varnothing\bigr\}.
\]

These are DIFFERENT optimization problems, and in general \( \nu\le\tau\le6\nu\); a greedily maximal packing need not realize ν. In the independently tested W32 original host there are 45 real flags, and the two historical complete original sixset populations are:

| Fixed full 15-by-15 globally injected original W(3,2) pair maps | D6 | B/B-overlap | All accepted original sixset hyperedges |
|---|---:|---:|---:|
| lex | 15 | 8 | 23 |
| reverse-line | 3 | 7 | 10 |

The completely independent 12-physical-coordinate original classification in \`research/hyp105_original_deletion_transversal_referee.py\` reconstructs every one of the 62,370 genuine original LEFT-qualified six-incidence subsets from the original W32 GQ source and for each candidate separately verifies both 6-coordinate degree-two projections, six named column-to-coordinate dual graphs, original point/line factor degree partitions, exact aligned C6/D6 dual pairing or the one-ID-overlap of the repeated two ORIGINAL factor pairs. This independent classifier must agree with the accepted historical seven-family classifier for EVERY left candidate, not just a sample. The complete resulting ten or twenty-three ORIGINAL six-ID hyperedges are retained explicitly in the hosted certificate.

### Exact finite proof method

For each real six-uniform original hypergraph the standalone referee:
1. **Exact minimum deletion tau**: depth-budgeted, complete source-ID branching on any uncovered original hyperedge, with conservative disjoint-edge packing prune; a size-τ ORIGINAL Z witness must hit ALL original sixsets, and exhaustive impossibility at τ−1 proves optimality. This is finite proof, not an ILP heuristic or local search with a time budget.
2. **Exact maximum original-ID packing ν**: complete independent include/exclude recurrence on the actual original sixset edge bitmasks, with caching, proving a maximum (not merely a maximal greedy) and saving the real disjoint ORIGINAL incidence-ID sets.
3. **All adversarial ORIGINAL deletion sets |Z|=0,1,2,3,4**: enumerate C(45,k) actual deletion sets for each k, measure the **minimum** number of surviving genuine accepted source motifs over every adversarial Z, the number of worst sets and one witness. Independently verify the exact double count
\[
 \sum_{|Z|=k}\#\{Q\in\mathcal H:Q\cap Z=\varnothing\}
   =|\mathcal H|\binom{45-6}{k}
   =|\mathcal H|\binom{39}{k}.
\]
The separate unit-test oracle independently recomputes every k=0,1,2,3 survivor count by direct Python set-intersection without the bitmask/cover solver. Source-ID hyperedges have size six and are explicitly original, not coordinate label or physical cycle edge aliases.

This is a stronger finite adversarial falsifier for the #674 deletion-interface claim than a few chosen source-ID Z, but it does **NOT** establish any uniform \(\Omega(s^4)\) source packing for ALL large s, and W32 does not satisfy the extremely large claimed analytic s₀ conditions.

## 2. NEW exact binomial repair-distance theorem for any verified original sixset packing

In the frozen parent [#726](https://github.com/definitely-stable/Mathlab/pull/726), a new all-N physical original-source lemma proves the TEN different balanced 3v3 signs on ONE accepted original D6 or B/B-overlap sixset are *mutually exclusive*, not independent: if two held, their difference would be an impossible internal source singleton (1+1) or 2+2 physical-GF5 equality. Consequently, for independently uniform 51-pattern nonzero checksum4 original GF5 source-column coefficients, the union of these ten signs has exact probability

\[
 p_j=\begin{cases}
 54162/51^6, & Q_j\in D_6,\\
 53526/51^6\text{ or }53838/51^6, & Q_j\in B/B\text{-overlap}.
 \end{cases}
 \quad p_j\ge q_{10}:=\frac{53526}{51^6}.
\]

For t pairwise SIX-ORIGINAL-ID-disjoint accepted sixsets Q_j, the ten-sign union indicator X_j depends only on the six independently chosen coefficient patterns for that Q_j; hence the X_j are **independent across the t motifs**, despite arbitrary correlations between the fixed physical pair labels f,g and any physical coordinate overlap across motifs. They are not necessarily identically distributed.

Let \(Y=\sum_{j=1}^t X_j\), and let \(d(\mathbf c,\mathcal A_{0:3})\) be the minimum number of original source-column coefficient palette changes to reach ANY full 0-to-3 GF(5) ASET on the SAME frozen global f,g (possibly +∞ if no such assignment exists). Any violated initial signed Q_j must have at least one of its SIX ORIGINAL incidence flags changed before it can disappear; no edit outside that original source set can affect its signed physical GF5 equality. Since Q_j are original-ID-disjoint, these repairs require DISTINCT changed original source IDs. Therefore **pointwise \(d\ge Y\)** for ANY simultaneous or nonmonotone recoloring.

Now, for each independent X_j with probability p_j≥q10, take one independent Uniform[0,1] U_j and realize X_j=1_{U_j<p_j}, and Z_j=1_{U_j<q10}. This yields \(X_j\ge Z_j\) for every j in the coupling, and the Z_j are i.i.d. Bernoulli(q10). Thus **Y stochastically dominates Binomial(t,q10)**.

**NEW exact finite tail theorem (stronger than #726's Chernoff summary):** for EVERY integer \(r\) with \(0\le r\le t+1\),

\[
\boxed{\Pr_{\mathbf c}\bigl(d(\mathbf c,\mathcal A_{0:3})<r\bigr)
   \le \sum_{j=0}^{r-1}\binom tj q_{10}^{\,j}(1-q_{10})^{t-j}.}
\tag{DELTRANS-BINOM}
\]

The RHS is an exact rational number for every finite t,r; no asymptotic approximation, Gaussian independence assumption, sign-union overcount or Monte Carlo sampling is required. The t from the **EXACT MAXIMUM** original packing ν in the true W32 source yields the strongest corresponding bound accessible solely from this particular selected six-motif family and its uniform q10. At r=1, the new exact binomial bound is \((1-q_{10})^\nu\). When the actual motif-specific p_j are also known, the separately stored parent #726 exact Poisson-binomial product can improve it further.

## 3. Independent exact symbolic all-h *conditional* constants audit

The claim that ANY complete pair of correlated fixed maps has \(t>\rho s^4/6\) at sufficiently large dyadic s is NOT derived from finite W32. It was asserted analytically in [Draft #674](https://github.com/definitely-stable/Mathlab/pull/674), depending on the accepted real even-cycle supersaturation theorem and the long geometric proof from #659/#672/#673. We audit its **quantitative algebra** in the entirely separate new \`research/hyp105_original_deletion_palette_allh_bridge.py\` implementation (which does NOT import #674), with independent crosscheck against the parent implementation in the tests.

Normalize *genuine, but numerically UNKNOWN* published graph SS6 constants \(C_{\mathrm{graph}}\ge1\), \(0<c_{\mathrm{graph}}\le1\). For its stated proof assumptions, the exact parent formulas are

\[
\begin{aligned}
K&=64,\quad T=2^{65}C_{\mathrm{graph}}^3,\\
\sigma_2^{-1}&=64(65)^2,\quad
\sigma_3^{-1}=64\cdot27\cdot65^3,\\
L_6&=24+576T^2,\quad
M_3^2=(\sigma_3^{-1})^2L_6,\\
\rho&=\min\{\frac1{32},\,\frac1{768M_3^2}\},\\
\delta&=\min\{\frac1{16},\,\frac{c_{\mathrm{graph}}}{2^{120}}\},\\
L_E^+&=200\sigma_3^{-1}T,\quad
L_4^+=140(\sigma_2^{-1})^2+56,\quad
L_B^+=24\lceil\sqrt{L_4^+}\rceil T^2,\\
s_0&=\max\{64,1008T,(12L_E^+)^2,(48L_B^+)^8\}.
\end{aligned}
\tag{UDEL-GATE}
\]

The checker verifies directly, in exact integer/rational arithmetic, that deleting original source IDs loses at most two full physical heavy edges per flag; that full heavy count and source flag ownership yield effective \(\epsilon=1/16\) and the asserted \(c2^{-120}s^6\) heavy-tail lower (assuming the published graph SS6 input applies); that the remaining dense original source retains ≥3/4 s⁴ flags; that \(\rho 768M_3^2\le1\) controls the original anchor Z mask, and that all three proper-path error powers \(5,\ 11/2,\ 47/8<6\) are absorbed at the specified \(s_0\). It tests FORMAL (C,c)=(1,1),(2,1/5),(5,1/17),(13,1/101) as **algebra-only placeholder input pairs**, NOT as actual certified graph supersaturation constants. It explicitly FAILS CLOSED if no acknowledgement of the not-independently-accepted #674 parent theorem is provided.

**Logical conditional corollary only:** If the actual #674 geometric proof is independently accepted for actual valid positive external graph constants \(C,c\), then uniformly for every complete fixed correlated f,g at every sufficiently large dyadic s:

\[
\boxed{\Pr(\text{uniform random legal 51-palette original source is FULL 0{:}3 ASET})
 \le\exp\left(-\frac{53526}{51^6}\frac{\rho(C)}6s^4\right)}
\]

and for its minimum source-flag recolor distance d,

\[
\boxed{\Pr\!\left(d<\frac{53526}{51^6}\frac{\rho(C)}{12}s^4\right)
 \le \exp\left(-\frac{53526}{51^6}\frac{\rho(C)}{48}s^4\right).}
\]

This is NOT a universal *deterministic* impossibility of rare special original GF5 source assignments, NOT a new all-h proof of Branch A, and NOT an ASET exponent advancement. The C,c=1 arithmetic example must never be represented as a quantified real s0 or rho without a valid graph theorem instantiation.

## 4. Reproducibility / strict acceptance and future mathematical focus

The source module and its test suite can be run in repository GitHub-hosted Actions via
\`python -m unittest discover -s research -p 'test_hyp105_original_deletion_transversal_referee.py' -v\`,
\`python -m unittest discover -s research -p 'test_hyp105_original_deletion_palette_allh_bridge.py' -v\`,
and
\`python -u research/hyp105_original_deletion_transversal_referee.py\`.

The specialized \`.github/workflows/hyp105-aa4-original-deletion-transversal-binomial.yml\` runs only GitHub-hosted Ubuntu and saves the complete **original-source hyperedge list, exact τ and ν witnesses, all 0..4 adversarial Z distributions, and exact probability bounds** as machine-readable Actions artifacts. The final permanent certificate is replayed by a separate negative-mutation referee. The tests use genuine W32 original 45 flags, never a synthetic replacement, and the all-h algebra test does not claim finite checks prove the geometry.

After this finite interface is accepted, the **actual unresolved proof gate** toward root #230 remains a fully independent mathematical proof or correction of the asymptotic original physical-heavy-degree, mixed full/core path blocker, and six-original-ID positive-class reconstruction in #659/#672/#674. Earlier internal audits found no fatal error but do not substitute for a mathematically qualified external review. Keep #230 OPEN_WITH_FORMAL_BLOCKER, no merges, no upstream/main mutations.
