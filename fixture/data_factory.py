from model.group import Group
from model.contact import Contact

class DataFactory:

    # Class for creating test data. Uses existing helper classes for real object creation through UI

    def __init__(self, app):
        self.app = app


    # For group

    def create_custom_group(self):
        group = Group(name="test_group", header="test_header", footer="test_footer")
        self.app.group.create(group)
        return group


    # For contact

    def create_contact_with_default_group(self):
        contact = Contact(firstname="test_firstname", middlename = "test_middlename", lastname="test_lastname", nickname = "test_nickname", title = "test_title", company = "test_company", address="test_address", home_phone = "123-456", mobile_phone = "+71234567890", work_phone = "789-900", email = "test@yandex.ru", email2 = "test@mail.ru", email3 = "test@gmail.com", homepage = "https:\\test.ru", bday = "1", bmonth = "January", byear = "2000", aday = "2", amonth = "February", ayear = "2020", new_group = "[none]")
        self.app.contact.create(contact)
        return contact

    def create_contact_with_custom_group(self, group_name = "test_new_group"):
        contact = Contact(firstname="test_firstname", middlename = "test_middlename", lastname="test_lastname", nickname = "test_nickname", title = "test_title", company = "test_company", address="test_address", home_phone = "123-456", mobile_phone = "+71234567890", work_phone = "789-900", email = "test@yandex.ru", email2 = "test@mail.ru", email3 = "test@gmail.com", homepage = "https:\\test.ru", bday = "1", bmonth = "January", byear = "2000", aday = "2", amonth = "February", ayear = "2020", new_group = group_name)
        self.app.contact.create(contact)
        return contact