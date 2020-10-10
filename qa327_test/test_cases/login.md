# Test Cases for `/login`

| Test Case ID | Target Spec | Purpose  |
|---|---|---|
| R1.1  | [GET] `/login`  | If the user hasn't logged in, show the login page  |
| R1.2  | [GET] `/login`  | The login page has a message that by default says 'please login'  |
| R1.3  | [GET] `/login`  | If the user has logged in, redirect to the user profile page  |
| R1.4  | [GET] `/login`  | The login page provides a login form which requests two fields: email and passwords  |
| R1.5  | [POST] `/login`  | The login form can be submitted as a POST request to the current URL  |
| R1.6a-c  | [POST] `/login`  | Email and password both cannot be empty  |
| R1.7a-b  | [POST] `/login`  | Email has to follow addr-spec defined in RFC 5322  |
| R1.8a-e  | [POST] `/login`  | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character  |
| R1.9  | [POST] `/login`  | For any formatting errors, render the login page and show the message 'email/password format is incorrect  |
| R1.10  | [POST] `/login`  | If email/password are correct, redirect to `/`  |
| R1.11a-b  | [POST] `/login`  | Otherwise, redict to `/login` and show message 'email/password combination incorrect'  |

# Test Plans for `/login`

Given the following test data for each test case:
```
    test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

## Test Case R1.1
If the user hasn't logged in, show the login page. 

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R1.2
The login page has a message that by default says 'please login'.
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that 'please login' is visible by checking for the `#message' element in DOM

## Test Case R1.3
If the user has logged in, redirect to the user profile page
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify verify that login page is visible
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R1.4
The login page provides a login form which requests two fields: email and passwords

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking for expected elements (eg. `form-group`) in DOM
- verify that `#email` and `#password` elements exist in the DOM

## Test Case R1.5
The login form can be submitted as a POST request to the current URL

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200

## Test Case R1.6a
Email and password both cannot be empty

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.6b
Email cannot be empty

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.6c
Password cannot be empty

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.7a
Email following addr-spec defined in RFC 5322 can login

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter a valid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200

## Test Case R1.7b
Email not following addr-spec defined in RFC 5322 cannot login and error message is displayed

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter an invalid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.8a
Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200


## Test Case R1.8b
User with password shorter than 6 characters cannot log in and error message is displayed

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.8c
User with password with no uppercase characters cannot log in and error message is displayed

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.8d
User with password with no lowercase characters cannot log in and error message is displayed

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.8e
User with password with no special characters cannot log in and error message is displayed

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.9
For any formatting errors, render the login page and show the message 'email/password format is incorrect.' 
**Duplicate of cases 8b-e**
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.10
If email/password are correct, redirect to `/`

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200
- verify that user is navigated to `/` profile page
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R1.11a
Invalid email redirects to `/login` with error message 'email/password combination incorrect'
**Duplicate of earlier test cases?**
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter invalid email for test_user
- click on `#password` element and enter valid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`

## Test Case R1.11b
Invalid password redirects to `/login` with error message 'email/password combination incorrect'
**Duplicate of earlier test cases?**
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter valid email for test_user
- click on `#password` element and enter invalid password for test_user
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401?
- verify login page displays error message by checking content of `#message`