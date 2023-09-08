from tkinter import Tk, Frame, Label, Entry, Button, W
import register
import login


# Initialize window
root = Tk()
root.title("ATM SYSTEM")
root.iconbitmap('wwticon.ico')
root['background'] = 'white'

# Set window size and center
root_x = 720
root_y = 720
root_pos_right = int(root.winfo_screenwidth()/2 - root_x/2)
root_pos_down = int(root.winfo_screenheight()/2 - root_y/2)
root.geometry(f'{root_x}x{root_y}+{root_pos_right}+{root_pos_down}')

# Initialize font variables
boldMainFont = ('Source Code Pro', 14, 'bold')
mainFont = ('Source Code Pro', 14)
sMainFont = ('Source Code Pro', 9)

# Initialize widgets
frame1 = Frame(root, bg="black")
frame1.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
window_label = Label(frame1, text="ATM System Login", bg='black', fg='white', font=('Source Code Pro', 24, 'bold'))
user_label = Label(frame1, text="User Name: ", bg='black', fg='white', anchor=W, font=boldMainFont)
pass_label = Label(frame1, text="Password: ", bg='black', fg='white', anchor=W, font=boldMainFont)
register_label = Label(frame1, text="Don't have an account?", bg='black', fg='#bababa', font=sMainFont)
user_main_entry = Entry(frame1, font=mainFont)
pass_main_entry = Entry(frame1, font=mainFont)
login_button = Button(frame1, text="Login", font=boldMainFont)
register_button = Button(frame1, text="Register", font=boldMainFont, command=register.reg_window)
# Configure login button
login_button.config(command=lambda: login.verify_login(user_main_entry, pass_main_entry, root))

# Display widgets

window_label.place(relx=0.1, rely=0.02, relheight=0.1, relwidth=0.8)

user_label.place(relx=0.02, rely=0.18, relheight=0.05, relwidth=0.3)
user_main_entry.place(relx=0.1, rely=0.24, relheight=0.05, relwidth=0.8)

pass_label.place(relx=0.02, rely=0.31, relheight=0.05, relwidth=0.3)
pass_main_entry.place(relx=0.1, rely=0.37, relheight=0.05, relwidth=0.8)

login_button.place(relx=0.4, rely=0.47, relheight=0.08, relwidth=0.2)

register_label.place(relx=0.1, rely=0.82, relheight=0.02, relwidth=0.8)
register_button.place(relx=0.4, rely=0.85, relheight=0.08, relwidth=0.2)

root.mainloop()