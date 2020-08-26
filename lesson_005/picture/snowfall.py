# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snowfall():
    flakes = dict(x=[], y=[], size=[])

    for i in range(N):
        flakes['x'].append(sd.random_number(0, sd.resolution[0] // 5))
        flakes['y'].append(sd.random_number(sd.resolution[1] - 400, sd.resolution[1] - 200))
        flakes['size'].append(sd.random_number(5, 30))

    while True:
        sd.start_drawing()
        if 'points' in locals():
            for index in range(N):
                sd.snowflake(center=points[index], length=flakes['size'][index], color=sd.background_color)
        points = []
        for index in range(N):
            point = sd.get_point(flakes['x'][index], flakes['y'][index])
            points.append(point)
            sd.snowflake(center=point, length=flakes['size'][index])
            if flakes['y'][index] > sd.random_number(130, 160):
                flakes['y'][index] -= sd.random_number(2, 10)
                flakes['x'][index] += sd.random_number(-5, 5)

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
