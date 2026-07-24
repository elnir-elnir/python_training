#------------------------------------------------------------------------------
# qa:
# description: проверка таблицы с контактами на главной странице
#------------------------------------------------------------------------------
import re
from random import randrange

from test import test_phones


def test_contact_not_in_group_on_home_page(app):
    # Предусловия
    # Переходим на страницу со списком контактов
    app.contact.open_contact_list_via_home_button()

    # Фильтруем контакты без группы
    app.contact.filter_contacts_by_group("[none]")

    # Если нет контактов без группы — создаём контакт
    if app.contact.count_of_contacts() == 0:
        app.data.create_contact_with_default_group()

    # Получаем список контактов из приложения (дз 11)
    contacts = app.contact.get_contact_list_in_group("[none]")
    # Определен случайным образом индекс проверяемого контакта (дз 13)
    index = randrange(len(contacts))

    # Получаем на главной странице информацию о проверяемом контакте по полученному индексу
    contact_from_home_page = app.contact.get_contact_list_full()[index]

    # Получаем информацию об этом контакте со странцы редактирования контакта
    contact_from_edit_page = app.contact.get_contact_info_with_address_and_email_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == test_phones.merge_phones_like_on_home_page(contact_from_edit_page)


# Добавлен метод получения строки без символов "пробел" с применением регулярных выражений
# На первом месте указывается, что надо заменить, на втором - на что надо заменить, на третьем -
# где надо заменить
def clear(s):
    return re.sub(" ", "", s)


# Добавляем метод склеивания строк (дз 14)
# Склеиваем при помощи перевода строки, используя функцию join, которой в качечтве параметров
# передаем список адресов электронной почты
# Исключаем элементы = None с помощью функции filter к списку (до применения функции map)
# Для очистки адресов электронной почты от дополнительных символов применяем map, чтобы применить
# метод clear ко всем элементам списка сразу
# А затем к результату функции map применяем filter того, чтобы не учитывать при склейке
# пустые адреса электронной почты
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

