# UCT-003 / TOM-006 — fixed finite q-gram budgets are arbitrarily weak (source-only COPY/ADD)

Date 2026-10-08. Parent [UCT-001 #74](https://github.com/definitely-stable/Mathlab/issues/74); supersets the q={1,2} weakness witness in [TOM-006](TOM-006-EARLY-KILL-GATE.md) **without changing its established proof or production model**.

**Status:** SELF-CONTAINED DERIVED_CLASSICAL / ADVERSARIAL GENERALIZATION / NO NOVELTY CLAIM / NO RUST. This is a negative theorem under a deliberately toy fixed-charge wire model, not a lower bound on actual VCDIFF bytes.

## Exact frozen model
Use TOM-006's source-only concatenation of nonempty `ADD(x)` (literal target bytes x) and `COPY(offset,length)` (a substring of old source B), no target self-copy, RUN, compressors or implicit zero-cost headers. Let L be total literal bytes and C the number of COPY instructions. Charge

    K(P) = L + #ADD_instructions + 2*C.

A COPY of any length costs two abstract units (NOT VCDIFF wire bytes). Define positional U_q(B,T) as the number of q-length target windows not appearing in B, where q>=1. Fix any finite maximum examined q=Qmax, independent of target length.

## Theorem — no uniform tightness for ANY fixed finite q maximum
For any integer r>=1 and every m>=1, choose an alphabet with distinct symbols a,b and

    B_(r,m) = (ab)^r  b^(2m)  (ab)^r,
    T_m     = (ab)^m.

Then:
1. |B|=2m+4r >= |T|=2m;
2. U_q(B,T)=0 for **every q from 1 through 2r**;
3. the q<=2r TOM-006 relaxed fixed-charge floor equals **2**, while the actual minimum parse cost satisfies

    4m / (2r+1) <= K*(B,T) <= 2*ceil(m/r).

Consequently K*/LB_(q<=2r) is unbounded as m→infinity for each fixed r, and for **any fixed Qmax>=1**, choose r=ceil(Qmax/2) to obtain the same divergence using all q<=Qmax.

**Proof.**
(1) follows immediately from lengths. For (2), q-length alternating substrings of T have at most two distinct phase patterns, one starting a and one starting b. For q<=2r, the first is a substring of (ab)^r and the second is a substring of b(ab)^r, which occurs at the junction of the long b-run and the second alternating block. Thus all target q-windows occur in B (not necessarily at different offsets), giving U_q=0.

Every substring copied from B to T must itself be alternating. In B, the longest alternating run has length at most 2r+1: the left (ab)^r has length 2r and is stopped by an adjacent b; the long b-run cannot contribute more than one b to an alternating substring; and at the right junction b(ab)^r has length 2r+1. Therefore each COPY in any valid parse supplies at most 2r+1 target bytes. For total target length n=2m we get 2m<=L+(2r+1)C. Since K(P)>=L+2C >= (2/(2r+1))(L+(2r+1)C), it follows that K(P)>=4m/(2r+1) for every parse. In the other direction, split T into at most ceil(m/r) contiguous alternating blocks of at most r `ab` pairs and COPY each block from the first (ab)^r: valid total cost at most 2ceil(m/r).

Because all U_q=0 and |B|>=|T|, the TOM-006 relaxation admits L=0, C=1 (optimistically copying all T in a single instruction), with optimistic floor 2. The nonempty T needs at least 2 toy cost units in any relaxed configuration, hence the relaxation returns exactly 2. Thus actual/relaxed ratio >=2m/(2r+1), unbounded for fixed r. For arbitrary fixed Qmax, take r=ceil(Qmax/2). QED.

## Scope / nonclaims
- The construction is a **negative** result about all **constant finite q window sets**. It does not exclude qmax growing with input, suffix-index-aware dynamic certificates, multi-scale string attractors, exact dynamic-programming lower bounds or different codec wire formats.
- It does not prove a general lower bound for RLE/VCDIFF/modern delta compressors, as target copy, run encoding, address-dependent encoding and compact length formats change the model.
- It does not prove a new named mathematical theorem. It is an elementary adversarial family extending the previous Mathlab q<=2 witness.
- The source is length-sufficient but a length-sufficient source cannot magically COPY an absent long alternating substring; the relaxation forgets this structural constraint.

## Falsification and independent exact oracle
`research/test_uct003_fixed_q.py` computes all source-substring memberships directly; independently optimizes ALL COPY/ADD parse choices by a suffix-position DP for small r,m; asserts absence of missing qgrams, both exact cost bounds and diverging ratio on larger symbolic cases. The executable finite test is a sanity-check and **not** the general proof.

## Research disposition and next step
**STOP** any claim that checking a fixed number of short q-length absent-window counts alone produces a uniformly tight patch-size certificate. **REOPEN** only for a theorem using a growing scale or stronger structure with proven *additional* information and fully charged preprocessing, or a model different from source-only COPY/ADD. This does not overrule other TOM-006 lines. For a new practical theorem, seek admissible bounds with guaranteed nontrivial tightness on an explicit workload *and* cheaper cost than reference encoding; compare known compressed matching and optimal parsing literature.
