# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (1200, 600)


def bubble(point, step, color):
    radius = 600
    for _ in range(3):
        radius -= step
        sd.circle(center_position=point, radius=radius, width=20, color=color)

radius1 = 600
for i in range(7):
    point = sd.get_point(1000, 0)
    radius1 -= 20
    sd.circle(center_position=point, radius=radius1, width=20, color=rainbow_colors[i])







# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
