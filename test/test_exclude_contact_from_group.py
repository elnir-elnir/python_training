#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

def test_exclude_contact_from_single_custom_group_via_home(app):
    app.user.login()
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_custom_group(group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group.name)
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.exclude_contact_from_group(group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group.name)
    app.session.logout()


def test_exclude_contact_from_single_modified_group_after_group_modification_via_home(app):
    app.user.login()
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_custom_group(group.name)
    modified_group = app.data.full_modified_group(group)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(modified_group.name)
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.exclude_contact_from_group(modified_group.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(modified_group.name)
    app.session.logout()


def test_exclude_contact_from_one_of_several_groups_via_home(app):
    app.user.login()
    group1, group2 = app.data.create_several_custom_groups()
    contact = app.data.create_contact_with_custom_group(group1.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group2)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group1.name)
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.exclude_contact_from_group(group1.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group1.name)
    app.contact.filter_contacts_by_group(group2.name)
    app.session.logout()
