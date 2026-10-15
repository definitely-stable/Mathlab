# HYP-105 / RCP-AA4S — Original root-conditioned Fréchet barrier

Scientific source: [D6-AA4-S PR #479](https://github.com/definitely-stable/Mathlab/pull/479), pinned original source commit 357b3d201e14713668fbd045b450ffd279610081. Infrastructure tracking [#474](https://github.com/definitely-stable/Mathlab/issues/474). Scientific root [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains open, independently unproved.

## All-h scope: exact original incidence IDs and global maps

Let \(s=2^h\), \(h\ge1\), \(d=s+1\), \(V=(s+1)(s^2+1)\), and \(a\) the minimal physical alphabet with \(\binom a2\ge V\). Let \(p\) be any true original point of \(W(3,s)\). Define \(U_p\) from six **distinct genuine original point–line incidence IDs** with point source profile \(B=(2,1,1,1,1)\), repeated exactly at \(p\), and line source profile \(A=(1,1,1,1,1,1)\). For independently typed complete **globally injected** point and line maps \(f,g\), \(L_p(f)\) and \(R_p(g)\) are the unilateral physical B and A candidate subsets **of the same original universe \(U_p\)**.

The exact valid root-wise Fréchet *lower certificate* is

\[
F_p(f,g)=\max\{0,\,|L_p(f)|+|R_p(g)|-|U_p|\}.
\]

The registered all-h source theorem gives

\[
\begin{aligned}
|U_p|&\ge M_p(s)=\binom d2\frac{\prod_{j=0}^{3} d(V-3-2j)}{24},\\
|L_p(f)|&\le B_p(s)=3\binom{a-2}{4}\binom d2d^4,\\
|R_p(g)|&\le A(s)=70\binom a6d^6,\\
M_p(s)&>B_p(s)+A(s).
\end{aligned}
\]

Consequently,

\[
\boxed{\forall h\ge1,\ \forall f,g,\ \forall p:\ F_p(f,g)=0.}
\]

This concerns **what marginal-only Fréchet reasoning can certify**, not the value of \(|L_p(f)\cap R_p(g)|\). The unrestricted set-theoretic Fréchet bound is sharp in an artificial arbitrary-subset relaxation; that relaxation does not necessarily preserve globally injected physical labels. The dual original line-root A/B statement is obtained via the genuine GQ duality. Original source counting and finite s=2,4,8,16 tables plus the analytic s>=32 argument are pinned in PR #479.

## Independent finite-source certificate (not an all-h witness)

The pinned genuine \(W(3,2)\) source has 15 original point IDs, 15 lines and 45 original incidences. The source reports \(|U_p|=111132\) for **each** of the 15 true point roots; the elementary source-only lower is just \(M_p(2)=58320\). For fully coherent S68 and S72 original global \(K_6\) mappings, all root-wise Fréchet floors are zero, although genuine accepted original joint B/A sets have **44** and **36** members respectively. This demonstrates that a zero marginal lower bound is compatible with *positive actual joint charge*, not that positive charge exists uniformly at all scales.

The two distinct registered claims are:

- `HYP105-AA4S-ROOT-FRECHET-ZERO` — universal all-h root-wise **marginal-certificate** zero, deterministic mode, source original GQ for **every** legal f,g,p.
- `HYP105-AA4S-W32-POSITIVE-JOINT-ZERO-MARGINAL` — a **finite** genuine original \(W(3,2)\) witness for positive true B/A while its root-marginal certificate is zero, not an infinite low-S counterfamily.

A new negative-knowledge record `HYP105-NG-AA4S-ROOT-MARGINAL-FRECHET-ZERO` blocks precisely the invalid inference that the unilateral root cardinalities alone enforce positive joint source incidence overlap. It does **not** rule out coupled original-incidence and physical-cycle inequalities, a full seven-class minimax proof, or correlated tensor methods.

## Source evidence and generated documents

The archive preserves the **exact original Git blob bytes** from source PR #479 at frozen SHA `357b3d201e14713668fbd045b450ffd279610081`:

| Git-retained archive | Original source file |
|---|---|
| `research/rcp/hyp105/archive/PR479/proof.md` | `docs/research/HYP-105-ISSUE230-D6AA4S-ROOT-CONDITIONAL-FRECHET.md` |
| `research/rcp/hyp105/archive/PR479/oracle.py.txt` | `research/hyp105_issue230_d6aa4s_root_conditional_frechet.py` |
| `research/rcp/hyp105/archive/PR479/independent_test.py.txt` | `research/test_hyp105_issue230_d6aa4s_root_conditional_frechet.py` |

Git blob SHA-1 is recorded in receipt `HYP105-EV-AA4S.json` and independent SHA-256 checksums in `sha256-pins.json`. Tests in this import check byte integrity and all finite root-envelope constants; they **do not assert a new independent mechanical proof** of the infinite h argument or rerun the entire original W32 full injection oracle.

Canonical formulas `HYP105-F-014` through `HYP105-F-016` are indexed into all five **permanent**, deterministic, Git-versioned Markdown registers under `docs/research/hyp105/registry/`: `RESULTS.md`, `FORMULAS.md`, `PROOF-GRAPH.md`, `PROTOCOLS.md`, `RESEARCH-MATRIX.md`.

To validate:

~~~bash
python -m unittest research.test_rcp_aa4s_import -v
python -m research.rcp.structured_docs --check
python -m research.rcp.evidence_ledger --output /tmp/rcp-aa4s-evidence
~~~

Source PR #479 remains an independent research Draft, and the import stays `DOCUMENTED_IN_DRAFT`, `NOT_REVIEWED`, `NOT_ASSESSED`, `ROOT_BRANCHES_OPEN`. The scientific issue #230 is **not** resolved by a method-specific obstruction.
