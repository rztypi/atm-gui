import tkinter as tk

import fonts
import login
import register


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        self.place(relheight=1, relwidth=1)

        window_label = tk.Label(self, text='ATM System Login', bg='black', fg='white', font=fonts.biggerFontBold)
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

        user_label = tk.Label(self, text='User Name: ', bg='black', fg='white', anchor=tk.W, font=fonts.boldMainFont)
        user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)

        pass_label = tk.Label(self, text='Password: ', bg='black', fg='white', anchor=tk.W, font=fonts.boldMainFont)
        pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)
        
        user_entry = tk.Entry(self, font=fonts.mainFont)
        user_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)

        pass_entry = tk.Entry(self, font=fonts.mainFont)
        pass_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)

        login_button = tk.Button(self, text='Login', font=fonts.boldMainFont)
        login_button.config(command=lambda: self.authenticate(user_entry, pass_entry, controller))
        login_button.place(relx=0.4, rely=0.47, relheight=0.08, relwidth=0.2)

        register_label = tk.Label(self, text="Don't have an account?", bg='black', fg='#bababa', font=fonts.sMainFont)
        register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(self, text='Register', font=fonts.boldMainFont, command=register.reg_window)
        register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)
    
    def authenticate(self, username, password, root):
        login.verify_login(username, password, root)

class ATMFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        self.place(relheight=1, relwidth=1)
        window_label = tk.Label(self, text='ATM WINDOW', bg='black', fg='white', font=fonts.biggerFontBold)
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('ATM System')
        self.iconbitmap('wwticon.ico')
        self['background'] = 'white'

        width = 720
        height = 720
        pos_right = int(self.winfo_screenwidth()/2 - width/2)
        pos_down = int(self.winfo_screenheight()/2 - height/2)
        self.geometry(f"{width}x{height}+{pos_right}+{pos_down}")

        container = tk.Frame(self)
        container.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        self.frames = {}
        for F in (LoginFrame, ATMFrame):
            print(F)
            frame = F(container, self)
            self.frames[F] = frame
        
        self.show_frame(LoginFrame)
    
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()