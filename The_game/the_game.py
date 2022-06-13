"""Игра угадай число
Компьютер сам загадывает и сам угадывает число при минимальном числе попыток
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """ Угадываем число методом горячо-холодно

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 0
    max = 101
    
    print(number)
    
    while True:
        count += 1
        predict_number = min + (max - min) // 2  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        if number < predict_number:  # если загаданное число меньше
            max = predict_number     # снижаем максимум
        else: min = predict_number   # иначе (если загаданное число больше) - повышаем минимум   
    print('count=', count)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []      # пустой список количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # список "загаданных" чисел

    for number in random_array:
        count_ls.append(random_predict(number))  # заполняем список количества попыток

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

# RUN
score_game(random_predict)