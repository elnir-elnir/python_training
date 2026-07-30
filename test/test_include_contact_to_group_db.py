#------------------------------------------------------------------------------
# qa:
# description: Тесты на включение контакта в группу с загрузкой списков из БД
# (дз 22)
#------------------------------------------------------------------------------
import random

from model.contact import Contact
from model.group import Group



def test_include_contact_in_custom_group_on_creation(app, orm, check_ui):
    # Предусловия
    # Получаем список групп
    groups = orm.get_group_list()
    # Проверяем наличие групп
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    # Обновляем список групп
    groups = orm.get_group_list()
    # Случайным образом выбираем группу
    group = random.choice(groups)
    print("group: ", group)

    # Тест
    # Получаем список контактов, включенных в выбранную группу
    old_contacts = orm.get_contacts_in_group(group)
    print("old_contacts: ", old_contacts)

    # Создаем контакт с включением в выбранную группу
    contact = app.data.create_contact_with_custom_group(group.name)
    # Добавляем созданный контакт в ранее полученный список контактов, включенных в выбранную группу
    old_contacts.append(contact)
    print("new_old_contacts: ", old_contacts)

    # Получаем новый список контактов, включенных в выбранную группу
    new_contacts = orm.get_contacts_in_group(group)
    print("new_contacts: ", new_contacts)

    # # Переходим на главную страницу и отбираем контакты по выбранной группе
    # app.contact.open_contact_list_via_addressbook_link()

    # Проверки
    # Проверяем количество контактов в группе
    assert len(old_contacts) == len(new_contacts)
    print("len_old_contacts: ", len(old_contacts), "  len_new_contacts: ", len(new_contacts))

    # Сравниваем списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group.name),
                       key=Contact.id_or_max))
        print("sorted(new_contacts): ", sorted(new_contacts, key=Contact.id_or_max))
        print("app_contacts: ", sorted(app.contact.get_contact_list_in_group(group.name),
                                       key=Contact.id_or_max))



def test_include_created_contact_in_custom_group_after_home_click(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(orm.get_group_list())
    print("group: ", group)

    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_any_group()) == 0:
        app.data.create_contact_with_default_group()

    contact = random.choice(orm.get_contacts_not_in_any_group())
    print("contact: ", contact)

    old_contact_groups = orm.get_groups_for_contact(contact)

    old_contacts = orm.get_contacts_in_group(group)
    print("old_contacts: ", old_contacts)

    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_id(contact.id)
    app.contact.set_group(group.name)

    old_contacts.append(contact)
    print("new_old_contacts: ", old_contacts)

    old_contact_groups.append(group)

    new_contacts = orm.get_contacts_in_group(group)
    print("new_contacts: ", new_contacts)

    new_contact_groups = orm.get_groups_for_contact(contact)

    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    assert len(old_contact_groups) == len(new_contact_groups)
    assert sorted(old_contact_groups, key=Contact.id_or_max) == sorted(new_contact_groups,
                                                                       key=Contact.id_or_max)

    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group.name), key=Contact.id_or_max))



