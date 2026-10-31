# HYP-105 #230 — AA4-EXCEND: exact exceptional original endpoint partition, uniform \(21s^5\), and integrated moment thresholds

**Scope and STOP:** New independent *all-\(h\) exact-combinatorial* result for the true original \(W(3,s)\), \(s=2^h\), every legal COMPLETE separately globally injected, arbitrarily mutually correlated point and line pair labeling \(f,g\) into the MINIMAL physical alphabet \(K_a\). It improves the conservative excluded ordered endpoint-pair count \(64s^5\) in scientific [Draft #672](https://github.com/definitely-stable/Mathlab/pull/672) to \(21s^5\) for **every dyadic \(s\ge64\)**, and rigorously repropagates stronger source path selection [#679](https://github.com/definitely-stable/Mathlab/pull/679), sixth physical moment [#680](https://github.com/definitely-stable/Mathlab/pull/680), and core fourth-moment/improper three-path estimates [#681](https://github.com/definitely-stable/Mathlab/pull/681). This is an internal scientific Draft lemma, not external independent referee acceptance of the root universal Branch A, and not a new ASET exponent. No parent/main changes or merges.

## 1. Exact disjoint partition of ALL ordered coordinate-proper physical endpoint PAIRS

Define the true original GQ counts
\[
\begin{gathered}
V=(s+1)(s^2+1),\quad N=V(s+1),\quad
a=\min\{t:\tbinom t2\ge V\},\quad M=\tbinom a2,\\
C_s=(s^2+1)(s^2+a-2),\\
\Omega=\{(q,r):q\text{ original point},\
 r\text{ original line},\ q\notin r\}.
\end{gathered}
\]
For each genuine nonincident original source pair \(q,r\in\Omega\), there is a UNIQUE ORIGINAL GQ projection
\(q-\ell-p-r\), determined by the full original incidence system, independent of any retained core.

Set
\[
 B_L=\{(q,r)\in\Omega: f(q)\cap f(p)\ne\varnothing\},\quad
 B_R=\{(q,r)\in\Omega:g(r)\cap g(\ell)\ne\varnothing\},\quad
 J=|B_L\cap B_R|.
\]
Recall the *already independently proved* ORIGINAL source-pencil identities from [#427](https://github.com/definitely-stable/Mathlab/pull/427) and [#626](https://github.com/definitely-stable/Mathlab/pull/626),
\[
 |B_L|=2sM_f,\qquad |B_R|=2sM_g,\qquad
 M_f+M_g\le2C_s .
\]
No assumption that \(B_L,B_R\) are disjoint or statistically independent is allowed. Indeed \(J\) depends on the fully correlated f,g.

Consider the entire set \(\mathcal E\) of ORDERED physical endpoint vertex pairs
\[
 (v_0,v_3)=((x,y),(z,w)),\quad x\ne z,\quad y\ne w.
\]
There are exactly \((2M)^2=4M^2\) such pairs, with both typed physical coordinate namespaces retained. These are ONLY *possible endpoints* of coordinate-proper physical paths, not all actual physical paths. The endpoint labels decode through f and g when the coordinate pairs \(\{x,z\},\{y,w\}\) are respectively occupied.

Partition \(\mathcal E\) into four **mutually disjoint, exhaustive** classes, ordered by the decision procedure "label missing → occupied/incident → occupied/nonincident and source-end-bad → occupied/nonincident and source-end-good":

| Ordered physical endpoint class | EXACT population |
| --- | ---: |
| At least one f/g physical pair label missing | \(4(M^2-V^2)\) |
| Both labels occupied, ORIGINAL q incident with ORIGINAL r | \(4N\) |
| Both labels occupied, ORIGINAL q,r nonincident, bad projection | \(4(2s(M_f+M_g)-J)\) |
| Both labels occupied, ORIGINAL q,r nonincident, good projection | \(4(|\Omega|-2s(M_f+M_g)+J)\) |

Here \(|\Omega|=V^2-N=s^2N\), so all four entries add **EXACTLY** to \(4M^2\). Proof: the globally injected source pair maps occupy exactly V distinct edges each in the two different typed copies of K_a; each choice of two occupied unoriented pair labels has exactly FOUR independent choices of coordinate orientations. Thus occupied ordered endpoints number \(4V^2\). Every original (q,r) occurs in exactly four orientations. Among those, N genuine ORIGINAL incidence pairs are the incident class; the rest are \(\Omega\), whose bad union has the *exact inclusion–exclusion* size \(2s(M_f+M_g)-J\). This proves all four entries for ALL dyadic s and EVERY fixed correlated f,g. It does not rely on an arbitrary random pairing of source labels or on the source core I.

Consequently the *actual exceptional endpoint set*, before path weighting, has the **exact** size
\[
\boxed{\quad
 E_{\rm exc}
 =4(M^2-V^2)+4N+8s(M_f+M_g)-4J.
\quad}\tag{EXCEND-EXACT}
\]
The strict negative \(-4J\) term keeps *real correlated f/g information* rather than counting it twice. If all necessary physical coordinate pairs are occupied, the missing term is zero. Missing physical pairs are counted by their exact \(K_a\) occupancy, not a union bound over the two typed coordinate namespaces.

## 2. NEW rigorous uniform ALL-h cap \(E_{\rm exc}\le21s^5\), s≥64

Because \(J\ge0\) and \(M_f+M_g\le2C_s\), (EXCEND-EXACT) gives
\[
 E_{\rm exc}\le4(M^2-V^2)+4N+16sC_s.\tag{EXCEND-BOUND}
\]
We prove this is at most \(21s^5\) for EVERY \(s\ge64\) (in fact the bound also covers all integer s in this range, but only dyadic orders are claimed).

**Step 1: a sharper completely explicit upper bound for the minimal physical alphabet.** Set \(t=\tfrac32s\sqrt{s}\). Since \(s\ge64\),
\[
 \binom{\lceil t\rceil}2
 \ge\tfrac12t(t-1)
 =\tfrac98s^3-\tfrac34s\sqrt{s}
 \ge (s+1)(s^2+1)=V.
\]
The last inequality follows on dividing by \(s^2\): \(s/8\ge8\), whereas the remaining terms are bounded by
\(1+1/64+1/4096+3/(4\sqrt{s})\le1+1/64+1/4096+3/32<2\). Thus \(a\le\lceil t\rceil\le t+1\). Since \(s\sqrt{s}\ge512\),
\[
\boxed{\qquad
 a\le\left(\frac32+\frac1{512}\right)s\sqrt{s}
 <\frac{97}{64}s\sqrt{s}.
\qquad}\tag{EXCEND-ALPHA}
\]
This proof is all-h, no numeric fit; the implementation checks the squared inequality between integers, without floating-point square roots.

**Step 2: exact physical missing-label surplus.** Minimality of a means \(0\le M-V<a-1\). Hence
\[
 4(M^2-V^2)
 =4(M-V)(M+V)<4a(a-1)^2<4a^3,
\]
and by (EXCEND-ALPHA),
\[
 \frac{4(M^2-V^2)}{s^5}
 <\frac4{\sqrt{s}}\left(\frac{97}{64}\right)^3
 \le\frac12\left(\frac{97}{64}\right)^3.
\]

**Step 3: genuine source incidence and GQ-book terms.** The existing all-h #672 conservative \(N\le2s^4\) yields \(4N/s^5\le1/8\) for s≥64. Meanwhile
\[
 \frac{16sC_s}{s^5}
 =16\left(1+\frac1{s^2}\right)
       \left(1+\frac{a-2}{s^2}\right)
 \le16\frac{4097}{4096}
       \left(1+\frac{97}{512}\right).
\]

Combine the three independently justified rational constants:
\[
\begin{aligned}
 \frac{E_{\rm exc}}{s^5}
 &<\frac12\left(\frac{97}{64}\right)^3
    +\frac18
    +16\frac{4097}{4096}\frac{609}{512}\\
 &=\frac{10958501}{524288}
 =20.901681900\ldots <21.
\end{aligned}
\]
Therefore
\[
 \boxed{\qquad E_{\rm exc}\le21s^5
 \qquad(s=2^h\ge64,\ \forall f,g).\qquad}\tag{EXCEND-21}
\]
This is a **strict all-h strengthening** of #672's previously documented \(64s^5\). The proof uses the physically minimal a, genuine source line/point books, and nonnegative actual original f/g overlap; no independence or special geometry of a single f,g labeling is required.

## 3. The ACTUAL proper-path-weighted exceptional mass

An unweighted endpoint count does **NOT** imply a proportional reduction in actual physical three-paths, because some ordered endpoints may carry many more paths. Let \(P_3(v_0,v_3)\) be the count of actual coordinate-proper directed three-edge paths in the same physical ORIGINAL flag core \(H_0\) as #672. The true exceptional path weight is
\[
 W_{\rm exc}=\sum_{(v_0,v_3)\in\mathcal E_{\rm exc}}P_3(v_0,v_3).
\]
Cauchy–Schwarz on these actual ENDPOINT cells, using (EXCEND-21) and the previously proven and now improved #679/#680 path-selector/sixth-moment bound, gives
\[
\begin{aligned}
 W_{\rm exc}^2
 &\le E_{\rm exc}\,\sum_{v_0,v_3}P_3(v_0,v_3)^2\\
 &\le21s^5\,
       (\sigma_{3,\rm new}^{-2}L_{6,\rm new}s^6).
\end{aligned}
\]
Consequently
\[
\boxed{
 W_{\rm exc}\le L_{E,\rm new}s^{11/2},
 \quad L_{E,\rm new}=\sqrt{21}\,\sigma_{3,\rm new}^{-1}
                            \sqrt{24+288T^2}.
}\tag{EXCEND-WEIGHT}
\]
The old #672 bound used \(L_{E,\rm old}=8\sigma_{3,\rm old}^{-1}\sqrt{24+576T^2}\). Both selector and sixth-moment improvements are rigorously independent of new endpoint counting, so combining them is valid. The new coefficient is strictly less; in particular its ratio to the old is
\[
 \frac{L_{E,\rm old}}{L_{E,\rm new}}
 =\frac8{\sqrt{21}}\cdot27\,
   \sqrt{\frac{24+576T^2}{24+288T^2}}>47.
\]
**No path endpoint uniformity, assumption of path-to-path independence, or probabilistic source map completion** is used. The exponent remains \(11/2\).

## 4. Audited sufficient threshold using #679–#681 improvements

With the SAME #672 original degree-tail dichotomy, original physical core H0, original B/B-overlap construction and mixed-book blocking bound, introduce exact conservative improvement inputs
\[
\begin{aligned}
 K&=64,\qquad T\ge1\text{ a fixed integer upper bound on the parent's physical cap},\\
 \sigma_{2,\rm new}^{-1}&=16(K+1)^2,\quad
 \sigma_{3,\rm new}^{-1}=64(K+1)^3,\\
 L_{6,\rm new}&=24+288T^2,\quad
 L_{4,\rm new}=2\sigma_{2,\rm new}^{-2}\sqrt{8L_{6,\rm new}}+40T,\\
 B_0&=64\sqrt{(K+1)T},\qquad
 L_{E,\rm new}^2=21\sigma_{3,\rm new}^{-2}L_{6,\rm new}.
\end{aligned}
\]
Use the #681 improved proper-path lower \(\#P_3\ge s^6/2-68Ts^5\), (EXCEND-WEIGHT) and the unchanged #672 mixed blocking completion \(I_{\rm internal}\le4\sqrt{B_0TL_{4,\rm new}}s^{47/8}\). The independently verified original-image two-to-one #677 lemma then yields
\[
\boxed{
 U_{B/B\mathrm{-overlap}}\ge
 \frac{s^6}{4}-34Ts^5
 -\frac{L_{E,\rm new}}2s^{11/2}
 -2\sqrt{B_0TL_{4,\rm new}}s^{47/8}.
}\tag{EXCEND-INTEGRATED}
\]
Under the *same parent full-tails/core/projection/absolute graph supersaturation hypotheses* as #672–#674, each of the three negative terms is at most \(s^6/24\) if
\[
\begin{aligned}
 s&\ge816T,\\
 s&\ge144\,L_{E,\rm new}^2,\\
 s&\ge48^8(B_0T L_{4,\rm new})^4.
\end{aligned}
\]
Thus the identical lower \(U_{B/B\mathrm{-overlap}}\ge s^6/8\) follows for dyadic s exceeding a **new valid sufficient threshold**, but this does not independently prove the parent tail/selector/full-to-original chain or assert that the new overall s0 is smaller than every previously published parent choice.

For a machine-checkable, exact-INTEGER, intentionally conservative sufficient threshold given ANY integer \(T\ge1\), use:
\[
\begin{aligned}
 L_{4,\rm upper}
 &=2[16(K+1)^2]^2\,\lceil\sqrt{8L_{6,\rm new}}\rceil+40T,\\
 B_{0,\rm upper}&=64\lceil\sqrt{(K+1)T}\rceil,\\
 s_{0,\rm safe}
 &=\max\{64,\ 816T,\ 144L_{E,\rm new}^2,\
      48^8(B_{0,\rm upper}T L_{4,\rm upper})^4\}.
\end{aligned}
\]
Every quantity is an exact integer (no floating point). For a noninteger original physical-cap constant \(T_*\), one may choose \(T=\lceil\max(1,T_*)\rceil\). **The unverified external balanced-C6 theorem parameters \(C,c\) are NOT set to one or replaced by numerical placeholders.** The original independent degree-tail/supersaturation inputs remain prerequisite. This is an audited compatibility calculation, not a new independently accepted universal theorem or a merge instruction.

## 5. Independent REAL ORIGINAL W32/W34 source and physical tests

Four new files on the stacked scientific branch:

- \`research/hyp105_exact_exceptional_endpoints.py\`: exact integer all-h physical \(a,M,V,N,C_s\) envelope, exact TRUE original W32/W34 source-FIRST endpoint classification using actual \(q-\ell-p-r\) projection, independent physical-coordinate-FIRST enumeration of **every one** of the \(4M^2\) ordered pairs, weighted proper physical three-path census and Cauchy, plus \`recomputed_allh_dense_branch_s0\` with exact ceiling integer square roots.
- \`research/test_hyp105_exact_exceptional_endpoints.py\`: confirms the four class populations including actual f/g intersection J and their exact sum, the genuine original source \(2sM_f,2sM_g\) identities, independent comparison with established source-book population oracle, and actual path-weighted endpoint exceptions. Five different legal globally injected true W32 right reassignments, genuine W34 full/shifted right maps, sparse/full/empty original flag cores, dyadic exact all-h arithmetic from s=64 through symbolic huge s values, explicit noninteger invalid-input controls.
- \`.github/workflows/hyp105-exact-exceptional-endpoints.yml\`: dedicated GitHub-hosted Python 3.12 exact-head fail-closed tests; require independent full Research and INDEX checks before any acceptance.

The high-h symbolic arithmetic never constructs \(W(3,2^{80})\). Genuine source geometry finite tests are **falsifiers**, not the mathematical basis of the all-h proof. The exact four-class partition is analytic from global physical pair injection and unique original GQ projection. The 21s5 proof is deterministic from exact minimal K_a and original source pencil bounds.

**Scientific STOP:** New 21s5 exceptional endpoint lemma and explicit improved conditional integrated bound are rigorously proved. They do NOT replace qualified independent external review of the entire Branch A core theorem, supersaturation inputs, or exact signed R3. No main/parent mutations, PR merges, issue #230 closure or new ASET exponent.
