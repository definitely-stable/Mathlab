# HYP-105 K3-G2-B — original-source closure tensor and paired kernel

Date: 2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of [PR #374](https://github.com/definitely-stable/Mathlab/pull/374), exact pinned parent HEAD `bd6d122bcf45bf8cb15cfce786da4d894c10c0d6`. No `main` changes, no merge. **RESTRICTED_THEOREM_C**, not Branch A/B.

## A. Exact original GQ closure tensor

Fix the SINGLE global legal injective f,g of the original W(3,s), s=2^h. For original source point q and line l with g(l)={y,y'}, T^g[q,l] counts physical t distinct from y,y' for which the two ORIGINAL lines mapped by g to {y,t},{y',t} both pass through original point q. Missing labels contribute zero. The dual T^f[original line, original point] uses f. For fixed l,t, two distinct original lines meet at at most one original point, hence sum_q T^g[q,l]<=a-2. No independence or vertex-label automorphism assumptions.

## B. Exact cross-original source pair kernel

For anchor original line l let F_l be the physical graph of point labels f(p) for p incident l, with adjacency A_l. Let P be the physical-coordinate x original-point binary endpoint matrix of ONE global f. Then K_l^f(q,r)=(P^T A_l P)[q,r] is the number of physical anchor edges connecting an endpoint of f(q) to an endpoint of f(r). For distinct q,r, 0<=K<=min(4,s+1). On the diagonal, K(q,q)=2 if q incident l, else 0 by global injectivity.

The horizontal repeated-column incidence has exact form

    J_h = (1/2) sum_l (T^g[:,l])^T P^T A_l P T^g[:,l]
    J_cross,h = sum_l sum_{q<r} T^g[q,l]*T^g[r,l]*K_l^f(q,r).

Identical dual formula for J_cross,v using source line origins and f-closures. Every physical third-coordinate t has at most one original source q, so q!=r path interiors are automatically distinct. K3-G2-B checks EXACTLY J_cross=J_cross,h+J_cross,v against the independently constructed K3-G2-A ledger. J_same is the diagonal.

## C. Exact geometric partition (no hidden source types)

Pairs of distinct original points q,r, relative to original anchor line l, split into four mutually exclusive categories: (i) both q,r on l; (ii) exactly one on l; (iii) both off l and collinear on some OTHER original line; (iv) both off l and noncollinear. The dual partition classifies original source lines relative to an anchor point. Contributions are integer, weighted by Tq*Tr*K, and their sum must be the exact J_cross. None of the four classes is asserted o(s^6).

## D. New universal physical-wedge packing theorem

For the global physical graph H_g of all V used g labels, let d_g(t) denote its physical vertex degree. Each unordered pair of different ORIGINAL lines g(l1),g(l2) meeting physically at t is a host wedge. If the original lines also meet, the GQ axiom makes their ORIGINAL intersection point unique. Such a source wedge may or may not have a third global physical label closing its host triangle. Consequently, all s=2^h:

    C_g = sum_{q,l} T^g[q,l]
        <= W_g = sum_q sum_t choose(d_{G_q}(t),2)
        <= sum_t choose(d_g(t),2)
        <= a*choose(a-1,2) = O(s^(9/2)).

The same inequalities hold for f. Relative to naive source-pencil accounting O(V*s^2)=O(s^5), the all-h host packing saves a square-root factor in s for the GLOBAL source wedge first moment. It does NOT prove J_cross=o(s^6); squared and cross-source correlations remain uncontrolled.

For ONE fixed pair labeling, an additional deterministic, ONE-side-independent conditional certificate is

    J_cross <= min(4,s+1)*(sum_l sum_{q<r} T^g[q,l]*T^g[r,l]
                             +sum_p sum_{l<m} T^f[l,p]*T^f[m,p]).

Do not misrepresent the conditional bound as all-h asymptotic saving.

## E. Oracles, scientific status, next gate

Reference: `research/hyp105_g5e2b3e1k3g2b_origin_pair_kernel.py`. Independent tests: `research/test_hyp105_g5e2b3e1k3g2b_origin_pair_kernel.py`. Independent anchor-first third-coordinate original-intersection oracle reconstructs T without using the source-pencil wedge algorithm. A separate point/line physical-anchor scanning oracle reconstructs K and every four-way geometric component. Full host original-meet wedge census and fail-closed budgets are included. Genuine globally labeled W(3,2) and W(3,4). Path-limited dedicated GitHub-hosted Contract plus inherited Research/INDEX, no redundant full matrix.

Next: determine whether the four geometric bins exhibit an all-h strict loss in one class, or prove a simultaneous C6 lower-vs-J_cross surplus with an explicit positive s^6 coefficient. The seven-family S barrier remains independent from full R3: no S=Omega(s^6), no ASET exponent, root issues remain open.