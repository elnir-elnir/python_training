#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
import time

from model.group import Group


# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_modify_contact_when_contact_not_in_group_via_details_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        app.contact.open_contact_list_via_home_button()
        app.contact.go_to_details_page_from_contact_list(contact.lastname)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.go_to_details_page_of_first_contact_from_contact_list()

    # Тест
    # Модифицируем контакт через страницу контакта
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(app.data.set_modified_contact())
    app.contact.return_to_home_page_after_contact_edit()



def test_modify_contact_when_contact_not_in_group_via_edit_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        app.contact.open_contact_list_via_home_button()
        app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Тест
    # Модифицируем контакт через страницу контакта
    app.contact.edit_contact(app.data.set_modified_contact())
    app.contact.return_to_home_page_after_contact_edit()



def test_modify_contact_when_contact_not_in_group_via_details_from_birthday_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        app.contact.go_to_next_birthdays_page()
        app.contact.go_to_details_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.go_to_next_birthdays_page()
        app.contact.go_to_details_page_of_first_page_from_birthday_list()

    # Тест
    # Модифицируем контакт через страницу контакта
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(app.data.set_modified_contact())
    app.contact.return_to_home_page_after_contact_edit()



def test_modify_contact_when_contact_not_in_group_via_edit_from_birthday_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        app.contact.go_to_next_birthdays_page()
        app.contact.go_to_edit_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.go_to_next_birthdays_page()
        app.contact.go_to_edit_page_of_first_contact_from_birthdays_page()

    # Тест
    # Модифицируем контакт через страницу контакта
    app.contact.edit_contact(app.data.set_modified_contact())
    app.contact.return_to_home_page_after_contact_edit()



def test_modify_contact_when_contact_in_group_via_edit_from_home_page(app):
    # Добавляем проверку наличия контакта, включенного в группу, и создание контакта и/или группы,
    # если их нет (урок 3-5)
    # Предусловия
    # Добавляем проверку наличия группы и создание группы, если группы нет (урок 3-5)
    group_name = "test"
    if app.group.count_group_by_name(group_name) == 0:
        app.group.create(Group(name=group_name))


    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group(group_name)

    # Если нет контактов, включенных в группу — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_custom_group(group_name)
        app.contact.open_contact_list_via_home_button()
        app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Тест
    # Модифицируем контакт через страницу контакта
    app.contact.edit_contact(app.data.set_modified_contact())
    app.contact.return_to_home_page_after_contact_edit()



def test_remodify_contact_names_when_contact_not_in_group_via_edit_from_birthday_page(app):
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_remodified_names_via_edit_from_birthday_page(contact)



def test_remodify_contact_names_when_contact_in_group_via_edit_from_birthday_page(app):
    contact = app.data.create_contact_with_custom_group((app.data.create_custom_group()).name)
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_remodified_names_via_edit_from_birthday_page(contact)
