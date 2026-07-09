#------------------------------------------------------------------------------
# qa:
# description: Тесты в соответствии с уроком 3-2
#------------------------------------------------------------------------------

from model.group import Group


# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)
def test_modify_first_group_name(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))

    # Получаем список групп из тестируемого приложения до модификации группы (урок 4-7)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (урок 4-7)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



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
