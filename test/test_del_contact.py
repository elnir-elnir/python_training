#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)
def test_delete_contact_not_in_group_via_edit_page(app):
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
    # Удаляем контакт через страницу редактирования
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()


def test_delete_contact_not_in_group_via_birthday_page(app):
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

    # Устанавливаем дату рождения, если её нет
    if app.contact.get_bday() == "0" or app.contact.get_bmonth() == "-":
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_of_first_contact_from_birthdays_page()
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()



def test_delete_contact_not_in_group_via_contact_list(app):
    # Добавляем проверку наличия контакта и создание контакта, если контакта нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        app.contact.open_contact_list_via_home_button()
        app.contact.select_contact_by_lastname(contact.lastname)
    else:
        # Иначе переходим на страницу редактирования первого контакта без группы
        app.contact.select_first_contact()

    # Тест
    # Удаляем контакт из списка контактов
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()


def test_delete_all_contacts_not_in_group_via_delete_button(app):
    contact1, contact2 = app.data.create_several_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_all_contacts()
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()


def test_delete_contact_included_in_group_via_edit_page(app):
    contact = app.data.create_contact_with_custom_group(app.data.create_custom_group().name)
    app.contact.open_contact_list_via_home_button()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()


def test_delete_several_contacts_included_in_one_group_via_checkboxes_and_delete_button(app):
    group = app.data.create_custom_group()
    contact1, contact2 = app.data.create_several_contact_with_custom_group(group.name)
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_contact_by_lastname(contact1.lastname)
    app.contact.select_contact_by_lastname(contact2.lastname)
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()


def test_delete_button_pressed_when_contact_not_selected(app):
    app.open_home_page()
    app.contact.delete_contact_from_contact_list()
    app.contact.delete_modal_window_closed()
