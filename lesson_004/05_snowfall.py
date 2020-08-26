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

_flakes = dict(x=[], y=[], size=[])

for i in range(N):
    _flakes['x'].append(sd.random_number(0, sd.resolution[0]))
    _flakes['y'].append(sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
    _flakes['size'].append(sd.random_number(10, 100))

while True:
    sd.start_drawing()
    if 'points' in locals():
        for index in range(N):
            sd.snowflake(center=points[index], length=_flakes['size'][index], color=sd.background_color)
    points = []
    for index in range(N):
        point = sd.get_point(_flakes['x'][index], _flakes['y'][index])
        points.append(point)
        sd.snowflake(center=point, length=_flakes['size'][index])
        if _flakes['y'][index] > sd.random_number(0, 40):
            _flakes['y'][index] -= sd.random_number(2, 10)
            _flakes['x'][index] += sd.random_number(-5, 5)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

#
sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
