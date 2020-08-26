# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


def build_wall():
    BRICK_X, BRICK_Y = 20, 10

    row = 0

    for y in range(100, 350, BRICK_Y):
        row += 1
        for x in range(400, 700, BRICK_X):
            x0 = x if row % 2 else x + BRICK_X // 2
            left_bottom = sd.get_point(x0, y)
            right_top = sd.get_point(x0 + BRICK_X, y + BRICK_Y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_DARK_ORANGE)


def draw_polygon(point, angle, length, corners_quantity):
    new_point = point
    step_corner = 360 // corners_quantity
    for next_angle in range(0, 360 - step_corner, step_corner):
        v = sd.get_vector(start_point=point, angle=angle + next_angle, length=length, width=50)
        v.draw(color=sd.COLOR_DARK_RED)
        point = v.end_point
    sd.line(start_point=new_point, end_point=point, width=50, color=sd.COLOR_DARK_RED)


point0 = sd.get_point(400, 380)
point1 = sd.get_point(550, 470)
point2 = sd.get_point(475, 430)
point3 = sd.get_point(625, 430)
point4 = sd.get_point(550, 550)
point_frame_window = sd.get_point(495, 200)
point_window = sd.get_point(500, 205)


def build_roof():
    draw_polygon(point=point0, angle=0, length=300, corners_quantity=3)
    sd.circle(center_position=point1, radius=70, color=sd.COLOR_DARK_RED, width=0)
    sd.circle(center_position=point2, radius=60, color=sd.COLOR_DARK_RED, width=0)
    sd.circle(center_position=point3, radius=60, color=sd.COLOR_DARK_RED, width=0)
    sd.circle(center_position=point4, radius=60, color=sd.COLOR_DARK_RED, width=0)


def window():
    sd.square(left_bottom=point_frame_window, side=110, color=sd.COLOR_ORANGE, width=5)
    sd.square(left_bottom=point_window, side=100, color=sd.COLOR_WHITE, width=0)