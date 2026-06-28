#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

# simplified removal method
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()



def test_delete_custom_group_when_group_has_no_contacts(app):
    app.user.login()
    app.group.delete_group_by_name((app.data.create_custom_group()).name)
    app.session.logout()



def test_delete_custom_group_when_group_has_contacts(app):
    app.user.login()
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.group.delete_group_by_name(group.name)
    app.session.logout()



def test_delete_modified_group_when_group_has_no_contacts(app):
    app.user.login()
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    app.group.delete_group_by_name(modified_group.name)
    app.session.logout()



def test_delete_modified_group_when_group_has_contacts(app):
    app.user.login()
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    contact = app.data.create_contact_with_custom_group(modified_group.name)
    app.group.delete_group_by_name(modified_group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.filter_contacts_by_group(group_name="[none]")
    app.session.logout()



def test_delete_several_groups(app):
    app.user.login()
    group1, group2 = app.data.create_several_custom_groups()
    app.group.select_group_by_name(group1.name)
    app.group.select_group_by_name(group2.name)
    app.group.delete_group()
    app.session.logout()
