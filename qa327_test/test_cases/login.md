# Test Cases for `/login`

| Test Case ID | Target Spec | Purpose  |
|---|---|---|
| R1.1  | [GET] `/login`  | If the user hasn't logged in, show the login page  |
| R1.2  | [GET] `/login`  | The login page has a message that by default says 'please login'  |
| R1.3  | [GET] `/login`  | If the user has logged in, redirect to the user profile page  |
| R1.4  | [GET] `/login`  | The login page provides a login form which requests two fields: email and passwords  |
| R1.5  | [POST] `/login`  | The login form can be submitted as a POST request to the current URL  |
| R1.6  | [POST] `/login`  | Email and password both cannot be empty  |
| R1.7  | [POST] `/login`  | Email has to follow addr-spec defined in RFC 5322  |
| R1.8  | [POST] `/login`  | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character  |
| R1.9  | [POST] `/login`  | For any formatting errors, render the login page and show the message 'email/password format is incorrect  |
| R1.10  | [POST] `/login`  | If email/password are correct, redirect to `/`  |
| R1.11  | [POST] `/login`  | Otherwise, redict to `/login` and show message 'email/password combination incorrect'  |

# Test Plans for `/login`

Given the following test data for each test case:
```
    test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
Provided all the test cases with necessary details regarding their input/expected output/actions. 
Think of you writing the test cases and the other testers (e.g. TAs) will have to implement those but not you.	
Test Run Plan. Have a thorough understanding of how the testing pipeline works (framework+GitHub-Acton and how your team will be organizing and running the test cases.

## Test Case R1.1
If the user hasn't logged in, show the login page. 

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- verify that login page is displayed by checking expected elements (eg. `form-group`) are the DOM

## Test Case R1.2
The login page has a message that by default says 'please login'.
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- verify that 'please login' is displayed by checking for the `#message' element in the DOM

## Test Case R1.3
If the user has logged in, redirect to the user profile page
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- verify verify that login page is displayed
- click on `#email` element and enter email for test_user
- click on `#password` element and enter password for test_user
- click on `#btn-submit` element to login
- navigate to `/login` and verify that [GET] `/login` was called
- verify that profile page is displayed by checking for `#welcome-header` element in the DOM

## Test Case R1.4
The login page provides a login form which requests two fields: email and passwords

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- verify that login page is displayed by checking expected elements (eg. `form-group`) are the DOM
- verify that `#email` and `#password` elements exist in the DOM
