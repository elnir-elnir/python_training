#------------------------------------------------------------------------------
# qa:
# description: Тесты в соответствии с уроком 3-2
#------------------------------------------------------------------------------
from random import randrange

from model.group import Group



# Добавляем новый тест - модификация группы по индексу, выбранному случайным образом (урок 4-11)
# Сравнение списков реализовано в рамках урока 4-9
def test_modify_some_group_name(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    if app.group.count() == 0:
        # Объявление перемнной выполнено в рамках дз 11
        app.group.create(Group(name="test"))

    # Получаем список групп из тестируемого приложения до модификации группы (урок 4-7)
    old_groups = app.group.get_group_list()
    # Случаным образом определяем индекс модифицируемой группы (урок 4-11)
    index = randrange(len(old_groups))

    # Создаем объект модифицированной группы (дз 11)
    group = Group(name="New group")
    # Определяем идентификатор группы с индексом index в полученном из приложения списке (дз 11; урок 4-11)
    group.id = old_groups[index].id
    print("first_group_id: ",group.id)

    # Модифицируем группу с индексом index в приложении - передаем в приложение значения объекта
    # модифицированной группы (дз 11) и индекс группы (урок 4-11)
    app.group.modify_group_by_index(index, group)

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (урок 4-7)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    # Выполняем замену модифицируемой группы из списка, полученного из приложения, на результат
    # модификации (на модифицированную группу) (дз 11; урок 4-11)
    old_groups[index] = group

    # Сравниваем группы: группу, полученную из приложения и группу с выполненной заменой
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)
def test_modify_first_group_name(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        # Объяление перемнной выполнено в рамках дз 11
        group = Group(name=group_name)
        app.group.create(group)

        # Получаем список групп из тестируемого приложения до модификации группы (дз 11)
        old_groups = app.group.get_group_list()
        # Запоминаем идентификатор созданной группы (урок 4-9)
        group.id = old_groups[0].id

    # Получаем список групп из тестируемого приложения до модификации группы (урок 4-7)
    old_groups = app.group.get_group_list()
    # Создаем объект модифицированной группы (дз 11)
    group = Group(name="New group")
    # Определяем идентификатор первой группы в полученном из приложения списке (дз 11)
    group.id = old_groups[0].id
    print("first_group_id: ",group.id)

    # Модифицируем первую группу в приложении - передаем в приложение значения объекта
    # модифицированной группы (дз 11)
    app.group.modify_first_group(group)

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (урок 4-7)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    # Выполняем замену модифицируемой группы из списка, полученного из приложения, на результат
    # модификации (на модифицированную группу) (дз 11)
    old_groups[0] = group

    # Сравниваем группы: группу, полученную из приложения и группу с выполненной заменой
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_first_group_header(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    if app.group.count() == 0:
        app.group.create(Group(header="Header"))

    # Получаем список групп из тестируемого приложения до модификации группы (урок 4-7)
    old_groups = app.group.get_group_list()

    app.group.modify_first_group(Group(header="New header"))

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (урок 4-7)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
