#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        wd.find_element(By.XPATH, f"//option[@value='{contact.bday}']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.XPATH, f"//option[@value='{contact.bmonth}']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        # code line from recorder has been fixed to its one
        #wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[4]").click()
        wd.find_element(By.CSS_SELECTOR, f'select[name="aday"] > option[value="{contact.aday}"]').click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        # code line from recorder has been fixed to its one
        #wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[3]").click()
        wd.find_element(By.CSS_SELECTOR, f'select[name="amonth"] > option[value="{contact.amonth}"]').click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "new_group").click()
        Select(wd.find_element(By.NAME, "new_group")).select_by_visible_text(contact.new_group)
        #wd.find_element(By.CSS_SELECTOR, f'select[name=new_group] > option[value="{contact.new_group}"]').click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[19]").click()


    def open_contact_list_via_home_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "/html/body/div/div[3]/ul/li[1]/a").click()


    def open_contact_list_via_addressbook_link(self):
        wd = self.app.wd
        wd.find_element(By.ID, "logo").click()


    def select_contact_by_lastname(self, lastname):
        wd = self.app.wd
        # creating xpath for contact string in contact list:
        row_xpath = f"//tr[@name='entry' and td[2][normalize-space()='{lastname}']]"
        #wd.execute_script("arguments[0].scrollIntoView({block: 'center'}):", row_xpath)
        # find contact string
        row = wd.find_element(By.XPATH, row_xpath)
        # find checkbox inside contact string
        row.find_element(By.XPATH, ".//input[@type='checkbox']").click()


    def select_all_contacts(self):
        wd = self.app.wd
        row_xpath = f"//input[@id=\"MassCB\"]"
        wd.find_element(By.XPATH, row_xpath).click()


    def set_group(self, group):
        wd = self.app.wd
        wd.find_element(By.NAME, "to_group").click()
        Select(wd.find_element(By.NAME, "to_group")).select_by_visible_text(group.name)
        wd.find_element(By.NAME, "add").click()


    def exclude_contact_from_group(self, group_name):
        wd = self.app.wd
        xpath = f"//input[@type='submit' and @name='remove' and @value='Remove from \"{group_name}\"']"
        wd.find_element(By.XPATH, xpath).click()


    def filter_contacts_by_group(self, group_name):
        wd = self.app.wd
        wd.find_element(By.NAME, "group").click()
        Select(wd.find_element(By.NAME, "group")).select_by_visible_text(group_name)


    def reset_contacts_filter(self, group_name="[all]"):
        wd = self.app.wd
        wd.find_element(By.NAME, "group").click()
        Select(wd.find_element(By.NAME, "group")).select_by_visible_text(group_name)


    def go_to_details_page_from_contact_list(self, lastname):
        wd = self.app.wd
        row_xpath = f"//tr[@name='entry' and td[2][normalize-space()='{lastname}']]//a[img/@title='Details']"
        details_link = wd.find_element(By.XPATH, row_xpath)
        details_link.click()


    def go_to_edit_page_from_details_page(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "modifiy").click()


    def go_to_edit_page_from_contact_list(self, lastname):
        wd = self.app.wd
        row_xpath = f"//tr[@name='entry' and td[2][normalize-space()='{lastname}']]//a[img/@title='Edit']"
        edit_link = wd.find_element(By.XPATH, row_xpath)
        edit_link.click()


    def go_to_next_birthdays_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "next birthdays").click()


    def go_to_edit_page_from_birthday_list(self, lastname, firstname, middlename):
        wd = self.app.wd
        row_xpath = f"//tr[contains(td[2][normalize-space()], '{lastname}') and contains(td[2][normalize-space()], '{middlename}') and td[3][normalize-space()]='{firstname}']//a[img/@title='Edit']"
        details_link = wd.find_element(By.XPATH, row_xpath)
        details_link.click()


    def go_to_details_page_from_birthday_list(self, lastname, firstname, middlename):
        wd = self.app.wd
        row_xpath = f"//tr[contains(td[2][normalize-space()], '{lastname}') and contains(td[2][normalize-space()], '{middlename}') and td[3][normalize-space()]='{firstname}']//a[img/@title='Details']"
        details_link = wd.find_element(By.XPATH, row_xpath)
        details_link.click()


    def return_to_home_page_after_contact_edit(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()


    def return_to_home_page_after_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()


    def return_to_home_page_after_contact_deletion(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()


    def edit_contact_only_names(self, new_firstname, new_lastname, new_middlename):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(new_firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(new_middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(new_lastname)
        wd.find_element(By.NAME, "update").click()


    def delete_contact_from_edit_page(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()


    def delete_contact_from_contact_list(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()


    def delete_modal_window_closed(self):
        wd = self.app.wd
        wd.switch_to.alert.accept()
