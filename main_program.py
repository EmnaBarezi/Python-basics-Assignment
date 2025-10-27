
from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    # Ask for name until valid
    while True:
        name = input("Enter your name: ").strip()
        if validate_input(name):
            break
        print("Invalid name! Please try again.")

    # Ask for age until it's numeric
    while True:
        age_str = input("Enter your age: ").strip()
        if age_str.isdigit():
            break
        print("Invalid age! Please enter a number.")

    age = int(age_str)
    return name, age

if __name__ == "__main__":
    show_intro()
    name, age = get_user_info()

    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)  # Accepts int directly

    message = create_message(name, age, name_binary, age_binary)
    print(message)

    save_message(message)
    read_message()
    show_exit_message()

