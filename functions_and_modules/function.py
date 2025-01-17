# The general syntax for function is 
# def function_name (optional arguments):
    #   function body
    #   code block to perform specific tasks
    #   return statement (optional)

# def greet_user():
#     input_name = input("What is your name ? ")
#     name = input_name
#     print("good morning " + name)


# greet_user()

# Fuction initialization
def addition(val1, val2, val3):
    if type(val1) == int and type(val2) == int and type(val3) == int:
        print(val1 + val2 + val3)
    else:
        print("Invalid input, please enter integers.")

# Positional argument
addition(5, 5, 4)
addition("Sam ", "king",5)

# keyword arguments (explicit arguments)
addition(val3=10, val1=20, val2=30)


# Default arguments
# values given to the argument incase values for the arguments are not specified
# def addition(val1=0, val2=0, val3=2):