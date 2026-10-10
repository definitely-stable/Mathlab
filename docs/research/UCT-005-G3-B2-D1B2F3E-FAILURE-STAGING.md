# UCT-005 D1-B2-F3-E — failed PIN update, speculative writes and authenticated-stage recovery

2026-10-11. [Research issue #299](https://github.com/definitely-stable/Mathlab/issues/299), [root #105](https://github.com/definitely-stable/Mathlab/issues/105), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). Upstream F2 two-pass [#283](https://github.com/definitely-stable/Mathlab/pull/283) and F3-C one-pass [#294](https://github.com/definitely-stable/Mathlab/pull/294) have merged. F3-D [#298](https://github.com/definitely-stable/Mathlab/pull/298) is a pending research predecessor. **Classification: PREVERIFICATION_FAILURE_STAGE_AMPLIFICATION / RESTRICTED_CONSTRUCTION_COUNTERMODELS / STOP_NOVELTY / UCT_ROOT_OPEN_UNPROVED.**

## What the successful-transcript comparison alone misses

The accepted same-F1 history gives 11M authenticated remote bitmap page reads for F2's two-pass bitmap mutation versus 7M for F3-C's speculative single-pass. This does not compare malicious failures or retries. Model M=ceil(ceil(2C/8)/P), where C is bounded number of epochs, P is a complete physical page size.

For an old bitmap where the served **full-size canonically padded bytes do not match the trusted SHA digest**, F2's *first SHA scan* reads all M pages and aborts before stage writes. F3-C's speculative scan reads the same M pages but sends M P-byte **untrusted stage writes** before discovering the SHA failure; it then issues M DROP_PAGE requests (eight-byte addresses). Both leave trusted root, PIN tokens and current epoch unchanged. This is not a cryptographic acceptance forgery.

For a missing page at zero-based position j, both attempt j+1 reads. F2 stages 0 pages. F3-C has staged exactly j pages, and pays j cleanup requests. For a noncanonical final-page padding byte, the corresponding F3-C staging prefix is M−1 pages. These are exact byte-level identities in these **specific reference algorithms**, not a lower bound over all verification policies.

| Adversarial event | F2 two-pass | F3-C one-pass speculative |
|---|---|---|
| Existing SHA-invalid old bitmap | M reads, 0 stage writes | M reads, M stage writes, M cleanup drops |
| Withheld old bitmap page j | j+1 reads, 0 stage writes | j+1 reads, j writes, j drops |
| Noncanonical final padding | M reads, 0 writes | M reads, M−1 writes and drops |
| Old page maliciously changes between pass1 and pass2 | 2M F2 reads, M tentative writes/drops before second SHA ABORT | Not applicable: no second pass |
| Tampered active bitmap after trusted publication | Future authenticated SET rejects; cannot guarantee availability | Same fail-closed boundary, no availability guarantee |

**Critical scope correction:** It would be false to say F2 *never* stages pages during a failed mutation. If a malicious remote changes complete page bytes between F2's already-verified first scan and its second scan, F2 may write all M new pages, only then reject the rechecked old hash and pay M stage-drop calls. This is separately reproduced, not conflated with PREEXISTING SHA-invalid input.

## Additional denial-of-service and liveness boundary

With k failed attempts against persistently SHA-invalid old bitmap bytes, F3-C stages and drops kM pages, uploads kMP bytes and sends 8kM cleanup address bytes with zero trusted root publications. In an unbounded retry horizon, the failure-side cost has no bound independent of k, but this is merely repeated wasted work, not a novel complexity theorem. A remote server may withhold stage writes/receipts, refuse deletes or corrupt an active slot after publication. Future authenticated operations will fail closed under the modeled digest; full honest liveness, durable storage, availability and crash recovery are NOT established. Old PIN client token remains independently trusted but an unavailable snapshot still cannot be read.

Remote pages in the Python reference are honest byte dictionaries except for *specific injected attacks*. The conditional recovery guarantee assumes honest cleanup, complete P-byte staging and ideal atomic trusted authority publication. Do not cite this as a real power-loss, rollback or fsync theorem, or as measured CPython RAM.

## Reproducibility and research-stop decision

[Reference auditor](../../research/uct005_d1b2f3e_failure_amp.py) separately constructs the two accepted classes; counters are read from actual execution, not simply populated by expected formulas. [Independent tests](../../research/test_uct005_d1b2f3e_failure_amp.py) cover C=8/17/257, P=1/2/64, every missing page index for selected small M, SHA invalid with valid full-page framing, malformed page padding, changes during F2 pass2, post-publication remote tampering and k=1/2/5 failed retries. All controls check trusted (generation,digest), independent PIN tokens, exact P-byte write volume, 8-byte cleanup request addresses and full stage clearance after ABORT.

No information-theoretic innovation is claimed: this is the classical schedule risk of **copy-before-verify versus verify-before-copy**, with F2's secondary TOCTOU risk explicitly priced. The desired UCT-005 theorem is **not** obtained by subtracting 11M−7M on an honest history or adding this failure-side write amplification to independent static lower bounds.

The single organizing theorem-tree parent is F3-D, *not* a proof implication; independent scientific sources remain F2 and F3-C. Accept only after predecessor #298 integration and final-head GitHub-hosted focused + Research/INDEX/D1-A and post-main gates. Root #105 remains `OPEN_UNPROVED`.
