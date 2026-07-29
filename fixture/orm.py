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

from pymysql.converters import decoders

from model.contact import Contact
from model.group import Group


class ORMFixture:

    db = Database()

    # Описание структуры таблиц

    # Описываем структуру таблицы group_list (урок 7-7)
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
        # Добавлен атрибут специального типа для описания связей между объектами (урок 7-8)
        # Связь осуществляется при помощи таблицы address_in_groups, поиск осуществляется по
        # указанному столбцу column, также указываем парное свойство reverse
        # Свойство lazy из PonyORM управляет тем, когда именно происходит загрузка связанных данных
        # из базы данных. Т. е. отвечает за рекурсивность запросов. При = True - запрещена рекурсивность.
        # Данные из связанной таблицы не загружаются в момент получения основного объекта.
        # По умолчанию = False. Данные из связанной таблицы загружаются сразу же, одним запросом (через
        # JOIN или дополнительные SELECT), в момент получения основного объекта
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id",
                       reverse="groups", lazy=True)


    # Описываем структуру таблицы addressbook (урок 7-7)
    class ORMContact(db.Entity):
        # Указываем название таблицы БД
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        middlename = Optional(str, column="middlename")
        lastname = Optional(str, column="lastname")
        bday = Optional(str, column="bday")
        bmonth = Optional(str, column="bmonth")
        deprecated = Optional(datetime, column="deprecated")
        # Добавлен атрибут специального типа для описания связей между объектами (урок 7-8)
        # Связь осуществляется при помощи таблицы address_in_groups, поиск осуществляется по
        # указанному столбцу column
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id",
                     reverse="contacts", lazy=True)


    # Описываем привязку к базе данных. В качестве параметров принимается такой же набор, как у db.fixture
    # (урок 7-7)
    def __init__(self, host, name, user, password):
        # Привязка выполняется с помощью метода bind с параметрами: mysql - тип БД, далее набор
        # параметров точно в таком виде, как передается при инициализации коннектора и параметр
        # conv для преобразования невалидной даты, т.к. в поле deprecated для актуальных контактов
        # отображаются значения 0000-00-00 00-00-00, а в методе конвертации мы это преобразовываем в None
        # В рамках дз 20 выполнена замена параметра conv=decoders на charset='utf8', т. к.
        # тест test_delete_some_contact_not_in_group_via_edit_page выполнился с ошибками:
        # Ошибка KeyError: <class 'str'> и TypeError: no default type converter defined
        #self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.bind('mysql', host=host, database=name, user=user, password=password,
                     charset='utf8')

        # В момент вызова метода generate_mapping выполняется сопоставление свойств описанных классов
        # с таблицами и полями таблиц БД
        self.db.generate_mapping()
        # Для вывода в консоль
        sql_debug(True)


    # Методы преобразования

    # Метод преобразования объектов типа ORMGroup в модельные объекты (урок 7-7)
    def convert_groups_to_model(self, groups):
        # Вспомогательная функция, конвертирующая одну отдельно взятую группу
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    # Метод преобразования объектов типа ORMContact в модельные объекты (урок 7-7)
    def convert_contacts_to_model(self, contacts):
        # Вспомогательная функция, конвертирующая одну отдельно взятую группу
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)

        return list(map(convert, contacts))



    # Функции, которые получают списки объектов

    ## Списки групп

    # Получение списка групп (урок 7-7)
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


    # Получение списка групп, содержащих более 1 контакта (дз 20)
    @db_session
    def get_group_list_with_several_contacts(self):
        # Получаем список всех групп
        all_groups = list(select(g for g in ORMFixture.ORMGroup))

        # Объявляем переменную для сохранения списка групп с несколькими контактами
        result = []

        # Для каждой группы из списка all_groups проверяем выполнение условий
        for group in all_groups:
            # Находим все контакты, у которых в таблице связей address_in_groups в поле group_id
            # указан id текущей группы (по которой выполняется цикл) и в поле deprecated отображается
            # 0000-00-00 00:00:00
            contacts_in_group = list(
                select(c for c in ORMFixture.ORMContact
                       if c.deprecated is None and group in c.groups)
            )
            # Определяем количество контактов в текущей группе и при выполнении условия > 1 добавляем
            # текущую группу в итоговый список result
            if len(contacts_in_group) > 1:
                result.append(group)
        return self.convert_groups_to_model(result)


    # Получение списка групп, несодержащих контакты (дз 20)
    @db_session
    def get_group_list_without_contacts(self):
        # Получаем список всех актуальных контактов
        actual_contacts = select(c for c in ORMFixture.ORMContact if c.deprecated is None)

        # Получаем id групп, в которые включены актуальные контакты
        group_id_with_contacts = set()
        for contact in actual_contacts:
            for group in contact.groups:
                group_id_with_contacts.add(group.id)

        # Получаем список всех групп
        all_groups = list(select(g for g in ORMFixture.ORMGroup))

        # Получаем список групп, в которые не включены контакты (групп нет в group_id_with_contacts)
        result = [g for g in all_groups if g.id not in group_id_with_contacts]

        return self.convert_groups_to_model(result)


    # Получение списка групп для контакта по id (дз 20)
    @db_session
    def get_groups_for_contact(self, contact):
        #orm_contact = list(select(c for c in ORMFixture.ORMContact if c.id == int(contact.id)))[0]
        orm_contact = ORMFixture.ORMContact.get(id=int(contact.id))
        return self.convert_groups_to_model(orm_contact.groups)


    # Получение группы для контакта, включенного только в одну группу, по id контакта (дз 20)
    @db_session
    def get_group_for_contact_by_index(self, contact, index):
        contact_groups = self.get_groups_for_contact(contact)

        if contact_groups:
            group = contact_groups[index]
        else:
            group = None
        return group


    ## Списки контактов

    # Получение списка контактов (урок 7-7)
    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(
            c for c in ORMFixture.ORMContact if c.deprecated is None))


    # Метод получения списка контактов, включенных в группу, по id (урок 7-8)
    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == str(group.id)))[0]
        return self.convert_contacts_to_model(orm_group.contacts)


    # Метод получения списка контактов, которые не входят в заданную группу, по id (урок 7-8)
    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == str(group.id)))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))


    # Получение списка контактов, которые не входят ни в одну группу (дз 20)
    @db_session
    def get_contacts_not_in_any_group(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) == 0))


    # Получение списка контактов, включенных только в одну групп (дз 20)
    @db_session
    def get_contacts_included_in_one_group(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) == 1))


    # Получение списка контактов, которые входят в несколько групп (дз 20)
    @db_session
    def get_contacts_in_several_group(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) > 1))



    # Получение данных контакта

    # Добавляем метод получения дня рождения контакта (bday) - дз 20
    @db_session
    def get_bday_from_db(self, contact):
        orm_contact = ORMFixture.ORMContact.get(id=int(contact.id))
        return orm_contact.bday

    # Добавляем метод получения месяца рождения контакта (bmonth) - дз 20
    @db_session
    def get_bmonth_from_db(self, contact):
        orm_contact = ORMFixture.ORMContact.get(id=int(contact.id))
        return orm_contact.bmonth


    # Добавлен метод проверки наличия у контакта даты рождения - дз 20
    @db_session
    def has_birthday(self, contact):
        bday = self.get_bday_from_db(contact)
        bmonth = self.get_bmonth_from_db(contact)

        day_valid = False
        month_valid = False

        if bday in range(1, 32):
            day_valid = True

        if bmonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                       'August', 'September', 'October', 'November', 'December']:
            month_valid = True

        return day_valid and month_valid
