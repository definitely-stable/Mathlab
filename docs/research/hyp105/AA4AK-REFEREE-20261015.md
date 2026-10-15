# HYP-105 / #230 — AA4-AK independent self-review and integration decision

**Scope:** scientific [#526](https://github.com/definitely-stable/Mathlab/pull/526) at exact source HEAD `cc11c8123fcd004cd6267e6c67aef445e2b763d9`, new all-map original 1+3 connected-C6 **pre-Hall** occupancy and genuine-original **Hall-failure** bound. Dependencies: [#518](https://github.com/definitely-stable/Mathlab/pull/518) (safe true-original line-pencil and occupied B-root C4), [#521](https://github.com/definitely-stable/Mathlab/pull/521) (exact original internal-link acceptance upper). Independent sibling results: [#523](https://github.com/definitely-stable/Mathlab/pull/523) (split-triangle site cap); [#524](https://github.com/definitely-stable/Mathlab/pull/524) (full original B/A sector); [#525](https://github.com/definitely-stable/Mathlab/pull/525) (adjacent C6). Overlapping two-bridge [#522](https://github.com/definitely-stable/Mathlab/pull/522) is a subset of #521.

**Reviewer verdict:** `SELF_REVIEW_MATH_PASS_CONDITIONAL_ON_DEPENDENCIES`. Independently checked combinatorial counting and constants, explicit quantifiers and excluded implications. This is a same-agent independently re-derived proof and separately implemented falsifier, **NOT an external expert's approval**, not a formal proof assistant certificate, not novel worldwide prior-art verification, and not scientific PR merge approval. Repository status of #230 stays `OPEN_WITH_FORMAL_BLOCKER`.

## Independently checked mathematical steps

Let `s=2^h`, `V=(s+1)(s²+1)`, `d=s+1`, `a=min{t: C(t,2)>=V}`, `m=C(a,2)-V<=a-2`, and N=V C(d,2). Fix **one arbitrary pair** of complete, separately globally injected original point and line physical pair maps f,g and actual source graph W(3,s), with six **different original incidence IDs** Q on BOTH projections.

1. **Four-cross blockage lemma** (new in #526). A missing physical edge `{x,y}` can join opposite endpoints of **at most (a-2)(a-3)** unordered disjoint physical pinned edge-pairs: select endpoints `r,t` outside x,y, r≠t, obtaining `{{x,r},{y,t}}`. A physically disjoint pinned pair with all FOUR possible cross-links absent is counted FOUR times across missing edges. The true GQ condition that two actual original lines intersect in at most one source point maps original rooted source pairs injectively into physical unordered pinned pairs under the **one global opposite map**. Hence the number of fully cross-blocked genuine source rooted pairs is at most `floor(m(a-2)(a-3)/4)`. We checked for physical K6/7/8 every four-hole configuration (including adversarial concentrated holes), not merely random injections.

2. **Physical occupied middle-link lemma.** For a surviving source pin pair with four cold endpoints (opposite missing degree strictly below a/16), select one occupied cross edge between two pinned endpoints. With remaining pinned endpoints r0,r1 define Y/Z as outside physical vertices joining r0/y or r1/z by occupied physical edges. Their sizes are each `>=15a/16-4`. Each absent unpinned middle physical edge yz invalidates no more than TWO ordered (y,z) choices. Removing coincidences `y=z` costs at most a. Thus at least
   `(15a/16-4)^2-a-2m >= a²/4`
   physically occupied 1+3 C6 exist, for a>=32 using m<=a-2. The inequality reduces to the nonnegative polynomial `161a²/256 -21a/2 +20` for a>=32, independent of f,g. Each H has a unique physical cross edge for the restricted 1+3 sector: no automorphism-orbit quotient or double counting. The source root/pins/B-C4 index is retained.

3. **Sharp known source prerequisite and nonempty original GQ roots.** With `N_safe` and `C4_floor` from scientific sibling #518, the first two steps yield `P_link >= [N_safe - floor(m(a-2)(a-3)/4)]_+ * C4_floor * ceil(a²/4)`. For s>=128 use #518's `N_safe>=N/2`. Since `a <=3s^(3/2)/2` and `N>=s^5/2`, the new dead fraction is at most `27/(16sqrt(s))<1/6`, so active roots >=N/3. From `C4_floor>=a^4/128` and a²>=2V>=2s³, we derive `P_link>=s^14/384`. Exceptional powers **16, 32, 64** were independently recomputed with integer arithmetic; no asymptotic fit was used.

4. **Authentic source 1+3 Hall rejection transfer.** Scientific parent #521 bounds accepted **true-original six-ID** 1+3 internal-link B/A Q per fixed root/two actual flags/occupied first-side C4 by `4 cross links * 4 original singleton middle-row choices * (s+1) genuine opposite neighbors * 2 y-z orientations * 6 remaining real row bijections = 192(s+1)`. This is an upper on matching **multiplicity**, so the number of Hall-positive physical H is at most this cap. Since each active safe cohort contains at least `ceil(a²/4)` occupied physical H and `a²>=2(s+1)(s²+1)`, the local success fraction is at most `192(s+1)/ceil(a²/4)<=384/(s²+1)`. For **all s=2^h>=32**, the indexed true-original Hall-FAILED physical mass is therefore at least
   `(1-384/(s²+1))*s^14/384`. **It is a forced failure LOWER; it cannot imply an accepted GF(5) or seven-family S lower.**

5. **Source semantics falsifier independent of scientific Draft code.** `research/test_hyp105_aa4ak_referee.py` reconstructs W(3,2) using **all 15 nonzero vectors of F₂⁴** and a directly computed alternating symplectic form, rebuilds its 15 lines and 45 true original incidence IDs, fixes **two complete nontrivially permuted global K6 physical maps**, enumerates physical six-cycles and all 24 true original matching permutations, and crosschecks against a wholly separate source-degree-middle-edge anchored algorithm. Neither the source constructor nor either matching oracle imports the #518/#521/#526 Python modules. This guards against a shared implementation mistake while not constituting an all-h proof.

## Exact independent integer boundary table

| s | minimal a | missing physical m | N_safe floor | dead upper | N_link floor |
|---:|---:|---:|---:|---:|---:|
| 16 | 94 | 2 | 192052 | 4186 | **187866** |
| 32 | 261 | 105 | 5777010 | 1754077 | **4022933** |
| 64 | 731 | 510 | 292596665 | 67665780 | **224930885** |

The independent verifier covers h=1..60 exactly using `math.isqrt`, integer powers, `math.comb` and `fractions.Fraction`, without reading the proposed theorem implementation. Its finite symplectic source checks are intentionally separate from the physical all-h proof.

## Scope/no-go and current independent review findings

- **PASS, scoped mathematical implications:** The four-cross double count, missing-edge physical completion lower, all-h threshold and source-degree forced Hall rejection are algebraically consistent and preserve one globally coherent f,g. Conditioned on the explicitly pinned #518/#521 upstream theorems, #526's new pre-Hall and Hall-FAILED estimates follow.
- **NOT independently approved as full repository science:** #518 and #521 remain scientific Draft dependencies; their end-to-end primary source proofs and novelty require their own independent acceptance, as does this reviewer-authored self-audit. Green CI is only finite falsification, not mathematical review.
- **Duplication corrected:** #524/#525 already derive adjacent-pinned C6 original Hall transfer. #526's adjacent transfer is a **cross-oracle only**, never an original theorem claim. Do not merge duplicate scientific branches blindly; reconcile per proof scope.
- **Explicitly not proved:** `inf_(f,g) S_s(f,g)=Omega(s^6)`; an infinite correlated `o(s^6)` original seven-family counterfamily; full R3 upper; any strict ASET exponent. A Hall-failure mass Omega(s^14) is compatible with a **small positive** Hall-success mass Omega(s^6).
- **Recommended integration decision:** `NO_SCIENCE_MERGE_YET`. Keep #518/#519/#521/#522/#523/#524/#525/#526 Draft until per-PR exact-HEAD **dedicated, INDEX, Proof Audit, Full Research all SUCCESS**, reviewed mathematical proofs and reconciled ancestry. The isolated review+independent test documentation here can integrate to `main` independently as **non-promoting evidence** when its own exact-HEAD CI and protected branch gates permit. Do not mark an RCP scientific claim ACCEPTED or hand-edit generated registry pages based on this self-review.

## Reproducibility

Run from root:

```bash
python -m unittest discover -s research -p "test_hyp105_aa4ak_referee.py" -v
```

GitHub-hosted `hyp105-aa4ak-independent-referee.yml` repeats the test and prints the independent true-original W32 finite census and exact all-h checkpoints; check its **actual PR HEAD SHA** and run after the repository changes, not this document's historical snapshot. To continue genuine original Hall positivity, the next mathematical gate is a **universal nonzero source-success lower under correlated global f,g**, using the already exact B/A sector and other true GF(5) modes. Do not extrapolate finite tests to that assertion.
