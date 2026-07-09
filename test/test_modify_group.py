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
        app.group.create(Group(name=group_name))
    # Добавляем проверку наличия в группе контактов (урок 3-5)
    if app.group.count_of_contacts_in_group(group_name) > 0:
        app.contact.select_all_contacts()
        app.contact.delete_contact_from_contact_list()

    app.group.full_modify_group_by_name(group_name, new_group_name="modified_test_group", new_group_header="modified_test_header", new_group_footer="modified_test_footer")



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
