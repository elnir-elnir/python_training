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
        tmp_group = Group(name="test")
        app.group.create(tmp_group)

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
    #assert old_groups == new_groups
    # Для сравнения списков отсортировали их в порядке возрастания идентификатора (id) (дз 11)
    assert sorted(old_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)



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

    # Получаем список групп из приложения и получаем из списка идентификатор группы (id) по ее
    # названию (дз 11)
    old_groups = app.group.get_group_list()
    group_id = app.group.get_group_id_by_name_from_list(old_groups, group_name)

    # Удаляем группу в приложении и получаем новый список из приложения (дз 11)
    app.group.delete_group_by_name(group_name)
    new_groups = app.group.get_group_list()

    # Получаем ожидаемый список (старый список - удаленная группа)  (дз 11)
    expected_groups = [g for g in old_groups if g.id != group_id]

    # Сравниваем
    assert len(old_groups) - 1 == len(new_groups)
    assert sorted(expected_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)



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

    # Получаем список групп из приложения и получаем из списка идентификатор группы (id) по ее
    # названию (дз 11)
    old_groups = app.group.get_group_list()
    group_id = app.group.get_group_id_by_name_from_list(old_groups, group_name)

    # Удаляем группу в приложении и получаем новый список из приложения (дз 11)
    app.group.delete_group_by_name(group_name)
    new_groups = app.group.get_group_list()

    # Получаем ожидаемый список (старый список - удаленная группа)  (дз 11)
    expected_groups = [g for g in old_groups if g.id != group_id]

    # Сравниваем
    assert len(old_groups) - 1 == len(new_groups)
    assert sorted(expected_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)



def test_delete_modified_group_when_group_has_no_contacts(app):
    tmp_group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(tmp_group)

    # Получаем список групп из приложения и получаем из списка идентификатор группы (id) по ее
    # названию (дз 11)
    old_groups = app.group.get_group_list()
    print("old:", old_groups)
    group_id = app.group.get_group_id_by_name_from_list(old_groups, modified_group.name)
    print("modified_group: name = " + modified_group.name + " id: " + group_id)

    # Удаляем группу в приложении и получаем новый список из приложения (дз 11)
    app.group.delete_group_by_name(modified_group.name)
    new_groups = app.group.get_group_list()
    print("new:", new_groups)

    # Получаем ожидаемый список (старый список - удаленная группа)  (дз 11)
    expected_groups = [g for g in old_groups if g.id != group_id]
    print("expected_groups:", expected_groups)

    # Сравниваем
    assert len(old_groups) - 1 == len(new_groups)
    assert sorted(expected_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)



def test_delete_modified_group_when_group_has_contacts(app):
    tmp_group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(tmp_group)
    contact = app.data.create_contact_with_custom_group(modified_group.name)
    app.group.delete_group_by_name(modified_group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.filter_contacts_by_group(group_name="[none]")



def test_delete_several_groups(app):
    group1, group2 = app.data.create_several_custom_groups()

    # Выполнение
    # Получаем из приложения текущий список групп (дз 11)
    old_groups = app.group.get_group_list()

    # Определяем идентификаторы групп, которые будем удалять (дз 11)
    tmp_id_list = []
    for g in old_groups:
        if g.name == group1.name or g.name == group2.name:
            tmp_id_list.append(g.id)

    # Получаем ожидаемый список групп (из старого списка удаляем группы с идентификаторами из
    # списка tmp_id_list (дз 11)
    expected_groups = [g for g in old_groups if g.id not in tmp_id_list]

    # Удаляем группы в приложении (дз 11)
    app.group.select_group_by_name(group1.name)
    app.group.select_group_by_name(group2.name)
    app.group.delete_group()

    # Получаем из приложения новый список групп (дз 11)
    new_groups = app.group.get_group_list()

    # Проверка (сравниваем)
    assert sorted(expected_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)
