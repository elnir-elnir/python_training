#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------
import re

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
        # Выполняем сброс кеша в связи с созданием контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


    # Добавлен новый метод, который используется взамен предыдущего в связи с определением в конструкторе
    # дефолтных значений (дз 15)
    def create_for_default_values(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form_for_default_values(contact)
        # wd.find_element(By.NAME, "new_group").click()
        # Select(wd.find_element(By.NAME, "new_group")).select_by_visible_text(contact.new_group)
        # #wd.find_element(By.CSS_SELECTOR, f'select[name=new_group] > option[value="{contact.new_group}"]').click()
        self.change_visible_value("new_group", contact.new_group)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[19]").click()
        # Выполняем сброс кеша в связи с созданием контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


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


    # Добавлен новый метод, который используется взамен предыдущего в связи с определением в конструкторе
    # дефолтных значений (дз 15)
    def fill_contact_form_for_default_values(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_visible_value("bday", contact.bday)
        self.change_visible_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_visible_value("aday", contact.aday)
        self.change_visible_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)


    # add new method (lesson 3-2, дз 15)
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    # add new method (lesson 3-2, дз 15)
    def change_visible_value(self, param_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, param_name).click()
            Select(wd.find_element(By.NAME, param_name)).select_by_visible_text(text)


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
        # Изменено в рамках урока 5-4 для улучшения читаемости кода
        #row_xpath = f"//input[@id=\"MassCB\"]"
        row_xpath = f'//input[@id="MassCB"]'
        wd.find_element(By.XPATH, row_xpath).click()


    # add new method (lesson 3-5)
    # Метод модифицирован в связи с добавлением нового метода - выбор контакта по индексу (дз 13)
    def select_first_contact(self):
        self.select_contact_by_index(0)


    # Добавляем новый метод - выбор контакта по индексу (дз 13)
    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()


    # Добавляем новый метод - выбор контакта по идентификатору (дз 20)
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()


    def set_group(self, group_name):
        wd = self.app.wd
        wd.find_element(By.NAME, "to_group").click()
        Select(wd.find_element(By.NAME, "to_group")).select_by_visible_text(group_name)
        wd.find_element(By.NAME, "add").click()
        # Выполняем сброс кеша после включения контакта в группу, чтобы считался новый кеш (дз 12)
        self.contact_in_group_cache = None


    def exclude_contact_from_group(self, group_name):
        wd = self.app.wd
        xpath = f"//input[@type='submit' and @name='remove' and @value='Remove from \"{group_name}\"']"
        wd.find_element(By.XPATH, xpath).click()
        # Выполняем сброс кеша после исключения контакта из группы, чтобы считался новый кеш (дз 12)
        self.contact_in_group_cache = None


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


    # Добавлен метод перехода на страницу редактирования контакта по идентификатору (в рамках дз 13)
    def go_to_details_page_by_contact_id(self, contact_id):
        wd = self.app.wd
        row_xpath = f"//a[contains(@href, 'view.php?id={contact_id}') and img/@title='Details']"
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


    # Добавлен метод перехода на страницу редактирования контакта по идентификатору (в рамках дз 13)
    def go_to_edit_page_by_contact_id(self, contact_id):
        wd = self.app.wd
        row_xpath = f"//a[contains(@href, 'edit.php?id={contact_id}') and img/@title='Edit']"
        edit_link = wd.find_element(By.XPATH, row_xpath)
        edit_link.click()


    # Добавлен метод для перехода в редактирование первого в списке контакта (урок 3-5)
    def go_to_edit_page_of_first_contact_from_contact_list(self):
        wd = self.app.wd
        #wd.find_element(By.XPATH, "//tr[@name='entry'][1]//img[@title='Edit']").click()
        wd.find_element(By.XPATH, "(//tr[@name='entry' and not(contains(@style, 'display: none'))]//a[img/@title='Edit'])[1]").click()


    # Добавлен метод из курса - переход в форму редактирования контакта (урок 5-5)
    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()


    # Добавлен метод из курса - переход в форму просмотра детальной информации о контакте (урок 5-5)
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()


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
        # Выполняем сброс кеша в связи с модификацией контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


    # Добавлен метод модификации контакта со значениями по умолчанию (дз 20)
    def edit_contact_for_default_values(self, contact):
        wd = self.app.wd
        self.fill_contact_form_for_default_values(contact)
        wd.find_element(By.NAME, "update").click()
        # Выполняем сброс кеша в связи с модификацией контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


    def delete_contact_from_edit_page(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()
        # Выполняем сброс кеша в связи с удалением контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


    def delete_contact_from_contact_list(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()
        # Выполняем сброс кеша в связи с удалением контакта, чтобы считался новый кеш (дз 12)
        self.contact_cache = None
        self.contact_in_group_cache = None


    def delete_modal_window_closed(self):
        wd = self.app.wd
        wd.switch_to.alert.accept()


    # Добавялем метод подсчета количества чек-боксов на странице контактов (определяем количество
    # созданных контактов) - урок 3-5
    def count_of_contacts(self):
        wd = self.app.wd
        self.open_contact_list_via_addressbook_link()

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


    # Объявляем глобальную переменную для сохранения кеша (дз 12)
    contact_cache = None


    # # Новый метод для получения списка контактов из тестируемого приложения (дз 11)
    # # В метод добавлено получение кеша (дз 12)
    # # Начиная с урока 5-5 применется не мой метод, а метод с курса (см. следующий метод)
    # def get_contact_list(self):
    #     # Проверяем наличие доступного кеша и возвращаем кешированное значение, если оно доступно
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.open_contact_list_via_addressbook_link()
    #
    #         # Объявляем список для хранения полученного списка в кеше (дз 12)
    #         self.contact_cache = []
    #
    #         # С помощью Inspect Element (Q) получаем имя, фамилию, которые хранятся в таблице, и
    #         # идентификаторы, которые хранятся в атрибуте value чек-бокса контакта
    #         # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
    #         # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
    #         # в виде css_selector, т. е. $$("tr[name='entry']"), то мы получим список элементов, которые
    #         # по этому селектору находятся
    #         for row in wd.find_elements(By.CSS_SELECTOR, "tr[name='entry']"):
    #             # для получения идентификатора внутри элемента entry находим элемент с именем selected[]
    #             # (чек-бокс) и у этого чек-бокса получаем значение атрибута value
    #             cntct_id = row.find_element(By.NAME, "selected[]").get_attribute("value")
    #
    #             # Получаем фамилию (2-й столбец)
    #             lastname = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
    #
    #             # Получаем имя (3-й столбец)
    #             firstname = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
    #
    #             # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_cache)
    #             self.contact_cache.append(Contact(id=cntct_id, firstname=firstname, lastname=lastname))
    #
    #     # Возвращаем копию полученного кеша в виде списка (дз 12)
    #     return list(self.contact_cache)


    # Тот же метод, но переписан из курса (урок 5-5)
    # Применяется, начиная с урока 5-5
    def get_contact_list(self):
        # Проверяем наличие доступного кеша и возвращаем кешированное значение, если оно доступно
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()

            # Объявляем список для хранения полученного списка в кеше (дз 12)
            self.contact_cache = []

            # С помощью Inspect Element (Q) получаем имя, фамилию, которые хранятся в таблице, и
            # идентификаторы, которые хранятся в атрибуте value чек-бокса контакта
            # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
            # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
            # в виде css_selector, т. е. $$("tr[name='entry']"), то мы получим список элементов, которые
            # по этому селектору находятся
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")

                # # Отладка: выводим содержимое ячейки с телефонами
                # phones_text = cells[5].text
                # print(f"Текст в ячейке: '{phones_text}'")
                # print(f"repr: {repr(phones_text)}")
                # print(f"splitlines(): {phones_text.splitlines()}")
                # print("---")

                # Получаем имя (3-й столбец)
                firstname = cells[2].text
                # Получаем фамилию (2-й столбец)
                lastname = cells[1].text
                # Получаем идентификатор
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                # # Получаем информацию обо всех телефонах сразу, т. к. в приложении они все хранятся в
                # # одной ячейке (урок 5-5)
                # all_phones = cells[5].text.splitlines()
                #
                # # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_cache)
                # self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, home_phone=all_phones[0], mobile_phone=all_phones[1], work_phone=all_phones[2]))

                # Меняем в рамках урока 5-6, чтобы реализовать метод обратной проверки (склеиваем строки)
                # Получаем информацию обо всех телефонах сразу, т. к. в приложении они все хранятся в
                # одной ячейке (урок 5-5)
                all_phones = cells[5].text

                # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_cache)
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        # Возвращаем копию полученного кеша в виде списка (дз 12)
        return list(self.contact_cache)


    # Тот же метод, но переписан в рамках дз 14
    def get_contact_list_full(self):
        # Проверяем наличие доступного кеша и возвращаем кешированное значение, если оно доступно
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()

            # Объявляем список для хранения полученного списка в кеше (дз 12)
            self.contact_cache = []

            # С помощью Inspect Element (Q) получаем имя, фамилию, которые хранятся в таблице, и
            # идентификаторы, которые хранятся в атрибуте value чек-бокса контакта
            # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
            # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
            # в виде css_selector, т. е. $$("tr[name='entry']"), то мы получим список элементов, которые
            # по этому селектору находятся
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")

                # Получаем имя (3-й столбец)
                firstname = cells[2].text
                # Получаем фамилию (2-й столбец)
                lastname = cells[1].text
                # Получаем идентификатор
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                # Получаем адрес (4-й столбец)
                address = cells[3].text
                # Получаем информацию обо всех e-mail сразу, т.к. в приложении они все хранятся в одной
                # ячейке (дз 14)
                all_emails = cells[4].text

                # # Получаем информацию обо всех телефонах сразу, т. к. в приложении они все хранятся в
                # # одной ячейке (урок 5-5)
                # all_phones = cells[5].text.splitlines()
                #
                # # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_cache)
                # self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, home_phone=all_phones[0], mobile_phone=all_phones[1], work_phone=all_phones[2]))

                # Меняем в рамках урока 5-6, чтобы реализовать метод обратной проверки (склеиваем строки)
                # Получаем информацию обо всех телефонах сразу, т. к. в приложении они все хранятся в
                # одной ячейке (урок 5-5)
                all_phones = cells[5].text

                # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_cache)
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, address=address, all_emails_from_home_page=all_emails,
                            all_phones_from_home_page=all_phones))

        # Возвращаем копию полученного кеша в виде списка (дз 12)
        return list(self.contact_cache)


    # Объявляем глобальную переменную для сохранения кеша контактов в конкретной группе (дз 12)
    contact_in_group_cache = None


    # Новый метод для получения списка контактов в группе из тестируемого приложения (дз 11)
    # В метод добавлено получение кеша (дз 12)
    def get_contact_list_in_group(self, group_name):
        # Проверяем наличие доступного кеша и возвращаем кешированное значение, если оно доступно
        if self.contact_in_group_cache is None:
            wd = self.app.wd
            self.open_contact_list_via_home_button()
            self.filter_contacts_by_group(group_name)

            # Объявляем список для хранения полученного списка в кеше (дз 12)
            self.contact_in_group_cache = []

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

                # Добавляем полученные элементы в список (в дз 12 изменили groups на self.contact_in_group_cache)
                self.contact_in_group_cache.append(Contact(id=cntct_id, firstname=firstname, lastname=lastname))

        # Возвращаем копию полученного кеша в виде списка (дз 12)
        return list(self.contact_in_group_cache)


    # Добавлен метод определения идентификатора контакта из списка контактов по фамилии и имени (дз 11)
    def get_contact_id_by_lastname_from_list(self, contact_list, lastname, firstname):
        for c in contact_list:
            if c.lastname == lastname and c.firstname == firstname:
                return c.id
        return None


    # Добавлен метод получения информации со страницы редактирования контакта (урок 5-5)
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        home_phone = wd.find_element(By.NAME, 'home').get_attribute('value')
        mobile_phone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        work_phone = wd.find_element(By.NAME, 'work').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)


    # Добавлен метод получения инфорамации с адресом и эл.почтой со страницы редактирования контакта (дз 14)
    def get_contact_info_with_address_and_email_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        address = wd.find_element(By.TAG_NAME, 'textarea').get_attribute('value')
        email = wd.find_element(By.NAME, 'email').get_attribute('value')
        email2 = wd.find_element(By.NAME, 'email2').get_attribute('value')
        email3 = wd.find_element(By.NAME, 'email3').get_attribute('value')
        home_phone = wd.find_element(By.NAME, 'home').get_attribute('value')
        mobile_phone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        work_phone = wd.find_element(By.NAME, 'work').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2, email3=email3, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone)


    # Добавлен метод получения информации со страницы просмотра информации о контакте (урок 5-5)
    # На тсранице с детальной информацией отсутствуют отдельные теги как для каждого телефона,
    # так и для блока телефонов (как это было на странице со списком контактов)
    # Поэтому вырезать номера телефонов надо с применением регулярных выражений
    # Тест test_phones_on_contact_view_page падает при пустых полях. Пересмотреть лекцию
    # (перепроверить метод). Или доработать метод.
    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)

        # Получаем весь текст со страницы с информацией
        text = wd.find_element(By.ID, "content").text
        # Применяем регулярные выражения к полученному тексту
        # .* означает, что мы смотрим произвольные символы до конца строки
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)



    '''Методы сравнения'''

    # Метод сравнения полей контактов, где contact1 - контакт полученый из приложения, contact2 -
    # контакт, полученный из базы данных (дз 21)
    def assert_contacts(self, contact1, contact2):
        assert contact1.firstname == contact2.firstname
        assert contact1.lastname == contact2.lastname
        assert contact1.address == contact2.address
        assert (contact1.all_emails_from_home_page ==
                self.merge_emails_like_on_home_page(contact2))
        assert (contact1.all_phones_from_home_page ==
                self.merge_phones_like_on_home_page(contact2))



    '''Методы обработки'''

    # Метод перенесен из файла test_phones.py в рамках дз 21
    # Добавлен метод получения строки без символов "пробел", "минус", скобок с применением регулярных выражений
    # На первом месте указывается, что надо заменить, на втором - на что надо заменить, на третьем -
    # где надо заменить
    def clear_brackets_space_and_hyphen(self, s):
        return re.sub("[() -]", "", s)


    # Метод перенесен из файла test_phones.py в рамках дз 21
    # Добавляем метод склеивания строк (урок 5-6)
    # Склеиваем при помощи перевода строки, используя функцию join, которой в качечтве параметров
    # передаем список телефонов
    # Исключаем элементы = None с помощью функции filter к списку (до применения функции map)
    # Для очистки телефонов от дополнительных символов применяем map, чтобы применить метод clear
    # ко всем элементам списка сразу
    # А затем к результату функции map применяем filter того, чтобы не учитывать при склейке
    # пустые телефоны
    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_brackets_space_and_hyphen(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


    # Метод перенесен из файла test_contact_list.py в рамках дз 21
    # Добавлен метод получения строки без символов "пробел" с применением регулярных выражений
    # На первом месте указывается, что надо заменить, на втором - на что надо заменить, на третьем -
    # где надо заменить
    def clear_space(self, s):
        return re.sub(" ", "", s)


    # Метод перенесен из файла test_contact_list.py в рамках дз 21
    # Добавляем метод склеивания строк (дз 14)
    # Склеиваем при помощи перевода строки, используя функцию join, которой в качечтве параметров
    # передаем список адресов электронной почты
    # Исключаем элементы = None с помощью функции filter к списку (до применения функции map)
    # Для очистки адресов электронной почты от дополнительных символов применяем map, чтобы применить
    # метод clear ко всем элементам списка сразу
    # А затем к результату функции map применяем filter того, чтобы не учитывать при склейке
    # пустые адреса электронной почты
    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_space(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3]))))
