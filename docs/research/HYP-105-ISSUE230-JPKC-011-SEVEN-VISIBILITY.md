# HYP-105 / issue #230 — JPKC-011: exact ORIGINAL seven-class P3 visibility

**2026-10-14. Research only; strict Draft child of JPKC-010 PR #440** on its pinned HEAD `0500f7846636f1e25f83e43e1f7eeef53cacf6cd`. No main change or merge. **Root Branch A/B OPEN**. This is not a full risk/ASET proof and W34 is deliberately excluded from the full positive-Q oracle.

## 1. Motivation and the previously missing majority

JPKC-010 found, on one coherent legal f,g each, **only 4 out of full 68** positive ORIGINAL six-incidence sets from *endpoint-bad* proper physical P3 seeds on W32 S68, and **5 out of full 72** on S72. The 64 and 67 missing Q are not necessarily B/B or C: some positive D6/B/A Q could lack this particular seed type.

JPKC-011 must count ORIGINAL six-incidence sets Q (not source-demand pairs, signed GF5 events, physical P3 occurrences, or independently relabeled Q), and classify **all seven accepted fixed-label necessary GF(5) classes** on exactly one globally injected original point/line pair map f,g. Use complete W32 original accepted `seven_census(...,witness_sets=True)`, which independently enumerates 62,370 true original left-sixcoordinate candidates. A positive Q must appear exactly once.

## 2. J38 — all-h exact visibility decomposition

Fix actual original W(3,s), s=2^h, and complete globally injective f,g into unordered physical coordinate pairs. Given an accepted ORIGINAL six-incidence set Q, let `P(Q)` be its set of **oriented, distinct 4-vertex physical graph 3-paths** whose three distinct ORIGINAL incidence IDs T are a subset of Q and whose four row AND four column coordinates are both distinct. Status of a path is determined by the **same** genuine original projection (q,r): `missing`, `incident`, `blocked_left_only`, `blocked_right_only`, `blocked_both`, or `unblocked`.

Partition each positive Q into FOUR mutually exclusive classes with strict priority:

- `endpoint_factor_bad_visible`: P(Q) contains a path with genuine ORIGINAL nonincident anchor q,r and an endpoint factor-label collision `f[q] ∩ f[p] != ∅` or `g[r] ∩ g[l] != ∅`, where (p,l) is the unique ORIGINAL GQ projection. This is the **exact JPKC-005/JPKC-010** endpoint-bad definition.
- `projection_blocked_but_not_endpoint_factor_bad`: P(Q) has a GQ path with `blocked_*` status because p/l intersects one of the four path coordinates, but NO endpoint-factor-bad witness. The collision can be purely internal.
- `other_proper_only`: P(Q) is nonempty but has no blocked projection path.
- `no_proper_P3`: P(Q) is empty.

For every fixed globally coherent original labeling and each accepted seven-class j, `S_j = S_j,factor_bad + S_j,projection_only + S_j,other + S_j,invisible`. This is all-h **exact partition algebra**, not a lower bound on any term.

**Critical independently falsified distinction:** the original JPKC-010 endpoint-bad seed has a source-factor endpoint collision, whereas the JPKC-002 broad projection `blocked_*` checks intersections with **all four** physical path symbols. On the first GitHub-hosted W32 scan the broader projection caught 73 (lex), 35 (reverse), 5 (S68) original positive Q, versus JPKC010 only 68/31/4. We now separate these cases and require strict equality of the factor-bad bin with independent JPKC010. This is a genuine new physical/source visibility nuance, not merely a spelling correction.

## 3. J39 — all-h structural C-half proper-P3 invisibility

A source half of type C is three ORIGINAL factors each repeated exactly twice. Its physical six-edge coordinate projection is **three doubled disjoint 2-cycles**, hence its *underlying simple physical pair graph is a matching*. Three consecutive coordinate-distinct physical edges of any proper synchronized P3 would form a simple four-coordinate P4 in EACH half. No P4 can be contained in a matching. Thus ANY accepted `C/A` or `C/B` ORIGINAL six-incidence set has P(Q)=empty and is in `no_proper_P3` for **all** h, independently of f,g.

Independently J15/J17 already prohibit accepted `B/B-overlap` or `B/B-disjoint` original Q from containing a **blocked endpoint-bad** physical P3. This permits B/B positive sets in the `other_proper_only` or `no_proper_P3` strata, and does not claim all B/B are completely invisible.

**Note:** C-half invisibility does not imply C/A or C/B positivity is universally forced; a true all-h lower bound on how many such Q must exist remains OPEN.

## 4. J40 — exact class-sensitive necessary GF5 floor decomposition

For the previously frozen **51-column exact nonzero checksum-4 GF(5)** necessary weights `w_j` of the seven accepted classes, the one-map fixed-label seven necessary floor numerator is exactly

```text
N_seven = sum_{j in seven classes} w_j * S_j
        = sum_{visibility state v} sum_j w_j * S_(j,v).
```

No assumption about independence of physical labels or different Q enters. This is a decomposition of the **necessary seven-class risk floor**, not the actual entire R3; it does not close S=Ω(s^6), an infinite counterexample family, or an ASET exponent. Count each ORIGINAL Q exactly once, regardless of number of physical seed witnesses or sign events.

## 5. Two genuinely different exact W32 oracle paths

1. **Global K2 physical-path index:** enumerate every oriented simple physical P3 using the actual common f,g, filter coordinate-proper paths, recover the unique ORIGINAL 3-incidence T, and key its original GQ projection status by physical path.
2. **Local ORIGINAL triple diagonal oracle:** for each of all 20 original T subsets of each accepted Q, independently construct all 2^3 signed diagonal edge combinations using the fixed physical pair labels of the exact incidence T; check both orientations, proper distinct row/col condition and original projection status. This does **not** consult the global K2 path index. Require per-T full physical-path-to-status dictionary equality, not mere count equality.

Every original Q is stratified once. J19 12/8/0 class-sensitive caps are separately tested, as is the exact weighted GF5 sum. On W32 S68/S72, independently run JPKC-010 and compare its exact endpoint-bad reached original positive Q **per class** with JPKC-011's `endpoint_bad_visible` sixset counts. Fail closed on any discrepancy.

## 6. Global source-factor coherence control

For each pinned genuine-original W32 base map S68 and S72, freeze all labels except the four ORIGINAL right line factors previously used in D6-AA4-B. Enumerate all **4! = 24** assignments of those four physical K6 pairs, without leaving their occupied image set and without relabeling individual Q independently. For each state: redo complete true W32 seven GF5 Q census, global P3 path index and visibility partition. Report the **joint per-state** seven-class visibility tensor and its GF5 weighted risk floor. Compare the minimum *over the same state* of S and the invisible population; do not conflate separately attained minima. States<24 are explicitly marked incomplete.

W(3,4) selected physical seeds from JPKC-010 are **not** a full original W34 seven-class census. The implementation rejects W34, rather than claiming visibility of unenumerated original Q.

## 7. Status gate and next research decision

This is a **restricted theorem C / finite exact structural decomposition**, not Root A or B. If most positive ORIGINAL Q are `no_proper_P3`, next develop a direct GF5 six-factor source tensor counting argument rather than revisiting Hall star demand counts. If many are `other_proper_only`, investigate incident/unblocked physical P3 seed charging and BB original GQ canonical closure; keep f,g globally coherent. Do not promote W32 24-state positivity to an all-h theorem.

Acceptance: exact FINAL-HEAD GitHub-hosted dedicated, INDEX, Proof Audit, full Research all SUCCESS, independent mathematical audit. Root #230/#176/#169 OPEN. No merge.

**2026-10-14 CI-found source-vs-physical subtlety:** original endpoint factor-pair intersections are narrower than full physical 4-coordinate projection blocks. This was independently exposed by the initial failed regression; both are now separate true-original strata with no claim about asymptotic sizes.

## 8. Frozen TRUE ORIGINAL W32 exact full-Q results (GitHub-hosted, 14 October)

Full complete W32 exact enumeration at implementation SHA `e094e836339e1c8e2f2bba9014f19bc78697b164`: dedicated 5-test job and BOTH full 24-state right-factor fiber matrix jobs SUCCESS. Before claiming final acceptance, revalidate at the later exact pinned regression HEAD, and wait for INDEX/Proof Audit/full Research.

| Map | All accepted original Q | JPKC010 factor-endpoint-bad visible | Internal physical projection blocked only | Other coordinate-proper only | **NO coordinate-proper P3** | Full necessary GF5 numerator |
|---|---:|---:|---:|---:|---:|---:|
| W32 lex | 259 | 68 | 5 | 17 | **169** | 11,225,795 |
| W32 reverse | 169 | 31 | 4 | 4 | **130** | 7,627,209 |
| W32 S68 | 68 | 4 | 1 | 0 | **63** | 3,112,510 |
| W32 S72 | 72 | 5 | 0 | 1 | **66** | 3,283,610 |

The older statement "S68 has 64 positive Q not reached by JPKC010" remains exactly valid; it is now refined into **1 projection-only + 0 other + 63 without any coordinate-proper P3**. Analogously S72 has **67** not reached by JPKC010, split into **0 + 1 + 66**. Numerically, **92.65%** of the full S68 and **91.67%** of the full S72 original positive Q cannot be accessed through *any* coordinate-proper P3.

**Most important class-specific falsifier:** S68 has no C/A, no C/B and no D6, yet among the 63 proper-P3-invisible accepted sixsets, **41** are genuine B-left/A-right, **19** are genuine A-left/B-right, and **3** are B/B. For S72 the invisible 66 split into **33 B-left/A-right, 28 A-left/B-right, 3 B/B, 2 C/A**. Thus not only C (structurally unable to host a P3), but even overwhelmingly the B/A wedge classes can be completely undetectable to coordinate-proper P3 paths under globally realizable source labeling.

This is a FINITE exact method obstruction, NOT an all-h theorem asserting invisible fraction tends to 1, nor an all-h Ω(s^6) seven-S estimate. Counting more copies of detected physical paths cannot recover invisible sixsets. The next rational line is a **direct ORIGINAL incidence support tensor / sixfactor polynomial coefficient extraction**, stratified by side A/B/C and physical cycle constraints, that never requires existence of a synchronized coordinate-proper P3.

## 9. Frozen complete coherent 24-state original-right fourfactor fibers

| Complete frozen family | Complete legal globally injected states | min full S | min JPKC010-visible Q | min entirely P3-invisible Q | min not JPKC010-visible Q | max not JPKC010-visible Q |
|---|---:|---:|---:|---:|---:|---:|
| W32 S68 | 24 | 68 | 4 | 63 | 64 | 126 |
| W32 S72 | 24 | 68 | 3 | 61 | 61 | 121 |

Each minimum is computed over ALL 24 *same-source* globally injective states but may be attained at a different state. DO NOT add separate minima as though they occurred jointly. Both original block assignment sets are precisely those used in D6-AA4-B; no independently optimized per-original-Q physical labels. Full W34 seven-census or infinite asymptotic inference not attempted.
