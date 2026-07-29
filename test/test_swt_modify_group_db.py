#------------------------------------------------------------------------------
# qa:
# description: Тесты на модификацию группы с загрузкой данных из БД (дз 20)
#------------------------------------------------------------------------------

import random

from model.group import Group


def test_modify_some_group_name(app, orm,check_ui,json_groups):

    if len(orm.get_group_list()) == 0:
        tmp_group = json_groups
        app.group.create(tmp_group)
        #app.group.create(Group(name="test"))

    # Получаем список групп из тестируемого приложения до модификации группы (дз 20)
    old_groups = orm.get_group_list()
    print("old_groups:", old_groups)
    # Случаным образом определяем группу для модификации
    group = random.choice(old_groups)
    print("group:", group)

    # Создаем объект модифицированной группы (дз 11)
    modified_group = Group(id=group.id, name="New group", header=group.header, footer=group.footer)
    print("modified_group:", modified_group)

    # Модифицируем выбранную случайным образом группу
    app.group.modify_group_by_id(group.id, modified_group)

    # Выполняем сравнение списка после модификации со списком, полученным до модификации (дз 20)
    new_groups = orm.get_group_list()
    print("new_groups:", new_groups)
    assert len(old_groups) == len(new_groups)
    print("len(old_groups):", len(old_groups), "   <   >   len(new_groups):", len(new_groups))

    # Выполняем замену модифицируемой группы из списка, полученного до модификации, на результат
    # модификации (на модифицированную группу) (дз 20)
    old_groups.remove(group)
    old_groups.append(modified_group)
    print("new_old_groups:", old_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                 key=Group.id_or_max)
        print("sorted(new_groups):", sorted(new_groups, key=Group.id_or_max))
        print("sorted(old_groups):", sorted(old_groups, key=Group.id_or_max))
        print("sorted(app_groups):", sorted(app.group.get_group_list(), key=Group.id_or_max))



def test_full_modify_some_group_initial_without_contacts(app, orm,check_ui):

    if len(orm.get_group_list_without_contacts()) == 0:
        app.group.create(Group(name="test"))

    # Получаем список групп из тестируемого приложения до модификации группы (дз 20)
    old_groups = orm.get_group_list_without_contacts()
    print("old_groups:", old_groups)
    # Случаным образом определяем группу для модификации
    group = random.choice(old_groups)
    print("group:", group)

    # Создаем объект модифицированной группы (дз 11)
    modified_group = Group(id=group.id, name="modified group name", header="modified_test_header",
                           footer="modified_test_footer")
    print("modified_group:", modified_group)

    # Модифицируем выбранную случайным образом группу
    app.group.modify_group_by_id(group.id, modified_group)

    # Выполняем сравнение списка после модификации со списком, полученным до модификации (дз 20)
    new_groups = orm.get_group_list_without_contacts()
    print("new_groups:", new_groups)
    assert len(old_groups) == len(new_groups)
    print("len(old_groups):", len(old_groups), "   <   >   len(new_groups):", len(new_groups))

    # Выполняем замену модифицируемой группы из списка, полученного до модификации, на результат
    # модификации (на модифицированную группу) (дз 20)
    old_groups.remove(group)
    old_groups.append(modified_group)
    print("new_old_groups:", old_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                 key=Group.id_or_max)
        print("sorted(new_groups):", sorted(new_groups, key=Group.id_or_max))
        print("sorted(old_groups):", sorted(old_groups, key=Group.id_or_max))
        print("sorted(app_groups):", sorted(app.group.get_group_list(), key=Group.id_or_max))


