# RESEARCH-LITERATURE-003 — широкая выборка математических работ 2026 года

**Срез:** 2026-10-08 · Issue [#61](https://github.com/definitely-stable/Mathlab/issues/61)  
**Результат:** 26 новых работ `LIT-050…LIT-075`; совокупный внешне-библиографический реестр **49 → 75**; 61 историческая внутренняя исследовательская запись НЕ изменена.  
**Статус:** оригинальные abstracts/официальные программы STOC'26, ICALP'26, EuroSys'26; независимой проверки полных доказательств, reproductions, Rust-реализаций **НЕТ**.

[Индекс всех первоисточников](catalog/LITERATURE.md) · [Обратный каталог по исследованиям](catalog/LITERATURE-BY-RESEARCH.md) · [Исходные метаданные](catalog/literature.json)

## Принципы отбора и исключения

Цель — **не** коллекция sketches. Материалы подбирались на стыке четырёх подпрограмм Mathlab и внешних исследовательских проектов: LENT/ASET; TOM (доказательная стоимость изменений); `openai/math` темы (PIT, память, формальные границы, графы, выборка, строки); DELSK patching. DeltaMeter streaming/reconciliation **0/26**. Это строго не «26 самых цитируемых в мире»: предварительный приоритет основан на новизне идей *относительно модели*, строгости заявленной теоремы, доказательной границе и возможности снять неверную гипотезу. Цитирования, impact score и full-text proof replication не проводились.

Материалы STOC'26 проверены по [официальному оглавлению ACM STOC 2026 с названиями, авторами, abstracts и ссылками DOI](https://acm-stoc.org/stoc2026/toc.html); непосредственные full-text ACM часто возвращают 403. LIPIcs-материалы проверены через [страницы статей ICALP 2026](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-374); инженерный EuroSys — по [программе EuroSys 2026](https://2026.eurosys.org/papers.html), при том DELSK ранее читал соответствующий издательский full text. DOI в `literature.json` сохраняется главным идентификатором. Нельзя писать **FULL_PROOF_VERIFIED** на основании официальной аннотации.

### Распределение новых публикаций

| Семья | Новых | Назначение |
| --- | ---: | --- |
| proof-complexity | 4 | IPS/PIT, rank, depth-restricted Res(⊕), границы формальных сертификатов |
| algebraic-complexity | 4 | Factors, tropical circuits, finite algebra identity checking, circuit lower bounds |
| graph-algorithms | 6 | Incremental SSSP, dynamic set cover / matching / clustering, separators |
| dynamic-data-structures | 3 | cell-probe barriers, dynamic succinct rank/select, sampling by probes |
| randomized-sampling | 3 | memory–sample lower bounds, parallel sampling, log-concave |
| sparse-coding | 3 | list recovery, locally evaluable independent hashes, pseudorandom edit codes |
| fine-grained-algorithms | 2 | exact-vs-approx edit distance, text indexing with k mismatches |
| delta-base-selection | 1 | FastDelta hash reuse across CDC, features and encoding |
| streaming-reconciliation | **0** | Не дублируем уже импортированную литературу |
| **ИТОГО** | **26** | **8 различных областей в новой выборке; 10 тем в полном каталоге** |

## Рейтинг по полезности для будущих задач Mathlab

**P0 — сильная необходимость для проверки того, что мы вообще можем доказывать.**

1. **[LIT-052 — The Natural Proofs Barrier against Data-Structure Lower-Bounds (STOC'26)](catalog/LITERATURE.md#lit-052)**. Главная работа для TOM/LENT: описывает условный барьер стандартных cell-probe нижних границ через LLU/local PRFs. Ошибка переноса — утверждать отсутствие любых возможных lower bounds; это барьер методов при допущении.
2. **[LIT-050](catalog/LITERATURE.md#lit-050) и [LIT-051](catalog/LITERATURE.md#lit-051) — IPS над малыми конечными полями, weak rank principle (STOC'26)**. Проверяют, где реальные размерности, коэффициенты и ограничения формальных доказательств. Приложимость к ASET/DRAT требует конкретной редукции; наш GF(5)-сертификат не становится сильнее автоматически.
3. **[LIT-053 — Compressing Dynamic Fully Indexable Dictionaries (STOC'26)](catalog/LITERATURE.md#lit-053)**. Очень близко к TOM, физически компактным состояниям и цене rank/select обновлений, но Word-RAM `M_B` ≠ потоковая сериализация, crash durability или history independence.
4. **[LIT-060 — PIT Is in NP If and Only If IPS Can Be p-Simulated… (STOC'26)](catalog/LITERATURE.md#lit-060)**. Ключевой *стоп-сигнал* для идеи «любой алгебраический proof легко проверяется детерминированно». Заявлена эквивалентность с caveats о поле, а не новое включение PIT в NP.
5. **[LIT-075 — Lower Bounds on Pure Dynamic Programming… (ICALP'26)](catalog/LITERATURE.md#lit-075)**. Указывает, как строго замораживать модель вычислений (tropical circuits), иначе трансфер нижней границы на все dynamic programs некорректен.

**P1 — важная соседняя теория для алгоритмического ядра и практических проверок.**

6. **[LIT-054 — Edit Distance and LCS quasi-strong subquadratic approximations (STOC'26)](catalog/LITERATURE.md#lit-054)**. Различает approximate ED и exact delta patch, даёт теоретический ориентир для бенчмарка approximation gap, а не немедленный production backend.
7. **[LIT-067 — FastDelta / Once Rolling Hashing is Enough (EuroSys'26)](catalog/LITERATURE.md#lit-067)**. Для DELSK/ChunkShift уже prior art на переиспользование rolling hash между CDC, поиском и encoder. Нужен ablation/whole-pipeline cost, не только совпадения chunks.
8. **[LIT-056](catalog/LITERATURE.md#lit-056), [LIT-059](catalog/LITERATURE.md#lit-059), [LIT-065](catalog/LITERATURE.md#lit-065), [LIT-066](catalog/LITERATURE.md#lit-066)**: обновления графовых объектов — ценны для TOM O01/O04, но нельзя приравнивать dynamic graph recourse к bytes rewritten или точному zero-effect.
9. **[LIT-073 — Classifying Identities, subcubic distributivity checking (STOC'26)](catalog/LITERATURE.md#lit-073)**. Модельное разграничение: что проверяется полностью за `|S|^ω`, что условно трудно, какие классы тождеств доступны для компактного Rust primitive.
10. **[LIT-063 — Combinatorial Bounds for List Recovery… (STOC'26)](catalog/LITERATURE.md#lit-063)**. Важный overlap с кодами, но ASET d=2 и list recovery имеют различные допустимые сообщения/ошибки, так что копировать показатели нельзя.

**P2 — широкое теоретическое питание, без немедленной продуктовой реализации.**

- [LIT-061](catalog/LITERATURE.md#lit-061), [LIT-062](catalog/LITERATURE.md#lit-062), [LIT-055](catalog/LITERATURE.md#lit-055): sampling, распределительная сложность, зависимость от параллельной работы и memory/sample.
- [LIT-057](catalog/LITERATURE.md#lit-057), [LIT-069](catalog/LITERATURE.md#lit-069), [LIT-070](catalog/LITERATURE.md#lit-070): алгебраические схемы, пороговые схемы и ограниченная глубина формальных доказательств.
- [LIT-058](catalog/LITERATURE.md#lit-058), [LIT-074](catalog/LITERATURE.md#lit-074): статические графовые структурные ускорения; подсказки для partitioning, не готовые динамические структуры.
- [LIT-064](catalog/LITERATURE.md#lit-064), [LIT-068](catalog/LITERATURE.md#lit-068), [LIT-071](catalog/LITERATURE.md#lit-071), [LIT-072](catalog/LITERATURE.md#lit-072): local independence, cell probes, pseudorandom edit-tolerant codes, text indexing.

## Следующие точные исследования (не запускать до gate)

| № | Результат на выходе | Kill condition |
| --- | --- | --- |
| Q1 | Заморозить cell-probe + physical-write модель TOM и сравнить с LIT-052/053 | Существующая конструкция даёт требуемую tradeoff или барьер запрещает proof route |
| Q2 | Понять, что из LIT-050/051/060/070 говорит о размере **конкретных** ASET SAT сертификатов | Нет корректного сохранения proof-system или поля ⇒ **STOP TRANSFER** |
| Q3 | Вычислить на независимых small instances разрыв между ошибкой ED-approx и фактическими delta patch bytes | Обычный trial encoder доминирует => **NO-GO** |
| Q4 | Проверить экспериментальный headroom после FastDelta/SpeedSketch и Git path-walk | Нет Pareto-улучшения по CPU+index+wire => **NO-GO** |
| Q5 | Для discrete sampling/structured counting выбрать явное пространство состояний, оракул и строгую погрешность | Только abstract sampling convergence без operational contract => **SCOUT ONLY** |

## Решение

**ACCEPT_PUBLICATION_METADATA / NOT THEOREM_VERIFICATION / NOT PRODUCT_GO**. 26 публикаций не дублируют DOI/заглавия предыдущих 49, каждый пункт имеет русское оригинальное содержание, ограничения применимости и ссылку на закреплённую research family. Только в отдельном исследовании допустимо сформулировать новую теорему после полного определения модели, проверки первичных proofs и поиска опровергающих случаев. G2B-B2, HYP/ASET алгоритмы, D13B и DELSK production untouched.
