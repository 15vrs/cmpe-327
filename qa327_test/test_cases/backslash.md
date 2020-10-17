# Test Cases for `/login`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R3.1 | [GET] `/` | If the user hasn't logged in, redirect the login page  |
| R3.2 | [GET] `/` | This page shows a header 'Hi {}'.format(user.name) |
| R3.3 | [GET] `/` | This page shows user balance. |
| R3.4 | [GET] `/` | This page shows a logout link, pointing to /logout |
| R3.5 | [GET] `/` | This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. |
| R3.6 | [GET] `/` | This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date. |
| R3.7 | [GET] `/` | This page contains a form that a user can buy new tickets. Fields: name, quantity |
| R3.8 | [GET] `/` | The ticket-selling form can be posted to /sell |
| R3.9 | [GET] `/` | The ticket-buying form can be posted to /buy |
| R3.10 | [GET] `/` | The ticket-update form can be posted to /update |

# Test Plans for `/`

## Test Case R3.1
**If the user hasn't logged in, redirect the login page.**  

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R3.2
**This page shows a header 'Hi {}'.format(user.name)**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
- verify that user is navigated to `/`
- verify that `/` shows header `'Hi test_frontend'`

## Test Case R3.3
**This page shows user balance.**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows the users balance `'Balance: 30'`

## Test Case R3.4
**This page shows a logout link, pointing to /logout.**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a logout link `'logout'` pointing to `/logout`

## Test Case R3.5
**This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/`shows a list of all available tickets that aren't expired

## Test Case R3.6
**This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a form to submit new tickets for sell with fields `#ticket-name`, `#quantity`, `#price`, `#date`

## Test Case R3.7
**This page contains a form that a user can buy new tickets. Fields: name, quantity.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a form to buy new tickets with fields `#ticket-name`, `#quantity`

## Test Case R3.8
**The ticket-selling form can be posted to /sell.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#sell_ticket_name` and enter `test_ticket.name`
- click on `#sell_quantity` and enter `test_ticket.quantity`
- click on `#sell_price` and enter `test_ticket.price`
- click on `#sell_date` and enter `test_ticket.date`
- click on `#sell_submit` to submit the form

## Test Case R3.9
**The ticket-buying form can be posted to /buy.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#buy_ticket_name` and enter `test_ticket.name`
- click on `#buy_quantity` and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form

## Test Case R3.10
**The ticket-update form can be posted to /update.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#update_ticket_name` and enter `test_ticket.name`
- click on `#update_quantity` and enter `test_ticket.quantity`
- click on `#update_price` and enter `test_ticket.price`
- click on `#update_date` and enter `test_ticket.date`
- click on `#update_submit` to submit the form
