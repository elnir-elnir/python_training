#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By



class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        # Мой вариант с xpath заменен на вариант из лекции, чтобы показать пример использования кавычек
        # вместо экранирования (урок 5-4)
        #wd.find_element(By.XPATH, "//input[@value='Login']").click()
        #wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()


    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()


    # Determining whether there are elements on the page that meet the conditions
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0


    # # Новый метод: определяем текущего пользователя (урок 3-4)
    # def is_logged_in_as(self, username):
    #     wd = self.app.wd
    #     # Строка изменена в рамках урока 5-4: "(" + username + ")" изменили на форматирование
    #     #return wd.find_element(By.XPATH, "/html/body/div/div[1]/form/b").text == "(" + username + ")"
    #     return wd.find_element(By.XPATH, "/html/body/div/div[1]/form/b").text == "(%s)" % username


    # Меняем метод из урока 3-4: читаем имя пользователя непосредственно из браузера с
    # применением нового метода get_logged_user (урок 5-4)
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    # Новый метод для чтения имени пользователя из браузера и удаления из него лишних скобок применив
    # вырезку от первого до предпоследнего символа (отрезаем нулевой и последний символы)
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "/html/body/div/div[1]/form/b").text[1:-1]


    # New method has been added to ensure that we are logged out (lesson 3-4)
    def ensure_logout(self):
        wd = self.app.wd

        # We check whether we are inside an active session or outside (lesson 3-4)
        if self.is_logged_in():
            self.logout()


    # Новый метод проверки - нужно ли нам выполнять авторизацию или нет (урок 3-4)
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            # Проверяем, что выполнена авторизация нужного пользователя
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
