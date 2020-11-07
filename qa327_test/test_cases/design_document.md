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

**How test cases of different levels (frontend, backend units, integration) are organized.**

- `???`

**The order to the test cases (which level first which level second).**

- The priority of tests is unit tests first, if everything passes then integration tests ran locally then tested on GitHub Actions.

**Techniques and tools used for testing.**

- The frontend and backend components will be integration tested using Selenium.
- Tests will be run locally as they are written, and must be passing on GitHub Actions before merging to master.
- The methods listed above will be tested at the unit test level using multiple inputs and verifying the output.

**Environments (all the local environment and the cloud environment) for the testing.**

- The enviroment used for testing will be...
- Windows 10 ver.2004 (local)
- `add whatever mac/linux machine you guys are using`
- Ubuntu 18.04 (cloud)
- exclusively using the Chrome browser

**Responsibility (who is responsible for which test case, and in case of failure, who should you contact)**

- The developer that wrote the test cases in A1 will be responsible for writing and maintaining test cases.

| Test Case     | Contact |
|---------------|---------|
| R1 - /login   | Vivian  |
| R2 - /register| Adrian  |
| R3 - /        | Kevin   |
| R4 - /sell    | Vivian  |
| R5 - /update  | Adrian  |
| R6 - /buy     | Kevin   |
| R7 - /logout  | Adrian  |
| R8 - /*       | Adrian  |

**Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unnecessary cost)**

- The repository owner can check how many action minutes are left and notify the rest of the team if there's a chance we'll hit the limit
- To minimize the amount of unnecessary action minutes used, the entire test suite will first be run locally to ensure everything passes before being pushed to Github.
- Can also skip running the CI if no code was changed
