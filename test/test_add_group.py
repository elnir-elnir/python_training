#------------------------------------------------------------------------------
# developer:
# description:
#------------------------------------------------------------------------------

from model.group import Group



# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Переписываем тесты в соответствии с уроком 4-7 - Загружаем информацию
# из тестируемого приложения в виде списков

def test_add_group(app):
    # Получаем старый список групп из приложения
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="dfgdfgdfg", header="dfgdfg", footer="dfgfgd"))

    # Получаем новый список групп
    new_groups = app.group.get_group_list()

    # Проверяем, что новый список на единицу длинее старого
    assert len(old_groups) + 1 == len(new_groups)



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
