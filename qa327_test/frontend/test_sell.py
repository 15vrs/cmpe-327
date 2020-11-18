import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import Mock, patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!'),
    balance=0
)
# Mock some sample tickets
test_ticket = Ticket(
    owner = 'test_frontend@test.com',
    name = 'test ticket',
    quantity = 1,
    price = 20,
    date = 20210901
)

@patch('qa327.backend.get_user', return_value=test_user)
@patch('qa327.backend.login_user', return_value=test_user)
class SellTest(BaseCase):

    def setupBeforeEachTest(self,  *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # login to access profile page
        self.open(base_url + '/login')
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        self.assert_element_present("h2#welcome-header")
        self.assert_text("Welcome", "h2#welcome-header")

    # R4.1a Ticket name with special characters produces an error message.
    def test_sell_ticket_name_special_characters(self, *_):
        SellTest.setupBeforeEachTest(self)
        self.type("#sell-name", "test ticker!@#")
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")



