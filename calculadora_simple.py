### A program that simulates a basic calculator with the operations: addition, subtraction, multiplication, and division.

def calculator():
    print("Select the type of operation you want to perform: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the option (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by 0 is not allowed")
    else:
        print("Invalid option")


if __name__ == '__main__':

    calculator()

