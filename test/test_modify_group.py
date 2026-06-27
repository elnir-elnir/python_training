#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------



def test_full_modify_new_group_initial_without_contacts(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    app.data.full_modified_group(group)
    app.session.logout()
    #print (group.name, group.header, group.footer)



def test_confirm_new_group_modify_without_changes_when_group_has_no_contacts(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group_name = app.data.create_custom_group().name
    app.group.open_and_confirm_group_modify_without_changes_by_name(group_name)
    app.session.logout()



def test_full_modify_new_group_initial_with_one_contact(app):
    #app.session.login(username="admin", password="secret")
    app.user.login()
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.data.full_modified_group(group)
    app.session.logout()



def test_full_modify_group_subsequent_when_group_has_no_contacts(app):
    app.user.login()
    group = app.data.create_custom_group()
    app.data.full_remodified_group(group)
    app.session.logout()



def test_full_modify_group_subsequent_when_group_with_one_contact(app):
    app.user.login()
    group = app.data.create_custom_group()
    app.data.create_contact_with_custom_group(group.name)
    app.data.full_remodified_group(group)
    app.session.logout()
