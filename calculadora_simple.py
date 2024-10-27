# Function to calculate compound interest with monthly deposits
def calculate_compound_interest(initial_capital, monthly_deposit, annual_interest_rate, years):
    # Convert the annual interest rate to a monthly rate
    monthly_rate = annual_interest_rate / 100 / 12
    months = years * 12

    # Initialize the total amount with the initial capital
    total_amount = initial_capital

    # Calculate compound interest with monthly deposits
    for month in range(1, months + 1):
        total_amount += monthly_deposit  # Add the monthly deposit
        total_amount *= (1 + monthly_rate)  # Apply the monthly interest

    return total_amount

def calculator():
    print("Select the type of operation you want to perform: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Compound Interest")

    operation = input("Enter the option (1/2/3/4/5): ")

    if operation in ['1', '2', '3', '4']:
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
    elif operation == '5':
        # User inputs
        initial_capital = float(input("Enter the initial capital: "))
        monthly_deposit = float(input("Enter the monthly deposit: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the time in years: "))

        # Calculate the final amount
        final_amount = calculate_compound_interest(initial_capital, monthly_deposit, annual_interest_rate, years)
        print(f"The final amount after {years} years is: ${final_amount:.2f}")

    else:
        print("Invalid command")

if __name__ == '__main__':
    calculator()
