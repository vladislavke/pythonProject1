# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def triangle(point1, angle, length, color):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    side1 = sd.get_vector(start_point=point1, angle=angle, length=length, width=2)
    sd.vector(start=point1, angle=angle, length=length, width=2, color=rainbow_colors[color])

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle + 120, length=length, width=2)
    sd.vector(start=side1.end_point, angle=angle + 120, length=length, width=2, color=rainbow_colors[color])

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle + 240, length=length, width=2)
    sd.vector(start=side2.end_point, angle=angle + 240, length=length, width=2, color=rainbow_colors[color])


def square(point1, angle, length, color):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    side1 = sd.get_vector(start_point=point1, angle=angle, length=length, width=2)
    sd.vector(start=point1, angle=angle, length=length, width=2, color=rainbow_colors[color])

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle + 90, length=length, width=2)
    sd.vector(start=side1.end_point, angle=angle + 90, length=length, width=2, color=rainbow_colors[color])

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle + 180, length=length, width=2)
    sd.vector(start=side2.end_point, angle=angle + 180, length=length, width=2, color=rainbow_colors[color])

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle + 270, length=length, width=2)
    sd.vector(start=side3.end_point, angle=angle + 270, length=length, width=2, color=rainbow_colors[color])


def pentagonal(point1, angle, length, color):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    side1 = sd.get_vector(start_point=point1, angle=angle, length=length, width=2)
    sd.vector(start=point1, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 72

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side1.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 72

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side2.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 72

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side3.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 72

    side5 = sd.get_vector(start_point=side4.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side4.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])


def geksagonal(point1, angle, length, color):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    side1 = sd.get_vector(start_point=point1, angle=angle, length=length, width=2)
    sd.vector(start=point1, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 60

    side2 = sd.get_vector(start_point=side1.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side1.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 60

    side3 = sd.get_vector(start_point=side2.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side2.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 60

    side4 = sd.get_vector(start_point=side3.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side3.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 60

    side5 = sd.get_vector(start_point=side4.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side4.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
    angle += 60

    side6 = sd.get_vector(start_point=side5.end_point, angle=angle, length=length, width=2)
    sd.vector(start=side5.end_point, angle=angle, length=length, width=2, color=rainbow_colors[color])


def polygon(point1, sides, length, color):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    if color > 6 or color < 0:
        return print("not in range")
    if sides < 3:
        return [print('маловато будет')]
    count = sides
    s_point = point1
    while count > 0:
        angle = (360 / sides) * count
        side = sd.get_vector(start_point=s_point, angle=angle, length=length, width=2)
        sd.vector(start=s_point, angle=angle, length=length, width=2, color=rainbow_colors[color])
        count -= 1
        s_point = side.end_point


print("input color: 0 - red, 1 - orange, 2 - yellow, 3 - green, 4 - cyan, 5 - blue, 6 - purple")
point = sd.get_point(250, 500)
color_input = int(input())
print("input number of sides")
sides_input = int(input())
polygon(point1=point, sides=sides_input, length=200, color=color_input)
triangle(point1=point, angle=30, length=200, color=color_input)
square(point1=point, angle=30, length=200, color=color_input)
pentagonal(point1=point, angle=30, length=200, color=color_input)
sd.pause()
