import json
from validators import validator
from getters import get_password, get_email


def registered_users():
    with open("users.json", "r") as read_file:
        users = json.load(read_file)
        return users


def users_choice():
    while True:
        user_choice = input("Please choose any option: \n"
                            "Login: enter 1\n"
                            "Registration: enter 2\n")
        if user_choice == "1":
            validator(registered_users())
        elif user_choice == "2":
            user_registration(registered_users())
        else:
            print("Wrong input, please enter 1 or 2.")


def check_name(users, add_new_email):
    for element in users:
        if element["email"] == add_new_email:
            return True
    return False


def user_registration(users):
    while True:
        add_new_email = get_email()
        if check_name(users, add_new_email):
            print("User with this login already exists")
        else:
            break
    while True:
        password = get_password()
        print("Repeat password")
        confirm_password = get_password()
        if password != confirm_password:
            print("Passwords dont match")
        else:
            break
    new_user = {"email": add_new_email, "password": password}
    with open("users.json", "r") as file:
        users_file = json.load(file)
        users_file.append(new_user)
    with open("users.json", "w") as json_file:
        json.dump(users_file, json_file)


users_choice()
