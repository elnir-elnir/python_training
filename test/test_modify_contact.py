#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
from random import randrange

from model.contact import Contact
from model.group import Group


# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Добавлен тест модификации контакта с индексом, определенным случайным образом (дз 13)
def test_modify_some_contact_when_contact_not_in_group_via_details_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если
    # его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        print("start_contact: ", contact)

    # Получаем список контактов из приложения до модификации контакта (дз 11)
    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # Определен случайным образом индекс модифицируемого контакта (дз 13)
    index = randrange(len(old_contacts))
    print("index: ", index)

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()
    print("contact: ", contact)
    print("old_contacts: ", old_contacts)
    print("contact_id: ", contact.id)

    # Запоминаем идентификатор контакта c полученным индексом (дз 13)
    contact_id = old_contacts[index].id
    contact.id = contact_id
    print("contact_id_new: ", contact.id)

    # переходим на страницу редактирования контакта без группы с заданным индексом (в рамках дз 13)
    app.contact.go_to_details_page_by_contact_id(contact_id)

    # Тест
    # Модифицируем первый в списке контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)
    print("new_contacts: ", new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11, 13)
    old_contacts[index] = contact
    print("modified_contacts: ", old_contacts)

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    print("sorted_modified_contacts: ", sorted(old_contacts, key=Contact.id_or_max))
    print("sorted_new_contacts: ", sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# Тест переименован и модифицирован в рамках дз 13
def test_modify_first_contact_when_contact_not_in_group_via_details_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если
    # его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    # Получаем список контактов из приложения до удаления контакта (дз 11)
    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # переходим на страницу редактирования первого контакта без группы
    app.contact.go_to_details_page_of_first_contact_from_contact_list()

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()

    # Запоминаем идентификатор первого в списке контакта (дз 11)
    contact.id = old_contacts[0].id

    # Тест
    # Модифицируем первый в списке контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11)
    old_contacts[0] = contact

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# Добавлен тест модификации контакта с индексом, определенным случайным образом (дз 13)
def test_modify_some_contact_when_contact_not_in_group_via_edit_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    # Получаем список контактов из приложения до модификации контакта (дз 11)
    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # Определен случайным образом индекс модифицируемого контакта (дз 13)
    index = randrange(len(old_contacts))

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()

    # Запоминаем идентификатор контакта с полученным индексом (дз 11, 13)
    contact_id = old_contacts[index].id
    contact.id = contact_id
    app.contact.go_to_edit_page_by_contact_id(contact_id)

    # Тест
    # Модифицируем контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11, 13)
    old_contacts[index] = contact

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# Тест переименован и модифицирован в рамках дз 13
def test_modify_first_contact_when_contact_not_in_group_via_edit_from_home_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    # Получаем список контактов из приложения до модификации контакта (дз 11)
    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()

    # Запоминаем идентификатор первого в списке контакта (дз 11)
    contact.id = old_contacts[0].id
    app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Тест
    # Модифицируем контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11)
    old_contacts[0] = contact

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# Тест переименован в рамках дз 13
def test_modify_first_contact_when_contact_not_in_group_via_details_from_birthday_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        contact = app.data.create_contact_with_default_group()
        # Получаем список контактов из приложения до модификации контакта (дз 11)
        old_contacts = app.contact.get_contact_list_in_group("[none]")
        # Запоминаем идентификатор первого в списке контакта (дз 11)
        contact.id = old_contacts[0].id

    app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Устанавливаем дату рождения, если её нет
    if app.contact.get_bday() == "0" or app.contact.get_bmonth() == "-":
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    contact = old_contacts[0]

    app.contact.go_to_next_birthdays_page()
    print(contact.lastname, contact.firstname, contact.middlename)

    app.contact.go_to_details_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()

    # Запоминаем идентификатор первого в списке контакта (дз 11)
    contact.id = old_contacts[0].id

    # Тест
    # Модифицируем контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11)
    old_contacts[0] = contact

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# Добавлен тест модификации контакта по индексу, определенному случайным образом (дз 13)
def test_modify_some_contact_when_contact_not_in_group_via_details_from_birthday_page(app):
    # Добавляем проверку наличия контакта, не включенного в группу, и создание контакта, если его нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    # Получаем список контактов из приложения до модификации контакта (дз 11)
    old_contacts = app.contact.get_contact_list_in_group("[none]")
    index = randrange(len(old_contacts))
    # Запоминаем идентификатор контакта с полученным индексом (дз 11, 13)
    contact_id = old_contacts[index].id

    app.contact.go_to_edit_page_by_contact_id(contact_id)

    # Устанавливаем дату рождения, если её нет
    if app.contact.get_bday() == "0" or app.contact.get_bmonth() == "-":
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_details_page_by_contact_id(contact_id)

    # Создаем объект модифицированного контакта (дз 11)
    contact = app.data.set_modified_contact()

    # Запоминаем идентификатор контакта с полученным индексом (дз 11)
    contact.id = contact_id

    # Тест
    # Модифицируем контакт через страницу контакта (модифицировано в рамках дз 11)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact(contact)
    app.contact.return_to_home_page_after_contact_edit()

    # Добавляем проверку списка после модификации со списком, полученным из тестируемого
    # приложения (дз 11)
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) == len(new_contacts)

    # Выполняем замену модифицируемого контакта из списка, полученного из приложения, на результат
    # модификации (на модифицированный контакт) (дз 11, 13)
    old_contacts[index] = contact

    # Сравниваем контакты: контакт, полученный из приложения и контакт с выполненной заменой
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



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
