from tkinter import *
from tkinter import messagebox

# Initialize font variables
boldMainFont = ('Source Code Pro', 14, 'bold')
mainFont = ('Source Code Pro', 14)
sMainFont = ('Source Code Pro', 9)
boldMainFont2 = ('Source Code Pro', 12, 'bold')
mainFont2 = ('Source Code Pro', 12)
sMainFont2 = ('Source Code Pro', 8)


def done_to_main(widget_list, window_set, done_win):
    # Unpack parameter "window_set"
    atm_win = window_set[2]

    # Forget withdraw screen widgets
    for widget in widget_list:
        widget.place_forget()

    done_win.destroy()
    atm_win.deiconify()
    open_main_screen(window_set)


def done_to_login(windows, done_win):
    root, atm_win = windows
    done_win.destroy()
    atm_win.destroy()
    root.deiconify()


def main_to_login(windows):
    root, atm_win = windows
    root.deiconify()
    atm_win.destroy()


def main_withdraw(widget_list, screen, window_set):
    # Forget existing widget
    for widget in widget_list:
        widget.place_forget()

    # Route to screen
    if screen == 'main':
        open_main_screen(window_set)
    elif screen == 'wdraw':
        open_withdraw_screen(window_set)
    else:
        print("There is an error.")


def open_done_screen(amount_input, widget_list, window_set):
    # Unpack parameter "windows"
    windows = window_set[1:]

    # Initialize done window
    done_win = Toplevel()
    done_win.title("Withdraw Successful")
    done_win.iconbitmap('wwticon.ico')
    done_win.geometry('600x600')
    done_win['background'] = 'white'

    # Set window size and center
    x = 600
    y = 600
    pos_right = int(done_win.winfo_screenwidth() / 2 - x / 2)
    pos_down = int(done_win.winfo_screenheight() / 2 - y / 2)
    done_win.geometry(f'{x}x{y}+{pos_right}+{pos_down}')

    # Initialize and place frame
    frame2 = Frame(done_win, bg='black')
    frame2.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Initialize done screen widgets
    window_label = Label(frame2, text="Withdraw Successful", bg='black', fg='white', font=('Source Code Pro', 20, 'bold'))
    window_desc = Label(frame2, text="Successfully withdrawn an amount of:", bg='black', fg='#bababa', font=sMainFont2)
    wdraw_amt_label = Label(frame2, text=f"₱{amount_input:,}", bg='black', fg='white', font=('Source Code Pro', 20, 'bold'))
    new_button = Button(frame2, text="New Transaction", font=boldMainFont)
    exit_button = Button(frame2, text="Exit Transaction", font=boldMainFont)

    # Configure withdraw and done buttons
    new_button.config(command=lambda: done_to_main(widget_list, window_set, done_win))
    exit_button.config(command=lambda: done_to_login(windows, done_win))

    # Place done screen widgets
    window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)
    window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)
    wdraw_amt_label.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)
    new_button.place(relx=0.3, rely=0.65, relheight=0.08, relwidth=0.4)
    exit_button.place(relx=0.3, rely=0.80, relheight=0.08, relwidth=0.4)


def withdraw(amount_input, widget_list, window_set):
    try:
        if int(amount_input) > 0:
            print(f"Withdrawn an amount of ₱{int(amount_input):,}")
            open_done_screen(int(amount_input), widget_list, window_set)
        else:
            messagebox.showerror("Withdraw Error", "Minimum withdraw amount is ₱1.00")
    except ValueError:
        messagebox.showerror("Withdraw Error", "Please enter whole numbers.")


def open_withdraw_screen(window_set):
    # Unpack parameters
    frame1 = window_set[0]

    # Initialize withdraw widgets
    window_label = Label(frame1, text="Withdraw", bg='black', fg='white', font=('Source Code Pro', 24, 'bold'))
    window_desc = Label(frame1, text="Enter withdraw amount:", bg='black', fg='#bababa', font=mainFont)
    wdraw_entry = Entry(frame1, font=('Source Code Pro', 50, 'bold'))
    wdraw_button = Button(frame1, text="Withdraw", font=boldMainFont)
    back_button = Button(frame1, text="Back", font=boldMainFont)

    # Config wdraw and back buttons
    widget_list = (window_label, window_desc, wdraw_entry, wdraw_button, back_button)
    wdraw_button.config(command=lambda: withdraw(wdraw_entry.get(), widget_list, window_set))
    back_button.config(command=lambda: main_withdraw(widget_list, 'main', window_set))

    # Place withdraw widgets
    window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)
    window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)
    wdraw_entry.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)
    wdraw_button.place(relx=0.4, rely=0.65, relheight=0.08, relwidth=0.2)
    back_button.place(relx=0.4, rely=0.80, relheight=0.08, relwidth=0.2)


def open_main_screen(window_set):
    # Unpack parameters
    frame1 = window_set[0]
    windows = window_set[1:]

    # Initialize ATM widgets
    window_label = Label(frame1, text="ATM System", bg='black', fg='white', font=('Source Code Pro', 24, 'bold'))
    window_desc = Label(frame1, text="Choose your transaction.", bg='black', fg='#bababa', font=mainFont)
    wdraw_button = Button(frame1, text="Withdraw", font=boldMainFont)
    exit_button = Button(frame1, text="Exit", font=boldMainFont)

    # Configure buttons
    widget_list = (window_label, window_desc, wdraw_button, exit_button)
    wdraw_button.config(command=lambda: main_withdraw(widget_list, 'wdraw', window_set))
    exit_button.config(command=lambda: main_to_login(windows))

    # Place ATM widgets
    window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)
    window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)
    wdraw_button.place(relx=0.3, rely=0.55, relheight=0.08, relwidth=0.4)
    exit_button.place(relx=0.3, rely=0.70, relheight=0.08, relwidth=0.4)


def open_atm_window(root):
    # Initialize ATM window
    atm_win = Toplevel()
    atm_win.title("ATM Window")
    atm_win.iconbitmap('wwticon.ico')
    atm_win['background'] = 'white'

    # Set window size and center
    x = 720
    y = 720
    pos_right = int(atm_win.winfo_screenwidth() / 2 - x / 2)
    pos_down = int(atm_win.winfo_screenheight() / 2 - y / 2)
    atm_win.geometry(f'{x}x{y}+{pos_right}+{pos_down}')

    # Minimize login window
    root.iconify()

    # Initialize and place frame
    frame1 = Frame(atm_win, bg='black')
    frame1.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Open the main screen
    window_set = (frame1, root, atm_win)
    open_main_screen(window_set)
