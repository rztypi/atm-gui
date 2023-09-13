import tkinter as tk

import fonts
from utils import widgets


class TwoFAWindow(tk.Toplevel):
    def __init__(self, app):
        tk.Toplevel.__init__(self)
        self.title("Two-Factor Authentication")
        self["background"] = "white"
        widgets.set_window_geometry(self, x=400, y=400)

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

            widgets.clear_entry_field(pin_entry)

            self.deiconify()

    def __open_atm_system(self, app):
        self.destroy()

        app.change_page_to("HomePage")

    def __pin_entry_validator(self, entry, input_text):
        limit = 4
        entry_under_limit = len(entry) <= limit
        if entry_under_limit:
            return input_text.isdigit()

        return False


window_list = [TwoFAWindow]
