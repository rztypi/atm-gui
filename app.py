import tkinter as tk
from random import randint

import colors
from db.database import Database
from utils import widgets


DB_PATH = "db/test.db"


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

        widgets.set_window_geometry(self, x=720, y=720)

        self.db = db
        self.active_user = ""

        self.__twofa_pin = ""

        self.__last_withdraw_amount = 0
        self.__last_deposit_amount = 0

        self.__container = tk.Frame(self, bg=colors.secondary)
        self.__container.place(relwidth=1, relheight=1)
        self.__active_page = tk.Frame()
        self.change_page_to("LoginPage")

    def change_page_to(self, page_name):
        """Changes the currently active page of the GUI."""
        self.__active_page.destroy()

        Page = widgets.get_page(page_name)
        self.__active_page = Page(self.__container, self)

    def show_window(self, window_name):
        """Shows the toplevel window specified by the Window object."""
        Window = widgets.get_window(window_name)
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
    
    @property
    def last_deposit_amount(self):
        return self.__last_deposit_amount
    
    @last_deposit_amount.setter
    def last_deposit_amount(self, amount):
        self.__last_deposit_amount = int(amount)


if __name__ == "__main__":
    db = Database(DB_PATH)
    app = App(db)
    app.mainloop()
    db.close()