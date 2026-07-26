#------------------------------------------------------------------------------
# qa:
# description: Класс для реализации фикстуры для взаимодействия с БД (урок 7-2)
#------------------------------------------------------------------------------

import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password)


    # Метод зачистки (урок 7-2)
    def destroy(self):
        self.connection.close()
