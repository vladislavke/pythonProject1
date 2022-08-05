# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей


def bubble(point, step):
    radius = 30
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=sd.random_color())


point = sd.get_point(100, 100)
bubble(point, 20)


for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 20)
    bubble(point, step)

sd.pause()
