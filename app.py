import tkinter as tk
from tkinter import messagebox
from random import randint

import fonts
import colors
from db.database import Database
from utils.validators import form_is_valid


DB_PATH = "db/test.db"
SKIP_TWOFA = False


class WidgetMethods:
    @staticmethod
    def set_window_geometry(window, x, y):
        x_offset = int(window.winfo_screenwidth() / 2 - x / 2)
        y_offset = int(window.winfo_screenheight() / 2 - y / 2)

        geometry_string = f"{x}x{y}+{x_offset}+{y_offset}"
        window.geometry(geometry_string)

    @staticmethod
    def clear_entry_field(entry_field):
        entry_field.delete(0, tk.END)


class WithdrawCompletePage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Withdrawal",
            bg="black",
            fg="white",
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="You have successfully withdrawn:",
            bg="black",
            fg="#bababa",
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        withdraw_amount_label = tk.Label(
            self,
            text=f"₱{app.last_withdraw_amount:,}",
            bg="black",
            fg="#bababa",
            font=fonts.bigFontBold,
        )
        withdraw_amount_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        new_button = tk.Button(
            self,
            text="New Transaction",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(HomePage),
        )
        new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(LoginPage),
        )
        exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


class WithdrawPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Withdrawal",
            bg="black",
            fg="white",
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Enter withdraw amount:",
            bg="black",
            fg="#bababa",
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        vcmd = (self.register(self.__withdraw_entry_validator), "%i", "%P", "%S")
        withdraw_entry = tk.Entry(
            self, validate="key", validatecommand=vcmd, font=fonts.biggestFontBold
        )
        withdraw_entry.bind("<Key>", self.__move_icursor_to_end)
        withdraw_entry.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        withdraw_button = tk.Button(
            self,
            text="Withdraw",
            font=fonts.boldMainFont,
            command=lambda: self.withdraw_button_handler(withdraw_entry, app),
        )
        withdraw_button.place(relx=0.4, rely=0.65, relheight=0.08, relwidth=0.2)

        back_button = tk.Button(
            self,
            text="Back",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(HomePage),
        )
        back_button.place(relx=0.4, rely=0.80, relheight=0.08, relwidth=0.2)

    def withdraw_button_handler(self, withdraw_entry, app):
        withdraw_amount = withdraw_entry.get()
        if withdraw_amount:
            app.last_withdraw_amount = int(withdraw_amount)

            app.change_page_to(WithdrawCompletePage)
        else:
            tk.messagebox.showerror("Withdraw Error", "Field must not be empty.")

    def __withdraw_entry_validator(self, index, entry, input_text):
        input_is_many = len(input_text) > 1
        first_char_is_zero = (index == "0" and input_text == "0") or entry[:1] == "0"
        if input_is_many or first_char_is_zero:
            return False

        return input_text.isdigit()

    def __move_icursor_to_end(self, event):
        event.widget.icursor(tk.END)


class HomePage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self, text="ATM System", bg="black", fg="white", font=fonts.biggerFontBold
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Choose your transaction.",
            bg="black",
            fg="#bababa",
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        withdraw_button = tk.Button(
            self,
            text="Withdraw",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(WithdrawPage),
        )
        withdraw_button.place(relx=0.3, rely=0.55, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(LoginPage),
        )
        exit_button.place(relx=0.3, rely=0.70, relheight=0.08, relwidth=0.4)


class RegisterPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Registration Form",
            bg="black",
            fg="white",
            font=fonts.bigFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        user_label = tk.Label(
            self,
            text="User Name: ",
            bg="black",
            fg="white",
            anchor=tk.W,
            font=fonts.boldMainFont2,
        )
        user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)

        pass_label = tk.Label(
            self,
            text="Password: ",
            bg="black",
            fg="white",
            anchor=tk.W,
            font=fonts.boldMainFont2,
        )
        pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)

        phone_label = tk.Label(
            self,
            text="Phone Number: ",
            bg="black",
            fg="white",
            anchor=tk.W,
            font=fonts.boldMainFont2,
        )
        phone_label.place(relx=0.02, rely=0.44, relheight=0.05, relwidth=0.3)

        user_entry = tk.Entry(self, font=fonts.mainFont2)
        user_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)

        pass_entry = tk.Entry(self, show="*", font=fonts.mainFont2)
        pass_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)

        vcmd = (self.register(self.__phone_entry_validator), "%d", "%i", "%P", "%S")
        phone_entry = tk.Entry(
            self, validate="key", validatecommand=vcmd, font=fonts.mainFont2
        )
        phone_entry.place(relx=0.1, rely=0.50, relheight=0.05, relwidth=0.8)
        phone_entry.insert(0, "+63")

        phone_ghostlabel = tk.Label(
            self,
            text="Format: +63**********",
            bg="black",
            fg="#bababa",
            anchor=tk.W,
            font=fonts.sMainFont2,
        )
        phone_ghostlabel.place(relx=0.1, rely=0.56, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(
            self,
            text="Register",
            font=fonts.boldMainFont2,
            command=lambda: self.register_button_click(
                user_entry, pass_entry, phone_entry
            ),
        )
        register_button.place(relx=0.4, rely=0.63, relheight=0.08, relwidth=0.2)

        back_button = tk.Button(
            self,
            text="Back",
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to(LoginPage),
        )
        back_button.place(relx=0.4, rely=0.8, relheight=0.08, relwidth=0.2)

    def register_button_click(self, user_entry, pass_entry, phone_entry):
        username = user_entry.get()
        password = pass_entry.get()
        phone_number = phone_entry.get()

        if form_is_valid(
            username=username,
            password=password,
            phone_number=phone_number,
        ):
            if app.db.register_account(username, password, phone_number):
                print("Registration success!")
            else:
                print("Registration failed.")

    @staticmethod
    def __user_check(username):
        if username:
            return True
        else:
            tk.messagebox.showerror(
                "Login Error", "You cannot leave the username blank."
            )

    def __phone_entry_validator(self, action, index, entry, input_text):
        limit = 13
        entry_under_limit = len(entry) <= limit
        if entry_under_limit:
            inserting_prefix = index == "0" and input_text == "+63" and action == "1"
            if inserting_prefix:
                return True

            overwriting_prefix = int(index) < 3
            if overwriting_prefix:
                return False

            return input_text.isdigit()

        return False


class TwoFAWindow(tk.Toplevel):
    def __init__(self, app):
        tk.Toplevel.__init__(self)
        self.title("Two-Factor Authentication")
        self["background"] = "white"
        WidgetMethods.set_window_geometry(self, x=400, y=400)

        app.generate_twofa_pin()
        print(app.twofa_pin)

        frame = tk.Frame(self, bg="black")
        frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            frame, text="Verify Code", bg="black", fg="white", font=fonts.bigFontBold
        )
        window_label.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            frame,
            text="Enter the 4-digit code\nwe sent to your phone number.",
            bg="black",
            fg="#bababa",
            font=fonts.sMainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        vcmd = (self.register(self.__pin_entry_validator), "%P", "%S")
        pin_entry = tk.Entry(
            frame,
            justify=tk.CENTER,
            validate="key",
            validatecommand=vcmd,
            font=("Source Code Pro", 69, "bold"),
        )
        pin_entry.place(relx=0.1, rely=0.4, relheight=0.25, relwidth=0.8)

        verify_button = tk.Button(
            frame,
            text="Verify",
            font=fonts.boldMainFont,
            command=lambda: self.authenticate_twofa(pin_entry, app),
        )
        verify_button.place(relx=0.3, rely=0.75, relheight=0.1, relwidth=0.4)

    def authenticate_twofa(self, pin_entry, app):
        pin = pin_entry.get()

        if pin == app.twofa_pin:
            self.__open_atm_system(app)
        else:
            tk.messagebox.showerror("Verification Error", "PIN does not match.")

            WidgetMethods.clear_entry_field(pin_entry)

            self.deiconify()

    def __open_atm_system(self, app):
        self.destroy()

        app.change_page_to(HomePage)

    def __pin_entry_validator(self, entry, input_text):
        limit = 4
        entry_under_limit = len(entry) <= limit
        if entry_under_limit:
            return input_text.isdigit()

        return False


class LoginPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="ATM System Login",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        user_label = tk.Label(
            self,
            text="User Name: ",
            bg=colors.primary,
            fg=colors.font_primary,
            anchor=tk.W,
            font=fonts.boldMainFont,
        )
        user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)

        pass_label = tk.Label(
            self,
            text="Password: ",
            bg=colors.primary,
            fg=colors.font_primary,
            anchor=tk.W,
            font=fonts.boldMainFont,
        )
        pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)

        user_entry = tk.Entry(self, font=fonts.mainFont)
        user_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)

        pass_entry = tk.Entry(self, show="*", font=fonts.mainFont)
        pass_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)

        login_button = tk.Button(
            self,
            text="Login",
            font=fonts.boldMainFont,
            command=lambda: self.authenticate_login(user_entry, pass_entry, app),
        )
        login_button.place(relx=0.4, rely=0.47, relheight=0.08, relwidth=0.2)

        register_label = tk.Label(
            self,
            text="Don't have an account?",
            bg=colors.primary,
            fg="#bababa",
            font=fonts.sMainFont,
        )
        register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(
            self,
            text="Register",
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to(RegisterPage),
        )
        register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)

    def authenticate_login(self, user_entry, pass_entry, app):
        username = user_entry.get()
        password = pass_entry.get()

        WidgetMethods.clear_entry_field(user_entry)
        WidgetMethods.clear_entry_field(pass_entry)

        if form_is_valid(username=username, password=password):
            if app.db.login_account(username, password):
                app.active_user = username

                if SKIP_TWOFA:
                    app.change_page_to(HomePage)
                else:
                    self.__open_twofa_window(app)
            else:
                tk.messagebox.showerror(
                    "Login Error", "Username and password not found."
                )

    def __open_twofa_window(self, app):
        app.show_window(TwoFAWindow)


class App(tk.Tk):
    """The root Tk window of the GUI.

    Attributes:
        db (gui.Database): A database class of the app.
        active_user (str): The username of the currently logged in user.
        twofa_pin (str): A 4-digit PIN generated for two-factor authentication.
        last_withdraw_amount (int): The withdraw amount displayed when withdraw is done.
        __active_page (tk.Frame): The currently displayed page of the GUI.
        __container (tk.Frame): The container of __active_page.
    """

    def __init__(self, db):
        """Initializes the App class and its attributes.

        Parameters:
            db (db.database.Database): The local database class of the GUI.
        """
        tk.Tk.__init__(self)
        self.title("ATM System")
        self["background"] = "white"

        WidgetMethods.set_window_geometry(self, x=720, y=720)

        self.db = db
        self.active_user = ""

        self.__twofa_pin = ""
        self.__last_withdraw_amount = 0

        self.__container = tk.Frame(self, bg=colors.secondary)
        self.__container.place(relwidth=1, relheight=1)
        self.__active_page = LoginPage(self.__container, self)

    def change_page_to(self, Page):
        """Changes the currently active page of the GUI."""
        self.__active_page.destroy()
        self.__active_page = Page(self.__container, self)
    
    def show_window(self, Window):
        """Shows the toplevel window specified by the Window object."""
        Window(self)

    def generate_twofa_pin(self):
        """Generates and sets a random 4-digit pin for the twofa_pin attribute."""

        def random_digit():
            return randint(0, 9)

        pin = f"{random_digit()}{random_digit()}{random_digit()}{random_digit()}"

        self.__twofa_pin = pin

    @property
    def twofa_pin(self):
        return self.__twofa_pin

    @property
    def last_withdraw_amount(self):
        return self.__last_withdraw_amount

    @last_withdraw_amount.setter
    def last_withdraw_amount(self, amount):
        self.__last_withdraw_amount = int(amount)


if __name__ == "__main__":
    db = Database(DB_PATH)
    app = App(db)
    app.mainloop()
    db.close()
