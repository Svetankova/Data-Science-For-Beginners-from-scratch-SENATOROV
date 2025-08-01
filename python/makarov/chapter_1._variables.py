"""Переменные в питоне."""

# ### Создание (объявление) переменных

# можно создать переменную, присвоив ей числовое значение
x1 = 15
print(x1)

# кроме того, переменной можно задать строковое (текстовое) значение
y1 = "Я программирую на Питоне"
print(y1)

# в Питоне можно присвоить разные значения сразу нескольким переменным
a1, b1, c1 = "Питон", "C++", "PHP"
print(a1, b1, c1)

# а также присвоить одно и то же значение нескольким переменным
x2 = y2 = z2 = "То же самое значение"
print(x2, y2, z2)

# каждый элемент списка можно "распаковать" в переменные
my_list = ["помидоры", "огурцы", "картофель"]
a2, b2, c2 = my_list
print(a2, b2, c2)

# ### Автоматическое определение типа данных

x3 = 256  # в этом случае переменной x присваивается тип int (целочисленное значение)
y3 = 0.25  # y становится float (десятичной дробью)
z3 = "Просто текст"  # z становится str (строкой)

# ### Как узнать тип переменной в Питоне

# узнаем тип переменных из предыдущего примера
print(type(x3), type(y3), type(z3))

# ### Присвоение и преобразование типа данных

# Присвоение типа данных

x4 = str(25)  # число 25 превратится в строку
y4 = int(25)  # число 25 останется целочисленным значением
z4 = float(25)  # число 25 превратится в десятичную дробь

print(type(x4), type(y4), type(z4))

# Изменение типа данных

# преобразуем строку, похожую на целое число, в целое число
print(type(int("25")))

# или строку, похожую на дробь, в настоящую десятичную дробь
print(type(float("2.5")))

# преобразуем дробь в целочисленное значение
# обратите внимание, что округления в большую сторону не происходит
print(int(36.6))
print(type(int(36.6)))

# конечно, и целое число, и дробь можно преобразовать в строку
print(type(str(25)))
print(type(str(36.6)))

# ### Именование переменных

# Допустимые имена переменных

# ```python
# variable = "Просто переменная"
# _variable = "Просто переменная"
# variable_ = "Просто переменная"
# my_variable = "Просто переменная"
# My_variable_123 = "Просто переменная"
# ```

# Имя переменной состоит из нескольких слов

# можно применить так называемый верблюжий регистр, camelCase
# все слова кроме первого начинаются с заглавной буквы и пишутся слитно
# camelCaseVariable = "Верблюжий регистр"
#
# нотацию Паскаль, PascalCase (то же самое, только тепер все слова пишутся с заглавной)
# PascalCaseVariable = "Нотация Паскаль"
#
# змеиный стиль, snake_case (с нижними подчеркиваниями)
# snake_case_variable = "Змеиная нотация"

# ### Ответы на вопросы

# **Вопрос**. Как можно преобразовать список чисел таким образом, чтобы каждый элемент списка превратился в отдельную строку?

# возьмем простой список
list5 = [1, 2, 3]

# использовать только функцию str() нельзя
str(list5)

# +
# вариант 1: объявить новый список и в цикле for помещать туда строковые значения
list_str = []

for x5 in list5:
    list_str.append(str(x5))

list_str
# -

# вариант 2: использовать list comprehension
new_method = [str(x5) for x5 in list5]

# вариант 3: функции map() и list()
list(map(str, list5))

# работаем
