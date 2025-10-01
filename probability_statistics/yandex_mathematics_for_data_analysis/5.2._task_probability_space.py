"""5 Блок.

5.2. Вероятностное пространство.
"""

# +
# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
# Задача A. Подкидывания монетки
import sys
from math import comb

def main1():
    """Подкидывания монетки."""
    n, k = map(int, input().split())
    p = float(input())
    
    probability = 0
    for i in range(k, n + 1):  # от k орлов и до более высчитываем кол-во комбинаций и веру
        # comb(n, i) - количество способов получить i орлов в n бросках
        probability += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    
    print(probability)



# +
# Задача B. Геометрическая вероятность
# import sys
from scipy.integrate import quad


def main2():
    """Геометрическая вероятность."""
    c, d = map(float, input().split())
    # Определяем нашу функцию
    def length_at_x(x):
    # Для данного x, находим допустимый диапазон y (тк не можем установить границы OY)
        if x >= d:          # Если x уже больше d, то y должен быть отрицательным
            return 0        # Но y не может быть < 0!
        elif x <= d - c:    # Если x достаточно мал, то y может быть до C
            return c        # Но y не может быть > C!
        else:               # Нормальный случай
            return d - x    # y от 0 до (d-x)
    
    # Вычисляем интеграл от 0 до c
    piece_s, error = quad(length_at_x, 0, c)
    general_s = c ** 2

    print(piece_s / general_s)


# почему не прокатит def f(x): return d - x? тк если прямая будет пересекать или даже не касаться квадрата - 
# будет появляться отрицательная площадь (высчитывается то, что ниже OX). А нам этого не нада

# +
# Задача C. Модель выбора шаров разных цветов из урны
# import sys
# from math import comb

def main3():
    """Модель выбора шаров разных цветов из урны."""
    r, g, b = map(int, input().split())
    all_ball = r + g + b
    # сочетание без возвращения
    # берем по 3 из мешка. Хотя бы 1 зеленый = 1 - никогда зеленый
    probability_green = 1 - comb(r + b, 3) / comb(all_ball, 3)  # 1 - вера(выпадет крас и син)
    probability_color = (comb(r, 3) + comb(g, 3) + comb(b, 3))/ comb(all_ball, 3)
    print(probability_green)
    print(probability_color)




# +
# Задача D. Проверка монетки на честность
# import sys
import math

def main4():
    """Проверка монетки на честность."""
    data = input().split()
    n = int(data[0])          # количество бросков
    I = float(data[1]) # уровень доверия (например 0.9)
    results = list(map(int, input().split())) # результаты бросков

    # Считаем сколько орлов выпало в реальности
    real_heads = sum(results)

    # Считаем вероятности для честной монетки
    probabilities = []  # сумма должна получиться 1
    for k in range(n + 1):
        # Сколько способов получить k орлов
        ways = math.comb(n, k)
        # Вероятность получить ровно k орлов
        # вера конкретной последовательности
        prob = ways * (0.5 ** n)  # чтобы получить 2 орла и 1 решку = 0.5*0.5*0.5
        probabilities.append(prob)

    # Находим границы доверительного интервала
    K = 0
    for candidate in range(n // 2 + 1):
        # Считаем вероятность попасть в интервал [candidate, n-candidate]
        total_prob = sum(probabilities[candidate : n - candidate + 1])
        
        if total_prob >= I:
            K = candidate  # запоминаем подходящее значение
        else:
            break  # остановимся, когда вероятность станет слишком мала

    # Выводим ответ
    lower = K
    upper = n - K
    print(lower, upper)

    # Проверяем монетку
    if lower <= real_heads <= upper:
        print("fair")    # честная
    else:
        print("biased")  # нечестная
