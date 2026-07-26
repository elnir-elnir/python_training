#------------------------------------------------------------------------------
# qa:
# description: Вместо файла  test_add_group.py в рамках урока 6-11
#------------------------------------------------------------------------------

# Пояснения по тесту см. в файле test_add_group.py

from model.group import Group



# Удалена аннотация parametrize и изменены параметры тестовой функции таким образом, чтобы название
# параметра указывало на источник тестовых данных. Например, data_groups указывает, что данные
# загружаются из модуля groups, который находится в пакете data (урок 6-11)
# Изменено название параметра для реализации загрузки тестовых данных из файла data\groups.json (урок 6-12)
def test_add_group(app, json_groups): # вместо data_groups теперь json_groups
    group = json_groups

    old_groups = app.group.get_group_list()
    print("old_groups: ", old_groups)

    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count()

    new_groups = app.group.get_group_list()
    print("new_groups: ", new_groups)

    old_groups.append(group)
    print("new_old_groups: ", old_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    print("sorted_old_groups: ", sorted(old_groups, key=Group.id_or_max))
    print("sorted_new_groups: ", sorted(new_groups, key=Group.id_or_max))