#------------------------------------------------------------------------------
# qa:
# description: Методы генерации данных для объекта Группа с сохранением в файл
#------------------------------------------------------------------------------

import random
import string

import os.path
import json
import jsonpickle # добавлен в рамках уровка 6-12 (но не стала удалять import json)

# Официальная документация о чтении опций из командной строки:
# https://docs.python.org/3/library/getopt.html (урок 6-10)
import getopt # для чтения опций командной строки (урок 6-10)
import sys # для получения доступа к опциям из предыдущего импорта (урок 6-10)

from model.group import Group



# Чтение опций из командной строки (урок 6-10)
try:
    # Используем две опции: n - задает количество генерируемых данных, f - задает файл, в который
    # данные должны записываться; а ["number of groups", "file"] - это подсказки (урок 6-10)
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


# Определены дефолтные значения опций (урок 6-10)
n = 5
f = "data/groups.json"

# на основании информации из официальной документации (урок 6-10)
for o, a in opts:
    if o == "-n":
        # если значение опции == -n, значит в ней задается количество групп a в виде целого числа
        n = int(a)
    # если значение опции == -f, значит в опции задается файл в виде строки
    elif o == "-f":
        f = a



# Методы генерации тестовых данных скопированы из файла data\add_group.py (урок 6-10)
# Пояснения по этим методам см. в указанном файле

def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for  i in range(random.randrange(maxlen))])



# Вариант 1: список из 1 пустой группы и 1 группы с заполненными полями
testdata1 = [
    Group(name=random_string("name", 10), header=random_string("header", 20),\
          footer=random_string("footer", 20)),
    Group(name="", header="", footer="")
]


# Вариант 2: 1 группа с пустыми полями + 5 (для примера) групп с заполненными полями
# Изменили способ определения количества генерируемых объектов - теперь указываем через опцию n (урок 6-10)
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),\
          footer=random_string("footer", 20)) for i in range(n)
]


# Вариант 3: с разными комбинациями заполненности полей (полный перебор возможных случаев)
testdata3 = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]



# Определен файл для сохранения сгенерированных тестовых данных (урок 6-10)
# Сразу в рамках урока изменили способ определения имени файла - теперь указываем через опцию f, здесь:
# os.path.dirname(os.path.abspath(__file__) - это путь к генератору
# ".." - переход на 1 уровень вверх, т. е. в корневую директорию проекта
# f - относительный путь к файлу, который указывается в качестве параметра
# file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json") # было
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) # стало


# В рамках урока 6-12 после импорта jsonpickle этот метод изменили. Я создала новый метод, а этот не стала
# удалять
# # Записываем сгенерированные данные в файл (урок 6-10)
# with open(file, "w") as out:
#     # Функция json.dumps превращает некторую структуру данных в строку в формате json, а lambda
#     # преобразовывает сгенерированные данные в словарь для последующего преобразования их в формат json,
#     # indent=2 - форматирует текст в файле groups.json (без этого форматирования весь результат отображается
#     # в одной строке (урок 6-10)
#     out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

# Новая редакия метода (урок 6-12)
# В результате выполнения этого метода в файле groups.json появляется ключ "py/object": "model.group.Group",
# который указывает на то, что сериализован объект типа model.group.Group
with open(file, "w") as out:
    # Определяем параметры форматирования, чтобы данные в файле отображались не в одну строку
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
