# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first", middlename="middle", lastname="last", nickname="nick",
                               title="title", company="comp", address="address", home_phone="123-456",
                               mobile_phone="+71234567890", work_phone="789-000", email="edc@ya.ru",
                               email2="edc@mail.ru", email3="edc@gmail.com", homepage="edc\\rfv.ru",
                               bday="1", bmonth="January", byear="2000", aday="2", amonth="February",
                               ayear="2020", new_group="[none]"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="",
                               mobile_phone="", work_phone="", email="",
                               email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-",
                               ayear="", new_group="[none]"))
    app.session.logout()
