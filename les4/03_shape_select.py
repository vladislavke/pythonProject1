# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


point = sd.get_point(200, 350)
print("input type of figure: 3 - triangle, 4 - square, 5 - pentagonal, 6 - hexagonal")
sides_input = int(input())
print("input color: 0 - red, 1 - orange, 2 - yellow, 3 - green, 4 - cyan, 5 - blue, 6 - purple")
color_input = int(input())
polygon(point1=point, sides=sides_input, length=200, color=color_input)
sd.pause()
