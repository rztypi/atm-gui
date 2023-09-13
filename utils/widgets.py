import tkinter as tk

from pages import page_list
from windows import window_list


__name_to_page = {cls.__name__: cls for cls in page_list}
__name_to_window = {cls.__name__: cls for cls in window_list}


def get_page(page_name):
    """Get the page class from its __name__."""
    return __name_to_page[page_name]


def get_window(window_name):
    """Get the window class from its __name__."""
    return __name_to_window[window_name]


def set_window_geometry(window, x, y):
    """Set the size of the given window and center it to the screen."""
    x_offset = int(window.winfo_screenwidth() / 2 - x / 2)
    y_offset = int(window.winfo_screenheight() / 2 - y / 2)

    geometry_string = f"{x}x{y}+{x_offset}+{y_offset}"
    window.geometry(geometry_string)


def clear_entry_field(entry_field):
    """Clear the contents of the given tk.Entry field."""
    entry_field.delete(0, tk.END)
