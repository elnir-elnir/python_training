#------------------------------------------------------------------------------
# qa:
# description: Класс для взаимодействия с БД
#------------------------------------------------------------------------------

import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit=True - если этот параметр указан, то кеш после каждого запроса в БД сбрасывается, а
        # если не указан, то данные кешируются
        # Параметр добавлен для получения правильного списка при выполнении тестов с действиями
        # непосредственно в БД (урок 7-4)
        # self.connection = pymysql.connect(host=host, db=name, user=user, password=password)
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password, autocommit=True)


    # Метод получения списка групп из БД (урок 7-3)
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    # Метод получения списка контактов из БД (урок 7-6)
    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            # В курсе запрос составлен исходя из того, что контакты в БД не удаляются, а отмечаются deprecated с
            # ненулевыми датой и временем, в для актуальных контактов в поле deprecated указывается
            # значение 0000-00-00 00:00:00, поэтому в курсе запрос такой (урок 7-6)
            #cursor.execute("select id, firstname, lastname from addressbook WHERE deprecated='0000-00-00 00:00:00'")
            # Но у меня при таком запросе количество = 0. Однако при следующем запросе полученное количество
            # соответствует количеству в UI. В phpMyAdmin не получается зайти
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list


    # Метод зачистки (урок 7-2)
    def destroy(self):
        self.connection.close()
