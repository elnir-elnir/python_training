# special file for a fixture which that should be shared by all tests

import pytest
from fixture.application import Application



#
# Global variable has been added to store the fixture between tests  (lesson 3-3)
# This variable will be undefined at first (= None)
fixture = None

# added validation of the fixture in fixture of initialization
@pytest.fixture
def app(request):
    # Inside the function, we declare that we will use global variable
    global fixture

    # added check for correct fixture
    if fixture is None:
        # fixture has been initialized
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        # We determine what to do if fixture has been corrupted (lesson 3-3)
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")

    # # lesson 3-4 - Функция login вынесена из if-then и заменена на интеллектуальную функцию
    # # ensure_login, чтобы выполняеть проверку, нужно ли нам выполнять логин, при каждом обращении
    # # к функции, инициализирующей фикстуру
    # fixture.session.login(username="admin", password="secret")
    return fixture


# Fixture for finalization. Finalization is performed once after all tests have been completed
# To nake the finalization fixture work automatically, add the parameter "property"
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # Logout function has been changed on new ensure_logout function (lesson 3-4)
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture