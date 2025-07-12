"""2.1. Input and output of data."""

# КУРС "Основы Python" - https://education.yandex.ru/handbook/python
# стандарт оформления кода PEP8
# https://peps.python.org/pep-0008/
#
# Все стандарты PEP8
# https://peps.python.org

# +
# Выведем, например, фразу Добрый день, %имя%.

name = "Пользователь"

print("Добрый день,", name, ".")  # пробелы между всеми словами
print("Добрый день, ", name, ".", sep="")  # через sep заменили на пустоту
print(f"Добрый день, {name}.")  # f-строка

# +
# f-строка. настраивать выравнивание внутри строки

print(f"{123:0>9}")  # 000000123 (выравнивание по правому краю)
print(f"{123:0<9}")  # 123000000 (выравнивание по левому краю)
print(f"{123:0^9}")  # 000123000 (выравнивание по центру)
# -

# ### метод format().
# 'Применение метода format() в Python'
# https://pyhub.ru/python/lecture-5-12-26/
# ```python
# name = "Алиса"
# age = 25
# sentence = "Меня зовут {} и мне {} лет.".format(name, age)
# print(sentence)
# ```
#
# Позиционное форматирование
# ```python
# first_name = "Иван"
# last_name = "Иванов"
# formatted_string = "Фамилия: {1}, Имя: {0}".format(first_name, last_name)
# print(formatted_string)
# ```
#
# Именованное форматирование
# ```python
# sentence = "Меня зовут {name} и я живу в {city}.".format(name="Мария", city="Москва")
# print(sentence)
# ```

# Управляющие символы в строках
# Внутри строк можно использовать управляющие символы, начинающиеся с \ (бэкслеш):
#
# \n — переход на новую строку;
# \t — табуляция;
# \r — возврат каретки в начало строки;
# \b — возврат каретки на один символ.
# \\ - ввод в строке \

# Параметры sep и end в print()
# По умолчанию пробел и \n

# Округление.
print(f"{2 ** 0.5:.2f}")  # до двух знаков после запятой

# +
# Системы счисления (СС).

# из CC с основанием от 2 до 36 в 10ную

# int(<строка>,<основание>):
# строка, представляющая запись числа в соответствующей системе счисления;
# основание системы счисления.

binary_value = "1001"
print(int(binary_value, 2))  # воспринимает строку

# из 10ной в 2ную, 8ную или 16ную

# bin(x) → Двоичная система (основание 2)
bin(10)  # '0b1010'
# oct(x) → Восьмеричная система (основание 8)
oct(10)  # '0o12'
# hex(x) → Шестнадцатеричная система (основание 16)
hex(255)  # '0xff'

# Общие особенности:
# Все функции возвращают строку (не число).

# Префикс (0b, 0o, 0x) указывает на систему счисления.

# Отрицательные числа также поддерживаются: -0b101
# -

# # ЗАДАЧИ

# Задание 1 (Привет, Яндекс!)
print("Привет, Яндекс!")

# Задание 2 (Привет, всем!)
name = input("Как Вас зовут?")
print(f"Привет, {name}")

# Задание 3 (Излишняя автоматизация)
info = input()
print((info + "\n") * 3)

# Задание 4 (Сдача)
total = int(input())
change = int(total - 38 * 2.5)
print(change)

# +
# Задание 5 (Магазин)
price = int(input())
weight = int(input())
total = int(input())

print(total - price * weight)

# +
# Задание 6 (Чек)
name = input()
price = int(input())
weight = int(input())
total = int(input())

print(
    f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {price * weight}руб
Внесено: {total}руб
Сдача: {total - price * weight}руб"""
)
# -

# Задание 7 (Делу — время, потехе — час)
count = int(input())
print("Купи слона!\n" * count)

# Задание 8 (Наказание)
count = int(input())
text = input()
print(f'Я больше никогда не буду писать "{text}"!\n' * count)

# +
# Задание 9 (Деловая колбаса)
# 1 ребенок съедает 1 кусок за 2 минуты
# 1 ребенок 0.5 куска за 1 мин -> 0.5 кусок/мин
children = int(input())
minutes = int(input())

print(int(children * 0.5 * minutes))

# +
# Задание 10 (Детский сад — штаны на лямках)
name = input()
number = input()

print(
    f"""Группа №{number[0]}.  
{number[2]}. {name}.  
Шкафчик: {number}.  
Кроватка: {number[1]}."""
)
# -

# Задание 11 (Автоматизация игры)
abcd = int(input())
letter_d = (abcd % 10) * 10
letter_c = abcd % 100 // 10
letter_b = (abcd % 1000 // 100) * 1000
letter_a = (abcd // 1000) * 100
print(letter_a + letter_b + letter_c + letter_d)

# +
# Задание 12 (Интересное сложение)
letter_a = int(input())
letter_b = int(input())

result_3 = (letter_a % 10 + letter_b % 10) % 10
letter_a, letter_b = letter_a // 10, letter_b // 10
result_2 = ((letter_a % 10 + letter_b % 10) % 10) * 10
letter_a, letter_b = letter_a // 10, letter_b // 10
result_1 = ((letter_a % 10 + letter_b % 10) % 10) * 100
print(result_1 + result_2 + result_3)

# +
# Задание 13 (Дед Мороз и конфеты)
children = int(input())
candies = int(input())

print(candies // children)
print(candies % children)

# +
# Задание 14 (Шарики и ручки)
red = int(input())
green = int(input())
blue = int(input())

print(red + blue + 1)

# +
# Задание 15 (В ожидании доставки)
hour = int(input())
minute = int(input())
delivery_min = int(input())

minute = minute + delivery_min

hour = (hour + minute // 60) % 24
minute = minute % 60

formatted_hours = f"{hour:02d}"
formatted_minutes = f"{minute:02d}"

print(f"{formatted_hours}:{formatted_minutes}")

# +
# Задание 16 (Доставка)
letter_a = int(input())
letter_b = int(input())
letter_c = int(input())

print((letter_b - letter_a) / letter_c)
# -

# Задание 17 (Ошибка кассового аппарата)
total = int(input())
binary_value = input()
price = int(binary_value, 2)
print(total + price)

# Задание 18 (Сдача 10)
price = int(input(), 2)
total = int(input())
print(total - price)

# +
# Задание 19 (Украшение чека)
name = input()
price = int(input())
weight = int(input())
user_money = int(input())

print(f"{'Чек':=^35}")
print(f"{'Товар:':<10}{name:>25}")
print(f"{'Цена:':<10}{f'{weight}кг * {price}руб/кг':>25}")
print(f"{'Итого:':<10}{f'{weight * price}руб':>25}")
print(f"{'Внесено:':<10}{f'{user_money}руб':>25}")
print(f"{'Сдача:':<10}{f'{user_money - weight * price}руб':>25}")
print("=" * 35)

# +
# Задание 20 (Мухи отдельно, котлеты отдельно)
total_weight = int(input())
price = int(input())
cutlet1_price = int(input())
cutlet2_price = int(input())

y_coordinate = (price * total_weight - total_weight * cutlet1_price) / (
    cutlet2_price - cutlet1_price
)
x_coordinate = total_weight - y_coordinate
print(int(x_coordinate), int(y_coordinate))
