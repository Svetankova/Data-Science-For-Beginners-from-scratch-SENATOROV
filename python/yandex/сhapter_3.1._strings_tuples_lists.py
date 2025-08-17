"""3.1. Строки, кортежи, списки."""

# Если обратиться к индексу, которого нет в коллекции - ошибка

# ### Цикл с enumerate
# Если нужно и значение, и его индекс — поможет функция enumerate(). Она возвращает пары: индекс и элемент. Это особенно удобно, когда мы работаем с элементами, но ещё и хотим показать номер строки, порядковый номер слова и т.д.:
#
# ```python
# text = input()
# for i, letter in enumerate(text):
#     print(f"{i}. {letter}")
# ```
# Этот способ — универсальный и часто используется в реальных проектах: он делает код понятным и избавляет от необходимости отдельно отслеживать индекс.

# ```python
# # Неизменяемость строк
#
# # будет ошибка
# # s = "hello world"
# # s[4] = 'a'
#
# # 1 способ. Через срезы
# s = "hello world"
# new_s = s[:4] + "a" + s[5:]
#
# # 2 способ. Через .replace()
# s = "hello world"
# new_s = s.replace("o", "a")
#
# # 3 способ. Через преобразование строки
# s = "hello world"
# s_list = list(s)
# s_list[4] = "a"
# new_s = "".join(s_list)
#
# # Списки же - изменяемые коллекции
# ```

# Методы строк
# Методы — это инструмент, «принадлежащий» конкретному типу данных.
#
# **islower()**
#
# **str.capitalize()**
# Описание
# Возвращает копию строки, у которой первая буква заглавная, а остальные приведены к строчным
#
# Пример:
# s = "hello, World!"
# s.capitalize()
#
# Результат:
# Hello, world!
#
#
# **str.count(sub)**
# Описание
# Возвращает количество неперекрывающихся вхождений подстроки sub. К примеру, если искать в строке «ААААА» неперекрывающиеся значения «АА», то первое вхождение будет «AAAAA». Второе — «AAAAA». Больше неперекрывающихся вхождений нет. Так, поиск последующих вхождений подстроки происходит с индекса, который следует за последним найденным вхождением
#
# Пример:
# s = "Hello, world!"
# s.count("l")
#
# Результат:
# 3
#
#
# **str.endswith(suffix)**
# Описание
# Возвращает True, если строка оканчивается на подстроку suffix. Иначе возвращает False. suffix может быть кортежем проверяемых окончаний строки
#
# Пример:
# s = "Hello, world!"
# s.endswith("world!")
#
# Результат:
# True
#
# **str.find(sub)**
# используется для поиска подстроки в строке и возвращает индекс первого вхождения этой подстроки. Если подстрока не найдена, метод возвращает -1.
#
#
# **str.index(sub)**
# Работает как .find, но если подстрока не найдена - ValueError
#
#
# **str.isalnum()**
# Описание
# Возвращает True, если все символы строки являются буквами и цифрами и в строке есть хотя бы один символ. Иначе возвращает False
#
# Пример:
# s = "abc123"
# s.isalnum()
#
# Результат:
# True
#
#
# **str.isalpha()**
# Описание
# Возвращает True, если все символы строки являются буквами и в строке есть хотя бы один символ. Иначе возвращает False
#
# Пример:
# s = "Letters"
# s.isalpha()
# Результат:
#
# True
#
# **str.lstrip(chars)**
# Описание
# Возвращает строку, у которой в начале удалены символы, встречающиеся в строке chars. Если значение chars не задано, то пробельные символы удаляются
#
# Пример:
#
# Скопировать код
# s = "BCCAstring"
# s.lstrip("ABC")
# Результат:
#
# "string"
#
# но те, что в середине или в конце - нет
# s = "BCCAstrABCABingABC" => strABCABingABC
#
# **str.strip(chars)**
# Описание
# Возвращает строку, у которой в начале и в конце удалены символы, встречающиеся в строке chars. Если значение chars не задано, то пробельные символы удаляются
#
# Пример:
# s = "abc Hello, world! cba"
# s.strip(" abc")
#
# Результат:
# "Hello, world!"
#
# s = "BCCA   strABCABing   ABC" => пробелы остаются

# **s.insert(i, x)**
# Описание
# Вставляет элемент x в список по индексу i
#
# Пример:
#
# Скопировать код
# s = [1, 3, 4]
# s.insert(1, 2)
# print(s)
# Результат:
#
# [1, 2, 3, 4]
#
#
# **s.sort()**
# Описание
# Сортирует список по возрастанию, меняя исходный список
# **sorted(s)**
# Описание
# Возвращает отсортированный по возрастанию список, не меняя исходный.
# reverse=True используется обоими

# В Python неизменяемость кортежа означает, что после создания кортежа его элементы не могут быть изменены, удалены или добавлены. Это основное отличие от списков, которые являются изменяемыми.
#
# Более подробно:
#
# Нельзя изменить значения элементов:
# Если у вас есть кортеж (1, 2, 3), вы не сможете изменить его на (4, 2, 3) после создания.
#
# Нельзя добавить новые элементы:
#
# Нельзя использовать методы, такие как append() или extend(), чтобы добавить новые элементы в кортеж.
#
# Нельзя удалить элементы:
#
# Нельзя использовать методы, такие как remove() или pop(), чтобы удалить элементы из кортежа.

# append(element): Добавляет переданный element как один элемент в конец списка. element может быть любым объектом, включая другой список.
#
#     my_list = [1, 2, 3]
#     my_list.append([4, 5])
#     print(my_list)  # Вывод: [1, 2, 3, [4, 5]]
# extend(iterable): Добавляет элементы из итерируемого объекта iterable в конец списка, по одному элементу за раз.
# Python
#
#     my_list = [1, 2, 3]
#     my_list.extend([4, 5])
#     print(my_list)  # Вывод: [1, 2, 3, 4, 5]

# +
# 1

count: int = int(input())
is_all_correct: bool = True
allowed_letters = ("а", "б", "в")

for _ in range(count):
    word = input()
    if not word.startswith(allowed_letters):
        is_all_correct = False

print("YES" if is_all_correct else "NO")

# +
# 2

value: str = input()
for i, char in enumerate(value):
    print(char)

# +
# 3

expected_title_length: int = int(input())
title_count: int = int(input())

for i in range(title_count):
    title: str = input()
    if len(title) > expected_title_length:
        result_title = title[: expected_title_length - 3] + "..."
    else:
        result_title = title
    print(result_title)

# +
# 4

while input_value := input():
    if not input_value:
        break
    result: str = input_value
    if input_value.endswith("@@@"):
        continue
    if input_value.startswith("##"):
        result = input_value[2:]
    print(result)

# +
# 5

input_string: str = input()

characters = list(input_string)
characters.reverse()
new_value = "".join(characters)

if input_string == new_value:
    print("YES")
else:
    print("NO")

# +
# 6

input_string_count = int(input())

count = 0

for _ in range(input_string_count):
    count += input().split().count("зайка")

print(count)

# +
# 7

input_sum_string: str = input()
values = input_sum_string.split(" ")
total_sum: int = 0

for value in values:
    total_sum += int(value)

print(total_sum)

# +
# 8

neighborhood_count: int = int(input())

for _ in range(neighborhood_count):
    neighborhood_desc: str = input()
    index = neighborhood_desc.find("зайка")
    if index < 0:
        print("Заек нет =(")
    else:
        print(index + 1)

# +
# 9

while True:
    line = input()
    if not line:
        break
    comment_index = line.find("#")
    if comment_index > -1:
        line = line[:comment_index]
    if line:
        print(line)

# +
# 10


frequencies: dict[str, int] = {}

while True:
    line = input().strip()
    if line == "ФИНИШ":
        break
    for char in line.lower():
        if char != " ":
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

most_common_char = ""
max_freq = -1

for char, freq in frequencies.items():
    if freq > max_freq or (freq == max_freq and char < most_common_char):
        max_freq = freq
        most_common_char = char

print(most_common_char)

# +
# 11

title_count = int(input())

titles = [input().strip() for _ in range(title_count)]

query = input().strip().lower()

for title in titles:
    if query in title.lower():
        print(title)

# +
# 12

porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

days = int(input())

for day in range(days):
    print(porridges[day % 5])

# +
# 13

number_count = int(input())

numbers_list = [int(input()) for _ in range(number_count)]

exponent = int(input())

for number in numbers_list:
    print(number**exponent)

# +
# 14

numbers = input().split()
exponent = int(input())

print(" ".join(str(int(number) ** exponent) for number in numbers))

# +
# 15


def gcd(first_nmb: int, second_nmb: int) -> int:
    """Return greatest common divisor."""
    while second_nmb != 0:
        first_nmb, second_nmb = second_nmb, first_nmb % second_nmb
    return first_nmb


input_numbers: list[int] = list(map(int, input().split()))

output_result: int = input_numbers[0]
for num in input_numbers[1:]:
    output_result = gcd(output_result, num)

print(output_result)

# +
# 16

max_length = int(input())
lines = []

for _ in range(int(input())):
    lines.append(input())

for line in lines:
    if max_length > 3:
        if len(line) >= max_length - 3:
            line = line[: max_length - 3] + "..."
        else:
            if max_length == 4:
                line = line + "..."

        print(line)
        max_length -= len(line)

# +
# 17

input_string = input()

cleaned_string = input_string.replace(" ", "").lower()

if cleaned_string == cleaned_string[::-1]:
    print("YES")
else:
    print("NO")

# +
# 18

input_string = input()

current_char = input_string[0]
count = 1

for char in input_string[1:]:
    if char == current_char:
        count += 1
    else:
        print(current_char, count)
        current_char = char
        count = 1

print(current_char, count)

# +
# 19


expression = input().split()

operand_stack: list[int] = []

for token in expression:
    if token in "+-*/":
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        operation_result: int = 0
        if token == "+":
            operation_result = operand1 + operand2
        elif token == "-":
            operation_result = operand1 - operand2
        elif token == "*":
            operation_result = operand1 * operand2
        elif token == "/":
            operation_result = operand1 // operand2

        operand_stack.append(operation_result)
    else:
        operand_stack.append(int(token))

print(operand_stack[0])

# +
# 20


def factorial(nmb: int) -> int:
    """Return the factorial of a number."""
    rsl: int = 1
    for multiplier_val in range(2, nmb + 1):
        rsl *= multiplier_val
    return rsl


expression_value: str = input().strip()
tokens: list[str] = expression_value.split()

stack: list[int] = []

for token in tokens:
    if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
        stack.append(int(token))
    elif token in {"+", "-", "*", "/"}:
        b_val: int = stack.pop()
        a_val: int = stack.pop()
        if token == "+":
            stack.append(a_val + b_val)
        elif token == "-":
            stack.append(a_val - b_val)
        elif token == "*":
            stack.append(a_val * b_val)
        elif token == "/":
            stack.append(a_val // b_val)
    elif token == "~":
        stack.append(-stack.pop())
    elif token == "!":
        stack.append(factorial(stack.pop()))
    elif token == "#":
        stack_value: int = stack[-1]
        stack.append(stack_value)
    elif token == "@":
        first: int = stack.pop()
        second: int = stack.pop()
        third: int = stack.pop()
        stack.extend([second, first, third])

print(stack.pop())
