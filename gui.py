import tkinter as tk
from tkinter import messagebox
from random import randint

import fonts
import colors


SKIP_TWOFA = True


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


class WithdrawCompleteFrame(tk.Frame):
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

        withdraw_amount = app.get_last_withdraw_amount()
        withdraw_amount_label = tk.Label(
            self,
            text=f"₱{withdraw_amount:,}",
            bg="black",
            fg="#bababa",
            font=fonts.bigFontBold,
        )
        withdraw_amount_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        new_button = tk.Button(
            self,
            text="New Transaction",
            font=fonts.boldMainFont,
            command=lambda: app.change_frame_to(HomeFrame),
        )
        new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            font=fonts.boldMainFont,
            command=lambda: app.change_frame_to(LoginFrame),
        )
        exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


class WithdrawFrame(tk.Frame):
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
            command=lambda: app.change_frame_to(HomeFrame),
        )
        back_button.place(relx=0.4, rely=0.80, relheight=0.08, relwidth=0.2)

    def withdraw_button_handler(self, withdraw_entry, app):
        withdraw_amount = withdraw_entry.get()
        if withdraw_amount:
            app.set_last_withdraw_amount(int(withdraw_amount))

            app.change_frame_to(WithdrawCompleteFrame)
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


class HomeFrame(tk.Frame):
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
            command=lambda: app.change_frame_to(WithdrawFrame),
        )
        withdraw_button.place(relx=0.3, rely=0.55, relheight=0.08, relwidth=0.4)

        exit_button = tk.Button(
            self,
            text="Exit",
            font=fonts.boldMainFont,
            command=lambda: app.change_frame_to(LoginFrame),
        )
        exit_button.place(relx=0.3, rely=0.70, relheight=0.08, relwidth=0.4)


class RegisterFrame(tk.Frame):
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
            self, text="Register", font=fonts.boldMainFont2, command=self.bell
        )
        register_button.place(relx=0.4, rely=0.63, relheight=0.08, relwidth=0.2)

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


class TwoFAToplevel(tk.Toplevel):
    def __init__(self, app):
        tk.Toplevel.__init__(self)
        self.title("Two-Factor Authentication")
        self["background"] = "white"
        WidgetMethods.set_window_geometry(self, x=400, y=400)

        app.generate_twofa_pin()
        print(app.get_twofa_pin())

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

        vcmd = (self.register(self.__pin_entry_validator), "%d", "%s", "%S")
        pin_entry = tk.Entry(
            frame,
            justify=tk.CENTER,
            validate="key",
            validatecommand=vcmd,
            font=("Source Code Pro", 69, "bold"),
        )
        pin_entry.bind("<Key>", self.__unfocus_entry)
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

        if pin == app.get_twofa_pin():
            self.__open_atm_system(app)
        else:
            tk.messagebox.showerror("Verification Error", "PIN does not match.")

            WidgetMethods.clear_entry_field(pin_entry)

            self.deiconify()

    def __open_atm_system(self, app):
        self.destroy()

        app.change_frame_to(HomeFrame)

    def __pin_entry_validator(self, action, entry, character):
        action_is_delete = action == "0"
        input_is_digit = character.isdigit()

        limit = 4
        entry_under_limit = len(entry) < limit

        if action_is_delete or (input_is_digit and entry_under_limit):
            return True
        return False

    # WORKING ON THIS
    def __unfocus_entry(self, event):
        entry_length = len(event.widget.get())

        if event.keysym == "BackSpace":
            entry_length -= 1
        else:
            entry_length += 1

        if entry_length >= 4:
            self.focus()


class LoginFrame(tk.Frame):
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
            command=lambda: app.change_frame_to(RegisterFrame),
        )
        register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)

    def authenticate_login(self, user_entry, pass_entry, app):
        username = user_entry.get()
        password = pass_entry.get()

        WidgetMethods.clear_entry_field(user_entry)
        WidgetMethods.clear_entry_field(pass_entry)

        if self.__user_check(username) and self.__pass_check(password):
            if SKIP_TWOFA:
                app.change_frame_to(HomeFrame)
            else:
                self.__open_twofa_window(app)

    def __user_check(self, username):
        if not username:
            tk.messagebox.showerror(
                "Login Error", "You cannot leave your username blank."
            )
            return False
        return True

    def __pass_check(self, password):
        if not password:
            tk.messagebox.showerror(
                "Login Error", "You cannot leave your password blank."
            )
            return False
        return True

    def __open_twofa_window(self, app):
        TwoFAToplevel(app)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("ATM System")
        self["background"] = "white"

        WidgetMethods.set_window_geometry(self, x=720, y=720)

        self.container = tk.Frame(self, bg=colors.secondary)
        self.container.place(relwidth=1, relheight=1)
        self.active_frame = LoginFrame(self.container, self)

        self.__twofa_pin = ""

        self.__last_withdraw_amount = 0

    def change_frame_to(self, Frame):
        self.active_frame.destroy()
        self.active_frame = Frame(self.container, app)

    def generate_twofa_pin(self):
        def random_digit():
            return randint(0, 9)

        pin = f"{random_digit()}{random_digit()}{random_digit()}{random_digit()}"

        self.__twofa_pin = pin

    def get_twofa_pin(self):
        return self.__twofa_pin

    def set_last_withdraw_amount(self, amount):
        self.__last_withdraw_amount = amount

    def get_last_withdraw_amount(self):
        return self.__last_withdraw_amount


if __name__ == "__main__":
    app = App()
    app.mainloop()
