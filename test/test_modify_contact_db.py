#------------------------------------------------------------------------------
# qa:
# description: Тесты на модификацию контакта с загрузкой данных из БД (дз 20)
#------------------------------------------------------------------------------

import random

from model.contact import Contact
from model.group import Group


def test_modify_some_contact_when_contact_not_in_group_via_details_from_home_page(app, orm,check_ui):
    # Предусловия
    group_name = "[none]"
    old_contacts = orm.get_contacts_not_in_any_group()
    print("old_contacts:", old_contacts)
    if len(old_contacts) == 0:
        app.contact.create_for_default_values(Contact(firstname="test", lastname="test"))
        old_contacts = orm.get_contacts_not_in_any_group()

    contact = random.choice(old_contacts)
    print("contact:", contact)

    modified_contact = Contact(id=contact.id, firstname="modified firstname",
                               middlename=contact.middlename, lastname="modified lastname",
                               bday=contact.bday, bmonth=contact.bmonth)
    print("modified_contact:", modified_contact)

    app.contact.open_contact_list_via_addressbook_link()
    app.contact.select_contact_by_id(contact.id)
    app.contact.go_to_details_page_by_contact_id(contact.id)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact_for_default_values(modified_contact)
    app.contact.open_contact_list_via_addressbook_link()
    app.contact.filter_contacts_by_group(group_name)

    new_contacts = orm.get_contacts_not_in_any_group()
    print("new_contacts:", new_contacts)

    assert len(old_contacts) == len(new_contacts)

    old_contacts.remove(contact)
    old_contacts.append(modified_contact)
    print("modified_contacts:", old_contacts)

    assert old_contacts == new_contacts

    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group_name),
                                                                     key=Contact.id_or_max))
        print("sorted_new_contacts: ", sorted(new_contacts, key=Contact.id_or_max))
        print("sorted_app_contacts: ", sorted(app.contact.get_contact_list_in_group(group_name),
                                              key=Contact.id_or_max))



def test_modify_some_contact_when_contact_not_in_group_via_details_from_birthday_page(app, orm, check_ui):
    # Предусловия
    group_name = "[none]"
    old_contacts = orm.get_contacts_not_in_any_group()
    print("old_contacts:", old_contacts)
    if len(old_contacts) == 0:
        app.contact.create_for_default_values(Contact(firstname="test", lastname="test",
                                                      bday="31", bmonth="July", byear="2000"))
        old_contacts = orm.get_contacts_not_in_any_group()

    contact = random.choice(old_contacts)
    print("contact:", contact)

    if orm.has_birthday(contact) is False:
        app.contact.open_contact_list_via_addressbook_link()
        app.contact.go_to_edit_page_by_contact_id(contact.id)
        app.contact.set_birthday(bday="3", bmonth="May", byear="1999")

    modified_contact = Contact(id=contact.id, firstname="modified firstname",
                               middlename=contact.middlename, lastname="modified lastname",
                               bday=contact.bday, bmonth=contact.bmonth)
    print("modified_contact:", modified_contact)

    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_details_page_by_contact_id(contact.id)
    app.contact.go_to_edit_page_from_details_page()
    app.contact.edit_contact_for_default_values(modified_contact)
    app.contact.open_contact_list_via_addressbook_link()
    app.contact.filter_contacts_by_group(group_name)

    new_contacts = orm.get_contacts_not_in_any_group()
    print("new_contacts:", new_contacts)

    assert len(old_contacts) == len(new_contacts)

    old_contacts.remove(contact)
    old_contacts.append(modified_contact)
    print("modified_contacts:", old_contacts)

    assert old_contacts == new_contacts

    if check_ui:
        assert (sorted(new_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list_in_group(group_name),
                                                                     key=Contact.id_or_max))
        print("sorted_new_contacts: ", sorted(new_contacts, key=Contact.id_or_max))
        print("sorted_app_contacts: ", sorted(app.contact.get_contact_list_in_group(group_name),
                                              key=Contact.id_or_max))
