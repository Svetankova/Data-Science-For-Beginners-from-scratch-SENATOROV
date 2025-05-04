# """Соглашение о коммитах."""

# Соглашение о коммитах: https://www.conventionalcommits.org/ru/v1.0.0/
#
# 2. Представьте, что вы исправили баг (-> fix) в функции, которая некорректно округляет числа. Сделайте фиктивный коммит и напишите для него сообщение в соответствии с Conventional Commits (используя тип fix).
# git commit -m 'fix: correct rounding error in calculate_price function'
#
# 3. Добавление новой функциональности -> feat:
# Допустим, вы реализовали новую функцию generateReport в проекте. Сделайте фиктивный коммит с типом feat, отражающий добавление этой функциональности
# git commit -m 'feat: add new function generateReport'
#
# 4. Модификация формата кода или стилей:
# Представьте, что вы поправили отступы и форматирование во всём проекте, не меняя логики кода. Сделайте фиктивный коммит с типом style
# git commit -m 'style: corrected indents and formatting'
#
# 5. Документация и тестирование:
# Сделайте фиктивный коммит с типом docs, добавляющий или улучшающий документацию для вашей новой функции.
# git commit -m 'docs: update documentation for function generateReport'
#
# Сделайте фиктивный коммит с типом test, добавляющий тесты для этой же функции.
# git commit -m 'test: add tests for function generateReport'

# +
"""3."""
# def calculate_price(number):
#     """
#     Неправильно округляет число, просто отбрасывая дробную часть.
#     """
#     return int(number)


def calculate_price(number: float, ndigits: int | None = None) -> float:
    """Правильно округляет число, используя встроенную функцию round()."""
    return round(number, ndigits)
