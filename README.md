# atm-gui

![atm-gui](https://github.com/rztypi/atm-gui/assets/84902994/52a43198-4d13-45b4-948f-3b9ae98c65ae)

A simple ATM interface using Tkinter.[^1]

**Features:**

- Login and registration forms with validators
- Account database using SQLite3
- Two-factor authentication[^2]
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

You can use the default account credentials to log in or register a new account on the app.
- Default username: `username`
- Default password: `password`

### Two-Factor Authentication

The 4-digit PIN is printed to the terminal. Alternatively, you may edit the `pages.py` file to skip two-factor authentication:
```py
# pages.py

SKIP_TWOFA = True
```


[^1]: This project was created as a requirement to our Software Design class.
[^2]: A Twilio trial account was previously used for academic submission purposes. PIN is now printed to the terminal.
