# UCT-005 D1-B2-E — total trusted PIN budget and exact full-audit information gate

**Date:** 2026-10-10. Owner [#255](https://github.com/definitely-stable/Mathlab/issues/255), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223), [root #105](https://github.com/definitely-stable/Mathlab/issues/105). Accepted comparators [PAGE-001 #241](https://github.com/definitely-stable/Mathlab/pull/241), [D1-B2-C #245](https://github.com/definitely-stable/Mathlab/pull/245), [D1-B2-D #253](https://github.com/definitely-stable/Mathlab/pull/253). Concurrent [page-COW tree #248](https://github.com/definitely-stable/Mathlab/pull/248) has distinct allocator costs and cannot be ranked by incomplete fields.

**Classification:** DERIVED_CLASSICAL_FULL_AUDIT_BOUND_AND_CONDITIONAL_F1_BUDGET. **ROOT_OPEN_UNPROVED.**

## 1. Exactly scoped unconditional information inequality

Fix H independent binary PIN-membership choices at distinct historical epochs: before each of H no-op SETs, reader0 either performs PIN_CURRENT or not; previously acquired PINs persist. At the end all 2^H histories have identical latest logical data and latest epoch, but distinct active historical PIN subsets.

Assume a deterministic exact **full-vector audit** whose task is to return all H membership bits in one run. All input-dependent persistent trusted states (author, both clients, authority, setup advice) are charged within s bits. The **entire** honest-server remote reply transcript, including all state-bearing responses/status/lengths/timing if used, has at most b bits. There are no uncharged independent source-state bits, client oracles, author logs, or hidden state-dependent advice. Adaptive addresses determined by already known trusted/reply bits cannot independently encode additional new state. The protocol must answer exactly on honest remote inputs; always ABORT is not an exact auditor.

Different membership vectors must induce distinct pairs (trusted encoding, remote response transcript), otherwise identical verifier input could not produce different entire H-bit answers. **Variable-length reply subtlety:** if responses can be arbitrary binary strings of length up to b with their lengths available for free, they have at most \(\sum_{j=0}^{b}2^j=2^{b+1}-1\) values, not merely \(2^b\). Nevertheless

\[
2^H\le 2^s(2^{b+1}-1)<2^{s+b+1}.
\]

Since H, s and b are integers, **\(\boxed{H\le s+b}\)** still follows. For canonical fixed-length b-bit reply encodings the simpler direct estimate \(2^H\le2^{s+b}\) holds. Any extra state-bearing side channel beyond the enumerated replies is additional charged input.

This is a **classical pigeonhole bound**, tight for the simplified channel by storing s prefix membership bits in trusted state and returning the remaining H-s bits directly. For H<=8 an independent brute-force oracle enumerates all words and verifies signature cardinality, full-audit injectivity and explicit collision witnesses when s+b<H. This is NOT a new information frontier or novel theorem.

**Nontransfer:** H<=s+b is false for one exact PIN(e) query: a direct-indexed honest remote H-bit membership array returns the desired bit with one bit read, s=0, for any H. Its remote service is **honest and unauthenticated, not F1**. Applying full-vector counting to the single-bit query would falsely claim H<=1. A 40-byte SHA256 generation+digest is not an injective information-theoretic representation of unbounded histories; F1 uses bounded capacity and computational binding assumptions with paid verification. No infinite post-hoc state extension is claimed.

## 2. Same F1 service and fully identified trust components

The experiment runs identical GF2 initial words and three SETs with a mandatory no-op epoch2; reader0 PIN_CURRENT epoch0, reader1 PIN_CURRENT epoch2, latest epoch3, every nonempty half-open RANGE_PARITY, AS_OF both historic roots, then sequential UNPIN and GC. Both already accepted implementations use the **same** PAGE-001 immutable 48-byte manifest, complete remote page size P, paid author updates, paid LATEST anchor and serialized trusted PIN authority.

**E — D1-B2-C full trusted PIN entries:** n-bit writer data, 40-byte latest epoch/root, two separately held 40-byte reader PIN tokens, plus 41 bytes per active authoritative PIN record. At two PIN epochs: s_E=n+8*(40+80+82)=n+1616 modeled persistent trusted bits. Trusted authority scans active PIN records during reclaim; remote page-delete commands are charged.

**R — D1-B2-D remote authenticated bitmap:** same n-bit writer, 40-byte latest root and two reader token copies, plus a 40-byte trusted bitmap generation/digest in the central PIN authority. At two PIN epochs: s_R=n+8*(40+80+40)=n+1280 modeled persistent trusted bits. The two reader roots still count: this is **NOT** O(1) total trust state in general. The bounded 2C-bit bitmap consumes L_B=ceil(ceil(2C/8)/P) remote pages and requires full authenticated reads, complete rewrites, SHA input and root publications on PIN/UNPIN. Every SET verifies the bitmap before reclaiming the previous latest. Remote DROP_PAGE requests are charged separately.

A full immutable snapshot costs L=ceil(ceil(n/8)/P)+ceil(48/P) complete remote pages. After epoch3, retained snapshots are {0,2,3}, so E uses 3L remote pages and R uses 3L+L_B. The remote bitmap occupies disjoint public physical page offsets from all snapshot slots; no free remote directory is used.

### Exact finite resource tradeoff (n=33, P=2, C=8)

| Quantity | E: trusted PIN registry | R: authenticated remote bitmap |
|---|---:|---:|
| Writer 33 bits | Included | Included |
| Trusted latest epoch/root 40 bytes | Included | Included |
| Two **reader-held** trusted PIN roots (80 bytes) | Included | Included |
| Central trusted PIN membership | 82 bytes | 40 bytes |
| **Total modeled persistent trusted bits** | **1649** | **1313** |
| Remote pages at e3 with three live snapshots | **81** | **82** |
| Remote full snapshot page writes across 3 SETs | **81** | **81** |
| Additional PIN-membership work | Trusted PIN record scans | Remote bitmap reads/rewrites, SHA, authority publications |

A **1600-bit modeled persistent-trust cap** admits R and excludes E for this exact transcript. The saved central PIN memory is 42 bytes (336 bits), bought with one remote bitmap page plus additional remote I/O, hashing and trusted publications. Tests explicitly check caps 1312, 1313, 1648, 1649. This is a **conditional finite upper-design separation**, not a universal lower bound or an unqualified Pareto improvement.

The reported budget is for precisely **modeled persistent trusted bits**, including all client roots, but not all possible transient RAM and unmodeled program/setup advice. Do not silently promote it to an absolute total trusted-memory claim.

## 3. Unknown costs are NOT zero

Explicitly unknown in the present finite upper reference: peak **transient trusted scratch RAM**, network framing/retries/authentication, real power-loss recovery and page barriers, real SSD/FTL write amplification, uniform asymptotic collision-resistance assumptions and program/one-time preprocessing advice bits. For R, SHA input counts and remote bitmap page updates are reported; for E, trusted PIN record page reads, bytes and comparisons are reported. Both price addressed page-delete calls. Missing cost dimensions prevent a full Pareto ranking or new same-model joint theorem.

All integrity statements remain conditional on an ideal linearizable anchor/PIN authority, SHA binding and an honest remote page-delete API for performance claims. Byzantine withholding permits ABORT and provides no availability. These assumptions are *not* derived from finite tests.

## 4. Primary-source/theorem-transfer firewall

- LIT-159, Tas–Boneh, *Vector Commitments with Efficient Updates*, AFT 2023, DOI 10.4230/LIPIcs.AFT.2023.29: proof **refresh** at changed commitment, not an automatic cost for immutable historical AS_OF roots.
- LIT-200, *Lower Bounding Update Frequency in Short Accumulators and Vector Commitments*, EUROCRYPT 2026, DOI 10.1007/978-3-032-25330-9_7: accumulator/VC witness-update and invalidation costs are not already the F1 PIN/GC/physical-page theorem.
- LIT-157, memory checking: trusted memory/probe quantifiers must be mapped alongside author memory, both clients, anchor, pin registry, page rounding, malicious server, and setup before transfer.

The full-vector inequality is **known and classical**, the single-member invalid transfer has an **explicit counterexample**, and the 1600-bit threshold is **finite and conditional**. **No original nonfactorizing UCT-005 joint lower bound has been proved**. Under a failed source-to-F1 same-task reduction, mark STOP_NOVELTY rather than extrapolate a proof from tests.

## 5. Reproducibility and next slice

Source: research/uct005_d1b2e_total_pin_budget.py.
Independent finite tests: research/test_uct005_d1b2e_total_pin_budget.py.
GitHub-hosted focused workflow: .github/workflows/uct005-d1b2e-total-pin-budget.yml.
Run the focused standalone diagnostics and full Research CI **on the exact PR head** before merging.

Following acceptance, D1-B2-F should price peak ephemeral trusted memory, root/authority durability, end-to-end bytes and source proof conditions, then compare the accepted segmented COW allocator with PIN bitmap under a frozen all-axis resource vector. Only after matching assumptions and falsifying against feasible upper constructions may a novel quantified joint theorem be proposed.
