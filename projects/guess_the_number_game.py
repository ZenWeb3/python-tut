# This program randomly selects a random number within a range and the user has to guess the number. 
# the program provides hints if the guess is high or low.


# Algorithm
# Randomly select a number
# Ask Player to guess the number
# If correct, say correct,
# If not correct, say not correct and keep repeating 
# till user gets the correct number 

 
random_number = 5
user_guess = 0

while (user_guess != random_number):
    user_guess = int(input("Guess the number: "))
    if user_guess == random_number:
        print("Congratulations you are correct!")

    else:
        if user_guess < random_number:
            print("Go a lil higher!")

        else:
            print("Go a lil lower!")