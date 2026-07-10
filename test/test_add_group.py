#------------------------------------------------------------------------------
# developer:
# description:
#------------------------------------------------------------------------------

from model.group import Group



# Methods app.session.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Переписываем тесты в соответствии с уроком 4-7 - Загружаем информацию
# из тестируемого приложения в виде списков

def test_add_group(app):
    # Получаем старый список групп из приложения
    old_groups = app.group.get_group_list()

    # Для последующего сравнения списков модифицируем тест - объявляем локальную
    # переменную group и передаем ее в качестве параметра в метод создания группы (урок 4-9)
    group = Group(name="", header="", footer="")
    app.group.create(group)

    # Получаем новый список групп (урок 4-7)
    new_groups = app.group.get_group_list()

    # Проверяем, что новый список на единицу длинее старого (урок 4-7)
    assert len(old_groups) + 1 == len(new_groups)

    # В список групп, полученный из приложения, добавляем новую группу (урок 4-9)
    old_groups.append(group)

    # # Сравниваем группы, но тест упал, т. к. не совпал порядок групп в списке (урок 4-9)
    # # Поэтому данный метод модифицируем в следующий за ним - с сортировкой (а текущий метод
    # # я закомментировала
    # assert old_groups == new_groups

    # Создаем новую функцию сравнения, в которой указываем в качестве ключа идентификатор - оба
    # списка сортируем по одинаковым правилам (урок 4-9)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# Аналогично предыдущему тесту модифицируем и этот тест (урок 4-9)
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
