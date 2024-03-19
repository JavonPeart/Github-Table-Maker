import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_labelFrame(self, textvar):
        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=NO, pady=[10, 0])

        banner = ttk.LabelFrame(
            master=container,
            bootstyle=INFO, 
            text="Output Panel",
            borderwidth=10,
            height=100,
        )
        banner.pack(fill=BOTH, padx=5, pady=[10, 15])
    
        bLabel = ttk.Label(banner, textvariable=textvar, padding=5, font=["Helvetica", 12, "bold"])
        bLabel.pack(pady=[0, 10], anchor=CENTER)