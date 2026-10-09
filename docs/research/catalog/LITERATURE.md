# External primary literature — тематический каталог

> Generated from `literature.json` by `research/literature.py`. Редактировать следует только JSON.

Срез: **2026-10-09** · **212** проверенных ссылок на первичные публикации/авторские рукописи.

**Критически важно:** проверенная библиография или авторский abstract не равны независимо проверенному доказательству, статистическому результату либо научной новизне. Точные условия — в каждой записи.

Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md). Внутренние исследования: [INDEX.md](INDEX.md).

| Направление | Записей |
| --- | ---: |
| [Кодирование, ограниченная поддержка, экстремальные границы](#sparse-coding) | 23 |
| [Динамические структуры, каноничность и локальность правок](#dynamic-data-structures) | 29 |
| [Инкрементальные вычисления и сертификаты](#incremental-computation) | 21 |
| [DELSK: поиск delta-базы, сжатие, признаки](#delta-base-selection) | 15 |
| [DeltaMeter: потоковые оценки и согласование множеств](#streaming-reconciliation) | 14 |
| [Сжатые структуры, индексация строк и нижние границы](#compressed-indexing) | 12 |
| [Онлайн-оптимизация, конкурентные оценки и барьеры](#online-optimization) | 12 |
| [Кэширование, online paging, консистентность и память](#caching) | 7 |
| [Динамические графы, гиперграфы и sparsification](#graph-algorithms) | 19 |
| [Алгебраические алгоритмы, subset sum и разреженные матрицы](#algebraic-algorithms) | 14 |
| [Машинные доказательства, сертификаты и верификация](#proof-certification) | 23 |
| [Нижние границы доказательств, IPS/PIT и сертификаты](#proof-complexity) | 12 |
| [Алгебраические схемы, математика и нижние границы](#algebraic-complexity) | 4 |
| [Edit distance, строки и тонкая сложность](#fine-grained-algorithms) | 3 |
| [Рандомизированная выборка, подсчёт и memory-sample](#randomized-sampling) | 4 |

## sparse-coding
*Кодирование, ограниченная поддержка, экстремальные границы*

### LIT-001
**[Bounded-Contention Coding for Wireless Networks in the High SNR Regime](https://arxiv.org/abs/1208.6125)** (2012)

Кодирование для декодирования сумм ограниченного числа одновременных сообщений; исходный объект уже близок к бинарному bounded-active identification.

**Ограничение:** Коммуникационная модель и допускаемое число участников отличаются от строгой поддержки столбцов ASET.

**Идентичность:** `arxiv:1208.6125` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-002
**[Location-correcting codes](https://doi.org/10.1109/18.485724)** (1996)

Классическая граница для слабых множеств Сидона используется в Mathlab для строгой конечной оценки 10≤A₅^set(3,2,2)≤11.

**Ограничение:** ASET влечёт weak Sidon, но обратное неверно; correction locality из LCC не равна write locality ASET.

**Идентичность:** `doi:10.1109/18.485724` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-008](INDEX.md#ml-008), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md) (cited)

### LIT-003
**[Probabilistic existence results for separable codes](https://arxiv.org/abs/1505.02597)** (2015)

Blackburn сопоставляет frameproof и t-separable коды и устанавливает вероятностные границы; приводит специальные ограничения при t=2.

**Ограничение:** Descendant-модель не совпадает автоматически с ограниченными конечнополевыми суммами и изменяемой поддержкой ASET.

**Идентичность:** `arxiv:1505.02597` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-004
**[Bounds and Constructions for overline-3-Separable Codes with Length 3](https://arxiv.org/abs/1507.00954)** (2015)

Границы и конструкции именно для 3-separable кодов длины 3, через partial Latin squares, perfect hashing и Steiner triple systems.

**Ограничение:** Речь о barred-3-separability (overline{3}), сильной fingerprinting-модели; нельзя без определения её отождествлять с обычным 3-separable или ASET d=2.

**Идентичность:** `arxiv:1507.00954` · **Авторы:** Minquan Cheng, Jing Jiang, Haiyan Li, Ying Miao, Xiaohu Tang · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-005
**[Sharp bounds for uniform union-free hypergraphs](https://arxiv.org/abs/2605.11949)** (2026)

Асимптотические экстремальные результаты для t-union-free r-однородных гиперграфов, а также разреженные упаковки.

**Ограничение:** Совпадение объединений рёбер не тождественно совпадению модульных сумм в GF(q); особенно осторожно при нечётной характеристике.

**Идентичность:** `arxiv:2605.11949` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-006
**[On Codes with Support-Constrained Parity Checks](https://arxiv.org/abs/2605.08644)** (2026)

Оптимальное минимальное расстояние линейного кода при заданной маске поддержки строк проверочной матрицы; конструкции над достаточно большими полями.

**Ограничение:** Строковые parity-check ограничения и расстояние кода не дают автоматически границы мощности ASET со столбцовыми ограничениями.

**Идентичность:** `arxiv:2605.08644` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-031
**[Signature Codes for a Noisy Adder Multiple Access Channel](https://arxiv.org/abs/2206.10735)** (2022)

q-арные signature codes для noisier integer-adder multiple access, включая явные конструкции и converse bounds.

**Ограничение:** Сумма берётся над целыми и учитывает канал с шумом, в отличие от безошибочной конечнополевой ASET-суммы.

**Идентичность:** `arxiv:2206.10735` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (model_overlap)

### LIT-033
**[Sign-Compute-Resolve for Tree Splitting Random Access](https://arxiv.org/abs/1602.02612)** (2016)

Суммы сигнатур активных передатчиков в физическом канале используются для восстановления участников при известной bound K.

**Ограничение:** Подпись в физическом аддер-канале и adaptive tree-splitting не являются sparse GF(q) ASET-конструкцией со строгим весом столбцов.

**Идентичность:** `arxiv:1602.02612` · **Авторы:** Jasper Goseling, Cedomir Stefanovic, Petar Popovski · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-034
**[Finite Field Multiple Access](https://arxiv.org/abs/2303.14086)** (2023)

FFMA, element-pair codes и unique sum-pattern mapping по конечным полям, обеспечивающие мультиплексирование в многопользовательском канале.

**Ограничение:** Результаты о channel coding/error curves не задают автоматически максимум ASET при ограничении числа ненулевых координат.

**Идентичность:** `arxiv:2303.14086` · **Авторы:** Qi-yue Yu, Jiang-xuan Li, Shu Lin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-035
**[Signature codes for weighted binary adder channel and multimedia fingerprinting](https://arxiv.org/abs/1905.10180)** (2019)

Исследуются signature-code конструкции для взвешенного аддер-канала и fingerprinting, близкие по допустимым коэффициентам к ограниченным суммам.

**Ограничение:** Взвешенная сумма и реальные/целочисленные коэффициенты не тождественны полевым суммам с коэффициентами лишь 0/1.

**Идентичность:** `arxiv:1905.10180` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-036
**[On Constant-Weight Binary B2-Sequences](https://arxiv.org/abs/2303.12990)** (2023)

Бинарные B₂-последовательности с постоянным весом — прямой формальный сосед hard-column-support ёмкости ASET.

**Ограничение:** Определение B₂ допускает собственное правило для повторяющихся слагаемых и обычные целые суммы: проверять связь со строгими d<=2 GF(q) subset sums.

**Идентичность:** `arxiv:2303.12990` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-037
**[Multi-Group Testing for Items with Real-Valued Status under Standard Arithmetic](https://arxiv.org/abs/1303.6020)** (2013)

Групповое тестирование со статусами произвольных вещественных значений и неадаптивными суммарными измерениями.

**Ограничение:** Объект — реальные арифметические суммы/measurement matrices, не конечнополевые уникальные subset sums.

**Идентичность:** `arxiv:1303.6020` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-043
**[Sparse Parity-Check Matrices over GF(q)](https://doi.org/10.1017/S0963548304006625)** (2005)

Lefmann: максимальная длина разреженных parity-check матриц с заданным ограничением nonzeros/column и независимостью любого k столбцов; bounds по q,k,r.

**Ограничение:** Класс всех signed linear dependences отличается от ASET ограниченных 0/1 subset-sum collisions; возможно даёт достаточные семейства, но не точное равенство capacities.

**Идентичность:** `doi:10.1017/S0963548304006625` · **Авторы:** Hanno Lefmann · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-044
**[On Parity Check (0,1)-Matrix over Z_p](https://doi.org/10.1137/120881129)** (2015)

Bshouty–Mazzawi: неадаптивные additive queries и (0,1) parity-check матрицы над Z_p с независимостью любых k столбцов.

**Ограничение:** Ограничено двоичностью элементов матрицы и проверкой k-wise independence; не равнозначно ASET с hard column support w.

**Идентичность:** `doi:10.1137/120881129` · **Авторы:** Nader H. Bshouty, Hanna Mazzawi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-083
**[Combinatorial Bounds for List Recovery via Discrete Brascamp-Lieb Inequalities](https://doi.org/10.1145/3798129.3800756)** (2026)

Дискретные неравенства Браскампа–Либа используются для новых комбинаторных верхних границ размера списка при list recovery.

**Ограничение:** Декодирование при множестве допустимых символов в координате не есть инъективность 0/1/2-сумм, вес столбца ASET не ограничивается теми же параметрами.

**Идентичность:** `doi:10.1145/3798129.3800756` · **Авторы:** Joshua Brakensiek, Yeyuan Chen, Manik Dhar, Zihan Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-084
**[Locally Computable High Independence Hashing](https://doi.org/10.1145/3798129.3800855)** (2026)

Dodis–Lovett–Wichs: локально вычисляемые k-wise independent семейства хешей, включая неявные конструкции через lossless expanders.

**Ограничение:** Высокая k-wise независимость хеш-значений не тождественна линейной независимости столбцов или независимости от адаптивного противника.

**Идентичность:** `doi:10.1145/3798129.3800855` · **Авторы:** Yevgeniy Dodis, Shachar Lovett, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-091
**[Improved Pseudorandom Codes from Permuted Puzzles](https://doi.org/10.1145/3798129.3800916)** (2026)

Псевдослучайные коды с устойчивостью к редактированиям над бинарным алфавитом и ключ-известным атакам при обозначенных криптографических гипотезах.

**Ограничение:** Криптографическая неразличимость опирается на permuted puzzles conjecture; кодовая устойчивость к edit noise не равна точному ASET при малом числе ненулевых координат.

**Идентичность:** `doi:10.1145/3798129.3800916` · **Авторы:** Miranda Christ, Noah Golowich, Sam Gunn, Ankur Moitra, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [OM-122](INDEX.md#om-122)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-118
**[Lower bounds for adaptive locally decodable codes](https://doi.org/10.1002/rsa.20069)** (2005)

Классические нижние границы локального декодирования сообщений с адаптивными запросами к повреждённым кодовым словам.

**Ограничение:** Это read/query locality на шумных кодах, тогда как LENT-001 задаёт write/update locality; равенство понятий и автоматический перенос границ недопустимы.

**Идентичность:** `doi:10.1002/rsa.20069` · **Авторы:** Amit Deshpande, Rahul Jain, T. Kavitha, Satyanarayana V. Lokam, Jaikumar Radhakrishnan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-127
**[Locally Updatable and Locally Decodable Codes](https://doi.org/10.1007/978-3-642-54242-8_21)** (2014)

Chandran–Kanukurthi–Ostrovsky строят локально обновляемые и локально декодируемые коды в модели Prefix Hamming metric и исследуют приложения к динамическому доказательству хранения.

**Ограничение:** Одновременное ограничение числа записываемых/читаемых символов давно известно; ошибка декодирования, модель атакующего и условие префиксной метрики не совпадают с чистой Hamming-ball моделью UCT.

**Идентичность:** `doi:10.1007/978-3-642-54242-8_21` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-128
**[Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes](https://arxiv.org/abs/1305.3224)** (2013)

Mazumdar–Chandar–Wornell изучают компромисс скорости кода, локального восстановления и стоимости обновления при приближении к пропускной способности зашумленного канала.

**Ограничение:** Канальная capacity с шумом и требования восстановления не определяются одной безошибочной моделью графа изменений. Нужна явная редукция при переносе границ.

**Идентичность:** `arxiv:1305.3224` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-133
**[Tight upper and lower bounds for leakage-resilient, locally decodable and updatable non-malleable codes](https://doi.org/10.1016/j.ic.2019.05.001)** (2019)

Работа доказывает нижние и верхние ограничения локального декодирования/обновления криптографических кодов при недоверенном изменении и утечке информации.

**Ограничение:** Криптографическая немодифицируемость и leakage-resilience требуют другой adversary/security модели и не сводятся к доказательству безошибочной вместимости шаров Хэмминга.

**Идентичность:** `doi:10.1016/j.ic.2019.05.001` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-138
**[Improved bounds on the size of sparse parity check matrices](https://doi.org/10.1109/ISIT.2005.1523645)** (2005)

Naor и Verstraëte (IEEE ISIT 2005) исследуют экстремальное число разреженных столбцов, когда любые k из них линейно независимы, и выводят верхние границы редукцией к графам с запрещёнными циклами.

**Ограничение:** Результаты относятся к произвольным коэффициентам линейных зависимостей, а не к двум ограниченным по размеру подписанным суммам ASET. Точная формула показателя в HTML библиографическом abstract и авторском PDF форматируется различно; без проверки полного оригинала конкретную новую оценку при k=6,r=3 не утверждаем.

**Идентичность:** `doi:10.1109/ISIT.2005.1523645` · **Авторы:** Assaf Naor, Jacques Verstraëte · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-152
**[Parity check matrices and product representations of squares](https://doi.org/10.1007/s00493-008-2195-2)** (2008)

Naor и Verstraëte (Combinatorica 2008) исследуют верхние оценки числа разреженных k-wise независимых столбцов и связи с циклами в графах; полный журнальный текст развивает работу ISIT 2005.

**Ограничение:** Произвольные коэффициенты линейной зависимости существенно отличаются от ограниченных ±1 трёх-сумм. Формулы в абстрактах форматируются неоднозначно; не утверждать улучшения показателя для k=6,r=4 без проверки математического оригинала.

**Идентичность:** `doi:10.1007/s00493-008-2195-2` · **Авторы:** Assaf Naor, Jacques Verstraëte · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md) (model_overlap)


## dynamic-data-structures
*Динамические структуры, каноничность и локальность правок*

### LIT-007
**[History-Independent Dynamic Partitioning: Operation-Order Privacy in Ordered Data Structures](https://doi.org/10.1145/3651609)** (2024)

Динамические группы размера Θ(B) с O(1) ожидаемым числом операций вставки/удаления против oblivious adversary.

**Ограничение:** Операции по группам не равны физически переписанным байтам; нельзя усиливать модель до adaptive adversary без доказательства.

**Идентичность:** `doi:10.1145/3651609` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-008
**[History-Independent Dynamic Partitioning with Applications to B-Trees, Skip Lists and Fusion Trees](https://doi.org/10.1145/3810240)** (2026)

Расширенная версия истории-независимого разбиения с применениями к B-tree, fusion tree и skip list.

**Ограничение:** Не утверждает строгую каноничность физических байтов persistent rope или худший случай против адаптивного противника.

**Идентичность:** `doi:10.1145/3810240` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-009
**[The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality](https://arxiv.org/abs/2509.11121)** (2025)

Предложены одновременные строгие гарантии длины CDC-чанков и локальности правок; обсуждается структурное представление Yarn.

**Ограничение:** Авторский preprint; модель частичных изменений, byte writes и deterministic canonical physical layout нужно сопоставлять отдельно.

**Идентичность:** `arxiv:2509.11121` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-011
**[Optimal Time-Space Tradeoff for Dynamic Difference-Encoded Dictionaries](https://arxiv.org/abs/2608.06077)** (2026)

Гарантии сжатого gap-encoded словаря с динамическими операциями и сопоставимой нижней границей.

**Ограничение:** Стоимость ориентируется на gap(S), а не на history-independent физическое расположение и на write locality после string edits.

**Идентичность:** `arxiv:2608.06077` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-012
**[Time-Optimal Construction of String Synchronizing Sets](https://doi.org/10.4230/LIPIcs.STACS.2026.36)** (2026)

Оптимальное по word-RAM времени построение позиций синхронизации с локальной согласованностью контекстов строки.

**Ограничение:** Результат для статической подготовки/конструкции, не готовая динамическая worst-case гарантия редактирования CDC.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.36` · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-058
**[Dynamic Pattern Matching with Wildcards](https://doi.org/10.4230/LIPIcs.STACS.2026.68)** (2026)

Полностью динамическое сопоставление текста и шаблона с k wildcard: суб-линейная сложность при малом k и условный запрет части режимов через SETH.

**Ограничение:** Зависимость от количества wildcard и сильной экспоненциальной гипотезы — обязательная часть утверждения; не lower bound на обычную CDC сегментацию.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.68` · **Авторы:** Arshia Ataee Naeini, Amir-Parsa Mobed, Masoud Seddighin, Saeed Seddighin · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-072
**[The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843)** (2026)

Перенос natural-proofs barrier на статические и динамические cell-probe нижние границы через local и locally-updatable PRF при криптографических допущениях.

**Ограничение:** Барьер условен на существование конкретных PRF; не является доказательством отсутствия всех новых нижних границ и не переносится на физическую запись байтов.

**Идентичность:** `doi:10.1145/3798129.3800843` · **Авторы:** Michal Koucký, Bruno Loff, Tulasimohan Molli, Michael E. Saks · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-073
**[Compressing Dynamic Fully Indexable Dictionaries in Word-RAM](https://doi.org/10.1145/3798129.3800839)** (2026)

Domingues строит динамический rank/select словарь с near-information-theoretic пространством и худшим временем обновлений в Word-RAM.

**Ограничение:** Требует заданной модели предвычисленной таблицы и word multiplication; entropy redundancy не тождественен стоимости physical rewrites или history independence.

**Идентичность:** `doi:10.1145/3798129.3800839` · **Авторы:** Gabriel Marques Domingues · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-088
**[Sampling Permutations with Cell Probes Is Hard](https://doi.org/10.1145/3798129.3800743)** (2026)

Новые ограничения на выборку перестановок в модели cell probes связывают память, доступ к оракулу и сложность рандомизации.

**Ограничение:** Не доказывает сложность доступа к любой канонической сериализации или запрет на конкретный алгоритм random permutation.

**Идентичность:** `doi:10.1145/3798129.3800743` · **Авторы:** Yaroslav Alekseev, Mika Göös, Konstantin Myasnikov, Artur Riazanov, Dmitry Sokolov · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-099
**[Longest Common Extension of a Dynamic String in Parallel Constant Time](https://doi.org/10.4230/LIPIcs.CPM.2026.20)** (2026)

CPM 2026 строит динамическую иерархию string synchronizing sets и отвечает на LCE при вставке и удалении символов в параллельной модели.

**Ограничение:** CRCW PRAM, частично устаревшие сведения и LCE-запросы не эквивалентны строгой канонической CDC локальности и физической переписи чанков.

**Идентичность:** `doi:10.4230/LIPIcs.CPM.2026.20` · **Авторы:** Daniel Alexander Albert · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-111
**[The cell probe complexity of dynamic data structures](https://doi.org/10.1145/73007.73040)** (1989)

Fredman–Saks вводят динамические cell-probe нижние границы с учётом операций обновления и запросов и техники chronogram; исходный метод уже связывает количество обращений к ячейкам и динамическую память.

**Ограничение:** Cell-probe считывания/записи слов с параметром размера ячейки отличаются от числа изменённых q-ичных координат в UCT; новую общую границу только из переименования получить нельзя.

**Идентичность:** `doi:10.1145/73007.73040` · **Авторы:** Michael L. Fredman, Michael E. Saks · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-112
**[Logarithmic Lower Bounds in the Cell-Probe Model](https://doi.org/10.1137/S0097539705447256)** (2006)

Pătraşcu–Demaine доказывают амортизированные рандомизированные нижние оценки для динамических структур, включая partial sums и connectivity, а также компромиссы стоимости обновлений и запросов.

**Ограничение:** Не переносить асимптотику, word-size или распределение входов без совпадения модели; UCT-A обязан сравниваться с этими сильными известными границами.

**Идентичность:** `doi:10.1137/S0097539705447256` · **Авторы:** Mihai Pătraşcu, Erik D. Demaine · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-113
**[On the Cell Probe Complexity of Dynamic Membership](https://doi.org/10.1137/1.9781611973075.12)** (2010)

Yi–Zhang исследуют динамическую принадлежность в модели cell-probe со специальным бесплатным кэшем и границами на обновления при почти одношаговых запросах.

**Ограничение:** Бесплатный кэш и последовательности случайных операций требуют отдельного resource ledger; нельзя смешивать с детерминированными worst-case Hamming writes.

**Идентичность:** `doi:10.1137/1.9781611973075.12` · **Авторы:** Ke Yi, Qin Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-114
**[On dynamic bit-probe complexity](https://doi.org/10.1016/j.tcs.2007.02.058)** (2007)

Исследование нижних границ dynamic membership и partial sums в bit-probe модели и продолжение техник chronogram; максимально близко к счёту изменённых битов.

**Ограничение:** Запись в один бит памяти, чтение бита и изменение координаты абстрактного кода являются разными ресурсами, которые требуют явной редукции.

**Идентичность:** `doi:10.1016/j.tcs.2007.02.058` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-115
**[New amortized cell-probe lower bounds for dynamic problems](https://doi.org/10.1016/j.tcs.2019.01.043)** (2019)

Новые амортизированные cell-probe нижние границы для динамического вычисления полиномов и online matrix-vector multiplication; демонстрируется общий метод нижних оценок.

**Ограничение:** Теоремы привязаны к конкретным семействам задач и амортизированной модели; не распространяются автоматически на любую динамическую систему.

**Идентичность:** `doi:10.1016/j.tcs.2019.01.043` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-119
**[An $\Omega((\log n / \log\log n)^2)$ Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/)** (2026)

Young Kun Ko, ECCC TR26-047, редакция 7 октября 2026: основной Theorem 1.1 для Multiphase Problem / inner product над F₂ при m=n^{1+Ω(1)}, t_u=n^{o(1)} утверждает t_tot=Ω((log n/log(t_u w))²); доказательство использует 2.5-round communication game с проверкой симуляции.

**Ограничение:** Точная формулировка теоремы проверена по авторской PDF (стр. 3), но полное доказательство не перепроверено. w — размер cell-probe слова, не LENT write locality; m — число preprocessed vectors, не code dimension. Нельзя переносить теорему на произвольную Boolean функцию, динамический range parity или HYP-103 authenticated certificates.

**Идентичность:** `publisher:eccc:tr26-047` · **Авторы:** Young Kun Ko · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-123
**[Optimal Dynamic Strings](https://doi.org/10.1137/1.9781611975031.99)** (2018)

SODA 2018: поддержка операций make_string, concat, split, сравнения строк и LCP с логарифмическим временем обновления с высокой вероятностью; доказана нижняя граница на сумму динамических затрат в модели сравнения равенства строк.

**Ограничение:** Структура сравнивает/представляет редактируемые строки, но не обязана выдавать тождественно стандартный BLAKE3-256; её Omega(log n) не является BLAKE3 compression-oracle lower bound.

**Идентичность:** `doi:10.1137/1.9781611975031.99` · **Авторы:** Paweł Gawrychowski, Adam Karczmarz, Tomasz Kociumaka, Jakub Łącki, Piotr Sankowski · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-124
**[A textbook solution for dynamic strings](https://doi.org/10.1016/j.tcs.2026.115746)** (2026)

TCS 2026: FeST — упрощённая структура динамических строк на улучшенных splay trees с амортизированными логарифмическими обновлениями, сравнениями подстрок и расширениями операций.

**Ограничение:** Строковые отпечатки используются с вероятностной корректностью; они не являются каноническим BLAKE3 и не решают точную задачу позиционного счётчика чанков.

**Идентичность:** `doi:10.1016/j.tcs.2026.115746` · **Авторы:** Zsuzsanna Lipták, Francesco Masillo, Gonzalo Navarro · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-141
**[Bit-Probe Lower Bounds for Succinct Data Structures](https://doi.org/10.1137/090766619)** (2012)

Viola доказывает дополнительные к информационно-теоретическому минимуму биты памяти для статического компактного представления троичных массивов и множеств при малом числе bit probes, включая адаптивное чтение.

**Ограничение:** Статическая схема доступа и избыточности не даёт автоматически динамическую границу на число переписанных ячеек или на совместную стоимость обновлений, сертификатов и внешнего оракула.

**Идентичность:** `doi:10.1137/090766619` · **Авторы:** Emanuele Viola · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-003-G1-SOURCE-AND-GAP-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-003-G1-SOURCE-AND-GAP-AUDIT.md) (model_overlap)

### LIT-175
**["Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK](https://www.usenix.org/conference/fast26/presentation/zhao)** (2026)

RASK индексирует непрерывные диапазоны блоков в лог-структурированных листьях, реализует range-aware split/merge, исследует RAM/IO tradeoff по производственным трассам.

**Ограничение:** Эффективность зависит от непрерывности операций записи; результаты не доказывают сокращение памяти на произвольных перестановочных updates и не являются cell-probe lower bound.

**Идентичность:** `usenix:fast26:zhao` · **Авторы:** Haoru Zhao, Mingkai Dong, Erci Xu, Zhongyu Wang, Haibo Chen · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [FAST 2026](https://www.usenix.org/conference/fast26/presentation/zhao) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-177
**[Optimal External Memory Interval Management](https://doi.org/10.1137/S009753970240481X)** (2003)

Arge–Vitter дают оптимальное внешнепамятное дерево для точного поиска всех интервалов, покрывающих точку, с динамическими вставками/удалениями.

**Ограничение:** Операция stabbing reports all covering intervals; здесь не задана latest-write-wins overwrite-карта, физический WAL и compaction. Автоматический перенос нижних оценок запрещён.

**Идентичность:** `doi:10.1137/S009753970240481X` · **Авторы:** Lars Arge, Jeffrey Scott Vitter · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-178
**[The Limits of Buffering: A Tight Lower Bound for Dynamic Membership in the External Memory Model](https://doi.org/10.1137/110842211)** (2013)

Verbin–Zhang устанавливают пороговый компромисс: при амортизированной стоимости update ниже единицы внешнепамятный membership требует существенных затрат на query в заданных b,m,n.

**Ограничение:** Модель внешнепамятного membership и число I/O не тождественны физическим байтам переписывания или range assign; единицы и условия должны сохраняться.

**Идентичность:** `doi:10.1137/110842211` · **Авторы:** Elad Verbin, Qin Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-182
**[Structural Designs Meet Optimality: Exploring Optimized LSM-tree Structures in a Colossal Configuration Space](https://doi.org/10.1145/3654978)** (2024)

Moose/Smoose предлагают гибкие LSM-настройки числа runs на уровне, size ratio и Bloom фильтров, оптимизируют point/range lookup и updates; авторы оценивают RocksDB.

**Ограничение:** Экспериментальный и аналитический результат для выбранного семейства LSM-конфигураций; не универсальная конкурентная или cell-probe граница для range-overwrite сервиса.

**Идентичность:** `doi:10.1145/3654978` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-184
**[C2LSM: A configuration paradigm for efficient compaction in LSM-tree-based key-value stores](https://doi.org/10.1016/j.future.2026.108425)** (2026)

C2LSM (FGCS 2026) формализует модель времени compaction и регулирует per-level ёмкости и размеры SSTable при заданных стоимостях диска.

**Ограничение:** Оптимизация исследована в пределах конкретного LSM family; экспериментальные проценты ускорений не универсальны и не доказывают нижних оценок SSD bytes.

**Идентичность:** `doi:10.1016/j.future.2026.108425` · **Авторы:** Jinkang Lu, Peixuan Li, Cheng Zhang, Yukun Huang, Qiang Cao, Ping Xie · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/c04acfe345d941eeaf1f9aa447f65c8eca2bb4cb/docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) (model_overlap)

### LIT-185
**[ArceKV: Towards Workload-driven LSM-compactions for Key-Value Store Under Dynamic Workloads](https://doi.org/10.14778/3796195.3796208)** (2026)

ArceKV в PVLDB 2026 развивает ElasticLSM и адаптивный Arce-контроллер compaction для непостоянных рабочих нагрузок с измерением накладных расходов переключения.

**Ограничение:** Адаптивная политика LSM не является новым универсальным онлайн-конкурентным доказательством для произвольных точных перезаписываемых диапазонов.

**Идентичность:** `doi:10.14778/3796195.3796208` · **Авторы:** Junfeng Liu, Haoxuan Xie, Siqiang Luo · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/c04acfe345d941eeaf1f9aa447f65c8eca2bb4cb/docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) (model_overlap)

### LIT-186
**[RangeReduce: Query-Driven LSM Compactions](https://doi.org/10.1109/ICDE65706.2026.00194)** (2026)

RangeReduce (ICDE 2026) направляет LSM compaction с учётом стоимости сканирования диапазонных запросов и множества пересекающихся SSTable runs.

**Ограничение:** Диапазон чтения через runs и range-as-key записываемые интервалы — разные API; результаты нельзя переносить на overwrite-фрагментацию без редукции.

**Идентичность:** `doi:10.1109/ICDE65706.2026.00194` · **Авторы:** Shubham Kaushik, Manos Athanassoulis, Subhadeep Sarkar · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/c04acfe345d941eeaf1f9aa447f65c8eca2bb4cb/docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) (model_overlap)

### LIT-193
**[Fast Decremental Tree Sums in Forests](https://doi.org/10.4230/LIPIcs.ICALP.2026.26)** (2026)

Алгоритмы динамических агрегированных групповых сумм в лесах при удалении рёбер и запросах компонент/путей с обсуждением универсальной оптимальности относительно модели операций.

**Ограничение:** Деревья/леса и group operation, только decremental режим. Не переносить на произвольные графы, хранилища с crash recovery или безусловные cell-probe нижние границы.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.26` · **Авторы:** Benjamin Aram Berendsohn, Marek Sokołowski · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.26) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-201
**[Lower Bounds on FSS from Dynamic Data Structures](https://doi.org/10.4230/LIPIcs.ITCS.2026.71)** (2026)

ITCS 2026: соответствие black-box PRF/OWF Function Secret Sharing с динамическими range-query структурами. Источник различает cell-probe и write-probe с бесплатными чтениями во время update.

**Ограничение:** FSS privacy не является authenticated soundness. Параметр n обозначает длину аргумента функции, а не число элементов RAM. Lower bound переносится лишь при правильной модели.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2026.71` · **Авторы:** Niv Gilboa, Daniel Weber · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-212
**[Compressing Dynamic Fully Indexable Dictionaries in Word-RAM](https://arxiv.org/abs/2603.23119)** (2026)

Динамический fully indexable dictionary в word-RAM: параметрический компромисс близкого к информационному минимуму объёма, rank/select и worst-case одноэлементного обновления; arXiv отмечает предстоящую публикацию в STOC 2026.

**Ограничение:** Модель word-RAM и отдельные битовые изменения не задают долговечность checkpoint, range overwrite, WAL, физические страницы или байты compaction. Утверждения статьи не воспроизведены независимо.

**Идентичность:** `arxiv:2603.23119` · **Авторы:** Gabriel Marques Domingues · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md](https://github.com/definitely-stable/Mathlab/blob/e161b04e5e3d3e634745be31e89c236e75c773a7/docs/research/INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md) (model_overlap)


## incremental-computation
*Инкрементальные вычисления и сертификаты*

### LIT-010
**[Incremental Computing by Differential Execution](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20)** (2025)

Дифференциальная семантика инкрементальных вычислений с формально проверенными свойствами корректности и оптимизациями циклов.

**Ограничение:** Корректность изменения вычисления не равна минимальной длине сертификата unchanged и lower bound на cell probes.

**Идентичность:** `doi:10.4230/LIPIcs.ECOOP.2025.20` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-013
**[Change actions: from incremental computation to discrete derivatives](https://arxiv.org/abs/2002.05256)** (2020)

Алгебраический аппарат change actions для композиционной семантики дискретных производных и инкрементальных запросов.

**Ограничение:** Общее правило композиции изменений не обеспечивает корректность объединения отдельно выданных сертификатов no-effect.

**Идентичность:** `arxiv:2002.05256` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-032
**[Bounded Incremental Computation](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/)** (1993)

Ramalingam исследует сложность инкрементального перерасчёта относительно размеров изменений ввода и вывода.

**Ограничение:** Сам output-sensitive cost не является новой нижней границей метаданных no-effect сертификата.

**Идентичность:** `publisher:msresearch:ramalingam:1993` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-041
**[Certificates in Data Structures](https://arxiv.org/abs/1404.5743)** (2014)

Wang–Yin исследуют сертификаты ответов static cell-probe запросов и нижние границы на число прочитанных ячеек.

**Ограничение:** Сертификат в недетерминированной static query модели не равен runtime-maintained zero-effect сертификату для dynamic DAG.

**Идентичность:** `arxiv:1404.5743` · **Авторы:** Yaoyu Wang, Yitong Yin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-045
**[Complexity models for incremental computation](https://doi.org/10.1016/0304-3975(94)90159-7)** (1994)

Miltersen–Subramanian–Vitter–Tamassia классифицируют incremental complexity и вводят критерии lower bounds для online re-evaluation.

**Ограничение:** Это model-level фундамент, а не автоматическая теорема об update cost или bytes rewritten в TOM/O01.

**Идентичность:** `doi:10.1016/0304-3975(94)90159-7` · **Авторы:** Peter Bro Miltersen, Sairam Subramanian, Jeffrey Scott Vitter, Roberto Tamassia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-046
**[Lower And Upper Bounds For Incremental Algorithms](https://doi.org/10.7282/T3HT2SXD)** (1992)

Berman: relative incremental lower bound и δ-анализ для динамических update algorithms, включая обновление transitive closure.

**Ограничение:** Работа о сложностях в собственной модели; не устанавливает универсальное zero-effect certificate lower bound TOM.

**Идентичность:** `doi:10.7282/T3HT2SXD` · **Авторы:** A. Michael Berman · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-055
**[DeltaSort: Incremental Sorting of Arrays with Known Updates](https://doi.org/10.4230/LIPIcs.SEA.2026.18)** (2026)

Операция инкрементальной сортировки массива, когда известны k изменённых индексов; автор даёт O(n sqrt(k)) ожидаемого времени и O(k) дополнительной памяти.

**Ограничение:** Оценка дана для модели случайных обновлений; не обеспечивает worst-case O(n sqrt(k)), no-effect certificate или стабильный физический порядок битов.

**Идентичность:** `doi:10.4230/LIPIcs.SEA.2026.18` · **Авторы:** Shubham Dwivedi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-056
**[Incremental Submodular Maximization: Better Than Greedy](https://doi.org/10.4230/LIPIcs.ESA.2026.134)** (2026)

Алгоритм адаптивного масштабирования улучшает конкурентное отношение всех префиксов cardinality constraint до 1.373; установлена нижняя граница 1.25 для детерминированных алгоритмов.

**Ограничение:** Incremental здесь означает возрастающий бюджет оптимизации, а не поддержание произвольных изменяемых DAG и не худший случай побайтовых правок.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.134` · **Авторы:** Marcin Bienkowski, Joakim Blikstad, Jarosław Byrka, Martín Costa, Yann Disser, Annette Lutz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-113](INDEX.md#om-113)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-096
**[Incremental Computation with Names](https://arxiv.org/abs/1503.07792)** (2015)

Nominal Adapton использует именованные вычислительные узлы и доказывает согласованность результатов с полным пересчётом при изменении входов.

**Ограничение:** Известное переиспользование именованных узлов не устанавливает минимальный размер совместного сертификата для произвольных Boolean DAG и батчей.

**Идентичность:** `arxiv:1503.07792` · **Авторы:** Matthew A. Hammer, Jana Dunfield, Kyle Headley, Nicholas Labich, Jeffrey S. Foster, Michael Hicks, David Van Horn · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-102
**[Riker: Always-Correct and Fast Incremental Builds from Simple Specifications](https://www.usenix.org/conference/atc22/presentation/curtsinger)** (2022)

USENIX ATC 2022 автоматически отслеживает файловые зависимости при инкрементальной сборке и поддерживает корректность относительно полного построения.

**Ограничение:** Полная POSIX-модель зависимости не доказывает оптимальную сложность совместных Boolean DAG сертификатов и требует оплаты системных метаданных.

**Идентичность:** `usenix:atc22:curtsinger` · **Авторы:** Charlie Curtsinger, Daniel W. Barowy · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-103
**[Query Maintenance Under Batch Changes with Small-Depth Circuits](https://doi.org/10.4230/LIPIcs.MFCS.2024.46)** (2024)

MFCS 2024: поддержание запросов после пакетов изменений полилогарифмического размера с помощью малоглубинных схем и итеративных first-order обновлений; прямая граница для широкой идеи batch-DAG.

**Ограничение:** DynFO и глубина обновляющих схем не задают минимального количества старых битов, которые обязан прочитать проверяющий сертификат частичного входа.

**Идентичность:** `doi:10.4230/LIPIcs.MFCS.2024.46` · **Авторы:** Samir Datta, Asif Khan, Anish Mukherjee, Felix Tschirbs, Nils Vortmeier, Thomas Zeume · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-104
**[Parallel Batch-Dynamic Trees via Change Propagation](https://doi.org/10.4230/LIPIcs.ESA.2020.2)** (2020)

ESA 2020: эффективная пакетная динамика деревьев через change propagation, вычислительную дистанцию и анализ ожидаемой работы для k обновлений.

**Ограничение:** Сложность пакетного обновления дерева с запросами путей/поддеревьев не равна минимальному свидетельству результата произвольного Boolean DAG при известном старом корне.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2020.2` · **Авторы:** Umut A. Acar, Daniel Anderson, Guy E. Blelloch, Laxman Dhulipala, Sam Westrick · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-109
**[Incremental Cryptography: The Case of Hashing and Signing](https://doi.org/10.1007/3-540-48658-5_22)** (1994)

CRYPTO 1994: вводится криптографическая постановка инкрементального хеширования и подписания, допускающая обновление преобразования после небольших изменений документа.

**Ограничение:** Примитивы 1994 года не обязаны давать тот же результат, что стандартный BLAKE3; новая теорема должна различать безопасность нового хеша и точную совместимость хеша по байтам.

**Идентичность:** `doi:10.1007/3-540-48658-5_22` · **Авторы:** Mihir Bellare, Oded Goldreich, Shafi Goldwasser · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md) (model_overlap)

### LIT-110
**[A New Paradigm for Collision-Free Hashing: Incrementality at Reduced Cost](https://doi.org/10.1007/3-540-69053-0_13)** (1997)

EUROCRYPT 1997: конкретные инкрементальные конструкции устойчивого к коллизиям хеширования MuHASH, AdHASH и LtHASH, с отдельными алгебраическими допущениями.

**Ограничение:** Эти алгоритмы строят другие хеши и не вычисляют стандартный BLAKE3-256 без изменений; из их доказательств нельзя выводить границу времени вставки в BLAKE3.

**Идентичность:** `doi:10.1007/3-540-69053-0_13` · **Авторы:** Mihir Bellare, Daniele Micciancio · **Проверка:** `author_paper_or_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md) (model_overlap)

### LIT-117
**[A Library for Self-Adjusting Computation](https://doi.org/10.1016/j.entcs.2005.11.043)** (2006)

Библиотека самомодифицирующихся вычислений со ссылками и memoization, примеры change propagation и ускорение инкрементального пересчёта.

**Ограничение:** Из инженерных speedups и программных инвариантов не вытекает универсальная минимальная стоимость обновлений или общий сертификат без полной модели доступа.

**Идентичность:** `doi:10.1016/j.entcs.2005.11.043` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-125
**[The BLAKE3 Hashing Framework (C2SP v1.0.0)](https://c2sp.org/BLAKE3@v1.0.0)** (2024)

Нормативная криптографическая спецификация C2SP: BLAKE3 разбивает вход на 1024-байтовые чанки; каждый блок листа получает счётчик, равный индексу чанка, а родительские узлы используют нулевой счётчик и отдельные флаги.

**Ограничение:** Это техническая спецификация, НЕ новая рецензируемая научная статья и НЕ нижняя граница сложности инкрементального хеширования; особый ROOT-флаг требует отдельной модели переиспользования.

**Идентичность:** `publisher:c2sp:blake3-v1-0-0` · **Авторы:** Jean-Philippe Aumasson, Samuel Neves, Jack O'Connor, Zooko Wilcox-O'Hearn · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-129
**[Annotations in Data Streams](https://doi.org/10.1145/2636924)** (2014)

Chakrabarti–Cormode–McGregor–Thaler вводят схемы аннотированных потоков: недоверенный доказатель сообщает вспомогательную информацию, а ограниченный по памяти верификатор обязан проверить ответ.

**Ограничение:** Длина честной аннотации — необходимый информационный ресурс, но сама по себе она не обеспечивает soundness. Известные нелинейные компромиссы annotation/verification-space не следуют из простого произведения размеров кодов.

**Идентичность:** `doi:10.1145/2636924` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-130
**[Annotations for Sparse Data Streams](https://arxiv.org/abs/1304.3816)** (2013)

Chakrabarti–Cormode–Goyal–Thaler исследуют online Merlin–Arthur/annotated streaming с малым числом действительных обновлений и показывают границы между вариантами моделей доказателя.

**Ограничение:** Сохранённое состояние, момент публикации свидетельства, адаптивность и сообщение недоверенного доказателя должны иметь отдельные контракты и оценки.

**Идентичность:** `arxiv:1304.3816` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-169
**[Principles and Methodologies for Serial Performance Optimization](https://www.usenix.org/conference/osdi25/presentation/park-sujin)** (2025)

Методика remove/replace/reorder и восемь вариантов оптимизации последовательной работы: batching, caching, precomputation, deferring, relaxation, contextualization, hardware specialization, layering.

**Ограничение:** Таксономия производительности и системные кейсы не образуют универсальную нижнюю границу по CPU, памяти или стоимости изменения состояния.

**Идентичность:** `usenix:osdi25:park-sujin` · **Авторы:** Sujin Park, Mingyu Guan, Xiang Cheng, Taesoo Kim · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/park-sujin) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-173
**[Incr: Faster Re-Execution via Bolt-On Incrementalization](https://www.usenix.org/conference/osdi26/presentation/xie-yizheng)** (2026)

Incr автоматически выявляет зависимости и эффекты и сохраняет промежуточные результаты для повторного исполнения shell-программ, включая неидемпотентные операции.

**Ограничение:** Экспериментальные ускорения не являются нижней границей вычислений; накладные расходы на отслеживание зависимостей, side effects и обновление кэша нельзя считать нулевыми.

**Идентичность:** `usenix:osdi26:xie-yizheng` · **Авторы:** Yizheng Xie, Evangelos Lamprou, Jerry Xia, Nikos Vasilakis · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/xie-yizheng) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-187
**[Incremental Reachability Index](https://doi.org/10.4230/LIPIcs.SEA.2025.9)** (2025)

Индекс достижимости для append-only ориентированного ациклического графа; сохраняет неизменность ранее опубликованных index-меток; предусмотрены O(1) и O(log n) запросы в зависимости от памяти.

**Ограничение:** Добавление только новых DAG узлов в топологическом порядке; не распространять на общие удаления ребер, нелинейные обновления, аутентификацию или изменяемый глобальный transitive closure.

**Идентичность:** `doi:10.4230/LIPIcs.SEA.2025.9` · **Авторы:** Laurent Bulteau, Pierre-Yves David, Florian Horn, Euxane Tran-Girard · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [SEA 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2025.9) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)


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

### LIT-087
**[Once Rolling Hashing is Enough: Exploiting Rolling Hash Reuse in Delta Compression](https://doi.org/10.1145/3767295.3803596)** (2026)

FastDelta переиспользует rolling hashes одновременно при CDC, поиске похожих фрагментов и delta encoding, экономя повторные вычисления.

**Ограничение:** Shared hash pipeline не доказывает оптимальное направление reference selection и не равен выигрышу от нового similarity sketch; требуется измерять весь patch pipeline.

**Идентичность:** `doi:10.1145/3767295.3803596` · **Авторы:** Haoliang Tan, Wenhao Ou, Xiangyu Zou, Cai Deng, Yanqi Pan, Hao Huang, Zhaoquan Gu, Wen Xia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [EuroSys 2026](https://2026.eurosys.org/papers.html) · **Доступ:** `conference_paper_list_and_delsk_fulltext_review`

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [DL-002](INDEX.md#dl-002), [DL-006](INDEX.md#dl-006)

**Происхождение цитаты / пересечения →** [DELSK:.work/research/claim-matrix.md](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/claim-matrix.md) (model_overlap)

### LIT-116
**[Noiseless coding of correlated information sources](https://doi.org/10.1109/TIT.1973.1055037)** (1973)

Slepian–Wolf — классическая теоретико-информационная модель безошибочного кодирования коррелированных случайных источников с распределённым описанием.

**Ограничение:** Стохастические асимптотические скорости кодирования и побочная информация не равны худшему случаю source-only COPY/ADD и оплате индексации; не объявлять lower bound для патчинга следствием SW.

**Идентичность:** `doi:10.1109/TIT.1973.1055037` · **Авторы:** David Slepian, Jack Wolf · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DL-001](INDEX.md#dl-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)


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

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)

### LIT-029
**[Space lower bounds for linear prediction in the streaming model](https://arxiv.org/abs/1902.03498)** (2019)

Dagan–Kur–Shamir: квадратичная по размерности потребность в памяти для конкретных линейных streaming inference задач.

**Ограничение:** Это не универсальное cell-probe ограничение для сертификатов неизменности DAG.

**Идентичность:** `arxiv:1902.03498` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)

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

### LIT-100
**[How Robust are Linear Sketches to Adaptive Inputs?](https://arxiv.org/abs/1211.1056)** (2012)

Hardt и Woodruff показывают уязвимость классических линейных sketch-оценок к адаптивно выбранным запросам, что критично для корректности повторных оценок.

**Ограничение:** Результат об определённых линейных sketches и нормах не является автоматическим impossibility theorem для секретно-ключевых нелинейных односторонних оценок.

**Идентичность:** `arxiv:1211.1056` · **Авторы:** Moritz Hardt, David P. Woodruff · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-003](INDEX.md#dm-003), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-101
**[Breaking the Quadratic Barrier: Robust Cardinality Sketches for Adaptive Queries](https://proceedings.mlr.press/v267/cohen25c.html)** (2025)

ICML 2025 даёт устойчивые оценки cardinality при адаптивных запросах в модели ограниченного повторного участия каждого элемента.

**Ограничение:** Гарантии bounded participation не переносятся автоматически на DeltaMeter one-sided parity estimator, keyed-PRF transcript и произвольные изменяемые множества.

**Идентичность:** `publisher:pmlr:cohen25c` · **Авторы:** Edith Cohen, Mihir Singhal, Uri Stemmer · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-003](INDEX.md#dm-003), [DM-007](INDEX.md#dm-007), [DM-004](INDEX.md#dm-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-132
**[Arthur–Merlin streaming complexity](https://doi.org/10.1016/j.ic.2014.12.011)** (2015)

Исследование моделей Arthur–Merlin для потоковой проверки, включая компромиссы длины доказательства и оперативной памяти и ограничения для Distinct Elements.

**Ограничение:** Статистическая полнота/корректность интерактивного доказательства отличается от финитной гарантии точной оценки множества; нельзя подменять одно другим.

**Идентичность:** `doi:10.1016/j.ic.2014.12.011` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-001](INDEX.md#dm-001), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)


## compressed-indexing
*Сжатые структуры, индексация строк и нижние границы*

### LIT-050
**[Dynamic Grammar-Compressed Self-Index in δ-Optimal Space](https://doi.org/10.4230/LIPIcs.ESA.2026.6)** (2026)

Динамический RR-index хранит повторяющиеся строки в сжатом виде, поддерживая вставки, удаления и поиск без полной распаковки; оценка объёма через δ-complexity.

**Ограничение:** Ожидаемые и амортизированные гарантии относятся к строковому индексу и locate-запросам; не означают постоянную стоимость переписывания байтов или CDC-локальность.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.6` · **Авторы:** Takaaki Nishimoto, Yasuo Tabei · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-051
**[Hardness of Frequency-Related Queries on Compressed Strings](https://doi.org/10.4230/LIPIcs.ESA.2026.143)** (2026)

Исследуются условные ограничения вычисления rank/frequency-подобных запросов по grammar/LZ-компрессированным строкам без развёртывания.

**Ограничение:** Модель сжатого индекса и условные lower bounds не являются нижними границами для exact ASET или произвольной инкрементальной метрики.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.143` · **Авторы:** Rajat De, Dominik Kempa · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-119](INDEX.md#om-119)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-052
**[OptFSST: Optimized FSST String Compression](https://arxiv.org/abs/2607.11271)** (2026)

Оптимальное динамическое программирование кодирования при фиксированной таблице символов FSST и NP-трудность обобщённого выбора таблицы; сохраняется независимая распаковка строк.

**Ограничение:** Оптимальность доказана при фиксированном словаре, а не для совместного поиска словаря; сравнение на 92 наборах — авторский эксперимент, не бенчмарк ChunkShift.

**Идентичность:** `arxiv:2607.11271` · **Авторы:** Hedi Chehaidar, Mihail Stoian, Moritz Stargalla, Andreas Kipf · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DM-014](INDEX.md#dm-014), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-053
**[Relative Compressed Reverse Suffix Array](https://doi.org/10.4230/LIPIcs.STACS.2026.62)** (2026)

Короткое относительное кодирование суффиксного массива обращённого текста, если уже имеется FM-index исходного текста; изучается стоимость доступа.

**Ограничение:** Это относительное индексирование структур и суффиксных массивов, не универсальный delta patch codec и не гарантия байтовой экономии.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.62` · **Авторы:** Muhammed Oguzhan Kulekci, Mano Prakash Parthasarathi, Rahul Shah, Sharma V. Thankachan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-054
**[Efficient Compression in Semigroups](https://doi.org/10.4230/LIPIcs.STACS.2026.80)** (2026)

Классификация классов конечных полугрупп, допускающих эффективное представление straight-line programs, и улучшения границ длины/ширины программ.

**Ограничение:** Семигрупповая algebraic compression и запросы Cayley table не эквивалентны сжатию файлов, кодекам дельт или инкрементальным сертификатам.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.80` · **Авторы:** Alexander Thumm, Armin Weiß · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-119](INDEX.md#om-119)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-126
**[Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts](https://doi.org/10.1007/s00224-026-10266-x)** (2026)

Theory of Computing Systems 2026: алгоритм IPM-запросов на грамматически сжатых и динамических строках за O(log n), применимый к fully persistent динамическим структурам; опубликован proof-of-concept Rust.

**Ограничение:** IPM-запросы и структурные представления подстрок не тождественны вычислению стандартного BLAKE3 digest после каждого редактирования, и нижние границы IPM не переносятся автоматически.

**Идентичность:** `doi:10.1007/s00224-026-10266-x` · **Авторы:** Anouk Duyster, Tomasz Kociumaka · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-179
**[Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries](https://doi.org/10.1109/FOCS57990.2023.00112)** (2023)

Li–Liang–Yu–Zhou доказывают нижние оценки cell-probe для динамического succinct-словаря по избыточным битам на ключ и времени операций при заданном размере слова.

**Ограничение:** Это модель членства/значений ключей и ячеечных обращений; не доказательство lower bound физических байтов для overwritten interval index.

**Идентичность:** `doi:10.1109/FOCS57990.2023.00112` · **Также:** arxiv:2306.02253 · **Авторы:** Tianxiao Li, Jingxun Liang, Huacheng Yu, Renfei Zhou · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-180
**[Practical Adaptive Dynamic Bitvectors](https://doi.org/10.1002/spe.3433)** (2025)

Navarro изучает практические адаптивные bitvectors с (1+epsilon)n бит и амортизированной O(log(n/q)) стоимостью при q запросах на обновление.

**Ограничение:** Речь о rank/select и одиночных bitvector-операциях; ratio q и стоимость в статье не означают гарантированную оптимальность LSM compaction/range writes.

**Идентичность:** `doi:10.1002/spe.3433` · **Авторы:** Gonzalo Navarro · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-181
**[Dynamic Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space](https://arxiv.org/abs/2608.06066)** (2026)

Blelloch и соавторы дают близкое к энтропийному пространство для динамических массивов фиксированного алфавита с O(1) операциями в конкретной word-RAM модели и доказывают специальную нижнюю границу.

**Ограничение:** Авторский препринт 2026; ограничены алфавит, entropy regime и модель вычисления; не установлена цена durable pages, WAL или физической compaction.

**Идентичность:** `arxiv:2608.06066` · **Авторы:** Guy E. Blelloch, Yang Hu, William Kuszmaul, Tianxiao Li, Renfei Zhou · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md](https://github.com/definitely-stable/Mathlab/blob/a5a9b347940579650cdb8c8164f59911cb2602cb/docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (model_overlap)

### LIT-183
**[(Worst-case) Optimal Adaptive Dynamic Bitvectors](https://doi.org/10.1007/s00224-025-10229-8)** (2025)

Navarro доказал специальную worst-case оптимальность адаптивной динамической битовой строки при разреженных обновлениях: n+o(n) бит и амортизированная сложность O(log(n/q)/log log n) при q запросах на изменение.

**Ограничение:** Ячеечная lower bound касается rank/select/точечных update и фиксированного отношения q; не является оценкой физического compaction для диапазонного overwrite.

**Идентичность:** `doi:10.1007/s00224-025-10229-8` · **Также:** arxiv:2405.15088, doi:10.1007/978-3-031-72200-4_16 · **Авторы:** Gonzalo Navarro · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/c04acfe345d941eeaf1f9aa447f65c8eca2bb4cb/docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) (model_overlap)

### LIT-197
**[Incongruity-Sensitive Access to Highly Compressed Strings](https://doi.org/10.4230/LIPIcs.ESA.2026.125)** (2026)

Сжатые RLSLP и block-tree индексы с доступом к символам, время которого зависит от максимальной повторяющейся подстроки вокруг позиции при O(g_rl) или O(L) метаданных.

**Ограничение:** Представление статической сжатой строки и локальная повторяемость — не общий динамический индекс, не обоснование сокращения CPU/GC в LSM, не произвольная compressed-memory bound.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.125` · **Авторы:** Ferdinando Cicalese, Travis Gagie, Zsuzsanna Lipták, Gonzalo Navarro, Nicola Prezza, Cristian Urbina · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ESA 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.125) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-213
**[Dynamic Grammar-Compressed Self-Index in δ-Optimal Space](https://arxiv.org/abs/2604.24080)** (2026)

Динамический грамматически сжатый self-index RR-index, стремящийся к δ-оптимальному объёму, поддерживает locate, вставки и удаления в модели сжатых текстов (arXiv v3 от июля 2026).

**Ограничение:** Подстрочные insert/delete и locate с ожидаемыми/амортизированными оценками не означают оптимальный WAL или физический recourse для latest-write-wins диапазонных присваиваний; доказательства и бенчмарки не воспроизведены.

**Идентичность:** `arxiv:2604.24080` · **Авторы:** Takaaki Nishimoto, Yasuo Tabei · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md](https://github.com/definitely-stable/Mathlab/blob/e161b04e5e3d3e634745be31e89c236e75c773a7/docs/research/INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md) (model_overlap)


## online-optimization
*Онлайн-оптимизация, конкурентные оценки и барьеры*

### LIT-057
**[Online and Incremental Fractional Vertex Cover on Trees](https://doi.org/10.4230/LIPIcs.ESA.2026.158)** (2026)

На деревьях получены competitive bounds 11/6 в online edge-arrival и 3/2 (с matching lower bound) для инкрементальной модели с известными обновлениями.

**Ограничение:** Вторая модель допускает знание всех будущих обновлений заранее; не переносить offline bound на online или на невозрастающие/удаляемые данные.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.158` · **Авторы:** Júlia Baligács, Bartłomiej Bosek, Yann Disser, Andreas Emil Feldmann, Grzegorz Gutowski, Katarzyna Kępińska, Paweł Putra, Anna Zych-Pawlewicz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-069
**[Lower Bounds for Ranking-Based Pivot Rules](https://doi.org/10.4230/LIPIcs.STACS.2026.31)** (2026)

Единый rank-information framework даёт superpolynomial lower bounds для классов strategy-improvement rules и subexponential bounds для policy iteration.

**Ограничение:** Ограничения доказаны для заданных ranking-based pivot rules и MDP/games; не доказывают невозможность всех динамических алгоритмов или произвольного Rust примитива.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.31` · **Авторы:** Yann Disser, Georg Loho, Matthew Maat, Nils Mosis · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-137](INDEX.md#om-137)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-097
**[Bigtable Merge Compaction](https://arxiv.org/abs/1407.3008)** (2014)

Формализует онлайновое объединение файлов Bigtable и конкурентную оценку политик компактации; предшествует гипотезе HYP-104 о pack rewrite.

**Ограничение:** Непосредственная модель не включает совместное хранение объектов и матрицу принадлежности одновременно закреплённых snapshots; год соответствует первой версии arXiv.

**Идентичность:** `arxiv:1407.3008` · **Авторы:** Claire Mathieu, Carl Staelin, Neal E. Young, Arman Yousefi · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-098
**[Competitive Data-Structure Dynamization](https://arxiv.org/abs/2011.02615)** (2020)

Онлайн-задачи обновления наборов данных с оплачиваемыми build/query затратами и конкурентными гарантиями при неравномерных потоках.

**Ограничение:** Онлайновые set-cover/merge модели нельзя напрямую приравнивать к immutable packs с shared snapshot pins и crash/GC semantics.

**Идентичность:** `arxiv:2011.02615` · **Авторы:** Claire Mathieu, Rajmohan Rajaraman, Neal E. Young, Arman Yousefi · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-160
**[New and Improved Bounds for Markov Paging](https://doi.org/10.4230/LIPIcs.ICALP.2025.123)** (2025)

Уточнена конкурентная оценка dominating-distribution для Markov paging: 2 относительно онлайн-оптимума заданной цепи, со специальной нижней оценкой 1.5907 для этого алгоритма.

**Ограничение:** Запросы исходят из марковской цепи. Перенос на адаптивного противника, объекты переменной длины и реальную задержку кэша без редукции недопустим.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2025.123` · **Авторы:** Chirag Pabbaraju, Ali Vakilian · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.123) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-161
**[Tight Results for Online Convex Paging](https://doi.org/10.1145/3717823.3718217)** (2025)

Точные по порядку конкурентные границы для convex paging с нелинейной стоимостью вытеснений, включая ограничения качества выпуклых релаксаций.

**Ограничение:** Норма вектора вытеснений и comparator определены в исходной модели; это не обычное количество cache misses и не готовый алгоритм ускорения.

**Идентичность:** `doi:10.1145/3717823.3718217` · **Авторы:** Anupam Gupta, Amit Kumar, Debmalya Panigrahi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2025](https://acm-stoc.org/stoc2025/toc.html) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-162
**[The Cost of Consistency: Submodular Maximization with Constant Recourse](https://doi.org/10.1145/3717823.3718131)** (2025)

Для monotone submodular online максимизации с константным recourse на шаг получены tight границы 2/3 в общем случае и 3/4 для coverage; отдельно обсуждается 0.51 randomized polytime.

**Ограничение:** Recourse меняет элементы комбинаторного решения, а не физические ячейки, байты кэша или проверяемые доказательства; функции и приближения различны.

**Идентичность:** `doi:10.1145/3717823.3718131` · **Авторы:** Paul Dütting, Federico Fusco, Silvio Lattanzi, Ashkan Norouzi-Fard, Ola Svensson, Morteza Zadimoghaddam · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2025](https://acm-stoc.org/stoc2025/toc.html) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-188
**[Incremental Maximization for a Broad Class of Objectives](https://doi.org/10.4230/LIPIcs.ESA.2025.92)** (2025)

Для монотонных beta-accountable целей построен scaling-алгоритм, конкурентный на каждом префиксе размера решения; охватывает монотонные субаддитивные функции.

**Ограничение:** Рассматривается рост решения за счет добавления элементов, а не произвольный инкрементальный перерасчёт с удалениями; beta-accountability является существенным условием.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2025.92` · **Авторы:** Yann Disser, David Weckbecker · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ESA 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.92) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-191
**[Online Disjoint Set Covers: Randomization Is Not Necessary](https://doi.org/10.4230/LIPIcs.STACS.2025.18)** (2025)

Детерминированный O(log² n)-конкурентный онлайн алгоритм раскраски поступающих гиперрёбер в непересекающиеся покрытия; derandomization via potential function.

**Ограничение:** Задача максимизации количества полных цветовых покрытий не равна стандартному offline set cover и не является кэш-замещением или ASET ограниченных сумм.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2025.18` · **Авторы:** Marcin Bienkowski, Jarosław Byrka, Łukasz Jeż · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STACS 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2025.18) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-209
**[Prior-Independent and Subgame Optimal Online Algorithms](https://doi.org/10.4230/LIPIcs.ITCS.2026.75)** (2026)

ITCS 2026: prior-independent и subgame-optimal критерии для онлайн-алгоритмов; конечногоризонтный ski-rental служит эталоном для проектирования стратегий с неизвестным будущим и сильным противником.

**Ограничение:** Выводы относятся к иным критериям и игровым моделям; нельзя переносить конкурентные отношения на WAL/checkpoint без совпадения времени раскрытия r_t и ресурсного J.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2026.75` · **Авторы:** Jason Hartline, Aleck Johnsen, Anant Shah · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md](https://github.com/definitely-stable/Mathlab/blob/7e62436374adc9e8cc15c98b68bf9d4a3a06644e/docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md) (model_overlap)

### LIT-210
**[Robust and Consistent Ski Rental with Distributional Advice](https://arxiv.org/abs/2603.29233)** (2026)

ICML 2026, PMLR 306: алгоритмы детерминированного и рандомизированного ski-rental c distributional advice, робастностью при ошибках прогноза и оптимизацией порогов покупки.

**Ограничение:** Алгоритмы требуют явной модели вероятностных предсказаний, отсутствующей в G2-B3-B; PMLR 2026 и arXiv относятся к одной работе и учтены одной идентичностью.

**Идентичность:** `arxiv:2603.29233` · **Также:** publisher:pmlr:v306:kim26l · **Авторы:** Jihwan Kim, Chenglin Fan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md](https://github.com/definitely-stable/Mathlab/blob/7e62436374adc9e8cc15c98b68bf9d4a3a06644e/docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md) (model_overlap)

### LIT-211
**[A new performance metric for the ski rental problem](https://doi.org/10.1016/j.orl.2025.107382)** (2026)

Operations Research Letters 2026 (DOI 2025): комбинированная стохастическая мера ski-rental EoR/RoE с улучшенной оценкой в иной целевой функции.

**Ограничение:** Оценки смешанной статистической метрики не являются худшим детерминированным ratio ALG/OPT для нашего checkpoint; DOI содержит 2025, но publication year — 2026.

**Идентичность:** `doi:10.1016/j.orl.2025.107382` · **Авторы:** Jonathan Chen, Jiawei Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md](https://github.com/definitely-stable/Mathlab/blob/7e62436374adc9e8cc15c98b68bf9d4a3a06644e/docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md) (model_overlap)


## caching
*Кэширование, online paging, консистентность и память*

### LIT-167
**[3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches](https://www.usenix.org/conference/fast25/presentation/zhou-wenbin)** (2025)

Объектно-ориентированное обучение политики вытеснения, учёт byte/object miss ratio и снижение CPU накладных расходов при обучении; авторские эксперименты на 4855 traces.

**Ограничение:** Это измеренные результаты для конкретных workloads и baselines, а не конкурентная нижняя граница или универсальная гарантия hit rate.

**Идентичность:** `usenix:fast25:zhou-wenbin` · **Авторы:** Wenbin Zhou, Zhixiong Niu, Yongqiang Xiong, Juan Fang, Qian Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [FAST 2025](https://www.usenix.org/conference/fast25/presentation/zhou-wenbin) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-168
**[Skybridge: Bounded Staleness for Distributed Caches](https://www.usenix.org/conference/osdi25/presentation/lyerly)** (2025)

Отдельный поток репликации обновляет сведения о свежести распределённых кэшей с измеренными распределениями lag и малым объёмом дополнительной инфраструктуры.

**Ограничение:** Эмпирическая доля записей, удовлетворяющих 2-секундной свежести, не является строгой детерминированной верхней границей и не равна linearizability.

**Идентичность:** `usenix:osdi25:lyerly` · **Авторы:** Robert Lyerly, Scott Pruett, Kevin Doherty, Greg Rogers, Nathan Bronson, John Hugg · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/lyerly) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-170
**[Merlin: An Efficient Adaptive Cache Eviction Algorithm via Fine-Grained Characterization](https://www.usenix.org/conference/osdi26/presentation/li-liujia)** (2026)

MERLIN адаптирует вытеснение на уровне отдельных объектов и характеристик обращений, отделяя компоненты политики, с авторской трассовой оценкой.

**Ограничение:** Авторские throughput/hit-rate результаты не дают гарантии для адаптивного противника или всякого будущего распределения обращений.

**Идентичность:** `usenix:osdi26:li-liujia` · **Авторы:** Liujia Li, Jinhao Guo, Yi Fan, Jianyu Wu, Zhenlin Wang, Jie Zhang, Yuval Tamir, Xiaolin Wang, Yingwei Luo, Diyu Zhou · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/li-liujia) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-171
**[Learning-Augmented Heuristics: Simple Yet Smart, Robust and Interpretable Cache Eviction](https://www.usenix.org/conference/osdi26/presentation/xia)** (2026)

LAH/S4-FIFO обучает параметры эвристики по агрегированным сигналам вне горячего пути, чтобы уменьшить стоимость принятия решения в cache dataplane.

**Ограничение:** Результаты на production traces с предобученной моделью и наблюдаемая устойчивость не являются формальным worst-case competitive ratio.

**Идентичность:** `usenix:osdi26:xia` · **Авторы:** Haocheng Xia, William Nixon, Bintang Dwi Marthen, Pranav Bhandari, Juncheng Yang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/xia) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-172
**[WriteGuards: Distributed Storage Support for Strongly Consistent Caches](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-writeguards)** (2026)

WriteGuards вводит fencing для записи на уровне диапазонов ключей, исключая delayed writes в заданной архитектуре владения и обеспечивая авторскую реализацию линерализуемых cache reads.

**Ограничение:** Требуются конкретные предпосылки о хранилище, fencing и владельцах; это не бесплатное доказательство аутентичности, rollback безопасности или криптографический commitment.

**Идентичность:** `usenix:osdi26:mao-ziming-writeguards` · **Авторы:** Ziming Mao, Atul Adya, Jonathan Ellithorpe, Rishabh Iyer, Matei Zaharia, Scott Shenker, Ion Stoica · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-writeguards) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-174
**[FORGE: Mitigating Synchronization Amplification for Memory-Disaggregated Caching Systems](https://www.usenix.org/conference/osdi26/presentation/yang-zhijun)** (2026)

Кэш с disaggregated memory сокращает synchronization amplification за счёт группировки объектов, ленивого обновления hotness-метаданных и FIFO обработки групп.

**Ограничение:** Зависит от RDMA NIC, модели распределённой памяти и тестовых нагрузок; не следует универсальной оптимальности online paging.

**Идентичность:** `usenix:osdi26:yang-zhijun` · **Авторы:** Zhijun Yang, Yu Hua, Ming Zhang, Menglei Chen, Yixiao Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/yang-zhijun) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-176
**[Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage](https://www.usenix.org/conference/fast26/presentation/ren)** (2026)

HATS координирует foreground чтения и background compaction с adaptive rate control/replica selection в распределённом LSM-хранилище.

**Ограничение:** Системные результаты Cassandra/LSM касаются конкретной нагрузки и планировщика, не доказательства универсального оптимума по recourse или времени.

**Идентичность:** `usenix:fast26:ren` · **Авторы:** Yuanming Ren, Siyuan Sheng, Zhang Cao, Yongkun Li, Patrick P. C. Lee · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [FAST 2026](https://www.usenix.org/conference/fast26/presentation/ren) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)


## graph-algorithms
*Динамические графы, гиперграфы и sparsification*

### LIT-059
**[Fully Dynamic Spectral Sparsification for Directed Hypergraphs](https://doi.org/10.4230/LIPIcs.STACS.2026.38)** (2026)

Поддержание спектрального sparsifier ориентированного гиперграфа под вставкой/удалением ребра и batch-dynamic работе с контролируемой амортизированной сложностью.

**Ограничение:** Спектральная ε-аппроксимация квадратичных форм не означает точного восстановления аддитивных множеств или ASET-коллизий.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.38` · **Авторы:** Sebastian Forster, Gramoz Goranci, Ali Momeni · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-076
**[Incremental Shortest Paths in Almost Linear Time via a Modified Interior Point Method](https://doi.org/10.1145/3798129.3800733)** (2026)

Детерминированно поддерживаются приближённые односточечные кратчайшие пути при вставке рёбер, суммарно близко к линейному времени.

**Ограничение:** Алгоритм работает с ориентированными взвешенными графами и аппроксимацией расстояния; не сертификат отсутствия эффекта произвольной правки DAG.

**Идентичность:** `doi:10.1145/3798129.3800733` · **Авторы:** Yang P. Liu · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-078
**[Separator Theorem for Minor-Free Graphs in Linear Time](https://doi.org/10.1145/3798129.3800727)** (2026)

Найден линейно-временной алгоритм сбалансированного O(√n)-сепаратора в графах без фиксированного минора.

**Ограничение:** Алгоритм статический и зависит от фиксированного запрещённого минора; нельзя приписывать ему поддержку динамической графовой разметки за O(1).

**Идентичность:** `doi:10.1145/3798129.3800727` · **Авторы:** Édouard Bonnet, Tuukka Korhonen, Hung Le, Jason Li, Tomáš Masařík · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-079
**[A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://doi.org/10.1145/3798129.3800868)** (2026)

Chuzhoy–Khanna–Song: детерминированное поддержание максимального matching в полностью динамическом графе с амортизированным временем n^(1/2+o(1)).

**Ограничение:** Maximal не означает maximum; амортизированная bound не худшая на операцию и не переносится на graph refinement без модели.

**Идентичность:** `doi:10.1145/3798129.3800868` · **Авторы:** Julia Chuzhoy, Sanjeev Khanna, Junkai Song · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-131](INDEX.md#om-131), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-085
**[Dynamic Set Cover with Worst-Case Recourse](https://doi.org/10.4230/LIPIcs.ICALP.2026.153)** (2026)

Solomon–Uzrad изучают динамическое покрытие множеств и контролируют число замен в решении на каждом обновлении.

**Ограничение:** Recourse решений не эквивалентен количеству переписанных байт памяти; конечные worst-case bounds применимы к собственной динамической set-cover модели.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.153` · **Авторы:** Shay Solomon, Amitai Uzrad · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.153) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-086
**[Static to Dynamic Correlation Clustering](https://doi.org/10.4230/LIPIcs.ICALP.2026.48)** (2026)

Преобразование статической аппроксимации корреляционного кластеринга в полностью динамическую с O(1) worst-case update в заявленной модели.

**Ограничение:** Гарантия качества сохраняется с указанной вероятностью; это не точное поддержание всех кластеров и не универсальная динамическая оптимизация.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.48` · **Авторы:** Nairen Cao, Vincent Cohen-Addad, Euiwoong Lee, Shi Li, David Rasmussen Lolck, Alantha Newman, Mikkel Thorup, Lukas Vogl, Shuyi Yan, Hanwen Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.48) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-094
**[Deterministic Padded Decompositions and Negative-Weight Shortest Paths](https://doi.org/10.1145/3798129.3800722)** (2026)

Jason Li строит детерминированные padded decompositions ориентированных графов и почти линейный negative-weight SSSP.

**Ограничение:** Статический SSSP с отрицательными рёбрами не даёт incremental support или гарантий размера delta patch.

**Идентичность:** `doi:10.1145/3798129.3800722` · **Авторы:** Jason Li · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-120
**[On cubical graphs](https://doi.org/10.1016/0095-8956(75)90067-2)** (1975)

Garey–Graham исследуют графы, представимые подграфами двоичного гиперкуба, и критически невкладываемые графы — классический prior art для UCT-A.

**Ограничение:** Обычное реберное вложение не является новой теорией локальности; требуются дополнительные строго оплачиваемые ресурсы и корректная структура наблюдений.

**Идентичность:** `doi:10.1016/0095-8956(75)90067-2` · **Авторы:** M. R. Garey, R. L. Graham · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-121
**[The complexity of cubical graphs](https://doi.org/10.1016/S0019-9958(85)80012-7)** (1985)

Работа устанавливает NP-полноту распознавания графов, вкладываемых в некоторый двоичный гиперкуб, и изучает минимальную размерность для специальных классов.

**Ограничение:** Новая универсальная теорема о простой решаемости гиперкубного вложения противоречила бы установленной сложности без усиленных ограничений модели.

**Идентичность:** `doi:10.1016/S0019-9958(85)80012-7` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-122
**[Embeddings in hypercubes](https://doi.org/10.1016/0895-7177(88)90486-4)** (1988)

Livingston–Stout систематизируют результаты о вложениях графов в гиперкубы, дилатации, расширении, деревьях, решётках и сложности embedding.

**Ограничение:** Нельзя заявлять впервые найденные locality/dilation tradeoffs без полного сравнения с классической теорией cubical graphs; isometric partial cubes — более сильная отдельная модель.

**Идентичность:** `doi:10.1016/0895-7177(88)90486-4` · **Авторы:** Marilynn Livingston, Quentin F. Stout · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-148
**[The Size of Bipartite Graphs with a Given Girth](https://doi.org/10.1006/jctb.2002.2123)** (2002)

Hoory (Journal of Combinatorial Theory B, 2002) обобщает экстремальные оценки числа рёбер двудольных графов заданного обхвата с разными размерами долей. При girth≥8 следствие O(V^(4/3)) обосновывает улучшенную границу ASET с четырёхразреженными столбцами и активностью d=3.

**Ограничение:** Статья доказывает графовую границу, но не автоматически новое ASET-утверждение: необходима отдельная корректная редукция от взвешенных векторов к 2+2 фактор-графу и анализ коллизий на C4/C6; нижняя конструкция и декодирование ASET этим источником не решены.

**Идентичность:** `doi:10.1006/jctb.2002.2123` · **Авторы:** Shlomo Hoory · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-163
**[A Simple Dynamic Spanner via APSP](https://doi.org/10.4230/LIPIcs.ICALP.2025.111)** (2025)

Динамический spanner с контролем приближения расстояний, операций обновления и total recourse при заданных последовательностях вставок и удалений.

**Ограничение:** Spanner приближает расстояния; он не сохраняет точно достижимость, не гарантирует отсутствие signed trades и не обеспечивает криптографическую верификацию.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2025.111` · **Авторы:** Rasmus Kyng, Simon Meierhans, Gernot Zöcklein · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.111) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-164
**[Fully Dynamic Algorithms for Transitive Reduction](https://doi.org/10.4230/LIPIcs.ICALP.2025.92)** (2025)

Поддержка минимального сохраняющего reachability подграфа ориентированного графа при вставках и удалениях; один алгоритм O(m+n log n) амортизированно на обновление.

**Ограничение:** Время обновления зависит от m,n и модели операций; reachability-preserving reduction не является доказательством нижней границы для DAG или доверенного сервера.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2025.92` · **Авторы:** Gramoz Goranci, Adam Karczmarz, Ali Momeni, Nikos Parotsidis · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.92) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-165
**[Minimizing Recourse in an Adaptive Balls and Bins Game](https://doi.org/10.4230/LIPIcs.ICALP.2025.77)** (2025)

Случайное размещение задач по живым корзинам даёт O(n log n) recourse против адаптивного противника в определённой модели удалений корзин; следствие для spanner.

**Ограничение:** Модель adversary наблюдает назначения и выводит из строя bins; не заменяет доказательство стойкости cache/LSM к произвольным сбоям и rollback.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2025.77` · **Авторы:** Adi Fine, Haim Kaplan, Uri Stemmer · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.77) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)

### LIT-189
**[Recognizing and Realizing Temporal Reachability Graphs](https://doi.org/10.4230/LIPIcs.ESA.2025.93)** (2025)

Распознавание графов достижимости по временному графу: почти все уточнённые варианты NP-полны; для недиректированных solid graphs дан FPT по feedback-edge-set параметру.

**Ограничение:** Temporal reachability требует возрастающего времени рёбер и зависит от strict/non-strict temporal path. Результат не является сложностью обычного динамического транзитивного замыкания.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2025.93` · **Авторы:** Thomas Erlebach, Othon Michail, Nils Morawietz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ESA 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.93) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-190
**[On Incremental Approximate Shortest Paths in Directed Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2025.93)** (2025)

Инкрементальные структуры (1+ε)-приближённых кратчайших путей в разреженных ориентированных графах с неотрицательными полиномиально ограниченными весами против адаптивного противника.

**Ограничение:** Только вставки рёбер и приближённые расстояния. Суммарная стоимость update не выражает физические write bytes, полную точную достижимость или проверку сертификата.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2025.93` · **Авторы:** Adam Górkiewicz, Adam Karczmarz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.93) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-192
**[Fully Dynamic Algorithms for Coloring Triangle-Free Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2026.16)** (2026)

Рандомизированная динамическая O(Δ/ln Δ) раскраска безтреугольных графов с амортизированным временем обновления Δ^{o(1)}log n и большой вероятностью против адаптивного противника; метод entropy compression.

**Ограничение:** Инвариант отсутствия треугольников, верхняя степень Δ, вероятностная гарантия и адаптивность обязательны; entropy compression здесь приём доказательства, а не сжатие файлов.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.16` · **Авторы:** Sepehr Assadi, Helia Yazdanyar · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.16) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-196
**[Fully Dynamic Spectral and Cut Sparsifiers for Directed Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2026.157)** (2026)

Динамические направленные cut/spectral sparsifiers, включая degree-balance preservation; для β-balanced классов обновление за polylog при ограничениях на ε, β и противника.

**Ограничение:** Направленная спектральная аппроксимация, cut approximation, точная достижимость и сертификаты подлинности различны. Не терять ε, β, degree balance и тип adversary.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.157` · **Авторы:** Yibin Zhao · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.157) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-198
**[Dynamic MIS Revisited: Incremental, Fault Tolerant and Fully Dynamic](https://doi.org/10.4230/LIPIcs.SWAT.2026.21)** (2026)

Инкрементальный maximal independent set за O(√m) амортизированно, fault-sensitive вариант после k удалений и полностью динамический O(m^{2/3}) режим.

**Ограничение:** Maximal не означает maximum; lower bound для adaptive adversary или отдельного incremental режима нельзя переносить на oblivious fully dynamic режим и все оптимизационные задачи.

**Идентичность:** `doi:10.4230/LIPIcs.SWAT.2026.21` · **Авторы:** Manoj Gupta, Shahbaz Khan, Madhu Surendra · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [SWAT 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2026.21) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)


## algebraic-algorithms
*Алгебраические алгоритмы, subset sum и разреженные матрицы*

### LIT-060
**[Robustifying Sparse Matrix Multiplication](https://doi.org/10.4230/LIPIcs.ESA.2026.157)** (2026)

Чёрноящичная редукция robust top-k sparse matrix multiplication к обычному sparse multiplication с polylog overhead и учётом output sparsity.

**Ограничение:** Робастное приближение крупнейших элементов матрицы — не точное GF(q) ASET-суммирование; knapsack-составляющая не делает алгоритм DeltaMeter backend.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.157` · **Авторы:** Karl Bringmann, Nick Fischer, Vasileios Nakos · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-061
**[Improving Lagarias-Odlyzko Algorithm for Average-Case Subset Sum: Modular Arithmetic Approach](https://doi.org/10.4230/LIPIcs.STACS.2026.57)** (2026)

Модульная арифметика используется в улучшении алгоритмов средней сложности subset sum на базе lattice reduction.

**Ограничение:** Average-case integer subset sum с распределительными условиями не эквивалентен детерминированному точному GF(q) декодированию bounded active IDs.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.57` · **Авторы:** Antoine Joux, Karol Węgrzycki · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-135
**[Extremal graphs with no C4's, C6's, or C10's](https://doi.org/10.1016/0095-8956(91)90097-4)** (1991)

Wenger (JCTB 1991) строит плотные графы с запрещёнными циклами C4, C6 и C10; классическая экстремальная основа для оценки числа вес-2 столбцов с различимыми трёхэлементными суммами.

**Ограничение:** Из графа без коротких циклов следует хорошая матрица инцидентности только после определения ориентированных весов, поля и интерпретации циклических зависимостей; общая новая теорема ASET не заявляется.

**Идентичность:** `doi:10.1016/0095-8956(91)90097-4` · **Авторы:** Rephael Wenger · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G1-W2D3-GIRTH8.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G1-W2D3-GIRTH8.md) (model_overlap)

### LIT-136
**[An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8](https://arxiv.org/abs/1111.3279)** (2011)

Abreu, Araujo-Pardo, Balbuena, Labbate (2011) дают явные формулы для (s+1,8)-клеток, графов инцидентности обобщённых четырёхугольников. Их число рёбер Θ(m^{4/3}) обеспечивает известную нижнюю конструкцию шестикратно независимых двухразреженных столбцов.

**Ограничение:** Геометрический порядок s и размер конечного поля q коэффициентов различны; конечные графы не доказывают без дополнительных доводов всю асимптотику, а теорема с d=3 является производным классическим следствием.

**Идентичность:** `arxiv:1111.3279` · **Авторы:** Marién Abreu, Gabriela Araujo-Pardo, Camino Balbuena, Domenico Labbate · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G1-W2D3-GIRTH8.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G1-W2D3-GIRTH8.md) (model_overlap)

### LIT-137
**[Constructing dense grid-free linear 3-graphs](https://doi.org/10.1090/proc/15673)** (2022)

Gishboliner и Shapira (Proc. AMS 2022) доказывают существование линейных 3-однородных гиперграфов с Ω(m²) рёбрами без конфигурации 3×3 grid. Через точную эквивалентность unit-incidence ASET для характеристики поля ≥5 получается A_set(q,m,3,3)=Θ_q(m²).

**Ограничение:** Графы без grid не обязательно имеют линейную независимость любых шести столбцов; квадратичная ёмкость ASET не подтверждает неограниченный разрыв A_set/A_lin и не применима автоматически в характеристиках 2 или 3.

**Идентичность:** `doi:10.1090/proc/15673` · **Авторы:** Lior Gishboliner, Asaf Shapira · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-139
**[The Brown-Erdős-Sós conjecture in dense triple systems](https://arxiv.org/abs/2508.09841)** (2025)

Santos и Tyomkyn (авторский препринт 2025) устанавливают заявленный частный случай Brown–Erdős–Sós для линейных тройных систем высокой плотности δ>4/5; исследование сопряжено с (9,6)-конфигурациями.

**Ограничение:** Экстремальные (9,6) конфигурации не тождественны grid и не гарантируют ненулевую линейную зависимость произвольных шести столбцов. Предположение о пороге высокой плотности не является общим o(m²) верхним пределом при каждом δ>0.

**Идентичность:** `arxiv:2508.09841` · **Авторы:** Giovanne Santos, Mykhaylo Tyomkyn · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-140
**[Triangle-Free Triple Systems](https://doi.org/10.37236/14115)** (2026)

Frankl, Füredi, Goorevitch, Holzman и Simonyi (Electronic Journal of Combinatorics, май 2026) классифицируют экстремальные ограничения комбинаций четырёх типов треугольников в 3-однородных гиперграфах, включая точные/асимптотические случаи.

**Ограничение:** Ограничения треугольников гиперграфов не равнозначны запрету двух трёхэлементных аддитивных сумм или шестикратной линейной зависимости; не переносить показатели без структурного доказательства.

**Идентичность:** `doi:10.37236/14115` · **Авторы:** Peter Frankl, Zoltán Füredi, Ido Goorevitch, Ron Holzman, Gábor Simonyi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-145
**[Grid-free linear hypergraphs via Cayley-Bacharach](https://arxiv.org/abs/2602.14716)** (2026)

Pohoata (февраль 2026) строит для каждого r≥3 линейные r-однородные гиперграфы с Θ_r(m²) рёбрами без r×r grid, используя Cayley–Bacharach. Этот первоисточник закрывает широкое заявление об оригинальности dense grid-free конструкций для r≥4.

**Ограничение:** При r=4 запрещённый grid состоит из 8 рёбер, тогда как d=3 допускает коллизии уже среди максимум 6 рёбер. Линейная r-однородная модель имеет лишь O_r(m²) рёбер и не даёт актуальной полной ASET lower Ω(m^(12/5)). Препринт не является автоматически рецензируемой статьёй.

**Идентичность:** `arxiv:2602.14716` · **Авторы:** Cosmin Pohoata · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-146
**[The linear Turán number of small triple systems or why is the wicket interesting?](https://doi.org/10.1016/j.disc.2022.113025)** (2022)

Gyárfás–Sárközy (Discrete Mathematics, 2022) анализируют линейные Turán-числа небольших 3-однородных конфигураций и особую роль 5-рёберного wicket.

**Ограничение:** Wicket состоит из пяти рёбер на девяти вершинах; GF(3) локальный signed-set obstruction имеет пять рёбер на семи вершинах. Приписывать wicket-free o(m²) результат иной конфигурации без доказанного содержания неправомерно.

**Идентичность:** `doi:10.1016/j.disc.2022.113025` · **Авторы:** András Gyárfás, Gábor N. Sárközy · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-147
**[Wickets in 3-uniform hypergraphs](https://doi.org/10.1016/j.disc.2024.114029)** (2024)

Solymosi (Discrete Mathematics, 2024) доказывает, что линейные 3-гиперграфы без wicket имеют o(m²) рёбер, разрешая вопрос Gyárfás–Sárközy о разреженности такой запрещённой конфигурации.

**Ограничение:** Не переносить результат об отсутствии wicket на 7-вершинную 5-рёберную характеристика-3 зависимость, и тем более на произвольные взвешенные q-арные ASET-семейства. Содержательная редукция между запретами отсутствует.

**Идентичность:** `doi:10.1016/j.disc.2024.114029` · **Авторы:** József Solymosi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-151
**[New Turán Exponents for Two Extremal Hypergraph Problems](https://doi.org/10.1137/20M1325769)** (2021)

Shangguan и Tamo (SIAM J. Discrete Math., 2021) устанавливают нижнюю Ω(n^{r/(t-1)}) для t-union-free r-однородных гиперграфов. Совместно с классической cover-free верхней O(n^ceil(r/(t-1))) в случае (t,r)=(3,4) получается U_3(n,4)=Θ(n²).

**Ограничение:** Это нижняя оценка для уникальных объединений, а не для произвольных сумм с полевыми коэффициентами. Константа U_3(n,4) не следует из новой статьи Liu–Shangguan–Zhang (LIT-005) версии v3: она явно исключает (3,4). Не переносить меньший показатель union-free на всю ASET.

**Идентичность:** `doi:10.1137/20M1325769` · **Авторы:** Chong Shangguan, Itzhak Tamo · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md) (model_overlap)

### LIT-153
**[Additive codes arising from hypergraphs](https://arxiv.org/abs/2609.39680)** (2026)

Alfarano (30 сентября 2026) изучает критический показатель аддитивных кодов посредством гиперграфических полиматроидов, Berge-girth и слабой хроматичности, а также аналоги границ Singleton/Griesmer.

**Ограничение:** Критический показатель аддитивного кода и folded Hamming distance не равны экстремальному числу отличимых сумм не более трёх разреженных столбцов. Это смежная работа, не прямой доказанный перенос ASET.

**Идентичность:** `arxiv:2609.39680` · **Авторы:** Gianira N. Alfarano · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md) (model_overlap)

### LIT-194
**[Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction](https://doi.org/10.4230/LIPIcs.ICALP.2026.44)** (2026)

Точная по модели связь максимальной длины включающих цепочек в union-closure семейства множеств с размером мультипликативно аппроксимирующего reweighted sparsifier; приложения к weighted CSP.

**Ограничение:** Мультипликативное сохранение весов множества не равнозначно точной инъективности subset-sum ASET или ограничению на signed trade в конечном поле.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.44` · **Авторы:** Joshua Brakensiek, Venkatesan Guruswami, Aaron Putterman · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.44) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)

### LIT-195
**[Dynamic Rank, Basis, and Matching](https://doi.org/10.4230/LIPIcs.ICALP.2026.45)** (2026)

Поддержка матричного ранга, базиса и максимальной matching-структуры; при point entry-update заявлена стоимость Õ(r^{1.405}), где r — ранг матрицы, и отдельно стоимость column-update.

**Ограничение:** Арифметика над полем, стоимость матричной операции, вид обновления и materialization определяют bound; не переименовывать в битовые пробы, байты записи или гарантию для произвольного кольца.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.45` · **Авторы:** Jan van den Brand, Vishal Kumar, Daniel J. Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.45) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/399e1db43a1b1847de1855261b1da9c145068e4a/docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md) (model_overlap)


## proof-certification
*Машинные доказательства, сертификаты и верификация*

### LIT-062
**[Formalization of a Proof Calculus for Incremental Linearization for Satisfiability Modulo Nonlinear Arithmetic and Transcendental Functions](https://doi.org/10.1145/3779031.3779111)** (2026)

CPP 2026: Lean формализация proof calculus cvc5 для инкрементальной линеаризации SMT нелинейной/трансцендентной арифметики; восстановление проверяемых доказательств.

**Ограничение:** Soundness формализованного calculus не делает SMT поиск полным; к нашим GF(q) и DRAT-протоколам перенос возможен только через отдельный verified encoding.

**Идентичность:** `doi:10.1145/3779031.3779111` · **Авторы:** Tomaz Mascarenhas, Harun Khan, Abdalrhman Mohamed, Andrew Reynolds, Haniel Barbosa, Clark W. Barrett, Cesare Tinelli · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-063
**[PBLean: Pseudo-Boolean Proof Certificates for Lean 4](https://arxiv.org/abs/2602.08692)** (2026)

Проверяющий VeriPB proof-certificate через отражение в Lean с доказанной корректностью и проверенными переводами комбинаторных задач; поддерживает cutting planes.

**Ограничение:** PB сертификаты не равны DRAT; принятие proof log без формально проверенной кодировки исходной ASET модели не даёт end-to-end теоремы.

**Идентичность:** `arxiv:2602.08692` · **Авторы:** Stefan Szeider · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-003](INDEX.md#ml-003), [ML-008](INDEX.md#ml-008), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-064
**[Certificate-Carrying Transformation of Event-Driven Block Programs](https://arxiv.org/abs/2607.00563)** (2026)

Недоверенный оптимизатор программ Scratch выдаёт предлагаемое преобразование, а отдельный fail-closed checker пересчитывает семантические условия; ключевая лемма механизирована в Lean.

**Ограничение:** Доказательство привязано к явной модели наблюдения и cooperative scheduling; не доказывает точность сертификатов произвольного кэша или DAG.

**Идентичность:** `arxiv:2607.00563` · **Авторы:** Yuan Si, Jialu Zhang · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-065
**[Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4](https://arxiv.org/abs/2606.09600)** (2026)

Формализация covering-code в Lean с проверяемыми сертификатами верхних, нижних и точных covering numbers, сферическими bound и композиционными правилами.

**Ограничение:** Covering codes задают покрытие шаров Хэмминга, а не точность sparse subset sums; машинно проверенная база автора не проверена Mathlab CI.

**Идентичность:** `arxiv:2606.09600` · **Авторы:** Andreas Florath · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-003](INDEX.md#ml-003), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-066
**[Mechanized Dominator Tree Certification](https://doi.org/10.1145/3779031.3779107)** (2026)

Проверяемый Rocq сертификат для быстрого вычисления dominator tree в CFG на базе критериев Georgiadis–Tarjan, интегрированный в CompCertSSA.

**Ограничение:** Проверяется доминирование потока управления, а не целостность storage/CDC или произвольная корректность incremental recomputation; важно разделение solver/checker.

**Идентичность:** `doi:10.1145/3779031.3779107` · **Авторы:** Jean-Christophe Léchenet · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-067
**[Towards Composable Proofs of Cache Coherence Protocols](https://doi.org/10.1145/3779031.3779106)** (2026)

Композitional MSI verification в Lean 4 через локальные инварианты MI/SI вместо одного сложного глобального доказательства.

**Ограничение:** Локальные инварианты зависят от formal model cache coherence; они не являются готовыми независимыми сертификатами immutable chunk packs или optimistic concurrency.

**Идентичность:** `doi:10.1145/3779031.3779106` · **Авторы:** Martina Camaioni, Yann Herklotz, Tz-Ching Yu, Thomas Bourgeat · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-068
**[Model-Generic Incrementally Verifiable Computation from Updatable BARGs](https://doi.org/10.4230/LIPIcs.ITCS.2026.6)** (2026)

Криптографическая IVC модель позволяет инкрементально обновлять проверяемое свидетельство длинных вычислений и переносит построение на distributed/online computation.

**Ограничение:** Криптографическая computational soundness и допущения BARG не равны безусловным exact lower bounds для TOM или локального сертификата без криптографии.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2026.6` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-105
**[Instance Complexity and Unlabeled Certificates in the Decision Tree Model](https://doi.org/10.4230/LIPIcs.ITCS.2020.56)** (2020)

ITCS 2020: instance-optimal алгоритмы сравниваются с конкурентами, знающими сертификат; отдельно изучаются немаркированные сертификаты и симметрии.

**Ограничение:** Instance-optimal decision-tree модель не равна удостоверению нового значения DAG при пакете overwrites; перенесено только понятие сложности сертификата, не результаты конкретных теорем.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2020.56` · **Авторы:** Tomer Grossman, Ilan Komargodski, Moni Naor · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-131
**[New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification](https://doi.org/10.4230/LIPIcs.ITCS.2024.53)** (2024)

Ghosh–Shah доказывают сильные границы и разделения для нетривиальных online Merlin–Arthur коммуникационных протоколов и аннотированных потоковых графовых задач.

**Ограничение:** Наличие доказателя не гарантирует выигрыш относительно прямой передачи: некоторые нетривиальные протоколы значительно дороже простых. Дополнительная проверка soundness обязательна.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2024.53` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-142
**[Quantum Certificate Complexity](https://doi.org/10.1016/j.jcss.2007.06.020)** (2008)

Aaronson вводит randomized certificate complexity и quantum certificate complexity, устанавливает связи с adversary-методами и показывает разделения между мерами сложности проверки функций.

**Ограничение:** Рандомизированная проверка битового утверждения и сертификаты давно известны; работа не доказывает динамическую стоимость физически изменённых ячеек, authenticated root и online-MA proof maintenance.

**Идентичность:** `doi:10.1016/j.jcss.2007.06.020` · **Авторы:** Scott Aaronson · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md) (model_overlap)

### LIT-150
**[Sound 3-Query PCPPs Are Long](https://doi.org/10.1145/1595391.1595394)** (2009)

Ben-Sasson, Harsha, Lachish и Matsliah исследуют компромисс длины probabilistically checkable proof of proximity и достижимой soundness при ограничении верификатора тремя обращениями.

**Ограничение:** PCPP гарантирует отклонение входов, достаточно далёких от допустимых, а противоположная чётность может отличаться одним битом. Это не источник точного soundness для всех ложно заявленных parity state; нельзя автоматически переносить нижние границы на UCT-004.

**Идентичность:** `doi:10.1145/1595391.1595394` · **Авторы:** Eli Ben-Sasson, Prahladh Harsha, Oded Lachish, Arie Matsliah · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md) (model_overlap)

### LIT-156
**[Checking the Correctness of Memories](https://doi.org/10.1109/SFCS.1991.185352)** (1991)

FOCS 1991 и журнальная версия Algorithmica 1994 уже рассматривают онлайн-чтение/запись недоверенной памяти при малом надежном локальном состоянии, вероятностную проверку, информационно-теоретические ограничения надежной памяти и time-space компромиссы.

**Ограничение:** Полные гипотезы каждой теоремы первого источника не проверены независимо; утверждение log n не переносится безусловно на все коды/запросы UCT. Оригинальная конференционная статья и журнальное расширение — одна работа.

**Идентичность:** `doi:10.1109/SFCS.1991.185352` · **Также:** doi:10.1007/BF01185212 · **Авторы:** Manuel Blum, William S. Evans, Peter Gemmell, Sampath Kannan, Moni Naor · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/536fd3aab5aedcc89ca80c24333162991e51ec4b/docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) (model_overlap)

### LIT-157
**[Memory Checking Requires Logarithmic Overhead](https://doi.org/10.1145/3618260.3649686)** (2024)

STOC 2024: p >= n/(log n)^{O(q)} для memory checking c надежной памятью p и удаленными пробами q. В отдельном несимметричном режиме p >= n/(q_r q_w log n)^{O(q_r)}, что исключает константные чтения при субполиномиальных записях и малом доверенном состоянии.

**Ограничение:** Рассматриваются удаленные пробы для логических RAM-операций, а не число реально измененных координат; полнота 2/3, soundness обратно-полиномиальная, не covert. Теорема 5 оригинального PDF изучена по постановке и вводным формулировкам, полный источник доказательства независимо не воспроизведен. JACM 2025 — версия той же статьи.

**Идентичность:** `doi:10.1145/3618260.3649686` · **Также:** doi:10.1145/3707202 · **Авторы:** Elette Boyle, Ilan Komargodski, Neekon Vafa · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/536fd3aab5aedcc89ca80c24333162991e51ec4b/docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) (model_overlap)

### LIT-158
**[The Complexity of Memory Checking with Covert Security](https://doi.org/10.1007/978-3-031-91092-0_11)** (2025)

EUROCRYPT 2025 продолжает memory checking при covert-безопасности: нарушитель может рискнуть обнаружением с постоянной вероятностью, но при read-only reads сохраняется известное нижнее ограничение порядка log n/loglog n для допустимых параметров.

**Ограничение:** Read-only reads запрещает менять удаленное и локальное состояние во время логического чтения; требуется точно учитывать физические размер и слово. Подробный полный PDF и доказательство Theorem 3 независимо не проверены, в этой записи проверены издательский и IACR abstracts.

**Идентичность:** `doi:10.1007/978-3-031-91092-0_11` · **Также:** publisher:iacr:2025-358 · **Авторы:** Elette Boyle, Ilan Komargodski, Neekon Vafa · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/536fd3aab5aedcc89ca80c24333162991e51ec4b/docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) (model_overlap)

### LIT-159
**[Vector Commitments with Efficient Updates](https://doi.org/10.4230/LIPIcs.AFT.2023.29)** (2023)

AFT 2023, Definition 4 и Theorem 5: для динамических proof-binding vector commitments если обновление отдельного доказательства имеет стоимость O(k^{1-nu}), вспомогательные обновляющие данные требуют Omega(k^nu); конструкции достигают близкого асимптотического компромисса.

**Ограничение:** Не переносить на произвольные position-binding сертификаты или иные параметры угрозы. Публичные изменения элементов/индексов НЕ входят в размер U; полная сетевая стоимость больше. Доказательство теоремы вынесено в полную версию и здесь не воспроизведено.

**Идентичность:** `doi:10.4230/LIPIcs.AFT.2023.29` · **Также:** arxiv:2307.04085 · **Авторы:** Ertem Nusret Tas, Dan Boneh · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/536fd3aab5aedcc89ca80c24333162991e51ec4b/docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) (model_overlap)

### LIT-199
**[Merkle Mountain Ranges are Optimal: On Witness Update Frequency for Cryptographic Accumulators](https://doi.org/10.1007/978-3-032-01878-6_6)** (2025)

CRYPTO 2025: ω(n) совокупных witness updates за n append-only добавлений, и Ω(n log n/log log n) в отдельном режиме; Merkle mountain ranges близки к оптимальности.

**Ограничение:** Частота изменений witness в append-only set accumulator, а не CPU или байты сети. Параметры случайного множества и длина digest обязательны; без них не переносить на UCT.

**Идентичность:** `doi:10.1007/978-3-032-01878-6_6` · **Также:** publisher:iacr:2025-234 · **Авторы:** Joseph Bonneau, Jessica Chen, Miranda Christ, Ioanna Karantaidou · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-200
**[Lower Bounding Update Frequency in Short Accumulators and Vector Commitments](https://doi.org/10.1007/978-3-032-25330-9_7)** (2026)

EUROCRYPT 2026: нижние границы ожидаемого количества инвалидированных proofs — почти n при коротком digest для exponential или superpolynomial universes.

**Ограничение:** Нужно фиксировать аддитивный аккумулятор / updatable VC, security/digest и размер универсума. Witness invalidation не равно стоимости обновления или коммуникации.

**Идентичность:** `doi:10.1007/978-3-032-25330-9_7` · **Также:** publisher:iacr:2025-1558 · **Авторы:** Hamza Abusalah, Gaspard Anthoine, Gennaro Avitabile, Emanuele Giunta · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-202
**[How Efficient Can Memory Checking Be?](https://doi.org/10.1007/978-3-642-00457-5_30)** (2009)

TCC 2009: lower bound deterministic non-adaptive online memory checker и конструкции асимметричного read/write checker, включая offline амортизацию.

**Ограничение:** Не переносить deterministic nonadaptive lower bound на произвольный randomized adaptive memory checker; offline и online различны по гарантии обнаружения ошибки.

**Идентичность:** `doi:10.1007/978-3-642-00457-5_30` · **Авторы:** Cynthia Dwork, Moni Naor, Guy N. Rothblum, Vinod Vaikuntanathan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-203
**[Verification-efficient Homomorphic Signatures for Verifiable Computation over Data Streams](https://eprint.iacr.org/2025/110)** (2025)

IACR ePrint 2025/110, FC 2025: новые linearly homomorphic signatures и verifier-efficient HSNP для вычислений по потокам, включая скользящие статистики.

**Ограничение:** Конструктивная верхняя оценка криптографической верификации с signed inputs, а не информационная lower bound. Отсутствует подтверждённый DOI конференционной версии.

**Идентичность:** `publisher:iacr:2025-110` · **Авторы:** Gaspard Anthoine, Daniele Cozzo, Dario Fiore · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-204
**[On the Impossibility of Batch Update for Cryptographic Accumulators](https://doi.org/10.1007/978-3-642-14712-8_11)** (2010)

LATINCRYPT 2010: атака на небезопасный batch-update accumulator и Ω(m) worst-case на обновление отдельного witness после m изменений в изученной модели.

**Ограничение:** Нельзя обобщать на все возможные cryptographic accumulator или VC; число инвалидированных свидетелей не равно цене одного witness-refresh.

**Идентичность:** `doi:10.1007/978-3-642-14712-8_11` · **Авторы:** Philippe Camacho, Alejandro Hevia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md](https://github.com/definitely-stable/Mathlab/blob/cd5a7ec2b0ed442d03bac0b03e091421ab5446ef/docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) (model_overlap)

### LIT-206
**[PoWER Never Corrupts: Tool-Agnostic Verification of Crash Consistency and Corruption Detection](https://www.usenix.org/conference/osdi25/presentation/leblanc)** (2025)

OSDI 2025: метод PoWER задаёт предусловия записей, обеспечивающие восстановимость, и модель обнаружения повреждений носителя; представлены верифицированные CapybaraKV (Verus) и CapybaraNS (Dafny).

**Ограничение:** Техника и результаты относятся к формально моделируемым storage API и persistent memory; исключения на GitHub-hosted POSIX не являются переносом доказательства crash consistency или проверкой физического SSD.

**Идентичность:** `usenix:osdi25:leblanc` · **Авторы:** Hayley LeBlanc, Jacob R. Lorch, Chris Hawblitzel, Cheng Huang, Yiheng Tao, Nickolai Zeldovich, Vijay Chidambaram · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md](https://github.com/definitely-stable/Mathlab/blob/6cc1496bf68a1909e1bccb4def731a3b7d5e99ad/docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md) (model_overlap)

### LIT-207
**[Specifying and Checking File System Crash-Consistency Models](https://doi.org/10.1145/2872362.2872406)** (2016)

ASPLOS 2016 Ferrite: формальные модели допустимых последствий сбоя файловых систем, litmus-тесты и проверка реального ext4. Модель API POSIX сама по себе не задаёт полный порядок сохранения после crash.

**Ограничение:** Работа не доказывает инварианты конкретной двухслотовой схемы Mathlab; для гарантий реального power loss необходима модель конкретной файловой системы и барьеров записи.

**Идентичность:** `doi:10.1145/2872362.2872406` · **Авторы:** James Bornholt, Antoine Kaufmann, Jialin Li, Arvind Krishnamurthy, Emina Torlak, Xi Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md](https://github.com/definitely-stable/Mathlab/blob/6cc1496bf68a1909e1bccb4def731a3b7d5e99ad/docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md) (model_overlap)

### LIT-208
**[Lightweight file system crash-consistency checking with differential fuzzing](https://doi.org/10.15514/ISPRAS-2026-38(1)-7)** (2026)

Proceedings of ISP RAS 2026: расширение DIFFuzzer на моделирование аварийных остановов файловой системы и дифференциальное выявление несогласованностей; сообщено об ошибках, подтверждённых авторами файловых систем.

**Ограничение:** Результаты тестирования файловых систем не доказывают устойчивость нашего протокола WAL/manifest. Для сильной гарантии требуется самостоятельная модель crash states и проверка реального устройства.

**Идентичность:** `doi:10.15514/ISPRAS-2026-38(1)-7` · **Авторы:** V. M. Kovalevsky, V. V. Kechin, A. S. Yanin, V. M. Itsykson · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md](https://github.com/definitely-stable/Mathlab/blob/6cc1496bf68a1909e1bccb4def731a3b7d5e99ad/docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md) (model_overlap)


## proof-complexity
*Нижние границы доказательств, IPS/PIT и сертификаты*

### LIT-070
**[Lower Bounds against the Ideal Proof System in Finite Fields](https://doi.org/10.1145/3798129.3800721)** (2026)

Elbaz и соавторы доказывают нижние границы для фрагментов IPS над конечными полями постоянного размера; конструкция knapsack и связи с AC0[p]-Frege.

**Ограничение:** Границы относятся к определённым классам алгебраических опровержений и глубин схем, а не к сложности всех DRAT-протоколов или ASET.

**Идентичность:** `doi:10.1145/3798129.3800721` · **Авторы:** Tal Elbaz, Nashlen Govindasamy, Jiaqi Lu, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-071
**[The Weak Rank Principle: Lower Bounds and Applications](https://doi.org/10.1145/3798129.3800735)** (2026)

Новые экспоненциальные нижние границы PCR над F2 для слабого rank principle и построение proof-complexity generators.

**Ограничение:** Алгебраические формулы XY=A и доказательства несостоятельности — не сертификат минимальной ёмкости конкретного ASET и не скорость SAT-решателя.

**Идентичность:** `doi:10.1145/3798129.3800735` · **Авторы:** Michal Garlík, Svyatoslav Gryaznov, Hanlin Ren, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-080
**[Polynomial Identity Testing and the Ideal Proof System: PIT Is in NP If and Only If IPS Can Be p-Simulated by a Cook-Reckhow Proof System](https://doi.org/10.1145/3798129.3800865)** (2026)

Grochow показывает эквивалентность эффективной детерминированной верифицируемости IPS при p-симуляции и включения PIT в NP (с оговорками о поле).

**Ограничение:** Не утверждается PIT∈NP и не предоставляется готовый детерминированный checker для произвольных полиномиальных схем.

**Идентичность:** `doi:10.1145/3798129.3800865` · **Авторы:** Joshua A. Grochow · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-090
**[Lower Bounds for Near-Quadratic-Depth Resolution over Parities](https://doi.org/10.1145/3798129.3800809)** (2026)

Экспоненциальные нижние границы длины refutation в Res(⊕) при глубине O(N^(2−ε)) для специальных Tseitin/CNF конструкций.

**Ограничение:** Доказательствo для глубинно ограниченного Res(⊕) не ограничивает произвольный SAT/DRAT checker и не доказывает трудность GF(5) ASET.

**Идентичность:** `doi:10.1145/3798129.3800809` · **Авторы:** Sreejata Kishor Bhattacharya, Farzan Byramji, Arkadev Chattopadhyay, Russell Impagliazzo · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-106
**[Certification complexity of Boolean functions](https://eccc.weizmann.ac.il/report/2026/206/)** (2026)

Сентябрь 2026, ECCC TR26-206: операционная сложность сертификации Boolean функций, характеристики классической/рандомизированной/квантовой сертификатной сложности и новые квантовые нижние границы.

**Ограничение:** Авторский отчёт не утверждает оптимальное доказательство для инкрементального batch-DAG обновления; результаты по квантовой сложности нельзя автоматически переносить на old-root read-probe модель.

**Идентичность:** `publisher:eccc:tr26-206` · **Авторы:** Chandrima Kayal, Sophie Laplante, Émile Larroque, Krisjanis Prusis, Jevgenijs Vihrovs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-107
**[On Condensation of Block Sensitivity, Certificate Complexity and the $\mathsf{AND}$ (and $\mathsf{OR}$) Decision Tree Complexity](https://arxiv.org/abs/2602.01042)** (2026)

Препринт 2026 v2: доказаны ограничения конденсации block sensitivity, certificate complexity и AND/OR decision trees при ограничениях переменных.

**Ограничение:** Заявление касается операций restriction/condensation, а не минимального shared batch certificate; версия v2 явно исключила доказательство из первой версии — цитировать только v2.

**Идентичность:** `arxiv:2602.01042` · **Авторы:** Sai Soumya Nalli, Karthikeya Polisetty, Jayalal Sarma · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-108
**[Complexity measures and decision tree complexity: a survey](https://doi.org/10.1016/S0304-3975(01)00144-X)** (2002)

Классический обзор связи certificate complexity, sensitivity, block sensitivity, степени Boolean функций и decision-tree query complexity; математический прототип нового HYP-103 сертификата.

**Ограничение:** Обзор не является новым доказательством специфического обещания old root + batch overwrite; позволяет классифицировать базовую модель как стандартную certificate complexity.

**Идентичность:** `doi:10.1016/S0304-3975(01)00144-X` · **Авторы:** Harry Buhrman, Ronald de Wolf · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-143
**[All Classical Adversary Methods Are Equivalent for Total Functions](https://doi.org/10.1145/3442357)** (2021)

Для полных булевых функций авторы доказывают эквивалентность классических adversary-методов оценки рандомизированной query complexity и их связь с fractional block sensitivity.

**Ограничение:** Дробная упаковка и randomized certificate adversary уже являются первоисточником prior art; частичные функции, физическая локальность обновления, недоверенное онлайн-доказательство и его стоимость требуют отдельных предпосылок.

**Идентичность:** `doi:10.1145/3442357` · **Авторы:** Andris Ambainis, Mārtiņš Kokainis, Krišjānis Prūsis, Jevgēnijs Vihrovs, Aleksejs Zajakins · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md) (model_overlap)

### LIT-144
**[Randomized Query Complexity Can Beat Certificate Complexity](https://arxiv.org/abs/2609.15063)** (2026)

Авторы препринта сентября 2026 построили полную булеву функцию с рандомизированной сложностью запросов существенно ниже детерминированной сертификатной сложности: R(f)=O-тильда(sqrt(C(f))).

**Ограничение:** Результат заявлен в авторском abstract, доказательство не перепроверено; нельзя переносить C(f) на bounded-error R(f). Модель не является динамическим онлайн-доказательством с учётом локальных записей, секретных монет верификатора и поддержки свидетельств.

**Идентичность:** `arxiv:2609.15063` · **Авторы:** Shalev Ben-David, Robin Kothari · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md) (model_overlap)

### LIT-149
**[Certification complexity of Boolean functions](https://arxiv.org/abs/2609.26757)** (2026)

Kayal, Laplante, Larroque, Prūsis и Vihrovs вводят операционную certification complexity для булевых функций, сопоставляют классические и квантовые сертификаты с randomized certificate complexity, sabotage/unambiguous certificate measures и границами query complexity.

**Ограничение:** Авторский препринт сентября 2026 проверен на уровне официального abstract/идентичности; полные теоремы не перепроверены. Применимость к нашему частному perfect-completeness/private-coin нелинейному proof-cover и динамической стоимости изменений требует явного theorem-to-theorem сопоставления.

**Идентичность:** `arxiv:2609.26757` · **Авторы:** Chandrima Kayal, Sophie Laplante, Émile Larroque, Krišjānis Prūsis, Jevgēnijs Vihrovs · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md) (model_overlap)

### LIT-154
**[Satisfiability Coding Lemma](https://doi.org/10.4086/cjtcs.1999.011)** (1999)

Первоисточник PPZ: upper bound 2^(n-n/k) на количество изолированных удовлетворяющих присваиваний k-CNF, доказательство через критические дизъюнкты и случайную перестановку переменных. На этом основана ограниченная нелинейная теорема G2-D о длине свидетельства.

**Ограничение:** Уже известная лемма 1999 года. Mathlab независимо выводит только используемый конкретный случай для изолированных решений, не весь исходный набор теорем. Не переносить на полностью оплаченные онлайн-доказательства, фиксированную малую ошибку, стоимость prover/verifier.

**Идентичность:** `doi:10.4086/cjtcs.1999.011` · **Авторы:** Ramamohan Paturi, Pavel Pudlák, Francis Zane · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md) (model_overlap)

### LIT-155
**[CNF Encodings of Parity](https://doi.org/10.4230/LIPIcs.MFCS.2022.47)** (2022)

MFCS 2022 устанавливает нижние границы для кодирования parity в CNF со вспомогательными nondeterministic variables, в том числе ширину k>=n/(s+1), используя PPZ и OR-of-CNF/depth-three circuits. Это ключевой prior art к G2-D.

**Ограничение:** Ширина CNF в оригинальной теореме включает вхождения дополнительных переменных; она не идентична числу проб данных p. Для G2-D применяется отдельная per-witness p-CNF без этих переменных, плюс PPZ. Не выдавать result за новый или за полную модель онлайн MA.

**Идентичность:** `doi:10.4230/LIPIcs.MFCS.2022.47` · **Авторы:** Gregory Emdin, Alexander S. Kulikov, Ivan Mihajlin, Nikita Slezkin · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md) (model_overlap)


## algebraic-complexity
*Алгебраические схемы, математика и нижние границы*

### LIT-077
**[Closure under Factorization from a Result of Furstenberg](https://doi.org/10.1145/3798129.3800738)** (2026)

Из классической формулы Фюрстенберга выводится замкнутость формул и constant-depth алгебраических схем относительно множителей над полями характеристики ноль.

**Ограничение:** Результат не распространяется автоматически на малую положительную характеристику, noncommutative models и произвольные PIT black-box инструкции.

**Идентичность:** `doi:10.1145/3798129.3800738` · **Авторы:** Somnath Bhattacharjee, Mrinal Kumar, Shanthanu S. Rai, Varun Ramanathan, Ramprasad Saptharishi, Shubhangi Saraf · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [OM-135](INDEX.md#om-135)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-089
**[Superquadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://doi.org/10.1145/3798129.3800802)** (2026)

Chen–Tal–Wang устанавливают сверхквадратичные нижние границы размера схем глубины два с линейными threshold gates.

**Ограничение:** Предел схем глубины 2 не становится автоматически пределом общего вычисления, Fourier трансформов или динамических алгоритмов.

**Идентичность:** `doi:10.1145/3798129.3800802` · **Авторы:** Lijie Chen, Avishay Tal, Yichuan Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-130](INDEX.md#om-130), [OM-132](INDEX.md#om-132)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-093
**[Classifying Identities: Subcubic Distributivity Checking and Hardness from Arithmetic Progression Detection](https://doi.org/10.1145/3798129.3800854)** (2026)

Алгебраические тождества конечных операций классифицированы по complexity проверки; distributivity за O(|S|^ω) и условные tight lower bounds.

**Ограничение:** Условные reductions из triangle detection/AP detection не дают безусловного lower bound для любой конечной GF(q) арифметики или проверки Rust crate.

**Идентичность:** `doi:10.1145/3798129.3800854` · **Авторы:** Bartłomiej Dudek, Nick Fischer, Geri Gokaj, Ce Jin, Marvin Künnemann, Xiao Mao, Mirza Redžić · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-095
**[Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width](https://doi.org/10.4230/LIPIcs.ICALP.2026.130)** (2026)

Kluk–Nederlof: нижние границы 2^Ω(k log log k) для tropical-circuit pure DP задач связности/коммивояжёра при pathwidth k.

**Ограничение:** Граница относится к конкретной модели tropical circuits; алгебраические ускорения и общие DP алгоритмы вне класса не опровергаются.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.130` · **Авторы:** Kacper Kluk, Jesper Nederlof · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.130) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [OM-133](INDEX.md#om-133), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## fine-grained-algorithms
*Edit distance, строки и тонкая сложность*

### LIT-074
**[Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://doi.org/10.1145/3798129.3800789)** (2026)

Mao–Rubinstein: рандомизированные (1+ε)-ED и (1−ε)-LCS схемы с ускорением относительно n² на субквадратическом масштабе.

**Ограничение:** Аппроксимация расстояния между строками не даёт exact edit script, оптимальной delta patch-базы или онлайн обновлений.

**Идентичность:** `doi:10.1145/3798129.3800789` · **Авторы:** Xiao Mao, Aviad Rubinstein · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-092
**[Space-Efficient Text Indexing with Mismatches using Function Inversion](https://doi.org/10.1145/3798129.3800818)** (2026)

Bibbens–Borevitz–McCauley строят линейно-пространственный индекс поиска строк с ≤k Hamming mismatches и сглаженным tradeoff query/space.

**Ограничение:** Поиск при Hamming distance не покрывает вставки/удаления и не является автоматическим поиском минимальной delta patch-базы.

**Идентичность:** `doi:10.1145/3798129.3800818` · **Авторы:** Jackson Bibbens, Levi Borevitz, Samuel McCauley · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-166
**[Bounded Edit Distance: Optimal Static and Dynamic Algorithms for Small Integer Weights](https://doi.org/10.1145/3717823.3718168)** (2025)

Авторы показывают ~O(k) worst-case стоимость изменения точного динамического unweighted edit distance в параметризованной модели; для bounded малых целых весов другая граница.

**Ограничение:** Не даёт аналогичной гарантии для произвольных весов, общего вычислительного DAG, delta patch bytes и компрессионной стоимости.

**Идентичность:** `doi:10.1145/3717823.3718168` · **Авторы:** Egor Gorbachev, Tomasz Kociumaka · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2025](https://acm-stoc.org/stoc2025/toc.html) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md](https://github.com/definitely-stable/Mathlab/blob/cce55aa0eb28e369eef3e032e01d3fce79304c1d/docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md) (model_overlap)


## randomized-sampling
*Рандомизированная выборка, подсчёт и memory-sample*

### LIT-075
**[A Unified Approach to Memory-Sample Tradeoffs for Detecting Planted Structures](https://doi.org/10.1145/3798129.3800739)** (2026)

Обобщённая схема нижних границ memory/sample для многопроходного обнаружения planted bicliques, sparse means и sparse PCA.

**Ограничение:** Распределительное различение planted-vs-null не равно set-only GF(2) строгой оценке d; число проходов и модель памяти должны совпасть.

**Идентичность:** `doi:10.1145/3798129.3800739` · **Авторы:** Sumegha Garg, Jabari Hastings, Chirag Pabbaraju, Vatsal Sharan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-081
**[Parallel Sampling via Autospeculation](https://doi.org/10.1145/3798129.3800828)** (2026)

Автоспекулятивная выборка с параллельным доступом к оракулам снижает ожидаемую глубину последовательного генерирования до примерно √n.

**Ограничение:** Выигрыш по параллельной глубине в oracle model не означает меньшую суммарную вычислительную работу, память или низкую latency Rust API.

**Идентичность:** `doi:10.1145/3798129.3800828` · **Авторы:** Nima Anari, Carlo Baronio, CJ Chen, Alireza Haqi, Frederic Koehler, Anqi Li, Thuy-Duong Vuong · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-113](INDEX.md#om-113), [OM-139](INDEX.md#om-139)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-082
**[Shifted Composition IV: Toward Ballistic Acceleration for Log-Concave Sampling](https://doi.org/10.1145/3798129.3800881)** (2026)

Altschuler–Chewi–Zhang исследуют недодемпфированную Langevin-динамику, KL ошибки дискретизации и ускоренную лог-вогнутую выборку.

**Ограничение:** Гарантии зависят от регулярности log-concave распределения, свойств ULD и модели oracle; не general uniform sampler для дискретных комбинаторных объектов.

**Идентичность:** `doi:10.1145/3798129.3800881` · **Авторы:** Jason M. Altschuler, Sinho Chewi, Matthew S. Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [OM-113](INDEX.md#om-113)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-134
**[Equivalent Comparisons of Experiments](https://doi.org/10.1214/aoms/1177729032)** (1953)

Blackwell формализует сравнение статистических экспериментов и относительную информативность наблюдений для задач принятия решений.

**Ограничение:** Порядок информативности не даёт автоматических cell-probe или patch-byte границ; требуется конкретный канал наблюдений и допустимое преобразование статистического эксперимента.

**Идентичность:** `doi:10.1214/aoms/1177729032` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DM-001](INDEX.md#dm-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/9beb9721ba7213a9a2701fc92a41d539bcc75b79/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)
