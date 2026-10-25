# HYP-105 / #230: quadratic end-posting multiplicity from paired subfield copies

Date: 2026-10-26. Research source checkout observed at `1ee8a76dbf407ed8f08d96184b1aa25b9e64753d`, after the preceding middle/end result. **Scoped all-h construction / root OPEN_WITH_FORMAL_BLOCKER.** This does not prove or disprove the seven-GF(5)-class conjecture. It rules out a constant upper bound on individual end postings.

## Statement

For every \(t=2^k\), \(k\ge2\), put \(s=t^2\), \(V=(s+1)(s^2+1)\), and let \(a\) be the minimal physical alphabet with \(\binom a2\ge V\). There exist complete separately injective typed maps \(f,g\) on the genuine source \(W(3,s)\), an original flag \(\alpha=(p_0,l_0)\), and a genuinely nonincident original endpoint pair \((q,r)\), such that the end-posting occupancy satisfies

\[
 m_\alpha(q,r)\ge (n-3)(t+1)\ge s^2,
 \qquad n=(t+1)(t^2+1).
\]

Here the posting counts reversal-orbits of proper coordinate-distinct physical three-paths with the same original endpoint pair, before internal projection blocking, as in the [middle/end audit](HYP-105-ISSUE230-SFC-INDEPENDENT-AUDIT-2026-10-26.md). The construction is deterministic if every finite choice below is taken lexicographically. It claims no efficient search algorithm.

The existing universal \(m_\alpha\le\Delta_H-1=O(s^2)\) therefore has the correct order for the maximum individual end posting along this infinite dyadic subsequence. Applying the middle bound \(m\le4\) to end postings would be false.

## 1. A genuine source subgeometry and a nearly disjoint translate

Work in the quadratic field extension \(\mathbb F_s/\mathbb F_t\), using the alternating form with coefficients in \(\mathbb F_t\) from [B1.0](HYP-105-G5-C3-B1-0-SYMPLECTIC-GF4.md). The normalized projective vectors in \(\mathbb F_t^4\) give \(n\) distinct ambient points, denoted \(P_0\). Extend each totally isotropic two-dimensional \(\mathbb F_t\)-subspace to its \(\mathbb F_s\)-span to obtain \(n\) distinct ambient lines \(L_0\). Row reduction over the subfield shows that extension preserves both distinctness and incidence: a subfield point belongs to an extended subfield line exactly when it belonged to the original subfield line. Thus the induced subgeometry is precisely \(W(3,t)\), with \(n(t+1)\) genuine source flags.

The finite group \(G=\mathrm{Sp}_4(\mathbb F_s)\) is transitive separately on ambient points and on totally isotropic ambient lines. For points, extend a nonzero vector to a symplectic basis and map one such basis to another. For lines, extend a basis of each Lagrangian plane to a symplectic basis. Both maps preserve the alternating form. Uniform \(A\in G\) therefore satisfies

\[
 \mathbb E_A|P_0\cap AP_0|=\frac{n^2}{V},\qquad
 \mathbb E_A|L_0\cap AL_0|=\frac{n^2}{V}.
\]

This averaging chooses a source automorphism to build an adversarial labeling. It assumes no independence between the final fixed maps \(f,g\).

For \(t\ge4\),

\[
 \frac{2n^2}{V}
 =\frac{2(t+1)^2(t^2+1)}{t^4+1}<4.
\]

Indeed the denominator comparison reduces to \(t^4-2t^3-2t^2-2t+1>0\), which follows from \(t^4\ge4t^3\) and \(t^2-t-1>0\). Since total intersection size is an integer, some \(A\) has \(k_P+k_L\le3\), where \(k_P=|P_0\cap AP_0|\), \(k_L=|L_0\cap AL_0|\). Choose the first such symplectic matrix in the fixed finite lexicographic order.

Set

\[
 P_* = P_0\setminus(P_0\cap AP_0),\qquad
 L_* = L_0\setminus(L_0\cap AL_0).
\]

Then \(P_*\cap AP_*=\varnothing\) and \(L_*\cap AL_*=\varnothing\). Each removed subfield point or line destroys at most \(t+1\) subfield flags, so the remaining incidence set

\[
 F_* = \{(p,l)\in P_*\times L_*:p\in l\}
\]

has size at least \(n(t+1)-(k_P+k_L)(t+1)\ge(n-3)(t+1)\). Every \((p,l)\in F_*\) has its paired genuine source flag \((Ap,Al)\). The two point supports and two line supports are separately disjoint. No claim that the entire two subgeometries are disjoint is needed.

## 2. The supports fit the minimal alphabet

For \(t\ge4\),

\[
 n+2=t^3+t^2+t+3\le\frac{87}{64}t^3,
 \qquad (87/64)^2<2.
\]

Consequently \(\binom{n+2}{2}<t^6<V\), and minimality of \(a\) gives \(a\ge n+3\). Reserve the three coordinate symbols \(0,1,2\). There are enough remaining symbols to injectively index every point of \(P_*\), and independently every line of \(L_*\), by symbols at least three.

Also \(V>4n\), since \(V/n=(t^4+1)/(t+1)>4\). The two paired point supports and two paired line supports each have size at most \(2n\). There is a genuine flag \((p_0,l_0)\) outside both paired supports: the total number of source flags is \(V(s+1)\), while flags touching either forbidden support number at most \(4n(s+1)\). Choose the first such flag.

Choose any \(q\) outside the paired point supports and different from \(p_0\). Since

\[
 V-2n-1>s+1,
\]

there is a line \(r\) outside the paired line supports and different from \(l_0\) which is not incident with \(q\). The inequality follows from \(V>4n\) and \(2n-1>s+1\). Take lexicographically first choices. This supplies the exact original nonincident endpoint condition, rather than a physical-label proxy.

## 3. Complete legal injections and the end posting

Assign distinct free symbols \(z_p\in\{3,\ldots,a-1\}\) to \(p\in P_*\), and independently \(Z_l\) to \(l\in L_*\). Prescribe

\[
\begin{aligned}
 f(p)&=\{1,z_p\},& f(Ap)&=\{2,z_p\},&
 f(p_0)&=\{0,1\},& f(q)&=\{0,2\},\\
 g(l)&=\{1,Z_l\},& g(Al)&=\{2,Z_l\},&
 g(l_0)&=\{0,1\},& g(r)&=\{0,2\}.
\end{aligned}
\]

On each typed side all prescribed source IDs and all prescribed coordinate pairs are distinct. Complete the remaining assignments by matching remaining source IDs to unused physical pairs in lexicographic order; \(\binom a2\ge V\) guarantees sufficient pairs. This does not change any prescribed label.

For each \((p,l)\in F_*\), the physical corner sequence

\[
 (0,0)\;--\;(1,1)\;--\;(z_p,Z_l)\;--\;(2,2)
\]

uses, in order, the genuine source flags \((p_0,l_0)\), \((p,l)\), \((Ap,Al)\). Each coordinate has four distinct symbols. Its endpoint coordinate pairs recover precisely \((q,r)\), which was chosen genuinely nonincident. The fixed flag \(\alpha=(p_0,l_0)\) is an end flag, and different retained subfield flags give different intermediate corners and hence different reversal-orbits. Thus \(m_\alpha(q,r)\ge|F_*|\).

Finally \((n-3)(t+1)=t^4+2t^3+2t^2-t-2\ge t^4=s^2\). This proves the stated infinite-family lower bound. Arbitrary completion may create additional orbits, which only strengthens it.

## Boundary for the root conjecture

One posting supplies \(C_{1,\mathrm{end}}\ge\binom{m_\alpha(q,r)}2=\Omega(s^4)\), which is compatible with an aggregate \(O(s^6)\) theorem. This is not an all-map lower bound for \(S_{\mathrm{seven}}\), not an \(o(s^6)\) counterfamily, not a bound on \(P\) or \(C_0\), and not a GF(5) acceptance transfer. It shows why the next proof should control aggregate proper codegree energy rather than the maximum individual end posting by a constant.

The nonincident endpoint conditioning is essential to that aggregate problem: with an end posting oriented as \(v_0-v_1-v_2-v_3\), its tail obeys \(v_0\in\Gamma_H(v_1)\setminus\Gamma_H(v_3)\). The missing physical edge \(v_0v_3\) is exactly the true source nonincidence \(q\notin r\), since both endpoint labels are occupied. Large common-neighbor multiplicity alone therefore does not imply many eligible tails; vertices with identical neighborhoods provide none.

## Genuine finite W(3,4) certificate

The [deterministic constructor](../../research/hyp105_end_posting_subfield.py) uses the true GF(4) source and two embedded GF(2) copies. For \(x\in\mathbb F_4^4\), compose the symplectic transvections \(x\mapsto x+\lambda B(x,v)v\) in this order:

| v | lambda |
|---|---:|
| (0,1,3,3) | 2 |
| (1,1,2,2) | 3 |
| (0,0,1,3) | 2 |
| (0,1,0,0) | 1 |

Field elements use the existing polynomial basis with \(x^2+x+1=0\), never integer arithmetic modulo four. The two GF(2) supports overlap in three original points and two original lines. At this smaller size, only eleven free coordinates fit; retain the first eleven nonoverlapping point IDs and first eleven line IDs, leaving 28 genuine paired flags. Choose the first external source flag and nonincident endpoint and complete all labels lexicographically, as in the code.

The recovered original IDs are \(\alpha=(29,3)\), \((q,r)=(3,4)\), with \(f(p_0)=g(l_0)=\{0,1\}\) and \(f(q)=g(r)=\{0,2\}\). Direct original-incidence products over all 121 free corners give **exactly 28** end reversal-orbits at this posting. This is a genuine complete-injection counterexample to an auxiliary end cap of four; it does not depend on extrapolating the large-field theorem to \(t=2\).

| Source census quantity | Exact value |
|---|---:|
| P | 73840 |
| Q | 1143472 |
| C0 | 103619 |
| C1 middle | 387 |
| C1 end | 20468 |
| Maximum middle / end occupancy | 3 / 28 |
| Maximum physical degree | 32 |
| Maximum N3 | 84 |

The [tests](../../research/test_hyp105_end_posting_subfield.py) independently check the source point/line automorphism, every original flag, complete injections, the target posting via original incidence products, and the full prior SFC/endpoint oracles. The [specialized workflow](../../.github/workflows/hyp105-issue230-weighted-endpoint.yml) runs these checks. Reproduction and exact source hashes are recorded in [the local experiment](../../research/hyp105_end_posting_subfield_run_20261026.json).

## Evidence and source pinning

This note derives its construction directly from the source model and elementary finite-group averaging. A literature search also located the primary paper [Cossidente–Penttila, *Subquadrangle m-regular systems on generalized quadrangles*, J. Combin. Designs 19 (2011), 28–41](https://onlinelibrary.wiley.com/doi/10.1002/jcd.20260), whose publisher abstract concerns embedded symplectic subquadrangles of \(W_3(q^2)\) for even \(q\). No theorem from that paper is needed or transferred here; its full proof was not inspected. The subfield embedding and translate argument above are explicit.

An executed Python 3 stdin sanity check at the observed checkout verified the exact integer inequalities `2*n*n < 4*V`, `(n+2)*(n+1) < 2*V`, `V > 4*n`, `V-2*n-1 > s+1`, and `(n-3)*(t+1) >= s*s` for `k=2..10`, with `t=1<<k`, `s=t*t`. Actual output: `DYADIC_PARAMETER_INEQUALITIES_PASS k=2..10 (finite sanity check; analytic proof separate)`. These finite checks do not establish the quantified theorem; the proofs above do. No ambient W(3,16) enumeration or full-path large-field experiment was executed by this investigator.

Observed SHA-256 hashes of raw Windows checkout source bytes:

| Source | SHA-256 |
|---|---|
| `docs/research/HYP-105-G5-C3-B1-0-SYMPLECTIC-GF4.md` | `2be875df0e44fc13e744660fbfe4357f62a2b8011c34c0d53545090d4b63c49d` |
| `docs/research/HYP-105-PHYSICAL-DEGREE-ENERGY.md` | `1aa5e5bccec323d83f21d26458f6f35a458dad0a14de62d78a974346744f5345` |
| `docs/research/HYP-105-ISSUE230-SFC-INDEPENDENT-AUDIT-2026-10-26.md` | `009b7becc6aa6ea93470e168f95e860225d6234c35ff175796a3046b3b19bf2b` |
| `research/hyp105_b1_symplectic.py` | `6451bcb7e76bc722bcde280985131c41b415712f23787c353ad29df729a5b80f` |

Exact runtime model variant was not exposed; this investigator inherits the parent GPT-6 runtime. Mathlab MCP reporting was unavailable. No scientific acceptance field or published snapshot was changed.

Local follow-up verification: **45 tests passed**, including the four new subfield tests, six SFC tests, prior invariant/variance/degree/endpoint certificates and workflow-shard checks. Catalog, known/STOP registry, literature and whitespace validators all passed. A separate read-only agent review found no actionable defect in the finite constructor or the quantified subfield proof; this is not a qualified external referee. Hosted checks for this new follow-up are evaluated separately after its commit.
