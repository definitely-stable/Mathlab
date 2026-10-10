# HYP-105 B3.2-E1-C21 — common-global-right random D6 transfer (not all-g)

2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230); scientific C20 [#315](https://github.com/definitely-stable/Mathlab/pull/315) and C20 lossless Research CI [#316](https://github.com/definitely-stable/Mathlab/pull/316). New scientific branch is stacked on exact 117-command CI HEAD of #316, **not on main**.

**SCIENTIFIC RESULT: positive all-h, ALL-fixed-left-f expectation over ONE COMMON random right bijection g, not a pointwise lower for EVERY g. The universal adversarial minimum of accepted seven-class S remains OPEN_WITH_FORMAL_BLOCKER.**

## Model and exact original sixset classes

For every h>=1, s=2^h, V=(s+1)(s²+1), Delta=s+1, a=min{n:C(n,2)>=V}, t=C(a,2)-V<a-1, and L(s)=60*C(a,6)-24*t*C(a-2,4)>0. Fix ANY occupied F_L,F_R subsets of edges of K_a, each exactly V edges, and ANY bijection f from the V ORIGINAL GQ points onto F_L. g is ONE uniformly random bijection from ALL V ORIGINAL GQ lines onto F_R, **shared by every original incidence**. All original incidence sixsets J are deduplicated by their six distinct original edge IDs. No fabricated per-J right assignments.

C20's LEFT simple C6 sixsets split by original RIGHT line multiplicities (they have six DISTINCT ORIGINAL left points):
* right A: six distinct ORIGINAL right lines. Right physical degree2 with matching LEFT/RIGHT column-position dual connected C6 is accepted as **D6**. Right A without the strict matching is rejected.
* right B: multiplicities (2,1,1,1,1). Accepted when right physical degree2 as **A-left/B-right**.
* right C: multiplicities (2,2,2). Accepted when right physical degree2 as **C/A**.
* all other right multiplicity patterns: rejected, even if left physical C6.

This partition concerns the **C20 simple C6 subpopulation**, not all A-left sources: other A-left two-triangle physical projections also exist. It is not a partition of all seven families.

## Theorem 1: all-h RIGHT DISTINCT original GQ line lifts

For any six distinct original GQ points p_1,...,p_6, each has Delta original lines. Two distinct points lie on at most one common original line. Of the Delta^6 choices of one incidence per point, the event that positions i,j select the same right line occurs for at most Delta^4 choices. Union over the 15 unordered position pairs gives

    #distinct-original-right-line lifts >= Delta^6 - 15 Delta^4.

For Delta>=5 (s>=4) this is strictly positive. For s=2, the 3-regular original GQ incidence bipartite graph has equal-size point and line parts; any subset P of left points has |N(P)|>=|P| by counting Delta*|P| incident edges against at most Delta*|N(P)|. Hall's condition holds for every six-point set, so there exists at least ONE injection selecting six distinct incident right lines. Define

    H(s) = max(1, Delta^6-15*Delta^4).

For EVERY globally compatible left f,

    N_leftC6_rightDistinct(f) >= C6(F_L)*H(s) >= L(s)*H(s).

No dependence on chosen right g; the six ORIGINAL right lines are distinct before assignment. Since H(s)=(1-o(1))s^6, this is Omega(s^15). The s=4 integer H(4)=6250.

## Theorem 2: exact ONE COMMON uniform random right D6 mean

Fix ONE ORIGINAL six-incidence J with six distinct original lines and physical LEFT simple C6. Under one globally uniform right bijection g, images of J's six named right lines are uniform among the (V)_6=V(V-1)...(V-5) ordered distinct physical right pair labels in F_R. For each simple right physical C6, precisely 12 bijections of its six edges onto the six fixed original incidence positions reproduce the left connected column-position dual C6: the dihedral automorphism group Aut(C6) has order 12. Physical cycles give disjoint ordered targets. Hence

    Pr_g[J has accepted strict D6] = 12*C6(F_R)/(V)_6.

Linearity of expectation (NO claim of independence between different sixsets) yields the EXACT identity

    E_g D6(f,g)
       = N_leftC6_rightDistinct(f)*12*C6(F_R)/(V)_6
       >= 12*L(s)^2*H(s)/(V)_6
       = (16/3-o(1))*s^6.

This holds for ALL s=2^h, all occupied F_L/F_R and every complete original-left f. The same random g is shared globally for every J. At s=2 the full occupied K6 gives exact single-J probability 12*60/(15)_6 = 1/5005.

The expectation guarantees some g with D6 at least this mean (up to integrality) but **does NOT guarantee a lower bound for the worst g**. In particular, inf_(f,g) S_seven=Omega(s^6) is still completely unproved. Nor does this imply any ASET exponent improvement or full GF5 R3 bound.

## Theorem 3: disjoint C5 B-left/A-right plus C21 strict D6, SAME g

The accepted C5 all-h theorem already lower-bounds, UNIFORMLY over the same fixed global left f and occupied right alphabet F_R, the expectation under ONE uniformly random globally shared g of the accepted B-left/A-right class:

    E_g U_{B-left/A-right}(f,g) >= M_B(s) = (140-o(1))*s^6.

This is the exact quantity returned by C5 occupied_target_uniform_floor(s)["one_common_right_bijection_mean_lower"]. C21 D6 and C5 B-left/A-right count DISJOINT ORIGINAL six-incidence sets: D6 uses six distinct ORIGINAL left points, whereas B-left/A-right uses one doubled original left point. Both are positive subclasses of S_seven and evaluated under the **same** global random g; no independence nor a second g is required. By pointwise nonnegativity and linearity,

    E_g S_seven(f,g) >= M_B(s) + 12*L(s)^2*H(s)/(V)_6
                       = (436/3-o(1))*s^6.

Furthermore the accepted GF5 necessary R3 floor in issue #230 gives, after expectation,

    E_g R3(f,g) >= [45600*M_B(s)
                        +5643*12*L(s)^2*H(s)/(V)_6] / 51^6.

These are **expectation** lower bounds, NOT a bound on inf_(f,g) S_seven, NOT a full R3 calculation and NOT a new ASET exponent. A single map g might do substantially worse than the mean. The functions and genuine W32 oracle independently compare this disjoint B/A + D6 contribution with C5's weighted-original-right source and B0 seven_census.

## Independent executable falsification

* research/hyp105_g5e2b3e1c21_global_right_transfer.py
* research/test_hyp105_g5e2b3e1c21_global_right_transfer.py
* .github/workflows/hyp105-c21-contract.yml
* Explicit two C21 test/report commands appended to the lossless 117-command six-hosted-shard Research suite, with updated immutable command fingerprint.

Six point GQ SDR counts use two different algorithms: enumeration of actual six ORIGINAL incidence choices, and independent bitmask dynamic programming on ORIGINAL right-line neighborhoods. They must agree **for each physical C6**, not just in total. Four real complete W(3,2) left mappings are covered (historical lex/reverse-line with and without nontrivial ORIGINAL point relabel), using exactly 45 ORIGINAL incidence IDs and 60*3^6=43,740 left C6 lifts each. A pre-existing seven-class classifier counts actual fixed-g strict D6, and two unchanged historical maps are independently compared to their FULL original-sixset seven_census D6 totals. For the right physical K6, independently enumerate all 60 cycles and their 720 right edge permutations each; precisely 720 ordered compatible targets must result.

Fail closed for invalid s, wrong budgets or insufficient complete original source. No extrapolation from finite W32. The symbolic proofs above, not passing bounded test samples, establish all-h status.

## Next C21-C/D hard gate

The next mathematical goal is to control **the worst globally correlated right bijection**, not simply its mean. Compare the C20 D6-only source with existing C3-C5 B-left/A-right mean Omega(s^6), and use C16 full-one-map witness classifiers. A new lower must beat known C18/C19 independent local block sabotage and C9/C10 low-pin zero barriers. Accept only explicit all-h quantifiers or a rigorous counterexample/restricted no-go with separate independent falsifiers.

Parent #230 remains **OPEN_WITH_FORMAL_BLOCKER**. No main merge or C20 ancestor merge claimed by this change. Scientific branch and CI must pass exact HEAD hosted Contract + full Research + INDEX before any integration.
