#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

def test_delete_contact_not_in_group_via_edit_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_home_button()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_contact_not_in_group_via_birthday_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_contact_not_in_group_via_contact_list(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_all_contacts_not_in_group_via_delete_button(app):
    app.user.login()
    contact1, contact2 = app.data.create_several_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_all_contacts()
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_contact_included_in_group_via_edit_page(app):
    app.user.login()
    contact = app.data.create_contact_with_custom_group(app.data.create_custom_group().name)
    app.contact.open_contact_list_via_home_button()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.contact.delete_contact_from_edit_page()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_several_contacts_included_in_one_group_via_checkboxes_and_delete_button(app):
    app.user.login()
    group = app.data.create_custom_group()
    contact1, contact2 = app.data.create_several_contact_with_custom_group(group.name)
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_contact_by_lastname(contact1.lastname)
    app.contact.select_contact_by_lastname(contact2.lastname)
    app.contact.delete_contact_from_contact_list()
    app.contact.return_to_home_page_after_contact_deletion()
    app.session.logout()


def test_delete_button_pressed_when_contact_not_selected(app):
    app.user.login()
    app.open_home_page()
    app.contact.delete_contact_from_contact_list()
    app.contact.delete_modal_window_closed()
    app.session.logout()
