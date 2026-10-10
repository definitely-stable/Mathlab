# TKG-001 G1-A — строгая граница применимости DAG lower bounds, page costs и двух часов provenance

**2026-10-10 source correction:** [IMPORT-011 external PDF audit](RESEARCH-LITERATURE-011-EXTERNAL-PDF-AUDIT-2026.md). LycheeMemory V2 supplies empirical consolidation/LLM-cost baselines only, not strict bitemporal, Byzantine, causal or freshness guarantees. Graph topology/persistent-homology cycles do not imply semantic contradictions; causal association does not imply provenance authentication. Cryptographic roots require independently trusted monotone publication for latest/fork claims, and CRDT joins do not preserve arbitrary DAG acyclicity for free.

Дата: 2026-10-10. [Issue #210](https://github.com/definitely-stable/Mathlab/issues/210), [G1 #195](https://github.com/definitely-stable/Mathlab/issues/195), [DAG-002 #133](https://github.com/definitely-stable/Mathlab/issues/133), [TKG-001 G0](TKG-001-G0-BITEMPORAL-PROVENANCE-AND-RECOURSE.md).

**CLASSICAL_TRANSFER_FIREWALL / EXACT_FINITE_ORACLES / PAID_LOGICAL_PAGE_IMAGES / NO_NEW_JOINT_LOWER_BOUND / NO_PHYSICAL_SSD / NO_CRYPTO / NO_PRODUCTION_RAG.**

## 1. Первичные результаты и строго разные модели

| Уже импортированный источник | Что доказано или предложено | Запрещённый без дополнительного доказательства перенос |
| --- | --- | --- |
| [LIT-298 Larsen–Yu, SIAM online 2025](https://doi.org/10.1137/24M1638215) | Super-logarithmic cell-probe lower bound для DAG с edge insertions между существующими вершинами; вариант теоремы в авторском тексте: \`t_q = Omega(log^(3/2)n / log²(t_u w))\` при обозначенных ограничениях на w и стоимости | Нижняя граница **не установлена** для строго append-only new-sink DAG, ограниченного remote graph oracle и immutable old labels; cell probe не равен SSD page-write |
| [LIT-187 Bulteau et al., SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9) | Append-only DAG индекс с неизменными старыми метками, цепочками и manifest; разные режимы query/memory | Не поддерживает произвольную вставку ребра между старыми вершинами и bitemporal retractions |
| [LIT-252 Green et al., PODS 2007](https://doi.org/10.1145/1265530.1265535) | Факторизуемая semiring provenance | Не является защищённым proof-of-absence или проверенной свежестью |
| [LIT-255 EDBT 2026](https://doi.org/10.48786/EDBT.2026.05), [LIT-254 FM 2026](https://doi.org/10.1007/978-3-032-26220-2_18) | Incremental provenance sketches, counted derivation and dynamic reachability | Sketch и abstract-interpretation имеют другие ошибки/семантику и не дают бесплатного exact complete output |
| [LIT-260 SAND 2026](https://doi.org/10.4230/LIPIcs.SAND.2026.5) | Point/interval temporal graph reachability complexity gap | Temporal journey (последовательность контактов) ≠ one fixed valid-time snapshot всех рёбер |

### Теорема L1 — сохранность старой пары (элементарная, не новая)

Пусть Gₙ содержит n старых вершин, а \`append(v,P_v)\` добавляет **только новую вершину v** с входящими arcs \`u→v\` для u из Gₙ, не добавляя исходящих из v arcs к старым вершинам. Тогда для любых старых u,w:
\`Reach(Gₙ,u,w) = Reach(Gₙ₊₁,u,w)\`.

**Доказательство.** Путь между двумя старыми вершинами в новом графе не может пройти через v: если он дошёл до v, выйти к старым вершинам невозможно, поскольку v — sink. Все ребра между старым множеством остались прежними. Следовательно, множества путей между старой парой равны. QED. Индукция по числу append сохраняет свойство для всех более поздних обновлений.

**Минимальный контрпример к переносу на существующее edge insertion.** На фиксированных вершинах 0,1,2 до вставок нет пути 0→2, затем вставляем 0→1 и 1→2: достижимость старой пары меняется. Уже одна вставка 0→1 на двух старых вершинах достаточна; трёхвершинный пример делает видимой транзитивность.

**Фальсификация:** все 64 topologically numbered DAG на четырёх старых вершинах × 16 подмножеств родителей нового sink = 1024 случаев; для каждого сравнить DFS с независимым Boolean Warshall и старые reachability bits. Эти проверки не доказывают ни одну новую асимптотическую нижнюю границу.

### Теорема L2 — узкая zero-remote-probe entropy barrier (уже DAG-002 G0)

На фиксированной антицепи из n старых вершин родительское множество S нового sink может быть любым из \`2^n\`. Если query может использовать только два immutable endpoint labels и mutable manifest без **какого-либо иного** input-dependent state/probes, суммарная длина нового label b и manifest g должна удовлетворять \`b+g>=n\`. Это прежнее ограничение DAG-002, а не новый G1-result.

**Неверное усиление, отвергаемое точным контрпримером:** \`b+g+q*w>=n\`, где q — число remote probe **одного запроса**, w — бит в ячейке. Для произвольного n положим b=g=0, удалённо сохраним n-битный bitmap S и публикуем один бит в заранее известном адресе i на запрос \`Reach(i,v)\`; q=1. При n=65,w=8 имеем \`q*w=8<65\`. Объём remote state в 65 бит и page image writes обязателен: **не бесплатен**. Почему нет инъекции в q бит: разные запросы читают **разные адреса** общего bitmap, а не одну общую q-битную строку.

## 2. Платные baseline в одной ограниченной единице

\`page_bytes=P\`, каждый \`page image = 8P\` бит; логический full-image write/read платится отдельно. Cache и data-address public в финитном источниковом контракте; диск, журнал durably committed snapshots, GC, клиентский bootstrap labels и trusted roots **не включены**, поэтому это НЕ NAND / SSD benchmark.

| Scheme | Client bits | Remote payload | Publish writes | Worst-case query remote reads | Trust + scope |
| --- | --- | --- | --- | --- | --- |
| Public parent bitlabel | n | 0 | ceil(n/(8P)) source label-page writes | 0 *после клиентского получения метки* | Клиент обязан иметь n-bit label; холодная доставка отдельно |
| Remote parent bitmap | 0 | n bits | ceil(n/(8P)) | 1 | Адрес старого u публичен; no auth/freshness |
| Header + one-parent-per-page append log | 0 | (d+1)P bytes | d+1 | d+1 (скан всех, включая отсутствие) | 1 платный header, отсутствие уплотнения, no index |

Каждый `parent ID` в log занимает не более одной страницы, поэтому вариант намеренно **отклоняет n>2^(8P)**, когда ID не помещается в запись; это не заявленный универсальный оптимальный журнал.

Для каждой scheme exact bit membership эквивалентен \`u∈S\`. Определение \`b,g,q,w,P\` не склеивает word-RAM operations, cell-probe and physical device I/O. Материализованный update-all-reachability baseline, page-accurate GC, timestamps и negative-certificate не выполнены в G1-A: **G1 #195 остаётся открытой**. Нулевой remote Q для локальной метки — **не нулевой полный системный I/O**.

## 3. Bitemporal история и граница сертификатов

TKG-001 G0 допускает \`add(id,src,dst,[valid_from,valid_to))\` между уже существующими вершинами и \`retract(id)\` в epoch s; это нарушает чистый new-sink append контракт. Для дуг 0→1 (valid [0,12)) и 1→2 (valid [-10,5)) запрос \`Q(0,2;s,t=3)\` получает разные значения при epoch до/после второго добавления; при retraction ещё раз меняется, а запрос к историческому epoch остаётся прежним.

\`verify_positive_witness\` удостоверяет только путь по локальному честному снимку. Полный отрицательный сертификат и аутентифицированная свежесть **не следуют**. Модель G1 обязана отдельно оплатить bits/page reads для доказательства отсутствия и freshness/trusted root; отсутствие доступа к актуальному независимому epoch-якорю допускает indistinguishability stale snapshot (UCT-005 G3-B2).

## 4. Что именно НЕ доказано

- Нет resource-preserving reduction от Larsen–Yu к new-sink model и нет нового нижнего ограничения на W_pages × Q_pages × certificate bits.
- Нет доказанного оптимума index size vs update recourse under compaction, никакого physical SSD evidence.
- Динамическое пересоздание/удаление evidence IDs не моделируется immutable old labels.
- Стоимость proof enumeration экспоненциальна по diamonds, но факторизация может оставаться линейной; это классический polynomial provenance, не новый joint theorem.

**NEXT G1-B:** фиксировать единый полностью специфицированный page-store с RAM cap, immutable historical roots, trust publications и materialized answer-index; затем конечный поиск сравнимых worst-case нижних границ или \`STOP_NO_NOVEL_JOINT_BOUND\`. Не допускать скрытого free oracle/query state. Исследование не вносит новых bibliographic IDs: все пять обязательных первоисточников уже находятся в canonical catalog, дублировать запрещено.
