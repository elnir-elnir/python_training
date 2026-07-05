#------------------------------------------------------------------------------
# qa:
# description: Тесты в соответствии с уроком 3-2
#------------------------------------------------------------------------------
from model.group import Group


# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)
def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New group"))



def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
