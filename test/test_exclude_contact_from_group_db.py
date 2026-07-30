#------------------------------------------------------------------------------
# qa:
# description: Тесты на исключение контакта из группы с загрузкой списков из БД
# (дз 22)
#------------------------------------------------------------------------------
import random
import time

from model.contact import Contact
from model.group import Group



def test_exclude_contact_from_single_custom_group_via_home(app, orm, check_ui):
    # Предусловия
    # Проверяем наличие группы
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    # Проверяем, что есть только 1 группа
    # Если групп несколько, удаляем лишние
    groups = orm.get_group_list()
    if len(groups) > 1:
        app.contact.open_contact_list_via_addressbook_link()
        # Определяем случайным образом группу для исключения контакта
        ## Отмечаем все группы
        for g in range(len(groups)):
            app.group.select_group_by_id(groups[g].id)
        ## Случайным образом выбираем группу для отключения чек-бокса
        index = random.randint(0, len(groups))
        app.group.select_group_by_id(groups[index].id)
        # Удаляем все отмеченные группы
        app.group.delete_group()

    # Получаем группу для исключения контакта, т. к.группа единственная, то применяем индекс 0
    #assert len(orm.get_group_list()) == 1
    group = orm.get_group_list()[0]

    # Проверяем наличие контактов
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_in_group(group)) == 0:
        app.data.create_contact_with_custom_group(group.name)

    # Тест
    # Получаем список контактов в группе до исключения контакта из группы
    old_contacts = orm.get_contacts_in_group(group)

    # Случайным образом выбираем контакт для исключения из группы
    contact = random.choice(old_contacts)

    # Получаем список групп, в которые включен данный контакт
    old_contact_groups = orm.get_groups_for_contact(contact)

    # Исключаем контакт из группы
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group.name)
    app.contact.select_contact_by_id(contact.id)
    app.contact.exclude_contact_from_group(group.name)

    # Получаем список контактов в группе и список групп для контакта после исключения контакта из группы
    new_contacts = orm.get_contacts_in_group(group)
    new_contact_groups = orm.get_groups_for_contact(contact)

    # Удаляем исключенный контакт из списка, полученного до исключения контакта из группы
    old_contacts.remove(contact)
    # Удаляем группу, из которой исключен контакт из списка, полученного до исключения контакта из группы
    old_contact_groups.remove(group)

    # Проверки
    # Проверяем количество контактов в группе и количество групп для контакта после исключения контакта
    assert len(old_contacts) == len(new_contacts)
    assert len(old_contact_groups) == len(new_contact_groups)

    # Проверяем соответствие списков контактов в группе и списков групп исключенного контакта
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert sorted(old_contact_groups, key=Group.id_or_max) == sorted(new_contact_groups,
                                                                     key=Group.id_or_max)

    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group.name),
                       key=Contact.id_or_max))
