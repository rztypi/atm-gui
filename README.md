# atm-gui

![atm-gui](https://github.com/rztypi/atm-gui/assets/84902994/52a43198-4d13-45b4-948f-3b9ae98c65ae)

A simple ATM interface using Tkinter.

> *This project was built as a requirement for our Software Design class.*

**Features:**

- Login and registration forms with validators
- Account database using SQLite3
- Two-factor authentication
- Withdraw, deposit, and balance inquiry

## Setup

> *Note: Make sure you have the latest version of [Python 3](https://www.python.org/downloads/) installed.*

1. Clone/download this repository.
    ```
    git clone https://github.com/rztypi/atm-gui.git
    ```
1. Change directory to the repository and run `app.py`.
    ```
    python3 app.py
    ```

## Using the GUI

### Logging In

You can use the default account credentials to log in or [register a new account](#registration) on the app.
- Default username: **`username`**
- Default password: **`password`**


### Registration

The username is the unique identifier of each account. The username must:
- not be blank;
- contain only letters and numbers; and
- should not be taken by another account.

The password must:
- not be blank; and
- be at least 8 characters long.

The phone number must:
- be prefixed with the PH dialing code (+63); and
- be followed by 10 digits.

### Two-Factor Authentication

The 4-digit PIN is printed to the terminal. Alternatively, you may edit the `pages.py` file to skip two-factor authentication:
```py
# pages.py

SKIP_TWOFA = True
```

> *Originally, this project used Twilio with a free trial account to send the OTP to the user's phone number.*

### Inside the ATM System

Each user starts with a zero balance. To view the account balance, you may press the `Inquiry` button.

The `Withdraw` and `Deposit` buttons allow the user to subtract and add amounts to their balance. However, it will not allow any transaction which causes the balance to either go below zero or go above the limit of 100,000,000.

To log out and exit the system, press the `Exit` button. This will take you back to the login page.