"""2.2. Условный оператор."""

# +
# Сравнение строк
# кодировка: функция ord() выдает кодировку буквы
# chr() - принимает код и выдает букву

print(ord("a"), ord("A"))  # англ
print(ord("а"), ord("А"))  # русс
# -

# Проверка вхождения с in
text = input()
if "добр" in text:
    print("Встретилось 'доброе' слово.")
else:
    print("Добрых слов не найдено.")

# Match-case
# | используется как or
color = input()
match color:
    case "красный" | "жёлтый":
        print("Стоп.")
    case "зелёный":
        print("Можно ехать.")
    case _:
        print("Некорректное значение.")

# **Ключевые выводы параграфа**
# Условные операторы if, elif, else позволяют выполнять разные действия в зависимости от условий.
# Логические операции and, or, not помогают объединять несколько условий.
# Строки сравниваются по кодировке символов; для правильного сравнения регистр нужно приводить к одному виду.
# Оператор in проверяет вхождение элементов в строки и коллекции.
# Конструкция match-case и встроенные функции, такие как len(), max(), min(), abs(), расширяют возможности проверки условий.

# # ЗАДАЧИ

# Задание 1 (Просто здравствуй, просто как дела)
name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
mood = input("Как дела?\n")
if mood == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")

# +
# Задание 2 (Кто быстрее?)
speed1 = int(input())
speed2 = int(input())

if speed1 > speed2:
    print("Петя")
else:
    print("Вася")

# +
# Задание 3 (Кто быстрее на этот раз?)
speed1 = int(input())
speed2 = int(input())
speed3 = int(input())

if max(speed1, speed2, speed3) == speed1:
    print("Петя")
elif max(speed1, speed2, speed3) == speed2:
    print("Вася")
else:
    print("Толя")

# +
# Задание 4 (Список победителей)
speed1 = int(input())
speed2 = int(input())
speed3 = int(input())

spisok = sorted([speed1, speed2, speed3], reverse=True)
position = 1
for i in spisok:
    if i == speed1:
        name = "Петя"
    elif i == speed2:
        name = "Вася"
    else:
        name = "Толя"
    print(f"{position}. {name}")
    position += 1

# +
# Задание 5 (Яблоки)
petya_apples = 7  # У Пети было 7 яблок
vasya_apples = 6  # У Васи было 6 яблок

petya_apples -= 3
vasya_apples += 3
petya_apples += 2

vasya_apples += 5
vasya_apples -= 2

n1 = int(input())
m1 = int(input())

petya_apples += n1
vasya_apples += m1

if petya_apples > vasya_apples:
    print("Петя")
else:
    print("Вася")
# -

# Задание 6 (Сила прокрастинации)
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

# Задание 7 (А роза упала на лапу Азора)
word = input()
if word[0] == word[3]:
    if word[1] == word[2]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

# Задание 8 (Зайка — 1)
nature = input()
if "зайка" in nature:
    print("YES")
else:
    print("NO")

# +
# Задание 9 (Первому игроку приготовиться)
name1 = input()
name2 = input()
name3 = input()

print(min(name1, name2, name3))

# +
# Задание 10 (Лучшая защита — шифрование)
number = int(input())
a1 = number // 100
b1 = number // 10 % 10
c1 = number % 10

ones = c1 + b1
tens = a1 + b1

if tens >= ones:
    print(str(tens) + str(ones))
else:
    print(str(ones) + str(tens))

# +
# Задание 11 (Красота спасёт мир)
number = int(input())
a1 = number // 100
b1 = number // 10 % 10
c1 = number % 10

spisok = [a1, b1, c1]
maximum = max(spisok)
spisok.remove(maximum)
minimum = min(spisok)
spisok.remove(minimum)

if (maximum + minimum) == (sum(spisok) * 2):
    print("YES")
else:
    print("NO")

# +
# Задание 12 (Музыкальный инструмент)
a1 = int(input())
b1 = int(input())
c1 = int(input())

if a1 + b1 > c1:
    if c1 + b1 > a1:
        if c1 + a1 > b1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

# +
# Задание 13 (Властелин Чисел: Братство общей цифры)

num1 = input()  # Вместо a1
num2 = input()  # Вместо b1
num3 = input()  # Вместо c1

digits1 = [int(d) for d in num1]  # Вместо spisok_a
digits2 = [int(d) for d in num2]  # Вместо spisok_b
digits3 = [int(d) for d in num3]  # Вместо spisok_c

# Проверяем первую цифру первого числа на наличие в других числах
if digits1[0] in digits2 and digits1[0] in digits3:
    print(digits1[0])
else:
    print(digits1[1])

# +
# Задание 14 (Властелин Чисел: Две Башни)
number1 = input()
spisok_0 = [int(i) for i in number1]
spisok_1 = [int(i) for i in number1]

# ищем минимальное число
spisok_0.remove(max(spisok_0))
if 0 in spisok_0:
    spisok_0 = sorted(spisok_0, reverse=True)
else:
    spisok_0 = sorted(spisok_0)

# ищем максимальное число
spisok_1.remove(min(spisok_1))
spisok_1 = sorted(spisok_1, reverse=True)


print(str(spisok_0[0]) + str(spisok_0[1]), str(spisok_1[0]) + str(spisok_1[1]))

# +
# Задание 15 (Властелин Чисел: Возвращение Цезаря)
a2 = input()
b2 = input()
spisok = [int(i) for i in (a2 + b2)]

maximum = max(spisok)
spisok.remove(maximum)

minimum = min(spisok)
spisok.remove(minimum)

average = sum(spisok) % 10

print(str(maximum) + str(average) + str(minimum))

# +
# Задание 16 (Легенды велогонок возвращаются: кто быстрее?)
petya = int(input())
vasya = int(input())
tolya = int(input())

spisok = [petya, vasya, tolya]

maximum = max(spisok)
if petya == maximum:
    first = "Петя"
elif vasya == maximum:
    first = "Вася"
else:
    first = "Толя"
spisok.remove(maximum)

maximum = min(spisok)
if petya == maximum:
    Third = "Петя"
elif vasya == maximum:
    Third = "Вася"
else:
    Third = "Толя"
spisok.remove(maximum)

average = spisok[0]
if petya == average:
    second = "Петя"
elif vasya == average:
    second = "Вася"
else:
    second = "Толя"

print(f"{first:^24}")
print(f"{second:^8}")
print(f"{Third:>22}")
print("   II      I      III   ")

# +
# Задание 17 (Корень зла)
a3 = float(input())
b3 = float(input())
c3 = float(input())

# все коэффициенты равны нулю;
if a3 == b3 == c3 == 0:
    print("Infinite solutions")
# коэффициенты a и b равны нулю;
elif a3 == b3 == 0:
    print("No solution")
# только a = 0;
elif a3 == 0:
    x3 = -c3 / b3
    print(x3)
# коэффициент a не равен нулю;
else:
    # если b и c равны нулю
    if b3 == c3 == 0:
        print(0.00)
    # если b и c не равны нулю
    else:
        d3 = b3**2 - 4 * a3 * c3
        if d3 < 0:
            print("No solution")
        elif d3 == 0:
            x3 = -b3 / (2 * a3)
            print(x3)
        else:
            x_2 = (-b3 - d3**0.5) / (2 * a3)
            x_1 = (-b3 + d3**0.5) / (2 * a3)
            print(min(x_2, x_1), max(x_2, x_1))

# +
# Задание 18 (Территория зла)
a4 = int(input())
b4 = int(input())
c4 = int(input())

spisok_t = [a4, b4, c4]
c4 = max(a4, b4, c4)
spisok_t.remove(c4)
a4, b4 = spisok_t[0], spisok_t[1]
# доказать прямоугольный ли через теорему Пифагора: c² = a² + b²
if c4**2 == a4**2 + b4**2:
    print("100%")
if c4**2 > a4**2 + b4**2:
    print("велика")
if c4**2 < a4**2 + b4**2:
    print("крайне мала")

# +
# Задание 19 (Автоматизация безопасности)
x1 = float(input())
y1 = float(input())

cond_1 = ((x1 + 1) ** 2) / 4 - 9 <= y1
cond_2 = y1 <= 5
cond_3 = x1**2 + y1**2 <= 25
cond_4 = y1 <= (5 * x1 + 35) / 3

# Присваиваем условие переменной is_in_danger_zone
is_in_danger_zone = cond_1 and cond_2 and cond_3 and cond_4

if x1**2 + y1**2 >= 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif is_in_danger_zone:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# Задание 20 (Зайка — 2)
line1 = input().strip()
line2 = input().strip()
line3 = input().strip()

candidates = []

if "зайка" in line1:
    candidates.append(line1)
if "зайка" in line2:
    candidates.append(line2)
if "зайка" in line3:
    candidates.append(line3)

if candidates:
    # min автоматически выбирает лексикографически меньшую строку
    # лексикографическая порядок - упорядочивание по алфавиту
    # (оценивается вся строка, каждая буква слова)
    chosen = min(candidates)
    print(chosen, len(chosen))
