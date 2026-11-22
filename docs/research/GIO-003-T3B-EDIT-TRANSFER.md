# GIO-001.3 / G6-B — certified six-motif obstruction for edited NON-GQ incidence systems

**Parent:** [#793](https://github.com/definitely-stable/Mathlab/issues/793) and [#790](https://github.com/definitely-stable/Mathlab/issues/790). **Frozen main:** `f42aa108a2f9e15dadebf5c45fa4923cc435742b` (merged [#799](https://github.com/definitely-stable/Mathlab/pull/799), established T1/T2 GQ resilience). **Classification:** `PROVED_GQ_TEMPLATE_EDIT_TRANSFER`, a **derived scoped transfer theorem** with a genuine non-GQ family and independent exact falsifiers; NOT the fully intrinsic/axiomatic T3 theorem. No claim of a new ASET exponent.

## 1. Fix the source and model before edits

Fix integer balance `b>=1` first. Let `Q=(P,L,I)` be ANY existing thick GQ(s,t), `r=min(s,t)`, `max(s,t)<=b*r`, with original named flag set `I subset P x L`, `|P|=(s+1)(st+1)`, `|L|=(t+1)(st+1)`. Fix arbitrary complete **separately injective** physical pair maps

```
f:P -> binom([aP],2),  aP=min{a:binom(a,2)>=|P|},
g:L -> binom([aL],2),  aL=min{a:binom(a,2)>=|L|}.
```

These maps can be arbitrarily correlated and adversarial; in fact, **they may be chosen AFTER the entire edit Z,E is known**. The proof freezes whichever complete f,g are finally selected and applies #793, whose quantifiers are uniform over all such choices. What must remain fixed is their interpretation on the **same factor vertex sets** when comparing the original GQ certificate and the edited source; no resampling or redefining labels per original flag is permitted. Let `Z subset I` be arbitrary old-source flags removed (allowed to depend on Q,f,g). Let `E subset (P x L)\I` be **any** new original point-line incidences, with no multiplicity, again arbitrarily chosen and correlated. The edited named flag source is

```
I' = (I\Z) union E.
```

It is **not assumed** to be a GQ, linear, biregular, connected, high-girth, uniquely projected or spectrally controlled. It uses the identical physical pair alphabets and original factor vertices. To stay inside the usual `N'=Theta_b(r^4)` regime, simply require `|E|=O_b(r^4)`; the mathematical preservation proof does not need an insertion-size bound. A new flag is a **new source ID** and samples its own 51-pattern GF(5) coefficient if the independent coefficient model is used.

### Historical sixset predicate on the edited source

For any six distinct **named flags** `H subset I'`, the historical `D6` and `B/B-overlap` predicates are computed solely from the six original point IDs, line IDs and their fixed labels f,g. They do not depend on how many *additional* incidences exist. These original predicates still make sense for `I'` even if there is no unique projection. Define

```
H*(I';Q) = all unchanged historical D6 sixsets from Q,
           plus all unchanged constructively produced aligned BBo
           sixsets certified by Q's original FULL projection.
```

The second term carries the original produced-BBo sign-topology certificate. We do **not** call it `BBo_produced(I')` in the absence of full edited-GQ projection uniqueness. This distinction is necessary: producing a new BBo using an arbitrary edited projection could fail, whereas an old sixset's local coordinate shape is invariant.

## 2. THEOREM E — all-order edit-stable non-GQ obstruction

**Input:** the internally reviewed all-order balanced GQ deletion theorem [#793 / #799](GIO-003-GENERALIZED-INCIDENCE.md), itself conditional on the explicitly cited ordinary graph C6 supersaturation theorem. It supplies, for each fixed b, constants `rho_b>0`, `delta_b>0`, integer `r0_b` such that every true GQ(s,t), every f,g and every `Z0 subset I` with `|Z0|<=rho_b*r^4` has at least `delta_b*r^6` original D6 plus **produced aligned original BBo** sixsets supported in `I\Z0`.

**Theorem E (edit transfer).** Define `eta_b=rho_b/2>0`. For EVERY existing balanced GQ(s,t) as above with `r>=r0_b`, EVERY complete separately injective f,g, EVERY arbitrary `Z subset I`, `E subset(P x L)\I` with `|Z|<=eta_b*r^4`, the resulting (possibly non-GQ) source `I'` satisfies, for EVERY additional arbitrary adversarial named source deletion `U subset I'` with `|U|<=eta_b*r^4`,

```
|H*(I'\U; Q)| >= delta_b * r^6,
D6_{I'\U}(f,g) + BBo_historical,I'\U(f,g) >= delta_b*r^6.
```

**Proof.** Put `Z0=Z union (U intersect I)`. This set comprises only old original Q flags, and `|Z0|<=|Z|+|U|<=2 eta_b r^4=rho_b r^4`. The accepted #793 theorem produces at least `delta_b r^6` original **distinct six-ID** D6 or aligned produced BBo witnesses in `I\Z0`. Each of their six flags is in `I'\U`; every point/line name, fixed physical pair label, local coordinate flow topology and type is identical in Q and in the edited source. Hence each witness is an actual historical D6 or BBo sixset on `I'\U`, and distinct witnesses remain distinct named sixsets. Added source flags cannot invalidate six-column equalities and are never counted in this certified subset. This proves both inequalities on the **same** maps, edits and additional deletion; no edit-independent random model and no new spectral or projection assumption.

**Explicit boundary:** for the original full strength `|Z|<=rho_b*r^4`, one retains the `Omega_b(r^6)` lower bound at `U=empty`, but no positive new deletion radius follows from the same simple budget. The half-radius `eta_b` is deliberately reserved to obtain post-edit robustness and packing. Neither `rho_b` nor `delta_b` is numerically evaluated here; the existing C6 constants are existential.

### Corollary: optimal-order source packing and independent GF5 tail

Let `H*(I';Q)` be the six-uniform certified source hypergraph **on preserved original GQ flags only**. Even when E is arbitrary and the edited source has many more flags, this certified hypergraph still has only `Theta_b(r^4)` available vertices; consequently its maximum packing has order `Theta_b(r^4)`. This is NOT an optimal upper bound on the full edited-source motif packing when `|E|\gg r^4`. Since for **every** `|U|<=eta_b*r^4`, at least one hyperedge survives, any transversal has size greater than `floor(eta_b*r^4)`. The union of a maximal packing of `k` pairwise source-flag-disjoint sixsets is a transversal, so `6k > eta_b*r^4`, hence

`k >= floor(eta_b*r^4/6)+1 = Theta_b(r^4).`

For the independently sampled, uniform checksum-four 51-pattern GF(5) coefficient distribution **per named source flag**, preselect one valid signed trade event on every packed old D6 / old produced-aligned BBo. The old topology gives each probability `>=p*=5175/51^6`. The events are mutually independent because their original six source IDs are disjoint. For X realized signed collisions among the k selected events,

```
P[X < (p*/2)k] <= exp(-p*k/8) = exp(-Omega_b(r^4)).
```

Any deletion-only cleanup hitting all realized events needs at least X flags. There is NO assertion about correlated coefficients, optimized deterministic coefficient assignments, other extraction methods, or unrestricted ASET. The scoped historic floor `R3 >= (5643/51^6)delta_b*r^6` follows only when R3 is the original independent 51-pattern **expected count of three-vs-three trades on all named edited flags**; it is NOT a full-risk upper.

## 3. THEOREM P — template-anchored missing-projection budget under arbitrary edits

Even though an edited source may contain short cycles and multiple projections, a *particular old GQ projection* can be frozen before edit. Every nonincident pair of Q has one original three-flag path, and each old flag occurs in exactly `3st` of those paths by #799 and #800/G6-A.

For any `Z subset I`, after arbitrary insertions E and additional deletions U, put `D=Z union (U intersect I)`. Any pair that was **nonincident in the original Q** and has all its frozen projection anchors outside D still has a three-edge path in the edited surviving source. Therefore initially nonincident pairs that become projectionless are at most `3st|D|`. Formerly incident pairs may become nonincident only by removal of their own old Q flag, at most `|D|` further pairs. Insertions only create additional paths or remove pairs from the set of nonincident pairs, never destroy an old path. Hence

```
#(newly nonincident or old-nonincident pairs with NO 3-path)
     <= (3st+1)*|D|.
```

This holds with **no** girth, regularity, spectrum, or bound on E in the edited graph. It counts actual missing paths, not uniqueness of *new* projections. Under fixed typed pair maps the corresponding oriented physical endpoint mask is at most fourfold. The external original-GQ provenance remains indispensable: no intrinsic path count or source-index theorem has been proved for arbitrary non-GQ sources.

## 4. Constructive genuine NON-GQ family for every thick GQ

Take two **noncollinear** original points `p,q`. Take any line `Lq` through `q`. By the GQ projection axiom, the unique projection of `p` to `Lq` is the two-step path `p--J--u--Lq`, where `u!=q` and `J` is a line through p. Choose another line `Lp` through p, `Lp!=J` (possible because t>=2). Since p,q are noncollinear, neither cross incidence `(p,Lq)` nor `(q,Lp)` exists.

Remove old `(p,Lp)`, `(q,Lq)`; insert new `(p,Lq)`, `(q,Lp)`. Every factor degree is unchanged, and the edited source has the **actual** four-cycle

```
p -- J -- u -- Lq -- p
```

because original flags `(p,J),(u,J),(u,Lq)` remain and `(p,Lq)` is new. Thus it is **provably not GQ**, although it retains the original point and line counts, bidegrees, minimal typed pair-label alphabets and `N=Theta_b(r^4)`. Its source incidence girth is now 4, yet Theorem E applies because only two old original flags were deleted, for every sufficiently large existing balanced GQ order with `2<=eta_b*r^4`. Such orders are included after increasing the existential all-order threshold if necessary.

**This is an explicit infinite non-GQ family, not merely an existence-conditioned example.** For every sufficiently large dyadic order `s=t=2^h`, the classical genuine symplectic `W(3,2^h)` exists (the accepted #230 foundation). Perform this two-edge switch. Its result is a non-GQ incidence system with `N=Theta(s^4)`, girth **4**, and the uniform historical `Omega(s^6)` obstruction for all admissible physical labels. Formally increase the lower order threshold to `max(r0_b,ceil((2/eta_b)^(1/4)))`, verified by exact integer fourth-power arithmetic in the formal ledger. The finite small fixtures are only falsification checks, not empirical evidence for the asymptotic bound.

Any sequence of degree-preserving legal switches with no more than `eta_b*r^4` distinct deleted original-Q flags also falls under the theorem, whether or not the edited graph contains additional short cycles or has lost GQ projection uniqueness. This does NOT construct an arbitrary non-GQ near-Moore structure without a GQ template; it is a genuinely non-GQ **perturbation family** whose obstruction is inherited.

## 5. Independent exact finite falsifiers

Files:
- `research/gio_t3b_edit_transfer.py`: true W(3,2), W(3,3), elliptic Q^-(5,2) GQ(2,4), dual GQ(4,2); deterministic explicit switched sources; independently literal historical six-owner point/line-port recognizer (not a projection classifier); recoded source-ID historical oracle; full GF5 signature identity for each preserved original D6/produced-aligned BBo; deleted/additional-insertion masks and source-disjoint greedy packing; rational **formal-only** symbolic half-radius ledger.
- `research/test_gio_t3b_edit_transfer.py`: separate literal C4 oracle, original-source six-ID hash/profile checks, inserts ALL missing W32 incidences, correlated f/g maps, malformed edit rejection, exact finite source intersections.
- `.github/workflows/gio003-t3b-edit-transfer.yml`: GitHub-hosted specialist, exact JSON certificate, test suite, retention 90 days, plus standard Research and INDEX gates.

All finite tests are counterexample/falsification checks only. In particular small W32/W33/small unequal fixtures do **not** satisfy the theorem's enormous asymptotic threshold, and their observed motif counts are not a lower-bound proof. The source checker must not silently relabel the new geometry as GQ or manufacture a post-edit full projection mapping.

## 6. Independent review of scope and prior art

Classical Moore bounds, GQ incidence spectra, and the ordinary graph C6 supersaturation theorem are prior art; compare [On biregular bipartite graphs of small excess](https://www.sciencedirect.com/science/article/pii/S0012365X19301232), [Bipartite biregular Moore graphs](https://www.sciencedirect.com/science/article/pii/S0012365X21002958), and the published ordinary graph input quoted in #799. The present `GQ template -> edited source` bound is an **immediate but explicitly validated consequence of accepted resilience plus monotonicity**. We do **not** claim a new intrinsic incidence obstruction theorem or publication priority for editing/switching.

**Outstanding intrinsic T3 gates:** (A1) uniform conflict/Gram bounds without a hidden GQ template, (A2) rainbow physical C6 to original D6 inverse under altered source short cycles, (A4) same-priority selected walk moments, (A5) mixed FULL/CORE book estimates, (A6) original produced aligned BBo inverse after genuinely multi-valued edited projections. These are **not** solved by this transfer. No general ASET exponent, external peer review, Lean certification, or numerical non-existential deletion radius claimed.

**Acceptance:** one narrow draft PR, independent mathematical critical review, exact-head specialist and full Research/INDEX SUCCESS before any integration. Leave parent #793 OPEN until independent abstract T3 closes. No blanket merge of old Drafts.
