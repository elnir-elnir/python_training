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
    # Доступ к параметру hook через значение опции --browser для передачи в фикстуру
    # Application (урок 5-8)
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    # added check for correct fixture
    if fixture is None:
        # fixture has been initialized
        fixture = Application(browser=browser, base_url=base_url)
    else:
        # We determine what to do if fixture has been corrupted (lesson 3-3)
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)

    # # lesson 3-4 - Функция login вынесена из if-then и заменена на интеллектуальную функцию
    # # ensure_login, чтобы выполняеть проверку, нужно ли нам выполнять логин, при каждом обращении
    # # к функции, инициализирующей фикстуру
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture



# Fixture for finalization. Finalization is performed once after all tests have been completed
# To nake the finalization fixture work automatically, add the parameter "property"
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # Logout function has been changed on new ensure_logout function (lesson 3-4)
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture



# Добавляем hook для указания параметров из командной строки (урок 5-8)
# Hook см. здесь: pytest.org/latest/plugins.html?highlight=pytest_addoption#well-specified-hooks
def pytest_addoption(parser):
    # --browser - параметр парсера, action - действие, которое надо выполнить, default - значение
    # по умолчанию
    # Доступ к параметру получаем через объект request
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/")
