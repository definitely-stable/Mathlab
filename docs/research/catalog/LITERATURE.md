# External primary literature — тематический каталог

> Generated from `literature.json` by `research/literature.py`. Редактировать следует только JSON.

Срез: **2026-10-09** · **144** проверенных ссылок на первичные публикации/авторские рукописи.

**Критически важно:** проверенная библиография или авторский abstract не равны независимо проверенному доказательству, статистическому результату либо научной новизне. Точные условия — в каждой записи.

Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md). Внутренние исследования: [INDEX.md](INDEX.md).

| Направление | Записей |
| --- | ---: |
| [Кодирование, ограниченная поддержка, экстремальные границы](#sparse-coding) | 22 |
| [Динамические структуры, каноничность и локальность правок](#dynamic-data-structures) | 19 |
| [Инкрементальные вычисления и сертификаты](#incremental-computation) | 18 |
| [DELSK: поиск delta-базы, сжатие, признаки](#delta-base-selection) | 15 |
| [DeltaMeter: потоковые оценки и согласование множеств](#streaming-reconciliation) | 14 |
| [Сжатые структуры, индексация строк и нижние границы](#compressed-indexing) | 6 |
| [Онлайн-оптимизация, конкурентные оценки и барьеры](#online-optimization) | 4 |
| [Динамические графы, гиперграфы и sparsification](#graph-algorithms) | 10 |
| [Алгебраические алгоритмы, subset sum и разреженные матрицы](#algebraic-algorithms) | 10 |
| [Машинные доказательства, сертификаты и верификация](#proof-certification) | 9 |
| [Нижние границы доказательств, IPS/PIT и сертификаты](#proof-complexity) | 7 |
| [Алгебраические схемы, математика и нижние границы](#algebraic-complexity) | 4 |
| [Edit distance, строки и тонкая сложность](#fine-grained-algorithms) | 2 |
| [Рандомизированная выборка, подсчёт и memory-sample](#randomized-sampling) | 4 |

## sparse-coding
*Кодирование, ограниченная поддержка, экстремальные границы*

### LIT-001
**[Bounded-Contention Coding for Wireless Networks in the High SNR Regime](https://arxiv.org/abs/1208.6125)** (2012)

Кодирование для декодирования сумм ограниченного числа одновременных сообщений; исходный объект уже близок к бинарному bounded-active identification.

**Ограничение:** Коммуникационная модель и допускаемое число участников отличаются от строгой поддержки столбцов ASET.

**Идентичность:** `arxiv:1208.6125` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-002
**[Location-correcting codes](https://doi.org/10.1109/18.485724)** (1996)

Классическая граница для слабых множеств Сидона используется в Mathlab для строгой конечной оценки 10≤A₅^set(3,2,2)≤11.

**Ограничение:** ASET влечёт weak Sidon, но обратное неверно; correction locality из LCC не равна write locality ASET.

**Идентичность:** `doi:10.1109/18.485724` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-008](INDEX.md#ml-008), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md) (cited)

### LIT-003
**[Probabilistic existence results for separable codes](https://arxiv.org/abs/1505.02597)** (2015)

Blackburn сопоставляет frameproof и t-separable коды и устанавливает вероятностные границы; приводит специальные ограничения при t=2.

**Ограничение:** Descendant-модель не совпадает автоматически с ограниченными конечнополевыми суммами и изменяемой поддержкой ASET.

**Идентичность:** `arxiv:1505.02597` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-004
**[Bounds and Constructions for overline-3-Separable Codes with Length 3](https://arxiv.org/abs/1507.00954)** (2015)

Границы и конструкции именно для 3-separable кодов длины 3, через partial Latin squares, perfect hashing и Steiner triple systems.

**Ограничение:** Речь о barred-3-separability (overline{3}), сильной fingerprinting-модели; нельзя без определения её отождествлять с обычным 3-separable или ASET d=2.

**Идентичность:** `arxiv:1507.00954` · **Авторы:** Minquan Cheng, Jing Jiang, Haiyan Li, Ying Miao, Xiaohu Tang · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-005
**[Sharp bounds for uniform union-free hypergraphs](https://arxiv.org/abs/2605.11949)** (2026)

Асимптотические экстремальные результаты для t-union-free r-однородных гиперграфов, а также разреженные упаковки.

**Ограничение:** Совпадение объединений рёбер не тождественно совпадению модульных сумм в GF(q); особенно осторожно при нечётной характеристике.

**Идентичность:** `arxiv:2605.11949` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-010](INDEX.md#ml-010), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (cited)

### LIT-006
**[On Codes with Support-Constrained Parity Checks](https://arxiv.org/abs/2605.08644)** (2026)

Оптимальное минимальное расстояние линейного кода при заданной маске поддержки строк проверочной матрицы; конструкции над достаточно большими полями.

**Ограничение:** Строковые parity-check ограничения и расстояние кода не дают автоматически границы мощности ASET со столбцовыми ограничениями.

**Идентичность:** `arxiv:2605.08644` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-031
**[Signature Codes for a Noisy Adder Multiple Access Channel](https://arxiv.org/abs/2206.10735)** (2022)

q-арные signature codes для noisier integer-adder multiple access, включая явные конструкции и converse bounds.

**Ограничение:** Сумма берётся над целыми и учитывает канал с шумом, в отличие от безошибочной конечнополевой ASET-суммы.

**Идентичность:** `arxiv:2206.10735` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (model_overlap)

### LIT-033
**[Sign-Compute-Resolve for Tree Splitting Random Access](https://arxiv.org/abs/1602.02612)** (2016)

Суммы сигнатур активных передатчиков в физическом канале используются для восстановления участников при известной bound K.

**Ограничение:** Подпись в физическом аддер-канале и adaptive tree-splitting не являются sparse GF(q) ASET-конструкцией со строгим весом столбцов.

**Идентичность:** `arxiv:1602.02612` · **Авторы:** Jasper Goseling, Cedomir Stefanovic, Petar Popovski · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-034
**[Finite Field Multiple Access](https://arxiv.org/abs/2303.14086)** (2023)

FFMA, element-pair codes и unique sum-pattern mapping по конечным полям, обеспечивающие мультиплексирование в многопользовательском канале.

**Ограничение:** Результаты о channel coding/error curves не задают автоматически максимум ASET при ограничении числа ненулевых координат.

**Идентичность:** `arxiv:2303.14086` · **Авторы:** Qi-yue Yu, Jiang-xuan Li, Shu Lin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-035
**[Signature codes for weighted binary adder channel and multimedia fingerprinting](https://arxiv.org/abs/1905.10180)** (2019)

Исследуются signature-code конструкции для взвешенного аддер-канала и fingerprinting, близкие по допустимым коэффициентам к ограниченным суммам.

**Ограничение:** Взвешенная сумма и реальные/целочисленные коэффициенты не тождественны полевым суммам с коэффициентами лишь 0/1.

**Идентичность:** `arxiv:1905.10180` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-036
**[On Constant-Weight Binary B2-Sequences](https://arxiv.org/abs/2303.12990)** (2023)

Бинарные B₂-последовательности с постоянным весом — прямой формальный сосед hard-column-support ёмкости ASET.

**Ограничение:** Определение B₂ допускает собственное правило для повторяющихся слагаемых и обычные целые суммы: проверять связь со строгими d<=2 GF(q) subset sums.

**Идентичность:** `arxiv:2303.12990` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-037
**[Multi-Group Testing for Items with Real-Valued Status under Standard Arithmetic](https://arxiv.org/abs/1303.6020)** (2013)

Групповое тестирование со статусами произвольных вещественных значений и неадаптивными суммарными измерениями.

**Ограничение:** Объект — реальные арифметические суммы/measurement matrices, не конечнополевые уникальные subset sums.

**Идентичность:** `arxiv:1303.6020` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-001](INDEX.md#ml-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-043
**[Sparse Parity-Check Matrices over GF(q)](https://doi.org/10.1017/S0963548304006625)** (2005)

Lefmann: максимальная длина разреженных parity-check матриц с заданным ограничением nonzeros/column и независимостью любого k столбцов; bounds по q,k,r.

**Ограничение:** Класс всех signed linear dependences отличается от ASET ограниченных 0/1 subset-sum collisions; возможно даёт достаточные семейства, но не точное равенство capacities.

**Идентичность:** `doi:10.1017/S0963548304006625` · **Авторы:** Hanno Lefmann · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-044
**[On Parity Check (0,1)-Matrix over Z_p](https://doi.org/10.1137/120881129)** (2015)

Bshouty–Mazzawi: неадаптивные additive queries и (0,1) parity-check матрицы над Z_p с независимостью любых k столбцов.

**Ограничение:** Ограничено двоичностью элементов матрицы и проверкой k-wise independence; не равнозначно ASET с hard column support w.

**Идентичность:** `doi:10.1137/120881129` · **Авторы:** Nader H. Bshouty, Hanna Mazzawi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/LENT-001-PRIOR-ART.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/LENT-001-PRIOR-ART.md) (cited)

### LIT-083
**[Combinatorial Bounds for List Recovery via Discrete Brascamp-Lieb Inequalities](https://doi.org/10.1145/3798129.3800756)** (2026)

Дискретные неравенства Браскампа–Либа используются для новых комбинаторных верхних границ размера списка при list recovery.

**Ограничение:** Декодирование при множестве допустимых символов в координате не есть инъективность 0/1/2-сумм, вес столбца ASET не ограничивается теми же параметрами.

**Идентичность:** `doi:10.1145/3798129.3800756` · **Авторы:** Joshua Brakensiek, Yeyuan Chen, Manik Dhar, Zihan Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-010](INDEX.md#ml-010)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-084
**[Locally Computable High Independence Hashing](https://doi.org/10.1145/3798129.3800855)** (2026)

Dodis–Lovett–Wichs: локально вычисляемые k-wise independent семейства хешей, включая неявные конструкции через lossless expanders.

**Ограничение:** Высокая k-wise независимость хеш-значений не тождественна линейной независимости столбцов или независимости от адаптивного противника.

**Идентичность:** `doi:10.1145/3798129.3800855` · **Авторы:** Yevgeniy Dodis, Shachar Lovett, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-091
**[Improved Pseudorandom Codes from Permuted Puzzles](https://doi.org/10.1145/3798129.3800916)** (2026)

Псевдослучайные коды с устойчивостью к редактированиям над бинарным алфавитом и ключ-известным атакам при обозначенных криптографических гипотезах.

**Ограничение:** Криптографическая неразличимость опирается на permuted puzzles conjecture; кодовая устойчивость к edit noise не равна точному ASET при малом числе ненулевых координат.

**Идентичность:** `doi:10.1145/3798129.3800916` · **Авторы:** Miranda Christ, Noah Golowich, Sam Gunn, Ankur Moitra, Daniel Wichs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [OM-122](INDEX.md#om-122)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-118
**[Lower bounds for adaptive locally decodable codes](https://doi.org/10.1002/rsa.20069)** (2005)

Классические нижние границы локального декодирования сообщений с адаптивными запросами к повреждённым кодовым словам.

**Ограничение:** Это read/query locality на шумных кодах, тогда как LENT-001 задаёт write/update locality; равенство понятий и автоматический перенос границ недопустимы.

**Идентичность:** `doi:10.1002/rsa.20069` · **Авторы:** Amit Deshpande, Rahul Jain, T. Kavitha, Satyanarayana V. Lokam, Jaikumar Radhakrishnan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-127
**[Locally Updatable and Locally Decodable Codes](https://doi.org/10.1007/978-3-642-54242-8_21)** (2014)

Chandran–Kanukurthi–Ostrovsky строят локально обновляемые и локально декодируемые коды в модели Prefix Hamming metric и исследуют приложения к динамическому доказательству хранения.

**Ограничение:** Одновременное ограничение числа записываемых/читаемых символов давно известно; ошибка декодирования, модель атакующего и условие префиксной метрики не совпадают с чистой Hamming-ball моделью UCT.

**Идентичность:** `doi:10.1007/978-3-642-54242-8_21` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-128
**[Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes](https://arxiv.org/abs/1305.3224)** (2013)

Mazumdar–Chandar–Wornell изучают компромисс скорости кода, локального восстановления и стоимости обновления при приближении к пропускной способности зашумленного канала.

**Ограничение:** Канальная capacity с шумом и требования восстановления не определяются одной безошибочной моделью графа изменений. Нужна явная редукция при переносе границ.

**Идентичность:** `arxiv:1305.3224` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-133
**[Tight upper and lower bounds for leakage-resilient, locally decodable and updatable non-malleable codes](https://doi.org/10.1016/j.ic.2019.05.001)** (2019)

Работа доказывает нижние и верхние ограничения локального декодирования/обновления криптографических кодов при недоверенном изменении и утечке информации.

**Ограничение:** Криптографическая немодифицируемость и leakage-resilience требуют другой adversary/security модели и не сводятся к доказательству безошибочной вместимости шаров Хэмминга.

**Идентичность:** `doi:10.1016/j.ic.2019.05.001` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-002](INDEX.md#ml-002)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-138
**[Improved bounds on the size of sparse parity check matrices](https://doi.org/10.1109/ISIT.2005.1523645)** (2005)

Naor и Verstraëte (IEEE ISIT 2005) исследуют экстремальное число разреженных столбцов, когда любые k из них линейно независимы, и выводят верхние границы редукцией к графам с запрещёнными циклами.

**Ограничение:** Результаты относятся к произвольным коэффициентам линейных зависимостей, а не к двум ограниченным по размеру подписанным суммам ASET. Точная формула показателя в HTML библиографическом abstract и авторском PDF форматируется различно; без проверки полного оригинала конкретную новую оценку при k=6,r=3 не утверждаем.

**Идентичность:** `doi:10.1109/ISIT.2005.1523645` · **Авторы:** Assaf Naor, Jacques Verstraëte · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)


## dynamic-data-structures
*Динамические структуры, каноничность и локальность правок*

### LIT-007
**[History-Independent Dynamic Partitioning: Operation-Order Privacy in Ordered Data Structures](https://doi.org/10.1145/3651609)** (2024)

Динамические группы размера Θ(B) с O(1) ожидаемым числом операций вставки/удаления против oblivious adversary.

**Ограничение:** Операции по группам не равны физически переписанным байтам; нельзя усиливать модель до adaptive adversary без доказательства.

**Идентичность:** `doi:10.1145/3651609` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-008
**[History-Independent Dynamic Partitioning with Applications to B-Trees, Skip Lists and Fusion Trees](https://doi.org/10.1145/3810240)** (2026)

Расширенная версия истории-независимого разбиения с применениями к B-tree, fusion tree и skip list.

**Ограничение:** Не утверждает строгую каноничность физических байтов persistent rope или худший случай против адаптивного противника.

**Идентичность:** `doi:10.1145/3810240` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-009
**[The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality](https://arxiv.org/abs/2509.11121)** (2025)

Предложены одновременные строгие гарантии длины CDC-чанков и локальности правок; обсуждается структурное представление Yarn.

**Ограничение:** Авторский preprint; модель частичных изменений, byte writes и deterministic canonical physical layout нужно сопоставлять отдельно.

**Идентичность:** `arxiv:2509.11121` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-011
**[Optimal Time-Space Tradeoff for Dynamic Difference-Encoded Dictionaries](https://arxiv.org/abs/2608.06077)** (2026)

Гарантии сжатого gap-encoded словаря с динамическими операциями и сопоставимой нижней границей.

**Ограничение:** Стоимость ориентируется на gap(S), а не на history-independent физическое расположение и на write locality после string edits.

**Идентичность:** `arxiv:2608.06077` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-012
**[Time-Optimal Construction of String Synchronizing Sets](https://doi.org/10.4230/LIPIcs.STACS.2026.36)** (2026)

Оптимальное по word-RAM времени построение позиций синхронизации с локальной согласованностью контекстов строки.

**Ограничение:** Результат для статической подготовки/конструкции, не готовая динамическая worst-case гарантия редактирования CDC.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.36` · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (cited)

### LIT-058
**[Dynamic Pattern Matching with Wildcards](https://doi.org/10.4230/LIPIcs.STACS.2026.68)** (2026)

Полностью динамическое сопоставление текста и шаблона с k wildcard: суб-линейная сложность при малом k и условный запрет части режимов через SETH.

**Ограничение:** Зависимость от количества wildcard и сильной экспоненциальной гипотезы — обязательная часть утверждения; не lower bound на обычную CDC сегментацию.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.68` · **Авторы:** Arshia Ataee Naeini, Amir-Parsa Mobed, Masoud Seddighin, Saeed Seddighin · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-072
**[The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843)** (2026)

Перенос natural-proofs barrier на статические и динамические cell-probe нижние границы через local и locally-updatable PRF при криптографических допущениях.

**Ограничение:** Барьер условен на существование конкретных PRF; не является доказательством отсутствия всех новых нижних границ и не переносится на физическую запись байтов.

**Идентичность:** `doi:10.1145/3798129.3800843` · **Авторы:** Michal Koucký, Bruno Loff, Tulasimohan Molli, Michael E. Saks · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-073
**[Compressing Dynamic Fully Indexable Dictionaries in Word-RAM](https://doi.org/10.1145/3798129.3800839)** (2026)

Domingues строит динамический rank/select словарь с near-information-theoretic пространством и худшим временем обновлений в Word-RAM.

**Ограничение:** Требует заданной модели предвычисленной таблицы и word multiplication; entropy redundancy не тождественен стоимости physical rewrites или history independence.

**Идентичность:** `doi:10.1145/3798129.3800839` · **Авторы:** Gabriel Marques Domingues · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-088
**[Sampling Permutations with Cell Probes Is Hard](https://doi.org/10.1145/3798129.3800743)** (2026)

Новые ограничения на выборку перестановок в модели cell probes связывают память, доступ к оракулу и сложность рандомизации.

**Ограничение:** Не доказывает сложность доступа к любой канонической сериализации или запрет на конкретный алгоритм random permutation.

**Идентичность:** `doi:10.1145/3798129.3800743` · **Авторы:** Yaroslav Alekseev, Mika Göös, Konstantin Myasnikov, Artur Riazanov, Dmitry Sokolov · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-099
**[Longest Common Extension of a Dynamic String in Parallel Constant Time](https://doi.org/10.4230/LIPIcs.CPM.2026.20)** (2026)

CPM 2026 строит динамическую иерархию string synchronizing sets и отвечает на LCE при вставке и удалении символов в параллельной модели.

**Ограничение:** CRCW PRAM, частично устаревшие сведения и LCE-запросы не эквивалентны строгой канонической CDC локальности и физической переписи чанков.

**Идентичность:** `doi:10.4230/LIPIcs.CPM.2026.20` · **Авторы:** Daniel Alexander Albert · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-111
**[The cell probe complexity of dynamic data structures](https://doi.org/10.1145/73007.73040)** (1989)

Fredman–Saks вводят динамические cell-probe нижние границы с учётом операций обновления и запросов и техники chronogram; исходный метод уже связывает количество обращений к ячейкам и динамическую память.

**Ограничение:** Cell-probe считывания/записи слов с параметром размера ячейки отличаются от числа изменённых q-ичных координат в UCT; новую общую границу только из переименования получить нельзя.

**Идентичность:** `doi:10.1145/73007.73040` · **Авторы:** Michael L. Fredman, Michael E. Saks · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-112
**[Logarithmic Lower Bounds in the Cell-Probe Model](https://doi.org/10.1137/S0097539705447256)** (2006)

Pătraşcu–Demaine доказывают амортизированные рандомизированные нижние оценки для динамических структур, включая partial sums и connectivity, а также компромиссы стоимости обновлений и запросов.

**Ограничение:** Не переносить асимптотику, word-size или распределение входов без совпадения модели; UCT-A обязан сравниваться с этими сильными известными границами.

**Идентичность:** `doi:10.1137/S0097539705447256` · **Авторы:** Mihai Pătraşcu, Erik D. Demaine · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-113
**[On the Cell Probe Complexity of Dynamic Membership](https://doi.org/10.1137/1.9781611973075.12)** (2010)

Yi–Zhang исследуют динамическую принадлежность в модели cell-probe со специальным бесплатным кэшем и границами на обновления при почти одношаговых запросах.

**Ограничение:** Бесплатный кэш и последовательности случайных операций требуют отдельного resource ledger; нельзя смешивать с детерминированными worst-case Hamming writes.

**Идентичность:** `doi:10.1137/1.9781611973075.12` · **Авторы:** Ke Yi, Qin Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-114
**[On dynamic bit-probe complexity](https://doi.org/10.1016/j.tcs.2007.02.058)** (2007)

Исследование нижних границ dynamic membership и partial sums в bit-probe модели и продолжение техник chronogram; максимально близко к счёту изменённых битов.

**Ограничение:** Запись в один бит памяти, чтение бита и изменение координаты абстрактного кода являются разными ресурсами, которые требуют явной редукции.

**Идентичность:** `doi:10.1016/j.tcs.2007.02.058` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-115
**[New amortized cell-probe lower bounds for dynamic problems](https://doi.org/10.1016/j.tcs.2019.01.043)** (2019)

Новые амортизированные cell-probe нижние границы для динамического вычисления полиномов и online matrix-vector multiplication; демонстрируется общий метод нижних оценок.

**Ограничение:** Теоремы привязаны к конкретным семействам задач и амортизированной модели; не распространяются автоматически на любую динамическую систему.

**Идентичность:** `doi:10.1016/j.tcs.2019.01.043` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-119
**[An $\Omega((\log n / \log\log n)^2)$ Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/)** (2026)

Young Kun Ko, ECCC TR26-047, редакция 7 октября 2026: основной Theorem 1.1 для Multiphase Problem / inner product над F₂ при m=n^{1+Ω(1)}, t_u=n^{o(1)} утверждает t_tot=Ω((log n/log(t_u w))²); доказательство использует 2.5-round communication game с проверкой симуляции.

**Ограничение:** Точная формулировка теоремы проверена по авторской PDF (стр. 3), но полное доказательство не перепроверено. w — размер cell-probe слова, не LENT write locality; m — число preprocessed vectors, не code dimension. Нельзя переносить теорему на произвольную Boolean функцию, динамический range parity или HYP-103 authenticated certificates.

**Идентичность:** `publisher:eccc:tr26-047` · **Авторы:** Young Kun Ko · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-123
**[Optimal Dynamic Strings](https://doi.org/10.1137/1.9781611975031.99)** (2018)

SODA 2018: поддержка операций make_string, concat, split, сравнения строк и LCP с логарифмическим временем обновления с высокой вероятностью; доказана нижняя граница на сумму динамических затрат в модели сравнения равенства строк.

**Ограничение:** Структура сравнивает/представляет редактируемые строки, но не обязана выдавать тождественно стандартный BLAKE3-256; её Omega(log n) не является BLAKE3 compression-oracle lower bound.

**Идентичность:** `doi:10.1137/1.9781611975031.99` · **Авторы:** Paweł Gawrychowski, Adam Karczmarz, Tomasz Kociumaka, Jakub Łącki, Piotr Sankowski · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-124
**[A textbook solution for dynamic strings](https://doi.org/10.1016/j.tcs.2026.115746)** (2026)

TCS 2026: FeST — упрощённая структура динамических строк на улучшенных splay trees с амортизированными логарифмическими обновлениями, сравнениями подстрок и расширениями операций.

**Ограничение:** Строковые отпечатки используются с вероятностной корректностью; они не являются каноническим BLAKE3 и не решают точную задачу позиционного счётчика чанков.

**Идентичность:** `doi:10.1016/j.tcs.2026.115746` · **Авторы:** Zsuzsanna Lipták, Francesco Masillo, Gonzalo Navarro · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-141
**[Bit-Probe Lower Bounds for Succinct Data Structures](https://doi.org/10.1137/090766619)** (2012)

Viola доказывает дополнительные к информационно-теоретическому минимуму биты памяти для статического компактного представления троичных массивов и множеств при малом числе bit probes, включая адаптивное чтение.

**Ограничение:** Статическая схема доступа и избыточности не даёт автоматически динамическую границу на число переписанных ячеек или на совместную стоимость обновлений, сертификатов и внешнего оракула.

**Идентичность:** `doi:10.1137/090766619` · **Авторы:** Emanuele Viola · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-003-G1-SOURCE-AND-GAP-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-003-G1-SOURCE-AND-GAP-AUDIT.md) (model_overlap)


## incremental-computation
*Инкрементальные вычисления и сертификаты*

### LIT-010
**[Incremental Computing by Differential Execution](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20)** (2025)

Дифференциальная семантика инкрементальных вычислений с формально проверенными свойствами корректности и оптимизациями циклов.

**Ограничение:** Корректность изменения вычисления не равна минимальной длине сертификата unchanged и lower bound на cell probes.

**Идентичность:** `doi:10.4230/LIPIcs.ECOOP.2025.20` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-013
**[Change actions: from incremental computation to discrete derivatives](https://arxiv.org/abs/2002.05256)** (2020)

Алгебраический аппарат change actions для композиционной семантики дискретных производных и инкрементальных запросов.

**Ограничение:** Общее правило композиции изменений не обеспечивает корректность объединения отдельно выданных сертификатов no-effect.

**Идентичность:** `arxiv:2002.05256` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-032
**[Bounded Incremental Computation](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/)** (1993)

Ramalingam исследует сложность инкрементального перерасчёта относительно размеров изменений ввода и вывода.

**Ограничение:** Сам output-sensitive cost не является новой нижней границей метаданных no-effect сертификата.

**Идентичность:** `publisher:msresearch:ramalingam:1993` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (cited)

### LIT-041
**[Certificates in Data Structures](https://arxiv.org/abs/1404.5743)** (2014)

Wang–Yin исследуют сертификаты ответов static cell-probe запросов и нижние границы на число прочитанных ячеек.

**Ограничение:** Сертификат в недетерминированной static query модели не равен runtime-maintained zero-effect сертификату для dynamic DAG.

**Идентичность:** `arxiv:1404.5743` · **Авторы:** Yaoyu Wang, Yitong Yin · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-045
**[Complexity models for incremental computation](https://doi.org/10.1016/0304-3975(94)90159-7)** (1994)

Miltersen–Subramanian–Vitter–Tamassia классифицируют incremental complexity и вводят критерии lower bounds для online re-evaluation.

**Ограничение:** Это model-level фундамент, а не автоматическая теорема об update cost или bytes rewritten в TOM/O01.

**Идентичность:** `doi:10.1016/0304-3975(94)90159-7` · **Авторы:** Peter Bro Miltersen, Sairam Subramanian, Jeffrey Scott Vitter, Roberto Tamassia · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-046
**[Lower And Upper Bounds For Incremental Algorithms](https://doi.org/10.7282/T3HT2SXD)** (1992)

Berman: relative incremental lower bound и δ-анализ для динамических update algorithms, включая обновление transitive closure.

**Ограничение:** Работа о сложностях в собственной модели; не устанавливает универсальное zero-effect certificate lower bound TOM.

**Идентичность:** `doi:10.7282/T3HT2SXD` · **Авторы:** A. Michael Berman · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-055
**[DeltaSort: Incremental Sorting of Arrays with Known Updates](https://doi.org/10.4230/LIPIcs.SEA.2026.18)** (2026)

Операция инкрементальной сортировки массива, когда известны k изменённых индексов; автор даёт O(n sqrt(k)) ожидаемого времени и O(k) дополнительной памяти.

**Ограничение:** Оценка дана для модели случайных обновлений; не обеспечивает worst-case O(n sqrt(k)), no-effect certificate или стабильный физический порядок битов.

**Идентичность:** `doi:10.4230/LIPIcs.SEA.2026.18` · **Авторы:** Shubham Dwivedi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-056
**[Incremental Submodular Maximization: Better Than Greedy](https://doi.org/10.4230/LIPIcs.ESA.2026.134)** (2026)

Алгоритм адаптивного масштабирования улучшает конкурентное отношение всех префиксов cardinality constraint до 1.373; установлена нижняя граница 1.25 для детерминированных алгоритмов.

**Ограничение:** Incremental здесь означает возрастающий бюджет оптимизации, а не поддержание произвольных изменяемых DAG и не худший случай побайтовых правок.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.134` · **Авторы:** Marcin Bienkowski, Joakim Blikstad, Jarosław Byrka, Martín Costa, Yann Disser, Annette Lutz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-113](INDEX.md#om-113)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-096
**[Incremental Computation with Names](https://arxiv.org/abs/1503.07792)** (2015)

Nominal Adapton использует именованные вычислительные узлы и доказывает согласованность результатов с полным пересчётом при изменении входов.

**Ограничение:** Известное переиспользование именованных узлов не устанавливает минимальный размер совместного сертификата для произвольных Boolean DAG и батчей.

**Идентичность:** `arxiv:1503.07792` · **Авторы:** Matthew A. Hammer, Jana Dunfield, Kyle Headley, Nicholas Labich, Jeffrey S. Foster, Michael Hicks, David Van Horn · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-102
**[Riker: Always-Correct and Fast Incremental Builds from Simple Specifications](https://www.usenix.org/conference/atc22/presentation/curtsinger)** (2022)

USENIX ATC 2022 автоматически отслеживает файловые зависимости при инкрементальной сборке и поддерживает корректность относительно полного построения.

**Ограничение:** Полная POSIX-модель зависимости не доказывает оптимальную сложность совместных Boolean DAG сертификатов и требует оплаты системных метаданных.

**Идентичность:** `usenix:atc22:curtsinger` · **Авторы:** Charlie Curtsinger, Daniel W. Barowy · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-103
**[Query Maintenance Under Batch Changes with Small-Depth Circuits](https://doi.org/10.4230/LIPIcs.MFCS.2024.46)** (2024)

MFCS 2024: поддержание запросов после пакетов изменений полилогарифмического размера с помощью малоглубинных схем и итеративных first-order обновлений; прямая граница для широкой идеи batch-DAG.

**Ограничение:** DynFO и глубина обновляющих схем не задают минимального количества старых битов, которые обязан прочитать проверяющий сертификат частичного входа.

**Идентичность:** `doi:10.4230/LIPIcs.MFCS.2024.46` · **Авторы:** Samir Datta, Asif Khan, Anish Mukherjee, Felix Tschirbs, Nils Vortmeier, Thomas Zeume · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-104
**[Parallel Batch-Dynamic Trees via Change Propagation](https://doi.org/10.4230/LIPIcs.ESA.2020.2)** (2020)

ESA 2020: эффективная пакетная динамика деревьев через change propagation, вычислительную дистанцию и анализ ожидаемой работы для k обновлений.

**Ограничение:** Сложность пакетного обновления дерева с запросами путей/поддеревьев не равна минимальному свидетельству результата произвольного Boolean DAG при известном старом корне.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2020.2` · **Авторы:** Umut A. Acar, Daniel Anderson, Guy E. Blelloch, Laxman Dhulipala, Sam Westrick · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-109
**[Incremental Cryptography: The Case of Hashing and Signing](https://doi.org/10.1007/3-540-48658-5_22)** (1994)

CRYPTO 1994: вводится криптографическая постановка инкрементального хеширования и подписания, допускающая обновление преобразования после небольших изменений документа.

**Ограничение:** Примитивы 1994 года не обязаны давать тот же результат, что стандартный BLAKE3; новая теорема должна различать безопасность нового хеша и точную совместимость хеша по байтам.

**Идентичность:** `doi:10.1007/3-540-48658-5_22` · **Авторы:** Mihir Bellare, Oded Goldreich, Shafi Goldwasser · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md) (model_overlap)

### LIT-110
**[A New Paradigm for Collision-Free Hashing: Incrementality at Reduced Cost](https://doi.org/10.1007/3-540-69053-0_13)** (1997)

EUROCRYPT 1997: конкретные инкрементальные конструкции устойчивого к коллизиям хеширования MuHASH, AdHASH и LtHASH, с отдельными алгебраическими допущениями.

**Ограничение:** Эти алгоритмы строят другие хеши и не вычисляют стандартный BLAKE3-256 без изменений; из их доказательств нельзя выводить границу времени вставки в BLAKE3.

**Идентичность:** `doi:10.1007/3-540-69053-0_13` · **Авторы:** Mihir Bellare, Daniele Micciancio · **Проверка:** `author_paper_or_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md) (model_overlap)

### LIT-117
**[A Library for Self-Adjusting Computation](https://doi.org/10.1016/j.entcs.2005.11.043)** (2006)

Библиотека самомодифицирующихся вычислений со ссылками и memoization, примеры change propagation и ускорение инкрементального пересчёта.

**Ограничение:** Из инженерных speedups и программных инвариантов не вытекает универсальная минимальная стоимость обновлений или общий сертификат без полной модели доступа.

**Идентичность:** `doi:10.1016/j.entcs.2005.11.043` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-125
**[The BLAKE3 Hashing Framework (C2SP v1.0.0)](https://c2sp.org/BLAKE3@v1.0.0)** (2024)

Нормативная криптографическая спецификация C2SP: BLAKE3 разбивает вход на 1024-байтовые чанки; каждый блок листа получает счётчик, равный индексу чанка, а родительские узлы используют нулевой счётчик и отдельные флаги.

**Ограничение:** Это техническая спецификация, НЕ новая рецензируемая научная статья и НЕ нижняя граница сложности инкрементального хеширования; особый ROOT-флаг требует отдельной модели переиспользования.

**Идентичность:** `publisher:c2sp:blake3-v1-0-0` · **Авторы:** Jean-Philippe Aumasson, Samuel Neves, Jack O'Connor, Zooko Wilcox-O'Hearn · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)

### LIT-129
**[Annotations in Data Streams](https://doi.org/10.1145/2636924)** (2014)

Chakrabarti–Cormode–McGregor–Thaler вводят схемы аннотированных потоков: недоверенный доказатель сообщает вспомогательную информацию, а ограниченный по памяти верификатор обязан проверить ответ.

**Ограничение:** Длина честной аннотации — необходимый информационный ресурс, но сама по себе она не обеспечивает soundness. Известные нелинейные компромиссы annotation/verification-space не следуют из простого произведения размеров кодов.

**Идентичность:** `doi:10.1145/2636924` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)

### LIT-130
**[Annotations for Sparse Data Streams](https://arxiv.org/abs/1304.3816)** (2013)

Chakrabarti–Cormode–Goyal–Thaler исследуют online Merlin–Arthur/annotated streaming с малым числом действительных обновлений и показывают границы между вариантами моделей доказателя.

**Ограничение:** Сохранённое состояние, момент публикации свидетельства, адаптивность и сообщение недоверенного доказателя должны иметь отдельные контракты и оценки.

**Идентичность:** `arxiv:1304.3816` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)


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

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)


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

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)

### LIT-029
**[Space lower bounds for linear prediction in the streaming model](https://arxiv.org/abs/1902.03498)** (2019)

Dagan–Kur–Shamir: квадратичная по размерности потребность в памяти для конкретных линейных streaming inference задач.

**Ограничение:** Это не универсальное cell-probe ограничение для сертификатов неизменности DAG.

**Идентичность:** `arxiv:1902.03498` · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-002-OM116-OM140-THEOREM-AUDIT.md) (cited)

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

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-101
**[Breaking the Quadratic Barrier: Robust Cardinality Sketches for Adaptive Queries](https://proceedings.mlr.press/v267/cohen25c.html)** (2025)

ICML 2025 даёт устойчивые оценки cardinality при адаптивных запросах в модели ограниченного повторного участия каждого элемента.

**Ограничение:** Гарантии bounded participation не переносятся автоматически на DeltaMeter one-sided parity estimator, keyed-PRF transcript и произвольные изменяемые множества.

**Идентичность:** `publisher:pmlr:cohen25c` · **Авторы:** Edith Cohen, Mihir Singhal, Uri Stemmer · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-003](INDEX.md#dm-003), [DM-007](INDEX.md#dm-007), [DM-004](INDEX.md#dm-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-132
**[Arthur–Merlin streaming complexity](https://doi.org/10.1016/j.ic.2014.12.011)** (2015)

Исследование моделей Arthur–Merlin для потоковой проверки, включая компромиссы длины доказательства и оперативной памяти и ограничения для Distinct Elements.

**Ограничение:** Статистическая полнота/корректность интерактивного доказательства отличается от финитной гарантии точной оценки множества; нельзя подменять одно другим.

**Идентичность:** `doi:10.1016/j.ic.2014.12.011` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [DM-001](INDEX.md#dm-001), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)


## compressed-indexing
*Сжатые структуры, индексация строк и нижние границы*

### LIT-050
**[Dynamic Grammar-Compressed Self-Index in δ-Optimal Space](https://doi.org/10.4230/LIPIcs.ESA.2026.6)** (2026)

Динамический RR-index хранит повторяющиеся строки в сжатом виде, поддерживая вставки, удаления и поиск без полной распаковки; оценка объёма через δ-complexity.

**Ограничение:** Ожидаемые и амортизированные гарантии относятся к строковому индексу и locate-запросам; не означают постоянную стоимость переписывания байтов или CDC-локальность.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.6` · **Авторы:** Takaaki Nishimoto, Yasuo Tabei · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-051
**[Hardness of Frequency-Related Queries on Compressed Strings](https://doi.org/10.4230/LIPIcs.ESA.2026.143)** (2026)

Исследуются условные ограничения вычисления rank/frequency-подобных запросов по grammar/LZ-компрессированным строкам без развёртывания.

**Ограничение:** Модель сжатого индекса и условные lower bounds не являются нижними границами для exact ASET или произвольной инкрементальной метрики.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.143` · **Авторы:** Rajat De, Dominik Kempa · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-119](INDEX.md#om-119)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-052
**[OptFSST: Optimized FSST String Compression](https://arxiv.org/abs/2607.11271)** (2026)

Оптимальное динамическое программирование кодирования при фиксированной таблице символов FSST и NP-трудность обобщённого выбора таблицы; сохраняется независимая распаковка строк.

**Ограничение:** Оптимальность доказана при фиксированном словаре, а не для совместного поиска словаря; сравнение на 92 наборах — авторский эксперимент, не бенчмарк ChunkShift.

**Идентичность:** `arxiv:2607.11271` · **Авторы:** Hedi Chehaidar, Mihail Stoian, Moritz Stargalla, Andreas Kipf · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DM-014](INDEX.md#dm-014), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-053
**[Relative Compressed Reverse Suffix Array](https://doi.org/10.4230/LIPIcs.STACS.2026.62)** (2026)

Короткое относительное кодирование суффиксного массива обращённого текста, если уже имеется FM-index исходного текста; изучается стоимость доступа.

**Ограничение:** Это относительное индексирование структур и суффиксных массивов, не универсальный delta patch codec и не гарантия байтовой экономии.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.62` · **Авторы:** Muhammed Oguzhan Kulekci, Mano Prakash Parthasarathi, Rahul Shah, Sharma V. Thankachan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-054
**[Efficient Compression in Semigroups](https://doi.org/10.4230/LIPIcs.STACS.2026.80)** (2026)

Классификация классов конечных полугрупп, допускающих эффективное представление straight-line programs, и улучшения границ длины/ширины программ.

**Ограничение:** Семигрупповая algebraic compression и запросы Cayley table не эквивалентны сжатию файлов, кодекам дельт или инкрементальным сертификатам.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.80` · **Авторы:** Alexander Thumm, Armin Weiß · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-119](INDEX.md#om-119)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-126
**[Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts](https://doi.org/10.1007/s00224-026-10266-x)** (2026)

Theory of Computing Systems 2026: алгоритм IPM-запросов на грамматически сжатых и динамических строках за O(log n), применимый к fully persistent динамическим структурам; опубликован proof-of-concept Rust.

**Ограничение:** IPM-запросы и структурные представления подстрок не тождественны вычислению стандартного BLAKE3 digest после каждого редактирования, и нижние границы IPM не переносятся автоматически.

**Идентичность:** `doi:10.1007/s00224-026-10266-x` · **Авторы:** Anouk Duyster, Tomasz Kociumaka · **Проверка:** `publisher_full_text_spotchecked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md) (model_overlap)


## online-optimization
*Онлайн-оптимизация, конкурентные оценки и барьеры*

### LIT-057
**[Online and Incremental Fractional Vertex Cover on Trees](https://doi.org/10.4230/LIPIcs.ESA.2026.158)** (2026)

На деревьях получены competitive bounds 11/6 в online edge-arrival и 3/2 (с matching lower bound) для инкрементальной модели с известными обновлениями.

**Ограничение:** Вторая модель допускает знание всех будущих обновлений заранее; не переносить offline bound на online или на невозрастающие/удаляемые данные.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.158` · **Авторы:** Júlia Baligács, Bartłomiej Bosek, Yann Disser, Andreas Emil Feldmann, Grzegorz Gutowski, Katarzyna Kępińska, Paweł Putra, Anna Zych-Pawlewicz · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-069
**[Lower Bounds for Ranking-Based Pivot Rules](https://doi.org/10.4230/LIPIcs.STACS.2026.31)** (2026)

Единый rank-information framework даёт superpolynomial lower bounds для классов strategy-improvement rules и subexponential bounds для policy iteration.

**Ограничение:** Ограничения доказаны для заданных ranking-based pivot rules и MDP/games; не доказывают невозможность всех динамических алгоритмов или произвольного Rust примитива.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.31` · **Авторы:** Yann Disser, Georg Loho, Matthew Maat, Nils Mosis · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-137](INDEX.md#om-137)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-097
**[Bigtable Merge Compaction](https://arxiv.org/abs/1407.3008)** (2014)

Формализует онлайновое объединение файлов Bigtable и конкурентную оценку политик компактации; предшествует гипотезе HYP-104 о pack rewrite.

**Ограничение:** Непосредственная модель не включает совместное хранение объектов и матрицу принадлежности одновременно закреплённых snapshots; год соответствует первой версии arXiv.

**Идентичность:** `arxiv:1407.3008` · **Авторы:** Claire Mathieu, Carl Staelin, Neal E. Young, Arman Yousefi · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)

### LIT-098
**[Competitive Data-Structure Dynamization](https://arxiv.org/abs/2011.02615)** (2020)

Онлайн-задачи обновления наборов данных с оплачиваемыми build/query затратами и конкурентными гарантиями при неравномерных потоках.

**Ограничение:** Онлайновые set-cover/merge модели нельзя напрямую приравнивать к immutable packs с shared snapshot pins и crash/GC semantics.

**Идентичность:** `arxiv:2011.02615` · **Авторы:** Claire Mathieu, Rajmohan Rajaraman, Neal E. Young, Arman Yousefi · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md) (model_overlap)


## graph-algorithms
*Динамические графы, гиперграфы и sparsification*

### LIT-059
**[Fully Dynamic Spectral Sparsification for Directed Hypergraphs](https://doi.org/10.4230/LIPIcs.STACS.2026.38)** (2026)

Поддержание спектрального sparsifier ориентированного гиперграфа под вставкой/удалением ребра и batch-dynamic работе с контролируемой амортизированной сложностью.

**Ограничение:** Спектральная ε-аппроксимация квадратичных форм не означает точного восстановления аддитивных множеств или ASET-коллизий.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.38` · **Авторы:** Sebastian Forster, Gramoz Goranci, Ali Momeni · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-076
**[Incremental Shortest Paths in Almost Linear Time via a Modified Interior Point Method](https://doi.org/10.1145/3798129.3800733)** (2026)

Детерминированно поддерживаются приближённые односточечные кратчайшие пути при вставке рёбер, суммарно близко к линейному времени.

**Ограничение:** Алгоритм работает с ориентированными взвешенными графами и аппроксимацией расстояния; не сертификат отсутствия эффекта произвольной правки DAG.

**Идентичность:** `doi:10.1145/3798129.3800733` · **Авторы:** Yang P. Liu · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-078
**[Separator Theorem for Minor-Free Graphs in Linear Time](https://doi.org/10.1145/3798129.3800727)** (2026)

Найден линейно-временной алгоритм сбалансированного O(√n)-сепаратора в графах без фиксированного минора.

**Ограничение:** Алгоритм статический и зависит от фиксированного запрещённого минора; нельзя приписывать ему поддержку динамической графовой разметки за O(1).

**Идентичность:** `doi:10.1145/3798129.3800727` · **Авторы:** Édouard Bonnet, Tuukka Korhonen, Hung Le, Jason Li, Tomáš Masařík · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-079
**[A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://doi.org/10.1145/3798129.3800868)** (2026)

Chuzhoy–Khanna–Song: детерминированное поддержание максимального matching в полностью динамическом графе с амортизированным временем n^(1/2+o(1)).

**Ограничение:** Maximal не означает maximum; амортизированная bound не худшая на операцию и не переносится на graph refinement без модели.

**Идентичность:** `doi:10.1145/3798129.3800868` · **Авторы:** Julia Chuzhoy, Sanjeev Khanna, Junkai Song · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-131](INDEX.md#om-131), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-085
**[Dynamic Set Cover with Worst-Case Recourse](https://doi.org/10.4230/LIPIcs.ICALP.2026.153)** (2026)

Solomon–Uzrad изучают динамическое покрытие множеств и контролируют число замен в решении на каждом обновлении.

**Ограничение:** Recourse решений не эквивалентен количеству переписанных байт памяти; конечные worst-case bounds применимы к собственной динамической set-cover модели.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.153` · **Авторы:** Shay Solomon, Amitai Uzrad · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.153) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-086
**[Static to Dynamic Correlation Clustering](https://doi.org/10.4230/LIPIcs.ICALP.2026.48)** (2026)

Преобразование статической аппроксимации корреляционного кластеринга в полностью динамическую с O(1) worst-case update в заявленной модели.

**Ограничение:** Гарантия качества сохраняется с указанной вероятностью; это не точное поддержание всех кластеров и не универсальная динамическая оптимизация.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.48` · **Авторы:** Nairen Cao, Vincent Cohen-Addad, Euiwoong Lee, Shi Li, David Rasmussen Lolck, Alantha Newman, Mikkel Thorup, Lukas Vogl, Shuyi Yan, Hanwen Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.48) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-094
**[Deterministic Padded Decompositions and Negative-Weight Shortest Paths](https://doi.org/10.1145/3798129.3800722)** (2026)

Jason Li строит детерминированные padded decompositions ориентированных графов и почти линейный negative-weight SSSP.

**Ограничение:** Статический SSSP с отрицательными рёбрами не даёт incremental support или гарантий размера delta patch.

**Идентичность:** `doi:10.1145/3798129.3800722` · **Авторы:** Jason Li · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [OM-133](INDEX.md#om-133)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-OPPORTUNITY-MAP.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-OPPORTUNITY-MAP.md) (model_overlap)

### LIT-120
**[On cubical graphs](https://doi.org/10.1016/0095-8956(75)90067-2)** (1975)

Garey–Graham исследуют графы, представимые подграфами двоичного гиперкуба, и критически невкладываемые графы — классический prior art для UCT-A.

**Ограничение:** Обычное реберное вложение не является новой теорией локальности; требуются дополнительные строго оплачиваемые ресурсы и корректная структура наблюдений.

**Идентичность:** `doi:10.1016/0095-8956(75)90067-2` · **Авторы:** M. R. Garey, R. L. Graham · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-121
**[The complexity of cubical graphs](https://doi.org/10.1016/S0019-9958(85)80012-7)** (1985)

Работа устанавливает NP-полноту распознавания графов, вкладываемых в некоторый двоичный гиперкуб, и изучает минимальную размерность для специальных классов.

**Ограничение:** Новая универсальная теорема о простой решаемости гиперкубного вложения противоречила бы установленной сложности без усиленных ограничений модели.

**Идентичность:** `doi:10.1016/S0019-9958(85)80012-7` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)

### LIT-122
**[Embeddings in hypercubes](https://doi.org/10.1016/0895-7177(88)90486-4)** (1988)

Livingston–Stout систематизируют результаты о вложениях графов в гиперкубы, дилатации, расширении, деревьях, решётках и сложности embedding.

**Ограничение:** Нельзя заявлять впервые найденные locality/dilation tradeoffs без полного сравнения с классической теорией cubical graphs; isometric partial cubes — более сильная отдельная модель.

**Идентичность:** `doi:10.1016/0895-7177(88)90486-4` · **Авторы:** Marilynn Livingston, Quentin F. Stout · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-001](INDEX.md#ml-001), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-001-PRIMARY-SOURCES.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-001-PRIMARY-SOURCES.md) (model_overlap)


## algebraic-algorithms
*Алгебраические алгоритмы, subset sum и разреженные матрицы*

### LIT-060
**[Robustifying Sparse Matrix Multiplication](https://doi.org/10.4230/LIPIcs.ESA.2026.157)** (2026)

Чёрноящичная редукция robust top-k sparse matrix multiplication к обычному sparse multiplication с polylog overhead и учётом output sparsity.

**Ограничение:** Робастное приближение крупнейших элементов матрицы — не точное GF(q) ASET-суммирование; knapsack-составляющая не делает алгоритм DeltaMeter backend.

**Идентичность:** `doi:10.4230/LIPIcs.ESA.2026.157` · **Авторы:** Karl Bringmann, Nick Fischer, Vasileios Nakos · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) (model_overlap)

### LIT-061
**[Improving Lagarias-Odlyzko Algorithm for Average-Case Subset Sum: Modular Arithmetic Approach](https://doi.org/10.4230/LIPIcs.STACS.2026.57)** (2026)

Модульная арифметика используется в улучшении алгоритмов средней сложности subset sum на базе lattice reduction.

**Ограничение:** Average-case integer subset sum с распределительными условиями не эквивалентен детерминированному точному GF(q) декодированию bounded active IDs.

**Идентичность:** `doi:10.4230/LIPIcs.STACS.2026.57` · **Авторы:** Antoine Joux, Karol Węgrzycki · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-007](INDEX.md#ml-007), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-135
**[Extremal graphs with no C4's, C6's, or C10's](https://doi.org/10.1016/0095-8956(91)90097-4)** (1991)

Wenger (JCTB 1991) строит плотные графы с запрещёнными циклами C4, C6 и C10; классическая экстремальная основа для оценки числа вес-2 столбцов с различимыми трёхэлементными суммами.

**Ограничение:** Из графа без коротких циклов следует хорошая матрица инцидентности только после определения ориентированных весов, поля и интерпретации циклических зависимостей; общая новая теорема ASET не заявляется.

**Идентичность:** `doi:10.1016/0095-8956(91)90097-4` · **Авторы:** Rephael Wenger · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G1-W2D3-GIRTH8.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G1-W2D3-GIRTH8.md) (model_overlap)

### LIT-136
**[An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8](https://arxiv.org/abs/1111.3279)** (2011)

Abreu, Araujo-Pardo, Balbuena, Labbate (2011) дают явные формулы для (s+1,8)-клеток, графов инцидентности обобщённых четырёхугольников. Их число рёбер Θ(m^{4/3}) обеспечивает известную нижнюю конструкцию шестикратно независимых двухразреженных столбцов.

**Ограничение:** Геометрический порядок s и размер конечного поля q коэффициентов различны; конечные графы не доказывают без дополнительных доводов всю асимптотику, а теорема с d=3 является производным классическим следствием.

**Идентичность:** `arxiv:1111.3279` · **Авторы:** Marién Abreu, Gabriela Araujo-Pardo, Camino Balbuena, Domenico Labbate · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G1-W2D3-GIRTH8.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G1-W2D3-GIRTH8.md) (model_overlap)

### LIT-137
**[Constructing dense grid-free linear 3-graphs](https://doi.org/10.1090/proc/15673)** (2022)

Gishboliner и Shapira (Proc. AMS 2022) доказывают существование линейных 3-однородных гиперграфов с Ω(m²) рёбрами без конфигурации 3×3 grid. Через точную эквивалентность unit-incidence ASET для характеристики поля ≥5 получается A_set(q,m,3,3)=Θ_q(m²).

**Ограничение:** Графы без grid не обязательно имеют линейную независимость любых шести столбцов; квадратичная ёмкость ASET не подтверждает неограниченный разрыв A_set/A_lin и не применима автоматически в характеристиках 2 или 3.

**Идентичность:** `doi:10.1090/proc/15673` · **Авторы:** Lior Gishboliner, Asaf Shapira · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-139
**[The Brown-Erdős-Sós conjecture in dense triple systems](https://arxiv.org/abs/2508.09841)** (2025)

Santos и Tyomkyn (авторский препринт 2025) устанавливают заявленный частный случай Brown–Erdős–Sós для линейных тройных систем высокой плотности δ>4/5; исследование сопряжено с (9,6)-конфигурациями.

**Ограничение:** Экстремальные (9,6) конфигурации не тождественны grid и не гарантируют ненулевую линейную зависимость произвольных шести столбцов. Предположение о пороге высокой плотности не является общим o(m²) верхним пределом при каждом δ>0.

**Идентичность:** `arxiv:2508.09841` · **Авторы:** Giovanne Santos, Mykhaylo Tyomkyn · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-140
**[Triangle-Free Triple Systems](https://doi.org/10.37236/14115)** (2026)

Frankl, Füredi, Goorevitch, Holzman и Simonyi (Electronic Journal of Combinatorics, май 2026) классифицируют экстремальные ограничения комбинаций четырёх типов треугольников в 3-однородных гиперграфах, включая точные/асимптотические случаи.

**Ограничение:** Ограничения треугольников гиперграфов не равнозначны запрету двух трёхэлементных аддитивных сумм или шестикратной линейной зависимости; не переносить показатели без структурного доказательства.

**Идентичность:** `doi:10.37236/14115` · **Авторы:** Peter Frankl, Zoltán Füredi, Ido Goorevitch, Ron Holzman, Gábor Simonyi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md) (model_overlap)

### LIT-142
**[Grid-free linear hypergraphs via Cayley-Bacharach](https://arxiv.org/abs/2602.14716)** (2026)

Pohoata (февраль 2026) строит для каждого r≥3 линейные r-однородные гиперграфы с Θ_r(m²) рёбрами без r×r grid, используя Cayley–Bacharach. Этот первоисточник закрывает широкое заявление об оригинальности dense grid-free конструкций для r≥4.

**Ограничение:** При r=4 запрещённый grid состоит из 8 рёбер, тогда как d=3 допускает коллизии уже среди максимум 6 рёбер. Линейная r-однородная модель имеет лишь O_r(m²) рёбер и не даёт актуальной полной ASET lower Ω(m^(12/5)). Препринт не является автоматически рецензируемой статьёй.

**Идентичность:** `arxiv:2602.14716` · **Авторы:** Cosmin Pohoata · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-143
**[The linear Turán number of small triple systems or why is the wicket interesting?](https://doi.org/10.1016/j.disc.2022.113025)** (2022)

Gyárfás–Sárközy (Discrete Mathematics, 2022) анализируют линейные Turán-числа небольших 3-однородных конфигураций и особую роль 5-рёберного wicket.

**Ограничение:** Wicket состоит из пяти рёбер на девяти вершинах; GF(3) локальный signed-set obstruction имеет пять рёбер на семи вершинах. Приписывать wicket-free o(m²) результат иной конфигурации без доказанного содержания неправомерно.

**Идентичность:** `doi:10.1016/j.disc.2022.113025` · **Авторы:** András Gyárfás, Gábor N. Sárközy · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)

### LIT-144
**[Wickets in 3-uniform hypergraphs](https://doi.org/10.1016/j.disc.2024.114029)** (2024)

Solymosi (Discrete Mathematics, 2024) доказывает, что линейные 3-гиперграфы без wicket имеют o(m²) рёбер, разрешая вопрос Gyárfás–Sárközy о разреженности такой запрещённой конфигурации.

**Ограничение:** Не переносить результат об отсутствии wicket на 7-вершинную 5-рёберную характеристика-3 зависимость, и тем более на произвольные взвешенные q-арные ASET-семейства. Содержательная редукция между запретами отсутствует.

**Идентичность:** `doi:10.1016/j.disc.2024.114029` · **Авторы:** József Solymosi · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-004](INDEX.md#ml-004), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-105-G4-CHARACTERISTIC-W4.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-105-G4-CHARACTERISTIC-W4.md) (model_overlap)


## proof-certification
*Машинные доказательства, сертификаты и верификация*

### LIT-062
**[Formalization of a Proof Calculus for Incremental Linearization for Satisfiability Modulo Nonlinear Arithmetic and Transcendental Functions](https://doi.org/10.1145/3779031.3779111)** (2026)

CPP 2026: Lean формализация proof calculus cvc5 для инкрементальной линеаризации SMT нелинейной/трансцендентной арифметики; восстановление проверяемых доказательств.

**Ограничение:** Soundness формализованного calculus не делает SMT поиск полным; к нашим GF(q) и DRAT-протоколам перенос возможен только через отдельный verified encoding.

**Идентичность:** `doi:10.1145/3779031.3779111` · **Авторы:** Tomaz Mascarenhas, Harun Khan, Abdalrhman Mohamed, Andrew Reynolds, Haniel Barbosa, Clark W. Barrett, Cesare Tinelli · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006), [OM-116](INDEX.md#om-116)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-063
**[PBLean: Pseudo-Boolean Proof Certificates for Lean 4](https://arxiv.org/abs/2602.08692)** (2026)

Проверяющий VeriPB proof-certificate через отражение в Lean с доказанной корректностью и проверенными переводами комбинаторных задач; поддерживает cutting planes.

**Ограничение:** PB сертификаты не равны DRAT; принятие proof log без формально проверенной кодировки исходной ASET модели не даёт end-to-end теоремы.

**Идентичность:** `arxiv:2602.08692` · **Авторы:** Stefan Szeider · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-003](INDEX.md#ml-003), [ML-008](INDEX.md#ml-008), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-064
**[Certificate-Carrying Transformation of Event-Driven Block Programs](https://arxiv.org/abs/2607.00563)** (2026)

Недоверенный оптимизатор программ Scratch выдаёт предлагаемое преобразование, а отдельный fail-closed checker пересчитывает семантические условия; ключевая лемма механизирована в Lean.

**Ограничение:** Доказательство привязано к явной модели наблюдения и cooperative scheduling; не доказывает точность сертификатов произвольного кэша или DAG.

**Идентичность:** `arxiv:2607.00563` · **Авторы:** Yuan Si, Jialu Zhang · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-065
**[Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4](https://arxiv.org/abs/2606.09600)** (2026)

Формализация covering-code в Lean с проверяемыми сертификатами верхних, нижних и точных covering numbers, сферическими bound и композиционными правилами.

**Ограничение:** Covering codes задают покрытие шаров Хэмминга, а не точность sparse subset sums; машинно проверенная база автора не проверена Mathlab CI.

**Идентичность:** `arxiv:2606.09600` · **Авторы:** Andreas Florath · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-002](INDEX.md#ml-002), [ML-003](INDEX.md#ml-003), [ML-011](INDEX.md#ml-011)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-002-B-QUADRATIC-THEOREM.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-002-B-QUADRATIC-THEOREM.md) (model_overlap)

### LIT-066
**[Mechanized Dominator Tree Certification](https://doi.org/10.1145/3779031.3779107)** (2026)

Проверяемый Rocq сертификат для быстрого вычисления dominator tree в CFG на базе критериев Georgiadis–Tarjan, интегрированный в CompCertSSA.

**Ограничение:** Проверяется доминирование потока управления, а не целостность storage/CDC или произвольная корректность incremental recomputation; важно разделение solver/checker.

**Идентичность:** `doi:10.1145/3779031.3779107` · **Авторы:** Jean-Christophe Léchenet · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-067
**[Towards Composable Proofs of Cache Coherence Protocols](https://doi.org/10.1145/3779031.3779106)** (2026)

Композitional MSI verification в Lean 4 через локальные инварианты MI/SI вместо одного сложного глобального доказательства.

**Ограничение:** Локальные инварианты зависят от formal model cache coherence; они не являются готовыми независимыми сертификатами immutable chunk packs или optimistic concurrency.

**Идентичность:** `doi:10.1145/3779031.3779106` · **Авторы:** Martina Camaioni, Yann Herklotz, Tz-Ching Yu, Thomas Bourgeat · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-068
**[Model-Generic Incrementally Verifiable Computation from Updatable BARGs](https://doi.org/10.4230/LIPIcs.ITCS.2026.6)** (2026)

Криптографическая IVC модель позволяет инкрементально обновлять проверяемое свидетельство длинных вычислений и переносит построение на distributed/online computation.

**Ограничение:** Криптографическая computational soundness и допущения BARG не равны безусловным exact lower bounds для TOM или локального сертификата без криптографии.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2026.6` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/TOM-001-B-PRIOR-ART-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/TOM-001-B-PRIOR-ART-AUDIT.md) (model_overlap)

### LIT-105
**[Instance Complexity and Unlabeled Certificates in the Decision Tree Model](https://doi.org/10.4230/LIPIcs.ITCS.2020.56)** (2020)

ITCS 2020: instance-optimal алгоритмы сравниваются с конкурентами, знающими сертификат; отдельно изучаются немаркированные сертификаты и симметрии.

**Ограничение:** Instance-optimal decision-tree модель не равна удостоверению нового значения DAG при пакете overwrites; перенесено только понятие сложности сертификата, не результаты конкретных теорем.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2020.56` · **Авторы:** Tomer Grossman, Ilan Komargodski, Moni Naor · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-005](INDEX.md#ml-005), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-131
**[New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification](https://doi.org/10.4230/LIPIcs.ITCS.2024.53)** (2024)

Ghosh–Shah доказывают сильные границы и разделения для нетривиальных online Merlin–Arthur коммуникационных протоколов и аннотированных потоковых графовых задач.

**Ограничение:** Наличие доказателя не гарантирует выигрыш относительно прямой передачи: некоторые нетривиальные протоколы значительно дороже простых. Дополнительная проверка soundness обязательна.

**Идентичность:** `doi:10.4230/LIPIcs.ITCS.2024.53` · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)


## proof-complexity
*Нижние границы доказательств, IPS/PIT и сертификаты*

### LIT-070
**[Lower Bounds against the Ideal Proof System in Finite Fields](https://doi.org/10.1145/3798129.3800721)** (2026)

Elbaz и соавторы доказывают нижние границы для фрагментов IPS над конечными полями постоянного размера; конструкция knapsack и связи с AC0[p]-Frege.

**Ограничение:** Границы относятся к определённым классам алгебраических опровержений и глубин схем, а не к сложности всех DRAT-протоколов или ASET.

**Идентичность:** `doi:10.1145/3798129.3800721` · **Авторы:** Tal Elbaz, Nashlen Govindasamy, Jiaqi Lu, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-071
**[The Weak Rank Principle: Lower Bounds and Applications](https://doi.org/10.1145/3798129.3800735)** (2026)

Новые экспоненциальные нижние границы PCR над F2 для слабого rank principle и построение proof-complexity generators.

**Ограничение:** Алгебраические формулы XY=A и доказательства несостоятельности — не сертификат минимальной ёмкости конкретного ASET и не скорость SAT-решателя.

**Идентичность:** `doi:10.1145/3798129.3800735` · **Авторы:** Michal Garlík, Svyatoslav Gryaznov, Hanlin Ren, Iddo Tzameret · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-080
**[Polynomial Identity Testing and the Ideal Proof System: PIT Is in NP If and Only If IPS Can Be p-Simulated by a Cook-Reckhow Proof System](https://doi.org/10.1145/3798129.3800865)** (2026)

Grochow показывает эквивалентность эффективной детерминированной верифицируемости IPS при p-симуляции и включения PIT в NP (с оговорками о поле).

**Ограничение:** Не утверждается PIT∈NP и не предоставляется готовый детерминированный checker для произвольных полиномиальных схем.

**Идентичность:** `doi:10.1145/3798129.3800865` · **Авторы:** Joshua A. Grochow · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-090
**[Lower Bounds for Near-Quadratic-Depth Resolution over Parities](https://doi.org/10.1145/3798129.3800809)** (2026)

Экспоненциальные нижние границы длины refutation в Res(⊕) при глубине O(N^(2−ε)) для специальных Tseitin/CNF конструкций.

**Ограничение:** Доказательствo для глубинно ограниченного Res(⊕) не ограничивает произвольный SAT/DRAT checker и не доказывает трудность GF(5) ASET.

**Идентичность:** `doi:10.1145/3798129.3800809` · **Авторы:** Sreejata Kishor Bhattacharya, Farzan Byramji, Arkadev Chattopadhyay, Russell Impagliazzo · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-007](INDEX.md#ml-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-106
**[Certification complexity of Boolean functions](https://eccc.weizmann.ac.il/report/2026/206/)** (2026)

Сентябрь 2026, ECCC TR26-206: операционная сложность сертификации Boolean функций, характеристики классической/рандомизированной/квантовой сертификатной сложности и новые квантовые нижние границы.

**Ограничение:** Авторский отчёт не утверждает оптимальное доказательство для инкрементального batch-DAG обновления; результаты по квантовой сложности нельзя автоматически переносить на old-root read-probe модель.

**Идентичность:** `publisher:eccc:tr26-206` · **Авторы:** Chandrima Kayal, Sophie Laplante, Émile Larroque, Krisjanis Prusis, Jevgenijs Vihrovs · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-107
**[On Condensation of Block Sensitivity, Certificate Complexity and the $\mathsf{AND}$ (and $\mathsf{OR}$) Decision Tree Complexity](https://arxiv.org/abs/2602.01042)** (2026)

Препринт 2026 v2: доказаны ограничения конденсации block sensitivity, certificate complexity и AND/OR decision trees при ограничениях переменных.

**Ограничение:** Заявление касается операций restriction/condensation, а не минимального shared batch certificate; версия v2 явно исключила доказательство из первой версии — цитировать только v2.

**Идентичность:** `arxiv:2602.01042` · **Авторы:** Sai Soumya Nalli, Karthikeya Polisetty, Jayalal Sarma · **Проверка:** `primary_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)

### LIT-108
**[Complexity measures and decision tree complexity: a survey](https://doi.org/10.1016/S0304-3975(01)00144-X)** (2002)

Классический обзор связи certificate complexity, sensitivity, block sensitivity, степени Boolean функций и decision-tree query complexity; математический прототип нового HYP-103 сертификата.

**Ограничение:** Обзор не является новым доказательством специфического обещания old root + batch overwrite; позволяет классифицировать базовую модель как стандартную certificate complexity.

**Идентичность:** `doi:10.1016/S0304-3975(01)00144-X` · **Авторы:** Harry Buhrman, Ronald de Wolf · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [ML-006](INDEX.md#ml-006)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md) (model_overlap)


## algebraic-complexity
*Алгебраические схемы, математика и нижние границы*

### LIT-077
**[Closure under Factorization from a Result of Furstenberg](https://doi.org/10.1145/3798129.3800738)** (2026)

Из классической формулы Фюрстенберга выводится замкнутость формул и constant-depth алгебраических схем относительно множителей над полями характеристики ноль.

**Ограничение:** Результат не распространяется автоматически на малую положительную характеристику, noncommutative models и произвольные PIT black-box инструкции.

**Идентичность:** `doi:10.1145/3798129.3800738` · **Авторы:** Somnath Bhattacharjee, Mrinal Kumar, Shanthanu S. Rai, Varun Ramanathan, Ramprasad Saptharishi, Shubhangi Saraf · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [OM-135](INDEX.md#om-135)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-089
**[Superquadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://doi.org/10.1145/3798129.3800802)** (2026)

Chen–Tal–Wang устанавливают сверхквадратичные нижние границы размера схем глубины два с линейными threshold gates.

**Ограничение:** Предел схем глубины 2 не становится автоматически пределом общего вычисления, Fourier трансформов или динамических алгоритмов.

**Идентичность:** `doi:10.1145/3798129.3800802` · **Авторы:** Lijie Chen, Avishay Tal, Yichuan Wang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-130](INDEX.md#om-130), [OM-132](INDEX.md#om-132)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-093
**[Classifying Identities: Subcubic Distributivity Checking and Hardness from Arithmetic Progression Detection](https://doi.org/10.1145/3798129.3800854)** (2026)

Алгебраические тождества конечных операций классифицированы по complexity проверки; distributivity за O(|S|^ω) и условные tight lower bounds.

**Ограничение:** Условные reductions из triangle detection/AP detection не дают безусловного lower bound для любой конечной GF(q) арифметики или проверки Rust crate.

**Идентичность:** `doi:10.1145/3798129.3800854` · **Авторы:** Bartłomiej Dudek, Nick Fischer, Geri Gokaj, Ce Jin, Marvin Künnemann, Xiao Mao, Mirza Redžić · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-116](INDEX.md#om-116), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-095
**[Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width](https://doi.org/10.4230/LIPIcs.ICALP.2026.130)** (2026)

Kluk–Nederlof: нижние границы 2^Ω(k log log k) для tropical-circuit pure DP задач связности/коммивояжёра при pathwidth k.

**Ограничение:** Граница относится к конкретной модели tropical circuits; алгебраические ускорения и общие DP алгоритмы вне класса не опровергаются.

**Идентичность:** `doi:10.4230/LIPIcs.ICALP.2026.130` · **Авторы:** Kacper Kluk, Jesper Nederlof · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.130) · **Доступ:** `publisher_article_abstract_and_bibliography_checked`

**Связь с исследованиями →** [OM-133](INDEX.md#om-133), [ML-004](INDEX.md#ml-004)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## fine-grained-algorithms
*Edit distance, строки и тонкая сложность*

### LIT-074
**[Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://doi.org/10.1145/3798129.3800789)** (2026)

Mao–Rubinstein: рандомизированные (1+ε)-ED и (1−ε)-LCS схемы с ускорением относительно n² на субквадратическом масштабе.

**Ограничение:** Аппроксимация расстояния между строками не даёт exact edit script, оптимальной delta patch-базы или онлайн обновлений.

**Идентичность:** `doi:10.1145/3798129.3800789` · **Авторы:** Xiao Mao, Aviad Rubinstein · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-092
**[Space-Efficient Text Indexing with Mismatches using Function Inversion](https://doi.org/10.1145/3798129.3800818)** (2026)

Bibbens–Borevitz–McCauley строят линейно-пространственный индекс поиска строк с ≤k Hamming mismatches и сглаженным tradeoff query/space.

**Ограничение:** Поиск при Hamming distance не покрывает вставки/удаления и не является автоматическим поиском минимальной delta patch-базы.

**Идентичность:** `doi:10.1145/3798129.3800818` · **Авторы:** Jackson Bibbens, Levi Borevitz, Samuel McCauley · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-099](INDEX.md#om-099), [OM-121](INDEX.md#om-121), [DL-001](INDEX.md#dl-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)


## randomized-sampling
*Рандомизированная выборка, подсчёт и memory-sample*

### LIT-075
**[A Unified Approach to Memory-Sample Tradeoffs for Detecting Planted Structures](https://doi.org/10.1145/3798129.3800739)** (2026)

Обобщённая схема нижних границ memory/sample для многопроходного обнаружения planted bicliques, sparse means и sparse PCA.

**Ограничение:** Распределительное различение planted-vs-null не равно set-only GF(2) строгой оценке d; число проходов и модель памяти должны совпасть.

**Идентичность:** `doi:10.1145/3798129.3800739` · **Авторы:** Sumegha Garg, Jabari Hastings, Chirag Pabbaraju, Vatsal Sharan · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-140](INDEX.md#om-140), [DM-007](INDEX.md#dm-007)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-081
**[Parallel Sampling via Autospeculation](https://doi.org/10.1145/3798129.3800828)** (2026)

Автоспекулятивная выборка с параллельным доступом к оракулам снижает ожидаемую глубину последовательного генерирования до примерно √n.

**Ограничение:** Выигрыш по параллельной глубине в oracle model не означает меньшую суммарную вычислительную работу, память или низкую latency Rust API.

**Идентичность:** `doi:10.1145/3798129.3800828` · **Авторы:** Nima Anari, Carlo Baronio, CJ Chen, Alireza Haqi, Frederic Koehler, Anqi Li, Thuy-Duong Vuong · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-113](INDEX.md#om-113), [OM-139](INDEX.md#om-139)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-082
**[Shifted Composition IV: Toward Ballistic Acceleration for Log-Concave Sampling](https://doi.org/10.1145/3798129.3800881)** (2026)

Altschuler–Chewi–Zhang исследуют недодемпфированную Langevin-динамику, KL ошибки дискретизации и ускоренную лог-вогнутую выборку.

**Ограничение:** Гарантии зависят от регулярности log-concave распределения, свойств ULD и модели oracle; не general uniform sampler для дискретных комбинаторных объектов.

**Идентичность:** `doi:10.1145/3798129.3800881` · **Авторы:** Jason M. Altschuler, Sinho Chewi, Matthew S. Zhang · **Проверка:** `publisher_abstract_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Первоисточник / издательский список:** [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) · **Доступ:** `official_conference_toc_abstract_linked_doi`

**Связь с исследованиями →** [OM-139](INDEX.md#om-139), [OM-113](INDEX.md#om-113)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) (model_overlap)

### LIT-134
**[Equivalent Comparisons of Experiments](https://doi.org/10.1214/aoms/1177729032)** (1953)

Blackwell формализует сравнение статистических экспериментов и относительную информативность наблюдений для задач принятия решений.

**Ограничение:** Порядок информативности не даёт автоматических cell-probe или patch-byte границ; требуется конкретный канал наблюдений и допустимое преобразование статистического эксперимента.

**Идентичность:** `doi:10.1214/aoms/1177729032` · **Проверка:** `publisher_bibliography_checked` · **Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.

**Связь с исследованиями →** [ML-004](INDEX.md#ml-004), [DM-001](INDEX.md#dm-001)

**Происхождение цитаты / пересечения →** [MATHLAB:docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md](https://github.com/definitely-stable/Mathlab/blob/de6f120c7a2982efd39213a5cd8de47e6b8a6088/docs/research/UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) (model_overlap)
