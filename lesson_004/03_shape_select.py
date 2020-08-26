# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

point0 = sd.get_point(250, 250)
point1 = sd.get_point(250, 250)
point2 = sd.get_point(270, 210)
point3 = sd.get_point(270, 200)


def triangle(point=point0, angle=0, length=100):
    for next_angle in range(0, 360, 120):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw()
        point = v.end_point


def square(point=point1, angle=0, length=100):
    for next_angle in range(0, 360, 90):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw()
        point = v.end_point


def pentagon(point=point2, angle=0, length=100):
    for next_angle in range(0, 360, 72):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw()
        point = v.end_point


def hexagon(point=point3, angle=0, length=100):
    for next_angle in range(0, 360, 60):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw()
        point = v.end_point


figures = [
    {'name': 'треугольник', 'function': triangle},
    {'name': 'квадрат', 'function': square},
    {'name': 'пятиугольник', 'function': pentagon},
    {'name': 'шестиугольник', 'function': hexagon}
]

print('Возможные фигуры:')
for counter, value in enumerate(figures):
    print(counter, ':', value['name'])

selected_figure = input('Введите желаемую фигуру: ')

while selected_figure.isalpha() or int(selected_figure) > 3:
    print('Вы ввели некорректный номер!')
    selected_figure = input('Введите желаемую фигуру: ')
selected_figure = int(selected_figure)

figures[selected_figure]['function']()

sd.pause()

# зачет!
