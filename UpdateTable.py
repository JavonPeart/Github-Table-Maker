import os
from time import sleep


def header(icon):
    return f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'

def footer(name):
    return f'| <p align="center">{name}</p>'

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
    else:
        print(f"Line number {line_number} is out of range.")

def update_data():
    filename = input("Enter the name of the file: ")
    initialize_file(filename, 3)

    while True:
        icon, name = input("Enter an [Icon] and its [Name]: ").split(';')

        head = ' ' + header(icon) + ' '
        foot = ' ' + footer(name) + ' '

        add_new_data(filename, 1, head)
        add_new_data(filename, 2, "|---")
        add_new_data(filename, 3, foot)
        
        clear_leading_spaces(filename)
        print("------------------------------")

def main():
    print("Welcome to the Icon and Name Editor!")
    print("Press Ctrl+C to exit at any time.\n\n")

    try:
        update_data()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
