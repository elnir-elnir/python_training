#------------------------------------------------------------------------------
# qa:
# description: Проверка соединения с базой данных MySQL
#------------------------------------------------------------------------------

# # "Официальный" драйвер (https://pypi.org/project/mysql-connector-python/,
# pip install mysql-connector-python)
# import mysql.connector
# Альтернативный драйвер (https://pypi.org/project/PyMySQL/, pip install PyMySQL )
import pymysql.cursors

from fixture.db import DbFixture

from fixture.orm import ORMFixture



## Проверка соединения с базой данных MySQL (урок 7-1)

# Устанавливаем соединение с базой данных (урок 7-1)
# # "официальным" драйвером
# connection = mysql.connector.connect(host="127.0.0.1", user="root", password="")
# "альтернативным" драйвером
# connection = pymysql.connect(host="127.0.0.1", user="root", password="", db="addressbook")
#
# try:
#     # Создаем курсор, т. е. указатель на объект в БД (урок 7-1)
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     # fetchall возвращает всю извлеченную информацию в виде набора строк (примерно в том же в виде, в
#     # котором хранится в БД (урок 7-1)
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()



## Получение информации из базы данных и вывод ее в консоль (урок 7-6)

#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# # Получаем список групп
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()


# # Получаем список контактов
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()


# Получаем список групп c помощью ORM

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
# ORM автоматически закрывает соединение с БД, поэтому блок finally не нужен - ставим заглушку
finally:
    pass
