# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


# method for fixture initialization
@pytest.fixture
def app(request):
    fixture = Application()
    # indication of how the fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture


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
