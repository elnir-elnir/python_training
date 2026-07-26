#------------------------------------------------------------------------------
# qa:
# description: Проверка соединения с базой данных MySQL
#------------------------------------------------------------------------------

# # "Официальный" драйвер
# import mysql.connector
# Альтернативный драйвер
import pymysql.cursors

# Устанавливаем соединение с базой данных (урок 7-1)
# # "официальным" драйвером
# connection = mysql.connector.connect(host="127.0.0.1", user="root", password="")
# "альтернативным" драйвером
connection = pymysql.connect(host="127.0.0.1", user="root", password="", db="addressbook")

try:
    # Создаем курсор, т. е. указатель на объект в БД (урок 7-1)
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    # fetchall возвращает всю извлеченную информацию в виде набора строк (примерно в том же в виде, в
    # котором хранится в БД (урок 7-1)
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
