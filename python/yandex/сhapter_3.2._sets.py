"""Sets."""

# Множества и словари - коллекции — неупорядоченные типы данных (в отличие от строк, списков и кортежей)

# ### Множества (set)
#
# Множество — это тип коллекции, в которой автоматически удаляются повторяющиеся значения, а порядок не сохраняется. У множеств нет индексов, но с ними можно выполнять полезные операции: быстро проверять наличие элемента, находить пересечения и объединения, удалять дубли.
#
# **Создание множества и преобразование из других коллекций**
#
# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
#
# **Неупорядоченность и уникальность**
# Элементы не имеют фиксированного порядка
# Элементы не повторяются
#
# **Проверка принадлежности**
# if letter.lower() in vowels:
#     print("Гласная буква")
#
# **Перебор элементов множества**
# for letter in vowels:
#
# **Операции над множествами**
# - Объединяет два множества — результат содержит все элементы из обоих. Повторы исключаются.
# Оператор: | или метод union().
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1 | s_2
# # s_union = s_1.union(s_2)
# print(s_union)
# ```
# Вывод программы:
# {1, 2, 3, 4, 5}
#
# - Пересечение. Возвращает только те элементы, которые есть в обоих множествах
# Оператор: & или метод intersection().
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1 & s_2
# # s_intersection = s_1.intersection(s_2)
# print(s_intersection)
# ```
# Вывод программы:
# {3}
#
# -  Разность множеств. Возвращает элементы из первого множества, которых нет во втором.
# Оператор: - или метод difference().
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_dif = s_1 - s_2
# # s_dif = s_1.difference(s_2)
# print(s_dif)
# ```
# s_2 - s_1 != s_1 - s_2
#
# Вывод программы:
# {1, 2}
#
# - Возвращает элементы, которые есть только в одном из двух множеств (в первом или втором, но не в обоих).
# ![image.png](attachment:image.png)
# Оператор: ^ или метод symmetric_difference()
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_sym_dif = s_1 ^ s_2
# # s_sym_dif = s_1.symmetric_difference(s_2)
# print(s_sym_dif)
# ```
# Вывод программы:
# {1, 2, 4, 5}
#
#
# **Ограничение на элементы множества**
# !!!Множество в Python может состоять только из неизменяемых объектов.
# Если попытаться включить во множество изменяемый объект, возникнет ошибка TypeError: unhashable type.
#
# Ниже представлен пример, где используются допустимые элементы для создания множества
# a = [1, 2, 3, 4, 3, 2, 3, 1, 3, 4, 2, 2, 2]
# # Удаляем дубликаты, преобразуя список в множество, а затем обратно в список
# a = list(set(a))
# print(a)
#
# А ниже представлен плохой пример создания множества
# b = [[1, 2, 3, 4],
#      [3, 2, 3, 1],
#      [3, 4, 2, 2]]
# b = set(b)
# print(b)
#
# Элементы, которые мы пытаемся поместить в множество b, сами являются списками. Поскольку списки в Python — изменяемые структуры данных, они не могут быть элементами множества. При попытке создать множество, содержащее изменяемый объект, возникнет ошибка TypeError: unhashable type
#
# Неизменяемыми (хэшируемыми) объектами, которые можно включать в множество, являются:
# Строки (str);
# Числа (int, float);
# Кортежи (tuple);
# frozenset (неизменяемое множество, о котором поговорим далее).
#
# valid_set = {"hello", 123, 3.14, (1, 2, 3)}
# print(valid_set)  # {3.14, 123, 'hello', (1, 2, 3)}
# Все элементы в valid_set являются неизменяемыми, поэтому множество создаётся успешно.
#
# **Преобразование множества в другие типы данных**

# ### Union
#
# Returns a set containing all unique elements from the combined sets.
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1 | s_2
# # s_union = s_1.union(s_2)
# print(s_union)
# ```
#
# ### Intersection
#
# Returns a set containing only the common elements of the intersecting sets.
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1 & s_2
# # s_intersection = s_1.intersection(s_2)
# print(s_intersection)
# ```
#
# ### Difference
#
# Returns a set containing elements from the first set that are not in the second (subtracted) set.
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_dif = s_1 - s_2
# # s_dif = s_1.difference(s_2)
# print(s_dif)
# ```
# ### Symmetric difference
#
# Returns a set containing elements that are in either of the sets but not in both.
#
# ```python
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_sym_dif = s_1 ^ s_2
# # s_sym_dif = s_1.symmetric_difference(s_2)
# print(s_sym_dif)
# ```
#
#
# ### Subset and Superset
#
# Subset (≤) – A set is a subset of another if all its elements are contained within the other set.
# Example: `{1, 2, 3} ≤ {1, 2, 3, 4} → True`
#
# Superset (≥) – A set is a superset of another if it contains all elements of the other set.
# Example: `{1, 2, 3, 4} ≥ {1, 2, 3} → True`
#
#
# ### Set Methods
#
# - `set.add(e)` – Adds an element to the set.
# - `set.remove(e)` – Removes an element; raises KeyError if the element is not found.
# - `set.discard(e)` – Removes an element if it exists; does nothing if it doesn’t.
# - `set.pop()` – Removes and returns an arbitrary element from the set.
# - `set.clear()` – Removes all elements from the set, leaving it empty.
#
# ### Dictionary Methods
#
# - `len(d)` – Returns the number of keys in the dictionary.
# - `del d[key]` – Removes a key from the dictionary; raises KeyError if the key is missing.
# - `dict.clear()` – Removes all keys and values from the dictionary.
# - `dict.copy()` – Returns a shallow copy of the dictionary.
# - `dict.get(key, default)` – Returns the value for key; if the key is missing, returns default.
# - `dict.items()` – Returns an iterable of key-value pairs as tuples.
# - `dict.keys()` – Returns an iterable of dictionary keys.
# - `dict.pop(key, default)` – Returns and removes the value of key; if missing, returns default.
# - `dict.values()` – Returns an iterable of dictionary values.

# ```python
# # преобразовать в список при помощи функции list:
#
# my_set = {1, 2, 3, 4, 5}
# my_list = list(my_set)
#
# print(my_list)  # [1, 2, 3, 4, 5]
# print(type(my_list))  # <class 'list'>
#
# # И также обратно из листа в множество
# ```

# ```python
# # преобразовать в строку при помощи функции str
#
# my_set = {1, 2, 3}
# my_str = str(my_set)
#
# print(my_str)  # "{1, 2, 3}"
# print(type(my_str))  # <class 'str'>
# # Результат будет включать фигурные скобки {} и кавычки ', что может быть неудобным.
# ```

# ```python
# # строковый метод join
#
# word_set = {"apple", "banana", "cherry"}
# text = ", ".join(word_set)
#
# print(text)  # banana, cherry, apple
# # Порядок элементов в строке может отличаться.
# # join не сработает для множество, в котором присутствует числа
# ```

# ```python
# # Чтобы объединить числовое множество в строку, нужно преобразовать числа в строки, например
#
# # через map:
# num_set = {1, 2, 3}
# text = ", ".join(map(str, num_set))
#
# # или генератор списков:
# num_set = {1, 2, 3}
# text = ", ".join([str(num) for num in num_set])
#
# print(text)  # '1, 2, 3'
# ```

# **Сравнение множеств**
# Проверяет, содержат ли два множества одни и те же элементы, независимо от порядка. Оператор: ==
#
# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2}
# print(s_1 == s_2) True
#
# Проверяет, входят ли все элементы одного множества в другое. Оператор: <=.
# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2) True
#
# Проверяет, содержит ли множество все элементы другого множества. Оператор: >=.
# s_1 = {1, 2, 3, 4}
# s_2 = {1, 2, 3}
# print(s1 >= s2) True
#
#
# **ПОДМНОЖЕСТВО**
# Множество A является подмножеством множества B (A ⊆ B), если все элементы A также содержатся в B.
#
# Виды подмножеств:
#     ➖ Нестрогое подмножество, обозначается как A ⊆ B — A может быть равным B;
#     ➖  Строгое подмножество, обозначается  A ⊂ B — A обязательно меньше B.
#
# Проверка на подмножество осуществляется при помощи операторов сравнения <, <= относительно левого операнда:
#
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 3}
#
# print(A <= B)  # True (A является подмножеством B)
# print(A < B)   # True (строгое подмножество)
# print(B < A)   # False (B не является подмножеством A)
# print(A <= C)  # True (A является подмножеством C)
# print(A < C)  # False (A не является строгим подмножеством C)
#
# **НАДМНОЖЕСТВО**
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 3}
#
# print(B >= A)  # True (B является надмножеством A)
# print(B > A)   # True (строгое надмножество)
# print(A > B)   # False (A не является надмножеством B)
# print(A >= C)  # True (A является надмножеством C)
# print(A > C)  # False (A не является строгим надмножеством C)

# ```python
#
# ```

# **Создание словаря через функцию dict()**
#
# city_codes = dict(moscow=495, saint_petersburg=812, penza=8412)
#
# print(city_codes)       # {'moscow': 495, 'saint_petersburg': 812, 'penza': 8412}
# print(type(city_codes)) # <class 'dict'>
#
# этот метод создания подходит **только для строковых ключей**, которые соответствуют правилам именования переменных (без пробелов, не начинаются с цифры и т.д.).
#
# Если необходимо использовать ключи других типов, таких как числа, кортежи или строки с пробелами, следует применять фигурные скобки {}. Пример:
#
# invalid_dict = dict(123=456)  # Ошибка!
# valid_dict = {123: 456}       # Работает
#
#
# **Создание словаря из списка пар**
# values = [['moscow', 495], ['saint petersburg', 812], ['penza', 8412]]
# city_codes = dict(values)
#
# print(city_codes)       # {'moscow': 495, 'saint petersburg': 812, 'penza': 8412}
# print(type(city_codes)) # <class 'dict'>
#
#
# **Обращение по ключу**
# Для получения значения по ключу используется следующий синтаксис:
# словарь[ключ]
#
# **Создание новой пары ключ:значение**
# словарь[новый ключ] = значение
#
# **Удаление пары ключ:значение**
# del словарь[ключ]
#
# **ключом может быть только неизменяемый объект**
# Неизменяемые объекты, которые могут быть ключами словаря:
#     ✅    Целые числа (int) и вещественные числа (float)
#     ✅    Строки (str)
#     ✅    None
#     ✅    Кортежи (tuple)
#     ✅    Неизменяемые множества (frozenset) (разберём в этом модуле)
#
# Изменяемые объекты, которые не могут быть ключами:
#     ❌    Списки (list)
#     ❌    Множества (set) (разберём позже)
#     ❌    Словари (dict)
#
# **значением может быть объект любого типа данных**

# **dict.get(key, default)**
# Описание
# Возвращает значение по ключу key. Если ключа нет, то возвращает значение default
# Пример:
#
# d = {"a": 1, "b": 2, "c": 3}
# print(d.get("e", "Ключа нет в словаре"))
# Вывод:
# Ключа нет в словаре
#
#
# **dict.items()**
# Описание
# Возвращает итерируемый объект, состоящий из кортежей (ключ, значение) словаря
#
# Пример:
# d = {"a": 1, "b": 2, "c": 3}
# for key, value in d.items():
#     print(key, value)
# Вывод:
# a 1
# b 2
# c 3
#
# **dict.keys()**
# Описание
# Возвращает итерируемый объект, состоящий из ключей словаря
#
# Пример:
# d = {"a": 1, "b": 2, "c": 3}
# for key in d.keys():
#     print(key)
# Вывод:
# a
# b
# c
#
# **d.pop(key, default)**
# Описание
# Возвращает значение по ключу key и удаляет его из словаря. Если ключа нет, то возвращает default
#
# Пример:
# d = {"a": 1, "b": 2, "c": 3}
# x = d.pop("a")
# print(x)
# Вывод:
# 1
#
#
# **dict.values()**
# Описание
# Возвращает итерируемый объект, состоящий из значений словаря
#
# Пример:
# d = {"a": 1, "b": 2, "c": 3}
# for value in d.values():
#     print(value)
# Вывод:
# 1
# 2
# 3

# **распаковка коллекции**
# print(*data, sep='')
#
#
# В Python символ * используется для распаковки итерируемых объектов, таких как списки, кортежи или множества. Когда вы пишете print(*data, sep=''), это означает, что все элементы из коллекции data будут переданы в функцию print как отдельные аргументы.
#
# Вот что происходит в вашем примере:
#
# • data — это итерируемый объект (например, список, кортеж или множество).
# • *data распаковывает элементы коллекции data, так что каждый элемент передается в print как отдельный аргумент.
# • Параметр sep='' указывает, что между элементами не должно быть пробелов или других разделителей.
#
# Таким образом, если data содержит, например, ['H', 'e', 'l', 'l', 'o'], то print(*data, sep='') выведет Hello без пробелов между буквами.

# +
# 1

entered_string = input()

unique_characters = set(entered_string)
for character in unique_characters:
    print(character, end="")

# +
# 2

value_1 = input()
value_2 = input()

print("".join(set(value_1) & set(value_2)))

# +
# 3

neighbourhood_count: int = int(input())

items = [set(input().split(" ")) for _ in range(neighbourhood_count)]

unique_items: set[str] = set()

for it in items:
    unique_items |= it

print("\n".join(unique_items))

# +
# 4

semolina_likes: int = int(input())
oatmeal_likes: int = int(input())

surnames_semolina_likes = [input() for _ in range(semolina_likes)]
surnames_oatmeal_likes = [input() for _ in range(oatmeal_likes)]

both_likes = set(surnames_semolina_likes) & set(surnames_oatmeal_likes)

if len(both_likes):
    print(len(both_likes))
else:
    print("Таких нет")

# +
# 5

semolina_prdg_likes: int = int(input())
oatmeal_prdg_likes: int = int(input())

surnames_prdg_likes = [
    input().strip() for _ in range(semolina_prdg_likes + oatmeal_prdg_likes)
]

one_prdg_like: dict[str, int] = {}


for surname in surnames_prdg_likes:
    if surname in one_prdg_like:
        one_prdg_like[surname] += 1
    else:
        one_prdg_like[surname] = 1

total_single_likes = 0
for surname, count in one_prdg_like.items():
    if count == 1:
        total_single_likes += 1

if total_single_likes == 0:
    print("Таких нет")
else:
    print(total_single_likes)

# +
# 6

semolina_prdg_lks: int = int(input())
oatmeal_prdg_lks: int = int(input())

surnames_prdg_likes = [
    input().strip() for _ in range(semolina_prdg_lks + oatmeal_prdg_lks)
]

only_one_prdg_like: dict[str, int] = {}


for surname in surnames_prdg_likes:
    if surname in only_one_prdg_like:
        only_one_prdg_like[surname] += 1
    else:
        only_one_prdg_like[surname] = 1

single_likes = sorted(
    [surname for surname, count in only_one_prdg_like.items() if count == 1]
)

if single_likes:
    for surname in single_likes:
        print(surname)
else:
    print("Таких нет")

# +
# 7

morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

input_text = input().strip().upper()
words = input_text.split()

for word in words:
    morse_word = " ".join(morse_dict[char] for char in word)
    print(morse_word)

# +
# 8

num_children = int(input())

children_porridge = {}

for _ in range(num_children):
    parts = input().split()
    surname = parts[0]
    porridges = set(parts[1:])
    children_porridge[surname] = porridges

target_porridge = input().strip()

loving_children = []

for surname, porridges in children_porridge.items():
    if target_porridge in porridges:
        loving_children.append(surname)

loving_children.sort()

if loving_children:
    for surname in loving_children:
        print(surname)
else:
    print("Таких нет")

# +
# 9

sightings: dict[str, int] = {}

while True:
    line = input().strip()
    if line == "":
        break
    for item in line.split():
        if item in sightings:
            sightings[item] += 1
        else:
            sightings[item] = 1

for item in sorted(sightings.keys()):
    print(item, sightings[item])

# +
# 10

translit_dict = {
    "А": "A",
    "а": "a",
    "Б": "B",
    "б": "b",
    "В": "V",
    "в": "v",
    "Г": "G",
    "г": "g",
    "Д": "D",
    "д": "d",
    "Е": "E",
    "е": "e",
    "Ё": "E",
    "ё": "e",
    "Ж": "ZH",
    "ж": "zh",
    "З": "Z",
    "з": "z",
    "И": "I",
    "и": "i",
    "Й": "I",
    "й": "i",
    "К": "K",
    "к": "k",
    "Л": "L",
    "л": "l",
    "М": "M",
    "м": "m",
    "Н": "N",
    "н": "n",
    "О": "O",
    "о": "o",
    "П": "P",
    "п": "p",
    "Р": "R",
    "р": "r",
    "С": "S",
    "с": "s",
    "Т": "T",
    "т": "t",
    "У": "U",
    "у": "u",
    "Ф": "F",
    "ф": "f",
    "Х": "KH",
    "х": "kh",
    "Ц": "TC",
    "ц": "tc",
    "Ч": "CH",
    "ч": "ch",
    "Ш": "SH",
    "ш": "sh",
    "Щ": "SHCH",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "IU",
    "ю": "iu",
    "Я": "IA",
    "я": "ia",
    "Ъ": "",
    "ъ": "",
    "Ь": "",
    "ь": "",
}

text = input()

result = []
for char in text:
    if char in translit_dict:
        if char.isupper() and len(translit_dict[char]) > 1:
            first_character = translit_dict[char][0]
            second_character = translit_dict[char][1:]
            replacement = first_character + second_character.lower()
            result.append(replacement)
        else:
            result.append(translit_dict[char])
    else:
        result.append(char)

print("".join(result))

# +
# 11

num_employees = int(input())

surname_counts: dict[str, int] = {}

for _ in range(num_employees):
    surname = input().strip()
    if surname in surname_counts:
        surname_counts[surname] += 1
    else:
        surname_counts[surname] = 1

total_namesakes = 0
for count in surname_counts.values():
    if count > 1:
        total_namesakes += count

print(total_namesakes)

# +
# 12

num_employees = int(input())

surname_counts = {}

for _ in range(num_employees):
    surname = input().strip()
    if surname in surname_counts:
        surname_counts[surname] += 1
    else:
        surname_counts[surname] = 1

namesakes = []

for surname, count in surname_counts.items():
    if count > 1:
        namesakes.append((surname, count))

namesakes.sort()

if namesakes:
    for surname, count in namesakes:
        print(f"{surname} - {count}")
else:
    print("Однофамильцев нет")

# +
# 13

num_available_dishes = int(input())

available_dishes = set()
for _ in range(num_available_dishes):
    dish = input().strip()
    available_dishes.add(dish)

num_days = int(input())

cooked_dishes = set()

for _ in range(num_days):
    num_dishes_in_day = int(input())
    for _ in range(num_dishes_in_day):
        dish = input().strip()
        cooked_dishes.add(dish)

not_cooked_dishes = available_dishes - cooked_dishes

sorted_not_cooked_dishes = sorted(not_cooked_dishes)

if sorted_not_cooked_dishes:
    for dish in sorted_not_cooked_dishes:
        print(dish)
else:
    print("Готовить нечего")

# +
# 14

num_available_products = int(input())

available_products = set()
for _ in range(num_available_products):
    product = input().strip()
    available_products.add(product)

num_recipes = int(input())

cookable_dishes = []

for _ in range(num_recipes):
    dish_name = input().strip()
    num_ingredients = int(input())
    ingredients = set()
    for _ in range(num_ingredients):
        ingredient = input().strip()
        ingredients.add(ingredient)

    if ingredients <= available_products:
        cookable_dishes.append(dish_name)

cookable_dishes.sort()

if cookable_dishes:
    for dish in cookable_dishes:
        print(dish)
else:
    print("Готовить нечего")

# +
# 15

numbers: list[str] = [bin(int(el))[2:] for el in input().split()]

statistics: list[dict[str, int]] = []

for number in numbers:
    number_statistics = {}
    number_statistics["digits"] = len(number)
    number_statistics["units"] = number.count("1")
    number_statistics["zeros"] = number.count("0")
    statistics.append(number_statistics)

print(statistics)

# +
# 16

adjacent_objects = set()

while True:
    line = input().strip()
    if line == "":
        break
    words = line.split()
    for i, word in enumerate(words):
        if words[i] == "зайка":
            if i > 0:
                adjacent_objects.add(words[i - 1])
            if i < len(words) - 1:
                adjacent_objects.add(words[i + 1])

for obj in sorted(adjacent_objects):
    print(obj)

# +
# 17

friendships: dict[str, set[str]] = {}

while True:
    line = input().strip()
    if line == "":
        break
    person1, person2 = line.split()

    if person1 not in friendships:
        friendships[person1] = set()
    if person2 not in friendships:
        friendships[person2] = set()

    friendships[person1].add(person2)
    friendships[person2].add(person1)

for person in sorted(friendships):
    second_level_friends = set()
    for friend in friendships[person]:
        second_level_friends.update(friendships[friend])

    second_level_friends.discard(person)
    second_level_friends.difference_update(friendships[person])

    print(f"{person}: {', '.join(sorted(second_level_friends))}")

# +
# 18

point_counts = int(input())
points = [tuple(map(int, input().split())) for _ in range(point_counts)]

groups: dict[tuple[int, int], list[tuple[int, int]]] = {}

for x_coord, y_coord in points:
    key = (x_coord // 10, y_coord // 10)
    groups.setdefault(key, []).append((x_coord, y_coord))

max_length = 0

for key, group in groups.items():
    group.sort()
    current_length = 1
    max_group_length = 1

    for i in range(1, len(group)):
        x_prev, y_prev = group[i - 1]
        x_curr, y_curr = group[i]

        if (x_prev // 10 == x_curr // 10) and (y_prev // 10 == y_curr // 10):
            current_length += 1
        else:
            current_length = 1

        max_group_length = max(max_group_length, current_length)

    max_length = max(max_length, max_group_length)

print(max_length)

# +
# 19

children_counts = int(input())

children_toys = {}

toy_count: dict[str, int] = {}

for _ in range(children_counts):
    parts = input().split(": ")
    name = parts[0]
    toys = parts[1].split(", ")

    children_toys[name] = set(toys)

    for toy in set(toys):
        if toy in toy_count:
            toy_count[toy] += 1
        else:
            toy_count[toy] = 1

unique_toys = [toy for toy, count in toy_count.items() if count == 1]

unique_toys.sort()

for toy in unique_toys:
    print(toy)

# +
# 20


def compute_gcd(val_1: int, val_2: int) -> int:
    """Return greatest common divisor."""
    while val_2:
        val_1, val_2 = val_2, val_1 % val_2
    return val_1


input_data = input().strip()
numbers_list: list[int] = list(map(int, input_data.split("; ")))

unique_numbers = []
for num in numbers_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
unique_numbers.sort()

coprime_dict = {}

for num in unique_numbers:
    coprime_list = []
    for other_num in unique_numbers:
        if num != other_num and compute_gcd(num, other_num) == 1:
            coprime_list.append(other_num)
    if coprime_list:
        coprime_dict[num] = coprime_list

for num in sorted(coprime_dict.keys()):
    coprime_numbers = ", ".join(map(str, sorted(coprime_dict[num])))
    print(f"{num} - {coprime_numbers}")
