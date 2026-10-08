# TOM-001-C — Exact zero-probe, one-update certificate calibration

Issue: [#18](https://github.com/definitely-stable/Mathlab/issues/18)  
Status: **ELEMENTARY DERIVED RESULT / FINITE EXACT ORACLE**  
Novelty: **NOT CLAIMED**  
Scope: certificate-state *lower baseline*, not an incremental-computation theorem.

## 1. Frozen model

Let \(X=\{0,1\}^n\), \(f:X\to\{0,1\}\) total deterministic, with free access to its description (e.g., a truth table in this finite oracle). Prior input \(x\) is *not* queryable at certificate-check time. The verifier knows the old output \(f(x)\) for free, and stores \(h(x)\) from an alphabet \([M]\).

The only query is a single replacement \(e=(i,b)\), for \(i\in[n], b\in\{0,1\}\). The verifier, given only \(f(x),h(x),e\), must output the **exact** \(f(x[i\leftarrow b])\) for **every** \(x,e\). It is neither allowed to probe old \(x\) nor to fall back to an unknown result.

- Cost measured: **number \(M\) of metadata labels**, equivalently \(\lceil \log_2 M\rceil\) extra *fixed-length* bits per retained baseline.
- Not charged: preprocessing time of \(h\), description size of \(f\) (assumed globally known).
- Not provided: a way to update \(h(x)\) after the edit without reading old inputs; no multi-edit guarantee.
- The old output \(f(x)\) is not included in the extra metadata bit count.
- No cryptographic soundness, approximate error, randomized assumption or Rust production contract.

## 2. Elementary exact theorem (calibration, NOT original)

Define the **response profile**

\[
R_f(x)=\left(f(x[i\leftarrow b])\right)_{(i,b)\in[n]\times\{0,1\}}.
\]

For every old output \(y\) define the fiber profile set

\[
P_y=\{R_f(x):x\in X,\ f(x)=y\}.
\]

Then the smallest possible number of extra labels for a deterministic always-correct zero-probe verifier is

\[
\boxed{M_{\min}(f)=\max_{y\in\operatorname{im}(f)}|P_y|.}
\]

Thus the exact fixed-length bit budget is \(s_{\min}(f)=\lceil\log_2 M_{\min}(f)\rceil\).

**Proof, lower bound.** If \(x,x'\) have identical free old output \(y\), but different profiles \(R_f(x)\ne R_f(x')\), there is a query \(e\) for which the true new outputs differ. If \(h(x)=h(x')\), a deterministic verifier receives identical inputs for both and must return an identical answer, contradiction. Thus each distinct profile in \(P_y\) requires a distinct metadata label; \(|P_y|\le M\) for all \(y\).

**Proof, upper bound.** Within each old-output fiber \(f^{-1}(y)\), assign separate labels \(1,\dots,|P_y|\) to distinct profiles, reusing labels across different fibers (the free old output already distinguishes those). The verifier maps \((y,h,e)\) to the \(e\)-component of the unique corresponding profile. Every response is exact. Hence \(M\le\max_y |P_y|\).

This is a direct distinguishability-classes/pigeonhole argument; it is **not** publication-level novelty, nor a lower bound on computation for arbitrary DAGs. It is an instance of finite state distinguishability, closely related in spirit to Myhill–Nerode equivalence.

## 3. Exact two-bit calibration cases

For \(n=2\):
- constant zero/constant one: \(M=1\), \(s=0\);
- projection \(f(x)=x_0\): \(M=1\), \(s=0\);
- OR: the three old states with output one, \((0,1),(1,0),(1,1)\), have pairwise distinct single-edit response profiles; \(M=3\), \(s=2\);
- AND: analogously the three output-zero states have distinct profiles; \(M=3\), \(s=2\).

Check the complete grid of **all 16** functions \(f:\{0,1\}^2\to\{0,1\}\). The independent exhaustive oracle enumerates all label assignments \(h:\{0,1\}^2\to[M]\), tries \(M=1,2,3,4\), and validates all pairs of original states and all four edit queries. It does not call the profile-count formula while checking the assignment's admissibility.

Artifacts:
- `research/tom_certificate.py`: exact profile quotient, independent brute-force label oracle, executable frozen check;
- `research/test_tom_certificate.py`: comparison for all 16 functions, pinned witness tests.

Expected markers once hosted CI succeeds:
- `TOM_C_EXACT_PROFILE_QUOTIENT_PASS`
- `TOM_C_FULL_16_FUNCTION_BRUTE_FORCE_PASS`
- `TOM_C_NO_NOVELTY_CLAIM`

## 4. Explicit negative decision

**STOP** pursuing novelty for the unconstrained **zero-probe / one-edit** metadata minimization model above: its optimal answer follows immediately from partitioning old states into distinguishability classes. This does not prove that richer resource tradeoffs are known.

Avoid an invalid conclusion: \(s_{\min}\) by itself is not a useful Rust memory/CPU bound when constructing \(h\) requires a huge truth table and when edits must dynamically update \(h\). The metadata-update problem is absent by definition.

## 5. Only eligible next model (if independent prior art allows)

For O01 a nontrivial study must charge simultaneously:

1. original input retention and word/cell probes in memory of \(x\);
2. auxiliary metadata bits and amortized/worst-case update maintenance;
3. certificate bytes and construction cost;
4. verifier work, fallback rate, and completeness vs soundness;
5. repeated adaptive edits, including partially overlapping updates.

One target might be an exact Pareto frontier for a **specified nontrivial function family** in the cell-probe or word-RAM model, with proof of a new upper bound and lower bound. **No theorem is selected** until existing dynamic data-structure/sensitivity results are mapped to that exact family and cost model.

Keep [TOM-001-B](TOM-001-B-PRIOR-ART-AUDIT.md), [parent #15](https://github.com/definitely-stable/Mathlab/issues/15) and LENT-001 G2B independent. Do not release a crate based on a finite calibration identity.
