# A program that repeatedly asks the user for input until valid data is entered.
#  Handle exceptions for invalid types, out-of-range values, and incorrect formats

# Algorithm
# create a function for the operation
# create a while loop in the func 
# use the try and catch blocks to catch and handle invalid inputs
# use if statements to check if the value reaches the required creteria
# provide the error message when the input id invalid

# ask user to input any number from 1 to 100
def get_user_input():
    while True:
        try:
            user_input = int(input("Enter number from 1 and 100: "))

            if 1 <= user_input <= 100: 
                print("Valid input recieved.", user_input)
                return user_input
            else:
                print("Invalid input recieved.", user_input)
        except ValueError:
            print("Error. Please enter a valid integer input.")


# Algorithm
# import re module to search string for inclusions of certain chars
# define a func
# define chars and email structure (regex values [regular expressions])
# create a while loop
# ask user for email input 
# use condition to check if the inputed email contains certain chars mentioned
# display the error if available
#  call function

import re
def get_user_email():
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
    while True:
       email_input = input("Enter a valid email address: ")

       if re.search(email_pattern, email_input):
           print("Valid email address recieved.", email_input)
       else:
            print("Invalid email address. Please try again", email_input)

get_user_email()