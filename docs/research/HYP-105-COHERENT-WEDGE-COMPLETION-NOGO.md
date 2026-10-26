# HYP-105 / #230 — AA4-CWNO: coherent packets refute the mean-\(O(s^2)\) C6 completion route

**Status:** quantified all-\(h\) (on the infinite dyadic-square subsequence \(s=t^2\)) **counterfamily, conditional on the packed genuine-source subfield construction in Draft PR #651**. The independent finite \(W(3,4)\) test certifies the local six-flag mechanism, and exact large-integer tests certify the numerical constants; these do **not independently reprove the infinitely many symplectic source-packet embeddings**. Root #230 stays **OPEN_WITH_FORMAL_BLOCKER**. This is a no-go theorem for an intermediate physical-defect-completion route, **NOT** a counterexample to the original seven-accepted-GF(5)-class \(\Omega(s^6)\) problem.

## 1. What changed since AA4-SPW

PR #653 proved that for an arbitrary fixed complete separately injected correlated pair-label map on the **genuine symplectic** \(W(3,s)\), the physical two-coordinate returning wedges satisfy \(J_x,J_y=O(s^5)\). PR #655 improved this to the genuine original-GQ spectral-star estimate

\[
\boxed{
J_x,J_y\le 2V(s-1)+2(s^2+1)(a-1)=O(s^4),
}
\]

where \(V=(s+1)(s^2+1)\), \(a=\min\{m:\binom m2\ge V\}\). PR #654 proved the **exact** physical six-cycle completion kernel and double-counting identity

\[
W_{2,x}=\sum_{w\in\mathcal J_x}\operatorname{comp}_6(w),\qquad
W_{2,y}=\sum_{w\in\mathcal J_y}\operatorname{comp}_6(w).
\]

An *unproved proposed proof gate* was a universal **fixed-map mean-completion** bound \((W_{2,x}+W_{2,y})/(J_x+J_y)=O(s^2)\). It would imply \(W_2=O(s^6)\). The current result **rules out this proposed gate**, already from the coherent packets of PR #651.

## 2. The imported genuine-source construction, with precise dependency

Use the **genuine original symplectic** \(W(3,s)\) and the **coherent first-copy packets** explicitly described in [the earlier packed-source theorem](HYP-105-END-ENERGY-TAIL-DIFFERENCE.md), section 3–8.

For every \(t=2^k\), \(k\ge4\), let

\[
s=t^2,\quad n=(t+1)(t^2+1),\quad d=t+1,\quad e=nd,\quad
R=\lfloor n/256\rfloor.
\]

The construction selects \(R\) pairs of source \(W(3,t)\) subfield packets in the larger \(W(3,t^2)\), with distinct source factor IDs between packets, full globally injective typed point and line labels and arbitrary correlation. For each packet \(j\), a retained original **base-subfield incidence flag** set \(F_j\subseteq F_0\) has \(|F_j|\ge7e/8\). These are genuine source incidences, not formal or synthetic graph edges.

Crucially, the first-copy physical hub \(h_j=(c_j,c_j)\) is adjacent to each **coherently identified** free corner \(z_{p,l}=(z_p,Z_l)\) whenever \((p,l)\in F_j\), by the actual original incidence flag \((A_jp,A_jl)\), with

\[
f(A_jp)=\{c_j,z_p\},\qquad
g(A_jl)=\{c_j,Z_l\}.
\]

All hub coordinates \(c_j\) are distinct from one another and from all free symbols, and the separate free symbol maps \(p\mapsto z_p\), \(l\mapsto Z_l\) are injective. Every prescribed physical edge carries one **genuine unique original incidence ID**. Completion of other unused original source labels does not remove edges.

**Logical dependency:** the existence and disjointness of these packet embeddings and full injections are taken from PR #651's all-\(h\) proof. The finite tests in this PR do **not** independently certify that infinite packing. The new counting lemma below is deterministic once that input is established; independent qualified scientific review of both steps remains necessary.

## 3. New all-h lower-bound theorem: \(W_{2,x}=\Omega(s^9)\)

**Theorem.** On the completed coherent packet maps above,

\[
\boxed{
W_{2,x}\ge\frac{15}{32}\binom R3\,e^2d
\ge2^{-33}t^{18}=2^{-33}s^9.
}
\]

In particular there are legal fixed correlated \(f,g\) along the infinite subsequence \(s=t^2\) whose average C6-completion count over **all** x-returning physical two-edge wedges satisfies

\[
\boxed{
\frac{W_{2,x}}{J_x}\ge
\frac{s^5}{9\cdot2^{33}}.
}
\]

Therefore no uniform all-map mean \(O(s^2)\) (or even \(O(s^4)\)) completion bound can hold under the original quantifiers.

### Proof, preserving every source incidence and avoiding six-cycle overcount

Fix any **unordered three distinct packet indices** \(i,j,k\). Their common genuine base incidence set

\[
F=F_i\cap F_j\cap F_k
\]

has size \(E=|F|\ge e-3e/8=5e/8\), by the plain union bound inside the *same original base \(W(3,t)\) flag universe*.

For each original base point \(p\), let \(d_F(p)=|\{l:(p,l)\in F\}|\). Then \(\sum_p d_F(p)=E\), \(d_F(p)\le d\) and there are exactly \(n\) base points. The number of unordered **point-pencil cherries**

\[
B=\sum_p\binom{d_F(p)}2
\]

satisfies the deterministic Cauchy–Schwarz bound

\[
B\ge\frac{E^2}{2n}-\frac E2
=\frac E2\left(\frac En-1\right).
\]

Because \(E\ge5nd/8\) and \(d=t+1\ge17\), one has \(E/n-1\ge d/2\). Thus

\[
\boxed{B\ge Ed/4\ge5ed/32.}
\]

Choose which of the three hubs is the *distinguished wedge center*, say \(h_i\) (three choices); choose one cherry \((p,l_1),(p,l_2)\in F\) with \(l_1\ne l_2\); and choose a third common flag \((p',l')\in F\) with \(p'\ne p\). As there are at most \(d\) flags incident with \(p\), this provides at least \(E-d\ge e/2\) choices for the third free corner.

Set
\[
a=(z_p,Z_{l_1}),\quad
c=(z_p,Z_{l_2}),\quad
z=(z_{p'},Z_{l'}).
\]
All three free corners are distinct, because \(l_1\ne l_2\) and \(p'\ne p\). The physical edges \(h_\ell-a\), \(h_\ell-c\), \(h_\ell-z\) exist for **each** \(\ell\in\{i,j,k\}\) because all three base incidence flags lie in their *common retained* \(F\).

The two different assignments of the other two hubs produce two distinct physically simple six-cycles:

\[
a-h_i-c-h_j-z-h_k-a,\qquad
a-h_i-c-h_k-z-h_j-a.
\]

Each such cycle has a **designated x-returning physical wedge** \(a-h_i-c\). At the other two hubs, the adjacent free first-coordinates are \(z_p\ne z_{p'}\), so no other hub hosts an x-return. At a free corner, the two neighboring hub first-coordinates are distinct. Therefore each constructed simple six-cycle has **exactly one x-returning wedge**, at \(h_i\).

Moreover, a constructed physical six-cycle uniquely recovers its three hub labels, the distinguished x-return hub, the two free corners of its cherry (an unordered pair), and the third free corner. Since the free point/line physical symbols are injective, this uniquely recovers the original base cherry and third original flag. The physical edge assignment distinguishes the two Hamilton orientations; different hub triples, different cherries, different third flags and different hub assignments **cannot** overcount the same simple cycle. All counted physical edges have genuine original source incidence IDs; no random graph approximation occurs.

For each hub triple this yields at least

\[
3\cdot B\cdot(E-d)\cdot2
\ge6\cdot\frac{5ed}{32}\cdot\frac e2
=\frac{15}{32}e^2d
\]

different physical simple C6s, each contributing once to \(W_{2,x}\). Summing over the \(\binom R3\) choices proves the first bound.

For \(R\ge3\), \(\binom R3\ge R^3/27\). The earlier packet constants give \(R\ge n/512\), \(e=nd\), \(n\ge t^3\), \(d\ge t\). Hence

\[
W_{2,x}\ge
\frac5{288\cdot512^3}n^5d^3
\ge \frac5{288\cdot512^3}t^{18}
\ge2^{-33}t^{18}.
\]

The last safe inequality is \(5\cdot64\ge288\). All constants are verified in exact unbounded integer arithmetic in the tests.

### Uniform all-map upper for the denominator

The exact source GQ spectral bound from PR #655 holds for these maps too. For every \(s\ge2\),

\[
V\le2s^3,\qquad
a-1\le2s^2,\qquad
s^2+1\le(5/4)s^2.
\]

Here \(a-1\le2s^2\) follows by checking \(\binom{2s^2+1}{2}\ge V\). Consequently

\[
J_x\le2V(s-1)+2(s^2+1)(a-1)
\le4s^4+5s^4=9s^4.
\]

Combining this with the *lower bound* on \(W_{2,x}\) proves the claimed mean lower bound. No assumption about independently distributed source label maps is made.

## 4. Independent finite genuine-source structural falsifier

The executable finite example constructs **three source-disjoint physical hub packets** inside the true original \(W(3,4)\), using actual incidence flags. For each hub choose a point \(p_j\) with two different incident source lines, plus another point \(p'_j\ne p_j\) with a third incident line; keep all six point IDs and all nine line IDs distinct. Use three distinct physical center symbols and coherent free symbols, assign exactly the corresponding genuine point/line pairs, and extend both maps to complete globally injected \(K_{14}\) images.

This preserves three physical hubs connected to three free corners \(a=(3,5)\), \(c=(3,6)\), \(z=(4,7)\), where \(a,c\) share their first-coordinate symbol. Both explicitly constructed simple six-cycles with hub orderings \((h_0,h_1,h_2)\) and \((h_0,h_2,h_1)\) are checked edge-by-edge against **genuine original source incidence IDs**; all six source flag IDs within each are distinct, but the cycles have the x-return \(a-h_0-c\) and are not accepted original D6 (nor any other historical GF(5) six-coordinate class).

The exact physical wedge completion kernel of PR #654 and the independent depth-four DFS both certify at least two completions of this genuine x-returning wedge. This finite certificate independently tests the **local mechanism**, not the existence of arbitrarily many packed paired source subgeometries.

## 5. Scientific interpretation: no-go for this proof gate, NOT for root HYP-105

The preceding proposed mean-\(O(s^2)\) completion hypothesis is **false if the packet embedding theorem of PR #651 is valid**. The actual obstruction is particularly strong: average number of C6-completions per x-returning wedge can be \(\Omega(s^5)\) even though the number of returning wedges themselves is uniformly only \(O(s^4)\). Therefore direct defect control through a uniform \(O(s^2)\) mean completion cannot establish \(W_2=O(s^6)\) for all fixed correlated label maps.

This **does not imply** failure of the root seven-class lower bound. On **the same coherent packet family**, PR #651 established a strong restricted positive accepted D6 bound \(D_6\ge2^{-35}s^{21/2}\). Our newly counted defective physical C6s have repeated **source POINT factors at the designated wedge** and fewer than six occupied physical x-coordinate symbols, so they do not contribute to D6. The accepted sixflag D6 cycles counted in PR #651 use distinct point and line factors; both large physical noises and large accepted motifs coexist.

**Next P0:** abandon an unconditional mean-completion bound under the original correlation allowances. Investigate a **source-ID-qualified compensation/dichotomy theorem** on the same fixed maps—large physical codegree/defect energy forces one of the accepted original six-ID families—or build a counterfamily to that dichotomy. A more restricted random or quasirandom-label theorem is permissible as a separate result but must not be promoted to the unrestricted root theorem.

**Acceptance:** proof depends on earlier draft #651's infinite packing existence; the exact new counting logic and finite structural oracle are independent and CI-checkable. Keep Draft and demand independent qualified proof review of *both* the imported packing and new no-overcount steps, plus green exact-head hosted specialized, Research and INDEX checks. Root OPEN_WITH_FORMAL_BLOCKER.
