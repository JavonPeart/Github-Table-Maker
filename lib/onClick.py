from ttkbootstrap.constants import *

def on_submit(self):
    i, n = self.icon.get(), self.name.get()

    try:
        if i == "" or n == "":
            self.output.set("Please enter an icon and name")
            print("No icon or name entered")
        else:
            # self.output.set(f'Successfully Added {n}')
            print("Successfully added")
    except TypeError as e:
        self.output.set(f'Error: {e}')
        print(f'Error: {e}')
            

def on_cancel():
    """Cancel and close the application."""
    # TODO: clear the forms if they have content
    # TODO: quit if all of them are empty
    quit()
