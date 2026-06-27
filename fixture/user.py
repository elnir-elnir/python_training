# ------------------------------------------------------------------------------
# qa:
# description:
# ------------------------------------------------------------------------------
from fixture.data_factory import DataFactory


class UserHelper:

    def __init__(self, app):
        self.app = app
        self.data_factory = DataFactory(app)

    def login(self):
        user = self.data_factory.create_user()
        self.app.session.login(user.password, user.login)
