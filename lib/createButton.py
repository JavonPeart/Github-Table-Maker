import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from lib.createTable import create_table

def create_buttonbox(self):
    """Create the application buttonbox"""
    container = ttk.Frame(self)
    container.pack(fill=X, expand=YES, pady=(5, 10))

    sub_btn = ttk.Button(
        master=container,
        text="Submit",
        command=lambda: create_table(self),
        bootstyle=SUCCESS,
        width=8,
    )
    sub_btn.pack(side=RIGHT, padx=5)

    cnl_btn = ttk.Button(
        master=container,
        text="Clear",
        command= lambda: clear_forms(self),
        bootstyle=INFO,
        width=8,
    )
    cnl_btn.pack(side=RIGHT, padx=5)

    exit_btn = ttk.Button(
        master=container,
        text="Exit",
        command= lambda: quit(),
        bootstyle=DANGER,
        width=8,
    )
    exit_btn.pack(side=RIGHT, padx=5)

def clear_forms(self):
    """Clear the entry forms"""
    if self.icon:
        self.icon.set("")
    if self.name:
        self.name.set("")
    self.output.set("Forms Cleared")