import tkinter as tk
from random import randint

import fonts
import login
import register


class WidgetMethods:
    @staticmethod
    def set_window_geometry(window, width, height, centered=True):
        geo_param = f'{height}x{width}'
        if centered:
            pos_right = int(window.winfo_screenwidth()/2 - width/2)
            pos_down = int(window.winfo_screenheight()/2 - height/2)
            geo_param += f'+{pos_right}+{pos_down}'
        window.geometry(geo_param)
    
    @staticmethod
    def clear_entry_field(entry_field):
        entry_field.delete(0, tk.END)


class TwoFA:
    def __open_atm_system(self, app):
        self.destroy()
        app.show_frame(HomeFrame)
        
    def generate_pin(self):
        def random_digit():
            return randint(0, 9)

        pin = f'{random_digit()}{random_digit()}{random_digit()}{random_digit()}'
        return pin

    def authenticate_twofa(self, code_entry, pin, app):
        code = code_entry.get()
        if code == pin:
            self.__open_atm_system(app)
        else:
            tk.messagebox.showerror('Verification Error', 'Code does not match.')
            WidgetMethods.clear_entry_field(code_entry)
            self.deiconify()


class TwoFAToplevel(tk.Toplevel, TwoFA):
    def __init__(self, app):
        tk.Toplevel.__init__(self)
        self.title('Two-Factor Authentication')
        self.iconbitmap('wwticon.ico')
        self['background'] = 'white'
        WidgetMethods.set_window_geometry(self, width=400, height=400)

        pin = self.generate_pin()
        print(pin)

        frame = tk.Frame(self, bg='black')
        frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        window_label = tk.Label(frame, text="Verify Code", bg='black', fg='white', font=fonts.bigFontBold)
        window_label.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

        window_desc_text = 'Enter the 4-digit code\nwe sent to your phone number.'
        window_desc = tk.Label(frame, text=window_desc_text, bg='black', fg='#bababa', font=fonts.sMainFont)
        window_desc.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)

        code_entry = tk.Entry(frame, font=('Source Code Pro', 79, 'bold'))
        code_entry.place(relx=0.1, rely=0.4, relheight=0.25, relwidth=0.8)

        verify_button = tk.Button(frame, text="Verify", font=fonts.boldMainFont, command=lambda: self.authenticate_twofa(code_entry, pin, app))
        verify_button.place(relx=0.3, rely=0.75, relheight=0.1, relwidth=0.4)


class Login:
    def __user_check(self, username):
        if not username:
            tk.messagebox.showerror('Login Error', 'You cannot leave your username blank.')
            return False
        return True
    
    def __pass_check(self, password):
        if not password:
            tk.messagebox.showerror('Login Error', 'You cannot leave your password blank.')
            return False
        return True

    def __open_twofa_window(self, app):
        twofa_window = TwoFAToplevel(app)


    def authenticate_login(self, user_entry, pass_entry, app):
        username = user_entry.get()
        password = pass_entry.get()

        WidgetMethods.clear_entry_field(user_entry)
        WidgetMethods.clear_entry_field(pass_entry)

        if self.__user_check(username) and self.__pass_check(password):
            self.__open_twofa_window(app)


class LoginFrame(tk.Frame, Login):
    def __init__(self, parent, app):
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
        login_button.config(command=lambda: self.authenticate_login(user_entry, pass_entry, app))
        login_button.place(relx=0.4, rely=0.47, relheight=0.08, relwidth=0.2)

        register_label = tk.Label(self, text="Don't have an account?", bg='black', fg='#bababa', font=fonts.sMainFont)
        register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)

        register_button = tk.Button(self, text='Register', font=fonts.boldMainFont, command=register.reg_window)
        register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)


class HomeFrame(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg='black')
        self.place(relheight=1, relwidth=1)
        window_label = tk.Label(self, text='ATM Window', bg='black', fg='white', font=fonts.biggerFontBold)
        window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('ATM System')
        self.iconbitmap('wwticon.ico')
        self['background'] = 'white'

        WidgetMethods.set_window_geometry(self, width=720, height=720)

        container = tk.Frame(self)
        container.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        self.frames = {}
        for F in (LoginFrame, HomeFrame):
            frame = F(container, self)
            self.frames[F] = frame
        
        self.show_frame(LoginFrame)
    
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()