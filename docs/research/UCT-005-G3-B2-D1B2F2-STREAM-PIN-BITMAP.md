# UCT-005 D1-B2-F2 — streamed authenticated remote PIN bitmap and transient trusted buffers

**2026-10-10.** Parent [#281](https://github.com/definitely-stable/Mathlab/issues/281), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223), [D1-B2-E #255](https://github.com/definitely-stable/Mathlab/issues/255). Existing paid reference [D1-B2-D PR #253](https://github.com/definitely-stable/Mathlab/pull/253) and [D1-B2-F resource reconciliation PR #265](https://github.com/definitely-stable/Mathlab/pull/265). Distinct from concurrent COW PIN reachability [D1-B2-F1 PR #272](https://github.com/definitely-stable/Mathlab/pull/272).

**Classification:** CONDITIONAL_STREAMED_F1_UPPER_AND_PEAK_BUFFER_NONTRANSFER. UCT ROOT_OPEN_UNPROVED. This is not an original joint lower bound, measured Python RSS, a cryptographic security theorem, physical page durability, or a full Pareto frontier.

## 1. Why persistent trusted state is not total trusted memory

In the accepted D1-B2-D upper point, the central authority keeps a 40-byte trusted bitmap generation/digest, while the two independent PIN clients retain their own 40-byte historical tokens and the writer retains n bits plus the globally trusted latest anchor. However its full-image read, bytearray copy and new immutable image materialization can reside simultaneously inside the authority in a specific bulk implementation. If the remote membership image has B=ceil(2C/8) bytes, then a **declared three-bitmap-image materialization schedule** has up to 3B conceptual trusted bitmap-byte residency. This is not CPython RSS or a claim that every optimized bulk implementation needs 3B; aliasing and streaming alternatives change the result. The old D1-B2-E upper only froze **persistent** trusted-state bits, not this transient coordinate.

We introduce a *different* fully executable reference program which receives remote bitmap pages into trusted chunk buffers of length at most min(B,P) for a physical P-byte complete-page API. A mutation needs one received page and one mutable updated page at once. In the expressly frozen algorithmic **bitmap buffer** accounting,

\[
M_{\mathrm{stream,bitmap}}\le 2\min(B,P)\ \mathrm{bytes}
\]

versus 3B bytes in the specified bulk three-image-lifetime protocol. The online ledger updates its peak at every chunk and tests equality to the upper schedule. This excludes cryptographic SHA engine/allocator memory, verifier call stack, static program and setup, network TLS framing, Python interpreter objects and server-side staging; **total peak trusted RAM is unknown**, not equal to the bitmap-only bound. No universal memory lower bound is inferred.

## 2. Full same-F1 PIN service, explicit streaming protocol

Same two readers, PAGE-001 immutable 48-byte epoch/data manifest and public fixed-stride snapshot page layout, PIN_CURRENT, no-op SET, LATEST/AS_OF half-open range XOR, UNPIN/GC. A bounded-capacity 2C-bit membership bitmap lives **remotely**, in exactly B=ceil(2C/8) packed bytes occupying M=ceil(B/P) complete remote pages, in its own physical region disjoint from snapshot slots. A separately trusted bitmap generation+SHA256 digest is 40 bytes, in addition to latest anchor, author bits and each client's PIN tokens.

PIN_CURRENT and UNPIN use a **two-pass authenticated immutable-bitmap change**:

1. Read the 40-byte trusted bitmap commitment, stream every remote bitmap page into one trusted at-most-P byte buffer, hash the complete sequence with domain separator and generation, verify against trusted digest, and extract at most the two requested epoch PIN bits. Withholding, malformed length, stale replay and forged contents produce ABORT **before** any PIN publication/revocation.
2. Re-fetch the complete current bitmap again from the **live remote source**, one page at a time, authenticate the second old-image transcript by a second complete SHA256 pass, flip exactly the desired membership bit in a second trusted at-most-P page buffer and stream the resulting pages into a separate **untrusted remote staging object**. Simultaneously hash the next-generation staged bytes. If the second old-image digest differs from the trusted old root (including a malicious replacement between passes), ABORT without changing trusted bitmap commitment or reader-held PIN; staging allocation/reads are charged, never silently counted as a durable published bitmap.
3. Once the second old-image digest has been checked, atomically install the new remote staged image and publish the trusted generation/root in an **ideal serialized authority transaction**. The transaction is not implemented as a crash-safe disk or distributed consensus protocol.

**Every mutating PIN/UNPIN** costs 2M full remote bitmap page reads, one new M-page remote bitmap image write, SHA inputs for both old passes and one new pass, one 40-byte trusted bitmap root update, and transient allocation of another M-page remote staging image. **SET** does not change the PIN bitmap; it costs one M-page authenticated scan and tests both PIN bits for the superseded latest epoch, then writes the unchanged PAGE-001 snapshot in L=ceil(ceil(n/8)/P)+ceil(48/P) full pages. When no PIN remains, reclaim an obsolete snapshot with L addressed 8-byte logical DROP_PAGE commands. Reader-held tokens are never silently dropped. All operations are serialized against the ideal PIN authority.

A bulk D1-B2-D comparison uses one bitmap scan per PIN/UNPIN and one full-image rewrite, so the streaming variant pays one **extra complete M-page read** per mutation (four mutating PIN operations in the common transcript: two PIN and two UNPIN) and a separately counted temporary M-page untrusted stage. It is NOT all-axis cheaper; it changes the resource tradeoff.

## 3. Honest remote correctness and corruption gates

After any completed serialized operation, under the **honest remote page-delete API** assumption, the exact live-epoch set remains latest union actively PINned epochs. The proof is the same elementary case induction accepted for D1-B2-C/D: PIN_CURRENT cannot first-time pin an obsolete epoch; SET retires previous latest iff both verified membership bits are false; UNPIN clears exactly one reader PIN and retires the version iff the other verified bit is false; GC is then vacuous. Latest/AS_OF reads still depend on the separately trusted PAGE-001 anchor and archived root integrity. Neither the SHA256 assumption nor durable atomicity follows from this finite induction.

The streaming reference independently checks that a replacement of the remote bitmap **between pass one and pass two** fails closed without publishing the next trusted root or changing a reader PIN. As with the bulk reference, a malicious server withholding pages may prevent progress; integrity and availability are not the same guarantee.

## 4. Finite exact resource witnesses and scope

For C=4096 and P=2, the 8192 PIN bits occupy B=1024 remote bytes, M=512 pages. The explicitly declared three-image bulk-materialization schedule has 3072 conceptual resident PIN bytes while streaming's online bitmap *chunk* peak is only 4 bytes; each PIN/UNPIN costs **an extra 512 complete bitmap page reads** and transient staging uses an additional 512 remote pages. Both keep the **same persistent trusted root state**, so neither is a uniform Pareto improvement. This is a finite algorithmic schedule, not total client-RAM or observed CPython heap usage.

Independent tests replay all binary words n<=5 at P=1,2,64, the same mandatory no-op, two PIN roots at epochs 0/2, all nonempty query intervals, independent unpin and GC, capacity/race/tamper/replay/withholding gates, a second-pass malicious substitution and complete byte/page conservation at C=8,17,128,256,4096. The unit tests and standalone reproducible report must pass the **exact PR head** in a GitHub-hosted runner; full Research and INDEX CI must also pass. No self-hosted runners, no production code modifications.

## 5. Next novelty gate

D1-B2-F3 should include a fully specified trusted authority heap/call-stack/crypto implementation, network framing, staged page publication/rollback protocol and durable PIN-root CAS semantics. Even then, prior art on streamed authenticated metadata, memory checking, vector commitments and classic time/space tradeoffs must be audited for a **same-task lower-bound reduction**. Do not elevate this useful conditional streaming upper to a new UCT theorem. Root UCT-005 remains OPEN_UNPROVED.
