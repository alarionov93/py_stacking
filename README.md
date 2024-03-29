# py_stacking
### is a simple code for stacking of images for python3

1. Clone this repo
2. Create some directory inside of root directory of repo, e.g. py_stacking/%dir_name%/
3. Put images into created directory, they must be identical by width and height, and taken from the same position.
4. In command line 
```
pip3 install -r requirements.txt
python3 main.py dir_name
```

## Проблемы и описание алгоритмов улучшения качества

### Объект автоматизации:
1. Процесс интеллектуальной пост-обработки изображений (стекинг, панорама, резкость и тд.), содержащих быстро изменяющиеся структуры и объекты.
##### *облака, молнии, звездное небо, и тд.*
### Свойства объекта автоматизации:
1. Софт, предназначенный для ручной обработки неудобен в использовании из-за большого количества рутинных операций, расходующих время.
2. Софт, существующий для автоматизации процесса обработки либо невозможно найти, либо работает с ошибками.
3. Написанная программа, использующая методы, встроенные в open-source GUI программу Hugin, работает также частично с ошибками (в части инструментов командной строки в hugin)
4. Существующие методы работы с изображениями не отвечают предъявляемым требованиям по распознаванию различных объектов с целью применения или не применения инструментов обработки к этим объектам на изображении. 
#### Примеры:
##### При стекинге медиана между пикселями не должна вычисляться в районе ярких объектов. (Молнии и др.)
##### При выполнении стекинга или сборке панорам необходимо корректно обрабатывать ГРИП на всех изображениях.
##### Необходимо манипулировать ГРИП в случае с недостаточным размытием фона или избыточным размытием объекта.
##### При стекинге изображений с облаками, звездами снятых на больших выдержках нужно применять аффинные преобразования для совмещения отдельно неподвижных (земля и др.) и подвижных (звезды и др.) объектов.

## Перечень смежных проектов:

## Название проекта
### Интеллектуальная система визуального анализа окружающей дорожной ситуации.

## Аннотация
Система предназначена для решения большого спектра проблем, связанных, в основном с техническими ограничениями существующих средств визуального контроля за окружающей обстановкой при движении по дорогам общего пользования.

## Перечень проблем, подлежащих решению:
1. Опасное поведение участников дорожного движения (пешеходы, авто, мотоциклы). Выявление в потоке.
2. Слепые зоны транспортных средств (в т.ч. загораживающие обзор предметы и части самих транспортных средств). Расширение зон обзора.
3. Низкое качество видеоданных. Улучшение качества методами мат. статистики.
4. Недостаточное количество видеоданных. Применение технологий кругового обзора.
5. Неизвестная траектория движения препятствий. Предположение траектории с помощью методов компьютерного зрения и искусственного интеллекта.
6. Слежение за зонами "между рядов", обнаружение мотоциклов и других быстро движущихся объектов в потоке.

## Подробное объяснение методов решения проблем:
1. С помощью методов машинного обучения и интеллектуального анализа изображений, а также связи между устройствами возможна фильтрация трафика вокруг автомобиля (и далее по ходу движения) с целью обнаружения опасно ведущих себя водителей, препятствий, ремонтов и неровностей дороги и т.д.

2. Расширение зон видимости может быть достигнуто благодаря технологиям обработки изображений, таким, как смена точки съёмки, трёхмерная реконструкция сцены, удаление лишних объектов из кадра по видеоданным и тд.

3. Возможные методы улучшения качества видеоданных включают в себя технологии интеллектуального стэкинга кадров видео, содержащих быстро изменяющиеся структуры и объекты.

4. Увеличение количества камер и связей между ними в перспективе приведёт к улучшению количества и качества распознавания окружающих объектов.

5. Расчет предполагаемой траектории объекта возможно производить на основе обученной нейросети, а также методов мат. статистики.

6. Предполагается отдельные методы решения проблемы идентификации мотоциклов (ИИ и обработка изображений, визуальная одометрия) и других объектов в трафике и отдельный перечень методов слежения за специфическими зонами дорожной инфраструктуры. 

## Описание работы пользователя с системой

### Работа с системой происходит методом получения предупреждений об различных опасностях водителем.

## Описание внешнего вида и исполнения системы

### В состав системы могут быть включены следующие элементы:
1. Вычислительный комплекс на графическом ядре (например, Jetson Nano)
2. Блоки камер, в т.ч. для 3d
3. Подсистема связи между компонентами по ЛВС
4. Подсистема связи со смежными системами

Блок камер закрепляется в районе крепления центрального зеркала заднего вида, вычислительный блок - в центре масс автомобиля для минимизации вибрационных и динамических нагрузок.

## Принадлежность к проектам в сфере ИИ

### Обоснование соответствия предмета проекта:
 
Проект относится к категориям "компьютерное зрение", "перспективные методы искусственного интеллекта".
 
### Обоснование выбора технологии:
 
В проекте предполагается использовать такие современные технологии обработки
изображений, как:
 
- смена точки съёмки
- трёхмерная реконструкция сцены (opencv)
- визуальная одометрия (opencv)
- удаление лишних объектов из кадра по видеоданным (opencv)
- нейросетевые технологии (yolo, tensorflow)
- методы мат. статистики
- технологии интеллектуального стэкинга кадров
- методы машинного обучения и ИИ

### Технологическая задача, на решение которой направлен проект:
 
- Распознавание объектов на дороге и помощь водителю.
- Интеллектуальный контроль за безопасностью дорожного движения.
 
### Обоснование выбора технологических задач:
### Результат реализации проекта:
### Обоснование выбора результата:
 
### Новизна предлагаемых в инновационном проекте решений:
 
Предлагаемые решения имеют признаки научной новизны. Так, например,
существующие реализации ...
 
### Матеиально-техническая база, необходимая для реализации проекта (имеющаяся в наличии и/или планируемая к привлечению):
 
- Вычислительные системы, в т.ч.:
 
- Вычислительный блок (Jetson Nano)
- Авто/мото техника для тестирования системы
- Открытое программное обеспечение для работы с видеоданными
- Высокоскоростное интернет соединение
- Современное съёмочное оборудование
 
### Задел по тематике проекта:

По тематике проекта коллективом авторов решен ряд задач, нашедших свое описание в ряде научных работ.

Также существует научно-технический задел, в виде репозитория с реализацией некоторых прототипов вышеперечисленных алгоритмов.

Ссылка на репозиторий https://github.com/alarionov93/py_stacking/

## ТЕХНИЧЕСКОЕ ЗАДАНИЕ НА ВЫПОЛНЕНИЕ НИОКР
 
1. Цель выполнения НИОКР
 
Интеллектуальная система визуального анализа окружающей дорожной ситуации (САДС) создается со следующими целями:
- повышения уровня общей безопасности ДД и контроль за соблюдением правил дорожного движения;
- обеспечения дополнительной информацией участников дорожного движения;
- сбор и аннотирование данных об окружающей дорожной обстановке;
- выявление опасных участников движения, нарушающих ПДД.
 
2. Назначение научно-технического продукта (изделия и т.п.)
 
САДС предназначена для использования на автомобилях, мотоциклах и прочих транспортных средсвах, имеющих право передвигаться по дорогам общего пользования, и решать задачи помощи водителю, снижения уровня аварийности и навигации в городском трафике.
 
3. Технические требования к научно-техническому продукту (прототипу, опытному
образцу), который должен быть разработан в рамках текущего этапа выполнения
НИОКР. Основные технические параметры, определяющие функциональные,
количественные (числовые) и качественные характеристики научно-технического
продукта, полученного в результате выполнения текущего этап НИОКР
 
3.1 Функции, выполнение которых должен обеспечивать разрабатываемый
научно-технический продукт
 
1) Предупреждение водителя о развитии опасной ситуации,
2) Построение модели траектории движения ТС,
3) Построение модели траектории движения окружающих объектов,
4) Увеличение поля зрения водителя ТС,
5) Выгрузка данных в сторонние сервисы,
6) Обмен информацией с аналогичными устройствами,
7) Сообщение о фактах нарушения ПДД в соответствующие инстанции.
 
3.2 Количественные параметры, определяющие выполнение научно-техническим продуктом
своих функций

===

0. Показатели, ТТХ железа и устройства.

1. Показатели, ТТХ железа и устройства, быстродействие (до 8К суммарно). Не ниже, чем Jetson Nano.
	1. Вычислительный блок: быстродействие (до 8К суммарно), не ниже, чем у Jetson Nano.
	1.1.Графический процессор: архитектура NVIDIA Maxwell не менее 64 ядрами или аналогичный;
	1.2.Процессор: не ниже, чем 2-х ядерный;
	1.3.Оперативная память: не менее 4 Гб LPDDR4, 64-bit;
	1.4.Память: SSD / Flash карта 1TB v10 (170/100 MB/sec);
	1.5.Кодирование/декодирование видео, кодек (H.264/H.265), не менее: 
		Разрешение 	Частота (к/сек)
		640х480		120	
		1080		60
		4k			25
		8k			10

2. Блок питания 120W. АКБ 12V, 10 Ah.

3. 4 камеры - 2 с широкоугольными объективами вперёд и назад, 1 с длиннофокусным вперёд и 1 со средним ФР в салон.
	3.1. Камера с объективом не менее чем f/2.8 и углом обзора > 130 градусов по диагонали - 2шт.
	3.2. Камера с объективом не менее чем f/5.6 и углом обзора < 20 градусов по диагонали - 1шт.
	3.3. Камера с объективом не менее чем f/2.8 и углом обзора > 80 градусов по диагонали - 1шт. 
	(Для контроля состояния водителя)

4. Видимость:
	4.1. День: при 5000лк - 150м облачно
			   при 50000лк - 500м ясный день
			   выше - 500м
	4.2. Ночь: при 10-50лк - 120м освещённые дороги
			   при 0.2-1лк - 70м неосвещнные участки
			   ниже - 30-40м
5. Характеристики ПО: используемый стек технологий
	1. python3
	2. opencv, pytorch
	3. tensorflow, scikit-learn
	4. numpy, pandas
	5. API Yandex 
6. Вид исполнения - зеркало заднего вида, установка внутри салона, и вычислительный	 блок установка в багажник/переднюю панель авто.
3. Слайд про организацию схемы работы устройства.
4. Рекомендательные письма.
5. Рассказать про дообучение при работе системы.

===
1) Объем обрабатываемых видеоданных - суммарно 8K видео с 3ех камер.
2) Определение опасных водителей - частота перестановок ТС в потоке.
3) Распознавание ТС в условиях плохой видимости - вероятность распознавания ТС в зависимости от погодных условий.
4) Распознавание ТС в условиях низкой освещенности - вероятность распознавания ТС в зависимости от освещения.
5) Уменьшение шума на кадрах, читаемых системой - вероятность распознавания ТС в зависимости от параметров алгоримов подавления шума.

3.3 Входные воздействия, необходимые для выполнения научно-техническим продуктом
заданных функций
 
1) Видеопоток с камеры.
2) Формализованные правила дорожного движения.
3) Информация о траектории ТС.
4) Оперативные картографические данные.
 
3.4 Выходные реакции, обеспечиваемые научно-техническим продуктом в результате
выполнения своих функций
 
- рекомендации водителю по безопасности вождения;
- обмен информацией с другими ТС;
- сообщения о нарушении правил дорожного движения в соответствующие инстанции;
- выдача информации в сторонние сервисы;

3.5 Требования к конструкции и составным частям научно-технического продукта
 
Cостав САДС
- Вычислительный комплекс на графическом ядре (например, Jetson Nano)
- Подсистема захвата видео с камер
- Подсистема вычисления параметров движения ТС и окружающих объектов
- Блоки камер, в т.ч. для 3d
- Подсистема связи между компонентами по ЛВС
- Подсистема связи со смежными системами
 
 
3.6 Требования к массогабаритным характеристикам научно-технического продукта
 
не применимо.
 
3.7 Вид исполнения, товарные формы
 
Встраиваемая система.
 
3.8 Требования к мощностным характеристикам научно-технического продукта – по
потребляемой/производимой энергии
 
не применимо.
 
3.9 Требования к удельным характеристикам научно-технического продукта – на
единицу производимой продукции
 
не применимо.
 
3.10 Требования к аппаратной части программных комплексов
=====

=====
 
3.11 Условия эксплуатации, использования научно-технического продукта
 
Температура: -50 ... +60 С
Влажность: 0 ... 100 %
Корпус и разъёмы устройства должны соответствовать стандарту IP66.
 
3.12 Иные требования к научно-техническому продукту (прототипу, опытному образцу),
который должен быть разработан в рамках текущего этапа выполнения НИОКР
 
На данном этапе разрабатывается прототип программного обеспечения, выполняющий
функции, указанные  в разделе 3.1. ПО должно работать под управлением ОС Linux,
в контейнерной инфраструктуре и поддерживать масштабирование.
 
4. Требования по патентной охране
 
Т.к. в составе ПО планируется широко использовать софт, распространяемый на
условиях коллективного авторства, исходные коды и сырые данные для обучения
моделей должны быть опубликованы для свободного изучения под лицензией
GPLv3.
 
5. Перечень основных категорий комплектующих и материалов (входящих в состав
разрабатываемого продукта (изделия) или используемых в процессе его
разработки и изготовления)
 
1. Вычислительный блок (Jetson Nano) или аналогичный.
2. Блок питания 500W.
3. 250 ГБ SSD M.2 накопитель, или флеш карта аналогичного объёма.
4. Камера разрешения не менее чем 8K с объективом не менее чем f/1.5 и углом обзора > 130 градусов по диагонали - 3шт.