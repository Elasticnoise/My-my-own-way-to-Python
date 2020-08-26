# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет


def bubble(point, step, color, width):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=width)


point = sd.get_point(300, 300)
color = sd.COLOR_DARK_ORANGE
bubble(point=point, step=20, color=color, width=2)

# Нарисовать 10 пузырьков в ряд


color = sd.COLOR_DARK_ORANGE
for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    bubble(point=point, step=5, color=color, width=2)


# Нарисовать три ряда по 10 пузырьков
# def bubble(point, step, color, width):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, color=color, width=width)
#
#
color = sd.COLOR_DARK_ORANGE
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, color=color, width=2)


# # Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# def bubble(point, step, color, width):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, color=color, width=width)
#
#
for _ in range(100):
    step = random.randint(2, 10)
    point = sd.random_point()
    color = sd.random_color()
    bubble(point=point, step=step, color=color, width=1)

sd.pause()

# зачет!
