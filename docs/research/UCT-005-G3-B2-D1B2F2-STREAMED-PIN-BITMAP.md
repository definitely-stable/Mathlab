# UCT-005 D1-B2-F2: streamed two-pass remote PIN bitmap and paid staging

2026-10-10. [Issue #281](https://github.com/definitely-stable/Mathlab/issues/281), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223), accepted [D1-B2-D](../../research/uct005_d1b2d_remote_pin_bitmap.py), [reference](../../research/uct005_d1b2f2_streamed_pin_bitmap.py), [tests](../../research/test_uct005_d1b2f2_streamed_pin_bitmap.py).

**Conditional finite page-image upper construction, not real-RAM/crypto/crash-safety proof. ROOT_OPEN_UNPROVED.**

## Missing resource axis

Baseline D1-B2-D retains 40 trusted persistent bitmap-root bytes (generation+SHA256), but its bulk read and mutate retain B=ceil(2C/8) bytes and a complete copy in trusted algorithmic working memory. A persistent-space claim does not price peak transient RAM. Actual runtime RSS and buffer lifetimes are NOT inferred.

## Physical grammar, two passes and trust boundary

Two public fixed-address bitmap regions, each M=ceil(B/P) complete P-byte pages, precede all PAGE-001 epoch slots. The trusted bitmap generation parity selects the active region; the other is transient staging, not a free object map. Remote pages include zero-checked canonical last-page padding. A page read costs one P-byte transfer plus eight addressed-request bytes.

Setup writes M zero page images and incrementally hashes domain || generation 0 || B bitmap bytes; bounded bitmap-page setup scratch. Every PIN_CURRENT/UNPIN first authenticates the entire remote M-page image with the previously trusted 40-byte generation/digest (pass 1). Pass 2 reads the M pages again, rehashes the old generation, applies one PIN bit change to a single current page, hashes the new generation and writes M full remote stage pages. The trusted authority publishes its new digest/generation and client PIN token only after pass-2 old hash equals the expected digest. If verification fails, stage-addressed DROP_PAGE controls are charged and trusted state is unchanged. The model assumes ideal serialized remote staging/authority publication; it does not prove real crash recovery.

Each PIN/UNPIN: 2M remote bitmap page reads, M staging page writes, up to 2M simultaneous bitmap page images at staging peak, full P-byte uploads, trusted SHA root publish and charged addressed retire/drop calls. SET performs one M-page authenticated bitmap pass, no bitmap stage writes, then uses the same immutable PAGE-001 historical snapshot and eager reclaim rules. LATEST and AS_OF use inherited independently authenticated GF(2) range parity. Two historical offline reader PIN tokens remain separate 40-byte client roots. An offline audit scans each bounded epoch with separately charged page reads; that diagnostic is not used as a free online lookup.

**Narrow scratch bound:** the conceptual algorithmic bitmap payload buffer residency is at most 2*min(B,P) bytes for old/new page images. This EXCLUDES SHA context, root/reader tokens, stack/call frames, allocator overhead, network buffering/retries, control bytes and any real Python heap implementation. Remote Python dictionaries model untrusted server pages, not trusted RAM. Thus this is O(P) bitmap scratch when P<=B, NOT O(P) total trust and NOT a CPython RSS bound.

## Threat and novelty stops

Missing, modified, replayed, truncated or noncanonical remote bitmap data fails authentication, with a second-pass check guarding changes after pass 1, subject to SHA-256 collision resistance and the ideal serialized authority. A malicious server may withhold availability, retain discarded data or crash between staging and publication; no SSD TRIM, atomic filesystem pages, fsync ordering, general crypto reduction, concurrent-process CAS or durable restoration theorem is claimed.

No strict Pareto theorem follows from a lower bitmap scratch bound: the protocol pays an additional remote pass, staging write, extra peak pages, and page deletion traffic. Remaining D1-B2-F total trusted/CPU/network/durability axes are unknown. UCT root #105 remains OPEN_UNPROVED.

## Reproduce

From repo root: python -m unittest discover -s research -p 'test_uct005_d1b2f2_streamed_pin_bitmap.py' -v

Also: python research/uct005_d1b2f2_streamed_pin_bitmap.py

Independent finite oracle tests all GF2 initial words n=1..5, every nonempty half-open interval, two historical reader PINs, mandatory no-op middle SET, P=1/2/64, UNPIN, staged second-pass mutation, missing/replay/truncated/noncanonical page, and conceptual page scratch bound. Hosted focused and full Research CI on exact PR HEAD are acceptance gates.

## Independent finite crash-prefix safety boundary (2026-10-10)

The additional [F2 crash-prefix model](../../research/uct005_d1b2f2_crash_prefix.py) and [separate regression oracle](../../research/test_uct005_d1b2f2_crash_prefix.py) freeze the two-slot publication sequence for the SAME bitmap bytes, fixed page size P, and generation/digest authority as the streamed reference. Let B=ceil(2C/8) and M=ceil(B/P), with old slot holding authenticated image X, target slot holding X' with one updated PIN bit. The legal transition is **M completely written durable stage page images → one atomic trusted generation/digest publication → M individually addressed old-slot page retirements**. Both the old and new generation images include domain separation and u64 generation in the SHA input. All P-byte page transfers and 8-byte retirement requests are separately counted.

**Restricted ordering lemma:** for each of the exactly 2M+2 crash cuts (including before the first and after the last operation), the slot designated by the durable trusted root contains the complete authenticated image: for cuts 0..M, old X; for cuts M+1..2M+1, new X'. Proof is by prefix cases: no old page is retired until after root publication, and every new page is written before that publication. Recovery consults ONLY the trusted generation-selected physical region; it must not silently fall back to the other region. Page truncation, omission, noncanonical padding or hash mismatch yields ABORT under the SHA-binding premise.

**Necessary-order negative controls:** publish root before all stage pages and crash after the premature publication -> trusted new region incomplete; retire old region before trusted publication and crash -> trusted old region incomplete. Both reject. Direct tests tamper, withhold and invalidate last-page padding at both sides of publication. Independently reconstruct the fully committed bitmap from the existing `StreamedPinBitmapF1` remote page images, digest, generation and staging/retirement ledgers, rather than simply calling the reference implementation's transition again.

The result is an **abstract conditional safety statement** assuming atomic, trusted publication; atomic full-page images; durability and ordering of every stage write before publication; and retirement only after publication. It is **NOT a proof that the current Python class persists pages across a crash**, nor an fsync/SSD/OS atomicity theorem, rollback-resistant trust infrastructure, distributed concurrency theorem, availability promise or novel UCT lower bound. Actual durable crash-recovery integration and transient total-RAM accounting remain separate blockers.

GitHub-hosted dedicated and full Research tests on exact PR HEAD remain mandatory. ROOT_OPEN_UNPROVED.
