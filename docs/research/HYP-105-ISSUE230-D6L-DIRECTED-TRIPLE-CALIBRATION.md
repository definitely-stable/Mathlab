# HYP-105 / issue #230 — D6-L: exact directed triple-pressure calibration

**2026-10-13. RESTRICTED_THEOREM_C. Branch A / Branch B OPEN.**

Strictly stacked over [D6-K Draft #410](https://github.com/definitely-stable/Mathlab/pull/410) with audited green parent HEAD 6f360a68ed0aac9c91f8a60455ce0d475d2ffb78. The source is always the ORIGINAL weighted GQ-incidence 3-hypergraph (blocked proper oriented P3 with BOTH endpoint E + internal I), and positive recipients are actual ORIGINAL accepted GF5 seven-class sixsets from the SAME globally coherent pair injections f,g, if such data are available. W34/W38 BB-only is NOT a complete denominator.

## 1. Why D6-K's pair graph is insufficient

For each original incidence port e in active source universe I, N=|I|, w(T) the blocked-path source weight, K>=0 and d_A(e) the number of actual accepted sixsets containing e, define

    L(e)=sum_(T containing e) w(T);
    p_K(e)=2*L(e)-K*d_A(e);
    G=sum_(e in I) p_K(e);
    q(e)=N*p_K(e)-G,    sum_I q(e)=0.

For F subset I, define the **directed** ORIGINAL hyperedge crossing boundary

    b_dir(F)=sum_(0<|T intersect F|<3) |T intersect F|*w(T).

D6-K proved the *exact identity*

    6M(F)-K D(F) = (G*|F|)/N
                    + (sum_(e in F) q(e))/N - 2*b_dir(F),

where M(F)=sum_(T subset F) w(T) and D(F)=sum_(e in F) d_A(e). Unlike an undirected pair cut, b_dir charges 1 or 2 selected incidence ports of a crossing T distinctly. For source triple T crossing F in two ORIGINAL ports, the undirected pair cut weighs 2w(T), but 2b_dir weighs 4w(T).

## 2. NEW directed integer auxiliary network, exact dual and independent witnesses

Construct a finite directed network with ORIGINAL incidence vertices e and **one auxiliary vertex t for each ORIGINAL source triple**. Each original port e in T has:
- directed arc e -> t with capacity 2N*w(T);
- directed arc t -> e with capacity INF, where INF=1+sum_(e:q(e)>0) q(e).

Add source -> e arc q(e) for q(e)>0; e -> sink arc -q(e) for q(e)<0. The source and sink supplies balance exactly and every arc has an INTEGER capacity. For any s-t cut selecting original incidence set F on the source side, a crossing original auxiliary t **must** be on the sink side if even one e in T is unselected. Then exactly |T intersect F| arcs e->t cross, each of capacity 2Nw(T). If ALL three e in T are selected, t is moved to the source side for free; if none are selected, t remains sink-side at no cost. Consequently the minimum cut shortfall satisfies exactly

    E_dir = positive supply - maximum directed integer flow
          = max_(F subset I) [sum_(e in F) q(e) - 2N*b_dir(F)]_+.

This result holds for every finite original 3-incidence hypergraph, every integer K and every h. The maxflow reconstructs:
- on success: each positive integer e->t and t->e original incidence flow, conservation at t, exact q(e) divergences, e->t<=2Nw(T);
- on failure: the complete ORIGINAL incidence support F, its DIRECTED 3-port boundary and an independent exact arithmetic shortfall equal to the residual mincut.

A strict positive E_dir is a counterexample ONLY to this **uniform-centered directed calibration**, NOT to full original Hall, original D6-I uniform Hall, Branch A, or actual GF5 sixset geometry.

## 3. NEW quantitatively sharp relation to true original Hall

Recall exact original UNIFORM-port Hall deficit from D6-I/D6-K:

    Delta6(K)=max_(F subset I) (6M(F)-K D(F))_+.

By the identity, for all F

    6M(F)-K D(F) <= max(0,G) + E_dir/N.

Since Delta6 and max(0,G) are INTEGER,

    0 <= Delta6(K)-max(0,G) <= floor(E_dir/N).       (A)

In particular E_dir=0 is a CONSTRUCTIVE certificate that the true
original UNIFORM-port Hall network has NO extra local obstruction
beyond global active-source pressure G.

**Balanced-pressure exactness:** if the TRUE active-source global pressure G=0 (e.g. a particular integral K exactly balances the sum of active port capacities), then q(e)=N*p_K(e) and the identity above directly gives

    E_dir=N*Delta6(K).

This is a fully exact equivalence between directed centered hyperedge calibration and uniform-port Hall in the balanced case, rather than only a sufficient gate. An independent synthetic disconnected-source regression pins this arithmetic, without claiming such a balanced K exists in high-h genuine GF5 cases.

D6-K's centered UNDIRECTED pair-flow shortfall E_pair is

    E_pair=max_F [sum_F q(e)-N*B_pair(F)]_+,

and the original 3-port identity B_pair(F)<=2*b_dir(F) yields

    0<=E_dir<=E_pair.                                (B)

Thus directed calibration is NEVER weaker than pair calibration. It is **not equivalent** to the true Hall optimum in general (G*|F|/N can differ from G), and equation (A) may be strict. These exact distinctions are pinned in independent tests.

The conditional implication to the ORIGINAL full D6-F integer exception is

    D_full(K) <= floor(Delta6(K)/6)
              <= floor((max(0,G)+floor(E_dir/N))/6).

This is a sufficient upper bound only, not a lower bound on S or an automatic high-h positive-sixset expansion lemma. If all original positive recipient ports are active then G=6(C-KS), but on a coherently retained subgraph H one may have D(I)<6S.

## 4. Non-geometric strict separation, with exactly 3 source incidence ports

Synthetic T={0,1,2}, w(T)=4, K=1; 17 accepted sixsets all meet T only at incidence 2 (other five ports are fresh). Then L(e)=4, target degrees d=(0,0,17), signed pressure p=(8,8,-9), N=3, G=7 and centered q=(17,17,-34).

For F={0,1}, the PAIR model permits only N*B_pair(F)=3*(2*4)=24 but needs q(F)=34, so E_pair>=10. The faithful ORIGINAL 3-port directed boundary permits 2N*b_dir(F)=2*3*(2*4)=48, so no such obstruction exists. Direct exhaustive enumeration proves E_dir=0. Therefore the directed theorem succeeds while pair calibration fails, even though pointwise p(0),p(1)>0.

This example demonstrates mathematical necessity of preserving ORIGINAL 1-port-versus-2-port crossings. It is SYNTHETIC, not a genuine correlated GF5 original W(3,s) labeling.

## 5. Honest real W32 and all-h status

The GitHub-hosted contract compares ORIGINAL full-seven positive GF5 W32 lex/reverse/S68/S72 at K_full-1 and K_full. All original endpoints/labels come from the SAME actual complete globally coherent W32 model. The exact original W32 K values and complete S are lex (4,259), reverse (6,169), S68 (9,68), S72 (10,72), and nonzero D6-F integer exceptions at K-1 are 165,53,62,10.

This stage **must not** conclude that the directed calibration is universally successful from finite cases. It reports exact primal or dual per real map. An empirical successful certificate has no implication for all h; a failed directed-centered certificate is NOT a full Hall obstruction.

**Circularity gate:** D_A(I)=sum_(Q in A) |Q intersect I|<=6S, so any supposed independent bound D_A(I)>=c*s^6 already proves S>=c*s^6/6, the original Branch A scale. Neither D6-L nor the directed flow supplies a genuine all-h GQ seven-positive GF5 lower bound, a uniform K for arbitrary correlated original f,g, an o(s^6) high-h exception bound, Branch A/B or the ASET exponent.

## 5a. Hosted TRUE W32 directed transport result — two real pair bottlenecks eliminated

[GitHub-hosted D6-L Contract #38365828118](https://github.com/definitely-stable/Mathlab/actions/runs/38365828118) passed 5/5 focused test methods, including 48 deterministic synthetic three-port systems × four K (192 independently exhaustively enumerated support-mincut comparisons). Genuine complete positive seven-family same-map W32 results at K_full-1:

| TRUE ORIGINAL W32 | C | Complete seven S | K_full | True D6-F exception K-1 | Centered PAIR deficit E_pair | New directed original TRIPLE deficit E_dir | Nonzero integer triple-port primal flows |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| lex | 942 | 259 | 4 | 165 | 0 | **0 — CERTIFIED** | 148 |
| reverse | 898 | 169 | 6 | 53 | 0 | **0 — CERTIFIED** | 179 |
| S68 | 606 | 68 | 9 | 62 | 372 | **0 — CERTIFIED** | 123 |
| S72 | 658 | 72 | 10 | 10 | 1215 | **0 — CERTIFIED** | 180 |

**Main finite scientific observation:** S68/S72 strictly distinguish genuine directed ORIGINAL source-triple connectivity from any equal-pressure PAIR-graph circulation. In both cases the original-pair calibration has a mathematically valid positive mincut shortage, but a separately reconstructed and verified positive integer *directed three-port primal flow* routes all of the centered source pressure. This supports study of ORIGINAL oriented hypergraph expansion rather than undirected pair spectral expansion. It is NOT an all-h correlation-independent GF5 geometry result.

## 6. Exact hosted evidence and next gate

- [Algorithm](../../research/hyp105_issue230_d6l_directed_triple_calibration.py): ORIGINAL 3-port auxiliary directed integer maxflow, exact dual original F and b_dir(F), explicit integer primal port certificates, D6-K pair comparison, D6-I uniform Hall and D6-F exact exception checks.
- [Independent tests](../../research/test_hyp105_issue230_d6l_directed_triple_calibration.py): all ORIGINAL incidence subsets (not only source-closed ones) for 48 deterministic synthetic hypergraphs × four K, direct arithmetic of the directed dual, disconnected unsupported source controls, source-empty, strict pair-vs-hypergraph separation, and four TRUE original complete-seven W32 same-map comparisons.
- [GitHub-hosted dedicated workflow](../../.github/workflows/hyp105-issue230-d6l-directed-triple-calibration.yml): fail-closed exact primal/dual and W32 pinning, INDEX, Proof Audit, full Research separate.

**Next D6-M:** use actual ORIGINAL W(3,s) GQ incidence identities and GF5 seven-class positive conditions to control q(e) and true directed 3-port boundary on coherent PR394 retained H for ALL global correlated f,g, not by replacing the seven-class positive denominator with BB-only or reasserting general flow duality. Keep all research PRs Draft and issue #230/#176/#169 OPEN; main unchanged.
