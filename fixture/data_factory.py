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

    def create_several_custom_groups(self):
        group1 = Group(name="test_group1", header="test_header1", footer="test_footer1")
        self.app.group.create(group1)
        group2 = Group(name="test_group2", header="test_header2", footer="test_footer2")
        self.app.group.create(group2)
        return group1, group2

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


    def create_several_contact_with_default_group(self):
        contact1 = Contact(firstname="test_firstname1", middlename="test_middlename1", lastname="test_lastname1",
                          nickname="test_nickname1", title="test_title1", company="test_company1", address="test_address1",
                          home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                          email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                          homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                          amonth="February", ayear="2020", new_group="[none]")
        self.app.contact.create(contact1)
        contact2 = Contact(firstname="test_firstname2", middlename="test_middlename2", lastname="test_lastname2",
                           nickname="test_nickname2", title="test_title2", company="test_company2",
                           address="test_address2",
                           home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                           email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                           homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                           amonth="February", ayear="2020", new_group="[none]")
        self.app.contact.create(contact2)
        return contact1, contact2


    def create_several_contact_with_custom_group(self,group_name):
        contact1 = Contact(firstname="test_firstname1", middlename="test_middlename1", lastname="test_lastname1",
                          nickname="test_nickname1", title="test_title1", company="test_company1", address="test_address1",
                          home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                          email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                          homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                          amonth="February", ayear="2020", new_group=group_name)
        self.app.contact.create(contact1)
        contact2 = Contact(firstname="test_firstname2", middlename="test_middlename2", lastname="test_lastname2",
                           nickname="test_nickname2", title="test_title2", company="test_company2",
                           address="test_address2",
                           home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                           email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                           homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                           amonth="February", ayear="2020", new_group=group_name)
        self.app.contact.create(contact2)
        return contact1, contact2


    def create_contact_with_custom_group(self, group_name):
        contact = Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname",
                          nickname="test_nickname", title="test_title", company="test_company", address="test_address",
                          home_phone="123-456", mobile_phone="+71234567890", work_phone="789-900",
                          email="test@yandex.ru", email2="test@mail.ru", email3="test@gmail.com",
                          homepage="https:\\test.ru", bday="1", bmonth="January", byear="2000", aday="2",
                          amonth="February", ayear="2020", new_group=group_name)
        self.app.contact.create(contact)
        return contact


    # По данному методу и его применению есть вопрос в файле test_include_contact_to_group
    def created_contact_found_by_lastname_and_included_in_modified_custom_group_via_home(self):
        group = self.create_custom_group()
        modified_group = self.full_modified_group(group)
        contact = self.create_contact_with_default_group()
        self.app.contact.open_contact_list_via_home_button()
        self.app.contact.select_contact_by_lastname(contact.lastname)
        self.app.contact.set_group(modified_group)


    def contact_with_modified_names_via_details_from_home_page(self):
        new_firstname = "modified_test_firstname"
        new_lastname = "modified_test_lastname"
        new_middlename = "modified_test_middlename"

        contact = self.create_contact_with_default_group()
        self.app.contact.return_to_home_page_after_contact_creation()
        self.app.contact.go_to_details_page_from_contact_list(contact.lastname)
        self.app.contact.go_to_edit_page_from_details_page()
        self.app.contact.edit_contact_only_names(new_firstname, new_lastname, new_middlename)
        modified_contact = Contact(firstname=new_firstname, middlename=new_middlename, lastname=new_lastname, nickname=contact.nickname, title=contact.title, company=contact.company, address=contact.address, home_phone=contact.home_phone, mobile_phone=contact.mobile_phone,
                 work_phone=contact.work_phone, email=contact.email, email2=contact.email2, email3=contact.email3, homepage=contact.homepage, bday=contact.bday, bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear, new_group=contact.new_group)
        self.app.contact.return_to_home_page_after_contact_edit()
        return modified_contact


    def contact_with_modified_names(self, contact):
        new_firstname = "modified_test_firstname"
        new_lastname = "modified_test_lastname"
        new_middlename = "modified_test_middlename"

        self.app.contact.edit_contact_only_names(new_firstname, new_lastname, new_middlename)
        modified_contact = Contact(firstname=new_firstname, middlename=new_middlename, lastname=new_lastname,
                                   nickname=contact.nickname, title=contact.title, company=contact.company,
                                   address=contact.address, home_phone=contact.home_phone,
                                   mobile_phone=contact.mobile_phone,
                                   work_phone=contact.work_phone, email=contact.email, email2=contact.email2,
                                   email3=contact.email3, homepage=contact.homepage, bday=contact.bday,
                                   bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth,
                                   ayear=contact.ayear, new_group=contact.new_group)
        self.app.contact.return_to_home_page_after_contact_edit()
        return modified_contact


    def contact_with_remodified_names_via_edit_from_birthday_page(self, contact):
        new_firstname = "remodified_test_firstname"
        new_lastname = "remodified_test_lastname"
        new_middlename = "remodified_test_middlename"

        modified_contact = self.contact_with_modified_names(contact)
        self.app.contact.go_to_next_birthdays_page()
        self.app.contact.go_to_edit_page_from_birthday_list(modified_contact.lastname, modified_contact.firstname, modified_contact.middlename)
        self.app.contact.edit_contact_only_names(new_firstname, new_lastname, new_middlename)
        modified_contact = Contact(firstname=new_firstname, middlename=new_middlename, lastname=new_lastname,
                                   nickname=contact.nickname, title=contact.title, company=contact.company,
                                   address=contact.address, home_phone=contact.home_phone,
                                   mobile_phone=contact.mobile_phone,
                                   work_phone=contact.work_phone, email=contact.email, email2=contact.email2,
                                   email3=contact.email3, homepage=contact.homepage, bday=contact.bday,
                                   bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth,
                                   ayear=contact.ayear, new_group=contact.new_group)
        self.app.contact.return_to_home_page_after_contact_edit()
        return modified_contact
