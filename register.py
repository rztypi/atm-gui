from tkinter import *
from tkinter import messagebox
import sqlite3

import fonts


def user_check(user_input, reg_win):
    is_valid = False

    # Checking if user name is taken
    same_name = False
    conn = sqlite3.connect("loginfo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loginfos")
    usernames = cursor.fetchall()
    for name in usernames:
        if name[0] == user_input:
            same_name = True
            break
        else:
            same_name = False

    # User name validation
    if user_input == "":
        messagebox.showerror("Registration Error", "You cannot leave your user name blank.")
    elif same_name:
        messagebox.showerror("Registration Error", "Your user name is already in use.")
    else:
        is_valid = True

    conn.close()
    reg_win.deiconify()
    return is_valid


def pass_check(pass_input, reg_win):
    # Password validation
    if pass_input == "":
        is_valid = False
        messagebox.showerror("Registration Error", "You cannot leave your password blank.")
    else:
        is_valid = True

    reg_win.deiconify()
    return is_valid


def phone_check(phone_input, reg_win):
    is_valid = False

    # Check if there are invalid characters
    wrong_char = False
    phone_no = phone_input
    for digit in phone_no.removeprefix("+"):
        if digit not in "0123456789":
            wrong_char = True
            break

    # Phone validation
    if phone_no == "":
        messagebox.showerror("Registration Error", "You cannot leave your phone number blank.")
    elif phone_no[0:3] != '+63':
        messagebox.showerror("Registration Error", "Phone number should start with '+63'.")
    elif wrong_char:
        messagebox.showerror("Registration Error",
                             "Phone number should contain numbers only.\n\n(Excluding prefix '+')")
    elif len(phone_no.removeprefix("+")) != 12:
        messagebox.showerror("Registration Error", "Phone number should have 12 digits.")
    else:
        is_valid = True

    reg_win.deiconify()
    return is_valid


def register(user_input, pass_input, phone_input, reg_win):
    if user_check(user_input, reg_win):
        if pass_check(pass_input, reg_win):
            if phone_check(phone_input, reg_win):
                conn = sqlite3.connect('loginfo.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO loginfos VALUES (:user_name, :password, :phone)",
                               {
                                    'user_name': user_input,
                                    'password': pass_input,
                                    'phone': phone_input
                               })
                conn.commit()
                conn.close()
                messagebox.showinfo("Registration Successful", "Successfully registered.")
                reg_win.destroy()


def reg_window():
    # Initialize registration window
    reg_win = Toplevel()
    reg_win.title("Registration")
    reg_win.iconbitmap('wwticon.ico')
    reg_win['background'] = 'white'

    # Set window size and center
    x = 600
    y = 600
    pos_right = int(reg_win.winfo_screenwidth() / 2 - x / 2)
    pos_down = int(reg_win.winfo_screenheight() / 2 - y / 2)
    reg_win.geometry(f'{x}x{y}+{pos_right}+{pos_down}')

    # Initialize registration window widgets
    frame1 = Frame(reg_win, bg='black')
    frame1.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    window_label = Label(frame1, text="Registration Form", bg='black', fg='white', font=fonts.bigFontBold)
    user_label = Label(frame1, text="User Name: ", bg='black', fg='white', anchor=W, font=fonts.boldMainFont2)
    pass_label = Label(frame1, text="Password: ", bg='black', fg='white', anchor=W, font=fonts.boldMainFont2)
    phone_label = Label(frame1, text="Phone Number: ", bg='black', fg='white', anchor=W, font=fonts.boldMainFont2)
    user_reg_entry = Entry(frame1, font=fonts.mainFont2)
    pass_reg_entry = Entry(frame1, font=fonts.mainFont2)
    phone_reg_entry = Entry(frame1, font=fonts.mainFont2)
    phone_ghostlabel = Label(frame1, text="Format: +63**********", bg='black', fg='#bababa', anchor=W, font=fonts.sMainFont2)
    register_param = lambda: register(user_reg_entry.get(), pass_reg_entry.get(), phone_reg_entry.get(), reg_win)
    register_button = Button(frame1, text="Register", font=fonts.boldMainFont2, command=register_param)

    # Place registration window widgets
    window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)
    user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)
    user_reg_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)
    pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)
    pass_reg_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)
    phone_label.place(relx=0.02, rely=0.44, relheight=0.05, relwidth=0.3)
    phone_reg_entry.place(relx=0.1, rely=0.50, relheight=0.05, relwidth=0.8)
    phone_reg_entry.insert(0, "+63")
    phone_ghostlabel.place(relx=0.1, rely=0.56, relheight=0.02, relwidth=0.8)
    register_button.place(relx=0.4, rely=0.63, relheight=0.08, relwidth=0.2)
