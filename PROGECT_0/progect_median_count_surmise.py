# Теперь необходимо создать алгоритм, который проделает данную операцию 1000 раз и 
# вычислит среднее арифметическое количества попыток.

import numpy as np
from progect_game import surmise_number


def median_count_surmise(surmise_number, N=1000) -> int:
    """Функция создает список из N случайных чисел, которые будет угадывать компьютер.
    Количество попыток на отгадывание заносится в список и считается среднее значение
    попыток угадывания за N итераций.

    Args:
        surmise_number (int): функция угадывания
        N (int): количество итераций

    Returns:
        int: среднее число угадываний за N попыток
    """
    #np.random.seed(1)
    random_numbers_lst = np.random.randint(1, 101, size=N)
    counts_lst = []
    
    for counts in random_numbers_lst:
        counts_lst.append(surmise_number(counts))
        
    score = int(np.mean(counts_lst))
    
    # печатаем результат выполнения функции
    print(f'Среднее количество попыток для отгадывания: {score}')   
    
        
    
    return score

# Отделим запуск от импорта
if __name__ == "_main_":
    median_count_surmise(surmise_number, N=1000)