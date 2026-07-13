#------------------------------------------------------------------------------
# developer:
# description:
#------------------------------------------------------------------------------
import re

# Добавлены тесты (урок 5-5) и модифицированы (урок 5-6)
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    # Модифицировано в обратную проверку - проверка путем склеивания (урок 5-6)
    #assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    #assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    #assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)



def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone



# Добавлен метод получения строки без символов "пробел", "минус", скобок с применением регулярных выражений
# На первом месте указывается, что надо заменить, на втором - на что надо заменить, на третьем -
# где надо заменить
def clear(s):
    return re.sub("[() -]", "", s)



# Добавляем метод склеивания строк (урок 5-6)
# Склеиваем при помощи перевода строки, используя функцию join, которой в качечтве параметров
# передаем список телефонов
# Исключаем элементы = None с помощью функции filter к списку (до применения функции map)
# Для очистки телефонов от дополнительных символов применяем map, чтобы применить метод clear
# ко всем элементам списка сразу
# А затем к результату функции map применяем filter того, чтобы не учитывать при склейке
# пустые телефоны
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))
