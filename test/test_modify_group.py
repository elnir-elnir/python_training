#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
import time

from model.group import Group



# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_full_modify_new_group_initial_without_contacts(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        # Объяление перемнной выполнено в рамках дз 11
        group = Group(name=group_name)
        app.group.create(group)

        # Получаем список групп из тестируемого приложения до модификации группы (дз 11)
        old_groups = app.group.get_group_list()
        # Запоминаем идентификатор группы с заданным именем (урок 4-9, дз 11)
        group.id = app.group.get_group_id_by_name_from_list(old_groups, group_name)

    # Добавляем проверку наличия в группе контактов (урок 3-5)
    if app.group.count_of_contacts_in_group(group_name) > 0:
        app.contact.select_all_contacts()
        app.contact.delete_contact_from_contact_list()

    # Получаем список групп из тестируемого приложения до модификации группы (урок 4-7)
    old_groups = app.group.get_group_list()
    # Создаем объект модифицированной группы (дз 11)
    group = Group(name="modified_test_group", header="modified_test_header", footer="modified_test_footer")
    # Определяем идентификатор группы по ее имени в полученном из приложения списке (дз 11)
    group.id = app.group.get_group_id_by_name_from_list(old_groups, group_name)

    # Выполняем модификацию
    app.group.full_modify_group_by_name(group_name, new_group_name="modified_test_group", new_group_header="modified_test_header", new_group_footer="modified_test_footer")

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (урок 4-7, hw 11)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    # Определяем индекс группы в списке по id (дз 11)
    i = app.group.find_group_index_by_id(old_groups, group.id)

    # Выполняем замену модифицируемой группы из списка, полученного из приложения, на результат
    # модификации (на модифицированную группу) (дз 11)
    old_groups[i] = group

    # Сравниваем группы: группу, полученную из приложения и группу с выполненной заменой (дз 11)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_confirm_new_group_modify_without_changes_when_group_has_no_contacts(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))
    # Добавляем проверку наличия в группе контактов (урок 3-5)
    if app.group.count_of_contacts_in_group(group_name) > 0:
        app.contact.select_all_contacts()
        app.contact.delete_contact_from_contact_list()

    app.group.open_and_confirm_group_modify_without_changes_by_name(group_name)



def test_full_modify_new_group_initial_with_one_contact(app):
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))
    # Добавляем проверку наличия в группе контактов (урок 3-5)
    if app.group.count_of_contacts_in_group(group_name) == 0:
        app.data.create_contact_with_custom_group(group_name)

    app.group.full_modify_group_by_name(group_name, new_group_name="modified_test_group", new_group_header="modified_test_header", new_group_footer="modified_test_footer")



def test_full_modify_group_subsequent_when_group_has_no_contacts(app):
    group = app.data.create_custom_group()
    app.data.full_remodified_group(group)



def test_full_modify_group_subsequent_when_group_with_one_contact(app):
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.data.full_remodified_group(group)
