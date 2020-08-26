# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
BRICK_X, BRICK_Y = 100, 50

row = 0

for y in range(0, sd.resolution[1], BRICK_Y):
    row += 1
    for x in range(0, sd.resolution[0], BRICK_X):
        x0 = x if row % 2 else x + BRICK_X // 2
        left_bottom = sd.get_point(x0, y)
        right_top = sd.get_point(x0 + BRICK_X, y + BRICK_Y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_DARK_ORANGE)

sd.pause()

# зачет!
