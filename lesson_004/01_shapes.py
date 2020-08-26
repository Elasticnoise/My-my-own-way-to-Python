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
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
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


# def triangle(point, angle, length=50):
#     for next_angle in range(0, 360, 120):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#
#
# def square(point, angle, length=50):
#     for next_angle in range(0, 360, 90):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#
#
# def pentagon(point, angle, length=50):
#     for next_angle in range(0, 360, 72):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#
#
# def hexagon(point, angle, length=50):
#     for next_angle in range(0, 360, 60):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#
#
# point0 = sd.get_point(100, 100)
# triangle(point=point0, angle=20, length=100)
# point1 = sd.get_point(400, 100)
# square(point=point1, angle=20, length=100)
# point2 = sd.get_point(100, 400)
# pentagon(point=point2, angle=20, length=100)
# point3 = sd.get_point(400, 400)
# pentagon(point=point3, angle=20, length=100)
#
# # 2 - часть
#
#
# def triangle(point, angle, length=50):
#     for next_angle in range(0, 360, 120):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#
#
# def square(point, angle, length=50):
#     for next_angle in range(0, 360, 90):
#         v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
#         v.draw()
#         point = v.end_point


def draw_polygon(point, angle, length, corners_quantity):
    new_point = point
    step_corner = 360 // corners_quantity
    for next_angle in range(0, 360 - step_corner, step_corner):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw()
        point = v.end_point
    sd.line(start_point=new_point, end_point=point, width=3)


point0 = sd.get_point(100, 100)
point1 = sd.get_point(400, 100)
point2 = sd.get_point(100, 400)
point3 = sd.get_point(400, 400)


def triangle():
    draw_polygon(point=point0, angle=20, length=100, corners_quantity=3)


def square():
    draw_polygon(point=point1, angle=20, length=100, corners_quantity=4)


def pentagon():
    draw_polygon(point=point2, angle=20, length=100, corners_quantity=5)


def hexagon():
    draw_polygon(point3, angle=20, length=100, corners_quantity=6)


triangle()
square()
pentagon()
hexagon()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# зачет первой части


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получитя:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# зачет!
