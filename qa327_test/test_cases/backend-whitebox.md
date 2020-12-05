# Test Cases for `buy_ticket`

| Path | Statements              | Email                   | Name        | Quantity |
|------|-------------------------|-------------------------|-------------|----------|
| P1   | 1,2,3,4                 | test_user@test.com      | Fake Ticket | 5        |
| P2   | 1,2,3,5,6               | test_user@test.com      | Test Ticket | 33       |
| P3   | 1,2,3,5,7,8             | penniless_user@test.com | Test Ticket | 5        |
| P4   | 1,2,3,5,7,9,10,11,13,14 | test_user@test.com      | Test Ticket | 32       |
| P5   | 1,2,3,5,7,9,10,12,13,14 | test_user@test.com      | Test Ticket | 5        |

# Test Plans for `buy_ticket`

For all test cases below, the following test data must be in the repository:

### Test data 
```
    User(
        email='penniless_user@test.com',
        name='penniless_user',
        password=generate_password_hash('Password!'),
        balance=0
	);

	User(
        email='test_user@test.com',
        name='test_user',
        password=generate_password_hash('Password!'),
        balance=5000
	);

	Ticket(
		owner = 'test_frontend@test.com',
		name = 'Test Ticket',
		quantity = '32',
		price = '20',
		date = '20210901'
	);
```

## Test case 1
Path: P1
Input:
	- email = `test_user@test.com`
	- name = `Fake Ticket`
	- quantity = `5`
Output: `Ticket does not exist`

## Test case 2
Path: P2
Input:
	- email = `test_user@test.com`
	- name = `Test Ticket`
	- quantity = `33`
Output: `Not enough tickets for sale`

## Test case 3
Path: P3
Input:
	- email = `penniless_user@test.com`
	- name = `Test Ticket`
	- quantity = `5`
Output: `Insufficient balance`

## Test case 4
Path: P4
Input:
	- email = `test_user@test.com`
	- name = `Test Ticket`
	- quantity = `32`
Output: None

## Test case 5
Path: P5
Input:
	- email = `test_user@test.com`
	- name = `Test Ticket`
	- quantity = `5`
Output: None