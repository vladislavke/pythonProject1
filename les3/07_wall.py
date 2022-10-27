# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
import random

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1200, 600)

line_width = 2
for count_x in range(0, 1201, 100):
    start_x = count_x
    for count in range(0, 601, 50):
        start_y = count
        if count % 100 == 0:
            start_point = sd.get_point(start_x, start_y)
            end_point = sd.get_point(start_x, start_y + 50)
        else:
            start_point = sd.get_point(start_x - 50, start_y)
            end_point = sd.get_point(start_x - 50, start_y + 50)
        sd.line(start_point, end_point, sd.COLOR_ORANGE, line_width)
for count_y in range(0, 601, 50):
    start_point = sd.get_point(0, count_y)
    end_point = sd.get_point(1200, count_y)
    sd.line(start_point, end_point, sd.COLOR_ORANGE, line_width)
sd.pause()
