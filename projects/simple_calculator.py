# Functions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Function to display the menu and get user input
def get_user_input():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    operation = input("Enter the operation (1/2/3/4): ")
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid input.")
        return None, None, None
    return operation, num1, num2

# Main function to handle calculator logic.

def main() :
        while True:
            operation, num1, num2 = get_user_input() 
            if operation is None:
                continue
            
            try:
                if operation == "1":
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif operation == "2":
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif operation == "3":
                    result = multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif operation == "4":
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                else:
                    print("Invalid operation! Please choose a valid option.")
            except ValueError as e:
                print(f"Error: {e}")
            another = input("Do you want to continue with another operation? (yes/no)").lower().strip()
            if another!= "yes":
                print("Goodbye")
                break   

if __name__ == "__main__":
    main()
