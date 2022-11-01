# -*- coding: utf-8 -*-
import random as rd
import simple_draw as sd



# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(point, angle, length, count):

    count -= 1
    if length > 10 and count > 0:
        side1 = sd.get_vector(start_point=point, angle=angle + 15, length=length, width=2)
        side1.draw()
        s1_point = side1.end_point
        side2 = sd.get_vector(start_point=point, angle=angle - 15, length=length, width=2)
        side2.draw()
        s2_point = side2.end_point
    else:
        return
    draw_branches(point=s1_point, angle=angle + rd.randint(25, 40), length=length * rd.uniform(0.55, 0.95), count=count)
    draw_branches(point=s2_point, angle=angle - rd.randint(25, 40), length=length * rd.uniform(0.55, 0.95), count=count)


point = sd.get_point(300, 30)
draw_branches(point=point, angle=90, length=100, count=11)
sd.pause()
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
