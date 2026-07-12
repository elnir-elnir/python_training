#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
from random import randrange


# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Добавлен тест удаления контакта по индексу, определенному случайным образом (дз 13)
def test_delete_some_contact_not_in_group_via_edit_page(app):
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

    # Определен случайным образом индекс удаляемого контакта (дз 13)
    index = randrange(len(old_contacts))

    # Переходим на страницу редактирования удаляемого контакта без группы по идентификатору контакта,
    # полученному по индексу (дз 13)
    app.contact.go_to_edit_page_by_contact_id(old_contacts[index].id)

    # Тест
    # Удаляем контакт через страницу редактирования
    app.contact.delete_contact_from_edit_page()

    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (урок 4-7), дз 11
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    # Реализуем сравнение списков (урок 4-8), дз 11
    # В старом списке удаляем элемент, соответствующий индексу (удаляем только = индексу [index:index+1],
    # т. к. при вырезке левая граница включается, а правая не включается, поэтому удалится
    # только тот элемент, который соответствует индекс index) и сравниваем списки
    old_contacts[index:index+1] = []
    # Для сравнения списков отсортировали их в порядке возрастания идентификатора (id) (дз 11)
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Тест переименован с test_delete_contact_not_in_group_via_edit_page и модифицирован (в рамках дз 13)
def test_delete_first_contact_not_in_group_via_edit_page(app):
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
    # Переходим на страницу редактирования первого контакта без группы
    app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Тест
    # Удаляем контакт через страницу редактирования
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (урок 4-7), дз 11
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    # Реализуем сравнение списков (урок 4-8), дз 11
    # В старом списке удаляем первый элемент (удаляем все элементы с 0 по 1 [0:1], но
    # при вырезке левая граница включается, а правая не включается, поэтому удалится
    # только первый элемент, у которого индекс 0) и сравниваем списки
    old_contacts[0:1] = []
    # Для сравнения списков отсортировали их в порядке возрастания идентификатора (id) (дз 11)
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Добавлен тест удаления контакта по индексу, определенному случайным образом (в рамках дз 13)
def test_delete_some_contact_not_in_group_via_birthday_page(app):
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
    # Определен случайным образом индекс удаляемого контакта (дз 13)
    index = randrange(len(old_contacts))
    # Определяем идентификатор контакта по полученному индексу (дз 13)
    contact_id = old_contacts[index].id
    # Переходим на страницу редактирования удаляемого контакта без группы по идентификатору контакта,
    # полученному по индексу (дз 13)
    app.contact.go_to_edit_page_by_contact_id(contact_id)

    # Устанавливаем дату рождения, если её нет
    if app.contact.get_bday() == "0" or app.contact.get_bmonth() == "-":
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_by_contact_id(contact_id)

    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (урок 4-7), дз 11
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    # Реализуем сравнение списков (урок 4-8), дз 11
    # В старом списке удаляем контакт, соответствующий индексу index (удаляем только элемент в позиции
    # index [index:index+1], т. к. при вырезке левая граница включается, а правая не включается, поэтому
    # удалится только тот элемент, у которого индекс index) и сравниваем списки
    old_contacts[index:index+1] = []
    # Для сравнения списков отсортировали их в порядке возрастания идентификатора (id) (дз 11)
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Тест переименован с test_delete_contact_not_in_group_via_birthday_page и модифицирован (в рамках дз 13)
def test_delete_first_contact_not_in_group_via_birthday_page(app):
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
    app.contact.go_to_edit_page_of_first_contact_from_contact_list()

    # Устанавливаем дату рождения, если её нет
    if app.contact.get_bday() == "0" or app.contact.get_bmonth() == "-":
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_of_first_contact_from_birthdays_page()

    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (урок 4-7), дз 11
    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    # Реализуем сравнение списков (урок 4-8), дз 11
    # В старом списке удаляем первый элемент (удаляем все элементы с 0 по 1 [0:1], но
    # при вырезке левая граница включается, а правая не включается, поэтому удалится
    # только первый элемент, у которого индекс 0) и сравниваем списки
    old_contacts[0:1] = []
    # Для сравнения списков отсортировали их в порядке возрастания идентификатора (id) (дз 11)
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Добавлен тест удаления контакта по индексу, определенному случайным образом (в рамках дз 13)
def test_delete_some_contact_not_in_group_via_contact_list(app):
    # Добавляем проверку наличия контакта и создание контакта, если контакта нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    old_contacts = app.contact.get_contact_list_in_group("[none]")
    # Определен случайным образом индекс удаляемого контакта (дз 13)
    index = randrange(len(old_contacts))
    # переходим на страницу редактирования первого контакта без группы по полученному индексу (дз 13)
    app.contact.select_contact_by_index(index)

    # Тест
    # Удаляем контакт из списка контактов
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()

    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Тест переименован с test_delete_contact_not_in_group_via_contact_list и модифицирован (в рамках дз 13)
def test_delete_first_contact_not_in_group_via_contact_list(app):
    # Добавляем проверку наличия контакта и создание контакта, если контакта нет (урок 3-5)
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    old_contacts = app.contact.get_contact_list_in_group("[none]")
    # переходим на страницу редактирования первого контакта без группы
    app.contact.select_first_contact()

    # Тест
    # Удаляем контакт из списка контактов
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()

    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts[0:1] = []
    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Добавлено сравнение списков контактов - дз 11
def test_delete_all_contacts_not_in_group_via_delete_button(app):
    contact1, contact2 = app.data.create_several_contact_with_default_group()

    # пока закомментировала, надо будет дописать проверку наличия контактов
    #app.contact.return_to_home_page_after_contact_creation()
    #app.contact.filter_contacts_by_group("[none]")

    old_contacts = app.contact.get_contact_list_in_group("[none]")

    # Определяем количество контактов в списке (дз 11)
    count = len(old_contacts)

    app.contact.select_all_contacts()
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()

    new_contacts = app.contact.get_contact_list_in_group("[none]")
    assert len(old_contacts) - int(count) == len(new_contacts)



# Добавлен тест удаления контакта по индексу, определенному случайным образом (в рамках дз 13)
def test_delete_some_contact_included_in_group_via_edit_page(app):
    if app.group.count() == 0:
        app.data.create_custom_group()

    groups = app.group.get_group_list()
    index = randrange(len(groups))
    group_name = groups[index].name

    app.contact.open_contact_list_via_addressbook_link()
    app.contact.filter_contacts_by_group(group_name)

    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_custom_group(group_name)

    old_contacts = app.contact.get_contact_list_in_group(group_name)
    index = randrange(len(old_contacts))

    app.contact.go_to_edit_page_by_contact_id(old_contacts[index].id)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    new_contacts = app.contact.get_contact_list_in_group(group_name)
    assert len(old_contacts) - 1 == (len(new_contacts))

    old_contacts[index:index + 1] = []

    assert sorted(old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Добавлено сравнение списков групп - дз 11
def test_delete_contact_included_in_group_via_edit_page(app):
    group = app.data.create_custom_group()
    tmp_contact = app.data.create_contact_with_custom_group(group.name)

    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group.name)

    old_contacts = app.contact.get_contact_list_in_group(group.name)
    contact_id = app.contact.get_contact_id_by_lastname_from_list(old_contacts, tmp_contact.lastname, tmp_contact.firstname)

    app.contact.go_to_edit_page_from_contact_list(tmp_contact.lastname)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    expected_contacts = [c for c in old_contacts if c.id != contact_id]

    new_contacts = app.contact.get_contact_list_in_group(group.name)
    assert len(old_contacts) - 1 == (len(new_contacts))

    assert sorted(expected_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id)



# Добавлено сравнение списков групп - дз 11
def test_delete_several_contacts_included_in_one_group_via_checkboxes_and_delete_button(app):
    group = app.data.create_custom_group()
    contact1, contact2 = app.data.create_several_contact_with_custom_group(group.name)
    app.contact.return_to_home_page_after_contact_creation()

    old_contacts = app.contact.get_contact_list_in_group(group.name)

    tmp_id_list = []
    for c in old_contacts:
        if c.lastname == contact1.lastname or c.lastname == contact2.lastname:
            tmp_id_list.append(c.id)

    app.contact.select_contact_by_lastname(contact1.lastname)
    app.contact.select_contact_by_lastname(contact2.lastname)
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()

    expected_contacts = [c for c in old_contacts if c.id not in tmp_id_list]

    new_contacts = app.contact.get_contact_list_in_group(group.name)
    assert len(old_contacts) - len(tmp_id_list) == (len(new_contacts))
    assert sorted(expected_contacts, key=lambda contact: contact.id) == sorted(new_contacts,
                                                                               key=lambda contact: contact.id)


# Добавлено сравнение списков групп - дз 11
def test_delete_button_pressed_when_contact_not_selected(app):
    app.contact.open_contact_list_via_home_button()

    old_contacts = app.contact.get_contact_list()

    app.contact.delete_contact_from_contact_list()
    app.contact.delete_modal_window_closed()

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)
    assert (sorted (old_contacts, key=lambda contact: contact.id) == sorted(new_contacts, key=lambda contact: contact.id))
