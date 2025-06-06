"""Виртуальное окружение."""

# pip - пакетный менеджер (инструмент управления зависимостями)
# conda - пакетный менеджер для ДС
#
# 1. Что делает команда python -m venv venv?
# Создаем папку виртуального окружения (ВО)
# python -m venv venv
# *(1 - обращение к модулю, к-рый создает ВО, 2 - название папки)
#
#
# 1.1. Что делает каждая команда в списке ниже?
#
# pip list - вывод команд по данному пакетному менеджеру
#
# pip freeze > requirements.txt
# - выгрузить все пакеты/библиотеки/зависимости в 1 файл (Если не было создано виртуальное окружение ВО, то файл с глобальными пакетами (куча); Если создано, то скаченные нами в течение использования данного окружения)
#
# pip install -r requirements.txt - установка всех библиотек из requirements.txt (при использовании репозитория другого программиста, чтобы скачать все пакеты 1 командой)
#
#
# 2. Что делает каждая команда в списке ниже?
#
# conda env list
# *отображает список всех Conda-окружений, созданных на вашем компьютере
# ![image.png](attachment:image.png)
#
# conda create -n env_name python=3.5
# *создает новое виртуальное окружение Conda.
# conda create: Основная команда для создания окружений.
# -n env_name (или --name env_name): Задает имя нового окружения как env_name. Вы замените env_name на желаемое имя, например, my_new_env.
# python=3.5: Указывает, что в этом новом окружении должен быть установлен Python версии 3.5. Вы также можете указать другие пакеты, которые хотите установить сразу при создании окружения (например, python=3.8 numpy pandas).
#
# conda env update -n env_name -f file.yml
# *обновляет существующее окружение Conda на основе спецификаций, указанных в файле YAML.
# conda env update: Команда для обновления окружения из файла.
# -n env_name: Указывает имя существующего окружения, которое нужно обновить.
# -f file.yml (или --file file.yml): Указывает путь к YAML-файлу (file.yml), который содержит список пакетов и их версий, каналов и т.д. для окружения.
# *Результаты (что вы увидите и что произойдет):
# Conda прочитает file.yml, сравнит его с текущим состоянием окружения env_name.
# Будут установлены недостающие пакеты, обновлены существующие до версий, указанных в YAML, или удалены пакеты, которых нет в YAML (в зависимости от того, как Conda обрабатывает "обновление").
# Вы увидите прогресс загрузки и установки/обновления пакетов.
# Окружение env_name будет приведено в соответствие (насколько это возможно) со спецификациями в file.yml. Это очень полезно для воспроизводимости окружений на разных машинах.
#
# source activate env_name
# *(для Linux/macOS) или conda activate env_name (современный, кроссплатформенный синтаксис)
#
# source deactivate
# *conda deactivate
# Деактивирует текущее активное Conda-окружение.
#
# conda clean -a
# *Очищает кеши Conda для освобождения дискового пространства.
# conda clean: Основная команда для очистки.
# -a (или --all): Указывает, что нужно очистить все типы кеша:
# Загруженные архивы пакетов (.tar.bz2).
# Неиспользуемые (не привязанные ни к одному окружению) пакеты.
# Кеш индекса.
# Кеш заблокированных файлов.
# Иногда и другой мусор.
# *Результаты (что вы увидите и что произойдет):
# Conda покажет список файлов и директорий, которые будут удалены, и запросит подтверждение (Proceed ([y]/n)?).
# После подтверждения файлы будут удалены.
# В конце будет выведено сообщение о том, сколько дискового пространства было освобождено.
# Это безопасная операция, она не удаляет ваши созданные окружения или установленные в них пакеты, а только кешированные и неиспользуемые файлы.
#
#
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
# ![image-2.png](attachment:image-2.png)
#
# ![image-3.png](attachment:image-3.png)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
# venv
# Чтобы установить необходимые пакеты внутрь виртуального окружения venv, вы должны:
# 1. Активировать это venv окружение.
# 2. Использовать команду pip install <имя_библиотеки> для скачивания и установки библиотек. Пакеты будут установлены именно в это активное окружение.
# Если у вас есть файл requirements.txt и в ходе работы появляются новые библиотеки, его нужно обновить (тк это не происходит автоматически): pip freeze > requirements.txt
#
# conda
# Установка пакетов с помощью conda install или pip install, при этом находясь в необходимом окружении
#
#
# 5. Что делают эти команды?
# pip freeze > requirements.txt - выгрузить пакеты/библиотеки/зависимости ВО в 1 файл
#
# conda env export > environment.yml - команда для экспорта (выгруза) текущего окружения в файл
#
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
# ![image-4.png](attachment:image-4.png)
#
#
#
# 6. Что делают эти команды?
# pip install -r requirements.txt - установка всех библиотек из requirements.txt (при использовании репозитория другого программиста, чтобы скачать все пакеты 1 командой)
#
# conda env create -f environment.yml - команда для считывания окружения из файла environment.yml
#
#
# 7. Что делают эти команды?
# pip list
# *отображает список всех Python-пакетов, установленных в текущем активном Python-окружении с помощью pip.
#
#
# pip show <package_name>
# *отображает подробную информацию о конкретном установленном Python-пакете
#
#
# conda list
# *отображает список всех пакетов, установленных в текущем активном Conda-окружении (или в указанном окружении, если использовать флаг -n env_name). Важно, что conda list показывает не только Python-пакеты, но и другие типы пакетов, которые Conda может менеджить (например, библиотеки C, R-пакеты, если они были установлены через Conda).
#
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
# ⦁   При создании пустого окружения: venv создает более "чистое" окружение с меньшим количеством пакетов по умолчанию. conda добавляет несколько своих служебных пакетов.
# ⦁   По доступности для установки:
#     ⦁   pip (через venv): Имеет доступ к PyPI – огромному репозиторию Python-пакетов.
#     ⦁   conda: Имеет доступ к Conda-каналам, которые содержат не только Python-пакеты, но и не-Python зависимости (библиотеки C/C++, Fortran и т.д.), что критично для многих научных пакетов. conda также может устанавливать пакеты из PyPI через pip.
# Итог по пакетам: pip имеет доступ к большему числу чисто Python-пакетов. conda лучше справляется с пакетами, имеющими сложные не-Python зависимости.
#
# 1. Управление сложными зависимостями: conda легко устанавливает пакеты (например, NumPy, SciPy, TensorFlow) вместе с их не-Python бинарными зависимостями, что часто является проблемой для pip, особенно на Windows.
# 2. Надежная изоляция окружений: conda позволяет легко создавать окружения с разными версиями Python и пакетов, полностью изолируя их друг от друга.
# 3. Воспроизводимость: Легко делиться и воспроизводить окружения с помощью файлов environment.yml, которые включают все зависимости, в том числе не-Python.
# 4. Кроссплатформенность: Хорошо работает на Windows, macOS и Linux.
# Кратко: conda упрощает жизнь дата-сайентистам, решая головную боль с установкой и управлением сложными научными пакетами и их зависимостями на разных системах.
#
#
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
# ![image-5.png](attachment:image-5.png)
#
#
# 10. добавьте в .gitignore папку SENATOROV
# 11. Зачем нужно виртуально окружение?
# Виртуальное окружение (ВО) в Python — это изолированная от основной системы среда, содержащая все необходимые зависимости для работы программного обеспечения.
#
# Мы изолируем библиотеки - Внутри виртуального окружения используется собственный набор библиотек, который рассматривается как уникальный, независимо от их использования в других проектах.
#
# Это необходимо для работы над большими проектами, чтобы их изолировать и избежать конфликтов между проектами на 1 компе, экспериментировать над новой библиотекой, облегчить передачу проекта другим разработчикам для воссоздания той же среды
#
#
# ******************************
# ! (восклицательный знак) - использование ячейки как терминал
# ipynb - файл юпитера
# user\.conda\pkgs - находятся скачанные пакеты анаконды
# анаконда - дистрибутив - совокупность пакетов

# #### Виртуальное окружение и файл зависимостей
# если в файлах много библиотек
# import numpy
# import pandas ...
# Каждому рабочему придется скачивать эти библиотеки, а хотим 1 командой и все сразу и только необходимые
#
# Концепция: Создаем ВО, закачиваем библиотеки (pip install), создание файла requirements.txt
#
# Это можно заменить 1 командой.
#
# Для начала:
# - выгрузить все пакеты/библиотеки/зависимости в 1 файл
# pip freeze > requirements.txt
# *новый файл с кучей зависимостей, хотя мы установили всего 2
#  (куча пакетов пришло из глобального питона)
#
# Виртуальное окружение (ВО) в Python — это изолированная от основной системы среда, содержащая все необходимые зависимости для работы программного обеспечения.
#
# Мы изолируем библиотеки - Внутри виртуального окружения используется собственный набор библиотек, который рассматривается как уникальный, независимо от их использования в других проектах.
#
#
# Создаем виртуальное окружение:
# 1. Создаем папку ВО
# python -m venv venv (1 - обращение к модулю, к-рый создает ВО, 2 - название папки)
#
# 2. Активация ВО
# venv\Scripts\activate (активация ВО) - здесь venv это папка, в к-ром ВО
#
# 2. по появлению (venv) загружаем библиотеки (как на фото)
#
# 3. Выгрузим заново наши пакеты
# pip freeze > requirements.txt
# Теперь только те пакеты, к-рые используются в нашем проекте
#
# если имеем дело с чужим репозиторием, просим предоставить файл requirements.txt
#
# Чтобы установить все библиотеки оттуда:
# pip install -r requirements.txt
#
#
# #### Пакетный менеджер для Data Science
# это Conda
# (*pip для разработчиков)
#
# команда
# # !conda list
# (в ячейке) - показывает сколько пакетов в conde
#
# Работа в Anaconda.Navigator
# Создаем ВО с помощью дистрибутива Anaconda
# (прямо в интерфейсе Conda)
#
# Концепция: создание ВО ('conda1'), к-рый будем использовать как интерпретатор. Входящие библиотеки будут работать при считывании кода, потому нет необходимости качать через pip или conda
#
# environment - create - 'conda1'
# *используем к опр.версии ВО опр.версию питон (может быть проект поддерживает только питон3.10)
# При выборе интерпретатора выбираем наше ВО 'conda1'
#
# Команда !pip freeze - увидим список пакетов в окружении 'conda1'
#
# Концепция: Выгруз используемых библиотек в ВО ('conda1')
#
# conda env export > environment.yml
# команда для экспорта (выгруза) текущего окружения в файл
#
# conda env create -f environment.yml
# команда для считывания окружения из файла
# (т.е. он есть в директории и нужно, чтобы он заработал)
