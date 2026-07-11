#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from model.contact import Contact



# Methods app.session.login(), app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_add_contact(app):
    # Получаем старый список контактов из приложения (дз 11)
    old_contacts = app.contact.get_contact_list()

    # Для последующего сравнения списков модифицируем тест - объявляем локальную
    # переменную contact и передаем ее в качестве параметра в метод создания контакта (дз 11)
    contact = Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
            title="title", company="comp", address="address", home_phone="123-456",
            mobile_phone="+71234567890", work_phone="789-000", email="edc@ya.ru",
            email2="edc@mail.ru", email3="edc@gmail.com", homepage="edc\\rfv.ru",
            bday="1", bmonth="January", byear="2000", aday="2", amonth="February",
            ayear="2020", new_group="[none]")
    app.contact.create(contact)

    # Получаем новый список контактов (дз 11)
    new_contacts = app.contact.get_contact_list()

    # Проверяем, что новый список на единицу длинее старого (дз 11)
    assert len(old_contacts) + 1 == len(new_contacts)

    # В список контактов, полученный из приложения, добавляем новый контакт (дз 11)
    old_contacts.append(contact)

    # Сравниваем отсортированные списки: ожидаемый и фактический
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print("old_contacts: ", old_contacts)
    print("new_contacts: ", new_contacts)



def test_add_new_contact_when_contact_created_via_add_next_from_confirm_page(app):
    app.data.create_contact_with_default_group()
    app.contact.go_to_next_contact_creation()
    app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_addressbook_link()


# Тест модифицирован в рамках дз 11
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="",
                               mobile_phone="", work_phone="", email="",
                               email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-",
                               ayear="", new_group="[none]")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
