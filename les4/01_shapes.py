# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(point, angle, length):
    side1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    side1.draw()

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle + 120, length=length, width=2)
    side2.draw()

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle + 240, length=length, width=2)
    side3.draw()


def square(point, angle, length):
    side1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    side1.draw()

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle + 90, length=length, width=2)
    side2.draw()

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle + 180, length=length, width=2)
    side3.draw()

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle + 270, length=length, width=2)
    side4.draw()

def pentagonal(point, angle, length):
    side1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    side1.draw()
    angle += 72

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle, length=length, width=2)
    side2.draw()
    angle += 72

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle, length=length, width=2)
    side3.draw()
    angle += 72

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle, length=length, width=2)
    side4.draw()
    angle += 72

    side5 = sd.get_vector(start_point=side4.end_point, angle=angle, length=length, width=2)
    side5.draw()

def geksagonal(point, angle, length):
    side1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    side1.draw()
    angle += 60

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle, length=length, width=2)
    side2.draw()
    angle += 60

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle, length=length, width=2)
    side3.draw()
    angle += 60

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle, length=length, width=2)
    side4.draw()
    angle += 60

    side5 = sd.get_vector(start_point=side4.end_point, angle=angle, length=length, width=2)
    side5.draw()
    angle += 60

    side6 = sd.get_vector(start_point=side5.end_point, angle=angle, length=length, width=2)
    side6.draw()

def polygon(point, sides, length):
    angle = 360 / sides
    if sides < 2:
        break
    else:
        angle += 360/sides
    sides -= 1
    if sides >= 1
    side1 = sd.get_vector(start_point=point, angle=360/, length=length, width=2)
    side1.draw()
    angle += 60

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle, length=length, width=2)
    side2.draw()
    angle += 60

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle, length=length, width=2)
    side3.draw()
    angle += 60

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle, length=length, width=2)
    side4.draw()
    angle += 60

    side5 = sd.get_vector(start_point=side4.end_point, angle=angle, length=length, width=2)
    side5.draw()
    angle += 60

    side6 = sd.get_vector(start_point=side5.end_point, angle=angle, length=length, width=2)
    side6.draw()
point = sd.get_point(200, 100)
# triangle(point=point, angle=30, length=200)
# square(point=point, angle=30, length=200)
# pentagonal(point=point, angle=30, length=200)
geksagonal(point=point, angle=0, length=200)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
