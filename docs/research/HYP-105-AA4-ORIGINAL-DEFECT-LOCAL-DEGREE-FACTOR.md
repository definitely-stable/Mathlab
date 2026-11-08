# HYP-105 / #230 — AA4-DEGFACT: exact local degree theorem and converse to mixed STAR deletion

Scientific Draft, strict child of [#747](https://github.com/definitely-stable/Mathlab/pull/747) at frozen SHA fc4f241cdf278f4d74156435fcb05a02e4fb336e. No parent/main mutations, no merge, no issue closure, no ASET exponent. Root status: OPEN_WITH_FORMAL_BLOCKER.

## 1. All-h theorem with exact original incidence-ID quantifiers

Fix any s=2^h, h>=1, the TRUE symplectic generalized quadrangle W(3,s) of order (s,s) and its named ORIGINAL point-line incidence IDs I. Let Z be ANY subset of I, chosen adversarially, including after seeing two arbitrarily correlated complete globally pair-injective physical maps f and g. Define deletion degrees d_Z(p) and d_Z(ell) by the number of deleted original flags through an original point p or line ell respectively.

The predecessor #747 defined D_Z as the number of genuine nonincident original pairs (q,r) whose UNIQUE FULL original GQ projection q--ell--p--r has its MIDDLE ORIGINAL flag (p,ell) in Z while BOTH outer ORIGINAL flags (q,ell),(p,r) avoid Z.

**NEW unconditional, exact all-h local-degree factorization:**

\[
\boxed{D_Z=\sum_{(p,\ell)\in Z}
(s+1-d_Z(p))(s+1-d_Z(\ell)).}
\tag{DF-1}
\]

No physical labels, probability, averaging over f/g, sixset multiplicity, GF(5) events or coordinate automorphisms enter this formula. Each deleted middle flag is counted ONCE.

### Bijection proof

Fix a deleted genuine original middle flag (p,ell). The first outer anchor is retained precisely when q is among the s other original points on ell whose flag (q,ell) is not deleted. There are s+1-d_Z(ell) choices. Independently, the last outer anchor is retained precisely when r is among the s other original lines through p whose flag (p,r) is not deleted. There are s+1-d_Z(p) choices.

For every such pair (q,r), q is NOT incident with r: otherwise two distinct original points p,q would lie on both distinct original lines ell,r, a prohibited incidence 4-cycle in the genuine generalized quadrangle. Its unique full GQ projection is necessarily q--ell--p--r, because that valid 3-path exists and the GQ axiom guarantees uniqueness. Conversely every isolated-middle projection with this named middle flag arises from exactly one such choice of q and r. Multiply the independent *combinatorial choices* (NOT independent physical maps or random events), then sum over distinct deleted middle original flags. This proves DF-1 for all h, including empty and complete Z.

### NEW inverse / precise structural classification

A point STAR I(p) is complete in Z iff d_Z(p)=s+1; similarly a line STAR I(ell) is complete iff d_Z(ell)=s+1. Every summand in DF-1 is nonnegative, and it vanishes iff the deleted middle flag belongs to at least one complete point or line STAR. Thus:

\[
\boxed{
D_Z=0\quad\Longleftrightarrow\quad
Z=\bigcup_{p\in P_0}I(p)\ \cup\
\bigcup_{\ell\in L_0}I(\ell)
\text{ for some original points }P_0
\text{ and lines }L_0.
}
\tag{DF-2}
\]

Proof of the converse: when D_Z=0, every deleted flag is covered by at least one full STAR. The union of all those full STARs is contained in Z by definition and covers all of Z, hence equals Z. The forward direction is the previously known #747 mixed-STAR closure. Empty STAR collections and overlaps are allowed. **No other original source deletion pattern has D_Z=0.** For a non-STAR Z, D_Z is a positive integer, but no uniform positive fraction of s²|Z| follows from that fact.

## 2. Exact computable predecessor interface, no extrapolation

Keep the predecessor #747 ORIGINAL FULL-GQ source projection identities without alteration, with H_Z counting all-three-anchor deleted projections and F_Z both-outer-deleted/middle-retained projections:

\[
M_Z=8s^2|Z|+4D_Z-4H_Z-4F_Z
\le8s^2|Z|+4D_Z.
\tag{DF-3}
\]

M_Z is the number of oriented typed physical endpoint pairs masked by Z *before* other non-Z geometric defects; every true original nonincident (q,r) has exactly four physical orientations. Inserting DF-1 gives the NEW exact local-degree upper certificate

\[
\boxed{
M_Z\le8s^2|Z|+
4\sum_{(p,\ell)\in Z}
(s+1-d_Z(p))(s+1-d_Z(\ell)).
}
\tag{DF-4}
\]

For Z nonempty, the exact effective defect fraction is

\[
\kappa_{\mathrm{eff}}=\frac{D_Z}{s^2|Z|}\in[0,1].
\]

The local formula makes this computable by counts of the deleted source IDs. With a prevalidated original source flag table, construction of deletion degrees and summation is O(|Z|); the provided strict module revalidates its input in O(|I|) each call, so its total call complexity is O(|I|+|Z|). Full source projection enumeration instead scans V(V-s-1) nonincident pairs, which is Theta(s^6). The degree-only procedure supports a constant-time-per-deleted-ID contribution and an explicit human-auditable kappa certificate.

If a full all-h HEAVY/LOW predecessor dependency DAG and the existential published ordinary C6 supersaturation theorem are separately accepted, #747's conditional fixed-kappa deletion radius applies unchanged:

\[
\rho_\kappa=
\frac{t_\star^2}{(8+4\kappa)q_3^2L_6}
=\frac{3}{2+\kappa}\rho_{\rm arbitrary}.
\tag{DF-5}
\]

This slice does **NOT** increase the radius, prove any new S_s lower, recertify the 18 inherited original-source HEAVY/LOW obligations, provide numerical external C6 constants, or prove a new ASET exponent. It upgrades the *kappa=0 classification* from sufficient to necessary-and-sufficient and makes any fixed kappa qualification exact via local original source data.

## 3. Independent genuine symplectic finite falsifiers

New self-contained research/hyp105_original_defect_factor_referee.py constructs true W(3,2) and W(3,4) directly from projective one-spaces in GF(s)^4 and totally isotropic two-spaces for the alternating symplectic bilinear form. GF(4) arithmetic uses the irreducible x²+x+1 polynomial. The main module does not import original Mathlab symplectic fixtures, #747 projector, signed GF(5) flow, HEAVY/LOW routines, physical map optimizers, or previous deletion code.

It compares TWO independently written methods: (a) the degree-only factor sum and full-STAR decomposition; (b) full nonincident (q,r) projection reconstruction, checking all three exact original role exposures s² and the independent D/H/F/M identity. The second oracle never invokes the first.

The ten strict independent tests include true W32/W34 source cardinalities, mixed incident and nonincident complete STAR unions, incomplete point pencils, singleton original ID saturation, full and empty Z, full point STAR plus one extra ID, deterministic adversarial deletion masks, ALL 990 W32 two-original-ID deletions with 27 independent projection comparisons, original ID permutation, point/line duality, bad input and duplicate-source fail-closed checks. A unique JSON certificate records 33 genuine original-source masks across W32 and W34. GitHub-hosted Ubuntu 24.04 Python 3.12 specialist workflow requires all ten tests and exact JSON invariants, plus independent INDEX and full Research exact PR-head CI review.

## 4. Scientific acceptance boundary

(DF-1) and (DF-2) have elementary all-h proofs (not finite-h interpolation), and the independent computational oracles are deliberate falsifiers. All seven original six-incidence-ID accepted classes remain as defined in root #230; this slice neither changes nor re-counts them. This is a scoped theorem, NOT PROVED_A, COUNTEREXAMPLE_B, RESTRICTED_THEOREM_C, or an accepted overall proof.

The most valuable next mathematical acceptance action after this slice is an independent line-by-line source proof DAG audit of the inherited HEAVY/LOW global obstruction, including the candidate original D6 0/1 and physical-produced BBo 0/2 six-ID inverses from #734, the GF(5) exact weights from #735/#741, and the precise class inclusion/quantifier dependencies in #743–#747. Independent verification of the published ordinary C6 supersaturation statement's normalization is also necessary. Do not duplicate #734's finite enumeration, and do not merge the scientific stack purely because CI is green.
