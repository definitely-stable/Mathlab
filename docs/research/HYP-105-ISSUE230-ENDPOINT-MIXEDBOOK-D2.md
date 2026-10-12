# HYP-105 #230 D2 — ORIGINAL endpoint mixed-book energy and exact antipodal-chord tensor

**2026-10-12, RESTRICTED_THEOREM_C / UNIVERSAL_ENDPOINT_ENERGY_BOUND_OPEN.** Draft child of [PR #395](https://github.com/definitely-stable/Mathlab/pull/395), pinned accepted D1 HEAD `976c5e47ac51203370ec2e39105754b58cbadda0`. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230) and upstream #176/#169 remain OPEN. No main merge and no invalid P2/P7 revival.

## 1. The actual proof gate

Parent #394 proved a proper `(16-o(1))s^6` physical P3 reservoir for arbitrary same global coherent f,g, an exact ORIGINAL GQ projection q-l-p-r, and an incident D6 mixed-book bound. Parent #395 showed the all-h exact blocking decomposition `C=E+I`: E is endpoint-bad weighted P3 mass on original nonincident pairs (q,r), and I is internal-only blocking on endpoint-good pairs. Neither E nor I has the needed all-h upper. S68 is a true W32 counterexample to the unit-mean P2/P7, NOT to `S=Omega(s^6)`.

## 2. New ALL-h exact bad-chord model

Let G be the physical rectangle-diagonal graph on `[a]x[a]` determined by all TRUE original GQ incidences and ONE globally coherent injective f,g. Let H be ANY undirected subgraph of G (including the original full G or a coherently pruned H from #394). Let `B_L,B_R` be D1's exact original nonincident endpoint-bad pair sets with ORIGINAL unique projection `q-l-p-r`:
- `(q,r) in B_L` iff `f(q) intersects f(p)`;
- `(q,r) in B_R` iff `g(r) intersects g(l)`.

Let `U=B_L union B_R`. For each `(q,r) in U`, write `f(q)={u,v}`, `g(r)={x,y}` and include exactly TWO *unordered physical grid antipodal chords* in a new relation `B_bad`:

    { (u,x),(v,y) },  { (u,y),(v,x) }.

These two chords are disjoint from ORIGINAL real G edges because q and r are nonincident, and from all other bad pair chords by global injectivity of physical pair labels. Thus `|E(B_bad)|=2|U|` and

    deg_Bbad(u,x) = # {(q,r) in U : u in f(q), x in g(r)}.

The complete original type is not forgotten: q is an original POINT and r an original LINE. The construction uses no new physical labels, no independent randomization, and no synthesized GQ symmetry.

## 3. New exact all-h 4-index weighted energy identity

Let `D_H(u,x)=deg_H(u,x)`. Then the mixed endpoint energy can be evaluated by two mathematically different expressions:

    W_H = sum_(u,x) deg_Bbad(u,x) * deg_H(u,x)
        = sum_((q,r) in U) sum_(u in f(q), x in g(r)) D_H(u,x).             (D2.1)

The two forms are equal by switching finite nonnegative sums. For `H=G`, the degree matrix has the independent ORIGINAL type-respecting product

    D_G = F * Inc_GQ * L^T,                                                (D2.2)

where `F[u,p]=1_{u in f(p)}` and `L[x,r]=1_{x in g(r)}`. One TRUE original incidence (p,r) contributes exactly four grid incident half-edge degrees, and the two diagonals are unique by global injectivity. The implementation computes D_G by original incidence iteration and compares with physical adjacency degrees.

For all h and all coherent f,g, the original pencil representation of U can be constructed without enumerating physical paths:

    B_L = { (q,r) : q,p on original l, q != p,
                         f(q) meets f(p), r on original p, r != l },
    B_R = { (q,r) : r,l on original p, r != l,
                         g(r) meets g(l), q on original l, q != p }.

Set identities are independently checked against all actual ORIGINAL unique GQ projections q-l-p-r. Their cardinalities are D1's exact formulas

    |B_L|=s sum_(l,z) r_lz(r_lz-1),
    |B_R|=s sum_(p,z) t_pz(t_pz-1),

and `|U|=O(s^5)`. This counts ORIGINAL endpoint pairs; the new energy W_H is their incidence-weighted path-relevant statistic.

## 4. Exact endpoint-walk tensor and properness

With `A_H` the 0/1 adjacency matrix of H and `A_B` that of B_bad, define the nonnegative *unrestricted* oriented length-three walk tensor

    T_B(H) = tr(A_H^3 A_B).

This is a finite exact integer; for each original `(q,r) in U` it sums the four orientations of the two antipodal physical chords and counts all choices of two intermediate physical grid vertices joined by an H edge. Repeated physical vertices and first/second coordinate collisions may be present in T_B.

Let E_H denote the number of PROPER oriented H-three-paths with exactly four distinct first and second coordinates whose original endpoint pair belongs to U. Then

    E_H <= T_B(H),                                                         (D2.3)
    T_B(H)-E_H = # improper endpoint-bad three-walks EXACTLY.

D1's endpoint-bad weighted mass is precisely E_G in the full G. The D2 oracle enumerates ORIGINAL endpoint pairs FIRST and then middle grid neighbors, independently of the D1 forward path scanner, to verify this equality on real W32/W34 and compute the improper-walk slack.

## 5. The ALL-h conditional mixed-book theorem (NO bound on W)

Let `t_H` be the maximum number of H-neighbors of any grid vertex in a fixed first-coordinate or second-coordinate block. The general endpoint-relation mixed-book lemma already proved in [#394](HYP-105-ISSUE230-INCIDENT-BOOK.md) applies with the genuine ORIGINAL B_bad relation. Because `B_bad` changes both coordinates for every chord, no extra graph assumptions are needed. Let `z_H=D6(H)`, the proper six-cycle count, and `B=|E(B_bad)|=2|U|`. Then

    E_H <= 24*t_H*W_H + sqrt(192*B*z_H).                                  (D2.4)

This theorem holds for every H subset G and every coherent global f,g; it is a direct restricted application of PR #394's proved mixed-book inequality, not a newly asserted all-h positive-GF5 lower.

**Precise usable sufficient gate.** Suppose H_s is the coherently spectrally pruned physical graph from #394 with `t_H=O(s^alpha)`, fixed `0<alpha<1/2`. If one can independently prove

    W_H=o(s^(6-alpha))   uniformly in globally correlated f,g,           (D2.5)

then on any hypothetical family with `S=o(s^6)` we have `z_H<=S=o(s^6)` and `B=O(s^5)`. Thus `24t_H W_H=o(s^6)`, and

    sqrt(192 B z_H)=sqrt(O(s^5)*o(s^6))=o(s^(11/2))=o(s^6).

Therefore **E_H=o(s^6)**. The remaining internal-only obstruction I_H must STILL be controlled separately. For the existing concrete pruning alpha=1/10, (D2.5) becomes `W_H=o(s^(59/10))`. **The required W_H bound is NOT proved by this PR.** A vacuous `W_H<=sqrt(sum deg_B^2 * sum deg_H^2)` cannot be called a solution.

A stronger fully compensated proposal is to establish `24t_H W_H<=eta' s^6+Lambda S` with enough remaining slack, or to charge E and I together into OTHER five positive GF5 families. Again this is a PROOF GOAL only.

## 6. Explicit finite non-vacuity check

The executable D2 report outputs:
- exact bad ORIGINAL pair sets obtained independently from pencils and unique projection;
- two chords per bad pair, an explicit zero overlap check with real G edges, and complete B-degree distribution;
- the independent ORIGINAL F*Inc*L^T degree matrix, exact energy W in two forms, `sum deg_B^2` / `sum deg_H^2` and Cauchy check;
- exact physical coordinate neighbor block bound t, allowance `24 t W`, and nontriviality flag `E_H>24 t W`;
- for complete W32/W34: independently counted unrestricted `T_B(H)`, exact proper E, explicit `T_B-E` coordinate/walk slack, D1 endpoint-mass equality;
- W38 finite exact ORIGINAL bad sets and W without an expensive second full threewalk census; no claim of full W38 proper-path replay in D2;
- synthetic subgraph tests where one true edge or ALL true edges are deleted, preserving theorem scope.

If the mixed-book certificate is numerically vacuous on unpruned W32/W34, report **VACUOUS**, do not tune constants after observing data. Finite W32/W34/W38 behavior cannot prove/falsify asymptotic (D2.5).

## 7. Next D3 after audited D2

Either prove a true-original-incidence weighted estimate on W_H for the spectrally pruned H with uniform h constants or construct a concrete coherent family where the desired `o(s^(59/10))` fails. Independently, investigate I_H, internal anchor-coordinate conflicts on endpoint-good original pairs, using actual fixed (q,r)-conditioned adjacent middle-edge tensors and compensated positive CA/CB/BB sixsets. Do not infer I from |U| or from W_H; it is a disjoint tensor. Any successful A proof must control the sum C=E+I (possibly amortized by S), not only E.

**Acceptance:** GitHub-hosted dedicated Contract, INDEX and full Research at exact final PR HEAD; separate mathematical audit and OPEN #230/#176/#169. No merge/main modification and no ASET exponent.
