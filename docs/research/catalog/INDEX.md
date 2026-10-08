# Research index — проверяемый каталог

> Generated from `registry.json` by `research/catalog.py`. Edit JSON, not this file.

Snapshot: **2026-10-08**. **51** selected entries; curated, not exhaustive.

Обозначения: `EXTERNAL_MANUSCRIPT_CLAIM` — только заявление каталога автора,
не независимо подтверждённая теорема. `EXACT_NUMERICAL` и `EMPIRICAL_RESULT`
не подтверждают асимптотическую новизну. Политика: [README](README.md).

| Источник | Записей | Раздел |
| --- | ---: | --- |
| Mathlab | 11 | [MATHLAB](#mathlab) |
| DELSK / Shift-lab | 12 | [DELSK](#delsk) |
| DeltaMeter | 14 | [DELTAMETER](#deltameter) |
| openai/math | 14 | [OPENAI_MATH](#openai-math) |

## MATHLAB

### ML-001
**Разреженные обновления: ограничение достижимых состояний**

Базовая граница: число различных малых множеств не превосходит объёма q-ичной сферы Хэмминга радиуса dw при обновлении не более w координат.

**Статус:** `DERIVED_RESULT` · **Проверка:** `repository_proof` · **Темы:** coding, lower-bounds, locality

**Применение:** Калибровка trade-off состояния и локальности. **Ограничения:** Граница подсчёта сама по себе не нова; не даёт matching construction.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-FOUNDATION.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-FOUNDATION.md) · первичные источники: —

**Связи →** [ML-002](#ml-002) (constrained_by), [DM-001](#dm-001) (related) · **Обратные ссылки ←** [DM-001](#dm-001) (related), [ML-002](#ml-002) (audits), [ML-003](#ml-003) (tests), [OM-119](#om-119) (conceptual_link)

### ML-002
**ASET: аудит новизны и разделение характеристик**

Отсекает общую новизну bounded-active signature coding; для q=2 фиксирует связь с бинарными кодами, для нечётных характеристик оставляет узкую задачу при жёсткой поддержке.

**Статус:** `PRIOR_ART_AUDIT` · **Проверка:** `primary_source_review` · **Темы:** coding, prior-art

**Применение:** Ограничивает допустимые научные claims. **Ограничения:** Отсутствие эквивалентного источника не доказывает новизну будущих оценок.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-G1B-AUDIT-03-FINAL.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-G1B-AUDIT-03-FINAL.md) · первичные источники: [1](https://arxiv.org/abs/1208.6125), [2](https://arxiv.org/abs/2605.08644)

**Связи →** [ML-001](#ml-001) (audits), [ML-003](#ml-003) (precedes) · **Обратные ссылки ←** [ML-001](#ml-001) (constrained_by), [ML-003](#ml-003) (extends), [ML-007](#ml-007) (informs), [ML-009](#ml-009) (constrained_by)

### ML-003
**ASET: конечные экстремальные значения G2A**

Сертифицированы малые случаи A_3(3,2,2)=5, A_5(2,2,2)=5, A_7(2,2,2)=7 и свидетели; выбран G2_EXPAND_GRID.

**Статус:** `EXACT_NUMERICAL` · **Проверка:** `exact_hosted_ci` · **Темы:** coding, finite-oracle

**Применение:** Проверка поисковых экстремальных алгоритмов. **Ограничения:** Два из трёх случаев имеют m=w; нет асимптотического результата.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-G2A-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-G2A-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/Mathlab/actions/runs/37746812318)

**Связи →** [ML-002](#ml-002) (extends), [ML-001](#ml-001) (tests) · **Обратные ссылки ←** [ML-002](#ml-002) (precedes), [ML-007](#ml-007) (foundation_for), [ML-008](#ml-008) (extends)

### ML-004
**TOM-001: карта математических возможностей**

Карта 14 предварительных задач в инкрементальных вычислениях, канонических структурах, доказательствах и кодировании с product-операциями и критериями опровержения.

**Статус:** `RESEARCH_MAP` · **Проверка:** `repository_review` · **Темы:** methodology, theorem-search

**Применение:** Навигация перед theorem selection. **Ограничения:** Кандидаты не являются подтверждёнными открытыми проблемами.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/TOM-001-OPPORTUNITY-MAP.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/TOM-001-OPPORTUNITY-MAP.md) · первичные источники: —

**Связи →** [ML-005](#ml-005) (refined_by), [ML-006](#ml-006) (refined_by) · **Обратные ссылки ←** [DL-007](#dl-007) (method_compare), [DL-009](#dl-009) (method_compare), [ML-005](#ml-005) (corrects), [OM-133](#om-133) (conceptual_link), [OM-137](#om-137) (conceptual_link)

### ML-005
**TOM-B: контрпримеры и уточнение prior art**

Документирует OR/AND контрпримеры к широким сертификатным утверждениям; понижает историю-независимое разбиение до узкого исследовательского режима.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `exact_hosted_ci` · **Темы:** incremental, history-independence, negative

**Применение:** Не допустить некорректной композиции сертификатов. **Ограничения:** Полнота аудита всех источников не заявлена.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) · первичные источники: [1](https://doi.org/10.1145/3810240), [2](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20)

**Связи →** [ML-004](#ml-004) (corrects), [ML-006](#ml-006) (precedes) · **Обратные ссылки ←** [ML-004](#ml-004) (refined_by), [ML-006](#ml-006) (extends), [OM-132](#om-132) (conceptual_link)

### ML-006
**TOM-C: точная конечная граница метаданных**

Элементарная формула минимального числа меток для одношагового zero-probe verifier; полный перебор 16 двухвходовых булевых функций.

**Статус:** `DERIVED_RESULT` · **Проверка:** `exact_hosted_ci` · **Темы:** incremental, finite-oracle, proof

**Применение:** Базовый sanity-check для будущих нижних границ. **Ограничения:** Предвычисление метаданных бесплатно, поддержание меток при повторных изменениях не учитывается; новизна не заявлена.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/TOM-001-C-EXACT-CERTIFICATE-BASELINE.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/TOM-001-C-EXACT-CERTIFICATE-BASELINE.md) · первичные источники: [1](https://github.com/definitely-stable/Mathlab/actions/runs/37755090131)

**Связи →** [ML-005](#ml-005) (extends), [DM-004](#dm-004) (method_compare) · **Обратные ссылки ←** [DM-004](#dm-004) (method_compare), [ML-004](#ml-004) (refined_by), [ML-005](#ml-005) (precedes), [OM-127](#om-127) (conceptual_link), [OM-129](#om-129) (conceptual_link)

### ML-007
**ASET signed relation: точный критерий коллизии**

Формализует равенство двух subset sums через ограниченные с двух сторон коэффициенты ±1; отличает поле характеристики 2 от нечётной.

**Статус:** `DERIVED_RESULT` · **Проверка:** `repository_proof` · **Темы:** coding, exact-model

**Применение:** Сохранение точных side constraints в поиске конструкций. **Ограничения:** Не тождествен произвольным коротким линейным зависимостям в нечётных полях.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-G1A-PROOF.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-G1A-PROOF.md) · первичные источники: —

**Связи →** [ML-002](#ml-002) (informs), [ML-003](#ml-003) (foundation_for) · **Обратные ссылки ←** [DM-010](#dm-010) (conceptual_link), [ML-010](#ml-010) (extends)

### ML-008
**ASET G2B-A: точное GF(3) и интервал GF(5)**

В действительно разреженном режиме доказано конечное значение A_3^set(4,2,2)=7; для A_5^set(3,2,2) дано только 10–15 и проверенный свидетель.

**Статус:** `EXACT_NUMERICAL` · **Проверка:** `exact_hosted_ci` · **Темы:** coding, finite-oracle, negative

**Применение:** Калибровка гиперграфового поиска, изучение масштабирования жёсткой поддержки. **Ограничения:** GF(5) поиск не исчерпан, интервал не точный максимум; никакой асимптотической новизны.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-G2B-A-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-G2B-A-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/Mathlab/actions/runs/37756386646)

**Связи →** [ML-003](#ml-003) (extends), [ML-009](#ml-009) (foundation_for), [DM-003](#dm-003) (method_compare) · **Обратные ссылки ←** [ML-009](#ml-009) (informs), [ML-010](#ml-010) (context), [ML-011](#ml-011) (method_compare)

### ML-009
**ASET G2B-A: замороженный протокол гиперграфового оракула**

Фиксирует первичную область допустимых конечных поисков, ограничения solver и правила сертификатов до расширения сетки q=3/q=5.

**Статус:** `RESEARCH_PROTOCOL` · **Проверка:** `repository_review` · **Темы:** coding, protocol, reproducibility

**Применение:** Воспроизводимый поиск и независимая верификация найденных семейств. **Ограничения:** Замороженный протокол сам по себе не доказывает полной корректности solver или новизны.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/LENT-001-G2B-A-PROTOCOL.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/LENT-001-G2B-A-PROTOCOL.md) · первичные источники: —

**Связи →** [ML-008](#ml-008) (informs), [ML-002](#ml-002) (constrained_by) · **Обратные ссылки ←** [ML-008](#ml-008) (foundation_for)

### ML-010
**HYP-001/002: двух- и трёхкоординатная ёмкость ASET**

Для нечётных простых q приведено самодостаточное доказательство A_q^set(m,2,2)=Θ_q(m^{3/2}); при w=3 получены границы Ω(m²) и O_q(m^{5/2}), а Θ_q(m²) остаётся гипотезой.

**Статус:** `DERIVED_RESULT` · **Проверка:** `repository_proof` · **Темы:** coding, lower-bounds, combinatorics

**Применение:** Анализ разрыва между write locality w=2 и w=3; возможная математическая постановка для следующего доказательства. **Ограничения:** HYP-001 основан на классических C4-free и projective-plane методах; самостоятельная научная новизна НЕ проверена; HYP-002 sharp exponent НЕ доказан.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/HYP-001-002-LOCALITY-TRANSITION.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/HYP-001-002-LOCALITY-TRANSITION.md) · первичные источники: —

**Связи →** [ML-007](#ml-007) (extends), [ML-011](#ml-011) (foundation_for), [ML-008](#ml-008) (context) · **Обратные ссылки ←** [ML-011](#ml-011) (tests)

### ML-011
**HYP-001/002: конструктивные конечные свидетельства**

GitHub CI проверил PG(2,2)/PG(2,3) incidence и Steiner triples на нечётных полях, а также GF(2) Pasch и нелинейные контрпримеры.

**Статус:** `EXACT_NUMERICAL` · **Проверка:** `exact_hosted_ci` · **Темы:** coding, finite-oracle, reproducibility

**Применение:** Воспроизводимые конечные проверки конструкций, уточнение характеристик и негативные регрессионные тесты. **Ограничения:** Численные примеры не формализуют асимптотические доказательства, не закрывают гипотезу w=3 и не доказывают публикационную новизну.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Mathlab/blob/c3ffc69563ac15241e67f4b6ccfe8063720590f1/docs/research/HYP-001-002-PHASE-A-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/Mathlab/blob/main/docs/research/HYP-001-002-PHASE-A-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/Mathlab/actions/runs/37762380556)

**Связи →** [ML-010](#ml-010) (tests), [ML-008](#ml-008) (method_compare) · **Обратные ссылки ←** [ML-010](#ml-010) (foundation_for)


## DELSK

### DL-001
**DELSK: матрица claims и первичного prior art**

Сопоставляет Finesse, DeepSketch, Odess, Argus, FastDelta и другие системы с encoder-aware scoring, бюджетами и воспроизводимостью; отделяет COVERED от PARTIAL.

**Статус:** `PRIOR_ART_AUDIT` · **Проверка:** `primary_source_review` · **Темы:** delta-compression, prior-art

**Применение:** Проверка продуктовой и алгоритмической новизны выбора delta-base. **Ограничения:** Часть публикаций доступна только по abstract; claim OPEN не гарантирует отсутствие prior art.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/claim-matrix.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/research/claim-matrix.md) · первичные источники: [1](https://www.usenix.org/system/files/fast19-zhang.pdf), [2](https://www.usenix.org/system/files/fast22-park.pdf), [3](https://doi.org/10.1145/3747839)

**Связи →** [DL-002](#dl-002) (updated_by), [DL-003](#dl-003) (background_for) · **Обратные ссылки ←** [DL-002](#dl-002) (extends), [DL-003](#dl-003) (context), [DL-007](#dl-007) (context), [DL-009](#dl-009) (extends), [OM-128](#om-128) (adjacent_application)

### DL-002
**DELSK: октябрьское обновление baselines**

Добавлены Git name-hash/path-walk, containment, MinHash, LZJD, trial encode; рекомендации честного Pareto-сравнения по bytes/CPU/index/codec.

**Статус:** `PRIOR_ART_AUDIT` · **Проверка:** `primary_source_review` · **Темы:** delta-compression, baselines, prior-art

**Применение:** Выбор сильных, дешёвых инженерных сравнений. **Ограничения:** Уровни P/M/U неодинаковы; не все методы воспроизведены.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md) · первичные источники: [1](https://github.blog/open-source/git/highlights-from-git-2-51/), [2](https://arxiv.org/abs/2507.10019)

**Связи →** [DL-001](#dl-001) (extends), [DL-004](#dl-004) (motivates) · **Обратные ссылки ←** [DL-001](#dl-001) (updated_by)

### DL-003
**DELSK-X0: отрицательный screening headroom**

В ограниченном скрининге простые baselines почти насыщают savings; решение NO_HEADROOM_AT_256 для исследованных ячеек.

**Статус:** `EMPIRICAL_RESULT` · **Проверка:** `exact_retained_measurement` · **Темы:** delta-compression, negative, evidence

**Применение:** Обоснование pivot от сложных descriptor-конструкций. **Ограничения:** Exploratory: небольшие выборки и один codec; нельзя переносить на все типы данных.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/corpus/x0/results.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/corpus/x0/results.md) · первичные источники: [1](https://github.com/definitely-stable/Shift-lab/actions/runs/37449333091)

**Связи →** [DL-001](#dl-001) (context), [DL-004](#dl-004) (motivates) · **Обратные ссылки ←** [DL-001](#dl-001) (background_for), [DL-004](#dl-004) (follows), [DL-008](#dl-008) (context)

### DL-004
**DELSK-S2: benchmark simple selector**

На hosted-runner заявлены p95=16.7 мкс при 1M объектов, top-2 parity 1.000, ≈40.7 B/index entry, 499–502 MiB/s descriptor; принят локальный performance gate.

**Статус:** `EMPIRICAL_RESULT` · **Проверка:** `exact_retained_measurement` · **Темы:** delta-compression, performance

**Применение:** Простейший bounded index как контроль для нового Rust-примитива. **Ограничения:** Синтетическая нагрузка, один runner/run, не строгая latency guarantee.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/selector/results-s2.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/selector/results-s2.md) · первичные источники: [1](https://github.com/definitely-stable/Shift-lab/actions/runs/37455719130)

**Связи →** [DL-003](#dl-003) (follows), [DL-005](#dl-005) (followed_by), [DL-006](#dl-006) (related) · **Обратные ссылки ←** [DL-002](#dl-002) (motivates), [DL-003](#dl-003) (motivates), [DL-005](#dl-005) (follows), [DL-006](#dl-006) (system_extension), [DL-012](#dl-012) (contrast), [DM-006](#dm-006) (method_compare)

### DL-005
**DELSK-S3: отказ от delta-encoding не принят**

Пороговый descriptor-abstention не проходит preregistered FN и loss thresholds; принято L=0.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `exact_retained_measurement` · **Темы:** delta-compression, negative, selection

**Применение:** Защита от ложных пропусков полезного delta. **Ограничения:** In-sample набор, нет общего теоретического утверждения.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/selector/results-s3.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/selector/results-s3.md) · первичные источники: [1](https://github.com/definitely-stable/Shift-lab/actions/runs/37458783363)

**Связи →** [DL-004](#dl-004) (follows), [DL-006](#dl-006) (precedes) · **Обратные ссылки ←** [DL-004](#dl-004) (followed_by), [DL-006](#dl-006) (context)

### DL-006
**DELSK-S4-D: ChunkShift integration development screen**

При K=2 около 1.06% экономии CSP байтов относительно previous1 ценой ~1.49x encode calls; verdict OPEN_CONFIRMATION_K2.

**Статус:** `EMPIRICAL_RESULT` · **Проверка:** `exact_retained_measurement` · **Темы:** delta-compression, system-evidence

**Применение:** Контроль системной пользы выбора кандидатов. **Ограничения:** Development screen, не sealed holdout; не доказывает готовность отдельного crate.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/results/SELECTOR-S4/README.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/results/SELECTOR-S4/README.md) · первичные источники: [1](https://github.com/definitely-stable/Shift-lab/issues/13)

**Связи →** [DL-004](#dl-004) (system_extension), [DL-005](#dl-005) (context) · **Обратные ссылки ←** [DL-004](#dl-004) (related), [DL-005](#dl-005) (precedes), [DL-012](#dl-012) (follows), [DM-013](#dm-013) (method_compare), [OM-121](#om-121) (adjacent_application)

### DL-007
**DELSK: практики воспроизводимой исследовательской лаборатории**

Предлагает цепочку issue→experiment→run→evidence→decision и учёт шума, допусков, копирований, памяти и отрицательных результатов.

**Статус:** `RESEARCH_SYNTHESIS` · **Проверка:** `repository_review` · **Темы:** methodology, reproducibility, benchmark

**Применение:** Шаблон доказательной дисциплины для экспериментов и протоколов Mathlab. **Ограничения:** Рекомендации, а не нормативный стандарт и не выполненное измерение.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/lab-practices.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/research/lab-practices.md) · первичные источники: —

**Связи →** [DL-001](#dl-001) (context), [ML-004](#ml-004) (method_compare) · **Обратные ссылки ←** [DL-008](#dl-008) (method_compare), [DL-010](#dl-010) (foundation), [DL-011](#dl-011) (method_compare), [DM-011](#dm-011) (method_compare)

### DL-008
**DELSK E0: adversarial candidate-universe и недоопределённая выборка**

Аудит показывает, что канонический JSON не гарантирует канонический выбор, а алиасы и split policy могут менять состав допустимых кандидатов.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `source_inspected` · **Темы:** selection, reproducibility, negative

**Применение:** Предупреждение о скрытом недетерминизме и протоколах запечатывания исследовательских наборов. **Ограничения:** Первоначальный E0 NOT READY относится к указанному снимку; позднее был принят отдельный контракт.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-002-E0-candidate-universe.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/research/DELSK-002-E0-candidate-universe.md) · первичные источники: —

**Связи →** [DL-007](#dl-007) (method_compare), [DL-003](#dl-003) (context) · **Обратные ссылки ←** —

### DL-009
**DELSK: критика двух внешних deep-research отчётов**

Разделяет уже известные Finesse/DeepSketch pipeline и проверяемые продуктовые гипотезы о budget, codec-conditioning и displacement.

**Статус:** `PRIOR_ART_AUDIT` · **Проверка:** `primary_source_review` · **Темы:** delta-compression, prior-art, negative

**Применение:** Проверка генеративных гипотез и корректировка параметров будущих Rust-исследований. **Ограничения:** Исходные пользовательские отчёты остаются вне каталога; новое утверждение о новизне не доказано.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/report-audit.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/research/report-audit.md) · первичные источники: —

**Связи →** [DL-001](#dl-001) (extends), [ML-004](#ml-004) (method_compare) · **Обратные ссылки ←** [DM-014](#dm-014) (method_compare)

### DL-010
**DELSK-003A: нормативный provenance contract v4**

Разделяет measurement v1 и надстройку v4 для регистрации попыток, фиксирует версионированные freeze bytes и условия авторизации G1.

**Статус:** `RESEARCH_PROTOCOL` · **Проверка:** `source_inspected` · **Темы:** provenance, protocol, reproducibility

**Применение:** Повторяемые эксперименты, запрет retrospective selection и надёжное происхождение результатов. **Ограничения:** Документ контрактный: статус natural G1 следует читать в отдельном activation/evidence; не является алгоритмической теоремой.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/oracle/contract-v4.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/oracle/contract-v4.md) · первичные источники: —

**Связи →** [DL-011](#dl-011) (followed_by), [DL-007](#dl-007) (foundation) · **Обратные ссылки ←** [DL-011](#dl-011) (uses)

### DL-011
**DELSK-003A: история GitHub-активации протокола v4**

Журнал содержит проверку правил GitHub, создание защищённого genesis и активацию registry по замороженному контракту v4.

**Статус:** `RESEARCH_EVIDENCE` · **Проверка:** `source_inspected` · **Темы:** provenance, hosted-ci, operational

**Применение:** Проверка того, что provenance-свидетельство действительно зарегистрировано до измерений. **Ограничения:** Журнал пояснительный, не нормативный; необходимо сверять этап и отдельные артефакты для окончательного вердикта.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/oracle/activation-v4-log.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/oracle/activation-v4-log.md) · первичные источники: —

**Связи →** [DL-010](#dl-010) (uses), [DL-007](#dl-007) (method_compare) · **Обратные ссылки ←** [DL-010](#dl-010) (followed_by)

### DL-012
**DELSK S4-C: предварительно зарегистрированный holdout**

Описывает заблокированную до измерений проверку K=2 selector на отдельно sealed E1-наборе с контролем previous1 и physical patch bytes.

**Статус:** `RESEARCH_PROTOCOL` · **Проверка:** `source_inspected` · **Темы:** delta-compression, holdout, protocol

**Применение:** План честного отделения development-gain от независимой проверки ChunkShift-патча. **Ограничения:** На зафиксированном snapshot статус PREREGISTRATION/NOT_RUN, выгода на holdout ещё не подтверждена.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/selector/s4-confirmation.md) · [актуальная ветка](https://github.com/definitely-stable/Shift-lab/blob/main/.work/selector/s4-confirmation.md) · первичные источники: —

**Связи →** [DL-006](#dl-006) (follows), [DL-004](#dl-004) (contrast) · **Обратные ссылки ←** [DM-008](#dm-008) (method_compare)


## DELTAMETER

### DM-001
**DeltaMeter: разделение F2 и GF(2) модели**

Документирует эквивалентные формулировки symmetric-difference cardinality через signed F2 и GF(2)-паритет, с различием семантики toggle и insert.

**Статус:** `RESEARCH_SYNTHESIS` · **Проверка:** `repository_review` · **Темы:** streaming, coding, models

**Применение:** Не смешивать гарантию множества и multiset. **Ограничения:** Модели требуют разных предпосылок к обновлениям.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/FOUNDATION.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/FOUNDATION.md) · первичные источники: —

**Связи →** [DM-002](#dm-002) (precedes), [ML-001](#ml-001) (related) · **Обратные ссылки ←** [DM-002](#dm-002) (foundation), [DM-006](#dm-006) (related), [ML-001](#ml-001) (related)

### DM-002
**GF(2)-F-PCSA: воспроизведение опубликованной конструкции**

Реализована опубликованная схема FIELDMAP, битового XOR и row-level статистики; детерминированный псевдо-оракул не равен идеальной случайности статьи.

**Статус:** `REPRODUCTION` · **Проверка:** `repository_tests` · **Темы:** streaming, parity, reproducibility

**Применение:** Различие теоремы об идеальной модели и reproducible code. **Ограничения:** Нет finite-sample гарантии из одной только инженерной реализации.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/M2-FPCSA-REPRODUCTION.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/M2-FPCSA-REPRODUCTION.md) · первичные источники: [1](https://arxiv.org/abs/2310.14977)

**Связи →** [DM-001](#dm-001) (foundation), [DM-003](#dm-003) (bounded_by) · **Обратные ссылки ←** [DM-001](#dm-001) (precedes), [DM-003](#dm-003) (extends)

### DM-003
**Post-M3: строгий Parity NO-GO и точные конечные законы**

Содержит Fourier full-state law, one-level PGF, truncation split и доказательство несостоятельности W как sufficient statistic; строгий опубликованный W_i backend остановлен.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `repository_proof` · **Темы:** streaming, finite-sample, negative

**Применение:** Фильтрация ошибочных strict confidence claims. **Ограничения:** NO-GO касается текущего published W_i пути; не теорема невозможности всех GF(2) оценивателей.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/STRICT-PARITY-POST-M3.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/STRICT-PARITY-POST-M3.md) · первичные источники: —

**Связи →** [DM-002](#dm-002) (extends), [DM-004](#dm-004) (counterpart) · **Обратные ссылки ←** [DM-002](#dm-002) (bounded_by), [DM-004](#dm-004) (contrast), [DM-007](#dm-007) (extends), [ML-008](#ml-008) (method_compare)

### DM-004
**STRICT-COMPACT-002: continuous range certificate**

Для идеальной статистической модели представлен точный рациональный сертификат диапазона для 32 KiB state и q95 U/d<=1.5, δ=10^-6; публичная строгая гарантия псевдо-оракула не разрешена.

**Статус:** `RESEARCH_EVIDENCE` · **Проверка:** `exact_hosted_ci` · **Темы:** streaming, finite-sample, certification

**Применение:** Шаблон строгой сертификации заявленного диапазона. **Ограничения:** Доказательство параметров идеальной модели не автоматически распространяется на детерминированный runtime oracle.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/STRICT-COMPACT-002-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/STRICT-COMPACT-002-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/issues/63)

**Связи →** [DM-003](#dm-003) (contrast), [DM-005](#dm-005) (precedes), [ML-006](#ml-006) (method_compare) · **Обратные ссылки ←** [DM-003](#dm-003) (counterpart), [DM-005](#dm-005) (uses), [DM-007](#dm-007) (context), [ML-006](#ml-006) (method_compare)

### DM-005
**STRICT-COMPACT: оптимизация state/range и layout**

После private feasibility предлагает последовательность OPT-A/B/C: параметризация уровней, maintained cache, progressive transfer, затем публичный контракт.

**Статус:** `RESEARCH_PLAN` · **Проверка:** `repository_review` · **Темы:** streaming, optimization, protocol

**Применение:** Дисциплина performance и API gates. **Ограничения:** Планы не являются результатами выполненных benchmark или новой теоремой.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/STRICT-COMPACT-OPT-NEXT-WORK.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/STRICT-COMPACT-OPT-NEXT-WORK.md) · первичные источники: —

**Связи →** [DM-004](#dm-004) (uses) · **Обратные ссылки ←** [DM-004](#dm-004) (precedes), [DM-014](#dm-014) (context)

### DM-006
**M6-D13B: системный protocol comparator**

Frozen контракт сравнения direct, maintained D11, RIBLT pull и stream lower-bound с RTT/bandwidth-моделью, без принятия production ExactSmallDelta.

**Статус:** `RESEARCH_PROTOCOL` · **Проверка:** `source_inspected` · **Темы:** reconciliation, benchmark, protocol

**Применение:** Проверка честности comparator и распределённых затрат. **Ограничения:** JSON описывает протокол измерения, не performance verdict.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/research/m6d13b/contract.json) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/research/m6d13b/contract.json) · первичные источники: —

**Связи →** [DM-001](#dm-001) (related), [DL-004](#dl-004) (method_compare) · **Обратные ссылки ←** [DM-008](#dm-008) (precedes), [DM-012](#dm-012) (extends)

### DM-007
**DeltaMeter: открытые finite-sample вопросы**

Реестр оставшихся математических проблем: tails для ParityLevelCounts, fixed-d de-Poissonization, информационные границы и допущения случайности.

**Статус:** `OPEN_QUESTION` · **Проверка:** `repository_review` · **Темы:** streaming, finite-sample

**Применение:** Очередь проверяемых математических задач. **Ограничения:** Открытые вопросы могут быть известны вне текущего аудита; не утверждать глобальную новизну.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/OPEN-QUESTIONS.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/research/OPEN-QUESTIONS.md) · первичные источники: —

**Связи →** [DM-003](#dm-003) (extends), [DM-004](#dm-004) (context) · **Обратные ссылки ←** —

### DM-008
**M6-D2: инкрементальные синдромы и отсутствие повторной передачи**

Лабораторный nested-prefix PinSketch64 сохраняет ранее отправленные синдромы; измеренный протокол ступеней k=1,2,4,8 избегает повторной передачи.

**Статус:** `RESEARCH_EVIDENCE` · **Проверка:** `exact_retained_measurement` · **Темы:** reconciliation, incremental, performance

**Применение:** Базис сравнений для поэтапной передачи информации в распределённых системах. **Ограничения:** Guard имеет эмпирическую надёжность; публичная реализация остаётся NO-GO.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D2-INCREMENTAL-PREFIX-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D2-INCREMENTAL-PREFIX-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37564857480)

**Связи →** [DM-006](#dm-006) (precedes), [DL-012](#dl-012) (method_compare) · **Обратные ссылки ←** [DM-009](#dm-009) (extends)

### DM-009
**M6-D3: incremental Berlekamp–Massey не улучшил скорость**

Математически согласованное переиспользование BM-состояния подтвердило равенство свежему расчёту, но performance gate отклонил оптимизацию.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `exact_retained_measurement` · **Темы:** reconciliation, negative, performance

**Применение:** Негативный benchmark для предотвращения повторного микропрофилирования малозначимых фаз. **Ограничения:** Корректность подтверждена на frozen workloads; нельзя экстраполировать производительность на другие профили.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D3-INCREMENTAL-BM-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D3-INCREMENTAL-BM-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37567202464)

**Связи →** [DM-008](#dm-008) (extends), [DM-010](#dm-010) (precedes) · **Обратные ссылки ←** [DM-010](#dm-010) (follows)

### DM-010
**M6-D11: ускорение fixed-constant GF(2^64) reduction**

Приватный эксперимент применил предвычисленные positional nibble tables при сокращении trace polynomials и прошёл предварительно объявленный performance gate.

**Статус:** `RESEARCH_EVIDENCE` · **Проверка:** `exact_retained_measurement` · **Темы:** finite-field, optimization, performance

**Применение:** Прикладная оптимизация точных операций с полем и полиномами. **Ограничения:** Production/public ExactSmallDelta NO-GO; результат ограничен зафиксированным decoder lane.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D11-FIXED-REDUCTION-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D11-FIXED-REDUCTION-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37598918009)

**Связи →** [DM-009](#dm-009) (follows), [DM-011](#dm-011) (followed_by), [ML-007](#ml-007) (conceptual_link) · **Обратные ссылки ←** [DM-009](#dm-009) (precedes), [DM-011](#dm-011) (extends), [OM-130](#om-130) (conceptual_link)

### DM-011
**M6-D12: STOP дальнейшей алгебраической микрооптимизации**

Пять независимых hosted workers не выявили устойчивой фазы декодирования, проходящей заранее установленный порог 25% общей задержки.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `exact_retained_measurement` · **Темы:** performance, negative, reproducibility

**Применение:** Определяет момент остановки оптимизации на основании предварительно зафиксированного порога. **Ограничения:** Отрицательный итог зависит от выбранных корпусов, платформ и протокола, не является нижней границей сложности.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D12-POST-D11-PROFILE-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D12-POST-D11-PROFILE-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37612343061)

**Связи →** [DM-010](#dm-010) (extends), [DL-007](#dl-007) (method_compare) · **Обратные ссылки ←** [DM-010](#dm-010) (followed_by), [DM-013](#dm-013) (context)

### DM-012
**M6-D13B0: readiness до измерения системного эффекта**

Заморожены исходники, границы измерений и подготовлены persistent sessions; readiness пройдена, но измеренного преимущества ещё не заявлено.

**Статус:** `RESEARCH_EVIDENCE` · **Проверка:** `exact_hosted_ci` · **Темы:** reconciliation, protocol, reproducibility

**Применение:** Точность сопоставления алгоритмов с фиксированной платой за поддержку состояния. **Ограничения:** Не результат latency comparison; ранний ложный кандидат подтверждает необходимость fail-closed проверки.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D13B0-MEASUREMENT-READINESS-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D13B0-MEASUREMENT-READINESS-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37646837382)

**Связи →** [DM-006](#dm-006) (extends), [DM-013](#dm-013) (precedes) · **Обратные ссылки ←** [DM-013](#dm-013) (extends)

### DM-013
**M6-D13B: системный STOP_SYSTEM_PRODUCT**

Пять независимых workers, 3900 наблюдений и 360 моделируемых ячеек не дали ни одной квалифицирующей ячейки для перехода к public system product.

**Статус:** `RESEARCH_DECISION` · **Проверка:** `exact_retained_measurement` · **Темы:** reconciliation, negative, system-evidence

**Применение:** Определяет продуктовый NO-GO после сопоставления direct exact, maintained state и RIBLT по протоколу. **Ограничения:** Это решение для конкретной матрицы и сети, а не теорема невозможности reconciliation.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D13B-SYSTEM-EVIDENCE.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-D13B-SYSTEM-EVIDENCE.md) · первичные источники: [1](https://github.com/definitely-stable/deltameter/actions/runs/37651049535)

**Связи →** [DM-012](#dm-012) (extends), [DM-011](#dm-011) (context), [DL-006](#dl-006) (method_compare) · **Обратные ссылки ←** [DM-012](#dm-012) (precedes)

### DM-014
**M6-B: аудит snapshot codec и научных предположений**

Сопоставляет внешние отчёты с фактическими byte layouts/CRC32C и отвергает выводы о post-optimization CPU share без измерений.

**Статус:** `PRIOR_ART_AUDIT` · **Проверка:** `repository_review` · **Темы:** codec, benchmark, methodology

**Применение:** Эталон корректного Amdahl accounting и версионированного serialization-review. **Ограничения:** Сведения о speedup контекстны для профиля и протокола, не универсальны.

**Происхождение:** [зафиксированная версия](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-B-CODEC-DECODER-RESEARCH-AUDIT.md) · [актуальная ветка](https://github.com/definitely-stable/deltameter/blob/main/docs/M6-B-CODEC-DECODER-RESEARCH-AUDIT.md) · первичные источники: —

**Связи →** [DM-005](#dm-005) (context), [DL-009](#dl-009) (method_compare) · **Обратные ссылки ←** —


## OPENAI_MATH

### OM-000
**OpenAI math: коллекция и границы проверки**

Официальный каталог рукописей с разной степенью Lean-формализации; предупреждает о возможных ошибках в неформализованных результатах.

**Статус:** `EXTERNAL_CATALOG` · **Проверка:** `source_catalog` · **Темы:** mathematics, formalization, provenance

**Применение:** Навигация по семействам, proof artifacts и release history. **Ограничения:** Количества рукописей и формализаций изменяются; это snapshot, не endorsement.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/README.md) · [актуальная ветка](https://github.com/openai/math/blob/main/README.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/main/lean/formalization.yaml)

**Связи →** [OM-099](#om-099) (contains), [OM-119](#om-119) (contains), [OM-121](#om-121) (contains), [OM-122](#om-122) (contains), [OM-103](#om-103) (contains) · **Обратные ссылки ←** [OM-099](#om-099) (catalogued_in), [OM-103](#om-103) (catalogued_in), [OM-119](#om-119) (catalogued_in), [OM-121](#om-121) (catalogued_in), [OM-122](#om-122) (catalogued_in), [OM-129](#om-129) (catalogued_in), [OM-130](#om-130) (catalogued_in), [OM-133](#om-133) (catalogued_in), [OM-134](#om-134) (catalogued_in)

### OM-099
**Family 099: заявленные границы искажения edit distance**

Каталог автора сообщает matching экспоненциальную шкалу искажения вложений edit-distance в ℓ1; привязан к manuscript и Lean-документации.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** edit-distance, geometry, lower-bounds

**Применение:** Методологический benchmark верхних/нижних оценок. **Ограничения:** Факт присутствия Lean-документа не равен независимой экспертизе математической публикации.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/099.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/099.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf), [3](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [OM-121](#om-121) (related) · **Обратные ссылки ←** [OM-000](#om-000) (contains), [OM-121](#om-121) (related), [OM-122](#om-122) (related)

### OM-103
**Family 103: заявленная дерaндомизация logspace**

Коллекция содержит рукопись с утверждением L=RL=BPL и ссылку на Lean-артефакты; запись импортирует заявление автора, не подтверждает теорему.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** complexity, derandomization

**Применение:** Пример необходимости отделять proof status от новизны и популярности. **Ограничения:** Сильное заявление; без независимого прочтения доказательства и формализации использовать лишь как предмет аудита.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/103.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/103.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in) · **Обратные ссылки ←** [OM-000](#om-000) (contains), [OM-137](#om-137) (related)

### OM-119
**Family 119: заявленное сжатие информации булевых функций**

Каталог относит к семейству Courtade–Kumar/Hellinger и заявляет sharp information contraction; есть ссылка на Lean-документацию.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** information-theory, boolean

**Применение:** Возможный методический источник для информационных ограничений. **Ограничения:** Модель noise/information не эквивалентна sparse-update lower bound.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/119.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/119.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [ML-001](#ml-001) (conceptual_link) · **Обратные ссылки ←** [OM-000](#om-000) (contains), [OM-127](#om-127) (related)

### OM-121
**Family 121: заявленная почти-линейная аппроксимация edit distance**

Рукопись заявляет рандомизированную (1+ε)-аппроксимацию edit-distance за N^{1+o(1)} при фиксированном ε; коллекция даёт Lean-метаданные.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** edit-distance, algorithms

**Применение:** Поиск algorithmic primitives только после source-level audit. **Ограничения:** Не проверялось сопоставление с актуальными внешними best-known алгоритмами; не использовать как продуктовый benchmark.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/121.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/121.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf)

**Связи →** [OM-099](#om-099) (related), [OM-000](#om-000) (catalogued_in), [DL-006](#dl-006) (adjacent_application) · **Обратные ссылки ←** [OM-000](#om-000) (contains), [OM-099](#om-099) (related), [OM-128](#om-128) (related)

### OM-122
**Family 122: заявленные оценки trace reconstruction**

Коллекция заявляет границы выборки и uniform decoder для реконструкции строк после удалений; документирует Lean-связку.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** edit-distance, information-theory, reconstruction

**Применение:** Соседняя область lower bounds для работы с изменениями строк. **Ограничения:** Не доказана применимость к dynamic state/cdc; заявленные достижения требуют независимого аудита.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/122.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/122.md) · первичные источники: [1](https://github.com/openai/math/blob/main/CONTENTS.md), [2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf), [3](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [OM-099](#om-099) (related) · **Обратные ссылки ←** [OM-000](#om-000) (contains)

### OM-127
**Family 127: заявленная средняя чувствительность threshold функций**

Каталог описывает Lean-формализацию границы средней чувствительности 8d sqrt(n) для булевых polynomial threshold functions.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** boolean, sensitivity, lower-bounds

**Применение:** Источник гипотез о влиянии одиночных изменений, но не готовый Rust-примитив. **Ограничения:** Формализация касается средней чувствительности в заявленной модели; не доказывает worst-case динамические bounds.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/127.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/127.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf)

**Связи →** [ML-006](#ml-006) (conceptual_link), [OM-119](#om-119) (related) · **Обратные ссылки ←** [OM-132](#om-132) (related)

### OM-128
**Family 128: заявленная 2-аппроксимация shortest common superstring**

Scope документ описывает детерминированную полиномиальную 2-аппроксимацию кратчайшей общей надстроки для конечного набора строк.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** strings, approximation, algorithms

**Применение:** Компаратор для string/dedup задач, где нужно явно различать аппроксимацию и оптимум. **Ограничения:** Утверждение коллекции; нет независимого воспроизведения, прямая переносимость в delta-base selection неизвестна.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/128.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/128.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf)

**Связи →** [OM-121](#om-121) (related), [DL-001](#dl-001) (adjacent_application) · **Обратные ссылки ←** —

### OM-129
**Family 129: заявленные экспоненциальные состояния двухсторонних автоматов**

Коллекция описывает Lean-границы для complementation и determinization двухсторонних автоматов с растущим алфавитом.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** automata, lower-bounds, complexity

**Применение:** Модель возможных нижних границ на стоимость компактного состояния. **Ограничения:** Алфавит растёт вместе с размером; нет выводов для фиксированного алфавита или состояния Rust-кэша.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/129.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/129.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [ML-006](#ml-006) (conceptual_link) · **Обратные ссылки ←** [OM-134](#om-134) (related)

### OM-130
**Family 130: заявленные суб-nlogn точные Fourier схемы**

Указан Lean scope точной DFT/свёртки со сложностью ниже n log n в модели точной комплексной арифметики и неограниченных коэффициентов.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** algorithms, complexity, algebra

**Применение:** Контекст для понимания разницы между arithmetic-circuit и реальной битовой сложностью. **Ограничения:** Не доказан выигрыш для обычного floating-point FFT, integer NTT, ограничения коэффициентов или практического Rust implementation.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/130.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/130.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [DM-010](#dm-010) (conceptual_link) · **Обратные ссылки ←** —

### OM-132
**Family 132: заявленное сверхквадратичное разделение sensitivity**

По данным Lean scope, построены булевы функции с неограниченным отношением block sensitivity к квадрату sensitivity.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** boolean, sensitivity, lower-bounds

**Применение:** Предостережение против ошибочных универсальных оценок влияния пакетных изменений. **Ограничения:** Источник не устанавливает минимальную стоимость поддержания сертификатов O01 при последовательных изменениях.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/132.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/132.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf)

**Связи →** [OM-127](#om-127) (related), [ML-005](#ml-005) (conceptual_link) · **Обратные ссылки ←** —

### OM-133
**Family 133: заявленная сложность Weisfeiler–Leman refinement**

Коллекция формализует выбранные конструкции parity-lift и заявленные пределы распознавания графов методами Weisfeiler–Leman.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** graphs, complexity, lower-bounds

**Применение:** Теоретический компаратор для графовых структур и проверяемых отличий состояний. **Ограничения:** Отдельные lower bounds и conditional exclusions могут не входить в формализованный subset; нужен theorem-level audit.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/133.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/133.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf)

**Связи →** [OM-000](#om-000) (catalogued_in), [ML-004](#ml-004) (conceptual_link) · **Обратные ссылки ←** —

### OM-134
**Family 134: заявленная верхняя граница star height три**

Scope документ сообщает Lean-формализацию представления регулярных языков обобщёнными регулярными выражениями с вложенностью Kleene star не более трёх.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** automata, language, algebra

**Применение:** Направление поиска компактных канонических форм формальных языков. **Ограничения:** Star-height bound не доказывает дешёвое инкрементальное построение или меньшую сериализацию.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/134.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/134.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf)

**Связи →** [OM-129](#om-129) (related), [OM-000](#om-000) (catalogued_in) · **Обратные ссылки ←** —

### OM-137
**Family 137: заявленная one-tape time–space simulation**

Описана Lean-формализация двух-пятых-степенной space simulation ограниченных one-tape машин, включая вариант без заранее известного time cap.

**Статус:** `EXTERNAL_MANUSCRIPT_CLAIM` · **Проверка:** `source_catalog` · **Темы:** complexity, memory, simulation

**Применение:** Пример аккуратного отделения модели вычислений от некорректной универсальной оценки. **Ограничения:** Результат ограничен одноленточной моделью и условиями доступа к input; на RAM напрямую не переносится.

**Происхождение:** [зафиксированная версия](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/137.md) · [актуальная ветка](https://github.com/openai/math/blob/main/lean/docs/137.md) · первичные источники: [1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf)

**Связи →** [OM-103](#om-103) (related), [ML-004](#ml-004) (conceptual_link) · **Обратные ссылки ←** —
