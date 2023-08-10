from tkinter import Toplevel, Frame, Label, Entry, Button, END
from tkinter import messagebox
# from twilio.rest import Client
from random import randint
import atm
import sqlite3

# Initialize font variables
boldMainFont = ('Source Code Pro', 12, 'bold')
mainFont = ('Source Code Pro', 12)
sMainFont = ('Source Code Pro', 8)


def find_phone(user_input):
    conn = sqlite3.connect('loginfo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loginfos WHERE user_name = ?;", [user_input])
    return cursor.fetchall()[0][2]


def verify(code_entry, veri_code, root, twofa_win):
    code_input = code_entry.get()
    if code_input == veri_code:
        twofa_win.destroy()
        atm.open_atm_window(root)
    else:
        messagebox.showerror("Verification Error", "Code does not match.")
        code_entry.delete(0, END)
        twofa_win.deiconify()


# def send_message(veri_code, user_input):
#     client = Client('AC33a5bc5d1a8a65268a57422317da1658', '34c5ffe51d7114fc7fc5734f87cf334c')
#     client.messages \
#         .create(
#              body=f"Your verification code is {veri_code}",
#              from_='+12548480405',
#              to=find_phone(user_input)
#          )


def twofa_window(user_input, root):
    # Initialize and send verification code to phone
    veri_code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
    print(veri_code) #TESTING LINE, REMOVE THIS
    #send_message(veri_code, user_input)

    # Initialize window
    twofa_win = Toplevel()
    twofa_win.title("Two-Factor Authentication")
    twofa_win.iconbitmap('wwticon.ico')
    twofa_win['background'] = 'white'

    # Set window size and center
    x = 400
    y = 400
    pos_right = int(twofa_win.winfo_screenwidth() / 2 - x / 2)
    pos_down = int(twofa_win.winfo_screenheight() / 2 - y / 2)
    twofa_win.geometry(f'{x}x{y}+{pos_right}+{pos_down}')

    # Initialize twofa widgets
    frame1 = Frame(twofa_win, bg='black')
    frame1.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    window_label = Label(frame1, text="Verify Code", bg='black', fg='white', font=('Source Code Pro', 18, 'bold'))
    window_desc = Label(frame1, text="Enter the 4-digit code\nwe sent to your phone number.",
                        bg='black', fg='#bababa', font=sMainFont)
    code_entry = Entry(frame1, font=('Source Code Pro', 79, 'bold'))
    verify_button = Button(frame1, text="Verify", font=boldMainFont, command=lambda: verify(code_entry, veri_code, root, twofa_win))

    # Place twofa widgets
    window_label.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)
    window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)
    code_entry.place(relx=0.1, rely=0.4, relheight=0.25, relwidth=0.8)
    verify_button.place(relx=0.3, rely=0.75, relheight=0.1, relwidth=0.4)
