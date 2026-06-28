#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

def test_modify_contact_names_when_contact_not_in_group_via_details_from_home_page(app):
    app.user.login()
    app.data.contact_with_modified_names_via_details_from_home_page()
    app.session.logout()



def test_modify_contact_names_when_contact_not_in_group_via_edit_from_home_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_modified_names(contact)
    app.session.logout()



def test_modify_contact_names_when_contact_not_in_group_via_details_from_birthday_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_details_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)
    app.contact.go_to_edit_page_from_details_page()
    app.data.contact_with_modified_names(contact)
    app.session.logout()



def test_modify_contact_names_when_contact_not_in_group_via_edit_from_birthday_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_next_birthdays_page()
    app.contact.go_to_edit_page_from_birthday_list(contact.lastname, contact.firstname, contact.middlename)
    app.data.contact_with_modified_names(contact)
    app.session.logout()



def test_modify_contact_names_when_contact_in_group_via_edit_from_home_page(app):
    app.user.login()
    contact = app.data.create_contact_with_custom_group((app.data.create_custom_group()).name)
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_modified_names(contact)
    app.session.logout()



def test_remodify_contact_names_when_contact_not_in_group_via_edit_from_birthday_page(app):
    app.user.login()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_remodified_names_via_edit_from_birthday_page(contact)
    app.session.logout()



def test_remodify_contact_names_when_contact_in_group_via_edit_from_birthday_page(app):
    app.user.login()
    contact = app.data.create_contact_with_custom_group((app.data.create_custom_group()).name)
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_edit_page_from_contact_list(contact.lastname)
    app.data.contact_with_remodified_names_via_edit_from_birthday_page(contact)
    app.session.logout()
