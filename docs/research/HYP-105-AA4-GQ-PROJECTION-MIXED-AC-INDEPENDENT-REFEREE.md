# HYP-105 / #230 — AA4-GQMIX: независимая рецензия полной GQ-проекции, удаления Z и четырёх смешанных A/C блокеров

**Статус:** математический исследовательский Draft, строго поверх замороженного [#745](https://github.com/definitely-stable/Mathlab/pull/745) HEAD d51b638a60f4aab6462e6fdea8d0fd78f7cd22f0. Предыдущие PR и main не меняются; #230 остаётся OPEN_WITH_FORMAL_BLOCKER. Это независимая проверка других двух математических интерфейсов исходной универсальной Branch A, не доказательство нового ASET exponent.

Главная цель issue #230 — нижняя оценка \(S_s(f,g)=\Omega(s^6)\) для семи классов шестёрок различных ORIGINAL incidence-ID, равномерно по любым фиксированным отдельно глобально pair-injective и произвольно коррелированным отображениям f и g. GF(5) риск R3 — отдельное аддитивное следствие, не замена S_s.

## 1. Единственная правильная модель и кванторы

Для dyadic s=2^h пусть настоящий симплектический \(W(3,s)\) имеет \(V=(s+1)(s^2+1)\) исходных точек и прямых и \(N=(s+1)V\) настоящих исходных point-line incidence flags \(I\). Физический алфавит имеет минимальный размер \(a=\min\{n:\binom n2\ge V\}\). Зафиксируем все f:P→binom([a],2), g:L→binom([a],2) **до** любых случайных приоритетов или раскрасок. Каждое отображение отдельно глобально инъективно, между ними допускается произвольная корреляция. Возьмём любое adversarial \(Z\subseteq I\) именно настоящих исходных ID. Полное разрешённое множество \(A=I\setminus Z\) отлично от меньшего парного ядра \(C\subseteq A\), полученного удалением владельцев всех физически высокостепенных рёбер полного H (Q заморожено ДО Z) и исходных владельцев с полной J-конфликтной степенью>K=64.

Каждый истинный source flag (p,ell) владеет ровно ДВУМЯ реальными противоположными физическими диагоналями прямоугольника f(p)×g(ell), а каждый физический edge uniquely source-owned вследствие отдельной глобальной pair injection. Обозначим физические степени в полном H_A через d_A(x,y), в H_C через d_C(x,y), \(\Delta=\max d_C(x,y)\). В полном допущенном оригинальном A физический максимум **не обязан** удовлетворять Δ. Это принципиально для Cauchy книг.

## 2. Полная ORIGINAL q--ell--p--r проекция и три исходные роли

Для каждого неинцидентного original (q,r), q∈P,r∈L, аксиома настоящей GQ даёт единственного p∈r, исходно коллинеарного q. Уникальная исходная прямая ell через p,q завершает полную проекцию

\[
q\longrightarrow\ell\longrightarrow p\longrightarrow r.
\]

Три различных исходных incidence-ID якоря этой проекции:

\[
a_1=(q,\ell),\quad a_2=(p,\ell),\quad a_3=(p,r).
\]

Каждый исходный flag i=(p,ell) появляется ровно \(s^2\) раз **в каждой из трёх позиций** по всем \(V(V-s-1)\) неинцидентным (q,r). Для первой позиции фиксируем q=p и ell: p'≠p выбирается из s других точек ell, а r≠ell — из s других исходных прямых через p'. Аналогично третья позиция двойственна. Для средней позиции фиксируем p,ell; q выбирается из s других точек ell, а r из s других прямых через p. Поэтому для любого выбранного adversarial Z:

\[
\sum_{q\notin r}m_Z(q,r)=3s^2|Z|,
\quad
m_Z(q,r):=\#\{a_1,a_2,a_3\}\cap Z\in\{0,1,2,3\}.
\tag{GQ-1}
\]

Именно **полная GQ**, не парное C, задаёт q,r,p,ell; исходные три якоря достаточно требовать принадлежащими A=I\Z, а не меньшему C.

### Новый точный all-h результат: overlap-rebate для source Z

Один неинцидентный (q,r) соответствует ровно ЧЕТЫРЁМ упорядоченным физическим парам концов с факторными парами f(q),g(r), с учётом обеих ориентировок каждого реального 2-label. Ранее использовалась только union bound \(12s^2|Z|\), причём проекции с двумя-тремя удалёнными якорями были посчитаны повторно.

Для любого Z, без случайности, определим точный исходный overlap-credit

\[
\Xi_Z=4\sum_{\substack{q\in P,\ r\in L\\q\notin r}}
(m_Z(q,r)-1)_+.
\]

Из (GQ-1) получаем ТOЧНУЮ формулу числа **всех Z-маскированных типизированных конечных пар полного GQ** (до исключения других плохих концов):

\[
\boxed{
M_Z=4\,\#\{(q,r):q\notin r,\ m_Z(q,r)>0\}
=12s^2|Z|-\Xi_Z.
}
\tag{GQ-2}
\]

Здесь \(0\le\Xi_Z\le12s^2|Z|\); положительность \(\Xi_Z\) означает реальные совпадения нескольких удалённых source anchors у ОДНОЙ проекции. Это действительно новое точное combinatorial source identity, действительное для ВСЕХ dyadic s и даже любых finite generalized quadrangles порядка (s,s). Отсюда старый универсальный bound \(M_Z\le12s^2|Z|\) сохраняется без дополнительных предположений. Важно: нет гарантии \(\Xi_Z\ge c\,s^2|Z|\) для **любого** adversarial Z. Поэтому нельзя искусственно уменьшить универсальную \(\rho_\star\) или увеличить R3-коэффициент только на основании средней finite-instance экономии. Нынешняя теорема #744 сохраняет прежнюю worst-case \(\rho_\star\).

Кроме того реальное число Z-исключений ПОСЛЕ отбрасывания non-Z-плохих концов может быть ещё меньше \(M_Z\); оно считается отдельно. Мы не маскируем случайно более строгий оценочный порядок: удаление Z может зависеть от f/g.

## 3. All-h \(24s^5\) для настоящих не-Z-плохих конечных пар

Для \(s\ge64\), \(B=\binom a2\), \(M=B-V\), число ordered физически off-coordinate пар (v0,v3) с разными первыми и вторыми координатами равно \(4B^2=a^2(a-1)^2\). Все они строго классифицируются в четыре категории (с порядком обработки):

1. Отсутствует хотя бы одна факторная label-пара среди полного f(P),g(L): **ровно** \(4(B^2-V^2)=4(2BM-M^2)\).
2. Обе пары существуют, но original q,r инцидентны: **ровно** 4N.
3. q,r неинцидентны, но полная projection имеет \(f(q)\cap f(p)\ne\varnothing\) или \(g(r)\cap g(\ell)\ne\varnothing\): сумма не больше \(8s(e_{\rm col}(f)+e_{\rm col}(g))\).
4. Иначе: original projection anchors удалены Z (по (GQ-2)) или конечные пары допустимы.

В третьем пункте, например, всякий оригинальный коллинеарный q,p с общим символом f-пар порождает не больше s исходных прямых r через p, отличных от ell(q,p), и четыре физические ориентации. Всего 2e_col(f) направленных q,p, отсюда ровно оценочный множитель \(8s\,e_{\rm col}(f)\). Двойственное рассуждение для g, **не требуется независимость f и g**.

Независимая SRG collinearity-лемма #737 даёт для каждой карты отдельно

\[
e_{\rm col}(f),e_{\rm col}(g)\le
C_s=(s^2+1)(s^2+a-2)\le\tfrac54s^4.
\]

Исходная минимальность a даёт \(B<9s^3/8,\ M<a\le(3/2)s^{3/2}\), откуда missing ≤2s^5 при s≥64. Число инцидентных ориентаций \(4N<s^5\). Два end-bad типа суммарно ≤20s^5. Следовательно

\[
\boxed{
E_{\rm bad,nonZ}\le4(2BM-M^2)+4N+
8s(e_{\rm col}(f)+e_{\rm col}(g))
\le24s^5.
}
\tag{GQ-3}
\]

Последняя оценка действует равномерно по ВСЕМ настоящим допустимым f,g и для всех dyadic s≥64, не является усреднением или экстраполяцией малого W32/W34.

В связке с точным original proper physical 3path endpoint Jensen \(\|P_3\|_F^2\le q_3^2L_6s^6\) настоящий Z-маскированный endpoint contribution оценивается Cauchy в точной форме

\[
\#P_{3,\rm masked}\le
q_3\sqrt{L_6s^6}\sqrt{M_Z}
\le q_3\sqrt{12L_6\rho}\,s^6,\quad |Z|\le\rho s^4,
\tag{GQ-4}
\]

и только на последнем шаге выбрасывается source-specific rebate \(\Xi_Z\). Для non-Z исключений отдельно \(q_3\sqrt{24L_6}s^{11/2}\), как в #740.

## 4. Истинные ORIGINAL FULL allowed A vs CORE C смешанные книги

Пусть point side (строки) f, line side g. Для original point p и правого физического символа y:

\[
R_A(p,y)=\#\{(p,\ell)\in A:y\in g(\ell)\},\quad
R_C(u,y)=\#\{(u,\ell)\in C:y\in g(\ell)\}.
\]

Смешанное число источников \(K_{AC}(p,u)=\sum_yR_A(p,y)R_C(u,y)\). Для первой физической координаты x, оригинальной point-коллинеарности и \(c_x(p)=\#\{q\sim p:x\in f(q)\}\) в **полном** point SRG:

\[
B_x=\sum_{\substack{u:\exists(u,\ell)\in C\\(x,k)\text{ are the two orientations of }f(u)}}
\sum_{p:k\in f(p)}c_x(p)K_{AC}(p,u).
\tag{MIX-1}
\]

Двойственный B_y строится независимо из source line SRG и f↔g. Не делать ложных замен \(A=C\) или \(B_x=B_y\), особенно для коррелированных f/g.

Положим \(F_{1,x}\) равным сумме квадратов \(c_x(p)\), а \(F_{2,x}\) сумме квадратов \(K_{AC}(p,u)\) по **тем же** индексам (x,k,u,p). Тогда обычное Cauchy:

\[
B_x^2\le F_{1,x}F_{2,x}.
\]

При фиксированном (x,p) каждый из не более двух возможных k из f(p) определяет не более одного u с f(u)={x,k}, благодаря глобальной pair-инъективности. Значит \(F_{1,x}\le2G_f\), \(G_f=\sum_{x,p}c_x(p)^2\) — исходная полная SRG source energy. Обратите внимание: в F1 не подменяется c_x(p) какой-либо degree ядра C.

Среди всех исходных core flags (u,ell) с фиксированным физическим y, содержащимся в g(ell), они образуют полный источник clique в source J; исходная полная J-степень core source ID ≤K, значит \(R_C(u,y)\le K+1\). Поскольку \(\sum_yR_A(p,y)\le2(s+1)\),

\[
K_{AC}(p,u)\le 2(s+1)(K+1).
\tag{MIX-2}
\]

Для любого реального физического угла (k,y) одна ORIGINAL инцидентность (p,ell) с k∈f(p), y∈g(ell) даёт ровно одно ребро H_A, соответственно H_C. Поэтому истинные corner степени:

\[
d_A(k,y)=\sum_{p:k\in f(p)}R_A(p,y),\quad
d_C(k,y)=\sum_{u:k\in f(u)}R_C(u,y).
\]

Перестановка **конечных сумм без равенства A=C** даёт точное тождество

\[
\boxed{
\Theta_{AC}=\sum_{k,y}d_A(k,y)d_C(k,y)
=\sum_{u:(u,\ell)\in C}\sum_{(x,k)\in f(u)}
\sum_{p:k\in f(p)}K_{AC}(p,u)
\le\Delta\sum_{k,y}d_A(k,y)
=4|A|\Delta.
}
\tag{MIX-3}
\]

Верхнюю границу Δ следует брать только от C; для A есть лишь сумма физических степеней \(4|A|\).

Combining (MIX-2,3):

\[
F_{2,x}\le2(s+1)(K+1)\Theta_{AC},\quad
\boxed{
B_x^2\le16(s+1)(K+1)|A|\Delta\,G_f.
}
\tag{MIX-4}
\]

Все четыре формулы имеют независимый line-dual с \(G_g\), физическим \(\Theta_{AC}\), но generally \(B_x\ne B_y\).

## 5. Истинный источник первой внутренней помехи: инъекция тройки в MIX book

Рассмотрим ORIGINAL paired physical CORE \(H_C\), \(t_4=\operatorname{tr}(A_C^4)\). Каждая physical candidate тройка \(T_{x,1}=(v_0,v_1,v_3)\), где v0,v1 — реальное CORE-ребро, истинные физические endpoint label-pairs \(f^{-1}\{x_0,x_3\}=q\), \(g^{-1}\{y_0,y_3\}=r\) определены и неинцидентны, оригинальная GQ projection q--ell--p--r имеет все три именованные anchors в полном A, и \(x_1\in f(p)\), отображается в конкретный MIX-1 witness:

\[
(u,\ell_u)\in C,\quad
(x,k)=(x_0,x_1)\text{ orientation of }f(u),\quad
p,q,\ r,\ y_0,\quad
(p,r)\in A,\quad
y_0\in g(r)\cap g(\ell_u).
\]

Здесь \((u,\ell_u)\) — единственный настоящий ORIGINAL владелец физического ребра v0v1. Поскольку q оригинально коллинеарна p и x0∈f(q), этот q действительно представлен одним из c_x(p) terms. Поскольку \((p,r)\in A\) и \((u,\ell_u)\in C\), символ y0 даёт соответствующий положительный член K_AC(p,u). И главное, исходная тройка восстанавливается из witness ОДНОЗНАЧНО:

\[
x_3=f(q)\setminus\{x_0\},\quad
y_3=g(r)\setminus\{y_0\},\quad
y_1=g(\ell_u)\setminus\{y_0\}.
\]

Поэтому запись candidate physical triple → source mixed-book term **инъективна**, несмотря на то что в полном A могут быть другие якоря, не входящие в C. Это даёт

\[
\boxed{|T_{x,1}|\le B_x.}\tag{BLOCK-1}
\]

Для любой такой triple число middle completions v1→v2→v3 ровно \((A_C^2)_{v_1v_3}\); мы можем считать и improper completions, лишь усиливая верхнюю оценку. Пусть \(I_{x,1}\) — число ВСЕХ реально допустимых endpoint-good, координатно proper физических 3paths с x1∈f(p). Тогда

\[
I_{x,1}\le\sum_{T_{x,1}}(A_C^2)_{v_1v_3}.
\]

При фиксированном ordered (v1,v3) не более \(\deg_C(v1)\le\Delta\) first-neighbor v0. Cauchy по candidate triples и точная матричная identity \(t_4=\sum_{v_1,v_3}(A_C^2)_{v_1v_3}^2\) дают

\[
\boxed{I_{x,1}^2\le B_x\Delta\,t_4.}\tag{BLOCK-2}
\]

Для x2 достаточно ревёрса actual physical path; full original q,r и projection anchors не меняются, поэтому та же bound, но не утверждается независимость или непересечение классов. Для y1 и y2 тот же аргумент применяется к действительному point↔line dual оригинальной GQ, при этом сохраняются отдельно K_AC dual и B_y. Получаем

\[
\boxed{
I_{x,j}^2\le B_x\Delta t_4,\qquad
I_{y,j}^2\le B_y\Delta t_4,\quad j=1,2.
}
\tag{BLOCK-3}
\]

Их union не больше суммы четырёх чисел, а не определяется как их сумма.

## 6. Новая полностью независимая конечная исходно-геометрическая проверка

Новый автономный сертификатор
research/hyp105_original_gq_projection_mixed_ac_referee.py
НЕ импортирует никакой старый proof, mixed-book, energy, selector, root или original six-ID inverse. В finite tests используются только доверенные symplectic ORIGINAL W32/W34 incidence fixtures и полные pair-injected f/g label constructors, затем вся математика заново вычисляется из исходных флагов.

Для каждого из шести REAL ORIGINAL W32/W34 cases, в том числе лексикографическая/обратно-нумерованная схемы, независимо сдвинутые полные f/g и кластерное adversarial Z:

- перебирает полную точную q,r неинцидентную исходную проекцию, проверяет 3 оригинальных source anchor ID, **ровно s² появлений каждого ID в каждой из трёх ролей**, полную дизъюнктивную классификацию ВСЕХ \(4\binom a2^2\) off-coordinate физических конечных пар;
- независимо считает \(e_{\rm col}(f)\) и \(e_{\rm col}(g)\), GQ missing/incident/nonZ-endbad и Z-маску, точную формулу (GQ-2), включая положительные source-overlap rebate в кластерном Z;
- заново строит полный true original physical H и FULL Q **до Z**, полный оригинальный конфликт J, разрешённое A, парное C и обе настоящие source-owned physical diagonals per ID; одновременно проверяет \(\Delta(H_C)\le Ts\);
- независимо, в несмешиваемых направлениях point и line, рассчитывает ВСЕ \(R_A,R_C,K_{AC},c_x,G,F_1,F_2,B,\Theta\), проверяет точное равенство \(\Theta=\sum_{k,y}d_Ad_C\) и все Cauchy/cap equations без допущения A=C или Bx=By;
- перечисляет независимо ВСЕ candidate physical first-inner source triples T_x1 и T_y1, требует unique term injection в оригинальный MIX book; считает для каждой реальное \((A_C^2)(v_1,v_3)\), verified original \(t_4=\operatorname{tr}(A_C^4)\) и upper \(B\Delta t_4\);
- перечисляет каждую реально proper 3step path с оригинально допустимой full GQ projection, отдельно классифицирует ВСЕ четыре blocker positions (x1,x2,y1,y2), проверяет каждое membership в соответствующем исходно-инъективном T (или reversed T), counts ≤middle-completions и Cauchy inequality, а также неотрицательный union overlap;
- прямо различает математические all-h утверждения и finite source falsifiers: all-h \(24s^5\) envelope тестируется точно на dyadic s≥64, а small s2/s4 не объявляются доказательством асимптотики.

Отдельные негативные тесты отвергают повторный/несуществующий ORIGINAL ID, неверную минимальную физическую alphabet, неправильный диагностический порог и подмену K/degree cap. Доказательства (GQ-1–4), (MIX-1–4), (BLOCK-1–3) записаны выше для **всех h**, а конечные тесты — независимые проверки против ошибки реализации, не основание для асимптотического обобщения.

GitHub-hosted Ubuntu-24.04/Python3.12 выполняет 12 независимых тестов, проверяет строго один полный JSON source witness, сохраняет артефакт; INDEX и FULL Research обязательны на том же final PR HEAD. Компьютер пользователя не используется. Предыдущая проверка #745 source selector/Jensen и selected ordinary BIPARTITE C6 trace, как и #744 heavy no-clone, остаётся замороженным parent.

## 7. Научный вердикт и следующий разрешённый шаг

В рамках перечисленных самостоятельных письменных доказательств, независимой исходной реализации и истинного geometry oracle, **полная GQ projection, Z-role exposure и FULL A/Core C mixed-book/четыре blocker source injections** проверены на уровне конкретных математических переходов. Новый точный Z-overlap rebate действительно уменьшает mask count для некоторых конкретных Z, но **не** уменьшает worst-case universal deletion estimate и не даёт самостоятельного нового ASET exponent.

Root #230 остаётся OPEN_WITH_FORMAL_BLOCKER: не все предшествующие ALL-h математические зависимости прошли финальную общую рецензию, а успешный CI не равен peer-reviewed publication. Следующий шаг — независимая систематическая проверка объединённой full-Branch-A версии, обнаружение/фиксация каждого первого неверного перехода или аккуратная acceptance matrix, затем только согласованное governance-решение. Ни main, ни родительские PR не менять, merge не выполнять, issue не закрывать автоматически.


## 8. NEW ALL-h structured-adversary theorem: 50% more original-ID deletion for COMPLETE point-/line-STARS

The new exact all-h GQ source projection overlap identity (GQ-2) proves a SECOND mathematically substantive result beyond the unconditional arbitrary-Z mask upper bound, when the adversarial ORIGINAL source set Z has a genuine **complete source-pencil STAR** form.

### 8.1. The two valid source STAR families

For ANY selected subset \(P_0\subseteq P\) of original symplectic GQ points, delete **ALL original flags incident to each selected point**:

\[
Z_{P_0}=\{(p,\ell)\in I:\ p\in P_0\},\qquad
|Z_{P_0}|=(s+1)|P_0|.
\tag{STAR-1}
\]

Alternatively, for ANY selected subset \(L_0\subseteq L\) of original lines, delete **ALL original flags incident to each selected line**:

\[
Z_{L_0}=\{(p,\ell)\in I:\ \ell\in L_0\},\qquad
|Z_{L_0}|=(s+1)|L_0|.
\tag{STAR-2}
\]

Both \(P_0,L_0\) may be chosen adversarially, including after seeing any fixed arbitrarily correlated separately globally pair-injected physical f/g. No randomness, independence, source homogeneity or choice of a preferred symplectic automorphism is assumed. This is a restriction only of the original DELETION PATTERN, not of the main maps.

### 8.2. Independent exact original source GQ counting

For every nonincident original (q,r), let its unique FULL-GQ projection be q--ell--p--r. Its three named distinct ORIGINAL anchors are (q,ell),(p,ell),(p,r).

For the complete POINT-STAR deletion (STAR-1),

\[
\boxed{m_Z(q,r)=\mathbf 1_{q\in P_0}+2\mathbf 1_{p\in P_0}.}
\tag{STAR-3}
\]

Whenever the projected middle point p lies in \(P_0\), **both original anchors** (p,ell) and (p,r) are deleted together. Every selected p is the middle projected source point in exactly (s+1)s² nonincident (q,r) projections: select one of s+1 original lines ell through p, one of s other q on ell, one of s other r lines through p. Thus the number of projections with p∈P0 is exactly \(s^2|Z|\). By (GQ-2), their two-deleted-anchor coincidences alone contribute at least \(4s^2|Z|\) to overlap rebate Xi_Z. More precisely, define

\[
\mathcal D_{P_0}:=\#\{(q,r):q\notin r,\ p(q,r)\in P_0,\ q\in P_0\}.
\]

Then (STAR-3) gives the **EXACT** all-h count:

\[
\boxed{
\Xi_{Z_{P_0}}=4s^2|Z_{P_0}|+4\mathcal D_{P_0},
\quad
M_{Z_{P_0}}=8s^2|Z_{P_0}|-4\mathcal D_{P_0}
\le8s^2|Z_{P_0}|.
}
\tag{STAR-4}
\]

The proof is just the pointwise identity \((m_Z-1)_+=\mathbf1_{p\in P_0}
+\mathbf1_{p\in P_0}\mathbf1_{q\in P_0}\); it uses FULL ORIGINAL GQ projection, not source CORE C.

For the LINE-STAR deletion (STAR-2) the true ORIGINAL point-line dual is

\[
\boxed{m_Z(q,r)=2\mathbf1_{\ell(q,r)\in L_0}+\mathbf1_{r\in L_0}.}
\tag{STAR-5}
\]

Each selected original ell is the projected *middle line* in precisely (s+1)s² projections; defining \(\mathcal D_{L_0}:=\#\{(q,r):q\notin r,\ell(q,r)\in L_0,\ r\in L_0\}\), independently obtain

\[
\boxed{
\Xi_{Z_{L_0}}=4s^2|Z_{L_0}|+4\mathcal D_{L_0},
\quad
M_{Z_{L_0}}=8s^2|Z_{L_0}|-4\mathcal D_{L_0}
\le8s^2|Z_{L_0}|.
}
\tag{STAR-6}
\]

In particular BOTH true complete source STAR types improve the worst-case endpoint mask factor from **12** down to **8** — a genuine deterministic all-h theorem about **structured adversarial ORIGINAL incidence-ID deletions**.

### 8.3. NEW full original Branch A robustness for structured Z: 3/2 times the previous radius

The independently documented #744 original source HEAVY no-clone lemma retains its improved uniform \(R=93313\), and the #745 priority/Jensen and selected C6 sixth-moment result is unchanged. Recall the existing mathematical constants after choosing once fixed rational published-existential SS6 bounds \(C_0\ge\max(1,C_{\rm graph})\), \(0<c_0\le\min(1,c_{\rm graph})\):

\[
\begin{gathered}
T=\lceil\tfrac{17}{2}93313^3C_0^3\rceil,\quad
q_3=64\binom{195}{3},\quad L_6=24+153T^2,\\
\delta=c_0/93313^6,\quad
t_\star=\frac{119}{24}-2\frac{54162}{53838}\delta,\quad
s_0=\max\{64,444T,(8E)^2,(8D)^8\}.
\end{gathered}
\]

For arbitrary original Z, the previous universal risk-preserving radius is \(\rho_{\rm arbitrary}=t_\star^2/(12q_3^2L_6)\). For TRUE complete POINT- or LINE-STAR source deletion, use the sharper exact mask upper \(M_Z\le8s^2|Z|\) from (STAR-4,6), and define

\[
\boxed{
\rho_{\rm STAR}:=\frac{t_\star^2}{8q_3^2L_6}
=\frac32\,\rho_{\rm arbitrary}.
}
\tag{STAR-7}
\]

It is critical to verify the new \(\rho_{\rm STAR}\) does not invalidate the HEAVY physical-density upgrade used to set R=93313. This holds uniformly and NONCIRCULARLY because \(L_6\ge24\), \(0<t_\star<119/24\) and q3 is fixed:

\[
0<\rho_{\rm STAR}<
\frac32\frac{(119/24)^2}{12q_3^2\cdot24}
<2^{-32}.
\tag{STAR-8}
\]

Thus the same HEAVY no-clone source constant R=93313 is valid even with these larger structured deletions, the same LOW retained original CORE remains ≥3s⁴/4 because \(\rho_{\rm STAR}<3/64\), the same q3/Jensen/L6 bound applies, and ALL THREE independent non-Z path-error budgets still satisfy their previous ≤s⁶/8 sufficient condition at the SAME dyadic s0.

By (STAR-4,6) the number of masked endpoints is ≤\(8s^2|Z|\le8\rho_{\rm STAR}s^6\), hence the Cauchy original physical 3path energy loss is

\[
q_3\sqrt{L_6s^6\cdot8\rho_{\rm STAR}s^6}
=q_3\sqrt{8L_6\rho_{\rm STAR}}\,s^6
=t_\star s^6.
\]

The previous root HEAVY/LOW composition closes **without changing T,s0,delta or the signed risk constant**: HEAVY produces at least \(\delta s^6\) real ORIGINAL D6 sixsets, or LOW with small D6 produces at least \((54162/53838)\delta s^6\) physically produced ORIGINAL BBo sixsets, via the already independent source one-sided 2-to-1 P3 inverse. Therefore:

**THEOREM AA4-STARZ, conditional on explicitly cited prior all-h source selector/HEAVY/LOW/GF5 lemmas and the published existential ordinary C6 SS6 result.** Fix any valid absolute C0,c0 once. For EVERY dyadic s≥s0, EVERY separately complete globally pair-injective, arbitrarily correlated fixed original f/g labeling, and EVERY adversarial ORIGINAL Z of either full point-star (STAR-1) or full line-star (STAR-2) form with

\[
|Z|\le\boxed{\rho_{\rm STAR}s^4=\tfrac32\rho_{\rm arbitrary}s^4},
\]

the original SEVEN-class UNWEIGHTED motif total and accepted additive full GF5 signed-event risk satisfy

\[
\boxed{
S_s(f,g)\ge\frac{c_0}{93313^6}s^6,\qquad
R_3(f,g)\ge\frac{54162\,c_0}{93313^6\,51^6}s^6.
}
\tag{STAR-9}
\]

This is **50% more allowed named ORIGINAL incidence-ID deletions for complete point/line STAR patterns** while holding the original universal risk coefficient and sufficient all-h threshold fixed. It is not a 50% improvement for arbitrary deletion Z and not a new ASET extraction exponent. Since full STAR Z=empty is allowed, it also leaves the base universal \(S_s=\Omega(s^6)\) conclusion unchanged.

### 8.4. Second independently implemented source and all-h arithmetic oracle

New standalone source code research/hyp105_original_full_star_z_50pct_referee.py uses independently reconstructed genuine W32/W34 incidence flags, the true unique full GQ q--ell--p--r projection, and complete pair-injective physically shifted f/g fixtures; it explicitly counts m_Z(q,r) and \(\mathcal D_{P_0}/\mathcal D_{L_0}\) for full point- and line-star deletion sets (including two-star subsets). It requires both exact (STAR-4) and (STAR-6) source identities, not just the safe bound; verifies all three source roles independently and complete ORIGINAL flag count |Z|=(s+1)|P0| or (s+1)|L0|. The same file independently constructs NEW T,q3,L6,s0,h0,delta,t_star,rho_STAR from exact Fraction, and proves for three formal-only C0/c0 inputs \(h_0=751,781,787\), with \(\rho_{\rm STAR}/\rho_{\rm arbitrary}=3/2\) and unchanged heavy/low signed-risk floors. Actual numeric published graph constants are not assumed.

The eight dedicated standalone negative/positive STAR tests include REAL ORIGINAL W32/W34 full-point-star AND full-line-star examples, independently shifted f/g, invalid duplicate STAR source indices and TEST-ONLY crosscheck of unchanged #744 root T/L6/s0/delta. These tests supplement the existing twelve genuine original full GQ/mixed A/C blocker tests, for **20 specialist tests total** plus two strict complete original-source JSON artifacts on GitHub-hosted Ubuntu-24.04/Python3.12. Finite tests do NOT establish the all-h theorem, which is proved by the direct projection multiplicity identities above.

**Scientific STOP:** Full point/line STAR source-deletion robustness is a new mathematically meaningful restricted-Z strengthening. The arbitrary original-Z radius \(\rho_{\rm arbitrary}\), external theorem's unknown numerical C/c and the unfinished total source proof governance remain unchanged. Root #230 stays OPEN_WITH_FORMAL_BLOCKER and all PRs remain Draft until a separate final mathematical acceptance review. No merge or issue closure.
