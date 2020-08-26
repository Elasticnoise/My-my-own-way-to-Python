# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x1 = 50
# x2 = 350
# width = 4
# for color in rainbow_colors:
#     point = sd.get_point(x1, 50)
#     point_end = sd.get_point(x2, 450)
#     sd.line(start_point=point, end_point=point_end, color=color, width=width)
#     x1 += 5
#     x2 += 5

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(370, 30)
radius = 400
for color in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=color, width=20)
    radius += 20


sd.pause()

# зачет!
