"""3.5. Потоковый ввод/вывод. Работа с текстовыми файлами. JSON."""

# ### стандартный поток ввода — stdin.
# Это поток, в который попадают все строки, вводимые пользователем. Программа может забирать их одну за другой, пока не достигнет конца ввода.

# **Подключение stdin**
# from sys import stdin

# <!-- # stdin — это итератор, по его строкам можно пройти в цикле
# # поэлементный перебор -->
# from sys import stdin
#
# lines = []
# for line in stdin:
#     lines.append(line)
#     # Если мешает (\n)
#     # удаление внутри новой строки и добавление чистой
#     # lines.append(line.rstrip("\n"))
# print(lines)  # ['Первая\n', 'Вторая\n', 'Третья\n']
# <!-- # этот код работает только с py -->

# <!-- # Чтение всех строк сразу
# # нет поэлементного перебора
# # с помощью readlines() -->
# from sys import stdin
#
# lines = stdin.readlines()
# print(lines)
# <!-- # тот же самый вывод, что и в предыдущем -->

# <!-- # Чтение всего ввода в одну строку -->
# from sys import stdin
#
# text = stdin.read()
# print([text])  # ['Первая\nВторая\nТретья\n']
#
# <!-- "\n" - видно, но когда использем split(), он также воспринимается как пробел и не нужно его убирать -->

# ### Какие методы позволяют считывать и записывать данные из текстовых файлов

# ### чтение файла

# Функция open()
#
# open(file, mode='r', encoding=None)
#
# Аргумент mode определяет режим доступа к файлу:
#
# 'r' — чтение (по умолчанию).
# Файл должен существовать, иначе будет ошибка.
# 'w' — запись с очисткой содержимого.
# Если файл существует, его содержимое удаляется. Если не существует — создаётся.
# 'a' — добавление в конец файла.
# Новый текст будет дописан после уже имеющегося. Если файл не существует — создаётся.
# 'r+' — чтение и запись, без удаления содержимого.
# Файл должен существовать. Запись идёт поверх существующего текста, начиная с начала файла.
# 'w+' — чтение и запись, с удалением содержимого.
# Файл очищается или создаётся заново. Подходит, если вы хотите сначала записать, а потом прочитать.
# 'a+' — чтение и добавление.
# Файл открывается в режиме добавления, но можно также его читать. При записи — курсор всегда в конце.

# <!-- # Построчное чтение файла -->
# file_in = open("python\\yandex\\sss\\input_1.txt", encoding="UTF-8")
# for line in file_in:
#     print(line)
#     # чтобы избавиться от пустых строк
#     # print(line.rstrip("\n"))
# file_in.close()
# <!-- # появляются пустые строки, тк удваивается \n (в самой строке и print) -->

# Не нужно одновреименно использовать стандартный ввод и чтение файла. тк стандартный ввод это как создание текста в консоли и после его вывод, а чтение - мы обращаемся к уже определенному файлу

# file_in = open("python\\yandex\\sss\\input_1.txt", encoding="UTF-8")
# <!-- # lines = file_in.readlines()
# # ['Привет!\n', 'Это пример текстового файла.\n', 'А это - последняя строка, которая заканчивается переходом на новую.\n'] -->
# lines = file_in.read()  # вывод в точности как в файле
# print(lines)
# file_in.close()

# <!-- # Чтение первых 10 символов файла -->
# with open("input_1.txt", encoding="UTF-8") as file_in:
#     symbols = file_in.read(10)
# print([symbols])
#
# <!-- # Вывод программы:
# # ['Привет!\nЭт']
# # Если в методе read() не указать количество считываемых символов, то прочитается весь файл. -->

# ### Закрытие файла

# <!-- # with вместо file_in.close() -->
# with open("input_1.txt", encoding="UTF-8") as file_in:
#     for line in file_in:
#         print(line.rstrip("\n"))

# ### Запись в файл

# Для записи в файл его необходимо сначала открыть в режиме записи (выше мы говорили о режимах доступа).
# Для записи данных из строковой переменной используется метод write():

# <!-- # Запись в файл - метод write() -->
# with open("output_1.txt", "w", encoding="UTF-8") as file_out:
#     n = file_out.write("Это первая строка\nА вот и вторая\nИ третья -- последняя\n")
#
# print(n)
#
# <!-- # Что делает программа:
#
# # 1.Открывает (или создаёт) файл output_1.txt в режиме записи. Если файл уже существует, его содержимое будет удалено.
# # 2.Записывает в него одну строку с символами перевода строки \n внутри — это создаст три строки в файле.
# # 3.Метод write() возвращает количество записанных символов, включая все пробелы и \n.
# # 4.Эта длина (в нашем случае — 55) выводится в консоль. -->

# <!-- # Запись списка строк - writelines() -->
# lines = ["Это первая строка\n", "А вот и вторая\n", "И третья - последняя\n"]
# with open("output_2.txt", "w", encoding="UTF-8") as file_out:
#     file_out.writelines(lines)
#
# <!-- # Содержимое выходного файла:
# # Это первая строка
# # А вот и вторая
# # И третья - последняя -->

# <!-- # Использование print() для записи в файл -->
#
# with open("output_3.txt", "w", encoding="UTF-8") as file_out:
#     print("Вывод в файл с помощью функции print()", file=file_out)
#
# <!-- # Содержимое выходного файла:
# # Вывод в файл с помощью функции print() -->

# ### Как устроен формат JSON и чем он отличается от обычного текста

# хранит в себе структурированные данные, выглядит как список

# ```python
# # Чтение JSON-файла - метод load()
# import json
# from pprint import pprint
#
# with open("data.json", encoding="UTF-8") as file_in:
#     records = json.load(
#         file_in
#     )  #  преобразует его в Python-объект (в твоём случае — список словарей).
# pprint(records)
#
# # Вывод программы:
# # [{'date_of_birth': '01.01.2001',
# #   'first_name': 'Иван',
# #   'group_number': 1,
# #   'last_name': 'Иванов',
# #   'patronymic': 'Иванович',
# #   'phone_numbers': ['+7 111 111 1111', '+7 111 111 1112']},
# #  {'date_of_birth': '10.10.2001',
# #   'first_name': 'Пётр',
# #   'group_number': 1,
# #   'last_name': 'Петров',
# #   'patronymic': 'Петрович',
# #   'phone_numbers': ['+7 111 111 1113', '+7 111 111 1114']}]
#
# # Из примера видно, что JSON-файл был преобразован в список словарей, а каждый словарь — это запись с информацией о студенте. Для обработки таких объектов можно применять стандартные методы и операции Python.
# ```

# ### Запись JSON-файла
#
# После того как вы изменили структуру данных в программе (например, обновили одно из полей словаря), результат можно сохранить обратно в JSON-файл.

# Запись JSON-файла - dump()
#
# Он преобразует объект Python в строку в формате JSON и записывает её в файл.
#
# Аргументы
# ensure_ascii — если True (по умолчанию), все не-ASCII-символы сохраняются как \uXXXX. При False сохраняются как есть (нужно для букв на кириллице).
#
# indent — задаёт отступы для форматирования:
# None (по умолчанию) — весь JSON в одну строку;
# число — количество пробелов на уровень вложенности (количество пробелов от начала строки).
#
# sort_keys — если True, ключи в словаре будут отсортированы.

# import json
#
# with open("data.json", encoding="UTF-8") as file_in:  # читаем и исправляем
#     records = json.load(file_in)
# records[1]["group_number"] = 2  # работаем как со словарем
# with open("data.json", "w", encoding="UTF-8") as file_out:  # запись в новый файл
#     json.dump(records, file_out, ensure_ascii=False, indent=2)  # Перезаписал файл

# <!-- # Преобразование ключей словаря
# # Модуль json автоматически преобразует ключи словаря в строки, если они были, например, целыми числами. -->
# import json
#
# records = {
#     1: "First",
#     2: "Second",
#     3: "Third"
# }
#
# with open("output.json", "w", encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent=2)

# <!-- # методы seek() и tell() -->
# with open('example.txt', 'rb') as file:
#     file.seek(0, 2)  # Перемещаемся в конец файла (seek только перемещает курсор)
#     end_pos = file.tell()  # Получаем позицию (размер файла в байтах)
#     print(f"Размер файла: {end_pos} байт")
#
# <!-- # file.seek(offset, whence):
# # offset — смещение в байтах.
#
# # whence — точка отсчёта:
# # 0 (по умолчанию) — от начала файла.
# # 1 — от текущей позиции.
# # 2 — от конца файла. -->

# <!-- # задание L
# # from sys import stdin -->
# import json
#
# # json_file_data1 = stdin.read().splitlines()
# # json_file_name1 = json_file_data1[0]
# # json_file_updates = json_file_data1[1]
#
# with open('python\\yandex\\sss\\users.json', encoding="UTF-8") as file_out, open('python\\yandex\\sss\\updates.json', encoding="UTF-8") as file_in:
#     json_records = json.load(file_out)  # список словарей
#     new_json = dict()
#     for person in json_records:
#         keys = list(person.keys())[1:]  # Берём все ключи, кроме первого
#         new_json[person['name']] = {key: person[key] for key in keys}
#
#     json_updates = json.load(file_in)  # список словарей
#     for new_info in json_updates:
#         upd_keys = list(new_info.keys())[1:]
#         for upd_key in upd_keys:
#             val = new_json[new_info['name']].get(upd_key, 0)
#             if val != 0:
#                 if new_json[new_info['name']][upd_key] < new_info[upd_key]:
#                     new_json[new_info['name']][upd_key] = new_info[upd_key]
#             else:
#                 new_json[new_info['name']][upd_key] = new_info[upd_key]
# with open('python\\yandex\\sss\\users_copy.json', "w", encoding="UTF-8") as file_out_me:
#     json.dump(new_json, file_out_me, ensure_ascii=False, indent=4)

# text = '᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!'.split()
# for i in text:
#     for b in i:
#         print(chr(ord(b) % 128))

# Ошибка возникает из-за неправильного разбора бинарных данных. Давайте разберём проблему и исправим код.
#
# ### Проблемы в вашем коде:
#
# 1. **Синтаксическая ошибка**:
#    - Вы пытаетесь разбить строку по `\x`, но в Python `\x` внутри строки должно сопровождаться HEX-кодом (например, `\x00`)
#    - Просто `split('\x')` вызывает синтаксическую ошибку
#
# 2. **Неправильный подход к разбору**:
#    - Вы пытаетесь обрабатывать бинарные данные как текст, что неверно
#    - Для бинарных данных нужно использовать байтовые строки
#
# ### Исправленный код:
#
# ```python
# with open("numbers.num", "rb") as f:  # Открываем файл в бинарном режиме
#     data = f.read()  # Читаем байты
#     result = 0
#
#     # Обрабатываем по 2 байта (для 2-байтных чисел)
#     for i in range(0, len(data), 2):
#         # Берем два байта и конвертируем в число
#         two_bytes = data[i : i + 2]
#         num = int.from_bytes(two_bytes, byteorder="big")
#         result += num
#
#     print(result % 2**16)
# ```
#
# ### Ключевые исправления:
#
# 1. **Бинарный режим чтения** (`"rb"`) - правильно читает байты
# 2. **Правильная обработка 2-байтных чисел**:
#    - Читаем файл как последовательность байтов
#    - Берем по 2 байта за раз
#    - Конвертируем в число с помощью `int.from_bytes()`
# 3. **Удалены ошибочные операции** с `split('\x')`
#
# ### Почему это работает:
#
# 1. Файл содержит последовательность 2-байтных чисел в бинарном формате
# 2. Каждые 2 байта представляют одно число в big-endian порядке
# 3. `int.from_bytes()` правильно преобразует байты в целое число
#
# ### Если порядок байт little-endian:
# Замените `byteorder='big'` на `byteorder='little'`
#
# ### PEP8 совместимость:
# Код теперь соответствует стандартам PEP8:
# - Правильные отступы
# - Пробелы вокруг операторов
# - Осмысленные имена переменных
#
# Попробуйте этот исправленный вариант - он должен работать корректно с бинарными файлами, содержащими 2-байтные числа.

# не понимаю. объясни как начинающему. почему мы обрабатываем по 2, однако число состоит из 4 цифр и они разделены \x
#
# 1. **Как выглядят данные в файле**
#    Ваш файл содержит не текст `"0001 0002..."`, а бинарные данные в виде:
#    `\x00\x01\x00\x02\x00\x03\x00\x04\x00\x05`
#    (Это видно из ошибки `ValueError` в вашем первом сообщении)
#
# 2. **Что такое `\x00\x01`**
#    - `\x` - это способ записи одного байта в шестнадцатеричном виде
#    - `\x00` = байт `00` (ноль)
#    - `\x01` = байт `01` (единица)
#    - Вместе `\x00\x01` = два байта, которые представляют число `0001` в HEX
#
# 3. **Почему split('\x') не работает**
#    - В Python нельзя просто взять и разбить строку по `\x`
#    - `\x` - это служебный символ для записи байтов, а не часть данных
#
# ### Как правильно читать такие данные (простой способ)
#
# ```python
# with open("numbers.num", "rb") as f:  # 'rb' - читаем как бинарные данные
#     data = f.read()  # Получаем байты: b'\x00\x01\x00\x02\x00\x03\x00\x04\x00\x05'
#
#     result = 0
#     # Проходим по данным с шагом 2 (каждые 2 байта = 1 число)
#     for i in range(0, len(data), 2):
#         # Берём два байта
#         byte1 = data[i]
#         byte2 = data[i + 1]
#
#         # Собираем их в число (первый байт - старший)
#         num = (byte1 << 8) + byte2
#         result += num
#
#     print(result)  # Выведет 15 для вашего примера
# ```
#
# ### Почему шаг 2, если в числе 4 цифры?
#
# 1. **4 HEX-цифры = 2 байта**
#    - Каждая HEX-цифра = 4 бита
#    - 4 цифры = 16 бит = 2 байта
#    - Поэтому `0001` хранится как `\x00\x01`
#
# 2. **Как это работает в коде**
#    - `\x00\x01` → byte1=0, byte2=1 → (0 << 8) + 1 = 1
#    - `\x00\x02` → byte1=0, byte2=2 → (0 << 8) + 2 = 2
#    - ...
#    - Сумма: 1 + 2 + 3 + 4 + 5 = 15
#
# ### Альтернативный вариант (если данные всё же текстовые)
#
# Если файл на самом деле содержит текст `"0001 0002 0003 0004 0005"` (можно открыть в блокноте и проверить), то правильный код:
#
# ```python
# with open("numbers.num", "r") as f:
#     text = f.read()  # Получаем строку "0001 0002 0003 0004 0005"
#     numbers = text.split()  # Разбиваем по пробелам
#
#     result = 0
#     for hex_num in numbers:
#         num = int(hex_num, 16)  # Переводим HEX-строку в число
#         result += num
#
#     print(result)  # Выведет 15
# ```
#
# ### Как определить, какой вариант нужен?
#
# 1. Откройте файл в обычном блокноте:
#    - Если видите `0001 0002...` → используйте текстовый вариант
#    - Если видите кракозябры или `\x00\x01...` → используйте бинарный вариант
#
# 2. Или добавьте в начало программы проверку:
# ```python
# with open("numbers.num", "rb") as f:
#     data = f.read(10)  # Читаем первые 10 байт
#     print(data)  # Покажет, что действительно в файле
# ```
#
# Это должно прояснить ситуацию. Если остались вопросы - спрашивайте!

# +
# 1

import json
import os
import sys
from sys import stdin

total: int = 0

for input_val in stdin:
    total += sum(map(int, input_val.split(" ")))
print(total)

# +
# 2


avrg_before: int = 0
avrg_after: int = 0
pupils_count: int = 0

for pupil_line in stdin:
    avrg_before += int(pupil_line.split(" ")[1])
    avrg_after += int(pupil_line.split(" ")[2])
    pupils_count += 1
height_diff = round(avrg_after / pupils_count - avrg_before / pupils_count)
print(height_diff)

# +
# 3


for program_line in stdin:
    comment_start_index = program_line.find("#")

    if comment_start_index != -1:
        cleaned_program_line = program_line[:comment_start_index]
        if cleaned_program_line.strip():
            print(cleaned_program_line)
    else:
        print(program_line, end="")

# +
# 4


title_lines = stdin.readlines()

titles = title_lines[:-1]
query = title_lines[-1].strip()

for title in titles:
    if title.lower().find(query.lower()) > -1:
        print(title, end="")

# +
# 5


palindromes = []

for ln in stdin:
    words = ln.split()
    for word in words:
        cleaned_word = word.strip().lower()
        if cleaned_word == cleaned_word[::-1]:
            palindromes.append(word.strip())

for word in sorted(set(palindromes)):
    print(word)

# +
# 6


translit_map = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "y",
    "э": "e",
    "ю": "iu",
    "я": "ia",
    "ъ": "",
    "ь": "",
    "Ъ": "",
    "Ь": "",
}

input_file = "cyrillic.txt"
output_file = "transliteration.txt"


with open(input_file, encoding="utf-8") as infile:
    text = infile.read()

transliterated_text = "".join(translit_map.get(char, char) for char in text)

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(transliterated_text)

# +
# 7


file_name = stdin.read().strip()

stats_numbers: list[int] = []

with open(file_name, encoding="UTF-8") as file_with_numbers:
    for number_line in file_with_numbers:
        stats_numbers.extend(int(nmb) for nmb in number_line.split())

print(len(stats_numbers))
print(len([pos_nmb for pos_nmb in stats_numbers if pos_nmb > 0]))
print(min(stats_numbers))
print(max(stats_numbers))
print(sum(stats_numbers))
print(f"{sum(stats_numbers) / len(stats_numbers):.2f}")

# +
# 8


unique_words: set[str] = set()
file_names = stdin.read().splitlines()
file_names_in = file_names[:-1]
file_name_out = file_names[-1]


for file_name in file_names_in:
    with open(file_name, encoding="UTF-8") as file_in:
        file_words = []
        for words_line in file_in:
            file_words.extend(words_line.split())
        unique_words ^= set(file_words)

with open(file_name_out, "w", encoding="UTF-8") as file_out:
    for word in sorted(unique_words):
        print(word, file=file_out)

# +
# 9


util_file_names = stdin.read().splitlines()
util_file_name_in = util_file_names[0]
util_file_name_out = util_file_names[1]

cleaned_lines: list[list[str]] = []

with open(util_file_name_in, encoding="UTF-8") as file_in:
    for text_line in file_in:
        words = text_line.strip().replace("\t", "").split()
        if words:
            cleaned_lines.append(words)

with open(util_file_name_out, "w", encoding="UTF-8") as file_out:
    for words_list in cleaned_lines:
        file_out.write(" ".join(words_list) + "\n")

# +
# 10


tail_file_input = stdin.read().splitlines()
tail_file_name = tail_file_input[0]
tail_file_lines = tail_file_input[1]

tail_data = []

with open(tail_file_name, encoding="UTF-8") as file_in:
    for ln in file_in:
        tail_data.append(ln)
for tail_line in tail_data[-int(tail_file_lines) :]:
    print(tail_line, end="")

# +
# 11


user_input_files = stdin.read().splitlines()
user_input_number_file = user_input_files[0]
user_input_statistics_file = user_input_files[1]

nmb_ls_full: list[int] = []

with open(user_input_number_file, encoding="UTF-8") as file_in:
    for ln in file_in:
        nmb_ls_full.extend(int(nmb_inp) for nmb_inp in ln.split())

with open(user_input_statistics_file, "w", encoding="UTF-8") as file_out:
    positive_count = len(list(filter(lambda vl: vl > 0, nmb_ls_full)))
    json.dump(
        {
            "count": len(nmb_ls_full),
            "positive_count": positive_count,
            "min": min(nmb_ls_full),
            "max": max(nmb_ls_full),
            "sum": sum(nmb_ls_full),
            "average": f"{sum(nmb_ls_full) / len(nmb_ls_full):.2f}",
        },
        file_out,
        ensure_ascii=False,
        indent=4,
    )

# +
# 12


input_files = stdin.read().splitlines()
input_file = input_files[0]
even_file = input_files[1]
odd_file = input_files[2]
eq_file = input_files[3]

with open(input_file, encoding="utf-8") as f_in, open(
    even_file, "w", encoding="utf-8"
) as f_even, open(odd_file, "w", encoding="utf-8") as f_odd, open(
    eq_file, "w", encoding="utf-8"
) as f_eq:

    for line in f_in:
        numbers = line.strip().split()
        even_numbers = []
        odd_numbers = []
        eq_numbers = []

        for num in numbers:
            evens = sum(1 for digit in num if int(digit) % 2 == 0)
            odds = len(num) - evens

            if evens > odds:
                even_numbers.append(num)
            elif odds > evens:
                odd_numbers.append(num)
            else:
                eq_numbers.append(num)

        f_even.write(" ".join(even_numbers) + "\n")
        f_odd.write(" ".join(odd_numbers) + "\n")
        f_eq.write(" ".join(eq_numbers) + "\n")

# +
# 13


user_inout_json_changes = stdin.read().splitlines()
user_json_file_name = user_inout_json_changes[0]
user_json_file_changes = user_inout_json_changes[1:]

with open(user_json_file_name, encoding="UTF-8") as file_in:
    json_records = json.load(file_in)

    for change in user_json_file_changes:
        [key, val] = change.split(" == ")
        json_records[key] = val

    with open(user_json_file_name, "w", encoding="UTF-8") as file_out:
        json.dump(json_records, file_out, ensure_ascii=False, indent=2)

# +
# 14


users_file, users_updates_file = stdin.read().splitlines()

with open(users_file, encoding="UTF-8") as file:
    users_data = json.load(file)

with open(users_updates_file, encoding="UTF-8") as file:
    users_updates_data = json.load(file)

result: dict[str, dict[str, str]] = {}
for user in users_data + users_updates_data:
    name = user["name"]
    if name not in result:
        result[name] = {}

    for key, value in user.items():
        if key == "name":
            continue

        result[name][key] = max(value, result[name].get(key, value))

with open(users_file, "w", encoding="UTF-8") as file:
    json.dump(result, file, indent=4)

# +
# 15


usr_answr = [line.strip() for line in stdin.read().splitlines()]

with open("scoring.json", encoding="UTF-8") as file:
    test_groups = json.load(file)

total_score = 0
index = 0

for group in test_groups:
    group_points = group["points"]
    tests = group["tests"]
    test_count = len(tests)
    points_per_test = group_points / test_count
    passed_tests = 0

    for test in tests:
        if index < len(usr_answr) and usr_answr[index] == test["pattern"]:
            passed_tests += 1
        index += 1

    total_score += int(passed_tests * points_per_test)

print(total_score)

# +
# 16


search_input_params = sys.stdin.read().splitlines()
search_query = " ".join(search_input_params[0].split()).lower()
search_files = search_input_params[1:]

found_files = []

for srch_fl in search_files:
    with open(srch_fl, encoding="UTF-8") as srch_file_in:
        file_content = " ".join(srch_file_in.read().split()).lower()
        if search_query in file_content:
            found_files.append(srch_fl)

if found_files:
    print("\n".join(found_files))
else:
    print("404. Not Found")

# +
# 17

with open("secret.txt", encoding="UTF-8") as f:
    print("".join([chr(ord(i) % 128) for i in f.read()]))

# +
# 18


size = os.path.getsize(input())
if size > 1024**3 - 1:
    size = int(size / 1024**3) + 1
    postfix = "ГБ"
elif size > 1024**2 - 1:
    size = int(size / 1024**2) + 1
    postfix = "МБ"
elif size > 1023:
    size = int(size / 1024) + 1
    postfix = "КБ"
else:
    postfix = "Б"
print(str(size) + postfix)

# +
# 19


shift = int(sys.stdin.read().strip())

with open("public.txt", encoding="UTF-8") as file:
    text = file.read()

encrypted_text = ""
for char in text:
    if "a" <= char <= "z":
        encrypted_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        encrypted_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    else:
        encrypted_text += char

with open("private.txt", "w", encoding="UTF-8") as file:
    file.write(encrypted_text)

# +
# 20

with open("numbers.num", "rb") as file:
    total_sum = 0
    while chunk := file.read(2):
        if len(chunk) < 2:
            continue
        total_sum += int.from_bytes(chunk, byteorder="big")

print(total_sum % 2**16)
