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


    def open_contact_list_using_home_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "/html/body/div/div[3]/ul/li[1]/a").click()


    def open_contact_list_using_addressbook_link(self):
        wd = self.app.wd
        wd.find_element(By.ID, "logo").click()


    def select_contact_by_lastname(self, lastname):
        wd = self.app.wd
        row_xpath = f"//tr[@name='entry' and td[2][normalize-space()='{lastname}']]"
        #wd.execute_script("arguments[0].scrollIntoView({block: 'center'}):", row_xpath)
        row = wd.find_element(By.XPATH, row_xpath)
        row.find_element(By.XPATH, ".//input[@type='checkbox']").click()


    def set_group(self, group):
        wd = self.app.wd
        wd.find_element(By.NAME, "to_group").click()
        Select(wd.find_element(By.NAME, "to_group")).select_by_visible_text(group.name)
        wd.find_element(By.NAME, "add").click()
