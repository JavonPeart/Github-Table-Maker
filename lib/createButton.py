import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from lib.onClick import * 
from lib.createTable import create_table

def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(5, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=lambda:[f(self) for f in [
                on_submit, 
                create_table
                ]
            ],
            bootstyle=SUCCESS,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=on_cancel,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)