from random import randint


def check_range():
    while True:
        range_from = int(input("Range from: "))
        range_to = int(input("Range to: "))
        if range_to - range_from + 1 >= 5:
            if range_to - range_from + 1 <= 30:
                return range_from, range_to
        print("Error. Please try again!")


def create_random_numbers(range_from_to):
    range_from, range_to = range_from_to
    random_numbers = set()
    while len(random_numbers) < 3:
        random_numbers.add(randint(range_from, range_to))
    return random_numbers


def input_user_numbers():
    user_numbers = set()
    while len(user_numbers) < 3:
        user_numbers.add(input("Enter number: "))
        if 'exit' in user_numbers:
            quit()
    return user_numbers


def checking_guessed_numbers(random_numbers, user_numbers):
    guessd = 0
    for element in user_numbers:
        if int(element) in random_numbers:
            guessd += 1
    return guessd


def play_game():
    my_range = check_range()
    random_numbers = create_random_numbers(my_range)
    while True:
        user_numbers = input_user_numbers()
        guessd_numbers = checking_guessed_numbers(random_numbers, user_numbers)
        print(f"Guessd {guessd_numbers} numbers")
        if guessd_numbers == 3:
            print("You win")
            quit()
        print("Try again!")


play_game()
