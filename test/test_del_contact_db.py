#------------------------------------------------------------------------------
# qa:
# description: Тесты на удаление контакта с загрузкой списков из БД (дз 20)
#------------------------------------------------------------------------------
import random

from model.contact import Contact
from model.group import Group


def test_delete_some_contact_not_in_group_via_edit_page(app, orm, check_ui):
    # Предусловия
    tmp_contacts = orm.get_contacts_not_in_any_group()
    print("tmp_contacts:  ", tmp_contacts)
    # Если нет контактов без группы — создаём контакт
    if len(tmp_contacts) == 0: # дз 20
        app.data.create_contact_with_default_group()

    # Получаем список контактов из БД до удаления контакта (дз 20)
    old_contacts = orm.get_contacts_not_in_any_group()
    print("old_contacts:  ", old_contacts)

    # Определен случайным образом контакт для удаления (дз 20)
    contact = random.choice(old_contacts)
    print("contact to delete: ", contact)

    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_addressbook_link()

    # Переходим на страницу редактирования удаляемого контакта без группы по идентификатору
    # контакта (дз 20)
    app.contact.go_to_edit_page_by_contact_id(contact.id)

    # Тест
    # Удаляем контакт через страницу редактирования
    app.contact.delete_contact_from_edit_page()

    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (дз 20)
    new_contacts = orm.get_contacts_not_in_any_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    print("new_contacts:  ", new_contacts)

    # Реализуем сравнение списков
    # Способ удаления контакта изменен с "по индексу" на "по идентификатору" (урок 7-4)
    # old_groups[index:index+1] = []
    old_contacts.remove(contact)

    assert old_contacts == new_contacts
    print("new old_contacts:  ", old_contacts)

    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5, дз 20)
    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group("[none]"),
                                                                     key=Contact.id_or_max))



def test_delete_some_contact_included_in_one_group_via_edit_page(app, orm, check_ui, data_groups):
    # Предусловия
    # Проверяем наличие контактов, включенных только в одну группу (дз 20)
    if len(orm.get_contacts_included_in_one_group()) == 0:
        # Проверяем наличие групп и групп, в которые не включены контакты. При остутствии создаем
        # группу
        if len(orm.get_group_list()) == 0 or len(orm.get_group_list_without_contacts()) == 0:
            #Group(app.data.create_custom_group())
            group = data_groups
            app.group.create(group)
        # Случайным образом получаем группу, в которой нет контактов
        group = random.choice(orm.get_group_list_without_contacts())
        print("group: ", group)

        # Проверяем наличие контактов и контактов, не включенных в какую-либо группу
        # При отсутствии создаем контакт, включенный в группу, выбранную на предыдущем шаге
        if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_any_group()) == 0:
            app.data.create_contact_with_custom_group(group.name)

        # Если есть контакт, не включенный в какую-либо группу, включаем его в группу, выбранную
        # при выполнении предыдущих шагов
        if len(orm.get_contacts_not_in_any_group()) > 0:
            contact = random.choice(orm.get_contacts_not_in_any_group())
            app.contact.open_contact_list_via_addressbook_link()
            app.contact.select_contact_by_id(contact.id)
            app.contact.set_group(group.name)

    # Получаем список контактов из БД до удаления контакта (дз 20)
    old_contacts = orm.get_contacts_included_in_one_group()
    print("old_contacts:  ", old_contacts)

    # Определен случайным образом контакт для удаления (дз 20)
    contact = random.choice(old_contacts)
    print("contact to delete: ", contact)

    # Определена группа, в которую включен выбранный контакт (дз 20)
    group = orm.get_group_for_contact_by_index(contact, 0)
    print("group:  ", group)

    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_addressbook_link()

    # Переходим на страницу редактирования удаляемого контакта без группы по идентификатору
    # контакта (дз 20)
    app.contact.go_to_edit_page_by_contact_id(contact.id)

    # Тест
    # Удаляем контакт через страницу редактирования контакта и возвращаемся на главную страницу
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    # Добавляем проверку списка после удаления со списком, полученным из тестируемого
    # приложения (дз 20)
    new_contacts = orm.get_contacts_included_in_one_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    print("new_contacts:  ", new_contacts)

    # Реализуем сравнение списков
    old_contacts.remove(contact)

    assert old_contacts == new_contacts
    print("new old_contacts:  ", old_contacts)

    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5, дз 20)
    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group.name),
                                                                     key=Contact.id_or_max))
        print("group: ", "id = ", group.id, "name = ", group.name, "header = ", group.header, "footer = ", group.footer)



# Добавлен тест удаления контакта со страницы next_birthday (дз 20)
def test_delete_some_contact_in_one_group_via_birthday_page(app, orm, check_ui):
    # Предусловия
    # Проверяем наличие групп с контактами (дз 20)
    if len(orm.get_contacts_included_in_one_group()) == 0:
        if len(orm.get_group_list()) == 0 or len(orm.get_group_list_without_contacts()) == 0:
            app.group.create(Group(app.data.create_custom_group()))
            # group = data_groups
            # app.group.create(group)
        group = random.choice(orm.get_group_list_without_contacts())
        print("group: ", group)

        if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_any_group()) == 0:
            app.data.create_contact_with_custom_group(group.name)

        if len(orm.get_contacts_not_in_any_group()) > 0:
            contact = random.choice(orm.get_contacts_not_in_any_group())
            app.contact.open_contact_list_via_addressbook_link()
            app.contact.select_contact_by_id(contact.id)
            app.contact.set_group(group.name)

    old_contacts = orm.get_contacts_included_in_one_group()
    print("old_contacts:  ", old_contacts)

    contact = random.choice(old_contacts)

    group = orm.get_group_for_contact_by_index(contact, 0)

    if orm.has_birthday(contact) is False:
        app.contact.open_contact_list_via_addressbook_link()
        app.contact.go_to_edit_page_by_contact_id(contact.id)
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_by_contact_id(contact.id)

    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()

    new_contacts = orm.get_contacts_not_in_any_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    print("new_contacts:  ", new_contacts)

    old_contacts.remove(contact)

    assert old_contacts == new_contacts
    print("new old_contacts:  ", old_contacts)

    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5, дз 20)
    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group.name),
                                                                     key=Contact.id_or_max))
