#------------------------------------------------------------------------------
# qa:
# description: Тесты на удаление группы с загрузкой данных из БД
#------------------------------------------------------------------------------

import random

from model.group import Group


# Файл создан в рамках урока 7-4
# Основные пояснения по тестам см. в файле test_del_group



# Добавляем параметр для вызова альтернативного способа загружки списка групп (урок 7-4)
def test_delete_some_group(app, db):
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

    assert sorted(old_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id)
