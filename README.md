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

## Проблема

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
### Система предназначена для решения большого спектра проблем, связанных, в основном с техническими ограничениями существующих средств визуального контроля за окружающей обстановкой при движении по дорогам общего пользования, 

## Перечень проблем, подлежащих решению:
1. Опасное поведение участников дорожного движения (пешеходы, авто, мотоциклы). Выявление в потоке.
2. Слепые зоны транспортных средств (в т.ч. загораживающие обзор предметы и части самих транспортных средств). Расширение зон обзора.
3. Низкое качество видеоданных. Улучшение качества методами мат. статистики.
4. Недостаточное количество видеоданных. Применение технологий кругового обзора.
5. Неизвестная траектория движения препятствий. Предположение траектории с помощью методов компьютерного зрения и искусственного интеллекта.
6. Слежение за зонами "между рядов", обнаружение мотоциклов и других быстро движущихся объектов в потоке. Методы визуальной одометрии.

## Подробное объяснение методов решения проблем:
1. С помощью методов машинного обучения и ИИ, а также связи между устройствами возможна фильтрация трафика вокруг автомобиля (и далее по ходу движения) с целью обнаружения опасно ведущих себя водителей, препятствий, ремонтов и неровностей дороги и т.д.

2. Расширение зон видимости может быть достигнуто благодаря технологиям интеллектуальной обработки изображений, таким, как смена точки съёмки, трёхмерная реконструкция сцены, удаление лишних объектов из кадра по видеоданным и тд.

3. Возможные методы улучшения качества видеоданных включают в себя технологии интеллектуального стэкинга кадров видео, содержащих быстро изменяющиеся структуры и объекты.

4. Увеличение количества камер и связей между ними в перспективе приведёт к улучшению количества и качества распознавания окружающих объектов.

5. Расчет предполагаемой траектории объекта возможно производить на основе обученной нейросети, а также методов мат. статистики.

6. Предполагается отдельные методы решения проблемы идентификации мотоциклов (ИИ и обработка изображений, визуальная одометрия) и других объектов в трафике и отдельный перечень методов слежения за специфическими зонами дорожной инфраструктуры. 

## Описание работы пользователя с системой
### Работа с системой происходит методом получения предупреждений об различных опасностях водителем.

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
- методов мат. статистики
- технологии интеллектуального стэкинга кадров
- методов машинного обучения и ИИ

### Технологическая задача, на решение которой направлен проект:
 
- Распознавание объектов на дороге и помощь водителю.
- Интеллектуальный контроль за безопасностью дорожного движения.
 
### Обоснование выбора технологических задач:
### Результат реализации проекта:
### Обоснование выбора результата:
 
### Новизна предлагаемых в инновационном проекте решений:
 
Предлагаемые решения имеют признаки научной новизны. Так, например,
существующие реализации ...
 
### Матеиально-техническая база, необходимая для реализации проекта (имеющаяся в наличии и/или планируемая к привлечению:
 
- Вычислительные системы, в т.ч.:
 
- Открытое программное обеспечение для 
- Высокоскоростное интернет соединение
- Современное съёмочное оборудование
 
### Задел по тематике проекта:
 
По тематике проекта коллективом авторов решен ряд задач, нашедших свое
описание в ряде работ, приведенных ниже. >?>?>?