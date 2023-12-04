from getters import get_email, get_password


def check_data(email, password, users):
    for element in users:
        if email == element["email"] and password == element["password"]:
            return f"Welcome {element['email']}"
    print("Sorry, invalid credentials!")


def validator(users):
    while True:
        result = check_data(get_email(), get_password(), users)
        if result:
            print("Welcome!")
            break
        else:
            print("Try again!")
