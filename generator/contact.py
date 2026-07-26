#------------------------------------------------------------------------------
# qa:
# description: Методы генерации данных для объекта Контакт с сохранением в файл
#------------------------------------------------------------------------------

import random
import string

import os.path
import jsonpickle # добавлен в рамках дз 18

import getopt # для чтения опций командной строки (урок 6-10, дз 18)
import sys # для получения доступа к опциям из предыдущего импорта (урок 6-10, дз 18)

from model.contact import Contact



# Чтение опций из командной строки (урок 6-10. дз 18)
try:
    # Используем две опции: n - задает количество генерируемых данных, f - задает файл, в который
    # данные должны записываться; а ["number of contacts", "file"] - это подсказки (урок 6-10)
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


# Определены дефолтные значения опций (урок 6-10, дз 18)
n = 2
f = "data/contacts.json"

# на основании информации из официальной документации (урок 6-10)
for o, a in opts:
    if o == "-n":
        # если значение опции == -n, значит в ней задается количество групп a в виде целого числа
        n = int(a)
    # если значение опции == -f, значит в опции задается файл в виде строки
    elif o == "-f":
        f = a



# Методы генерации тестовых данных скопированы из файла test_add_contact.py (дз 18)


# Добавлен  вспомогательный метод для генерации случайных тестовых данных (дз 15)
def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for  i in range(random.randrange(maxlen))])


# Добавлен вспомогательный метод для случайного выбора даты (дз 15)
def random_valid_date():
    day = ""
    days_list = ["", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    month_list = ["-", "January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]

    year = random.choice([""] + [str(y) for y in range (1900, 2027)])
    month = random.choice(month_list)

    if month == "-":
        day = random.choice(["", "-"])
        year = ""
    elif month in ["January", "March", "May", "July", "August", "October", "December"]:
        day = random.choice(days_list[2:])
    elif month in ["April", "June", "September", "November"]:
        day = random.choice(days_list[2:32])
    elif month in ["February"]:
        if year == "":
            day = random.choice(days_list[2:31])
        else:
            int_year = int(year)
            if ((int_year % 4) == 0 and int_year % 100 != 0) or ((int_year % 400) == 0):
                day = random.choice(days_list[2:31])
            else:
                day = random.choice(days_list[2:30])

    return day, month, year



# def random_valid_date():
#     month = "-"
#     year = random.choice([""] + [str(y) for y in range (1900, 2027)])
#     month_with_31 = ["January", "March", "May", "July", "August", "October", "December"]
#     month_with_30 = ["April", "June", "September", "November"]
#     month_with_28_or_29 = ["February"]
#     days_list = ("", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
#                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
#                  "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
#     day = random.choice(days_list)
#
#     if day == "" or day == "-":
#         month = "-"
#         year = ""
#         return day, month, year
#
#     day_num = int(day)
#
#     if day == 31:
#         month = random.choice(month_with_31)
#         return day, month, year
#
#     feb_days = 29
#
#     if year != "":
#         if not (((int(year) % 4) == 0 and int(year) % 100 != 0) or ((int(year) % 400) == 0)):
#             feb_days = 28
#
#     if day_num < 31 and day_num != feb_days:
#         month = random.choice(month_with_30 + month_with_31)
#         return day, month, year
#
#     if day_num == feb_days:
#         month = random.choice(month_with_30 + month_with_31 + month_with_28_or_29)
#         return day, month, year
#
#     return day, month, year



contact_testdata = [Contact(firstname="", middlename="", lastname="", address="", home_phone="",
                    mobile_phone="", work_phone="", email="", email2="", email3="")] + [
    (lambda: (lambda d1, d2: Contact(firstname=random_string("firstname", 20),
            middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20),
            address=random_string("address", 40),
            home_phone=random_string("hp", 17),
            mobile_phone=random_string("mp", 17),
            work_phone=random_string("wp", 17),
            email=random_string("email", 20),
            email2=random_string("email2", 20),
            email3=random_string("email3", 20),
            bday=d1[0], bmonth=d1[1], byear=d1[2],
            aday=d2[0], amonth=d2[1], ayear=d2[2],
            new_group="[none]"
            ))(random_valid_date(), random_valid_date()))() for i in range(n)
]



# Определен файл для сохранения сгенерированных тестовых данных (урок 6-10, дз 18)
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


# Записываем сгенерированные данные в файл (урок 6-10, дз 18)
with open(file, "w") as out:
    # Определяем параметры форматирования, чтобы данные в файле отображались не в одну строку
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(contact_testdata))
