# External primary literature — тематический каталог

> Generated from `literature.json` by `research/literature.py`. Редактировать следует только JSON.

Срез: **2026-10-08** · **75** проверенных ссылок на первичные публикации/авторские рукописи.

**Критически важно:** проверенная библиография или авторский abstract не равны независимо проверенному доказательству, статистическому результату либо научной новизне. Точные условия — в каждой записи.

Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md). Внутренние исследования: [INDEX.md](INDEX.md).

| Направление | Записей |
| --- | ---: |
| [Кодирование, ограниченная поддержка, экстремальные границы](#sparse-coding) | 17 |
| [Динамические структуры, каноничность и локальность правок](#dynamic-data-structures) | 8 |
| [Инкрементальные вычисления и сертификаты](#incremental-computation) | 6 |
| [DELSK: поиск delta-базы, сжатие, признаки](#delta-base-selection) | 14 |
| [DeltaMeter: потоковые оценки и согласование множеств](#streaming-reconciliation) | 11 |
| [Сложность доказательств, сертификаты, PIT/IPS](#proof-complexity) | 4 |
| [Алгебраическая сложность и условные барьеры](#algebraic-complexity) | 4 |
| [Строки, edit distance и тонкая сложность](#fine-grained-algorithms) | 2 |
| [Динамические графы, обновления и алгоритмы](#graph-algorithms) | 6 |
| [Рандомизированная выборка, подсчёт, память](#randomized-sampling) | 3 |

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
**[Bounds and Constructions for overline-3-Separable Codes with Length 3](https://arxiv.org/abs/1507.00954)** (2015)

Границы и конструкции именно для 3-separable кодов длины 3, через partial Latin squares, perfect hashing и Steiner triple systems.

**Ограничение:** Речь о barred-3-separability (overline{3}), сильной fingerprinting-модели; нельзя без определения её отождествлять с обычным 3-separable или ASET d=2.

**Идентичность:** `arxiv:1507.00954` · **Авторы:** Minquan Cheng, Jing Jiang, Haiyan Li, Ying Miao, Xiaohu Tang · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

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

### LIT-033
**[Sign-Compute-Resolve for Tree Splitting Random Access](https://arxiv.org/abs/1602.02612)** (2016)

Суммы сигнатур активных передатчиков в физическом канале используются для восстановления участников при известной bound K.

**Ограничение:** Подпись в физическом аддер-канале и adaptive tree-splitting не являются sparse GF(q) ASET-конструкцией со строгим весом столбцов.

**Идентичность:** `arxiv:1602.02612` · **Авторы:** Jasper Goseling, Cedomir Stefanovic, Petar Popovski · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-034
**[Finite Field Multiple Access](https://arxiv.org/abs/2303.14086)** (2023)

FFMA, element-pair codes и unique sum-pattern mapping по конечным полям, обеспечивающие мультиплексирование в многопользовательском канале.

**Ограничение:** Результаты о channel coding/error curves не задают автоматически максимум ASET при ограничении числа ненулевых координат.

**Идентичность:** `arxiv:2303.14086` · **Авторы:** Qi-yue Yu, Jiang-xuan Li, Shu Lin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-035
**[Signature codes for weighted binary adder channel and multimedia fingerprinting](https://arxiv.org/abs/1905.10180)** (2019)

Исследуются signature-code конструкции для взвешенного аддер-канала и fingerprinting, близкие по допустимым коэффициентам к ограниченным суммам.

**Ограничение:** Взвешенная сумма и реальные/целочисленные коэффициенты не тождественны полевым суммам с коэффициентами лишь 0/1.

**Идентичность:** `arxiv:1905.10180` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-036
**[On Constant-Weight Binary B2-Sequences](https://arxiv.org/abs/2303.12990)** (2023)

Бинарные B₂-последовательности с постоянным весом — прямой формальный сосед hard-column-support ёмкости ASET.

**Ограничение:** Определение B₂ допускает собственное правило для повторяющихся слагаемых и обычные целые суммы: проверять связь со строгими d<=2 GF(q) subset sums.

**Идентичность:** `arxiv:2303.12990` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-037
**[Multi-Group Testing for Items with Real-Valued Status under Standard Arithmetic](https://arxiv.org/abs/1303.6020)** (2013)

Групповое тестирование со статусами произвольных вещественных значений и неадаптивными суммарными измерениями.

**Ограничение:** Объект — реальные арифметические суммы/measurement matrices, не конечнополевые уникальные subset sums.

**Идентичность:** `arxiv:1303.6020` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-043
**[Sparse Parity-Check Matrices over GF(q)](https://doi.org/10.1017/S0963548304006625)** (2005)

Lefmann: максимальная длина разреженных parity-check матриц с заданным ограничением nonzeros/column и независимостью любого k столбцов; bounds по q,k,r.

**Ограничение:** Класс всех signed linear dependences отличается от ASET ограниченных 0/1 subset-sum collisions; возможно даёт достаточные семейства, но не точное равенство capacities.

**Идентичность:** `doi:10.1017/S0963548304006625` · **Авторы:** Hanno Lefmann · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-044
**[On Parity Check (0,1)-Matrix over Z_p](https://doi.org/10.1137/120881129)** (2015)

Bshouty–Mazzawi: неадаптивные additive queries и (0,1) parity-check матрицы над Z_p с независимостью любых k столбцов.

**Ограничение:** Ограничено двоичностью элементов матрицы и проверкой k-wise independence; не равнозначно ASET с hard column support w.

**Идентичность:** `doi:10.1137/120881129` · **Авторы:** Nader H. Bshouty, Hanna Mazzawi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-063
**[Combinatorial Bounds for List Recovery via Discrete Brascamp-Lieb Inequalities](https://doi.org/10.1145/3798129.3800756)** (2026)

Дискретные неравенства Браскампа–Либа используются для новых комбинаторных верхних границ размера списка при list recovery.

**Ограничение:** Декодирование при множестве допустимых символов в координате не есть инъективность 0/1/2-сумм, вес столбца ASET не ограничивается теми же параметрами.

**Идентичность:** `doi:10.1145/3798129.3800756` · **Авторы:** Joshua Brakensiek, Yeyuan Chen, Manik Dhar, Zihan Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-064
**[Locally Computable High Independence Hashing](https://doi.org/10.1145/3798129.3800855)** (2026)

Dodis–Lovett–Wichs: локально вычисляемые k-wise independent семейства хешей, включая неявные конструкции через lossless expanders.

**Ограничение:** Высокая k-wise независимость хеш-значений не тождественна линейной независимости столбцов или независимости от адаптивного противника.

**Идентичность:** `doi:10.1145/3798129.3800855` · **Авторы:** Yevgeniy Dodis, Shachar Lovett, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-071
**[Improved Pseudorandom Codes from Permuted Puzzles](https://doi.org/10.1145/3798129.3800916)** (2026)

Псевдослучайные коды с устойчивостью к редактированиям над бинарным алфавитом и ключ-известным атакам при обозначенных криптографических гипотезах.

**Ограничение:** Криптографическая неразличимость опирается на permuted puzzles conjecture; кодовая устойчивость к edit noise не равна точному ASET при малом числе ненулевых координат.

**Идентичность:** `doi:10.1145/3798129.3800916` · **Авторы:** Miranda Christ, Noah Golowich, Sam Gunn, Ankur Moitra, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [OM-122](INDEX.md#om-122)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


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
**[The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality](https://arxiv.org/abs/2509.11121)** (2025)

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

### LIT-052
**[The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843)** (2026)

Перенос natural-proofs barrier на статические и динамические cell-probe нижние границы через local и locally-updatable PRF при криптографических допущениях.

**Ограничение:** Барьер условен на существование конкретных PRF; не является доказательством отсутствия всех новых нижних границ и не переносится на физическую запись байтов.

**Идентичность:** `doi:10.1145/3798129.3800843` · **Авторы:** Michal Koucký, Bruno Loff, Tulasimohan Molli, Michael E. Saks · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-053
**[Compressing Dynamic Fully Indexable Dictionaries in Word-RAM](https://doi.org/10.1145/3798129.3800839)** (2026)

Domingues строит динамический rank/select словарь с near-information-theoretic пространством и худшим временем обновлений в Word-RAM.

**Ограничение:** Требует заданной модели предвычисленной таблицы и word multiplication; entropy redundancy не тождественен стоимости physical rewrites или history independence.

**Идентичность:** `doi:10.1145/3798129.3800839` · **Авторы:** Gabriel Marques Domingues · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-068
**[Sampling Permutations with Cell Probes Is Hard](https://doi.org/10.1145/3798129.3800743)** (2026)

Новые ограничения на выборку перестановок в модели cell probes связывают память, доступ к оракулу и сложность рандомизации.

**Ограничение:** Не доказывает сложность доступа к любой канонической сериализации или запрет на конкретный алгоритм random permutation.

**Идентичность:** `doi:10.1145/3798129.3800743` · **Авторы:** Yaroslav Alekseev, Mika Göös, Konstantin Myasnikov, Artur Riazanov, Dmitry Sokolov · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


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

### LIT-041
**[Certificates in Data Structures](https://arxiv.org/abs/1404.5743)** (2014)

Wang–Yin исследуют сертификаты ответов static cell-probe запросов и нижние границы на число прочитанных ячеек.

**Ограничение:** Сертификат в недетерминированной static query модели не равен runtime-maintained zero-effect сертификату для dynamic DAG.

**Идентичность:** `arxiv:1404.5743` · **Авторы:** Yaoyu Wang, Yitong Yin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-045
**[Complexity models for incremental computation](https://doi.org/10.1016/0304-3975(94)90159-7)** (1994)

Miltersen–Subramanian–Vitter–Tamassia классифицируют incremental complexity и вводят критерии lower bounds для online re-evaluation.

**Ограничение:** Это model-level фундамент, а не автоматическая теорема об update cost или bytes rewritten в TOM/O01.

**Идентичность:** `doi:10.1016/0304-3975(94)90159-7` · **Авторы:** Peter Bro Miltersen, Sairam Subramanian, Jeffrey Scott Vitter, Roberto Tamassia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-046
**[Lower And Upper Bounds For Incremental Algorithms](https://doi.org/10.7282/T3HT2SXD)** (1992)

Berman: relative incremental lower bound и δ-анализ для динамических update algorithms, включая обновление transitive closure.

**Ограничение:** Работа о сложностях в собственной модели; не устанавливает универсальное zero-effect certificate lower bound TOM.

**Идентичность:** `doi:10.7282/T3HT2SXD` · **Авторы:** A. Michael Berman · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)


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
**[FastCDC: A Fast and Efficient Content-Defined Chunking Approach for Data Deduplication](https://www.usenix.org/system/files/conference/atc16/atc16-paper-xia.pdf)** (2016)

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
**[SEDD: Scalable and Efficient Dataset Deduplication with GPUs](https://arxiv.org/abs/2501.01046)** (2025)

SEDD (Son–Kim–Lee) ускоряет потоковую крупномасштабную дедупликацию текстовых датасетов, включая MinHash/LSH GPU kernels, снижая сетевые и shuffle-затраты.

**Ограничение:** Первичный arXiv:2501.01046 имеет название SEDD, а не FED. Корпус и измерения относятся к текстовым LLM-datasets/GPU, не к выбору бинарной delta-базы DELSK.

**Идентичность:** `arxiv:2501.01046` · **Авторы:** Youngjun Son, Chaewon Kim, Jaejin Lee · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-002](INDEX.md#dl-002), [DL-007](INDEX.md#dl-007)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md) (cited)

### LIT-030
**[Odess: Speeding up Resemblance Detection for Redundancy Elimination by Fast Content-Defined Sampling](https://doi.org/10.1109/ICDE51399.2021.00048)** (2021)

Оригинальная конференционная работа Odess про fast content-defined sampling для ускорения resemblance.

**Ограничение:** Версия ICDE 2021 отличается от журнала ACM TOS 2023 по экспериментальной конфигурации/цифрам.

**Идентичность:** `doi:10.1109/ICDE51399.2021.00048` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-038
**[Chunk Content is not Enough: Chunk-Context Aware Resemblance Detection for Deduplication Delta Compression](https://arxiv.org/abs/2106.01273)** (2021)

Chunk-context features уточняют поиск похожих блоков при delta compression; соседний prior art к признакам и locality DELSK.

**Ограничение:** Context-dependent retrieval не доказывает optimal byte-savings у любого codec или самостоятельную новизну направленного scorer.

**Идентичность:** `arxiv:2106.01273` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/literature-review.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md) (cited)

### LIT-048
**[Binary Fuse Filters: Fast and Smaller Than Xor Filters](https://arxiv.org/abs/2201.01174)** (2022)

Graf–Lemire: approximate membership filters с меньшим overhead чем xor filters для дорогих storage lookup.

**Ограничение:** Структура ускоряет membership prefilter, не является скетчем similarity и не ранжирует delta patch reference candidates.

**Идентичность:** `arxiv:2201.01174` · **Авторы:** Thomas Mueller Graf, Daniel Lemire · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-007](INDEX.md#dl-007)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/lab-practices.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/lab-practices.md) (model_overlap)

### LIT-049
**[The Fuse XORier Lookup Table: Exploration, Implementation, and Revision of Probabilistic Sets and Maps](https://arxiv.org/abs/2312.13541)** (2023)

FXLT развивает probabilistic sets/maps и Bloomier-подобные lookup структуры на основе пространственного coupling.

**Ограничение:** Вероятностный lookup не равен stable source ordering и codec-aware patch gain ranking; benchmark автора не воспроизводился.

**Идентичность:** `arxiv:2312.13541` · **Авторы:** Eric Breyer, Alan Liu · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-007](INDEX.md#dl-007)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/lab-practices.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/lab-practices.md) (model_overlap)

### LIT-067
**[Once Rolling Hashing is Enough: Exploiting Rolling Hash Reuse in Delta Compression](https://doi.org/10.1145/3767295.3803596)** (2026)

FastDelta переиспользует rolling hashes одновременно при CDC, поиске похожих фрагментов и delta encoding, экономя повторные вычисления.

**Ограничение:** Shared hash pipeline не доказывает оптимальное направление reference selection и не равен выигрышу от нового similarity sketch; требуется измерять весь patch pipeline.

**Идентичность:** `doi:10.1145/3767295.3803596` · **Авторы:** Haoliang Tan, Wenhao Ou, Xiangyu Zou, Cai Deng, Yanqi Pan, Hao Huang, Zhaoquan Gu, Wen Xia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [EuroSys 2026](https://2026.eurosys.org/papers.html) · **Доступ:** `conference_paper_list_and_delsk_fulltext_review`

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002), [DL-006](INDEX.md#dl-006)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/claim-matrix.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/claim-matrix.md) (model_overlap)


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

**Идентичность:** `doi:10.1145/3651890.3672219` · **Также:** arxiv:2402.02668 · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

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

### LIT-039
**[Invertible Bloom Lookup Tables](https://arxiv.org/abs/1101.2245)** (2011)

Goodrich–Mitzenmacher: probabilistic invertible table поддерживает вставки, удаления и listing содержимого ниже порога загрузки.

**Ограничение:** Вероятностное full-listing не даёт строгого exact recovery при произвольной хэш-конфигурации и adversarial keys.

**Идентичность:** `arxiv:1101.2245` · **Также:** doi:10.1109/ALLERTON.2011.6120248 · **Авторы:** Michael T. Goodrich, Michael Mitzenmacher · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-006](INDEX.md#dm-006), [DM-008](INDEX.md#dm-008)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (model_overlap)

### LIT-040
**[Invertible Bloom Lookup Tables with Listing Guarantees](https://arxiv.org/abs/2212.13812)** (2022)

Worst-case гарантии listing для ограниченного числа элементов через stopping sets, Steiner systems и covering arrays.

**Ограничение:** Гарантированность зависит от конкретной детерминированной incidence-конструкции и предельной ёмкости, не любого hash-based IBLT.

**Идентичность:** `arxiv:2212.13812` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-006](INDEX.md#dm-006), [DM-008](INDEX.md#dm-008), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (model_overlap)

### LIT-042
**[Toward Optimal Time-Space Tradeoffs for Set Reconciliation](https://arxiv.org/abs/2609.14442)** (2026)

XYZ-Sketch заявляет O(1) update, примерно (1+ε)d передаваемых элементов и O(d log V) decode; fixed-support extremality остаётся условной гипотезой.

**Ограничение:** Это авторские гарантии в заданной модели; условная optimality не является безусловной lower bound, а payload элементов не сопоставлен с полным байтовым wire протоколом.

**Идентичность:** `arxiv:2609.14442` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-006](INDEX.md#dm-006), [DM-008](INDEX.md#dm-008), [DM-013](INDEX.md#dm-013)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (model_overlap)

### LIT-047
**[Tight Bounds for Low-Error Frequency Moment Estimation and the Power of Multiple Passes](https://arxiv.org/abs/2509.07599)** (2025)

Green-Maimon–Zamir: точные по порядку битовые F₂ bounds при малой относительной ошибке и separation по числу проходов.

**Ограничение:** Гарантия относится к классическому frequency moment, а не directly GF(2) set-only parity и не даёт finite-sample exact capacity.

**Идентичность:** `arxiv:2509.07599` · **Авторы:** Naomi Green-Maimon, Or Zamir · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-001](INDEX.md#dm-001), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [DELTAMETER:docs/research/REFERENCES.md](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/research/REFERENCES.md) (model_overlap)


## proof-complexity
*Сложность доказательств, сертификаты, PIT/IPS*

### LIT-050
**[Lower Bounds against the Ideal Proof System in Finite Fields](https://doi.org/10.1145/3798129.3800721)** (2026)

Elbaz и соавторы доказывают нижние границы для фрагментов IPS над конечными полями постоянного размера; конструкция knapsack и связи с AC0[p]-Frege.

**Ограничение:** Границы относятся к определённым классам алгебраических опровержений и глубин схем, а не к сложности всех DRAT-протоколов или ASET.

**Идентичность:** `doi:10.1145/3798129.3800721` · **Авторы:** Tal Elbaz, Nashlen Govindasamy, Jiaqi Lu, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-051
**[The Weak Rank Principle: Lower Bounds and Applications](https://doi.org/10.1145/3798129.3800735)** (2026)

Новые экспоненциальные нижние границы PCR над F2 для слабого rank principle и построение proof-complexity generators.

**Ограничение:** Алгебраические формулы XY=A и доказательства несостоятельности — не сертификат минимальной ёмкости конкретного ASET и не скорость SAT-решателя.

**Идентичность:** `doi:10.1145/3798129.3800735` · **Авторы:** Michal Garlík, Svyatoslav Gryaznov, Hanlin Ren, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-060
**[Polynomial Identity Testing and the Ideal Proof System: PIT Is in NP If and Only If IPS Can Be p-Simulated by a Cook-Reckhow Proof System](https://doi.org/10.1145/3798129.3800865)** (2026)

Grochow показывает эквивалентность эффективной детерминированной верифицируемости IPS при p-симуляции и включения PIT в NP (с оговорками о поле).

**Ограничение:** Не утверждается PIT∈NP и не предоставляется готовый детерминированный checker для произвольных полиномиальных схем.

**Идентичность:** `doi:10.1145/3798129.3800865` · **Авторы:** Joshua A. Grochow · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-070
**[Lower Bounds for Near-Quadratic-Depth Resolution over Parities](https://doi.org/10.1145/3798129.3800809)** (2026)

Экспоненциальные нижние границы длины refutation в Res(⊕) при глубине O(N^(2−ε)) для специальных Tseitin/CNF конструкций.

**Ограничение:** Доказательствo для глубинно ограниченного Res(⊕) не ограничивает произвольный SAT/DRAT checker и не доказывает трудность GF(5) ASET.

**Идентичность:** `doi:10.1145/3798129.3800809` · **Авторы:** Sreejata Kishor Bhattacharya, Farzan Byramji, Arkadev Chattopadhyay, Russell Impagliazzo · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## algebraic-complexity
*Алгебраическая сложность и условные барьеры*

### LIT-057
**[Closure under Factorization from a Result of Furstenberg](https://doi.org/10.1145/3798129.3800738)** (2026)

Из классической формулы Фюрстенберга выводится замкнутость формул и constant-depth алгебраических схем относительно множителей над полями характеристики ноль.

**Ограничение:** Результат не распространяется автоматически на малую положительную характеристику, noncommutative models и произвольные PIT black-box инструкции.

**Идентичность:** `doi:10.1145/3798129.3800738` · **Авторы:** Somnath Bhattacharjee, Mrinal Kumar, Shanthanu S. Rai, Varun Ramanathan, Ramprasad Saptharishi, Shubhangi Saraf · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [OM-135](INDEX.md#om-135)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-069
**[Superquadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://doi.org/10.1145/3798129.3800802)** (2026)

Chen–Tal–Wang устанавливают сверхквадратичные нижние границы размера схем глубины два с линейными threshold gates.

**Ограничение:** Предел схем глубины 2 не становится автоматически пределом общего вычисления, Fourier трансформов или динамических алгоритмов.

**Идентичность:** `doi:10.1145/3798129.3800802` · **Авторы:** Lijie Chen, Avishay Tal, Yichuan Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-130](INDEX.md#om-130), [OM-132](INDEX.md#om-132)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-073
**[Classifying Identities: Subcubic Distributivity Checking and Hardness from Arithmetic Progression Detection](https://doi.org/10.1145/3798129.3800854)** (2026)

Алгебраические тождества конечных операций классифицированы по complexity проверки; distributivity за O(|S|^ω) и условные tight lower bounds.

**Ограничение:** Условные reductions из triangle detection/AP detection не дают безусловного lower bound для любой конечной GF(q) арифметики или проверки Rust crate.

**Идентичность:** `doi:10.1145/3798129.3800854` · **Авторы:** Bartłomiej Dudek, Nick Fischer, Geri Gokaj, Ce Jin, Marvin Künnemann, Xiao Mao, Mirza Redžić · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-075
**[Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width](https://doi.org/10.4230/LIPIcs.ICALP.2026.130)** (2026)

Kluk–Nederlof: нижние границы 2^Ω(k log log k) для tropical-circuit pure DP задач связности/коммивояжёра при pathwidth k.

**Ограничение:** Граница относится к конкретной модели tropical circuits; алгебраические ускорения и общие DP алгоритмы вне класса не опровергаются.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.130` · **Авторы:** Kacper Kluk, Jesper Nederlof · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.130) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [OM-133](INDEX.md#om-133), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## fine-grained-algorithms
*Строки, edit distance и тонкая сложность*

### LIT-054
**[Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://doi.org/10.1145/3798129.3800789)** (2026)

Mao–Rubinstein: рандомизированные (1+ε)-ED и (1−ε)-LCS схемы с ускорением относительно n² на субквадратическом масштабе.

**Ограничение:** Аппроксимация расстояния между строками не даёт exact edit script, оптимальной delta patch-базы или онлайн обновлений.

**Идентичность:** `doi:10.1145/3798129.3800789` · **Авторы:** Xiao Mao, Aviad Rubinstein · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-072
**[Space-Efficient Text Indexing with Mismatches using Function Inversion](https://doi.org/10.1145/3798129.3800818)** (2026)

Bibbens–Borevitz–McCauley строят линейно-пространственный индекс поиска строк с ≤k Hamming mismatches и сглаженным tradeoff query/space.

**Ограничение:** Поиск при Hamming distance не покрывает вставки/удаления и не является автоматическим поиском минимальной delta patch-базы.

**Идентичность:** `doi:10.1145/3798129.3800818` · **Авторы:** Jackson Bibbens, Levi Borevitz, Samuel McCauley · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## graph-algorithms
*Динамические графы, обновления и алгоритмы*

### LIT-056
**[Incremental Shortest Paths in Almost Linear Time via a Modified Interior Point Method](https://doi.org/10.1145/3798129.3800733)** (2026)

Детерминированно поддерживаются приближённые односточечные кратчайшие пути при вставке рёбер, суммарно близко к линейному времени.

**Ограничение:** Алгоритм работает с ориентированными взвешенными графами и аппроксимацией расстояния; не сертификат отсутствия эффекта произвольной правки DAG.

**Идентичность:** `doi:10.1145/3798129.3800733` · **Авторы:** Yang P. Liu · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-058
**[Separator Theorem for Minor-Free Graphs in Linear Time](https://doi.org/10.1145/3798129.3800727)** (2026)

Найден линейно-временной алгоритм сбалансированного O(√n)-сепаратора в графах без фиксированного минора.

**Ограничение:** Алгоритм статический и зависит от фиксированного запрещённого минора; нельзя приписывать ему поддержку динамической графовой разметки за O(1).

**Идентичность:** `doi:10.1145/3798129.3800727` · **Авторы:** Édouard Bonnet, Tuukka Korhonen, Hung Le, Jason Li, Tomáš Masařík · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-059
**[A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://doi.org/10.1145/3798129.3800868)** (2026)

Chuzhoy–Khanna–Song: детерминированное поддержание максимального matching в полностью динамическом графе с амортизированным временем n^(1/2+o(1)).

**Ограничение:** Maximal не означает maximum; амортизированная bound не худшая на операцию и не переносится на graph refinement без модели.

**Идентичность:** `doi:10.1145/3798129.3800868` · **Авторы:** Julia Chuzhoy, Sanjeev Khanna, Junkai Song · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-131](INDEX.md#om-131), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-065
**[Dynamic Set Cover with Worst-Case Recourse](https://doi.org/10.4230/LIPIcs.ICALP.2026.153)** (2026)

Solomon–Uzrad изучают динамическое покрытие множеств и контролируют число замен в решении на каждом обновлении.

**Ограничение:** Recourse решений не эквивалентен количеству переписанных байт памяти; конечные worst-case bounds применимы к собственной динамической set-cover модели.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.153` · **Авторы:** Shay Solomon, Amitai Uzrad · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.153) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-066
**[Static to Dynamic Correlation Clustering](https://doi.org/10.4230/LIPIcs.ICALP.2026.48)** (2026)

Преобразование статической аппроксимации корреляционного кластеринга в полностью динамическую с O(1) worst-case update в заявленной модели.

**Ограничение:** Гарантия качества сохраняется с указанной вероятностью; это не точное поддержание всех кластеров и не универсальная динамическая оптимизация.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.48` · **Авторы:** Nairen Cao, Vincent Cohen-Addad, Euiwoong Lee, Shi Li, David Rasmussen Lolck, Alantha Newman, Mikkel Thorup, Lukas Vogl, Shuyi Yan, Hanwen Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.48) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-074
**[Deterministic Padded Decompositions and Negative-Weight Shortest Paths](https://doi.org/10.1145/3798129.3800722)** (2026)

Jason Li строит детерминированные padded decompositions ориентированных графов и почти линейный negative-weight SSSP.

**Ограничение:** Статический SSSP с отрицательными рёбрами не даёт incremental support или гарантий размера delta patch.

**Идентичность:** `doi:10.1145/3798129.3800722` · **Авторы:** Jason Li · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)


## randomized-sampling
*Рандомизированная выборка, подсчёт, память*

### LIT-055
**[A Unified Approach to Memory-Sample Tradeoffs for Detecting Planted Structures](https://doi.org/10.1145/3798129.3800739)** (2026)

Обобщённая схема нижних границ memory/sample для многопроходного обнаружения planted bicliques, sparse means и sparse PCA.

**Ограничение:** Распределительное различение planted-vs-null не равно set-only GF(2) строгой оценке d; число проходов и модель памяти должны совпасть.

**Идентичность:** `doi:10.1145/3798129.3800739` · **Авторы:** Sumegha Garg, Jabari Hastings, Chirag Pabbaraju, Vatsal Sharan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-061
**[Parallel Sampling via Autospeculation](https://doi.org/10.1145/3798129.3800828)** (2026)

Автоспекулятивная выборка с параллельным доступом к оракулам снижает ожидаемую глубину последовательного генерирования до примерно √n.

**Ограничение:** Выигрыш по параллельной глубине в oracle model не означает меньшую суммарную вычислительную работу, память или низкую latency Rust API.

**Идентичность:** `doi:10.1145/3798129.3800828` · **Авторы:** Nima Anari, Carlo Baronio, CJ Chen, Alireza Haqi, Frederic Koehler, Anqi Li, Thuy-Duong Vuong · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-113](INDEX.md#om-113), [OM-139](INDEX.md#om-139)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-062
**[Shifted Composition IV: Toward Ballistic Acceleration for Log-Concave Sampling](https://doi.org/10.1145/3798129.3800881)** (2026)

Altschuler–Chewi–Zhang исследуют недодемпфированную Langevin-динамику, KL ошибки дискретизации и ускоренную лог-вогнутую выборку.

**Ограничение:** Гарантии зависят от регулярности log-concave распределения, свойств ULD и модели oracle; не general uniform sampler для дискретных комбинаторных объектов.

**Идентичность:** `doi:10.1145/3798129.3800881` · **Авторы:** Jason M. Altschuler, Sinho Chewi, Matthew S. Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Проверенный издательский реестр:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [OM-113](INDEX.md#om-113)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/eee8e89e1d844bca9f418587d4c8ddba731c2673/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)
