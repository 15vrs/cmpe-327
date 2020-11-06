# Design Document

## Architecture

| Classes          | Description                                        |
|------------------|----------------------------------------------------|
| User(db.Model)   | Contains all stored information for a given user   |
| Ticket(db.Model) | Contains all stored information for a given ticket |

| Layer    | Methods                                         | Description                                                           |
|----------|-------------------------------------------------|-----------------------------------------------------------------------|
| Frontend | register_get()                                  | Renders register page if not logged in                                |
| Frontend | register_post()                                 | Attempts to register with supplied new user information               |
| Frontend | login_get()                                     | Renders login page with a login message                               |
| Frontend | login_post()                                    | Attempts to login with an email and password                          |
| Frontend | authenticate(inner_function)                    | Wrapper, authenticates user before allowing access to other functions |
| Frontend | profile(user)                                   | Renders user’s profile page and tickets menu                          |
| Frontend | email_check(email)                              | Verifies format of email passed in                                    |
| Frontend | pwd_check(password)                             | Verifies format of password passed in                                 |
| Frontend | username_check(name)                            | Verifies format of username passed in                                 |
| Backend  | get_user(email)                                 | Attempt to return user based on supplied email                        |
| Backend  | login_user(email, password)                     | Attempt to authenticate user’s login                                  |
| Backend  | register_user(email, name, password, password2) | Attempt to register new user to the database                          |
| Backend  | get_all_tickets()                               | Return all non-expired tickets from database                          |
| Backend  | set_ticket(owner, name, quantity, price, date)  | Attempt to register a new ticket to the database                      |

## Test Plan

points to cover:
- How test cases of different levels (frontend, backend units, integration) are organized.
- The order ot the test cases (which level first which level second).
- Techniques and tools used for testing.
- Environments (all the local environment and the cloud environment) for the testing.
- Responsibility (who is responsible for which test case, and in case of failure, who should you contact)
- Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)
