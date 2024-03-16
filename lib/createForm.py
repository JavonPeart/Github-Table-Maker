import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_form_entry(self, label, variable, fc=False):
    """Create a single form entry"""
    container = ttk.Frame(self)
    container.pack(fill=BOTH, expand=NO, pady=[10, 0])

    lbl = ttk.Label(master=container, text=label.title(), width=5, font=["", 14])
    lbl.pack(side=LEFT, padx=5)

    ent = ttk.Entry(master=container, textvariable=variable)
    ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
    
    if fc: ent.focus_set()