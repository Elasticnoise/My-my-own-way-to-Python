# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)

# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#

global _flakes
global _quantity
global fallen_flakes
fallen_flakes = []


def create_snowflakes(n=0):
    global _flakes
    global _quantity
    if n == len(fallen_flakes):
        _flakes['x'].append(sd.random_number(0, sd.resolution[0]))
        _flakes['y'].append(sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
        _flakes['size'].append(sd.random_number(10, 100))
    else:
        _quantity = n
        _flakes = dict(x=[], y=[], size=[])
        for i in range(_quantity):
            _flakes['x'].append(sd.random_number(0, sd.resolution[0]))
            _flakes['y'].append(sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
            _flakes['size'].append(sd.random_number(10, 100))


def draw_snowflakes_in_color(color):
    points = []
    for index in range(_quantity):
        point = sd.get_point(_flakes['x'][index], _flakes['y'][index])
        points.append(point)
        sd.snowflake(center=point, length=_flakes['size'][index], color=color)


def move_snowflakes():
    for index in range(_quantity):
        if _flakes['y'][index] > (-1)*(_flakes['size'][index]):
            _flakes['y'][index] -= sd.random_number(2, 10)
            _flakes['x'][index] += sd.random_number(-5, 5)


def get_fallen_snowflakes():
    global fallen_flakes
    fallen_flakes = []
    for index in range(_quantity):
        if _flakes['y'][index] < (-1)*(_flakes['size'][index]):
            fallen_flakes.append(index)
    fallen_flakes.reverse()  # это достаточно делать один раз, вынес из цикла
    return fallen_flakes


def remove_snowflakes(fallen_flakes_value):
    for i in fallen_flakes_value:
        _flakes['x'].pop(i)
        _flakes['y'].pop(i)
        _flakes['size'].pop(i)
        fallen_flakes_value.remove(i)
