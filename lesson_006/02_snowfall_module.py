# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#     #  нарисовать_снежинки_цветом(color=sd.background_color)
#     #  сдвинуть_снежинки()
#     #  нарисовать_снежинки_цветом(color)
#     #  если есть номера_достигших_низа_экрана() то
#     #       удалить_снежинки(номера)
#     #       создать_снежинки(count)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


sf.create_snowflakes(n=20)
while True:
    sd.start_drawing()
    sf.draw_snowflakes_in_color(color=sd.background_color)
    sf.move_snowflakes()
    sf.draw_snowflakes_in_color(color=sd.COLOR_WHITE)
    fallen_flakes = sf.get_fallen_snowflakes()
    if fallen_flakes:
        sf.remove_snowflakes(fallen_flakes_value=fallen_flakes)
        sf.create_snowflakes(n=len(fallen_flakes))

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
