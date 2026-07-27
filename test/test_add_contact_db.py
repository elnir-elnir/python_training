#------------------------------------------------------------------------------
# qa:
# description: Вместо файла test_add_contact_рц_19.py в рамках модуля 7, дз 20
#------------------------------------------------------------------------------

# Пояснения по тесту см. в файле test_add_contact.py

from model.contact import Contact



# Загрузка списка контактов непосредственно из БД (дз 20)
# Данные загружаются из файла data\contacts.json, который находится в пакете data (урок 6-12, дз 19)
def test_add_contact(app, db, json_contacts):
    contact = json_contacts

    old_contacts = db.get_contact_list()
    print("old_contacts: ", old_contacts)

    app.contact.create_for_default_values(contact)

    # Проверка удаляется в рамках дз 20
    #assert len(old_contacts) + 1 == app.contact.count_of_contacts()

    new_contacts = db.get_contact_list()
    print("new_contacts: ", new_contacts)

    old_contacts.append(contact)
    print("new_old_contacts: ", old_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print("sorted_old_contacts: ", sorted(old_contacts, key=Contact.id_or_max))
    print("sorted_new_contacts: ", sorted(new_contacts, key=Contact.id_or_max))
