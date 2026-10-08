# RESEARCH-LITERATURE-003 — широта исследований 2026 и проверка перспективности

Дата: **2026-10-08** · [Issue #57](https://github.com/definitely-stable/Mathlab/issues/57).  
Базовый Mathlab: f039c269bbd78031d415f50d3320993cdc8e78fe.  
Статус: **CURATED PRIMARY ABSTRACTS / NO INDEPENDENT PROOF OR BENCHMARK VERIFICATION**.  
[Полный каталог](LITERATURE.md) · [обратные связи](LITERATURE-BY-RESEARCH.md) · [метаданные](literature.json).

## Что добавлено и почему это не очередная коллекция sketch

Добавлены **20 уникальных публикаций 2026 года**, LIT-050–069. Всего **69 работ вместо 49**. 16 опубликованных proceedings/DOI и 4 авторских arXiv preprint. **0 новых работ относятся к sketch/reconciliation.** Существующие 49 записей и 61 внутреннее исследование не изменяют своих научных статусов. Каталог теперь охватывает 10 направлений вместо 5.

| Направление новой выборки | Число | Главный научный интерес |
| --- | ---: | --- |
| Сжатые структуры/индексация/строки | 5 | локальность, стоимость динамических изменений, нижние границы запросов |
| Машинные сертификаты/верификация | 7 | независимая проверка, доверенная база, Lean и Rocq |
| Инкрементальные алгоритмы | 2 | известные изменённые позиции, монотонные бюджеты |
| Онлайн-оптимизация и границы | 2 | доступ к будущему, ограничения класса алгоритмов |
| Динамический поиск по шаблону | 1 | параметризация изменений, условная сложность |
| Динамические гиперграфы | 1 | аппроксимация и batch-work |
| Алгебраические алгоритмы | 2 | sparse matrices, модульные subset sum |

**Проверка:** у каждой записи есть официальный DOI либо первичный arXiv, название, год, краткая научная формулировка, ограничение на перенос, связь ML/DL/DM/OM и provenance категории model_overlap. Исторические документы не содержали буквальных ссылок на большинство новых работ: model_overlap это тематическая связь, а не утверждение о цитировании. В полном тексте статей не воспроизводились доказательства и опубликованные бенчмарки.

## Приоритет A — работы, из которых есть конкретная экспериментальная или теоремная постановка

1. **[PBLean, LIT-063](https://arxiv.org/abs/2602.08692)** — Stefan Szeider, preprint 2026. Reflective VeriPB checker с доказанной в Lean корректностью и проверяемыми кодировками исходных комбинаторных задач. **Для Mathlab:** проверить не просто UNSAT сертификат G2B, а корректность перевода самой ASET-модели в CNF/PB. VeriPB не является DRAT, а кодировки не переносимы автоматически.
2. **[Mechanized Dominator Tree Certification, LIT-066](https://doi.org/10.1145/3779031.3779107)** — Léchenet, CPP 2026. Быстрый расчёт и отдельно формально проверенный Rocq валидатор. **Для TOM:** определить минимальные размеры сертификатов и стоимость проверяющего вместо абстрактного утверждения об инкрементальной полезности.
3. **[Certificate-Carrying Transformation, LIT-064](https://arxiv.org/abs/2607.00563)** — Si/Zhang, preprint Jul 2026. Недоверенный преобразователь, fail-closed checker и формализованные условия сохранения наблюдаемого поведения. **Для TOM:** no-effect certificate должен зависеть от явно заданного наблюдателя и interleavings; контрпример при другом schedule обязателен.
4. **[DeltaSort, LIT-055](https://doi.org/10.4230/LIPIcs.SEA.2026.18)** — Dwivedi, SEA 2026. Ожидаемое O(n sqrt(k)) и O(k) дополнительной памяти **при заранее известных k изменённых индексах и random update assumption**. **Для Mathlab:** сравнить доверенный список изменённых координат с недоверенным, считать стоимость его получения и проверки.
5. **[Dynamic Grammar-Compressed Self-Index, LIT-050](https://doi.org/10.4230/LIPIcs.ESA.2026.6)** — Nishimoto/Tabei, ESA 2026. Динамическое δ-optimal индексирование повторяющихся текстов. **Для ChunkShift/DELSK:** отдельно измерять изменённые байты persistent representation и амортизированную стоимость обновления; авторские expected index bounds не дают byte-locality.
6. **[OptFSST, LIT-052](https://arxiv.org/abs/2607.11271)** — Chehaidar et al., preprint Jul 2026. Оптимальное DP-кодирование **при фиксированной** таблице символов, обобщённый выбор таблицы NP-hard. **Для продуктового дизайна:** отделить exact inner optimizer от heuristic candidate selection, как для patch-base+codec.
7. **[Hardness of Frequency-Related Queries on Compressed Strings, LIT-051](https://doi.org/10.4230/LIPIcs.ESA.2026.143)** — De/Kempa, ESA 2026. Ограничения запросов по grammar/LZ строкам. **Для Mathlab:** честно зафиксировать источник условных нижних границ; не переносить их на любую сжатую структуру.
8. **[Dynamic Pattern Matching with Wildcards, LIT-058](https://doi.org/10.4230/LIPIcs.STACS.2026.68)** — Naeini et al., STACS 2026. Параметризованные суб-линейные обновления и SETH-обусловленный барьер. **Для TOM:** исследовать роль числа изменяемых/неопределённых позиций; отсутствие wildcard — другая задача.
9. **[Robustifying Sparse Matrix Multiplication, LIT-060](https://doi.org/10.4230/LIPIcs.ESA.2026.157)** — Bringmann/Fischer/Nakos, ESA 2026. Чёрноящичная sparse-to-robust reduction с polylog overhead. **Для математических идей:** стиль reduction-first, но приближённый top-k не равен exact GF(q) subset sum.
10. **[Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes, LIT-065](https://arxiv.org/abs/2606.09600)** — Florath, preprint Jun 2026. Lean-структуры сертификатов точных covering-code чисел. **Для Mathlab:** способ хранения/проверки конечных witness bounds, не перенос чисел K_q на ASET.
11. **[Formalization of a Proof Calculus for Incremental Linearization, LIT-062](https://doi.org/10.1145/3779031.3779111)** — Mascarenhas et al., CPP 2026. Lean-модель proof rules SMT cvc5. **Для Mathlab:** soundness правил и полнота SMT-алгоритма не одно и то же.
12. **[Model-Generic Incrementally Verifiable Computation, LIT-068](https://doi.org/10.4230/LIPIcs.ITCS.2026.6)** — ITCS 2026. Верифицируемые инкрементальные вычисления при cryptographic soundness. **Для TOM:** computational soundness нельзя назвать строгой информационно-теоретической точностью без assumptions.

## Приоритет B — смежные идеи с отдельными границами

- [LIT-053 Relative Compressed Reverse Suffix Array](https://doi.org/10.4230/LIPIcs.STACS.2026.62) — относительный индекс требует уже имеющегося FM-index; не является delta patch.
- [LIT-054 Efficient Compression in Semigroups](https://doi.org/10.4230/LIPIcs.STACS.2026.80) — прямая algebraic straight-line-program compression; не файлы.
- [LIT-056 Incremental Submodular Maximization](https://doi.org/10.4230/LIPIcs.ESA.2026.134) — 1.373 vs lower 1.25, но growing constraint — не обновления входа.
- [LIT-057 Online and Incremental Fractional Vertex Cover](https://doi.org/10.4230/LIPIcs.ESA.2026.158) — online 11/6 против offline-known-updates 3/2: знание будущего меняет задачу.
- [LIT-059 Fully Dynamic Spectral Sparsification for Directed Hypergraphs](https://doi.org/10.4230/LIPIcs.STACS.2026.38) — динамические спектральные аппроксимации, не точные множества.
- [LIT-061 Improving Lagarias-Odlyzko for Average-Case Subset Sum](https://doi.org/10.4230/LIPIcs.STACS.2026.57) — решается случайный integer subset sum, а не детерминированные GF(q) суммы.
- [LIT-067 Towards Composable Proofs of Cache Coherence](https://doi.org/10.1145/3779031.3779106) — локальные Lean инварианты композиции MSI; не автоматически crash consistency CAS.
- [LIT-069 Lower Bounds for Ranking-Based Pivot Rules](https://doi.org/10.4230/LIPIcs.STACS.2026.31) — ограничения rank-information алгоритмов, не все algorithms.

## Следующие исследования — без фокуса на sketch

**P1 — Verified Incremental Change Certificate.** Конкретная Rust-операция могла бы принимать сохранённое состояние, обновление, доказательство неизменности и независимый checker. Теоретический вопрос: нижняя граница metadata+read probes при приёме *всех* настоящих no-effect обновлений. Перед новизной: сравнить LIT-055/064/066/068, TOM-003 и self-adjusting computation; доказать информационный model или закрыть направление. Ставить NO-GO, если verifier фактически читает весь input.

**P2 — Proof-Carrying Finite Extremal Search.** ASET компьютерные значения с отдельным доказанно корректным encoder model → CNF/PB → proof checker → Lean theorem. Первые источники LIT-063/065 и действующий G2B DRAT pipeline. Цель — независимость от ошибочных encoder premises, не очередной solver.

**P3 — Edit-Local Compressed Representation.** В frozen exact-byte model сопоставить 2026 dynamic RR-index, known-update DeltaSort, Chonkers (2025), synchronizing sets (2026) и strong history-independent trees. Определять worst-case rewrite bytes, update CPU, space and canonicality раздельно. Ни один отдельный источник не гарантирует всё одновременно.

**P4 — Conditional Lower-Bound Registry.** Исследовать когда SETH/Cell-probe/online adversary/cryptography связаны с TOM/ASET, и запрещать неразмеченные перенесения. Проверять контрпримеры на ослабление premises.

**P5 — Algebraic Reduction Bench.** Модулярные subset sum и robust sparse matrix algorithms — только методологический prior art. Не называть их без готового формального reduction новым декодером.

## Практика импорта

Только metadata + оригинальные краткие аннотации, идентификаторы DOI/arXiv, pinned origin из ранее существующего каталога и явно model_overlap. Новые статьи не добавляются в число 61 внутренних математических доказательств и не получают статус THEOREM. Предусмотрены офлайн проверки публикационного года, отличия preprint/proceedings, уникальности ID, названий 4 preprint, невыдуманных cited edges, возрастающего индекса и детерминированных cross-links. Lean, Rust, сторонние бинарники и PDF не импортируются.
