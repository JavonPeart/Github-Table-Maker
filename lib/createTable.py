import os
from ttkbootstrap.constants import *

def create_table(self):
    i, n = self.icon.get(), self.name.get()

    try:
        if i == "" or n == "":
            self.output.set("Please enter an icon and name")
        else:
            def header(icon): return f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'

            def footer(name): return f'| <p align="center"> `{name}` </p>'

            def initialize_file(filename, num_lines):
                if not os.path.exists(filename):
                    with open(filename, 'w') as file:
                        file.writelines('\n'* num_lines)
                    self.output.set(f'Table created in file: {filename}')
                
                if os.path.getsize(filename) == 0:
                    with open(filename, 'w') as file:
                        file.writelines('\n'* num_lines)
                    self.output.set(f'Table Added in file: {filename}')

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
                filename = self.file.get()
                initialize_file(filename, 4)

                head = ' ' + header(i) + ' '
                foot = ' ' + footer(n) + ' '

                add_new_data(filename, 1, head)
                add_new_data(filename, 2, "|---")
                add_new_data(filename, 3, foot)
                self.output.set(f'Table Updated in {self.file.get()}')
  
            update_data()
            print(f'Table Updated: {self.file.get()}')
    
    except Exception as e:
        print(e)
        self.output.set(f'Error: {e}')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # i = self.icon.get()
    # n = self.name.get()

    # def header(icon):
    #     return f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'

    # def footer(name):
    #     return f'| <p align="center"> `{name}` </p>'

    # def initialize_file(filename):
    #     if not os.path.exists(filename):
    #         with open(filename, 'w') as file:
    #             for _ in range(4):
    #                 file.write('\n')

    # def clear_leading_spaces(filename):
    #     with open(filename, 'r') as file:
    #         lines = file.readlines()

    #     # Strip leading whitespace from each line
    #     lines = [line.lstrip() for line in lines]

    #     with open(filename, 'w') as file:
    #         file.writelines(lines)


    # def add_new_data(filename, line_number, new_content):
    #     # Determine the number of lines in the file
    #     with open(filename, 'r') as file:
    #         lines = file.readlines()

    #     # Modify the specific line
    #     if 0 < line_number <= len(lines):
    #         lines[line_number - 1] = lines[line_number - 1].strip() + new_content + '\n'  # -1 because index starts from 0

    #         # Write the modified content back to the file
    #         with open(filename, 'w') as file:
    #             file.writelines(lines)

    # def update_data():
    #     filename = "output.md"
    #     initialize_file(filename)

    #     head = ' ' + header(i) + ' '
    #     foot = ' ' + footer(n) + ' '

    #     add_new_data(filename, 1, head)
    #     add_new_data(filename, 2, "|---")
    #     add_new_data(filename, 3, foot)
    #     clear_leading_spaces(filename)

    # if n == "" or i == "":
    #     self.output.set("Error")
    # else:    
    #     update_data()