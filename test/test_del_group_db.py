#------------------------------------------------------------------------------
# qa:
# description: Тесты на удаление группы с загрузкой данных из БД
#------------------------------------------------------------------------------

import random

from model.group import Group


# Файл создан в рамках урока 7-4
# Основные пояснения по тестам см. в файле test_del_group



# Добавляем параметр для вызова альтернативного способа загрузки списка групп (урок 7-4)
# Параметр check_ui добавлен для реализации отключаемой проверки соответствия списка групп из UI
# списку групп из БД, чтобы включать эту проверку при запуске теста (урок 7-5)
# !!!!!При выполнении теста в IE тест падает в
# if check_ui:
# >           assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
#                                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                                                      key=Group.id_or_max)
# с ошибкой:
# selenium.common.exceptions.JavascriptException: Message: Error from JavaScript: Объект не поддерживает свойство или метод "includes"
# env\Lib\site-packages\selenium\webdriver\remote\errorhandler.py:232: JavascriptException
# Возможно, что проблема решена в более новой версии IE и веб-драйвера (проверить после курса).
# Если не решена, то проверку надо переписать с учетом этой особенности IE
# Установленные версии: IE 11.1882.26100.0, IEDriverServer.exe 4.14.0.0 (32-bit)!!!!!
def test_delete_some_group(app, db, check_ui):
    # Подсчет количества групп также выполняем через обращение к базе данных (урок 7-4)
    #if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        tmp_group = Group(name="test")
        app.group.create(tmp_group)

    # Меняем способ загрузки списка групп (урок 7-4)
    old_groups = db.get_group_list()

    # Меняем способ удаления группы, т. к. способы сортировки списка в БД и UI разные, и удаление по
    # индексу теперь не подходит. Новый способ - поиск и удаление по идентификатору (урок 7-4)
    #index = randrange(len(old_groups))
    #app.group.delete_group_by_index(index)
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)

    # Меняем способ загрузки списка групп (урок 7-4)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

    # Способ удаления группы изменен с "по индексу" на "по идентификатору" (урок 7-4)
    #old_groups[index:index+1] = []
    old_groups.remove(group)

    assert old_groups == new_groups
    # Добавляем отключаемую проверку соответствия списка групп в UI списку групп из БД
    # Для этого добавлен параметр в тестовую функцию и создана фикстура (урок 7-5)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                 key=Group.id_or_max)
