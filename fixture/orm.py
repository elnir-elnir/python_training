#------------------------------------------------------------------------------
# qa:
# description: Класс для сопоставления классов, полей объектов кода Python и
# таблиц БД
#------------------------------------------------------------------------------

from datetime import datetime

# Реализация ORM поддерживает связи (или отношения) между объектами, в результате для
# извлечения объектов (в т. ч. объектов со связями) не потребуется писать запросы SQL,
# они будут генерироваться автоматически (урок 7-7)
# Для реализации ORM используются специальные инструменты:
# - PonyORM (http://ponyorm.com, pip install pony) - взаимодействует только с
# "альтернативным" драйвером БД - PyMySQL;
# - иные - здесь (http://www.pythoncentral.io/sqlalchemy-vs-orms) сравнение различных
# ORM-систем для Python

from pony.orm import *

from model.group import Group


class ORMFixture:

    db = Database()

    # Описываем структуру таблицы group_list
    # Параметр db.Entity нужен для того, чтобы привязать этот класс к базе данных - к тому объекту,
    # который только что создали, - в качестве базового указывается вложенный внутрь этого объекта
    # класс db.Entity. Т. е. теперь этот класс описывает какие-то объекты, которые будут сохраняться
    # в эту базу данных. Т. е. класс ORMGroup наслеедуются от класса db.Entity
    class ORMGroup(db.Entity):
        # Указываем название таблицы БД
        _table_ = "group_list"
        # column - для сопоставления столбцов таблиц БД и полей объекта класса в коде
        id = PrimaryKey(int, column="group_id")
        # Optional - т. к. поле может быть пустым
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")


    # Описываем структуру таблицы addressbook
    class ORMContact(db.Entity):
        # Указываем название таблицы БД
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")


    # Описываем привязку к базе данных. В качестве параметров принимается такой же набор, как у db.fixture
    def __init__(self, host, name, user, password):
        # Привязка выполняется с помощью метода bind с параметрами: mysql - тип БД, далее набор
        # параметров точно в таком виде, как передается при инициализации коннектора
        self.db.bind('mysql', host=host, database=name, user=user, password=password)

        # В момент вызова метода generate_mapping выполняется сопоставление свойств описанных классов
        # с таблицами и полями таблиц БД
        self.db.generate_mapping()
        # Для вывода в консоль
        sql_debug(True)


    # Метод преобразования объектов типа ORMGroup в модельные объекты
    def convert_groups_to_model(self, groups):
        # Вспомогательная функция, конвертирующая одну отдельно взятую группу
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    # Функции, которые получают списки объектов
    # Каждый блок кода, в котором происходит взаимодействие с БД, должен быть особым образом помечен -
    # необходимо указать, что это блок кода должен выполняться в рамках сесси (при этом сессия открывается
    # и закрывается автоматически)
    # 2 способа отметки
    # Способ 1 - через фикстуру, если надо отметить всю функцию
    @db_session
    def get_group_list(self):
        # Возвращает объекты типа ORMGroup, которые надо преобразовать в модельные объекты
        #return list(select(g for g in ORMFixture.ORMGroup))
        # Преобразование объектов типа ORMGroup выполняется с помощью функции convert_groups_to_model
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))


    # # Способ 2 - через конструкцию with, в которой указывается блок кода, который должен выполняться в
    # рамках сессии
    # def get_group_list(self):
    #     with db_session:
    #         return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
