#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By



class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
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


    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()


    # add new method (swt, lesson 3-2)
    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def delete_group_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_name(group_name)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()


    def delete_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()


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


    def open_and_confirm_group_modify_without_changes_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_name(group_name)
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "update").click()


    # add new method (swt, lesson 3-2)
    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
