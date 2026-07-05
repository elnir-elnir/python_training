#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

# Methods app.session.login(), app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# simplified removal method
def test_delete_first_group(app):
    app.group.delete_first_group()



def test_delete_custom_group_when_group_has_no_contacts(app):
    app.group.delete_group_by_name((app.data.create_custom_group()).name)



def test_delete_custom_group_when_group_has_contacts(app):
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.group.delete_group_by_name(group.name)



def test_delete_modified_group_when_group_has_no_contacts(app):
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    app.group.delete_group_by_name(modified_group.name)



def test_delete_modified_group_when_group_has_contacts(app):
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    contact = app.data.create_contact_with_custom_group(modified_group.name)
    app.group.delete_group_by_name(modified_group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.filter_contacts_by_group(group_name="[none]")



def test_delete_several_groups(app):
    group1, group2 = app.data.create_several_custom_groups()
    app.group.select_group_by_name(group1.name)
    app.group.select_group_by_name(group2.name)
    app.group.delete_group()
