from tkinter import *
from tkinter import messagebox
import twofa
import sqlite3


def user_check(user_input):
    if user_input == "":
        is_valid = False
        messagebox.showerror("Login Error", "You cannot leave your user name blank.")
    else:
        is_valid = True
    return is_valid


def pass_check(pass_input):
    if pass_input == "":
        is_valid = False
        messagebox.showerror("Login Error", "You cannot leave your password blank.")
    else:
        is_valid = True
    return is_valid


def match_check(user_input, pass_input):
    is_valid = False

    # Check if user exists
    conn = sqlite3.connect('loginfo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loginfos WHERE user_name=?;", [user_input])

    # Check if password matches
    try:
        user_name = cursor.fetchall()[0][1]
        if user_name == pass_input:
            is_valid = True
        else:
            messagebox.showerror("Login Error", "User name and password do not match.")
    except IndexError:
        messagebox.showerror("Login Error", "User not found.")

    conn.close()
    return is_valid


def verify_login(user_main_entry, pass_main_entry, root):
    user_input = user_main_entry.get()
    pass_input = pass_main_entry.get()
    user_main_entry.delete(0, END)
    pass_main_entry.delete(0, END)
    if user_check(user_input):
        if pass_check(pass_input):
            if match_check(user_input, pass_input):
                twofa.twofa_window(user_input, root)
