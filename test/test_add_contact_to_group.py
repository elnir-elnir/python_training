#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

def test_include_contact_in_custom_group_on_creation(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.session.logout()



def test_include_created_contact_in_custom_group_after_home_click(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group)
    app.session.logout()



def test_include_created_contact_in_custom_group_after_logo_click(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_addressbook_link()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group)
    app.session.logout()
