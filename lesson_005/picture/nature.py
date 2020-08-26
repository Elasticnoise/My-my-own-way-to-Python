# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

root_point = sd.get_point(1000, 100)


def draw_branches(start_point=root_point, angle=90, length=150):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=5)
    v2 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=5)
    if length < 30:
        v1.draw(color=sd.COLOR_GREEN, width=1)
        v2.draw(color=sd.COLOR_GREEN, width=1)
    else:
        v1.draw(color=sd.COLOR_DARK_GREEN)
        v2.draw(color=sd.COLOR_DARK_GREEN)
    next_point = v1.end_point
    next_length = length * 0.75
    next_angle = angle - 30
    next_angle1 = angle + 30
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    draw_branches(start_point=next_point, angle=next_angle1, length=next_length)


left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(sd.resolution[0] * 2.25, 100)


def ground():
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_YELLOW, width=0)
