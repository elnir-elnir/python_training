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



def test_include_contact_in_modified_custom_group_on_creation(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    modified_group = app.data.full_modified_group(group)
    app.data.create_contact_with_custom_group(modified_group.name)
    app.session.logout()



# Какой вариант правильнее: как в этом тесте или как в предыдущих? Или должен быть некий третий вариант?
def test_include_created_contact_in_modified_custom_group_via_home(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    app.data.created_contact_found_by_lastname_and_included_in_modified_custom_group_via_home()
    app.session.logout()



def test_include_modified_contact_in_custom_group_via_home(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_details_page_from_contact_list(contact.lastname)
    app.contact.go_to_edit_page_from_details_page()
    modified_contact = app.data.contact_with_modified_names(contact)
    app.contact.select_contact_by_lastname(modified_contact.lastname)
    app.contact.set_group(group)
    app.session.logout()



def test_include_created_contact_in_multiple_groups_sequentially_via_home(app):
    app.user.login()
    group1, group2 = app.data.create_several_custom_groups()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group1)
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group2)
    app.session.logout()



def test_include_modified_contact_in_multiple_groups_sequentially_via_home(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group1, group2 = app.data.create_several_custom_groups()
    contact = app.data.create_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.go_to_details_page_from_contact_list(contact.lastname)
    app.contact.go_to_edit_page_from_details_page()
    modified_contact = app.data.contact_with_modified_names(contact)
    app.contact.select_contact_by_lastname(modified_contact.lastname)
    app.contact.set_group(group1)
    app.group.go_to_group_page(group1.name)
    app.contact.select_contact_by_lastname(modified_contact.lastname)
    app.contact.set_group(group2)
    app.group.go_to_group_page(group2.name)
    app.session.logout()




def test_reinclude_created_contact_in_another_group_after_exclusion_via_home(app):
    app.user.login()
    group1, group2 = app.data.create_several_custom_groups()
    contact = app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_home_button()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group1)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group1.name)
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.exclude_contact_from_group(group1.name)
    app.contact.open_contact_list_via_home_button()
    app.contact.reset_contacts_filter()
    app.contact.select_contact_by_lastname(contact.lastname)
    app.contact.set_group(group2)
    app.contact.open_contact_list_via_home_button()
    app.contact.filter_contacts_by_group(group1.name)
    app.contact.filter_contacts_by_group(group2.name)
    app.session.logout()



def test_include_all_created_contacts_in_group(app):
    app.user.login()
    group = app.data.create_custom_group()
    contact1, contact2 = app.data.create_several_contact_with_default_group()
    app.contact.return_to_home_page_after_contact_creation()
    app.contact.select_all_contacts()
    app.contact.set_group(group)
    app.session.logout()

