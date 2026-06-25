# -*- coding: utf-8 -*-



def test_set_group_in_contact_creation_mode(app):
    app.session.login(username="admin", password="secret")
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.session.logout()


def test_set_group_for_created_contact_with_home_button(app):
    app.session.login(username="admin", password="secret")
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_using_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group)
    app.session.logout()


def test_set_group_for_created_contact_with_addressbook_link(app):
    app.session.login(username="admin", password="secret")
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_using_addressbook_link()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group)
    app.session.logout()
