# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, color=color, width=50)
    eye_left = sd.get_point(x - 20, y + 20)
    eye_right = sd.get_point(x + 20, y + 20)
    mask_left_bottom = sd.get_point(x - 35, y - 30)
    mask_right_top = sd.get_point(x + 35, y)
    mask_lace_right = sd.get_point(x + 50, y + 5)
    mask_lace_left_start = sd.get_point(x - 35, y)
    mask_lace_left_end = sd.get_point(x - 50, y + 5)
    sd.circle(center_position=eye_left, radius=15, color=sd.COLOR_BLUE, width=10)
    sd.circle(center_position=eye_right, radius=15, color=sd.COLOR_BLUE, width=10)
    sd.rectangle(left_bottom=mask_left_bottom, right_top=mask_right_top, color=sd.COLOR_WHITE)
    sd.line(start_point=mask_right_top, end_point=mask_lace_right, color=sd.COLOR_WHITE)
    sd.line(start_point=mask_lace_left_start, end_point=mask_lace_left_end, color=sd.COLOR_WHITE)
# smile(100, 200, sd.COLOR_YELLOW)


def smile_random():
    for _ in range(10):
        x = sd.random_number(0, 600)
        y = sd.random_number(0, 600)
        smile(x, y, sd.COLOR_YELLOW)


smile_random()
sd.pause()

# зачет!
