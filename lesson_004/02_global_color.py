# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = [
    {'name': 'красный', 'code': sd.COLOR_RED},
    {'name': 'оранжевый', 'code': sd.COLOR_ORANGE},
    {'name': 'желтый', 'code': sd.COLOR_YELLOW},
    {'name': 'зеленый', 'code': sd.COLOR_GREEN},
    {'name': 'циан', 'code': sd.COLOR_CYAN},
    {'name': 'синий', 'code': sd.COLOR_BLUE},
    {'name': 'фиолетовый', 'code': sd.COLOR_PURPLE}
]


def triangle(point, angle, color, length=50):
    for next_angle in range(0, 360, 120):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw(color=color)
        point = v.end_point


def square(point, angle, color, length=50):
    for next_angle in range(0, 360, 90):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw(color=color)
        point = v.end_point


def pentagon(point, angle, color, length=50):
    for next_angle in range(0, 360, 72):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw(color=color)
        point = v.end_point


def hexagon(point, angle, color, length=50):
    for next_angle in range(0, 360, 60):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=3)
        v.draw(color=color)
        point = v.end_point


print('Возможные цвета:')

for counter, value in enumerate(colors):
    print(counter, ':', value['name'])

selecting_color = input('Введите желаемый цвет: ')
while selecting_color.isalpha() or int(selecting_color) > 6:
    print('Вы ввели некорректный номер!')
    selecting_color = input('Введите желаемый цвет: ')
selected_color = colors[int(selecting_color)]['code']

point0 = sd.get_point(100, 100)
triangle(point=point0, angle=20, length=100, color=selected_color)
point1 = sd.get_point(400, 100)
square(point=point1, angle=20, length=100, color=selected_color)
point2 = sd.get_point(100, 400)
pentagon(point=point2, angle=20, length=100, color=selected_color)
point3 = sd.get_point(400, 400)
pentagon(point=point3, angle=20, length=100, color=selected_color)

sd.pause()

# зачет!
