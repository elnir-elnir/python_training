#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

import pytest

from model.group import Group

# Импорт сгенерированных случайных данных (урок 6-9)
from data.add_group import testdata
from data.add_group import testdata1
from data.add_group import testdata3

# # Импорт фиксированных данных (например, для отладки тестов) (урок 6-9)
# from data.add_group import constant as testdata


# Методы генерации тестовых данных random_string и testdata, testdata1, testdata3, составленные
# в рамках урока 5-7, перенесены из этого файла в файл add_group.py (урок 6-9)


# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Переписываем тесты в соответствии с уроком 4-7 - Загружаем информацию
# из тестируемого приложения в виде списков

# Добавлена парметризация теста (урок 5-7)
# Здесь testdata - исчтоник тестовых данных, group - параметр для передачи тестовых данных в тестовую функцию,
# ids - параметр для формирования списка с текстовым представлением тестовых данных для формирования отчета
# о выполнении теста (чтобы в отчете было видно, с какими именно тестовыми данными выполнялся тест)
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    # Получаем старый список групп из приложения
    old_groups = app.group.get_group_list()
    print("old_groups: ", old_groups)

    # Для последующего сравнения списков модифицируем тест - объявляем локальную
    # переменную group и передаем ее в качестве параметра в метод создания группы (урок 4-9)
    # Убираем объявление локальной переменной в связи с параметризацией теста (урок 5-7)
    # group = Group(name="", header="", footer="")
    app.group.create(group)

    # Проверяем, что новый список на единицу длинее старого (урок 4-7)
    # Но если данная проверка неуспешна, то дальнейшее поэлементное сравнение списков
    # не имеет смысла. Поэтому для ускорения этой проверки ее надо выполнить, не загружая список групп
    # Для этого меняем проверку: сравнение выполняем не с новым списком, а с подсчитанным количеством групп
    # Новый список загружаем только после успешного выполнения этой проверки. Это и есть хеширование.
    # А функция app.group.count() - это хеш-функция (урок 4-10)
    assert len(old_groups) + 1 == app.group.count()

    # Меняем очередность выполнения сравнения количества групп и получение обновленного
    # нового списка групп, который мы стали получить с урока 4-7 (урок 4-10)
    new_groups = app.group.get_group_list()
    print("new_groups: ", new_groups)

    # В список групп, полученный из приложения, добавляем новую группу (урок 4-9)
    old_groups.append(group)
    print("new_old_groups: ", old_groups)

    # # Сравниваем группы, но тест упал, т. к. не совпал порядок групп в списке (урок 4-9)
    # # Поэтому данный метод модифицируем в следующий за ним - с сортировкой (а текущий метод
    # # я закомментировала
    # assert old_groups == new_groups

    # Создаем новую функцию сравнения, в которой указываем в качестве ключа идентификатор - оба
    # списка сортируем по одинаковым правилам (урок 4-9)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    print("sorted_old_groups: ", sorted(old_groups, key=Group.id_or_max))
    print("sorted_new_groups: ", sorted(new_groups, key=Group.id_or_max))



# Тест закоментирован в рамках урока 5-7 "Параметризация тестов"
# # Аналогично предыдущему тесту модифицируем и этот тест (урок 4-9)
# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
