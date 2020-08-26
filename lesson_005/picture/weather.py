# -*- coding: utf-8 -*-
import simple_draw as sd


def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    point = sd.get_point(400, 50)
    radius = 1000
    for color in rainbow_colors:
        sd.circle(center_position=point, radius=radius, color=color, width=20)
        radius += 20


def sun():
    point = sd.get_point(100, 700)
    sd.circle(center_position=point, radius=40, width=0)
    for angle in range(0, 360, 20):
        v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v1.draw(color=sd.COLOR_YELLOW)
