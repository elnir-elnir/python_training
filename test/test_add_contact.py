#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
import random
import string

import pytest

from model.contact import Contact



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
            ))(random_valid_date(), random_valid_date()))() for i in range(1)
]




# Methods app.session.login(), app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

# Добавлена парметризация теста (дз 15)
# Здесь contact_testdata - исчтоник тестовых данных, group - параметр для передачи тестовых данных
# в тестовую функцию, ids - параметр для формирования списка с текстовым представлением тестовых
# данных для формирования отчета о выполнении теста (чтобы в отчете было видно, с какими именно
# тестовыми данными выполнялся тест)
@pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
def test_add_contact(app, contact):
    # Получаем старый список контактов из приложения (дз 11)
    old_contacts = app.contact.get_contact_list()
    print("old_contacts: ", old_contacts)

    # Убираем объявление локальной переменной в связи с параметризацией теста (урок 5-7, дз 15)
    # # Для последующего сравнения списков модифицируем тест - объявляем локальную
    # # переменную contact и передаем ее в качестве параметра в метод создания контакта (дз 11)
    # contact = Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
    #         title="title", company="comp", address="address", home_phone="123-456",
    #         mobile_phone="+71234567890", work_phone="789-000", email="edc@ya.ru",
    #         email2="edc@mail.ru", email3="edc@gmail.com", homepage="edc\\rfv.ru",
    #         bday="1", bmonth="January", byear="2000", aday="2", amonth="February",
    #         ayear="2020", new_group="[none]")
    #app.contact.create(contact)
    app.contact.create_for_default_values(contact)

    # Проверяем, что новый список на единицу длинее старого (дз 11)
    assert len(old_contacts) + 1 == app.contact.count_of_contacts()

    # Получаем новый список контактов (дз 11)
    new_contacts = app.contact.get_contact_list()
    print("new_contacts: ", new_contacts)

    # # Проверяем, что новый список на единицу длинее старого (дз 11)
    # assert len(old_contacts) + 1 == len(new_contacts)

    # В список контактов, полученный из приложения, добавляем новый контакт (дз 11)
    old_contacts.append(contact)
    print("new_old_contacts: ", old_contacts)

    # Сравниваем отсортированные списки: ожидаемый и фактический
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print("sorted_old_contacts: ", sorted(old_contacts, key=Contact.id_or_max))
    print("sorted_new_contacts: ", sorted(new_contacts, key=Contact.id_or_max))



def test_add_new_contact_when_contact_created_via_add_next_from_confirm_page(app):
    app.data.create_contact_with_default_group()
    app.contact.go_to_next_contact_creation()
    app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_addressbook_link()


# # Тест модифицирован в рамках дз 11
# Тест закоментирован в связи с добавлением паоаметризации тестов - в первом тесте также создается
# объект с пустыми полями (дз 15)
# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="",
#                                title="", company="", address="", home_phone="",
#                                mobile_phone="", work_phone="", email="",
#                                email2="", email3="", homepage="",
#                                bday="", bmonth="-", byear="", aday="", amonth="-",
#                                ayear="", new_group="[none]")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
