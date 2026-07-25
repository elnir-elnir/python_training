# special file for a fixture which that should be shared by all tests
import json
import os.path

import pytest

from fixture.application import Application



#
# Global variable has been added to store the fixture between tests  (lesson 3-3)
# This variable will be undefined at first (= None)
fixture = None
# Определяем глобальную переменную, чтобы конфигурационный файл читать только один раз (при создании
# фикстуры), а не при выполнении каждого теста (урок 6-7)
target = None

# added validation of the fixture in fixture of initialization
@pytest.fixture
def app(request):
    # Inside the function, we declare that we will use global variable
    global fixture
    # Указываем, что собираемся использовать глобальную переменную в функции, которая инициализирует
    # фикстуру (урок 6-7)
    global target
    # Доступ к параметру hook через значение опции --browser для передачи в фикстуру
    # Application (урок 5-8)
    browser = request.config.getoption("--browser")

    # Проверяем, загружена ли конфигурация (урок 6-7)
    if target is None:
        # Определена переменная для хранения информации о расположении конфигурационного файла
        # относительно файла conftest.py с помощью специальной встроенной переменной __file__,
        # чтобы не указывать путь до файла в ранере (урок 6-8)
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   request.config.getoption("--target"))
        # Читаем конфигурационный файл, при этом удалена переменная base_url, перенесенная в
        # конфигурационный файл (урок 6-7)
        with open(config_file) as f:
            target = json.load(f)

    # !!!Чтобы при работе в IDE загружался конфигурационный файл, необходимо явно указать в ранере
    # место расположения этого файла, т. к. по умолчанию при запуске в IDE рабочей директорией считается
    # директория, в которой расположен файл python.exe, а не директория проекта.
    # Для этого в ранере через Edit configuration задаем путь до конфигурационного файла в поле
    # "Working directory", т. е. в моем случае путь: C:/Users/.../developing/PythonProject/python_training
    # (см. на примере ранера Python tests in test_add_group.py (chrome))

    # added check for correct fixture
    # Условие оптимизировано - удален блок else (из урока 3-3) за счет объединения условий
    # в результате чего удалено дублирование (урок 6-7)
    if fixture is None or not fixture.is_valid():
        # fixture has been initialized
        # Переменная base_url читается из конфигурационного файла (урок 6-7)
        fixture = Application(browser=browser, base_url=target['base_url'])

    # # lesson 3-4 - Функция login вынесена из if-then и заменена на интеллектуальную функцию
    # # ensure_login, чтобы выполняеть проверку, нужно ли нам выполнять логин, при каждом обращении
    # # к функции, инициализирующей фикстуру
    # Переменные username и password читаются из конфигурационного файла (урок 6-7)
    fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    # Определение стартовой страницы приложения перенесено в конфигурационный файл, ссылка на который
    # должна быть указана при запуске тестов в параметре target (урок 6-7)
    parser.addoption("--target", action="store", default="target.json")
