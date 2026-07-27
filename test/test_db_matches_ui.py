#------------------------------------------------------------------------------
# qa:
# description: Тесты, направленные на проверку соответствия БД и UI
#------------------------------------------------------------------------------
from model.group import Group
from timeit import timeit


# Проверяем соответствие списка групп. В качестве параметров передаются фикстуры (урок 7-3)
def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    # В связи с тем, что в БД хранится информация со всеми введенными символами, а в UI лишние
    # символы пробела в начале и конце удаляются, непосредственно при выполнении теста удаляем
    # лишние пробелы в списке, полученном из БД, с помощью функции clean.
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)



# Это не тест как таковой. Этот метод создан для понимания разницы в скорости выполнения операций
# получения списка групп из БД и через UI (урок 7-4)
# По умолчанию timeit вызывается 1 млн раз, поэтому уменьшили количество вызовов
# assert = False, чтобы получить отображение в консоли результатов, т. к. если тест Passed, мы
# ничего не увидим
def test_group_list_time(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))

    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
