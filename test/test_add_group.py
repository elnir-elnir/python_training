#------------------------------------------------------------------------------
# developer:
# description:
#------------------------------------------------------------------------------

from model.group import Group



def test_add_group(app):
    # calling new helper methods that we created by refactoring
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dfgdfgdfg", header="dfgdfg", footer="dfgfgd"))
    app.session.logout()



def test_add_empty_group(app):
    # calling new helper methods that we created by refactoring
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
