import tkinter as tk
from tkinter import messagebox

def update_data():
    icon = icon_entry.get()
    name = name_entry.get()

    if not icon or not name:
        messagebox.showerror("Error", "Both icon and name fields are required.")
        return

    head = f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'
    foot = f'| <p align="center"> `{name}` </p>'

    # Write the header, separator, and footer to the file
    with open("output.md", 'w') as file:
        file.write(f"{head}\n")
        file.write("|---\n")
        file.write(f"{foot}\n")

    messagebox.showinfo("Success", "Data updated successfully.")

# Create the main window
window = tk.Tk()
window.title("GH Icon and Name Editor")

# Create icon and name input fields
icon_label = tk.Label(window, text="Icon:")
icon_label.grid(row=0, column=0, padx=10, pady=10)
icon_entry = tk.Entry(window)
icon_entry.grid(row=0, column=1, padx=10, pady=10)


name_label = tk.Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1, padx=10, pady=10)


# Create update button
update_button = tk.Button(window, text="Update Data", command=update_data)
update_button.grid(row=2, column=0, columnspan=4, padx=20, pady=20)

# Run the main event loop
window.mainloop()
