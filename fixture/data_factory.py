# ------------------------------------------------------------------------------
# qa:
# description:
# ------------------------------------------------------------------------------

from model.group import Group
from model.contact import Contact
from model.user import User



class DataFactory:

    # Class for creating test data. Uses existing helper classes for real object creation through UI

    def __init__(self, app):
        self.app = app



    # For user

    def create_user(self):
        return User(login="admin", password="secret")




    # For group

    def create_custom_group(self):
        group = Group(name="test_group", header="test_header", footer="test_footer")
        self.app.group.create(group)
        return group


    def full_modified_group(self, group):
        group_name = group.name
        new_group_name = "modified_test_group"
        new_group_header = "modified_test_header"
        new_group_footer = "modified_test_footer"
        self.app.group.full_modify_group_by_name(group_name, new_group_name, new_group_header, new_group_footer)
        modified_group = Group(name=new_group_name, header=new_group_header, footer=new_group_footer)
        return modified_group


    def full_remodified_group(self, group):
        modified_group = self.full_modified_group(group)
        group_name = modified_group.name
        new_group_name = "remodified_test_group"
        new_group_header = "remodified_test_header"
        new_group_footer = "remodified_test_footer"
        self.app.group.full_modify_group_by_name(group_name, new_group_name, new_group_header, new_group_footer)
        remodified_group = Group(name=new_group_name, header=new_group_header, footer=new_group_footer)
        return remodified_group



    # For contact

    def create_contact_with_default_group(self):
        contact = Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname",
                          nickname="test_nickname", title="test_title", company="test_company", address="test_address",
                          home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                          email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                          homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                          amonth="February", ayear="2020", new_group="[none]")
        self.app.contact.create(contact)
        return contact


    def create_contact_with_custom_group(self, group_name):
        contact = Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname",
                          nickname="test_nickname", title="test_title", company="test_company", address="test_address",
                          home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                          email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                          homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                          amonth="February", ayear="2020", new_group=group_name)
        self.app.contact.create(contact)
        return contact
