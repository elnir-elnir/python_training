#------------------------------------------------------------------------------
# developer:
# description:
#------------------------------------------------------------------------------

from model.group import Group



# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_add_group(app):
    app.group.create(Group(name="dfgdfgdfg", header="dfgdfg", footer="dfgfgd"))



def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
