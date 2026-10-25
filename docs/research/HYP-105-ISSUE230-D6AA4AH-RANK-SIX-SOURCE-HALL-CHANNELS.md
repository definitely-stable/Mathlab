# HYP-105 / issue #230 — AA4-AH: exact rank-six genuine ORIGINAL two-triangle Hall kernel

**Status:** research-only, restricted exact all-h theorem, strict child of [AA4-AG PR #516](https://github.com/definitely-stable/Mathlab/pull/516) at parent SHA \`5bb081e43bf0e091089adf0b176b7bcfea2f9c0e\`. This does **NOT** establish Branch A/B/C, all-map Hall-positive density, a full R3/ASET bound, or an exponent improvement. Original source W(3,s), s=2^h>=2, TWO complete globally injected original typed physical pair maps f and g, and six DISTINCT real original incidence IDs are mandatory. This is not a random-per-Q sampling model.

## 1. Motivating verified all-map AG result and exact new target

AA4-AG proved that for **every** pair of globally injected f,g and every s=2^h>=2^19, the number of INDEXED original p+two-flags, first-side occupied physical C4 and opposite-side occupied physical disjoint two-triangle A candidates before the genuine original source-Hall gate obeys P_triangle(f,g)>=s^14/256.

The missing step is NOT physical occupancy. An actual W(3,4) random globally injected map has 438 physical two-triangle completions from six selected C4 under one pinned original line-root pair but zero genuine original accepted Q due to 438 original singleton-row Hall deficits. Other original flags, roots and GF5 tags can compensate. Any global S=o(s^6) would require an extremely sparse genuine Hall-positive fraction among the AG indexed pre-Hall family.

AA4-AH replaces the four-by-four permanent/15-Hall-subset evaluation for **each** physical two-triangle H with an EXACT six-channel physical-coordinate-set formula. The formula makes globally correlated overlap measurable without assuming independence and gives an explicit bilinear contraction for future JPKC/EICE research.

## 2. AA4-AH1 theorem: EXACT six 2-by-2 rook channels over TRUE ORIGINAL GQ

Fix s=2^h>=2, genuine original W(3,s), arbitrary complete globally injective physical point f and line g. Choose a REAL original point p, two DISTINCT REAL incidence IDs (p,l0),(p,l1), and one OCCUPIED complementary physical point-C4; its four occupied physical edges inverse-map under f to four distinct original points (q0,q1,q2,q3), none equal p.

Let the pinned opposite physical images under the one global g be e0={u,v}, e1={w,x}. If these overlap physically then there is no disjoint physical two-triangle completion and the claimed count is zero. Otherwise their endpoints are four different physical coordinates. Define the ACTUALLY occupied auxiliary site sets:

Y={y not in {u,v,w,x} : {u,y} AND {v,y} in im(g)}
Z={z not in {u,v,w,x} : {w,z} AND {x,z} in im(g)}.

For any two distinct row IDs i,j, and y in Y, let L_{ij}(y) be the permanent of the 2x2 **TRUE ORIGINAL source incidence matrix** whose two rows are qi,qj and whose two columns are the actual original line factors g^-1({u,y}),g^-1({v,y}). Because true original generalized quadrangle forbids SOURCE four-cycles, this 2x2 permanent lies in {0,1}, not {0,1,2}; two different 2-rook matchings would be an original C4. Define the physical-coordinate set Y_{ij}={y in Y:L_{ij}(y)=1}. Define Z_{ij} analogously using g^-1({w,z}),g^-1({x,z}) for z in Z.

For every S subset {0,1,2,3} of size 2, write Sbar for its complementary row pair. Then the number T_triangle of **distinct actual original six-incidence-ID Q** accepted by first-side physical B, opposite-side physical TWO DISJOINT TRIANGLES A, and this one pinned exact original root/C4 cohort is EXACTLY:

    T_triangle = SUM_{S in binom([4],2)}
                      ( |Y_S| |Z_Sbar| - |Y_S intersection Z_Sbar| ).

All SIX summands are NONNEGATIVE integers. The second term is not an asymptotic correction: y=z would create a FIVE-physical-coordinate vertex union, hence INVALID for the accepted six-coordinate GF5-A class, even if all SIX opposite physical edges are globally occupied. Every valid y!=z is a unique disjoint two-triangle physical-A completion. The two left original singleton flags consume the rows S; the two right consume Sbar. The 2x2 permanents assign distinct actual original line columns inside each triangle. Combining them yields exactly one of the original four-source perfect matchings. Conversely every accepted Q splits uniquely into its two left and two right original source-row assignments.

**Exact deterministic positivity criterion:** T_triangle>0 iff for some S the Cartesian product Y_S x Z_Sbar contains at least one OFF-DIAGONAL pair (y,z), y!=z. Equivalently both sets are nonempty and are NOT the identical singleton set. No probabilistic or conditional expectation is involved.

This is a complete **single-cohort Hall criterion**, not a guarantee that it is ever positive in each original rootpair. A local zero is compatible with full all-root original positive GF5 mass.

## 3. AA4-AH2: the ABSTRACT full 8-bit-signature kernel has EXACT rank SIX

For any abstract two-sided 8-bit signatures sigma,tau in {0,..,255}, encode four rows each with two candidate columns per side. Let K(sigma,tau)=per(M(sigma,tau)), where M is the four-by-four binary matrix with the first two columns from sigma's two-bit row entries and the last two from tau's two-bit row entries.

**Universal 4x4 permanent Laplace identity (no GQ assumption):**

    K(sigma,tau)
      = SUM_{S in binom([4],2)}
          per(M_left[S,{0,1}]) *
          per(M_right[Sbar,{2,3}]).

Every summand separates as a function of sigma times a function of tau. Thus rank_Q(K)<=6, even though K has 256x256 entries and potentially value 24 in the unrestricted abstract matrix class.

To prove rank_Q(K)>=6, choose six left signatures sigma_S, one for each row pair S, with EXACTLY ONE occupied entry in each of the two rows S assigning those rows bijectively to the two left columns, other rows empty. Choose six right signatures tau_T for complementary rows Tbar, similarly assigning them bijectively to the right columns. Then the 6x6 submatrix [K(sigma_S,tau_T)]_(S,T) is EXACTLY I_6, since when S!=T at least one row lacks every candidate column. Therefore:

    rank_Q(K) = 6   (EXACT, independent of s,a and global maps).

This rank-six theorem belongs to the abstract 4x4 permanent with a 2+2 column partition; do NOT claim the Laplace expansion itself is a new mathematical discovery. The novel application is the exact finite-rank, occupied-physical-diagonal-corrected reduction of TRUE ORIGINAL GF5 B/A Hall transfer. The complete 65,536 (sigma,tau) abstract combinations are independently checked against direct 24-permutation permanent, and the explicit I6 witness is tested.

**Crucial scope:** a generic signature K entry can have permanent up to 24; only physically realized pairs generated by the genuine original source geometry and four distinct opposite factors are constrained to permanent 0/1/2 by AA4-AE. Do not apply true GQ girth-eight permanent bounds to all abstract 256x256 entries.

## 4. AA4-AH3: deterministic six-channel density/barrier target

For any complete global f,g and actual source-C4 cohort, six set-intersection formulas count precisely accepted original GF5 two-triangle Q without enumerating all O(a²) physical auxiliary site pairs, all original 4x4 Hall matrices, or the original perfect-matchings explicitly. Construction cost for six row-pair sets is O(a) physical-site scans with 6 two-row incidence checks; intersection products cost O(a). The source original C4 enumeration itself is NOT O(a); scope this improvement to evaluation of a specified cohort.

Aggregate over all actual source roots, two DISTINCT original flags and occupied physical C4s without orbit quotient. The resulting sum is exactly the restricted T_triangle(f,g)<=C_BA(f,g)<=S_s(f,g). From AG:

    if S_s(f_s,g_s)=o(s^6)
    then [sum over S,roots,C4 off-diagonal six-channel pairs] / P_triangle(f_s,g_s)
         = o(s^-8).

Conversely a uniform >=c/s^8 Hall-positive fraction among P_triangle physical candidates would suffice for Branch A. AA4-AH does **not** prove this density lower. The six-channel formula isolates a concrete JPKC/EICE target: show that global source-incidence/physical-label constraints force sufficient matching between six genuine occupied auxiliary site sets in aggregate, or exhibit an actual infinite globally injected all-class failure. A zero single-rootpair is not a counterexample to the global lower.

## 5. Independent verification and falsifiers

- Exact complete 256x256 abstract signature pairs: independent literal 24-permutation 4x4 permanent vs six independently evaluated 2x2 Laplace products (including abstract permanent 24), plus the exact rational rank-six I6 minor.
- True ORIGINAL W(3,2) source flags on both typed sides in real globally complete S68, S72, lex, reverse mappings, with no fake per-Q map redraw. Compare accepted Q of each selected original-C4 cohort to the *independent earlier* AG actual two-triangle 4x4-girth-eight Hall oracle. Count full W32 two-triangle source subset across ALL 15 true original point roots, ALL 15 line roots and all three actual flag pairs per root; compare with prior AA4-AE whole physical A GF5 B/A totals 44/21, 36/31, 98/110, 77/74 respectively (subclass must be <=full count).
- True ORIGINAL W(3,4) lex and random globally complete but non-surjective physical injections (a=14,K=91,V=85,m=6). Two typed source root orientations. Independently literal (y,z) x 24 source four-matching enumeration vs six-channel products, and strict cross-check with AG physical-C4+Hall enumeration.
- Actual common-source geometry and independent point/line physical relabeling invariance for a fixed selected original C4; invalid source and abstract-signature domains rejected.
- Eight independent regression tests and dedicated GitHub-hosted CI. The hosted CI tests must be checked on the EXACT final PR HEAD; unit tests and Proof Audit alone are NOT independent mathematical acceptance.

### Entire genuine W(3,2) triangle-A subtype, all original roots (GitHub-hosted initial run)

Using the full 15 actual original point roots / 15 line roots, every three pairs of two distinct real original flags through each root and **all three** physically occupied complementary C4 per original root, the exact six-channel formula yielded:

| Complete global source labeling | B(point)/A(line) two-triangle only | A(point)/B(line) dual two-triangle only | Full historical B/A | Full historical A/B |
|---|---:|---:|---:|---:|
| S68 | **1** | **0** | 44 | 21 |
| S72 | **1** | **2** | 36 | 31 |
| lex | **3** | **12** | 98 | 110 |
| reverse | **2** | **4** | 77 | 74 |

All numbers count six DIFFERENT actual original incidence-ID Q, not signed GF5 event counts or source automorphism orbits. The two-triangle family is a strict subclass of the physical A sector of 70 total accepted 6-coordinate 2-factors (10 two-C3, 60 C6 on a fixed six-physical-coordinate vertex set). Hence it is expected to be much smaller for these finite labeling instances. This table is from the first hosted successful W32 job of [AA4-AH dedicated run #38763145628](https://github.com/definitely-stable/Mathlab/actions/runs/38763145628); the initial run had an unrelated physical C4 *ordering*-sensitive fixture check in the W34 relabel-invariance test, which was fixed by validating the set of four actual original source factors rather than the physical-enumeration order. The full eight-test final HEAD must still pass.

**Importantly:** S68 has ZERO genuine original dual two-triangle A/B Q over ALL actual original line roots, but has 21 accepted dual A/B in the full original GF5 class. Thus claiming that *this restricted subclass by itself* has positive all-map mass on every finite original root or typed side is false. No conclusion follows about large-h full-seven-class obstruction without additional proof.

## 6. Integration protocol

Strict Draft child on AA4-AG PR #516. Maintain parent/child merge chain; do not merge to main, register accepted claims in RCP JSON or hand edit generated five Markdown registries until all exact-HEAD dedicated/INDEX/Proof Audit/Full Research checks and an independent mathematical referee. The parent AA4-AF and AA4-AG Full Research runs are CANCELLED, not SUCCESS, and must be treated as acceptance blockers. Main issue #230 remains OPEN; no Branch A/B/C, full seven-GF5 all-h or R3/ASET result is claimed.
