# Test Cases for `/sell`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R4.1  | [POST] `/sell`  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character  |
| R4.2  | [POST] `/sell`  | The name of the ticket is no longer than 60 characters  |
| R4.3  | [POST] `/sell`  | The quantity of the tickets has to be more than 0, and less than or equal to 100  |
| R4.4  | [POST] `/sell`  | Price has to be of range [10, 100]  |
| R4.5  | [POST] `/sell`  | Date must be given in the format YYYYMMDD (e.g. 20200901)  |
| R4.6  | [POST] `/sell`  | For any errors, redirect back to / and show an error message  |
| R4.7  | [POST] `/sell`  | The added new ticket information will be posted on the user profile page  |

# Test Plans for `/sell`

The following test data is to be used for each test case:
```
    test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

To setup for each test case, the following steps will be completed (omitted from each test case for brevity):
- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- enter valid email and password for test_user in `#email` and `#password` elements
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R4.1
The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

- steps

## Test Case R4.2
The name of the ticket is no longer than 60 characters

- steps

## Test Case R4.3
The quantity of the tickets has to be more than 0, and less than or equal to 100.

- steps

## Test Case R4.4
Price has to be of range [10, 100]

- steps

## Test Case R4.5
Date must be given in the format YYYYMMDD (e.g. 20200901).

- steps

## Test Case R4.16
For any errors, redirect back to / and show an error message.

- steps

## Test Case R4.17
The added new ticket information will be posted on the user profile page.

- steps