from tkinter import Tk, Frame, Label, Entry, Button, W

import fonts
import register
import login


class GUI:
    def __init__(self, master):
        self.master = master
        master.title('ATM SYSTEM')
        master.iconbitmap('wwticon.ico')
        master['background'] = 'white'

        master_x = 720
        master_y = 720
        master_pos_right = int(master.winfo_screenwidth()/2 - master_x/2)
        master_pos_down = int(master.winfo_screenheight()/2 - master_y/2)
        master.geometry(f'{master_x}x{master_y}+{master_pos_right}+{master_pos_down}')

        self.frame = Frame(master, bg='black')
        self.window_label = Label(self.frame, text="ATM System Login", bg='black', fg='white', font=fonts.biggerFontBold)
        self.user_label = Label(self.frame, text="User Name: ", bg='black', fg='white', anchor=W, font=fonts.boldMainFont)
        self.pass_label = Label(self.frame, text="Password: ", bg='black', fg='white', anchor=W, font=fonts.boldMainFont)
        self.register_label = Label(self.frame, text="Don't have an account?", bg='black', fg='#bababa', font=fonts.sMainFont)
        self.user_main_entry = Entry(self.frame, font=fonts.mainFont)
        self.pass_main_entry = Entry(self.frame, font=fonts.mainFont)
        self.login_button = Button(self.frame, text="Login", font=fonts.boldMainFont)
        self.register_button = Button(self.frame, text="Register", font=fonts.boldMainFont, command=register.reg_window)
        self.login_button.config(command=lambda: login.verify_login(self.user_main_entry, self.pass_main_entry, root))

        self.frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
        self.window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)
        self.user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)
        self.user_main_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)
        self.pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)
        self.pass_main_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)
        self.login_button.place(relx=0.4, rely=0.47, relheight=0.08, relwidth=0.2)
        self.register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)
        self.register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)


root = Tk()
gui = GUI(root)
root.mainloop()