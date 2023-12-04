def calc():
    first_number = int(input("Input first number: "))
    operator = input("Input operator (+, -, *, /, ): ")
    second_number = int(input("Input second number: "))

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "**":
        result = first_number ** second_number
    elif operator == "/":
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            print("Can't divide by zero!")
            quit()

    print("Result of operation: ", result)


calc()
