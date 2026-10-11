# HYP-105 C24-B8-D — exact two-line influence and the signed-discrepancy gate

Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked parent [B8-C PR #359](https://github.com/definitely-stable/Mathlab/pull/359), HEAD `04ccac48399ab405ab40d90ffde0b70313651377`. No main modification or merge. This document concerns only the ORIGINAL seven GF(5)-necessary six-incidence families, NOT full R3 or an ASET exponent.

## Domain and complete-global-injection law

Let s=2^h>=2, n=(s+1)(s^2+1), a=min{a:C(a,2)>=n}, M=C(a,2), and f be ANY complete legal LEFT physical-edge injection of all original GQ points. RIGHT g is sampled uniformly among injections of ALL n original lines to distinct K_a edges. Define S(f,g) as the seven positive ORIGINAL distinct-sixset score in #230. All terms refer to the SAME globally coherent g.

For original right lines i!=j write Z_ij(g)=1 if g(i),g(j) share a coordinate; otherwise zero. Since two images of a uniform global injection form a uniform ordered pair of distinct K_a edges,

    p = P(Z_ij=1) = 2(a-2)/(M-1) = 4/(a+1);
    q = 1-p = (a-3)/(a+1).

For fixed f define mu=E_g[S(f,g)] and I_f(i,j)=E[S|Z_ij=1]-E[S|Z_ij=0]. The elementary covariance identity gives, EXACTLY,

    Cov(S,Z_ij) = p*q*I_f(i,j);
    mu_adj = mu + q*I_f(i,j);
    mu_dis = mu - p*I_f(i,j).

This is an all-h equality, not a discrepancy inequality; the two conditionings are the complete global-injection uniform conditionings from B8-C, NOT independently chosen per-source right maps.

## Original source-local conditional covariance: all three pin intersections

Fix an ORIGINAL six-incidence source J left-admissible under f. For ordinary tags its right acceptance event is a 2-factor on exactly SIX physical coordinates; for D6 it is one FIXED matching connected six-position dual signature. Let k in {3,5,6} be its number of distinct original right lines and r_J=P(X_J=1 | f), the exact rational B8-B/C probability for right multiplicities A=(1^6), B=(2,1^4), C=(2^3), or ONE matching D6 signature. Denote theta_J(i,j)=P(Z_ij=1 | X_J=1,f). The exact source contribution is

    I_J(i,j) = r_J * (theta_J(i,j)-p)/(p*q).

Indeed E[X_J Z_ij]=r_J theta_J and E[X_J]=r_J. Add over all ORIGINAL sixsets with their ORIGINAL multiplicities using linearity; no independence of acceptance events is used.

The k selected DISTINCT physical edges inside the accepted source form precisely one of:
- right-A ordinary: a 6-cycle or disjoint 3+3 cycles; its selected-edge adjacency-pair count b=6, and each selected edge has two selected neighbors.
- right-B: one doubled physical edge (isolated in the selected-edge adjacency graph), plus four singleton edges forming a C4. Thus b=4; doubled edge has zero selected neighbors, singleton edge has two.
- right-C: a three-edge perfect matching; b=0, every selected edge has zero selected neighbors.
- matched D6: the prescribed connected C6 dual positional signature, b=6; each selected edge has two selected neighbors.

**Both pins inside J:** theta is 2/5 for ordinary A (6 of 15 exchangeable labeled pairs); for B, 2/3 if both original lines occur once, otherwise zero; for C it is zero; for D6 it is EXACTLY 1 iff the two ORIGINAL incidence positions of i,j are adjacent in the fixed LEFT dual C6 signature, otherwise zero. D6 MUST NOT be replaced with a generic Boolean A 2-factor.

**One pin inside J:** let d_i be the number of distinct selected source physical edges adjacent to the selected image of i. If the other pinned original line is outside J, its edge is uniformly distributed over M-k unselected host edges. Thus

    theta = [2(a-2)-d_i]/(M-k).

**Neither pin inside J:** remaining M-k host edges induce the complement of k vertices in the line graph L(K_a). L(K_a) has M(a-2) unordered adjacent edge pairs. Deleting the selected k vertices and restoring b internal adjacent pairs leaves

    H_rem = M(a-2) - 2k(a-2) + b;
    theta = 2 H_rem / [(M-k)(M-k-1)].

THIS THIRD CASE IS ESSENTIAL: it usually differs from p even when J contains neither i nor j. Dropping it gives an incorrect matrix. The formulas are valid at all a>=6; there is no k-completion enumeration or per-source independent global assignment.

## Exact sufficient aggregate algorithm

For each source record (tag, positional_right_lines, positional_left_D6_signature, ORIGINAL_multiplicity), let w=multiplicity*r_J, z0=theta(neither pin), z_i=theta(only i pinned), z_ij=theta(both pinned). Accumulate per tag:

    base += w*z0
    one[i] += w*(z_i-z0)                  for i in J
    both[i,j] += w*(z_ij-z_i-z_j+z0)       for i,j in J

Then for ANY distinct i,j,

    E[S*Z_ij] = SUM_TAGS(base_t + one_t[i] + one_t[j] + both_t[i,j]);
    I_f(i,j) = (E[S*Z_ij]-p*mu)/(p*q).

This is merely a sparsity-aware exact rearrangement of the true complete-injection expectation; complexity O(number_of_compressed_records * 6^2 + 7*n^2) rational operations, with no 15! search and all seven tag contributions retained. For D6 `right_lines` must retain ORIGINAL incidence order, not be independently sorted: B2 `compile_left` does preserve this, as does its left dual signature.

## New exact row-sum identity; limitation for nonfull physical hosts

If n=M (in particular genuine W(3,2): n=M=15, a=6), then g is a physical-edge BIJECTION. For any g and each original right line i,

    SUM_(j!=i) Z_ij(g) = 2(a-2).

Covary both sides with S. Since the p*q coefficient is common to every pair, for ANY legal fixed global f,

    SUM_(j!=i) I_f(i,j) = 0.             [EXACT full-bijection all-f theorem]

The matrix is symmetric and has zero row/column sums and a zero eigenvalue. If it is nonzero, it contains both positive and negative off-diagonal influences. This is a finite physical-host theorem; W32 tests it with exact rationals.

If n<M, write U(g) for the unoccupied host physical edges and Q_i(g) for the number of those edges adjacent to g(i). Then the exact replacement is

    SUM_(j!=i) I_f(i,j) = -Cov(S,Q_i)/(p*q),

because SUM_(j!=i)Z_ij=2(a-2)-Q_i(g). An unqualified zero-row claim for all h would be FALSE; a positive lower bound cannot be deduced from zero rows, covariance signs, eigenvalues or the first two-pinned orbit alone.

## Independent verification and scientific NO-GO scope

Fast physical falsifiers cross-check all three pin-presence cases against B8-C's independent actual K6-edge pinned-completion enumerator; they include C and B doubled edges, ordinary A, the exact D6 positional signature, invalid signatures, and full-bijection zero-row conservation. Only the dedicated hosted B8-D Contract executes the genuine independent original W32 sixset cross-check on selected right pairs and the complete compressed 105-pair matrix. No 15!, no repeated 11,236-map local search, and no heavyweight default `unittest discover`.

**Structural insufficiency, not a claim about this particular seven-score:** The vector (mu, {I_ij}) has at most 106 scalar degrees of freedom when n=M=15. The space of coordinate-invariant functions on bijections g onto all 15 edges of K6 has at least 15!/6! > 106 dimensions: the physical coordinate action is free on full edge bijections. Hence there exists a nonzero mean-zero right-coordinate-invariant function Y orthogonal to EVERY Z_ij. Necessarily Y takes positive and negative values. For any C>||Y||_infinity, the TWO nonnegative invariant scores C and C+Y have the SAME mu and entire pair-influence matrix (all zero), but DIFFERENT minimum. Therefore NO universal recovery of the minimum of an arbitrary nonnegative coordinate-invariant score from the pair-conditional matrix exists. This does NOT show that this exact seven-motif GQ score has a nonzero higher-order residual, nor provide Branch A or B.

More fundamentally, the collection of ACTUAL pair relations {Z_ij(g)} for a full K6-edge bijection identifies the line-graph labeling up to physical coordinate renaming; it is the FIRST-ORDER CONDITIONAL MEANS, not the realized full adjacency graph, that the no-go addresses. The two objects must not be confused.

**Verdict:** RESTRICTED_THEOREM_C_TWO_LINE_EXACT_COVARIANCE; Branch A and B OPEN_WITH_FORMAL_BLOCKER. Next meaningful gate is a rigorously defined higher-order harmonic/conditional residual or an all-h quantitative source-count and signed-discrepancy inequality. Naive pair spectral bounds are not valid without controlling the residual and the dependent feature Gram matrix.
