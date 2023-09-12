from tkinter import messagebox


def username_is_valid(username):
    """Checks if username is not empty. Shows a messagebox if invalid."""
    if username:
        return True
    else:
        messagebox.showerror(
            "Form Error", "Username field must not be blank."
        )
        return False

def password_is_valid(password):
    """Checks if password is not empty. Shows a messagebox if invalid."""
    if password:
        return True
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
            "Form Error", "Phone number field must have a length of 13."
        )


__field_to_checker_func = {
    "username": username_is_valid,
    "password": password_is_valid,
    "phone_number": phone_number_is_valid,
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

        if not is_valid(value):
                return False

    return True