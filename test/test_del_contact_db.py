#------------------------------------------------------------------------------
# qa:
# description: Тесты на удаление контакта с загрузкой списков из БД (дз 20)
#------------------------------------------------------------------------------
import random

from model.contact import Contact


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
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                     key=Contact.id_or_max)
