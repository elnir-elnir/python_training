# ------------------------------------------------------------------------------
# qa:
# description:
# ------------------------------------------------------------------------------
from sys import maxsize


class Contact:
    # Добавляем в параметры идентификатор (дз 11)
    # И модифицируем конструктор - None is special value/ None means that field not initialized (lesson 3-2)
    # Добавляем атрибут all__phones_from_home_page, чтобы реализовать метод обратной проверки - путем
    # склеивания строк (урок 5-6)
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home_phone=None, mobile_phone=None,
                 work_phone=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, new_group=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id


    # Для получения информации об объекте реализуем функцию, которая определяет вывод объекта в консоль
    # урок 4-8, дз 11
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    # Определяем функцию для логического сравнения, т. е. по смыслу (по имени, фамилии, идентификаторам).
    # Дорабатываем метод, чтобы он учитывал неопределенный идентификатор - идентификаторы нужно
    # сравнивать тольок, если они определены, т. е. != None (урок 4-9), дз 11
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname


    # Добавляем сортировку списков по идентификаторам (урок 4-9), дз 11
    # Но перед этим пишем метод, который будет вычислять по контакту ключ, используемый для сравнения
    # Новый контакт всегда имеет самое большое значения идентификатора, поэтому для контакта,
    # добавленного в тесте в старый список, можно назначить в качестве идентификатора какое-то
    # большое число (урок 4-9), дз 11
    def id_or_max(cntct):
        if cntct.id:
            # возвращаемый идентификатор преобразуем из строки в число (урок 4-9)
            return int(cntct.id)
        else:
            # В языке Python нет максимального целого числа, поэтому рекомендуется использовать
            # специальную константу maxsize (урок 4-9)
            return maxsize
