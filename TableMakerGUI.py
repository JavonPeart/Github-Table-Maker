import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from lib.createForm import create_form_entry
from lib.createButton import create_buttonbox
from lib.windowManager import *
from lib.createFrame import create_labelFrame


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=[170, 50])
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.icon = ttk.StringVar(value="")
        self.name = ttk.StringVar(value="")
        self.output = ttk.StringVar(value="")
        self.file = ttk.StringVar(value="")
        self.file.set("output.md")
        self.output.set("Welcome!")

        # form header
        hdr_txt = "Enter Icon and Name" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=100, font=["Helvetica", 20, "bold"], anchor=CENTER)
        hdr.pack(fill=X, pady=[50, 0])

        hdr_txt2 = "(See the Skill-Icons Github Repo for a list of icons and their names)"
        hdr2 = ttk.Label(master=self, text=hdr_txt2, width=100, font=["Helvetica", 11, "italic"], anchor=CENTER)
        hdr2.pack(fill=X, pady=[0, 20])

        # form entries
        create_form_entry(self, "File", self.file)
        create_form_entry(self, "Icon", self.icon, True)
        create_form_entry(self, "Name", self.name)
        create_buttonbox(self)
        create_labelFrame(self, self.output)


if __name__ == "__main__":

    app = ttk.Window("Skill-Icons Table Maker", "superhero", resizable=(FALSE, FALSE))
    center_window(app, 800, 510)
    DataEntryForm(app)
    app.bind("<Escape>", lambda e: quit())
    app.mainloop()