# -*- coding: utf-8 -*-

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

import random

import simple_draw as sd


def screensaver():
    sd.resolution = (1200, 600)
    for _ in range(10):
        x = random.randint(0, 1200)
        y = random.randint(0, 600)
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=50, width=2, color=sd.random_color())
        left_eye = sd.get_point(x - 20, y + 10)
        sd.circle(center_position=left_eye, radius=4, width=2, color=sd.random_color())
        right_eye = sd.get_point(x + 20, y + 10)
        sd.circle(center_position=right_eye, radius=4, width=2, color=sd.random_color())
        mouse_left = sd.get_point(x - 15, y - 20)
        mouse_right = sd.get_point(x + 15, y - 15)
        sd.ellipse(mouse_left, mouse_right, sd.random_color(), width=0)
    sd.sleep(2)
    sd.clear_screen()


x = 1
while x:
    screensaver()

sd.pause()
