# -*- coding: utf-8 -*-
from random import randint
global _secret_number


def make_number():
    global _secret_number
    generate_num = set(str(randint(1000, 9999)))
    while len(generate_num) < 4:
        generate_num.add(str(randint(0, 9)))
    saved_number = list(generate_num)
    if saved_number[0] == '0':
        saved_number.reverse()
        _secret_number = (list(saved_number))
    else:
        _secret_number = (list(generate_num))
    return _secret_number


def check_number(input_number):
    quantity_bulls = 0
    quantity_cows = 0

    for i in range(len(input_number)):
        for j in _secret_number:
            if _secret_number[i] == input_number[i]:
                quantity_bulls += 1
            if input_number[i] == j:
                quantity_cows += 1
    bulls = quantity_bulls // 4
    cows = quantity_cows - bulls
    result = {'bulls': bulls, 'cows': cows}
    return result
