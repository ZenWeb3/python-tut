# Algorithm
# A simple multiplication generator
# ask the user for a number to generate its multiplication
# display the multiplication

def multiplication_table() :
    user_input = int(input("Enter a number to generate a multiplication table"))
    for i in range(1, 11) :
        print(f"{user_input} X {1} = {user_input * i}")
    

multiplication_table()