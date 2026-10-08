# External primary literature — тематический каталог

> Generated from `literature.json` by `research/literature.py`. Редактировать следует только JSON.

Срез: **2026-10-08** · **32** проверенных ссылок на первичные публикации/авторские рукописи.

**Критически важно:** проверенная библиография или авторский abstract не равны независимо проверенному доказательству, статистическому результату либо научной новизне. Точные условия — в каждой записи.

Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md). Внутренние исследования: [INDEX.md](INDEX.md).

| Направление | Записей |
| --- | ---: |
| [Кодирование, ограниченная поддержка, экстремальные границы](#sparse-coding) | 7 |
| [Динамические структуры, каноничность и локальность правок](#dynamic-data-structures) | 5 |
| [Инкрементальные вычисления и сертификаты](#incremental-computation) | 3 |
| [DELSK: поиск delta-базы, сжатие, признаки](#delta-base-selection) | 10 |
| [DeltaMeter: потоковые оценки и согласование множеств](#streaming-reconciliation) | 7 |

## sparse-coding
*Кодирование, ограниченная поддержка, экстремальные границы*

### LIT-001
**[Bounded-Contention Coding for Wireless Networks in the High SNR Regime](https://arxiv.org/abs/1208.6125)** (2012)

Кодирование для декодирования сумм ограниченного числа одновременных сообщений; исходный объект уже близок к бинарному bounded-active identification.

**Ограничение:** Коммуникационная модель и допускаемое число участников отличаются от строгой поддержки столбцов ASET.

**Идентичность:** `arxiv:1208.6125` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-002
**[Location-correcting codes](https://doi.org/10.1109/18.485724)** (1996)

Классическая граница для слабых множеств Сидона используется в Mathlab для строгой конечной оценки 10≤A₅^set(3,2,2)≤11.

**Ограничение:** ASET влечёт weak Sidon, но обратное неверно; correction locality из LCC не равна write locality ASET.

**Идентичность:** `doi:10.1109/18.485724` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-008](INDEX.md#ml-008), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md) (cited)

### LIT-003
**[Probabilistic existence results for separable codes](https://arxiv.org/abs/1505.02597)** (2015)

Blackburn сопоставляет frameproof и t-separable коды и устанавливает вероятностные границы; приводит специальные ограничения при t=2.

**Ограничение:** Descendant-модель не совпадает автоматически с ограниченными конечнополевыми суммами и изменяемой поддержкой ASET.

**Идентичность:** `arxiv:1505.02597` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-004
**[Bounds and Constructions for 3-Separable Codes with Length 3](https://arxiv.org/abs/1507.00954)** (2015)

Границы и конструкции именно для 3-separable кодов длины 3, через partial Latin squares, perfect hashing и Steiner triple systems.

**Ограничение:** ВАЖНО: статья о t=3, а не непосредственно о 2-separable/ASET d=2; пересечение методологическое.

**Идентичность:** `arxiv:1507.00954` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-005
**[Sharp bounds for uniform union-free hypergraphs](https://arxiv.org/abs/2605.11949)** (2026)

Асимптотические экстремальные результаты для t-union-free r-однородных гиперграфов, а также разреженные упаковки.

**Ограничение:** Совпадение объединений рёбер не тождественно совпадению модульных сумм в GF(q); особенно осторожно при нечётной характеристике.

**Идентичность:** `arxiv:2605.11949` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-006
**[On Codes with Support-Constrained Parity Checks](https://arxiv.org/abs/2605.08644)** (2026)

Оптимальное минимальное расстояние линейного кода при заданной маске поддержки строк проверочной матрицы; конструкции над достаточно большими полями.

**Ограничение:** Строковые parity-check ограничения и расстояние кода не дают автоматически границы мощности ASET со столбцовыми ограничениями.

**Идентичность:** `arxiv:2605.08644` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-031
**[Signature Codes for a Noisy Adder Multiple Access Channel](https://arxiv.org/abs/2206.10735)** (2022)

q-арные signature codes для noisier integer-adder multiple access, включая явные конструкции и converse bounds.

**Ограничение:** Сумма берётся над целыми и учитывает канал с шумом, в отличие от безошибочной конечнополевой ASET-суммы.

**Идентичность:** `arxiv:2206.10735` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (model_overlap)


## dynamic-data-structures
*Динамические структуры, каноничность и локальность правок*

### LIT-007
**[History-Independent Dynamic Partitioning: Operation-Order Privacy in Ordered Data Structures](https://doi.org/10.1145/3651609)** (2024)

Динамические группы размера Θ(B) с O(1) ожидаемым числом операций вставки/удаления против oblivious adversary.

**Ограничение:** Операции по группам не равны физически переписанным байтам; нельзя усиливать модель до adaptive adversary без доказательства.

**Идентичность:** `doi:10.1145/3651609` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-008
**[History-Independent Dynamic Partitioning with Applications to B-Trees, Skip Lists and Fusion Trees](https://doi.org/10.1145/3810240)** (2026)

Расширенная версия истории-независимого разбиения с применениями к B-tree, fusion tree и skip list.

**Ограничение:** Не утверждает строгую каноничность физических байтов persistent rope или худший случай против адаптивного противника.

**Идентичность:** `doi:10.1145/3810240` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-009
**[The Chonkers Algorithm: Content-Defined Chunking with Strict Guarantees on Size and Locality](https://arxiv.org/abs/2509.11121)** (2025)

Предложены одновременные строгие гарантии длины CDC-чанков и локальности правок; обсуждается структурное представление Yarn.

**Ограничение:** Авторский preprint; модель частичных изменений, byte writes и deterministic canonical physical layout нужно сопоставлять отдельно.

**Идентичность:** `arxiv:2509.11121` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-011
**[Optimal Time-Space Tradeoff for Dynamic Difference-Encoded Dictionaries](https://arxiv.org/abs/2608.06077)** (2026)

Гарантии сжатого gap-encoded словаря с динамическими операциями и сопоставимой нижней границей.

**Ограничение:** Стоимость ориентируется на gap(S), а не на history-independent физическое расположение и на write locality после string edits.

**Идентичность:** `arxiv:2608.06077` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-012
**[Time-Optimal Construction of String Synchronizing Sets](https://doi.org/10.4230/LIPIcs.STACS.2026.36)** (2026)

Оптимальное по word-RAM времени построение позиций синхронизации с локальной согласованностью контекстов строки.

**Ограничение:** Результат для статической подготовки/конструкции, не готовая динамическая worst-case гарантия редактирования CDC.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.36` · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)


## incremental-computation
*Инкрементальные вычисления и сертификаты*

### LIT-010
**[Incremental Computing by Differential Execution](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20)** (2025)

Дифференциальная семантика инкрементальных вычислений с формально проверенными свойствами корректности и оптимизациями циклов.

**Ограничение:** Корректность изменения вычисления не равна минимальной длине сертификата unchanged и lower bound на cell probes.

**Идентичность:** `doi:10.4230/LIPIcs.ECOOP.2025.20` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-013
**[Change actions: from incremental computation to discrete derivatives](https://arxiv.org/abs/2002.05256)** (2020)

Алгебраический аппарат change actions для композиционной семантики дискретных производных и инкрементальных запросов.

**Ограничение:** Общее правило композиции изменений не обеспечивает корректность объединения отдельно выданных сертификатов no-effect.

**Идентичность:** `arxiv:2002.05256` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-032
**[Bounded Incremental Computation](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/)** (1993)

Ramalingam исследует сложность инкрементального перерасчёта относительно размеров изменений ввода и вывода.

**Ограничение:** Сам output-sensitive cost не является новой нижней границей метаданных no-effect сертификата.

**Идентичность:** `publisher:msresearch:ramalingam:1993` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)


## delta-base-selection
*DELSK: поиск delta-базы, сжатие, признаки*

### LIT-014
**[Finesse: Fine-Grained Feature Locality based Fast Resemblance Detection for Post-Deduplication Delta Compression](https://www.usenix.org/conference/fast19/presentation/zhang)** (2019)

Чанки делятся на subchunks, признаки агрегируются в super-features для поиска delta-базы; обязательный классический baseline DELSK.

**Ограничение:** Показатель resemblance не эквивалентен реальной длине патча; оригинальный first-fit и переосмысленные реализации отличаются.

**Идентичность:** `usenix:fast19:zhang` · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-009](INDEX.md#dl-009)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-015
**[DeepSketch: A New Machine Learning-Based Reference Search Technique for Post-Deduplication Delta Compression](https://www.usenix.org/conference/fast22/presentation/park)** (2022)

Обучаемые sketch-признаки и approximate-nearest-neighbor поиск; обучение учитывает delta-compression ratio конкретного кодера.

**Ограничение:** Идея codec-aware выбора баз уже имеется; цифры авторских бенчмарков не воспроизведены в DELSK.

**Идентичность:** `usenix:fast22:park` · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-009](INDEX.md#dl-009)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-016
**[Palantir: Hierarchical Similarity Detection for Post-Deduplication Delta Compression](https://doi.org/10.1145/3620665.3640353)** (2024)

Иерархические super-features, отбрасывание ложных delta-кандидатов и учёт временной локальности backup-потока.

**Ограничение:** Заявленные улучшения относятся к конкретным датасетам и кодерам; не означают универсальный оптимальный выбор базы.

**Идентичность:** `doi:10.1145/3620665.3640353` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-009](INDEX.md#dl-009)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-017
**[The Design of Fast and Lightweight Resemblance Detection for Efficient Post-Deduplication Delta Compression](https://doi.org/10.1145/3584663)** (2023)

Журнальная версия Odess: content-defined sampling, SIMD-ускорение rolling hash и сравнение с transform-based аналогами.

**Ограничение:** Техника ускоряет поиск resemblance, а не доказывает качество нового scorer DELSK; показатели 2021 и 2023 не смешиваются.

**Идентичность:** `doi:10.1145/3584663` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-018
**[SpeedSketch: An Ultra-Fast Sketch Generation and Delta Encoding Framework for Delta Compression](https://doi.org/10.1145/3754598.3754628)** (2025)

Объединяет sketch-поиск delta-базы с ускорением delta-encoding, включая фильтрацию экономически невыгодных случаев.

**Ограничение:** Прирост кодирования нельзя без контроля декомпозиции приписывать только точности поиска; репозиторий и статья используют разные параметры CDC.

**Идентичность:** `doi:10.1145/3754598.3754628` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-019
**[FastCDC: A Fast and Efficient Content-Defined Chunking Approach for Data Deduplication](https://www.usenix.org/conference/atc16/technical-sessions)** (2016)

Gear-based content-defined chunking, пропуск недопустимо коротких разрезов и нормализация длин.

**Ограничение:** FastCDC — chunk-boundary baseline, не новая модель оптимальной направленной delta-базы и не строгая история-независимая партиция.

**Идентичность:** `usenix:atc16:xia` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-020
**[On the Resemblance and Containment of Documents](https://doi.org/10.1109/SEQUEN.1997.666900)** (1997)

Broder: независимое сэмплирование fingerprints для resemblance и асимметричного containment.

**Ограничение:** Направленный containment давно известен; не означает предсказания patch bytes у конкретного codec.

**Идентичность:** `doi:10.1109/SEQUEN.1997.666900` · **Проверка:** `author_paper_or_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-009](INDEX.md#dl-009)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-021
**[LSHBloom: Memory-efficient, Extreme-scale Document Deduplication](https://arxiv.org/abs/2411.04257)** (2024)

Замена тяжёлого MinHash-LSH индекса Bloom filters для крупномасштабной дедупликации документов.

**Ограничение:** False-positive rate и savings относятся к document-level dedup, не прямо к содержимому delta patch.

**Идентичность:** `arxiv:2411.04257` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-002](INDEX.md#dl-002), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md) (cited)

### LIT-022
**[FED: Fast and Efficient Dataset Deduplication Framework with GPU Acceleration](https://arxiv.org/abs/2501.01046)** (2025)

Оптимизация генерации MinHash/LSH сигнатур на GPU-кластерах с переиспользованием дешёвых хэшей.

**Ограничение:** Опыт GPU-LLM текстовой дедупликации не переносится без тестов на ограниченный CPU descriptor DELSK.

**Идентичность:** `arxiv:2501.01046` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-002](INDEX.md#dl-002), [DL-007](INDEX.md#dl-007)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md) (cited)

### LIT-030
**[Odess: Speeding up Resemblance Detection for Redundancy Elimination by Fast Content-Defined Sampling](https://doi.org/10.1109/ICDE51399.2021.00048)** (2021)

Оригинальная конференционная работа Odess про fast content-defined sampling для ускорения resemblance.

**Ограничение:** Версия ICDE 2021 отличается от журнала ACM TOS 2023 по экспериментальной конфигурации/цифрам.

**Идентичность:** `doi:10.1109/ICDE51399.2021.00048` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)


## streaming-reconciliation
*DeltaMeter: потоковые оценки и согласование множеств*

### LIT-023
**[Probabilistic Counting in Generalized Turnstile Models](https://arxiv.org/abs/2310.14977)** (2023)

Dingyu Wang: F-PCSA для конечнополевых turnstile-обновлений, включая GF(2); опубликованная конструкция воспроизведена в DeltaMeter.

**Ограничение:** Из асимптотической относительной ошибки не следует строгая one-sided finite-sample coverage для данного d.

**Идентичность:** `arxiv:2310.14977` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-002](INDEX.md#dm-002), [DM-003](INDEX.md#dm-003)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/M2-FPCSA-REPRODUCTION.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/M2-FPCSA-REPRODUCTION.md) (cited)

### LIT-024
**[The Space Complexity of Approximating the Frequency Moments](https://doi.org/10.1145/237814.237823)** (1996)

Alon–Matias–Szegedy: foundational stream sampling/sign sketches for frequency moments F₂.

**Ограничение:** Обычный F₂ turnstile не тождественен обещанию set-only GF(2) Hamming/L₀ после XOR обновлений.

**Идентичность:** `doi:10.1145/237814.237823` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-001](INDEX.md#dm-001), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (cited)

### LIT-025
**[Information Theoretic Limits of Cardinality Estimation: Fisher Meets Shannon](https://arxiv.org/abs/2007.08051)** (2020)

Pettie–Wang вводят Fish-number, сравнивающий предельную энтропию состояния и Fisher information у cardinality estimators.

**Ограничение:** Fish-number/asymptotic statistical efficiency не даёт конечновыборочной one-sided гарантии ParityDeltaMeter.

**Идентичность:** `arxiv:2007.08051` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-003](INDEX.md#dm-003), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (cited)

### LIT-026
**[Simple Set Sketching](https://arxiv.org/abs/2211.03683)** (2022)

Три независимых XOR таблицы и гиперграфовый peel decoder позволяют восстанавливать малое множество ниже порога загрузки с высокой вероятностью.

**Ограничение:** Вероятностная успешная декодируемость не тождественна unconditional exact coverage для любых ключей.

**Идентичность:** `arxiv:2211.03683` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-006](INDEX.md#dm-006), [DM-008](INDEX.md#dm-008)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (cited)

### LIT-027
**[Practical Rateless Set Reconciliation](https://doi.org/10.1145/3651890.3672219)** (2024)

Rateless IBLT передаёт возрастающий prefix coded symbols до получения set difference, сравним с инкрементальным PinSketch по протоколу.

**Ограничение:** Число символов не равно байтам на проводе: symbol/hash/count/framing следует учитывать явно.

**Идентичность:** `doi:10.1145/3651890.3672219` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-006](INDEX.md#dm-006), [DM-008](INDEX.md#dm-008)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/M6-D2-RIBLET-COMPARATOR.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D2-RIBLET-COMPARATOR.md) (cited)

### LIT-028
**[Memory-Sample Tradeoffs for Linear Regression with Small Error](https://arxiv.org/abs/1904.08544)** (2019)

Sharan–Sidford–Valiant: нижняя граница числа noisy Gaussian samples при субквадратичном числе битов памяти.

**Ограничение:** Есть ненулевой шум; более поздний OM-140 noiseless результат является отдельной теоремой, не прямым уточнением в той же модели.

**Идентичность:** `arxiv:1904.08544` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)

### LIT-029
**[Space lower bounds for linear prediction in the streaming model](https://arxiv.org/abs/1902.03498)** (2019)

Dagan–Kur–Shamir: квадратичная по размерности потребность в памяти для конкретных линейных streaming inference задач.

**Ограничение:** Это не универсальное cell-probe ограничение для сертификатов неизменности DAG.

**Идентичность:** `arxiv:1902.03498` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)
