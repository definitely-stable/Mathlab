# UCT-005 D1-B2-F3-C — speculative one-pass authenticated PIN bitmap staging

2026-10-11. Parent [#105](https://github.com/definitely-stable/Mathlab/issues/105); science [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). Stacked research predecessor [F3-B #290](https://github.com/definitely-stable/Mathlab/pull/290) and [F2 #283](https://github.com/definitely-stable/Mathlab/pull/283) are NOT accepted until their own required final-head CI and merges. This slice is a **counterconstruction to the necessity of two bitmap-read passes**, not a proof of a universal optimal upper or UCT-005 joint lower.

**Scope:** conditional ideal serialized trusted publisher, public fixed remote page addresses, trusted SHA-256 digest + monotone generation, two independently trusted reader PIN tokens, adversarial untrusted bytes, page size P, epoch cap C, honest staging writes and addressed deletes. Crash durability/final fsync is out of scope. Remote stage can be written *speculatively* before validating the old bytes, provided it remains unobservable as authoritative until trusted digest publication and is dropped on failure.

## Why F2's second pass can be eliminated

F2 first fully authenticates the old bitmap by SHA scan, then rereads it while staging a new bitmap and verifying old digest again. This is useful if a mutation must make **zero speculative remote writes before old-data authentication**, but is not forced by the F1 trust contract. The remote stage has no trusted authority until publication. A speculative protocol can:

1. Read immutable trusted (generation, SHA digest). Initialize two streaming SHA-256 states, one for old generation and one for generation+1. Keep no trusted full bitmap and reserve a distinct untrusted staging slot at next-generation fixed addresses.
2. For each of M=ceil(B/P) old P-byte pages (B=ceil(2C/8)), validate length and zero padding, feed old valid bytes to old hash, modify at most the selected bit within that page, feed new valid bytes to new hash, and **write the full P-byte new page to staging**. Charge one bitmap page read, one stage full-page write and one eight-byte addressed locator. Only two conceptual payload page buffers are live (<=2 min(B,P)); Python's untrusted remote dictionaries and cryptographic/runtime memory are explicitly excluded.
3. After scanning **all** pages, compare old SHA to independently trusted digest. If mismatch or reader's independently trusted PIN token contradicts an authenticated bit, **ABORT without trusted publication or reader-token mutation**, and issue paid DROP_PAGE for *every staged page*. Partial failures before the last page drop only the attempted prefix. No untrusted staging page is usable as a fresh trusted root.
4. If verification succeeds, publish new trusted generation/digest in an ideal atomic transaction, switch active slot, then issue M addressed retirement page deletes for the old slot. An aborted/withheld remote stage has no successful liveness guarantee. Pages orphaned after a crash remain a separate GC/durability problem, not free reclaim.

Crucial distinction: *failure-side untrusted speculative writes are permitted*, but **failure-side authoritative writes are prohibited**. F2's original no-staged-writes-before-verified-old schedule is a stricter operational variant. This F3-C result shows a **different Pareto candidate**, not that the implementation is universally preferable.

## Exact ledger on the same history

With four bitmap mutations (PIN0, PIN2, UNPIN0, UNPIN2) and three SETs, the independently instantiated bulk, two-pass and speculative one-pass implementations receive identical initial GF(2) word, updates (including no-op e2), PIN/AS_OF/LATEST queries, and release schedule:

| Resource on this exact history | Bulk bitmap | F2 two-pass staged | F3-C one-pass staged |
| --- | ---: | ---: | ---: |
| Online bitmap page reads | 7M | 11M | 7M |
| Mutated bitmap image full-page writes | 4M | 4M | 4M |
| Peak remote page images | 3S+M | 3S+2M | 3S+2M |
| Speculative stage writes *before* old digest authentication | not this protocol | 0 | 4M |
| Bound on *bitmap payload* scratch only | selected 3B buffer upper | 2min(B,P) | 2min(B,P) |

Here S=ceil(ceil(n/8)/P)+ceil(48/P) is the immutable snapshot image page count. F3-C saves exactly 4M bitmap read pages versus *this chosen* F2 two-pass protocol and does **not** claim an all-axis Pareto ordering. In particular failed/retried operations can increase staging writes, aborted-stage DROP_PAGE traffic, remote garbage retention and storage wear. CPU, SHA backend scratch, wire framing, trusted root publication durability, client crash recovery, author offline PIN audit and code/initialization costs remain separately priced or **unknown**. No model-independent lower bound is claimed.

## Counterexamples and failure gates

The [reference](../../research/uct005_d1b2f3c_onepass_speculative_pin.py) and [independent finite tests](../../research/test_uct005_d1b2f3c_onepass_speculative_pin.py) exhaust all initial GF(2) words for n=1..5 and P=1,2,64, check every range query, no-op SETs, PIN0/PIN2, both retire stages and exact 7M/11M/7M ledgers; exercise n=33/257 and C=8/17/257 boundary pages, SHA-corrupt but valid-length bitmap (exact M speculative stage writes then M paid drops and zero publisher commits), missing final page (M-1 staged writes/drop), forged internally inconsistent independently trusted PIN token, duplicate same-epoch readers and invalid client input. The full old image digest is always verified **before publication**, even though untrusted staging may already have happened.

A separate F2 crash-prefix oracle proves only a *conditional* stage/publish/retire ordering with ideal durable page writes and atomic trusted publication. This subclass inherits its assumptions but **does not** provide real fsync power-loss evidence, verified stage receipts or rollback-resistant authority implementation. A remote server can withhold, mutate or falsely acknowledge staged writes; correctness after root publication requires stronger storage/atomicity semantics than the Python dict emulator establishes. The class is a research counterexample in a frozen upper-construction grammar.

## Integration and novelty gates

New GitHub-hosted focused workflow plus F2/F3-B inherited regressions, full Research/INDEX/D1-A on exact final head, then sequential predecessor merges. This stacked draft **MUST NOT** merge while F2 or F3-B remains draft/unaccepted. The rooted UCT theorem tree has exactly one organizing parent (F3-B); cross-document source dependencies are not second-parent edges. UCT root #105 **OPEN_UNPROVED**. Next mathematical test: formulate a quantitative same-model adversarial *minimax* tradeoff over failed staging writes versus read passes and permitted abort windows; STOP if it reduces to classical two-pass hash verification or a trivial copying protocol.
