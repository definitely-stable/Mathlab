# HYP-105 / RCP-AA4T — 60-position original D6 tensor and all-h conditional floor

Scientific original: [AA4-T PR #484](https://github.com/definitely-stable/Mathlab/pull/484) pinned at immutable Git commit `c51448b4e47b17737285ef8e6b7ea09991a8c289`. Infrastructure tracking: [issue #474](https://github.com/definitely-stable/Mathlab/issues/474). Unresolved scientific root: [issue #230](https://github.com/definitely-stable/Mathlab/issues/230).

## Exact original six-incidence positional theorem

For genuine \(W(3,s)\), \(s=2^h\ge2\), let \(\mathcal Q_{AA}\) be all six-element sets of **distinct actual original source point-line incidence IDs** with all six original point factors and original line factors distinct. Fix the common canonical six original positions of a given \(Q\). There are exactly **60 connected labelled \(C_6\)** duals \(H\) on those unchanged six positions.

For an arbitrary pair of separately typed **complete globally injective** physical pair-label maps \(f,g\), \(A_f(H,Q)\) and \(A_g(H,Q)\) indicate that the respective source point/line physical coordinate-column dual is the connected cycle \(H\). Both indicators refer to the **same original six incidence IDs** with the **same original column order**. The accepted original aligned physical D6 seven-GF5 class is precisely

\[
D_6(f,g)=\sum_{H\in\mathcal C_6}\sum_{Q\in\mathcal Q_{AA}} A_f(H,Q)A_g(H,Q).
\]

This is an exact **joint inner product**, not an inference from the unilateral sizes of source projection candidate sets. Original non-AA, unaligned-AA and disconnected AA cases contribute zero to this D6 tensor.

## Conditional expectation and all-h quantitative bounds

For \(V=(s+1)(s^2+1)\), the **minimal** physical \(a\) with \(K=\binom a2\ge V\), fix any legal complete source point map \(f\). Let \(g\) be ONE independent uniformly sampled COMPLETE source-line global injection shared by all \(Q,H\). Then

\[
T_f=\sum_{H,Q} A_f(H,Q),\qquad
\mathbb E_g[D_6(f,g)\mid f]=\frac{(a)_6}{(K)_6}\,T_f.
\]

Each original six-line image marginal is ordered injective. The \(D_6\) acceptance events of different \(Q\) **need not be independent**, and no concentration theorem is claimed.

With \(m=K-V\le a-2\), the physical occupied-cycle deletion union bound and genuine original bipartite GQ Hall matching imply

\[
T_f\ge\left[\frac{(a)_6}{12}-m(a-2)_4\right]\max\{1,(s+1)_6\}.
\]

For \(s=2,4\), Hall gives at least one globally genuine source matching even though \((s+1)_6=0\). For \(s\ge8\), analytic inequalities yield a uniform floor. The pinned source therefore states, for **all** \(h\ge1\),

\[
\boxed{\forall f:\quad \mathbb E_g[D_6(f,g)\mid f]\ge \frac{s^6}{98304}.}
\]

By genuine GQ original point/line duality, **separately**

\[
\forall g:\quad \mathbb E_f[D_6(f,g)\mid g]\ge\frac{s^6}{98304}.
\]

**Numerical context:** for \(s\ge8\), the previously recorded AA4-R-CYC / #480 stronger bound \(\mathbb E_gD_6\ge s^6/8\) remains in force. The AA4-T bound adds the domain \(s=2,4\) and a new **exact 60-position D6 tensor representation**, not an improved large-order constant.

## Finite true original W32 disproof of incorrect pointwise inference

The original-source tests on true W(3,2), 45 source incidence IDs and globally coherent physical K6 S68/S72 pairs record

\[
T_{f,\mathrm{S68}}=T_{f,\mathrm{S72}}=21186,\qquad
\mathbb E_g D_6=\frac{21186}{5005}=\frac{1926}{455}>0.
\]

But each **specific, adversarially fixed, complete** right-map fixture has \(D_6(f,g)=0\); the total seven-positive accepted counts remain \(S=68\) and \(S=72\), respectively. Positive \(\mathbb E_gD_6\) does not imply \(D_6(f,g)>0\) for every \(g\). Finite \(s=2\) does not establish an infinite low-S counterfamily, nor does it resolve the all-seven \(\inf_{f,g} S_s(f,g)\) problem. This is captured by dedicated `HYP105-NG-AA4T-POSITIVE-TENSOR-MARGINAL-NOT-POINTWISE` no-go record.

## Five separate registered statements

- `HYP105-AA4T-POSITIONAL-D6-TENSOR`: all-h deterministic exact 60-original-position D6 tensor.
- `HYP105-AA4T-QUENCHED-TENSOR-IDENTITY`: all-h exact conditional mean with one full opposite global map.
- `HYP105-AA4T-ALLH-QUENCHED-D6-LOWER`: every-f full-right-map conditional bound with \(1/98304\), including s=2,4.
- `HYP105-AA4T-ALLH-DUAL-QUENCHED-LOWER`: genuine point-line dual every-g bound.
- `HYP105-AA4T-W32-POSITIVE-MEAN-ZERO-D6`: distinct finite true-source quantifier obstruction.

Each is **DOCUMENTED_IN_DRAFT**, **NOT_REVIEWED**, **NOT_ASSESSED**, with root status **ROOT_BRANCHES_OPEN**. CI validates registrations and finite arithmetic; it is not independent mathematical acceptance.

## Durable source evidence, reproducible outputs

The original PR #484 immutable source proof, original oracle and independent test are copied byte-identically to

- `research/rcp/hyp105/archive/PR484/proof.md`
- `research/rcp/hyp105/archive/PR484/oracle.py.txt`
- `research/rcp/hyp105/archive/PR484/independent_test.py.txt`

Their immutable original Git blob SHA-1 values and separately computed SHA-256 pins appear in `HYP105-EV-AA4T.json` and `sha256-pins.json`. The original command remains **documented, not falsely claimed freshly executed** by the archival operation. The independent import test performs exact rational finite sample checks and validates all archived source bytes. It does **not** re-run the full original positional W32 source oracle or independently certify infinitely many orders.

Five additional scoped LaTeX formulas `HYP105-F-017` through `HYP105-F-021` feed the five committed generated files under `docs/research/hyp105/registry/`: `RESULTS.md`, `FORMULAS.md`, `PROOF-GRAPH.md`, `PROTOCOLS.md`, `RESEARCH-MATRIX.md`.

~~~bash
python -m unittest research.test_rcp_aa4t_import -v
python -m research.rcp.claim_registry
python -m research.rcp.evidence_ledger --output /tmp/hyp105-aa4t-ledger
python -m research.rcp.structured_docs --check
~~~

Original scientific research Draft PR #484 is not merged by this registry import.
