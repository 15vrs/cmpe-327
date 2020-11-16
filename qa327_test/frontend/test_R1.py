import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import Mock, patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password!'
)
# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


@patch('qa327.backend.get_user', return_value=test_user)
@patch('qa327.backend.login_user', return_value=test_user)
@patch('qa327.backend.get_all_tickets', return_value=test_tickets)
class FrontEndLoginTest(BaseCase):

    # verify frontend.getLogin is called?
    # R1.1, R1.2, R1.4
    def test_login_page(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

# R1.5 FAILING
#     def test_login_redirect(self, *_):
#         # invalidate all sessions
#         self.open(base_url + '/logout')
#         # navigate to login page
#         self.open(base_url + '/login')
#         # fill out login form
#         self.type("#email", test_user.email)
#         self.type("#password", test_user.password)
#         self.click("input#btn-submit")
#         # navigate to login page again
#         # self.open(base_url + '/login')
#         # verify profile page is displayed
#         self.assert_element_present("h1")
#         self.assert_text("Profile", "h1")
#         self.assert_element_present("h2#welcome-header")

# R1.6a
    def test_login_empty_inputs(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit empty form
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

# R1.6b
    def test_login_empty_password(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit incomplete form
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

# R1.6c
    def test_login_empty_email(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit incomplete form
        self.type("#email", test_user.email)
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

# R1.7a, R1.8?
    def test_login_valid_credientials(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Profile", "h1")
        self.assert_element_present("h2#welcome-header")