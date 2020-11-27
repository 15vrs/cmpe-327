from flask import render_template, request, session, redirect
from qa327 import app
from datetime import date
import qa327.backend as bn
import re

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # if already logged in, redirect to profile page
    if 'logged_in' in session:
	    return redirect('/')
    else:
	# templates are stored in the templates folder
        return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if (email_check(email) is None) or (pwd_check(password) is None): #no match in regex
        error_message = 'Email/Password combination incorrect'

    elif password != password2:
        error_message = "The passwords do not match"

    elif username_check(name) is None: #no match in regex
        error_message = "Username format error"

    else:
        error_message = bn.register_user(email, name, password, password2)
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('login.html', message=error_message)
    else:
        return redirect('/login')

def username_check(name):
    if name != None:
        # regex to check username is alphanumeric
        regex = '^[a-zA-Z0-9]+[a-zA-Z0-9 ]?[a-zA-Z0-9]+$'
        # check username is of required length
        if len(name) > 2 and len(name) < 20:
            return re.match(regex, name)

@app.route('/login', methods=['GET'])
def login_get():
    if 'logged_in' in session:
        return redirect('/')
    else:
        return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    if (email_check(email) is None) or (pwd_check(password) is None): #no match in regex
        return render_template('login.html', message='email/password format is incorrect')

    else:
        user = bn.login_user(email, password)
        if user:
            session['logged_in'] = user.email
            """
            Session is an object that contains sharing information 
            between browser and the end server. Typically it is encrypted 
            and stored in the browser cookies. They will be past 
            along between every request the browser made to this services.
    
            Here we store the user object into the session, so we can tell
            if the client has already login in the following sessions.
    
            """
            # success! go back to the home page
            # code 303 is to force a 'GET' request
            return redirect('/', code=303)
        else:
            return render_template('login.html', message='email/password combination incorrect')

def email_check(email):
    if email != None:
        # regex to check email conforms to RFC-5322
        regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        return re.match(regex, email)

def pwd_check(password):
    if password != None:
        # regex to check pwd conforms to minimum length 6,
        # at least an upper case, a lower case, and a special characters
        regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[A-Za-z\d\W]{6,}$'
        return re.match(regex, password)

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)

@app.route('/update', methods=['POST'])
def update_post():
    user_email = session['logged_in']
    user_name = bn.get_user(email)
    ticket_name = request.form.get('update-name')
    ticket_quantity = request.form.get('update-quantity')
    ticket_price = request.form.get('update-price')
    ticket_date = request.form.get('update-date')
    error_message = None

    if (ticket_name_check(ticket_name) is None): #no match in regex
        error_message = 'Ticket name is incorrect'

    elif ticket_quantity <= 0 or ticket_quantity > 100:
        error_message = "Invalid quantity in ticket update form"

    elif ticket_price < 10 or ticket_price > 100:
        error_message = "Invalid price in ticket update form"

    elif len(ticket_date) != 8:
        error_message = "Invalid date in ticket update form"
    
    elif (ticket_date < int(date.today().strftime("%Y%m%d"))):
        error_message = "Date in ticket update form has already past"
    
    else:
        set_ticket(user_name, ticket_name, 3, ticket_price, ticket_date)
        error_message = bn.update_ticket(user_name, ticket_name, ticket_quantity, ticket_price, ticket_date)

    if error_message:
        return render_template('index.html', message=error_message)
    else:
        return redirect('/')
    
def ticket_name_check(name):
    if name != None:
        # regex to check username is alphanumeric
        regex = '^[a-zA-Z0-9]+[a-zA-Z0-9 ]?[a-zA-Z0-9]+$'
        # check username is of required length
        if len(name) <= 60:
            return re.match(regex, name)