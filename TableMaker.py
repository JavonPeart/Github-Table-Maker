def create_text_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)

def header(icon):
    return f'| <img align="center" height="48px" width="48px" src="https://skillicons.dev/icons?i={icon}"/>'

def footer(name):
    return f'| <p align="center">{name}</p>'

def build_text():
    head = ''
    middle = ''
    foot = ''
    x=3
    
    for i in range(x):
        icon, name = input("Enter an Icon and its Name: ").split(' ')
        head += header(icon) + ' '
        middle += '|---'
        foot += footer(name) + ' '

    return head + '\n' + middle + '\n' + foot


create_text_file("text.txt", build_text())