#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app


    # Добавлена проверка открытой страницы (урок 3-6)
    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()


    def go_to_group_page(self, group_name):
        wd = self.app.wd
        row_xpath = f"//div[@id='content']//a[contains(text(), 'group page \"{group_name}\"')]"
        group_page_link = wd.find_element(By.XPATH, row_xpath)
        group_page_link.click()


    def create(self, group):
        wd = self.app.wd
        # open groups page replaced from tests to create_group method
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        # return to groups page replaced from tests to create_group method
        self.return_to_groups_page()
        # Выполняем сброс кеша в связи с добавлением группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    # add new method (swt, lesson 3-2)
    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    # add new method (swt, lesson 3-2)
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    # Модифицируем метод удаления первой группы в связи с появлением нового метода удаления группы
    # по индексу (урок 4-11)
    def delete_first_group(self):
        self.delete_group_by_index(0)


    # Добавляем новый метод удаления группы - по случайно определенному индексу (урок 4-11)
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # Меняем метод выбора группы с select_first_group на select_group_by_index (урок 4-11)
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        # Выполняем сброс кеша в связи с удалением группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    # add new method (swt, lesson 3-2)
    # Метод модифицирован в связи с добавлением нового метода - выбор группы по индексу (урок 4-11)
    def select_first_group(self):
        self.select_group_by_index(0)


    # Добавляем новый метод - выбор группы по индексу (урок 4-11)
    def select_group_by_index(self, index):
        wd = self.app.wd
        # Изменилась функция выбора группы в списке (урок 4-11)
        #wd.find_element(By.NAME, "selected[]").click()
        wd.find_elements(By.NAME, "selected[]")[index].click()


    def delete_group_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_name(group_name)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        # Выполняем сброс кеша в связи с удалением группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    def delete_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        # Выполняем сброс кеша в связи с удалением группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    def select_group_by_name(self, group_name):
        wd = self.app.wd
        row_xpath = f"//span[@class='group' and normalize-space()='{group_name}']"
        row = wd.find_element(By.XPATH, row_xpath)
        row.find_element(By.XPATH, ".//input[@type='checkbox']").click()


    def full_modify_group_by_name(self, group_name, new_group_name, new_group_header, new_group_footer):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_name(group_name)
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(new_group_name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(new_group_header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(new_group_footer)
        wd.find_element(By.NAME, "update").click()
        # Выполняем сброс кеша в связи с модификацией группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    # Добавлен метод модификации группы по индексу (дз 13)
    def full_modify_group_by_index(self, index, new_group_name, new_group_header, new_group_footer):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(new_group_name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(new_group_header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(new_group_footer)
        wd.find_element(By.NAME, "update").click()
        # Выполняем сброс кеша в связи с модификацией группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    def open_and_confirm_group_modify_without_changes_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_name(group_name)
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "update").click()


    # add new method (swt, lesson 3-2)
    # Метод изменен в связи с добавлением метода модификации группы по индексу (урок 4-11)
    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)


    # Добавлен метод модификации группы по индексу (урок 4-11)
    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        # Выполняем сброс кеша в связи с модификацией группы, чтобы считался новый кеш (урок 4-10)
        self.group_cache = None


    # Добавялем метод подсчета количества чек-боксов на странице groups (определяем количество
    # созданных групп) - урок 3-5
    def count(self):
        wd = self.app.wd
        self.open_groups_page()

        # wd.find_elements(By.NAME, "selected[]") - находим на странице все элементы
        # с названием "selected[]"
        # len(wd.find_elements(By.NAME, "selected[]")) - считаем количество найденных элементов
        return len(wd.find_elements(By.NAME, "selected[]"))


    # Добавляем метод подсчета количества групп по имени (урок 3-5)
    def count_group_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        row_xpath = f"//span[@class='group' and normalize-space()='{group_name}']"
        row = wd.find_elements(By.XPATH, row_xpath)
        return len(row)

    # Добавялем метод подсчета количества чек-боксов на странице контактов (определяем количество
    # созданных контактов) - урок 3-5
    def count_of_contacts_in_group(self, group_name):
        wd = self.app.wd
        self.app.contact.open_contact_list_via_home_button()
        self.app.contact.filter_contacts_by_group(group_name)
        return len(wd.find_elements(By.NAME, "selected[]"))


    # Объявляем глобальную переменную для сохранения кеша (урок 4-10)
    group_cache = None

    # Новый метод для получения списка групп из тестируемого приложения (урок 4-7)
    # В метод добавлено получение кеша (урок 4-10)
    def get_group_list(self):

        # Проверяем наличие доступного кеша и возвращаем кешированное значение, если оно доступно
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()

            # Объявляем список для хранения полученного списка в кеше (урок 4-10)
            self.group_cache = []

            # С помощью Inspect Element (Q) получаем название групп и  идентификаторы, которые
            # хранятся в атрибуте value чек-бокса группы
            # Чтобы убедиться, что в по запросу span.group храняться нужные нам элементы в браузере в
            # Инструменте разработчика переходим во вкладку Console и вызываем функцию $$ с параметром
            # в виде css_selector, т. е. $$('span.group'), то мы получим список элементов, которые
            # по этому селектору находятся
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                # Для получения текста обращаемся к свойству text
                text = element.text

                # для получения идентификатора внутри элемента span находим элемент с именем selected[]
                # (чек-бокс) и у этого чек-бокса получаем значение атрибута value
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")

                # Добавляем полученные элементы в список (в уроке 4-10 изменили groups на self.group_cache)
                self.group_cache.append(Group(name=text, id=id))
        # Возвращаем копию полученного кеша в виде списка (урок 4-10)
        return list(self.group_cache)


    def get_group_id_by_name_from_list(self, group_list, group_name):
        for g in group_list:
            if g.name == group_name:
                return g.id
        return None


    def find_group_index_by_id(self, group_list, group_id):
        for i, g in enumerate(group_list):
            if g.id == group_id:
                return i
        return None
