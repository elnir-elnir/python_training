#------------------------------------------------------------------------------
# qa:
# description: проверка таблицы с контактами на главной странице с загрузкой
# списков из БД (дз 21)
#------------------------------------------------------------------------------
import random

from model.contact import Contact
from test import test_phones
from test.test_contact_list import merge_emails_like_on_home_page


def test_contact_list_on_home_page(app, orm, check_ui):
    # Предусловия
    # Получаем список контактов из базы данных
    contacts_from_db = orm.get_contact_list() # параметр contact2
    # Проверяем наличие контактов
    if len(contacts_from_db) == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
        contacts_from_db = orm.get_contact_list()

    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_addressbook_link()

    # Получаем список контактов на главной странице
    contact_from_home_page = app.contact.get_contact_list_full() # параметр contact1

    # Тест
    # Сравниваем количество контактов в приложении и БД
    assert len(contact_from_home_page) == len(contacts_from_db)

    # Сравниваем контакты
    for i in range(len(contacts_from_db)):
        contact1 = contact_from_home_page[i]
        contact2 = contacts_from_db[i]
        print("contact_from_home_page: ", contact1)
        print("contact_from_db: ", contact2)
        assert_contacts(contact1, contact2)








# Метод сравнения полей контактов, где contact1 - контакт полученый из приложения, contact2 -
# контакт, полученный из базы данных (дз 21)
def assert_contacts(contact1, contact2):
    assert contact1.firstname == contact2.firstname
    assert contact1.lastname == contact2.lastname
    #assert contact1.address == contact2.address
    # assert (contact1.all_emails_from_home_page ==
    #         merge_emails_like_on_home_page(contact2))
    # assert (contact1.all_phones_from_home_page ==
    #         test_phones.merge_phones_like_on_home_page(contact2))

