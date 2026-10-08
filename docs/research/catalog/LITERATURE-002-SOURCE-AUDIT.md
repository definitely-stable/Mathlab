# RESEARCH-LITERATURE-002 — библиографический аудит и расширение

**Дата:** 2026-10-08 · [Issue #47](https://github.com/definitely-stable/Mathlab/issues/47)  
**Решение:** IMPORT_PRIMARY_METADATA; mathematical novelty / re-proven theorem: **NONE**.  
[Основной список литературы](LITERATURE.md) · [Обратный индекс](LITERATURE-BY-RESEARCH.md) · [Машинный реестр](literature.json)

## 1. Результат и точность формулировок

Корпус увеличен с **32 до 49 самостоятельных публикаций** (+17, идентификаторы LIT-033..LIT-049). Пять направлений: 14 — sparse coding, 5 — dynamic structures, 6 — incremental computation, 13 — delta/base-selection, 11 — streaming/reconciliation. Прежний каталог **61 внутренней исследовательской записи не менялся**. Ни один новый математический результат не был заявлен, G2B-B2 не редактировался.

Входной DOI/arXiv проверяется по семантике заглавия и заявленной математической модели там, где изучался первичный abstract/страница издателя. `verification` — это ограниченный уровень **метаданных и abstract**, не сертификат проверки математического доказательства. PDF-тексты и код не включаются в репозиторий. CI работает офлайн, проверяет только модель метаданных и детерминированные представления.

### Исправленные ошибки прошлого импорта

| Запись | Ошибка или риск | Исправление и источник |
| --- | --- | --- |
| [LIT-022](LITERATURE.md#lit-022) | `arxiv:2501.01046` ранее ошибочно назван FED | **SEDD: Scalable and Efficient Dataset Deduplication with GPUs**, Youngjun Son, Chaewon Kim, Jaejin Lee. [Оригинальная страница arXiv](https://arxiv.org/abs/2501.01046). Уточнён model scope GPU MinHash dedup |
| [LIT-004](LITERATURE.md#lit-004) | «3-separable» ошибочно сглаживало `overline{3}` | В заглавии теперь **overline-3-Separable**; barred-3 — особое определение, не `d=2` ASET. [Первичный arXiv](https://arxiv.org/abs/1507.00954) |
| [LIT-009](LITERATURE.md#lit-009) | Пропущено *Provable* в заглавии Chonkers | Название приведено к [arXiv:2509.11121](https://arxiv.org/abs/2509.11121) |
| [LIT-019](LITERATURE.md#lit-019) | Ссылка указывала на всю конференцию, а не конкретную статью FastCDC | Прямая [официальная копия USENIX](https://www.usenix.org/system/files/conference/atc16/atc16-paper-xia.pdf) |
| [LIT-027](LITERATURE.md#lit-027) | RIBLT имел только DOI, рисковал дублированием при импорте arXiv | Добавлен **альтернативный arXiv:2402.02668** для *той же* работы SIGCOMM 2024 |
| [LIT-039](LITERATURE.md#lit-039) | Оригинальный IBLT доступен и как arXiv, и как публикация Allerton | Одна запись: `arxiv:1101.2245` + alias `doi:10.1109/ALLERTON.2011.6120248`, без двойного счёта |

`SOURCE_TITLE_PINS` охраняет ключевые восстановленные заглавия. Валидатор отклоняет `alternate_identities`, совпадающие с canonical/aliases другой публикации.

## 2. 17 новых работ и их функция

| Новые LIT IDs | Тема, установленные первичные формулировки | К каким исследовательским границам относятся |
| --- | --- | --- |
| 033 / 034 | [Sign-Compute-Resolve](https://arxiv.org/abs/1602.02612), [Finite Field Multiple Access](https://arxiv.org/abs/2303.14086) | Суммирующие каналы и конечнополевые signature codes, **не** автоматически ASET hard-support bounds |
| 035 / 036 | [Weighted adder signatures](https://arxiv.org/abs/1905.10180) и [constant-weight binary B2-sequences](https://arxiv.org/abs/2303.12990) | Coefficient alphabet, repeated summands vs distinct subsets, finite-field characteristic |
| 037 | [Arithmetic multi-group testing](https://arxiv.org/abs/1303.6020) | Реальные weighted queries против GF(q) |
| **043** | [Lefmann, sparse parity-check GF(q), 2005](https://doi.org/10.1017/S0963548304006625) | **Высокий приоритет HYP-001/002:** почти совпадает столбцовая поддержка, но linear independence намного сильнее/иначе restricted ± collisions |
| **044** | [Bshouty–Mazzawi, parity check 0/1 over Z_p, 2015](https://doi.org/10.1137/120881129) | K-wise independence и additive queries; другая support/coefficient спецификация |
| 038 | [Chunk-context aware resemblance](https://arxiv.org/abs/2106.01273) | DELSK: контекст и местоположение в дополнение к fingerprints |
| 048 / 049 | [Binary fuse filter](https://arxiv.org/abs/2201.01174), [FXLT](https://arxiv.org/abs/2312.13541) | DELSK: недорогой metadata prefilter и probabilistic map, **не** направленное ранжирование патча |
| 039 / 040 | [Original IBLT](https://arxiv.org/abs/1101.2245), [IBLT listing guarantees](https://arxiv.org/abs/2212.13812) | DeltaMeter: вероятностное восстановление vs hard guarantee for bounded sets |
| **042** | [XYZ-Sketch, 2026](https://arxiv.org/abs/2609.14442) | DeltaMeter: close communication/update-time comparator; claimed optimality **conditional** on unproven conjecture |
| 047 | [Tight low-error F₂ bounds, 2025](https://arxiv.org/abs/2509.07599) | DeltaMeter: low-error F₂ in specific streaming pass model, not strict GF(2) cardinality coverage |
| 041 / 045 / 046 | [Certificates in Data Structures](https://arxiv.org/abs/1404.5743), [Complexity Models](https://doi.org/10.1016/0304-3975(94)90159-7), [Incremental Lower Bounds](https://doi.org/10.7282/T3HT2SXD) | TOM: static cell-probe query certificates, dynamic incremental computation and δ-analysis are **different** cost models |

### Strongest primary-source comparisons

1. **Lefmann** permits max r nonzeros *per column* in GF(q) parity-check matrix but requires any k columns to be independent. ASET forbids only particular signed short relations with distinct original elements and a very specific bound on both sides. Directly copying Lefmann exponents as ASET upper bounds is unjustified. Conversely, his constructions may become *sufficient* ASET families for certain k if carefully reduced — **not a novelty claim**.
2. **Bshouty–Mazzawi** gives GF(p) independence and ordinary additive signature coding with (0,1) entries; this is an important precedent against claiming an original general finite-field sparse decoder.
3. **XYZ-Sketch** already proposes the conjunction near-optimal payload, constant update and efficient decoding. Its fixed-support optimality is **under an explicit open conjecture**. No unconditional lower bound from this manuscript is claimed and practical metadata costs must be measured separately.
4. **Original IBLT and worst-case guaranteed listing** must not be conflated. Original random hash implementation can fail; worst-case guarantees require a specific design and restricted set cardinality.
5. **SEDD vs FED** is not a stylistic naming issue: misidentifying arXiv creates misleading prior-art provenance. Regression tests now explicitly falsify that error.

## 3. Quality protocol: what was checked

- Existing source IDs LIT-001–032 preserved. Four problematic titles/citations/identities were corrected directly, plus an original-paper URL; strict duplicate checks introduced.
- Added relevant works from actual earlier Mathlab/DELSK/DeltaMeter references, plus clearly marked `model_overlap` references. `cited` retains *literal* occurrence semantics only.
- External abstracts/titles were checked at source arXiv, author/institution/publisher landing pages. Not every 49-article bibliography was re-read fully: previous provenance and `verification` tiers are preserved.
- No automated browsing in GitHub CI; no DOI registration timing/freshness guarantee; no claim of exhaustive world-literature search.
- Added regression tests for alias collisions, first-party title errors, source traceability, existing downstream research IDs, consistency of both generated documents and prohibiting false theorem/reproduction promotion.

## 4. Next best research questions (outside G2B-B2)

**Priority A — Mathlab.** Definition-level reduction grid for Lefmann (2005), Bshouty–Mazzawi (2015), barred-3 separable codes and constant-weight B₂ to the *exact ASET (d=2)* relation. Extract admissible reductions, counterexamples, exact leading constants and proof novelty status; see issue #25. Avoid an unjustified «мы первые доказали Θ(m²)».

**Priority B — DeltaMeter.** Separate rate-compatible transmission `(1+ε)d` **elements** from real bytes and decode CPU. Compare XYZ-Sketch/RIBLT/IBLT guaranteed listing against D13B system-NO-GO, not via headline numbers.

**Priority C — DELSK.** Test whether chunk-context and probabilistic prefilters provide independent benefit after already-known Finesse/DeepSketch/Palantir and actual codec-aware benchmarks; do not revive an unproven novelty story.

**Acceptance:** 49 work records; no theorem-status promotions; no G2B-B2 edits; post-merge GitHub-hosted CI must pass at exact main commit.
