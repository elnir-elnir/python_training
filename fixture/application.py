#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.data_factory import DataFactory
from fixture.user import UserHelper



class Application:

    # driver is initialized when the fixture is created
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        # helper gets a reference to an object of the Application class
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        # add Data class for creating test data
        self.data = DataFactory(self)
        self.user = UserHelper(self)


    # Checks that the WebDriver can interact with the current browser window    #
    # Used for safe execution of operations when the browser may be closed
    def is_valid(self):
        try:
            # Requesting the URL of the currently open page
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
