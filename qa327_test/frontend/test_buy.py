import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
import qa327.backend as bn

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!'),
    balance=5000
)

test_ticket = Ticket(
    owner = 'test_seller@test.com',
    name = 'Test Ticket',
    quantity = 10,
    price = 10,
    date = 20201230
)

class SellTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    def _login(self, *_):
        # Navigate to /logout to invalidate any existing sessions
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click('input[type="submit"]')

    def test_R6_1a(self, *_):
        """
        The name of the ticket must be alphanumeric-only.
        """
        self._login()
        self.type("#buy-name", "#invalidticket")
        self.type("#buy-quantity", test_ticket.quantity)
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_1b(self, *_):
        """
        The name of the ticket is not allowed if the first character is a space.
        """
        self._login()
        self.type("#buy-name", " firstchar")
        self.type("#buy-quantity", test_ticket.quantity)
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_1c(self, *_):
        """
        The name of the ticket is not allowed if the last character is a space.
        """
        self._login()
        self.type("#buy-name", "lastchar ")
        self.type("#buy-quantity", test_ticket.quantity)
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_2(self, *_):
        """
        The name of the ticket is no longer than 60 characters
        """
        self._login()
        self.type("#buy-name", "unfortunatelythistickethasalittleoversixtycharactersinitsname")
        self.type("#buy-quantity", test_ticket.quantity)
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_3a(self, *_):
        """
        Ticket quantity of 0 or less produces an error message.
        """
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "0")
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid quantity in ticket buy form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')
    
    def test_R6_3b(self, *_):
        """
        Ticket quantity of over 100 produces an error message.
        """
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "101")
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid quantity in ticket buy form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_4a(self, *_):
        """
        The ticket name exists in the database and the quantity available is more than the quantity requested to buy(positive).
        """
        # Delete old database then add a new user and ticket to database
        bn.delete_database()
        bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)
        bn.set_ticket(test_ticket.owner, test_ticket.name, test_ticket.quantity, test_ticket.price, test_ticket.date)
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "5")
        # Click on `#update-submit` element
        self.click('input[value="Buy"]')
        # Verify profile page displays no error message and balance has been reduced
        self.assert_element_not_visible("#message")
        self.assert_element("#balance")
        self.assert_text("User Balance: $4930", "#balance")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_4b(self, *_):
        """
        The ticket name exists in the database and the quantity avilable is less than the quantity requested to buy(negative).
        """
        # Delete old database then add a new user and ticket to database
        bn.delete_database()
        bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)
        bn.set_ticket(test_ticket.owner, test_ticket.name, test_ticket.quantity, test_ticket.price, test_ticket.date)
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "11")
        self.click('input[value="Buy"]')
        # Verify profile page displays an error message and balance not reduced
        self.assert_element("#message")
        self.assert_text("Not enough tickets for sale", "#message")
        self.assert_element("#balance")
        self.assert_text("User Balance: $5000", "#balance")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_4c(self, *_):
        """
        The ticket does not exists in the database and the quantity available is more than the quantity requested to buy(negative).
        """
        # Delete old database then add a new user and ticket to database
        bn.delete_database()
        bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)
        bn.set_ticket(test_ticket.owner, test_ticket.name, test_ticket.quantity, test_ticket.price, test_ticket.date)
        self._login()
        self.type("#buy-name", "noTicketHere")
        self.type("#buy-quantity", "5")
        self.click('input[value="Buy"]')
        # Verify profile page displays an error message and balance not reduced
        self.assert_element("#message")
        self.assert_text("Ticket does not exist", "#message")
        self.assert_element("#balance")
        self.assert_text("User Balance: $5000", "#balance")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_5a(self, *_):
        """
        The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)(positive).
        """
        # Delete old database then add a new user and ticket to database
        bn.delete_database()
        bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)
        bn.set_ticket(test_ticket.owner, test_ticket.name, test_ticket.quantity, test_ticket.price, test_ticket.date)
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "10")
        self.click('input[value="Buy"]')
        # Verify profile page displays no error message and balance has been reduced
        self.assert_element_not_visible("#message")
        self.assert_element("#balance")
        self.assert_text("User Balance: $4860", "#balance")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    def test_R6_5b(self, *_):
        """
        The user has less balance than the ticket price * quantity + service fee (35%) + tax (5%)(negative).
        """
        # Delete old database then add a new user and ticket to database
        bn.delete_database()
        bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)
        bn.set_ticket(test_ticket.owner, test_ticket.name, test_ticket.quantity, 1000, test_ticket.date)
        self._login()
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", "10")
        self.click('input[value="Buy"]')
        # Verify profile page displays an error message and balance not reduced
        self.assert_text("Insufficient balance", "#message")
        self.assert_element("#balance")
        self.assert_text("User Balance: $5000", "#balance")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')
