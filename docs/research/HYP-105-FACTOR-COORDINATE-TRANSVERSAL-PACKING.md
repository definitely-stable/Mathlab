# HYP-105 #230 — AA4-XPACK: all-h original-factor and physical-coordinate erasure robustness; three disjoint-packing scales

**New deterministic all-\(h\) corollary of the universal six-ORIGINAL-ID deletion theorem in scientific [Draft #674](https://github.com/definitely-stable/Mathlab/pull/674).** Original all-map Branch A is stated in [Draft #672](https://github.com/definitely-stable/Mathlab/pull/672), with follow-up [#673](https://github.com/definitely-stable/Mathlab/pull/673). No external qualified scientific acceptance is implied by this new corollary. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN_WITH_FORMAL_BLOCKER. This argument does NOT re-prove #672–#674 independently, and inherits their published balanced C6 supersaturation constants and same-original-source assumptions.

## 1. Actual model, quantifiers and notation

Let \(s=2^h\) with \(h\ge1\), \(d=s+1\), \(V=(s+1)(s^2+1)\), \(N=Vd\), and
\[
  a=\min\left\{t:\binom t2\ge V\right\}
   =(\sqrt2+o(1))s^{3/2}.
\]
The ORIGINAL host is the true symplectic generalized quadrangle \(W(3,s)\). Maps \(f:P(W(3,s))\hookrightarrow E(K_a)\) and \(g:L(W(3,s))\hookrightarrow E(K_a)\) are **complete, separately globally injective, arbitrarily correlated** typed pair-label maps. No physical labels are reassigned during any deletion.

Let \(\mathcal H(f,g)\) be the collection of **historically accepted, strictly positive GF(5) original sixsets** of the two disjoint classes \(D6\) and \(B/B\)-overlap. Each sixset comprises exactly SIX DISTINCT ORIGINAL incidence IDs \((p,\ell)\), the SAME original IDs on both typed physical halves. In either class, exactly six physical coordinate symbols have degree two on each side. D6 uses six distinct ORIGINAL point factors and six ORIGINAL line factors; B/B-overlap uses exactly five of each. Thus each accepted sixset occupies:

- six distinct ORIGINAL incidence ID symbols;
- at most 12 distinct, typed ORIGINAL point/line factor symbols (six each maximum);
- **exactly 12 distinct, typed physical coordinate symbols** (six on f-side and six on g-side; namespaces independent).

The parent #674 proves the following all-\(h\) assertion subject to its scientific review. There are absolute positive \(\rho,\delta\) and a finite sufficiently large \(s_0\), independent of full \(f,g\), such that for every \(s=2^h\ge s_0\) and every set of actual original incidence IDs \(Z\) with
\[
 |Z|\le\rho s^4,
\]
there are at least \(\delta s^6\) accepted original D6 or B/B-overlap sixsets disjoint from \(Z\) in **ALL SIX** original flag IDs.

The new results are deterministic consequences of this exact statement. **If the parent analytic argument fails during independent mathematical peer review, the present all-\(h\) consequences must be demoted too; finite checks do not rescue them.**

## 2. New original point/line-factor erasure theorem

Let \(P_\mathrm{bad}\subseteq P(W(3,s))\) be ANY set of original point factors and \(L_\mathrm{bad}\subseteq L(W(3,s))\) ANY set of original line factors. They may be selected adaptively after observing f,g. Delete ALL original incidence flags touching either bad set:
\[
 Z_{\rm factor}
 =\{(p,\ell):p\in P_{\rm bad}\text{ or }\ell\in L_{\rm bad}\}.
\]
Every ORIGINAL point and every ORIGINAL line of \(W(3,s)\) is incident with EXACTLY \(d=s+1\) ORIGINAL flags, so
\[
\boxed{
|Z_{\rm factor}|
 \le d\bigl(|P_{\rm bad}|+|L_{\rm bad}|\bigr).
}\tag{XPACK-F}
\]
This is a union bound with a **true original source geometry degree**, not a physical degree bound or a random incidence model. Any accepted original sixset avoiding \(Z_{\rm factor}\) automatically uses NONE of the deleted original point/line factors, since every one of its six flags has both typed endpoints outside the deleted sets.

Hence the #674 theorem implies for arbitrary f,g, bad sets and sufficiently large dyadic s:
\[
\boxed{
 |P_{\rm bad}|+|L_{\rm bad}|
 \le\left\lfloor\frac{\rho s^4}{d}\right\rfloor
 \ \Longrightarrow\ 
 \#\{Q\in\mathcal H(f,g):
    P(Q)\cap P_{\rm bad}=L(Q)\cap L_{\rm bad}=\varnothing\}
 \ge\delta s^6.
}\tag{XPACK-F-ROBUST}
\]
Because \(d\sim s\), this permits \(\Omega(s^3)\) arbitrary **original point/line factor erasures** across both typed factor domains.

### A new source-factor-disjoint packing of size Ω(s³)

Take ANY maximal-by-inclusion family \(\mathcal M_F\subseteq\mathcal H\) of accepted sixsets whose ORIGINAL point factors are pairwise disjoint and whose ORIGINAL line factors are pairwise disjoint. Let \(\nu_F=|\mathcal M_F|\). Every selected sixset uses at most 12 typed original factors, so the union of the factor supports has at most \(12\nu_F\) typed factor labels. This union meets every accepted sixset — otherwise \(\mathcal M_F\) would not be maximal.

If \(\nu_F\le\rho s^4/(12d)\), the factor union is a legal erasure in (XPACK-F-ROBUST), which **forces a new accepted sixset** outside the union, contradicting maximality. Therefore
\[
\boxed{\quad
 \nu_F>\frac{\rho s^4}{12(s+1)}
       =\left(\frac{\rho}{12}-o(1)\right)s^3.
 \quad}\tag{XPACK-F-PACK}
\]
This is **stronger disjointness than source-ID-disjoint**: two sixsets in the packing cannot share a source point or a source line even through different original incidences.

## 3. New physical coordinate erasure theorem for BOTH halves

Let \(X\subseteq [a]\) be ANY forbidden **left physical coordinate symbols** and \(Y\subseteq[a]\) ANY forbidden **right physical coordinate symbols**, with the two \([a]\) namespaces regarded as DISTINCT typed domains. The sets may depend on the complete, correlated physical maps f,g.

Since f is globally injected into the simple edge set \(E(K_a)\), each physical coordinate symbol \(x\in[a]\) belongs to at most \(a-1\) different ORIGINAL point labels f(p), because \(K_a\) has exactly \(a-1\) pairs incident with x. Each such original point has exactly d ORIGINAL incidence flags. The same independent injection and source pencil argument holds on the g-side for ORIGINAL line factors. Therefore deleting all actual ORIGINAL flags whose f or g pair touches a bad physical coordinate gives
\[
\begin{aligned}
Z_{\rm coord}(X,Y)=\{(p,\ell):&
     f(p)\cap X\ne\varnothing\;\text{or}\\
   &g(\ell)\cap Y\ne\varnothing\},\\
\boxed{
 |Z_{\rm coord}(X,Y)|
 \le d(a-1)(|X|+|Y|).
}\tag{XPACK-C}
\end{aligned}
\]
All flags are genuinely original \((p,\ell)\) of the SAME source, no physical graph is substituted. The inequality remains valid under every arbitrary source cross-map correlation.

If an accepted original sixset Q avoids this Z, every physical coordinate symbol used on its left half lies outside X and every symbol used on its right half lies outside Y, because each original source flag contributes its physical f(p) and g(ℓ) labels to the same sixset. Consequently:
\[
\boxed{
 |X|+|Y|
 \le\left\lfloor\frac{\rho s^4}{d(a-1)}\right\rfloor
 \ \Longrightarrow\
 \#\{Q\in\mathcal H(f,g):
 \operatorname{coord}_L(Q)\cap X
 =\operatorname{coord}_R(Q)\cap Y=\varnothing\}
 \ge\delta s^6.
}\tag{XPACK-C-ROBUST}
\]
The deleted physical alphabet budget is **Ω(a)**: since \(a^2=(2+o(1))s^3\), \(d(a-1)a=(2+o(1))s^4\), so
\[
 \frac{\rho s^4}{d(a-1)}
   =\left(\frac{\rho}{2}-o(1)\right)a.
\]
Therefore the all-h theorem remains valid after removing an arbitrary small positive **fraction** of the combined physical coordinate names, even if f,g were deliberately correlated and the bad names were chosen adversarially.

### A new simultaneously two-half-coordinate-disjoint packing of size Ω(s^(3/2))

Let \(\mathcal M_C\subseteq\mathcal H\) be a maximal family of accepted original D6 or B/B-overlap sixsets such that distinct members use DISJOINT left physical coordinate supports and, separately, DISJOINT right physical coordinate supports. Every accepted sixset uses exactly six left and six right coordinate names; its combined typed physical support has **exactly 12** names.

If \(\nu_C=|\mathcal M_C|\), the union of its typed physical coordinate supports has exactly \(12\nu_C\) names, and it hits the typed physical support of every remaining accepted original sixset. Otherwise another accepted sixset could be appended. Apply (XPACK-C-ROBUST) to this entire physical coordinate union. If \(12\nu_C\le\rho s^4/[d(a-1)]\), it yields an accepted original sixset avoiding all selected physical coordinate supports, contradicting maximality. Thus
\[
\boxed{\quad
\nu_C>\frac{\rho s^4}{12(s+1)(a-1)}
       =\left(\frac{\rho}{12\sqrt2}-o(1)\right)s^{3/2}.
\quad}\tag{XPACK-C-PACK}
\]
This is stronger than mere source-ID-disjointness: no two of the selected accepted source sixsets share ANY physical left coordinate or ANY physical right coordinate. Their original six incidence IDs are automatically disjoint, since sharing an original flag would repeat both physical pair labels.

## 4. The THREE nonintersecting levels

For every large enough dyadic s, any complete correlated legal f,g on the original GQ admits:

| Typed support of accepted original D6∪BBo | Guaranteed maximal packing lower | Asymptotic scale |
|---|---|---|
| Six original incidence IDs | \(\nu_{\rm flags}>\rho s^4/6\) | \(\Omega(s^4)\) |
| Original point factors and original line factors | \(\nu_F>\rho s^4/[12(s+1)]\) | \(\Omega(s^3)\) |
| Left physical coordinates and right physical coordinates | \(\nu_C>\rho s^4/[12(s+1)(a-1)]\) | \(\Omega(s^{3/2})\) |

All three inequalities are **strict** because if a maximal support-disjoint family lay at or under the displayed threshold, the parent deletion theorem would force one more accepted original sixset outside its support. The bounds concern existence, not a polynomial-time algorithm that efficiently finds such packing at all h. The selection of a maximal family is finite and constructive if all historical accepted original sixsets are available.

## 5. Scope of independent finite and rational checks

\`research/hyp105_transversal_hierarchy.py\` implements exact rational all-h threshold arithmetic (no floating point), genuine W32/W34 factor and physical coordinate mask construction using f,g injections, an independent direct-original-flag mask comparison, finite original D6 and B/B-overlap certified subset oracles and greedy typed factor or physical coordinate support packings. It retains original and physical domains separately. Mathematical \(\rho,\delta,s_0\) come directly from #674, with the unknown external graph supersaturation constants as **formal inputs**, not numerical claims that their actual values equal 1.

\`research/test_hyp105_transversal_hierarchy.py\` independently checks:

1. Exact rational identities and all three strict packing thresholds across many dyadic s and several *formal* positive graph theorem constants.
2. True W32 and W34 original point/line factor degree exposure and physical coordinate erasure budgets over mixed and dense sets, using direct ORIGINAL flag enumeration independently of the new factor-led masking.
3. Five distinct complete legal W32 g-reassignments on fixed genuine original f, exhaustive historical GF(5) original D6/B/B-overlap source class supports by all 62,370 candidate original sixsets, and equality of original six-ID erasure and typed factor/coordinate avoidance.
4. Greedy **maximal typed source-factor and physical-coordinate-disjoint packings** for the complete independent historical W32 classes; independent historical sixset support hitting-set proof and physically reconstructed source D6/BBo zero-survivor checks after deleting those factors or physical names.
5. True W34 complete legal fixed maps, removal of genuine original factors and physical coordinate names, source-backed accepted D6/BBo subfamily classification and all-six source-flag avoidance. Invalid typed inputs fail closed.

**No small W32/W34 certificate claims s>=s0**, and no independent finite test demonstrates the all-h density or packing constants. A qualified external mathematical referee for the parent #672/#673/#674 remains needed; #230 stays open. These new consequences have no asserted effect on exact full signed \(R_3\) or a new ASET exponent.
