# special file for a ficture which that should be shared by all tests

import pytest
from fixture.application import Application


# method for fixture initialization replaced from test file
# scope parameter added to fixture to launch the browser to run all tests in one session
@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    # indication of how the fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture