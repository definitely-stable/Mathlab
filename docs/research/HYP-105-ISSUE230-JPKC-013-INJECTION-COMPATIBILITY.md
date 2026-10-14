# HYP-105 / issue #230 — JPKC-013, global injection compatibility

**2026-10-14, evidence-only Draft.** Strict child of JPKC-012 [PR #443](https://github.com/definitely-stable/Mathlab/pull/443), parent pinned at `edf373d93024f5546b4b96cf094032cd51adaeb0`. Work exclusively in `research/hyp105-issue230-jpkc013-injection-compatibility`; leave `main` unchanged. Root A/B OPEN.

## 1. Precise problem after JPKC-012

A single true original W(3,s) left factor injection f determines nonnegative source incidence tensors `T_{α,m,o}(f)` and positional named-line D6 tensor `T^D_{R,D}(f)`. For *one common globally injected* right assignment g define `S_m(f,g)` as the number of accepted ORIGINAL six-incidence sets Q with original right-line source multiset m. Then `S(f,g)=sum_m S_m(f,g)`. There is **no** proper physical P3 prerequisite.

The fixed W32 original right four-line fiber had:
- S68: `sum_m min_g S_m=11` while `min_g S=68`;
- S72: `sum_m min_g S_m=0` while `min_g S=68`.

Neither an independent profile-zero assignment nor independent choices of original Q labels need correspond to *one* legal globally injected g. The objective of this slice is to certify this incompatibility, without silently generalizing the finite fiber to all global f,g.

## 2. J44 — all-h source-line support locality (exact, conditional identity)

For every genuine host W(3,s), fixed original f, and original right-source multiset m of size six (counting repetitions), **all** terms contributing to `S_m(f,g)` depend only on the images `g(r)` of original right lines `r in supp(m)`, and not on any other original right-line images. For six non-D6 classes this is direct from physical degree-two conditions and original line type. For D6 it also holds because `D_g(R)` is defined only by the six actual original right line labels for `R=supp(m)` and compared to the fixed original-line-named left dual. Therefore for any two legal complete g1,g2 with `g1|supp(m)=g2|supp(m)`, `S_m(f,g1)=S_m(f,g2)`.

This exact **cylinder locality** is NOT an unconditional positivity theorem: each S_m may be zero on some or all g.

## 3. J45 — exact matching-cover conditional global injection inequality (all h)

Fix a finite original right-line factor block B, freeze a legal complete globally injective assignment outside B, and let E be the available physical unordered pair labels for B. The family `F` consists of **ALL** injective maps `g_B:B->E` extending the fixed outside labels. If |B|=b and |E|=e, then |F|=(e)_b. In the W32 K6 pinned 4-line fibers, b=e=4, so F has exactly 4!=24 members.

Define original source-profile **positive cylinder** `A_m={g_B in F: S_m(f,g)>0}`. By J44, A_m is a union of local restrictions `g|B cap supp(m)`. For a selected set U of source profiles, the statement

`union_{m in U} A_m=F`

is an **exact finite matching-cover certificate**. It is equivalent to the universally valid inequality over these completions:

`sum_{m in U} 1[S_m(f,g)>0] >= 1  (all g in F)`.

As every positive S_m is an *integer count of genuine ORIGINAL sixsets*, the stronger inequality `S(f,g)>=sum_{m in U} S_m(f,g)>=1` follows, and the finite minimum `min_{g in F}sum_{m in U}S_m(f,g)` may exceed 1. This is the correct way to represent a no-simultaneous-zero clause with a shared global g.

With binary original factor assignment variables `x_{r,e}`, global injection means `sum_e x_{r,e}=1` for each r and `sum_r x_{r,e}<=1` for each e. Profile positivity is a disjunction of locally injective assignment cylinders `AND_{r in B cap supp(m)} x_{r,e_r}`. The cover inequality is not an added assumption; it follows **only after** an exhaustive source-compatible cover of ALL globally legal completions is established.

The W32 24-member universe does NOT certify the inequality over other four-line blocks, other W32 maps, W34, or all-h source assignments.

## 4. J46 — complete finite minimum-cardinality source-profile cover

The executable compiles one JPKC-012 direct incidence tensor per fixed-left true W32 scheme S68/S72. It visits all 24 globally legal right four-line physical pair permutations, evaluates exact nonnegative original Q profile scores using the same common g, and independently verifies **all seven** GF5 classes of each state via historical `seven_census`.

For every globally positive source multiset m, a 24-bit mask indicates the legal states where S_m>0. Every mask is independently checked to be constant on restrictions of g to `B cap supp(m)`, the J44 locality property. The solver:
1. Deduplicates equal state masks and keeps a lexicographically pinned ORIGINAL source-profile witness;
2. Discards strict-subset masks dominated by supersets (safe for *cardinality* set cover only);
3. Computes a greedy feasible upper bound;
4. Uses complete rarest-uncovered-state memoized branch-and-bound, iterating cardinality k=1,2,..., until a cover is found.

The result proves **minimum cardinality over all original active source profiles for this exact 24-state family**, not just greedy feasibility. For each winning profile, preserve actual source-line multiset, exact positive-state mask, and the full original Q count across all 24 same-global-map states. A deterministic sufficient small source-profile matching-cover certificate follows. It does not claim an optimal weighted cover, an optimal globally general assignment solution, or a universal S bound.

## 5. Independent checks and acceptance

The dedicated GitHub-hosted CI runs five fail-closed tests including synthetic covers with independently checked combinations, invalid mask/budget tests, true-original partial-state cylinder guards, and full 24-state S68/S72 independent GF5 checks. Both scheme-specific 24-state workflows additionally emit explicit source-factor profile witness masks, minimum cover size, and minimum genuine Q charged by those witnesses; acceptance pins actual output on the final HEAD. Partial state prefixes are explicitly never full-fiber certificates.

Required: final exact HEAD dedicated SUCCESS, INDEX SUCCESS, Proof Audit SUCCESS, Full Research SUCCESS, and independent mathematical review. No `main` changes or merges.

## 6. Next research frontier

Use the J44 cylinder property to test whether local original incidence capacity forces a **uniform matching-cover / packing lower bound across every globally injective assignment**, with weights sufficient for `S_s=Omega(s^6)`. The serious blocker is the currently unconstrained growing original right-line block and physical label alphabet, not absence of a finite W32 cover. Neither root A nor root B is proved. Do not promote a finite certificate to an ASET exponent.
