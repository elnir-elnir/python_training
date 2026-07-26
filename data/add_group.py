#------------------------------------------------------------------------------
# qa:
# description: Методы генерации тестовых данных для объекта Группа
#------------------------------------------------------------------------------

import random
import string
from model.group import Group



# Добавлен список фиксированных данных, который может быть использован, например, для отладки
# тестов (урок 6-9)
constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]



# Методы генерации тестовых данных перенесены из файла test_add_group.py (урок 6-9)


# Добавлен вспомогательный метод для генерации случайных тестовых данных (урок 5-7)
# В качестве параметров передается префикс и параметр, определяющий максимальную длину генерируемой
# строки (урок 5-7)
# " "*10 - увеличение количества символов пробела для повышения вероятности включения пробела в
# сгенерированную строку
def random_string(prefix, maxlen):
    # Определяем символы, которые мы будем использовать для генерации тестовых данных (урок 5-7)
    # Временно убрала string.punctuation и " " * 10 (чтобы тесты не падали из-за "`" и " "
    # во время их отладки в рамках выполнения дз 15 и дз 16)
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "
    # Случайным образом выбираем символ из заданной строки и генерируем данные случайно длины, не
    # превышающей максимальную длину. Склиеваем символы в одну строку (урок 5-7)
    return prefix + "".join([random.choice(symbols) for  i in range(random.randrange(maxlen))])



# Добавляем тестовые данные, определенные вне тестов, для параметризации тестов
# чтобы тестовые данные передавались в тестовую функцию в качестве параметра (урок 5-7)
# В виде фиксированного списка (урок 5-7) - закоментировано после добавления метода генерации
# тестовых данных
# testdata = [
#     Group(name="scasc", header="fdbvd", footer="dsvb"),
#     Group(name="", header="", footer="")
# ]
# В виде сгенерированных тестовых данных (урок 5-7)
# Вариант 1: список из 1 пустой группы и 1 группы с заполненными полями
testdata1 = [
    Group(name=random_string("name", 10), header=random_string("header", 20),\
          footer=random_string("footer", 20)),
    Group(name="", header="", footer="")
]


# Вариант 2: 1 группа с пустыми полями + 5 (для примера) групп с заполненными полями
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),\
          footer=random_string("footer", 20)) for i in range(5)
]


# Вариант 3: с разными комбинациями заполненности полей (полный перебор возможных случаев)
testdata3 = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]
