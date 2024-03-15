import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


"""
HOW TO CONVERT TO AN EXE

Command: pyinstaller 'SampleDataEntry'.py --collect-all ttkbootstrap
"""

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=[170, 50])
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.icon = ttk.StringVar(value="")
        self.name = ttk.StringVar(value="")
        self.output = ttk.StringVar(name="PlaceHolder")

        # form header
        hdr_txt = "Enter Icon and Name" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=100, font=["Helvetica", 20, "bold"], anchor=CENTER)
        hdr.pack(fill=X, pady=[50, 0])

        hdr_txt2 = "(See the Skill-Icons Github Repo for a list of icons and their names)"
        hdr2 = ttk.Label(master=self, text=hdr_txt2, width=100, font=["Helvetica", 11, "italic"], anchor=CENTER)
        hdr2.pack(fill=X, pady=[0, 20])

        # form entries
        self.create_form_entry("Icon", self.icon, True)
        self.create_form_entry("Name", self.name)
        self.create_buttonbox()
        
        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=NO, pady=[10, 5])

        banner = ttk.LabelFrame(
            master=container,
            bootstyle=INFO, 
            text="Output",
            borderwidth=10,
            height=100,
        )
        banner.pack(fill=X, padx=5, pady=[5, 5])
    
        bLabel = ttk.Label(banner, textvariable=self.output, padding=5, font=["Helvetica", 12, "italic"])
        bLabel.pack(anchor=CENTER)



    def create_form_entry(self, label, variable, fc=False):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=NO, pady=[10, 0])

        lbl = ttk.Label(master=container, text=label.title(), width=5, font=["", 14])
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        
        if fc: ent.focus_set()


 
    
    
    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(5, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=lambda:[f() for f in [
                self.on_submit, 
                self.create_table
                ]
            ],
            bootstyle=SUCCESS,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        self.output.set("Success")

    def on_cancel(self):
        """Cancel and close the application."""
        # TODO: clear the forms if they have content
        # TODO: quit if all of them are empty
        self.quit()



    def create_table(self):
        i = self.icon.get()
        n = self.name.get()

        if n == "" or i == "":
            self.output.set("Error")
        else:
            def header(icon):
                return f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'

            def footer(name):
                return f'| <p align="center"> `{name}` </p>'

            def initialize_file(filename, num_lines):
                if not os.path.exists(filename):
                    with open(filename, 'w') as file:
                        for _ in range(num_lines+1):
                            file.write('\n')

            def clear_leading_spaces(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()

                # Strip leading whitespace from each line
                lines = [line.lstrip() for line in lines]

                with open(filename, 'w') as file:
                    file.writelines(lines)


            def add_new_data(filename, line_number, new_content):
                # Determine the number of lines in the file
                with open(filename, 'r') as file:
                    lines = file.readlines()

                # Modify the specific line
                if 0 < line_number <= len(lines):
                    lines[line_number - 1] = lines[line_number - 1].strip() + new_content + '\n'  # -1 because index starts from 0

                    # Write the modified content back to the file
                    with open(filename, 'w') as file:
                        file.writelines(lines)

            def update_data():
                filename = "output.md"
                initialize_file(filename, 3)

                head = ' ' + header(i) + ' '
                foot = ' ' + footer(n) + ' '

                add_new_data(filename, 1, head)
                add_new_data(filename, 2, "|---")
                add_new_data(filename, 3, foot)
                
                clear_leading_spaces(filename)
        
            update_data()

if __name__ == "__main__":

    app = ttk.Window("Data Entry", "superhero", resizable=(FALSE, FALSE), size=[800, 500])
    DataEntryForm(app)
    app.mainloop()
