"""Типы данных в Питоне."""

# ### Работа с числами

a1 = 25  # целое число (int)
b1 = 2.5  # число с плавающей точкой (float)
c1 = 3 + 25j  # комплексное число (complex)

# экспоненциальная запись, 2 умножить на 10 в степени 3
d1 = 2e3
print(d1)
print(type(d1))

# Арифметические операции

# сложение, вычитание, умножение, деление, возведение в степень
print(2 + 2, 4 - 2, 2 * 2, 4 / 2, 2**3)

# +
# новая для нас операция: разделим 7 на 2, и найдем целую часть и остаток

# целая часть
print(7 // 2)

# остаток от деления
print(7 % 2)
# -

# Операторы сравнения

# больше, меньше, больше или равно и меньше или равно
# print(4 > 2, 4 < 2, 4 >= 2, 4 <= 2)

# равенство
# print(2 == 4)
#
# и новый для нас оператор неравенства
# print(2 != 4)

# Логические операции

# логическое И, обе операции должны быть истинны
# print(4 > 2 and 2 != 3)
#
# логическое ИЛИ, хотя бы одна из операций должна быть истинна
# print(4 < 2 or 2 == 2)
#
# логическое НЕ, перевод истинного значения в ложное и наоборот
# print(not (4 == 4))

# Перевод чисел в другую систему счисления

# +
# создадим число в десятичной системе
d2 = 25

# переведем в двоичную (binary)
bin_d = bin(d2)
print(bin_d)

# переведем обратно в десятичную
print(int(bin_d, 2))

# +
# создадим число в десятичной системе
d3 = 25

# переведем в восьмеричную (octal)
oct_d = oct(d3)
print(oct_d)

# переведем обратно в десятичную
print(int(oct_d, 8))

# +
# создадим число в десятичной системе
d4 = 25

# переведем в шестандцатеричную (hexadecimal)
hex_d = hex(d4)
print(hex_d)

# переведем обратно в десятичную
print(int(hex_d, 16))
# -

# ### Строковые данные

string_1 = "это строка"
string_2 = "это тоже строка"

multi_string = """Мы все учились понемногу
Чему-нибудь и как-нибудь,
Так воспитаньем, слава богу,
У нас немудрено блеснуть."""

# Длина строки

# воспользуемся функцией len()
len(multi_string)

# Объединение строк

# +
# создадим три строки
a2, b2, c2 = "Программирование", "на", "Питоне"

# соединим с помощью + и добавим пробелы ' '
a2 + " " + b2 + " " + c2
# -

# Индекс символа в строке

# +
# выведем первый элемент строки multi_string
print(multi_string[0])

# теперь выведем последний элемент
print(multi_string[-1])
# -

# Срезы строк

# выберем элементы с четвертого по шестой
print(multi_string[3:6])

# +
# выведем все элементы вплоть до второго
print(multi_string[:2])

# а также все элементы, начиная с четвертого
print(multi_string[3:])
# -

# Циклы в строках

# выведем буквы в слове Питон
for i in "Питон":
    print(i)

# Методы .strip() и .split()

# +
# применим метод .strip(), чтобы удалить *
print("***15 849 302*****".strip("*"))

# если ничего не указать в качестве аргумента, то удаляются пробелы по краям строки
print(" 15 849 302 ".strip())
# -

# применим метод .split(), чтобы разделить строку на части
print(multi_string.split())

# посчитаем количество слов в тексте (длину списка)
len(multi_string.split())

# Замена символа в строке

# +
# предположим данные содержатся вот в таком формате
data = "20,25"

# теперь заменим ',' на '.'
data = data.replace(",", ".")

# и преобразуем в число
data1 = float(data)
print(data1)
print(type(data1))
# -

# ### Логические значения

# создадим переменную и запишем в нее логическое значение True
# (обязательно с большой буквы)
v1 = False
type(v1)

# +
# напишем небольшую программу, которая будет показывать,
# какое значение содержится в переменной var

if v1 is True:
    print("Значение переменной истинно")
else:
    print("Значение переменной ложно")
# -

# работаем
