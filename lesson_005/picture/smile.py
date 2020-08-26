# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


def draw_smile(x, y, color):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=55, color=color, width=50)
    eye_left = sd.get_point(x - 20, y + 20)
    eye_right = sd.get_point(x + 20, y + 20)
    mask_left_bottom = sd.get_point(x - 35, y - 30)
    mask_right_top = sd.get_point(x + 35, y)
    mask_lace_right = sd.get_point(x + 50, y + 5)
    mask_lace_left_start = sd.get_point(x - 35, y)
    mask_lace_left_end = sd.get_point(x - 50, y + 5)
    sd.circle(center_position=eye_left, radius=10, color=sd.COLOR_BLUE, width=10)
    sd.circle(center_position=eye_right, radius=10, color=sd.COLOR_BLUE, width=10)
    sd.rectangle(left_bottom=mask_left_bottom, right_top=mask_right_top, color=sd.COLOR_DARK_CYAN)
    sd.line(start_point=mask_right_top, end_point=mask_lace_right, color=sd.COLOR_DARK_CYAN)
    sd.line(start_point=mask_lace_left_start, end_point=mask_lace_left_end, color=sd.COLOR_DARK_CYAN)
