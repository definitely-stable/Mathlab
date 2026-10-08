# UCT-001 — finite transition/observation model, classical theorem and falsifiers

Date 2026-10-08. Parent [UCT-001 #74](https://github.com/definitely-stable/Mathlab/issues/74). **Status: SELF-CONTAINED DERIVED_CLASSICAL proof; finite CI oracle separate; NO originality claim, NO Lean claim, NO Rust.**

## A. Frozen object (do not silently conflate with cell-probe)
Let X be a nonempty finite state set; E subset X × X a directed allowed-transition relation, with graph distance dist_G(x,y) the minimum number of steps in E (infinity if unreachable). Let O:X→Y be a *current-state* observable.

An encoding phi:X→F_q^m is **exact for O** iff phi(x)=phi(y) implies O(x)=O(y). It need not inject distinct x with identical O. A **write-local** encoding with budget w in {0,...,m} satisfies d_H(phi(x),phi(y))<=w for every directed edge (x,y) in E. Only the number of changed *coordinates* is charged; computing the new code and reading the old code are unbounded and are NOT hidden inside the proof.

For a state x and d>=0, let R_d(x)={y: dist_G(x,y)<=d}. Let N_O(x,d)=|{O(y):y in R_d(x)}|. Different current observables require distinct codes. If correctness requires full-state recovery, take O(x)=x.

**Important**: if an update algorithm receives only a public label (such as overwrite(i,b)) and phi(x), representation state must additionally implement transitions consistently on phi-classes: phi(x)=phi(y) => phi(u(x))=phi(u(y)) for each enabled label, with equal observable outputs. That requirement is NOT supplied by the simple graph theorem; it is a separate deterministic-automaton congruence. Future-trace equivalence is strictly stronger than current output equality.

## B. Baseline theorem (elementary Hamming-ball counting)
For any x∈X and integer d>=0, every exact write-local encoding as above obeys

    N_O(x,d) <= V_q(m, min(dw,m))
              = sum_{j=0}^{min(dw,m)} binom(m,j) (q-1)^j.

**Proof.** For any y in R_d(x), select an allowed transition path from x to y of length at most d. Along each transition, Hamming distance between the endpoint codes is at most w. Triangle inequality yields d_H(phi(x),phi(y))<=dw, and of course at most m. Thus every code phi(y) for y in R_d(x) lies in the q-ary Hamming ball of radius min(dw,m) around phi(x). Correctness for current O means that any two states with distinct observable values must have distinct codes. Therefore the number of distinct observable values in R_d(x) cannot exceed the number of codewords in the Hamming ball, namely the stated volume. QED.

**Exact specialization to Mathlab LENT-001:** X consists of all subsets S⊆[V] with |S|<=d; O(S)=S; E is singleton insertion with |S|<d; x=empty set. Write phi(S)=sum_{i∈S}a_i over F_q, where |supp(a_i)|<=w. Every subset is reached in <=d insertions, so N_O(empty,d)=sum_{j=0}^d binom(V,j), obtaining KR-001. The proof does *not* establish additive linearity or existence of such columns; it is a necessary capacity condition only.

**Tightness for a star:** With graph of one center x and K directed adjacent leaves, all observably distinct, d=1 and w=1, the bound gives K+1<=1+m(q-1). This is sharp: map center to 0^m and each leaf to one of the m(q-1) distinct weight-one words. No performance or cryptographic claims.

## C. Counterexample: capacity is NOT sufficient for embedding
Take q=2, m=2, w=1, d=1, X={0,1,2}, O(x)=x, and E containing both directions of every edge of a triangle. Every radius-one reachable set has three vertices, and V_2(2,1)=1+2=3, so the *necessary* counting bound holds everywhere.

Yet no exact encoding obeying w=1 exists. The two-bit hypercube's unit-distance graph is bipartite, while a triangle is an odd cycle. Injectively mapping all three triangle vertices so every pair is at Hamming distance <=1 is impossible. In contrast a three-node path embeds as 00--01--11 at w=1.

Consequently **a sufficient characterisation of write-local representations needs more than graph growth/ball volume**. The next possible theorem must account for edge structure, graph homomorphism/cut geometry, and the *actual update algorithm*, not merely the number of reachable states. This counterexample is elementary and is not an originality claim.

## C2. Bipartiteness still is not sufficient: K(2,3)
Consider the complete bipartite update graph with parts of sizes 2 and 3, q=2,w=1,m=3 and O(x)=x. Every vertex in the size-2 part has three adjacent vertices, so N_O(x,1)=4=V_2(3,1). The other vertices have N_O(x,1)=3<=4. Every vertex reaches all five vertices by distance 2, so N_O(x,2)=5<=V_2(3,2)=7. Thus all radius bounds hold at every vertex for every d (for d>=3 the radius covers all eight words).

**Nonetheless there is no 1-local injective embedding into F_2^m for any m.** Distinct binary words u,v have at most two common Hamming-distance-one neighbors: if they differ in exactly two coordinates, the two intermediates are the only possibilities; at every other distance they have none. The two vertices in the size-2 part would need three distinct common neighbors, contradiction. QED.

This is a **classical cubical-graph obstruction**, not a new theorem. Original-source overlap: Garey–Graham 1975; cubical graph recognition NP-complete by the 1985 paper (UCT-SRC-12/13), Livingston–Stout 1988 (UCT-SRC-14). Do not confuse arbitrary subgraph embedding ("cubical") with *isometric* embedding ("partial cube"), which requires stronger distance preservation.

## D. Counterexample: same output ≠ interchangeable online state
Let f(a,b)=a∧b. Old states x=(0,0), y=(0,1) both have f=0. Under the common public overwrite a<-1, outputs become f(1,0)=0 versus f(1,1)=1. Storing only f(x) cannot implement correct arbitrary overwrites. An assumption that old values are externally authenticated is a different model (TOM-003 D1/T); requiring exact future behavior creates an automaton observational-equivalence condition stronger than equality of current f.

## E. Explicit transfer barriers and cost ledger
| Assertion | Why the theorem does not imply it |
|---|---|
| A cell-probe update lower bound | Only changed q-ary coordinates are charged, no word access cost, no adaptive queries or word size. Compare FS'89, PD'06, Yi–Zhang. |
| A q-ary code construction | Ball volume is necessary; triangle falsifies sufficiency even for a finite graph. |
| Memory savings from observation equivalence | Current output equality need not be preserved under future public update labels (AND example). |
| A lower bound on bytes transmitted | There is no communication, source access, entropy distribution or encoding length in model A. |
| A randomized approximate lower bound | Deterministic exact representation only. No distribution/coins/epsilon in the baseline proof. |
| Automatic bound for additive ASET | Only necessary capacity transfers. Structure of columns and signed-subset collision restrictions require separate analysis. |
| A conditional cryptographic security guarantee | There are no hashes, adversaries or cryptographic assumptions in this model. |

## F. Independent finite verification protocol
`research/test_uct001_baseline.py`:
1. independent reachability BFS and observational image counting vs direct Hamming-ball enumeration, across all directed graphs on <=3 nodes, q=2, m=0..3, w=0..m, d=0..3;
2. enumerate all distinct encodings of three states into F_2^2; path admits w=1, triangle does not, though both satisfy capacity; separately exhaust K(2,3) embeddings in F_2^3 and check common-neighbor lemma for m<=5;
3. enumerate all 16 Boolean f(a,b) truth tables and old/new overwrite traces; check that output equality alone does not ensure future-trace equivalence;
4. compare star bound with explicit weight-one construction for q=2,3 and small m.

Tests can falsify a mistaken universal statement, not establish asymptotic generality. The proof above is direct; software is a regression verifier only.

## G. Research fork after baseline
- **G1-A:** request a strictly stronger joint inequality for a named dynamic problem and unified cost model; compare [UCT sources](UCT-001-PRIMARY-SOURCES.md).
- **G1-B:** existing binary unit-edge embeddability is the classical cubical-graph problem (NP-complete recognition). STOP novelty for generic subgraph obstructions; only reopen for an explicitly novel observation-quotient, update-algorithm, or multi-resource setting with source-level separation. Isometric partial cubes are strictly different.
- **G1-C:** separately model deterministic observable-preserving update congruences and state minimization. This is a classical automata-theory object; narrow to a resource improvement only when fully costed.
