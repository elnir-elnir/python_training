#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from model.contact import Contact



# Methods app.session.login(), app.user.login() and app.session.logout() have been removed from
# all tests because fixture have been optimized (lesson 3-3)

def test_add_contact(app):
    app.contact.create(Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
                               title="title", company="comp", address="address", home_phone="123-456",
                               mobile_phone="+71234567890", work_phone="789-000", email="edc@ya.ru",
                               email2="edc@mail.ru", email3="edc@gmail.com", homepage="edc\\rfv.ru",
                               bday="1", bmonth="January", byear="2000", aday="2", amonth="February",
                               ayear="2020", new_group="[none]"))



def test_add_new_contact_when_contact_created_via_add_next_from_confirm_page(app):
    app.data.create_contact_with_default_group()
    app.contact.go_to_next_contact_creation()
    app.data.create_contact_with_default_group()
    app.contact.open_contact_list_via_addressbook_link()



def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="",
                               mobile_phone="", work_phone="", email="",
                               email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-",
                               ayear="", new_group="[none]"))
