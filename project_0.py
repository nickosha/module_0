import numpy as np
def game_core_v2(number):
    '''Функция принимает загаданное число и возвращает число попыток'''
    number_lst = [x for x in range(1,101)]
    predict = number_lst[round(len(number_lst)/2)]
    count = 1
    while number != predict:
        count += 1
        if number > predict:
            number_lst = number_lst[number_lst.index(predict)+1:]
            predict = number_lst[round(len(number_lst)/2)]
        elif number < predict:
            number_lst = number_lst[:number_lst.index(predict)]
            predict = number_lst[round(len(number_lst)/2)]
    return(count) # выход из цикла, если угадали
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v2)