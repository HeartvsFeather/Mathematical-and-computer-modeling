# Mathematical and computer modeling
## Description
Данный репозиторий создан для отчетов по курсу компьютерного моделирования
## First problem
### Условие с занятия:
Для данной функции cos(3 * x) + 0.2 * x найти и вывести градиентный спуск к ближайшему локальному минимуму функции. Отобразить спуск на графике
### Примечание к решению:
1. Функция отрисована и использована на отрезке от -5 до 5 с шагом 0.01, что сильно увеличивает погрешность конечного результата поиска ближайшего локального минимума функции. Погрешность любого решения будет +- 0.01
2. Шаг смещения вправо или влево зависит от знака функции в точке (если начальная точка будет задана локальным максимумом, то градиентный спуск начнется влево) ((если задать начальную точку локальным минимум, то конечный результат все равно будет отличаться шагом на 0.01 влево или вправо))
3. Длина шага смещения равна 0.01
4. Зацикленность возле локальной точки минимума прерывает цикл поиска и отрисовывает график градиентного спуска (стрелки не так точно показывают конечный результат, они нужны для лучшего понимания, что происходит) ((результат отобразится в терминале))
### Примечание к коду:
1. Для решения нужны зависимости из requirements.txt и Python 3.11.8
2. Отрисовка происходит в отдельном окне, а решение проблемы в консоли
## Second problem
### Условие с занятия:
За столом сидят два игрока. У первого в распоряжении находится x рублей, у второго в распоряжении находится y. Перед ними на столе лежит асимметричная монета (вероятность, что выпадет орел, равняется p). Если на монете выпадает орел, то рубль выигрывает первый игрок (второй игрок выплачивает первому 1 рубль), а если выпадает решка, то первый игрок платит второму один рубль. Максимальное число шагов - N, число игр N game. Требуется найти вероятность проигрыша каждого игрока и вычислить среднюю длину игры (N = 100 и N_game = 1000)
### Примечание к решению:
1. В решении было учтено два вида игры: первый засчитывал победу одного из игроков при полном разорении второго; второй вид игры засчитывал победу либо при полном разорении одного из игроков, либо по окончании N раундов выигрывал игрок, у которого остается больше монет
2. Была использована библиотека random с равномерным распределением
### Примечание к коду:
1. Для решения нужен только Python 3.11.8 без зависимостей
2. Решение отображается в консоли
## Third problem
### Условие с занятия:
Дана функция sqrt((1 - cos(2 * x)) / 2). Найти определенный интеграл f(x) на отрезке от 0 до Pi. Сделать это аналитическим методом, методом левых прямоугольников, правых прямоугольников, методом трапеций, методом Монте-Карло для разных N (количество разбиений) ((1000, 500, 100, 10)) и методом Симпсона. Количество разбиений N взять 1000
### Примечание к решению:
1. В решении не было использовано округление конечных результатов, чтобы можно было понять точность и расхождения по сравнению с аналитическим решением
2. Для каждого решения отображена абсолютная и относительная погрешность относительно аналитического решения
3. Можно поменять f(x) на неберущиеся интегралы и посчитать их
4. Была использована библиотека random с равномерным распределением
### Примечание к коду:
1. Для решения нужен только Python 3.11.8 и numpy==1.26.4 без остальных зависимостей
2. Решение отображается в консоли
## Fourth problem
### Условие с занятия:
Дана функция sin(x) * e ** x ** 2 + x / cos(x). Найти корень f(x) (пересечение f(x) с осью OX) на отрезке от 3 до 3.2 методом бисекции. Условие поставлено так, что f(x) существует на отрезке, f(x) пересекает ось OX ровно один раз на отрезке, f(x) не имеет разрывов никакого порядка на отрезке. Требуемая точность решения должна быть 1e-12
### Примечание к решению:
1. В решении был создан свой метод getSign для удобства, хотя в numpy такой метод есть
2. Оба ответа при решении не будут отличаться, но проверка требуемой точности происходит по двум разным методом, хотя суть от этого не меняется
### Примечание к коду:
1. Для решения нужен только Python 3.11.8 и numpy==1.26.4 без остальных зависимостей
2. Решение отображается в консоли
## Technologies
Python 3.11.8
## Author
Антон Абраменков (HeartvsFeather)
