# GIO-001.3 / G6-C2 — intrinsic FULL-A/CORE-C books and partial-projection BBo inverse

**Parent** [#793](https://github.com/definitely-stable/Mathlab/issues/793), **research meta** [#790](https://github.com/definitely-stable/Mathlab/issues/790), **stacked prerequisite** G6-C1 [PR #802](https://github.com/definitely-stable/Mathlab/pull/802) exact `8932e4c76c2d04c3e1c15f7f56f15a50a7d8f918`. This slice carries forward its **intrinsic**, without GQ-witness, structural setting and adds local **A5 mixed books and A6 partial-projection lift**. It does NOT claim the full T3 obstruction or change the original HYP-105/ASET exponent.

## 1. Domain and quantifiers

Let `I subset P x L` be any **simple**, finite, (s,t)-biregular original source incidence graph with girth >=8; `s,t>=2`. The source may be disconnected or non-GQ and need not have all unique full projections. Let `f:P->binom([aP],2)` and `g:L->binom([aL],2)` be arbitrary fixed complete separately injective point/line physical pair maps (minimal alphabets when invoking the G6-C1 asymptotic spectral bounds). The maps may be arbitrarily correlated with the source, original flag deletions or core selection.

Let `A subset I` be the actual **FULL surviving original source flags** after any adversarial deletion; let `C subset A` be an **arbitrary retained CORE**. Original source factor names and **original FULL projection table** remain frozen from I. A nonincident `(q,r)` has at most one three-flag path by original girth eight, and it is either present in I or missing forever in this frozen table. We do not recompute projections after source deletion and do not fill missing pairs with any GQ completion.

All historical D6 and B/B-overlap sixsets use six distinct **original named flag IDs**, not abstract point/line triples or physical graph edges. The latter can be used to reconstruct genuine original sixsets only when all their original flags survive in A.

## 2. Theorem M — FULL-A/CORE-C mixed book bound without GQ

For the point factor, let `c_x(p)=|{q in P: q original-collinear with p, x in f(q)}|`. For each second-symbol y, let

`R_A(p,y)=|{(p,r) in A:y in g(r)}|`,
`R_C(j,y)=|{(j,m) in C:y in g(m)}|`.

Define the **actual mixed book** `K_AC(p,j)=sum_y R_A(p,y)R_C(j,y)` and the original source book

```
B_x = sum_(j in P) sum_((x,k) oriented f(j))
      sum_(p: k in f(p)) c_x(p) K_AC(p,j).
```

Let `J_C` be the actual **original named flag conflict graph** on C, with an edge between flags sharing an original point and at least one g symbol, or sharing an original line and at least one f symbol; suppose `Delta(J_C)<=K`. Define the actual physical simple graphs H_A and H_C consisting only of diagonals of owners in A and C; denote `Delta_C=max_v degree_HC(v)` and `N_A=|A|`. Pair injectivity makes each physical edge have exactly one named source owner.

Put `G_f=sum_(x,p) c_x(p)^2`. Then

```
B_x^2 <= 16 (t+1) (K+1) N_A Delta_C G_f,
B_y^2 <= 16 (s+1) (K+1) N_A Delta_C G_g.
```

**Proof, with literal full/retained distinction.** Apply Cauchy over index quadruples `(j,(x,k),p)`: `B_x^2<=F1 F2`, where `F1=sum c_x(p)^2` and `F2=sum K_AC(p,j)^2` over exactly these indices. For fixed `(x,p)`, there are at most TWO k in f(p), and for each k there is at most one j whose pair label is {x,k}, by injectivity. Hence `F1<=2G_f`.

For each `(j,y)`, all C flags counted in `R_C(j,y)` share original point j and physical line-symbol y. They form a clique in J_C. Therefore `R_C(j,y)<=K+1`. Also `sum_y R_A(p,y)=2 degree_A(p)<=2(t+1)`; hence `K_AC(p,j)<=2(t+1)(K+1)`. As K_AC nonnegative, `F2<=2(t+1)(K+1) sum K_AC`.

Reindex the **same full/retained sum** by physical corners `(k,y)` to obtain the exact identity

```
sum_(j,(x,k),p) K_AC(p,j)
  = sum_(k,y) degree_HA(k,y) degree_HC(k,y)
  = Theta_AC.
```

There are four source corners per original flag, so `Theta_AC<=4 N_A Delta_C`. Multiplying the bounds proves the displayed point book. Swapping original points and lines proves the dual **separately**, with `s+1` rather than blindly reusing `t+1`. None of this invokes a GQ projection axiom or an SRG identity.

For a complete minimal physical map and the **fixed-b, fixed-C linear Moore excess** source family of G6-C1, its intrinsic corrected Gram bound gives `G_f,G_g<=G0(b,C) r^(11/2)`; `N_A<=n0(b,C)r^4` with `n0=(b+1)v0` and `v0=(b+1)(b²+1+C)`. Under the actual LOW core degree cap `Delta_C<=T r` and actual conflict cap `K` (fixed, independent of r), we obtain

`B_x²,B_y² <= 16(b+1)(K+1)n0 T G0 r^(23/2)`.

Thus the needed mixed-book *scaling* holds intrinsically. The separate **three-corner path-to-book injection** and fourth-moment application from #230/#799 are to be audited before declaring the full LOW error proved; a book bound by itself is **not** the entire four-blocker argument.

## 3. Theorem I — genuine original BBo reconstruction from PARTIAL projections

For any actual proper directed length-three physical walk `v0,v1,v2,v3` in H_C whose four first coordinate symbols are pairwise distinct and whose four second coordinate symbols are pairwise distinct, decode its endpoint point and line factor labels from `{x0,x3}` and `{y0,y3}`. If both original factor labels exist, they define **unique original factor IDs** `q,r`.

Require all of the following *literal* conditions:

1. The pair `(q,r)` has an existing, originally **unique** length-three projection `(q,ell),(p,ell),(p,r)` in I. (A missing original projection is REJECTED, not completed.)
2. All three original anchor flags belong to FULL A; the physical walk's three actual residual source owners belong to CORE C.
3. The four physical first symbols avoid both symbols in `f(p)`, and the four physical second symbols avoid both symbols in `g(ell)`. The residual owners are all distinct, and each of the six total named source flags is distinct.

Then the six named original flags are exactly a historical B/B-overlap structural sixset with repeated original point p and repeated original line ell sharing the old middle original flag (p,ell). Its physical path is an actual, **aligned produced BBo** witness, not merely an abstract overlap. Conversely, its original-owner source inverse reconstructs exactly the two reverse directed physical three-walk orientations. This is a literal local six-column factor-label proof: no GQ full-projection axiom beyond the *one existing frozen projection* and no field operations occur.

For *any* original biregular girth-eight I, full A and core C, the certified set of sixsets produced by this partial-projection rule is recovered by three independent algorithms: physical-first proper threewalk census, explicit literal source/anchor classifier, and middle-original-owner source-first join. These sets agree exactly, and every sixset has **two** oriented reversed threewalks.

The theorem does **NOT** assert that most candidate physical threewalks are eligible. In particular when `Delta_L>0`, `|P| Delta_L` original nonincident endpoint pairs have NO original 3path, and they cannot be counted as BBo.

## 4. Theorem E — expanded intrinsic endpoint error mask

For the fixed source I, let `V_P=|P|,V_L=|L|, N=|I|`; let the minimal physical alphabets have `M_P=binom(aP,2)-V_P` and `M_L=binom(aL,2)-V_L` missing factor pairs. For ANY adversarial A=I\Z, classify each ordered physical endpoint pair with distinct x and y symbols by precedence: missing factor label; original incident (q,r); nonincident but originally projectionless; original projected with outer factor-label intersection `f(q)∩f(p)!=empty` or `g(r)∩g(ell)!=empty`; projected/outer-clean but at least one frozen original anchor deleted; otherwise good. These six classes form an exact exhaustive, disjoint partition.

With `e_col,P(f)` and `e_col,L(g)` counting original source collinearity factor-symbol conflicts, the union of the five bad classes is bounded by

```
E_bad <= 4(M_P V_L+M_L V_P+M_P M_L)
       + 4N + 4 V_P Delta_L
       + 8t e_col,P(f) + 8s e_col,L(g)
       + 12 s t |Z|.
```

**Why:** first term counts unavailable typed factor pairs; second counts literal original incident pairs; the new third term is EXACTLY four orientations for each missing original projection (G6-C1, no GQ axiom). Every source-collinear point pair (q,p) sharing an f symbol can be the unique projection foot for at most t nonincident r, and dual for lines; each unordered collinear conflict has two q/p orders, four endpoint orientations, hence the conservative 8t,8s. Every deleted source flag lies in exactly 3st frozen existing projections, giving ≤12st|Z| ordered endpoint orientations. Adding these individual upper bounds handles overlaps automatically; the literal precedence partition used by the code never double-counts an actual endpoint.

For fixed b,C linear excess, the extra `4 V_P Delta_L=O_b,C(r^4)` is *subleading* compared with original O(r^5) endpoint geometry/label defects. Thus the endpoint estimate required by the classic LOW proof is stable for this restricted intrinsic family, with an explicitly new Moore-hole term. For `Delta_L=O(r²)` this new term alone is still O(r^5), but **A1 conflict bounds at that weaker excess have NOT been proved**.

## 5. Exact independent falsifiers and limits

- `research/gio_t3c2_partial_books.py` builds only **original incidence lines** of genuine small W32/W33/GQ(2,4)/dual(4,2) and original non-GQ disconnected/connected switched double-W32 girth-eight sources. It accepts independent lex/correlated factor maps and arbitrary nested masks A,C, computes exact non-GQ source partial projections, literal FULL/core mixed flag books and symbolic physical degrees; tests independent original-source original owner conflicts. The partial produced inverse is independently enumerated with full original flags, not a GQ completion.
- `research/test_gio_t3c2_partial_books.py` independently brute-counts literal mixed book terms and physical corner degree products, enumerates all original source endpoint orientation classes without shared production classifier, exercises adversarial masks and empty CORE, checks each sixset against independent physical-first, middle-owner-source-first, and historical original source inverse routines. Checks unequal s/t (dual), actual graph with Moore holes, correlated f/g.
- `.github/workflows/gio003-g6c2-partial-books.yml` GitHub-hosted Python 3.12 and JSON certificate. Built as a **stacked Draft** based on exact G6-C1 PR #802 head to avoid copying/rewriting its not-yet-merged code; new changes are exclusively the 4 G6-C2 files. No upstream main changes.

**Acceptance:** all exact-head specialist, full Research and INDEX gates green; independent internal critical mathematical review of the three local lemmas and quantifiers. This is not an external human referee or Lean proof.

**STOP:** G6-C2 proves *local* A5 book scaling, A6 partial projection reconstruction, and an intrinsic endpoint error inventory; it is not a complete global A4/A5/A6 LOW sixset supersaturation theorem. The shared global selector and its moment controls, the triple-to-book blocker completion bound with a common retained CORE, and resulting HEAVY/LOW alternative have **not** been rerun as an integrated all-order non-template proof. No new unrestricted ASET exponent or external numeric Simonovits constants are claimed. Parent #793 remains OPEN. Next G6-C3 should integrate these sharp local gates into the accepted #799 HEAVY/LOW calculus with a completely explicit fixed-(b,C) parameter ledger and rigorous comprehensive proof review.
