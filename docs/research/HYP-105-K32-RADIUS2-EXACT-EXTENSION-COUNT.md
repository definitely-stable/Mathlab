# HYP-105 / #230 — AA4-K32X2: exact genuine-source two-flag extensions

**Status:** an all-h scoped exact classification and global deduplication theorem. This is NOT the root seven-class Omega(s^6) proof. Status of #230 remains OPEN_WITH_FORMAL_BLOCKER. All applications use the genuine original symplectic W(3,s), s=2^h, complete separately injective and arbitrarily correlated fixed physical pair maps f,g.

## 1. Preconditions and dependence

PR #659 gives genuine original-incidence-ID selectors and two physical-coordinate cuts, retaining BOTH physical diagonals of every selected ID. PR #661 classifies saturated strong-codegree C6-free triangles as physical K3,2; PR #662 proves their six ORIGINAL source incidence IDs cannot form any accepted GF5 sixset or become accepted by one ID replacement.

This slice counts ALL **two**-source-incidence-ID replacements that are accepted by the historical **seven-class** GF5 classifier. Work with an actual physical K3,2 having hubs h0,h1,h2 and free corners z0,z1, with five pairwise distinct typed first symbols and five distinct typed second symbols. Every physical edge has a unique backing ORIGINAL incidence ID due to the global pair injections, and the six old IDs have six different source points and six different source lines. The same conditions hold in the source-ID coherent graphs of previous PRs; the counting theorem does not require the K3,2 to remain saturated in the full physical graph.

Let F be these six original source IDs. For hubs hi,hj define the NEW full-physical common-neighbor set

\[
W_{ij}(F)=\{w\in N_H(h_i)\cap N_H(h_j): w_x\notin X(F),\ w_y\notin Y(F)\},
\]

where X(F),Y(F) are the five physical symbols of the original K3,2 on their respective typed axes. All edges in the full H originate from **actual original incidence IDs**.

## 2. Complete all-h two-ID accepting classification

Define E2(F) to be all accepted historical GF5 sixsets F' of actual source incidence IDs with |F\setminus F'|=|F'\setminus F|=2.

**Theorem A.** Every F' in E2(F) belongs to the historical ORIGINAL D6 class, and

\[
\boxed{ |E_2(F)| = 2\sum_{0\le i<j\le2}|W_{ij}(F)|. }
\]

For every w in W_ij, remove EITHER the two old edges hi-z0 and hj-z1, OR the two old edges hi-z1 and hj-z0. Add the two true source-ID edges hi-w and hj-w. Each resulting sixset is a genuine original accepted D6, and no two such constructions collide.

**Proof (exhaustive structural cases).** The old coordinate pair projection is K3,2 on five coordinate symbols, with degree profile (3,3,2,2,2). Every one of the seven accepted classes requires EXACTLY six coordinate symbols of degree two on EACH typed axis. Removing two old edges incident with the SAME free corner leaves the other free symbol degree three, impossible after insertion of two new edges. Hence the two removed edges touch different frees.

If both removed edges share the SAME hub, the four remaining old edges form K2,2 with four symbols ALREADY of degree two. Each two new x-label pairs must then be the SAME pair of two other symbols to yield six degree-two symbols, forcing the two distinct inserted original flags to share ONE source point by injectivity of f. The exactly symmetric y argument forces those two flags to share ONE source line by injectivity of g. Two distinct flags with identical original source point AND line would be the same incidence: forbidden in the TRUE simple source graph. Thus NONE of the seven classes, including B/B, can arise in this case.

The remaining case removes edges incident with DIFFERENT hubs and DIFFERENT frees, i.e. a size-two matching. The four surviving old coordinate edges form a four-edge path through all five old symbols; the two deficient hub symbols each have degree one. To achieve a 2-regular six-symbol x projection, the two newly inserted point-pair labels MUST connect those two deficient hub x-symbols to one common NEW x-symbol. Analogously on the y axis, the new line-pair labels must connect the corresponding deficient hub y-symbols to one NEW y-symbol. Since every new label contains a fresh coordinate, both added original point IDs and both line IDs differ from all retained ones and each other. Therefore only historical A/A acceptance is possible.

The historical A/A D6 acceptance requires the six named-column dual edges of the two projections to coincide and form one connected C6. On the x side, each deficient hub is joined to a specific new incidence ID; on the y side, the same retained old flag at the corresponding hub must be paired with THAT SAME new incidence ID. A crossed assignment on y would give a different named-column dual graph and is rejected. Hence BOTH new flags must represent ACTUAL full-physical edges from their respective hubs to the SAME fresh corner w=(w_x,w_y), and w belongs to W_ij(F). Conversely such two genuine physical edges close a coordinate-rainbow sixcycle, with six distinct original point and line factors, giving precisely D6. Its two possible old matching deletions are distinct source sixsets. Old discarded IDs uniquely recover the hub pair and which matching was deleted; added physical pair labels uniquely recover w. No overcount remains. QED.

## 3. Global all-h multiplicity bound — at most SIX source parents

Take ANY collection K of **distinct** original six-ID sets underlying actual physically coordinate-transverse K3,2 configurations in the SAME full f,g. The original accepted D6 ↔ physical coordinate-rainbow simple C6 correspondence from AA4-RC6 PR #652 is a bijection.

**Theorem B.**
\[
\boxed{
2\sum_{F\in\mathcal K}\sum_{i<j}|W_{ij}(F)|
=\sum_{F\in\mathcal K}|E_2(F)|
\le6D_6(f,g)\le6S_{\mathrm{seven}}(f,g).
}
\]
In particular,
\[
\boxed{
D_6(f,g)\ge\frac13
\sum_{F\in\mathcal K}\sum_{i<j}|W_{ij}(F)|.
}
\]

**Proof.** Fix an accepted original D6 sixset F', with its UNIQUE unrooted unoriented coordinate-rainbow physical C6. If F' is a two-exchange extension of an old source K3,2 F, the TWO newly added physical edges meet at a new vertex w of this cycle. There are SIX possible choices of w. Removing the two physical cycle edges incident to w leaves a four-edge path on five vertices. Its endpoints must be the two deficient old K3,2 hubs, and its middle degree-two vertex the third hub; its other two vertices are the two frees. The two missing K3,2 cross-edges that recover F are therefore uniquely forced, each backed by AT MOST ONE genuine original incidence ID due to the global pair injections. For fixed w there is at most one parent F. Thus every D6 has at most SIX parent source sixsets. Summing counts proves the bound. QED.

The coefficient six is SHARP for the unrestricted class of coordinate-transverse physical K3,2 (not necessarily saturated): nine true source incidence flags forming one physically coherent K3,3 yield six original D6, six distinct K3,2 parents and 36 two-exchange parent memberships. These nine flags come from the genuine W(3,4), globally separate typed f/g maps are completed over all 85 source points and lines, and all second-parity physical diagonals are retained.

The theorem is a **conditional positive certificate**. No lower bound on the genuine-source extension mass on its right-hand side has been shown for every fixed full correlated f/g. The bound six for the saturated-only subfamily might be improvable.

## 4. Independent original W(3,4) numerical falsifiers

The code has TWO structurally different finite true-source enumerators:
- A full physical original-ID neighbor-intersection census: take the genuine original W(3,4) full 425-source-flag physical H, intersect hub neighborhoods, exclude all five occupied symbols on each axis, recover both original flag IDs and classify every resulting sixset with the historical seven-family GF5 oracle.
- An independently built ORIGINAL SOURCE POINT-label-indexed swap census: examine all admissible two-edge deletion patterns; for each fresh x-symbol look up source points with the required original f-label pairs, enumerate their REAL incident lines, and pass constructed sixsets to the historical GF5 classifier, without using the physical common-neighbor lists. Independently enumerate same-hub repeated-point alternatives to reject hidden B/B acceptance. Both must produce exactly the SAME accepted source sixsets.

Additional checks use the previous parent #662 protected 8-flag true W(3,4) example: exactly ONE fresh common corner, giving exactly TWO accepted original D6 by two original-ID replacements (none with one ID). When the y-line labels of the two new flags are swapped without breaking separate global injectivity, their x and y named-column duals disagree: no true original D6 two-exchange is accepted. This prevents accidental promotion of unrelated left/right 2-regular counts.

A separate TRUE W(3,4) 9-source-flag submatching of the previous protected 4x4 construction gives a physical coordinate-rainbow K3,3 and opposite-parity companion matching. Every one of its six accepted original D6 has six distinct K3,2 parents, proving exact membership totals 36 and 6, hence SHARPNESS of the universal sixfold bound. The source incidence flags are genuine, not synthetic.

All-h mathematics is in the proof above. Runtime oracles use only finite h=2 as falsifiers, not substitutes for infinite proofs.

## 5. Remaining root acceptance blocker

This quantifies a **real same-map, globally de-duplicated** compensation mechanism: saturated K3,2 mass produces accepted original GF5 D6 if its hub pairs admit enough **new full-physical common neighbors** at fresh symbols. A large number of saturated K3,2 by itself does NOT force such extensions; the extension mass could be zero.

Next mathematical P0: prove or falsify a **genuine original symplectic source** all-map lower bound on the cumulative fresh hub-pair common-neighbor population for a suitably large family of distinct saturated K3,2 from a fixed coherent selection, or prove a separate same-map positive lower from OTHER historical GF5 six-ID classes when that extension mass is small. No unrestricted S_seven Omega(s^6) proof and no ASET exponent. Keep Draft pending exact-head GitHub-hosted specialized, Research and INDEX CI and independent qualified proof referee. No main merge.
