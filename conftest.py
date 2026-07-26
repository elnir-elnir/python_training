# special file for a fixture which that should be shared by all tests
import json
import os.path
import importlib
import jsonpickle

import pytest

from fixture.application import Application
from fixture.db import DbFixture

#
# Global variable has been added to store the fixture between tests  (lesson 3-3)
# This variable will be undefined at first (= None)
fixture = None
# Определяем глобальную переменную, чтобы конфигурационный файл читать только один раз (при создании
# фикстуры), а не при выполнении каждого теста (урок 6-7)
target = None


# Добавлен метод загрузки конфигурационного файла в связи с добавлением фикстуры для взаимодействия
# с базой данных и дополнением конфигурационного файла информацией о БД(урок 7-2)
def load_config(file):
    global target
    if target is None:
        # Определена переменная для хранения информации о расположении конфигурационного файла
        # относительно файла conftest.py с помощью специальной встроенной переменной __file__,
        # чтобы не указывать путь до файла в ранере (урок 6-8)
        # Здесь:
        # os.path.abspath(__file__) - получаем путь к файлу conftest.py
        # os.path.dirname(...) - определяем директорию, в которой расположен файл conftest.py
        # os.path.join(...(...)) - подклеиваем путь к файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        # Читаем конфигурационный файл, при этом удалена переменная base_url, перенесенная в
        # конфигурационный файл (урок 6-7)
        with open(config_file) as f:
            target = json.load(f)
    return target


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

    # Проверяем, загружена ли конфигурация (урок 6-7). В связи с созданием метода load_config
    #  внесены изменения и добавлена переменная web_config (урок 7-2)
    # ['web'] - означает, что берутся данные блока "web" конфигурационного файла
    web_config = load_config(request.config.getoption("--target"))['web']

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
        # target заменен на web_config (урок 7-2)
        fixture = Application(browser=browser, base_url=web_config['base_url'])

    # # lesson 3-4 - Функция login вынесена из if-then и заменена на интеллектуальную функцию
    # # ensure_login, чтобы выполняеть проверку, нужно ли нам выполнять логин, при каждом обращении
    # # к функции, инициализирующей фикстуру
    # Переменные username и password читаются из конфигурационного файла (урок 6-7)
    # target заменен на web_config (урок 7-2)
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture



# Существует 2 способа создания фикстуры для взаимодействия с БД:
# 1) независимая фикстура - задается в файле conftest.py, вариант подходит для ситуации, когда необходимо
# выполнять тесты не только с запуском браузера, но и без запуска браузера;
# 2) как вспомогательный методы (Helper), который вызывается при запуске фикстуры Application - вариант
# подходит для выполнения тестов только с запуском браузера
# Добавляем независимую фикстуру для взаимодействия с базой данных по упрощенному варианту, т. е.
# предполагаем, что она не может сломаться
# Фикстура будет иницилизироваться в начале сессии, а в конце останавливаться(урок 7-2)
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



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


# Добавлен метод для параметризации тестовой функции путем загрузки тестовых данных из указанного модуля
# В качестве параметра передается особый объект metafunc, через который можно получить практически полную
# информацию о тестовой функции (урок 6-11)
# Это своего рода фабрика тестов (генератор тестов), которая позволяет динамически посдтавлять значения
# параметров
def pytest_generate_tests(metafunc):
    # Получаем информацию о фикстурах (они же параметры), которые есть у этой тестовой функции
    for fixture in metafunc.fixturenames:
        # Нас интересуют только те параметры, которые начинаются с префикса data_
        if fixture.startswith("data_"):
            # Как-только встретилась фикстура data_, загружаем тестовые данные из модуля, который имеет
            # такое же название, как фикстура, но обрезанное (удалены первые 5 символов)
            testdata = load_from_module(fixture[5:])
            # Используем загруженные тестовые данные, чтобы параметризовать тестовую функцию. Также
            # подставляем строковое представление (ids=)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

        # Дополняем метод проверкой фикстуры для загрузки из файла json (урок 6-12)
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# Добавлен метод для загрузки данных из модуля с заданным именем (урок 6-11)
def load_from_module(module):
    # Указываем названи е модуля, который хотим импортировать ("data.%s" % module) и берем из него
    # данные (testdata)
    return importlib.import_module("data.%s" % module).testdata


# Добавлен метод загрузки тестовых данных из файла json (урок 6-12)
# Для преобразования данных из файла json необходимо импортировать библиотеку jsonpickle
# (pip install jsonpickle) в env проекта и меняем метод записи сгенерированных тестовых данных
# в файл в generator\group.py, т. к. нам необходимо связать загружаемые данные
# с конкретным классом (урок 6-12)
# Библиотека jsonpickle: https://jsonpickle.github.io/
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        # Перекодируем прочитанный файл обратно в исходный формат в виде набора объектов Python
        return jsonpickle.decode(f.read())
