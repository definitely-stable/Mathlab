# HYP-105 / issue #230 — JPKC-005: alternate ORIGINAL three-incidence completion

**13 October 2026. RESTRICTED_THEOREM_C + exact finite W32 ORIGINAL census; no Root A/B proof.**
Research-only strict stacked Draft on fully 4/4 CI successful JPKC-004 [#429], exact parent HEAD `05c3360deaa2304106eb5b4f9936821947816451`. `main` untouched, no merges. JPKC-004 showed the direct two-P3 six-incidence union supplies only D6; this stage searches a **DIFFERENT ORIGINAL three-incidence completion** of one physical P3 seed, not another path using the identical original six edges.

## 1. Correct new object: one proper oriented 3-path seed and a DIFFERENT source triple

Fix s=2^h, V=(s+1)(s²+1), N=V(s+1), a=min{n:binom(n,2)>=V}, a globally complete independently injective ORIGINAL point map f and line map g. In their original two-diagonal Kikuchi graph G, take a physical **coordinate-proper** ORIENTED 3-path P=(u,b,c,v). Its three unique ORIGINAL incidence IDs form an unordered set T(P), |T|=3. Their physical point-edge and line-edge projections are each a 3-edge simple P4 on exactly four physical symbols.

Assume the ORIGINAL endpoint point/line labels q=f^-1(pair(first rows u,v)), r=g^-1(pair(second columns u,v)) exist and are nonincident, with unique ORIGINAL projection q--ell--p--r. The P3 is **endpoint-bad** if f(q) shares a physical coordinate with f(p), or g(r) shares a physical coordinate with g(ell). JPKC-003 J7 forces a conditional concentration of such paths in hypothetical small-S counterfamilies.

The direct canonical completion A(q,r)={ (q,ell), (p,ell), (p,r) } is forbidden for endpoint-bad paths by JPKC-004 J9. **Instead**, search a DIFFERENT original triple U, |U|=3, disjoint from T, such that Q=T∪U is SIX different original incidence IDs and one of the seven SOURCE-certified two-sided GF5 positive motif classes.

Do not assume U is another ORIGINAL GQ length-three walk. Recover whether it forms a GQ projection anchor and record that Boolean/anchor when it actually does. It may instead be a genuinely different three-incidence source topology. Distinguish a source triple from physical endpoint labels; never invent GQ automorphisms or independently resample f/g.

## 2. THEOREM J14 (ALL h): uniform 320 witness multiplicity for physical P3 seeds

Fix ANY original six-incidence set Q (no need to assume it is accepted). The number of ORIENTED SIMPLE physical length-three paths whose graph edges correspond to THREE DISTINCT ORIGINAL incidences from Q is at most **320**, regardless of globally injected f,g and h.

**Proof.** Choose the three source incidence IDs from Q in at most C(6,3)=20 ways. Every original incidence generates exactly TWO undirected physical graph-diagonal edges. For a chosen triple there are at most 2^3=8 possible physical edge triples. A fixed set of three distinct undirected graph edges either is NOT a simple P4 or forms exactly one undirected P4 with TWO oriented directions. Therefore at most `C(6,3)*2^3*2=320` oriented physical three-paths are possible. This overcounts paths that fail the coordinate-proper or endpoint-bad requirements, so it is valid for all of them. QED.

In particular, a fixed source three-incidence seed T can support at most `2^3*2=16` oriented physical P3 realizations, uniformly in h.

For any family `F` of DISTINCT selected original sixsets, and any collection `P_E` of endpoint-bad physical three-paths, let `H_E` be the count of ordered pairs (P,Q), P in P_E, Q in F, with T(P)⊂Q. Then

```
H_E <= 320 |F|.
# {endpoint-bad oriented physical seeds admitting >=1 alternate accepted Q}
   <= H_E <= 320 S.
```

This is a **rigorous all-h upper multiplicity**, NOT a positive lower bound on H_E. Under the hypothetical JPKC-003 endpoint-dominated Branch-B obstruction `E>=(8-o(1))s^6` with `S=o(s^6)`, at least `E-320S=(8-o(1))s^6` endpoint-bad physically proper seeds have NO accepted original alternative three-incidence completion at all. Their fraction among E tends to 1. Thus the new, more flexible alternative-completion route also cannot by itself turn a hypothetical huge endpoint-bad seed mass into positive GF5 sixsets: a nontrivial *extension theorem* would still be required. This does NOT settle Root A/B.

## 3. THEOREM J15 (ALL h): a coordinate-proper P3 seed CANNOT extend to a C-type half

The original seven-family positive classes on six ORIGINAL incidence positions have physical two-sided six-coordinate 2-regular projections with original factor-count partitions:
- A: six source factors used once;
- B: one source factor used twice, and four used once;
- C: THREE source factors each used twice.

A C-type projection consists of THREE physically disjoint double edges: each repeated ORIGINAL factor has one injective physical pair label; its two original incidences give the same edge in the six-position projection, producing a connected component with exactly two physical vertices (a 2-cycle). Distinct source pair labels are globally injective and no physical coordinate can have degree >2, so these three 2-cycles have disjoint physical supports.

But the three projected physical edges of a coordinate-proper P3 seed form a CONNECTED physical 3-edge path on FOUR DISTINCT physical vertices, a P4. Such a path cannot be contained in a disjoint union of 2-vertex components. Therefore **no genuine accepted sixset containing T(P) can have type C on the left OR right**, for ANY h.

Hence only `D6, B-left/A-right, A-left/B-right, B/B-overlap, B/B-disjoint` are reachable by alternate completion of a proper physical P3 seed. `C/A` and `C/B` (the other two original accepted motif classes) are **provably inaccessible** to this seed witness. This applies even if U is a different original GQ anchor or an arbitrary additional source triple.

This is a *strict restricted-method exclusion*, not a claim that C/A and C/B have no role in the global seven-family S.

## 4. THEOREM J16: the canonical ORIGINAL projection triple cannot be a positive alternate completion

For an endpoint-bad physical P3, its canonical projection triple A(q,r) cannot make a six-coordinate 2-regular original Q because it produces a physical degree at least 3 on one side (JPKC-004 J9). Thus for every positive extension Q with U=Q\T, `U != A(q,r)`. Equivalently at least ONE of the three canonical completion incidences must be replaced; the exact number of common canonical IDs is 0,1,or 2, never 3.

Do NOT claim a uniform requirement of two replacement incidences. The B-type positive projection may consist of a physical C4 plus a disjoint repeated-edge C2; an original endpoint chord can participate in that C4. The stronger "all q or r labels are forbidden" shortcut would be FALSE for B/B-overlap completions. The executable checks actual canonical intersections rather than assuming an unsupported fixed edit distance.

## 5. Exact true ORIGINAL W32 falsifier; truthful W34 boundary

The new standalone `research/hyp105_issue230_jpkc005_alternate_three_completion.py`:
1. Reconstructs the full ORIGINAL globally injected f,g, every physical graph edge's ORIGINAL incidence ID, and ALL proper ORIENTED P3 seed source triples.
2. Builds an **EXHAUSTIVE** W32 true-original accepted seven-family sixset index from the existing independently checked 62,370 left candidates. Every accepted sixset Q contributes exactly C(6,3)=20 triple-index entries, retaining actual source IDs and true GF5 class, not an image-degree proxy.
3. Enumerates ALL endpoint-bad oriented physical P3 seeds, looks up every genuinely accepted Q containing T, excludes the forbidden canonical GQ completion, and separates alternate three-source-incidence U into `second_true_original_GQ_walk` vs `not_three_incidence_GQ_walk`. Reports positive extension counts, original class breakdown, physical seed coverage, and U∩A size.
4. Proves from finite actual physical paths the <=16 realizations per original 3-ID seed and <=320 oriented proper physical seeds per accepted original Q. Independently reclassifies EVERY one of the 62,370 W32 structural candidate sixsets for S68 and S72 with a general-physical-palette implementation of the true ORIGINAL seven-family acceptance rules. This is a stringent equality oracle against the existing W32 classifier.
5. On W34 lex/random and REAL D4 symplectic-spread complete f,g, **does NOT claim a full seven-family Q census**. Instead checks source 3seed physical geometry, physical reversal counts, and that EVERY original unblocked GQ 3+3 completion belongs to the true B/B-overlap structural class under the generalized sixset classifier. No W34 selected GF5 sixset total is fabricated.

Fail closed for illegal global pair injections, W34 `exact_W32=True` scope, physical-path budgets, accepted-sixset budgets, bad original IDs or unsupported source completions. The acceptance gates are to run ONLY on GitHub-hosted CI; no self-hosted runner required.

### Cross-stack interpretation

D6-Z [#428] established that image-only sharp occupied physical edge adjacency / global six-incidence wedge statistics are NOT enough to determine seven GF5 S. JPKC-005 retains the ORIGINAL six incidence positions and 3seed completions, not merely 2regular physical graph degree. D6-X/Y show that local pseudomarginal consistency cannot replace global occupancy; here every fixture uses one fully globally injective f,g.

## 6. Next mathematically honest target, contingent on observed exact completion data

If the actual W32 S68/S72 finite oracle demonstrates many endpoint-bad seeds with **ZERO** positive alternate 3-incidence completions, the naive "there is always a nearby source-positive Q" hypothesis is falsified already at W32. If extension coverage is high in W32 but bounded in pathological D4, conduct a **separate** clearly scoped W34 targeted positive-Q construction/verification, not an unbounded C(425,6) census.

For any eventual all-h compensation, one needs either:
- a PROVED uniform extension theorem (e.g. `>=epsilon*s^6` endpoint-bad proper P3 seeds carry a genuine seven-positive alternate source-Q), together with J14's uniform 320 charge (then `S>=epsilon/320*s^6`), OR
- a genuinely different global invariant (multi-anchor, additional source incidences, physical occupancy-coupled matching) that bypasses the J14 extension-isolation obstruction.

Do not claim J14 alone proves any unconditional S floor. Root #230/#176/#169 remain OPEN. No full R3 upper or ASET exponent. Strict Draft and independent mathematical review before merge.
