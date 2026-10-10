# HYP-105 B3.2-E1-C13 — simultaneous original GQ and BOTH physical-side orbit reduction

Date: 2026-10-11. Parent issue [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked on #291 C12 after #288 C11 and the prior C1–C10 chain. Parallel C7-B PR #280 is NOT an ancestor.

**TYPE: EXACT ALL-h GROUP-EQUIVARIANCE THEOREM + FINITE GENUINE W(3,2) Sp(4,2) JOINT ORBIT/STABILIZER/CANONICALIZATION ORACLE.** This is a true reduction of the **JOINT** original-GQ incidence graph, injective left physical labels, and injective right physical labels. It DOES NOT prove a positive all-f,g Ω(s^6) seven-family lower or any new ASET exponent. Full finite exhaustive optimization over all equivalence classes is explicitly NOT claimed.

## 1. Deep C12 audit and research decision

C12's exact physical Aut(F_R) quotient removes right-coordinate relabel duplicates for ONE fixed left f and right occupied F_R, but cannot by itself optimize over **every left physical pair-label assignment**, and it never reduces the symplectic **original point/line incidence graph**. C11/C12 W32 gives an honest joint right-map counterexample to treating a frozen original prefix as universal: original B/A 77, a legal transformed right map 56, seven classes 169→141, and for fixed original f and full right F_R the all-g certified B/A minimum is only in [0,56]. Even its C11 conditional variance gives lower42 only for a fixed 11-right-pin prefix, not the entire right-map space.

Remaining viable approaches were compared:
- More independent or low-pin sixset rearrangements: **rejected** as primary approach, because C9–C10 rigorously force this exact relaxation to zero for <=3 pins at all s>=16.
- More independent moment assumptions for different original doubled-point pairs: **rejected**, since C11 requires ONE shared right map and C4's separate conditional experiments cannot be combined as an all-g bound.
- Exhausting all left and right maps naively: **rejected**, for W32 it involves (15!)² mapping pairs even at fixed K6 palettes.
- An exact JOINT quotient preserving original GQ structure and BOTH physical halves: **selected**. It is model-preserving, gives an independent finite acceptance oracle, admits a canonical representative and exact stabilizer, and sets up future all-f,g reduction without false positive asymptotics.

The current phase first establishes the equivalence relation and executable proof obligations. It does not assert the quotient alone makes the full exact search feasible.

## 2. All-h three-group equivariance theorem

Let s=2^h, original symplectic W(3,s) with ORIGINAL point set P, ORIGINAL line set L, and incidence set I⊂P×L. Let f:P→F_L⊆E(K_{a_L}) and g:L→F_R⊆E(K_{a_R}) be arbitrary legal injective physical pair-edge maps. The physical alphabets need not be equal or complete. Define the independent physical-coordinate stabilizer groups H_L=Aut(K_{a_L},F_L) and H_R=Aut(K_{a_R},F_R). Define Γ=Aut(P,L,I), the *part-preserving* original GQ incidence automorphism group. Interchanging original point and line parts by a duality is NOT included, since the seven classes distinguish left and right.

For σ=(σ_P,σ_L)∈Γ, h_L∈H_L, h_R∈H_R, define the **simultaneous** transport

    f'(σ_P(p)) = h_L(f(p)),
    g'(σ_L(l)) = h_R(g(l)),

where each h_i acts on a physical pair edge via its endpoints. The new f',g' are honest legal injections into the SAME respective occupied F_L,F_R, and (σ_P,σ_L) maps every ORIGINAL incidence (p,l) to exactly one ORIGINAL incidence.

**Theorem (all h, every legal f,g):** the complete seven-class original six-incidence motif count VECTOR, its sum S_seven and its accepted GF5 necessary-floor numerator are exactly invariant under this triple action. Reason: σ bijects actual original incidence columns; each physical h_i is a coordinate permutation, preserving distinctness, degree profiles, physical cycles, and other named six-edge physical graphs for every incidence subset. Thus the motif class of every original six-incidence set is preserved under the simultaneous transformation. No single motif is allowed a separately chosen σ or h.

An even stronger statement holds for the actual GF(5) selected support matrix under a consistent column permutation plus global left/right coordinate-row permutations: these operations do not change its linear dependencies or the full risk. This is a classical row/column permutation invariance, NOT a new estimate of full R3. The executable C13 acceptance tests concern the exact seven-class vector and necessary-floor numerator; they do not compute entire GF5 R3.

Let H_L^edge and H_R^edge be the **images on actually occupied physical pair-edge labels**, deduplicated if physical-coordinate permutations act nonfaithfully (e.g. isolated coordinates). The finite group G=Γ×H_L^edge×H_R^edge acts on the set of legal pairs (f,g) with the FIXED physical occupied images F_L,F_R. It partitions all such pairs into genuine equivalence classes. Consequently

    inf_(ALL legal f,g into fixed F_L,F_R) S_seven(f,g)
      = inf_(ONE representative per G-orbit) S_seven(f,g).

If images F_L,F_R vary, this statement must be applied across their permitted physical graph isomorphism types; a fixed-F equivalence does NOT automatically cover ALL occupied graphs or unequal alphabets.

## 3. Exact joint pair stabilizer, orbit-stabilizer theorem

For fixed f,g and a chosen original σ∈Γ, a physical occupied-edge permutation h_L satisfying

    h_L(f(p)) = f(σ_P(p))    for ALL original p

is uniquely determined because f is a BIJECTION from P onto its occupied image F_L. The same uniqueness holds for h_R with g and σ_L.

Therefore the entire joint stabilizer can be counted by looping ONLY over σ∈Γ, constructing these forced h_L,h_R and testing membership in H_L^edge,H_R^edge:

    stab(f,g) = # {σ∈Γ :
                    f∘σ_P∘f^{-1} ∈ H_L^edge
                    AND g∘σ_L∘g^{-1} ∈ H_R^edge}.

Here f^{-1},g^{-1} are their inverses as bijections onto occupied physical label sets. Thus

    |Orbit_G(f,g)| = |Γ| |H_L^edge| |H_R^edge| / stab(f,g).

The model does NOT claim the combined group action is free. This corrects any naive division by 720³ when a nontrivial original automorphism correlates the two physical assignments.

## 4. Exact canonical key for a TRUE joint equivalence orbit

For every σ∈Γ, transport the left and right assigned label arrays back into the original canonical W32 index order. Minimize their images independently under every left and right **physical** edge-action permutation. Because h_L and h_R are independent, the pair of separate minima equals the lexicographic minimum of the complete left×right action for that fixed σ. Finally minimize the entire **PAIR** across every σ:

    C(f,g) = min_(σ∈Γ) (
                   min_(h_L∈H_L^edge) h_L∘f∘σ_P^{-1},
                   min_(h_R∈H_R^edge) h_R∘g∘σ_L^{-1}
             ).

Then two legal W32 mapping pairs with the same occupied left/right image palettes have the same canonical key **if and only if** they belong to the SAME joint orbit. This is an exact exhaustive normal form, not a probabilistic hash. It does not enumerate all possible (f,g) pairs, so it cannot determine how many distinct global mapping-pair orbits exist without further enumeration or independent Burnside counting.

The executable finite q=2 oracle imposes a HARD comparison budget (720*(720+720)=1,036,800 physical normalizations for full K6) and raises without returning a truncated "canonical key" on budget failure. For larger q, the theorem remains true abstractly; no claim executable symplectic group enumeration or canonical key beyond W32.

## 5. Independently constructed W32 symplectic automorphism group

Instead of importing a hard-coded graph automorphism table, the reference generates every symplectic basis of GF(2)^4 for the alternating form

    <u,v> = u0*v2 + u2*v0 + u1*v3 + u3*v1  (over GF(2)).

Choose A=image(e0), C=image(e2), B=image(e1), D=image(e3), with <A,C>=<B,D>=1 and all other distinct basis pairings zero. Counts are 15 choices A, 8 choices C, 3 choices B and 2 choices D:

    |Sp(4,2)| = 15*8*3*2 = 720.

Each basis defines an invertible symplectic linear map; with q=2 no nontrivial field scalar or Frobenius projective ambiguity remains. The resulting action on all 15 ORIGINAL points is derived from their coordinates, and on all 15 ORIGINAL lines from their 3-point incidence subsets. ALL 45 ORIGINAL incidence edges are independently verified under all 720 automorphisms.

An additional exact original W32 pair-orbit test checks that the 225 ordered pairs (ORIGINAL point p, ORIGINAL line l) split into precisely TWO orbits:
- 45 actual ORIGINAL incidence flags p~l,
- 180 original NONincidence antiflags.

These are NOT the two physical right pair-label edge-orbits "physically adjacent" vs "physically disjoint" from C12, and the proof never interchanges them.

For full occupied left and right physical K6 images, both physical edge-action groups have order 720. Thus the product action group has size 720³ = 373,248,000, but the actual orbit of any fixed mapping pair is 720³/stab(f,g), with stab(f,g) determined by the independent original 720-element loop. A truly correlated original transformation plus independent left/right physical actions must preserve the exact full seven-class W32 motif vector and its GF5 necessary-floor numerator; explicit regressions check this for several nonidentity elements.

## 6. Acceptance gates, honest limitations, future C14

Code: [exact joint group/orbit certificate](../../research/hyp105_g5e2b3e1c13_joint_orbits.py) and [independent exhaustive original-incidence and seven-class tests](../../research/test_hyp105_g5e2b3e1c13_joint_orbits.py). Dedicated GitHub-hosted hyp105-c13-contract and full Research workflow must both be SUCCESS on the EXACT PR HEAD. Dependence on C12 #291 and the earlier C1–C11 stack means no direct main merge. Parent #230 and #176 remain OPEN_WITH_FORMAL_BLOCKER; no all-h positive seven-motif lower or ASET exponent.

C14 may add a Burnside/stabilizer-based global orbit COUNT and branch-and-bound over canonical joint pair keys for finite W32, with a hard resource gate. This is a finite certification program, NOT automatically a proof of all-h Ω(s^6). A stronger all-h theorem would require additional source-target inequalities invariant under BOTH physical halves and original incidence group; if C13/C14 cannot produce such positive lower, the mathematical result must remain a restricted symmetry reduction rather than a fictitious universal bound.
