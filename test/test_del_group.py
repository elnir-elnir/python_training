#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
from model.group import Group


# Methods app.session.login(), app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# simplified removal method
def test_delete_first_group(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    # Получаем список групп из тестируемого приложения до удаления группы (урок 4-7)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (урок 4-7)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

    # Реализуем сравнение списков (урок 4-8)
    # В старом списке удаляем первый элемент (удаляем все элементы с 0 по 1 [0:1], но
    # при вырезке левая граница включается, а правая не включается, поэтому удалится
    # только первый элемент, у которого индекс 0) и сравниваем списки
    old_groups[0:1] = []
    assert old_groups == new_groups



def test_delete_custom_group_when_group_has_no_contacts(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))
    # Добавляем проверку наличия в группе контактов (урок 3-5)
    if app.group.count_of_contacts_in_group(group_name) > 0:
        app.contact.select_all_contacts()
        app.contact.delete_contact_from_contact_list()
        app.group.open_groups_page()
    app.group.delete_group_by_name(group_name)



def test_delete_custom_group_when_group_has_contacts(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))

    # Добавляем проверку наличия созданных контактов (урок 3-5)
    app.contact.open_contact_list_via_home_button()
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_custom_group(group_name)
    else:
        # Добавляем проверку наличия контактов в тестовой группе (урок 3-5)
        if app.group.count_of_contacts_in_group(group_name) == 0:
            app.data.create_contact_with_custom_group(group_name)

    app.group.delete_group_by_name(group_name)



def test_delete_modified_group_when_group_has_no_contacts(app):
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    app.group.delete_group_by_name(modified_group.name)



def test_delete_modified_group_when_group_has_contacts(app):
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    contact = app.data.create_contact_with_custom_group(modified_group.name)
    app.group.delete_group_by_name(modified_group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.filter_contacts_by_group(group_name="[none]")



def test_delete_several_groups(app):
    group1, group2 = app.data.create_several_custom_groups()
    app.group.select_group_by_name(group1.name)
    app.group.select_group_by_name(group2.name)
    app.group.delete_group()
