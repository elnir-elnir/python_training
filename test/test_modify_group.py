#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------


# Methods app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_full_modify_new_group_initial_without_contacts(app):
    group = app.data.create_custom_group()
    app.data.full_modified_group(group)



def test_confirm_new_group_modify_without_changes_when_group_has_no_contacts(app):
    group_name = app.data.create_custom_group().name
    app.group.open_and_confirm_group_modify_without_changes_by_name(group_name)



def test_full_modify_new_group_initial_with_one_contact(app):
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.data.full_modified_group(group)



def test_full_modify_group_subsequent_when_group_has_no_contacts(app):
    group = app.data.create_custom_group()
    app.data.full_remodified_group(group)



def test_full_modify_group_subsequent_when_group_with_one_contact(app):
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.data.full_remodified_group(group)
