from calculator import Calculator


def decor(func):
    def wrap():
        print()
        print("=" * 20)
        func()
        print("=" * 20)

    return wrap


@decor
def menu():
    print("Menu\t:")
    print(
        "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n7. Sin\n8. Cos\n9. Tan\n10. Exit"
    )


print("=" * 35)
print("Welcome to Calculator Application")
print("Created by MRSyafapri")
menu()
choice = int(input("Enter your choice: "))
calculator = Calculator()
while choice != 10:
    if choice >= 1 and choice <= 6:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
    elif choice >= 7 and choice <= 9:
        number = int(input("Enter number: "))
    if choice == 1:
        result = calculator.addition(first_number, second_number)
        print("{} + {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 2:
        result = calculator.substraction(first_number, second_number)
        print("{} - {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 3:
        result = calculator.multiplication(first_number, second_number)
        print("{} * {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 4:
        result = calculator.division(first_number, second_number)
        print("{} / {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 5:
        result = calculator.modulus(first_number, second_number)
        print("{} % {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 6:
        result = calculator.exponentiation(first_number, second_number)
        print("{} ** {} = {}".format(first_number, second_number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 7:
        result = calculator.sin(number)
        print("sin {} = {}".format(number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 8:
        result = calculator.cos(number)
        print("cos {} = {}".format(number, result))
        menu()
        choice = int(input("Enter your choice: "))
    elif choice == 9:
        result = calculator.tan(number)
        print("tan {} = {}".format(number, result))
        menu()
        choice = int(input("Enter your choice: "))
    else:
        print("Please enter the appropriate options")
        menu()
        choice = int(input("Enter your choice: "))
else:
    print("Thank you. Have a nice day")
print("=" * 35)
