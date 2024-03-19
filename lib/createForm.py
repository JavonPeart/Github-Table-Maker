import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from lib.createTable import create_table

def create_form_entry(self, label, variable, fc=False):
    """Create a single form entry"""
    container = ttk.Frame(self)
    container.pack(fill=BOTH, expand=NO, pady=[10, 0])

    lbl = ttk.Label(master=container, text=label.title(), width=5, font=["", 14])
    lbl.pack(side=LEFT, padx=5)

    ent = ttk.Entry(master=container, textvariable=variable)
    ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
    ent.bind("<Return>", lambda e: create_table(self))
    
    if fc: ent.focus_set()