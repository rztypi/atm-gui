import tkinter as tk


def set_window_geometry(window, x, y):
    x_offset = int(window.winfo_screenwidth() / 2 - x / 2)
    y_offset = int(window.winfo_screenheight() / 2 - y / 2)

    geometry_string = f"{x}x{y}+{x_offset}+{y_offset}"
    window.geometry(geometry_string)


def clear_entry_field(entry_field):
    entry_field.delete(0, tk.END)
