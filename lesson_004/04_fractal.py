# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

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

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v2.draw()
    next_point = v1.end_point
    next_length = length * 0.75
    next_angle = angle - 30
    next_angle1 = angle + 30
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    draw_branches(start_point=next_point, angle=next_angle1, length=next_length)


root_point = sd.get_point(300, 30)


draw_branches(start_point=root_point, angle=90, length=150)


# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

# зачет!
