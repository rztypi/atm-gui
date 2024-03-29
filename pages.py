import tkinter as tk
from tkinter import messagebox

import fonts
import colors
from utils import widgets
from utils.validators import form_is_valid, withdraw_is_valid, deposit_is_valid


SKIP_TWOFA = False


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
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont,
            command=lambda: self.authenticate_login(user_entry, pass_entry, app),
        )
        login_button.place(relx=0.35, rely=0.47, relheight=0.08, relwidth=0.3)

        register_label = tk.Label(
            self,
            text="Don't have an account?",
            bg=colors.primary,
            fg=colors.font_secondary,
            font=fonts.sMainFont,
        )
        register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(
            self,
            text="Register",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont,
            command=lambda: app.change_page_to("RegisterPage"),
        )
        register_button.place(relx=0.35, rely=0.85, relheight=0.08, relwidth=0.3)

    def authenticate_login(self, user_entry, pass_entry, app):
        username = user_entry.get()
        password = pass_entry.get()

        widgets.clear_entry_field(user_entry)
        widgets.clear_entry_field(pass_entry)

        if form_is_valid(username=username, password=password):
            if app.db.login_account(username, password):
                app.active_user = username
                app.active_user_balance = app.db.get_account_balance(username)

                if SKIP_TWOFA:
                    app.change_page_to("HomePage")
                else:
                    app.show_window("TwoFAWindow")
            else:
                tk.messagebox.showerror(
                    "Login Error", "Username and password not found."
                )


class RegisterPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Registration Form",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.bigFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        user_label = tk.Label(
            self,
            text="User Name: ",
            bg=colors.primary,
            fg=colors.font_primary,
            anchor=tk.W,
            font=fonts.boldMainFont2,
        )
        user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)

        pass_label = tk.Label(
            self,
            text="Password: ",
            bg=colors.primary,
            fg=colors.font_primary,
            anchor=tk.W,
            font=fonts.boldMainFont2,
        )
        pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)

        phone_label = tk.Label(
            self,
            text="Phone Number: ",
            bg=colors.primary,
            fg=colors.font_primary,
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
            bg=colors.primary,
            fg=colors.font_secondary,
            anchor=tk.W,
            font=fonts.sMainFont2,
        )
        phone_ghostlabel.place(relx=0.1, rely=0.56, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(
            self,
            text="Register",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: self.register_button_click(
                user_entry, pass_entry, phone_entry, app
            ),
        )
        register_button.place(relx=0.35, rely=0.63, relheight=0.08, relwidth=0.3)

        back_button = tk.Button(
            self,
            text="Back",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("LoginPage"),
        )
        back_button.place(relx=0.35, rely=0.8, relheight=0.08, relwidth=0.3)

    def register_button_click(self, user_entry, pass_entry, phone_entry, app):
        username = user_entry.get()
        password = pass_entry.get()
        phone_number = phone_entry.get()

        if form_is_valid(
            username=(username, True),
            password=(password, True),
            phone_number=phone_number,
        ):
            if app.db.register_account(username, password, phone_number):
                tk.messagebox.showinfo(
                    "Registration", "Registration successful."
                )
            else:
                tk.messagebox.showerror(
                    "Registration Error", "Username is already taken."
                )
            
            widgets.clear_entry_field(user_entry)
            widgets.clear_entry_field(pass_entry)
            widgets.clear_entry_field(phone_entry, start=3)

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


class HomePage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self, text="ATM System",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Choose your transaction.",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        withdraw_button = tk.Button(
            self,
            text="Withdraw",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("WithdrawPage"),
        )
        withdraw_button.place(relx=0.1, rely=0.55, relheight=0.08, relwidth=0.35)

        deposit_button = tk.Button(
            self,
            text="Deposit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("DepositPage"),
        )
        deposit_button.place(relx=0.55, rely=0.55, relheight=0.08, relwidth=0.35)

        inquiry_button = tk.Button(
            self,
            text="Inquiry",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("InquiryPage"),
        )
        inquiry_button.place(relx=0.1, rely=0.7, relheight=0.08, relwidth=0.35)

        exit_button = tk.Button(
            self,
            text="Exit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("LoginPage"),
        )
        exit_button.place(relx=0.55, rely=0.7, relheight=0.08, relwidth=0.35)


class WithdrawPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Withdrawal",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Enter withdraw amount:",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        vcmd = (self.register(self.__withdraw_entry_validator), "%P", "%S")
        withdraw_entry = tk.Entry(
            self, validate="key", validatecommand=vcmd, font=fonts.biggestFontBold
        )
        withdraw_entry.bind("<Key>", self.__move_icursor_to_end)
        withdraw_entry.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        withdraw_button = tk.Button(
            self,
            text="Withdraw",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: self.withdraw_button_click(withdraw_entry, app),
        )
        withdraw_button.place(relx=0.35, rely=0.65, relheight=0.08, relwidth=0.3)

        back_button = tk.Button(
            self,
            text="Back",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("HomePage"),
        )
        back_button.place(relx=0.35, rely=0.80, relheight=0.08, relwidth=0.3)

    def withdraw_button_click(self, withdraw_entry, app):
        withdraw_amount = withdraw_entry.get()
        widgets.clear_entry_field(withdraw_entry)

        if form_is_valid(amount=withdraw_amount):
            withdraw_amount = int(withdraw_amount)

            if withdraw_is_valid(withdraw_amount, app.active_user_balance):
                app.last_withdraw_amount = withdraw_amount
                app.active_user_balance -= withdraw_amount

                app.db.set_account_balance(app.active_user, app.active_user_balance)

                app.change_page_to("WithdrawCompletePage")

    def __withdraw_entry_validator(self, entry, input_text):
        first_char_is_zero = entry[:1] == "0"
        if first_char_is_zero:
            return False

        return input_text.isdigit()

    def __move_icursor_to_end(self, event):
        event.widget.icursor(tk.END)


class WithdrawCompletePage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Withdrawal",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="You have successfully withdrawn:",
            bg=colors.primary,
            fg=colors.font_secondary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        withdraw_amount_label = tk.Label(
            self,
            text=f"₱{app.last_withdraw_amount:,.2f}",
            bg=colors.white,
            fg=colors.black,
            font=fonts.bigFontBold,
        )
        withdraw_amount_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        new_button = tk.Button(
            self,
            text="New Transaction",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("HomePage"),
        )
        new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("LoginPage"),
        )
        exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


class DepositPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Deposit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Enter deposit amount:",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        vcmd = (self.register(self.__deposit_entry_validator), "%P", "%S")
        deposit_entry = tk.Entry(
            self, validate="key", validatecommand=vcmd, font=fonts.biggestFontBold
        )
        deposit_entry.bind("<Key>", self.__move_icursor_to_end)
        deposit_entry.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        deposit_button = tk.Button(
            self,
            text="Deposit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: self.deposit_button_click(deposit_entry, app),
        )
        deposit_button.place(relx=0.35, rely=0.65, relheight=0.08, relwidth=0.3)

        back_button = tk.Button(
            self,
            text="Back",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("HomePage"),
        )
        back_button.place(relx=0.35, rely=0.80, relheight=0.08, relwidth=0.3)

    def deposit_button_click(self, deposit_entry, app):
        deposit_amount = deposit_entry.get()
        widgets.clear_entry_field(deposit_entry)

        if form_is_valid(amount=deposit_amount):
            deposit_amount = int(deposit_amount)

            if deposit_is_valid(deposit_amount, app.active_user_balance):
                app.last_deposit_amount = deposit_amount
                app.active_user_balance += deposit_amount

                app.db.set_account_balance(app.active_user, app.active_user_balance)

                app.change_page_to("DepositCompletePage")

    def __deposit_entry_validator(self, entry, input_text):
        first_char_is_zero = entry[:1] == "0"
        if first_char_is_zero:
            return False

        return input_text.isdigit()

    def __move_icursor_to_end(self, event):
        event.widget.icursor(tk.END)


class DepositCompletePage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Cash Deposit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="You have successfully deposited:",
            bg=colors.primary,
            fg=colors.font_secondary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        deposit_amount_label = tk.Label(
            self,
            text=f"₱{app.last_deposit_amount:,.2f}",
            bg=colors.white,
            fg=colors.black,
            font=fonts.bigFontBold,
        )
        deposit_amount_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        new_button = tk.Button(
            self,
            text="New Transaction",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("HomePage"),
        )
        new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("LoginPage"),
        )
        exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


class InquiryPage(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=colors.primary)
        self.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(
            self,
            text="Balance Inquiry",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.biggerFontBold,
        )
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        window_desc = tk.Label(
            self,
            text="Your current balance is:",
            bg=colors.primary,
            fg=colors.font_secondary,
            font=fonts.mainFont,
        )
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        balance_label = tk.Label(
            self,
            text=f"₱{app.active_user_balance:,.2f}",
            bg=colors.white,
            fg=colors.black,
            font=fonts.bigFontBold,
        )
        balance_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        new_button = tk.Button(
            self,
            text="New Transaction",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("HomePage"),
        )
        new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            bg=colors.primary,
            fg=colors.font_primary,
            font=fonts.boldMainFont2,
            command=lambda: app.change_page_to("LoginPage"),
        )
        exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


page_list = [
    LoginPage,
    RegisterPage,
    HomePage,
    WithdrawPage,
    WithdrawCompletePage,
    DepositPage,
    DepositCompletePage,
    InquiryPage,
]
