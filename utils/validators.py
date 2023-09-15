from tkinter import messagebox


def username_is_valid(username, is_registration=False):
    """Checks if username is not empty. Shows a messagebox if invalid."""
    if username:
        if not is_registration:
            return True

        if username.isalnum():
            return True
        else:
            messagebox.showerror(
                "Form Error", "Username must contain only letters and numbers."
            )
            return False
    else:
        messagebox.showerror(
            "Form Error", "Username field must not be blank."
        )
        return False

def password_is_valid(password, is_registration=False):
    """Checks if password is not empty. Shows a messagebox if invalid."""
    if password:
        if not is_registration:
            return True

        if len(password) >= 8:
            return True
        else:
            messagebox.showerror(
                "Form Error", "Password must have at least 8 characters."
            )
            return False
    else: 
        messagebox.showerror(
            "Form Error", "Password field must not be blank."
        )
        return False

def phone_number_is_valid(phone_number):
    """Checks if phone_number has a length of 13. Shows a messagebox if invalid."""
    if len(phone_number) == 13:
        return True
    else:
        messagebox.showerror(
            "Form Error", "Phone number field must have 12 digits."
        )
        return False

def amount_is_valid(amount):
    """Checks if amount is not empty. Shows a messagebox if invalid."""
    if amount:
        return True
    else:
        messagebox.showerror(
            "Form Error", "Amount field must not be empty."
        )
        return False


def withdraw_is_valid(withdraw_amount, balance):
    """Checks if withdraw_amount is less than or equal to balance."""
    if withdraw_amount <= balance:
        return True
    else:
        messagebox.showerror(
            "Withdraw Error", f"Insufficient balance. (₱{balance:,})"
        )

def deposit_is_valid(deposit_amount, balance):
    """Checks if deposit_amount + balance does not exceed the account limit."""
    LIMIT = 100_000_000
    if deposit_amount + balance <= LIMIT:
        return True
    else:
        messagebox.showerror(
            "Deposit Error", f"Balance exceeds the limit of ₱{LIMIT:,}."
        )


__field_to_checker_func = {
    "username": username_is_valid,
    "password": password_is_valid,
    "phone_number": phone_number_is_valid,
    "amount": amount_is_valid,
}

def form_is_valid(**kwargs):
    """Checks if field values specified are valid.

    Associates field names to their corresponsing checker function.

    Parameters:
        username (optional) (str): The username field.
        password (optional) (str): The password field.
        phone_number (optional) (str): The phone_number field.

    Returns:
        bool: True if form is valid, False if not.
    """
    for field, value in kwargs.items():
        is_valid = __field_to_checker_func[field]

        if isinstance(value, str):
            if not is_valid(value):
                return False
        else:
            if not is_valid(value[0], value[1]):
                return False

    return True