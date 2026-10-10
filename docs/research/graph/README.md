# Mathlab research graph / AI retrieval v1

**Статус:** инфраструктура поиска, а не новая теорема. Граф и связи не доказывают математических утверждений.

## Архитектура

**Единственный источник научных данных — существующие реестры; граф является производным индексом.** Не создавать второй ручной каталог с копиями заголовков, публикаций, авторов, научных статусов и proof grades.

| Реестр | Данные | Узлы графа |
| --- | --- | --- |
| catalog/registry.json | собственные исследования и связанные проекты | R:ML-001, R:DM-001 и др. |
| catalog/literature.json | DOI/arXiv/издатель, проверка и ограничения источника | P:LIT-355 |
| UCT-005-THEOREM-TREE.json | организация UCT-005 и корректные научные статусы | T:UCT005 |
| KNOWN-AND-STOPPED-RESEARCH.json | классические и отрицательные результаты | K:KR-001 |
| UCT-005-G4-TYPED-BRIDGES.json | контрмодели и типизированные переносы | B:G4-B01 |
| IMPORT-012-SOURCE-GENEALOGY.json | подтверждённые source relations и STOP gates | P:LIT-* ↔ R:ML-* |
| graph/curation.json | двуязычные концепты, aliases, аннотации документов, links к Issue | TAG:*, ISSUE:* |

Генератор также **автоматически сканирует каждый будущий Markdown** из docs/research и добавляет полнотекстовые фрагменты, даже если у нового документа ещё нет собственного реестрового ID. В таком случае не выдумываются научные зависимости. Миграция всех старых документов на YAML frontmatter не требуется: автоматические (по canonical registry) теги и необязательный sidecar устраняют двойное редактирование.

## Семантика и безопасность ссылок

- Исследования, публикации, деревья теорем, задачи, документы, фрагменты и понятия — **разные типы узлов**. IDs научных сущностей берутся из исходных реестров; переименование файла не меняет ID исследования.
- DOC:relative/path и C:hash — производные адреса документа и чанка, **не долговременные ID доказательства**. При перемещении файла обновить source path/redirect.
- Каждое ребро имеет from, to, relation, semantics, evidence_path и qualifier.
- ORG_TREE — организация, CATALOG_RELATED — связь каталога, SOURCE_GENEALOGY — источник/метод/STOP, TRACKS_RESEARCH — привязка задачи, DOCUMENTED_AT — provenance. Ни один из этих типов не является математическим PROVES / IMPLIES.
- Для UCT-005 корневой статус всегда OPEN_UNPROVED до самостоятельной proof+novelty экспертизы; countermodel и unproved reduction не превращаются в следствие через кратчайший путь графа.
- Научная уверенность, верификация цитаты, статус issue, прохождение CI и близость retrieval — разные атрибуты, которые нельзя агрегировать в единственную величину confidence.
- Изолированный источник внутри graph не означает его отсутствие в научной литературе. Конфликтующие DOI/arXiv alias разрешаются только на каноническом каталоге.

## Команды

Только стандартная библиотека Python, без MCP/LLM/графовой БД. Команды из корня Mathlab:

~~~bash
python research/research_graph.py validate
python -m unittest discover -s research -p 'test_research_graph.py' -v
python research/research_graph.py build --out .work/research-graph

python research/research_graph.py search "GF5 signed trade" --limit 10
python research/research_graph.py search "аутентифицированная наблюдаемость" --limit 10
python research/research_graph.py search "page recourse" --kind internal_research
python research/research_graph.py neighbors T:UCT005 --hops 2
python research/research_graph.py neighbors P:LIT-355 --hops 1

# Fast repeated AI queries: SQLite FTS5, incremental sync by source hashes.
python research/research_graph_fts.py sync --jsonl .work/research-graph/retrieval.jsonl
python research/research_graph_fts.py search "GF5 signed trade" --limit 10
python research/research_graph_fts.py search "граф памяти" --limit 10
~~~

Build outputs: graph.json (nodes+evidence edges), graph.jsonld (JSON-LD 1.1 projection, NOT RO-Crate), adjacency.json (outbound+reverse inbound), retrieval.jsonl (node/chunk searchable records), manifest.json (SHA-256 input inventory), INDEX.md. CI research-graph-integrity builds this index as an Actions artifact on GitHub-hosted runner. It is **derived**, not a separately edited source; no generated JSON should be used as authority for theorem proof or bibliography.

AI pipeline: exact ID/lexical + RU/EN aliases + tags + title + summary/limitations + Markdown chunks; graph expansion via neighbors; verify evidence_path and exact commit; optional external embedding/BM25 reranker on retrieval.jsonl, without adding hallucinated edges. Future quality eval: fixed bilingual relevance fixtures, recall@k/precision@k, correct negative-claim retrieval, citation grounding and fresh/dated CI accuracy.

## Adding research in 2026 and later

1. **Новое исследование:** добавить каноническую запись в catalog/registry.json с новым стабильным ID, model scope, summary_ru, limitations_ru, local source path, topics и обоснованными related. Граф автоматически подхватит её при следующем build.
2. **Новая публикация:** проверить DOI/arXiv и alias на дубли, присвоить свободный LIT-ID на текущем main, указать verification, limits_ru, mentioned_in; сохранить существующие LIT-IDs; выполнить literature.py --write. Нельзя исполнять устаревший план LIT-206..215 буквально.
3. **Новый proof brick / STOP:** зафиксировать в существующем UCT tree или known/stopped registry с реальным scope; организационные связи не порождают доказательства.
4. **Новый Markdown:** автоматически попадёт в DOC и C-chunks. Для улучшения семантического поиска необязательно добавлять явные aliases/tags/focus в graph/curation.json. Синонимы задаются контролируемой taxonomy, а не свободными тегами с десятками вариаций.
5. **Новая связь:** определить тип, направление, проверяемый evidence_path и, при переносе математических результатов, формальное отображение предпосылок в исходном научном реестре. Негативный результат сохранять как поискозначимый, а не отбрасывать.
6. **Изменение ID/переименование:** старые scientific IDs не переиспользовать; path-based DOC обновить через canonical source, при необходимости сохранить alias mapping.
7. Перед слиянием запускать catalog.py --check, literature.py --check, research_graph.py validate, focused unit и полный GitHub-hosted Research CI на точном PR HEAD.

Когда PR #256/#257 станут частью main, генератор может читать их status/issue snapshot как **датированные** данные; он не выдаёт их за живой статус GitHub.

## Интероперабельность

Рекомендация: JSON-first + typed property graph + provenance + deterministic JSONL. Не выбирать Neo4j, NetworkX, RDF triple store или Cytoscape.js как обязательные зависимости. Добавлен отдельный JSON-LD 1.1 projection с полными node/edge IRIs и явными направленными предикатами. Это НЕ валидированный RO-Crate package, PROV-O доказательная модель или новый canonical registry. RO-Crate package можно построить отдельно при публикации материала; формат graph.json остаётся внутренним.

Стандарты для проверки внешней совместимости: JSON-LD 1.1 (W3C Recommendation, 2020), PROV-O (W3C Recommendation, 2013), RO-Crate 1.3 (текущая опубликованная линия, перепроверять перед экспортом) и стабильная 1.2 (2025); они не дают математических гарантий и не заменяют identity/proof registry. Простая выгрузка graph.json в JSON-LD без валидного context и IRIs не заявляется готовым RO-Crate.

## Ограничения

Версия 1 — text/metadata retrieval, а не готовая GraphRAG-LLM-система. Нет морфологического RU-поиска (FTS5 использует lexical Unicode tokenizer), эмбеддингов, онлайнового мониторинга PR/CI, proof checker и автоматической генерации утверждений. Графовые сообщества/центральности нельзя выдавать за оценку научной значимости. Generated fragments — индекс, а не независимая верификация исходника.

Пример трассы: ISSUE:105 → T:UCT005 → организационные theorem children; ISSUE:223 → T:UCT005G3B2D1B0 → DOC:...; ISSUE:230 → T:HYP105G5 (отдельная открытая ветка). Для любого ребра нужно открыть evidence_path и подтвердить реальную модель. Научная новизна UCT-005 остаётся OPEN_UNPROVED.

### Масштабирование без переиндексации вручную

Регенерация JSONL перечитывает изменившиеся canonical entries и Markdown, фиксируя хеши входов в manifest.json. Опциональный SQLite FTS5 кэш сравнивает SHA-256 записей: неизменные записи пропускаются, новые добавляются, изменённые заменяются, удалённые очищаются **в одной транзакции**. Это снижает стоимость повторного поиска при росте числа документов; первичная генерация графа остаётся полной/детерминированной. Измерений latency или качества релевантности пока нет.

Для точной научной ссылки использовать path + line_start/line_end + sha256 текста, затем проверять конкретный Git commit отдельно. Хеш текста не является криптографическим утверждением о подлинности автора или CI-сертификатом.

## Проверка поиска и автоматическое связывание будущих документов

В отличие от прежней статической гипотезы об «около 100 узлах», размер графа вычисляется при каждой сборке из актуального дерева файлов и каталогов. Каждое новое Markdown-исследование автоматически индексируется как `DOC` с отдельными текстовыми фрагментами, номером строки и SHA-256. Упоминания действующих `LIT-###` или `ML/DM/DL/OM-###` создают ребро `TEXT_MENTIONS_ID`: **это буквальная текстовая ссылка, НЕ проверенная библиографическая цитата и НЕ доказательство**. Неизвестные ID не превращаются в фиктивные сущности.

Стабильный набор русско-английских запросов и релевантных ID размещён в [retrieval-fixtures.json](retrieval-fixtures.json). Проходят проверку точные ID, словарь синонимов и обнаружение F1-документа по русской терминологии. Получить воспроизводимый отчёт:

~~~bash
python research/research_graph_eval.py --check \
  --report .work/research-graph/retrieval-evaluation.json
python -m unittest discover -s research -p 'test_research_graph_eval.py' -v
python research/research_graph.py neighbors R:ML-002 --hops 1 \
  --direction in --relation MAPS_TO_RESEARCH --max-nodes 500
~~~

Здесь `recall@k` измеряет **только попадание известных документов и записей**; он не означает полноту современной литературы или правильность исходной теоремы. Регрессионные запросы допускают дополнение новыми темами без перемещения старых ID. При расширении корпуса метрики и сложность поиска оцениваются отдельно на сохранённых relevance-метках. Для работы с новой статьёй импорт остаётся атомарным через канонический каталог и его исходные DOI/arXiv aliases.

## Анализ влияния новой или изменённой публикации

Для AI-агентов: `python research/research_graph.py impact P:LIT-355 --depth 2 --limit 100`. Вывод содержит пути `P:LIT → R:ML/DM/DL/OM → DOC` и, если они есть, обратные упоминания из Markdown. Каждое звено имеет `evidence_path`, `relation`, направление обхода и **тип достоверности**: `CURATED_MODEL_OVERLAP_NOT_PROOF`, `CATALOG_MENTION_NOT_PROOF` или `UNVERIFIED_TEXT_MENTION`. Это *список мест для ручной переоценки* при импорте новых papers, не автоматический перенос доказательств или статус CI. Глубина ограничена тремя, объём выдачи параметром `--limit`; научный статус не наследуется по пути.
