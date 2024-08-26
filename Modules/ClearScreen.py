import os

def clear_screen():
    if os.name == 'posix':  # Linux or macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print("Unsupported OS")
