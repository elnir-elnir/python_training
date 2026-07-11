#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "new_group").click()
        Select(wd.find_element(By.NAME, "new_group")).select_by_visible_text(contact.new_group)
        #wd.find_element(By.CSS_SELECTOR, f'select[name=new_group] > option[value="{contact.new_group}"]').click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[19]").click()


    def fill_contact_form(self, contact):
        wd = self.app.wd
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
        #wd.find_element(By.CSS_SELECTOR, f'select[name="amonth"] > option[value="{contact.amonth}"]').click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)



    def go_to_next_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add next").click()


    def open_contact_list_via_home_button(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "/html/body/div/div[3]/ul/li[1]/a").click()


    # Добавлена проверка открытой страницы (урок 3-6)
    def open_contact_list_via_addressbook_link(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "delete")) > 0 and len(wd.find_elements(By.NAME, "remove")) == 0):
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


    # add new method (lesson 3-5)
    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def set_group(self, group_name):
        wd = self.app.wd
        wd.find_element(By.NAME, "to_group").click()
        Select(wd.find_element(By.NAME, "to_group")).select_by_visible_text(group_name)
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


    def go_to_details_page_of_first_contact_from_contact_list(self):
        wd = self.app.wd
        row_xpath = f"(//tr[@name='entry' and not(contains(@style, 'display: none'))]//a[img/@title='Details'])[1]"
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


    # Добавлен метод для перехода в редактирование первого в списке контакта (урок 3-5)
    def go_to_edit_page_of_first_contact_from_contact_list(self):
        wd = self.app.wd
        #wd.find_element(By.XPATH, "//tr[@name='entry'][1]//img[@title='Edit']").click()
        wd.find_element(By.XPATH, "(//tr[@name='entry' and not(contains(@style, 'display: none'))]//a[img/@title='Edit'])[1]").click()


    # Добавлен метод для перехода в редактирование первого в списке дней рождений (урок 3-5)
    def go_to_edit_page_of_first_contact_from_birthdays_page(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "// img[ @ alt = 'Edit']").click()


    def go_to_next_birthdays_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/birthdays.php")):
            wd.find_element(By.LINK_TEXT, "next birthdays").click()


    def go_to_edit_page_from_birthday_list(self, lastname, firstname, middlename):
        wd = self.app.wd
        row_xpath = f"//tr[contains(td[2][normalize-space()], '{lastname}') and contains(td[2][normalize-space()], '{middlename}') and td[3][normalize-space()]='{firstname}']//a[img/@title='Edit']"
        details_link = wd.find_element(By.XPATH, row_xpath)
        details_link.click()


    def go_to_details_page_from_birthday_list(self, lastname, firstname, middlename):
        wd = self.app.wd
        row_xpath = f"//tr[contains(td[2][normalize-space()], '{lastname}') and contains(td[2][normalize-space()], '{middlename}') and td[3][normalize-space()]='{firstname}']//a[img/@title='Details']"
        if middlename is None:
            row_xpath = f"//tr[contains(td[2][normalize-space()], '{lastname}') and td[3][normalize-space()]='{firstname}']//a[img/@title='Details']"
        details_link = wd.find_element(By.XPATH, row_xpath)
        details_link.click()


    def go_to_details_page_of_first_page_from_birthday_list(self):
        wd = self.app.wd
        row_xpath  = f"(//a[img/@title='Details'])[1]"
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


    def edit_contact(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
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


    # Добавялем метод подсчета количества чек-боксов на странице контактов (определяем количество
    # созданных контактов) - урок 3-5
    def count_of_contacts(self):
        wd = self.app.wd

        # wd.find_elements(By.NAME, "selected[]") - находим на странице все элементы
        # с названием "selected[]"
        # len(wd.find_elements(By.NAME, "selected[]")) - считаем количество найденных элементов
        return len(wd.find_elements(By.NAME, "selected[]"))


    # Добавляем метод получения дня рождения контакта (bday) - урок 3-5
    def get_bday(self):
        wd = self.app.wd
        select = Select(wd.find_element(By.NAME, "bday"))
        bday = select.first_selected_option.get_attribute("value")
        #return select.first_selected_option.get_attribute("value")
        return bday


    # Добавляем метод получения месяца рождения контакта (bmonth) - урок 3-5
    def get_bmonth(self):
        wd = self.app.wd
        select = Select(wd.find_element(By.NAME, "bmonth"))
        return select.first_selected_option.get_attribute("value")


    # Добавлен метод установки даты рождения контакта (урок 3-5)
    def set_birthday(self, bday, bmonth, byear):
        wd = self.app.wd
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(bday)
        wd.find_element(By.XPATH, f"//option[@value='{bday}']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(bmonth)
        wd.find_element(By.XPATH, f"//option[@value='{bmonth}']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(byear)
        wd.find_element(By.NAME, "update").click()


    # Новый метод для получения списка контактов из тестируемого приложения (дз 11)
    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_list_via_addressbook_link()

        # Объявляем список для хранения полученного списка
        contacts = []

        # С помощью Inspect Element (Q) получаем имя, фамилию, которые хранятся в таблице, и
        # идентификаторы, которые хранятся в атрибуте value чек-бокса контакта
        # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
        # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
        # в виде css_selector, т. е. $$("tr[name='entry']"), то мы получим список элементов, которые
        # по этому селектору находятся
        for row in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
            # для получения идентификатора внутри элемента entry находим элемент с именем selected[]
            # (чек-бокс) и у этого чек-бокса получаем значение атрибута value
            cntct_id = row.find_element(By.NAME, "selected[]").get_attribute("value")

            # Получаем фамилию (2-й столбец)
            lastname = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text

            # Получаем имя (3-й столбец)
            firstname = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text

            # Добавляем полученные элементы в список
            contacts.append(Contact(id=cntct_id, firstname=firstname, lastname=lastname))

        # Возвращаем полученный готовый список
        return contacts


    # Новый метод для получения списка контактов в группе из тестируемого приложения (дз 11)
    def get_contact_list_in_group(self, group_name):
        wd = self.app.wd
        self.open_contact_list_via_home_button()
        self.filter_contacts_by_group(group_name)

        # Объявляем список для хранения полученного списка
        contacts = []

        # С помощью Inspect Element (Q) получаем имя, фамилию, которые хранятся в таблице, и
        # идентификаторы, которые хранятся в атрибуте value чек-бокса контакта
        # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
        # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
        # в виде css_selector, т. е. $$("tr[name='entry']"), то мы получим список элементов, которые
        # по этому селектору находятся
        for row in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
            # для получения идентификатора внутри элемента entry находим элемент с именем selected[]
            # (чек-бокс) и у этого чек-бокса получаем значение атрибута value
            cntct_id = row.find_element(By.NAME, "selected[]").get_attribute("value")

            # Получаем фамилию (2-й столбец)
            lastname = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text

            # Получаем имя (3-й столбец)
            firstname = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text

            # Добавляем полученные элементы в список
            contacts.append(Contact(id=cntct_id, firstname=firstname, lastname=lastname))

        # Возвращаем полученный готовый список
        return contacts


    # Добавлен метод определения идентификатора контакта из списка контактов по фамилии и имени (дз 11)
    def get_contact_id_by_lastname_from_list(self, contact_list, lastname, firstname):
        for c in contact_list:
            if c.lastname == lastname and c.firstname == firstname:
                return c.id
        return None

